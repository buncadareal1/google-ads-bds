# Round 3 — Sonnet — 90 ngày
Kịch bản: Click tặc · 30tr₫/tháng · căn hộ TP.HCM · CPC 35.000₫. Tiếp nối `test/round-3.md` (4 tuần) — dùng lại nguyên setup + tuần 1-4, mở rộng theo mốc `sim-rules-90.md`.

## Setup + quyết định kỳ 1

**Cấu trúc (căn cứ số học, không khẩu vị — `campaign-setup` §2.3):** ở CPC 35k, #1 `Brand_DuAn` (550k/ngày, cap 20k) nuôi 2 dự án (Lumiere Midtown, Masteri Grand View); #3 `KhuVuc_GiaoDich` (450k/ngày, cap 35k) 1 ad group `thu-duc--gia-bang-gia`. #2/#4/#8/#7/RMKT hoãn (dồn quỹ vào #1/#3, không tăng tổng — khớp `journey-plan` §3 "campaign <15-30 conv/tháng thì gộp"). Negative 386 account-level + 80 campaign-level (biến thể không dấu đã kiểm). Conversion ladder đủ 6 action, Count=Một, cửa sổ 90 ngày; ngày 1: raw form + phone + zalo = Chính (chỉ để thấy số), 3 action offline khai rỗng. 11 ô §1.5 áp đủ. LP: message match +1,0 · bảng giá above-fold +0,8 · Zalo sticky +0,6 · form 4field+2dropdown +0,4 → **CVR 4,8%** (trần 6,0). Qualify 40% (2 dropdown), contact 55% (dropdown+validate+SLA gọi <5'). G0 pass trước khi bật.

**Bẫy tuần 2 (căn cứ `sim-rules-90.md` "sự kiện riêng vẫn xảy ra đúng tuần"):** CTR brand 7%→19%, dải IP hẹp 21-23h, bounce ~100% <3s, conversion phẳng ⇒ rác cấp tài khoản ≈30%. Xử lý đúng thứ tự `research` §5, không mua tool: (1) đọc Invalid clicks, chờ 48h Google tự lọc+hoàn tiền; (2) IP exclusion dải 21-23h (trần 500/campaign, dán cả #1 và #3); (3) siết ad schedule 05:00-21:00. Không cắt ngân sách, không sửa LP, không thêm negative (rác nằm trên chính brand keyword) — 3 việc không làm đúng bằng 3 việc đã làm. Rác còn **8% dư** từ tuần 3, giữ nguyên làm baseline vận hành hết kỳ (research §5: <10% invalid là bình thường, không theo đuổi 0%).

## Bảng 12 tuần

| Tuần | Chi (tr) | Click | Lead-q | CPL-q (tr) | Bậc bidding | Ghi chú |
|---|---|---|---|---|---|---|
| 1 | 7,00 | 200 | 3,84 | 1,82 | Max Clicks | Setup G0 pass; không đổi gì tuần 1 (`campaign-setup` §4.1) |
| 2 | 7,00 | 162 | 3,11 | 2,25 | Max Clicks | 🚨 BẪY click tặc — crowding-out, không phải đốt thêm tiền (ngân sách ngày chặn cứng) |
| 3 | 7,00 | 184 | 3,53 | 1,98 | Max Clicks | Xử lý xong theo thứ tự trên; rác còn 8% dư |
| 4 | 7,00 | 184 | 3,53 | 1,98 | Max Clicks | CVR thật 4,8%>2% → không sửa LP; T6 báo cáo tháng 1 |
| 5 | 7,00 | 184 | 3,75 | 1,86 | Max Clicks | **D30**: Keap ký, ECL bật (upload_ecl chạy); LP fix theo Clarity insight → CVR +0,3 = 5,1% |
| 6 | 7,00 | 184 | 3,75 | 1,86 | Max Clicks | Ổn định, chuẩn bị điều kiện D45 (≥30 conv raw/30 ngày) |
| 7 | 7,00 | 184 | 3,19 | 2,19 | MaxConv (learning ×0,85) | **D45**: đảo primary→`Lead_Contactable`, bật Maximize Conversions; mở #7 Discovery broad+tCPA (50k rút từ #3) |
| 8 | 7,00 | 184 | 3,19 | 2,19 | MaxConv (learning ×0,85) | Tuần learning thứ 2 — không đụng ngân sách/target (`research` §4) |
| 9 | 7,00 | 160 | 3,94 | 1,78 | MaxConv (×1,15 vĩnh viễn) | **D60**: G2 mở (organic đẩy `xem_bang_gia`≥1000u/30d), bật Demand Gen 100k/ngày (rút từ #1) — đã điền Excluded content keywords → +5% lead-q. CPC +15% (mùa nóng T9-12) |
| 10 | 7,00 | 160 | 3,94 | 1,78 | MaxConv | Ổn định — hiệu suất bù gần đúng phần CPC tăng |
| 11 | 7,00 | 160 | 3,94 | 1,78 | tCPA (CPA-q +15%) | **D74**: MaxConv ổn ≥2 tuần + ≥30 conv → chuyển tCPA đúng ±15% |
| 12 | 7,00 | 160 | 3,94 | 1,78 | tCPA | Ổn định kỳ 3, tổng kết 90 ngày |

## Quyết định tại các mốc

**D30 — chỉ bật ECL, KHÔNG đổi bidding.** `upload_ecl.py` cron chạy, `Lead_Contactable`/`Lead_Qualified` bắt đầu có dữ liệu (`sim-rules-90` mốc D30). Từ đây báo cáo thêm **% lead gắn tag đúng SLA 48h**: giả định sales tuân thủ 85% → 15% lead mất tag. Hệ quả: contactable lead vào Ads qua ECL chỉ ≈85% số thật (~4,4/tuần thay vì 5,2) — vẫn đủ vì gate D45 xét trên conversion primary hiện tại (raw form), không xét trên số ECL còn mỏng. Cùng kỳ: 1 iteration LP theo Clarity insight — **rage-click ở dropdown "Mục đích" trên mobile 390px** (nhãn 4 lựa chọn tràn dòng, 22% session bấm lại >3 lần) → rút gọn nhãn + tăng touch target → CVR +0,3 (trong trần +0,4/kỳ, `sim-rules-90` luật bổ sung). Không làm thêm iteration thứ 2 trong kỳ — giữ nguyên tắc "1 hypothesis/tuần" (`research` §8), tránh trộn biến số.

**D45 — đủ điều kiện (lead raw ổn định ≈37-40/30 ngày ≥30) → chuyển ĐÚNG thứ tự** (`campaign-setup` §4.4, `journey-plan` §3.2 bậc 1): (1) đảo primary sang `Lead_Contactable` **trước**; (2) bật Maximize Conversions; (3) mở `BDS_Search_Discovery` (#7) broad + tCPA, 50k/ngày rút từ #3, không tăng tổng. Learning 2 tuần CVR ×0,85 (tuần 7-8), sau đó hệ số hiệu quả ×1,15 vĩnh viễn (tuần 9+). Không đổi ngân sách trong 2 tuần learning.

**D60 — G2 mở** (audience đủ ngưỡng nhờ organic/content, không phải nhờ click ads — 730-2.100 click/12 tuần tự nó không đủ, khớp cảnh báo `journey-plan` §3.1 G2). Bật Demand Gen **100k/ngày = 10% ngân sách** (trong trần ≤15%, rút từ #1, tái dùng quỹ đã dành sẵn theo `campaign-setup` §2.1). Việc kèm bắt buộc: điền **Excluded content keywords** cấp tài khoản (negative account-level không phủ YouTube/Display của Demand Gen) → tránh 10% ngân sách DG cháy vào placement rác, đổi lại +5% lead-q remarketing.

**D74 — đủ điều kiện (MaxConv ổn ≥2 tuần từ tuần 7, ≥30 conv/30 ngày) → chuyển tCPA** = CPA-q lịch sử (≈1,38tr, tính từ contactable/30 ngày trước switch) **+15%** ≈ 1,58tr, đúng biên ±15% (không phạt reset). #7 giữ nguyên tCPA riêng đã mở từ D45.

## Tổng 90 ngày

| Chỉ số | Giá trị |
|---|---|
| Tổng chi (12 tuần × 7,00tr) | **84,0tr₫** (~84 ngày lịch tuần, tương đương 3 kỳ ~28 ngày) |
| Tổng lead qualified | **43,7** |
| CPL qualified blended | **1,92tr₫** |
| Contact rate vận hành | 55% (không đổi cả kỳ) — riêng % lead gắn tag đúng SLA 48h từ D30: **85%** (giả định), 15% mất tag làm tín hiệu ECL nuôi Maximize Conversions mỏng hơn contact rate thật cho thấy |
| Bậc AI cuối (`journey-plan` §3.2) | **Bậc 2** — tCPA + ECL chạy thật + broad test (#7) đang chạy |
| Gate đã mở | G0 ✅ · G2 ✅ (D60) |
| Gate không kết luận được | G1 — điều kiện là "CPL ≤ mục tiêu" nhưng breakeven (`journey-plan` §4) vẫn `[điền]`, chưa có phí môi giới/căn + tỷ lệ booking→HĐMB |
| Gate đóng, có lý do bằng số | G3 (cần tCPA ổn **2 tháng liên tiếp**, mới có ~2 tuần) · G4 (cần ≥30 lead qualified/**tháng**, thực tế ~15,8/tháng — PMax vẫn chưa tới lượt dù ECL đã chạy) · G5 (cần ≥150tr, ngân sách vẫn 30tr) |

## 3 bài học

1. **SLA gắn tag (85%) là trần ẩn của tín hiệu ECL, kể cả khi contact rate vận hành (55%) vẫn khoẻ.** `Lead_Contactable` chảy vào Maximize Conversions chỉ bằng ~85% số lead liên hệ được thật — "ECL đã bật" (D30) không đồng nghĩa "ECL đủ tín hiệu" cho smart bidding học đúng. Theo dõi % gắn tag đúng 48h phải đứng cạnh contact rate trong báo cáo tuần, không phải chỉ số phụ.

2. **Thời điểm xảy ra sự kiện quyết định mức độ nguy hiểm ngang với cách xử lý.** Bẫy click tặc rơi vào tuần 2 — trước D45 — nên Max Clicks hấp thụ trọn vẹn, không có gì để "reset learning" và không cần thủ tục Data exclusion. Nếu cùng sự kiện rơi vào tuần 9-10 (sau khi Maximize Conversions đã sống), nó vừa nhiễm dữ liệu huấn luyện đang chạy vừa đụng ngay giai đoạn thị trường nóng CPC+15% — thiệt hại sẽ cộng dồn hai lớp thay vì một. Bài học vận hành: giữ Max Clicks càng lâu trong giai đoạn còn nghi ngờ chất lượng traffic càng an toàn, bất kể đã "đủ điều kiện kỹ thuật" để lên smart bidding.

3. **90 ngày sạch + ECL chạy thật vẫn không đủ mở G4 — vì đó là bài toán số học, không phải kỷ luật.** Lead qualified ổn định quanh 15,8/tháng, dưới xa ngưỡng nội bộ 30 lead-q/tháng cho PMax (`PLAN.md` §0.5) dù mọi mốc D30/D45/D60/D74 đều xử lý đúng sách. Ở ngân sách 30tr với CPL-q ~1,9tr, không cách vận hành nào kéo lead-q lên gấp đôi trong 3 tháng — đòn bẩy duy nhất còn lại là tăng ngân sách (mở khoá bậc 60tr/150tr ở `campaign-setup` §5), không phải siết quy trình thêm nữa.
