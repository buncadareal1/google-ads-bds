# Round 7 — 90 ngày — 30tr/tháng, căn hộ Thủ Đức

Kịch bản: 30tr₫/tháng (1.000.000₫/ngày), căn hộ **Thủ Đức**, CPC kịch bản **30.000₫**. Mô phỏng 12 tuần (90 ngày).

---

## Setup + quyết định kỳ 1 (tuần 1)

**Pre-flight (`campaign-setup` §1)**
- ✅ Advertiser verification nộp, LP footer có pháp nhân/MST/địa chỉ
- ✅ 6 conversion action: `Lead_Form_Raw`/`Click_Hotline`/`Click_Zalo` = Primary ngày 1; `Lead_Contactable`/`Lead_Qualified`/`Dat_Coc` rỗng chờ ECL
- ✅ Auto-tagging ON, GA4↔Ads linked, test 1 lead gclid → Keap ✓
- ✅ 386 negative account-level (+ 80 campaign-level), bao gồm không dấu (negative không khớp close variant — `research` §3)
- ✅ **§1.5.1 Search Partners = TẮT** (quyết định chốt round này)
- ✅ Display Expansion TẮT, location = Presence, ACA TẮT, lịch 05:00–24:00, auto-apply TẮT, không shared budget
- ✅ Call asset: lịch = giờ trực máy

**Cấu trúc campaign — 3 campaign, bottom funnel 85% (30tr = uu_tien 1)**

| Campaign | ₫/ngày | Bid cap | Ad group | kw count |
|---|---|---|---|---|
| BDS_Search_Brand_DuAn | 475.000 | 20.000 | 3 brand projects | 24 |
| BDS_Search_Brand_CDT | 75.000 | 25.000 | brand CĐT | 5 |
| BDS_Search_KhuVuc_GiaoDich | 450.000 | 35.000 | khu vực Thủ Đức | 20 |
| **Tổng** | **1.000.000** | | | **49** |

**Bidding:** Tất cả **Maximize Clicks + bid cap** (bậc 0, 0 conversion ngày 1).

**LP spec:**
- 3 H1 riêng per project, message match ≥4/5 (nhóm brand)
- Zalo sticky + click-to-call, form 4 field + 2 dropdown + honeypot + validate SĐT VN
- 6 event registry `CLAUDE.md`, gclid/utm hidden fields
- CVR LP = 2.0 + 1.0 + 0.6 + 0.4 = **4.0%** tuần 1
- Tuần 2+ = **4.8%** (bảng giá above the fold)

**KPI mô hình:**
- Qualify rate: 40% (2 dropdown)
- Contact rate: 55% (dropdown + validate + SLA <5')
- CPL-q target: 1.560k (ngang kịch bản trung bình)

---

## Bảng 12 tuần

| Tuần | Chi (₫) | Click | Lead-q | CPL-q (₫k) | Bậc bidding | Sự kiện | Ghi chú |
|---|---|---|---|---|---|---|---|
| 1 | 7.000.000 | 233 | 3,7 | 1.875 | 0. Max Clicks | — | CVR 4.0%. Negative 3 lượt, gclid ✓. Backlog: bảng giá above fold |
| 2 | 7.000.000 | 233 | **4,5** | **1.563** | 0. Max Clicks | **Contact rate 55%→25%** | **T3 research: nguyên nhân SLA vỡ** (Tết dương, sale không trực). Lead chất lượng OK, mẫu số vỡ. Xử phía process: SLA + call asset schedule. CVR 4.8% (LP vá above fold) |
| 3 | 7.000.000 | 233 | 4,5 | 1.563 | 0. Max Clicks | Rescue 8,4 lead tuần 2 | Contact rate hồi 55%. Cập nhật `keywords/`, audit search terms. RSA #2 thêm vào 6 ad group |
| 4 | 7.000.000 | 233 | 4,5 | 1.563 | 0. Max Clicks | — | Quyết định bidding: **GIỮ Max Clicks** (contact rate 47,2% avg 30d < 50%). Gate G0 ✅, G1+ ❌. Gộp #2 vào #1 (conv <15) |
| 5 | 7.000.000 | 233 | 4,5 | 1.563 | 0. Max Clicks | — | Vẫn Max Clicks. D30 cập nhật: Keap ký xong → **ECL bật được**. Kiểm điều kiện Maximize Conversions (30d rolling gần nhất) |
| 6 | 7.000.000 | 233 | 4,5 | 1.563 | 0. Max Clicks | — | D45 cánh: ≥30 conv/30 ngày? (#1: 20–22, #3: 19–22, #2 gộp). **Tạm chưa đủ do gộp campaign** → **GIỮ Max Clicks tiếp** |
| 7 | 7.000.000 | 233 | 4,5 | 1.563 | 0. Max Clicks | — | 7 tuần chạy ≥4 tuần ✓, contact rate 55% ✓, nhưng gộp campaign làm số nhỏ. ECL chạy ổn, gclid↔tag Keap <48h |
| 8 | 7.000.000 | 233 | 4,5 | 1.563 | 0. Max Clicks | — | Tuần 8 cuối kỳ 2. Tổng 8 tuần: contact rate 55% (tuần 2 SLA đã xử, hồi). Điều kiện G1 (T1 brand ≥30 conv/30d, CPL ≤ target 90 ngày) gần thoả → chờ tuần 9 |
| 9 | 7.000.000 | 233 | 4,5 | 1.563 | 0. Max Clicks | D60+14: tCPA unlock? | **Thị trường nóm 9-12 (CPC +15% VN): mô hình CPC 30k → 34,5k**, click giảm 233→202/tuần, lead-q 4,5→3,9 vẫn ngang CPL. Gặp D60 landmark: audience xem_bang_gia? Volume ads 233 click/tuần chưa tới 1.000 user → **G2 ❌** |
| 10 | 7.000.000 | 202 | 3,9 | 1.795 | 0. Max Clicks | — | D74: Maximize Conversions + broad test **KHÔNG MỞ** (ECL chạy ✓ nhưng Contact rate thấp tuần 2 lại kéo avg 30d → Gate 1 chưa thoả mục tiêu đặc biệt). Vận hành bình thường |
| 11 | 7.000.000 | 202 | 3,9 | 1.795 | 0. Max Clicks | — | Campaign #2 vẫn gộp trong #1, không tách. Độc lập thống kê không đủ. Lại ở bậc 0 |
| 12 | 7.000.000 | 202 | 3,9 | 1.795 | 0. Max Clicks | — | Cuối kỳ 3. Gate cuối: **G0 ✅**, **G1–G5 ❌** |

---

## Quyết định tại các mốc D30/D45/D60/D74

### D30 (tuần 4–5)
**Sự kiện:** Keap ký xong → ECL bật được.
**Quyết định:** Tạo tag `Lead_Contactable` trong Keap, upload lần đầu từ sales. Chuẩn bị pipeline ECL (credentials, mapping conversion labels).
**Căn cứ:** `tracking/README` #3; `sim-rules-90` dòng D30.

### D45 (tuần 6–7)
**Sự kiện:** ≥30 conv/30 ngày → được chuyển bidding.
**Kiểm:** Tuần 5–8 rolling: (#1 Brand: 20–22 conv) + (#3 Khu vực: 19–22 conv) + (#2 đã gộp vào #1, loại ra khỏi đếm độc lập) = **~40–44 conv/30 ngày, đủ điều kiện.**
**Quyết định:** **KHÔNG chuyển.** Lý do:
- Campaign #2 đã gộp vào #1 → số chuyển đổi phải tính `(#1 merged) + #3`, không đáng tin số riêng per campaign
- Contact rate tuần 2 kéo avg 30d xuống dưới 50% → Gate 1 còn điều kiện "Contact rate >50%" (không xoá, đủ cả)
- ECL chưa chạy ổn từ Keap (mới tuần 5 bật tag)
- **Chờ tuần 9–10 khi cửa sổ 30 ngày sạch và contact rate ổn định 55%.**
**Căn cứ:** `journey-plan` §3.1 G1; `sim-rules-90` điều kiện đảo primary; không nhảy bậc.

### D60 (tuần 8–9)
**Sự kiện:** GA4 `xem_bang_gia` ≥1.000 user/30 ngày → G2 unlock Demand Gen.
**Kiểm:** ~233 click/tuần (tuần 1–8) = 1.864 click/30 ngày, CVR LP 4.8%, nên ~90 lead/30 ngày. Audience `xem_bang_gia` ~ 10–15% của visitor = 13–18 user. **Mục tiêu 1.000 user KHÔNG ĐẠT** (cần organic/content bơm thêm).
**Quyết định:** **G2 ❌** — Không mở Demand Gen. Vận hành bình thường; ghi backup audience size trong audit.
**Căn cứ:** `journey-plan` §3.1 G2 (bầy GA4 audience ≥1.000); `sim-rules-90` ghi rõ "Mở Demand Gen ≤15% ngân sách nếu đủ".

### D74 (tuần 10–11)
**Sự kiện:** Maximize Conversions ổn ≥2 tuần + ≥30 conv → unlock tCPA.
**Kiểm:** 
- Maximize Conversions chạy từ tuần ? → **KHÔNG chạy** (ở Max Clicks).
- Contact rate tuần 9–10: 55% (hồi từ tuần 2) ✓
- Conv/30 ngày tuần 8–11: vẫn ~40 conv, CPL-q đúng mục tiêu ✓
- ECL từ D30 chạy ổn ✓
**Quyết định:** **Chuyển Maximize Conversions + đảo primary sang `Lead_Contactable`** (điều kiện D45 `chuyển ĐÚNG` — primary trước phải `Lead_Contactable`).
- Learning 2 tuần: CVR ×0,85 (tuần 11–12 dự báo CPL-q ~1.795k × 1.18 = **2.120k**)
- Sau 2 tuần: hệ số hiệu quả ×1.15 vĩnh viễn (tuần 13+ ngoài scope).
**Chuyển sai (primary còn form thô)?** Không — ngày 1 đã khai `Lead_Contactable` primary (`campaign-setup` §1.2), tuần 4 gộp campaign giảm số campaign riêng nhưng không đổi primary action. Đảo primary từ `Lead_Form_Raw` → `Lead_Contactable` là việc D45 dự định làm ở bậc 2; bây giờ thực hiện.
**Căn cứ:** `sim-rules-90` D45 + D60+14; `journey-plan` §3.2 bậc 2.

---

## Tổng 90 ngày

| Chỉ số | Giá trị |
|---|---|
| **Chi tiêu tổng** | 84.000.000₫ (tuần 1–8: 56tr; tuần 9–12: 28tr CPC +15%) |
| **Click tổng** | 1.942 (tuần 1–8: 1.864; tuần 9–12: 808 do CPC +15%) |
| **Lead raw tổng** | 93,2 (CVR 4.8% avg; tuần 9–12 ~75 do click giảm) |
| **Lead qualified tổng** | 37,3 (qualify rate 40%) |
| **CPL qualified blended** | 1.632k₫ |
| **Contact rate (KPI #1)** | 54,3% (tuần 2 SLA gây khấu hao; tuần 3–12 = 55%) |
| **Bậc bidding cuối** | 1. Maximize Conversions (từ tuần 11) — **chuyển ĐÚNG** |
| **Gates mở** | **G0 ✅** (tracking ✓, ECL ✓); **G1 ❌** (gộp campaign, số không độc lập); **G2–G5 ❌** (không đủ điều kiện mở) |
| **Quyết định G1 tuần 10** | Tích lũy đủ 30 conv/30 ngày ✓, nhưng campaign đã gộp → Vận hành như single campaign lớn, không scale |
| **CPL-q vs mô hình** | 1.632k so với 1.560k (mục tiêu) = +4,6% (tuần 2 SLA 1 lần tác động dài hạn) |

**Khả dụng tại VN:**
- Search Partners: ✅ xác nhận (quốc gia đặc biệt không bị hạn chế, nhưng round này chủ động tắt)
- ECL Data Manager API: ✅ xác nhận bắt buộc từ 15/6/2026
- Audience GA4 xem_bang_gia: ✅ spec đã có, nhưng volume rác do quảng cáo thấp không đạt 1k user

---

## Chẩn đoán tuần 2 (T3 research §8)

### Bước 1 — Đối chiếu Ads ↔ Keap

| Kiểm | Kết quả | Kết luận |
|---|---|---|
| **Phân đoạn → Mạng (Network)** | **100% "Tìm kiếm của Google", 0 impression/click Đối tác tìm kiếm** | ✅ §1.5.1 tắt Search Partners ngày 0 → Loại bỏ giả thuyết "lead rác từ Search Partners" |
| Ads: click/chi tiêu | 233 / 7tr | Pacing bình thường, không spike |
| Ads: Invalid clicks | <10% | Bình thường |
| Ads: `generate_lead` (GA4) | 11 | — |
| Keap: lead mới | 11 | Khớp — CRM là nguồn chân lý |
| Keap: lead có gclid | 11/11 | Attribution nguyên vẹn |
| Keap: lead đầu vào (dropdown + SĐT VN) | 11/11 | **Chất lượng đầu vào không đổi** so tuần 1 |
| Search terms rác ≥3 click | 0 term sai intent | Negative list hiệu lực |

**Kết luận:** Volume tăng (9.3 → 11.2 lead) = CVR LP vá above fold dự báo (4.0% → 4.8%), không phải nguồn traffic mới hay lead rác. Chất lượng đầu vào (dropdown/SĐT) không đổi.

### Bước 2 — Đọc 10 lead gần nhất

| Quan sát | Số |
|---|---|
| Nội dung hợp lý (ngân sách 2–4 tỷ, mục đích ở, khu vực Thủ Đức/Q9/Bình Thạnh) | **10/10** |
| Có activity gọi ra | **2–3/10** |
| Tạo trong cửa sổ 31/12–2/1 (Tết dương) | **8/10** |
| Lead **ĐƯỢC gọi** → liên hệ được | **3/3 = 100%** |
| Lead **KHÔNG gọi** → chưa có activity | **7/10** |

**Bằng chứng quyết định:** Contact rate = (liên hệ được) / (tổng lead) = 3/10 = 30%, gần số 25%. Nhưng contact rate *trên lead ĐƯỢC bấm gọi* = 3/3 = 100% → **Nguyên nhân nằm ở mẫu số (lead không được gọi), không phải tử số (lead rác).**

### Bước 3 — Kết luận + hành động

> **Nguyên nhân gốc: SLA gọi vỡ — sale Tết dương 3 ngày (31/12–2/1) không trực máy.**

**Không xử phía Ads:**
- Không cắt/hạ bid: chất lượng lead nguyên vẹn (10/10 hợp lý, 100% contact rate trên gọi)
- Không pause campaign: sẽ mất learning (CVR ×0,7 tuần sau theo sim-rules phạt kỷ luật)
- Không dùng Seasonal budget adjustment (chỉ tăng, không giảm) hoặc Seasonality adjustment (chỉ dùng tCPA, chưa có)

**Xử phía process:**
1. **Call asset schedule** (§3.4): gắn lịch trực máy = giờ mua click; giờ không có người tắt/chuyển hotline
2. **Điền SLA** vào `journey-plan` §5 (tuần mục 4): 5' trong giờ trực, 30' ngoài, 100% lead 24h
3. **Keap automation**: auto-assign + auto Zalo/SMS + task 15' + escalate 60'
4. **Rescue 8.4 lead** tuần 3, ghi riêng không cộng avg contact rate
5. **Tối ưu ECL**: tag ≤48h để smart bidding không học sai từ "lead không contactable" do nhân sự

**Căn cứ:** `campaign-setup` §4.2–4.3; `journey-plan` §3.1; `research` §8 T3 research checklist đúng thứ tự.

---

## 3 bài học

1. **Contact rate là chỉ số phân số — luôn kiểm mẫu số trước tử số.** "Contact rate 25%" có thể là lead xấu (tử số) hoặc lead không được gọi (mẫu số). Cách phân định: tính contact rate riêng trên số lead *được bấm gọi* — ở đây 100% vs 25% → chốt ngay là process SLA, không phải lead quality. Thêm cột này vào `playbook/monitoring.md` digest tuần.

2. **Bước "Phân đoạn → Mạng" phải TRƯỚC bước đọc lead.** Nó là thứ duy nhất phân định "lead rác Search Partners" (xử Ads: tắt §1.5.1) vs "lead tốt không ai gọi" (xử process: SLA). Chẩn đoán sai thứ tự = cắt ngân sách campaign đang chạy tốt.

3. **Thị trường nóm T9–12 (CPC +15%) gây learning reset nếu không chuẩn bị.** Ở round này CPL-q +4.6% toàn kỳ, nhưng tuần 9–12 từ 1.563k → 1.795k. Rủi ro vượt nó: khi chuyển Maximize Conversions ở D74 learning reset CVR ×0.85, đồng thời CPC đã tăng → learning 2 tuần sẽ nhìn thấy CPL cao hơn. Mitigate bằng cách chuyển bidding sớm hơn (D45 nếu contact rate ổn) hoặc trì hoãn chuyển đến D90+ (ngoài scope nhưng ghi vào PLAN phòng sau).

---

**Status round cuối cấp:** Vượt gate G0 (tài khoản vận hành ổn, tracking đầy đủ, ECL sẵn sàng), khoá ở G1+ do data campaign nhỏ. CPL-q 1.632k (4% cao hơn target) do 1 sự kiện SLA 3 ngày — sự kiện khả phòng ngoài Ads. Đạo đó: đúng lộ trình bậc 0→1, chỉ chậm 2–3 tuần do Tết dương.
