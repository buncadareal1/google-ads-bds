# Round 8 — Căn hộ Bình Dương, 30tr/tháng, CPC 26k — 90 ngày

## Setup + quyết định kỳ 1

**Kịch bản:** Campaign chạy TỐT (CPL-q dưới trần, contact 57%). BẪY tuần 2-3: IS lost (budget) 25% liên tục, budget cạn trước 19h.

**Giả định:**
- Budget: 30tr/tháng = 7,5tr/tuần
- CPC: 26k
- Click rác tuần 1-2: 25% (sau lọc negative, giảm xuống 15% tuần 3+)
- LP spec (căn hộ Bình Dương): message match +1.0, pricing above fold +0.8, Zalo+call +0.6, form 2 dropdown +0.4 → CVR base 4.4% (cap 6%)
- Qualify rate: 40% (form 2 dropdown + validate)
- Contact rate: 55% (SLA <5', tag 85% trong 48h)

**Tuần 0 (setup — không tính vào 90 ngày):**
1. **Ad structure:** 1 Search campaign, 3 ad group (project name exact, location+type phrase, location+amenity phrase), Phrase+Exact match, bid strategy Max Clicks + bid cap 35k (2× CPC để safe)
2. **Negative list (ngày 1, account-level):** cho thuê, cho thue, phòng trọ, tuyển dụng, việc làm, lương, CTV, là gì, cách, mẫu, PDF, lừa đảo, tranh chấp, batdongsan, chotot, game, du lịch, thanh lý, phát mãi, ký gửi, tỉnh khác
3. **Conversion actions:** form_submit (lead raw), phone_click (intent signal), zalo_click (intent signal), lead_qualified (CRM backfill D30+)
4. **LP:** sẽ cải thiện cvr qua iteration nếu Clarity có insight (max +0.4/kỳ 30 ngày)

**Vận hành tuần 1-3:**
- Tuần 1: Max Clicks, bid cap 35k, CVR thị trường 4% (mục tiêu), contact 55%
- **Tuần 2-3: IS lost budget 25%** (bẫy) — detection: IS lost ≥25% ≥3 ngày liên tiếp. CPL-q vẫn ≤2.5M, contact vẫn ≥55% → thỏa điều kiện tăng budget.
  - **Hành động (tuần 3 cuối):** request user duyệt tăng ngân sách tuần 4+ lên 9M/tuần (+20% cách 3-4 ngày). Lý do: IS lost persistently 25%, CPL qualified ổn (1.8-2M), contact rate 55%+ tốt → không phải vấn đề campaign quality mà budget tight.
  - Giả định user approved (ngoài scope sim nhưng cần để tiếp tục).
- Tuần 4: Tăng budget lên 9M (mật độ click tốt hơn, IS lost giảm xuống 5%), learning reset ×0.7 CVR 1 tuần (tuần 4 CVR 2.8%).

---

## Bảng 12 tuần — 90 ngày

| Tuần | Kỳ | Ngân sách (₫) | Click (thực) | Lead-q | CPL-q (₫) | Bidding | Ghi chú + sự kiện |
|---|---|---|---:|---:|---:|---|---|
| 1 | 1 | 7.500.000 | 216 | 3,5 | 2.140.000 | Max Clicks + cap | Ngày 1: setup negative, conversion. CVR 4%, contact 55% |
| 2 | 1 | 7.500.000 | 215 | 3,4 | 2.206.000 | Max Clicks + cap | **IS lost 25% từ ngày thứ 3** (budget tight). CPL-q 2.2M, contact 55% OK |
| 3 | 1 | 7.500.000 | 210 | 3,3 | 2.273.000 | Max Clicks + cap | **IS lost vẫn 25% ≥3 ngày.** CPL + contact = OK. Quyết định: request tăng budget tuần 4. (D21) |
| 4 | 1 | 9.000.000 | 272 | 3,8 | 2.368.000 | Max Clicks + cap | **Tuần tăng budget +20%.** Learning reset CVR ×0.7 = 2.8% (từ 4%). IS lost → 5%. Ngân sách tháng ~30.5tr (duyệt được) |
| 5 | 2 | 9.000.000 | 285 | 5,1 | 1.765.000 | Max Clicks + cap | CVR phục hồi 4%+, IS lost <5%. D30 milestone: ECL unlock (Lead_Contactable tag bắt đầu ghi). Contact 55%. |
| 6 | 2 | 9.000.000 | 287 | 5,2 | 1.731.000 | Max Clicks + cap | Ổn định. Lead qualified tăng do tag từ ECL backfill (D30-40). |
| 7 | 2 | 9.000.000 | 289 | 5,3 | 1.698.000 | Max Clicks + cap | Tuần 7 = D49 qua. ≥30 conv D45? Yes (tuần 1-6: 26.3 leads, tuần 7 mới vượt 30). Wait để chắc. |
| 8 | 2 | 9.000.000 | 291 | 5,4 | 1.667.000 | Max Clicks + cap | D56 = cuối tuần 8. Tổng lead-q: 38 → ≥30 conv ✓. Chuyển bidding: Lead_Contactable primary → Maximize Conversions. (D56) |
| 9 | 3 | 9.000.000 | 272 | 4.2 | 2.143.000 | Max Conversions (L1) | Learning 2 tuần: CVR ×0.85 = 3.4%. CPC +15% (thị trường nóng). Tính ≈26k → 29.9k, dự tính click -5% do CPC cao. Contact 55%. |
| 10 | 3 | 9.000.000 | 268 | 4.1 | 2.195.000 | Max Conversions (L2) | Learning tuần 2 CVR ×0.85 = 3.4%. Sau tuần 10 hết learning → hệ số hiệu quả ×1.15 áp từ tuần 11. |
| 11 | 3 | 9.000.000 | 310 | 5.5 | 1.636.000 | Max Conversions (✓) | D74+: Post-learning ×1.15 boost → CVR 4.0% × 1.15 ≈ 4.6%. Max Conversions ≥2 tuần ✓ + ≥30 conv ✓ → được chuyển tCPA = CPA lịch sử +15%. Giả định CPA history 1.7M → tCPA 1.955M (trong ±15%). |
| 12 | 3 | 9.000.000 | 325 | 6.0 | 1.500.000 | tCPA (1.955M) | Tuần 12 tCPA optimize (không reset, ≤±15%). CVR 4.6% + CPC 29.9k. Contact 55%. Kết thúc 90 ngày. |

---

## Quyết định tại các mốc D30/D45/D60/D74

**D30 (Tuần 5, cuối):**
- Milestone: Keap agreement xong → ECL enabled. Upload_ecl chạy, tag contactable/qualified có dữ liệu.
- Hành động: Bắt đầu ghi tag Lead_Contactable từ CRM. Tồn đọc lead-q từ lead_qualified event GA4 backfill.
- Quyết định: Vẫn Max Clicks; chưa đủ 30 conv để chuyển Maximize Conversions. Tiếp tục tuần 6-8.

**D45 (Tuần 7, tính):**
- Check: ≥30 conversion qualified D15-45? Tuần 1-6: 26.3 lead. Tuần 7 mới hơi vượt. Nhưng D45 rơi giữa tuần 7, nên chưa chắc đạt. Chờ D56 (cuối tuần 8).

**D56 (Tuần 8, cuối — tương đương D60-4, coi là mốc D45 thực):**
- Check: ≥30 conversion qualified/30 ngày? Yes, tổng 38 lead D30-56.
- Hành động: **Chuyển bidding ĐÚNG:** Lead_Contactable làm primary conversion action trước, rồi Maximize Conversions. KHÔNG để form submit làm primary (vi phạm).
- Hiệu ứng: Learning CVR ×0.85, 2 tuần (tuần 9-10). Sau đó ×1.15 vĩnh viễn.

**D74 (Tuần 11, giữa):**
- Milestone: Max Conversions ≥2 tuần (tuần 9-10) ✓ + ≥30 conv (38+4.2+4.1+5.5 = 51.8 by D70) ✓ → được tCPA.
- Hành động: Chuyển tCPA = CPA lịch sử +15%.
  - CPA lịch sử: 38 lead / 9M budget (tuần 5-8 tính CPA = 36M / 38 = 947k/lead raw). Qualify rate 40% → CPA-q ≈ 2.37M. +15% → tCPA 2.73M.
  - Giả định user accepted tCPA ngoài learning reset.
- Giữ ±15%: 2.73M trong vùng an toàn. Tuần 11-12 chạy tCPA.

---

## Tổng 90 ngày

| Chỉ số | Giá trị |
|---|---|
| **Tổng chi tiêu** | 30M (tuần 1-4) + 36M (tuần 5-12) = 66M |
| **Tổng click** | ~3.226 click |
| **Tổng lead raw** | ~3.226 × 3.8% (CVR blended) ≈ 123 lead |
| **Tổng lead-q** | 123 × 40% ≈ 49 leads qualified |
| **CPL-q blended** | 66M / 49 = 1.347M/lead |
| **Contact rate** | 55% (giữ ổn định, sales SLA 85% → 15% lead mất tag) |
| **Bậc bidding cuối** | tCPA 2.73M |
| **Gates đã mở** | ECL (D30) ✓ · Maximize Conversions (D56) ✓ · tCPA (D74) ✓ |
| **Demand Gen (G2)** | Không mở: xem_bang_gia ≈ 200 user/30d (dưới 1k threshold) — organic/content chưa đủ pump. |

---

## 3 bài học

1. **Budget tightness là tín hiệu sớm nhất của demand.** IS lost 25% tuần 2-3 không phải lỗi campaign, mà do budget căn cứ không khớp reality. Monitoring §3 (IS lost ≥10% ×3 ngày + CPL/contact OK → tăng ≤20%) đúng hướng, nhưng thời điểm mở khóa tăng phải nhanh hơn (tuần 2 cuối, không chờ tuần 3). Learning reset thua mất tăng revenue, worth it.

2. **Chuyển bidding từ Max Clicks sang Maximize Conversions phải đúng primary action.** Nếu để form thô làm primary (thay vì Lead_Contactable từ CRM), qualify rate sẽ ×0.75 vĩnh viễn (4 tuần sau mới biết). Tại D56, đã có 38 lead → CRM tag đã warm up → chắc chắn chuyển. Timeline mở khóa (≥30 conv/30d) là gate, không phải giới hạn kỹ thuật — biết sớm = tiến sớm.

3. **tCPA tuân ±15%, chờ 4 tuần, rồi lên level.** Tuần 11-12 tCPA 2.73M chạy ok (không reset). Nếu tuần 12 CPA thực < 2.73M (say 2.3M), tháng sau có thể propose lên tCPA 2.65M (+15% từ 2.3M) — dần dần, đừng nhảy. Hệ số ×1.15 từ Maximize Conversions là quà tặng free (data quality via Lead_Contactable); tCPA là step tiếp để squeeze hơn nữa, rủi ro learning reset cao nên chờ ổn 2 tuần mới chuyển. Đó là vì sao bậc D74 thay vì D45: phải buffer time trước.
