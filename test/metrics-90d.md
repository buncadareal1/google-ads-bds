# Lịch chỉ số 90 ngày — mỗi ngày 1 chỉ số, 30 chỉ số × 3 chu kỳ, ngưỡng siết dần

Dùng cho: (a) chấm war-game 90 ngày, (b) sau này là lịch giám sát THẬT (nạp vào vòng Telegram —
mỗi ngày guard chạy chỉ số của ngày đó ngoài bộ alert cố định). Quy tắc chung: chỉ số nào không có
dữ liệu → ghi N/A + lý do, không bịa. Nguồn ngưỡng: research/journey-plan/monitoring (trích cột cuối).

| Ngày | Chỉ số | Công thức / cách đo | Ngưỡng ĐẠT kỳ 1 (D1-30) | Kỳ 2 (D31-60) | Kỳ 3 (D61-90) | Nguồn quy tắc |
|---|---|---|---|---|---|---|
| 1 | Spend pacing | chi lũy kế / (ngân sách tháng × %thời gian) | 0,9–1,1 | như kỳ 1 | như kỳ 1 | monitoring §1 |
| 2 | CPC blended | chi / click | ≤ CPC kịch bản +10% | +5% | ≤ kịch bản (đã trừ QS cải thiện) | research §2 |
| 3 | CTR Search | click/impression | ≥5% | ≥6,5% | ≥7,6% (benchmark ngành) | research §2 |
| 4 | Brand IS | impression share nhóm brand | ≥70% | ≥80% | ≥85% | journey-strategy §3 |
| 5 | IS lost (budget) | từ báo cáo | <20% | <15% | <10% (hoặc có kế hoạch tăng đã duyệt) | monitoring §3 |
| 6 | IS lost (rank) | từ báo cáo | <25% | <20% | <15% | research §8 T5 |
| 7 | CVR LP | lead raw / click | ≥3% | ≥4% | ≥4,5% | research §6: 3-6%, <2%=LP hỏng |
| 8 | Lead raw/tuần | đếm | ≥8 | ≥10 | ≥12 | KPI tree journey-plan §4 |
| 9 | **Contact rate** | gọi được / tổng lead | ≥50% | ≥52% | ≥55% | PLAN §0.4 — KPI số 1 |
| 10 | Qualify rate | qualified / lead | ≥30% (căn hộ) / ≥18% (đất nền) | +2đ | +2đ | research §2 theo phân khúc |
| 11 | CPL raw | chi / lead raw | ≤700k | ≤650k | ≤600k | mô hình research §2 |
| 12 | **CPL qualified** | chi / lead-q | ≤1,9tr | ≤1,7tr | ≤1,56tr | mốc kịch bản trung bình |
| 13 | Search terms xử lý | # term mới phân loại + negative thêm/tuần | 100% term ≥30 click được phân loại | như kỳ 1 | như kỳ 1 | UPDATE.md tuần |
| 14 | % chi tiêu intent sai | chi vào term đã bị đánh dấu rác | <8% | <5% | <3% | research §9 #2 |
| 15 | Invalid clicks % | cột Invalid clicks | <10% | <10% | <10%; ≥10% → quy trình §5 | research §5 |
| 16 | Learning stability | # thay đổi lớn gây reset trong 14 ngày | 0 | 0 | 0 | research §4.2 |
| 17 | Budget discipline | mọi lần đổi ≤±20%, cách ≥3 ngày | 100% tuân thủ | 100% | 100% | research §4.2 |
| 18 | Bid/tCPA discipline | mọi lần đổi ≤±15% | 100% | 100% | 100% | research §4.2 |
| 19 | **Gate đúng nhịp** | trạng thái gate vs điều kiện thực | không mở sớm | D45 xét bidding nếu đủ | D60 xét G2; không muộn vô lý | journey-plan §3 + sim-rules-90 |
| 20 | Primary conversion đúng | action nào đang Primary | generate_lead (trước ECL) | đảo Lead_Contactable ≤7 ngày sau đủ điều kiện | Lead_Contactable | tracking/README luật #2 |
| 21 | ECL freshness | ngày từ lần upload cuối | N/A (chưa mở) | ≤7 ngày | ≤3 ngày | curriculum: delay ≤7d |
| 22 | % lead có gclid | từ Keap | ≥80% | ≥85% | ≥90% | ecl-keap-pipeline |
| 23 | % tag đúng SLA 48h | từ Keap | N/A | ≥80% | ≥85% | PLAN §6.6 (sim: 85%) |
| 24 | Message match score | chấm 3 luồng chính 1-5 | ≥4/5 | ≥4/5 | ≥4,5/5 | landing-page/README |
| 25 | Scroll tới bảng giá | Clarity scroll depth | ≥50% | ≥55% | ≥60% | clarity-checklist §2 |
| 26 | Rage/dead click form | % phiên | <5%/<4% | <4%/<3% | <3%/<2% | clarity-checklist §2 |
| 27 | Phân tán CPL-q campaign | max/min CPL-q giữa campaign | <2,5× | <2× | <2× hoặc đã kill nhánh tệ | journey-plan §3.1 |
| 28 | % ngân sách bottom funnel | (T1+T2)/tổng | ≥80% (30tr) | theo kịch bản | theo kịch bản | journey-plan §3 |
| 29 | Báo cáo đúng format | contact rate đứng trước CPL, có nguồn số | đạt/không | đạt | đạt | monitoring §1 |
| 30 | **Tổng kết tháng** | CPL-q blended vs trần + 1 quyết định kỳ sau có căn cứ | có, đúng format | có | có + so 3 kỳ | research §8 tháng |

## Quy tắc chấm bằng lịch chỉ số (bổ sung vào rubric)

- Mỗi run 90 ngày được chấm **độ phủ**: bao nhiêu / 30 chỉ số suy ra được từ output (bảng tuần + mốc).
  Độ phủ <60% = trừ tối đa 5đ mục Đo lường (vận hành mà không đo là vận hành mù).
- Chỉ số fail có kèm **hành động đúng quy tắc** (vd IS lost 25% → kế hoạch tăng 2 nhịp) = vẫn ĐẠT về
  vận hành — lịch chỉ số đo *phản xạ*, không đo *may mắn*.
- 3 chỉ số in đậm (9, 12, 19) là **trọng số kép** khi tính điểm sức khỏe tổng.

## Điểm sức khỏe hệ (dùng cả khi chạy thật)

`Health = % chỉ số ĐẠT trong chu kỳ 30 ngày gần nhất (chỉ số kép ×2)` — xanh ≥85% · vàng 70-84% · đỏ <70%.
Khi hệ chạy thật: lịch này nạp vào vòng Telegram — mỗi ngày guard chạy đúng chỉ số của ngày + bộ alert cố định monitoring §2.
