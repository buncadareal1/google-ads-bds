# BÀI HỌC từ kỳ thi Vinhomes Hóc Môn (đối chiếu đáp án gốc DAP_AN_RUBRIC_1.md, 2026-08-03)

## 3 điểm mù HỆ THỐNG (cả 5/5 Opus trượt giống hệt nhau → lỗi tài liệu, không phải lỗi model)

| # | Điểm mù | Đáp án gốc | Đã vá vào |
|---|---|---|---|
| 1 | **Không quét chuỗi thời gian tìm điểm gãy** — cả 5 chỉ nhìn trung bình kỳ nên trượt P7: đối thủ đấu giá brand từ N52 (CPC 10.803→19.113 = +74%, IS sập còn 28,8%) dù dữ liệu ngày nằm lộ thiên trong sheet 02. Agent 5 còn viết "không có Auction Insights nên không biết" — trong khi tự tính được từ dữ liệu có sẵn. | P7 (3đ) | `playbook/monitoring.md` §4: nghi thức quét WoW CPC/CTR/IS từng campaign mỗi thứ 6 + ngưỡng alert |
| 2 | **Không gọi tên bẫy Simpson** — P9: CVR tổng giảm 1,65%→1,12% sau khi đổi LP (do YouTube bật N55 kéo tụt) trong khi từng campaign đều cải thiện (Brand 3,82→5,42%, Generic 2,06→3,75%). Cả 5 kết luận ĐÚNG CHIỀU (nhờ sheet 10C cho sẵn số LP-level) nhưng không con nào bóc theo campaign để chỉ ra nghịch lý → chỉ được 3/5đ. Gặp đề không cho sẵn sheet 10C là sập bẫy. | P9 (5đ) | `playbook/monitoring.md` §4 (luật Simpson mọi so sánh trước/sau) + `landing-page/README.md` yếu tố 3 (luật Simpson khi so LP) |
| 3 | **Data exclusion chỉ được coi là việc của máy học, không phải của phân tích** — P8: cả 5 truy đúng nguyên nhân GTM v23, nhưng chỉ agent 5 nêu khai data exclusion (nhờ đọc monitoring.md §2.1), và **0/5** loại 3 ngày N44–46 khỏi phép tính trung bình khi phân tích. | P8 (6đ, mất ~1đ/con) | `playbook/monitoring.md` §2.1: luật "exclusion áp cho CẢ phân tích" |

## Bài học cho GIÁM KHẢO (Fable)

- Rubric v1 của tôi phủ ~85% đáp án gốc: **trượt đúng 3 mục trên + phễu form 77% + 3 điểm thưởng**. Nguyên nhân giống hệt thí sinh: tôi cũng chỉ tổng hợp tĩnh (totals theo campaign/giai đoạn), không quét chuỗi thời gian, không nghĩ đến Simpson. → Khi xây rubric chấm war-game sau này: bắt buộc chạy **changepoint scan** trên dữ liệu ngày + liệt kê các bẫy thống kê kinh điển (Simpson, survivorship, mẫu nhỏ, mixed-cohort) trước khi chốt "vấn đề phải thấy".
- Điểm thưởng của đáp án gốc (KPI 32 cọc × 181tr = ROAS 2,76x mâu thuẫn KPI 3,0x; không ngoại suy GĐ3 vì có sự kiện mở bán; thẻ GA4 trùng làm nhiễu so sánh LP) — **cả 5 thí sinh đều tự tìm ra ≥2/3** dù rubric của tôi không có. Tài liệu hệ đã dạy được phản xạ "kiểm tra mâu thuẫn KPI" và "nghi ngờ mẫu số".

## Bài học vận hành (không liên quan đề thi)

- **/tmp là tmpfs** — mất trắng đợt 1 khi máy reboot. Mọi artifact war-game/exam từ nay ghi vào `test/` trong repo. (Đã áp dụng từ đợt 2.)
- Agent viết bài dài phải **ghi theo từng phần** (Write A → Edit nối B/C/D/E) để sống sót đứt kết nối. (Đã thành luật trong prompt.)
- **Effort medium đủ dùng cho bài phân tích có tài liệu + luật script**: điểm trung bình 94,4/100 (chưa tính thưởng), ngang war-game effort cao. Tiết kiệm đáng kể cho vòng lặp tuần.
- Kỷ luật tuân thủ đề (trần 150 từ D5, "đúng 2 hạng mục" D6) là chỗ mất điểm phổ biến nhất của Opus — thêm nhắc "đọc kỹ ràng buộc độ dài/số lượng trong đề" vào prompt template thi.
