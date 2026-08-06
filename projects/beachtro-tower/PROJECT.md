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

> **Chốt 2026-08-06: KHÔNG sửa GTM.** Chuỗi đo vẫn chạy — conversion Ads đến thẳng từ thẻ `awct` khi khách vào trang cảm ơn, không đi qua GA4. Giá phải trả: đếm trùng nếu F5 (bù bằng Count = Một), không dùng được Enhanced Conversions, không biết lead đến từ form/tòa nào. Chi tiết: `audit-lp.md`.

> **Chốt 2026-08-06: mọi thao tác trên tài khoản Google Ads do user tự làm trên UI.** Ở repo chỉ chuẩn bị dữ liệu, tài liệu, file import và lệnh kiểm tra. Agent chỉ **đọc** qua API để đối chiếu, không ghi.

| # | Việc | Ai làm |
|---|---|---|
| 1 | **Gate G0**: bắn 1 lead test thật → Ads có conversion ≤24h · Keap có `gclid` | user |
| 2 | Ads: import **382 negative cấp tài khoản** (hiện 1 dòng) — lệnh xuất danh sách ở `campaign-setup.md §1.4` | user (UI) |
| 3 | Ads: gắn **tracking URL template UTM** (hiện rỗng) — chuỗi ở `campaign-setup.md §1.5.9` | user (UI) |
| 4 | Dựng campaign `BDS_Search_Brand_DuAn` + 2 ad group + RSA + extensions, để **Tạm dừng** — dùng `keywords/launch-uu-tien-1.tsv` + `ad-copy.md` | user (UI/Editor) |
| 5 | Nộp **xác minh nhà quảng cáo** (Tổ chức, 3–5 ngày) | user |

### ✅ Đã đúng sẵn — không phải sửa (đọc API 2026-08-06)

| Mục | Giá trị | Đối chiếu spec |
|---|---|---|
| `counting_type` của conversion `7709665581` | **ONE_PER_CLICK** | ✔ `§1.2.3` — 1 lượt nhấp = tối đa 1 lead, trang cảm ơn load lại bao nhiêu lần cũng vậy |
| Cửa sổ chuyển đổi lượt nhấp | **90 ngày** | ✔ `§1.2.4` |
| Mô hình phân bổ | Dựa trên dữ liệu | ✔ `§1.2.5` |
| Trạng thái / danh mục | ENABLED · WEBPAGE · SUBMIT_LEAD_FORM · primary | ✔ `§1.2.7` |
| Gắn thẻ tự động (auto-tagging) | True | ✔ `§1.3.1` |

Lệch nhẹ, không chặn: **cửa sổ xem qua = 1 ngày** (spec `§1.2.5` là 30). Chỉ ảnh hưởng view-through conversion của Display — hiện chưa chạy Display nên không tác động.

## Nhận diện doanh nghiệp trên LP — chốt 2026-08-06: KHÔNG làm footer

LP công ty từ trước tới nay không chạy footer, và **không cần**: yêu cầu của Google là nhận diện được doanh nghiệp đứng sau trang, không phải một khối footer đúng khuôn. Trang này đã có sẵn, kiểm 2026-08-06:

- Section riêng **"SmartRealtors & Partners"** với nội dung giới thiệu đơn vị
- Dòng **"Phân phối chính thức SmartRealtors & Partners — đối tác chiến lược của Sun Group hơn 10 năm"**
- Hotline `0937 837 888` hiển thị ở nav + link `tel:`
- Link **Chính sách bảo mật & quyền riêng tư** ở mọi form

→ Miễn cả footer lẫn MST cho dự án này (`campaign-setup.md §1.1.4` là luật nội bộ chặt hơn thực tế). Dòng "Phân phối chính thức… đối tác chiến lược của Sun Group" đồng thời **thỏa ràng buộc #4 của `ad-copy.md`** — RSA được phép dùng chữ "phân phối chính thức" mà không dính lỗi mạo nhận CĐT. **Không được xóa dòng này khỏi LP.**

Rủi ro còn lại nếu Google vẫn từ chối vì thiếu thông tin doanh nghiệp: **thấp và đảo ngược được** — thêm khối thông tin rồi gửi duyệt lại trong ngày, không mất tài khoản.

## 🟡 Backlog (không chặn launch)

- LP: thêm **link + sticky Zalo** — CTA chính của khách VN đang thiếu hẳn
- GA4: đánh dấu key event (chỉ để báo cáo GA4 đọc được; Ads không phụ thuộc)
- Link GA4 ↔ Google Ads (cần quyền Quản trị Ads)
- Thêm 2 dropdown qualifying vào form **ngay khi có bảng giá**
- Hoãn: Clarity · sửa GTM về registry · `xem_bang_gia` / `xem_mat_bang`

## Nhật ký

| Ngày | Thay đổi |
|---|---|
| 2026-08-05 | Kết nối Google Ads API + GA4, nghiệm thu 2 cổng (`nghiem-thu.md`) |
| 2026-08-06 | Mở hồ sơ trong `projects/`; audit LP (3,50/5, rớt 2 hard gate); +2 dòng `projects.tsv` → 220 brand keyword; viết 2 bộ RSA |
