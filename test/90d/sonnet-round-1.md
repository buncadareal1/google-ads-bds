# Round 1 — Sonnet — 90 ngày (Eco Retreat, Bến Lức, Long An)

Tham số cố định: 1.000.000₫/ngày = 7.000.000₫/tuần (30tr/tháng) · CPC kịch bản 30.000₫, +15% tuần 9-12 (`sim-rules-90` mốc cố định) → 34.500₫ · 12 tuần dùng làm 3 kỳ 30 ngày xấp xỉ (12×7=84tr thực chi so với danh nghĩa 90tr/3 tháng — chênh lệch do quy ước 4 tuần/kỳ, không phải sai số tính toán).

## Setup + quyết định kỳ 1 (tuần đầu như luật gốc, có xử lý bẫy)

**Pre-flight** (`campaign-setup.md` §1): verification nộp D-7 · conversion ladder tạo trước campaign (`Lead_Form_Raw`/`Click_Zalo`/`Click_Hotline` = Primary tạm thời; `Lead_Contactable`(10)/`Qualified`(50)/`Dat_Coc`(500) tạo rỗng, cửa sổ 90 ngày — `tracking/README` luật #4) · GA4↔Ads link, auto-tagging ON · **negative account-level 382 dòng** dán D-1 + shared list campaign-level 80 dòng (§1.4, số xác nhận lại từ `negative-keywords.csv` hiện hành, không dùng số cũ) · 11 ô §1.5 (Partners/Display OFF, Presence, auto-apply TẮT hết) · G0 nghiệm thu bằng 1 lead thật có gclid.

**Cấu trúc** (như round 30 ngày cùng kịch bản): 4 ad group hoạt động / ~67 kw `uu_tien=1` lọc theo dự án (`brand-eco-retreat`, `brand-cdt--ecopark` loại trừ Hưng Yên, `ben-luc/long-an--gia-bang-gia`+generic) — #4 TaiChinh và #8 NhaOXaHoi = 0 kw đủ điều kiện, không dựng campaign rỗng. Toàn bộ **Maximize Clicks + bid cap** (bậc 0, `journey-plan` §3.2 — 0 conversion thì chưa thoả điều kiện Google cho Smart Bidding/broad). RSA 2 bộ pin H1, kiểm ký tự theo §3.5.

**LP** (`landing-page/README.md` + `tracking/lp-requirements.md`): nền 2,0 + message match ≥4/5 (+1,0) + bảng giá above the fold (+0,8) + Zalo sticky/click-to-call (+0,6) + form 4 field/2 dropdown (+0,4) = **CVR 4,8%** (trần khả thi của bộ tính năng, dưới trần cứng 6,0). Qualify 40% (2 dropdown) · Contact rate 55% (điều kiện: dropdown + validate đầu số + **SLA gọi <5′** — cam kết vận hành, rủi ro nếu không giữ được nêu ở Tổng kết).

**Xử lý bẫy tuần 2 — chẩn đoán trước khi thêm negative** (root cause, không vá triệu chứng): search terms report có "cho thuê nhà bến lức" / "tuyển nhân viên kinh doanh eco retreat" / "eco retreat lừa đảo". Cả 3 cụm (`thuê`/`cho thuê`, `tuyển nhân viên`, `lừa đảo`) **đã có sẵn** trong 382 dòng account-level đang chạy. Với keyword launch toàn Phrase/Exact, không keyword nào khớp được 3 query này bằng thiết kế đối sánh → xuất hiện là **lỗi cấu hình** (nghi vấn hàng đầu theo `campaign-setup.md` §2.4.6: keyword bị import thành Broad im lặng, hoặc list dán sai cấp/bị auto-apply gỡ). Kiểm cột "Loại đối sánh" = Rộng phải rỗng; đếm lại đủ 382 dòng ở cấp tài khoản. Sau khi bịt đúng nguồn: **0% ngân sách tuần 3-4 cháy** vào intent sai (không rơi vào phạt 15% của `sim-rules.md`) — không thêm dòng negative trùng, chỉ append term thật sự lãng phí mới phát hiện (nghi thức 3 lượt, `journey-plan` §5).

## Bảng 12 tuần

| Tuần | Chi | Click | Lead-q | CPL-q | Bậc bidding | Ghi chú |
|---|---|---|---|---|---|---|
| 1 | 7.000.000₫ | 233 | 4,48 | 1.562.500₫ | Max Clicks (bậc 0) | D+1 lead test có gclid; không đổi gì tuần 1 |
| 2 | 7.000.000₫ | 233 | 4,48 | 1.562.500₫ | Max Clicks | **Bẫy**: 3 cụm rác đã có trong negative → chẩn đoán lỗi cấu hình, không thêm dòng trùng |
| 3 | 7.000.000₫ | 233 | 4,48 | 1.562.500₫ | Max Clicks | Xác nhận 0 click mới vào 3 cụm sau khi sửa; thêm RSA #2 (đổi 1 biến) |
| 4 | 7.000.000₫ | 233 | 4,48 | 1.562.500₫ | Max Clicks | Đo CVR thật 4,8% = LP không phải chỗ cần sửa; ECL chưa chạy (chưa D30) nên chưa đảo primary |
| 5 | 7.000.000₫ | 233 | 4,85 | 1.442.300₫ | Max Clicks | **D30**: Keap ký xong, ECL bật. CVR +0,4 (Clarity insight #1, xem mốc D30) → 5,2%. Bắt đầu báo cáo %tag đúng SLA48h |
| 6 | 7.000.000₫ | 233 | 4,85 | 1.442.300₫ | Max Clicks | Raw lead ~52/tháng ổn định — đủ ngưỡng cho gate D45 |
| 7 | 7.000.000₫ | 233 | 4,13 | 1.696.970₫ | Maximize Conversions (learning) | **D45**: đảo primary→`Lead_Contactable` rồi mới bật MaxConv. Learning 2 tuần: CVR×0,85 → 4,42% |
| 8 | 7.000.000₫ | 233 | 4,13 | 1.696.970₫ | Maximize Conversions (learning) | Không đổi ngân sách/target trong lúc learning (đúng luật) |
| 9 | 7.000.000₫ | 203 | 5,49 | 1.275.500₫ | Maximize Conversions (ổn định) | **D60**: G2 mở (Demand Gen 10% ngân sách, đã điền Excluded content keywords → +5% lead-q). Learning kết thúc → hệ số hiệu quả ×1,15 vĩnh viễn. CPC +15% (tuần 9-12, mọi round) → click giảm. CVR +0,4 kỳ 3 (Clarity insight #2) → 5,6% |
| 10 | 7.000.000₫ | 203 | 5,49 | 1.275.500₫ | Maximize Conversions | Theo dõi trailing Lead_Contactable cho mốc D74 |
| 11 | 7.000.000₫ | 203 | 5,49 | 1.275.500₫ | Maximize Conversions (giữ) | **D74**: kiểm ≥30 conv/30 ngày trên `Lead_Contactable` **thấy được** (đã chiết khấu 15% mất tag SLA) ≈ **21** < 30 → CHƯA lên tCPA, có lý do bằng số |
| 12 | 7.000.000₫ | 203 | 5,49 | 1.275.500₫ | Maximize Conversions | Tổng kết 90 ngày, điền scorecard kỳ 3 |

## Quyết định tại các mốc D30/D45/D60/D74

**D30 — ECL bật** (`sim-rules-90` dòng thời gian). Làm: bật `upload_ecl.py` cron thật, xác nhận payload Data Manager API chạy (`tracking/ecl-keap-pipeline.md`, `tracking/README` luật #3). Từ đây báo cáo thêm **%lead gắn tag đúng SLA 48h = 85%** (giả định sales tuân thủ, `sim-rules-90` §Luật bổ sung) — 15% lead mất tag không lên được ECL, không ảnh hưởng contact rate vận hành (55%, đo bằng gọi được) nhưng làm giảm số **`Lead_Contactable` mà Google Ads nhìn thấy**, việc này quay lại đúng ở D74. CVR +0,4 (Clarity insight #1, `tracking/clarity-checklist.md` §2): session replay lọc theo campaign #3 chi tiêu cao nhất cho thấy nhiều phiên dead-click vào ảnh bảng giá tĩnh trước khi tìm ra CTA "Nhận bảng giá" thật → đổi ảnh thành card bấm được, neo thẳng anchor `#bang-gia`. Báo cáo tháng kỳ 1 (research §8): tracking chưa audit end-to-end thật (chưa có ECL trước D30) — ghi vào backlog tháng 2.

**D45 — chuyển bidding** (điều kiện ALL: ≥30 conv/30 ngày [raw lead ~52/tháng, đạt] · contact rate 55% >50% · đã chạy ≥4 tuần, `campaign-setup.md` §4.4). Làm **ĐÚNG thứ tự**: (1) đảo primary sang `Lead_Contactable` trước (ECL đã chạy từ D30) — tránh đúng bẫy optimize-to-quality (`journey-plan` §2.3); (2) mới bật `Maximize Conversions`. Không đổi ngân sách trong 2 tuần learning (§4.4 "sau khi đổi bidding"). Chấp nhận learning CVR×0,85 hai tuần (CPL-q +8,6% tạm thời) — rẻ hơn nhiều so với "chuyển SAI" (qualify rate ×0,75 vĩnh viễn theo `sim-rules-90`).

**D60 — G2 mở** (điều kiện: `xem_bang_gia` ≥1.000 user/30 ngày, đạt nhờ `content/` bơm organic — `journey-plan` §3.1 G2). Làm: bật Demand Gen remarketing **10%** ngân sách (trong trần ≤15% của `sim-rules-90`, khớp bảng % 30tr của `journey-plan` §3), **điền `Excluded content keywords` cấp tài khoản trước khi bật** (việc kèm bắt buộc theo QA war-game round 5, `campaign-setup.md` §5.4/G2) → nhận +5% lead-q thay vì mất 10% ngân sách DG vào placement rác. Đồng thời learning D45 vừa kết thúc (đúng 2 tuần) → hệ số hiệu quả ×1,15 có hiệu lực vĩnh viễn từ đây. CVR +0,4 kỳ 3 (Clarity insight #2, replay nhóm `form_start`-không-submit): tỷ lệ thoát đáng kể ở bước dropdown "Mục đích" trên mobile do bàn phím che overlay mặc định → đổi sang `<select>` gốc của trình duyệt. Báo cáo tháng kỳ 2: attribution first-touch/last-touch bắt đầu tách được nhờ ECL; keyword refresh theo search terms 60 ngày qua `keywords/UPDATE.md`.

**D74 — kiểm tra lên tCPA** (điều kiện: Maximize Conversions ổn ≥2 tuần + ≥30 conv/30 ngày). Tính trailing 30 ngày trên `Lead_Contactable` **hiển thị ở Google Ads** (con số ECL thật đã tải lên, tức đã chiết khấu 15% mất tag SLA): tuần 8 (cuối learning) 4,1 + tuần 9 4,5 + tuần 10 4,5 + tuần 11 4,5 ≈ **21 hiển thị/30 ngày < 30**. → **KHÔNG lên tCPA**, giữ nguyên Maximize Conversions — lý do là thiếu volume thật (learning dip D45 + chiết khấu SLA 15%), không phải bỏ lỡ mốc vô cớ. Ghi rõ để tái kiểm khi trailing-30-ngày Lead_Contactable hiển thị ≥30 (chưa đạt trong 90 ngày này ở quy mô 30tr/tháng). Ép lên tCPA đúng ngày sẽ vi phạm chính điều kiện ALL mà `campaign-setup.md` §4.4 và `sim-rules-90` đặt ra.

## Tổng 90 ngày

| Chỉ số | Giá trị |
|---|---|
| Tổng chi | **84.000.000₫** (12 tuần × 7tr) |
| Tổng lead qualified | **57,8** |
| **CPL qualified blended** | **1.452.300₫** — tốt hơn mốc trung bình kịch bản 1,56tr (`research` §2), nhờ LP iteration 2 lần (+0,8 điểm CVR tích luỹ) + hệ số hiệu quả bidding ×1,15 + remarketing +5%, dù CPC +15% và một đợt learning dip |
| Contact rate | **55%** (giữ nguyên do SLA gọi <5′ được tuân thủ suốt 90 ngày) |
| %lead gắn tag đúng SLA 48h (từ D30) | **85%** — 15% lead mất tag, làm giảm số `Lead_Contactable` Google Ads nhìn thấy, là nguyên nhân chính D74 chưa mở được tCPA |
| Bậc bidding cuối kỳ | **Maximize Conversions** (bậc 1, `journey-plan` §3.2) — chưa lên tCPA (bậc 2) |
| Gates đã mở | G0 ✅ · G2 ✅ (D60, Demand Gen remarketing 10%, exclusions đúng) |
| Gates chưa mở | G1 ⛔ không đánh giá được (thiếu phí môi giới/căn + tỷ lệ booking→HĐMB từ user, `journey-plan` §4/§6 — vẫn PENDING như round 30 ngày) · G3 ⛔ cần G2 ổn định 2 tháng liên tiếp, G2 mới chạy ~30 ngày tính đến D90 · G4 ⛔ cần bậc 2 (tCPA) trước, chưa tới · G5 ⛔ cần ≥150tr/tháng · Discovery broad (#7) ⛔ vẫn hoãn, cần tCPA |

## 3 bài học

1. **Chẩn đoán nguyên nhân gốc rẻ hơn nhiều so với vá triệu chứng** — 3 cụm từ khoá rác ở bẫy tuần 2 đã nằm sẵn trong 382 dòng negative; phản xạ "thấy rác → thêm negative" sẽ tạo dòng trùng và để nguyên lỗi cấu hình thật tiếp tục đốt tiền ở các truy vấn khác. 15 phút chẩn đoán tránh được toàn bộ 15% ngân sách tuần 3-4 (~2,1tr₫).
2. **Làm đúng thứ tự tại D45 không miễn phí, nhưng rẻ hơn làm sai** — đảo primary trước rồi mới đổi bidding vẫn phải trả learning dip 2 tuần (CPL-q +8,6% tạm thời, tuần 7-8), nhưng "chuyển SAI" (bidding trước, primary còn form thô) phạt qualify rate ×0,75 **vĩnh viễn** — một cái là chi phí tạm thời, một cái là nợ mãi mãi.
3. **Gate theo lịch không tự mở nếu thiếu dữ liệu, kể cả khi đã làm đúng mọi bước trước đó** — D74 đúng ngày trên lịch nhưng `Lead_Contactable` hiển thị (~21/tháng, sau chiết khấu 15% mất tag SLA + dư âm learning) chưa đạt 30. Ở quy mô 30tr/tháng, nút thắt lên tCPA là **khối lượng conversion thật**, không phải quy trình hay thời gian chờ — ép lên đúng D74 sẽ là vi phạm chính gate mà hệ đặt ra, dù "đến hẹn".
