# Round 5 — Scale 150tr ĐỦ điều kiện (3 dự án, CPC 25k₫, đã qua G3)

**Điều kiện đầu vào (kịch bản):** 3 tháng chạy · 35 conv qualified/30 ngày · ECL upload ổn định · contact rate 58% · đã qua G0→G3 → mức đang chạy = **60tr/tháng (2.000.000₫/ngày)** theo `campaign-setup.md` §5.1, có #1,#2,#3,#4,#8 + #7 broad + RMKT Demand Gen (G2) + #5,#6 T3 (G3); tCPA đã bật ở #1,#2,#3.

**Mốc thời gian:** T0 = 28/7/2026 → 4 tuần = 28/7 → 24/8/2026.

---

## Setup tuần 0 (quyết định + căn cứ doc)

### 0.1 Hiệu chỉnh mô hình từ dữ liệu thật — làm TRƯỚC khi quyết gì

Công thức CVR của `sim-rules` cho LP hiện tại: `2,0 + 1,0 (message match) + 0,8 (bảng giá ATF) + 0,6 (Zalo sticky) + 0,4 (form 4 field + 2 dropdown) = **4,8%**`.
Nhưng dữ liệu 3 tháng của tài khoản nói khác: 60,8tr/tháng ÷ CPC 25k = **2.432 click** → 35 qualified ÷ 40% qualify = **87,5 lead raw** → **CVR thật = 3,60%**.

Hiệu chỉnh (giữ chênh 1,0 điểm giữa nhóm có/không message match ≥4/5, theo `sim-rules`):

| Nhóm traffic | CVR hiệu chỉnh | Gồm |
|---|---|---|
| **Core** (message match ≥4/5) | **3,87%** | #1, #2, #3 (exact/phrase), #4 |
| **Non-core** (mất adder message match) | **2,87%** | #7 broad, ad group broad mới, #5, #6, RMKT Demand Gen |

Kiểm chứng: mix 60tr = core 73% / non-core 27% → `0,73×3,87 + 0,27×2,87 = 3,60%` → 2.432 × 3,60% × 40% = **35,0 qualified** ✅ khớp đúng số kịch bản.

> 🔴 **Phát hiện quan trọng nhất của round:** core thực 3,87% vs mô hình 4,8% → **thiếu đúng ~1 adder** (0,93 điểm). Theo `landing-page/README.md` §Yếu tố 3, rà theo thứ tự: (1) message match 3 luồng chấm 1-5, (2) 5 phần tử above the fold, (3) form 4 field + đúng 2 dropdown. **Vá 1 adder có giá trị lớn hơn toàn bộ kế hoạch scale này** — xem §Tổng kết. Đây là việc user làm (LP do user tự làm, `PLAN.md` §4), không bị gate nào chặn → giao ngay tuần 1.

### 0.2 Bảng quyết định CÓ/KHÔNG

| Công cụ | Quyết định | Căn cứ |
|---|---|---|
| **Keyword `uu_tien` 1+2+3** | ✅ **CÓ — bước ĐẦU TIÊN** | `journey-plan` §3 bảng bộ keyword (150tr = 1+2+3, 8.512 kw trước khi lọc). Chạy script `campaign-setup` §2.4 với `1,2,3` + regex 3 dự án & khu vực của chúng. Kiểm 2.4.6: **0 keyword match Broad** ngoài #7 và ad group broad có chủ đích |
| **tCPA** | ✅ **giữ, KHÔNG chỉnh** ở #1,#2,#3 · #4 chỉ chuyển khi tự đạt ≥30 conv/30 ngày · #5,#6 giữ Max Clicks + cap | `journey-plan` §3 bảng volume · `campaign-setup` §4.4. Đang trong ramp ngân sách → chỉnh tCPA cùng lúc = 2 biến, `sim-rules` phạt reset ×0,7 |
| **Broad barbell** | ✅ **CÓ, 1 bậc** — 1 ad group broad trong #3, tCPA, trần **15% ngân sách #3** (luật nội bộ, `research` §3). #7 đã broad sẵn. Tên dự án **LUÔN Exact** | `research` §3 ("&gt;60tr + offline import ổn: barbell đầy đủ") · `journey-plan` §3.2 bậc 2 (≥30 conv + ECL thật). Google: "It's critical to use Smart Bidding with broad match" → đã có tCPA ✔ |
| **Demand Gen remarketing** | ✅ **CÓ, scale** 300k → 747k/ngày | G2 đã mở từ 60tr. `research` §1: best practice ≥$100/ngày **hoặc ≥10× tCPA/ngày** — 747k ≈ 10× tCPA khi tCPA ~75k |
| **PMax (G4)** | ❌ **KHÔNG — hoãn, chốt §5.4 = phương án (b)** | Điều kiện G4 **đã đủ** (ECL chạy, Search ≥30 conv/tháng, negative account-level tự phủ) nhưng `campaign-setup` §5.4 ghi rõ: *"Chưa chốt thì KHÔNG bật PMax, kể cả khi đã qua G4."* Chốt (b) — chuyển 8% (400k/ngày) sang Demand Gen, nơi **đã có audience GA4 thật**. Lý do: (i) 400k/ngày (~$15) rải **6 kênh** không đủ mật độ; (ii) chưa có bộ creative **≥7 ảnh đúng 3 tỷ lệ + ≥1 video** cho 3 dự án (§5.5 bước 3) — phải có TRƯỚC khi bật; (iii) tiền đó đưa DG vượt ngưỡng ≥10× tCPA. **Mở lại khi:** có creative kit 1 dự án **và** cấp được ≥1tr₫/ngày cho **1 asset group duy nhất** |
| **AI Max** | ❌ **KHÔNG** | 2 lý do độc lập. (1) `journey-plan` §3.2: AI Max = **bậc 4**, cần "Search ổn định ≥6 tuần ở **bậc 3**" (value-based bidding). Hệ mới vào bậc 3 ở tuần 5-6 → AI Max sớm nhất ~tuần 12. (2) Cách an toàn duy nhất để test là **AI Max experiment** (chia trong cùng campaign, `curriculum` §E2) — mà nó **bị chặn bởi Portfolio Bidding Strategy, Shared Budgets, text customization, Display targeting, bidding exploration**. → giữ portfolio + shared budget **TẮT** để không tự khoá đường này |
| **Portfolio bidding** | ❌ **KHÔNG** | (i) **Không thoả điều kiện của chính doc**: `campaign-setup` §5.2 yêu cầu "≥4 campaign **cùng CPA mục tiêu**" — hệ có brand (#2, CPA thấp), generic (#4), T3 nghiên cứu (#5,#6, CPA cao hẳn) → **khác CPA**, và `research` §4 cấm gộp brand với generic. (ii) Chặn AI Max experiment (trên). (iii) Nếu kèm shared budget thì chặn luôn **seasonal budget adjustment** (`research` §4 bảng) — công cụ cần cho đợt mở bán T10-12. (iv) Có cách rẻ hơn cho campaign thiếu volume: **gộp/tắt** (`journey-plan` §3: "dưới ~15-30 conv/tháng thì gộp, đừng tách") → xem quyết định #8 |
| **#8 NhaOXaHoi** | ❌ **TẮT**, dồn 57k/ngày vào #3 | `campaign-setup` §2.1 ghi chú #8: "chỉ bật nếu **thực sự** phân phối NOXH". 3 dự án không có NOXH → campaign này chỉ tạo thêm 1 nguồn dưới ngưỡng volume. Đây là lời đáp cho "cần portfolio bidding" mà không phải bật portfolio |
| **YouTube (G5)** | ❌ **KHÔNG** | G5 cần **G4 ổn định ≥6 tuần** (G4 chưa mở) + video dự án tự sản xuất + **media plan Reach Planner** (`journey-plan` §3.1). Thiếu cả 3 |
| **tROAS / value-based (bậc 3)** | ⏸ **Lên lịch tuần 5-6**, không làm trong round | Điều kiện đã đủ (thang 10/50/500 = 2 giá trị non-zero, ≥15 conv/tháng cấp tài khoản, `research` §5) nhưng `campaign-setup` §5.7: "mở **một** gate mỗi lần". Đổi bid strategy giữa lúc ramp ngân sách = reset learning. Khi làm: đi bằng **campaign experiment** (`curriculum` §E2) chứ không đổi thẳng |
| **Tool chống click tặc** | ❌ chưa | Chi tiêu đã >50tr nên "được phép cân nhắc" (§5.3), nhưng `research` §5 thứ tự: đọc cột **Lượt nhấp không hợp lệ** trước (<10% là bình thường). Chưa có số → chưa mua |
| **Shared budget** | ❌ **KHÔNG** (giữ nguyên §1.5.10) | Chặn seasonal budget adjustment + AI Max experiment. Đã lợi 3 lần vì không bật |

### 0.3 Ramp ngân sách — con số phải nói trước

Luật: **≤20%/lần, cách ≥3-5 ngày** (`journey-plan` §3). Từ 2.000.000 → 5.000.000₫/ngày cần **6 bậc**; không có đường tắt.

🗓️ **Chặn mùa vụ — `campaign-setup` §5.7: "Mùa vụ ghi đè mọi kế hoạch scale".** **1/7 âm ≈ 13/8/2026** (Rằm ≈ 27/8, hết tháng ≈ 10/9 — cần xác nhận bằng lịch âm). Tuần 3-4 của round nằm **trong tháng 7 âm**, giai đoạn `research` §4 ghi "sụt phân khúc để ở → chuyển remarketing/nurture". → **KHÔNG hoàn thành ramp tới 150tr trong tháng 7 âm.** Dừng ramp ở bậc cuối trước 13/8, giữ mức đó, đổi **mix** thay vì đổi tiền; ramp nốt từ ~11/9 để 150tr đầy đủ rơi vào cao điểm T10-12.
*(Không dùng seasonality adjustment: Google cấm dùng cho mùa vụ **định kỳ** và cho giai đoạn >14 ngày. Không dùng seasonal budget adjustment: nó **chỉ tăng**. Tháng 7 âm = thao tác tay.)*

| Bậc | Ngày | Tổng ₫/ngày | Δ |
|---|---|---|---|
| 0 | — | 2.000.000 | — |
| 1 | D1 (28/7) | 2.400.000 | +20% |
| 2 | D4 (31/7) | 2.870.000 | +19,6% |
| 3 | D7 (3/8) | 3.430.000 | +19,5% |
| 4 | D10 (6/8) | 3.960.000 | +15,5% |
| 5 | D13 (9/8) | **4.285.000** | +8,2% |
| — | D13→D28 | **GIỮ 4.285.000** | tháng 7 âm |

→ Run-rate cuối kỳ = 4.285.000 × 30,4 = **130,3tr/tháng = 87% mandate**. Phần còn lại mở sau 10/9. Mỗi bậc chỉ bấm khi **Lost IS (budget) > Lost IS (rank)**; nếu ngược lại thì vấn đề là rank/coverage, không phải tiền.

**Phân bổ tại D13** (không campaign nào đổi >20%/bậc):

| Campaign | 60tr | D13 | × | Ghi chú |
|---|---|---|---|---|
| #1 Brand_DuAn | 583.000 | **875.000** | 1,50 | 3 ad group = 3 dự án. **Trần theo brand IS**, không scale tuyến tính — dừng khi IS ≥90%, tiền dư đẩy sang #3 |
| #2 Brand_CDT | 117.000 | **175.000** | 1,50 | cùng lý do |
| #3 KhuVuc_GiaoDich | 627.000¹ | **1.560.000** | 2,49 | gồm ad group **broad ≤234.000** (15%) |
| #4 TaiChinh | 133.000 | **331.000** | 2,49 | |
| #7 Discovery broad | 100.000 | **249.000** | 2,49 | đã có tCPA từ 60tr |
| RMKT Demand Gen | 300.000 | **747.000** | 2,49 | +400k của PMax hoãn → tới 1.150.000 khi ramp nốt sau 10/9 |
| #5 PhapLy_TienDo | 60.000 | **149.000** | 2,49 | |
| #6 NghienCuu | 80.000 | **199.000** | 2,49 | nhận keyword `uu_tien` 3 |
| #8 NhaOXaHoi | 57.000 | **0** | — | tắt, dồn vào #3 |
| PMax / YouTube | 0 | **0** | — | §5.4 (b) / G5 chưa đủ |
| **Tổng** | 2.000.000 | **4.285.000** | | |

¹ đã gồm 57.000 của #8.

### 0.4 Việc bắt buộc kèm scale (không phải "tuỳ chọn")

| # | Việc | Căn cứ |
|---|---|---|
| 1 | **`Excluded content keywords`** (cấp tài khoản) — 386 negative account-level **chỉ phủ Search + Shopping**. RMKT **Demand Gen đang chạy YouTube/Display** → inventory đó hiện **không có negative nào**. Ô này đáng ra phải điền từ lúc mở G2, không phải đợi G4 | `campaign-setup` §5.5 hộp cảnh báo |
| 2 | **Account-level placement exclusion**: loại `App categories` / `Games` | §5.5 bước 7 |
| 3 | **Audience exclusion `da_generate_lead_14d`** khỏi mọi campaign acquisition + #7 + DG. Là **bước SAU khi publish**, không có ô trong luồng tạo campaign | `journey-plan` §2.1 hộp chặn GĐ5 · §5.5 |
| 4 | Rà lại **11 ô §1.5** cho mọi campaign; đặc biệt **1.5.6 ACA TẮT** (mốc 9/2026 auto-upgrade ACA→AI Max) và **1.5.11 auto-apply TẮT HẾT** | `campaign-setup` §1.5 · §5.7 |
| 5 | 5 audience GA4 gắn **Observation** trên mọi Search campaign (không Targeting) — miễn phí, để đọc chênh CVR | `research` §3 |
| 6 | Ad group broad mới: đọc search terms **hàng ngày 7 ngày đầu**, không phải hàng tuần | `journey-plan` §5 nghi thức 3 lượt |

---

## Nhật ký tuần 1-4

Giả định giữ nguyên: CPC 25k · qualify 40% (2 dropdown) · contact rate **58%** (số quan sát của kịch bản; công thức `sim-rules` cho 55% khi có dropdown + validate đầu số + SLA <5' → 58% là trên mức mô hình, không cần suy lại). Tỷ lệ click rác chưa lọc: **0%** tuần 1 (negative đã chạy 3 tháng), **1%** tuần 2-3 (ad group broad mới, trước khi quét), **0,5%** tuần 4.

| Tuần | Chi tiêu | Click | Lead raw | Lead qualified | Contact rate | CPL-q | Sự kiện | Hành động + căn cứ |
|---|---|---|---|---|---|---|---|---|
| **1**<br>28/7–3/8 | 19.240.000 | 770 | 28 | 11 | 58%<br>(16 liên hệ được) | **1.749.000** | Ngân sách tăng nhưng tCPA **không tiêu hết** — Lost IS (budget) thấp, Lost IS (rank) cao ở #3/#6 → thiếu **độ phủ**, không thiếu tiền | **Coverage trước, tiền sau, target sau cùng.** (a) Chạy script §2.4 `uu_tien 1,2,3` lọc 3 dự án + khu vực → import Exact/Phrase, kiểm 2.4.6 **0 dòng Broad**; (b) **tắt #8**, dồn vào #3 (§2.1); (c) bậc ramp 1-3; (d) **KHÔNG** chỉnh tCPA (`journey-plan` §3: ±15%/lần, chờ 1-2 tuần — sẽ đẩy CPL lên trực tiếp, coverage thì không); (e) giao user **audit LP theo `landing-page/README` §Yếu tố 3** — thiếu 0,93 điểm CVR (§0.1); (f) điền `Excluded content keywords` + placement exclusion (§0.4) |
| **2**<br>4/8–10/8 | 27.310.000 | 1.081 | 38 | 15 | 58%<br>(22) | **1.821.000** | 🪤 **Bẫy 1:** #4/#5/#6 đều dưới 30 conv/30 ngày → trang Recommendations đẩy "gộp bằng **portfolio bidding** + **shared budget**" | ❌ **Từ chối cả hai.** Doc của chính hệ (§5.2) chỉ cho portfolio khi "≥4 campaign **cùng CPA mục tiêu**" — brand/generic/T3 khác CPA và `research` §4 cấm gộp brand+generic. Cái giá thật: portfolio/shared budget **chặn AI Max experiment** (`curriculum` §E2) và shared budget chặn **seasonal budget adjustment**. Cách lười hơn đã dùng ở tuần 1: **tắt #8**. → Mở **broad barbell 1 bậc**: 1 ad group broad trong #3, tCPA, trần 15% (234k); đọc search terms **hàng ngày**. Bậc ramp 4-5. `Auto-apply` vẫn TẮT — dismiss recommendation làm **tăng optimization score**, và score **không phải KPI** (`research` §7b) |
| **3**<br>11/8–17/8 | 29.995.000 | 1.188 | 41 | 16 | 58%<br>(24) | **1.875.000** | 🪤 **Bẫy 2:** G4 đủ điều kiện trên giấy → Recommendations đẩy **PMax** + **AI Max**. Đồng thời **1/7 âm ≈ 13/8** | ❌ **PMax KHÔNG** — chốt §5.4 = **(b)**: 400k/ngày rải 6 kênh không đủ mật độ, chưa có ≥7 ảnh đúng 3 tỷ lệ + video (§5.5 bước 3); 8% chuyển sang DG. *(Nếu sau này bật: 12 bước §5.5 là bắt buộc, hai ô dễ chết nhất là **bước 5 brand exclusions** và việc negative **chỉ phủ nửa Search/Shopping** của PMax → phải có `Excluded content keywords` cho nửa Display/YouTube.)* ❌ **AI Max KHÔNG** — bậc 4 cần bậc 3 ổn ≥6 tuần (`journey-plan` §3.2); bật lúc này còn tự chặn đường experiment nếu đã có portfolio. 🗓️ **Mùa vụ ghi đè**: **dừng ramp**, giữ 4.285.000₫/ngày; đổi **mix** — nghiêng DG remarketing/nurture + nhóm `dau-tu` (tháng 7 âm sụt phân khúc **để ở**, không sụt đầu tư), giữ nguyên tổng tiền (không cắt >20% để khỏi reset learning) |
| **4**<br>18/8–24/8 | 29.995.000 | 1.194 | 41 | 16 | 58%<br>(24) | **1.875.000** | Broad ad group đã qua 2 vòng quét → waste về 0,5%. Cuối kỳ báo cáo + review gate | Checklist tuần đủ (`research` §8): T2 search terms + invalid clicks + placement · T3 **contact rate trước CPL** + đối chiếu Ads↔GA4↔**CRM (CRM thắng)** + upload ECL · T4 CPC/CVR/CPL theo intent tier · T5 Auction Insights + Lost IS budget vs rank · T6 báo cáo 8 số + 1 hypothesis. **Chấm chất lượng lead 0-9** (`journey-plan` §5 tuần #6) xếp hạng ad/keyword **theo điểm, không theo CPL**. Lên lịch tuần 5-6: **bậc 3 value-based qua campaign experiment**, không đổi thẳng. Lịch: ramp nốt lên 5.000.000₫/ngày từ ~**11/9** |

**Không có phạt kỷ luật nào bị áp:** mọi bậc ngân sách ≤20% · tCPA không chỉnh · negative đã có từ ngày 1 · không bật broad/PMax/tCPA khi chưa đủ gate · không đổi bid strategy giữa ramp → **không learning reset**.

---

## Tổng kết

| Chỉ số | 4 tuần | So baseline (60tr) |
|---|---|---|
| Chi tiêu | **106.540.000₫** | run-rate cuối kỳ 130,3tr/tháng = **87% mandate** (13% giữ lại cho tháng 7 âm) |
| Click | 4.233 | |
| **Lead raw** | **148** | |
| **Lead liên hệ được** (58%) | **86** | KPI báo cáo **trước** CPL (`research` §5) |
| **Lead qualified** | **58** | run-rate 69/tháng vs 35 → **+97% volume** |
| **CPL qualified** | **1.837.000₫ (1,84tr)** | baseline 1,74tr → **+6%**. Kịch bản "trung bình" của `research` §2 = 1,56tr → **kém 18%** |
| CTR giả định | **7,6%** → impression ≈ **55.700** | `research` §2 WordStream 2026 Real Estate (**Mỹ**) — mốc thô, **không phải benchmark VN**. Tài khoản đã chạy 3 tháng → **dùng CTR thật trong Ads, đừng dùng số này**; nó chỉ là chỗ trống vì kịch bản không cấp |

**Đọc đúng con số 1,84tr:** hệ **không** đạt 1,56tr, và lý do **không phải** kỷ luật scale mà là **CVR**. Tài khoản vào round đã ở 1,74tr (CVR thật 3,60% vs mô hình 4,8%). Scale lên trên phễu tất yếu đẩy CPL-q lên vì tỷ trọng non-core tăng 27% → 42%. Đổi 6% CPL-q lấy 97% volume là đánh đổi **có lợi** ở mức 150tr — nhưng đòn bẩy thật nằm chỗ khác:

> **Upside CRO (không bị gate nào chặn):** vá lại 1 adder thiếu ở LP → core 3,87% → 4,8%, non-core 2,87% → 3,8%. CVR mix tuần 4 = 4,38% → 52 lead raw, **21 qualified**, **CPL-q = 1.428.000₫ (1,43tr)** — **thắng cả mốc 1,56tr**, không tốn thêm đồng ngân sách nào. `landing-page/README`: "Nâng CVR 1,5% → 4% ngang tăng 2,5× ngân sách."

**Trạng thái gate cuối kỳ**

| Gate / bậc AI | Trạng thái |
|---|---|
| G0, G1, G2, G3 | ✅ đã qua, đang chạy |
| **G4 (PMax)** | ⚠️ **điều kiện ĐỦ, quyết định HOÃN** — §5.4 chốt phương án **(b)**, ngày 2026-07-28. Mở lại khi: creative kit 1 dự án (≥7 ảnh đúng 3 tỷ lệ + ≥1 video) **và** ≥1tr₫/ngày cho 1 asset group |
| **G5 (YouTube)** | ❌ chưa — thiếu G4 ổn định ≥6 tuần, video, media plan Reach Planner |
| Bậc AI (`journey-plan` §3.2) | **bậc 2** (tCPA + ECL thật + broad có kiểm soát). Bậc 3 (value-based) lên lịch tuần 5-6 **qua campaign experiment**. Bậc 4 (AI Max) sớm nhất ~tuần 12 |
| Portfolio bidding / shared budget | ❌ **cố ý TẮT** — giữ mở đường AI Max experiment + seasonal budget adjustment |

### 3 bài học

1. **Ở 150tr, ràng buộc không phải tiền mà là độ phủ.** tCPA sẽ **không tiêu hết** ngân sách vừa tăng nếu không mở coverage trước — và phản xạ sai là nâng tCPA (đẩy CPL lên ngay). Thứ tự đúng: **coverage (keyword `uu_tien` 3, broad có trần, thêm khu vực) → ngân sách → target**, đọc `Lost IS (budget)` vs `(rank)` để biết mình đang thiếu cái nào.
2. **"150tr/tháng" trên giấy = ~107tr chi thực trong 4 tuần đầu.** Luật ≤20%/bậc biến 2,5× thành 6 bậc, và mùa vụ (tháng 7 âm từ ~13/8) ghi đè nốt phần còn lại. Ai hứa chi hết 150tr từ tuần 1 là đang hứa một lần learning reset. **Con số này phải nói trước khi nhận ngân sách**, không phải giải thích sau.
3. **Điểm mù negative: 386 dòng account-level chỉ phủ Search + Shopping.** RMKT Demand Gen đã chạy YouTube/Display từ lúc mở G2 — inventory đó **chưa có negative nào**, và `Excluded content keywords` bị cả hệ mặc định coi là "việc của G4/PMax". Câu hỏi rà quét đúng không phải "đã dán negative chưa" mà **"campaign nào của mình đang chạy trên inventory không phải Search?"**.

---

### Việc phải ghi ngược vào doc (agent này không được sửa file khác)

| Doc | Nội dung cần ghi |
|---|---|
| `playbook/customer-journey-plan.md` §3.1 | Chốt §5.4 = **(b)** hoãn PMax, ngày 2026-07-28 + điều kiện mở lại (§5.4 yêu cầu ghi vào đây) |
| `playbook/campaign-setup.md` §5.4 | Đổi trạng thái từ "⚠️ QA CHƯA CHỐT" → đã chốt (b) |
| `playbook/campaign-setup.md` §5.2 | Thêm cảnh báo: portfolio bidding **loại nhau** với AI Max experiment; kèm điều kiện "≥4 campaign **cùng CPA**" phải kiểm thật, không mặc định đúng ở 150tr |
| `playbook/campaign-setup.md` §1.4 hoặc §5.5 | Nâng `Excluded content keywords` thành việc của **G2** (khi mở Demand Gen), không phải G4 |
| `playbook/monitoring.md` | Mốc mùa vụ: tháng 7 âm 2026 ≈ 13/8 → 10/9 — **khoá ramp** trong khoảng này |
