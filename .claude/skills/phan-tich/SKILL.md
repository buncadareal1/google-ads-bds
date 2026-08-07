---
name: phan-tich
description: Phân tích nhanh hiệu suất ads Beachtro (Ads + GA4) và báo cáo SIÊU NGẮN. Dùng khi user nói "phân tích", "check chỉ số", "báo cáo", "số hôm nay như nào", "soi camp/GA4". User có ADHD — output mặc định ≤10 dòng, chi tiết chỉ khi được hỏi thêm.
---

# Phân tích nhanh — flow chuẩn (đúc từ session 2026-08-07)

## Bước 1 — Kéo số Ads (1 lệnh)

```bash
.venv-ads/bin/python scripts/bao_cao.py
```

Cho ra: ngày × 7 (impr/click/CTR/CPC/chi/conv/IS/mất-rank/mất-budget), hôm nay theo giờ, search terms, trạng thái ad.

## Bước 2 — Kéo GA4 (MCP `analytics-ga4`, property `548678683`)

Hai report, date range từ 2026-08-06 (ngày bật camp) đến hôm nay:

1. **Nguồn × thiết bị**: dims `sessionSourceMedium, deviceCategory` · metrics `sessions, averageSessionDuration, userEngagementDuration`
2. **Event KHÔNG LỌC**: dims `eventName` · metric `eventCount` — ⚠️ tuyệt đối không lọc theo bộ event chuẩn (`generate_lead`…) vì LP này chỉ bắn event tự động GA4 (`form_start`, `form_submit`, `scroll`); lọc là mất dữ liệu (đã dính 1 lần)

Cần địa lý thì thêm report `city × sessionSourceMedium`.

## Bước 3 — Kiểm chéo (chỉ đánh dấu ✓/✗, không viết dài)

- Click Ads ≈ session google/cpc GA4 (hao 10–30% là bình thường; GA4 trễ vài GIỜ — chỉ so ngày đã chốt)
- Tổng chi search terms < tổng chi ngày → phần lệch = term ẩn (bình thường nếu <15%)
- IS/keyword-IS của HÔM NAY luôn = 0% → nghĩa là CHƯA CÓ SỐ, không phải 0. Chỉ đọc IS ngày đã chốt
- form_submit từ desktop/direct = test nội bộ, không phải lead ads (đối chiếu thiết bị+nguồn với click ads)

## Bước 4 — Báo cáo. FORMAT BẮT BUỘC (≤10 dòng):

```
🚦 [1 câu verdict: ổn / có vấn đề X]
💰 Hôm nay: chi X | click Y | CPC Z — so hôm qua ↑↓
👀 IS ngày chốt gần nhất: X% (mất-rank Y% / mất-budget Z%)
🔍 Search terms: sạch ✓ / N term rác → đã negative
🌍 GA4: N session ads · ~Xs/phiên · Y% TP.HCM
📞 Lead: chưa có (mốc kỳ vọng ~30-50 click) / CÓ → kiểm gclid ngay
👉 Cần làm: [1 việc duy nhất, hoặc "không — đợi"]
```

Không thêm bảng, không giải thích phương pháp, không kể quá trình query. User hỏi "vì sao" mới mở rộng đúng mục đó.

## Cờ đỏ — CHỈ những trường hợp này mới được viết dài hơn 10 dòng

1. **Lead đầu tiên xuất hiện mà không có gclid trong Keap** → đề nghị PAUSE campaign (task #20)
2. Search term rác/sai ngành → liệt kê + negative ngay
3. Chi bất thường >2× nhịp cũ (cả tốt lẫn xấu — luật Twyman) hoặc chạm phanh 30tr/tháng
4. Ad bị DISAPPROVED / strength tụt xuống POOR
5. Ngày tracking hỏng → vứt toàn bộ số ngày đó, nói rõ

## Bối cảnh cố định (đỡ tra lại)

- Campaign `24103805490` · budget 1tr₫/ngày · trần CPC 35.000₫ (nâng từ 20k ngày 2026-08-06)
- Baseline ngày đầu 06/08: 89 impr · 4 click · IS 47% · mất-rank 50%
- Tuần 1 (đến ~13/08): đóng băng bid/budget/RSA/keyword, chỉ thêm negative
- GA4 không đo được phone/zalo click (quyết định không sửa GTM) — "0 cuộc gọi" nghĩa là "không đo được"
- Hồ sơ đầy đủ: `projects/beachtro-tower/PROJECT.md` + `plan-chay-ads.md`
