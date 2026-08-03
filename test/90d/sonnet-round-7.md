# Round 7 — Sonnet — 90 ngày

Kịch bản: 30tr₫/tháng (1.000.000₫/ngày → 7.000.000₫/tuần, mô hình quy 12 tuần × 7 ngày = 84 ngày ≈ 90 ngày, cùng quy ước `test/round-7.md` gốc), **căn hộ Thủ Đức**, CPC nền **30.000₫**. Click/tuần = ngân sách tuần / CPC (negative 386 dòng vào ngày 1 → không phạt click rác, `sim-rules` §Công thức).

## Setup + quyết định kỳ 1 (có xử lý bẫy)

**Pre-flight** (`campaign-setup.md` §1, giống `round-7.md` gốc — không lặp lại chi tiết): verification nộp trước · 6 conversion action (count=One, cửa sổ 90 ngày, goal category §1.2.7) · GA4↔Ads + auto-tagging · **386 negative account-level**. **11 ô §1.5 — quyết định ăn thua của round này: §1.5.1 Search Partners = TẮT** (cùng Display Expansion tắt, location Presence, ACA tắt, auto-apply tắt hết). Đây là lựa chọn của agent khi dựng tài khoản, không phải mặc định — chốt tắt vì playbook liệt nó vào 11 ô bắt buộc, không phải tuỳ chọn.

**Cấu trúc (3 campaign, `journey-plan` §3 = uu_tien 1, giống `round-7.md`):**

| # | Campaign | ₫/ngày | Cap | uu_tien=1 |
|---|---|---|---|---|
| 1 | `Brand_DuAn` (3 dự án Thủ Đức) | 475.000 | 20.000 | 24 kw |
| 2 | `Brand_CDT` | 75.000 | 25.000 | 5 kw |
| 3 | `KhuVuc_GiaoDich` (thu-duc--*) | 450.000 | 35.000 | 20 kw |

#4 TaiChinh, #8 NOXH = 0 (dồn vào #3, không đủ kw uu_tien=1). #7 Discovery, RMKT = 0 — hoãn tới gate. **Bidding: Max Clicks + cap** cả 3 (bậc 0, `research` §4).

**LP (`landing-page/README.md` ma trận CRO):** message match brand ≥4/5 (+1,0) · Zalo sticky/click-to-call (+0,6) · form 4 field + 2 dropdown ngân sách/mục đích (+0,4) · **bảng giá above the fold thiếu tuần 1** (nghiệm thu 3/5 mục đó, tổng vẫn ≥3,0 → launch, backlog tuần 1). CVR = 2,0 nền +1,0+0,6+0,4 = **4,0%** tuần 1 → **4,8%** từ tuần 2 khi vá bảng giá (+0,8). Trần 6,0 chưa chạm. Qualify rate **40%** (2 dropdown). Contact rate mô hình **55%**.

**Tuần 1:** không đổi cap/ngân sách/RSA/kw (`campaign-setup` §4.1). Chi 7,0tr, click 233,3, lead-q 3,73, CPL-q **1.876k**, contact **55%**.

**Tuần 2 — BẪY: contact rate 55%→25% dù lead raw tăng** (CVR đã lên 4,8% sau khi vá LP). Chẩn đoán đúng thứ tự `research` §8 T3 (đối chiếu Ads↔Keap → đọc 10 lead → mới kết luận), **không đọc lead trước**:

| Bước 1 — đối chiếu Ads↔Keap | Kết quả |
|---|---|
| Ads → Phân đoạn → Mạng | **100% "Tìm kiếm của Google", 0 click Đối tác** — vì §1.5.1 đã tắt từ tuần 0. Loại ngay giả thuyết "lead rác từ Search Partners" |
| Ads `generate_lead` vs Keap lead mới cùng kỳ | Khớp (không lệch nguồn/dedup) |
| Keap: lead có gclid, đủ 2 dropdown, đầu số hợp lệ | 11/11 — chất lượng đầu vào không đổi so với tuần 1 |
| Search terms tuần 2 | 0 term sai intent ≥3 click |

→ Traffic sạch, chất lượng đầu vào không đổi. Nếu là lead rác phải thấy chi tiêu ở Đối tác hoặc lead thiếu gclid/dropdown — **không thấy cái nào**, nên bước 2 mới đọc lead (không phải để tìm nguyên nhân mà để xác nhận).

| Bước 2 — đọc 10 lead gần nhất | Kết quả |
|---|---|
| Nội dung hợp lý (ngân sách/mục đích khớp Thủ Đức) | 10/10 |
| Có activity gọi ra trong Keap | 2-3/10 |
| Lead **được gọi** thì liên hệ được | 3/3 = 100% |

**Bước 3 — kết luận:** mẫu số vỡ, không phải tử số. **Nguyên nhân gốc: nhân viên trực máy nghỉ 3 ngày liên tục giữa tuần, không bàn giao ca → SLA gọi <5' vỡ.** Vì §1.5.1 đã tắt tuần 0 nên nhánh "lead rác từ đối tác" bị loại bằng số ở bước 1 — đây là process, không phải Ads. **Không đụng bid/ngân sách/keyword** (kỷ luật `campaign-setup` §4.2-4.3: chỉ số vỡ nằm sau lead). Hành động: lịch trực luân phiên có bàn giao + Keap automation (auto-assign, Zalo/SMS tự động khi submit, escalate nếu 60' chưa có activity) + rescue 8,4 lead nguội ở tuần 3 (ghi riêng, không cộng vào contact rate) + điền SLA vào `journey-plan` §5 (5' trong giờ trực, 100% lead có người bấm gọi trong 24h).

**Tuần 3-4:** contact rate hồi 55%, vòng negative 3 lượt bình thường (`journey-plan` §5), thêm RSA thứ 2 tuần 3. Không đổi bidding.

## Bảng 12 tuần

| Tuần | Chi | Click | Lead-q | CPL-q | Bậc bidding | Ghi chú |
|---|---|---|---|---|---|---|
| 1 | 7,0tr | 233,3 | 3,73 | 1.876k | Max Clicks | CVR 4,0% (chưa vá bảng giá) |
| 2 | 7,0tr | 233,3 | 4,48 | 1.563k | Max Clicks | CVR 4,8%; **BẪY contact 55%→25%** — chẩn đoán ở trên, kết luận: process |
| 3 | 7,0tr | 233,3 | 4,48 | 1.563k | Max Clicks | Contact hồi 55%; rescue 8,4 lead nguội (riêng) |
| 4 | 7,0tr | 233,3 | 4,48 | 1.563k | Max Clicks | Ổn định, chuẩn bị D30 |
| 5 | 7,0tr | 233,3 | 4,85 | 1.442k | Max Clicks | **D30** ECL bật nhưng contact rate 30-ngày (t.1-4) = 47,5% <50% → **chưa** đủ điều kiện chuyển bidding, giữ nguyên. CVR +0,4 (Clarity: rage-click nút dropdown "Mục đích" bị Zalo sticky che ở mobile 390px → tăng z-index/margin) → **5,2%** |
| 6 | 7,0tr | 233,3 | 4,85 | 1.442k | Max Clicks | Rolling contact rate sạch (t.3-6 = 55%) nhưng **D45 chưa tới** — không chuyển sớm dù đủ điều kiện bề mặt (mốc cố định, `sim-rules-90`) |
| 7 | 7,0tr | 233,3 | 4,12 | 1.697k | Maximize Conv (học) | **D45** đủ ≥30 conv/30 ngày + contact >50% → đảo primary **`generate_lead`→`Lead_Contactable` TRƯỚC**, rồi bật Maximize Conversions (`campaign-setup` §4.4). Learning 2 tuần: CVR ×0,85 → 4,42% |
| 8 | 7,0tr | 233,3 | 4,12 | 1.697k | Maximize Conv (học) | Không đổi gì khác trong learning (`research` §4) |
| 9 | 5,95tr+1,05tr DG | 172,5 (Search) | 4,35 | 1.611k | Maximize Conv | **D60** G2 mở (audience đủ nhờ content/organic) → Demand Gen 150k/ngày (=15%, đúng trần), điền Excluded content keywords → +5% lead-q. CPC brand+khu vực **+15%→34.500₫** (mùa nóng T9-12). Learning hết: hệ số hiệu quả ×1,15 → CVR chạm **trần 6,0%** (5,6%×1,15=6,44%, cắt về trần) |
| 10 | 7,0tr | 172,5 | 4,35 | 1.611k | Maximize Conv | Ổn định tuần thứ 2 liên tiếp — chuẩn bị D74 |
| 11 | 7,0tr | 172,5 | 4,35 | 1.611k | tCPA | **D74** đủ (Maximize Conv ổn ≥2 tuần + ≥30 conv) → tCPA = CPA lịch sử **+15%** (đúng trần luật, không quá) |
| 12 | 7,0tr | 172,5 | 4,35 | 1.611k | tCPA | Giữ nguyên, không chỉnh gì thêm trong kỳ (learning tCPA) |

**[GIẢ ĐỊNH MÔ HÌNH — sim-rules-90 không nói cơ chế multiplier gắn vào đại lượng nào]:** áp "CVR ×0,85 học" và "hệ số hiệu quả ×1,15" lên **CVR** (chuỗi CVR→lead raw→lead-q→CPL-q là chuỗi duy nhất sim-rules định nghĩa), không áp lên CPL-q trực tiếp — ghi rõ đây là suy diễn, không phải công thức có sẵn.

## Quyết định tại các mốc D30/D45/D60/D74

**D30 — không chuyển bidding dù ECL đã bật.** Điều kiện `campaign-setup` §4.4 (Max Clicks→Maximize Conversions) đòi contact rate **>50% trong 30 ngày**; trailing tuần 1-4 = (55+25+55+55)/4 = **47,5%** — tuần bẫy còn kéo số xuống. ECL sống (upload_ecl chạy) nhưng chưa dùng để đổi chiến lược đấu giá. Đúng bài học round-7 gốc: không "làm sạch" cửa sổ bằng cách loại tuần xấu.

**D45 — chuyển ĐÚNG.** Tại mốc cố định này (không sớm hơn dù t.3-6 đã sạch 55% — dòng thời gian mở khoá là cố định cho mọi round, `sim-rules-90` §Dòng thời gian), kiểm đủ cả 2: ≥30 conv/30 ngày (raw ~44-49/tháng) và contact rate >50% (55% rolling). Thứ tự thực thi đúng luật: **đảo primary sang `Lead_Contactable` trước**, rồi mới bật Maximize Conversions — tránh nhánh "chuyển SAI" (qualify rate ×0,75 vĩnh viễn vì bidding học form thô).

**D60 — G2 mở, không mở PMax/broad dù kỹ thuật cho phép.** Audience `xem_bang_gia` đạt ngưỡng nhờ content/organic (sự kiện cố định của dòng thời gian, không phải traffic ads — ở 30tr/tháng riêng ads không đủ, khớp `journey-plan` §3.1 ghi chú). Mở **Demand Gen remarketing 150.000₫/ngày = đúng trần 15%** (đủ mức tối thiểu ~$5/ngày `journey-plan` §2.1), **điền Excluded content keywords ngay khi mở** (không phải việc "làm sau" — bài học war-game round 5 SCORECARD #5) → +5% lead-q. Nguồn ngân sách: 100k lấy lại từ #1 (khoản này vốn được ghi chú là "mượn từ quỹ Remarketing" ngay từ setup ngày 1, `campaign-setup` §2.1 — trả lại không phải một cú đổi ±20% bất ngờ, #1 chỉ về đúng baseline gốc 375k) + 50k lấy từ quỹ "Discovery" dự trữ ở #3 (450k→400k, -11%, trong hạn ±20%). **Không mở #7 Discovery** dù campaign-setup §4.4 gợi ý mở cùng lúc Maximize Conversions — lệch có ý thức: `journey-plan` §3.2 bậc 2 (nơi thật sự cho phép test broad) đòi ≥30 conv + **ECL chạy thật ở bậc tCPA**, tức ngang hàng điều kiện D74 chứ không phải D45; mở #7 ở D45 sẽ là bật broad khi tài khoản còn ở Maximize Conversions vừa vào learning — không có bằng chứng cần thêm campaign type lúc này (ponytail, `CLAUDE.md`). Hoãn quyết định #7 sang quý sau.

**D74 — tCPA đúng luật.** Maximize Conversions ổn định ≥2 tuần (t.9-10), ≥30 conv/30 ngày → tCPA = CPA lịch sử **+15%** (đúng biên, không vượt — tránh learning reset ×0,7). Không đồng thời đổi ngân sách (learning riêng, `research` §4).

## Tổng 90 ngày

| Chỉ số | Giá trị |
|---|---|
| Tổng chi | **84.000.000₫** (12 tuần × 7,0tr) |
| Tổng lead-q | **52,5** |
| **CPL-q blended** | **1.600.000₫** (so mốc tham chiếu 1,56tr → +2,6%, gần hết chênh nằm ở tuần 1 CVR thấp + học Maximize Conv t.7-8, được bù bởi hệ số ×1,15 + DG t.9-12) |
| Contact rate blended (KPI #1, báo trước CPL) | **52,4%** (67,7 lead-contactable / 129,2 lead raw) — chỉ 1/12 tuần dưới 50%, đủ để không bị coi là "vấn đề nghiêm trọng" (<40%, `research` §5) |
| % lead gắn tag đúng SLA 48h (từ D30, giả định sim-rules-90) | **85%** — 15% lead contactable mất tag, làm ECL/bidding thấy ít conversion hơn thực tế |
| Bậc bidding cuối kỳ | **tCPA** (từ D74, tuần 11-12) |
| Gate đã mở | **G0** ✅ (D0) · **G2** ✅ (D60, Demand Gen ≤15% + Excluded content keywords) |
| Gate còn đóng | **G1** ❌ (chưa có CPL mục tiêu — thiếu phí môi giới/căn + booking→HĐMB, `journey-plan` §6) · **G3** ❌ (cần tCPA ổn 2 **tháng**, mới có ~1,5 tháng tới D90) · **G4** ❌ (chưa có ≥2 giá trị non-zero chảy về — `Lead_Qualified`/`Dat_Coc` chưa upload volume đủ, mới có `Lead_Contactable`) · **G5** ❌ (cần ≥150tr/tháng) · **#7 Discovery** hoãn có chủ đích (xem D60) |

## 3 bài học

1. **Cửa sổ đo càng dài, một tuần bẫy càng bị pha loãng — nhưng kết luận nguyên nhân không được đổi theo cửa sổ.** Contact rate blended 12 tuần = 52,4% (qua ngưỡng 50%), trong khi bản 4 tuần gốc (`round-7.md`) cùng bẫy cho 47,2% (dưới ngưỡng). Nếu chỉ nhìn con số blended dài hạn sẽ dễ kết luận "không có vấn đề gì" — sai: root cause (SLA vỡ 3 ngày) vẫn phải được chẩn đoán và xử lý ở đúng tuần nó xảy ra, không chờ pha loãng rồi bỏ qua.
2. **Dòng thời gian mở khoá D30/D45/D60/D74 là cố định, không phải "ngưỡng sớm nhất nếu đủ điều kiện".** Tuần 6 đã đủ điều kiện bề mặt để chuyển Maximize Conversions (rolling 55%, ≥30 conv) nhưng vẫn phải chờ tới D45 — kỷ luật giữ gate đúng nhịp (rubric bổ sung 90 ngày) đôi khi có nghĩa là *chờ* dù số liệu đã "xanh", không chỉ là *từ chối* khi số liệu "đỏ".
3. **15% lead mất tag SLA 48h là thuế vô hình lên chính dữ liệu nuôi Smart Bidding.** Từ D30, ECL chỉ thấy 85% lead contactable thật — nghĩa là ngay sau khi đảo primary sang `Lead_Contactable` ở D45, thuật toán đang học từ một tập dữ liệu thiếu 15%, một lỗi process (không phải lỗi kỹ thuật) âm thầm làm chậm chất lượng learning của cả nhánh bidding. Củng cố `PLAN.md` §6.6: SLA gắn tag Keap phải chốt bằng văn bản trước khi tin tưởng số ECL.
