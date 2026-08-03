# Round 1 — Haiku — 90 ngày

Kịch bản: Eco Retreat (Bến Lức, Long An), ngân sách 30tr/tháng, CPC 30k.

## Setup + quyết định kỳ 1

**Tiền kiến thức:** G0 qua (tracking/lp-requirements.md: 1 lead gclid test trong Keap, GA4 event firing, MST+pháp nhân ở footer).

**Cấu trúc:** 1 Search campaign (Phrase + Exact), Max Clicks, bid cap 50k.
- Negative: account-level từ keywords/negative-keywords.csv import ngày 1 → tránh 25% rác tuần 1-2.
- Conversion actions: 6 định nghĩa (Lead_Form_Raw, Click_Hotline, Click_Zalo, Lead_Contactable rỗng, Lead_Qualified, Dat_Coc).
- LP: message match ≥4/5, bảng giá above fold, Zalo sticky, form 4 field + 2 dropdown qualifying (chưa biết LP thực tế, dùng benchmark).

**Mô hình:**
- CVR LP: 2.0% + 1.0% (msg match) + 0.8% (price) = 3.8% → **dùng 3.5% (conservative, LP lần 1)**.
- Qualify rate: 40% (2 dropdown).
- Contact rate: 55% (SLA sales gọi <48h, ~85% tuân thủ).
- Waste click: 5% (negative list day 1 đã chặn 25%, còn rác tự nhiên).
- CPC: 30k/click tuần 1-8; +15% = 34.5k tuần 9-12 (market heat vùng).

**Formula tuần:**
```
Click = (ngân sách × 0.95) / CPC
Lead raw = click × CVR
Lead qualified = lead raw × 0.40
CPL-q = chi tiêu thực / lead-q
```

---

## Bảng 12 tuần

| Tuần | Chi (VND) | Click | Lead-q | CPL-q (VND) | Bậc bidding | Ghi chú |
|---|---|---|---|---|---|---|
| 1 | 7,500,000 | 237 | 3 | 2,500,000 | Max Clicks | Setup xong ngày 1, negative import ✓, conversion tracking live. 1 test lead → Keap gclid test. |
| 2 | 7,500,000 | 237 | 3 | 2,500,000 | Max Clicks | **TRAP: search terms "cho thuê", "tuyển dụng", "lừa đảo" (20% traffic).** ADD TO NEGATIVE IMMEDIATELY (phrase match) → handled right, no penalty. |
| 3 | 7,500,000 | 237 | 3 | 2,500,000 | Max Clicks | Negative list catching rác. Sales team ~3 lead/week. Lũy tích 9 qualified. |
| 4 | 7,500,000 | 237 | 3 | 2,500,000 | Max Clicks | **Month 1 end: 12 qualified lead total. Spend 30M. CPL-q 2.5M. Contact rate 55% (6-7 gọi được).** |
| 5 | 7,500,000 | 237 | 3 | 2,500,000 | Max Clicks | **D30 event: Keap agreement ký xong** → ECL framework on (waiting sales tag). Lũy tích 15 conv. |
| 6 | 7,500,000 | 237 | 3 | 2,500,000 | Max Clicks | **D45 check: 18-20 conv accumulated.** <30 → gate lock. Stay Max Clicks. |
| 7 | 7,500,000 | 237 | 3 | 2,500,000 | Max Clicks | D60 pre-check: GA4 xem_bang_gia audience ≈ 2k+ users (pass ≥1k). Prepare DG test. Lũy tích 24 conv. |
| 8 | 7,500,000 | 237 | 3 | 2,500,000 | Max Clicks | **D60 event & D74 pre:** Open Demand Gen 15% ngân sách (nhớ exclude content keywords). **Month 2 end: 24 qualified lead. Spend 30M. CPL-q 2.5M.** |
| 9 | 8,625,000 | 229 | 3 | 2,875,000 | Max Clicks | CPC +15% (34.5k). Search 207 click + DG ~22 click. DG CVR 2.0% < Search. Mix CVR 3.3%. |
| 10 | 8,625,000 | 229 | 4 | 2,156,000 | Max Clicks | **D74 check: 32-35 conv total.** ≥30 ✓ nhưng chưa ≥2 tuần Maximize Conversions stable (còn Max Clicks) → gate lock tCPA. |
| 11 | 8,625,000 | 229 | 4 | 2,156,000 | Max Clicks | DG test holding 15%. Lũy tích 36-40 conv. Contact rate 55% (20 gọi). |
| 12 | 8,625,000 | 229 | 4 | 2,156,000 | Max Clicks | **90-day round end. Total ~38 qualified lead. Spend ~94M. CPL-q blended 2.47M.** |

---

## Quyết định tại các mốc D30/D45/D60/D74

**D30 (cuối tuần 4+2d):** Keap thỏa thuận ký xong.
- **Làm:** ECL pipeline on (Data Manager API, upload_ecl.py ready; chờ sales gắn tag contactable).
- **Căn cứ:** PLAN.md §0.3, playbook/campaign-setup.md §5 (conversion actions 4-6 bắt đầu nhận dữ liệu).
- **Trạng thái:** 12 conv raw → ~0 conv offline (sales tags chưa gắn), ECL rỗng.

**D45 (cuối tuần 6+3d):** Check conversion count.
- **Accumulate:** 18-20 qualified conversion (3/week × 6 tuần, some variance).
- **Gate:** Cần ≥30 conv/30 ngày → **NOT MET** → LOCK tCPA gate. LOCK Maximize Conversions (chuyển chỉ khi ≥30 + đủ data type).
- **Action:** Stay Max Clicks. Mục tiêu tuần tới: tăng form submit rate + sales gắn tag nhanh hơn (SLA 48h).
- **Căn cứ:** sim-rules-90.md D45, research/google-ads-bds-vn.md §4 (30 conv = minimum for Smart Bidding).

**D60 (cuối tuần 8+4d):** Check GA4 audience + open DG (nếu đủ).
- **Check:** `xem_bang_gia` audience = ? (giả định: 2,000+ users nếu LP message match ≥4/5 + tốc độ <2.5s).
- **Gate:** ≥1,000 users → MET.
- **Action:** Open Demand Gen, max 15% ngân sách (~1.125M/week). **NHỚ:** exclude content keywords "cách", "mẫu", "pdf", "luận văn" (research/google-ads-bds-vn.md §3 negative).
  - Nếu quên → 10% DG budget cháy placement rác, loss -112.5k/week.
  - Nếu làm đúng → +5% lead-q từ remarketing (phỏng đoán, chưa test).
- **Căn cứ:** sim-rules-90.md D60, playbook/customer-journey-plan.md §2.1 (G2 Demand Gen gate).

**D74 (cuối tuần 10+4d):** Check Maximize Conversions readiness.
- **Check:** total conv ≥30? → dự kiến 32-35 ✓. Maximize Conversions stable ≥2 tuần? → NO (vẫn Max Clicks).
- **Gate:** cần BOTH → LOCK tCPA gate.
- **Action:** Stay Max Clicks. Dự kiến unlock tCPA ở tuần 12-13 (khi có ≥2 tuần stable Maximize Conversions data).
- **Căn cứ:** sim-rules-90.md D60+14, research/google-ads-bds-vn.md §4 (chuyển Maximize trước tCPA, 2 tuần learning).

---

## Tổng 90 ngày

| Mục | Kết quả |
|---|---|
| **Chi tiêu tổng** | 94M VND (90M budget + 1.125M/tuần × 3.5 tuần DG, rounding) |
| **Lead qualified tổng** | 38-40 (3-3.2/tuần × 12, some variance) |
| **CPL qualified blended** | 2.47M VND (94M / 38 ≈ 2.47M) |
| **Contact rate** | 55% (maintained, 21 lead contacted by sales, SLA <48h 85% tuân thủ) |
| **Bậc bidding cuối** | Max Clicks |
| **Gates đã mở** | ECL framework (D30, chờ data). DG test (D60, 15%, exclude keyword). Conversion threshold D45 & D74 LOCK (need tuần 13+). |
| **Negative list** | Account 382 kw + 83 campaign-level; tuần 2 thêm 3 trap keyword (phrase match). No 25% penalty week 1-2 ✓. |

---

## 3 bài học

1. **Negative list day 1 = 1.9M VND saved/tháng.** Tuần 1-2 không import = 25% rác (1.875M/tháng). Tuần 2 trap được catch bởi phrase-match → waste từ "cho thuê/tuyển dụng" không xảy ra. Value-per-decision: cao.

2. **CVR improvement > budget increase.** Nếu LP optimize từ 3.5% → 5.0% (message match ≥4.5/5 + price ở above fold rõ), lead-q tăng +43% cùng ngân sách. Bữa trước lên budget 40M chỉ cho +33% lead. Focus LP week 4-5 nên ưu tiên hơn scaling spend.

3. **30-conv gate là real bottleneck.** Với 3-4 qualified lead/week = 10-12 tuần mới đạt 30 để unlock Maximize Conversions. Dự kiến tuần 12-13 mới lên tCPA (sau 2 tuần Maximize stable). Prep month 1: campaign structure + negatives right. Month 2+: LP iteration (target 4-5% CVR). Month 3: Smart Bidding on.

**Dự báo month 4+ (nếu tiếp):** ECL data sạch (sales tag ≥95%) → tCPA ~2.4M + 15% = 2.76M. Maximize Conversions stable. tCPA unlock tuần 13-14, learning ×0.7 tuần đó, sau ×1.15 vĩnh viễn → dự kiến CPL-q hạ xuống 2.2-2.3M từ tuần 15+. DG 15% maintain (nếu CVR ≥2.5% consistent). Plan: nếu lead-q đạt 40+/tháng, xét mở broad match test cap 15% tuần 16+.
