# Beachtro Tower — Blanca City

| Mục | Giá trị |
|---|---|
| Chủ đầu tư | Sun Group |
| Vị trí | Blanca City, Vũng Tàu (BR-VT) |
| Loại hình | căn hộ nghỉ dưỡng ven biển |
| Trạng thái | ⬜ **chưa launch** — tài khoản Ads trống, 0 campaign |
| Ngày mở hồ sơ | 2026-08-05 |

## Cổng kết nối

| Cổng | ID | Trạng thái |
|---|---|---|
| Google Ads customer | `6918288556` (SMR- Sun Galaxy - 7490 - Mạnh) | ✅ đọc được qua API v24, VND / Asia/Saigon, 0 campaign |
| GA4 property | `548678683` | ✅ đọc được qua API · ❌ chưa link Google Ads · 1 session test |
| GTM container | `[chưa có]` | ⬜ |
| Clarity project | `[chưa có]` | ⬜ |
| Sheet export (`scripts/ads-export.js`) | `[chưa tạo]` | ⬜ đường A dự phòng |
| Landing page | `[chưa có URL]` | ⬜ user tự làm, theo `tracking/lp-requirements.md` |

Chi tiết nghiệm thu 2 cổng: `nghiem-thu.md` (cùng thư mục).

## Ngân sách & KPI

| Chỉ số | Mục tiêu | Ghi chú |
|---|---|---|
| Ngân sách/ngày | `[điền từ tuần chạy đầu]` | |
| CPL mục tiêu | `[điền từ tuần chạy đầu]` | KPI = CPL raw (`generate_lead`) — hệ KHÔNG đo lead sau đó (chốt 2026-08-05) |
| CPC trần | `[điền từ tuần chạy đầu]` | |
| IS brand | ≥ 80% | ngưỡng chuẩn campaign brand, `playbook/monitoring.md §4` |

## Conversion action (đối chiếu `playbook/campaign-setup.md §1.2`)

| # | Tên | ID | Trạng thái |
|---|---|---|---|
| 1 | Lượt gửi biểu mẫu khách hàng tiềm năng (WEBPAGE · SUBMIT_LEAD_FORM · primary) | `7709665581` | ✅ có |
| 2 | Click_Hotline | — | ❌ thiếu |
| 3 | Click_Zalo | — | ❌ thiếu |
| 4–6 | 3 action offline (ECL) | — | ⛔ đóng băng — hệ không đo lead |

Conversion tracking: `MANAGED_BY_SELF`, id `18359425041`.

## Blocker đang treo (theo thứ tự)

- [ ] LP thật + GTM bắn đúng **6 event registry** — hiện GA4 nhận `view_content`, **sai registry**
- [ ] Đánh dấu key event trong GA4 — hiện **0 key event**
- [ ] Tạo đủ conversion action còn thiếu + import từ GA4
- [ ] Import **382 negative cấp tài khoản** — hiện mới 1 dòng
- [ ] Gắn tracking URL template (UTM) — hiện **rỗng** (auto-tagging đã bật ✔)
- [ ] Dựng campaign theo `playbook/campaign-setup.md §2`
- [ ] Thêm "beachtro tower" / "blanca city" vào `keywords/projects.tsv` → sinh bộ brand kw → lọc ra `keywords/brand.csv`

## Nhật ký

| Ngày | Thay đổi |
|---|---|
| 2026-08-05 | Kết nối Google Ads API + GA4, nghiệm thu 2 cổng |
| 2026-08-06 | Mở hồ sơ dự án trong `projects/` |
