# Round 2 — 60tr + cám dỗ PMax

Kịch bản: 60tr₫/tháng · 2 dự án (**Eco Retreat** — Ecopark, Bến Lức Long An · **Legacy Central** — Kim Oanh Group, Thuận An Bình Dương) · CPC kịch bản **28.000₫**.
Mọi số suy từ công thức `test/sim-rules.md` + quyết định dưới đây. Số chưa có dữ liệu ghi `[điền]` (tracking/README luật #5).

## Setup tuần 0 (quyết định + căn cứ doc)

**Ngân sách ngày = 1.970.000₫** (2tr × 0,985 → trần tháng `×30,4` = 59,9tr ≈ đúng 60tr — `campaign-setup` §2.1). Tuần = **13,79tr**.

**1. Cấu trúc — 2 campaign, 4 ad group** (không phải 8 campaign của bản đồ)

| Campaign | ₫/ngày | Ad group | Bid cap | Căn cứ |
|---|---|---|---|---|
| #1 `BDS_Search_Brand_DuAn` | **945.000** | `brand-eco-retreat`, `brand-legacy-central` | 25.000 | journey-plan §3 cột 60tr: T1 brand 35% |
| #3 `BDS_Search_KhuVuc_GiaoDich` | **1.025.000** | `ben-luc--gia-bang-gia` (gộp `--mua-ban`, `--mo-ban-moi`, `--du-an-khu-vuc`, `--generic-*`), `thuan-an--gia-bang-gia` (gộp tương tự) | 40.000 | T2 38%; **chuẩn hoá 35:38 về 100%** sau khi tắt campaign chưa qua gate (journey-plan §3 ghi rõ cách này) |

- **Bộ keyword = `uu_tien=1`** của 4 nhóm trên → **74 keyword** (script `campaign-setup` §2.4 với `'^(brand-eco-retreat|brand-legacy-central|ben-luc--|thuan-an--)'`). `uu_tien=2` mở ở **G1**, không mở ngày 1 (`campaign-setup` §5.2).
- **Gộp ad group trong #3** vì ngưỡng ≥10 conv/tháng/ad group (`adgroup-map` §"Gộp là mặc định"): #3 = 256 click/tuần ÷ 2 ad group = 512 click/tháng × 4,8% ≈ **24 lead/ad group/tháng** ✔. Tách 4-5 ad group thì mỗi cái ~7 lead → dưới ngưỡng.
- **KHÔNG gộp Bến Lức với Thuận An** dù `adgroup-map` cho phép cụm "vệ tinh Nam" — 2 LP khác nhau, gộp là phá message match (QA Q2).
- **KHÔNG bật #2 `Brand_CDT`** dù có 10 kw `uu_tien=1`: (a) `ecopark *` phrase kéo tệp Ecopark Văn Giang/Hưng Yên — LP Long An không khớp message match, phải có negative địa lý trước; (b) 100k/ngày ÷ 28k = 3,6 click/ngày → không tới ngưỡng 10 conv/tháng → **gộp là mặc định**. Xem lại ở tuần 4.
- **KHÔNG bật:** #4 TaiChinh (kw `ben-luc--tai-chinh`/`thuan-an--tai-chinh` đều `uu_tien=2`, chờ G1) · #5, #6 (**G3**) · #7 Discovery broad (bắt buộc tCPA, đang 0 conv) · #8 NOXH (không phân phối) · RMKT Demand Gen (**G2**) · PMax (**G4**) · YouTube (**G5**).
- 27% ngân sách của các campaign chưa mở **không tạo campaign mới** — chuẩn hoá vào #1/#3; trả lại khi mở gate (`campaign-setup` §2.1 pattern "mượn quỹ").

**2. Bidding khởi điểm:** cả 2 campaign **Maximize Clicks + bid cap** (research §4: tuần 1-3 không smart bidding; bậc 0 của journey-plan §3.2). Cap 25k/40k neo vào dải research §2 (25k trung bình / 40k thận trọng); CPC kịch bản 28k áp cho cả hai — cap là **trần**, không phải CPC dự kiến.
Quy tắc chỉnh cap: chỉ khi IS lost (rank) >40% **và** chưa tiêu hết ngân sách → +20%/lần, cách ≥3 ngày (`campaign-setup` §2.2).

**3. Negative — ngày 1** (nếu bỏ: sim-rules phạt 25% ngân sách tuần 1-2)
- 386 dòng `cap_do=account` → **từ khoá phủ định cấp tài khoản** (tự áp mọi campaign type, kể cả PMax về sau — `campaign-setup` §1.4.1). Kiểm chứng đủ 386 dòng dạng `"phrase"` (§1.4.2).
- 80 dòng `cap_do=campaign` → shared list `NEG_BDS_Campaign_v1` gắn #1, #3.
- **Ô pre-flight tôi thêm (chưa có trong checklist): rà chéo negative × bộ keyword launch trước khi bật.** Chạy được ngay:

```bash
python3 - <<'P'
import csv,unicodedata,re
def t(s): return unicodedata.normalize('NFC',s.lower()).split()
neg=list(csv.DictReader(open('keywords/negative-keywords.csv')))
launch=re.compile(r'^(brand-eco-retreat|brand-legacy-central|ben-luc--|thuan-an--)')
kw=[r for r in csv.DictReader(open('keywords/master-keywords.csv')) if launch.search(r['nhom_adgroup'])]
for n in neg:
    a=t(n['keyword'])
    for k in kw:
        b=t(k['keyword'])
        if any(b[i:i+len(a)]==a for i in range(len(b)-len(a)+1)):
            print(n['keyword'],'|',n['cap_do'],'->',k['keyword'],k['nhom_adgroup'])
P
```

**Kết quả thật: 12 xung đột, 1 nghiêm trọng.**

| Negative | Ý định gốc (`ly_do`) | Nó chặn gì thật | Xử lý |
|---|---|---|---|
| `bao` | biến thể không dấu của `báo` ("Đọc tin") | **12 keyword launch** chứa cụm `giá bao nhiêu` — gồm `eco retreat giá bao nhiêu`, `legacy central giá bao nhiêu` (`uu_tien=1`, modifier hỏi giá = intent cao nhất) | **Xoá `bao` trần khỏi account list**; giữ 2 dòng dài đã có sẵn `bao cao thuc tap`, `bao gia xay dung` — chúng phủ đúng ý định gốc. Negative không khớp close variant nên `bao` không cần thiết để chặn `báo` |
| `anh` | biến thể không dấu của `ảnh` ("Tìm ảnh") | Không chặn kw của hệ, nhưng chặn mọi truy vấn có từ "anh" (rất phổ biến tiếng Việt) | Hạ xuống cụm: `hinh anh`, `anh du an` — không để 1 token |
| `booking` | "Đặt phòng du lịch" | Chặn truy vấn giữ chỗ BĐS (`booking <dự án>`) — chính là intent GĐ4/GĐ5 của journey-plan §1 | Hạ xuống **campaign-level** cho #3, giữ account-level thì mất nhóm truy vấn nóng nhất |

→ Đây là 3 sửa **bằng tay, trong `keywords/negative-keywords.csv`** (không sửa trong round này — chỉ ghi để Fable/`keyword-planner` vào theo `keywords/UPDATE.md`). Nó cũng là bằng chứng cho quyết định ở tuần 3: recommendation "Remove conflicting negative keywords" **không phải rác 100%** — nhưng cách xử lý đúng là đọc từng cặp rồi sửa tay, không bấm apply.

**4. Conversion actions:** tạo cả 6 theo `campaign-setup` §1.2 (`Lead_Form_Raw` 1 · `Click_Hotline` 1 · `Click_Zalo` 1 · `Lead_Contactable` 10 · `Lead_Qualified` 50 · `Dat_Coc` 500). Count = **Một** · cửa sổ nhấp **90 ngày** · goal **category** chuẩn Google (§1.2.7, vì recommendation/PMax đọc category không đọc tên). Ngày 1: 1-3 Primary (chỉ để thấy số, Max Clicks không đấu theo conversion), 4-6 rỗng chờ ECL. `phone_click`/`zalo_click` = Secondary **vĩnh viễn** (tracking/README luật #2).

**5. 11 ô cài đặt `campaign-setup` §1.5** — áp cho cả 2 campaign. Bốn ô quyết định vòng này:
- **1.5.11 TẮT TOÀN BỘ auto-apply recommendations** (`Đề xuất → Tự động áp dụng` **và** `Cài đặt tài khoản → Tự động áp dụng`), ghi ngày kiểm. Đây là ô làm cho sự kiện tuần 3 trở thành vô hại — làm trước, không làm sau.
- 1.5.1/1.5.2 Search Partners + Display Network **TẮT** (điều kiện G0).
- 1.5.4 Vị trí = **Sự hiện diện** (không "hoặc mối quan tâm").
- 1.5.6 ACA/DSA **TẮT** — rà lại hàng tháng (auto-upgrade ACA → AI Max từ 9/2026).

**6. LP — 2 trang riêng, 1 dự án/trang** (`landing-page/README.md`). CVR cộng dồn theo sim-rules:

| Mục | Điểm | Thực thi |
|---|---|---|
| Nền | 2,0 | — |
| Message match ≥4/5 | +1,0 | 2 luồng đang bật: brand (H1 = `<Tên dự án> Bảng Giá Mới Nhất`, pin H1 RSA) · khu vực (H1 = loại hình + khu vực + `Giá Từ …`). Luồng tài chính chưa bật campaign → không tính |
| Bảng giá above the fold | +0,8 | Eco Retreat: `từ 2,5 tỷ` (Forest Onsen — số có nguồn `research/competitors/2026-07-eco-retreat.md`). Legacy Central: `[điền từ bảng giá đợt hiện tại]` |
| Zalo sticky + click-to-call | +0,6 | `zalo_click` / `phone_click` (Secondary) |
| Form 4 field + 2 dropdown | +0,4 | ngân sách / mục đích — kéo qualify rate lên 40% |
| **CVR dùng cho cả kỳ** | **4,8%** | trần 6,0 chưa chạm |

Hard gate LP (rớt 1 = không launch): đủ 6 event registry · footer pháp nhân + MST · hidden field `gclid/gbraid/wbraid/gad_source` tới Keap · <2,5s/4G · có bảng giá.
Ràng buộc policy cứng: headline `Giá Gốc CĐT` **chỉ dùng nếu LP nói rõ mình là đơn vị phân phối, không phải CĐT** — mạo nhận = đình chỉ tài khoản không cảnh báo (research §7). Objection Eco Retreat: **bàn giao Q2/2028** (đối thủ Waterpoint đã có >500 hộ ở) → block tiến độ ảnh thật + biến ân hạn 24 tháng thành lý do mua sớm.

**7. Hai điều kiện tiên quyết CHƯA xanh — ghi ra vì kết quả treo trên chúng**
- **SLA gọi lead <5'**: contact rate 55% của sim-rules đòi dropdown + validate đầu số + SLA <5'. Hai cái đầu tôi làm được trên LP; SLA là thoả thuận với sale mà `PLAN.md` §6.6 đang **PENDING** (chưa có quyền xem quy trình sale). Không có SLA → tụt xuống **35%**, mất ~1/3 lead gọi được. Đây là việc phải chốt trước ngày launch, không phải việc tuần 4.
- **ECL/Data Manager API**: pipeline có spec + selftest pass nhưng chưa chạy thật (thiếu credentials + quy tắc gắn tag Keap). Đây là **đồng tiền duy nhất mua được gate G4/bậc 2-3** (journey-plan §3.2: "thứ mở khoá AI không phải ngân sách, mà là dữ liệu conversion chất lượng").

## Nhật ký tuần 1-4

Công thức: click/tuần = 13,79tr ÷ 28k = **492** (negative đã import ngày 1 → không có 25% click rác) · lead raw = 492 × 4,8% = **23,6** · qualified = ×40% = **9,4** · gọi được = ×55% = **13,0** · CPL-q = 13,79tr ÷ 9,44.

| Tuần | Chi tiêu | Click | Lead raw | Lead qualified | Contact rate | CPL-q | Sự kiện | Hành động + căn cứ |
|---|---|---|---|---|---|---|---|---|
| 1 | 13,79tr | 492 | 23,6 | 9,4 | 55% (13,0 gọi được) | **1,46tr** | — | **KHÔNG đổi** bid cap/ngân sách/RSA/keyword (`campaign-setup` §4.1). D+0: mọi ad `Đã phê duyệt`, có click sau 12h. D+1: lead thật có `gclid` trong Keap — trống thì **tạm dừng toàn bộ** (§4.3). D+3: negative chỉ cho term rõ sai ngành |
| 2 | 13,79tr | 492 | 23,6 | 9,4 | 55% (13,0) | 1,46tr | — | **Nghi thức search terms 3 lượt** (journey-plan §5): lãng phí ≥3 click/0 conv → negative · term có conv → nâng Exact · phrase trôi nghĩa → siết. Cập nhật `keywords/` theo `UPDATE.md`. Đọc **10 lead gần nhất**, tính contact rate lần đầu (research §5, đích >50%). Đề xuất bổ sung kw thiếu: `eco retreat long an`, `ecopark long an`, `forest onsen` (competitor doc đã chỉ ra, master list chưa có) |
| 3 | 13,79tr | 492 | 23,6 | 9,4 | 55% (13,0) | 1,46tr | 🚨 **Rep Google mời PMax + auto-apply ("+20% conversion, chuyên gia setup miễn phí"); UI có recommendation `Remove conflicting negative keywords` đang chờ auto-apply.** Tài khoản 11 conv/30 ngày, ECL chưa chạy | **TỪ CHỐI PMax + auto-apply** — 6 căn cứ ở bảng dưới. Không phạt gate. Việc thường tuần vẫn chạy: báo cáo theo giờ/thiết bị → siết ad schedule; cột `Lượt nhấp không hợp lệ` (<10% bình thường); thêm **RSA thứ 2** vào mỗi ad group, đổi **một** biến (góc offer) |
| 4 | 13,79tr | 492 | 23,6 | 9,4 | 55% (13,0) | 1,46tr | — | **GIỮ Max Clicks.** Điều kiện Maximize Conversions = ≥15 conv/30 ngày *cấp campaign* + contact rate >50% + ≥4 tuần (`campaign-setup` §4.4) → account chỉ 11 → **chưa đủ, không đổi**. Không mở G1/G2/G3, không bật #7. Đo CVR LP thật; <2% thì sửa LP trước, không đụng bid. Điền tháng 1 vào scorecard journey-plan §4 |
| **Σ 4 tuần** | **55,16tr** | **1.968** | **94,4** | **37,8** | 55% (51,9) | **1,46tr** | | |

> ⚠️ **Hai con số "conversion" khác nhau — không bịa cầu nối.** Kịch bản tiêm **11 conv/30 ngày** (cột `Conversions` mà rep đang nhìn) < lead raw công thức của tôi (23,6/tuần). Cơ chế giải thích, không phải phép chỉnh số: cột `Conversions` chỉ đếm **Primary** = `generate_lead`, còn `phone_click`/`zalo_click` là **Secondary vĩnh viễn** (tracking/README luật #2) và Zalo/hotline là CTA chính của khách VN (`CLAUDE.md`) → phần lớn lead raw **không nằm trong cột đó**; `All conversions` thì lại gộp cả Secondary + view-through (`monitoring` §1). Tôi **dùng 11** cho mọi quyết định gate/bidding vì đó là con số Google Ads dùng để xét ngưỡng, và ghi rõ nó không phải tổng lead.

### Tuần 3 — xử lý sự kiện tiêm, theo đúng thứ tự ưu tiên

**Ưu tiên 1 (làm trong ngày, trước cả khi gọi lại rep): chặn đường tự động, vì nó không cần mình đồng ý.**
`Đề xuất → Cài đặt tự động áp dụng` + `Cài đặt tài khoản → Tự động áp dụng` phải **rỗng**; mở **History tab** xem có gì đã tự apply, ai bật, lúc nào. Nếu `Remove conflicting negative keywords` đã chạy → **re-import 386 dòng** account-level và kiểm chứng đủ số (§1.4.1-1.4.2); mất negative list ≈ hình phạt "không import ngày 1" của sim-rules: 25% ngân sách cháy ⇒ −5,9 lead raw/tuần. Căn cứ: auto-apply **chỉ có cấp tài khoản, không loại trừ được campaign** ("Only account-level auto-apply is available") và danh sách của nó có cả `Remove conflicting negative keywords`, `Use Display expansion`, `Add broad match keywords` (curriculum §A1) — hai cái đầu phá đúng 2 quyết định nền của hệ (§1.4, §1.5.2).

**Ưu tiên 2: recommendation `Remove conflicting negative keywords` — không apply, cũng không dismiss mù.**
Mở chi tiết, đọc từng cặp negative ↔ keyword bị chặn. Vòng pre-flight tuần 0 đã chứng minh loại xung đột này **có thật** (`bao` chặn 12 keyword `giá bao nhiêu`). Luật xử lý (`adgroup-map` §"Cảnh báo xung đột"): xung đột thật thì **hạ negative xuống campaign-level** hoặc thay bằng cụm dài hơn — **không xoá khỏi account list** (xoá là mở lại rò rỉ "cho thuê/tuyển dụng", nguồn lãng phí lớn nhất của ads BĐS VN). Cặp không phải xung đột thật → Dismiss, ghi `ops/audit-log.jsonl`. Biết trước 2 điều: **dismiss LÀM TĂNG optimization score**, và score **không phải KPI** (research §7b) → không báo cáo nó, không lấy nó làm lý do bấm gì.

**Ưu tiên 3: trả lời rep — từ chối PMax, có căn cứ.**

| # | Căn cứ | Trạng thái thật |
|---|---|---|
| 1 | **G4** (journey-plan §3.1) đòi ĐỦ CẢ: offline import chạy thật · brand exclusion · Search ≥30 conv/tháng · negative apply cho PMax ngày 1 | ECL **chưa chạy**, conv **11 < 30** → rớt 2/4 điều kiện cứng |
| 2 | **Bậc thang AI** (journey-plan §3.2): PMax = **bậc 5**; hệ đang ở **bậc 0** (Max Clicks, 0 conv offline). Bậc 2 mới được test broad | Nhảy 5 bậc |
| 3 | **`campaign-setup` §5.5 bước 1**: conversion goal của PMax phải là category `Qualified lead`/`Converted lead` với ≥15 conv/30 ngày | Action `Lead_Qualified` đang **rỗng** (ECL chưa chạy) → chỉ còn form raw để feed. PMax "tối ưu theo signal được đưa vào; signal rác thì nó mua rác rất hiệu quả" |
| 4 | **Ngân sách**: journey-plan §3 cột 60tr cho PMax **0%**; PMax chỉ xuất hiện 8% ở kịch bản 150tr, và ngay cả ở đó `campaign-setup` §5.4 ghi **QA CHƯA CHỐT → không bật** | Không có ô ngân sách nào cho PMax ở 60tr |
| 5 | **Kỹ thuật**: negative của hệ chỉ phủ **Search + Shopping inventory** của PMax; phần Display/YouTube cần `Excluded content keywords` cấp tài khoản — **chưa điền** (§5.5 hộp cảnh báo) | Bật bây giờ = ad BĐS chạy trên app game/parked domain mà 386 negative không cứu |
| 6 | **Learning**: 1-2 tuần, **tới 6 tuần khi volume thấp** (research §4, nguồn Google) | 11 conv/30 ngày = cận trên → learning ăn hết phần còn lại của kỳ |

Về lời hứa **"+20% conversion"**: không có nguồn kiểm chứng được, cùng loại với claim "+15% conversion khi Ad Strength Poor→Excellent" mà research §7b đã đánh dấu là **tương quan tổng hợp toàn bộ advertiser, không phải nhân quả cho 1 tài khoản**. Và chính Google đặt điều kiện tiên quyết cho nhánh tự động: *"It's critical to use Smart Bidding with broad match"* — hệ đang Max Clicks nên **chưa thoả điều kiện của chính Google** (research §3).

**Giá của việc nhận lời** (sim-rules: CVR ×0,6 + 20% chi tiêu lãng phí): tuần 3-4 CVR 4,8% → 2,88%, click hữu ích 492 → 394 ⇒ lead qualified **4,5/tuần** (thay vì 9,4), **CPL-q ~3,04tr** (thay vì 1,46tr), CPL-q cả kỳ **~1,97tr** (55,16tr ÷ 27,95 lead-q) — đắt hơn cả kịch bản trung bình 1,56tr của research §2. Nói con số này cho rep, không nói "chúng tôi không thích PMax".

**Nhận cái gì từ "chuyên gia miễn phí" (đúng gate, không tốn ngân sách):**
1. **Onboarding Data Manager API cho ECL** — đúng blocker duy nhất đang khoá G4/bậc 2-3. Đây là việc đáng lấy nhất.
2. Kiểm `Tools → Audience manager` xem **Customer Match có khả dụng ở VN** cho account này — Google **không publish** danh sách quốc gia, chỉ mở account ra mới biết (journey-plan §2.1, PLAN §6.6).
3. Rà **goal category** của 6 conversion action (§1.2.7) + trạng thái **advertiser verification** (30 ngày không nộp = tạm ngưng tài khoản).
4. Reach Planner để dành cho G5 — chưa cần.
5. **Quyền truy cập:** rep/chuyên gia nhận **Read-only**, không Standard/Admin. Luật hệ: *"mọi suggest đều là ĐỀ XUẤT — người bấm nút chi tiền"* (`monitoring` §6). Mọi thay đổi rep đề xuất đi qua đúng đường đó.

**Ưu tiên 4: đóng vòng.** Ghi `ops/audit-log.jsonl` (nội dung cuộc gọi, quyết định, lý do) + đưa vào rà **thứ 2 đầu tháng** (`monitoring` §4): auto-apply còn tắt không · experiment sắp hết hạn (tự apply nếu "favorable") · **Ask Advisor / mọi mục Gemini-agent** đã xuất hiện chưa (đường auto-apply thứ 4, ô §1.5.11 có thể không phủ được).

## Tổng kết

| Chỉ số | Cả kỳ 4 tuần |
|---|---|
| Chi tiêu | **55,16tr₫** (1.970k/ngày × 28 ngày) |
| Click | **1.968** (CPC kịch bản 28k) |
| Lead raw | **94,4** |
| Lead gọi được (contact rate 55%) | **51,9** |
| Lead qualified (40%) | **37,8** |
| **CPL qualified** | **1,46tr₫** — dưới kịch bản trung bình research §2 (1,56tr) |
| CPL raw | 584k₫ |
| CTR giả định | **7,61%** — WordStream 2026 Real Estate (Mỹ), research §2, **mốc thô không phải KPI** → ~25.900 impression. Sim-rules không mô hình hoá CTR |
| Nguồn chân lý | CRM (Keap). Không cộng dồn conversion Ads/GA4/CRM (journey-plan §4) |

**Trạng thái gate cuối kỳ**

| Gate | Trạng thái | Thiếu gì |
|---|---|---|
| G0 | ✅ đạt | — |
| G1 (mở `uu_tien=2`, khu vực mới) | ⛔ | Cần brand ≥`[điền]` conv/tháng **và** CPL ≤ mục tiêu 30 ngày liên tiếp — mà `CPL mục tiêu` chưa tính được: thiếu phí môi giới/căn + tỷ lệ booking→HĐMB (journey-plan §6) |
| G2 (RMKT Demand Gen) | ⛔ | Audience `xem_bang_gia`/`engaged_60s` ≥1.000 user/30 ngày. Trần lý thuyết là 1.968 click/30 ngày ⇒ cần >50% khách scroll tới bảng giá; **phải đọc số GA4 thật**, không đoán. Xem lại tháng 2 |
| G3 (Search T3) | ⛔ | Cần tCPA 2 tháng liên tiếp + G2 |
| G4 (PMax) | ⛔ | **ECL chưa chạy** + 11 < 30 conv/30 ngày. Đã từ chối ở tuần 3 |
| G5 (YouTube) | ⛔ | Ngân sách <150tr + chưa G4 |
| Bậc AI (§3.2) | **bậc 0** | Max Clicks · Phrase+Exact · auto-apply TẮT · ACA TẮT |

**Bidding cuối kỳ:** vẫn Max Clicks + cap ở cả 2 campaign. Không reset learning lần nào (0 lần đổi ngân sách, 0 lần đổi chiến lược) → không ăn phạt ×0,7 của sim-rules.

**3 bài học**

1. **60tr không mua được gate — ECL mới mua được.** Ngân sách tăng 2× so với kịch bản 30tr nhưng bậc mở khoá vẫn là **bậc 0**, vì điều kiện của mọi gate là *dữ liệu conversion chất lượng*, không phải chi tiêu (journey-plan §3.2). Hệ quả vận hành: việc đáng làm nhất tháng 2 không phải mở campaign mới mà là **chốt quy tắc gắn tag Keap + bật `upload_ecl.py`** — và đó cũng là việc duy nhất nên nhờ chuyên gia Google làm miễn phí.
2. **Đường tự động nguy hiểm hơn lời mời của rep.** Rep phải chờ mình đồng ý; auto-apply thì không. Vì vậy ưu tiên 1 của sự kiện là **kiểm ô auto-apply + History tab**, chỉ ưu tiên 3 mới là gọi lại rep. Và ô đó phải được tắt từ **tuần 0** (§1.5.11) — nếu để tới lúc recommendation xuất hiện thì đã muộn.
3. **Đọc đúng cột trước khi tranh luận bằng số.** Rep nói "11 conversion, PMax sẽ +20%"; hệ đo 23,6 lead raw/tuần. Hai số không mâu thuẫn — `Conversions` chỉ có Primary (`generate_lead`), `All conversions` gộp cả Secondary + view-through, còn Zalo/hotline (CTA chính của khách VN) nằm ngoài cột quyết định ngưỡng. Không dựng lại được chuỗi cột này thì mọi cuộc tranh luận về ngưỡng gate là hai bên nói về hai tập dữ liệu khác nhau — và **contact rate (55%) mới là số phải báo cáo trước CPL**.

**2 việc phát sinh cần Fable/`keyword-planner` xử lý (ngoài phạm vi file này):** (a) 3 negative sai phạm vi trong `keywords/negative-keywords.csv` — `bao`, `anh`, `booking`; (b) thiếu 3 keyword đã được `research/competitors/2026-07-eco-retreat.md` chỉ định: `eco retreat long an`, `ecopark long an`, `forest onsen`.
