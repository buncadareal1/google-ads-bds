# SCORECARD — War-game 10 vòng ads giả lập (2026-07-28)

Chấm bởi Fable (PM/QA) theo rubric `test/sim-rules.md` (100đ). Mọi số mô phỏng deterministic từ
mô hình research — test đo **chất lượng quyết định vận hành**, không đo thị trường thật.

## Bảng điểm

| Vòng | Kịch bản | Điểm | Lead-q | CPL-q | Contact | Bẫy tiêm | Kết quả bẫy |
|---|---|---|---|---|---|---|---|
| 1 | Baseline 30tr | **97** | 17,9 | 1.563k | 55% | Search terms rác | ✅ Nhận ra sự kiện tự mâu thuẫn → audit config, thêm 0 negative |
| 2 | 60tr + PMax cám dỗ | **97** | 37,8 | 1.460k | 55% | Rep mời PMax + auto-apply | ✅ Từ chối 6 căn cứ; kiểm auto-apply TRƯỚC khi gọi lại |
| 3 | Click tặc | **93** | 14,0 | 2.000k* | 55% | Rác 30% | ✅ 4 bước đúng thứ tự, 0₫ tool; insight crowding-out |
| 4 | Disapproved + verification | **94** | 15,1 | 1.823k* | 55% | Copy "cam kết sinh lời" + deadline 30 ngày | ✅ Sửa gốc cả LP/script; verification thành nộp bổ sung |
| 5 | Scale 150tr hợp lệ | **95** | 58 | 1.840k | 58% | AI Max × portfolio xung đột; PMax quên exclusions | ✅ Né cả hai; mùa vụ ghi đè scale |
| 6 | Xuyên Tết | **94** | 11,7 | 1.651k | 55% | Tắt hẳn = reset learning | ✅ Cắt 3 bậc −48,8%, chứng minh tắt hẳn không lợi |
| 7 | Contact rate sập | **96** | 17,2 | 1.630k | 47%→100%/lead-được-gọi | 2 nguyên nhân triệu chứng giống nhau | ✅ Loại nhánh bằng số trước khi đọc lead; "mẫu số vỡ" |
| 8 | Thắng nhưng nghẽn budget | **95** | 25,1 | 1.354k | 57% | Nhảy vọt +48% | ✅ 2 nhịp +20% cách 4 ngày + xin duyệt user |
| 9 | Đất nền lead rác | **94** | 14,1 | 1.987k* | 55% | Tăng tiền/đổi bid thay vì nhận diện phân khúc | ✅ Kill rule theo chi tiêu lũy kế; pause nhánh không pause campaign |
| 10 | Bid war brand | **95** | 15,4 | 1.786k* | 55% | Bid ngược tên đối thủ khi IS 55% | ✅ Từ chối (IS<90% + đang thua 2 trục); chứng minh tăng bid không mua lại IS |

\* CPL-q cao là **trần số học của kịch bản** (CPC/segment bị chốt), không phải lỗi vận hành — đã verify công thức từng bài.

## ĐIỂM HỆ THỐNG: **95,0/100** — Bẫy né được: **10/10**

Phân rã theo rubric (trung bình): Pre-flight 18,9/20 · Kỷ luật bidding 19,8/20 · Xử lý sự kiện 19,5/20 · Đo lường 14,3/15 · Kỷ luật gate 15/15 (tuyệt đối — không vòng nào mở gate sai, kể cả khi "đủ điều kiện bề mặt") · Kinh tế 8,7/10.

Hành vi lặp lại đáng giá nhất: **cả 10 vòng đều từ chối lên smart bidding dù đủ điều kiện kỹ thuật**, vì primary còn là form thô khi ECL chưa chạy — tức bài học "optimize-to-quality trap" đã ngấm vào mọi ngóc ngách hệ thống.

## 9 lỗi hệ thống war-game bắt được → đã vá ngay (2026-07-28)

1. 🔴 **Negative `bao` chặn 599 kw launch** (+`anh` 42, `báo` chặn "báo giá") — sinh từ script biến thể không dấu. Vá: xóa 3, thay bằng cụm an toàn (`đọc báo`, `hinh anh`), hạ `booking`/`resort giá` xuống campaign-level. Bộ negative giờ **465 (382 account / 83 campaign)**, conflict còn lại duy nhất `miễn phí`×1 (chấp nhận). Thêm ô pre-flight **1.4.4 rà chéo** kèm script.
2. 🔴 Campaign #4/#8 **rỗng ở bộ launch** (3 vòng vấp) → §2.1 thêm luật: chạy script lọc TRƯỚC, chốt ngân sách SAU, campaign 0 kw không tạo.
3. Doc đá nhau primary/secondary → §1.2 sửa: phone/zalo = Phụ từ ngày 1 (khớp tracking/README).
4. Số negative stale 3 file → đồng bộ.
5. `Excluded content keywords` nâng từ G4 lên **G2** (Demand Gen chạy YouTube/Display mà negative không phủ).
6. Guard mới monitoring: **CTR >2× + conversion phẳng** = click tặc crowding-out (không có alert chi tiêu vì ngân sách chặn cứng).
7. Thang dropdown ngân sách **theo phân khúc** (căn hộ/đất nền/biệt thự) → landing-page/README.
8. §5.4 PMax chốt phương án (b): hoãn, chuyển Demand Gen.
9. G2 ghi rõ bất khả thi bằng số ở bậc 30tr — cần organic/content bơm audience.

## Việc đẩy sang agent `keyword-planner` (chưa chạy)

Thiếu 3 brand variant (`eco retreat long an`, `ecopark long an`, `forest onsen`) · 8 negative chống cannibalize sibling Ecopark (`văn giang`, `sky oasis`, `ecovillage saigon river`... + không dấu) · kho đất nền Long An mỏng (1 kw/khu vực, 0 exact, 0 dự án đất nền trong projects.tsv) · Prodezi chưa có `brand-cdt--`.

## Giới hạn của bài test (đọc trước khi tin điểm)

Open-book: agent đọc đúng bộ tài liệu được luyện — điểm đo việc **tài liệu có dẫn tới quyết định đúng không**, không đo trí nhớ. Số mô phỏng deterministic — thị trường thật có variance, click tặc thật tinh vi hơn, và con người vận hành có sai số mà agent không có. Điểm 95 nghĩa là: *khi có dữ liệu thật, hệ thống ra quyết định đúng sách* — còn sách đúng tới đâu thì 30 ngày chạy thật đầu tiên mới trả lời.
