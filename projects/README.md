# projects/ — hồ sơ từng dự án đang chạy ads

Mỗi dự án mình chạy ads = **một thư mục con** ở đây. Tài sản dùng chung (playbook, tracking spec, bộ sinh keyword) nằm ngoài, không copy vào từng dự án.

> ⚠️ **Đừng nhầm hai chữ "projects"**
> - `keywords/projects.tsv` = danh mục **245 dự án BĐS toàn thị trường VN**, chỉ dùng làm nguyên liệu sinh keyword. Có dự án ở đây **không** nghĩa là mình đang chạy ads cho nó.
> - `projects/<slug>/` (thư mục này) = **dự án mình thật sự chạy ads**, có tài khoản, có ngân sách, có người chịu trách nhiệm.
> Một dự án đang chạy ads phải có mặt ở **cả hai** chỗ.

## Cái gì riêng / cái gì chung

| Riêng từng dự án (`projects/<slug>/`) | Dùng chung (giữ nguyên chỗ cũ) |
|---|---|
| `PROJECT.md` — ID tài khoản, LP, KPI, trạng thái | `playbook/` — chiến lược, checklist, ngưỡng alert |
| `nghiem-thu.md` — nghiệm thu cổng đo của dự án | `tracking/` — spec GTM/GA4, registry 6 event |
| `ad-copy.md` — RSA headline/description | `keywords/gen.py`, `master-keywords.csv`, `negative-keywords.csv` |
| `keywords/brand.csv`, `keywords/negative.csv` | `scripts/` — ads-export.js, approve-bot, telegram |
| `data/ads/`, `data/ga4/` — export theo ngày | `content/` ở gốc — bài SEO không gắn dự án nào |
| `content/` — bài SEO gắn dự án | `research/` |

Landing page **không** nằm trong repo (user tự làm) — `PROJECT.md` chỉ ghi URL.

## Mở dự án mới

```bash
SLUG=ten-du-an
cp -r projects/_TEMPLATE projects/$SLUG
mkdir -p projects/$SLUG/{keywords,data/ads/search-terms,data/ga4,content}
```

Rồi:
1. Điền `projects/$SLUG/PROJECT.md` (ID Ads, GA4, GTM, URL LP, ngân sách, CPL mục tiêu).
2. Thêm dòng dự án vào `keywords/projects.tsv` → dispatch agent `keyword-planner` → `cd keywords && python3 gen.py master-keywords.csv`.
3. Lọc bộ brand keyword ra thư mục dự án (không cần script riêng):
   ```bash
   awk -F, 'NR==1 || $2=="brand-'$SLUG'"' keywords/master-keywords.csv > projects/$SLUG/keywords/brand.csv
   ```
4. Thêm dòng vào bảng "Dự án active" trong `COWORK.md`.
5. Làm việc trên nhánh `cowork/<slug>-<việc>`, PR về main — không push thẳng main.

## Nhịp file data

| File | Nguồn | Nhịp |
|---|---|---|
| `data/ads/campaign-daily-<yyyy-mm-dd>.csv` | Google Ads API hoặc export UI (theo NGÀY, không lấy tổng kỳ) | tuần |
| `data/ads/search-terms/<yyyy-mm-dd>.csv` | `FROM search_term_view` hoặc export UI | tuần |
| `data/ads/auction-insights-<yyyy-mm-dd>.csv` | **chỉ tải tay từ UI** — API bị chặn (allowlist Google đã đóng) | tuần, bắt buộc |
| `data/ga4/*.csv` | GA4 API | khi cần đối chiếu |
