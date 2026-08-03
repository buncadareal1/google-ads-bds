# Phụ lục luật giả lập 90 NGÀY (đọc SAU test/sim-rules.md — luật gốc vẫn áp dụng)

Mô phỏng 12 tuần = 3 kỳ 30 ngày. Báo cáo theo KỲ (không cần bảng từng tuần — bảng 12 dòng gộp được).

## Dòng thời gian mở khóa (cố định cho mọi round)

| Mốc | Sự kiện |
|---|---|
| D30 | Thỏa thuận Keap ký xong → **ECL bật được** (upload_ecl chạy, tag contactable/qualified có dữ liệu từ D30) |
| D45 | Nếu ≥30 conv/30 ngày: được chuyển bidding. **Chuyển ĐÚNG** (đảo primary sang `Lead_Contactable` trước, rồi Maximize Conversions): 2 tuần learning CVR ×0,85, sau đó hệ số hiệu quả **×1,15** vĩnh viễn. **Chuyển SAI** (primary còn form thô): qualify rate ×0,75 vĩnh viễn (bidding mua rác) |
| D60 | Content/organic bơm audience → `xem_bang_gia` đạt 1.000 user/30 ngày → **G2 mở được**. Mở Demand Gen ≤15% ngân sách: nhớ điền `Excluded content keywords` → thêm +5% lead-q (remarketing); quên → 10% ngân sách DG cháy vào placement rác |
| D60+14 | Nếu Maximize Conversions ổn ≥2 tuần + ≥30 conv: được lên **tCPA** = CPA lịch sử +15%. Đúng luật ±15%: ổn; sai: learning reset ×0,7 một kỳ 2 tuần |
| Tuần 9-12 | Thị trường nóng: CPC +15% (mọi round) |

## Luật bổ sung

- CVR cải thiện từ iteration LP (dựa Clarity insight): tối đa +0,4 điểm/kỳ 30 ngày, phải nêu rõ sửa gì và insight nào (bịa insight = 0 điểm mục đo lường).
- Contact rate: giữ luật gốc; từ D30 phải báo cáo thêm **% lead được gắn tag đúng SLA 48h** (giả định sales tuân thủ 85% — tức 15% lead mất tag, ảnh hưởng số ECL).
- Mỗi kỳ 30 ngày = 1 báo cáo tháng theo checklist research §8 (ngắn — 5 dòng/kỳ).
- Sự kiện riêng của kịch bản (bẫy) vẫn xảy ra đúng tuần như đề bài gốc; sau đó vận hành bình thường theo timeline trên.

## Format output (GỌN — tối đa ~120 dòng)

```
# Round <n> — <model> — 90 ngày
## Setup + quyết định kỳ 1 (tuần đầu như luật gốc, có xử lý bẫy)
## Bảng 12 tuần: tuần | chi | click | lead-q | CPL-q | bậc bidding | ghi chú
## Quyết định tại các mốc D30/D45/D60/D74 (mỗi mốc: làm gì + căn cứ doc)
## Tổng 90 ngày: tổng chi, tổng lead-q, CPL-q blended, contact rate, bậc cuối, gates đã mở
## 3 bài học
```

## Rubric bổ sung khi chấm (cộng vào rubric gốc, tổng vẫn quy về 100)

- **Tiến trình gate đúng nhịp** (thay 5đ của mục Kinh tế): mở đúng thứ tự tại đúng mốc — không sớm (phạt như luật gốc), không muộn vô lý (bỏ lỡ D45/D60 mà không có lý do = -3).
