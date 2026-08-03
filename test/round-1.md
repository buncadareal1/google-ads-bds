# Round 1 — Baseline 30tr (Eco Retreat, Bến Lức, Long An · CPC kịch bản 30k₫)

Tham số cố định: ngân sách 1.000.000₫/ngày = 7.000.000₫/tuần · CPC 30.000₫ · 4 tuần = 28.000.000₫.
Nguồn số dự án (không bịa): `research/competitors/2026-07-eco-retreat.md` — căn hộ Forest Onsen **từ 2,5 tỷ** · **25% đến khi nhận nhà** · vay **70%** · ân hạn gốc+lãi **24 tháng** · CK tới **12%** khi TT sớm 95% · 220ha · bàn giao cuối 2026→**Q2/2028**.

## Setup tuần 0 (quyết định + căn cứ doc)

**Pre-flight (§1 campaign-setup)**
- D-7: nộp advertiser verification (Tổ chức + ĐKKD/MST + CCCD) — `research` §7: "all advertisers will eventually be required", 30 ngày không nộp = treo tài khoản. Hồ sơ thanh toán: Doanh nghiệp / **VND** / **GMT+7** (không đổi được sau).
- 6 conversion action đủ thang (§1.2): `Lead_Form_Raw`/`Click_Hotline`/`Click_Zalo` = Primary ngày 1 · `Lead_Contactable`(10)/`Lead_Qualified`(50)/`Dat_Coc`(500) tạo rỗng. Count=**Một**, cửa sổ nhấp **90 ngày** (chu kỳ BĐS 3–12 tháng, `tracking/README` luật #4), goal **category** đúng chuẩn Google (§1.2.7), `Lead_Contactable` khai là mục tiêu chính cấp tài khoản để pipeline ECL không phải sửa schema.
- GA4 ↔ Ads link + **auto-tagging ON**, import 3 event GA4. `phone_click`/`zalo_click` = **Secondary vĩnh viễn** (`tracking/README` luật #2 — bẫy optimize-to-quality).
- **Negative ngày 1**: dán **386 dòng `cap_do=account`** vào Từ khoá phủ định **cấp tài khoản** (tự áp mọi campaign type, kể cả PMax sau này — QA chốt §1.4) + kiểm chứng trang hiển thị đủ 386 dòng dạng `"phrase"` (§1.4.2). 80 dòng campaign-level → shared list `NEG_BDS_Campaign_v1` gắn #1–#3.
- **11 ô §1.5**: Search Partners OFF · Display/Display Expansion OFF · Vị trí = VN, tuỳ chọn = **Sự hiện diện** · Ngôn ngữ VI+EN · **ACA/Dynamic sitelink OFF** · lịch 05:00–24:00 (siết về giờ trực máy cho Call asset) · phân phối Chuẩn · tracking template UTM (bắt buộc cho Clarity↔Ads) · **không** shared budget · **auto-apply recommendations TẮT HẾT** (nguy hiểm nhất: `Remove conflicting negative keywords`, `Use Display expansion`).
- G0 (`journey-plan` §3.1) nghiệm thu bằng **1 lead thật** đi tới Keap có `gclid`, LP <3s mobile. Chưa pass = không bật ad.

**Bộ launch = 67 keyword** (lọc `uu_tien=1` + regex `^(brand-eco-retreat|brand-cdt--ecopark|ben-luc--|long-an--)` = 71, **bỏ 4 kw** `nhà phố|đất nền bến lức/long an`: Eco Retreat không bán đất nền, nhà phố 5,8 tỷ+ chưa đủ 10 conv/tháng để có ad group riêng → `adgroup-map` "gộp là mặc định, tách là ngoại lệ").

| # | Campaign | ₫/ngày | Cap | Ad group (số kw) | Căn cứ |
|---|---|---|---|---|---|
| 1 | `BDS_Search_Brand_DuAn` | **475.000** | 20k | `brand-eco-retreat` (8) | §2.1 (375k + 100k mượn quỹ RMKT) · 1 dự án phân phối → 1 AG (§2.3) |
| 2 | `BDS_Search_Brand_CDT` | **75.000** | 25k | `brand-cdt--ecopark` (5) | §2.1 · **loại trừ Hưng Yên + Hà Nội** (§1.5.3): 5 kw này khu_vuc=Hưng Yên, người search "ecopark bảng giá" ở Bắc là tệp Văn Giang — không phân phối |
| 3 | `BDS_Search_KhuVuc_GiaoDich` | **450.000** | 35k | AG1 `ben-luc+long-an--gia-bang-gia` (30) · AG2 `--mua-ban/mo-ban-moi/du-an-khu-vuc/generic-can-ho+chung-cu` (24) | 350k + **30k của #8** + **70k của #4** · tối đa 2 AG (§2.3) · gộp Bến Lức+Long An theo "Cụm vệ tinh Nam" (`adgroup-map`) |
| 4 | `BDS_Search_TaiChinh` | **0** | — | — | **Phát hiện:** `ben-luc--tai-chinh`/`long-an--tai-chinh` toàn bộ ở `uu_tien=2` → 0 keyword đủ điều kiện ngày 1. Không dựng campaign rỗng (ponytail); 70k dồn #3 |
| 8 | `BDS_Search_NhaOXaHoi` | **0** | — | — | Eco Retreat không phải NOXH → §2.1 "dồn vào #3" |
| 7 | `BDS_Search_Discovery` (broad) | **0 — hoãn** | — | — | Bắt buộc tCPA, ngày 1 có 0 conversion (`adgroup-map` #7 · `journey-plan` §3.2 bậc 2) |
| — | `BDS_RMKT_Demand Gen` | **0 — hoãn** | — | — | Chưa qua G2 |
| | **Tổng** | **1.000.000** | | **4 AG / 67 kw** | |

**Bidding**: tất cả **Maximize Clicks + bid cap** (`research` §4: tuần 1–3 không smart bidding; 0 conversion → mọi thứ "AI" học từ hư không, `journey-plan` §3.2 bậc 0). Cap neo vào dải 15/25/40k của `research` §2.
**Kiểm sau import (bắt buộc)**: §2.4.6 — lọc cột `Loại đối sánh` = **Rộng phải trả về rỗng** (broad là default của Google, dòng import sai cột thành broad im lặng). Phân bố thực tế: 18 exact / 49 phrase. Mỗi AG có Final URL/anchor riêng, **không AG nào trỏ homepage** (Q2).

**RSA**: 2 RSA/AG (chừa 1 slot cho tuần 3). Bộ 1 cho #1/#2, bộ 2 cho #3 (§3), pin **H1** khoá message match. Đã điền số thật và kiểm ký tự (§3.5): `Eco Retreat Bảng Giá Mới Nhất` 29 · `Eco Retreat Giá Từ 2,5 Tỷ` 25 · `Chỉ 25% Đến Khi Nhận Nhà` 24 · `Ân Hạn Gốc & Lãi 24 Tháng` 25 · `Chiết Khấu Đến 12%` 18 · `Căn Hộ Bến Lức Giá Từ 2,5 Tỷ` 28 — tất cả ≤30, không ALL-CAPS, không tên đối thủ, không cam kết sinh lời.
🚨 Headline `Eco Retreat - Giá Gốc CĐT` (§3.1 #4) **chỉ dán nếu LP có dòng "đơn vị phân phối, không phải chủ đầu tư"** — mạo nhận CĐT = đình chỉ tài khoản không cảnh báo (`research` §7). Chưa có dòng đó ở nghiệm thu LP → bỏ headline này.
**Extensions**: 6 sitelink cấp campaign trỏ **anchor trên chính LP** (§3.4, đủ ngưỡng 6 của Google), 5 callout + 1 Call (Google forwarding number **TẮT** — chưa hỗ trợ VN) cấp tài khoản. Location: **bỏ qua** (chưa có GBP đã xác minh — không tạo hồ sơ ảo).

**LP spec chọn (user tự làm theo `tracking/lp-requirements.md`) → cấu thành CVR**

| Thành phần | Điểm CVR | Nội dung chốt |
|---|---|---|
| Nền | 2,0 | LP **riêng cho Eco Retreat**, không homepage (gửi homepage = ×0,4) |
| Message match ≥4/5 cả 3 luồng | +1,0 | H1 brand = "Eco Retreat — Bảng giá 07/2026"; luồng khu vực = "Khu đô thị sinh thái Bến Lức, từ 2,5 tỷ"; anchor riêng `#bang-gia`/`#mat-bang`/`#tra-gop` khớp Path RSA |
| Bảng giá/khoảng giá above the fold | +0,8 | "Từ 2,5 tỷ" + USP số "25% đến khi nhận nhà · ân hạn 24 tháng" ngay màn hình đầu 390px (đối thủ **không ai** có giá ở hero — competitor §3 mục 4) |
| Zalo sticky + click-to-call | +0,6 | `zalo_click`/`phone_click`, sticky bar thay exit popup (mobile 75–85%) |
| Form 4 field + 2 dropdown qualifying | +0,4 | Tên · SĐT (validate đầu số) · dropdown **Ngân sách** (<3/3–5/5–10/>10 tỷ) · dropdown **Mục đích** (ở/đầu tư/second home) · email tuỳ chọn · honeypot + reCAPTCHA v3 · hidden `gclid/gbraid/wbraid/gad_source/utm_*` |
| **CVR LP** | **4,8%** | = trần khả thi của bảng luật (2,0+2,8), dưới trần cứng 6,0 |

Ngoài công thức, vẫn bắt buộc theo `landing-page/README.md` hard gate: 6 event đúng registry `CLAUDE.md`, footer pháp nhân+MST, block objection **bàn giao Q2/2028** (ân hạn 24 tháng phủ gần trọn thời gian chờ), ảnh tiến độ có ghi tháng.

**Qualify rate 40%** (có 2 dropdown) · **Contact rate 55%** — điều kiện: 2 dropdown ✔ + validate đầu số ✔ + **SLA gọi <5′**. SLA là điều kiện launch tôi đặt ra và phải có người chịu trách nhiệm; `PLAN.md` §6.6 ghi quy trình sau-lead đang PENDING → **rủi ro đã khai**: không có cam kết SLA thì contact rate rơi về 35% (xem sensitivity ở Tổng kết).

## Nhật ký tuần 1-4

| Tuần | Chi tiêu | Click | Lead raw | Lead qualified | **Contact rate** | CPL-q | Sự kiện | Hành động + căn cứ |
|---|---|---|---|---|---|---|---|---|
| 1 | 7.000.000₫ | 233 | 11,2 | 4,48 | **55%** (6,2 contactable) | 1.562.500₫ | — | D+0 10:00 mọi ad `Đã phê duyệt`; D+0 18:00 có click đầu; **D+1 lead test có `gclid` trong Keap** (trống = tạm dừng toàn bộ, §4.1). D+3 search terms lượt 1: chỉ thêm negative **term rõ ràng sai ngành**, chưa cắt keyword. **KHÔNG đổi bid cap/ngân sách/RSA/keyword** (§4.1 — đổi = reset learning) |
| 2 | 7.000.000₫ | 233 | 11,2 | 4,48 | **55%** (6,2) | 1.562.500₫ | **⚠️ Search terms đầy "cho thuê nhà bến lức", "tuyển nhân viên kinh doanh eco retreat", "eco retreat lừa đảo"** | Xử lý theo thứ tự dưới bảng. Thêm: đọc **10 lead gần nhất** tính contact rate lần đầu (§4.1 tuần 2); cập nhật `keywords/` theo `UPDATE.md`; **D+8 nâng cap #1 20k→24k, #2 25k→30k; D+11 #1 24k→28,8k** (§2.2: chỉ khi Lost IS (rank) >40% **và** chưa tiêu hết ngân sách, +20%/lần cách ≥3 ngày — CPC thị trường 30k > cap 20k của brand). Cap ≠ ngân sách ≠ tCPA → **không** thuộc diện reset learning |
| 3 | 7.000.000₫ | 233 | 11,2 | 4,48 | **55%** (6,2) | 1.562.500₫ | Hệ quả sự kiện: **0%** chi tiêu vào intent sai (đã xử lý đúng quy trình) | Báo cáo theo **giờ + thiết bị** → siết lịch nếu có khung rác; kiểm cột **Lượt nhấp không hợp lệ** (<10% bình thường, `research` §5); thêm **RSA #2** mỗi AG, đổi **một** biến (góc offer: "ân hạn 24 tháng" vs CTA: "nhận bảng giá qua Zalo"); Clarity 1 lượt/tuần (10 req/ngày) đọc rage/dead click trên form + block bảng giá |
| 4 | 7.000.000₫ | 233 | 11,2 | 4,48 | **55%** (6,2) | 1.562.500₫ | — | Đo **CVR LP thật = 4,8% > 2%** → LP không phải chỗ cần sửa (§4.1 tuần 4). **Quyết định bidding: GIỮ Max Clicks** (lý do dưới bảng). Review gate G1–G5. Điền tháng 1 vào scorecard `journey-plan` §4 — ghi rõ **CRM là nguồn đếm, không cộng dồn Ads/GA4/CRM** (Q8) |

**Xử lý sự kiện tuần 2 — chẩn đoán trước khi thêm negative (root cause, không vá triệu chứng)**

Cả **3/3 cụm đã có trong 386 dòng account-level** đang chạy: `thuê`, `cho thuê`, `thuê nhà`, `cho thue`, `thue nha` (dòng 2–6, 426–432) · `tuyển nhân viên kinh doanh`, `tuyển nhân viên`, `tuyen nhan vien` · `lừa đảo`, `lua dao`. Với 67 keyword phrase/exact hiện tại, **không keyword nào có thể khớp 3 truy vấn này** (exact không khớp query thêm từ; phrase không chứa cụm). → Việc chúng xuất hiện **không phải lỗ hổng danh sách negative, mà là lỗi cấu hình**. Thêm negative trước khi chẩn đoán = công việc giả và che mất lỗi thật.

| # | Giả thuyết | Kiểm trong ≤5′ | Sửa |
|---|---|---|---|
| 1 | Term thuộc cửa sổ dữ liệu **trước khi list có hiệu lực** (negative chỉ áp cho phiên đấu giá tương lai) | Segment theo **ngày**: có click nào sau ngày apply không? | Nếu 0 click sau ngày apply → **không làm gì**. Đóng lượt |
| 2 | **Keyword bị import thành Broad im lặng** (broad là default của Google Ads — `adgroup-map` §Match type, §2.4.6). Đây là cơ chế duy nhất giải thích được cả 3 term | Lọc cột `Loại đối sánh` = **Rộng** | Sửa match type về phrase/exact, pause dòng lỗi, chạy lại kiểm §2.4.6 cho toàn bộ 67 kw |
| 3 | 386 dòng **dán sai chỗ** (shared list chưa gắn / dán cấp campaign 1 nơi) hoặc bị `auto-apply → Remove conflicting negative keywords` xoá (§1.5.11) | `Quản trị → Cài đặt tài khoản → Từ khoá phủ định` đếm đủ 386 dòng `"phrase"`? Lịch sử thay đổi có bản ghi auto-apply? | Dán lại + tắt lại auto-apply, kiểm chứng theo §1.4.2 |

Sau khi bịt nguồn, chạy **nghi thức search terms 3 lượt** (`journey-plan` §5 tuần #1):
- **(a) lãng phí** — term ≥3 click / 0 conv → negative. **0 dòng thêm vào `negative-keywords.csv` cho 3 cụm này** (đã phủ; thêm nữa là dòng trùng). Đúng theo `UPDATE.md` Q1 chỉ append cái **chưa có**.
- **(b) thắng** — term có conv chưa là keyword → nâng exact/phrase.
- **(c) trôi** — hạ match type. Ghi chú: `research` §3 — search terms report **luôn ẩn term ít volume**, mục tiêu là **giảm dần rò rỉ**, không phải "0 term rác".

**Đề xuất thật cho `keywords/` (ngoài phạm vi file này, đẩy qua `UPDATE.md` cho agent `keyword-planner`)** — negative **campaign-level** cho #1/#2 chống cannibalize dự án cùng CĐT Ecopark (competitor §"Loại khỏi tập đối thủ": xử lý bằng negative chéo, **không** viết copy phản công), hiện grep = 0 dòng, kèm biến thể không dấu vì negative không khớp close variant:
```csv
văn giang,"Sibling Ecopark Văn Giang - khác miền, cannibalize brand CĐT",campaign
van giang,"biến thể không dấu",campaign
sky oasis,"Sibling Ecopark Văn Giang",campaign
solforest,"Sibling Ecopark Văn Giang",campaign
haven park,"Sibling Ecopark Văn Giang",campaign
đảo châu âu,"Sibling Ecopark Văn Giang",campaign
dao chau au,"biến thể không dấu",campaign
ecovillage saigon river,"Sibling Ecopark Nhơn Trạch - cùng CĐT, phân khúc cao hơn 1 bậc",campaign
```
Và keyword **thiếu**: `ecopark long an`, `eco retreat long an`, `forest onsen` (competitor §Action 1 đề xuất nhưng bộ 22 kw đã tạo không có) — khách miền Nam gọi dự án theo tên CĐT + tỉnh.

**Quyết định bidding tuần 4 — GIỮ Max Clicks, không lên Maximize Conversions**
Điều kiện §4.4 về **volume** đã đạt: #1 ≈ 21 conv/30 ngày (47,5% chi tiêu), #3 ≈ 20 (45%) — cả hai ≥15; #2 chỉ ≈ 3,4 → **gộp, không tách** (`journey-plan` §3), contact rate 55% >50%, đã chạy 4 tuần. Nhưng `journey-plan` §3.2 **bậc 1** yêu cầu **đảo primary sang `Lead_Contactable` TRƯỚC** khi bật smart bidding, mà `Lead_Contactable` cần **ECL chạy thật** — đang bị chặn bởi `PLAN.md` §6.6 (chưa có quyền Keap để thống nhất quy tắc gắn tag) + thiếu credentials Data Manager API. Bật Max Conversions lúc primary vẫn là **form thô** = đúng bẫy optimize-to-quality (`journey-plan` §2.3): nó sẽ mua form-fill rẻ nhất. → **Việc đáng làm duy nhất ở tuần 4 không phải đổi bidding, mà là gỡ chặn ECL.**

## Tổng kết

| Chỉ số | 4 tuần |
|---|---|
| Chi tiêu | **28.000.000₫** |
| Click | **933** |
| Lead raw | **44,8** (≈45) |
| **Contact rate** | **55% → 24,6 lead liên hệ được** |
| Lead qualified | **17,9** (≈18) |
| CPL raw | **625.000₫** |
| **CPL qualified** | **1.562.500₫** |
| CTR **giả định** | **7,61%** → ≈12.260 impression. ⚠️ Đây là WordStream 2026 Real Estate (Mỹ, `research` §2) — **giả định lập kế hoạch, không phải số đo VN**; không có benchmark CTR BĐS VN đáng tin (`research` §Khoảng trống #1) |

CPL-q **1,5625tr = đúng kịch bản "trung bình"** của `research` §2 (1,56tr) — không phải trùng hợp: 4,8% là **trần khả thi** của bảng luật CVR, nên với CPC 30k và qualify 40% thì `CPC/(CVR×qualify)` đã bị chốt. Ở round này giá trị tạo ra nằm ở chỗ **không mất** tiền: 0 lần reset learning, 0% chi tiêu vào intent sai, LP đạt trần CVR từ tuần 1.

**Đối chứng nếu xử lý sai sự kiện tuần 2** (15% chi tiêu tuần 3–4 cháy vào intent sai): click 198,3/tuần → lead qualified kỳ 16,58 → **CPL-q 1.689.190₫ (+126.690₫, +8,1%)**, mất **1,34 lead qualified**.
**Sensitivity contact rate**: không có cam kết SLA <5′ → 35% → chỉ **15,7** lead liên hệ được thay vì 24,6 (**−36%**). CPL-q không đổi (qualify rate độc lập) — đây chính là lý do `tracking/README` luật #4 đặt contact rate là KPI số 1, báo cáo **trước** CPL: CPL trông y nguyên trong khi mất hơn 1/3 lead thật.

**Trạng thái gate cuối kỳ — không gate nào mở**

| Gate | Trạng thái | Lý do bằng số |
|---|---|---|
| G0 | ✅ đã qua | lead thật có gclid, LP <3s, 386 negative account-level, Partners+Display OFF, Presence |
| G1 (mở rộng T2) | ⛔ **không đánh giá được** | Điều kiện là "CPL ≤ mục tiêu 30 ngày liên tiếp", nhưng `CPL mục tiêu` phải tính từ breakeven `journey-plan` §4 — thiếu **phí môi giới TB/căn** và **booking→HĐMB %** (user chưa điền, §6). Không có số này thì mọi kill rule/gate là đoán |
| G2 (Demand Gen RMKT) | ⛔ **bất khả thi ở bậc 30tr** | Cần ≥1.000 user/30 ngày vào `xem_bang_gia`/`engaged_60s`. Toàn bộ traffic ads = **933 click/tháng** → kể cả 100% cũng <1.000. → 10% quỹ remarketing (100k/ngày #1 đang mượn) **giữ nguyên chỗ mượn**; muốn mở G2 phải có organic/`content/` bơm thêm, không phải chờ |
| G3 (Search T3) | ⛔ | Cần G2 đã chạy |
| G4 (PMax) | ⛔ | Cần **ECL chạy thật** — đang chặn ở quyền Keap (`PLAN.md` §6.6) + credentials Data Manager API |
| G5 (YouTube) | ⛔ | Cần ≥150tr/tháng + G4 ổn 6 tuần + media plan Reach Planner |
| Discovery broad (#7) | ⛔ vẫn hoãn | Bắt buộc tCPA; chưa tới bậc 2 (`journey-plan` §3.2) |

**3 bài học**

1. **Cấu trúc doc ≠ cấu trúc chạy được — phải đối chiếu với bộ keyword thật trước khi dựng.** `#4 TaiChinh` và `#8 NhaOXaHoi` có ngân sách trong §2.1 nhưng **0 keyword đủ điều kiện** cho dự án này (tài chính Bến Lức/Long An toàn bộ `uu_tien=2`). Dựng campaign rỗng = 100k/ngày nằm chết. Bước thiếu trong `campaign-setup.md` §2.1: chạy script §2.4 **trước** khi chốt bảng ngân sách, không phải sau.
2. **Search terms report đầy term đã có trong negative list là tín hiệu lỗi CẤU HÌNH, không phải tín hiệu thiếu negative.** Phản xạ "thấy term rác → append negative" ở đây sẽ thêm dòng trùng, báo cáo "đã xử lý", và để nguyên nguồn thật (broad im lặng / list dán sai chỗ / auto-apply xoá negative) tiếp tục đốt tiền ở mọi truy vấn khác. Chẩn đoán 3 giả thuyết mất 15 phút; sửa sai chỗ mất 15% ngân sách 2 tuần.
3. **Ở 30tr₫/tháng với CPC 30k, thứ khoá mọi cửa là dữ liệu conversion, không phải tiền.** 933 click/tháng làm G2 bất khả thi bằng toán học, và G1 không đánh giá được vì thiếu 2 con số kinh doanh của user. Đòn bẩy duy nhất còn lại trong kỳ là **ECL** (`journey-plan` §3.2: "ECL không phải việc của tuần 8 — nó là điều kiện tiên quyết của toàn bộ nhánh AI"). Ưu tiên tháng 2 vì vậy là: (1) thoả thuận gắn tag Keap + SLA gọi <5′, (2) credentials Data Manager API, (3) bổ 3 keyword brand còn thiếu — **không** phải mở campaign type mới.
