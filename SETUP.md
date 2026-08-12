# Setup credentials cho 4 MCP servers

`.mcp.json` đã cấu hình sẵn 4 server. Bạn chỉ cần cung cấp credentials qua biến môi trường (thêm vào `~/.bashrc` hoặc export trước khi mở Claude Code).

## 1. Google Ads API — ✅ ĐÃ KẾT NỐI 2026-08-05

Developer token của Smartland + OAuth refresh_token đã ráp xong. **File credential: `~/google-ads-smartland.yaml`** (chmod 600, đã trong `.gitignore` — KHÔNG commit, không dán vào chat).

- venv: `.venv-ads/` (`google-ads==31.0.0`, API **v24**) · script sinh token: `~/get_ads_refresh_token.py`
- Khuôn script chuẩn: xem `HUONG-DAN-KET-NOI-GG-ADS-CLAUDE.md` mục 5 — **bắt buộc** `client.login_customer_id = <ID account con>`, không thì query account con báo không thấy.

**Tài khoản đọc được (verify 2026-08-05):**

| ID | Tên | Loại | Tiền/TZ | Hiện trạng |
|---|---|---|---|---|
| `6918288556` | SMR- Sun Galaxy - 7490 - Mạnh | thường (không MCC) | VND / Asia/Saigon | **0 campaign, 0 ngân sách** — tài khoản trống, sẵn sàng dựng Beachtro. Có 1 conversion action: `7709665581` "Lượt gửi biểu mẫu khách hàng tiềm năng" (WEBPAGE, SUBMIT_LEAD_FORM, **primary**) |

⚠️ Refresh_token hiện tại chỉ thấy **1 account** này. Muốn thấy toàn bộ account con Smartland → sinh lại token bằng user quản lý MCC (chạy `~/get_ads_refresh_token.py`).

⚠️ `LAST_90_DAYS` KHÔNG phải date literal hợp lệ trong GAQL — dùng `LAST_30_DAYS` hoặc `segments.date BETWEEN "..." AND "..."`.

### Bẫy API v24 đã vấp thật (dựng campaign Beachtro 2026-08-06) — đọc trước khi VIẾT lên tài khoản

Mọi script mới: dùng `scripts/ads_client.py` (client + retry + đổi VND↔micros) thay vì viết lại boilerplate.

| # | Bẫy | Cách đúng |
|---|---|---|
| 1 | **Đơn vị micros**: 1 VND = 1.000.000 micros. Đặt `amount_micros=1_000_000` tưởng là 1tr đ nhưng thực ra là **1.000 đ** — lỗi im lặng, campaign vẫn tạo được | `vnd(1_000_000)` từ `ads_client.py`. Sau mọi mutate tiền bạc: **đọc lại bằng search để nghiệm thu** |
| 2 | Tạo campaign báo `REQUIRED ... contains_eu_political_advertising` | v24 bắt buộc: `cp.contains_eu_political_advertising = DOES_NOT_CONTAIN_EU_POLITICAL_ADVERTISING` |
| 3 | Negative cấp tài khoản: `CustomerNegativeCriterion.keyword` → `Unknown field` | Đường đúng 3 bước: `SharedSet` type `ACCOUNT_LEVEL_NEGATIVE_KEYWORDS` → nhét keyword bằng `SharedCriterionService` → gắn set bằng `CustomerNegativeCriterion.negative_keyword_list`. Đang dùng: set `NEG_BDS_Account_v1` (12184898936, 382 kw) |
| 4 | **RSA bất biến** — không sửa được headline của ad đã tạo | Sửa = tạo ad mới + remove ad cũ (2 operation) |
| 5 | Ảnh + logo doanh nghiệp bị `UNSUPPORTED_FIELD_TYPE` / `Customer is not verified` | KHÔNG phải lỗi code — `AD_IMAGE`/`BUSINESS_LOGO` yêu cầu **đã xác minh nhà quảng cáo**. Upload vào thư viện được ngay, gắn thì phải chờ verify. UI cũng không có mục Hình ảnh khi chưa verify |
| 6 | Structured snippet header tiếng Việt bị `invalid string value` | Header phải thuộc danh sách định sẵn. **Hợp lệ (đã probe)**: Tiện nghi, Thương hiệu, Điểm đến, Chương trình, Khóa học, Khách sạn nổi bật. KHÔNG hợp lệ: Loại hình, Kiểu dáng, Khu dân cư, Danh mục dịch vụ |
| 7 | `mutate_assets(..., validate_only=True)` → `unexpected keyword` | `validate_only` là field của **request object**: `req=get_type("MutateAssetsRequest"); req.validate_only=True; svc.mutate_assets(request=req)` |
| 8 | Thi thoảng `503 UNAVAILABLE ... ipv6 Network is unreachable` | Lỗi mạng tạm thời của máy, không phải tài khoản — `retry()` trong `ads_client.py` |
| 9 | **Keyword Planner hoạt động ngay** với credential hiện tại (không cần quyền thêm) | `KeywordPlanIdeaService.generate_keyword_historical_metrics` (volume bộ kw có sẵn) + `generate_keyword_ideas` (mở rộng). VN = geo `2704`, tiếng Việt = lang `1040` |
| 10 | Ad Strength đọc được qua API, kèm gợi ý sửa | `ad_group_ad.ad_strength` + `ad_group_ad.action_items`. **Ghim H1 = tụt thẳng POOR** — xem `campaign-setup.md §3` (đã sửa luật ghim 2026-08-06) |
| 11 | **SĐT trong headline/description = vi phạm policy `PHONE_NUMBER_IN_AD_TEXT`** (dính thật 2026-08-12: `Gọi Ngay 0937 837 888` → ad APPROVED_LIMITED, campaign LIMITED) | SĐT chỉ đi qua **call asset**. Trước khi ghi RSA lên tài khoản: grep headline+description, thấy chuỗi dạng SĐT là chặn. Sau khi ghi: đọc lại `policy_summary.policy_topic_entries`, không chỉ `approval_status` |
| 12 | GAQL `user_location_view` (và các view tương tự) báo `EXPECTED_REFERENCED_FIELD_IN_SELECT_CLAUSE` khi lọc `campaign.id` trong WHERE | Field dùng ở WHERE phải có mặt trong SELECT — thêm `campaign.id` vào SELECT là chạy |
| 13 | `keyword_view` đổi grain khi SELECT `segments.date`: 1 dòng/keyword/ngày thay vì 1 dòng/keyword (probe thật 12/08: 16 dòng → 58 dòng, tổng chi y hệt) | Lọc ngày ở WHERE thì metric đã gộp sẵn — chỉ SELECT `segments.date` khi thật sự cần theo ngày, và khi đó phải tự gộp theo (ad_group + keyword + match_type) |
| 14 | Response của lệnh ghi = "Google đã nhận", KHÔNG phải "trạng thái đúng như mình nghĩ" (bẫy #1 chỉ nói tiền — luật này là tổng quát) | Sau MỌI mutate: đọc lại đúng resource vừa đổi bằng search hẹp nhất (negative → đọc list; bid → đọc field bid; RSA → đọc asset + `policy_topic_entries`). Verify fail thì nói "chưa xác minh được", cấm nói "xong" |

### Bổ trợ: chỉ số qua GA4 (không bắt buộc nữa, vẫn nên link)

**Việc cần làm 1 lần cho mỗi dự án:** GA4 → Admin → **Product links → Google Ads links → Link** → chọn tài khoản Google Ads → bật *Enable personalized advertising* + *Enable auto-tagging*. Cần quyền Admin ở cả GA4 lẫn Google Ads.

Sau khi link, đọc được qua GA4 API (`run_report`):
- Metrics: `advertiserAdCost`, `advertiserAdClicks`, `advertiserAdImpressions`, `advertiserAdCostPerClick`, `advertiserAdCostPerKeyEvent`
- Dimensions: `sessionGoogleAdsCampaignName`, `sessionGoogleAdsAdGroupName`, `sessionGoogleAdsKeyword`, `sessionSourceMedium`

**Làm tay trên Google Ads UI** (API không thay được): search terms report (→ negative keywords hằng tuần), auction insights, sửa bid/budget/campaign.

### Đường A — Google Ads Script → Google Sheet (KHUYẾN NGHỊ khi không có developer token)

Không cần developer token, không cần billing, không cần quyền Quản trị — chỉ cần **quyền Chuẩn (Standard)** trên tài khoản Ads.

1. Tạo Google Sheet trống → copy URL.
2. Google Ads → **Công cụ → Thao tác hàng loạt → Tập lệnh** → **+** → dán `scripts/ads-export.js` → sửa `SHEET_URL` → **Chạy thử** → ủy quyền.
3. Đặt lịch **hằng ngày 04:00**.
4. Sheet → **File → Chia sẻ → Xuất bản lên web** → từng tab (`campaign_daily`, `search_terms`, `keyword_daily`) → định dạng **CSV** → copy 3 link, lưu vào `SETUP-secrets.md` (không commit) hoặc đưa Claude.

Hệ đọc 3 link CSV đó bằng `curl` — tự động, không cần credentials. Vẫn thiếu **auction insights** (Google Ads Script không truy cập được) → mục đó export tay hằng tuần.

### Đường B — Fallback export CSV tay (khi chỉ có quyền Xem)

Export CSV tay từ Google Ads UI (quyền Xem/Chuẩn là đủ), bỏ vào repo — Cowork/agent đọc file này thay cho GA4:

| File | Lấy ở đâu | Nhịp |
|---|---|---|
| `projects/<slug>/data/ads/campaign-daily-<yyyy-mm-dd>.csv` | Chiến dịch → thêm cột Ngày → Tải xuống CSV (chi phí, click, hiển thị, CTR, CPC, chuyển đổi, IS) | tuần |
| `projects/<slug>/data/ads/search-terms/<yyyy-mm-dd>.csv` | Chiến dịch → Thông tin chi tiết → Cụm từ tìm kiếm → Tải xuống | tuần |
| `projects/<slug>/data/ads/auction-insights-<yyyy-mm-dd>.csv` | Chiến dịch → Auction insights → Tải xuống | tuần (bắt buộc — GA4 không có dữ liệu này) |

⚠️ Export **theo ngày**, không lấy tổng kỳ — quét điểm gãy chuỗi thời gian (monitoring §4) cần dữ liệu ngày.

| Property GA4 | ID | Link Ads |
|---|---|---|
| Beachtro Tower - Blanca City | `548678683` | ⬜ chưa link |

## 2. GA4 MCP (`analytics-ga4`) — ✅ HOÀN TẤT 2026-07-28

✔ gcloud CLI cài tại `~/google-cloud-sdk` · ✔ ADC + scope analytics.readonly (account webdev@smartland.vn, project `omega-branch-503804-t3`, quota project set) · ✔ 2 API đã bật · ✔ env vars trong `~/.bashrc` · ✔ **Test Admin API thành công** — đọc được account "Smartland & Smartreltors" (properties: smartland.vn, smartrealtors.vn, Smartproperty, Gladia Height, Eco - Rừng Phượng...).

Việc cuối: **mở lại Claude Code** (để nhận env vars mới) → `/mcp` → `analytics-ga4` sẽ connected.

<details><summary>Hướng dẫn gốc (đã hoàn thành, giữ để tham khảo)</summary>

⚠️ **Lỗi "Ứng dụng này đã bị chặn"**: OAuth client mặc định của gcloud KHÔNG được Google cho xin scope `analytics.readonly` → bắt buộc tạo OAuth client riêng và truyền `--client-id-file`.

**Bước A — làm trong trình duyệt (console.cloud.google.com):**
1. Chọn/tạo project.
2. APIs & Services → **OAuth consent screen**: User type = External → điền tên app + email → **Test users: thêm chính email của bạn** (thiếu bước này sẽ bị chặn tiếp với lỗi `access_denied`).
3. APIs & Services → **Credentials → Create credentials → OAuth client ID → Desktop app** → Download JSON, lưu về `~/ga4-oauth-client.json`.

**Bước B — chạy từng lệnh một trong session Claude Code (tiền tố `! `, thay PROJECT_ID thật):**

```bash
! ~/google-cloud-sdk/bin/gcloud auth login
! ~/google-cloud-sdk/bin/gcloud config set project PROJECT_ID
! ~/google-cloud-sdk/bin/gcloud services enable analyticsadmin.googleapis.com analyticsdata.googleapis.com
! ~/google-cloud-sdk/bin/gcloud auth application-default login --client-id-file="$HOME/ga4-oauth-client.json" --scopes=https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/analytics.readonly
! ~/google-cloud-sdk/bin/gcloud auth application-default set-quota-project PROJECT_ID
```

Lưu ý: chạy **từng dòng riêng**, đừng dán cả khối (dấu `!` ở đầu dòng trong bash là history expansion, sẽ lỗi). Màn hình consent sẽ hiện cảnh báo "app chưa xác minh" — bấm Advanced → Go to (unsafe) → cho phép, an toàn vì app là của chính bạn.

Sau đó thêm vào `~/.bashrc`:
```bash
export GOOGLE_APPLICATION_CREDENTIALS="$HOME/.config/gcloud/application_default_credentials.json"
export GOOGLE_PROJECT_ID="PROJECT_ID"
```

Điều kiện cuối: tài khoản Google đăng nhập phải **có quyền đọc GA4 property** (Viewer trở lên trong GA4 Admin → Property access management). Xong hết → mở lại Claude Code → `/mcp` kiểm tra `analytics-ga4` connected.

</details>

## 3. Google Tag Manager MCP (`gtm`)
Không cần env var — dùng remote server của Stape (`https://gtm-mcp.stape.ai/mcp`), OAuth Google sẽ bật trình duyệt lần đầu kết nối.

## 4. Microsoft Clarity MCP (`clarity`) — ✅ HOÀN TẤT 2026-07-28

✔ Token Data.Export trong `~/.bashrc` (`CLARITY_API_TOKEN`) · ✔ **Test API 200 OK** (project-live-insights).

Giới hạn API: 10 request/ngày/project, dữ liệu 3 ngày gần nhất, tối đa 3 dimensions/request — kỷ luật dùng trong `tracking/clarity-checklist.md` §3. Dùng toàn trang: xem checklist §1.

## Kiểm tra
Mở lại Claude Code trong folder này → `/mcp` để xem trạng thái 4 server.
