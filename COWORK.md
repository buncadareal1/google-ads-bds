# COWORK — quy tắc làm việc trên cloud

Repo này là nền tảng vận hành Google Ads BĐS **đa dự án**. Mọi session Cowork bắt đầu bằng prompt dưới đây (copy nguyên khối, thay dòng cuối bằng việc cụ thể).

## Dự án active

| Dự án | CĐT | Vị trí | Trạng thái |
|---|---|---|---|
| **Beachtro Tower — Blanca City** | Sun Group | Vũng Tàu | Active từ 2026-08-05 |

Dự án mới: thêm dòng vào bảng này + `keywords/projects.tsv` (qua keyword-planner), không fork repo.

## Prompt khởi động session

```
Repo này là hệ thống vận hành Google Ads BĐS đa dự án. Dự án active: xem bảng trong
COWORK.md. Repo là nền tảng làm việc duy nhất.

QUY TẮC GIT: KHÔNG push vào main. Đầu session tạo nhánh mới từ main tên
`cowork/<dự-án>-<việc>` (ví dụ cowork/beachtro-keywords), mọi commit push vào nhánh đó.
Xong việc mở Pull Request về main kèm mô tả tiếng Việt — tôi review và merge,
Cowork không tự merge.

Trước khi làm bất cứ gì:
1. Đọc CLAUDE.md và PLAN.md — tuân thủ tuyệt đối.
2. Đụng tracking → đọc tracking/README.md trước. Đụng LP → landing-page/README.md trước.
   Việc từ khóa → quy trình keywords/UPDATE.md, dispatch keyword-planner, không sửa tay.
3. Registry 6 event GA4 trong CLAUDE.md là nguồn chân lý — không đặt tên event mới.
4. Số liệu phải có nguồn, tính bằng script, không bịa benchmark. Ponytail: ngắn nhất chạy được.

Nhiệm vụ thường trực:
A. QUẢN LÝ CHỈ SỐ: theo dõi chỉ số nền tảng theo playbook/monitoring.md — Ads
   (CPC/CTR/IS/conv on-site), GA4 events, Clarity. Ngưỡng alert, quét WoW điểm gãy §4,
   luật Simpson, exclusion áp cho cả phân tích §2.1.
   LƯU Ý: hệ KHÔNG đo lead (đã chốt 2026-08-05, bỏ Keap API — user tự quản lý lead
   riêng). KPI vận hành = CPL raw (generate_lead) + chất lượng traffic.
B. BÁO CÁO TELEGRAM: gửi báo cáo qua bot theo khung giờ trong monitoring.md, dùng
   TG_BOT_TOKEN + TG_CHAT_ID trong env vars. Tiếng Việt, đơn vị ₫, số liệu kèm nguồn,
   tách theo từng dự án active.
C. TOKEN/ID: khi tôi cung cấp ID mới (GTM-, G-, AW-, conversion labels) → cập nhật
   SETUP.md và file liên quan. Token bí mật chỉ vào env vars, TUYỆT ĐỐI không commit.
D. HỒ SƠ DỰ ÁN: dự án active chưa có trong keywords/projects.tsv → dispatch
   keyword-planner thêm dự án + sinh bộ từ khóa brand theo gen.py.

Giới hạn cloud: không có Google Ads API / GA4 ADC / GTM OAuth — chỉ Clarity API và
Telegram qua env vars (TG_BOT_TOKEN, TG_CHAT_ID, CLARITY_API_TOKEN). Việc cần
credentials local thì ghi chú vào PLAN.md mục chờ, không giả lập kết quả.

Việc hôm nay: [MÔ TẢ VIỆC CỤ THỂ]
```

## Checklist trước khi mở session Cowork

1. Local đã commit + push (`git status` sạch).
2. Env vars của session: `TG_BOT_TOKEN`, `TG_CHAT_ID`, `CLARITY_API_TOKEN`.
3. Sau session: review PR trên GitHub → merge → local `git pull`.
