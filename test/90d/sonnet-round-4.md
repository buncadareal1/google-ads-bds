# Round 4 — Sonnet 5 — 90 ngày

Kịch bản: **biệt thự nghỉ dưỡng Phan Thiết** · 30tr₫/tháng (985.000₫/ngày) · CPC 35.000₫ (40.250₫ tuần 9-12, +15% mùa nóng). **Ràng buộc phân khúc vĩnh viễn** (`research/google-ads-bds-vn.md` §2: *"biệt thự/hạng sang — volume rất thấp, **KHÔNG dùng tCPA**"*) → trần lộ trình bidding cả 90 ngày = **Bậc 1 (Maximize Conversions)**, không phải Bậc 2 (tCPA), bất kể đạt gate D45/D74 hay không. Tiếp nối `test/round-4.md` (4 tuần) — không lặp lại setup, chỉ dẫn số cần dùng lại.

## Setup + quyết định kỳ 1 (D1-30)

Setup tuần 0 và xử lý 2 bẫy **giống `test/round-4.md`, đã QA pass** (không lặp lại chi tiết): 2 campaign (#1 `Brand_DuAn` 521k/ngày cap 30k · #3 `KhuVuc_GiaoDich` 464k/ngày cap 40k), 22 kw/0 broad, negative 386 account + 80 campaign (đã chặn `căn hộ`/`condotel`/`chung cư` + cụm du lịch/resort), conversion ladder 6 action cửa sổ 90 ngày (primary ngày 1 = `Lead_Form_Raw`, offline = Secondary rỗng), 11 ô §1.5 đủ, dropdown biệt thự `<10/10-20/20-30/>30 tỷ` + mục đích (nghỉ dưỡng cá nhân/đầu tư khai thác/cả hai) theo `landing-page/README.md`. LP: message match +1,0 · khoảng giá above-fold +0,8 · Zalo sticky +0,6 · form 4field+2dropdown +0,4 → **CVR 4,8%** (trần 6,0). Qualify 40%, contact 55% (dropdown+validate+SLA gọi <5', đã có văn bản thoả thuận sale). G0 pass trước khi bật.

**Bẫy T1 — RSA disapproved "Unreliable claims"** (headline `Cam Kết Sinh Lời 30%/Năm` do sale gửi): **0 click mất** vì §2.5-b7 quy định 2 RSA/ad group, RSA #1 (đã verify) vẫn served. Xử lý đúng gốc: không nộp lại nguyên bản, quét cụm cấm (`cam kết sinh lời`, `bao lãi`...) trên toàn asset (RSA khác, sitelink, LP, script Zalo sale), thay bằng headline đã verify, thêm assert cụm cấm vào script đếm ký tự §3.5.

**Bẫy T2 — yêu cầu advertiser verification** (deadline 30 ngày, 30 ngày không nộp = tạm ngưng tài khoản): đã nộp pre-flight từ D-7 (`campaign-setup` §1.1) → đây là bổ sung, nộp lại ĐKKD+MST+CCCD trong ≤48h, đóng băng ngân sách/cấu trúc trong lúc chờ. Duyệt xong tuần 3.

Kết quả D30: CVR LP 4,8%, qualify 40%, contact 55%, CPL-q **1.823.000₫** — sàn số học của phân khúc (CPC 35k cố định, không phải benchmark trung bình 1,56tr). #1+#3 đạt ~38 `Lead_Form_Raw`/30 ngày + contact >50% + ≥4 tuần → đủ điều kiện **SỐ** của `campaign-setup` §4.4 nhưng **không chuyển bidding** vì ECL chưa chạy (primary còn là form thô — bẫy optimize-to-quality, `tracking/README` luật #2).

## Bảng 12 tuần

| Tuần | Chi (₫) | Click | Lead-q | CPL-q (₫) | Bậc bidding | Ghi chú |
|---|---|---|---|---|---|---|
| 1 | 6.895.000 | 197 | 3,8 | 1.823.000 | 0 Max Clicks | RSA disapproved → sửa gốc, 0 click mất (2 RSA/ad group) |
| 2 | 6.895.000 | 197 | 3,8 | 1.823.000 | 0 | Yêu cầu verification bổ sung → nộp ≤48h, đóng băng ngân sách/cấu trúc |
| 3 | 6.895.000 | 197 | 3,8 | 1.823.000 | 0 | Verification duyệt; vòng negative nghi thức 3 lượt |
| 4 | 6.895.000 | 197 | 3,8 | 1.823.000 | 0 | Hết kỳ 1; CVR thật 4,8% trong dải đích 3-6%; scorecard tháng 1 |
| **D30** | — | — | — | — | — | **Keap ký xong → ECL bật** (`upload_ecl.py` chạy thật) |
| 5 | 6.895.000 | 197 | 4,0 | 1.716.000 | 0 | LP fix theo Clarity insight (dưới) → CVR 4,8%→5,1%. Primary vẫn `Lead_Form_Raw`, chờ D45 |
| 6 | 6.895.000 | 197 | 4,0 | 1.716.000 | 0 | Ổn định; tích luỹ conv 30 ngày cho gate D45 (~39/30 ngày ≥30) |
| **D45** | — | — | — | — | — | Đảo primary→`Lead_Contactable` **trước**, rồi bật Maximize Conversions. **Không tCPA** (cấm phân khúc) |
| 7 | 6.895.000 | 197 | 3,4 | 2.018.000 | 1 Max Conv (learning) | CVR ×0,85 (tuần học 1/2) — không đổi ngân sách/target |
| 8 | 6.895.000 | 197 | 3,4 | 2.018.000 | 1 (learning) | Tuần học 2/2. Báo cáo tháng 2: 85% lead gắn tag đúng SLA48h |
| **D60** | — | — | — | — | — | Learning hết → hiệu quả **×1,15 vĩnh viễn**. **G2 mở** (organic đẩy `xem_bang_gia`≥1.000 user/30 ngày). CPC +15% mùa nóng bắt đầu |
| 9 | 6.895.000 | 146* | 3,6 | 1.923.000 | 1 (ổn định) | Demand Gen 147.750₫/ngày (=15%, rút từ #1/#3) — **đã điền Excluded content keywords** → +5% lead-q |
| 10 | 6.895.000 | 146 | 3,6 | 1.923.000 | 1 | Ổn định; hiệu quả ×1,15 + LP fix bù gần hết phần CPC+15% |
| **D74** | — | — | — | — | — | Kiểm tCPA: chặn bởi **2 lý do độc lập** (dưới) → giữ Maximize Conversions |
| 11 | 6.895.000 | 146 | 3,6 | 1.923.000 | 1 | Không đổi bidding; #7 Discovery broad vẫn đóng (gắn tCPA, cấm phân khúc) |
| 12 | 6.895.000 | 146 | 3,6 | 1.923.000 | 1 | Chốt kỳ 3, tổng kết 90 ngày |

*click tuần 9-12 chỉ tính Search (837.250₫/ngày ÷ 40.250₫); Demand Gen không dùng công thức click/CVR, chỉ cộng +5% lead-q khi Excluded content keywords đã điền.

## Quyết định tại các mốc

| Mốc | Làm gì | Căn cứ doc |
|---|---|---|
| **D30** | Bật `upload_ecl.py` (Keap ký xong); `Lead_Contactable`/`Lead_Qualified` bắt đầu có dữ liệu thật. Cùng kỳ: 1 iteration LP theo Clarity insight — **replay cho thấy bounce ngay sau bảng giá, trước khi tới block pháp lý/sổ hồng riêng** (rào cản niềm tin lớn nhất của biệt thự nghỉ dưỡng — sợ giống condotel không sổ riêng) → chuyển block pháp lý lên ngay sau bảng giá thay vì cuối trang → CVR +0,3 (trong trần +0,4/kỳ). Không đổi bidding | `sim-rules-90` mốc D30 · `landing-page/README.md` §3 mục 4 (objection) · trần CVR luật bổ sung |
| **D45** | ≥30 `Lead_Form_Raw`/30 ngày ✓ (~39) + contact >50% ✓ → **chuyển ĐÚNG**: đảo primary sang `Lead_Contactable` TRƯỚC, rồi mới bật Maximize Conversions. **Không đặt tCPA** dù kỹ thuật đủ điều kiện — `research` §2 cấm tCPA phân khúc biệt thự/hạng sang vô điều kiện. Không đổi ngân sách trong 2 tuần learning | `campaign-setup` §4.4 · `journey-plan` §3.2 bậc 1 · `research` §2 |
| **D60** | Mở Demand Gen remarketing 147.750₫/ngày (đúng 15%, không vượt trần, rút từ #1/#3 giữ tỷ lệ 52,9:47,1) sau khi `xem_bang_gia` đạt 1.000 user/30 ngày qua organic/content (855 click/tháng của ads không tự đủ — đúng cảnh báo `journey-plan` §3.1 G2). **Điền Excluded content keywords** cấp tài khoản trước khi bật (negative Search không phủ inventory Demand Gen) | `journey-plan` §3.1 G2 · SCORECARD.md bài học #5 |
| **D74** | Maximize Conversions ổn ≥2 tuần ✓ (từ tuần 9) nhưng **KHÔNG chuyển tCPA**, vì **2 lý do độc lập, cộng dồn**: (1) `research` §2 cấm tCPA phân khúc này — vô điều kiện, không phụ thuộc gate; (2) ngay cả khi không có lệnh cấm, `Lead_Contactable` trailing 30 ngày (tuần 7-10) chỉ ~**17,7** — dưới ngưỡng ≥30 conv/30 ngày vì primary giờ là proxy nghiêm hơn `Lead_Form_Raw`. #7 `Discovery` broad cũng giữ đóng vĩnh viễn — `adgroup-map` gắn campaign này với tCPA, cấm tCPA kéo theo cấm broad test | `research` §2 · `campaign-setup` §4.4 · `journey-plan` §3.2 bậc 2 |

**Báo cáo tháng (research §8, rút gọn):** Kỳ 1: contact 55% ổn, CPL-q 1.823.000₫ là số duy nhất dùng được (chưa ECL). Kỳ 2: ECL sống từ D30, đảo primary đúng thứ tự tại D45, LP fix +0,3 CVR có insight cụ thể (không bịa), 85% lead đúng SLA48h. Kỳ 3: G2 mở đúng lúc + Excluded content keywords đủ, CPC+15% mùa nóng đã phản ánh vào CPL-q, tCPA bị chặn đúng 2 lần độc lập tại D74.

## Tổng 90 ngày

| Chỉ số | Giá trị |
|---|---|
| Tổng chi tiêu | **82.740.000₫** (985k/ngày × 84 ngày, không đổi tổng ngân sách lần nào) |
| Tổng click | ~2.158 |
| Tổng lead qualified | **44,3** |
| **CPL qualified blended** | **1.866.000₫** (vs kịch bản trung bình 1,56tr — cao hơn vì CPC 35-40k cố định + trần CVR 4,8-5,865% + qualify trần 40%, là sàn số học phân khúc, không phải lỗi vận hành) |
| Xu hướng CPL-q theo kỳ | 1.823.000 → ~1.867.000 (kỳ 2, có tuần học 2.018.000) → **1.923.000₫** (kỳ 3, CPC+15% gần như bị LP fix + hiệu quả ×1,15 bù lại) |
| Contact rate | 55% ổn định cả 90 ngày; % lead gắn tag đúng SLA48h từ D30: **85%** (giả định), 15% mất tag làm tín hiệu ECL mỏng hơn contact rate thật |
| Tổng lead liên hệ được (contactable) | ~60,0 · CPL contactable **~1.379.000₫** |
| Bậc bidding cuối kỳ | **Bậc 1 — Maximize Conversions**, primary `Lead_Contactable`, ECL chạy thật. **tCPA không bao giờ mở** ở round này |
| Gates đã mở | G0 ✓ (D0) · G2 ✓ (D60, Demand Gen ≤15% + Excluded content keywords) |
| Gates đóng, có lý do bằng số | G1 — breakeven CPL vẫn `[chưa điền]` (`PLAN` §6, chưa có phí môi giới/căn + tỷ lệ booking→HĐMB) → không tự đặt số thay user. G3 — cần tCPA ổn 2 tháng, cấm nên đóng theo cấu trúc vĩnh viễn. G4 (PMax) — lead qualified ~14,3/tháng (kỳ 3) vs ngưỡng ≥30 (`PLAN` §0.5); brand exclusion list cũng chưa set. G5 — cần ≥150tr, vẫn 30tr |

## 3 bài học

1. **Lệnh cấm phân khúc (`research` §2) và ngưỡng volume (`journey-plan` §3.1) là hai lý do độc lập chặn cùng một quyết định — phải kiểm cả hai, không dừng ở lý do đầu tiên tìm thấy.** Tại D74, dù không có lệnh cấm tCPA, `Lead_Contactable` trailing 30 ngày (~17,7) vẫn dưới 30 vì primary giờ nghiêm hơn `Lead_Form_Raw` cũ (~39) từng dùng để qua gate D45. Nếu chỉ kiểm một điều kiện sẽ dễ kết luận sai theo hướng nào cũng có vẻ hợp lý.
2. **Một iteration LP đúng insight (khách quan, có cơ chế cụ thể) đủ sức bù gần hết một cú sốc mùa vụ.** CVR 4,8%→5,1% (kỳ 2, insight bounce trước block pháp lý) qua hiệu quả bidding ×1,15 thành 5,865% ở kỳ 3 — gần bù trọn CPC+15%, nên CPL-q kỳ 3 (1.923.000₫) chỉ cao hơn kỳ 1 khoảng 5,5%, không phải 15% như CPC tự thân. Đòn bẩy CRO vẫn mạnh hơn mọi tối ưu bidding trong ngắn hạn, đúng nguyên tắc `landing-page/README.md`.
3. **90 ngày không mở thêm gate nào ngoài G2, và đó là kết quả đúng, không phải thiếu sót.** G1 kẹt vì thiếu 1 số duy nhất từ user (breakeven), G3 đóng theo cấu trúc (tCPA cấm), G4 đóng vì lead-q chưa đủ nửa ngưỡng dù ECL đã chạy thật 60 ngày. Kỷ luật gate đúng nghĩa là chấp nhận trần này thay vì đi tìm cách "kỹ thuật" để leo bậc — bậc 1 vẫn là trần đúng của phân khúc biệt thự/hạng sang, dù có chạy 90 ngày hay 900 ngày.
