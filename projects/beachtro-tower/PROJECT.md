# Beachtro Tower — Blanca City

| Mục | Giá trị |
|---|---|
| Chủ đầu tư | Sun Group (Sun Property) |
| Vị trí | Mặt tiền đường 3/2, P.10 & P.11, TP. Vũng Tàu — trong đại đô thị Blanca City (96 ha, 1 km bờ biển) |
| Loại hình | Căn hộ **sở hữu lâu dài** · 4 tòa E6–E9 · 1.785 căn · Studio → 3BR+ |
| Bàn giao | Dự kiến 8/2028 |
| Vai trò của ta | **Phân phối chính thức** (SmartRealtors & Partners) — không phải CĐT |
| Trạng thái | ⬜ **chưa launch** — Ads account trống, LP live nhưng còn 4 việc chặn |
| Ngày mở hồ sơ | 2026-08-05 |

## Cổng kết nối (verify 2026-08-06 bằng API thật)

| Cổng | ID | Trạng thái |
|---|---|---|
| Google Ads customer | `6918288556` (SMR- Sun Galaxy - 7490 - Mạnh) | ✅ API v24 · VND / Asia/Saigon · **0 campaign** |
| Google Ads conversion id | `18359425041` · label `rRYqCK3SoNwcEJGwurJE` | ✅ đã gắn trong GTM |
| GA4 property | `548678683` · measurement `G-RRXWDGQ206` | ✅ có dữ liệu · ❌ **0 key event** · ❌ chưa link Ads |
| GTM | `GTM-TKDNJXJ9` (account `6353959536` / container `260355978` / workspace `6`) | ✅ đã publish |
| Clarity | — | ❌ chưa cài |
| Landing page | `https://smartrealtors.vn/beachtro-tower-blanca-city/` | ✅ live · audit: `audit-lp.md` (3,50/5) |
| Trang cảm ơn | `/thank-you/cam-on-dang-ky-beachtro-tower-blanca-city/` | ✅ HTTP 200 |
| CRM | Keap form xid `c661fd73838c0b58bfab553297fd79fd` (`rhq551.infusionsoft.com`) | ✅ nhận gclid/UTM qua `inf_custom_url` |
| Hotline | `0937 837 888` | ✅ trên LP |
| Sheet export (`scripts/ads-export.js`) | `[chưa tạo]` | ⬜ đường A dự phòng |

## Ngân sách & KPI

| Chỉ số | Mục tiêu | Ghi chú |
|---|---|---|
| Ngân sách/ngày | `[user chốt]` | Kịch bản mẫu 30tr₫/tháng = 1.000.000 ₫/ngày (`campaign-setup.md §2.1`) |
| CPL raw | `[điền từ tuần chạy đầu]` | Hệ **không đo lead sau đó** — KPI là CPL raw + chất lượng traffic |
| CPC trần #1 Brand | **20.000 ₫** | Theo `campaign-setup.md §2.2` cho campaign brand |
| IS brand | ≥ 80% | Ngưỡng `monitoring.md §4` |

⚠️ **Giai đoạn pre-launch, chưa có bảng giá** → CPL raw sẽ rẻ giả tạo (LP không có rào tài chính). Không so CPL giai đoạn này với giai đoạn sau khi công bố giá.

## Conversion action

| # | Tên | ID | Trạng thái |
|---|---|---|---|
| 1 | Lượt gửi biểu mẫu KH tiềm năng (WEBPAGE · SUBMIT_LEAD_FORM · primary) | `7709665581` | ✅ có, đang bắn từ GTM |
| 2 | Click_Hotline | — | ❌ thiếu (LP chưa bắn `phone_click`) |
| 3 | Click_Zalo | — | ❌ thiếu (**LP chưa có link Zalo**) |
| 4–6 | 3 action offline (ECL) | — | ⛔ đóng băng — hệ không đo lead |

## Bộ từ khóa

`keywords/brand.csv` — **220 keyword**, 2 ad group:

| Ad group | Tổng | `uu_tien=1` (bộ launch) |
|---|---|---|
| `brand-beachtro-tower` | 110 | 40 |
| `brand-blanca-city` | 110 | 40 |

Sinh từ `keywords/projects.tsv` (2 dòng: `beachtro tower` + `blanca city`, hạng A, kèm alias) → `gen.py`. File import sẵn: `keywords/launch-uu-tien-1.tsv` (80 dòng, campaign `BDS_Search_Brand_DuAn`).
Rà chéo negative account-level × 80 kw launch: **0 xung đột**.

Ad copy 2 bộ RSA: `ad-copy.md`.

## 🔴 Blocker chặn launch (theo thứ tự)

| # | Việc | Ai làm |
|---|---|---|
| 1 | LP: thêm **footer pháp nhân + MST + địa chỉ** (thiếu = rủi ro disapproved) | user |
| 2 | GTM: trigger Custom Event `generate_lead` cho cả tag Ads + GA4; đổi tên event GA4 `gui_form_beachtro_tower` → `generate_lead` | tôi (GTM API) |
| 3 | GA4: **đánh dấu key event** `generate_lead` (hiện 0 key event) | user (GA4 UI) |
| 4 | Ads: import **382 negative cấp tài khoản** (hiện 1 dòng) | tôi (Ads API) |
| 5 | Ads: gắn **tracking URL template UTM** (hiện rỗng) | tôi (Ads API) |
| 6 | **Gate G0**: bắn 1 lead test thật → GA4 Realtime có `generate_lead` · Ads có conversion ≤24h · Keap có `gclid` | user + tôi |
| 7 | Dựng campaign `BDS_Search_Brand_DuAn` + 2 ad group + RSA + extensions, để **Tạm dừng** | tôi (Ads API) — **chờ user duyệt ngân sách** |
| 8 | Nộp **xác minh nhà quảng cáo** (Tổ chức, 3–5 ngày) | user |

## 🟡 Backlog tuần đầu (không chặn launch)

- LP: thêm **link + sticky Zalo** (CTA chính của khách VN đang thiếu hẳn), bắn `zalo_click` / `phone_click`
- Gắn **Clarity** vào container GTM
- Link GA4 ↔ Google Ads (cần quyền Quản trị Ads)
- Thêm 2 dropdown qualifying vào form **ngay khi có bảng giá**
- Event `xem_bang_gia` / `xem_mat_bang` khi có bảng giá thật

## Nhật ký

| Ngày | Thay đổi |
|---|---|
| 2026-08-05 | Kết nối Google Ads API + GA4, nghiệm thu 2 cổng (`nghiem-thu.md`) |
| 2026-08-06 | Mở hồ sơ trong `projects/`; audit LP (3,50/5, rớt 2 hard gate); +2 dòng `projects.tsv` → 220 brand keyword; viết 2 bộ RSA |
