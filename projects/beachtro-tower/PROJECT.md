# Beachtro Tower — Blanca City

| Mục | Giá trị |
|---|---|
| Chủ đầu tư | Sun Group (Sun Property) |
| Vị trí | Mặt tiền đường 3/2, P.10 & P.11, TP. Vũng Tàu — trong đại đô thị Blanca City (96 ha, 1 km bờ biển) |
| Loại hình | Căn hộ **sở hữu lâu dài** · 4 tòa E6–E9 · 1.785 căn · Studio → 3BR+ |
| Phạm vi bán | **CHỈ căn hộ Beachtro** (chốt 2026-08-06) — không bán biệt thự / shophouse / nhà phố trong Blanca City → 15 negative cấp campaign, xem `keywords/negative.csv` |
| Bàn giao | Dự kiến 8/2028 |
| Vai trò của ta | **Phân phối chính thức** (SmartRealtors & Partners) — không phải CĐT |
| Trạng thái | 🟢 **ĐANG CHẠY từ 2026-08-06** — bật theo lệnh user, BỎ QUA gate G0 → phanh cứng: lead đầu không có gclid trong Keap = PAUSE ngay |
| Ngày mở hồ sơ | 2026-08-05 |

## Cổng kết nối (verify 2026-08-06 bằng API thật)

| Cổng | ID | Trạng thái |
|---|---|---|
| Google Ads customer | `6918288556` (SMR- Sun Galaxy - 7490 - Mạnh) | ✅ API v24 · VND / Asia/Saigon · **1 campaign (PAUSED)** |
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
| Ngân sách/ngày | **1.000.000 ₫** (chốt 2026-08-06) | **1 campaign brand duy nhất** — `plan-chay-ads.md` |
| CPL mục tiêu | **chưa đặt** — chốt ở tuần 4 từ số thật | Tháng 1 dùng **kill rule cấu trúc**, không cắt theo giá (`plan-chay-ads.md §4`) |
| CPC trần | **28.000 ₫** (20k → 35k ngày bật → 28k ngày 12/08) | Hạ vì IS đã đạt 76%, mất-rank chỉ 24% — vài % thị phần cuối rất đắt, không đáng mua |
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

| Ad group | Tổng | `uu_tien=1` (bộ launch) | Volume/tháng thật |
|---|---|---|---|
| `brand-beachtro-tower` | 110 | 40 | **0** ⚠️ |
| `brand-blanca-city` | 110 | 41 | **18.520** |

Sinh từ `keywords/projects.tsv` (2 dòng: `beachtro tower` + `blanca city`, hạng A, kèm alias) → `gen.py`. File import sẵn: `keywords/launch-uu-tien-1.tsv` (**81 dòng**, campaign `BDS_Search_Brand_DuAn`) — quy tắc lọc: `uu_tien=1` **hoặc** có volume thật > 0 (thêm `blanca city vị trí`, 30 lượt/tháng).
Rà chéo negative account-level × 81 kw launch: **0 xung đột**.

⚠️ **Search volume thật (Keyword Planner API 2026-08-06)**: chỉ **9/220** keyword có volume (8 trong bộ launch gốc + `blanca city vị trí`), **toàn bộ ở "blanca city"** — tên "Beachtro" chưa ai gõ (0 volume). Ad group `brand-beachtro-tower` sẽ gần như 0 impression cho tới khi CĐT truyền thông tên tòa. Volume đã ghi thẳng vào `keywords/brand.csv` (5 cột `vol_thang`/`canh_tranh`/`bid_thap_d`/`bid_cao_d`/`ngay_do_volume`, đo 2026-08-06, **đo lại mỗi quý**). Bản chụp rời: `keywords/volume-2026-08-06.csv` + `keywords/keyword-ideas-2026-08-06.csv` (505 ý tưởng). Phân tích: `plan-chay-ads.md §1`.

Ad copy 2 bộ RSA: `ad-copy.md`. Plan chạy: `plan-chay-ads.md`.

## 🔴 Blocker chặn launch (theo thứ tự)

> **Chốt 2026-08-06: KHÔNG sửa GTM.** Chuỗi đo vẫn chạy — conversion Ads đến thẳng từ thẻ `awct` khi khách vào trang cảm ơn, không đi qua GA4. Giá phải trả: đếm trùng nếu F5 (bù bằng Count = Một), không dùng được Enhanced Conversions, không biết lead đến từ form/tòa nào. Chi tiết: `audit-lp.md`.

> **Chốt 2026-08-06 (đổi so với ban đầu): user yêu cầu agent dựng campaign qua API**, user tự vào UI duyệt trước khi bật.

### ✅ Đã dựng qua API — **ĐANG CHẠY từ 2026-08-06** (ENABLED · SERVING · 2 ad ĐÃ DUYỆT)

| Thành phần | Giá trị | ID |
|---|---|---|
| Campaign | `BDS_Search_Brand_DuAn` · **ENABLED/SERVING** · Search · Maximize Clicks | `24103805490` |
| Ngân sách | **1.000.000 ₫/ngày** (không dùng chung) | `15778630477` |
| Trần CPC | **28.000 ₫** (campaign + cả 2 ad group — 20k → 35k ngày bật → 28k ngày 12/08, verify qua API) | |
| Ad group | `brand-beachtro-tower` · `brand-blanca-city` | `195939193901` · `195939194061` |
| Keyword | **81** (40 exact + 41 phrase, 0 broad) | |
| RSA | 2 bộ, ghim H1, path `/bang-gia/2026` và `/blanca-city/can-ho` | |
| Asset | 6 sitelink + 4 callout (cấp campaign) | |
| Negative campaign | **15** (biệt thự/shophouse/nhà phố/… + bản không dấu) | |
| Negative tài khoản | shared set `NEG_BDS_Account_v1`, **382 keyword**, đã gắn | `12184898936` |
| Mạng | Search ✔ · Search Partners ✘ · Display ✘ | |
| Vị trí | Việt Nam (`2704`), **PRESENCE** | |
| Ngôn ngữ | Tiếng Việt + Tiếng Anh | |
| Lịch | 7 ngày, **05:00–24:00** | |
| Tracking template | UTM cấp tài khoản, đã gắn | |

### 🔴 Còn lại — user làm trên UI

| # | Việc | Ghi chú |
|---|---|---|
| 1 | ~~Duyệt + bật campaign~~ | ✅ ĐÃ BẬT 2026-08-06 theo lệnh user |
| 2 | ~~Gate G0~~ → thay bằng **phanh cứng D+1**: lead thật đầu tiên phải có `gclid` trong Keap, không có → PAUSE | user chốt bỏ qua G0 |
| 3 | Tắt **Tài sản tự động tạo (ACA)** + **Dynamic sitelinks** | API không expose, phải làm trên UI |
| 4 | Tắt **Auto-apply recommendations** (cấp tài khoản) | UI: Đề xuất → Tự động áp dụng → bỏ tick hết |
| 5 | Nộp **xác minh nhà quảng cáo** (Tổ chức, 3–5 ngày) — ⚠️ giờ là nút thắt của 2 loại tài sản: Google từ chối gắn cả **hình ảnh** lẫn **biểu tượng doanh nghiệp** với lỗi "Customer is not verified". Logo SmartRealtors (asset `404392250361`) + 4 ảnh đã nằm sẵn thư viện, xác minh xong là gắn được ngay. **Đọc theo costly signalling (Alchemy): xác minh là việc MARKETING chứ không phải hành chính** — huy hiệu "đã xác minh" là tín hiệu tốn công không ai giả được, đúng trục "chắc chắn hơn" của khách 35+ | user — **ưu tiên cao nhất trong các việc chờ** |

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
| 2026-08-06 | Mở hồ sơ trong `projects/`; audit LP (3,50/5); +2 dòng `projects.tsv` → 220 brand keyword; viết 2 bộ RSA |
| 2026-08-06 | Duyệt plan chạy ads: 1 campaign brand, 1tr₫/ngày, chưa đặt CPL mục tiêu |
| 2026-08-06 | Lấy volume thật từ Keyword Planner: **18.520** lượt/tháng, **toàn bộ ở "blanca city"**; "beachtro" = 0 |
| 2026-08-06 | Chốt phạm vi bán = chỉ căn hộ → 15 negative cấp campaign chặn biệt thự/shophouse/nhà phố/liền kề/đất nền/condotel |
| 2026-08-06 | Dựng campaign qua API (PAUSED): 2 ad group, 81 kw, 2 RSA, 6 sitelink anchor nội bộ, 8 callout, 2 snippet, call asset, UTM template, 382 negative account |
| 2026-08-06 | Target tuổi **35+** (loại 18-24, 25-34; GIỮ Unknown) — chốt user. +13 negative campaign chặn khách du lịch (vé/Sun World/công viên nước/tắm biển/resort) + thứ cấp (thanh lý/chuyển nhượng) → 28 negative campaign |
| 2026-08-06 | **BẬT CAMPAIGN** (lệnh user, bỏ qua gate G0): ENABLED · SERVING · 2 ad đã duyệt · bidding learning. Phanh cứng D+1: lead đầu phải có gclid |
| 2026-08-06 | Ad Strength: POOR/AVERAGE → **GOOD cả 2** (bỏ ghim H1 + đa dạng headline + vòng 2 nhồi keyword bộ beachtro). Ảnh: 4 file trong thư viện, tài khoản chưa đủ điều kiện gắn (UI không có mục Hình ảnh) — retry sau xác minh + 1-2 tuần chạy |

### 2026-08-12 — Tuần 2 mở màn
- **Hạ trần CPC 35.000₫ → 28.000₫** (campaign + 2 ad group) — lý do: IS đạt 76%, mất-rank chỉ 24%, vài % thị phần cuối quá đắt. Verify qua API.
- **Thêm RSA thứ 2 vào cả 2 ad group** (bộ v4, sau 3 vòng audit theo `research/books/` + research dự án):
  - `brand-blanca-city` → ad `820622531236`
  - `brand-beachtro-tower` → ad `820622531239`
  - 15 headline · 0 ghim · 4 description · ENABLED
- **12/08 chiều — dính policy `PHONE_NUMBER_IN_AD_TEXT`**: headline `Gọi Ngay 0937 837 888` vi phạm luật cấm SĐT trong ad text → cả 2 ad mới bị APPROVED_LIMITED, campaign gắn cờ LIMITED. Sửa: thay bằng `Gọi Tư Vấn Miễn Phí Hôm Nay`, tạo ad mới + xóa 2 ad lỗi (RSA bất biến). **Ad thay thế: blanca `820626531246` · beachtro `820626531249`.** Hotline không mất — call asset `404214595370` (0937837888) vẫn gắn campaign ENABLED. Bài học ghi `SETUP.md §1 bẫy #11`.
- **Phát hiện đổi chiến lược:** Sun World Vũng Tàu khai trương **12/02/2026**, tại trung tâm Blanca City — đã vận hành 6 tháng. Đây là Sinatra Test mạnh nhất (khách tự kiểm được), vá lỗ hổng **0/30 headline cũ có bằng chứng đang tồn tại**. Chi tiết: `research-du-an-2026-08-12.md`.
- ⚠️ **Hai thay đổi trong cùng ngày** (bid + RSA) → không tách được tác động riêng của từng cái. Khi đọc số tuần này phải nhớ điều đó; kỳ đo mới bắt đầu từ 13/08.
