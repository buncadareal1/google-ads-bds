# Round 8 — Sonnet 5 — 90 ngày

**Kịch bản:** căn hộ Bình Dương · 30tr₫/tháng (1.000.000₫/ngày, trần tháng ~30,4tr `campaign-setup` §2.1) · CPC **26.000₫** (29.900₫ tuần 9-12, +15% mùa nóng `research` §4) · dự án phân phối thật: **`the emerald 68`** (Tập đoàn Lê Phong, Thuận An, Bình Dương — `keywords/master-keywords.csv`). Campaign chạy TỐT ngay từ đầu: CPL-q dưới trần tham chiếu, **contact rate 57%** (số cho trước của kịch bản, trên nền 55% mặc định `sim-rules`, nhờ SLA gọi <5' + validate đầu số triệt để). Mục tiêu placeholder CPL-q = **1.560.000₫** (`research` §2 "trung bình" — breakeven thật vẫn `[chưa điền]`, `journey-plan` §4/§6).

## Setup + quyết định kỳ 1 (D1-30)

**Cấu trúc (bậc 0, `campaign-setup` §2):** #1 `Brand_DuAn` 475k/ngày cap 20k (16 kw `uu_tien=1` từ `brand-the-emerald-68`) · #2 `Brand_CDT` 75k cap 25k (`brand-cdt--tap-doan-le-phong`) · #3 `KhuVuc_GiaoDich` 450k cap 35k (`binh-duong--gia-bang-gia` 15kw + `binh-duong--mua-ban` 6kw) · #4 TaiChinh/#8 NOXH/#7 Discovery/RMKT = 0, dồn vào #3 (0 kw launch ở tier 1). Max Clicks + bid cap, Phrase+Exact, 0 broad. Negative: 382 account-level + 83 campaign-level dán ngày 1 (`keywords/negative-keywords.csv`). Primary = `Lead_Form_Raw`; `phone_click`/`zalo_click` Secondary vĩnh viễn (`tracking/README` luật #2). 11 ô §1.5 áp đủ.

**LP (user tự làm, `tracking/lp-requirements.md`):** CVR = nền 2,0 + message match ≥4/5 (+1,0) + bảng giá above-the-fold (+0,8) + Zalo sticky/click-to-call (+0,6) + form 4 field + 2 dropdown (+0,4) = **4,8%** (trần 6,0, `landing-page/README` yếu tố 1-3). Qualify rate 40% (2 dropdown). Dropdown ngân sách căn hộ: `<2/2-4/4-7/>7 tỷ` (`landing-page/README` checklist nghiệm thu).

**Tuần 1 (D1-7):** không đổi gì (`campaign-setup` §4.1) — chỉ negative D+3 cho term sai ngành rõ rệt.

**Bẫy tuần 2-3 (D8-21):** IS lost (budget) **25%** liên tục + budget cạn trước **19h** mỗi ngày. Kiểm 3 điều kiện `monitoring` §3 "Tăng budget": (a) IS lost budget ≥10% liên tục ≥3 ngày — **25% từ D8-10, đạt** · (b) CPL-q ≤ trần — **1.354.000₫ ≤ 1.560.000₫, đạt** · (c) contact rate đạt — **57% ≥ 50%, đạt**. Cả 3 đúng → soạn đề xuất tăng ngân sách, **nhưng KHÔNG tự áp**: mức tăng cần thiết sẽ đẩy tổng ngân sách tháng vượt 30tr đã duyệt → escalate xin duyệt user (đúng yêu cầu, không phải whitelist auto-apply của `monitoring` §6). **Không nhảy vọt một lần** (tránh học lại từ đầu, `sim-rules` §Phạt kỷ luật: đổi >±20% một lần = learning reset ×0,7) — làm **2 bước ≤20%/lần, cách ≥4 ngày**, mỗi bước re-check điều kiện trước khi áp (`monitoring` §6 luật 4):
- D15 (user duyệt): 1.000.000 → **1.200.000₫/ngày** (+20%).
- D19 (≥4 ngày sau, IS lost vẫn ≥10%, CPL/contact vẫn đạt): 1.200.000 → **1.440.000₫/ngày** (+20%).
- Tổng: 1.000.000 → 1.440.000₫/ngày (**+44% qua 2 bước**, không phải 1 bước — khác hẳn đường "nhảy vọt +48%" đã bị war-game round 8 (4 tuần) đánh dấu là sai).

## Bảng 12 tuần

| Tuần | Chi (₫) | Click | Lead-q | CPL-q (₫) | Bậc bidding | Ghi chú |
|---|---|---|---|---|---|---|
| 1 | 7.000.000 | 269 | 5,17 | 1.354.000 | 0 Max Clicks | Không đổi gì, chỉ negative D+3 |
| 2 | 7.000.000 | 269 | 5,17 | 1.354.000 | 0 | 🚨 IS lost budget 25%, cạn ngân sách trước 19h, 3 ngày liên tiếp (D8-10) → soạn đề xuất, escalate user |
| 3 | 9.120.000 | 351 | 6,74 | 1.353.000 | 0 | D15 +20%→1,2tr (duyệt user) · D19 +20%→1,44tr (re-check đủ điều kiện) |
| 4 | 12.960.000 | 499 | 9,58 | 1.353.000 | 0 | Ổn định ở ngân sách mới; CPL-q không đổi (chứng minh IS lost trước đó chỉ chặn *lượng*, không phải *chất*) |
| **D30** | — | — | — | — | — | **Keap ký xong → ECL bật, `upload_ecl.py` chạy thật** |
| 5 | 10.080.000 | 388 | 7,91 | 1.274.000 | 0 | CVR +0,3 (kỳ 2, insight Clarity mô phỏng: dead-click trên dropdown Ngân sách mobile 390px — native `<select>` khó chạm đúng → đổi bottom-sheet picker, `tracking/clarity-checklist.md` §2) |
| 6 | 10.080.000 | 388 | 7,91 | 1.274.000 | 0 | #1 đã ≥15 conv/30 ngày + contact >50% + ≥4 tuần — đủ điều kiện SỐ §4.4, chờ D45 để đảo primary đúng thứ tự |
| **D45** | — | — | — | — | — | **Chuyển ĐÚNG:** đảo primary → `Lead_Contactable` TRƯỚC, rồi mới bật Maximize Conversions |
| 7 | 10.080.000 | 388 | 6,72 | 1.500.000 | 1 Max Conv (learning 1/2) | CVR ×0,85 — không đổi ngân sách/gì khác trong 2 tuần learning |
| 8 | 12.960.000 | 499 | 9,32 | 1.391.000 | 1 (learning 2/2 → post D59) | Learning hết D58; D59-60 CVR ×1,15 vĩnh viễn (5,1%→5,865%, dưới trần 6,0). Báo cáo tháng 2: 85% lead gắn tag đúng SLA48h (15% mất tag — rủi ro ECL đã biết) |
| **D60** | — | — | — | — | — | **G2 mở** (`xem_bang_gia` ≥1.000 user/30 ngày nhờ content/organic). Mở Demand Gen **15%** ngân sách (216k/ngày, rút từ pool — không xin thêm tiền), Search còn 85% (1.224k/ngày). **Đã điền `Excluded content keywords`** cấp tài khoản → +5% lead-q remarketing (`journey-plan` §3.1 G2) |
| 9 | 10.080.000 | 337 | 7,97 | 1.265.000 | 1 (ổn định, DG bật) | CPC +15%→29.900₫ (mùa nóng T9-12, `research` §4). Search 286,6 click + DG 50,6 click |
| 10 | 10.080.000 | 337 | 7,97 | 1.265.000 | 1 | Ổn định, không đổi gì — tích đủ ≥2 tuần post-learning trước khi xét tCPA |
| **D74** | — | — | — | — | — | Max Conv ổn ≥2 tuần (D59-74) + ≥30 conv/30 ngày → **chuyển `tCPA` = CPA lịch sử +15%** (trong biên ±15%, không phạt) |
| 11 | 10.080.000 | 337 | 7,97 | 1.265.000 | 2 tCPA | tCPA áp từ D75, không đổi ngân sách cùng lúc (`research` §4: mỗi thay đổi 1 lần) |
| 12 | 12.960.000 | 434 | 10,25 | 1.264.000 | 2 | Chốt scorecard 90 ngày |

## Quyết định tại các mốc

| Mốc | Làm gì | Căn cứ doc |
|---|---|---|
| **D30** | ECL bật, `upload_ecl.py` chạy thật; sales bắt đầu tag `Lead_Contactable` SLA 48h (85% tuân thủ, 15% mất tag — biết trước, không phải lỗi mới) | `sim-rules-90` bảng mốc · `PLAN` §6.6 |
| **D45** | Đảo primary → `Lead_Contactable` TRƯỚC, rồi mới `Max Clicks`→`Maximize Conversions`; không đổi ngân sách trong 2 tuần learning | `campaign-setup` §4.4 · `journey-plan` §3.2 bậc 1 |
| **D60** | Mở Demand Gen 15% (tái phân bổ, không tăng tổng ngân sách) sau khi `xem_bang_gia` ≥1.000 user/30 ngày; điền `Excluded content keywords` bắt buộc | `journey-plan` §3.1 G2 · war-game round 5 |
| **D60 (đề xuất)** | **Đề xuất ngân sách tháng mới cho user, có số liệu:** chính thức hoá mức 1.440.000₫/ngày (~43,8tr/tháng, +44% so 30tr gốc) làm baseline — CPL-q ổn định 1,26-1,35tr (thấp hơn trần 1,56tr suốt 60 ngày), IS lost đã về dưới 10% sau 2 bước tăng, contact rate 57% không đổi, G0-G2 đã mở sạch. Không đề xuất tăng thêm nữa lúc này — chưa có bằng chứng cần (ponytail, `CLAUDE.md`) | Yêu cầu bài (60 ngày sau được phép đề xuất) |
| **D74** | Chuyển `Maximize Conversions` → `tCPA` = CPA thực 30 ngày lịch sử **+15%** (đúng biên, không sai) | `campaign-setup` §4.4 · `journey-plan` §3.2 bậc 2 |
| **Không làm** | G1 (mở khu vực/loại hình mới): ngưỡng conv/tháng vẫn `[điền]` — user chưa chốt → không tự mở. G3 (cần tCPA ổn 2 tháng, mới có ~2 tuần) · G4/G5 (PMax/YouTube — chưa có bằng chứng cần vượt Search+DG hiện tại, dù kỹ thuật đủ ECL+30conv) | `journey-plan` §3.1 · ponytail |

## Tổng 90 ngày

| Chỉ số | Giá trị |
|---|---|
| Tổng chi tiêu | **122.480.000₫** (kỳ 1: 36,08tr · kỳ 2: 43,2tr · kỳ 3: 43,2tr — tăng do budget được duyệt ở D15/D19, không phải vung tay) |
| Tổng click | 4.494 |
| Tổng lead qualified | **92,68** |
| **CPL qualified blended** | **1.322.000₫** = 0,85× mục tiêu placeholder 1,56tr (dưới trần suốt 90 ngày, không ngày nào vượt) |
| Xu hướng CPL-q theo kỳ | 1.354.000 → 1.309.000 (kỳ 2 blended) → 1.264.000₫ (hội tụ nhờ CRO + hiệu số Max Conv, bù được cả CPC+15% mùa nóng) |
| Contact rate | **57% ổn định cả 90 ngày**; 85% lead gắn tag đúng SLA48h từ D30 (15% rủi ro mất tín hiệu ECL — chưa xử lý, không phải lỗi mới phát sinh) |
| Qualify rate blended | ~40,1% (không có trần phân khúc như đất nền) |
| Bậc bidding cuối kỳ | **2 — tCPA + ECL + Demand Gen 15%** |
| Gates đã mở | G0 ✓ · G2 ✓ (D60) · G1 ❌ (ngưỡng chưa điền) · G3/G4/G5 ❌ (chưa đủ thời gian ổn định / chưa có bằng chứng cần) |

**Đọc số quan trọng nhất:** khác round đất nền (round 9), phân khúc này **không có trần qualify cứng** — CPL-q giảm dần và có dư địa (0,85× mục tiêu tham chiếu ở cuối kỳ, so với đất nền chạm đúng sàn 1,0×). Đây là lý do đề xuất ngân sách tháng mới ở D60 hợp lý về kinh tế, không chỉ vì "IS lost đòi tăng" — CPL-q không xấu đi khi ngân sách tăng 44%, nghĩa là đường cầu chưa bão hoà ở mức chi hiện tại.

## 3 bài học

1. **IS lost (budget) dai dẳng + CPL/contact đạt là tín hiệu tăng ngân sách rõ nhất hệ có, nhưng "đúng luật" nghĩa là hai việc tách biệt: tốc độ tăng (≤20%/lần, cách ≥3-4 ngày) và quyền quyết định (vượt ngân sách tháng đã duyệt = việc của user, không phải whitelist auto-apply nội bộ). Nhầm lẫn hai luật này ra hai lỗi khác nhau: tăng nhanh quá = learning reset; tăng mà không hỏi = vượt thẩm quyền vận hành.
2. **Hai bước ≤20% cách nhau ≥4 ngày đạt được gần như toàn bộ hiệu quả của một bước "nhảy vọt" (+44% vs +48%) mà không trả giá learning reset.** CPL-q ở tuần 3-4 giữ nguyên tỷ lệ so với tuần 1-2 (1.353-1.354k) — chứng minh IS lost trước đó chặn *lượng*, không phải *chất*; kỷ luật tốc độ không tốn hiệu suất, chỉ tốn vài ngày lịch trình.
3. **Đúng nhịp gate (đảo primary trước Max Conv, chờ đủ 2 tuần trước tCPA, không mở G4/G5 dù kỹ thuật đủ điều kiện) là đòn bẩy kinh tế ngang với tăng ngân sách.** CPL-q hội tụ về 1.264.000₫ ở tuần 12 — thấp hơn cả CPL-q tuần 1 (1.354.000₫) dù CPC đã tăng 15% vì mùa nóng — hoàn toàn nhờ thực thi đúng thứ tự (CRO, ECL, Max Conv, DG, tCPA), không nhờ phá luật nào.
