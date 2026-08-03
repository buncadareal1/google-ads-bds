# SCORECARD 90 NGÀY — 10 Sonnet + 10 Haiku, cùng 10 kịch bản (2026-07-28)

Chấm bởi Fable theo rubric `sim-rules.md` + tiến trình gate `sim-rules-90.md` + độ phủ `metrics-90d.md`.
Số của mọi bài nghi vấn đã verify bằng công thức (bằng chứng trích từ chính file agent).

## Bảng điểm theo model

| Round | Kịch bản | Sonnet | Haiku | Ghi chú chấm |
|---|---|---|---|---|
| 1 | Baseline | **96** | 85 | S: bắt meta-bẫy + tự verify 382 negative từ CSV. H: xử bẫy kiểu "thêm negative" (trượt meta), D74 khóa gate không rõ lý do |
| 2 | PMax cám dỗ | **95** | 80 | S: từ chối chuẩn + không bịa insight. H: gate ĐÚNG thứ tự nhưng **số kỳ 1 bịa** (123 lead-q/870 click = 14%, trần công thức ~1,9%) |
| 3 | Click tặc | **94** | 84 | S: đúng toàn bộ. H: chuyển Maximize Conversions ngay **D30** (luật D45) |
| 4 | Policy biệt thự | **95** | 90 | Cả hai tôn trọng lệnh cấm tCPA phân khúc. S: chặn D74 bằng 2 lý do độc lập |
| 5 | Scale 150tr | 94 | **68** | S: từ chối bonus CVR vì không có insight thật. H: **số sai bậc ×28** (14.286 click/tuần thay vì 500 → CPL-q 200k ảo) |
| 6 | Tết | **95** | 88 | S: từ chối tCPA tại mốc lịch vì data chưa đủ. H: ổn, CPL cao có giải thích |
| 7 | Contact sập | **96** | 92 | Cả hai chẩn đoán đúng thứ tự + "mẫu số vỡ". Bài tốt nhất của Haiku |
| 8 | Nghẽn budget | **96** | 91 | S: 2 nhịp + đề xuất ngân sách mới D60 + từ chối gate đủ-điều-kiện-kỹ-thuật. H: đúng trình tự, số khớp |
| 9 | Đất nền | **95** | 89 | S: tính sàn CPL cấu trúc → "quyết định kinh doanh, hết đòn bẩy Ads". H: verdict có số nhưng tự áp nhầm penalty tCPA |
| 10 | Bid war | **94** | 82 | S: đếm gate bằng primary metric mới (21<30 → không tCPA). H: nhảy chuỗi (Maximize D36, tCPA D46) + phạm luật phone/zalo secondary |
| **TB** | | **95,0** | **84,9** | Opus (4 tuần, không có precedent): **95,0** |

## Kết luận thí nghiệm — "tài liệu gánh model tới đâu"

1. **Kỷ luật gate/quyết định: tài liệu gánh được cả 3 tầng model.** Bẫy chiến lược (PMax, auto-apply, bid ngược, tắt Tết): Sonnet né 10/10, Haiku né ~9/10. Không model nào tự tiêu tiền sai chỗ. → Phần "luật + gate + checklist" của hệ viết đủ rõ để model rẻ nhất vẫn tuân thủ.
2. **Số học: KHÔNG gánh được Haiku.** 3/10 bài Haiku có số bịa/sai bậc (H5 ×28, H2 ×7, H1 nhẹ) dù công thức nằm ngay trong đề. Sonnet 0/10 lỗi loại này (2 bài còn chủ động TỪ CHỐI bonus vì không có bằng chứng).
3. **Trình tự thời gian: Haiku trượt 3/10** (nhảy mốc D30/D36/D46 thay vì D45/D74). Sonnet 0/10 — thậm chí 3 bài từ chối mở đúng mốc lịch vì dữ liệu chưa đủ ("mốc là điều kiện, không phải ngày hẹn").
4. **Sonnet = Opus khi có tài liệu chín + tiền lệ.** Sonnet đạt 95,0 bằng đúng Opus — một phần nhờ đọc lại các bản 4-tuần đã QA (hành vi tận dụng tiền lệ, được thưởng điểm chứ không trừ). Ngụ ý vận hành: **vòng lặp tuần chạy bằng Sonnet là đủ**, Opus để dành cho thiết kế/QA/tình huống mới.

## Chính sách model rút ra cho vận hành thật (ghi vào hệ)

| Việc | Model tối thiểu | Điều kiện |
|---|---|---|
| Vòng check ngày/tuần, suggest theo luật monitoring | **Sonnet** | Có docs + tiền lệ |
| Tính toán số liệu (pacing, CPL, forecast) | **Bất kỳ model + SCRIPT** | Không để model nào tự tính tay — kể cả Opus; số phải từ script/API |
| Thiết kế mới, QA, phân xử mâu thuẫn, tình huống chưa có tiền lệ | **Opus/Fable** | |
| Haiku | Chỉ việc phân loại/đọc-tóm tắt | KHÔNG giao số học, KHÔNG giao trình tự nhiều mốc |

## Độ phủ lịch chỉ số (metrics-90d)

Sonnet: ~25/30 chỉ số suy được từ output (thiếu nhóm Clarity thật + Auction Insights — đúng vì mô phỏng không có). Haiku: ~19/30. Không bài nào bị trừ điểm phủ (<60% mới trừ) nhưng chênh lệch cho thấy Sonnet báo cáo đủ chiều hơn ở cùng đề bài.

## Vá phát sinh từ đợt này (đã áp)

- Xung đột Discovery broad: campaign-setup §2.2/§4.4 nói "bật cùng lúc chuyển tCPA/Maximize" ↔ journey-plan §3.2 gate ở bậc 2 — đã thống nhất theo gate nghiêm hơn (S7 phát hiện).
- Ghi chú test-harness: luật ×1,15 của sim-rules-90 mơ hồ (áp vào CVR hay lead-q) — S1/S10 hiểu 2 kiểu, đều flag rõ; lỗi đề bài, không trừ điểm agent.
