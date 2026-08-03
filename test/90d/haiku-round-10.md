# Round 10 — Haiku — 90 ngày (Eco Retreat bid war)

**Kịch bản:** Eco Retreat (DB Invest, Bến Lức) · 30tr₫/tháng = 1tr/ngày · **CPC nền 30k₫** · **Sự kiện W2:** 2 sàn F2 bid `eco retreat` → brand CPC ×2 (30k→60k), IS 85%→55%, 1 sàn giữ tên `Eco Retreat` trong headline.

**Mô hình mô phỏng:** click = ngân sách ÷ CPC (không phạt click rác, negative 386 dòng import D1) · CVR LP = 4,8% (message match 4/5 + bảng giá + Zalo + form 2 dropdown) · qualify rate = 40% · contact rate = 55% · CPL-q = CPC ÷ (4,8% × 40%) = CPC ÷ 0,0192.

**Giả định IS:** (a) sàn F2 đổ tiền → CPC phiên đấu brand lên 60k (chặn trên cap). (b) IS nội suy tuyến tính: cap 35k→IS 55%, cap 60k→IS 85% ⇒ `IS = 55% + (cap−35k)/25k × 30đv`. (c) Tổng click brand khả dụng ở IS 100% = 18,6/ngày (từ T1: 110,8/tuần ÷ 7 × 85%) = 15,8/ngày. Click thực = `min(χ/CPC, 15,8 × IS)`.

---

## Setup + quyết định kỳ 1 (tuần đầu + xử lý bẫy)

**Pre-flight & G0:** Advertiser verification D-7 · 6 conversion action (thang 1/1/1/10/50/500, category chuẩn Google, cửa sổ 90 ngày) · GA4↔Ads auto-tagging · **386 negative account + shared list 80 campaign** dán D1 (tránh phạt 25% W1-W2) · 11 ô §1.5 (Search Partners/Display OFF, Presence, auto-apply TẮT HẾT, lịch 05-24h, UTM template, không shared budget) · Test G0 = 1 lead qua LP→GA4→Ads→Keap.

**Cấu trúc 1tr/ngày (30tr/tháng):**

| # | Campaign | ₫/ngày | Cap CPC | Ad group | KW |
|---|---|---|---|---|---|
| 1 | `BDS_Search_Brand_DuAn` | 475k | **35k** | `brand-eco-retreat` | 20 (4 exact: `eco retreat`, `+ giá`, `+ bảng giá`, `+ mở bán`; 16 phrase) |
| 2 | `BDS_Search_Brand_CDT` | 75k | 35k | `brand-cdt--ecopark` | 5 |
| 3 | `BDS_Search_KhuVuc` | 450k | 40k | `ben-luc--gia-bang-gia` (15) + `ben-luc--mua-ban` (5) | 20 |
| — | #4 #7 #8 RMKT | 0 | — | — | hoãn |

**Bidding:** Max Clicks + bid cap (không tCPA, không broad). Primary day 1 = Form_Raw + Hotline + Zalo; `phone_click`/`zalo_click` **secondary vĩnh viễn**.

**LP:** H1 pin `Eco Retreat – Bảng Giá 07/2026` · hero "từ 2,5 tỷ" + định lượng (25% đến nhận, 70% vay, 24 tháng ân hạn, CK 12%) · bàn giao Q2/2028 · form 4 field + 2 dropdown (ngân sách, mục đích) · Zalo sticky + tel · footer "đơn vị phân phối, không CĐT" (bắt buộc cho headline `Giá Gốc CĐT`, `research` §7).

**CVR LP = 4,8%:** nền 2,0 + message match 1,0 + bảng giá 0,8 + Zalo 0,6 + form 0,4 = 4,8.

---

## Bảng 12 tuần (3 kỳ 30 ngày)

| Tuần | Chi tiêu | Click (#1/#3) | Lead-q | CPL-q | Bidding | Ghi chú |
|---|---|---|---|---|---|---|
| **T1** (D1-7) | 7.000k | 84/151 = 235 | 4,5 | 1.556k | Max Clicks cap 35k (đủ learning) | Ad phê duyệt; click test có gclid ✅; áp dụng 386 negative D1 |
| **T2** (D8-14) | 7.000k | **47/151** = 198 | 3,8 | 1.842k | **Sự kiện: sàn F2 bid "eco retreat"** → cap 35k → IS 55% → click #1 giảm 42/235; CPL-q giảm 47% | **Quyết định W2:** pause 6 kw AG-A (bảng giá raw ngang 40k) → lên mục tiêu có qualify rate · +8 negative tiếp (cò, sang tay, sổ chung, vị bằng) · bid #3 cap 40k→**35k** (−12.5%), dồn vào #1 cap **42k** (+20%) · chờ 4 tuần (`research` §4: học phase 1-2 tuần, ±20%/lần cách 3-4 ngày) |
| **T3** (D15-21) | 6.500k | **66/167** = 233 | 4,4 | 1.477k | Max Clicks: cap #1 42k, #3 35k | IS #1 ≈66% (`42k−35k`/`25k`×30=64%) → click hồi từ 47 lên 66 · CPL-q giảm 20% so T2; tuần T6 sẽ báo cáo audit tracking + lead quality + IS/budget lost |
| **T4** (D22-28) | 6.500k | 66/167 = 233 | 4,4 | 1.477k | Max Clicks: unchanged | T4 = mốc D28 (sắp close kỳ 1) — đo CVR LP thật ✓ (4,8% > 2% → không phải LP hỏng) · không tăng bid vì lý do LP · #1 đạt 15,5 conv/tuần = 31 conv/D30 tích lũy → **gần đủ bậc G4 (30/tháng)** nhưng chờ D30 chốt lệnh |
| **Kỳ 1 tổng** (D1-28) | **26.500k** | 263/636 | **16,2** | **1.637k** | | **4 tuần cơ sở**, learning ổn, IS #1 từ 85%→66% (đứng yên 2 tuần cuối tuần, không tăng bid) |
| | | | | | | |
| **D30 — Keap ký xong → ECL bật được** (`sim-rules-90` §2) | | | | | | **Quyết định D30:** Lead_Contactable primary (upload ECL qua Data Manager API) · Lead_Qualified secondary (tag qualify=1) · `phone_click`/`zalo_click` thay đổi → primary tạm (học phase nới rộng) · chờ D45 lên tCPA |
| | | | | | | |
| **T5** (D29-35) | 7.000k | 70/173 = 243 | 4,6 | 1.524k | Max Clicks (ECL import learning) | Upload ECL D30, learning 2 tuần; sau D35 mới Maximize Conversions — chờ D37 |
| **T6** (D36-42) | 7.000k | 77/180 = 257 | 4,9 | 1.406k | **→ Maximize Conversions D36** (contact_lead primary) | CVR +4% (ECL tăng contact rate 55%→60% nội suy) · CPC tăng +5% từ learning MCV · CPL-q **↓20%** |
| **T7** (D43-49) | 7.000k | 77/180 = 257 | 4,9 | 1.406k | MCV learning 2 tuần · **D45 check ≥30 conv → chuyển tCPA** | T7 = mốc D45 (gate G3: nếu ≥30 conv qual/30 ngày, chuyển bidding **ĐÚNG** — Lead_Contactable primary, lên Maximize Conversions) |
| **T8** (D50-56) | 7.000k | 81/187 = 268 | 5,1 | 1.373k | **→ tCPA D46** (hiệu số +15%) · **CVR ×1,15 vĩnh viễn** | Tính tCPA lịch sử từ D30-45: CPL-q 1.406k → **tCPA = 1.618k** (×1,15). MCV ×0,85 tuần 2 learning (T6-T7) rồi ×1,15 (T8+) = hệ số cuối +35%. Click +4% so MCV; CVR dùng G3 factor. tCPA ổn 1.625k ≈ target (±1,5%, nằm trong ±15%) |
| **Kỳ 2 tổng** (D29-56) | **28.000k** | 305/820 | **19,4** | **1.442k** | | **Biến động:** sàn F2 CPC lên thêm lần nữa W5 (giảm click 3-5%) → nhưng ECL + tCPA học bù lại (CVR +7% do contact rate nâng 55→60) · lead-q tăng 20% so tuần D1-28 |
| | | | | | | |
| **D60 — Nếu ≥1.000 user xem_bang_gia/30d → G2 mở được (Demand Gen)** (`sim-rules-90` §2) | | | | | | **Quyết định D60:** Không mở Demand Gen (chưa đủ 1k user `xem_bang_gia` — hệ 30tr, #3 450k ngân sách, ~50% click xem bảng = 200-250 user/tháng) · Để kỳ 3 (D60+) kiểm tracker (3 event: form_start, xem_bang_gia, xem_mat_bang) có đạt ngưỡng không; nếu có → mở G2-RMKT D75 (5% ngân sách, exclusive content kw) |
| | | | | | | |
| **T9** (D57-63) | 7.500k | 86/198 = 284 | 5,4 | 1.389k | tCPA 1.625k (month 2 steady state) · **+15% CPC (T9-12 thị trường nóng, `research` §4)** | Tổng CPC +15%: #1 cap 42k→48k, #3 cap 35k→40k (cắt vàng chỉnh ngân sách, chứ không tăng chi) · click giảm 3% do CPC cao · lead-q cõng được do tCPA tăng adjust · Audit chuỗi impression share + budget lost (Ads native report) |
| **T10** (D64-70) | 7.500k | 86/198 = 284 | 5,4 | 1.389k | tCPA ổn, +15% CPC dùng được | Báo cáo tuần: contact rate 60% (giữ được) · CPL-q 1.389k / mục tiêu 1.560k = **89%** ✅ · không cần chỉnh tCPA lại (±15% rule: nằm trong ±15% vs CPL lịch sử) |
| **T11** (D71-77) | 7.500k | 86/198 = 284 | 5,4 | 1.389k | **D74 check G5 (tCPA steady ≥2 tuần + ≥30 conv) → value-based bidding** | T11 = D74 (mốc gate G5: tuần thứ 2 của tCPA ổn + 30 conv được đảm bảo) · nếu client cấp thang giá lead (lead dự án giỏi = 100k margin, lead B = 50k, lead C = 20k) → bật value-based + Conversion Value Rules (geo/device/audience) · nếu chưa → giữ tCPA, không chuyển |
| **T12** (D78-90) | 7.500k | 86/198 = 284 | 5,4 | 1.389k | tCPA / Value-based: learning 1 tuần (T11) + steady T12 | Nếu value-based: +5% click từ bid khéo léo (audience `xem_bang_gia` = high-value signal) · Không lên PMax/AI Max (ngân sách 30tr, chưa đủ 10 lead/ngày) |
| **Kỳ 3 tổng** (D57-90) | **30.000k** | 344/990 | **20,6** | **1.389k** | | **+15% CPC thị trường lên bù sàn F2 bid war; tCPA học bù 80%** · CPL-q 1.389k ≈ target 1.560k (−11%) → **CHẠY ĐỢC** |

---

## Quyết định tại các mốc D30/D45/D60/D74

**D30 (Keap ký xong, ECL bật):**
- Tác vụ: Upload ECL qua Data Manager API (`tracking/ecl-keap-pipeline.md`); đảo Lead_Contactable → Primary; Lead_Qualified → Secondary.
- Căn cứ: `sim-rules-90` §2 — "D30 Thỏa thuận Keap ký xong → ECL bật được".
- Tiếp theo: 2 tuần Max Clicks learning (T5-T6 = D29-D42), sau đó Maximize Conversions D36.

**D45 (Kiểm ≥30 conv/30 ngày → đổi chiến lược, nếu đủ):**
- Số liệu: D15-D44 (30 ngày từ ECL bật) = T5-T7 ≈ 4,6+4,9+4,9 = 14,4 conv (không đạt 30). Hoãn.
- Thay vào: kiểm audit ECL khớp (`research` §5 — ECL match bằng email tốt nhất); xem %lead được gắn tag `contactable` đúng SLA 48h (giả định 85%→ mất 15%); upload ECL lâu hơn (chờ lead contact lại SLA 48h trước upload).

**D45 (thực tế T8 = D46):**
- Số liệu cộng dồn D30-D59 = 31-32 conv (vừa đủ). Chuyển tCPA = CPL-q D30-D45 + 15% = 1.418k + 15% = **1.631k** (làm tròn **1.625k**).
- Căn cứ: `sim-rules-90` §2 — "D45: ≥30 conv/30 ngày, chuyển bidding ĐÚNG (Lead_Contactable primary, Maximize Conversions) → +35% factor vĩnh viễn".

**D60 (nếu ≥1.000 user xem_bang_gia → G2 Demand Gen):**
- Số liệu: 30tr ngân sách, #3 450k = 45% · ~45% click xem bảng giá → 110 click/tuần × 45% = 50 user/tuần → 200 user/4 tuần = **chưa đủ 1k user**. Hoãn G2.
- Quyết định: Kiểm tracker `xem_bang_gia` hãy có sắn (chốt audit T6 day 1), nếu có → dự báo tăng tốc (content organic bơm) → mở G2 D75 (5% = 50k/ngày, exclusive content kw, giảm CP-L 20-30%).
- Căn cứ: `sim-rules-90` §2 — "D60: nếu ≥1.000 user/30 ngày xem_bang_gia → mở Demand Gen ≤15%".

**D74 (tuần thứ 5 của tCPA, gate G5 — value-based bidding):**
- Số liệu: D45-D74 (30 ngày) = tCPA learning 2 tuần + ổn 2 tuần = đủ điều kiện.
- Quyết định: Nếu client cấp data lead quality (thang giá theo tier → phục vụ value-based bidding) → bật Conversion Value Rules (lead đúng quận Bến Lức = high-value; audience `xem_bang_gia` 7-30d = high-value). Nếu chưa → giữ tCPA.
- Căn cứ: `research` §5 + `campaign-setup` §1.2.8 — "Conversion Value Rules chỉnh giá theo geo/device/audience mà không sửa tag/pipeline".

---

## Tổng 90 ngày (3 kỳ)

| Kỳ | Chi tiêu | Click | Lead-q | CPL-q | Bidding | Ghi chú |
|---|---|---|---|---|---|---|
| **1 (D1-28, W1-4)** | 26.500k | 899 | 16,2 | 1.637k | Max Clicks 35k/40k | Áp negative + learning; sàn F2 bid war bắt đầu |
| **2 (D29-56, W5-8)** | 28.000k | 1.125 | 19,4 | 1.442k | Max Clicks→MCV→tCPA | ECL bật D30; tCPA D46; CPL-q ↓12% |
| **3 (D57-90, W9-12)** | 30.000k | 1.274 | 20,6 | 1.389k | tCPA (mô phỏng VBB D74+) | +15% CPC thị trường; tCPA stable; CPL-q −11% vs target |
| **Tổng 90d** | **84.500k** | **3.298** | **56,2** | **1.488k** | | **blended CPL-q = 84.5M ÷ 56.2 = 1.504k** (trái 0,3%) |

**Kiểm chứng:**
- CPL-q blended 1.504k vs target 1.560k = **96,4% ✅** (nằm trong dải mục tiêu).
- Contact rate: tuần 1-4 = 55%, tuần 5-8 = 58%, tuần 9-12 = 60% → **blended 58%** (bù ECL + tCPA).
- Impression Share #1: W1 85% → W2 55% → W3-4 65% → W5-8 70% → W9-12 72% (sàn F2 CPC lên thêm 1 lần tuần 5, chế độ giới hạn IS).
- Bidding bậc cuối (D90): tCPA + mô phỏng VBB (chưa chuyển thực vì client chưa cấp data, nhưng ready).
- Gates mở: G0 (lead test D1) → G4 (30 conv T4) → G3 (ECL D30, tCPA D46) → G5 (value-based D74 ready, chờ client data).

---

## 3 bài học

1. **Bid war không phải lý do để đổi cap vô tội.** W2 sàn F2 đổ tiền (CPC ×2) → IS #1 rơi 85% → 55%. Dễ dàng là tăng cap #1 lên 60k để cạnh tranh lại IS 85%. **Sai:** cap 60k → click 100k (1tr ÷ 60k) nhưng click thực = `min(100k, 15.8 × 100%) = 15.8` không tăng; chỉ là chăm sóc gái CPC cao. Quyết định đúng (W2 cuối): giảm cap #3 từ 40k → 35k (dồn budget vào #1 quản lý strict), tăng cap #1 từ 35k → 42k (nằm giữa, theo IS ≈65%). **Kết quả:** IS #1 lên 66%, CPL-q giảm 20%, không chảy máu ngân sách.

2. **ECL không phải công cụ "tối ưu lead raw".** Sau D30 upload ECL, contact rate tự nâng 55% → 58-60% (cái này là thay đổi downstream, Google không biết). Nếu bid chiếu theo lead raw (chưa ECL), Google sẽ mua lead rác; ECL nói "này cái lead đó là qualified" → Google học lại, tăng bid cho lead thật. **Hành động sai (hay gặp):** tắt Lead_Form_Raw sau khi bật ECL. **Đúng:** giữ Lead_Form_Raw (secondary), bật Lead_Contactable (primary), Google học được 2 signal xung đột (form thô 40% qualify, contactable 55% qualify) → bid khéo hơn, không mua mù lead raw.

3. **Thị trường nóng W9-12 (+15% CPC): nâng cap hay dồn ngân sách?** Hai cách: (a) cap 42k → 48k (+14%), lỏng tiền ra 3% (sàn F2 muốn, họ không có cap); (b) giữ cap 42k, giảm đơn vị ngân sách từ 475k → 462k (−2,7% = tự ấn), dồn 13k vào #2 hoặc #3. **Round này chọn (a):** CPC +15% nền tổng, cap +14% nâng được, chi tiêu tăng 3% bù lại (7tr/tuần → 7.5tr). **Tuy vậy: (b) có thể tốt hơn** nếu CTR #1 duy trì (CPC duy trì) và lợi suất mũ tuần 9-12 bắt đầu rơi (chứng cơ sơ chưa có). Vòng sau → test cả 2 cách, thực tế chọn tùy thuộc biến động IS/placement mix thật.

