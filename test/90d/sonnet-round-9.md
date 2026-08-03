# Round 9 — Sonnet 5 — 90 ngày

**Kịch bản:** đất nền Long An · 30tr₫/tháng (1.000.000₫/ngày) · CPC 18.000₫ (20.700₫ tuần 9-12, +15% mùa nóng) · **qualify rate trần 25%** đặc thù phân khúc (cò dò giá) dù form đủ 2 dropdown. Dự án `phúc an city` + `la home` (nguồn: kỳ 1 = `test/round-9.md`, không lặp lại chi tiết setup).
Mục tiêu placeholder CPL-q = 1.560.000₫ (`journey-plan` §4 — breakeven thật vẫn `[chưa điền]`, `PLAN` §6.6/§6.7).

## Setup + quyết định kỳ 1 (D1-30)

Setup tuần 0 và xử lý bẫy **giống hệt** `test/round-9.md` (không lặp lại): Max Clicks + bid cap (bậc 0), 44 kw/0 broad, 386+12 negative, dropdown đất nền `1,5-2/2-3/>3 tỷ` + ô `mua đi bán lại` (không `<1,5 tỷ`), RSA neo `Đất Nền Long An Từ 1,5 Tỷ`, primary=`generate_lead` (ECL chưa chạy).

**Bẫy T2-3 (đã xử lý tại D14, chi tiết đầy đủ ở `round-9.md`):** CPL-q AG-A vượt trần → chẩn đoán bằng cặp **contact rate 55% cao + qualify rate 5% thấp** = PHÂN KHÚC, không phải setup → pause 6 keyword head-term/giá-bao-nhiêu trong AG-A (giữ AG-B là producer), +12 negative, budget nội bộ #3 450k→360k / #1 475k→565k (**tổng vẫn 1.000k/ngày — không tăng tiền**). Không đụng bid, không đụng LP.

Kết quả D30: CVR LP 4,8%, qualify blended 17,2%→20,5%, contact 55%, CPL-q blended **1.989.000₫**. #1 Brand đạt 38,8 conv/30 ngày + contact >50% + chạy ≥4 tuần → đủ điều kiện **SỐ** của `campaign-setup` §4.4 nhưng **không chuyển bidding** vì chưa có `Lead_Contactable` (ECL chưa chạy) — đúng gate bậc 1 `journey-plan` §3.2.

## Bảng 12 tuần

| Tuần | Chi (₫) | Click | Lead-q | CPL-q (₫) | Bậc bidding | Ghi chú |
|---|---|---|---|---|---|---|
| 1 | 7.500.000 | 417 | 3,44 | 2.180.000 | 0 Max Clicks | Setup ổn, không đụng gì (`campaign-setup` §4.1) |
| 2 | 7.500.000 | 417 | 3,44 | 2.180.000 | 0 | 🚨 bẫy: CPL-q vượt trần 3 ngày → chẩn đoán PHÂN KHÚC, pause 6 kw AG-A + 12 negative + resplit ngân sách nội bộ |
| 3 | 7.500.000 | 417 | 4,10 | 1.829.000 | 0 | AG-A hồi phục; **không** đổi ngân sách lần 2 (`research` §4: ±20%/lần, cách ≥3-4 ngày) |
| 4 | 7.500.000 | 417 | 4,10 | 1.829.000 | 0 | #1 đủ điều kiện số §4.4, chưa chuyển (chưa có ECL) |
| **D30** | — | — | — | — | — | **Keap ký xong → ECL bật được** |
| 5 | 7.500.000 | 417 | 4,56 | 1.645.000 | 0 | CVR +0,4 (kỳ 2, insight Clarity mô phỏng: rage-click/scroll-drop trước bảng giá mobile → đôn bảng giá lên + thêm nav-anchor "Xem bảng giá"). ECL live, sales tag SLA48h |
| 6 | 7.500.000 | 417 | 4,56 | 1.645.000 | 0 | #1 đủ 3 điều kiện §4.4 (≥15 conv, contact>50%, ≥4 tuần) — chờ D45 để đảo primary đúng thứ tự |
| **D45** | — | — | — | — | — | **Chuyển ĐÚNG**: đảo primary→`Lead_Contactable` TRƯỚC, rồi mới bật Maximize Conversions |
| 7 | 7.500.000 | 417 | 3,87 | 1.938.000 | 1 Max Conv (learning) | CVR ×0,85 (tuần học 1/2) — không đổi ngân sách trong 2 tuần |
| 8 | 7.500.000 | 417 | 3,87 | 1.938.000 | 1 (learning) | Tuần học 2/2. Báo cáo tháng 2: contact rate ổn định 55%, 85% lead gắn tag đúng SLA48h (15% mất tag — rủi ro ECL đã biết) |
| **D60** | — | — | — | — | — | Learning hết → hệ số hiệu quả **×1,15 vĩnh viễn** (qualify 21%→24,15%, dưới trần 25%). **G2 mở** (content bơm `xem_bang_gia` ≥1.000 user/30 ngày) |
| 9 | 7.500.000 | 308* | 4,37 | 1.716.000 | 1 (ổn định) | CPC +15%→20.700₫ (mùa nóng T9-12). DG bật 150k/ngày (≤15%, Search còn 850k/ngày), **đã điền Excluded content keywords** → +5% lead-q remarketing |
| 10 | 7.500.000 | 308 | 4,37 | 1.716.000 | 2 tCPA | **D74**: chuyển tCPA = CPA lịch sử +15% (trong biên ±15% — không phạt); mở test 1 ad group broad (bậc 2 đủ điều kiện: ≥30 conv/30 ngày + ECL chạy thật) |
| 11 | 7.500.000 | 308 | 4,37 | 1.716.000 | 2 | Không đổi ngân sách/tCPA trong 2 tuần learning |
| 12 | 7.500.000 | 308 | 4,37 | 1.716.000 | 2 | Chốt scorecard 90 ngày |

*click tuần 9-12 chỉ tính phần Search (850k/ngày ÷ 20.700₫); DG không dùng công thức click/CVR, chỉ cộng +5% lead-q khi Excluded content keywords đã điền (`journey-plan` G2).

## Quyết định tại các mốc

| Mốc | Làm gì | Căn cứ doc |
|---|---|---|
| **D30** | Nhận thoả thuận Keap, bật ECL/`upload_ecl.py` chạy thật, sales bắt đầu tag `Lead_Contactable` SLA 48h | `sim-rules-90` bảng mốc · `PLAN` §6.6 |
| **D45** | Đảo primary sang `Lead_Contactable` TRƯỚC, rồi mới chuyển `Max Clicks`→`Maximize Conversions` cho #1; không đổi ngân sách 2 tuần | `campaign-setup` §4.4 · `journey-plan` §3.2 bậc 1 |
| **D60** | Mở Demand Gen remarketing 150k/ngày (≤15%, rút từ #3) sau khi `xem_bang_gia` đạt 1.000 user/30 ngày; **điền Excluded content keywords** cấp tài khoản (bắt buộc — negative Search không phủ inventory Demand Gen) | `journey-plan` §3.1 G2 · war-game round 5 |
| **D74** | Chuyển `Maximize Conversions`→`tCPA` = CPA thực 30 ngày lịch sử **+15%** (trong biên ±15%, không sai); mở 1 ad group broad + Data exclusion (bậc 2 đủ điều kiện) | `campaign-setup` §4.4 · `journey-plan` §3.2 bậc 2 |
| **Không làm** | G1 (mở khu vực mới): ngưỡng conv/tháng vẫn `[điền]` — user chưa chốt → **không mở**, không tự bịa ngưỡng. G3/G4/G5 (PMax/YouTube): ngoài phạm vi ngân sách 30tr (`PLAN` §0.1, cần ≥150tr) | `journey-plan` §3.1 |

**Báo cáo tháng (research §8, rút gọn):** Kỳ 1: contact rate 55% ổn, chưa có ECL → CPL-q là số duy nhất dùng được. Kỳ 2: ECL sống, 85% lead đúng SLA48h, đảo primary đúng thứ tự, learning theo đúng lịch. Kỳ 3: tCPA đúng biên +15%, broad test mới mở (chưa đủ dữ liệu đánh giá riêng), CPC+15% mùa nóng đã phản ánh vào CPL-q.

## Tổng 90 ngày

| Chỉ số | Giá trị |
|---|---|
| Tổng chi tiêu | **90.000.000₫** (3 × 30tr, không tăng ngân sách tổng lần nào) |
| Tổng click | 4.568 |
| Tổng lead qualified | **49,4** |
| **CPL qualified blended** | **1.821.000₫** = 1,17× mục tiêu placeholder 1,56tr |
| Xu hướng CPL-q theo kỳ | 1.989.000 → 1.779.000 → **1.716.000₫** (giảm dần, hội tụ) |
| Contact rate | 55% ổn định cả 90 ngày; 85% lead gắn tag đúng SLA48h từ D30 (15% rủi ro mất tín hiệu ECL) |
| Qualify rate blended | 21,6% (trần phân khúc 25% — chưa từng vượt) |
| Bậc bidding cuối kỳ | **2 — tCPA + ECL + broad test + Data exclusion** |
| Gates đã mở | G0 ✓ · G2 ✓ (D60) · G1 ❌ (ngưỡng chưa điền, không tự mở) · G3/G4/G5 ❌ (ngoài phạm vi 30tr) |

**Trần kinh tế — con số quyết định.** Sàn CPL-q lý thuyết ở CPC 20.700₫ (mùa nóng) + qualify trần 25% + CVR trần 6% = **~1.725.000₫**. Kết quả thực đo được ở kỳ 3 là **1.716.000₫** — tức hệ thống đã chạm **đúng sàn cấu trúc của phân khúc**, dù đã đi hết lộ trình: LP tối ưu 2 lần (+0,8 CVR), ECL sống, bidding chuyển đúng nhịp cả 2 mốc (D45, D74), G2 mở thêm remarketing. **Không còn đòn bẩy Ads nào để hạ CPL-q thêm** — mọi cải thiện còn lại (siết dropdown thêm bậc, content lọc organic) chỉ dịch chuyển ai trả tiền cho ai dò giá, không phá được trần 25%.

**Quyết định 90 ngày (bằng số):** sàn cấu trúc (~1,72tr₫) **vẫn cao hơn** mục tiêu placeholder (1,56tr₫) ngay cả ở kịch bản tốt nhất có thể đạt trong Ads. Nếu breakeven thật (`journey-plan` §4/§6 — phí môi giới/nền + tỷ lệ booking→HĐMB, **vẫn chưa có** từ user) cho CPL mục tiêu dưới ~1,72tr₫ → kết luận là **dừng phân khúc đất nền Long An ở cấu hình này**, không phải "tối ưu thêm". Nếu breakeven thật cao hơn 1,72tr₫ (biên lợi nhuận/nền đủ lớn) → **tiếp tục**, vì hệ đã ở sàn kỹ thuật, ổn định, không còn rủi ro vận hành. Đây là quyết định kinh doanh, không phải quyết định Ads — số duy nhất còn thiếu để chốt là breakeven, vẫn treo từ round 9 kỳ 1.

## 3 bài học

1. **90 ngày không phá được trần cấu trúc phân khúc, dù chạy đúng mọi gate.** CPL-q giảm 1,989tr→1,716tr (-14%) hoàn toàn nhờ thực thi đúng (ECL, đảo primary đúng thứ tự, tCPA đúng biên, G2 đúng lúc) — không phải nhờ phá trần qualify 25%. Trần đặc thù phân khúc là giới hạn **kinh doanh**, không phải giới hạn **vận hành**; 90 ngày dữ liệu đủ để khẳng định cái nào là cái nào, 30 ngày thì chưa.
2. **Đúng nhịp (không sớm, không muộn) tự nó là một dạng CPL-q thấp hơn.** Chuyển bidding đúng lúc D45 (đảo primary trước) tránh được hình phạt qualify×0,75 vĩnh viễn; chuyển tCPA đúng biên ±15% tại D74 tránh reset learning ×0,7. Hai cú tránh phạt này cộng lại lớn hơn bất kỳ tối ưu keyword/RSA nào có thể làm trong cùng 2 tuần.
3. **"Chưa có breakeven" là một khoảng trống ngày càng đắt theo thời gian, không phải một ô trống vô hại.** Sau 90 ngày và 90 triệu₫ chi tiêu, quyết định go/no-go vẫn treo ở đúng một số duy nhất (phí môi giới/nền × tỷ lệ chốt) mà user chưa cấp từ round 9 kỳ 1. Ads đã làm hết phần việc của mình (chạm sàn kỹ thuật); phần còn lại không thuộc phạm vi Ads.
