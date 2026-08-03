#!/usr/bin/env bash
# Gửi thông báo Telegram cho vòng check ads.
# Cần 2 env vars: TG_BOT_TOKEN (từ @BotFather), TG_CHAT_ID (chat với bot).
# Dùng: ./scripts/notify-telegram.sh "nội dung" — hỗ trợ Markdown.
set -euo pipefail
: "${TG_BOT_TOKEN:?Thiếu TG_BOT_TOKEN}" "${TG_CHAT_ID:?Thiếu TG_CHAT_ID}"
curl -s --fail-with-body "https://api.telegram.org/bot${TG_BOT_TOKEN}/sendMessage" \
  -d chat_id="${TG_CHAT_ID}" \
  -d parse_mode="Markdown" \
  --data-urlencode text="${1:?Thiếu nội dung}" >/dev/null && echo "sent"
