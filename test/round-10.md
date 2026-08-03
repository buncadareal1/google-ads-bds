# Round 10 — Bid war brand 30tr (Eco Retreat, Bến Lức)

Kịch bản: 30tr₫/tháng (1tr/ngày), 1 dự án phân phối = **Eco Retreat** (Ecopark/DB Invest, Thanh Phú, Bến Lức, Long An), **CPC nền 30k₫**.
Sự kiện tiêm tuần 2: 2 sàn F2 bắt đầu bid `eco retreat` → CPC nhóm brand ×2 (30k → 60k), brand IS 85% → 55%, 1 sàn để tên `Eco Retreat` trong headline của họ.

**Mô hình số (mọi con số dưới đây suy ra từ đây, không có số nào ngoài mô hình):**

| Tham số | Giá trị | Nguồn |
|---|---|---|
| Click/tuần mỗi campaign | `ngân sách tuần / CPC` (không phạt click rác — negative list 386 dòng import ngày 1) | sim-rules §Công thức |
| CVR LP | **4,8%** = 2,0 nền +1,0 message match ≥4/5 +0,8 bảng giá above the fold +0,6 Zalo sticky/click-to-call +0,4 form 4 field & 2 dropdown. LP riêng (không homepage) → không ×0,4. **Đây là trần khả thi của bảng adder** (6,0 không đạt được bằng 4 mục có sẵn) | sim-rules + `landing-page/README.md` |
| Qualify rate | **40%** (form có 2 dropdown) | sim-rules |
| Contact rate | **55%** (có 2 dropdown + validate đầu số VN + SLA gọi <5' trong giờ trực máy 05:00–24:00) | sim-rules · `campaign-setup.md` §3.4 |
| CPL-q suy ra | `CPC / (4,8% × 40%)` = **CPC / 0,0192** → 30k ⇒ 1,563tr · 42k ⇒ 2,19tr · 47k ⇒ 2,45tr · 60k ⇒ 3,13tr | dẫn xuất |
| **[GIẢ ĐỊNH MÔ HÌNH — không có công thức trong sim-rules cho IS]** | (a) giá thanh toán phiên đấu brand sau sự kiện = **60k**; CPC thực = `min(cap, 60k)` — tính **chặn trên**: áp cap cho toàn bộ click #1, dù tail không bị tranh nên thực tế rẻ hơn. (b) IS brand nội suy tuyến tính giữa 2 mốc đề bài cho: cap 35k → 55%, cap 60k → 85% ⇒ `IS = 55% + (cap−35k)/25k × 30đv`. (c) Tổng click brand khả dụng ở IS 100% = **18,6 click/ngày** (suy từ tuần 1: 110,8 click/tuần ở IS 85%). Click thực = `min(ngân sách/CPC, 18,6 × IS)` | ghi rõ là giả định, không phải fact |
| Giả định khác | 4 tuần **không** trùng Tết/tháng 7 âm (sim không mô hình mùa vụ; nếu trùng → xử theo `research` §4, không tự cắt ngân sách giữa bid war) | |

---

## Setup tuần 0 (quyết định + căn cứ doc)

**Pre-flight (`campaign-setup.md` §1):** advertiser verification nộp trước (D-7, chờ 3-5 ngày) · 6 conversion action theo thang 1/1/1/10/50/500 + goal **category** chuẩn (§1.2.7) + cửa sổ chuyển đổi **90 ngày** · GA4↔Ads link + auto-tagging ON · **386 negative account-level** (tự phủ mọi campaign type) + shared list 80 dòng campaign-level · **11 ô §1.5** (Search Partners OFF, Display OFF, location = **Presence**, ACA OFF, auto-apply recommendations **TẮT HẾT**, lịch 05:00–24:00, tracking template UTM, không dùng ngân sách chung).
**G0 (`journey-plan` §3.1):** 1 lead thật đi hết LP → GA4 → Ads → Keap có `gclid`. Trống = không bật quảng cáo.

**Cấu trúc (30tr = 1 khối Search, `research` §1 + `journey-plan` §3):**

| # | Campaign | ₫/ngày | Cap CPC | Ad group / keyword |
|---|---|---|---|---|
| 1 | `BDS_Search_Brand_DuAn` | **475.000** | **35.000** | `brand-eco-retreat` — **20 kw** (4 exact head: `eco retreat`, `+ giá`, `+ bảng giá`, `+ mở bán`; 16 phrase) |
| 2 | `BDS_Search_Brand_CDT` | **75.000** | **35.000** | `brand-cdt--ecopark` — 5 kw `uu_tien` 1 (khách gõ "ecopark long an") |
| 3 | `BDS_Search_KhuVuc_GiaoDich` | **450.000** | **40.000** | `ben-luc--gia-bang-gia` (15 kw) + `ben-luc--mua-ban` (5 kw) |
| — | #4 TaiChinh, #8 NOXH, #7 Discovery, RMKT | **0** | — | xem 3 lệch dưới |
| | **Tổng** | **1.000.000** | | |

**3 lệch so với `campaign-setup.md` §2.1-2.3 — có lý do, không phải ứng biến:**
1. **Cap brand 35k (doc ghi 20k) và cap #3 40k (doc 35k):** doc neo vào dải CPC 15/25/40k của `research` §2; đề bài đặt CPC nền **30k** → neo lại theo dải mới, giữ nguyên nguyên lý "brand thấp hơn generic một bậc" (brand QS cao → CPC thực rẻ hơn cap).
2. **#8 NOXH = 0 và #4 TaiChinh = 0, dồn 100k vào #3:** Eco Retreat không phải NOXH (doc cho phép dồn vào #3); `ben-luc--tai-chinh` chỉ có **2 kw `uu_tien` 2** → không thể đạt ngưỡng ≥10 conv/ad group (§2.3) → không dựng campaign 1 người. Nhu cầu trả góp đi bằng kw `eco retreat trả góp`/`lãi suất` trong #1 + sitelink `#tra-gop` (§3.4).
3. **#1 bật cả `uu_tien` 1+2 của `brand-eco-retreat` (20/22 kw), tắt 2 kw `tiến độ xây dựng` + `bàn giao khi nào`:** `journey-plan` §3 ghi 30tr = `uu_tien` 1, nhưng mục đích của bộ lọc đó là **giới hạn số dự án** — ở đây chỉ có 1 dự án. `keywords/journey-strategy.md` §1.1 chỉ định rõ 2 kw kia **tắt ở kịch bản 30tr** (khách đã mua, không tạo lead mới) và xếp `mặt bằng/nhà mẫu/trả góp/chiết khấu/review` vào diện **Search**.

**Bidding khởi điểm:** tất cả **Maximize Clicks + bid cap** (`research` §4 — tuần 1-3 không smart bidding; `journey-plan` §3.2 bậc 0: 0 conversion thì mọi thứ "AI" học từ hư không). **Không** tCPA, **không** broad, **không** PMax/Demand Gen/YouTube/AI Max/lead form asset.
**Conversion primary ngày 1:** `Lead_Form_Raw` + `Click_Hotline` + `Click_Zalo`; `phone_click`/`zalo_click` là **Secondary vĩnh viễn** khi ECL chạy (`tracking/README.md` luật #2).

**LP spec (điều kiện của CVR 4,8% — `research/competitors/2026-07-eco-retreat.md` Action 2-4):** H1 pin = `Eco Retreat – Bảng Giá 07/2026` khớp headline RSA · hero có **"từ 2,5 tỷ"** + block định lượng **25% đến khi nhận nhà · vay 70% · miễn gốc lãi 24 tháng · CK tới 12% khi TT sớm 95%** (số đang bị giấu ở site sàn F2, không có trên `ecoretreat.vn`) · block objection **bàn giao Q2/2028** (ảnh công trường có tháng + "24 tháng ân hạn phủ gần trọn thời gian chờ") · form 4 field + dropdown Ngân sách (`<3` / `3-5` / `5-10` / `>10 tỷ`) + Mục đích (ở / đầu tư / second home) · Zalo sticky + `tel:` · 6 event registry · footer pháp nhân + MST + **1 dòng "đơn vị phân phối, không phải chủ đầu tư"** — thiếu dòng này thì **bỏ headline `Giá Gốc CĐT`** (mạo nhận CĐT = đình chỉ tài khoản ngay, `research` §7).

---

## Nhật ký tuần 1-4

| Tuần | Chi tiêu | Click | Lead raw | Lead qualified | **Contact rate** | CPL-q | Sự kiện | Hành động + căn cứ |
|---|---|---|---|---|---|---|---|---|
| **1** | 7.000k | 233,3 | 11,2 | 4,5 | **55%** (6,2 contactable) | **1.563k** | — | Tuần 1 **không đổi** cap/ngân sách/RSA/keyword (`campaign-setup` §4.1). Chỉ: D+0 kiểm ad đã duyệt · D+1 lead có `gclid` · D+3 negative cho term sai ngành. Brand IS 85%, cả 3 campaign tiêu hết ngân sách |
| **2** | 6.767k (**hụt 233k**) | 199,5 | 9,6 | 3,8 | **55%** (5,3) | **1.766k** | **F2 vào đấu giá**: brand CPC ×2 (→60k), IS 85%→55% | Guard 🟡 `CPC brand >2× baseline 7 ngày` bắn (D2, `monitoring.md` §2) → **xác minh trước, không tăng bid ngay** (PLAYBOOK 2.3: nâng QS rẻ hơn nâng bid): Auction Insights **cấp keyword** nhóm brand + đọc 3 cột QS + cột `Lượt nhấp không hợp lệ` (<10% là bình thường, `research` §5) + Transparency Center bằng **browser thật**. D3: cap 35k→**42k** (+20%, `campaign-setup` §2.2, điều kiện đúng: IS lost **rank** 45% VÀ chưa tiêu hết ngân sách). **KHÔNG đổi ngân sách tuần này** — §2.2: hụt IS do rank thì không phải vấn đề ngân sách; và giữ nguyên tắc **1 thay đổi/lần** |
| **3** | 6.793k | 185,0 | 8,9 | 3,6 | **55%** (4,9) | **1.912k** | Bid war duy trì; 1 sàn F2 vẫn để `Eco Retreat` trong headline | D1: #1 475k→**565k (+18,9%)**, lấy từ #3 450k→**360k (−20%)** — mỗi campaign đổi **1 lần ≤20%** (không learning reset). D4: cap 42k→**47k** (+11,9%, sau khi #1 lại hụt IS rank ở mức ngân sách mới). **DỪNG leo thang ở 47k** — xem §Trần bid dưới. Cùng tuần (§4.1 tuần 3): thêm **RSA thứ 2** đổi 1 biến = trục phản công `Ân Hạn Gốc & Lãi 24 Tháng` / `Chiết Khấu Đến 12%` (nâng expected CTR = đòn bẩy CPC không tốn tiền); gửi hồ sơ khiếu nại nhãn hiệu cho CĐT (§Trademark) |
| **4** | 7.000k | 185,6 | 8,9 | 3,6 | **55%** (4,9) | **1.964k** | Trạng thái ổn định: brand CPC 47k, IS **64%** | **Giữ nguyên, không đụng gì** (§4.1 tuần 4 = đo, không sửa): CVR LP thật đã ở trần mô hình 4,8% → không còn đòn bẩy CVR trong sim · rà gate: **không mở gate nào** (§Gate cuối kỳ) · giữ **Max Clicks** dù 38,6 conv/30 ngày ≥30, vì `journey-plan` §3.2 bậc 1 buộc **đảo primary sang `Lead_Contactable` TRƯỚC** khi bật smart bidding, mà ECL chưa chạy (thiếu credentials + SLA gắn tag Keap còn treo, `PLAN.md` §6.6) |

**Chi tiết số #1 (campaign bị tấn công):** T1 110,8 click @30k · T2 20,5 click @35k (2 ngày) + 56,5 @42k (5 ngày) = 77,0 click / 3.092k · T3 35,4 @42k (3 ngày, còn hụt 69k/ngày) + 48,1 @47k (4 ngày) = 83,5 click / 3.748k · T4 84,1 @47k / 3.955k. IS brand: 85% → 55-60% → 64-69% → **64%** (hụt: ~31 điểm do rank, ~5 điểm do ngân sách).

### Xử lý sự kiện — 4 quyết định

**1. Exact giữ nhà.** Giữ 4 head term ở **exact** (`eco retreat`, `+ giá`, `+ bảng giá`, `+ mở bán`) — `research` §3: tên dự án LUÔN exact. Không nới sang broad, không bật AI Max để "mở rộng phòng thủ": broad cần Smart Bidding theo chính điều kiện của Google, AI Max **không chạy với Max Clicks** (`campaign-setup` §5.6). Không tách 4 head term ra campaign riêng để bid cao hơn: cap là **trần**, không phải bid — tail không bị tranh vẫn thanh toán ~30k, nên một lần nâng cap đã tự phân biệt head/tail. (Bỏ qua: split campaign + Manual CPC keyword-level; thêm khi CPC tail thực sự tăng.)

**2. Trần bid — vì sao dừng ở 47k, không match 60k.** Số học của mô hình:

| Cap | IS trần theo rank | Click/ngày mua được với 565k | Ràng buộc thực | CPL-q của #1 |
|---|---|---|---|---|
| 35k | 55% | 16,1 | rank → 10,2 click | 1,82tr |
| 42k | 63% | 13,5 | rank → 11,8 | 2,19tr |
| **47k** | **69%** | **12,0** | **ngân sách → 12,0** | **2,45tr** |
| 60k | 85% | 9,4 | ngân sách → **9,4 (ít hơn!)** | 3,13tr |

→ **Với ngân sách cố định, nâng cap quá điểm ngân sách bắt đầu chặn thì IS TỤT, không tăng** (60k cho 9,4 click = IS 51%, thấp hơn cả 55% lúc bị tấn công). Đúng luật `campaign-setup` §2.2: "tiêu hết ngân sách mà cap chưa chạm → không tăng cap, đó là vấn đề ngân sách". Muốn giữ IS 85% ở giá 60k cần **18,6 × 85% × 60k = 950k/ngày = 95% ngân sách toàn tài khoản** (bỏ hết generic khu vực) → không khả thi ở 30tr. Vì vậy: nâng cap **chỉ tới điểm campaign vừa tiêu hết ngân sách**, tăng ngân sách **±20%/lần** và mỗi bước kiểm lại CPL-q, dừng khi CPL-q của nhánh brand vượt xa mốc tham chiếu 1,56tr (`research` §2, kịch bản "trung bình" — **mốc tham chiếu, không phải target**; CPL target thật cần phí môi giới/căn + tỷ lệ booking→HĐMB mà user chưa điền, `journey-plan` §4/§6).
**Đã cân nhắc và LOẠI: `Target impression share`.** Nó là công cụ sách vở cho phòng thủ brand, nhưng nó đuổi IS bất chấp giá → ở 30tr nghĩa là nuốt 100%+ ngân sách tài khoản (số trên) và bỏ luôn 20 kw generic khu vực. Ngoài gate bidding của hệ (`journey-plan` §3.2).

**3. Transparency Center + hồ sơ khiếu nại (PLAYBOOK 2.1 + 4.4, `research` §7).**
- Tra bằng **browser thật** (`adstransparency.google.com/?region=VN&domain=<domain>`, Region = Vietnam, 30 ngày, Format = Text) — WebFetch trả **JS shell rỗng**, đã kiểm ở vòng competitor 2026-07. Danh sách domain cần tra có sẵn: `ecoretreatlongan.vn`, `ecoretreat.city`, `ecopark-longan.com`, `ecoretreatland.vn`, `ecoretreat.online`, `ecoretreatlongan.info.vn` (đều ở trang 1 SERP tên dự án). Lấy: headline lặp nhiều nhất, con số offer, ngày first-shown, có chạy Display/Video hay chỉ Search. Không mở được browser → ghi **"không xác minh được"**, không đoán ad copy.
- **Điều kiện khiếu nại nhãn hiệu — và vị thế F1 của mình:**
  | Câu hỏi | Trả lời |
  |---|---|
  | Cơ chế | **Complaint-driven từ 2/2025** — không có chặn tự động; không ai khiếu nại thì ad cứ chạy (`research` §7) |
  | Phạm vi hiệu lực | Chỉ chặn được **tên trong ad text** (headline/description/path/sitelink/callout/business name). **Không** chặn được việc họ **bid keyword** `eco retreat` — bid tên là **được phép** (PLAYBOOK 4.4). ⇒ Khiếu nại thắng vẫn **không** trả lại CPC cũ, chỉ hạ CTR của họ |
  | Ai được gửi | **Chủ sở hữu nhãn hiệu**, hoặc đại diện **có văn bản uỷ quyền**. Mình là **sàn F1 phân phối** ⇒ **KHÔNG tự gửi được** — phải có uỷ quyền văn bản từ **liên danh DB Invest – Ecopark**, hoặc để CĐT tự gửi |
  | Rủi ro bị từ chối | Nếu sàn F2 đó cũng là **nhà phân phối hợp pháp** và không mạo nhận là CĐT thì ngoại lệ reseller có thể bảo vệ họ (PLAYBOOK 4.4 — đây là vùng xám). Khiếu nại kiểu này hay bị bác |
  | Đường mạnh hơn | Nếu LP/ad của họ **mạo nhận là chủ đầu tư** ("giá gốc CĐT" mà không khai là đơn vị phân phối) → đó là **misrepresentation / unacceptable business practices** = đình chỉ tài khoản ngay, nặng hơn hẳn khiếu nại nhãn hiệu (`research` §7). Cần bằng chứng: screenshot Transparency Center + ảnh LP đích + URL |
  | ⚠️ Chưa xác minh | Nguyên văn form + hồ sơ Google yêu cầu **không có nguồn trong repo** → khi làm thật phải đọc trang policy trademark và **lưu văn bản trả lời của Google**, không coi bảng này là fact |
- **Đòn rẻ nhất, làm song song:** yêu cầu CĐT (a) gửi khiếu nại/uỷ quyền, (b) siết **chính sách phân phối** — cấm F2 bid brand là điều khoản hợp đồng, không phải việc của Google Ads. Đây là cách duy nhất hạ giá phiên đấu mà không tốn tiền.
- **Tuyệt đối không làm:** đưa tên 2 sàn F2 (hoặc tên đối thủ Waterpoint/LA Home) vào ad text của mình — **không ngoại lệ** (journey-strategy §3.3). Đánh vào thuộc tính: `Ân Hạn Gốc & Lãi 24 Tháng`, `Chiết Khấu Đến 12%`, `Chỉ 25% Đến Khi Nhận Nhà`.

**4. BẪY — KHÔNG mở campaign bid tên đối thủ.** `keywords/journey-strategy.md` §3.1 đòi **cả 4** điều kiện; hiện fail 2:

| # | Điều kiện | Thực tế cuối kỳ | Kết luận |
|---|---|---|---|
| 1 | Brand IS **≥90%** | **64%** | ❌ FAIL — "đừng bid tên đối thủ khi brand mình còn hở, đó là đổi lead rẻ lấy lead đắt" |
| 2 | Đối thủ đắt hơn / bàn giao chậm hơn rõ rệt | **Ngược lại**: LA Home 2,99 tỷ (−48%) và bàn giao Q4/2026; Waterpoint đã có >500 hộ ở, mình Q2/2028 | ❌ FAIL — mình đang **thua** trục này, bid tên họ là mời khách so sánh ở nơi mình yếu |
| 3 | Có LP so sánh tử tế | Chưa có (bài so sánh mới là đề xuất Action 3) | ❌ chưa đủ |
| 4 | Đủ ngân sách sau khi #1 đạt IS ≥90% (kịch bản ≥60tr) | 30tr, #1 còn đang hụt IS | ❌ FAIL |

Số học củng cố: nhánh brand đã 47k CPC (CPL-q 2,45tr), tệp tên đối thủ có contact rate **thấp hơn brand** (journey-strategy §3.1) → mở nó là làm CPL-q toàn tài khoản xấu thêm để đổi lấy lead kém hơn. **Quyết định: đóng, xét lại khi brand IS ≥90% ổn định 30 ngày.**

---

## Tổng kết

| Chỉ số (4 tuần = 28 ngày) | Giá trị |
|---|---|
| Chi tiêu | **27.560k₫** (còn 233k hụt tuần 2 do IS lost rank, không thu hồi được) |
| Click | 803,5 · **CPC blended 34,3k** (nền 30k) |
| **Contact rate** (báo trước CPL) | **55%** — 21,2 lead contactable / 38,6 raw |
| Lead raw | **38,6** · Lead qualified **15,4** |
| CPL raw | 715k |
| **CPL qualified** | **1.786k** (mốc tham chiếu kịch bản trung bình 1,56tr → **+14%**; tuần 1 trước bid war đúng 1.563k, tuần 4 đã 1.964k) |
| CTR | **[GIẢ ĐỊNH]** blended ~5,5% ⇒ ~14.600 impression. Neo vào WordStream 2026 real estate **7,61% (Mỹ)**, hạ xuống vì mix có generic khu vực. Không có benchmark CTR BĐS VN đáng tin — không dùng số này làm KPI (`research` §2) |
| Brand IS | 85% → **64%** |

**Trạng thái gate cuối kỳ (`journey-plan` §3.1):**

| Gate | Trạng thái | Lý do bằng số |
|---|---|---|
| G0 | ✅ đạt (điều kiện bật quảng cáo) | lead test có `gclid`, negative account-level, Presence, Partners/Display OFF |
| G1 (mở rộng T2) | ❌ | CPL chưa ≤ target 30 ngày liên tiếp — **chưa có target** (thiếu phí môi giới/căn từ user); và brand IS đang hở |
| G2 (Remarketing Demand Gen) | ❌ **bất khả thi ở 30tr tháng này** | cần audience ≥**1.000 user**/30 ngày; cả tài khoản chỉ có **803,5 click**/28 ngày → kể cả 100% click cũng không đủ |
| G3 / G4 / G5 | ❌ | phụ thuộc G2 / ECL chạy thật / ≥150tr |
| Bidding | **giữ Max Clicks + cap** | 38,6 conv/30 ngày ≥30 nhưng conv là **form raw**; §3.2 bậc 1 buộc đảo primary sang `Lead_Contactable` trước, ECL chưa chạy → bật smart bidding bây giờ = dạy nó mua form rẻ |
| Campaign tên đối thủ | ❌ đóng | brand IS 64% < 90% (2/4 điều kiện fail) |

**3 bài học**

1. **Ngân sách cố định thì tăng bid không mua lại được Impression Share — nó đổi click lấy vị trí.** Match đủ giá mới (60k) cho 9,4 click/ngày = IS 51%, *thấp hơn* mức 55% lúc bị tấn công. Luật thực thi rút ra: **nâng cap chỉ tới điểm campaign vừa tiêu hết ngân sách; muốn IS cao hơn thì phải tăng ngân sách (±20%/lần) và mỗi bước kiểm lại CPL-q.** Giữ IS 85% ở giá 60k cần 950k/ngày = 95% ngân sách toàn tài khoản, tức phải xoá sạch 20 kw generic khu vực.
2. **Khi CPC bị đẩy ×2 mà CVR đã ở trần (4,8%), đòn bẩy còn lại không phải tiền:** (a) gỡ ad dùng tên mình bằng khiếu nại nhãn hiệu/misrepresentation — nhưng **F1 không tự gửi được, phải có uỷ quyền CĐT**, và thắng cũng chỉ gỡ được *tên trong ad text*, không chặn được việc họ bid keyword; (b) nâng expected CTR/ad relevance/LP experience (rẻ hơn nâng bid, PLAYBOOK 2.3); (c) siết chính sách phân phối của CĐT — đòn duy nhất hạ giá phiên đấu mà không tốn đồng nào; (d) **generic khu vực `ben-luc--*` không bị tấn công → là hedge tự nhiên, đừng rút cạn nó để nuôi brand** (tuần 3 chỉ rút đúng −20%, một lần).
3. **Brand IS hở là lệnh cấm phản công, không phải lời khuyên.** Bid tên sàn/đối thủ khi IS 64% fail 2/4 điều kiện journey-strategy §3.1, và ở đây còn fail điều kiện #2 theo hướng tệ nhất: Eco Retreat đang **thua** trục giá (LA Home 2,99 tỷ) và trục bàn giao (Waterpoint đã có cư dân, mình Q2/2028) — bid tên họ là chủ động mời khách so sánh ở đúng chỗ mình yếu. Việc đúng thứ tự: sửa nhà mình trước (đưa con số chính sách + objection bàn giao lên LP), giành lại IS, rồi mới nói tới tệp đối thủ.

**Nợ lại cho vòng sau:** target CPL thật (cần phí môi giới/căn + booking→HĐMB, `journey-plan` §6) · nguyên văn điều kiện form khiếu nại trademark của Google · ad copy thật của 2 sàn F2 (cần browser) · SLA gắn tag Keap cho ECL (`PLAN.md` §6.6) — không có nó thì hệ **kẹt ở bậc 0 bidding vĩnh viễn** bất kể chi bao nhiêu.
