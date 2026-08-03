# Round 9 — Đất nền Long An 30tr

**Kịch bản:** đất nền Long An · 30tr₫/tháng (1.000.000₫/ngày, trần tháng 30,4tr theo `campaign-setup` §2.1) · CPC kịch bản **18.000₫** (mức "rẻ", giữa 15k *tốt* và 25k *trung bình* của `research` §2) · **trần qualify rate 25%** cho phân khúc dù form chuẩn (`research` §2: "đất nền — CPC thấp, lead rác nhiều nhất").

**Dự án phân phối (thật, từ `keywords/projects.tsv`):** `phúc an city` (Trần Anh Group, Đức Hòa) · `la home` (Prodezi, Bến Lức). Sản phẩm: nền đất phân lô + nhà phố xây thô.

**CPL qualified mục tiêu = 1.560.000₫** — lấy từ mô hình "trung bình" `research` §2, **là placeholder**: breakeven thật cần phí môi giới/nền + tỷ lệ booking→HĐMB (`journey-plan` §4, §6 — user chưa cấp). Ngưỡng kill 1,5× = **2.340.000₫**.

---

## Setup tuần 0 (quyết định + căn cứ doc)

### 1. Pre-flight — G0 (`journey-plan` §3.1)

| Việc | Quyết định | Căn cứ |
|---|---|---|
| Advertiser verification | Nộp D-7, loại Tổ chức, tên pháp nhân khớp hồ sơ thanh toán | `campaign-setup` §1.1 |
| Hồ sơ thanh toán | Doanh nghiệp · VND · GMT+07 (không đổi được về sau) | §1.1.5 |
| 6 conversion action | `Lead_Form_Raw`/`Click_Hotline`/`Click_Zalo` (=1, Primary ngày 1) · `Lead_Contactable`(10)/`Lead_Qualified`(50)/`Dat_Coc`(500) tạo rỗng. Count=**Một**, cửa sổ click **90 ngày**, goal **category** chuẩn Google | §1.2, `tracking/README` luật #2, #4 |
| `phone_click`/`zalo_click` | **Secondary vĩnh viễn** | `tracking/README` luật #2 |
| Negative account-level | 386 dòng `cap_do=account`, dạng `"phrase"`, dán ngày 1 | §1.4.1 — **tránh phạt 25% cháy ngân sách tuần 1-2** |
| Negative campaign-level | shared list `NEG_BDS_Campaign_v1` 80 dòng gắn #1–#3 | §1.4.3 |
| 11 ô cài đặt | Search Partners **TẮT** · Display **TẮT** · Vị trí **Việt Nam**, tuỳ chọn **Sự hiện diện** · Ngôn ngữ VI+EN · **ACA TẮT** · lịch 05:00–24:00 · Standard delivery · tracking template UTM · **không** shared budget · **auto-apply TẮT HẾT** | §1.5.1–1.5.11 |
| Audience GA4 | 5 audience gắn **Observation** trên cả 3 campaign (miễn phí, rủi ro 0) | `research` §3 |
| Test G0 | 1 lead thật → GA4 Realtime + Ads 24h + Keap có `gclid` | §1.3.6 |

### 2. Cấu trúc campaign — 1.000.000₫/ngày

| # | Campaign | ₫/ngày | Bid cap | Ad group | KW |
|---|---|---|---|---|---|
| 1 | `BDS_Search_Brand_DuAn` | **475.000** | 18.000 | `brand-phuc-an-city`, `brand-la-home` | 16 |
| 2 | `BDS_Search_Brand_CDT` | **75.000** | 20.000 | `brand-cdt--tran-anh-group` | 4 |
| 3 | `BDS_Search_KhuVuc_GiaoDich` | **450.000** | 25.000 | **AG-A** `LongAn--dat-nen-gia-bang-gia` (gộp `*--gia-bang-gia` + `*--generic-dat-nen/nha-pho`, 3 khu vực) · **AG-B** `LongAn--dat-nen-mua-ban` | 18 + 6 |
| 4 | `TaiChinh` | **0** | — | KW `*--tai-chinh` toàn bộ `uu_tien=2` → không có trong bộ launch; thêm nữa "đất nền trả góp" là mồi hút khách dưới ngân sách → **cố ý không chạy** | — |
| 8 | `NhaOXaHoi` | **0** | — | Không phân phối NOXH → **dồn vào #3** | — |
| 7 | `Discovery` (broad) | **0 — hoãn** | — | Bắt buộc tCPA, ngày 1 chưa có conversion | — |
| — | `RMKT` | **0 — hoãn** | — | Chưa qua **G2** | — |
| | **Tổng** | **1.000.000** | | **5 ad group** | **44** |

- **Phân bổ:** §3 cho 30tr = 45% Quyết định (#1,#2) + 40% So sánh (#3,#4,#8) + 5% Discovery + 10% RMKT. `campaign-setup` §2.1 đã mượn 15% hoãn vào #1 (+100k) và #3 (+50k) → 475/75/350/70/30. Sau đó **70k (#4) + 30k (#8) dồn vào #3 = 450k**, đúng tiền lệ §2.1 ("#8 không phân phối thì dồn vào #3"). Bottom funnel = **100%** (Q4 yêu cầu ≥80%).
- **Bidding: Maximize Clicks + bid cap** cho cả 3 campaign. Không tCPA, không Max Conversions, không broad — bậc **0** của `journey-plan` §3.2 (0 conversion thì mọi thứ "AI" học từ hư không).
- **Bộ keyword:** lọc `uu_tien=1` + regex 2 dự án + 3 khu vực → 51 kw, **bỏ 7 kw căn hộ/chung cư** (`*--generic-can-ho`, `*--generic-chung-cu`, `*--mo-ban-moi`, `*--du-an-khu-vuc` đều là truy vấn *căn hộ*, `trần anh group căn hộ`) vì không có LP block tương ứng → gửi khách căn hộ vào LP đất nền là đứt message match (QA Q2). **Còn 44 kw, 0 broad** (kiểm §2.4.6 — broad là mặc định, sai cột là thành broad im lặng).
- **AG-A gom toàn bộ nhánh rủi ro vào MỘT ad group** (bảng giá + head term generic) — chủ đích, để kill rule sau này pause được bằng 1 thao tác mà không đụng nhánh sản xuất (AG-B).

### 3. Ba đòn bẩy tự lọc — làm từ tuần 0, không phải sau khi cháy tiền

`research` §2 đã nói trước: đất nền = lead rác nhiều nhất. Không chờ data mới phòng.

**(a) RSA neo giá tối thiểu (anchoring tự lọc — `landing-page/README` yếu tố 2 #2).** Bộ 2 sửa từ `Căn Hộ {Quận} Giá Từ …` sang đất nền, headline #1 = **`Đất Nền Long An Từ 1,5 Tỷ`** (25 ký tự). Không dùng "Giá Tốt"/"Giá Rẻ". Bỏ headline `Đất Nền Long An Trả Góp` khỏi bộ — mâu thuẫn với chiến lược neo 1,5 tỷ. Cả 2 bộ (15 headline + 4 description) đã chạy script §3.5: **0 lỗi**, không ALL-CAPS, không cam kết sinh lời.
- ⚠️ Ô kiểm cứng: headline `Giá Gốc CĐT - Không Chênh` **chỉ dùng khi LP có dòng nói rõ mình là đơn vị phân phối, không phải CĐT** (`research` §7 — mạo nhận = đình chỉ tài khoản ngay). `Từ 1,5 Tỷ` phải là nền thật đang bán, có bảng giá đợt hiện tại làm bằng chứng (nhánh minh bạch chi phí).

**(b) Dropdown ngân sách — sửa THANG, không chỉ sao chép doc.** `research` §5 cho thang `<2 / 2-4 / 4-7 / >7 tỷ` — thang đó thiết kế cho **căn hộ HCM**. Đất nền Long An gần như 100% lead sẽ chọn `<2 tỷ` → **dropdown qualifying không qualify được gì**. Thang dùng cho round này:
- Ngân sách: `1,5–2 tỷ` · `2–3 tỷ` · `trên 3 tỷ` — **không có ô dưới 1,5 tỷ** (khách dưới ngưỡng tự rơi ra ở form, đúng nguyên tắc tự lọc bằng khoảng giá).
- Mục đích: `xây nhà ở ngay` · `giữ đất đầu tư dài hạn` · `mua đi bán lại` ← ô cuối để **cò/flipper tự khai**; bỏ `cho thuê` (vô nghĩa với đất nền, và `cho thuê` là negative account-level).
- Vẫn đúng luật "4 field + 2 dropdown, không hơn" (`landing-page/README` yếu tố 3).

**(c) 12 negative riêng đất nền, dán ngày 1.** Bộ 386 dòng đã chặn tốt nhánh tra cứu nhà nước (`bảng giá đất nhà nước`, `khung giá đất`, `giá đất nhà nước`, `tra cứu quy hoạch`, `bản đồ quy hoạch`, `guland`, `làm sổ đỏ`, `đất nông nghiệp`, `tách thửa`) nhưng **thiếu** nhóm dưới. Đề xuất bổ sung (đưa vào `keywords/negative-keywords.csv` qua `keywords/UPDATE.md` — round này không sửa file ngoài phạm vi):

`giá đất long an` · `giá đất bến lức` · `giá đất đức hòa` · `cò đất` · `sang tay` · `sổ chung` · `vi bằng` · `đất ruộng` · `đất vườn` · `kho xưởng` · `đất công nghiệp` · `đất nền giá rẻ`
— **kèm đủ 12 biến thể không dấu** (`gia dat long an`, `co dat`, `so chung`, `vi bang`, `dat ruong`, `dat vuon`, `kho xuong`, `dat cong nghiep`, `dat nen gia re`…) vì **negative không khớp close variant** (`research` §3 hộp cảnh báo).
- Kiểm xung đột (bài học `cho thuê` trong `adgroup-map` §Cảnh báo): 0/44 keyword launch chứa cụm `giá đất long an` hay `đất nền giá rẻ` → không keyword nào bị khoá chết.

### 4. LP spec (user tự làm theo `tracking/lp-requirements.md`) — CVR dự phóng

| Thành phần | Có | Điểm CVR |
|---|---|---|
| Nền 2,0% | — | 2,0 |
| Message match ≥4/5 nhóm ad chính (H1 = `Đất Nền Long An Từ 1,5 Tỷ` / `Phúc An City Bảng Giá Nền`, anchor riêng từng ad group) | ✔ | +1,0 |
| Bảng giá + khoảng giá above the fold (390px) | ✔ | +0,8 |
| Zalo sticky + `tel:` click-to-call | ✔ | +0,6 |
| Form 4 field + 2 dropdown qualifying (thang (b) ở trên) | ✔ | +0,4 |
| **CVR LP dùng cho mô phỏng** | | **4,8%** (trần 6,0; trong dải đích 3-6% `research` §6) |

LP riêng cho từng đích, **không ad group nào trỏ homepage** (nếu trỏ homepage: ×0,4 → CVR 1,9% = LP hỏng).
Block bắt buộc riêng đất nền: **sơ đồ phân lô từng block** (thay "mặt bằng căn hộ") · sổ hồng riêng từng nền · hạ tầng ảnh thật có ngày · footer pháp nhân + MST.
Contact rate dự phóng **55%** = có dropdown + validate đầu số VN + SLA gọi <5' (hotline trực 05:00–21:00, log tay ra sheet ở tháng 1 vì thoả thuận tag Keap chưa có — `PLAN` §6.6).

---

## Nhật ký tuần 1-4

Công thức: click = chi tiêu ÷ 18.000 (click rác chưa lọc = 0 nhờ negative dán ngày 1) · lead raw = click × 4,8% · qualified = raw × qualify rate nhánh · contact rate 55%.

| Tuần | Chi tiêu | Click | Lead raw | Lead qualified | **Contact rate** | CPL-q | Sự kiện | Hành động + căn cứ |
|---|---|---|---|---|---|---|---|---|
| **T1** | 7.000.000 | 389 | 18,7 | 3,2 (17,2%) | **55%** (10,3 contactable) | 2.180.000 | Ad đã phê duyệt; click đầu về trong 12h; lead test có `gclid` | **Không đổi gì** (`campaign-setup` §4.1 T1: không đụng bid cap/ngân sách/RSA/keyword). D+3: thêm negative cho term sai ngành rõ rệt. Đọc 10 lead gần nhất |
| **T2** | 7.000.000 | 389 | 18,7 | 3,2 (17,2%) | **55%** | 2.180.000 | 🚨 **CPL-q vượt trần kill rule 3 ngày liên tiếp** | Xem khối "Xử lý sự kiện" dưới bảng. Cuối T2 (D+14): pause 6 kw trong AG-A · +12 negative · #3 450k→**360k** (−20%) · #1 475k→**565k** (+19%) |
| **T3** | 7.000.000 | 389 | 18,7 | 3,8 (20,5%) | **55%** | 1.826.000 | AG-A hồi từ 7,50tr → 3,13tr CPL-q | **Không đổi ngân sách lần 2** (`research` §4: ±20%/lần cách ≥3-4 ngày, chờ 4 tuần mới phán xét). T3: báo cáo theo giờ/thiết bị + kiểm cột `Lượt nhấp không hợp lệ` (ngưỡng bình thường <10%, `research` §5 — công thức không sinh số này nên chỉ ghi việc kiểm, không ghi số) · thêm RSA thứ 2 vào AG-B, đổi **một** biến (góc offer) |
| **T4** | 7.000.000 | 389 | 18,7 | 3,8 (20,5%) | **55%** | 1.826.000 | #1 đạt 38,8 conv raw/30 ngày + contact rate 55% → **đủ điều kiện số của `campaign-setup` §4.4** | **KHÔNG chuyển Maximize Conversions.** Xem "Quyết định gate cuối kỳ". Đo CVR LP thật (4,8% > 2% → LP không phải vấn đề, **không đụng bid vì lý do LP**) · điền scorecard `journey-plan` §4 |

**Phân rã theo nhánh (4 tuần):**

| Nhánh | Chi tiêu | Click | Lead raw | Qualified | Qualify rate | CPL-q | so mục tiêu 1,56tr |
|---|---|---|---|---|---|---|---|
| #1 `Brand_DuAn` | 14.560.000 | 809 | 38,8 | 9,7 | 25% (= trần phân khúc) | **1.500.000** | **0,96×** ✅ |
| #2 `Brand_CDT` | 2.100.000 | 117 | 5,6 | 1,1 | 20% | 1.875.000 | 1,20× ⚠️ |
| #3 **AG-A** bảng giá/head term | 6.363.000 | 354 | 17,0 | 1,3 | 5% → 12% | **5.003.000** | **3,21×** ❌ |
| #3 **AG-B** mua-ban | 4.977.000 | 276 | 13,3 | 2,0 | 15% | 2.500.000 | 1,60× ⚠️ |

> Qualify rate theo nhánh là **giả định phân bổ nội bộ**, ràng buộc: blended luôn ≤ **trần 25%** của kịch bản, và nhánh brand là nhánh duy nhất chạm trần. Không phải benchmark, không trích được về doc nào — đánh dấu rõ để không ai tái sử dụng như số thật.

### Xử lý sự kiện T2-T3 — kill rule đúng `journey-plan` §3.1

**Bước 1 — không hành động theo 3 điểm dữ liệu ngày.** Cả tài khoản ra 3,2 lead qualified/tuần; một nhánh ra <1 qualified/tuần → **CPL-q theo NGÀY của một nhánh chỉ có hai giá trị: 0 hoặc vô cực**. "Vượt trần 3 ngày liên tiếp" ở mức volume này là nhiễu, không phải tín hiệu. Đổi sang luật đo được của cùng §3.1: *"Keyword/ad group mới: pause khi chi 2–3× CPL mục tiêu mà 0 conversion"* — đo bằng **chi tiêu luỹ kế**, không đo bằng số ngày.

**Bước 2 — chẩn đoán theo đúng thứ tự ưu tiên, không nhảy vào bid.**

| Kiểm | Số | Kết luận |
|---|---|---|
| Contact rate (`campaign-setup` §4.2: <40% = sửa form/LP TRƯỚC khi sửa Ads) | **55%** | ✅ Form, validate đầu số, SLA gọi đều ổn → **không phải setup lead** |
| CVR LP (`research` §6: <2% = LP hỏng) | **4,8%** | ✅ Trong dải đích 3-6% → **không phải LP** |
| Tracking (`gclid` vào CRM, 6 event) | đủ | ✅ → **không phải đo lường** |
| Invalid clicks | trong ngưỡng <10% | ✅ → **không phải click tặc**. Kể cả nếu vượt: `research` §5 nói ngân sách <30tr thì sửa LP/form có ROI cao hơn chống click tặc, và click tặc **không giải thích được** chênh qualify 5% vs 25% giữa hai nhánh dùng chung một LP |
| Search terms AG-A | phần lớn là **truy vấn đúng intent** (`đất nền long an giá bao nhiêu`, `giá đất nền bến lức`) do **người không mua** gõ | ❌ **Đây là vấn đề** |
| Qualify rate AG-A vs #1 | 5% vs 25% (cùng LP, cùng form, cùng SLA) | ❌ Chênh 5× trong khi mọi biến khác giống nhau → **biến duy nhất còn lại là NGƯỜI GÕ TRUY VẤN** |

→ **Chẩn đoán: vấn đề là PHÂN KHÚC, không phải setup.** Bằng chứng cứng nhất là cặp *contact rate 55% + qualify rate 5%*: gọi được nhưng không phải người mua. Đó là chân dung cò dò giá, đúng như `research` §2 mô tả. Hệ quả quan trọng: **negative list không cứu được**, vì `đất nền long an giá bao nhiêu` là truy vấn đúng ngành, đúng khu vực, đúng loại hình — không có từ nào để phủ định. 12 negative dán ngày 1 chỉ cắt được phần rìa (tra cứu giá đất nhà nước, đất ruộng, kho xưởng).

**Bước 3 — hành động, theo đúng §3.1 (pause nhánh tệ, KHÔNG pause cả campaign).**

| # | Hành động | Căn cứ |
|---|---|---|
| 1 | **Pause 6 keyword trong AG-A**: 3 head term trần (`đất nền long an/bến lức/đức hòa`) + 3 `… giá bao nhiêu`. **Giữ** `… bảng giá` (khách xin đúng bảng giá = intent cao hơn, và là neo message match của `adgroup-map`) | §3.1 keyword-level: AG-A luỹ kế **4.095.000₫ = 2,6× CPL mục tiêu** với ~0 qualified → trong cửa sổ 2–3× |
| 2 | **KHÔNG pause cả AG-A, KHÔNG pause campaign #3** | §3.1: *"không pause producer khi chưa có bản thay thế"*. AG-B là producer (2,0 qualified/tháng); #3 là nhánh volume duy nhất ngoài brand |
| 3 | **#3: 450k → 360k/ngày (−20%)**, **#1: 475k → 565k/ngày (+19%)**. Tổng giữ nguyên 1.000k → không sốc pacing tài khoản | `research` §4 ngân sách ±20%/lần. #1 là nhánh **duy nhất** dưới mục tiêu (0,96×) → tiền chảy về nơi có bằng chứng |
| 4 | ⚠️ **Điều kiện tiên quyết của #3:** đọc `Tỷ lệ hiển thị bị mất (ngân sách)` của #1 trước khi chuyển. Nếu <10% thì brand đã ăn hết volume có sẵn (chỉ 16 keyword, 2 dự án) → **không dồn thêm, hạ tổng xuống 910k/ngày và giữ tiền lại**. Mua thêm click brand không tồn tại chỉ đẩy CPC lên | `campaign-setup` §2.2: "tiêu hết ngân sách mà cap chưa chạm thì đó là vấn đề ngân sách", suy ngược lại cũng đúng |
| 5 | +12 negative nhóm đất nền (mục Setup 3c) qua nghi thức search terms 3 lượt | `journey-plan` §5 tuần #1 |

**Bước 4 — 5 việc CỐ Ý KHÔNG làm (và vì sao).**

| Không làm | Vì sao |
|---|---|
| Tăng ngân sách để "bù" lead qualified | Ở trần qualify 25%, thêm tiền chỉ mua thêm cò theo đúng tỷ lệ cũ. CPL-q **không đổi theo ngân sách** |
| Đổi bid cap / bid strategy để "chữa" CPL-q | CPL-q vỡ vì **qualify rate**, không vì CPC (18k đã là mức rẻ). Đổi bid = reset learning (CVR ×0,7 tuần sau) mà không đụng nguyên nhân |
| Bật tCPA / Maximize Conversions | Bậc 1-2 `journey-plan` §3.2 chưa mở (xem gate cuối kỳ) |
| Bật broad / #7 Discovery | `research` §3: broad cần Smart Bidding — điều kiện của chính Google. Truy vấn mới đã lấy đủ từ search terms của phrase |
| Bật PMax / Demand Gen / remarketing | G2 chưa mở (xem gate), G4 cần ECL chạy thật |

---

## Tổng kết

### Số 4 tuần (28 ngày)

| Chỉ số | Giá trị |
|---|---|
| Chi tiêu | **28.000.000₫** (tháng đủ 30,4 ngày ≈ 30,4tr) |
| Impression (**CTR giả định 7,61%** — WordStream 2026 Real Estate, `research` §2; **không phải số VN**, chỉ để suy impression) | ~20.400 |
| Click / CPC | **1.556** / 18.000₫ |
| CVR LP | **4,8%** (dải đích 3-6% ✅) |
| **Lead raw** | **74,7** — CPL raw 375.000₫ |
| **Lead contactable (contact rate 55%)** | **41,1** ← báo cáo TRƯỚC CPL (`research` §5) |
| **Lead qualified** | **14,1** (qualify rate blended **18,9%**, trần phân khúc 25%) |
| **CPL qualified** | **1.987.000₫** = **1,27×** kịch bản trung bình 1,56tr |
| CPL-q quỹ đạo ra (T3-T4) | **1.826.000₫** |
| Qualified/contactable | 34% |

### Trần kinh tế của phân khúc — con số quan trọng nhất của round này

Ở CPC 18k và trần qualify 25%, CPL-q **không thể thấp hơn**:

| Điều kiện | CPL-q sàn |
|---|---|
| CVR 4,8% (LP hiện tại), qualify 25% | **1.500.000₫** |
| CVR 6,0% (**trần LP**), qualify 25% | **1.200.000₫** |

→ Đất nền Long An ở 30tr/tháng **không có đường xuống dưới ~1,2tr₫/lead qualified**, kể cả LP hoàn hảo và mix hoàn hảo. Nếu breakeven thật (`journey-plan` §4, chờ phí môi giới/nền + tỷ lệ booking→HĐMB) cho CPL mục tiêu dưới 1,2tr thì **kết luận không phải "tối ưu thêm", mà là "sai phân khúc"** — và quyết định đó là của kinh doanh, không phải của Ads.

### Trạng thái gate cuối kỳ

| Gate | Trạng thái | Lý do |
|---|---|---|
| **G0** | ✅ **ĐÃ QUA** | 6 event test, `gclid` vào CRM, LP <3s, 386 negative, Partners+Display OFF, location Presence |
| **G1** (mở rộng T2) | 🔲 **chờ 2 ngày** | #1 CPL-q 1,50tr ≤ mục tiêu 1,56tr — nhưng §3.1 đòi **30 ngày liên tiếp**, mới có 28. Rà lại D+30. Ngưỡng conv/tháng của G1 vẫn là `[điền]` — user phải chốt |
| **G2** (Remarketing) | ❌ **ĐÓNG — đóng bằng số học** | Cần ≥1.000 user `xem_bang_gia`/30 ngày. Cả tháng chỉ có **1.556 click** → cần >64% người vào LP scroll tới bảng giá mới đủ. Ở 30tr/tháng + CPC 18k, **G2 không thể mở** → quỹ 10% remarketing của §3 đúng khi để hoãn từ ngày 1, không phải "làm sau" |
| **G3 / G4 / G5** | ❌ ĐÓNG | G3 cần G2. G4 cần ECL chạy thật. G5 cần ≥150tr/tháng |
| **Bậc AI (§3.2)** | **vẫn bậc 0** (Max Clicks + bid cap) | Xem dưới |

**Quyết định gate quan trọng nhất — #1 đủ điều kiện SỐ nhưng KHÔNG chuyển bidding.**
`campaign-setup` §4.4 (Max Clicks → Maximize Conversions) đòi 3 điều kiện: ≥15 conv/30 ngày (#1 có **38,8** ✅) · contact rate >50% (**55%** ✅) · đã chạy ≥4 tuần (✅). Đủ cả ba. Vẫn **không chuyển**, vì §4.4 buộc làm kèm việc thứ nhất: *"Đảo primary/secondary conversion — nếu không, smart bidding học theo form thô và sẽ mua lead rác"*. ECL chưa chạy (chưa có thoả thuận tag Keap — `PLAN` §6.6) → **không có `Lead_Contactable` để đảo sang**. Chuyển Maximize Conversions lúc này = cho bidding tối ưu `generate_lead` thô, trong khi **81% lead thô của phân khúc này là rác** → đúng cái bẫy optimize-to-quality mà `journey-plan` §2.3 cảnh báo, và ở đất nền nó là nước đi tệ nhất có thể.
→ Đòn bẩy số 1 cho tháng 2 **không phải tiền, là ECL**: xin quyền Keap + chốt quy tắc tag `Lead_Contactable` (SLA 48h, muộn nhất 7 ngày). `journey-plan` §3.2: *"thứ mở khoá AI không phải ngân sách, mà là dữ liệu conversion chất lượng"*.

### Việc tháng 2 (theo thứ tự đòn bẩy, không có món nào là "tăng tiền")

1. **ECL** — quyền Keap + quy tắc tag → mở bậc 1 (`journey-plan` §3.2). Chặn tất cả mọi thứ khác.
2. **Content lọc** — bài SEO trong `content/` (skill `seo-machine`) đúng truy vấn `giá đất nền Long An 2026` để **hút nhánh dò giá về organic**, thay vì trả 18k/click cho nó. Đây là cách duy nhất phục vụ nhóm đó mà không phải mua họ.
3. **Siết dropdown thêm một bậc** — biến ngưỡng 1,5 tỷ thành cổng cứng, đặt bảng giá **sau** cổng. ⚠️ Không claim được con số: công thức mô phỏng chỉ cho +0,4 CVR cho "4 field + 2 dropdown", không mô hình hoá độ chặt của thang → phải **đo bằng A/B test 1 hypothesis/tuần** (`journey-plan` §5 tuần #7), không được ghi trước một mức tăng.
4. **Mở rộng bộ keyword đất nền** — kho `keywords/` lệch nặng về căn hộ (4.556 kw căn hộ vs **330 đất nền**), Long An chỉ có **1 kw đất nền/khu vực** và **0 exact**; `projects.tsv` không có dự án nào phân loại `đất nền` ở Long An; Prodezi (CĐT của La Home) chưa có `brand-cdt--`. → **dispatch agent `keyword-planner`** (`CLAUDE.md`), không tự sửa.
5. **Breakeven thật** — phí môi giới/nền + booking→HĐMB (`journey-plan` §6). Không có 2 số này thì mọi kill rule của round này vẫn đang neo vào placeholder 1,56tr.

### 3 bài học

1. **Cặp `contact rate cao + qualify rate thấp` là chữ ký của lỗi PHÂN KHÚC; cặp `contact rate thấp` là chữ ký của lỗi SETUP.** Đọc đúng cặp này ở tuần 2 là thứ ngăn được cả một tháng đi sửa sai chỗ (đổi bid, làm lại LP, tăng ngân sách). Đó cũng là lý do `research` §5 bắt báo cáo contact rate **trước** CPL — không phải để đẹp báo cáo, mà để chẩn đoán đúng.
2. **Negative list chặn được truy vấn sai, không chặn được NGƯỜI sai.** `đất nền long an giá bao nhiêu` là truy vấn hoàn hảo do người không mua gõ. Với phân khúc lead rác cao, đòn bẩy phải nằm **trước cú click** (RSA neo giá tối thiểu) và **tại form** (thang dropdown đúng phân khúc), không nằm ở danh sách phủ định. Và thang dropdown trong `research` §5 là thang **căn hộ HCM** — sao chép nguyên sang đất nền Long An thì mọi lead đều trả lời `<2 tỷ` và dropdown qualifying không qualify được gì.
3. **Alert theo NGÀY vô dụng ở volume thấp; luật đo được là chi tiêu LUỸ KẾ.** Một nhánh ra <1 lead qualified/tuần thì CPL-q ngày chỉ có 0 hoặc vô cực. `journey-plan` §3.1 có sẵn hai luật cho hai tình huống — luật "2-3× CPL mục tiêu mà 0 conversion" (đo bằng tiền) dùng cho nhánh volume thấp, luật "CPL 1,5-2× trên mục tiêu" (đo bằng tỷ lệ) dùng cho nhánh đã có conversion. Chọn sai luật thì hoặc pause quá sớm, hoặc đốt tiền chờ mãi.
