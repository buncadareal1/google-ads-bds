# Round 4 — Policy 30tr (biệt thự nghỉ dưỡng Phan Thiết)

Kịch bản: 30tr₫/tháng · CPC 35k₫ · phân khúc **biệt thự nghỉ dưỡng Phan Thiết**.
Ràng buộc phân khúc (`research` §2): *"biệt thự/hạng sang — volume rất thấp, **KHÔNG dùng tCPA**"* → tCPA bị **cấm vĩnh viễn** ở round này, kể cả nếu đạt 30 conv/30 ngày. Trần lộ trình bidding = **bậc 1 (Maximize Conversions)**, và chỉ sau khi ECL chạy.
Ngày mốc: tuần 0 = 28/7–3/8 · launch 06:00 **4/8** · T1 4–10/8 · T2 11–17/8 · T3 18–24/8 · T4 25–31/8.

## Setup tuần 0 (quyết định + căn cứ doc)

**1. Pre-flight — advertiser verification làm ĐẦU TIÊN** (`campaign-setup` §1.1): nộp ngày 28/7, không chờ Google hỏi. Lý do đúng (§1.1, `research` §7): *"all advertisers will eventually be required"*, và khi đã có yêu cầu thì **30 ngày không nộp = tạm ngưng cả tài khoản**. Kiểm trước hồ sơ thanh toán = **Doanh nghiệp**, VND, GMT+07 (§1.1.5 — không đổi được về sau) và **tên pháp nhân khớp 100%** ĐKKD (§1.1.2). *Quyết định này là lý do sự kiện tuần 2 không giết được tài khoản.*

**2. Cấu trúc — 2 campaign, không 5** (`research` §1 "<20tr–30tr: 1 khối Search, không chia 5-10 campaign nhỏ"; `adgroup-map` "gộp là mặc định, tách là ngoại lệ"):

| Campaign | ₫/ngày | % | Bid cap | Ad group |
|---|---|---|---|---|
| #1 `BDS_Search_Brand_DuAn` | **521.000** | 52,9% | 30.000₫ | `brand-novaworld-phan-thiet`, `brand-costamigo-phan-thiet` |
| #3 `BDS_Search_KhuVuc_GiaoDich` | **464.000** | 47,1% | 40.000₫ | 1 ad group **gộp** `phan-thiet + mui-ne — biệt thự biển` |
| **Tổng** | **985.000** | 100% | | 3 ad group |

985.000 × 30,4 = **29,94tr** (§2.1: trần tháng = ngày × 30,4; phải nhân 0,985 mới ra đúng 30tr).

Bốn campaign của §2.1 **KHÔNG bật**, mỗi cái một lý do đo được:
- #2 `Brand_CDT` (75k/ngày): 65 click/tháng → 3,1 conv → **dưới ngưỡng ≥10 conv/ad group** (`adgroup-map`). Thêm: truy vấn `brand-cdt--novaland` ở phân khúc này kéo về tin tức tái cấu trúc CĐT, không phải intent mua.
- #4 `TaiChinh`: **không có ad group nào tồn tại** cho khu vực này (`phan-thiet--tai-chinh` không có trong master list) và khách 20-40 tỷ không đi bằng trục trả góp. Không dựng campaign rỗng.
- #8 `NhaOXaHoi`: §2.1 ghi rõ "chỉ bật nếu **thực sự** phân phối NOXH" → không.
- #7 `Discovery` (broad): `adgroup-map` #7 **bắt buộc tCPA** — phân khúc này cấm tCPA → **hoãn vô thời hạn**, không phải "hoãn tới tuần 4". Truy vấn mới lấy từ search terms của phrase match.
- `RMKT_Display`/Demand Gen: **G2 bất khả thi bằng toán học** — xem §Gate cuối kỳ.
15% quỹ Remarketing + Discovery + 18% của #2/#4/#8 được chia lại cho #1/#3 **giữ đúng tỷ lệ 45:40** của `journey-plan` §3 (45/85 và 40/85). Bottom funnel = **100%** (Q4 yêu cầu ≥80%).

**3. Bộ keyword launch = 22 dòng**, `uu_tien=1`, **0 broad** (§2.4.6 — broad là default của Google, phải lọc cột `Loại đối sánh` = rỗng sau import):
- 16 kw brand (8 exact + 8 phrase) của 2 dự án thật đang phân phối.
- 6 kw `biệt thự biển phan thiết|mũi né` (+ giá/bảng giá).
- **Loại bỏ có chủ đích** 20 kw `căn hộ`/`condotel` Phan Thiết trong cùng `nhom_adgroup` — không phân phối sản phẩm đó. Kèm negative campaign-level `"căn hộ"`, `"can ho"`, `"chung cư"`, `"chung cu"`, `"condotel"` để không trả tiền cho sai sản phẩm.
- Mũi Né gộp vào ad group Phan Thiết: Mũi Né **thuộc** Phan Thiết, và `adgroup-map` §cụm biển đã xếp chung. Gộp vì volume thấp, không tách.
- ⚠️ 22 kw là rất mỏng → rủi ro thật là **không tiêu hết ngân sách**, không phải cháy tiền. Nếu IS lost (rank) cao mà budget còn → hành động là **mở `uu_tien=2` (+20 kw brand modifier)**, KHÔNG tăng bid cap (§2.2: "tiêu hết ngân sách mà cap chưa chạm → không tăng cap").

**4. Negative ngày 1** (`campaign-setup` §1.4): 386 dòng `cap_do=account` dán vào **Từ khoá phủ định cấp tài khoản** (tự áp mọi campaign type) + shared list 80 dòng campaign-level gắn cho #1, #3. Phân khúc nghỉ dưỡng ăn may: list đã có `du lịch`, `tour`, `khách sạn`, `đặt phòng`, `booking`, `resort giá`, `homestay`, `giá phòng`, `theo ngày` — rò rỉ lớn nhất của resort là **intent du lịch**, đã bị bịt trước.
⚠️ Xung đột phải biết trước (`adgroup-map` §Cảnh báo): `cho thuê` là negative **account-level**. Sản phẩm này bán bằng câu chuyện khai thác cho thuê → **không** được viết keyword chứa "cho thuê" (sẽ eligible nhưng không bao giờ served). Dùng "khai thác dòng tiền". Trên **form** thì dùng chữ "cho thuê" thoải mái — đó không phải keyword.

**5. Conversion ladder** — tạo cả 6 action trước khi có campaign (§1.2), `Số lượng`=Một, **cửa sổ nhấp 90 ngày** (§1.2.4 — chu kỳ BĐS nghỉ dưỡng dài hơn cả căn hộ), goal **category** chuẩn Google (§1.2.7, không chỉ đặt tên). Ngày 1: `Lead_Form_Raw`/`Click_Hotline`/`Click_Zalo` = Primary chỉ để thấy số; `Lead_Contactable`(10)/`Lead_Qualified`(50)/`Dat_Coc`(500) = Secondary rỗng chờ ECL.
🚩 **Cảnh báo đọc số**: 3 action web đều Primary ngày 1 → cột `Conversions` gộp cả `phone_click`/`zalo_click`. Mọi ngưỡng gate (≥15/≥30 conv) phải đo trên **`Lead_Form_Raw` riêng**, nếu không sẽ qua gate bằng click nút. Cột đọc = `Conversions`, không phải `All conversions` (`monitoring` §1).

**6. 11 ô §1.5**: Search Partners OFF · Display expansion OFF · VN + `Presence` · VI+EN · **ACA/Dynamic ad text OFF** (rà lại hàng tháng — 9/2026 Google auto-upgrade ACA thành AI Max) · lịch 05:00–24:00 · Standard · tracking template UTM · không shared budget · **auto-apply recommendations TẮT HẾT** (§1.5.11 — `Remove conflicting negative keywords` sẽ phá đúng cái list vừa dán).

**7. LP spec chọn gì** (`landing-page/README.md`) — 4 đòn bẩy CVR bật hết từ ngày 1:

| Đòn bẩy | Trạng thái | +CVR |
|---|---|---|
| Message match keyword→H1 (`brand-<slug>` mod *bảng giá* → H1 "{Dự án} Bảng Giá Mới Nhất" + anchor `#bang-gia`; luồng khu vực → "Biệt Thự Biển Phan Thiết Giá Từ … ₫") — tự chấm **4/5** | ✔ | +1,0 |
| Khoảng giá above the fold ("từ X tỷ/căn") | ✔ | +0,8 |
| Zalo sticky + `tel:` click-to-call | ✔ | +0,6 |
| Form 4 field + 2 dropdown qualifying | ✔ | +0,4 |
| **CVR LP = 2,0 + 2,8 = 4,8%** (trần 6,0 — 4 đòn bẩy chỉ cộng tối đa 2,8 nên **4,8% là mức tối ưu đạt được**, không phải mức trung bình) | | **4,8%** |

Hard gate `landing-page/README.md`: footer pháp nhân/MST/địa chỉ/hotline + **1 dòng "đơn vị phân phối, không phải chủ đầu tư"** — bắt buộc vì bộ RSA §3.1 có headline `Giá Gốc CĐT`, và mạo nhận CĐT = **đình chỉ tài khoản NGAY, không cảnh báo** (`research` §7).
Không gửi về homepage (×0,4 toàn bộ CVR). Mỗi ad group một anchor riêng (§2.4.7).

**8. Điều kiện G0 phải chốt trước khi bật ads** (`journey-plan` §3.1): 1 lead thật đi tới Keap có `gclid` · LP <3s mobile · negative đã apply · Partners/Display OFF · Presence. **Thêm 1 ô do phân khúc**: `research` §5 quy contact rate 55% cho "dropdown + validate đầu số + **SLA gọi <5'**" → SLA <5' phải có **văn bản thoả thuận với sale** trước launch, không thì contact rate rơi về 35%. Ở 8-9 lead/tuần thì SLA <5' là khả thi về nhân sự. ⚠️ `PLAN` §6.6 đang PENDING (chưa có quyền xem quy trình sale) → đây là **rủi ro số 1 của cả round**, không phải chi tiết.

## Nhật ký tuần 1-4

Công thức: click = 6.895.000 ÷ 35.000 = **197** (negative import ngày 1 → 0% click rác chưa lọc, không bị phạt 25%) · lead raw = 197 × 4,8% · lead q = × 40% (2 dropdown) · contact rate 55% (dropdown + validate đầu số + SLA <5').

| Tuần | Chi tiêu | Click | Lead raw | Lead q | Contact rate | CPL-q | Sự kiện | Hành động + căn cứ |
|---|---|---|---|---|---|---|---|---|
| **1**<br>4–10/8 | 6.895.000₫ | 197 | 9,5 | 3,8 | **55%** (5,2 gọi được) | 1.823.000₫ | 🔴 **RSA disapproved — "Unreliable claims"**: headline `Cam Kết Sinh Lời 30%/Năm` do sale gửi copy, nằm ở RSA #2 ad group `brand-novaworld-phan-thiet` | **Không mất click**: §2.5-b7 quy định **2 RSA/ad group** ngày 1 → RSA #1 (bộ §3.1 đã verify policy) vẫn served. Xử lý 6 bước — xem §Sự kiện T1 dưới bảng. Tuần 1 **không đổi** bid cap/ngân sách/keyword (§4.1) — chỉ sửa ad + thêm negative. **D+3**: vòng negative lần 1, chỉ term rõ sai ngành: +14 negative resort (`vé`, `giá vé`, `combo`, `voucher`, `công viên nước`, `2 ngày 1 đêm`, `chơi gì`, `check in` + **8 biến thể không dấu** — negative KHÔNG khớp close variant, `research` §3) |
| **2**<br>11–17/8 | 6.895.000₫ | 197 | 9,5 | 3,8 | 55% (5,2) | 1.823.000₫ | 🔴 **Yêu cầu advertiser verification**, deadline 30 ngày (D+30 = **10/9**), không nộp = **tạm ngưng toàn tài khoản** | Đã nộp từ 28/7 (§1.1) → đây là yêu cầu bổ sung, **không phải khởi đầu từ 0**. Xử lý theo `monitoring` §2 dòng 🔴 verification: nộp trong **≤48h**, không chờ ngày 29 — xem §Sự kiện T2 dưới bảng. **Đóng băng mọi thay đổi ngân sách/cấu trúc** đến khi có kết quả duyệt (đổi trong lúc chờ = không biết biến động do đâu). T2 checklist: vòng negative **nghi thức 3 lượt** (`journey-plan` §5) + đọc **10 lead gần nhất**, contact rate lần 1 (`research` §8) |
| **3**<br>18–24/8 | 6.895.000₫ | 197 | 9,5 | 3,8 | 55% (5,2) | 1.823.000₫ | Verification **đã duyệt** (nộp 12/8, duyệt 3-5 ngày) | Báo cáo **theo giờ + thiết bị** (§4.1): **không siết lịch quảng cáo** — ở 28 click/ngày, cắt khung giờ đẩy ad group xuống dưới ngưỡng ≥10 conv, thiệt hơn lợi. Kiểm `Lượt nhấp không hợp lệ` <10% (`research` §5). **Không thêm RSA #3**: 197 click/tuần chia 3 ad group thì RSA thứ 3 không bao giờ đủ mẫu. Hypothesis tuần thay bằng việc có đòn bẩy thật — xem §Phát hiện T3 |
| **4**<br>25–31/8 | 6.895.000₫ | 197 | 9,5 | 3,8 | 55% (5,2) | 1.823.000₫ | — | CVR LP thật = **4,8%**, trong dải đích 3-6% (`research` §6) → **không đụng LP, không đụng bid**. Quyết định bidding (§4.4): **GIỮ Max Clicks** — 2 lý do độc lập, xem §Quyết định T4. Rà gate `journey-plan` §3.1 → **không mở gate nào**. Điền scorecard tháng 1 (`journey-plan` §4). **Không đổi ngân sách** (không có bằng chứng cần đổi; đổi >±20% = reset learning) |

### Sự kiện T1 — RSA disapproved "Unreliable claims" (6 bước, thứ tự ưu tiên)

1. **Khoanh phạm vi trước khi sửa**: đây là **ad-level disapproval**, chưa phải account-level. Mở `Policy Manager` xem có cờ cấp tài khoản không. Xác nhận RSA #1 cùng ad group vẫn `Đã phê duyệt` → traffic không đứt (§4.1 D+0 10:00).
2. **KHÔNG gửi duyệt lại nguyên bản.** Nộp lại ad vi phạm là đường ngắn nhất từ "disapproved" sang cảnh báo tài khoản.
3. **Sửa gốc, không sửa triệu chứng.** Copy của sale không chỉ nằm ở 1 headline — quét toàn bộ điểm nó có thể đã lọt: 3 bộ RSA khác · sitelink/callout (§3.4) · **LP (destination cũng bị review — `research` §7 "cam kết sinh lời X%" là lý do disapproved kinh điển)** · bài `content/` · script Zalo của sale. Danh sách cụm cấm để quét: `cam kết sinh lời`, `cam kết lợi nhuận`, `lợi nhuận X%`, `sinh lời X%`, `bao lãi`, `chắc chắn tăng giá`, `cam kết cho thuê lại`.
4. **Thay bằng headline đã verify**, không tự viết mới lúc đang gấp: lấy từ bộ §3.1 (`Chính Sách Bán Hàng Đợt Mới` 27 ký tự). Sửa xong chạy lại script đếm ký tự §3.5.
5. **Xác minh con số 30%/năm với CĐT.** Nếu hợp đồng cam kết khai thác thật chỉ 8-12%/năm thì "30%" là **số sale bịa** → đó mới là nguyên nhân gốc, và nó là vấn đề policy **lẫn** pháp lý (`research` §7 minh bạch chi phí: mọi số phải là căn thật, có bằng chứng). Nếu cam kết là thật và có hợp đồng: điều khoản đó nằm **trên LP kèm điều kiện + nguồn**, **không bao giờ trong ad text** — ad text không có chỗ cho điều kiện kèm theo, nên mọi con số lợi nhuận trong ad text đều là unreliable claim.
6. **Guard để không tái diễn** (đề xuất cho Fable, round này không sửa file khác): copy do sale gửi **không đi thẳng vào Ads**. Thêm **1 dòng assert cụm cấm** vào script §3.5 đang có sẵn — không dựng công cụ mới:
   `assert not any(p in s.lower() for s in H+D for p in ('cam kết sinh lời','cam kết lợi nhuận','sinh lời','bao lãi'))`
   Ghi 1 dòng vào `ops/audit-log.jsonl`.

### Sự kiện T2 — advertiser verification (thứ tự ưu tiên)

1. **Giờ đầu tiên — kiểm cái không sửa được**: hồ sơ thanh toán là **Doanh nghiệp** hay cá nhân? Tên trên ĐKKD **khớp 100%** tên hồ sơ thanh toán? (§1.1.2, §1.1.5) Đây là điểm chết thật: hồ sơ cá nhân đi xác minh Tổ chức thì hồ sơ bị từ chối và không có đường sửa nhanh.
2. **≤48h**: nộp ĐKKD + MST (§1.1.2) + CCCD người đại diện (§1.1.3). Không xếp lịch "làm trước deadline".
3. **Cùng ngày**: rà LP có đủ footer pháp nhân + MST + địa chỉ + hotline (§1.1.4) — reviewer xem cả trang đích; thiếu là lý do disapproved độc lập.
4. **Giám sát**: đếm ngược D-10 (từ 31/8) alert **mỗi ngày, không cooldown 2h** (`monitoring` §2). Chưa xác nhận GAQL expose trạng thái verification → khởi đầu là **mục kiểm tay thứ 2 hàng tuần** (`Quản trị → Xác minh`), nâng lên tự động sau.
5. **Đóng băng thay đổi** trong lúc chờ duyệt: không tăng/giảm ngân sách, không mở gate. Bị treo giữa lúc scale = mất cả learning lẫn dữ liệu so sánh.
6. **Nếu vẫn bị tạm ngưng**: lead không dừng — LP + Zalo + hotline + `content/` vẫn chạy. **Tuyệt đối không mở tài khoản Ads thứ 2** để lách (đó là circumventing systems → ban vĩnh viễn, nặng hơn tạm ngưng).

### Phát hiện T3 — dropdown qualifying của `research` §5 SAI phân khúc

Dải dropdown Ngân sách trong `research` §5 (`<2 / 2-4 / 4-7 / >7 tỷ`) viết cho **căn hộ**. Biệt thự nghỉ dưỡng Phan Thiết 20-40 tỷ → **100% lead rơi vào ô ">7 tỷ"** → dropdown vẫn tồn tại nhưng **không còn qualify gì**, tức 40% qualify rate là danh nghĩa. Sửa: chia lại `<10 / 10-20 / 20-30 / >30 tỷ`; dropdown Mục đích đổi từ (ở / đầu tư / cho thuê) sang (**nghỉ dưỡng cá nhân / đầu tư khai thác dòng tiền / vừa dùng vừa khai thác**) — đây mới là trục phân loại khách của sản phẩm này.
Không đổi số của round (luật sim cố định qualify rate 40%), nhưng là điều kiện để 40% đó **thật** ở tháng 2. Ghi vào `keywords/UPDATE.md`/`tracking/lp-requirements.md` là việc của Fable.

### Quyết định T4 — vì sao KHÔNG lên smart bidding dù số đã đủ

Điều kiện §4.4 cho Max Clicks → Maximize Conversions: campaign ≥15 conv/30 ngày ✔ (#1 = 21,7 · #3 = 19,3) · contact rate >50% ✔ (55%) · đã chạy ≥4 tuần ✔. **Vẫn không chuyển**, 2 lý do:
1. **`journey-plan` §3.2 bậc 1 buộc đảo primary sang `Lead_Contactable` TRƯỚC khi bật smart bidding.** ECL chưa chạy (`PLAN` §6.6 pending: sale chưa thống nhất tag Keap) → primary vẫn là form thô → bật Maximize Conversions bây giờ = dạy bidding đi mua form rẻ nhất = **optimize-to-quality trap** (`tracking/README` luật #2).
2. **Con số 21,7/19,3 chưa đáng tin**: 3 action web đang cùng Primary nên cột `Conversions` gộp cả `phone_click`/`zalo_click`. Phải tách `Lead_Form_Raw` ra đo lại trước khi coi là qua ngưỡng.
→ Việc thật của tuần 4 **không phải đổi bidding, mà là chốt thoả thuận tag Keap + bật `upload_ecl.py`**. `journey-plan` §3.2: *"thứ mở khoá AI không phải ngân sách, mà là dữ liệu conversion chất lượng"*.
Và ngay cả khi ECL chạy: trần của phân khúc này là **Maximize Conversions**, **không bao giờ tCPA** (`research` §2).

## Tổng kết

| Chỉ số | 4 tuần (28 ngày) |
|---|---|
| Chi tiêu | **27.580.000₫** (985k/ngày × 28) |
| Click | **788** |
| **Contact rate** | **55%** — 20,8 lead gọi được / 37,8 raw *(KPI số 1, báo cáo trước CPL — `research` §5)* |
| Lead raw | **37,8** |
| Lead qualified | **15,1** |
| **CPL qualified** | **1.823.000₫** |
| CPL contactable | 1.326.000₫ |
| CVR LP | 4,8% (dải đích 3-6%) |
| CTR **giả định** | **7,61%** → ~10.400 impression. Đây là WordStream 2026 Real Estate (Mỹ) từ `research` §2 — **giả định lập kế hoạch, KHÔNG phải số đo**; không có benchmark CTR BĐS VN đáng tin (`research` §Khoảng trống 1) |
| Cột đọc | `Conversions`, quy về **ngày CLICK** (`monitoring` §1) — không phải `All conversions` |

**CPL-q 1,82tr vs kịch bản trung bình 1,56tr — đây là điểm tối ưu, không phải kém.** Chứng minh: CPC cố định 35k (mô hình "trung bình" của `research` §2 là 25k). 4 đòn bẩy CVR trong luật sim chỉ cộng được tối đa +2,8 → CVR trần thực tế **4,8%**, không phải 6,0%. Qualify rate trần 40%. Vậy CPL-q sàn = 6.895.000 ÷ (197 × 4,8% × 40%) = **1.823.000₫**. Muốn xuống 1,56tr ở phân khúc này thì phải hạ CPC hoặc nâng qualify rate — cả hai đều nằm ngoài đòn bẩy của round.

**Trạng thái gate cuối kỳ — 0 gate mở, mỗi cái một lý do đo được:**

| Gate | Trạng thái | Lý do |
|---|---|---|
| G0 | ✅ đã qua | lead thật có gclid vào Keap · LP <3s · negative apply · Partners/Display OFF · Presence · **+ SLA gọi <5' có văn bản** |
| G1 | ❌ **không đánh giá được** | Cần "CPL ≤ mục tiêu 30 ngày liên tiếp", nhưng CPL mục tiêu tính từ breakeven (`journey-plan` §4) cần **phí môi giới/căn + tỷ lệ booking→HĐMB** — user chưa cung cấp (§6). Không có số đó thì mọi kill rule là đoán → **không tự đặt số thay user** |
| G2 | ❌ **bất khả thi bằng toán học** | Cần audience `xem_bang_gia`/`engaged_60s` ≥**1.000 user**/30 ngày. Cả tài khoản có **855 click/tháng** → không thể. Ở 30tr₫ + phân khúc này, remarketing **không phải "chưa tới lúc" mà là không tồn tại** → 10% quỹ đó đã chuyển cho #1/#3 vĩnh viễn, đúng, không phải mượn tạm |
| G3 | ❌ | Cần T1+T2 đạt tCPA mục tiêu 2 tháng — mà tCPA bị **cấm** ở phân khúc này → G3 đóng theo cấu trúc |
| G4 (PMax) | ❌ | Cần offline import chạy thật + ≥30 conv/tháng. ECL chưa chạy |
| G5 (YouTube) | ❌ | Cần ≥150tr/tháng |
| Bậc bidding | **Bậc 0** (Max Clicks + cap) | Trần của phân khúc = bậc 1. Điều kiện còn thiếu duy nhất: **ECL** |

**3 bài học**

1. **Quyết định rẻ nhất của cả round được ra ở tuần 0, không phải lúc có sự cố.** Nộp verification ngày 28/7 (§1.1) biến sự kiện tuần 2 từ "khủng hoảng 30 ngày" thành một lần nộp bổ sung; và luật **2 RSA/ad group** (§2.5-b7) làm sự kiện tuần 1 mất **0 click**. Cả hai đều là ô checklist bị coi là thủ tục — chúng chính là bảo hiểm.
2. **Copy do sale gửi là một biên giới tin cậy, phải validate như input người dùng.** "Cam Kết Sinh Lời 30%/Năm" không phải lỗi đánh máy: nó là câu chào hàng mặc định của môi giới nghỉ dưỡng, nên nó sẽ quay lại ở LP, sitelink, script Zalo. Sửa 1 headline là sửa triệu chứng; grep cụm cấm trên toàn bộ asset + 1 assert trong script §3.5 đang có sẵn mới là sửa gốc — và rẻ hơn.
3. **Ràng buộc phân khúc ghi đè cả lộ trình.** "Biệt thự/hạng sang KHÔNG dùng tCPA" (một dòng trong `research` §2) làm sập theo dây: #7 Discovery không bao giờ bật · G3 đóng theo cấu trúc · trần bidding là Maximize Conversions · và 855 click/tháng làm G2 bất khả thi. Ở phân khúc volume rất thấp, gần như mọi thứ "mở rộng" là bẫy — việc duy nhất còn đáng làm là **ECL + chất lượng lead**, không phải thêm campaign.
