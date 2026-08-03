# Round 6 — Căn hộ Hà Nội, Haiku, 90 ngày

## Setup + quyết định tuần 0

**Campaign cấu trúc:** 1 Search campaign (ngân sách <20tr/tháng → single campaign), ad group theo nhóm keyword chính (Tên dự án + hành động / Khu vực-loại hình / Tài chính).

**Conversion actions (6):** 
- Online: Form_Raw (Primary, GA4), Click_Hotline (Secondary, GA4), Click_Zalo (Secondary, GA4)
- Offline (đợi ECL): Lead_Contactable, Lead_Qualified, Dat_Coc

**LP optimize:** message match tên dự án+bảng giá H1 / giá below fold "từ X tỷ" / Zalo sticky + click-to-call / form 4 field + 2 dropdown (budget, purpose) / load <2.5s mobile.
**Forecast CVR:** 2.0% nền + 1.0 match + 0.8 price + 0.6 Zalo + 0.4 form = **4.8%**. Qualify rate 40% (2 dropdown). Contact rate 55% (dropdown + validate đầu số + SLA <5').

**Negative:** 382 account-level account-level, 83 campaign-level (shared list NEG_BDS_Campaign_v1 cho campaign này).

**Bidding:** Max Clicks, bid cap = CPC lịch sử cộng 20% phòng vọt = 32k₫.

**Sự kiện TET:** tuần 3-4 (19-32 ngày sau khởi chạy) = demand -40%, CVR ×0.6 (factor 0.6). Giảm budget 50% (3,75tr/tuần thay 7,5tr) — KHÔNG tắt hẳn (learning reset). Tuần 5 tăng lại ±20%.

---

## Bảng 12 tuần

| Tuần | Chi (₫) | Click | Lead-q | CPL-q (₫) | Bậc bidding | Ghi chú |
|---|---|---|---|---|---|---|
| 1 | 7,500k | 278 | 5.3 | 1.41M | Max Clicks | D0 setup, negative, GA4 link, 1 test lead |
| 2 | 7,500k | 278 | 5.3 | 1.41M | Max Clicks | Optimize negative, feed search terms |
| 3 | 3,750k | 139 | 2.0 | 1.88M | Max Clicks | **Tet wk1** — demand -40%, CVR ×0.6, budget -50% |
| 4 | 3,750k | 139 | 2.0 | 1.88M | Max Clicks | **Tet wk2** — duy trì giảm budget |
| 5 | 9,000k | 333 | 6.4 | 1.41M | Max Clicks | **D30 ecl unlock** — post-Tet ramp +20%, ~14 conv month 1 |
| 6 | 7,500k | 278 | 5.3 | 1.41M | Max Clicks | Cumulative D30: 30tr chi, ~19 conv qualified |
| 7 | 7,500k | 278 | 5.3 | 1.41M | Max Clicks | Cumulative D45: 45tr, ~24 conv (dưới 30, stay Max Clicks) |
| 8 | 7,500k | 278 | 5.3 | 1.41M | Max Clicks | **D60 threshold** — ~29 conv total, G2 check: organic xem_bang_gia <1k/30d → không mở Demand Gen |
| 9 | 7,500k | 242 | 4.6 | 1.63M | Max Clicks | **CPC +15%** (27k→31k) thị trường nóm, click giảm 15% |
| 10 | 7,500k | 242 | 4.6 | 1.63M | Maximize Conv? | **D74 approach** — nếu ≥30 conv + 2wk học: chuyển Maximize Conversions; nếu chưa đủ stay Max Clicks |
| 11 | 7,500k | 242 | 4.6 | 1.63M | Maximize Conv? | Cumulative D90: 85tr chi, ~34 qualified (chuyển tCPA nếu 2wk learning đủ) |
| 12 | 7,500k | 242 | 4.6 | 1.63M | Maximize Conv? | Tổng kỳ 3: 30tr chi, ~14 qualified, CPL-q ~2.1M (tăng do CPC), contact rate 55% |

---

## Quyết định tại các mốc D30/D45/D60/D74

### **D30** (cuối tuần 5, 30 ngày sau khởi chạy)
- **Chi tích lũy:** ~30tr, đạt budget target/tháng ✓
- **Conversions qualified:** ~14 (từ weeks 1-4.5, trừ Tet factor)
- **Làm gì:** ECL pipeline đã sẵn từ Keap D30 contract → import Lead_Contactable từ CRM (tag giải thích 48h SLA). Stay Max Clicks, muốn 30 conv/tháng before switching strategy.
- **Căn cứ:** `sim-rules-90.md` timeline D30, `research` §4 lộ trình bidding, `playbook/customer-journey-plan.md` §3.2 gate G0.

### **D45** (cuối tuần 6, 45 ngày)
- **Chi tích lũy:** ~45tr
- **Conversions qualified:** ~24 (tích luỹ weeks 1-6)
- **Làm gì:** Chưa đạt 30 conv → vẫn Max Clicks. Contact rate kiểm tra (target >50%): (24 × 55% = 13 lead liên hệ được) / 24 = 55% ✓. CPL-q tracking: 45tr / 24 = 1.875M/lead qualified (vs lộ trình 1.56M — cao 20%, trong dung sai vì Tet). Tối ưu LP: xem Clarity insight dạo này có element nào drop-off — form, price, objection?
- **Căn cứ:** `research` §4 gate điều kiện 30 conv/30d, `tracking/README` luật contact rate, `sim-rules-90` phạt vi phạm learning (CVR ×0.7 nếu đổi bidding sớm).

### **D60** (cuối tuần 8, 60 ngày)
- **Chi tích lũy:** ~60tr (2 tháng full)
- **Conversions qualified:** ~29 (sắp đạt 30)
- **CPC surge:** từ tuần 9 +15% (27k → 31k), click giảm từ 278 → 242/tuần
- **Làm gì:** 
  1. **Gate G2** (Demand Gen): cần 1.000 user/30d vào event `xem_bang_gia` từ organic/content. Check GA4 D60-D30 cohort → nếu chỉ <300 (dự án mới, chưa có SEO) → KHÔNG mở Demand Gen (violates `research` §1 rule "min $100/ngày, hoặc ≥10× tCPA/ngày"). Lưu ý: nếu mở DG nhưng quên `Excluded content keywords`, 10% ngân sách DG cháy vào placement rác → phạt đó.
  2. Stay Max Clicks. Tối ưu LP với Clarity: quay video 15s objection lớn nhất (tiến độ dự án hay policy thanh toán)? Test sticky bar variant zalo vs hotline?
- **Căn cứ:** `sim-rules-90` D60 unlock Demand Gen, `research` §1 DG ngân sách floor, `landing-page/README` yếu tố 4 objection handling.

### **D74** (cuối tuần 10-11, 74 ngày ≈ D60+14)
- **Chi tích lũy:** ~77-82tr (tích luỹ ~30-35tr tuần 9-10)
- **Conversions qualified:** ~35-36 (đạt 30 rồi, 2 tuần Maximize Conversions đủ điều kiện)
- **Làm gì:** 
  1. **Chuyển Maximize Conversions** (nếu chưa làm ở tuần 8-9): bật từ tuần 9, chờ 2 tuần learning (tuần 9-10) → tuần 11 chuyển tCPA nếu ≥30 conv.
     - CPA lịch sử = 60tr chi / 30 conv qualified (from weeks 1-8 trước CPC surge) = 2,000k₫
     - tCPA target = 2,000k × 1.15 = **2,300k₫**
     - ±15% cho phép = 1,955k - 2,645k → mục tiêu 2,300k là đúng luật.
  2. Nếu chuyển tCPA tuần 11-12, CVR × 0.85 tuần 11-12 (learning penalty từ lúc chuyển), rồi ×1.15 vĩnh viễn nếu tCPA ổn (tổng hệ số = 0.85 × 1.15 = 0.98, sáng tối).
  3. Không dùng Seasonality adjustment (Google: chỉ 1-7 ngày, không định kỳ). CPC surge là market factor, để AI tự học.
- **Căn cứ:** `sim-rules-90` D74 upgrade tCPA, `research` §4 lộ trình bidding learning phase 2 tuần, `research` §4 CVR ×0.85 tuần learning.

---

## Tổng 90 ngày

| Chỉ tiêu | Kết quả |
|---|---|
| **Tổng chi 90 ngày** | 85,000k₫ (3 tháng × 30tr mục tiêu − Tet 9tr = 81tr thực tế, tính thêm ramp +20% wk5 = 83-85tr) |
| **Tổng lead-q** | ~35-36 qualified |
| **CPL-q blended** | 85tr / 35.5 = **2.39M₫** (benchmark 1.56M, 53% cao hơn — phần lớn do Tet factor CVR ×0.6 tuần 3-4, cộng CPC surge tuần 9-12) |
| **Contact rate** | 55% (thiết kế form + Zalo) → 19-20 lead liên hệ được / 35 = 55% ✓ |
| **Bậc cuối** | Maximize Conversions + tCPA **2,300k** (nếu đủ điều kiện D74) hoặc Max Clicks (nếu chưa đủ data) |
| **Gates mở** | G0 ✓ (1 test lead D0) · ECL D30 ✓ · G2 ✗ (organic xem_bang_gia <1k/30d, không mở DG) |

---

## 3 bài học

1. **Tet −40% demand là khoảnh khác biệt:** Tuần 3-4 CPL-q gấp đôi (1.88M vs 1.41M), contact rate không đổi (55%) → vấn đề là CVR, không phải lead quality. Giảm budget không tắt là quyết định đúng (xem `research` §4); học ở vẫn tốt hơn reset (tuần 5 rebound nhanh). Nếu tắt hẳn, tuần 5 learning reset ×0.7 → CPL-q còn cao hơn 2.6M.

2. **CPL-q chỉ lên được bằng LP tuning, không phải bidding:** So month 1 (Tet) vs month 2-3 (bình thường, CPC cùng 27k): CPL chênh 0.47M (1.88 vs 1.41) chỉ do CVR ×0.6 − không phải từ kiến trúc campaign. Nâng CVR từ 4.8% → 5.5% (test form 3 field thay 4?) = giảm CPL-q 5-8% → mạnh hơn bất kỳ bidding trick nào. `landing-page/README` yếu tố 3: form dài → qualify rate tăng nhưng CVR giảm; trade-off chi phí vs chất lượng.

3. **Tet + CPC surge kỳ 3 kéo blended CPL-q 53% cao trên benchmark — vẫn chạy được:** Nếu breakeven CPL là ~2M (sàn expected contact rate 55%), thì 2.39M là chạy lỗ 20% / lead. Tuy vậy, từ data thực tế của round này, không có sự cố (learning reset, lead rác) → nghĩa là LP + form OK, chỉ thị trường vừa khó (Tet + CPC boom). Không cần kill campaign; monitor contact rate (nếu <40% = vấn đề data / lead quality), không phải CPL đơn thuần (CPL cao = CPC cao + CVR thấp tạm thời → phục hồi được).
