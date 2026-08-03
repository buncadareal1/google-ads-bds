#!/usr/bin/env python3
"""Keap -> Google Data Manager API: upload offline conversions (ECL).

Chay hang ngay 07:00 ICT. Xem tracking/ecl-keap-pipeline.md truoc khi sua.

    pip install requests google-auth
    python3 tracking/upload_ecl.py --selftest     # kiem tra logic, khong goi mang
    python3 tracking/upload_ecl.py --dry-run      # goi that + validateOnly=true, khong ghi
    python3 tracking/upload_ecl.py                # chay that

Google Ads API da chan offline conversion upload tu 15/6/2026 -> chi con Data Manager API.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import logging
import os
import re
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path
from urllib.parse import parse_qs, urlparse

# ── PONYTAIL: DIEN VAO DAY ────────────────────────────────────────────────────
# Moi placeholder duoi day deu co huong dan lay o dau trong ecl-keap-pipeline.md.

KEAP_BASE = "https://api.infusionsoft.com/crm/rest/v1"
KEAP_KEY = os.environ.get("KEAP_SERVICE_ACCOUNT_KEY", "")  # PONYTAIL: Keap Admin > Settings > Service Account Key

GADS_CUSTOMER_ID = os.environ.get("GADS_CUSTOMER_ID", "1234567890")  # PONYTAIL: customer ID, khong dau gach
GADS_LOGIN_CUSTOMER_ID = os.environ.get("GADS_LOGIN_CUSTOMER_ID", "") or GADS_CUSTOMER_ID  # PONYTAIL: MCC ID neu truy cap qua MCC

# PONYTAIL: 3 tag ID trong Keap (GET /crm/rest/v1/tags?limit=200)
#           + 3 conversion action ID trong Google Ads (tham so ctId tren URL khi mo action).
# Gia tri 10/50/500 la DIEM tuong doi, khong phai VND — xem gtm-container-spec.md §4.1.
STAGES = {
    "contactable": {"keap_tag_id": 111, "conversion_action_id": "PONYTAIL_CTID_CONTACTABLE", "value": 10},
    "qualified":   {"keap_tag_id": 222, "conversion_action_id": "PONYTAIL_CTID_QUALIFIED",   "value": 50},
    "dat_coc":     {"keap_tag_id": 333, "conversion_action_id": "PONYTAIL_CTID_DAT_COC",     "value": 500},
}

# PONYTAIL: ID cua custom field trong Keap (GET /crm/rest/v1/contacts/model -> custom_fields[].id).
# Duong A (SmartLand proxy) chi co LANDING_URL -> script tu parse gclid ra tu query string.
# Duong B co field rieng -> uu tien doc thang. Khong co field nao thi de None, script bo qua.
KEAP_FIELD_IDS = {
    "gclid": None,        # PONYTAIL: vd 7
    "gbraid": None,       # PONYTAIL: vd 8
    "wbraid": None,       # PONYTAIL: vd 9
    "landing_url": None,  # PONYTAIL: vd 10 — field chua LP URL kem ?gclid=...
}

# PONYTAIL: service account. Impersonation an toan hon key file (khuyen nghi cua Google).
SA_IMPERSONATE = os.environ.get("ECL_SA_EMAIL", "")            # ecl-uploader@<project>.iam.gserviceaccount.com
SA_KEY_FILE = os.environ.get("GOOGLE_APPLICATION_CREDENTIALS", "")  # fallback neu khong impersonate

DM_ENDPOINT = "https://datamanager.googleapis.com/v1/events:ingest"
DM_SCOPE = "https://www.googleapis.com/auth/datamanager"
MAX_EVENTS_PER_REQUEST = 2000  # gioi han cua Data Manager API
LOOKBACK_DAYS = 7              # bu cho ngay cron loi; transactionId lo phan khu trung
STATE_FILE = Path(__file__).with_name(".ecl_state.json")
# ──────────────────────────────────────────────────────────────────────────────

log = logging.getLogger("ecl")


# ── Chuan hoa + hash ──────────────────────────────────────────────────────────
# Sai mot buoc o day thi match rate = 0 va khong co loi nao bao. Doc ky.

def sha256_hex(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


def normalize_email(raw: str | None, gmail_rules: bool = True) -> str | None:
    """lowercase + bo khoang trang; gmail_rules=True (mac dinh, cho ECL/user-provided data):
    bo dau '.' va '+suffix' o local part gmail — VN gmail ap dao, thieu buoc nay mat match rate.
    gmail_rules=False cho CUSTOMER MATCH: doc chuan hoa CM chi yeu cau lowercase+strip (vong 3
    curriculum §F6b) — ap gmail rules vao CM co the TUT match rate im lang. Re-verify voi doc
    hien hanh truoc lan upload audience dau tien.
    Khong co '@' thi coi nhu khong co email."""
    if not raw:
        return None
    e = re.sub(r"\s+", "", str(raw)).lower()
    if "@" not in e:
        return None
    local, _, domain = e.rpartition("@")
    if gmail_rules and domain in ("gmail.com", "googlemail.com"):
        local = local.split("+", 1)[0].replace(".", "")
    return f"{local}@{domain}"


def to_e164_vn(raw: str | None) -> str | None:
    """SDT VN -> E.164 (+84...). Chi chap nhan di dong 10 so va so ban 10-11 so."""
    if not raw:
        return None
    d = re.sub(r"\D", "", str(raw))
    if d.startswith("840"):
        d = "0" + d[3:]
    elif d.startswith("84") and not d.startswith("840"):
        d = "0" + d[2:]
    if not d.startswith("0") or not (10 <= len(d) <= 11):
        return None
    if len(set(d)) <= 2:  # 0000000000 / 0999999999 — rac
        return None
    return "+84" + d[1:]


def hash_identifiers(email: str | None, phone: str | None) -> list[dict]:
    """-> userData.userIdentifiers[] cho Data Manager API (encoding HEX)."""
    out = []
    e = normalize_email(email)
    if e:
        out.append({"emailAddress": sha256_hex(e)})
    p = to_e164_vn(phone)
    if p:
        out.append({"phoneNumber": sha256_hex(p)})
    return out


def extract_click_ids(contact: dict) -> dict:
    """gclid/gbraid/wbraid tu custom field rieng, fallback: parse tu landing URL."""
    fields = {f.get("id"): f.get("content") for f in contact.get("custom_fields") or []}
    ids = {}
    for key in ("gclid", "gbraid", "wbraid"):
        fid = KEAP_FIELD_IDS.get(key)
        val = fields.get(fid) if fid is not None else None
        if val:
            ids[key] = str(val).strip()
    if not ids:
        url = fields.get(KEAP_FIELD_IDS.get("landing_url")) or contact.get("website") or ""
        qs = parse_qs(urlparse(str(url)).query)
        for key in ("gclid", "gbraid", "wbraid"):
            if qs.get(key):
                ids[key] = qs[key][0]
    return ids


def primary_email(contact: dict) -> str | None:
    for slot in contact.get("email_addresses") or []:
        if slot.get("email"):
            return slot["email"]
    return contact.get("email")


def primary_phone(contact: dict) -> str | None:
    for slot in contact.get("phone_numbers") or []:
        if slot.get("number"):
            return slot["number"]
    return None


# ── Keap ──────────────────────────────────────────────────────────────────────

def keap_get(path: str, params: dict | None = None) -> dict:
    import requests  # import tre: --selftest chay duoc khi chua cai dependency

    r = requests.get(
        f"{KEAP_BASE}{path}",
        headers={"Authorization": f"Bearer {KEAP_KEY}", "Accept": "application/json"},
        params=params or {},
        timeout=30,
    )
    r.raise_for_status()
    return r.json()


def keap_tagged_contacts(tag_id: int, since: datetime) -> list[dict]:
    """Contact mang tag, loc theo date_applied >= since. Phan trang limit/offset (v1)."""
    out, offset = [], 0
    while True:
        page = keap_get(f"/tags/{tag_id}/contacts", {"limit": 1000, "offset": offset})
        items = page.get("contacts") or []
        for c in items:
            applied = parse_ts(c.get("date_applied"))
            if applied and applied >= since:
                out.append({"id": c["contact"]["id"] if "contact" in c else c.get("id"),
                            "applied_at": applied})
        if len(items) < 1000:
            return out
        offset += 1000


def keap_contact(contact_id: int) -> dict:
    return keap_get(f"/contacts/{contact_id}", {"optional_properties": "custom_fields"})


def parse_ts(value) -> datetime | None:
    if not value:
        return None
    try:
        return datetime.fromisoformat(str(value).replace("Z", "+00:00"))
    except ValueError:
        return None


# ── Dung payload ──────────────────────────────────────────────────────────────

def build_event(contact: dict, stage: str, applied_at: datetime) -> dict | None:
    """None = khong du dinh danh de Google match -> bo qua, dung gui rac."""
    cid = contact.get("id")
    identifiers = hash_identifiers(primary_email(contact), primary_phone(contact))
    click_ids = extract_click_ids(contact)
    if not click_ids and not identifiers:
        log.warning("contact %s stage %s: khong co gclid lan email/phone -> bo qua", cid, stage)
        return None

    event = {
        "eventTimestamp": applied_at.astimezone(timezone(timedelta(hours=7))).isoformat(),
        "transactionId": f"keap-{cid}-{stage}",  # khoa khu trung phia Google
        "conversionValue": STAGES[stage]["value"],
        "currency": "VND",
    }
    if click_ids:
        event["adIdentifiers"] = click_ids
    if identifiers:
        event["userData"] = {"userIdentifiers": identifiers}
    return event


def build_request(stage: str, events: list[dict], dry_run: bool) -> dict:
    return {
        "destinations": [{
            "operatingAccount": {"accountType": "GOOGLE_ADS", "accountId": GADS_CUSTOMER_ID},
            "loginAccount": {"accountType": "GOOGLE_ADS", "accountId": GADS_LOGIN_CUSTOMER_ID},
            "productDestinationId": STAGES[stage]["conversion_action_id"],
        }],
        "encoding": "HEX",
        "events": events,
        # Traffic 100% VN (ngoai EEA) — xem tracking/lp-requirements.md §1.1.
        "consent": {"adUserData": "CONSENT_GRANTED", "adPersonalization": "CONSENT_GRANTED"},
        "validateOnly": dry_run,
    }


# ── Google auth + upload ──────────────────────────────────────────────────────

def access_token() -> str:
    import google.auth
    import google.auth.transport.requests as gtr
    from google.oauth2 import service_account

    if SA_IMPERSONATE:
        from google.auth import impersonated_credentials
        source, _ = google.auth.default(scopes=["https://www.googleapis.com/auth/cloud-platform"])
        creds = impersonated_credentials.Credentials(
            source_credentials=source,
            target_principal=SA_IMPERSONATE,
            target_scopes=[DM_SCOPE],
        )
    elif SA_KEY_FILE:
        creds = service_account.Credentials.from_service_account_file(SA_KEY_FILE, scopes=[DM_SCOPE])
    else:
        creds, _ = google.auth.default(scopes=[DM_SCOPE])
    creds.refresh(gtr.Request())
    return creds.token


def upload(stage: str, events: list[dict], token: str, dry_run: bool) -> int:
    """Tra ve so event gui thanh cong. Tu chia batch theo gioi han 2000."""
    import requests

    sent = 0
    for i in range(0, len(events), MAX_EVENTS_PER_REQUEST):
        batch = events[i:i + MAX_EVENTS_PER_REQUEST]
        r = requests.post(
            DM_ENDPOINT,
            headers={"Authorization": f"Bearer {token}", "Content-Type": "application/json"},
            json=build_request(stage, batch, dry_run),
            timeout=60,
        )
        if r.status_code >= 400:
            # PONYTAIL: khong retry. Cron chay lai ngay mai voi lookback 7 ngay va
            # transactionId chan dem dup — do la co che retry. Them backoff khi nao
            # log cho thay loi 5xx thuc su lap lai.
            log.error("stage %s batch %d loi %s: %s", stage, i // MAX_EVENTS_PER_REQUEST, r.status_code, r.text[:500])
            continue
        log.info("stage %s: gui %d event, requestId=%s", stage, len(batch), r.json().get("requestId"))
        sent += len(batch)
    return sent


# ── State (idempotent phia minh) ──────────────────────────────────────────────

def load_state() -> set[str]:
    if STATE_FILE.exists():
        return set(json.loads(STATE_FILE.read_text()).get("uploaded", []))
    return set()


def save_state(uploaded: set[str]) -> None:
    STATE_FILE.write_text(json.dumps({"uploaded": sorted(uploaded)}, indent=0))


# ── Main ──────────────────────────────────────────────────────────────────────

def run(dry_run: bool) -> int:
    since = datetime.now(timezone.utc) - timedelta(days=LOOKBACK_DAYS)
    done = load_state()
    token = access_token()
    total_sent = total_skipped = 0

    for stage in STAGES:
        events, keys = [], []
        for row in keap_tagged_contacts(STAGES[stage]["keap_tag_id"], since):
            key = f"keap-{row['id']}-{stage}"
            if key in done:
                total_skipped += 1
                continue
            event = build_event(keap_contact(row["id"]), stage, row["applied_at"])
            if event:
                events.append(event)
                keys.append(key)
        if not events:
            log.info("stage %s: khong co gi moi", stage)
            continue
        sent = upload(stage, events, token, dry_run)
        total_sent += sent
        if sent and not dry_run:
            done.update(keys[:sent])

    if not dry_run:
        save_state(done)
    log.info("uploaded=%d skipped=%d failed=%d dry_run=%s",
             total_sent, total_skipped, 0, dry_run)
    return 0


def selftest() -> int:
    """Mot check chay duoc: chuan hoa + hash + parse gclid + hinh dang payload."""
    # Test vector that — doi chieu voi ecl-keap-pipeline.md §4
    assert normalize_email("  Test@Example.COM ") == "test@example.com"
    assert normalize_email("khong-phai-email") is None
    # Luat gmail: bo dau '.' va '+suffix' o local part — CHI ap cho gmail/googlemail
    assert normalize_email("Nguyen.Van.A+bds@Gmail.com") == "nguyenvana@gmail.com"
    assert normalize_email("a.b@yahoo.com") == "a.b@yahoo.com"  # domain khac giu nguyen dau cham
    # Customer Match dung gmail_rules=False (chuan hoa CM khac ECL — curriculum §F6b)
    assert normalize_email("Nguyen.Van.A+bds@Gmail.com", gmail_rules=False) == "nguyen.van.a+bds@gmail.com"
    assert sha256_hex("test@example.com") == \
        "973dfe463ec85785f5f95af5ba3906eedb2d931c24e69824a89ea65dba4e813b"

    assert to_e164_vn("0912345678") == "+84912345678"
    assert to_e164_vn("0912 345 678") == "+84912345678"
    assert to_e164_vn("84912345678") == "+84912345678"
    assert to_e164_vn("+84 912 345 678") == "+84912345678"
    assert to_e164_vn("0000000000") is None      # rac
    assert to_e164_vn("123") is None
    assert sha256_hex("+84912345678") == \
        "ed644edf0566470f0b5a8c13c792fa8e8a489574da3aceec119b9456e870d396"

    # Duong A: khong co custom field rieng -> parse gclid tu landing URL
    KEAP_FIELD_IDS.update({"gclid": None, "gbraid": None, "wbraid": None, "landing_url": 10})
    contact_a = {
        "id": 48213,
        "email_addresses": [{"email": "Test@Example.com"}],
        "phone_numbers": [{"number": "0912345678"}],
        "custom_fields": [{"id": 10, "content": "https://lp.vn/du-an/?gclid=ABC123&utm_source=google"}],
    }
    assert extract_click_ids(contact_a) == {"gclid": "ABC123"}

    # Duong B: co custom field rieng -> uu tien field, bo qua URL
    KEAP_FIELD_IDS.update({"gclid": 7, "landing_url": 10})
    contact_b = dict(contact_a, custom_fields=[
        {"id": 7, "content": "FIELD_GCLID"},
        {"id": 10, "content": "https://lp.vn/du-an/?gclid=URL_GCLID"},
    ])
    assert extract_click_ids(contact_b) == {"gclid": "FIELD_GCLID"}

    # Hinh dang payload
    applied = datetime(2026, 7, 28, 2, 15, tzinfo=timezone.utc)
    KEAP_FIELD_IDS.update({"gclid": None, "landing_url": 10})
    ev = build_event(contact_a, "qualified", applied)
    assert ev["transactionId"] == "keap-48213-qualified"
    assert ev["conversionValue"] == 50
    assert ev["adIdentifiers"] == {"gclid": "ABC123"}
    assert ev["eventTimestamp"] == "2026-07-28T09:15:00+07:00"      # doi ve ICT
    assert len(ev["userData"]["userIdentifiers"]) == 2
    assert all(len(list(i.values())[0]) == 64 for i in ev["userData"]["userIdentifiers"])  # hex SHA-256

    req = build_request("qualified", [ev], dry_run=True)
    assert req["encoding"] == "HEX"
    assert req["validateOnly"] is True
    assert req["destinations"][0]["operatingAccount"]["accountType"] == "GOOGLE_ADS"
    assert req["destinations"][0]["productDestinationId"] == STAGES["qualified"]["conversion_action_id"]

    # Khong dinh danh nao -> khong gui
    assert build_event({"id": 1, "custom_fields": []}, "contactable", applied) is None

    print("selftest OK")
    return 0


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--dry-run", action="store_true", help="goi API that voi validateOnly=true")
    ap.add_argument("--selftest", action="store_true", help="kiem tra logic, khong goi mang")
    args = ap.parse_args()

    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
    if args.selftest:
        sys.exit(selftest())
    if not KEAP_KEY:
        log.error("thieu KEAP_SERVICE_ACCOUNT_KEY")
        sys.exit(1)
    sys.exit(run(args.dry_run))
