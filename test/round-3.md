# Round 3 — Click tặc 30tr

Kịch bản: 30tr₫/tháng · căn hộ TP.HCM · CPC kịch bản **35.000₫** (sát mức "thận trọng 40k" của `research` §2 — căn hộ = phân khúc cạnh tranh nặng nhất, §2).
Đơn vị tuần: **7.000.000₫/tuần** (1.000.000₫/ngày × 7; trần tháng 30,4tr theo `campaign-setup` §2.1). 4 tuần = 28,0tr.

## Setup tuần 0 (quyết định + căn cứ doc)

**Dự án thật chọn từ `keywords/projects.tsv`:** `lumiere midtown` + `masteri grand view` (Masterise Homes, căn hộ, Thủ Đức TP.HCM, hạng A). Cùng khu vực → 1 ad group khu vực phục vụ cả 2.

**1. Cấu trúc — 2 campaign, 3 ad group (KHÔNG phải 5 campaign như `campaign-setup` §2.1 mặc định).**
Lý do là số học, không phải khẩu vị: §2.3 tính 3 ad group cho #1 dựa trên **bid cap 20k**. Ở CPC kịch bản **35k**, mỗi 100k₫/ngày chỉ mua 2,9 click/ngày → `#2 Brand_CDT` (75k) và `#4 TaiChinh` (70k) mỗi cái ~2 click/ngày ≈ 3 lead/tháng, dưới ngưỡng **≥10 conv/ad group** (`adgroup-map`) và dưới luật **"campaign <15–30 conv/tháng thì gộp, đừng tách"** (`journey-plan` §3). `research` §1 ở dải 20–80tr chỉ bắt buộc **tách Brand khỏi Generic** — 2 campaign là đủ luật.

| # | Campaign | ₫/ngày | Ad group | Kw (uu_tien=1) | Bid cap |
|---|---|---|---|---|---|
| 1 | `BDS_Search_Brand_DuAn` | **550.000** (55%) | `brand-lumiere-midtown`, `brand-masteri-grand-view` | 8 + 8 | 20.000 |
| 3 | `BDS_Search_KhuVuc_GiaoDich` | **450.000** (45%) | `thu-duc--gia-bang-gia` | 15 | 35.000 |

Hoãn (ghi rõ để không ai tưởng bỏ quên): `#2 Brand_CDT` (tier 3 intent, `research` §3) · `#4 TaiChinh` · `#8 NhaOXaHoi` (không phân phối NOXH) · `#7 Discovery` broad (bắt buộc tCPA, ngày 1 có 0 conversion) · `RMKT` (chưa qua G2). Bottom funnel = **100%** ≥80% → thoả QA Q4 `journey-plan` §5.
Ngân sách 15% của Discovery+RMKT dồn vào #1/#3 theo đúng cơ chế "mượn quỹ" §2.1, **không** tăng tổng.

**2. Bidding:** cả 2 campaign **Maximize Clicks + bid cap** (`research` §4: tuần 1–3 không smart bidding). Cap chỉ chỉnh khi IS lost (rank) >40% **và** chưa tiêu hết ngân sách, +20%/lần cách ≥3 ngày (§2.2).
*(Ghi nhận mâu thuẫn model: cap brand 20k nhưng CPC kịch bản 35k. Luật giả lập buộc dùng 35k cho mọi click → mọi số dưới đây tính ở 35k. Thực tế brand CPC sẽ rẻ hơn → CPL-q brand thực sẽ tốt hơn bảng này.)*

**3. Negative ngày 1:** **386 dòng** `cap_do=account` vào Từ khoá phủ định **cấp tài khoản** (`campaign-setup` §1.4.1 — tự áp mọi campaign type, không có bẫy "quên gắn"), **80 dòng** `cap_do=campaign` thành shared list gắn cho #1 và #3. Đã kiểm biến thể **không dấu** có trong list (negative KHÔNG khớp close variant — `research` §3 hộp cảnh báo).

**4. Conversion ladder:** tạo đủ **6** action theo `campaign-setup` §1.2, Count=**Một**, cửa sổ click **90 ngày**, goal **category** chuẩn (§1.2.7). Ngày 1: `Lead_Form_Raw` + `Click_Hotline` + `Click_Zalo` = Chính (chỉ để thấy số; Max Clicks không đấu giá theo conversion). `Lead_Contactable`/`Lead_Qualified`/`Dat_Coc` khai sẵn, rỗng.

**5. 11 ô §1.5 áp cho cả 2 campaign:** Search Partners **TẮT** · Display expansion **TẮT** · Vị trí VN + `Sự hiện diện` · Ngôn ngữ VI+EN · ACA **TẮT** · Lịch **05:00–24:00** · phân phối Chuẩn · tracking template UTM · không ngân sách dùng chung · **auto-apply recommendations TẮT HẾT** (§1.5.11 — `Remove conflicting negative keywords` sẽ phá negative list).
→ Hai ô đầu là **lá chắn click tặc dựng trước sự kiện**: Search Partners + Display là nơi click rác rẻ nhất.

**6. LP spec (quyết định CVR):** 2 LP riêng, **không** ad group nào trỏ homepage (§2.4.7 — homepage = ×0,4 toàn bộ CVR).

| Yếu tố `landing-page/README.md` | Chọn | Cộng CVR |
|---|---|---|
| Message match brand ≥4/5 (H1 = headline #1 đã pin, `campaign-setup` §3.1) | ✔ | +1,0 |
| Bảng giá + "từ X tỷ" above the fold 390px | ✔ | +0,8 |
| Zalo sticky + `tel:` click-to-call | ✔ | +0,6 |
| Form 4 field + 2 dropdown (Ngân sách, Mục đích) + validate đầu số + honeypot | ✔ | +0,4 |
| **CVR LP** | | **4,8%** (trần 6,0) |

Qualify rate **40%** (có 2 dropdown). Contact rate **55%** — đủ cả 3 điều kiện: dropdown ✔ · validate đầu số ✔ · **SLA gọi <5'** (chốt ở tuần 0 làm điều kiện bật quảng cáo; đo bằng sổ trực máy tay, không phải ECL).
Hidden field `gclid/gbraid/wbraid/gad_source/gad_campaignid/utm_*` → Keap (skill `ad-click-attribution`); 6 event dataLayer đúng registry `CLAUDE.md`.

**7. G0 (`journey-plan` §3.1) — pass mới bật:** 1 lead thật đi tới Keap có `gclid` ✔ · LP <3s mobile ✔ · negative account-level đã apply ✔ · Search Partners + Display OFF, location Presence ✔.
⚠️ **ECL vẫn CHẶN** (`PLAN.md` §6.6): chưa có quyền thoả thuận quy tắc gắn tag Keap → không có `Lead_Contactable` → hệ bị khoá ở **bậc 0** của `journey-plan` §3.2 suốt 4 tuần. Đây là ràng buộc quyết định của round này, không phải chi tiết phụ.

## Nhật ký tuần 1-4

Tỷ lệ click rác chưa lọc: **T1 0% · T2 19% · T3 8% · T4 8%**. T2 nội suy theo ngày giữa 2 mốc kịch bản cho (30% không xử lý → 8% xử lý đúng), theo đúng lúc từng biện pháp có hiệu lực: `30-30-30-14-14-8-8` → TB **19,1%**.

| Tuần | Chi tiêu | Click | Lead raw | Lead qualified | Contact rate | CPL-q | Sự kiện | Hành động + căn cứ |
|---|---|---|---|---|---|---|---|---|
| 1 | 7,00tr | 200 | 9,6 | 3,84 | 55% | **1,82tr** | — | **KHÔNG đổi** cap/ngân sách/RSA/keyword (`campaign-setup` §4.1 tuần 1). D+3: search terms lượt 1, chỉ negative term sai ngành rõ ràng. D+1 kiểm `gclid` trong Keap ✔ |
| 2 | 7,00tr | 162 | 7,78 | 3,11 | 55% | **2,25tr** | 🚨 **CLICK TẶC**: CTR brand 7%→19%, click từ dải IP hẹp khung 21–23h, bounce ~100%, time-on-page <3s, conversion **không đổi** | 4 bước theo `research` §5 "Click tặc VN" — chi tiết dưới bảng |
| 3 | 7,00tr | 184 | 8,83 | 3,53 | 55% | **1,98tr** | Rác còn 8% (dư sau IP+lịch) | T2 vòng negative đủ 3 lượt (`journey-plan` §5) — **không** thêm negative cho sự kiện (rác nằm trên chính brand keyword, negative là công cụ SAI). T3 contact rate 10 lead gần nhất = 55% ✔. T5 Auction Insights: xác nhận không phải bid war |
| 4 | 7,00tr | 184 | 8,83 | 3,53 | 55% | **1,98tr** | Ổn định | Đo CVR LP thật 4,8% >2% → **không** sửa LP (`research` §6). Quyết định bidding: **GIỮ Max Clicks** (lý do ở Tổng kết). T6 báo cáo + 1 hypothesis |
| **Tổng** | **28,0tr** | **730** | **35,0** | **14,0** | **55%** | **2,00tr** | | |

**Xử lý sự kiện tuần 2 — đúng thứ tự `research` §5, KHÔNG mua tool:**

| Ngày | Bước | Làm gì | Căn cứ |
|---|---|---|---|
| T2.d2 | **0. Phân loại** | Morning brief bắt spend/click đột biến (`monitoring` §2 🔴 ">150% nhịp giờ"). Đối chiếu 3 nguồn: click Ads ↑, session GA4 ↑, lead Keap **phẳng** → là **traffic**, không phải tracking gãy. Clarity xác nhận session không scroll (1 request trong quota 10/ngày) | `journey-plan` §4 (CRM là nguồn đếm) |
| T2.d2–d4 | **1. Invalid clicks** | Đọc cột `Lượt nhấp không hợp lệ` — Google tự lọc + **hoàn tiền**, <10% là bình thường. Chờ đủ **48h** mới đọc (Google xử lý chậm 24–48h) | `research` §5 bước 1 · `monitoring` §1 |
| T2.d3 | **2. IP exclusion** | Dải IP hẹp = đúng ca "click văn phòng cố định" mà `research` §5 cho phép chặn. Dán dải vào `Cài đặt khác → Loại trừ IP` — **trần 500/campaign và KHÔNG có cấp tài khoản** → phải dán cho **cả #1 và #3** | `research` §5 bước 2 |
| T2.d5 | **3. Ad schedule** | Đọc báo cáo **theo giờ** tuần 1 trước: khung 21–24h tuần 1 có lead thật hay không. Siết lịch **05:00–21:00**. Chi phí gần bằng 0 vì campaign đang `limited by budget` — cắt giờ chỉ **dồn** ngân sách vào 05–21h, không mất click. Đặt lịch rà lại T4 | `research` §5 bước 3 · `campaign-setup` §1.5.7, §4.1 tuần 3 |
| — | **4. Tool trả phí: KHÔNG** | ClickCease/Spider AF ~$50–100/tháng chỉ mở ở **>50tr/tháng** (`campaign-setup` §5.3). Ở 30tr, `research` §5 nói thẳng: "sửa LP có ROI cao hơn chống click tặc" | `research` §5 bước 4 |

**3 việc KHÔNG làm trong tuần 2 (quan trọng ngang việc đã làm):**
1. **Không cắt ngân sách #1.** CPL brand tuần 2 xấu là do bị tấn công, không do campaign. Đổi ngân sách >±20% = learning reset (CVR ×0,7 tuần sau) và không sửa được nguyên nhân. `journey-plan` §3.1: không pause producer khi chưa có bản thay thế.
2. **Không sửa LP.** CVR brand tuần 2 sụt vì **mẫu số bị nhiễm**, không vì LP. `research` §6 "CVR <2% = LP hỏng" sẽ báo động giả nếu tính trên click rác.
3. **Không thêm negative.** Truy vấn kích hoạt là chính tên dự án — negative sẽ tự chặn nhóm intent cao nhất.

**Đối chiếu số (không bịa, suy từ luật):**
- Rác tập trung **toàn bộ ở #1** (kịch bản nói CTR *nhóm brand* tăng). T2: #1 mua 110 click/tuần (550k×7÷35k) trong đó **38 rác / 72 thật**; #3 không bị ảnh hưởng, 90 click. 72+90 = 162 ✔.
- **Chéo kiểm 2 số kịch bản cho:** CTR brand 7%→19% ⇒ rác = (1−7/19) = 63% click brand; brand chiếm 55% ngân sách ⇒ rác cấp tài khoản = 34,7% ≈ **30%** như kịch bản nêu. Hai con số **khớp nhau** → 19% là CTR ngày đỉnh, 30% là mức tài khoản dùng cho công thức.
- **Cơ chế thiệt hại thật không phải "tốn thêm tiền" — ngân sách ngày chặn cứng ở 550k. Là CROWDING-OUT:** impression brand = click ÷ CTR quan sát → T1 110÷7,0% = **1.571 imp**; T2 110÷19% = **579 imp** (−63% tiếp cận khách thật); T3–4 110÷8,2% = **1.343 imp**. Khách thật bị đẩy ra khỏi phiên đấu giá — đó là lý do công thức trừ vào *click hữu ích* chứ không cộng vào chi tiêu.
- **Bẫy báo cáo:** CTR brand T3–4 (~8,2%) *thấp hơn* T2 (10,7% TB tuần) → **không phải suy giảm hiệu suất**, là baseline hết bị nhiễm. Đừng lấy CTR tuần 2 làm mốc so sánh.
- Hoàn tiền invalid clicks: **không đưa vào bảng** (kịch bản không cho số) → CPL-q thực tế **tốt hơn** 2,00tr một khoản chưa lượng hoá.

**Chia theo campaign (4 tuần):**

| Campaign | Chi tiêu | Click hữu ích | Lead raw | Lead-q | CPL-q |
|---|---|---|---|---|---|
| #1 Brand_DuAn | 15,4tr | 370 | 17,76 | 7,10 | **2,17tr** |
| #3 KhuVuc_GiaoDich | 12,6tr | 360 | 17,28 | 6,91 | **1,82tr** |

## Tổng kết

**Lead:** 35,0 raw · **19,3 contactable** (55%) · **14,0 qualified** (40%).
**CPL qualified: 2,00tr₫** — so kịch bản "trung bình" 1,56tr của `research` §2: **kém 28%**, nhưng 1,56tr là số ở **CPC 25k**. Ở CPC 35k mà kịch bản áp, sàn số học là 35.000 ÷ 4,8% ÷ 40% = **1,82tr** kể cả khi không có một click rác nào. Khoảng cách 1,82 → 2,00tr chính là toàn bộ thiệt hại còn lại của sự kiện.
**Giá trị của việc xử lý đúng:** nếu để rác 30% từ tuần 2 → 11,90 lead-q, CPL-q **2,35tr**. Xử lý đúng thứ tự = **+2,1 lead qualified** và **−15% CPL-q**, chi phí bỏ ra bằng 0₫ (không mua tool).

**CTR giả định:** brand thật **7,0%** (mốc kịch bản cho, khớp WordStream real estate 7,61% `research` §2). Quan sát: T1 7,0% · T2 10,7% TB tuần (đỉnh 19%) · T3–4 8,2% (còn 8% rác). CTR nhóm khu vực `thu-duc--gia-bang-gia`: **[không suy được từ luật giả lập — cần impression thật]**.

**Trạng thái gate cuối kỳ:**

| Gate | Trạng thái | Vì sao |
|---|---|---|
| G0 | ✅ pass | Đủ 5 điều kiện, đã bật |
| G1 | ⚠️ **không kết luận được** | Điều kiện là "CPL ≤ **mục tiêu**" nhưng CPL mục tiêu tính từ breakeven `journey-plan` §4 — chưa có phí môi giới/căn + tỷ lệ booking→HĐMB. Ngưỡng conv của G1 trong doc vẫn là `[điền]`. **Không tự chấm pass** |
| G2 | 🔒 đóng | Audience `xem_bang_gia`/`engaged_60s` cần ≥1.000 user/30 ngày. 730 click/4 tuần → không thể đạt. ⚠️ Traffic rác tuần 2 **không** đẩy gate này lên vì cả 2 audience đòi hành vi engagement mà bot không có — nhưng `all_visitors_30d` bị phồng, **đừng đọc nó như tiến độ G2** |
| G3 | 🔒 đóng | Cần G2 trước |
| G4 | 🔒 đóng | ECL chưa chạy thật (`PLAN.md` §6.6) |
| G5 | 🔒 đóng | Cần ≥150tr + G4 ổn 6 tuần |
| Bậc AI (`journey-plan` §3.2) | **bậc 0** | Vẫn Max Clicks + Phrase/Exact + auto-apply TẮT |

**Quyết định bidding cuối tuần 4 — GIỮ Max Clicks, không lên Maximize Conversions.**
Điều kiện §4.4 *đã đủ* trên giấy: #1 = 17,8 conv/28 ngày ≥15 · contact rate 55% >50% · chạy ≥4 tuần. Nhưng bậc 1 của §3.2 buộc **đảo primary sang `Lead_Contactable` TRƯỚC** khi bật smart bidding — mà `Lead_Contactable` rỗng vì ECL bị chặn. Bật Maximize Conversions lúc này = để bidding học từ **form thô** = tự mua lead rác (bẫy optimize-to-quality, `tracking/README.md` luật #2). Thêm nữa 1 trong 4 tuần dữ liệu bị nhiễm bởi sự kiện → mẫu chưa sạch.
→ **Việc số 1 của tuần 5 không phải đổi bidding, mà là mở chặn thoả thuận gắn tag Keap.** Không có nó, hệ ở bậc 0 vĩnh viễn bất kể chi bao nhiêu (`journey-plan` §3.2 điểm mấu chốt).

**3 bài học:**

1. **Kỷ luật "Max Clicks trước" biến sự kiện click tặc từ thảm hoạ thành phiền toái.** Siết ad schedule giữa tuần 2 không tốn một ngày learning nào vì không có smart bidding để reset — và `Data exclusion` (thứ đúng ra phải làm khi dữ liệu conversion bị nhiễm) **không dùng được** ở bậc Max Clicks, cũng không cần. Nếu đã ở tCPA, cùng sự kiện đó sẽ vừa nhiễm dữ liệu huấn luyện, vừa buộc thêm 1 thủ tục 9 bước (`monitoring` §2.1), vừa cấm phán xét hiệu suất 1–2 conversion cycle.
2. **Ngân sách ngày chặn thiệt hại về TIỀN, không chặn thiệt hại về TIẾP CẬN.** Chi tiêu tuần 2 vẫn đúng 7,00tr, không có alert "vượt trần" nào nổ — nhưng impression tới khách thật giảm 63%. Triệu chứng duy nhất nhìn thấy là **CTR tăng** và **conversion phẳng**, tức là hai cột mà bản năng đọc ngược: CTR cao trông như tin tốt. Ngưỡng cảnh báo đúng cho `monitoring` §2 là **"CTR ↑ >2× mà conversion phẳng"**, hiện chưa có trong bảng guard.
3. **Ở 30tr với CPC 35k, số ad group nuôi được là 3 — không phải 6.** `campaign-setup` §2.3 tính ra 3 dự án cho #1 vì dùng cap 20k; thay bằng CPC thật của căn hộ TP.HCM thì cả `Brand_CDT`, `TaiChinh`, `NhaOXaHoi` đều tụt dưới ngưỡng ≥10 conv/ad group. **Luật cấu trúc phải neo vào CPC thật của phân khúc, không vào bid cap kế hoạch** — nếu không, ngân sách bị xé thành 5 mảnh không mảnh nào đủ dữ liệu để mở bất kỳ gate nào.
