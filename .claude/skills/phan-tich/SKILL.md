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

## Bước 4b — Khi user xin BÁO CÁO TỔNG HỢP / báo cáo gửi sếp

Dùng format chuẩn công ty (Mạnh Sâm MKT), KHÔNG dùng format 10 dòng ở trên:

```
Thời gian: <dd/mm> đến <dd/mm/yyyy>
Beachtro Tower - Blanca City | <tên người chạy> | Google Ads

Ngân sách đã chạy: <chi> đ
Số lead: <n> (<a> F1 + <b> đang chấm)
Chi phí/lead (CPL): <chi/lead> đ
Chi phí / F1: <chi/F1> đ

Tổng lead (form, hotline, zalo): <n> (<a> đang chấm + <b> F1)
Tổng lead F1: <n>
Tỷ lệ qualify lead: <%>
Tổng ngân sách đã chạy: <đ>
Booking, F4 từ chiến dịch: <n> BK, <n> Deal
```

⚠️ Dữ liệu KHÔNG tự có, phải hỏi user (sale/CRM giữ): **F1, tỷ lệ qualify, booking, deal, lead qua hotline/Zalo**. Điền `— cần anh cung cấp` chứ TUYỆT ĐỐI không bịa. Phần Google Ads (chi, lead form, CPL) tự lấy từ script + GA4.

## Cờ đỏ — CHỈ những trường hợp này mới được viết dài hơn 10 dòng

1. **Lead đầu tiên xuất hiện mà không có gclid trong Keap** → đề nghị PAUSE campaign (task #20)
2. Search term rác/sai ngành → liệt kê + negative ngay
3. Chi bất thường >2× nhịp cũ (cả tốt lẫn xấu — luật Twyman) hoặc chạm phanh 30tr/tháng
4. Ad bị DISAPPROVED / **APPROVED_LIMITED** / campaign primary_status LIMITED vì policy / strength tụt xuống POOR — đọc `policy_topic_entries` để biết topic (bao_cao.py đã in sẵn). Đã dính thật: `PHONE_NUMBER_IN_AD_TEXT` 12/08
5. Ngày tracking hỏng → vứt toàn bộ số ngày đó, nói rõ

## Bối cảnh cố định (đỡ tra lại)

- Campaign `24103805490` · budget 1tr₫/ngày · trần CPC 28.000₫ (20k → 35k ngày 06/08 → 28k ngày 12/08)
- Mỗi ad group có 2 RSA từ 12/08 (bộ gốc + bộ v4 "bằng chứng Sun World"). KHÔNG phải A/B test — chỉ đọc tổng lead/CPL cả nhóm
- Baseline tuần 1 (06-12/08): 1.714 impr · 122 click · CTR 7,1% · chi 3,16tr · 3 conv (CPL ~1,05tr)
- Kỳ đo mới từ 13/08 (ngày 12/08 đổi cả bid lẫn RSA — không so trực tiếp với tuần 1)
- GA4 không đo được phone/zalo click (quyết định không sửa GTM) — "0 cuộc gọi" nghĩa là "không đo được"
- Hồ sơ đầy đủ: `projects/beachtro-tower/PROJECT.md` + `plan-chay-ads.md`
