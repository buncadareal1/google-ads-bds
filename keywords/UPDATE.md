# Quy trình update bộ từ khóa

Bộ keyword chết sau ~6 tuần nếu không nuôi: dự án mới mở bán liên tục, search term mới xuất hiện mỗi tuần, rổ hàng đổi. File này là vòng lặp giữ nó sống.

## Cấu trúc thư mục

| File | Vai trò | Sửa tay? |
|---|---|---|
| `gen.py` | Bộ sinh ma trận [loại hình]×[khu vực]×[modifier] + [dự án]×[modifier] | **Có** — thêm khu vực / modifier ở đây |
| `projects.tsv` | 239 dự án thật (`tên \| CĐT \| loại hình \| khu vực \| hạng A/B`) | **Có** — thêm dự án mới ở đây |
| `master-keywords.csv` | Output sinh ra | **KHÔNG** — sẽ bị ghi đè |
| `negative-keywords.csv` | Negative list | **Có** — append thủ công |
| `adgroup-map.md` | Map → campaign, ngân sách | Có |
| `pending-negatives.csv` | **Chưa tồn tại — sinh lúc chạy.** Hàng đợi negative do suggest engine đề xuất (`playbook/monitoring.md` §3, mẫu tin §7). Được **commit để review diff** vào thứ 6 hàng tuần (monitoring §4), không gitignore. Duyệt xong thì append sang `negative-keywords.csv` rồi xoá | Không sửa tay |

Regenerate:
```bash
cd keywords && python3 gen.py master-keywords.csv
```
Script tự chạy self-check (không trùng, ≤80 ký tự, ≤10 từ, lowercase, match_type/tier/ưu tiên hợp lệ) và abort nếu sai.

## Versioning

Cột `ngay_them` (ISO `YYYY-MM-DD`) trên mọi dòng master. Vì `gen.py` stamp `date.today()` cho toàn bộ output, mỗi lần regenerate sẽ reset cột này — nên **commit `master-keywords.csv` vào git sau mỗi lần chạy**, lịch sử thật nằm ở git chứ không ở cột ngày:

```bash
git add keywords/ && git commit -m "keywords: thêm N dự án <tên>, M negative từ search terms tuần <ISO week>"
git log --oneline -- keywords/projects.tsv     # xem dự án được thêm khi nào
git diff HEAD~1 -- keywords/master-keywords.csv | grep '^+' | wc -l
```

Muốn giữ ngày thêm gốc cho từng keyword (thay vì ngày regenerate), set biến môi trường trước khi chạy — hoặc đơn giản hơn: dựa vào `git log -S "<keyword>" -- keywords/master-keywords.csv`.

---

## Hàng tuần — đọc search terms qua MCP `google-ads`

MCP server official (`googleads/google-ads-mcp`) expose 3 tool: **`search`** (chạy GAQL), `get_resource_metadata`, `list_accessible_customers`. Toàn bộ vòng lặp dưới đây dùng `search`.

> 📉 **Search terms report LUÔN ẩn term ít volume** vì privacy threshold ([About the search terms report](https://support.google.com/google-ads/answer/2472708?hl=en): "Some search terms that don't have enough query activity are omitted… in order to keep with our standards on data privacy"). Ba hệ quả áp thẳng vào vòng lặp này:
> 1. Tổng click cộng từ `search_term_view` **< tổng click của `campaign`**. **Không phải bug** — đừng đi tìm lỗi GAQL, đừng báo "MCP trả thiếu dữ liệu".
> 2. Negative list **không bao giờ phủ hết**. Luôn còn rò rỉ dư. Mục tiêu là **giảm dần**, không phải "0 term rác" — đặt mục tiêu 0 là tự tạo việc vô hạn.
> 3. Mọi báo cáo tự động (`playbook/monitoring.md`) phải khai rõ đang đọc `search_term_view` hay `campaign`, và **không được** trừ hai con số đó cho nhau rồi kết luận gì.
> Điều này áp cho **mọi** Search campaign, kể cả khi bật AI Max — không phải hạn chế riêng của AI Max (`research/google-ads-bds-vn.md` §1).

Trong Claude Code, prompt mẫu:

> Dùng MCP `google-ads` tool `search` trên customer `<CUSTOMER_ID>` chạy query dưới đây, rồi phân loại kết quả thành 3 nhóm: (1) search term nên thêm làm keyword mới, (2) nên thêm làm negative, (3) bỏ qua.

### Q1 — Search term đốt tiền nhưng không ra lead → nguồn negative

```sql
SELECT
  search_term_view.search_term,
  search_term_view.status,
  campaign.name,
  ad_group.name,
  segments.keyword.info.text,
  segments.keyword.info.match_type,
  metrics.impressions,
  metrics.clicks,
  metrics.cost_micros,
  metrics.conversions
FROM search_term_view
WHERE segments.date DURING LAST_7_DAYS
  AND metrics.clicks >= 3
  AND metrics.conversions = 0
ORDER BY metrics.cost_micros DESC
LIMIT 200
```

Xử lý: mỗi dòng có `cost_micros` ≥ 50.000.000 (= 50.000 ₫) mà 0 conversion → cân nhắc negative. Append vào `negative-keywords.csv`:
```csv
<search term>,"Đốt <X> ₫ / <Y> click / 0 lead tuần <ISO week>",campaign
```
Chỉ đưa lên `account` khi cụm đó chắc chắn không bao giờ liên quan (ví dụ "tuyển dụng", "thuê"), còn lại để `campaign` cho an toàn.

### Q2 — Search term CÓ conversion nhưng chưa phải keyword → nguồn keyword mới

```sql
SELECT
  search_term_view.search_term,
  search_term_view.status,
  campaign.name,
  ad_group.name,
  metrics.clicks,
  metrics.cost_micros,
  metrics.conversions,
  metrics.conversions_value
FROM search_term_view
WHERE segments.date DURING LAST_30_DAYS
  AND metrics.conversions > 0
  AND search_term_view.status != 'ADDED'
ORDER BY metrics.conversions DESC
LIMIT 200
```

`search_term_view.status` nhận `ADDED | EXCLUDED | ADDED_EXCLUDED | NONE | UNKNOWN`. Dòng `NONE` + có conversion = **tiền đang nằm dưới đất**. Xử lý:
- Nếu là biến thể của một modifier có sẵn → thêm modifier đó vào `MOD_CORE`/`MOD_MID` trong `gen.py` để nhân ra toàn bộ khu vực/dự án.
- Nếu là tên dự án lạ → thêm dòng vào `projects.tsv`.
- Nếu là truy vấn one-off → thêm tay vào list `GENERIC` trong `gen.py`.

### Q3 — Keyword đang chạy: Quality Score và hiệu quả

```sql
SELECT
  ad_group_criterion.keyword.text,
  ad_group_criterion.keyword.match_type,
  ad_group_criterion.quality_info.quality_score,
  ad_group_criterion.quality_info.creative_quality_score,
  ad_group_criterion.quality_info.post_click_quality_score,
  ad_group_criterion.quality_info.search_predicted_ctr,
  campaign.name,
  ad_group.name,
  metrics.impressions,
  metrics.clicks,
  metrics.ctr,
  metrics.average_cpc,
  metrics.cost_micros,
  metrics.conversions,
  metrics.cost_per_conversion
FROM keyword_view
WHERE segments.date DURING LAST_30_DAYS
  AND ad_group_criterion.status = 'ENABLED'
  AND metrics.impressions > 100
ORDER BY metrics.cost_micros DESC
LIMIT 500
```

Hành động theo `quality_score` (chỉ có giá trị khi keyword đã đủ impression):
- QS ≤ 4 → sai message match. Sửa RSA headline hoặc chuyển keyword sang ad group đúng chủ đề (xem bảng message match trong `adgroup-map.md`).
- `post_click_quality_score` = BELOW_AVERAGE → lỗi landing page, không phải lỗi keyword. Chuyển sang `landing-page/` + đối chiếu Clarity.
- QS ≥ 8 + CPL dưới mục tiêu → tăng bid / tách campaign riêng để scale.

### Q4 — Keyword chi tiêu cao, zero conversion 30 ngày → tạm dừng

```sql
SELECT
  ad_group_criterion.keyword.text,
  ad_group_criterion.keyword.match_type,
  campaign.name,
  ad_group.name,
  metrics.cost_micros,
  metrics.clicks,
  metrics.conversions
FROM keyword_view
WHERE segments.date DURING LAST_30_DAYS
  AND metrics.conversions = 0
  AND metrics.cost_micros > 500000000
ORDER BY metrics.cost_micros DESC
```
(`500000000` micros = 500.000 ₫. Chỉnh ngưỡng theo CPL mục tiêu — quy tắc thường dùng: ngưỡng = 2× CPL mục tiêu.)

### Q5 — Đối chiếu campaign để phân bổ lại ngân sách

```sql
SELECT
  campaign.name,
  campaign.advertising_channel_type,
  campaign_budget.amount_micros,
  metrics.impressions,
  metrics.clicks,
  metrics.cost_micros,
  metrics.conversions,
  metrics.cost_per_conversion,
  metrics.search_impression_share,
  metrics.search_budget_lost_impression_share
FROM campaign
WHERE segments.date DURING LAST_30_DAYS
  AND campaign.status = 'ENABLED'
ORDER BY metrics.cost_micros DESC
```
`search_budget_lost_impression_share` > 0.20 ở campaign brand dự án = đang bỏ lỡ intent cao nhất vì thiếu tiền → dịch ngân sách từ campaign #5/#6 sang.

### Checklist tuần (~30 phút)

- [ ] Q1 → append negative mới vào `negative-keywords.csv`, upload lại negative list
- [ ] Q2 → append keyword/dự án mới vào `gen.py` / `projects.tsv`
- [ ] Q3 → xử lý keyword QS ≤ 4
- [ ] Q4 → pause keyword đốt tiền
- [ ] Q5 → dịch ngân sách theo impression share
- [ ] `python3 gen.py master-keywords.csv` → self-check pass
- [ ] `git commit` với message ghi rõ tuần ISO

---

## Hàng tháng — quét dự án mở bán mới

Prompt mẫu trong Claude Code:

> WebSearch + WebFetch các nguồn: cafeland.vn/du-an/tai-<tỉnh>/, batdongsan.com.vn/du-an-bat-dong-san-<tỉnh>, cafef.vn, vietnambiz.vn, vnexpress.net/bat-dong-san, trang chủ CĐT (vinhomes, masterisehomes, ecopark, sungroup, khangdien, namlongvn, novaland). Tìm dự án BĐS **mới mở bán / sắp mở bán / khởi công** trong 30 ngày qua tại <danh sách tỉnh>. Với mỗi dự án trả về `tên | CĐT | loại hình | khu vực | hạng`. Chỉ nhận dự án xuất hiện ở ≥2 nguồn độc lập. So sánh với `keywords/projects.tsv` và chỉ liệt kê dự án CHƯA có.

Rồi append vào `projects.tsv` và regenerate. Một dự án hạng A sinh 22 keyword, hạng B sinh 16.

**Lưu ý nguồn:** `batdongsan.com.vn` và `dothi.net` chặn WebFetch (HTTP 403) — dùng `cafeland.vn` (fetch được trang danh mục theo tỉnh) + WebSearch đối chiếu.

**Quy tắc chống bịa:** không thêm dự án nếu không xác nhận được ở ≥2 nguồn độc lập. Sai tên dự án = đốt ngân sách vào keyword không ai search, và tệ hơn là ad copy sai tên → policy strike.

### Việc khác hàng tháng

- **Đổi năm trong keyword**: các modifier chứa "2026" (`bảng giá 2026`, `dự án nào đáng đầu tư nhất 2026`) và negative `năm 2020`–`năm 2023` phải rà lại tháng 12 hàng năm. Thêm `năm 2024`, `năm 2025` vào negative khi chúng thành thông tin cũ.
- **Dự án đã bán hết / bàn giao xong**: hạ `uu_tien` xuống 3 hoặc xóa khỏi `projects.tsv`. Truy vấn của khách đã mua ("tiến độ xây dựng", "bàn giao khi nào") không tạo lead mới.
- **Sáp nhập hành chính**: từ 1/7/2025 Bình Dương + BR-VT nhập TP.HCM, Quảng Nam → Đà Nẵng, Bình Thuận → Lâm Đồng, Kiên Giang → An Giang, Bình Định/Phú Yên → Gia Lai, Ninh Thuận → Khánh Hòa. Bộ này **cố ý giữ tên cũ** vì người Việt vẫn gõ tên cũ. Khi search terms cho thấy tên tỉnh mới bắt đầu có volume, thêm vào `REGIONS` trong `gen.py` — **giữ cả hai**, đừng thay thế.

---

## Hàng quý — đối chiếu chéo

| Nguồn | Dùng để |
|---|---|
| MCP `analytics-ga4` | So conversion theo `sessionSource/Medium` với Google Ads. Lệch >20% = lỗi tracking, không phải lỗi keyword |
| MCP `clarity` | Rage/dead click trên form của LP nhận traffic từ ad group CPL cao (10 req/ngày, dữ liệu 3 ngày — dùng tiết kiệm) |
| Google Search Console | Query organic ranking top 3 mà vẫn đang bid → cân nhắc pause để dồn ngân sách (paid–organic cannibalization) |
| `content/` | Query T3_nghien_cuu có volume cao nhưng CPL xấu → chuyển từ ads sang bài SEO, giữ ads cho remarketing |

## Nhật ký thay đổi

| Ngày | Thay đổi | Số KW |
|---|---|---|
| 2026-07-28 | Khởi tạo: 107 khu vực, 239 dự án thật (quét web T7/2026), 44 CĐT, 256 negative | 8.512 |
| 2026-07-28 | +eco retreat (Ecopark, Bến Lức — phát hiện từ competitor research: có đạn bắn đối thủ, thiếu đạn giữ nhà) → 240 dự án | 8.534 |
| 2026-07-28 | Thêm `journey-strategy.md`: ma trận 48 modifier → 5 giai đoạn hành trình, phủ 100% bộ kw | 8.534 |
| 2026-07-28 | +210 biến thể không dấu cho negative-keywords.csv (negative KHÔNG khớp close variant — QA vòng 2) → 466 negative (386 account / 80 campaign) | 8.534 |
| 2026-07-28 | Vá war-game (SCORECARD): cơ chế **alias** cột 6 `projects.tsv` (+3 alias Eco Retreat: eco retreat long an / ecopark long an / forest onsen — dùng chung ad group `brand-eco-retreat`, không tách dự án); +5 dự án đất nền Long An (đức hòa new city, dragon pearl đức hòa, king hill residences, đất nam soluna, iris residence cần giuộc — mỗi dự án ≥2 nguồn) + 6 alias của chúng → 245 dự án; `LAND` đảo thứ tự loại hình cho 4 khu vực Long An (đất nền thành loại hình chính → đủ modifier + bản exact), cần giuộc B→A, chặn modifier `cau-hinh-can`/`san-sang-o` cho đất nền; +CĐT `prodezi` (LA Home); +8 negative **campaign-level** chống cannibalize sibling Ecopark (văn giang/van giang, sky oasis, solforest, haven park, đảo châu âu/dao chau au, ecovillage saigon river) → **473 dòng** negative (382 account / 91 campaign — số cũ "466" ở dòng trên đếm cả dòng header, thực tế là 465). Rà chéo §1.4.4: account-level chỉ còn conflict đã chấp nhận (`miễn phí` × 1 kw); 8 negative mới chặn **0** kw trong 88 kw campaign Eco Retreat. ⚠️ 8 dòng này PHẢI ở campaign-level: nếu áp lên account sẽ chặn 61 kw `uu_tien=1` của các dự án Ecopark Văn Giang | 8.805 |
| 2026-08-05 | **+dự án ĐANG PHÂN PHỐI: `blanca city`** (Sun Group, căn hộ, Vũng Tàu BR-VT, hạng A) + 4 alias `beachtro tower` / `blanca city vũng tàu` / `sun blanca city` / `beachtro tower vũng tàu` → 246 dự án, **+110 kw** ad group `brand-blanca-city`. Beachtro Tower là **phân khu** của Blanca City nên vào cột alias, KHÔNG tạo dòng riêng (luật dòng 2 `projects.tsv` + adgroup-map "1 ad group / dự án đang bán"). Xác minh 4 nguồn độc lập: vnexpress.net, dantri.com.vn, baodautu.vn, tinnhanhchungkhoan.vn (kick-off 30/07/2026, Thisky Hall Sala). · **+CĐT `sun property`** vào `DEVELOPERS` trong `gen.py` (+8 kw `brand-cdt--sun-property`): mọi nguồn đều gọi CĐT là "Sun Property (thành viên Sun Group)", bộ cũ chỉ có `sun group` → thiếu nhánh truy vấn thương hiệu BĐS thật. · QA: self-check gen.py OK, 0 keyword bị xóa, **rà chéo §1.4.4 = 0 xung đột** giữa 473 dòng negative và 118 kw mới. ⚠️ CHƯA thêm negative sibling (beacon tower / casa townhouse / casa villa / casa grand villa) — chờ user xác nhận có phân phối các phân khu đó không; xem PR mô tả | 8.923 |
