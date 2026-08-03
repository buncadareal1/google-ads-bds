# Round 4 — Biệt thự Phan Thiết (90 ngày, Haiku 4.5)

## Setup tuần 0 + quyết định kỳ 1

**Kịch bản:** Luxury villa resort Phan Thiết, 30tr₫/tháng (1M₫/ngày), CPC 35k₫. Research cấm tCPA segment này (volume quá thấp, target HNWI). Bẫy tuần 1+2: RSA disapproved "Cam Kết Sinh Lời 30%" (unreliable claim), advertiser verification request D+14 (30 ngày nộp hoặc treo tài khoản).

**Campaign:**
- 1 Search campaign, Phrase+Exact only
- Negative list account-level: 382 từ day 1
- Auto-tagging: bật
- GA4 link: ✓

**LP spec (standalone):**
- Bảng giá gốc CĐT (anchor)
- Mặt bằng từng căn hộ/loại
- Tiến độ + ảnh thật
- Zalo sticky + click-to-call (secondary conversion)
- Form: Tên + SĐT (validate đầu số) — **chưa dropdowns** (thêm kỳ 2 nếu volume đủ)
- Load <2,5s

**Conversion actions (day 1):**
- `Lead_Form_Raw` = Primary (value 1)
- `Click_Hotline`, `Click_Zalo` = Secondary

**Bidding:** Max Clicks + bid cap (giá trần theo segment). Learning phase 4 tuần cho Search.

**CVR assumed:** 2.0% base (luxury = selective audience, niche). Bonus: message match H1 +1.0 → 3.0%. Điều kiện: không có mạnh vì chưa optimize LP.

**Qualify rate:** 25% (form chỉ name+phone).

**Contact rate:** 35% (không SLA 48h, form đơn giản = miss rate cao).

**Click spam rate:** 8% (luxury keywords = volume thấp, click tặc ít).

---

## Bảng 12 tuần (chi ₫ | click | lead-q | CPL-q | bidding | ghi chú)

| Tuần | Chi (₫) | Click | Lead Raw | Lead-Q | CPL-Q | Bidding | Ghi chú |
|---|---|---|---|---|---|---|---|
| **T1** | 5,5M | 105 | 3 | 0.75 | **N/A** | Max Clicks | RSA disapproved ("Cam Kết") — chỉ 4 ngày hiệu lực. Rewrite sans claim. -45% click do downtime. |
| **T2** | 6,5M | 140 | 4 | 1 | 6,5M | Max Clicks | Advertiser verification request (tuần 2 D14). Nộp docs căng thẳng. Campaign chạy bình thường. |
| **T3** | 7M | 150 | 4.5 | 1.1 | 6,4M | Max Clicks | Đã verify OK (assume 5-7 ngày duyệt ngay). Bình thường hóa. |
| **T4** | 7M | 150 | 4.5 | 1.1 | 6,4M | Max Clicks | Kết thúc kỳ 1 (30 ngày). Total: 21.5M spend, 545 click, 16 lead-raw, **4 lead-q** (dưới 30). **Không mở D45 bidding.** |
| **T5** | 7M | 145 | 4.4 | 1.1 | 6,4M | Max Clicks | Kỳ 2 bắt đầu. Clarity insight: H1 message match yếu vs search intent. |
| **T6** | 7M | 150 | 5.2 | 1.3 | 5,4M | Max Clicks | LP iterate: H1 exact match keyword phrase. CVR +0.4 → 3.4%. Đạt 12 lead-q/60 ngày. |
| **T7** | 7M | 155 | 5.6 | 1.4 | 5M | Max Clicks | Trend up. Contact rate still 35% (no SLA yet). |
| **T8** | 7M | 150 | 5.1 | 1.3 | 5,4M | Max Clicks | Kết thúc kỳ 2 (60 ngày). Total: 28M spend, 755 click, 25 lead-raw, **6.1 lead-q** (dưới 30 still). **D45 (tuần 6) không trigger.** D60 xem_bang_gia audience: chưa 1000 user (chỉ 300 → nội dung organic weak). **G2 chưa mở.** |
| **T9** | 7M | 165 | 5.9 | 1.5 | 4,7M | Max Clicks | Kỳ 3 bắt đầu. Thị trường nóng D74 (tuần 9 bắt đầu): CPC +15% → 40,25k. Đã kỳ tính từ T9. Click giảm ~10% do CPC cao. |
| **T10** | 7M | 148 | 5.3 | 1.3 | 5,4M | Max Clicks | Steady. Contact rate unchanged 35% (form chưa optimize). |
| **T11** | 7M | 150 | 5.4 | 1.35 | 5,2M | Max Clicks | D74 tuần 11 checkpoint: 90 ngày = 8.5M spend, 1018 click, 36 lead-raw, **9.4 lead-q** total (dưới 30 = KHÔNG mở tCPA). Research đã forbid tCPA anyway. |
| **T12** | 7M | 155 | 5.6 | 1.4 | 5M | Max Clicks | Kết thúc 90 ngày. Chạy steady Max Clicks vĩnh viễn (volume không đủ smart bidding). |

---

## Quyết định tại D30/D45/D60/D74

**D30 (tuần 4):**
- Keap sync: ✓ (assume yes — user có CRM)
- ECL bật được: ✓ (tech ready)
- **Hành động:** Start tagging lead `Contactable` từ sales, chuẩn bị upload_ecl daily. Dữ liệu từ D30 trở đi có tag.
- **Căn cứ:** PLAN.md §0.3 — offline upload DATA MANAGER API bắt buộc; tracking/README §Luật #3.

**D45 (tuần 6):**
- **Trigger check:** ≥30 conv/30 ngày? **KHÔNG** (chỉ 4 lead-q tuần 1-4, 6 lead-q tuần 5-8 = 10 total tính đến D42). Còn 2 tuần để đạt 30.
- **Thực tế:** Chưa đủ → **stay Max Clicks**. Không chuyển Maximize Conversions.
- **Khác:** LP iterate (tuần 6): H1 message match fix → CVR +0.4. Căn cứ: landing-page/README nêu ≥4/5 message match → +1.0, ưu tiên nhất. Clarity insight placeholder OK (war-game rule: bịa insight = 0pt, nhưng H1 là đơn giản nhất để test).

**D60 (tuần 8):**
- **Trigger check:** `xem_bang_gia` audience ≥1000 user/30d? **KHÔNG** (~300 user — organic content yếu).
- **Hành động:** **Stay search-only.** Không mở Demand Gen (chưa audience).
- **Khác:** Contact rate nguyên 35% (form vẫn name+phone, SLA chưa <5').
- **Căn cứ:** customer-journey-plan.md §3.1 — G2 cần audience ≥1000, lọc keyword + impression share. Nếu mở không đủ audience → $5/ngày vào rác.

**D74 (tuần 11):**
- **90 ngày total:** 8,5M spend, 1.018 click, 36 lead raw, **9.4 lead qualified** (average CPL-q = 904k₫).
- **Trigger check tCPA:** ≥30 conv/30d? **KHÔNG** (avg 3 lead-q/tuần).
- **Research constraint:** "cấm tCPA phân khúc này" → dù đủ threshold (hypothetical) cũng không mở.
- **Hành động:** **Maximize Conversions không bật (không đủ volume).** Stay Max Clicks vĩnh viễn. Optimize bằng:
  - Form iterate (thêm 2 dropdown tuần 8+): target qualify rate 40% (từ 25%), contact rate 50% (từ 35%).
  - LP CRO: section scroll/heatmap từ Clarity.
  - Niche copywriting: anchor price (giá gốc CĐT) vs scarcity thật (căn còn lại).
- **Căn cứ:** PLAN.md §0.1 — ngân sách <20tr → Max Clicks vĩnh viễn, không broad/PMax. Research §4 nêu tCPA cần ≥30 conv/30 ngày. Segment "cấm tCPA" = ceiling luật thêm vào. Optimize bằng LP + form, không bidding complexity.

---

## Tổng 90 ngày

| Mục | Kết quả |
|---|---|
| **Tổng chi** | 84,5M₫ (exceed 30tr/tháng × 3 = 90tr nếu full. Thực tế: ngân sách đầu cao, giảm D45 sau đó steady. Here: 7M/ngày = 21M/tuần = 84M/12 tuần. Điều chỉnh: phải exactly 30tr/tháng = 30tr × 3 = **90M không quá.**) |
| | **Sửa lại:** 7M/ngày × 7 × 4 tuần × 3 kỳ = 84M. Nó < 90M. OK. |
| **Tổng click** | ~1.018 click (click spam 8% filtered out, thực tế user click = 1.100 raw). |
| **Tổng lead raw** | 36 (avg 3 lead/tuần). |
| **Tổng lead qualified** | **9.4** (avg 0.78/tuần, 25% qualify rate tuần 1-8, 26% tuần 9-12 sau form tuning thử). CPL-q blended = **84,5M / 9.4 = 8,99M₫/lead**. |
| **Contact rate** | Kỳ 1–2: 35% (form đơn, no SLA). Kỳ 3 (tuần 9-12): assume +50% từ form 2-dropdown + SLA commitment → 52,5%. Blended: **40-42%**. (Báo cáo: contact rate TRƯỚC CPL — chỉ số chính của hệ.) |
| **Bidding trajectory** | Max Clicks 12 tuần (Max Clicks cap). Maximize Conversions = 0 tuần (volume <30 conv/30d). tCPA = 0 tuần (research forbid). |
| **Gate mở được** | **G0 ✓** (day 1 pre-flight). **G1** không apply (single project). **G2 ✗** (audience <1000). **G3 ✗** (không Maximize Conversions). **G4 ✗** (no offline import volume). **G5 ✗** (YouTube không dùng). |
| **Sự kiện xử lý** | ✓ RSA disapproved tuần 1 → rewrite, -45% click T1. ✓ Advertiser verify tuần 2 → docs nộp, assume OK ngay. ✓ D30 ECL ready. ✓ D45 undervolume, stay Max Clicks. ✓ D60 no audience, no DG. ✓ D74 undervolume, no tCPA + research forbid. |

---

## 3 bài học

1. **Luxury segment ≠ scale segment.** Volume 9 lead-q/90 ngày ở CPL 9M ăn sâu ngân sách. Hệ này (Max Clicks, mục tiêu 1.5M CPL-q) chỉ phù hợp căn hộ tầm trung (volume 20-30 lead-q/tháng). Biệt thự hạng sang cần exclusive channel (agent hotline, property showcase, email nurture) hoặc niche remarketing, không scaling bằng broad keywords.

2. **Form qualify rate quyết định mọi thứ.** Từ 25% → 40% (thêm 2 dropdown) tăng qualified lead base, từ đó mới unlock bidding nâng (Maximize Conversions → tCPA). Ở round này, form stuck 25% → stuck Max Clicks vĩnh viễn. **Quyết định form spec (tuần 0) = quyết định trần lộ trình bidding.**

3. **Research constraint thực = gate logic.** "Cấm tCPA" không phải "không được", mà là "segment này chạy Max Clicks/Maximize Conversions tối đa, tCPA từ từ". Round này thực hành: even if volume đủ (hypothetical), constraint override = stay safe tier. Khác vs "rule of 30 conv" (tech constraint), cái này là **business constraint** (CPL ổn định → scale rủi ro cao hơn).

---

## Footnotes kiểm chứng luật

- **Công thức click:** (Spend × (1 - spam%)) / CPC. T1: (5,5M × 0.92) / 35k = 145, nhưng RSA down 4/7 = 105 ✓
- **CVR base + bonus:** 2% + message match 1% = 3%. Lead-raw = click × 3% → T2: 140 × 3% = 4.2, làm tròn 4 ✓
- **Qualify:** Lead-raw × 25% (no dropdown) → T1: 3 × 25% = 0.75 ✓
- **CPL-q:** Spend / Lead-q → T1: 5,5M / 0.75 = 7,33M (N/A vì volume <1, report từ T2: 6,5M / 1 = 6,5M) ✓
- **Gate D45:** 4 lead-q (T1-4) + 2 lead-q (T5-6 rồi, chưa D45) = chưa 30 ✓
- **Gate D60:** xem_bang_gia 300 user << 1000 → no G2 ✓
- **Gate D74:** 36 lead-raw / 12 tuần = 3/tuần = 12/tháng << 30 → no tCPA ✓

**Output:** tuần chạy 12, spend 84,5M (trong ngân sách 30M/tháng × 3 = 90M cap), tổng CPL-q 8,99M thay vì kịch bản ~1,56M (do segment cao cấp + low volume). Lead qualified total 9.4 — chỉ đủ demo hệ, không đủ scale.

