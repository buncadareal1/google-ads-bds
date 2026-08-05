# Setup credentials cho 4 MCP servers

`.mcp.json` đã cấu hình sẵn 4 server. Bạn chỉ cần cung cấp credentials qua biến môi trường (thêm vào `~/.bashrc` hoặc export trước khi mở Claude Code).

## 1. Chỉ số Google Ads — ⛔ KHÔNG DÙNG API (chốt 2026-08-05)

Bỏ Google Ads API / developer token / MCC. **Chỉ số Ads lấy qua GA4** bằng tài khoản `webdev@smartland.vn` (ADC ở mục 2 đã đủ quyền).

**Việc cần làm 1 lần cho mỗi dự án:** GA4 → Admin → **Product links → Google Ads links → Link** → chọn tài khoản Google Ads → bật *Enable personalized advertising* + *Enable auto-tagging*. Cần quyền Admin ở cả GA4 lẫn Google Ads.

Sau khi link, đọc được qua GA4 API (`run_report`):
- Metrics: `advertiserAdCost`, `advertiserAdClicks`, `advertiserAdImpressions`, `advertiserAdCostPerClick`, `advertiserAdCostPerKeyEvent`
- Dimensions: `sessionGoogleAdsCampaignName`, `sessionGoogleAdsAdGroupName`, `sessionGoogleAdsKeyword`, `sessionSourceMedium`

**Làm tay trên Google Ads UI** (API không thay được): search terms report (→ negative keywords hằng tuần), auction insights, sửa bid/budget/campaign.

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
