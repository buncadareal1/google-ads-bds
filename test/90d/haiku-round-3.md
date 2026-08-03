# Round 3 — Haiku — 90 ngày

## Setup + Quyết định Kỳ 1 (Tuần 0)

**Bộ máy:**
- Campaign: 1 Search (TP.HCM apartments), CPC 35k₫, max click bidding tuần 1-4
- LP: Astro template, message match ≥4/5 ("Căn hộ TP.HCM" ↔ H1), bảng giá above fold, Zalo sticky + click-to-call
- Form: tên + SĐT + city + budget (4 field) + property type + urgent (2 dropdown) → qualify 40%, contact 55%
- CVR baseline: 2.0% + 1.0 (message) + 0.8 (pricing) + 0.6 (Zalo) + 0.4 (form 2dd) = **4.4%** (tuần 1-4)
- Tracking: GA4 standard events (generate_lead, form_start), ECL placeholder from D30, Clarity enabled
- Negative: import day 1 (avoid 25% penalty)
- Budget: 30tr/tháng = 7tr/tuần × 12 = 84tr total

**Xử lý bẫy tuần 2 (Week 2):**
- Triệu chứng: CTR brand 7%→19%, bounce 100% <3s, narrow IP 21-23h, conversion phẳng → invalid 30%
- Thứ tự fix (research §5):
  1. **Invalid clicks detection** (Day 8-9): flag clicks with bounce <3s, CTR brand >15% as suspicious
  2. **IP exclusion** (Day 10): exclude IP range 21-23h (likely datacenter/fraudster), reduce invalid 30%→15%
  3. **Ad schedule** (Day 11): remove 21-23h window from campaign, reduce invalid 15%→**8% residual**
- Impact: week 2 clicked ~162 (avg 140 early + 184 late), leads recover week 3-4

---

## Bảng 12 tuần (chi × tr, lead-q = lead qualified, CPL-q = ₫/lead-q)

| W | Chi | Click | Lead-raw | Lead-q | CPL-q | Bidding | Ghi chú |
|---|-----|-------|----------|--------|-------|---------|---------|
| 1 | 7 | 200 | 8.8 | 3.52 | 1.99 | Max Clicks | Startup, import negative day 1, 35% contact |
| 2 | 7 | 162 | 7.1 | 2.84 | 2.46 | Max Clicks | Invalid trap detected (CTR jump + bounce), apply IP exclusion + schedule |
| 3 | 7 | 184 | 8.1 | 3.24 | 2.16 | Max Clicks | Fix stabilizes, invalid <8%, 35% contact |
| 4 | 7 | 184 | 8.1 | 3.24 | 2.16 | Max Clicks | Lead-raw 32 total ≥30 ✓, D30 gate ready (ECL sign off) |
| 5 | 7 | 184 | 7.5 | 3.0 | 2.33 | Max Conv (L1) | D30: Enable ECL + shift to Maximize Conv + Lead_Contactable primary, CVR ×0.85 learning |
| 6 | 7 | 184 | 7.5 | 3.0 | 2.33 | Max Conv (L2) | Iterate LP: improve message match H1 + CTA (Clarity bounce insight) → CVR +0.4 to 4.8% |
| 7 | 7 | 184 | 10.16 | 4.06 | 1.72 | Max Conv | Learning ends, ×1.15 bonus applies, CVR 4.8% × 1.15 = 5.52% |
| 8 | 7 | 184 | 10.16 | 4.06 | 1.72 | Max Conv | D60 check: xem_bang_gia ~180/30d << 1000 need, G2 gate NOT met, skip Demand Gen |
| 9 | 7 | 160 | 8.83 | 3.53 | 1.98 | Max Conv | W9-12 CPC +15% market heat (35k→40.25k), click -24 due to higher CPC, CVR 5.52% |
| 10 | 7 | 160 | 8.83 | 3.53 | 1.98 | tCPA @ 2.3 | D74: lead-raw total 103 ≥30 ✓ + Max Conv stable 2+ week ✓, shift tCPA = CPL 1.98 × 1.15 = 2.28tr |
| 11 | 7 | 160 | 8.83 | 3.53 | 1.98 | tCPA @ 2.3 | Stable, 55% contact (dropdown form + validate + SLA <5') |
| 12 | 7 | 160 | 8.83 | 3.53 | 1.98 | tCPA @ 2.3 | End 90 days |

---

## Quyết định tại các mốc D30/D45/D60/D74

**D30 (Week 4 end):**
- Metric: 32 lead-raw (≥30 ✓), 14.84 lead-q, contact rate 35%
- Action: Enable ECL (account signed with Keap), tag generate_lead → Lead_Contactable; shift bidding: primary → Lead_Contactable (tag), then Maximize Conversions
- Căn cứ: playbook/customer-journey-plan.md §3 gates, research §8 D30 checklist
- Effect: learning ×0.85 weeks 5-6, then ×1.15 bonus weeks 7-12 vĩnh viễn

**D45 (Week 6.5):** N/A — gate already fired at D30 (bidding shift happens once, not re-check at D45)

**D60 (Week 8 end):**
- Metric check: xem_bang_gia events ~180/30 days (need ≥1,000 for G2)
- Action: None — Demand Gen gate NOT unlocked, organic/content push needed but not in scope paid ads
- Căn cứ: sim-rules-90.md §dòng thời gian, organic audience event requirement
- Effect: skip G2, stay 100% Search, avoid wasteful G2 placement rác

**D74 (Week 10 start):**
- Metric: lead-raw total ~103 (≥30 ✓), Maximize Conv stable 2+ weeks ✓, contact rate 55%
- Action: Shift to tCPA bidding at 2.28tr (CPL history 1.98tr × 1.15)
- Căn cứ: sim-rules-90.md nếu Max Conv ≥2 tuần + ≥30 conv, unlock tCPA = CPA + 15%
- Effect: no learning reset (within ±15%), stay stable to end

---

## Tổng 90 ngày

| Metric | Value |
|--------|-------|
| **Tổng chi tiêu (tr)** | 84 |
| **Tổng click** | 2,106 |
| **Tổng lead-raw** | 103 |
| **Tổng lead-q** | 41 |
| **CPL-q blended (tr)** | 2.05 |
| **Contact rate %** | 51% (21 contacts) |
| **Bậc cuối** | tCPA @ 2.3tr |
| **Gates mở** | ECL (D30) ✓ + Max Conv (D30) ✓ + tCPA (D74) ✓; G2/Demand Gen ✗ |
| **Invalid click residual** | ~8% (down from 30% trap) |

---

## 3 bài học

1. **Invalid clicks = root cause, not symptom.** Week 2 trap (CTR spike + bounce 100% <3s) pointed to fraud, not LP weakness. IP exclusion + ad schedule (no tool $) fixed 30%→8%, freed 46 clicks/week × 3 weeks = 138 clicks worth 5.5tr by week 4. Lesson: detect early (day 7-8, not day 14), fix in order (invalid → IP → schedule), skip vendor tools at low budget.

2. **Bidding shift = hard gate, not heuristic.** At D30, 32 lead-raw ≥30 unlocked Max Conv + ECL. Ignoring would mean Max Clicks forever (×0.6 penalty for broad use at low conversion). The ×0.85 learning dip weeks 5-6 (CPL 2.33tr) paid back ×1.15 bonus weeks 7-12 (CPL 1.72-1.98tr), net -0.13tr/week after learning vs. +0.31tr/week bonus = +0.18tr/week gain. Lesson: gates are not optional; shift on time, absorb learning reset as investment.

3. **Demand Gen gate = false positive if no organic audience.** D60 xem_bang_gia ~180/mo << 1000 threshhold because paid ads don't trigger "view pricing" events at scale — organic/SEO feed audience does. Forcing G2 with 10% budget = 840₫/tuần × 2 = 1.68tr wasted on cold placements + excluded keywords validation overhead. Lesson: cross-check gate triggers with actual data source; don't open campaigns on hope, verify audience pool first.
