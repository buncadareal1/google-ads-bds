# PLAYBOOK — Nghiên cứu đối thủ để cải thiện Google Ads (chạy hàng tháng)

Phạm vi: đối thủ **cùng sản phẩm**, không phải "mọi dự án BĐS". Output mỗi vòng là **1 bảng so sánh + 3–5 action** ghi vào `research/competitors/<YYYY-MM>-<slug-dự-án>.md`.

Thời lượng mục tiêu: 3–4 giờ/dự án/tháng. Chạy vào tuần 1 của tháng, trước buổi review ngân sách.

Quy tắc bất di bất dịch: **mọi fact có URL nguồn**. Site chặn (403/JS shell/cần login) → ghi "không xác minh được", **không suy đoán nội dung**.

---

## Bước 1 — Xác định tập đối thủ (30')

Ba điều kiện phải cùng lúc đúng. Chỉ đúng 1–2 → **không phải đối thủ**, đừng tốn thời gian.

| Điều kiện | Cách kiểm |
|---|---|
| **Cùng phân khúc** | Loại hình (khu đô thị / căn hộ / thấp tầng) + khoảng giá chồng lấn ≥40% với rổ hàng mình đang bán |
| **Cùng khu vực** | Cùng huyện/cụm địa lý, hoặc ≤20 phút lái xe từ dự án mình; nếu khác tỉnh thì phải cùng "hướng" từ TP.HCM (Tây vs Đông là 2 tệp khác nhau) |
| **Cùng tệp khách** | Cùng mục đích mua (ở / second home / đầu tư) + cùng mức ngân sách khách |

Công cụ:
- `keywords/projects.tsv` — lọc theo cột khu vực + loại hình + hạng (A/B). Đây là nguồn nhanh nhất, có sẵn CĐT.
- WebSearch: `"<loại hình> <huyện> giá bán 2026"`, `"dự án tương tự <tên dự án>"`.
- SERP của chính từ khóa brand mình: ai mua ads/SEO trên trang 1 khi search tên dự án mình → đó là đối thủ đang cướp traffic thật.

Phân tầng đầu ra:
- **Tier 1 — trực tiếp**: cùng huyện + giá chồng lấn. Theo dõi hàng tháng, đầy đủ mọi bước.
- **Tier 2 — cùng tệp khác địa bàn**: khách so sánh nhưng ít khi thay thế. Chỉ làm bước 4 (keyword) + bước 5 (offer).
- **Loại bỏ**: cùng CĐT (là sibling, cannibalize chứ không phải đối thủ — nhưng phải gắn negative chéo và **brand exclusion** nếu chạy PMax); khác phân khúc giá >2×; khác mục đích mua.

Số đối thủ hợp lý: **3–5 Tier 1**. Nhiều hơn = không ai được soi kỹ.

---

## Bước 2 — Soi quảng cáo đối thủ (45')

> Skills chuyên trách đã cài (invoke khi chạy bước này): `ads-competitor` (audit đối thủ paid, 2.6K installs) ·
> `adspy-analytics-intelligence` (phân tích ad intelligence) · `ad-library-teardown` (teardown Meta Ad Library).
> Chiến lược bid từ khóa đối thủ theo giai đoạn hành trình: xem `keywords/journey-strategy.md`.

### 2.1 Google Ads Transparency Center — `adstransparency.google.com`

Đây là nguồn duy nhất xem được **ad copy đang chạy thật** của đối thủ, miễn phí, không cần tài khoản.

Cách tra:
1. Mở `adstransparency.google.com`, set **Region = Vietnam**, **Date range = Last 30 days**.
2. Ô search nhận **advertiser name** hoặc **domain**. Với BĐS VN gõ **domain** hiệu quả hơn tên (nhiều sàn F2 chạy dưới pháp nhân lạ, không tra được bằng tên dự án).
3. Deep-link tiện dụng: `https://adstransparency.google.com/?region=VN&domain=<domain-đối-thủ>`
4. Với mỗi domain đối thủ: lọc **Format = Text** để lấy RSA headline/description; lọc **Format = Image/Video** để xem creative Display/YouTube.
5. Chụp lại: headline lặp nhiều nhất, con số/offer xuất hiện trong ad text, ngày first-shown (ad mới = đợt mở bán mới), có chạy Display/YouTube hay chỉ Search.

⚠️ **Giới hạn đã kiểm chứng**: trang này là **JS shell** — WebFetch/curl trả về khung rỗng, không lấy được data. Bắt buộc mở bằng **browser thật** (hoặc MCP có headless browser). Nếu vòng nào không mở được browser → ghi "không xác minh được", đừng đoán ad copy.

⚠️ BĐS VN một dự án có **hàng chục domain sàn F2** cùng chạy. Tra domain của: (a) site chính chủ CĐT, (b) 3–5 domain top SERP khi search tên dự án đó. Mỗi domain là một advertiser riêng.

### 2.2 Meta Ad Library — `facebook.com/ads/library`

Set Country = Vietnam, Ad Category = **All ads** (BĐS VN không thuộc special category, nên không có bộ lọc housing như US). Search theo **tên Page** của sàn/dự án.
Lấy: hook 3 giây đầu của video, offer trong caption, số biến thể creative đang chạy (nhiều biến thể = ngân sách lớn), ngày bắt đầu chạy.
Dùng để: đối chiếu message Meta vs Search — offer nào họ dám nói trên Meta thường là offer thật đang đẩy.

### 2.3 Auction Insights (chỉ khi có data của chính mình)

Vị trí: Google Ads → Campaigns/Ad groups/Keywords → **Segment > Auction insights**. Chạy ở **cấp keyword** cho nhóm `brand-<dự-án>` và `<khu-vực>--gia-bang-gia` — cấp campaign quá thô.

Đọc 5 cột:

| Cột | Nghĩa hành động |
|---|---|
| Impression share | Đối thủ có mặt bao nhiêu % phiên đấu mình tham gia |
| Overlap rate | Tần suất chạm mặt — >50% = đối thủ trực tiếp thật sự, dù bước 1 không xếp vào |
| Position above rate | Họ trên mình bao nhiêu % → dấu hiệu Ad Rank (bid × Quality Score) thua |
| Top of page rate | Ai đang giữ top 4 |
| Outranking share | KPI tổng hợp — dưới 50% với đối thủ Tier 1 = cần xử lý |

Diễn giải: outranking share thấp **không** đồng nghĩa phải tăng bid. Kiểm Quality Score trước (Ad relevance / Expected CTR / LP experience) — nâng QS rẻ hơn nâng bid.

**Điều kiện dùng**: cần MCP `google-ads` + developer token đã duyệt (xem `SETUP.md` / `research/mcp-servers.md`). Chưa có → bước này ghi "chưa khả dụng", không thay bằng phỏng đoán. Auction Insights **không** xuất qua Google Ads API dạng report chuẩn — nếu MCP không hỗ trợ, xuất tay bằng UI ra CSV.

### 2.4 Nguồn phụ (khi có ngân sách tool)

Semrush / Ahrefs → Advertising Research: lịch sử keyword paid + ad copy + landing page ước lượng. Data VN mỏng, dùng làm gợi ý chứ không làm fact. MCP Semrush có trong danh sách nhưng cần authenticate.

---

## Bước 3 — Teardown landing page đối thủ (60')

Với mỗi đối thủ, chọn **2 LP**: (a) site chính chủ CĐT, (b) LP sàn F2 xếp cao nhất SERP (đây mới là thứ khách click từ ads).

Checklist chấm điểm — theo `research/google-ads-bds-vn.md` §6 + skill `cro`. Mỗi mục: **Có / Không / Không xác minh được**.

**Bậc 1 (bắt buộc — thiếu là LP hỏng)**

| # | Mục | Chuẩn đạt |
|---|---|---|
| 1 | **Bảng giá** | Có bảng theo loại sản phẩm, có số thật, không phải "liên hệ để biết giá" |
| 2 | **Mặt bằng** | Mặt bằng tổng + mặt bằng từng loại căn/lô |
| 3 | **Tiến độ + ảnh thật** | Ảnh công trường **có ghi tháng**, không phải render/phối cảnh |
| 4 | **Khoảng giá hiện ở hero** | "từ X tỷ" nhìn thấy không cần scroll — tự lọc tài chính |
| 5 | **Zalo nổi cố định + click-to-call** | Nút nổi bám khi scroll, số hotline bấm gọi được trên mobile |
| 6 | **Form qualifying** | Họ tên + SĐT + **dropdown ngân sách** + **dropdown mục đích** (ở / đầu tư) |
| 7 | **Tốc độ** | PageSpeed Insights mobile: LCP <2,5s trên 4G |

**Bậc 2 (đòn bẩy cạnh tranh)**

| # | Mục | Ghi lại gì |
|---|---|---|
| 8 | Pháp lý | Sổ gì, ngân hàng bảo lãnh nào, CĐT/liên danh nào |
| 9 | **Offer + chính sách thanh toán** | % vốn ban đầu, % vay, ân hạn gốc/lãi bao lâu, chiết khấu từng phương án |
| 10 | **Deadline thật** | Có ngày cụ thể không, hay chỉ "ưu đãi có hạn" chung chung |
| 11 | Social proof | Số căn đã bàn giao, số cư dân, tiện ích đã vận hành |
| 12 | Footer pháp nhân/MST/địa chỉ | Thiếu → họ có rủi ro bị disapproved, mình làm đủ để thắng LP experience |

Công cụ: WebFetch để lấy nội dung (nhanh, nhưng mất layout & phần render bằng JS); browser thật để chấm mục 5/7 và bắt sticky bar/popup. PageSpeed Insights cho mục 7.

⚠️ Site chặn hoặc render JS: **batdongsan.com.vn trả 403 với WebFetch** (đã kiểm) — cần browser. Ghi thẳng "403, không xác minh được", không lấy nội dung từ bản cache/mô tả SERP rồi coi là fact.

Sản phẩm của bước này: **bảng 12 dòng × N đối thủ + cột "Eco Retreat / dự án mình"**. Ô nào mình "Không" mà ≥2 đối thủ "Có" → ưu tiên sửa cao nhất.

---

## Bước 4 — Keyword overlap (30')

Đối chiếu với `keywords/master-keywords.csv` (cột `nhom_adgroup` dạng `brand-<slug>`).

Bốn câu hỏi, theo thứ tự:

**4.1 Dự án mình đã có bộ brand keyword chưa?**
```bash
grep -ci "<tên dự án>" keywords/master-keywords.csv
```
Trả 0 = **lỗ hổng nghiêm trọng**: đang trả tiền cho generic trong khi tier intent cao nhất (T1_brand) bỏ trống, và sàn F2 tự do bid tên dự án mình. Bộ chuẩn 22 keyword/dự án (template lấy từ bất kỳ `brand-*` nào có sẵn): `<tên>`, `+ giá`, `+ bảng giá`, `+ giá bao nhiêu`, `+ mở bán`, `mua +`, `+ chủ đầu tư`, `+ vị trí`, `+ mặt bằng`, `+ tiện ích`, `+ chính sách bán hàng`, `+ tiến độ thanh toán`, `+ pháp lý`, `+ có nên mua`, `+ nhà mẫu`, `+ trả góp`, `+ chiết khấu`, `+ lãi suất`, `+ tiến độ xây dựng`, `+ review`, `+ đánh giá`, `+ bàn giao khi nào`. Tên dự án trần + hỏi giá + mở bán để **exact**, còn lại **phrase**.

**4.2 Đối thủ có bid tên dự án mình không?**
Search ẩn danh tên dự án mình trên Google (mobile + desktop, geo VN), đếm số ad không phải của mình. Chéo với Auction Insights ở nhóm `brand-<dự-án-mình>`. Có đối thủ → phải giữ IS ≥90% ở brand; mất brand IS là mất lead rẻ nhất.

**4.3 Mình có bid tên đối thủ không / có nên bid?**
```bash
grep -i "<tên đối thủ>" keywords/master-keywords.csv | cut -d, -f2 | sort -u
```
Nên bid khi cả 3 đúng: (a) đối thủ đắt hơn hoặc bàn giao chậm hơn rõ rệt, (b) mình có LP so sánh tử tế (không phải LP bán hàng thẳng), (c) đủ ngân sách sau khi brand mình đã đạt IS ≥90%. **Đừng bid tên đối thủ khi brand mình còn hở** — đó là đổi lead rẻ lấy lead đắt.

**4.4 ⚠️ Quy tắc trademark (`research/google-ads-bds-vn.md` §7)**
- **Bid keyword tên đối thủ: ĐƯỢC PHÉP.** Google không cấm.
- **Tên đối thủ trong ad text (headline/description/path/sitelink/callout/business name): KHÔNG.** Từ 2/2025 cơ chế complaint-driven — không bị chặn tự động, nhưng đối thủ khiếu nại là ad bị gỡ và tài khoản dính flag.
- Reseller hợp pháp được nhắc tên nếu **không mạo nhận là CĐT** — sàn F2 phân phối chính thức thì được, nhưng đây là vùng xám, tránh.
- Cách viết an toàn: đánh vào **thuộc tính so sánh**, không vào tên. "Bàn giao 2026 – Không Chờ 3 Năm", "Chỉ 25% Đến Khi Nhận Nhà", "Từ 2,5 Tỷ – Rẻ Hơn 40% Khu Đông".
- Đặt ad group tên đối thủ vào **campaign riêng**, ngân sách trần cứng, LP là trang so sánh, và **theo dõi contact rate riêng** — lead từ tệp này chất lượng thấp hơn brand.

---

## Bước 5 — So sánh offer / giá / chính sách thanh toán → góc phản công (30')

Lập bảng, mỗi ô phải có URL nguồn:

| Trục | Ghi gì |
|---|---|
| Giá vào (thấp nhất/căn) | Con số + loại sản phẩm nào đạt mức đó |
| Giá/m² | Chuẩn hóa để so sánh thật (giá/căn lệch vì diện tích) |
| Vốn ban đầu | % thanh toán đến khi nhận nhà |
| Hỗ trợ vay | % vay tối đa + ân hạn gốc/lãi bao nhiêu tháng |
| Chiết khấu | Từng phương án thanh toán, con số cụ thể |
| Quà tặng | Nội thất / phí quản lý / voucher |
| Bàn giao | Quý/năm |
| Deadline | Có ngày cụ thể không |

**Chuyển sang RSA copy** — mỗi trục mình thắng thành 1 headline, mỗi trục mình thua thành 1 objection phải xử lý trên LP:

| Mình thắng ở | Headline mẫu (≤30 ký tự) | Vị trí |
|---|---|---|
| Giá vào thấp hơn | `Từ 2,5 Tỷ – Sở Hữu Ngay` | Headline 1–3 (pin) |
| Vốn ban đầu thấp hơn | `Chỉ 25% Đến Khi Nhận Nhà` | Headline 4–6 |
| Ân hạn dài hơn | `Ân Hạn Gốc & Lãi 24 Tháng` | Headline 4–6 |
| Chiết khấu cao hơn | `Chiết Khấu Đến 12%` | Headline 7–9 |
| Bàn giao sớm hơn | `Nhận Nhà Quý 4/2026` | Headline 7–9 |
| Deadline thật | `Ưu Đãi Đến 31/8` | Description 1 |

Ràng buộc chính sách (`research/google-ads-bds-vn.md` §7): **không** "cam kết sinh lời X%" (unreliable claims) — dùng "tiềm năng/dự kiến". Không ALL-CAPS. Con số trong ad **phải khớp con số trên LP**, lệch là mất Quality Score và có nguy cơ disapproved "destination mismatch".

Mình thua ở trục nào → đó là block bắt buộc trên LP (FAQ hoặc bảng so sánh), không phải thứ để giấu.

---

## Bước 6 — Output chuẩn hóa

File `research/competitors/<YYYY-MM>-<slug>.md`, đúng 5 phần:

1. **Tập đối thủ** — Tier 1/Tier 2/loại bỏ, kèm lý do một dòng mỗi cái.
2. **Bảng so sánh** — dự án mình + N đối thủ × các trục: giá vào, giá/m², vốn ban đầu, vay/ân hạn, chiết khấu, bàn giao, quy mô, CĐT. **Mỗi ô có URL.**
3. **Teardown LP** — bảng 12 mục × N site + ghi rõ site nào không truy cập được và vì sao.
4. **Điểm mạnh / điểm yếu từng đối thủ** — 2–3 gạch đầu dòng mỗi bên, mỗi gạch neo vào một fact có nguồn.
5. **3–5 action** — mỗi action: *làm gì · file/nơi thực thi · vì sao (fact nào) · đo bằng metric nào*. Không quá 5. Action thứ 6 trở đi là danh sách ước, không phải kế hoạch.

Đối chiếu vòng trước: mở file tháng liền trước, đánh dấu action nào đã xong, action nào trượt và tại sao. Đối thủ đổi giá/chính sách → highlight delta, đó là tin quan trọng nhất của vòng.

---

## Những gì KHÔNG làm

- Không coi mọi dự án BĐS là đối thủ. Sai tệp = mọi kết luận sau đó vô nghĩa.
- Không copy ad copy đối thủ nguyên văn — copy **cấu trúc offer**, không copy chữ.
- Không đưa tên đối thủ vào ad text. Không ngoại lệ.
- Không lấy mô tả trong kết quả SERP làm nội dung LP khi LP thật chặn truy cập.
- Không đổi bid/ngân sách ngay trong vòng research. Bid đổi theo data tài khoản (`research/google-ads-bds-vn.md` §4), không theo việc đối thủ vừa giảm giá.
- Không chạy vòng research khi tài khoản chưa có LP riêng + negative list + form qualifying. Sửa nhà mình trước — nó rẻ hơn và chắc ăn hơn (`§9` Top 10).
