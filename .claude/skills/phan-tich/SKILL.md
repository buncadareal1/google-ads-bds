---
name: phan-tich
description: Phân tích nhanh hiệu suất ads Beachtro (Ads + GA4) và báo cáo SIÊU NGẮN. Dùng khi user nói "phân tích", "check chỉ số", "báo cáo", "số hôm nay như nào", "soi camp/GA4". User có ADHD — output mặc định ≤10 dòng, chi tiết chỉ khi được hỏi thêm.
---

# Phân tích nhanh — flow chuẩn (đúc từ session 2026-08-07, nâng cấp 12/08 từ notfair + claude-ads)

## Bước 0 — Sổ thay đổi (bao_cao.py in sẵn ở đầu)

`ops/change-log.jsonl` — mỗi thay đổi có `review_sau` (+7 ngày cho bid/negative/budget, +14 ngày cho RSA/cấu trúc). **Thay đổi chưa tới hạn → CẤM phán tác động**, chỉ nói "còn N ngày". Tới hạn → so với `gia_thuyet`/`metric_thanh_cong`/`guardrail` đã đăng ký TRƯỚC, phán 1 trong 4: tốt / xấu (CPA +20% hoặc conv −20% → đề xuất revert) / không kết luận được / còn non. **Mọi thay đổi mới lên tài khoản = thêm 1 dòng vào file này, mỗi lần chỉ đổi 1 biến.**

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
- Tổng chi search terms < tổng chi ngày → phần lệch = term ẩn (bình thường nếu <15%). **Lệch >30% = KHÔNG phải term ẩn, phải soi `segments.ad_network_type` ngay** — dính thật 14-15/08: Display Expansion bật ngầm, ăn 1,03tr / 54 click / 0 conv (bao_cao.py giờ in sẵn khối MẠNG HIỂN THỊ)
- Impression tăng đột biến + CTR tụt cùng lúc = **pha loãng mạng**, không phải ad kém. Đọc riêng phần SEARCH rồi mới kết luận về ad/bid
- IS/keyword-IS của HÔM NAY luôn = 0% → nghĩa là CHƯA CÓ SỐ, không phải 0. Chỉ đọc IS ngày đã chốt
- form_submit từ desktop/direct = test nội bộ, không phải lead ads (đối chiếu thiết bị+nguồn với click ads)
- **Nút thắt (chọn đúng 1 nhãn trước khi đề xuất)**: mất-budget >40% = thiếu VỐN (thêm tiền nếu CPL đạt) · mất-rank >30% + QS/LPX yếu = thiếu CHẤT (sửa ad/LP, KHÔNG thêm tiền) · cả hai thấp + impr thấp = HẾT CẦU (bằng chứng hợp lệ duy nhất để mở non-brand) · tiền chảy vào term rác = QUERY · tag hỏng = TRACKING
- **Cổng đủ mẫu**: trước khi phán "X không ra lead" → `click × CVR tài khoản (~2,5%) ≥ 3`, tức ~120 click. Dưới ngưỡng = "chưa đủ mẫu", không quyết định
- **So sánh**: cùng account + cùng độ dài kỳ + cùng độ chín conversion-lag mới được so. Benchmark ngành chỉ gắn nhãn "định hướng"
- **3 nguồn số không cộng chéo**: conv Ads (attributed, chẩn đoán delivery) ≠ GA4 (hành trình) ≠ CRM/Keap (lead nghiệm thu thật). Mỗi con số phải khai nguồn

## Bước 4 — Báo cáo. FORMAT BẮT BUỘC (≤10 dòng):

```
🚦 [1 câu verdict; nếu thay đổi đang chín chưa tới hạn → verdict là "TẠM"]
💰 Hôm nay: chi X | click Y | CPC Z — so hôm qua ↑↓
👀 IS ngày chốt: X% (mất-rank Y% / mất-budget Z%) → nút thắt: [1 nhãn]
🔍 Search terms: sạch ✓ / N term rác → đã negative
🌍 GA4: N session ads · ~Xs/phiên · Y% TP.HCM
📞 Lead: chưa có (mốc kỳ vọng ~30-50 click) / CÓ → kiểm gclid ngay
⚪ Không đo được: phone/zalo click, lead ngoài form (luôn nhắc — đừng đọc "0" thành "không có")
👉 Cần làm: [1 việc duy nhất] / "đợi đến <ngày review / ngưỡng click cụ thể>" — cấm chữ "đợi" trần
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
⚠️ Mỗi con số phải khai nguồn ngay cạnh: `(Ads, 30d click)` / `(GA4)` / `(CRM — anh cung cấp)` — 3 hệ đếm khác nhau, cộng chéo là sai.

## Cờ đỏ — CHỈ những trường hợp này mới được viết dài hơn 10 dòng

1. **Lead đầu tiên xuất hiện mà không có gclid trong Keap** → đề nghị PAUSE campaign (task #20)
2. Search term rác/sai ngành → liệt kê + negative ngay
3. Chi/impression bất thường >2× nhịp cũ (cả tốt lẫn xấu — luật Twyman) hoặc chạm phanh 30tr/tháng. **Nghi can số 1: mạng CONTENT** (bẫy #18), số 2: search term mới
4. Ad bị DISAPPROVED / **APPROVED_LIMITED** / campaign primary_status LIMITED vì policy — đọc `policy_topic_entries` (bao_cao.py in sẵn). Đã dính thật: `PHONE_NUMBER_IN_AD_TEXT` 12/08. **Ad Strength POOR KHÔNG phải cờ đỏ với campaign brand** (brand pin khớp LP → POOR nhưng CTR/CVR cao là bình thường — notfair rsa-best-practices)
5. Ngày tracking hỏng → vứt toàn bộ số ngày đó, nói rõ

## Bối cảnh cố định (đỡ tra lại)

- Campaign `24103805490` · budget 1tr₫/ngày · trần CPC 35.000₫ (20k → 35k → 28k ngày 12/08 → 35k ngày 14/08 sau Auction Insights)
- Mỗi ad group có 2 RSA từ 12/08 (bộ gốc + bộ v4 "bằng chứng Sun World"). KHÔNG phải A/B test — chỉ đọc tổng lead/CPL cả nhóm
- Baseline tuần 1 (06-12/08): 1.714 impr · 122 click · CTR 7,1% · chi 3,16tr · 3 conv (CPL ~1,05tr)
- Kỳ đo mới từ 13/08 (ngày 12/08 đổi cả bid lẫn RSA — không so trực tiếp với tuần 1)
- **CVR/CPL CHỈ đọc từ cột conversions của Ads.** `gui_form_beachtro_tower` GA4 bắn theo MỖI pageview trang cám ơn (F5/back = đếm thêm — tuần 1 GA4 đếm 5 vs Ads 3, thổi +67%). GA4 chỉ dùng xem hành vi
- Cuộc gọi TỪ QUẢNG CÁO đo được từ 12/08: action `7718436367` "Cuộc gọi từ quảng cáo (>=60s)" — **SECONDARY**, nằm ở cột "Tất cả conversion", KHÔNG cộng vào cột conversions chính. Phone/zalo click TRÊN LP vẫn không đo (quyết định không sửa GTM)
- Hồ sơ đầy đủ: `projects/beachtro-tower/PROJECT.md` + `plan-chay-ads.md`
