"""Cổng ghi lên tài khoản Ads — mọi mutate đi qua đây (SETUP.md §1 bẫy #11 + #14).

Dùng:
    from ghi import check_ad_text, ghi, log_change
    check_ad_text(headlines + descriptions)          # chặn SĐT trước khi ghi
    ghi(lambda: svc.mutate_...(...),                 # lệnh ghi
        lambda: doc_lai_va_kiem(),                   # read-back: True nếu remote đúng
        "hạ trần CPC nhóm X xuống 32k")
    log_change("hạ trần CPC ...", gia_tri_cu="28k", gia_thuyet="...",
               metric="...", guardrail="...", review_ngay=7)
"""
import re, json, os, datetime

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PHONE = re.compile(r"0\d[\d .\-]{7,}")


def check_ad_text(texts):
    """Chặn policy PHONE_NUMBER_IN_AD_TEXT (dính thật 12/08) trước khi ghi RSA."""
    bad = [t for t in texts if PHONE.search(t)]
    assert not bad, f"SĐT trong ad text — vi phạm PHONE_NUMBER_IN_AD_TEXT: {bad}"


def ghi(mutate_fn, verify_fn, mo_ta):
    """Ghi + read-back. Response của mutate = 'Google đã nhận', KHÔNG phải bằng chứng.
    verify_fn phải đọc lại đúng resource và trả True. Fail → raise, cấm nói 'xong'."""
    resp = mutate_fn()
    assert verify_fn(), f"CHƯA XÁC MINH ĐƯỢC: {mo_ta} — mutate được nhận nhưng read-back không khớp"
    print(f"✅ {mo_ta} — đã ghi + verify read-back")
    return resp


def log_change(thay_doi, gia_tri_cu, gia_thuyet, metric, guardrail="—", review_ngay=7):
    """Ghi sổ ops/change-log.jsonl — ĐĂNG KÝ TRƯỚC giả thuyết + hạn review.
    review_ngay: 7 cho bid/negative/budget, 14 cho RSA/cấu trúc."""
    today = datetime.date.today()
    e = {"date": today.isoformat(), "thay_doi": thay_doi, "gia_tri_cu": gia_tri_cu,
         "gia_thuyet": gia_thuyet, "metric_thanh_cong": metric, "guardrail": guardrail,
         "review_sau": (today + datetime.timedelta(days=review_ngay)).isoformat(),
         "reviewed": False}
    with open(os.path.join(REPO, "ops/change-log.jsonl"), "a") as f:
        f.write(json.dumps(e, ensure_ascii=False) + "\n")
    print(f"📓 change-log: review {e['review_sau']}")


if __name__ == "__main__":
    check_ad_text(["Căn Hộ Biển Blanca City"])
    try:
        check_ad_text(["Gọi Ngay 0937 837 888"]); raise SystemExit("FAIL: không bắt được SĐT")
    except AssertionError:
        pass
    try:
        ghi(lambda: "resp", lambda: False, "test"); raise SystemExit("FAIL: verify=False mà vẫn qua")
    except AssertionError:
        pass
    print("selftest OK")
