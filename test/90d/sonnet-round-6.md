# Round 6 — Sonnet — 90 ngày

Kịch bản: 30tr₫/tháng (1.000.000₫/ngày), căn hộ **Hà Nội**, CPC kịch bản **27.000₫**, launch đầu tháng 1 dương lịch.
Bẫy: tuần 3–4 = 2 tuần Tết Nguyên đán (demand −40%, CVR ×0,6). Mốc D30/D45/D60/D74 theo lịch cố định (`sim-rules-90.md`).
Tuần n = D+(n-1)·7 → D+(n-1)·7+6. D30≈D+29 (tuần 5) · D45≈D+44 (tuần 7) · D60≈D+59 (tuần 9) · D74≈D+73 (tuần 11).

## Setup + quyết định kỳ 1

**Pre-flight G0** (`campaign-setup` §1): verification Tổ chức · billing VND/GMT+7 · 6 conversion action thang 1/10/50/500, count=One, cửa sổ 90 ngày (`tracking/README` luật #4) · GA4↔Ads + auto-tagging · 382 negative account-level ngày 1 · 11 ô cài đặt §1.5 · 1 lead thật kiểm gclid→Keap.

**Campaign** (`campaign-setup` §2, tái dùng đúng cấu trúc round 6 gốc — #4 TaiChinh/#8 NOXH rỗng ở bộ launch nên dồn về #1/#3):

| Campaign | ₫/ngày | Bid cap |
|---|---|---|
| `BDS_Search_Brand_DuAn` (3 dự án) | 505.000 | 22.000 |
| `BDS_Search_Brand_CDT` | 75.000 | 27.000 |
| `BDS_Search_KhuVuc_GiaoDich` (2 khu vực) | 420.000 | 35.000 |

**Primary ngày 1** = `Lead_Form_Raw` (`generate_lead`); `phone_click`/`zalo_click` = Secondary vĩnh viễn (`tracking/README` luật #2). Max Clicks + bid cap, Phrase+Exact, không broad.

**LP CVR** (`landing-page/README` ma trận): nền 2,0 + message match brand ≥4/5 (+1,0) + bảng giá ATF (+0,8) + Zalo sticky/tel: (+0,6) + form 4 field/2 dropdown (+0,4) = **4,8%** (trần 6,0). Qualify rate 40% (2 dropdown) · Contact rate 55% (dropdown+validate+SLA<5').

**Kế hoạch Tết chốt từ tuần 0** (`research` §4, `PLAN` §0.6): giảm ngân sách tay theo bậc ≤20%/lần cách ≥3 ngày, **KHÔNG tắt** (tắt = learning reset ×0,7); 3 bậc D+7/D+11/D+14 = −20%/−20%/−20% (0,8³ = **−48,8%**, trong dải 40–60%) rồi đóng băng hết Tết; **không dùng seasonality adjustment** (event >14 ngày + Max Clicks không dùng được tCPA/tROAS + đây là mùa vụ định kỳ — 3 lý do độc lập); bung lại sau Tết cũng ≤20%/lần.

## Bảng 12 tuần

| Tuần | Chi tiêu | Click | Lead-q | CPL-q | Bậc bidding | Ghi chú |
|---|---|---|---|---|---|---|
| 1 | 7.000.000 | 259 | 4,98 | 1.406k | Max Clicks | Launch, không đổi gì (tuần 1 cố định, `campaign-setup` §4.1) |
| 2 | 5.120.000 | 190 | 3,64 | 1.406k | Max Clicks | Bậc giảm 1–2 (−20%/−20%) chuẩn bị Tết; search terms vòng 1; chốt lịch trực Tết |
| 3 | 3.584.000 | 133 | 1,53 | 2.344k | Max Clicks | **Tết tuần 1**: bậc giảm 3 (−20%, tổng −48,8%) rồi ĐÓNG BĂNG; CVR×0,6 (2,88%); KHÔNG tắt |
| 4 | 3.584.000 | 133 | 1,53 | 2.344k | Max Clicks | **Tết tuần 2**: giữ nguyên, không thao tác gì; CPL cao là trần số học, không phải LP hỏng (research §6, CVR thật 2,88%>2%) |
| 5 | 4.667.000 | 173 | 3,32 | 1.406k | Max Clicks | Bung lại bậc 1–2 (+20%/+20%); **D30: ECL bật** (Keap ký) → tag contactable có dữ liệu; bắt đầu báo % lead gắn tag SLA 48h (giả định 85%) |
| 6 | 6.277.000 | 232 | 4,46 | 1.407k | Max Clicks | Bung lại bậc 3–4 (+20%/+13%) → về 100% ngân sách đúng D+40 |
| 7 | 7.000.000 | 259 | 4,98 | 1.406k | Max Clicks | Ổn định 1 tuần trước khi đổi gì tiếp; **D45: ~32 lead raw/30 ngày ≥30** → đủ điều kiện chuyển bidding cuối tuần |
| 8 | 7.000.000 | 259 | 4,23 | 1.655k | Maximize Conv. (học 1/2) | Đảo primary→`Lead_Contactable` TRƯỚC, rồi đổi bidding (`campaign-setup` §4.4 điểm 1); CVR×0,85 learning; không đụng ngân sách 2 tuần |
| 9 | 7.000.000 | 225 | 3,68 | 1.902k | Maximize Conv. (học 2/2) | CPC hot +15% bắt đầu (27.000→31.050₫, tuần 9–12, mọi round); **D60: G2 KHÔNG mở** — thiếu bằng chứng ≥1.000 user/30d |
| 10 | 7.000.000 | 225 | 5,29 | 1.323k | Maximize Conv. (ổn định) | Học xong → hệ số hiệu quả ×1,15 vĩnh viễn; + LP fix (Clarity, xem dưới) +0,3đ CVR → CVR 5,87% |
| 11 | 7.000.000 | 225 | 5,29 | 1.323k | Maximize Conv. | **D74: contactable ~21/30 ngày <30** → CHƯA đủ điều kiện lên tCPA, giữ nguyên |
| 12 | 7.000.000 | 225 | 5,29 | 1.323k | Maximize Conv. | Ổn định, chờ review tháng tiếp theo (`research` §8) |
| **Tổng** | **72.232.000** | **2.540** | **48,22** | **1.498k** | Maximize Conv. | — |

**LP iteration kỳ 3** (appendix luật bổ sung, tối đa +0,4đ/kỳ): Clarity ghi nhận rage-click trên nút "Nhận Bảng Giá" bị thanh Zalo sticky che một phần trên viewport <375px (`tracking/clarity-checklist.md` §2 — rà rage/dead click form hàng tuần). Sửa: nâng z-index CTA + đệm safe-area dưới. +0,3đ (dưới trần 0,4), cộng vào nền 4,8 → 5,1%, nhân hệ số hiệu quả D45 (×1,15) = 5,87% — không vượt trần 6,0.

## Quyết định tại các mốc

| Mốc | Làm gì | Căn cứ doc |
|---|---|---|
| **D30** | ECL bật (upload_ecl chạy qua Data Manager API), tag contactable/qualified có dữ liệu từ nay. Không đổi gì khác cùng lúc (ramp ngân sách đang chạy riêng — một thay đổi một lúc) | `sim-rules-90` dòng thời gian; `tracking/README` luật #2,#3 |
| **D45** | Trailing 30 ngày lead raw (`generate_lead`, primary hiện tại) ≈32 ≥30 → **đủ điều kiện**. Thực hiện **ĐÚNG thứ tự**: (1) đảo primary sang `Lead_Contactable`, `generate_lead` lùi Secondary; (2) đổi Max Clicks→Maximize Conversions. Không đổi ngân sách 2 tuần kế | `campaign-setup` §4.4 điểm 1; `journey-plan` §2.3 (bẫy optimize-to-quality) |
| **D60** | Kiểm G2 (`journey-plan` §3.1: audience `xem_bang_gia`/`engaged_60s` ≥1.000 user/30 ngày). Traffic ads toàn hệ ~900 click/tháng ở 30tr — chính doc đã cảnh báo ngưỡng này "bất khả thi bằng số nếu chỉ dựa traffic ads, cần organic/content bơm thêm"; kịch bản không có sự kiện bơm organic → **KHÔNG mở G2**, không dựng Demand Gen, không bịa số user để mở gate dù "hấp dẫn". Đồng thời CPC hot +15% áp cho mọi campaign đang chạy (không phải điều kiện riêng của G2) | `journey-plan` §3.1, §2.1; `PLAN` §0.5/§0.6 |
| **D74** (D60+14) | Maximize Conversions đã ổn định >2 tuần (đủ) nhưng conversion hiện là `Lead_Contactable`: trailing 30 ngày ≈21 <30 (Tết + learning dip kéo giảm phễu tháng trước) → **CHƯA đủ điều kiện lên tCPA**. Ở lại Maximize Conversions, không ép lên tCPA chỉ vì đúng ngày hẹn; rà lại ở review tháng kế | `campaign-setup` §4.4; `sim-rules-90` phụ lục |

## Tổng 90 ngày

| Chỉ số | Giá trị |
|---|---|
| Tổng chi tiêu | **72.232.000₫** (kế hoạch 84.000.000 → tiết kiệm 11.768.000, chủ yếu từ bậc giảm Tết; không tái đầu tư vì không gate nào đủ điều kiện mở rộng trong kỳ) |
| Tổng lead-q | **48,22** |
| CPL-q blended | **1.498.000₫** (kịch bản trung bình 1.560k → **−4,0%**, tốt hơn benchmark nhờ hệ số hiệu quả D45 + LP fix bù lại phần đắt do Tết + CPC hot) |
| Contact rate | **55%** xuyên suốt (thực tế vận hành); tag đúng SLA 48h ~85% (giả định) → phần Google Ads "nhìn thấy" cho bidding thực chất ~55%×85%≈46,75% của lead raw — rủi ro cần theo dõi nếu sales trễ SLA |
| Bậc cuối | **Maximize Conversions**, primary = `Lead_Contactable` |
| Gates đã mở | G0 (từ đầu). G2/G3/G4/G5: **chưa** — G2 thiếu bằng chứng số, G3+ chưa tới điều kiện tiên quyết ở kịch bản 30tr (`journey-plan` §3.1). tCPA: **chưa** (D74 chưa đủ 30 conv/30 ngày) |

## 3 bài học

1. Tết và mùa nóng CPC (tuần 9–12) siết phễu từ hai đầu cùng lúc — hệ số hiệu quả ×1,15 (D45) + LP fix (+0,3đ) chỉ vừa đủ bù CPC+15%, không tạo dư địa để mở gate mới. CPL-q tốt hơn benchmark không đồng nghĩa đủ điều kiện scale.
2. D30/D45/D60/D74 là điểm **KIỂM**, không phải điểm **MỞ** tự động — D60 và D74 đều đúng lịch nhưng cả hai đều trả lời "chưa", và đó là quyết định đúng (có số chứng minh) chứ không phải bỏ lỡ.
3. Đổi 2 biến cùng lúc (bidding strategy + primary conversion) ở D45 là thao tác nặng nhất trong 90 ngày — tách nó khỏi mọi thay đổi ngân sách trong 2 tuần liền là điều duy nhất giữ learning phase sạch ngay sau khi vừa ra khỏi Tết.
