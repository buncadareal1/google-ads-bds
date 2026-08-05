# Hệ thống Google Ads BĐS

Repo này là hệ thống vận hành Google Ads cho bất động sản VN — **nền tảng dùng chung cho NHIỀU dự án** (playbook/tracking/keywords là tài sản chung, mỗi dự án chỉ thêm bộ kw + LP + chỉ số riêng). Đọc `PLAN.md` trước.
**Dự án đang active: BEACHTRO TOWER — Blanca City (Sun Group, Vũng Tàu).** Dự án mới = thêm vào `keywords/projects.tsv` + mục riêng trong COWORK.md, không fork repo.

- `playbook/` — chiến lược campaign, keyword, ad copy, checklist tuần
- `landing-page/` — template LP Astro (chuẩn skill `no-code-landing-re`, có `ad-click-attribution`)
- `tracking/` — spec GTM/GA4/Clarity + pipeline ECL. **Đụng vào đo lường: đọc `tracking/README.md` TRƯỚC** (bản đồ + 6 luật bất di bất dịch + skill nào cho việc nào)
- `landing-page/` — **làm/review/audit LP: đọc `landing-page/README.md` TRƯỚC** (message match, above the fold, khung phân tích điểm yếu CVR, checklist nghiệm thu 10 mục)
- `content/` — bài SEO hỗ trợ (chuẩn `seo-machine`)
- **Lead: NGOÀI PHẠM VI hệ (chốt 2026-08-05)** — bỏ Keap API, hệ KHÔNG đo lead; user tự quản lý lead riêng. Pipeline ECL trong `tracking/` đóng băng.
- **Google Ads API ĐÃ KẾT NỐI (2026-08-05)** — credential `~/google-ads-smartland.yaml`, venv `.venv-ads/`, API v24. Account đang dùng: `6918288556` (SMR- Sun Galaxy, VND, **trống — chưa có campaign**). Gọi bằng script Python, KHÔNG dùng MCP `google-ads` (ghim MCC khác). Luôn set `client.login_customer_id = ACCOUNT`. Chi tiết + bẫy: `SETUP.md §1`.
- MCP: dùng `analytics-ga4` + `clarity` + `gtm`. Credentials xem `SETUP.md`
- Cowork (cloud): quy tắc làm việc + prompt khởi động trong `COWORK.md` — push nhánh `cowork/*`, không push main

Quy ước: nội dung tiếng Việt, đơn vị ₫, số điện thoại/Zalo là CTA chính. Event GA4 chuẩn (registry duy nhất — LP và tracking/ phải khớp): `generate_lead`, `phone_click`, `zalo_click`, `xem_bang_gia`, `xem_mat_bang`, `form_start`.

## Vận hành
- **Fable 5 (main agent) = Project Manager + QA.** Mọi output của subagent phải qua QA trước khi coi là xong: kiểm tra chéo event names (LP↔tracking), message match (keyword↔ad copy↔LP), số liệu phải có nguồn, không bịa benchmark.
- Subagent làm việc = model Opus, chạy song song, mỗi agent một thư mục riêng, không sửa file ngoài phạm vi.
- `keywords/` là tài sản sống: update hàng tuần từ search terms report (quy trình trong `keywords/UPDATE.md`). **Mọi việc về từ khóa → dispatch agent `keyword-planner`** (định nghĩa trong `.claude/agents/keyword-planner.md`, model Opus).
- Ponytail: giải pháp ngắn nhất chạy được; không thêm campaign type/công cụ khi chưa có data chứng minh cần.
