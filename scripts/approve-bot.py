#!/usr/bin/env python3
"""Bot duyệt-là-chạy: long-poll Telegram, apply action đã duyệt qua Google Ads API.

Chạy: TG_BOT_TOKEN=... TG_CHAT_ID=... python3 scripts/approve-bot.py
Test: python3 scripts/approve-bot.py --selftest
Spec + luật an toàn: playbook/monitoring.md §6. Action chờ duyệt: ops/pending-actions.jsonl
"""
import json, os, sys, time, urllib.request, urllib.parse

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PENDING = os.path.join(HERE, "ops", "pending-actions.jsonl")
AUDIT = os.path.join(HERE, "ops", "audit-log.jsonl")
EXPIRY_S = 24 * 3600
ALLOWED = {"add_negative", "budget_change", "tcpa_change", "pause_entity", "promote_exact"}


def tg(method, **params):
    tok = os.environ["TG_BOT_TOKEN"]
    data = urllib.parse.urlencode(params).encode()
    with urllib.request.urlopen(f"https://api.telegram.org/bot{tok}/{method}", data, timeout=35) as r:
        return json.load(r)


def load_actions():
    if not os.path.exists(PENDING):
        return {}
    with open(PENDING) as f:
        return {a["id"]: a for a in map(json.loads, f) if a}


def audit(entry):
    os.makedirs(os.path.dirname(AUDIT), exist_ok=True)
    with open(AUDIT, "a") as f:
        f.write(json.dumps(entry, ensure_ascii=False) + "\n")


def apply_action(a):
    """Apply 1 action qua Google Ads API. Trả (ok, message)."""
    if a["type"] not in ALLOWED:
        return False, f"type {a['type']} ngoài whitelist"
    if time.time() - a["created_at"] > EXPIRY_S:
        return False, "action quá 24h, số liệu cũ — tạo suggest mới"
    done = {e.get("action_id") for e in map(json.loads, open(AUDIT))} if os.path.exists(AUDIT) else set()
    if a["id"] in done:
        return False, "đã chạy rồi (idempotent)"
    # PONYTAIL: executor thật cần developer token + google-ads lib.
    # Mỗi type: re-check điều kiện từ API (budget hiện tại, learning phase, conv 30d)
    # theo giới hạn cứng trong monitoring.md §6 TRƯỚC khi mutate. Điền khi có token.
    return False, "executor chưa nối Google Ads API (chờ developer token) — action hợp lệ, đã ghi log"


def selftest():
    os.makedirs(os.path.join(HERE, "ops"), exist_ok=True)
    a = {"id": "t1", "type": "budget_change", "created_at": time.time(), "params": {"campaign": "X", "new": 550000}}
    ok, msg = apply_action(a)
    assert not ok and "developer token" in msg, msg
    ok, msg = apply_action({**a, "type": "delete_campaign"})
    assert not ok and "whitelist" in msg, msg
    ok, msg = apply_action({**a, "created_at": time.time() - 90000})
    assert not ok and "24h" in msg, msg
    print("selftest OK")


def main():
    chat_id = os.environ["TG_CHAT_ID"]
    offset = 0
    print("approve-bot: long-polling...")
    while True:
        for u in tg("getUpdates", offset=offset, timeout=30).get("result", []):
            offset = u["update_id"] + 1
            cb = u.get("callback_query")
            if not cb:
                continue
            # kiểm NGƯỜI BẤM (from.id), không chỉ chat — trong group mọi thành viên đều bấm được nút
            if str(cb["message"]["chat"]["id"]) != str(chat_id) or str(cb["from"]["id"]) != str(os.environ.get("TG_USER_ID", chat_id)):
                audit({"event": "reject_foreign", "from": cb["from"].get("id"), "ts": time.time()})
                continue
            decision, _, action_id = cb["data"].partition(":")  # "approve:<id>" | "skip:<id>"
            a = load_actions().get(action_id)
            if not a:
                tg("answerCallbackQuery", callback_query_id=cb["id"], text="Không tìm thấy action")
                continue
            if decision == "approve":
                ok, msg = apply_action(a)
                audit({"action_id": action_id, "decision": "approve", "ok": ok, "msg": msg,
                       "action": a, "ts": time.time()})
                tg("sendMessage", chat_id=chat_id, text=f"{'✅' if ok else '⚠️'} {a['type']}: {msg}")
            else:
                audit({"action_id": action_id, "decision": "skip", "ts": time.time()})
                tg("sendMessage", chat_id=chat_id, text=f"⏭ Bỏ qua: {a.get('summary', action_id)}")
            tg("answerCallbackQuery", callback_query_id=cb["id"])
        time.sleep(1)


if __name__ == "__main__":
    selftest() if "--selftest" in sys.argv else main()
