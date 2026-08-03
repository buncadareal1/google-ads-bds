# Luật giả lập ads test (war-game) — mọi round dùng chung

Bạn (agent) là người vận hành Google Ads cho 1 kịch bản. Mô phỏng 4 TUẦN vận hành.
KHÔNG bịa số ngoài công thức dưới — mọi số phải suy từ luật này + quyết định của bạn.

## Công thức mô phỏng (từ research/google-ads-bds-vn.md §2, deterministic)

**Click/tuần** = (ngân sách tuần × (1 − tỷ_lệ_click_rác_chưa_lọc)) / CPC_kịch_bản

**CVR LP** = 2.0% nền, cộng dồn nếu LP/campaign của bạn có (theo landing-page/README.md):
- Message match keyword→H1 đạt ≥4/5 cho nhóm ad chính: +1.0
- Bảng giá/khoảng giá above the fold: +0.8
- Zalo sticky + click-to-call đúng chuẩn: +0.6
- Form 4 field + 2 dropdown qualifying: +0.4 (nhưng xem qualify rate)
- Gửi về homepage thay LP riêng: ×0.4 toàn bộ
- Trần: 6.0%

**Qualify rate**: 40% nếu form có 2 dropdown; 25% nếu form chỉ tên+SĐT.
**Contact rate**: 55% nếu có dropdown + validate đầu số + SLA gọi <5'; 35% nếu thiếu ≥2 trong số đó.
**Lead raw/tuần** = click × CVR. **Lead qualified** = lead × qualify rate.
**CPL qualified** = chi tiêu thực / lead qualified.

**Phạt kỷ luật (tự áp vào kết quả nếu vi phạm):**
- Bật broad/PMax/tCPA khi chưa đủ điều kiện gate → CVR ×0.6 do lead rác, +20% chi tiêu lãng phí.
- Đổi ngân sách >±20% hoặc tCPA >±15% một lần → learning reset: tuần kế tiếp CVR ×0.7.
- Không import negative list ngày 1 → 25% ngân sách tuần 1-2 cháy vào click sai intent.
- Không xử lý sự kiện được tiêm (xem kịch bản) → hậu quả ghi trong kịch bản.

## Nhiệm vụ của agent (mỗi round)

1. Đọc: CLAUDE.md, PLAN.md §0, playbook/campaign-setup.md (checklist), playbook/customer-journey-plan.md §3 (gates + kill rules), landing-page/README.md (ma trận CRO), tracking/README.md (6 luật), research/google-ads-bds-vn.md §8 (checklist tuần). Invoke skill liên quan kịch bản nếu cần.
2. Ra quyết định TUẦN 0 (setup): cấu trúc campaign theo ngân sách, bidding khởi điểm, negative, conversion actions, LP spec chọn gì.
3. Vận hành TUẦN 1→4: mỗi tuần tính số theo công thức, chạy checklist tuần, phản ứng với SỰ KIỆN được tiêm trong kịch bản, ghi quyết định + lý do (trỏ về doc/gate nào).
4. Output: ghi vào `test/round-<số>.md` — NGẮN GỌN đúng format:

```
# Round <số> — <tên kịch bản>
## Setup tuần 0 (quyết định + căn cứ doc)
## Nhật ký tuần 1-4 (bảng: tuần | chi tiêu | click | lead raw | lead qualified | contact rate | CPL-q | sự kiện | hành động + căn cứ)
## Tổng kết: tổng lead, CPL qualified, CTR giả định, trạng thái gate cuối kỳ, 3 bài học
```

KHÔNG sửa file nào khác ngoài test/round-<số>.md của mình.

## Rubric chấm (Fable chấm, 100đ)

| Mục | Điểm | Chấm gì |
|---|---|---|
| Pre-flight & cấu trúc | 20 | Đúng cấu trúc theo ngân sách (§2 research), negative ngày 1, conversion ladder, 11 ô cài đặt |
| Kỷ luật bidding & learning | 20 | Max Clicks trước, không tCPA sớm, đổi ngân sách ±20%, không reset learning vô cớ |
| Xử lý sự kiện | 20 | Phản ứng đúng playbook với sự kiện được tiêm, đúng thứ tự ưu tiên |
| Đo lường & báo cáo | 15 | Contact rate đứng trước CPL, đối chiếu số, format checklist T6 |
| Kỷ luật gate | 15 | Không mở PMax/broad/YouTube khi chưa đủ điều kiện — kể cả khi "hấp dẫn" |
| Kết quả kinh tế | 10 | CPL qualified so với kịch bản trung bình (~1,56tr); thưởng nếu tốt có căn cứ |
