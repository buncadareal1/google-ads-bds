# COWORK — quy tắc làm việc trên cloud

Repo này là nền tảng vận hành Google Ads BĐS **đa dự án**. Mọi session Cowork bắt đầu bằng prompt dưới đây (copy nguyên khối, thay dòng cuối bằng việc cụ thể).

## Dự án active

| Dự án | Thư mục | CĐT | Vị trí | Trạng thái |
|---|---|---|---|---|
| **Beachtro Tower — Blanca City** | `projects/beachtro-tower/` | Sun Group | Vũng Tàu | Active từ 2026-08-05 · GA4 property `548678683` · Ads account `6918288556` (0 campaign — chưa launch) |

Mỗi dự án có hồ sơ riêng trong `projects/<slug>/` (PROJECT.md, keywords/, data/, ad-copy.md, nghiem-thu.md). Quy ước + cách mở dự án mới: `projects/README.md`. Dự án mới = copy `projects/_TEMPLATE/` + thêm dòng vào bảng này và `keywords/projects.tsv` (qua keyword-planner), không fork repo.

## Prompt khởi động session

```
Repo này là hệ thống vận hành Google Ads BĐS đa dự án. Dự án active: xem bảng trong
COWORK.md. Repo là nền tảng làm việc duy nhất.

QUY TẮC GIT: KHÔNG push vào main. Đầu session tạo nhánh mới từ main tên
`cowork/<dự-án>-<việc>` (ví dụ cowork/beachtro-keywords), mọi commit push vào nhánh đó.
Xong việc mở Pull Request về main kèm mô tả tiếng Việt — tôi review và merge,
Cowork không tự merge.

Trước khi làm bất cứ gì:
0. Hồ sơ dự án nằm ở `projects/<slug>/` — đọc `projects/README.md` + `projects/<slug>/PROJECT.md`
   trước khi đụng việc của dự án đó. File riêng dự án (data export, ad copy, keyword brand,
   nghiệm thu) ghi vào trong thư mục đó, KHÔNG rải ra gốc repo.
   ⚠️ `projects/` (dự án mình chạy ads) ≠ `keywords/projects.tsv` (245 dự án toàn thị trường).
1. Đọc CLAUDE.md và PLAN.md — tuân thủ tuyệt đối.
2. Đụng tracking → đọc tracking/README.md trước. Đụng LP → landing-page/README.md trước.
   Việc từ khóa → quy trình keywords/UPDATE.md, dispatch keyword-planner, không sửa tay.
3. Registry 6 event GA4 trong CLAUDE.md là nguồn chân lý — không đặt tên event mới.
4. Số liệu phải có nguồn, tính bằng script, không bịa benchmark. Ponytail: ngắn nhất chạy được.

Nhiệm vụ thường trực:
A. QUẢN LÝ CHỈ SỐ: nguồn chỉ số = **Google Ads API** (đã kết nối 2026-08-05, chi tiết
   SETUP.md §1) + GA4 + Clarity. ⚠️ Trên Cowork KHÔNG gọi được 3 cổng này (credentials
   ở máy local) → viết rõ truy vấn/việc cần chạy để user chạy local, KHÔNG giả lập số.
   Phân tích theo playbook/monitoring.md: ngưỡng alert, quét WoW điểm gãy §4, luật
   Simpson, exclusion áp cho cả phân tích §2.1.
   LƯU Ý 1: hệ KHÔNG đo lead (bỏ Keap API — user tự quản lý lead riêng). KPI vận hành =
   CPL raw (generate_lead) + chất lượng traffic, KHÔNG phải contact rate.
   LƯU Ý 2: **Auction Insights không đọc được qua API** (allowlist Google đã đóng) →
   luôn là việc tải tay hằng tuần, xem projects/beachtro-tower/nghiem-thu.md.
B. BÁO CÁO TELEGRAM: gửi báo cáo qua bot theo khung giờ trong monitoring.md, dùng
   TG_BOT_TOKEN + TG_CHAT_ID trong env vars. Tiếng Việt, đơn vị ₫, số liệu kèm nguồn,
   tách theo từng dự án active.
C. TOKEN/ID: khi tôi cung cấp ID mới (GTM-, G-, AW-, conversion labels) → cập nhật
   SETUP.md và file liên quan. Token bí mật chỉ vào env vars, TUYỆT ĐỐI không commit.
D. HỒ SƠ DỰ ÁN: dự án active chưa có trong keywords/projects.tsv → dispatch
   keyword-planner thêm dự án + sinh bộ từ khóa brand theo gen.py.

Giới hạn cloud: credential Google Ads (~/google-ads-smartland.yaml) và ADC của GA4 nằm
ở máy local, KHÔNG có trên Cowork → không gọi được Google Ads API / GA4 / GTM. Trên
Cowork chỉ có Clarity API + Telegram qua env vars (TG_BOT_TOKEN, TG_CHAT_ID,
CLARITY_API_TOKEN). Cần số từ 3 cổng kia thì viết sẵn script/GAQL để user chạy local,
không giả lập kết quả.

Việc hôm nay: [MÔ TẢ VIỆC CỤ THỂ]
```

## Việc Cowork LÀM ĐƯỢC / KHÔNG làm được

| Làm được trên Cowork | Phải làm ở local |
|---|---|
| Đọc/sửa toàn bộ tài liệu, playbook, checklist | Mọi lệnh gọi Google Ads API (dựng campaign, đọc chỉ số, negative) |
| Bộ từ khóa (keyword-planner, gen.py), negative list | Mọi lệnh gọi GA4 / GTM |
| Viết content SEO, RSA copy, kiểm ký tự | Apply thay đổi lên tài khoản Ads thật |
| Phân tích file CSV/export user tải về | |
| Clarity API + gửi Telegram (có env vars) | |

## Checklist trước khi mở session Cowork

1. Local đã commit + push (`git status` sạch).
2. Env vars của session: `TG_BOT_TOKEN`, `TG_CHAT_ID`, `CLARITY_API_TOKEN`.
3. Sau session: review PR trên GitHub → merge → local `git pull`.
