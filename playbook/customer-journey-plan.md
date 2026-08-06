# Kế hoạch Google Ads theo hành trình khách hàng — BĐS VN

Chu kỳ cân nhắc 3–12 tháng. Tài liệu này map **giai đoạn hành trình → chiến thuật Ads → ngân sách → KPI → nhịp vận hành**.

**Nguồn:** skills `ads` (intent ladder, kill rules, breakeven, scaling quadrant), `google-ads` + `google-ads-manager` (bidding theo volume, QS, RSA), `marketing-psychology`, `offers` (value equation, 6 thành phần offer, scarcity thật), `cro`, `attribution`. Dữ liệu keyword: `keywords/master-keywords.csv` + `keywords/adgroup-map.md`.

**Quy ước số:** mọi con số chưa có dữ liệu account ghi `[điền từ research/tuần chạy đầu]`. Không dùng benchmark ngoại suy.

---

## 0. Hai trục dễ nhầm: intent tier ≠ giai đoạn hành trình

`intent_tier` trong `keywords/` quyết định **keyword ở campaign nào**. Modifier của truy vấn quyết định **khách đang ở giai đoạn nào**. Một keyword `T1_brand_du_an` vẫn có thể là khách giai đoạn 3.

| intent_tier (`keywords/`) | Tier theo quy ước hội thoại | Campaign (`adgroup-map.md`) |
|---|---|---|
| `T1_brand_du_an`, `T1_brand_cdt` | Tier 1 — quyết định | #1, #2 |
| `T2_giao_dich` | Tier 2 — so sánh/giao dịch | #3, #4, #7, #8 |
| `T3_nghien_cuu` | Tier 3 — tìm hiểu | #5, #6 |

**Modifier phân giai đoạn** (bộ 22 modifier brand có sẵn trong master list):

| Giai đoạn | Modifier brand tương ứng |
|---|---|
| Nghiên cứu | `pháp lý`, `chủ đầu tư`, `vị trí`, `tiến độ xây dựng`, `bàn giao khi nào` |
| So sánh | `có nên mua`, `review`, `đánh giá`, `giá bao nhiêu`, `tiện ích`, `mặt bằng` |
| Quyết định | `(tên trần)`, `bảng giá`, `giá`, `mua`, `mở bán`, `chính sách bán hàng`, `chiết khấu`, `nhà mẫu`, `trả góp`, `lãi suất`, `tiến độ thanh toán` |

→ Hệ quả vận hành: **tách RSA + LP block theo modifier, không tách theo tier.** Bảng message match trong `adgroup-map.md` đã làm việc này.

---

## 1. Hành trình khách mua BĐS VN

| # | Giai đoạn | Thời lượng điển hình | Tâm lý & câu hỏi trong đầu | Mental model áp dụng (`marketing-psychology`) |
|---|---|---|---|---|
| 1 | **Nhận biết** | Tuần 0 – tháng 2 | "Có nên mua nhà lúc này không? Tiền mình mua được gì?" Chưa có dự án nào trong đầu, chỉ có nhu cầu/nỗi lo (giá lên, con vào lớp 1, tiền để không mất giá). | Mere exposure · Availability heuristic · Mental accounting ("từ X tr/tháng" thay vì tổng tiền) |
| 2 | **Tìm hiểu / Nghiên cứu** | Tháng 1 – 4 | "Khu này có dự án gì? Pháp lý sao? CĐT này có uy tín không? Bao giờ bàn giao?" Bắt đầu lập shortlist 3–8 dự án. | Authority bias (CĐT, pháp lý) · Reciprocity (cho bảng giá/brochure trước) · Curse of knowledge (giải thích đơn giản) |
| 3 | **So sánh / Cân nhắc** | Tháng 2 – 8 | "Dự án A vs B cái nào hơn? Giá/m² có hợp lý? Vay được bao nhiêu, trả bao nhiêu/tháng? Có nên mua không?" | **Anchoring** (bảng giá: giá gốc → giá sau CK) · Contrast effect · Paradox of choice (chỉ 3 loại căn) · Regret aversion · Rule of 7 (cần ~7 chạm) |
| 4 | **Quyết định / Liên hệ** | Tháng 3 – 10 | "Còn căn nào view đó không? Chính sách đợt này thế nào? Ai bán? Gọi ai?" Đã chọn dự án, đang chọn căn và chọn người bán. | **Loss aversion** (số căn còn thật, đợt mở bán thật) · Scarcity/urgency **thật** · Default effect · Activation energy thấp (form 3 field) |
| 5 | **Sau lead → booking/giữ chỗ** | Ngày 0 – 90 sau lead | "Đặt cọc rồi có rút được không? Ký gì? Có bị ép không?" Sợ mất tiền hơn sợ mất căn. | Commitment & consistency (giữ chỗ = cam kết nhỏ → HĐMB) · Endowment effect ("căn của anh/chị") · Goal-gradient · Peak-end rule |

### Truy vấn đặc trưng theo giai đoạn (mẫu thật từ `master-keywords.csv`)

| Giai đoạn | Mẫu truy vấn | `intent_tier` | `nhom_adgroup` chủ đề | `uu_tien` |
|---|---|---|---|---|
| 1. Nhận biết | `có nên mua căn hộ hồ chí minh`, `đầu tư căn hộ dòng tiền` | `T3_nghien_cuu` | `tu-van-quyet-dinh`, `dau-tu` | 3 |
| 2. Tìm hiểu | `căn hộ quận 4 pháp lý`, `căn hộ hưng yên tiến độ`, `kiểm tra quy hoạch đất`, `<CĐT> dự án` | `T3_nghien_cuu`, `T1_brand_cdt` | `phap-ly`, `tien-do`, `brand-cdt--*` | 2–3 |
| 3. So sánh | `căn hộ hóc môn bảng giá`, `chung cư văn giang giá bao nhiêu`, `<dự án> có nên mua`, `<dự án> review`, `căn hộ 2pn dưới 3 tỷ` | `T2_giao_dich` + brand modifier so sánh | `*--gia-bang-gia`, `phan-khuc-ngan-sach`, `cau-hinh-can`, `tai-chinh` | 1–2 |
| 4. Quyết định | `<tên dự án>`, `<dự án> bảng giá`, `<dự án> chính sách bán hàng`, `<dự án> nhà mẫu`, `mua căn hộ đồng nai`, `căn hộ quận 7 mở bán` | `T1_brand_du_an`, `T2_giao_dich` | `brand-<slug>`, `*--mua-ban`, `*--mo-ban-moi` | 1 |
| 5. Sau lead | *(không có truy vấn — 100% remarketing/CRM)* | — | — | — |

---

## 2. Map giai đoạn → chiến thuật Google Ads

### 2.1 Campaign & audience

| Giai đoạn | Campaign type | Campaign (`adgroup-map.md`) | Audience / remarketing list |
|---|---|---|---|
| 1. Nhận biết | Search T3 (Max Clicks, CPC trần) · YouTube (chỉ dự án lớn, xem gate 5) | #6 `NghienCuu` | In-market: Residential Properties (chỉ làm **observation**, không target ở ngân sách nhỏ) |
| 2. Tìm hiểu | Search T3 + brand CĐT | #5 `PhapLy_TienDo`, #2 `Brand_CDT` | GA4: `all_visitors_30d` (nguồn nuôi list) |
| 3. So sánh | Search T2 (chủ lực) · Display remarketing | #3 `KhuVuc_GiaoDich`, #4 `TaiChinh`, #8 `NhaOXaHoi` | GA4: **`xem_bang_gia`** · **`xem_mat_bang`** · **`engaged_60s`** |
| 4. Quyết định | Search T1 brand (chủ lực) · Demand Gen remarketing | #1 `Brand_DuAn`, #7 `Discovery` | GA4: `form_start_khong_submit` · `xem_bang_gia_7d` (nóng) · **loại trừ** `da_generate_lead_14d` |
| 5. Sau lead | Demand Gen customer match · **không** Search | — | Customer Match từ CRM: `lead_chua_booking`, `lead_qualified_chua_di_xem` — ⚠️ **đọc chặn dưới trước khi lập kế hoạch** |

> ⛔ **CHẶN GĐ5 (mới, 2026-07-28): Customer Match ở quy mô hệ chỉ EXCLUDE được, chưa TARGET được.**
> [Customer Match policy](https://support.google.com/google-ads/answer/6299717?hl=en): mở `Targeting` (target thật + bid adjustment) cần **90 ngày history + >$50.000 USD lifetime spend**. Dưới ngưỡng: chỉ được dùng `Observation` và `Exclusions`. Hệ ở 30tr₫/tháng (~$1.100) → **nhiều năm mới tới $50k**.
> **Hệ quả cho kế hoạch GĐ5:** chiến thuật "Demand Gen remarketing tới `lead_chua_booking` bằng Customer Match" **chưa chạy được**. Cái chạy được ngay và có giá trị thật:
> 1. **Exclusion** — dùng list khách đã mua/đã cọc để **loại khỏi mọi campaign acquisition**. Đây là việc đáng làm nhất và không bị ngưỡng chặn.
> 2. **Observation** — gắn list để đọc chênh CVR, không đổi phân phối.
> 3. Remarketing GĐ5 thật thì đi bằng **audience GA4** (`da_generate_lead_14d` và bạn của nó), không bằng Customer Match.
> Yêu cầu khác vẫn phải thoả: privacy policy phải nói rõ **có chia sẻ dữ liệu khách với bên thứ 3**, list cần **≥100 thành viên** cập nhật trong 540 ngày, membership tối đa **540 ngày**. Chi tiết + đường upload: `research/google-official-curriculum.md` §E5, §F6.
>
> **Cách làm Exclusion — đã xác nhận (vòng 3, 2026-07-28,** [About Exclusions](https://support.google.com/google-ads/answer/2549058?hl=en)**):** `Audiences` → mục `Exclusions` → drop-down **`Exclude from`** = `Campaign` hoặc `Ad group` → tick list → **`Save Audience Segment Exclusions`**. Hỗ trợ ở "Search, Display, Demand Gen, Standard Shopping, Video, and **Performance Max**".
> 🚨 **Bẫy thực thi:** "Audience exclusions **aren't available during campaign creation**, but you can add exclusions to an existing campaign." → Exclusion là **bước sau Publish**, không có ô trong luồng tạo campaign. Ai dựng campaign mà không biết điều này sẽ tưởng tính năng không tồn tại và bỏ qua. Đã ghi vào `playbook/campaign-setup.md` §5.5.
> **Khả dụng tại VN: ĐÓNG — không xác nhận được bằng tài liệu.** Vòng 3 đọc lại [Customer Match policy](https://support.google.com/google-ads/answer/6299717?hl=en) và [trang upload data file](https://support.google.com/google-ads/answer/10589050?hl=en): **Google không publish danh sách quốc gia** cho Customer Match. → Không phải "chưa research đủ", mà là **không có nguồn để research**. Cách duy nhất biết: mở `Tools → Audience manager` trong tài khoản thật xem có `Customer list` hay không. Đừng lên kế hoạch phụ thuộc trước khi kiểm.

**Định nghĩa GA4 audience** (điều kiện — hành vi, không phải trang):

| Audience | Điều kiện | Window |
|---|---|---|
| `xem_bang_gia` | scroll tới section bảng giá HOẶC click tab bảng giá | 30 ngày |
| `xem_mat_bang` | xem section mặt bằng ≥ 1 lần | 30 ngày |
| `engaged_60s` | `user_engagement` ≥ 60s trên LP dự án | 30 ngày |
| `form_start_khong_submit` | có `form_start`, không có `generate_lead` | 7 ngày |
| `da_generate_lead_14d` | có `generate_lead` — **dùng để exclude** | 14 ngày |

> ✅ **Đã giải toả (QA 2026-07-28).** Cả 6 event đã vào registry `CLAUDE.md` và có spec trong `tracking/gtm-container-spec.md`: `generate_lead`, `phone_click`, `zalo_click`, `xem_bang_gia`, `xem_mat_bang`, `form_start`. LP không cần fallback.

### 2.2 Thông điệp, offer, landing page

Áp dụng `offers`: mỗi offer phải đủ 6 thành phần (deliverable · bonus · guarantee · scarcity · tên · giá & cách thanh toán). **Chỉ dùng scarcity thật** — số căn còn lại thật, deadline đợt mở bán thật. Fake countdown = cấm.

| Giai đoạn | Thông điệp chính | Offer (đổi lấy thông tin) | LP section bắt buộc |
|---|---|---|---|
| 1. Nhận biết | "Với [X] tỷ, mua được gì ở [khu vực] năm nay" — framing theo ngân sách, không theo dự án | **Bài so sánh khu vực / bảng giá thị trường** (`content/`, không phải LP bán hàng) | Bài SEO dài + CTA mềm "nhận bảng giá khu vực" |
| 2. Tìm hiểu | "Pháp lý sổ hồng đầy đủ — CĐT [tên]. Tiến độ cập nhật [tháng]" | **Brochure + hồ sơ pháp lý** (reciprocity, zero-price effect) | Pháp lý · Tiến độ (ảnh có timestamp) · Hồ sơ CĐT · Form nhẹ (SĐT + tên) |
| 3. So sánh | "Bảng giá gốc CĐT [tháng/năm] — [N] loại căn, giá từ [X] ₫/m²" | **Bảng giá gốc + bảng tính vay** (dream outcome ↑, effort ↓) | **Bảng giá (anchor: giá gốc → giá sau CK)** · Mặt bằng layout · Tính vay/dòng tiền · So sánh 3 loại căn (paradox of choice) · FAQ xử lý phản đối |
| 4. Quyết định | "[Dự án] — Đợt mở bán [N]: chiết khấu [X]% thanh toán sớm. Còn [N] căn." | **Ưu đãi giữ chỗ**: suất ưu tiên chọn căn + **quà booking** + **chiết khấu thanh toán sớm** — kèm **guarantee hoàn 100% tiền giữ chỗ nếu không chọn được căn** (risk reversal, hạ regret aversion) | Chính sách bán hàng · Số căn còn lại (thật) · Nhà mẫu · Sticky CTA gọi/Zalo · Form 3 field |
| 5. Sau lead | "Giữ chỗ [X] triệu — hoàn 100%. Ưu tiên chọn căn ngày [ngày mở bán thật]" | Cohort scarcity (ngày mở bán) + price-increase scheduling **chỉ khi giá đợt sau thật sự tăng** | Trang cảm ơn có bước tiếp theo rõ ràng (peak-end) · Lịch xem nhà mẫu |

**Message match (bắt buộc):** headline RSA phải lặp lại đúng cụm khách gõ. Bảng ánh xạ ad group → headline → LP block đã có sẵn ở `keywords/adgroup-map.md` §Message match — **không viết lại, chỉ tuân thủ**.

### 2.3 KPI theo giai đoạn: micro-conversion vs lead

| Giai đoạn | Conversion đếm trong Google Ads | Micro-conversion (chỉ báo, **không** để smart bidding học) | KPI chính |
|---|---|---|---|
| 1. Nhận biết | Không đặt conversion | `scroll` 75%, `user_engagement` ≥60s | Cost/engaged session · Audience size tăng |
| 2. Tìm hiểu | Không (hoặc secondary) | `xem_bang_gia`, `xem_mat_bang` | Tỷ lệ vào audience remarketing |
| 3. So sánh | `generate_lead` (secondary nếu volume thấp) | `form_start`, tải bảng giá | CVR LP · CPC · Tỷ lệ vào list nóng |
| 4. Quyết định | **`generate_lead` = primary** (giai đoạn chưa có offline import) → đảo sang `Lead_Contactable` primary khi ECL chạy. `phone_click`/`zalo_click` = **secondary** — để primary là bẫy optimize-to-quality: bidding sẽ mua click nút rẻ thay vì lead thật (QA chốt 2026-07-28, khớp PLAN §0.4 + tracking/gtm-container-spec) | — | **CPL** · CPQL · Search impression share |
| 5. Sau lead | **Offline conversion import** (lead qualified, booking) | — | Lead→qualified % · Qualified→booking % · CAC/booking |

> Nguyên tắc từ `ads`/`b2b-paid-playbook` — *the optimize-to-quality trap*: nếu chỉ feed form-fill thô cho smart bidding, nó sẽ mua form-fill rẻ và rác. Chỉ đặt primary conversion ở giai đoạn 4; mở offline import sớm nhất có thể.

---

## 3. Phân bổ ngân sách — 3 kịch bản

Nguyên tắc: **không nhảy bậc thang intent** (`ads`/google-search-playbook). Ngân sách nhỏ dồn bottom funnel; chỉ mở lên trên khi CPL ổn định.

| Giai đoạn funnel | 30tr ₫/tháng (~1tr/ngày) | 60tr ₫/tháng (~2tr/ngày) | 150tr ₫/tháng (~5tr/ngày) |
|---|---|---|---|
| **4. Quyết định** — Search T1 brand (#1, #2) | **45%** | 35% | 25% |
| **3. So sánh** — Search T2 (#3, #4, #8) | **40%** | 38% | 32% |
| **Bottom funnel (T1+T2)** | **85%** | **73%** | **57%** |
| Discovery broad (#7) — dò truy vấn mới | 5% | 5% | 5% |
| **5. Sau lead + 3.** — Remarketing **Demand Gen** (Display đã bị Google migrate vào Demand Gen từ 6/2026 — không dùng Display campaign mới) | 10% | 15% | 15% |
| **2. Tìm hiểu** — Search T3 (#5, #6) | 0% (tắt) | 7% | 10% |
| PMax feed-less | 0% | 0% | 8% |
| **1. Nhận biết** — YouTube | 0% | 0% | 5% |
| **Tổng** | 100% | 100% | 100% |

**Chia nhỏ trong khối Search:** theo tỷ trọng `keywords/adgroup-map.md` §Bản đồ campaign, chuẩn hoá lại về 100% sau khi tắt campaign không dùng.

**Bộ keyword bật theo kịch bản** (cột `uu_tien`):

| Kịch bản | Bật `uu_tien` | Số keyword |
|---|---|---|
| 30tr | 1 | 4.538 → lọc còn dự án đang phân phối |
| 60tr | 1 + 2 | 7.825 → lọc |
| 150tr | 1 + 2 + 3 | 8.512 → lọc |

**Bidding theo volume conversion/campaign/tháng** (`google-search-playbook`):

| Conv/tháng | Chiến lược |
|---|---|
| 0–15 | Manual CPC hoặc Maximize Conversions (không target) |
| 15–30 | Maximize Conversions |
| 30+ ổn định | Target CPA — đặt bằng hoặc cao hơn nhẹ CPA thực 30 ngày gần nhất |
| Có giá trị lead thật chảy về | Target ROAS |

Điều chỉnh tCPA **±10–15%/lần, chờ 1–2 tuần**. Tăng ngân sách **≤20%/lần, chờ 3–5 ngày**. Campaign dưới ~15–30 conv/tháng thì **gộp**, đừng tách.

### 3.1 Gate — điều kiện mở khoá bậc chi tiêu tiếp theo

Không mở campaign type mới khi chưa có data chứng minh cần. Mỗi gate phải đo được bằng số + khoảng thời gian.

| Gate | Mở khoá | Điều kiện (ALL) |
|---|---|---|
| **G0** | Được phép bật quảng cáo | ✅ `generate_lead` / `phone_click` / `zalo_click` đã test bằng **1 lead thật** đi tới CRM · ✅ gclid/gad_source ghi vào CRM · ✅ LP load <3s mobile · ✅ negative list account-level đã apply · ✅ Search Partners + Display OFF, location = **Presence** |
| **G1** | Mở rộng T2 sang khu vực/loại hình mới | T1 brand đạt ≥ `[điền]` conv/tháng **và** CPL ≤ mục tiêu trong **30 ngày liên tiếp** |
| **G2** | Bật Remarketing **Demand Gen** (không tạo Display mới — Google khai tử từ 6/2026, lưu ý Demand Gen min $5/ngày). **Việc kèm bắt buộc khi mở (war-game round 5): điền `Excluded content keywords` cấp tài khoản** — negative keyword (mọi cấp) chỉ phủ Search+Shopping, inventory YouTube/Display của Demand Gen KHÔNG được 382 negative che | GA4 audience `xem_bang_gia` hoặc `engaged_60s` đạt ≥ 1.000 user/30 ngày (lưu ý: bậc 30tr ~900 click/tháng → G2 bất khả thi bằng số nếu chỉ dựa traffic ads — cần organic/content bơm thêm) · GA4 ↔ Google Ads đã link · LP có traffic ổn định ≥ 4 tuần |
| **G3** | Bật Search T3 (#5, #6) | T1+T2 đạt tCPA mục tiêu **2 tháng liên tiếp** · G2 đã chạy (T3 cần đích đến là audience) |
| **G4** | Bật PMax feed-less | **Offline conversion import đã chạy thật** (lead qualified từ CRM → Google Ads) · brand exclusion list đã set · Search ≥ 30 conv/tháng · negative list apply cho PMax từ ngày 1 |
| **G5** | Bật YouTube | Ngân sách ≥ 150tr/tháng · có video dự án đạt chuẩn (không để Google tự sinh) · G4 ổn định ≥ 6 tuần · **đã có media plan từ Reach Planner** (xem dưới) · đo bằng **brand search lift**, không đo bằng CPL |

**Điều kiện tiên quyết mới của G5 — Reach Planner media plan.** Không mở YouTube khi chưa có dự phóng reach/frequency (đúng nguyên tắc gate: mọi gate phải đo được **trước** khi mở). Reach Planner cho dự phóng reach · frequency · views · conversions · impressions, dựa trên trend + campaign tương tự, dữ liệu tối đa **92 ngày**. Google nói rõ nó **không bảo đảm** kết quả.
→ Phân vai: **Reach Planner để XIN ngân sách** (trước khi chạy) · **brand search lift để NGHIỆM THU** (sau khi chạy). Hai thứ bổ sung, không thay nhau. Không có plan = không biết 250.000₫/ngày mua được bao nhiêu reach → không có cách phán G5 thành hay thất bại.

### 3.2 Gate nào mở khoá tính năng AI nào

Google gọi việc này là **"AI automation strategy"** — lập chiến lược có gate thay vì bật hết. Hệ đã có gate G0-G5; bảng dưới map gate ↔ tính năng để không ai bật sớm. Nguồn: `research/google-official-curriculum.md` §C2.6.

| Bậc | Điều kiện (khớp gate) | Được bật | Vì sao KHÔNG sớm hơn |
|---|---|---|---|
| **0** | Ngày 1, 0 conversion — **G0** | Max Clicks + bid cap · Phrase+Exact · **auto-apply TẮT hết** · ACA TẮT | Chưa có conversion thì mọi thứ "AI" đều học từ hư không |
| **1** | ≥15 conv/30 ngày cấp campaign + contact rate >50% | `Maximize Conversions` (chưa đặt tCPA) · **đảo primary sang `Lead_Contactable`** | Đảo primary TRƯỚC khi bật smart bidding, không thì nó học form thô và mua lead rác |
| **2** | ≥30 conv/30 ngày + **ECL chạy thật** — **G4** phần dữ liệu | `tCPA` · **giờ mới** test 1 ad group **broad** · `Data exclusion` bắt đầu có tác dụng | Google: "It's **critical** to use Smart Bidding with broad match" — bậc 0-1 chưa thoả điều kiện của chính Google |
| **3** | Giá trị lead phân tầng chảy về, ≥2 giá trị non-zero | `Maximize conversion value` / `tROAS` · **Conversion Value Rules** | Cần "2 or more unique, non-zero values" mới có gì để tối ưu theo giá trị |
| **4** | Search ổn định ≥6 tuần ở bậc 3 | **AI Max** (bắt buộc conversion-based bidding; TẮT final URL expansion) | AI Max search term matching **không chạy với Manual CPC/Max Clicks** — bật sớm là bật vô nghĩa |
| **5** | Đã ở bậc 4 + có creative đúng 3 tỷ lệ | **PMax** (`campaign-setup.md` §5.5) / **Demand Gen** | PMax tối ưu theo signal được đưa vào; signal rác thì nó mua rác rất hiệu quả |

> 🔑 **Điểm mấu chốt:** thứ mở khoá AI **không phải ngân sách, mà là dữ liệu conversion chất lượng.** Vì vậy **ECL không phải "việc của tuần 8"** — nó là điều kiện tiên quyết của toàn bộ nhánh AI. Hoãn ECL = tự khoá mình ở bậc 0-1 vĩnh viễn, bất kể chi bao nhiêu.

**Gate ngược (rút lui):** kill rules từ `ads`/b2b-paid-playbook —
- Ad/keyword mới: pause khi chi **2–3× CPL mục tiêu mà 0 conversion**.
- Ad chạy >7–14 ngày: pause khi CPL **1,5–2× trên mục tiêu**.
- Campaign nào cũng vậy: không pause producer khi chưa có bản thay thế sẵn sàng.

---

## 4. KPI tree — công thức ngược từ số booking

```
                     BOOKING / GIỮ CHỖ  (B)          ← mục tiêu kinh doanh
                              ▲  ÷ r_book
                     LEAD QUALIFIED     (Q)          ← CRM chấm điểm
                              ▲  ÷ r_qual
                     LEAD               (L)          ← generate_lead + phone_click + zalo_click
                              ▲  ÷ CVR_lp
                     CLICK              (C)          ← CTR × impression
                              ▲  × CPC
                     NGÂN SÁCH          (S)
```

### Công thức ngược

| Bước | Công thức | Giá trị |
|---|---|---|
| Booking mục tiêu | `B` | `[điền — mục tiêu kinh doanh/tháng]` |
| Lead qualified cần | `Q = B / r_book` | `r_book` = qualified→booking `[điền từ CRM/tuần chạy đầu]` |
| Lead cần | `L = Q / r_qual` | `r_qual` = lead→qualified `[điền từ CRM/tuần chạy đầu]` |
| Click cần | `C = L / CVR_lp` | `CVR_lp` `[điền từ research/tuần chạy đầu]` |
| Ngân sách | `S = C × CPC` | `CPC` `[điền từ tuần chạy đầu — theo tier, brand rẻ hơn khu vực]` |
| **CPL** | `S / L` | dẫn xuất |
| **CPQL** | `S / Q` | dẫn xuất |
| **CAC/booking** | `S / B` | dẫn xuất |

### Trần chi phí (breakeven — từ `ads`/b2b-paid-playbook)

```
Giá trị 1 booking   = phí môi giới trung bình/căn × (booking → HĐMB %)
Breakeven CPL       = giá trị 1 booking × (lead → booking %)
Breakeven CPC       = Breakeven CPL × CVR_lp
CPL mục tiêu        = Breakeven CPL × (1 − biên lợi nhuận yêu cầu)
```

Mọi kill rule và quyết định scale đều neo vào `CPL mục tiêu` này, **không** neo vào benchmark ngành.

### Bảng điền (một dòng/tháng — đây là scorecard sống)

| Chỉ số | Nguồn | Tháng 1 | Tháng 2 | Tháng 3 |
|---|---|---|---|---|
| Chi tiêu (S) | Google Ads | | | |
| Impression / CTR | Google Ads | | | |
| Click (C) / CPC | Google Ads | | | |
| CVR_lp | GA4 | | | |
| Lead (L) | GA4 `generate_lead` + `phone_click` + `zalo_click` | | | |
| CPL | dẫn xuất | | | |
| Lead qualified (Q) / r_qual | **CRM** | | | |
| CPQL | dẫn xuất | | | |
| Booking (B) / r_book | **CRM** | | | |
| CAC/booking | dẫn xuất | | | |
| Search impression share | Google Ads | | | |
| Lost IS (budget) vs (rank) | Google Ads | | | |
| **Chiết khấu/quà TB phải bỏ ra để chốt 1 booking** | **CRM/sale, nhập tay** | | | |

> Dòng chiết khấu (thêm 2026-08-06, Binet-Field): lợi nhuận của brand mạnh nằm ở GIÁ chứ không ở volume — 30 năm dữ liệu IPA không có case direct-response nào giảm được độ nhạy giá. Với sàn, biến tương đương là mức chiết khấu/quà để chốt deal; không ghi số này thì không bao giờ thấy được brand equity đang rẻ đi hay đắt lên. Chi tiết: `research/books/long-and-short.md`.

> **Nguồn chân lý** (`attribution`): **CRM quyết định số lượng conversion.** GA4 và Google Ads chỉ giải thích *đến từ đâu*. **Không cộng dồn** conversion giữa các nguồn. Với chu kỳ 3–12 tháng, luôn báo cáo **first-touch và last-touch cạnh nhau** — khoảng cách giữa hai con số chính là insight. Bổ sung câu "Anh/chị biết dự án qua đâu?" trong form/cuộc gọi đầu (self-reported) — đây là thứ duy nhất bắt được truyền miệng và Zalo group, vốn rất lớn trong BĐS VN.

---

## 5. Nhịp vận hành PM/QA

### Hàng ngày (10–15 phút)

| # | Việc | Gắn với giai đoạn |
|---|---|---|
| 1 | Kiểm tra pacing ngân sách + ad bị disapproved | Tất cả |
| 2 | CPC/CPL spike bất thường (>±30% so hôm trước) | 3, 4 |
| 3 | Lead mới trong CRM **có gclid/gad_source không** — nếu trống, tracking hỏng | 4, 5 |
| 4 | Lead mới đã được gọi trong `[điền SLA — giờ]` chưa | 5 |

### Hàng tuần

| # | Việc | Gắn với giai đoạn |
|---|---|---|
| 1 | **Nghi thức search terms 3 lượt**: (a) lãng phí — term ≥3 click, 0 conv → negative; (b) thắng — term có conv chưa là keyword → thêm exact/phrase; (c) trôi — phrase/broad kéo nghĩa lệch → siết match | 1–4 |
| 2 | Cập nhật `keywords/` theo `keywords/UPDATE.md` (tài sản sống) | 1–4 |
| 3 | **Scorecard 8 số**: chi tiêu · lead · CPL · lead→qualified % · qualified · CPQL · impression share · top search term lãng phí | Tất cả |
| 4 | Kích thước audience remarketing (đủ ngưỡng chưa → G2) | 3, 5 |
| 5 | Clarity: rage click / dead click trên form và bảng giá (giới hạn 10 request/ngày — chỉ đọc 1 lần/tuần) | 3, 4 |
| 6 | **Chấm chất lượng lead** — người trực máy chấm 0–3 mỗi trục, tối đa 9: **Nhu cầu/thời điểm** · **Tài chính** · **Phù hợp** (ở/đầu tư, khu vực, phân khúc). Sau ~20 lead: xếp hạng ad/keyword theo **điểm trung bình, không theo CPL**. Cắt biến thể dưới ~5 điểm. | 4, 5 |
| 7 | Kiểm tra ≥3 split test đang chạy (ad copy / LP / offer) | 3, 4 |

### Hàng tháng

| # | Việc | Gắn với giai đoạn |
|---|---|---|
| 1 | Đối soát Google Ads ↔ GA4 ↔ CRM. **Khi lệch, CRM thắng.** | Tất cả |
| 2 | Chạy offline conversion import (lead qualified + booking → Google Ads) | 5 |
| 3 | Review bidding theo bảng volume; đổi chiến lược nếu vượt ngưỡng | Tất cả |
| 4 | **Review gate** — đủ điều kiện mở G1→G5 chưa? Có gate nào phải rút lui không? | Tất cả |
| 5 | Quality Score <6: sửa thành phần yếu (CTR kỳ vọng / độ liên quan / LP) **trước khi** tăng bid | 3, 4 |
| 6 | Tái phân bổ % ngân sách theo bảng §3, cập nhật CPL mục tiêu theo breakeven mới | Tất cả |

### Tiêu chí QA — Fable (main agent) dùng để nghiệm thu

| # | Tiêu chí | Đạt khi |
|---|---|---|
| Q1 | **Event name khớp** (A↔C) | Registry `CLAUDE.md` = 6 event, đã có spec trong `tracking/`. Mọi event mới phải vào registry + `tracking/gtm-container-spec.md` trước khi LP dùng. |
| Q2 | **Message match** (A↔B) | Mỗi ad group được bật đều có: headline RSA chứa cụm quy định + LP có block tương ứng, theo `keywords/adgroup-map.md` §Message match. Không có ad group nào trỏ về homepage. |
| Q3 | **Không bịa số** | Mọi con số trong file này hoặc là `[điền …]`, hoặc trích được về `keywords/`, `PLAN.md`, hay skill reference. Không có benchmark CPL/CVR ngành nào được nêu như sự thật. |
| Q4 | **Ngân sách cộng đủ 100%** | Cả 3 cột §3 tổng = 100%; bottom funnel ≥80% ở kịch bản 30tr. |
| Q5 | **Gate đo được** | Mỗi gate có ngưỡng số + khoảng thời gian. Không có gate nào chỉ ghi "khi ổn định". |
| Q6 | **Ponytail** | Không đề xuất campaign type / công cụ mới nào nằm ngoài hệ thống gate. PMax và YouTube chỉ xuất hiện ở G4/G5. |
| Q7 | **Offer trung thực** | Mọi scarcity trong §2.2 là thật (số căn, ngày mở bán, lịch tăng giá). Không countdown giả, không "worth $X" thổi phồng. |
| Q8 | **Nguồn chân lý conversion** | Mọi báo cáo nêu rõ CRM là nguồn đếm; không cộng dồn conversion giữa Google Ads/GA4/CRM. |

---

## 6. Việc user cần điền

| Cần | Dùng ở | Ghi chú |
|---|---|---|
| Danh sách dự án **đang thực sự phân phối** | §2, §3 | Lọc `nhom_adgroup` trong `master-keywords.csv`; phần còn lại là kho dự phòng |
| Phí môi giới trung bình/căn · tỷ lệ booking→HĐMB | §4 breakeven | Quyết định trần CPL — không có số này thì mọi kill rule là đoán |
| Mục tiêu booking/tháng (`B`) | §4 | |
| Chính sách bán hàng đợt hiện tại: % chiết khấu thanh toán sớm, mức giữ chỗ, quà booking, ngày mở bán | §2.2 | Phải là số thật — offer giả làm hỏng Q7 |
| SLA gọi lead (giờ) | §5 daily | |
| Kịch bản ngân sách chọn: 30 / 60 / 150tr | §3 | |
