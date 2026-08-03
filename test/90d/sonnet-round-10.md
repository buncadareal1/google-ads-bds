# Round 10 — Sonnet — 90 ngày

Kịch bản: 30tr₫/tháng cố định suốt 90 ngày, Eco Retreat (Bến Lức), CPC nền 30k₫. Kỳ 1 (tuần 1-4) = y nguyên `test/round-10.md` (không sửa file đó, chỉ trích số đã QA) — tuần 2 vẫn là bẫy gốc: 2 sàn F2 bid `eco retreat`, CPC brand ×2, IS 85%→55%, 1 sàn để tên trong headline. Kỳ 2-3 áp thêm mốc cố định của `test/sim-rules-90.md`.

## Giả định mô hình (khai rõ — không có công thức gốc cho các mốc mới)

| Giả định | Giá trị | Vì sao |
|---|---|---|
| Hệ số hiệu quả D45 "×1,15 vĩnh viễn" | Áp vào **qualify rate** (40%→46%), không áp vào CVR | Đối xứng với nhánh "sai" (qualify rate ×0,75) — cùng một đòn bẩy, và đúng bản chất: primary=`Lead_Contactable` khiến bidding tìm traffic *dễ liên hệ hơn*, thứ quyết định qualify chứ không quyết định CVR-click→lead |
| CPC Demand Gen | 20k₫ (trước heat), 23k₫ (sau heat T9-12) | Remarketing thường rẻ hơn cold search; sim không cho số riêng cho DG |
| Ad mạo nhận bị gỡ ~tuần 6 | IS phục hồi 64%→66% | Follow-up của hồ sơ misrepresentation nộp qua CĐT ở tuần 3 (round-10.md); không có mốc luật riêng cho việc này, ghi rõ là suy luận vận hành |
| Blended CPC giữ ~37,7k tuần 5-8 (cap 47k không đổi) | Không leo thang thêm | Đã chứng minh ở round-10.md: leo cap thêm làm IS *tụt* khi ngân sách cố định |

## Setup + quyết định kỳ 1

Pre-flight, cấu trúc campaign (#1 `Brand_DuAn` 475k/ngày cap 35k · #2 `Brand_CDT` 75k/ngày cap 35k · #3 `KhuVuc_GiaoDich` 450k/ngày cap 40k), LP spec (CVR 4,8% trần 4 adder), conversion ladder — **y nguyên `test/round-10.md`**, đã QA.

**Xử lý bẫy tuần 2 (tóm tắt, chi tiết ở round-10.md):** guard `CPC brand >2× baseline` → xác minh qua Auction Insights + Transparency Center (browser thật) **trước khi** tăng bid (PLAYBOOK 2.3: QS rẻ hơn bid) → cap 35k→42k→47k (2 bước ≤20%/lần, `campaign-setup` §4.4) → budget #1 +18,9% / #3 −20% (1 lần, không reset learning) → RSA thứ 2 đánh vào thuộc tính, không vào tên → gửi hồ sơ **ủy quyền cho CĐT** (F1 không tự khiếu nại được, `PLAYBOOK` 4.4 + `research` §7) vì 1 sàn dùng "Eco Retreat" trong headline có dấu hiệu mạo nhận CĐT (misrepresentation, nặng hơn trademark thường). **Không** mở campaign bid tên đối thủ/sàn (IS 55%→64% cuối kỳ 1, fail điều kiện #1 của `journey-strategy` §3.1: cần ≥90%).

## Bảng 12 tuần

| Tuần | Chi (k₫) | Click | Lead-q | CPL-q (k₫) | Bậc bidding | Ghi chú |
|---|---|---|---|---|---|---|
| 1 | 7.000 | 233,3 | 4,5 | 1.563 | Max Clicks + cap | Setup, negative D1, không đổi gì (`campaign-setup` §4.1) |
| 2 | 6.767 | 199,5 | 3,8 | 1.766 | Max Clicks + cap | **Bẫy**: F2 vào đấu, IS 85→55%. Guard → verify → cap 35k→42k (D3, +20%) |
| 3 | 6.793 | 185,0 | 3,6 | 1.912 | Max Clicks + cap | Cap 42→47k (+11,9%), #1 +18,9%/#3 −20%, RSA2, gửi ủy quyền CĐT |
| 4 | 7.000 | 185,6 | 3,6 | 1.964 | Max Clicks + cap | Ổn định, IS 64%. Không đổi (ECL chưa chạy → không đảo primary) |
| 5 | 7.000 | 185,7 | 3,9 | 1.813 | Max Clicks + cap | **D30**: Keap ký, ECL bật (`upload_ecl.py` chạy). CVR +0,4 (Clarity #1) |
| 6 | 7.000 | 185,7 | 3,9 | 1.813 | Max Clicks + cap | Giữ nguyên; IS ~66% (giả định: ad mạo nhận bị gỡ) |
| 7 | 7.000 | 185,7 | 3,3 | 2.134 | Maximize Conv. (learning 1/2) | **D45**: đảo primary→`Lead_Contactable`, bật Maximize Conversions. Learning CVR×0,85 |
| 8 | 7.000 | 185,7 | 3,3 | 2.134 | Maximize Conv. (learning 2/2) | Learning tuần 2/2, không đụng gì thêm |
| 9 | 7.000 | 171,7 | 4,1 | 1.695 | Maximize Conv. + DG | **D60**: G2 mở (content bơm 1.000 user), DG 72k/ngày (cắt #3 −20%, ≤15% trần). Qualify rate +15% vĩnh viễn. Heat CPC+15% bắt đầu (T9-12) |
| 10 | 7.000 | 171,7 | 4,5 | 1.573 | Maximize Conv. + DG | CVR +0,4 (Clarity #2 — kéo block chính sách lên trên bảng giá) |
| 11 | 7.000 | 171,7 | 4,5 | 1.573 | Maximize Conv. + DG | **D74**: contactable/tháng ~21 <30 → **KHÔNG** lên tCPA, giữ Maximize Conversions |
| 12 | 7.000 | 171,7 | 4,5 | 1.573 | Maximize Conv. + DG | Ổn định cuối kỳ, không đổi gì |

## Báo cáo tháng (`research/google-ads-bds-vn.md` §8, 5 dòng/kỳ)

**Kỳ 1 (D1-30):** Chi 27.560k · Click 803,4 · Lead-q 15,5 · CPL-q 1.786k · Contact 55%. Sự kiện: bẫy F2 bid brand, xử lý bằng cap+budget theo bậc, không reset learning. Chuyển giai đoạn bidding: chưa (ECL chưa chạy). Attribution: chưa audit — gclid test D+1 pass, chưa có volume đủ để audit tháng thật.

**Kỳ 2 (D31-60):** Chi 28.000k · Click 743 · Lead-q 14,4 · CPL-q ~1.944k (kéo lên bởi 2 tuần learning D45). Contact 55%, **85% lead gắn tag đúng SLA 48h từ D30** (15% mất tag — nhiễu tín hiệu ECL, chưa ảnh hưởng contact rate đo được). Chuyển giai đoạn bidding: **Maximize Conversions** (D45, đúng thứ tự — đảo primary trước). Keyword: chưa research mới (đẩy `keyword-planner` nếu cần). Refresh creative: RSA2 vẫn dùng từ kỳ 1, chưa thêm.

**Kỳ 3 (D61-90):** Chi 28.000k · Click 686,8 · Lead-q 17,6 · CPL-q ~1.591k (phục hồi nhờ qualify +15% và DG, dù CPC heat +15%). Contact 55%, tag SLA 48h vẫn 85%. Chuyển giai đoạn bidding: **giữ nguyên** ở D74 (contactable/tháng chưa đủ 30). G2 (Demand Gen) mở đúng thủ tục — đã điền `Excluded content keywords`. Tính lại CPL target: vẫn treo, thiếu phí môi giới/căn từ user (`journey-plan` §6).

## Quyết định tại các mốc

**D30 — ECL bật.** Hành động: chỉ bật upload, **không** đổi bidding ngay (dù điều kiện kỹ thuật §4.4 "Max Clicks→Maximize Conversions" đã đủ từ tuần 4) — đợi đúng mốc kịch bản D45 để có ≥2 tuần dữ liệu contactable thật trước khi đảo primary, tránh đảo dựa trên 0-vài ngày dữ liệu. Song song: bắt đầu báo cáo % tag đúng SLA 48h (85%, theo giả định sim).

**D45 — chuyển bidding ĐÚNG thứ tự.** Điều kiện đủ: ≥30 conv/30 ngày (raw form ~38-48/tháng, thoả từ kỳ 1), contact rate 55% >50%, chạy ≥4 tuần. Làm đúng 2 bước `campaign-setup` §4.4: (1) đảo primary→`Lead_Contactable`, (2) bật Maximize Conversions — **không** làm ngược (primary vẫn form thô thì bidding mua rác, phạt qualify×0,75 vĩnh viễn theo sim-rules-90). Nhận phạt tạm thời đã biết trước: learning 2 tuần CVR×0,85 (tuần 7-8), đổi lấy qualify rate 40%→46% vĩnh viễn từ tuần 9 — đánh đổi hợp lý vì phạt là tạm, thưởng là vĩnh viễn. Nhắc lại: brand IS ~66% <90% → **vẫn không** mở campaign tên đối thủ (`journey-strategy` §3.1 điều kiện #1 fail).

**D60 — G2 mở, Demand Gen.** Điều kiện: `xem_bang_gia` đạt 1.000 user/30 ngày qua content/organic (ngoài phạm vi ads — tự ads không bao giờ đủ: kỳ 1 chỉ 803 click/28 ngày, dù 100% xem bảng giá vẫn <1.000). Mở **72k/ngày (7,2% ngân sách, dưới trần 15%)**, lấy từ cắt #3 đúng **1 lần −20%** (450→360 đã cắt kỳ 1; kỳ này cắt tiếp 360→288, không vi phạm luật ±20%/lần) — chọn dưới trần 15% vì #3 vẫn là hedge tự nhiên (không bị tấn công), rút quá tay là bỏ phòng thủ khu vực để nuôi remarketing chưa chứng minh ROI. **Điền `Excluded content keywords`** ngay khi tạo (journey-plan §3 G2 note) → nhận +5% lead-q thay vì mất 10% ngân sách DG vào placement rác.

**D74 — kiểm tra trước khi lên tCPA, KHÔNG lên.** Điều kiện `campaign-setup` §4.4: Maximize Conversions ổn ≥2 tuần (thoả, đã chạy từ tuần 7) **và** ≥30 conv/30 ngày ổn định. Nhưng "conv" bây giờ là primary hiện tại = `Lead_Contactable`, không phải form thô: leadraw tuần 9-11 ~9,6/tuần × contact 55% × ~4,3 tuần/tháng ≈ **21 contactable/tháng — dưới 30**. Quyết định: **giữ Maximize Conversions**, không ép tCPA dù đúng ngày hẹn kịch bản — số học của chính conversion đang là primary chưa đủ, không phải "sắp đủ nên cứ bật".

## Tổng 90 ngày

| Chỉ số | Giá trị |
|---|---|
| Tổng chi | **83.560k₫** (93% của 90tr trần — 2 tuần hụt IS kỳ 1 không thu hồi được) |
| Tổng click | 2.233,0 · CPC blended **37,4k** (nền 30k, +25% do bid war + heat) |
| Tổng lead raw | 112,1 |
| Tổng lead qualified | **47,5** |
| **CPL qualified blended** | **1.759k₫** (mốc tham chiếu 1,56tr → **+13%**, cải thiện nhẹ so với snapshot kỳ 1 riêng +14%) |
| Contact rate | **55%** suốt 90 ngày (không đổi — đúng luật gốc) |
| % lead tag đúng SLA 48h (từ D30) | **85%** — 15% lead mất tag, làm nhiễu tín hiệu ECL nhưng không đổi contact rate đo được |
| Brand IS | 85% → 55% (bẫy) → 64% (cuối kỳ1) → ~66% (kỳ2, gỡ ad mạo nhận) → ~60-62% (kỳ3, heat nén lại) — **chưa từng chạm 90%** |
| Bậc bidding cuối kỳ | **Maximize Conversions** (primary `Lead_Contactable`) + Demand Gen remarketing 7,2% ngân sách — **chưa** tCPA |
| Gates đã mở | G0 ✅ · G1 ❌ (chưa có CPL target từ user) · **G2 ✅** (D60) · G3 ❌ · G4 ❌ (PMax cần ≥30 lead-qualified/tháng, kỳ 3 mới ~19,3/tháng) · G5 ❌ |
| Campaign tên đối thủ | ❌ đóng suốt 90 ngày — IS không lần nào ≥90% |

## 3 bài học

1. **Nâng cap không mua lại IS còn đúng cả khi không có kẻ tấn công mới.** Heat thị trường tuần 9-12 (+15% CPC, áp cho mọi round, không phải bẫy) tự nó nén IS từ ~66% xuống ~60-62% dù cap giữ nguyên 47k — cùng cơ chế toán học đã chứng minh ở round-10.md (ngân sách cố định + giá lên = ít click hơn ở cùng vị trí). Kết luận: phòng thủ brand ở ngân sách cố định là một **trạng thái cần bảo trì liên tục**, không phải việc làm một lần rồi xong.
2. **Đảo primary sang chất lượng cao hơn làm SỐ ĐẾM conversion tụt, dù chất lượng tăng — và gate tiếp theo đo bằng đúng con số đã tụt đó.** Sau D45, "conversion" mà Google Ads đếm để xét tCPA là `Lead_Contactable` (~21/tháng), không phải form thô (~40-48/tháng đã dùng để mở Maximize Conversions). Ngưỡng ≥30 không tự động thoả chỉ vì đã thoả ở bước trước với một định nghĩa conversion khác. Vận hành đúng nghĩa là đọc lại điều kiện bằng đúng chỉ số đang được coi là primary tại thời điểm đó, không tái dùng số cũ.
3. **G2 (remarketing) là gate duy nhất không thể tự mở bằng ads ở 30tr/tháng — nó cần content/organic chạy song song.** 803 click/28 ngày ở kỳ 1 chứng minh: kể cả 100% traffic ads xem bảng giá cũng không chạm 1.000 user/30 ngày. Khi D60 hoàn thành nhờ nguồn ngoài ads, việc còn lại chỉ là **kỷ luật thực thi nhỏ** (điền `Excluded content keywords`, không rút quá 20%/lần) — nhưng thiếu nguồn ngoài đó thì gate treo vĩnh viễn bất kể vận hành ads giỏi đến đâu.

**Giới hạn của bản 90 ngày này:** mọi mốc D30/D45/D60/D74 và hệ số ×1,15/×0,75/×0,85/+15%/+5%/−10% đều lấy nguyên văn từ `test/sim-rules-90.md`; phần agent tự quyết là **áp hệ số vào lever nào** (đã khai ở bảng giả định) và **thời điểm/độ lớn** các bước cắt ngân sách/CVR-iteration — không có số nào ngoài công thức + giả định đã nêu.
