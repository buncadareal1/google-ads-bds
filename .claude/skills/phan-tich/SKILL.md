---
name: phan-tich
description: Phân tích nhanh hiệu suất ads Beachtro (Ads + GA4) và báo cáo SIÊU NGẮN. Dùng khi user nói "phân tích", "check chỉ số", "báo cáo", "số hôm nay như nào", "soi camp/GA4". User có ADHD — output mặc định ≤10 dòng, chi tiết chỉ khi được hỏi thêm.
---

# Phân tích nhanh — flow chuẩn (đúc từ session 2026-08-07, nâng cấp 12/08 từ notfair + claude-ads)

## Bước 0 — Sổ thay đổi + MỨC TIN CẬY (bao_cao.py in sẵn ở đầu)

`ops/change-log.jsonl` — mỗi thay đổi có `review_sau` (+7 ngày bid/negative/budget, +14 ngày RSA/cấu trúc).

**Luôn phải có kết luận. Chỉ khác nhau ở mức tin cậy — không được từ chối đọc số.**

| Mức | Khi nào | Cách viết |
|---|---|---|
| 🟢 **CHỐT** | tới hạn review **và** đủ mẫu (click × CVR ≥ 3) | phán dứt khoát: tốt / xấu (CPA +20% hoặc conv −20% → đề xuất revert) / không đổi |
| 🟡 **NGHIÊNG** | chưa tới hạn hoặc thiếu mẫu | **vẫn nói hướng**: "đang nghiêng về X (n=…)" + chốt được vào ngày/ngưỡng nào. Không dừng ở "chưa đủ mẫu" |
| ⚫ **KHÔNG ĐỌC ĐƯỢC** | ngày tracking hỏng, đổi ≥2 biến cùng lúc, mạng nhiễm | trường hợp DUY NHẤT được từ chối kết luận — phải nói rõ lý do |

**Mọi thay đổi mới lên tài khoản = 1 dòng vào file này, mỗi lần đổi 1 biến.**

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
- **Cổng đủ mẫu**: `click × CVR tài khoản (~2,5%) ≥ 3` (~120 click) mới gọi là CHỐT. Dưới ngưỡng vẫn phải nêu hướng + con số cần đạt để chốt (vd: "nghiêng xấu, n=39, chốt được ở ~120 click ≈ 5 ngày nữa")
- **So sánh**: cùng account + cùng độ dài kỳ + cùng độ chín conversion-lag mới được so. Benchmark ngành chỉ gắn nhãn "định hướng"
- **3 nguồn số không cộng chéo**: conv Ads (attributed, chẩn đoán delivery) ≠ GA4 (hành trình) ≠ CRM/Keap (lead nghiệm thu thật). Mỗi con số phải khai nguồn

## Bước 4 — Báo cáo. FORMAT BẮT BUỘC (≤10 dòng):

```
🚦 [1 câu verdict + mức tin cậy: CHỐT / NGHIÊNG / KHÔNG ĐỌC ĐƯỢC]
💰 Hôm nay: chi X | click Y | CPC Z — so hôm qua ↑↓
👀 IS ngày chốt: X% (mất-rank Y% / mất-budget Z%) → nút thắt: [1 nhãn]
🔍 Search terms: sạch ✓ / N term rác → đã negative
🌍 GA4: N session ads · ~Xs/phiên · Y% TP.HCM
📞 Lead: N (nguồn Ads) — CÓ lead mới thì kiểm gclid ngay
👉 Cần làm: [1 việc làm được NGAY]. Nếu việc đó là chờ → ghi "chốt được vào <ngày/ngưỡng>" kèm số cụ thể
```

**Luật cân bằng giọng (thêm 19/08 — user phản hồi skill quá "chặt", phủ định quá nhiều):**

- Mỗi báo cáo phải có **≥1 câu kết luận có hướng** và **đúng 1 việc làm được ngay**. Không có việc để làm thì nói thẳng "hệ đang chạy đúng, không cần đụng" — đó cũng là một kết luận.
- **Tối đa 1 dòng** cảnh báo / "không đo được" trong cả báo cáo. Dòng ⚪ phone/zalo chỉ nhắc khi user đang đọc con số lead, không nhắc mỗi lần.
- Đếm trước khi gửi: nếu bản nháp có **>2 câu** chứa *chưa / không / cấm / đợi / chưa đủ* → viết lại theo hướng khẳng định ("n=39, hướng nghiêng xấu, chốt ở 120 click").
- Cảnh báo phải kèm **con số + ngày**, không cảnh báo suông.

Không thêm bảng, không giải thích phương pháp, không kể quá trình query. User hỏi "vì sao" mới mở rộng đúng mục đó.

## Bước 4b — Khi user xin BÁO CÁO TỔNG HỢP / báo cáo gửi sếp

Format chuẩn công ty (Mạnh Sâm MKT). **Hai khối, hai phạm vi khác nhau — sai chỗ này là sai cả báo cáo (dính thật 19/08):**

- **Khối trên = CHỈ kỳ báo cáo** (khoảng ngày user hỏi)
- **Khối dưới = LŨY KẾ từ ngày bật campaign đến nay** (cộng cả các kỳ trước)

```
Thời gian: <dd/mm> đến <dd/mm/yyyy>
Beachtro Tower - Blanca City | Tường Đặng MKT | Google Ads

Ngân sách đã chạy: <chi KỲ NÀY> đ
Số lead: <n kỳ này> (<a> F1 + <b> đang chăm)
Chi phí/lead (CPL): <chi kỳ / lead kỳ> đ
Chi phí / F1: <chi kỳ / F1 kỳ> đ

Tổng lead (form, hotline, zalo): <LŨY KẾ> (<a> F1 + <b> đang chăm)
Tổng lead F1: <LŨY KẾ>
Tỷ lệ qualify lead: <F1 lũy kế / lead lũy kế>
Tổng ngân sách đã chạy: <chi LŨY KẾ> đ
Booking, F4 từ chiến dịch: <n> BK, <n> Deal
```

**Cách làm cho đúng:**

1. Kéo chi kỳ này + chi lũy kế bằng 2 query riêng (`segments.date BETWEEN`), đừng trừ nhẩm.
2. Lead/F1/booking do **CRM giữ** — hỏi user, không bịa. User đưa số thì hỏi rõ **"số này của kỳ hay lũy kế?"** nếu chưa nói.
3. Cộng dồn kỳ trước: đọc bảng nghiệm thu ở nhật ký `PROJECT.md` (mục "Nghiệm thu lead từ CRM") — các kỳ cũ đã chốt nằm sẵn ở đó.
4. **Luôn kèm 1 dòng CPL tính trên riêng chi Search** khi có mạng/kênh không ra lead bị loại — đó mới là hiệu quả thật của tiền chạy đúng chỗ.
5. Mỗi con số khai nguồn: `(Ads)` / `(GA4)` / `(CRM — anh cung cấp)`.

**CRM > Ads là bình thường, không phải lỗi đo**: hệ không đo lead qua hotline/Zalo. Ghi chênh lệch thành 1 câu giải thích, đừng để sếp tưởng thất thoát dữ liệu.

## Cờ đỏ — CHỈ những trường hợp này mới được viết dài hơn 10 dòng

1. **Lead đầu tiên xuất hiện mà không có gclid trong Keap** → đề nghị PAUSE campaign (task #20)
2. Search term rác/sai ngành → liệt kê + negative ngay
3. Chi/impression bất thường >2× nhịp cũ (cả tốt lẫn xấu — luật Twyman) hoặc chạm phanh 30tr/tháng. **Nghi can số 1: mạng CONTENT** (bẫy #18), số 2: search term mới
4. Ad bị DISAPPROVED / **APPROVED_LIMITED** / campaign primary_status LIMITED vì policy — đọc `policy_topic_entries` (bao_cao.py in sẵn). Đã dính thật: `PHONE_NUMBER_IN_AD_TEXT` 12/08. **Ad Strength POOR KHÔNG phải cờ đỏ với campaign brand** (brand pin khớp LP → POOR nhưng CTR/CVR cao là bình thường — notfair rsa-best-practices)
5. Ngày tracking hỏng → vứt toàn bộ số ngày đó, nói rõ

## Bối cảnh cố định (đỡ tra lại)

- Campaign `24103805490` · budget 1tr₫/ngày · trần CPC 35.000₫. **Lịch sử bật/tắt: chạy 06→17/08 (user tắt ngưng lỗ) → BẬT LẠI 18/08.** Kỳ đo hiện tại tính từ **18/08**, không nối với kỳ cũ
- Mạng Display **đã tắt 15/08** (rò 1,03tr / 52 click / 0 conv). Mỗi lần phân tích kiểm lại khối MẠNG HIỂN THỊ trong bao_cao.py
- Mỗi ad group có 2 RSA từ 12/08 (bộ gốc + bộ v4 "bằng chứng Sun World"). KHÔNG phải A/B test — chỉ đọc tổng lead/CPL cả nhóm
- **Kết quả kỳ 1 (06–18/08, đã đóng sổ)**: 8.027 impr · 274 click · chi 7,15tr · 4 conv Ads · **6 lead CRM / 2 F1** · CPL 1,19tr (964k nếu chỉ tính chi Search). Bảng đầy đủ 2 kỳ: `PROJECT.md` mục nghiệm thu 19/08
- **CVR/CPL CHỈ đọc từ cột conversions của Ads.** `gui_form_beachtro_tower` GA4 bắn theo MỖI pageview trang cám ơn (F5/back = đếm thêm — tuần 1 GA4 đếm 5 vs Ads 3, thổi +67%). GA4 chỉ dùng xem hành vi
- Cuộc gọi TỪ QUẢNG CÁO đo được từ 12/08: action `7718436367` "Cuộc gọi từ quảng cáo (>=60s)" — **SECONDARY**, nằm ở cột "Tất cả conversion", KHÔNG cộng vào cột conversions chính. Phone/zalo click TRÊN LP vẫn không đo (quyết định không sửa GTM)
- Hồ sơ đầy đủ: `projects/beachtro-tower/PROJECT.md` + `plan-chay-ads.md`
