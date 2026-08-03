# Round 5 — Sonnet — 90 ngày

**Kịch bản:** 150tr/tháng · 3 dự án · CPC 25k₫ · tài khoản **đã qua G3 từ D0** (35 conv qualified/30 ngày, ECL chạy ổn, contact 58%) → mốc lịch D30 không áp dụng (ECL không "bật" ở D30, đã chạy từ trước) — gate mở đúng lộ trình ngay. T0 = 28/7/2026.
**Bẫy round:** AI Max × portfolio bidding/shared budget (chọn 1) · PMax chỉ bật nếu đủ checklist G4 (brand exclusions, campaign negatives, `Excluded content keywords`) · `campaign-setup.md` §5.4 đã chốt phương án **(b) hoãn PMax** (xác nhận: dòng đã ghi trong doc, ngày 2026-07-28).

## Setup + quyết định kỳ 1 (tuần 1-4 = ngày 0-27)

Chi tiết đầy đủ + căn cứ doc từng dòng đã có ở `test/round-5.md` (bản 30 ngày, cùng kịch bản đầu vào) — tóm tắt để giữ khuôn khổ:

- **Hiệu chỉnh mô hình trước khi quyết:** công thức `sim-rules` cho CVR LP = 4,8%; dữ liệu 3 tháng thật của tài khoản (60,8tr/tháng ÷ 25k = 2.432 click; 35 qualified ÷ 40% = 87,5 raw) → **CVR thật 3,60%**, tách core (message match ≥4/5: #1,#2,#3 exact/phrase,#4) = **3,87%**, non-core (#7 broad, #5,#6, DG) = **2,87%**. Thiếu đúng ~1 adder (0,93đ) — vá LP là việc của user (`PLAN.md` §4), giao tuần 1, **không** cộng vào số vì chưa có xác nhận sửa.
- **CÓ:** keyword `uu_tien` 1+2+3 (script §2.4, 0 dòng lọt Broad ngoài #7/#3-broad) · giữ tCPA #1,#2,#3 không chỉnh · broad barbell **1 bậc** trong #3 (trần 15% = 234k) · Demand Gen scale 300k→747k (research §1: ≥10×tCPA/ngày) · tắt #8, dồn #3 · rà 11 ô §1.5 (ACA tắt, auto-apply tắt) · `Excluded content keywords` + placement exclusion + audience exclusion `da_generate_lead_14d` (§0.4 round-5.md) · 5 audience GA4 Observation.
- **KHÔNG:** PMax (§5.4 chốt b — thiếu creative kit ≥7 ảnh 3 tỷ lệ + video, 400k/ngày dư ra chuyển DG) · AI Max (bậc 4 cần bậc 3 ổn ≥6 tuần, mới ở bậc 2; và bị **portfolio bidding + shared budget khoá đường experiment** — 2 lý do độc lập) · Portfolio bidding/shared budget (campaign-setup §5.2 cần "≥4 campaign cùng CPA" — brand/generic/T3 khác CPA; giữ TẮT để không tự khoá AI Max experiment + seasonal budget adjustment) · YouTube (G5 thiếu G4 ổn định, video, Reach Planner).
- **Ramp:** ≤20%/lần, ≥3-5 ngày → 2.000.000→4.285.000₫/ngày qua 5 bậc (D1→D13). **Mùa vụ ghi đè:** tháng 7 âm ≈13/8→10/9 → **dừng ramp**, giữ 4.285.000₫/ngày tới hết tháng 7 âm (campaign-setup §5.7 "mùa vụ ghi đè mọi kế hoạch scale").
- **Tuần 1:** Lost IS (rank) > Lost IS (budget) ở #3/#6 → coverage trước tiền, không chỉnh tCPA (tránh 2 biến/reset). **Tuần 2 — bẫy 1:** Recommendations đề xuất portfolio bidding + shared budget gộp #4/5/6 dưới ngưỡng volume → **từ chối cả hai**, dùng cách rẻ hơn (đã tắt #8, mở broad barbell có trần). **Tuần 3 — bẫy 2:** G4 đủ điều kiện bề mặt, Recommendations đẩy PMax + AI Max đúng lúc 1/7 âm (13/8) → **từ chối cả hai**, dừng ramp theo mùa vụ. **Tuần 4:** waste về 0,5%, checklist T6 đủ, lên lịch bậc 3 (value-based) cho tuần 5-6 qua campaign experiment (không đổi thẳng bid strategy).
- Kết quả kỳ 1 (khớp round-5.md): chi 106.540.000₫ · lead-q 58 · CPL-q 1.837.000₫ · contact 58% · **0 phạt kỷ luật**.

## Bảng 12 tuần

| Tuần | Chi | Click | Lead-q | CPL-q | Bậc bidding | Ghi chú |
|---|---|---|---|---|---|---|
| 1 | 19.240.000 | 770 | 11 | 1.749.000 | tCPA #1-3 · MaxConv #4 · MaxClicks #5/6 | Coverage (uu_tien 1-3), tắt #8, không chỉnh tCPA |
| 2 | 27.310.000 | 1.081 | 15 | 1.821.000 | + broad barbell #3 (trần 15%) | Bẫy 1: từ chối portfolio+shared budget (gộp #4/5/6) |
| 3 | 29.995.000 | 1.188 | 16 | 1.875.000 | giữ nguyên | Bẫy 2: từ chối PMax(§5.4b)+AI Max; dừng ramp (tháng 7 âm 13/8) |
| 4 | 29.995.000 | 1.194 | 16 | 1.875.000 | giữ nguyên | waste→0,5%; checklist T6 đủ; lên lịch bậc 3 tuần 5-6 |
| 5 | 29.995.000 | 1.194 | 16 | 1.875.000 | + bậc 3 thử nghiệm (#1-3, campaign experiment) | giữ 4.285.000₫/ngày (còn tháng 7 âm); Rằm 27/8 — không thêm hành động |
| 6 | 29.995.000 | 1.194 | 16 | 1.875.000 | bậc 3 TN tiếp | giữ nguyên, chờ hết tháng 7 âm ~10/9 |
| 7 | 32.855.000 | 1.308 | 18 | 1.825.000 | bậc 3 TN | **D45 (11/9):** ramp bậc 6 → 5.000.000₫/ngày (+16,7%, giữa tuần); #4 ước <30 conv/tháng → giữ MaxConv |
| 8 | 35.000.000 | 1.393 | 19 | 1.842.000 | bậc 3 rollout 100% (#1-3) | Mandate 150tr/tháng đạt đủ; rollout sau 3 tuần TN ổn định; checklist T6 |
| 9 | 35.000.000 | 1.211 | 16 | 2.188.000 | bậc 3 (100%) | CPC +15%→28.750₫ (tuần 9-12, mọi round); **D60 (26/9):** G2/negative đã ổn từ trước round → không hành động mới |
| 10 | 35.000.000 | 1.211 | 16 | 2.188.000 | giữ | Bẫy tái diễn: Recommendations lại đề xuất portfolio bidding cho #4/5/6 → từ chối (lý do y hệt bẫy 1) |
| 11 | 35.000.000 | 1.211 | 16 | 2.188.000 | #4 → tCPA (đơn lẻ) | **D74 (10/10):** #4 đạt ~30 conv/tháng → chuyển tCPA = CPA lịch sử +15%, KHÔNG đổi ngân sách cùng tuần |
| 12 | 35.000.000 | 1.211 | 16 | 2.188.000 | bậc 3 ổn định; bậc 4 chưa | AI Max cần bậc 3 ổn ≥6 tuần tính từ full-rollout (~21/9) → sớm nhất ~2/11, ngoài 90 ngày → không mở |

Không phạt kỷ luật nào bị áp trong 12 tuần: mọi ramp ≤20%/lần cách ≥3-5 ngày · tCPA không đổi cùng lúc ngân sách · negative có từ ngày 1 · không bật PMax/AI Max/portfolio khi chưa đủ gate.

## Quyết định tại các mốc D30/D45/D60/D74

- **D30 (27/8):** **Không áp dụng** — ECL đã chạy ổn định từ trước D0 (đầu vào kịch bản), không có sự kiện "bật ECL" nào ở mốc này; gate G0-G3 và G2 (Demand Gen) đã mở đúng lộ trình từ baseline 60tr trước round.
- **D45 (11/9):** (a) Ramp bậc 6: 4.285.000→5.000.000₫/ngày (+16,7% ≤20%, cách >20 ngày từ bậc 5 → không learning reset), đạt đủ mandate 150tr/tháng. (b) Rà theo campaign: #4 TaiChinh ước ~18-20 conv/tháng (dưới 30, tỷ trọng nhỏ trong core) → giữ Maximize Conversions; #5/#6 giữ Max Clicks + cap theo thiết kế gốc (không phải campaign "chờ graduate"). Không đổi biến nào khác cùng tuần.
- **D60 (26/9):** Mốc chuẩn của luật 90 ngày dành cho tài khoản **mở G2 lần đầu** ở D60 (xem_bang_gia ≥1.000 user/30 ngày). Ở round này G2 đã mở từ baseline 60tr trước D0 → không có hành động mới. `Excluded content keywords` đã điền từ kỳ 1 (§0.4 round-5.md) → xác nhận vẫn active, không phạt 10% DG waste. DG hiện ~23% ngân sách (>15% mặc định của luật chung) — **giữ nguyên**, có căn cứ độc lập từ kế hoạch gốc (research §1: ≥10×tCPA/ngày), không lùi về 15%.
- **D74 = D60+14 (10/10):** #4 TaiChinh tích lũy vượt 30 conv/30 ngày, Maximize Conversions ổn ≥2 tuần → chuyển **tCPA = CPA lịch sử 30 ngày gần nhất +15%**, làm ĐƠN LẺ (ngân sách tuần 11 giữ nguyên 35.000.000₫ — không chồng 2 biến). Căn cứ: `sim-rules-90` D60+14 + `journey-plan` §3 "đặt bằng hoặc cao hơn nhẹ CPA thực".
- **Bậc AI (song song, không gắn mốc lịch cố định):** bậc 3 (value-based/Conversion Value Rules) mở tuần 5-6 qua **campaign experiment** trên #1-3 — điều kiện đã đủ (`journey-plan` §3.2: thang giá trị 10/50/500, ≥15 conv/tháng cấp account) từ trước round; rollout 100% cuối tuần 8 sau 3 tuần thử nghiệm không bất thường. **Bậc 4 (AI Max):** cần bậc 3 ổn định ≥6 tuần **tính từ lúc rollout đầy đủ** (~21/9), không phải từ lúc mở experiment → sớm nhất ~2/11/2026, ngoài phạm vi 90 ngày → **không mở trong round này**, dù Recommendations tiếp tục nhắc portfolio + shared budget ở tuần 10 — từ chối lặp lại, giữ 2 công cụ đó TẮT xuyên suốt để không tự khoá đường AI Max experiment sau ngày 90.

## Tổng 90 ngày

| Chỉ số | Giá trị | Ghi chú |
|---|---|---|
| Tổng chi | **374.385.000₫** | Run-rate cuối kỳ = 150tr/tháng = 100% mandate (đạt từ D45, 11/9) |
| Tổng click | 12.144 | |
| Tổng lead raw | 487 | |
| Lead liên hệ được (58%) | **282** | KPI đứng trước CPL (`research` §5); trong đó tag đúng SLA 48h (giả định sales tuân thủ 85%) ≈ **240**, mất tag ≈ 42 (15%) — ảnh hưởng tín hiệu ECL, không phải contact rate thật |
| Tổng lead qualified | **191** | qualify 40% (2 dropdown), không đổi trong 90 ngày |
| **CPL qualified blended** | **1.960.000₫** | Baseline kịch bản trung bình `research` §2 ~1,56tr → kém 26%. Nguyên nhân là **CVR thật 3,60% nền vs mô hình 4,8%** (thiếu 1 adder LP, chưa xác nhận vá — xem dưới), **không phải** kỷ luật vận hành 90 ngày |
| Contact rate | 58% xuyên suốt | Không đổi vì scenario input cố định |
| Bậc bidding cuối kỳ | Bậc 3 (value-based, full rollout) cho #1-3 · #4 vừa lên tCPA (bậc 2) · #5/#6 Max Clicks (thiết kế cố định) · Bậc 4 AI Max **chưa mở** | |
| Gate cuối kỳ | G0-G3 + G2 (DG remarketing) đã chạy từ trước round · **G4 (PMax) vẫn HOÃN** theo §5.4(b) — chưa có creative kit ≥7 ảnh 3 tỷ lệ + video → chưa đủ điều kiện mở lại · G5 (YouTube) chưa đủ điều kiện | |
| Portfolio bidding / shared budget | **TẮT xuyên suốt**, từ chối bẫy 2 lần (tuần 2, tuần 10) | |

**Không cộng CVR-uplift từ iteration LP** dù `sim-rules-90` cho phép tới +0,4đ/kỳ 30 ngày: luật yêu cầu nêu rõ insight Clarity thật, agent không có insight thật để dẫn trong kịch bản này → bịa insight = 0 điểm đo lường, nên giữ CVR thuần theo công thức mix core/non-core. Đòn bẩy rẻ nhất vẫn treo nguyên như round-5.md đã chỉ ra: vá 1 adder LP (core 3,87%→4,8%) đưa CPL-q dưới 1,56tr mà không tốn thêm ngân sách — chưa có xác nhận đã làm nên không đưa vào số.

## 3 bài học

1. **Mốc lịch cố định (D30/D45/D60/D74) chỉ đúng nghĩa cho tài khoản mở ECL tại D30.** Khi tài khoản đã ở G3 từ D0 (như round này), phải tự map lại: D30 bỏ, D45/D60/D74 chỉ còn áp cho campaign/chỉ số CHƯA đạt ngưỡng riêng (ở đây chỉ #4) — không áp đồng loạt cho cả tài khoản. Copy mốc lịch mà không kiểm trạng thái thực = mở gate sai thời điểm.
2. **"Bậc 3 ổn định ≥6 tuần" phải tính từ lúc rollout đầy đủ, không phải từ lúc mở campaign experiment.** Chênh lệch cách tính này (bắt đầu 25/8 vs rollout 21/9) quyết định AI Max có kịp mở trong 90 ngày hay không — ở đây không kịp (sớm nhất đầu tháng 11). Tính từ mốc thử nghiệm là cách phổ biến nhất để "hợp lý hoá" mở gate sớm.
3. **Không bịa CVR-uplift dù luật cho phép** — phần thưởng +0,4đ/kỳ chỉ có giá trị khi có insight Clarity thật; không có thì giữ nguyên số. CPL-q kém baseline nghiên cứu 26% là con số thật của một LP chưa vá, không phải lỗi vận hành 90 ngày, và vẫn là đòn bẩy rẻ hơn toàn bộ kế hoạch scale.

---
*Output duy nhất của round này: `test/90d/sonnet-round-5.md`. Không sửa file nào khác.*
