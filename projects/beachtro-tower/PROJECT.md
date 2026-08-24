# Beachtro Tower — Blanca City

| Mục | Giá trị |
|---|---|
| Chủ đầu tư | Sun Group (Sun Property) |
| Vị trí | Mặt tiền đường 3/2, P.10 & P.11, TP. Vũng Tàu — trong đại đô thị Blanca City (96 ha, 1 km bờ biển) |
| Loại hình | Căn hộ **sở hữu lâu dài** · 4 tòa E6–E9 · 1.785 căn · Studio → 3BR+ |
| Phạm vi bán | **CHỈ căn hộ Beachtro** (chốt 2026-08-06) — không bán biệt thự / shophouse / nhà phố trong Blanca City → 15 negative cấp campaign, xem `keywords/negative.csv` |
| Bàn giao | Dự kiến 8/2028 |
| Vai trò của ta | **Phân phối chính thức** (SmartRealtors & Partners) — không phải CĐT |
| Trạng thái | 🟢 **ĐANG CHẠY — bật lại 2026-08-18** (kỳ đo 2). Kỳ 1 (06–18/08): 7,15tr · 274 click · 4 conv Ads · 6 lead CRM / 2 F1 · CPL 1,19tr. Display đã tắt 15/08, không bật lại |
| Ngày mở hồ sơ | 2026-08-05 |

## Cổng kết nối (verify 2026-08-06 bằng API thật)

| Cổng | ID | Trạng thái |
|---|---|---|
| Google Ads customer | `6918288556` (SMR- Sun Galaxy - 7490 - Mạnh) | ✅ API v24 · VND / Asia/Saigon · **1 campaign ENABLED (từ 06/08)** |
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
| CPC trần | **35.000 ₫** (20k → 35k ngày bật → 28k ngày 12/08 → 35k ngày 14/08) | Đảo lại sau Auction Insights: pqr.vn bid đè (trên mình 92% khi cùng hiện) — lệnh user 14/08 |
| IS brand | guardrail ≥65% (`ops/change-log.jsonl` 12/08) · cảnh báo −15đ WoW (`monitoring.md §4`) |

⚠️ **Giai đoạn pre-launch, chưa có bảng giá** → CPL raw sẽ rẻ giả tạo (LP không có rào tài chính). Không so CPL giai đoạn này với giai đoạn sau khi công bố giá.

## Conversion action

| # | Tên | ID | Trạng thái |
|---|---|---|---|
| 1 | Lượt gửi biểu mẫu KH tiềm năng (WEBPAGE · SUBMIT_LEAD_FORM · primary) | `7709665581` | ✅ có, đang bắn từ GTM |
| 2 | Cuộc gọi từ quảng cáo (>=60s) (AD_CALL · PHONE_CALL_LEAD · **secondary**) | `7718436367` | ✅ bật 12/08 — đo cuộc gọi từ SỐ TRÊN AD (call asset). Click hotline TRÊN LP vẫn không đo |
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
| Trần CPC | **35.000 ₫** (campaign + cả 2 ad group — 20k → 35k ngày bật → 28k ngày 12/08 → 35k ngày 14/08, verify qua API) | |
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
| 5 | ~~Nộp xác minh nhà quảng cáo~~ | ✅ **ĐÃ DUYỆT — xác nhận 12/08 bằng probe API** (lỗi "Customer is not verified" biến mất). Logo `404392250361` đã gắn cấp tài khoản qua API (ENABLED, verify read-back). |
| 6 | **Gắn 4 ảnh vào campaign trên UI**: Chiến dịch → Tài sản → Hình ảnh (mục này giờ mới hiện). 4 ảnh có sẵn trong thư viện: `404213620169` (ngang 1200×628) · `404213620172` (vuông 1200×1200) · `404213620181` (vuông 566×566) · `404315555485` (ngang 1200×628) | user — API bị chặn allowlist (`SETUP.md` bẫy #16), chỉ UI làm được |

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
- **12/08 chiều — dính policy `PHONE_NUMBER_IN_AD_TEXT`**: headline `Gọi Ngay 0937 837 888` vi phạm luật cấm SĐT trong ad text → cả 2 ad mới bị APPROVED_LIMITED, campaign gắn cờ LIMITED. Sửa: thay bằng `Gọi Tư Vấn Miễn Phí Hôm Nay`, tạo ad mới + xóa 2 ad lỗi (RSA bất biến). **Ad thay thế: blanca `820626531246` · beachtro `820626531249`.** Hotline không mất — call asset `404214595370` (0937837888) vẫn gắn campaign ENABLED. Bài học ghi `SETUP.md §1 bẫy #11`. Cờ LIMITED của campaign đã tự gỡ sau khi xóa 2 ad.
- **12/08 chiều — đại tu kỷ luật hệ (audit 3 mũi: quy trình + đo lường + cấu hình tài khoản)**: push 33 commit tồn đọng lên origin; đồng bộ trạng thái campaign ở 5 file nói ngược nhau; thống nhất ngưỡng negative (~120 click cho 0-conv); sửa CRLF làm export sót 8 negative campaign; chốt 1 tiêu chí thoát Max Clicks duy nhất (`plan-chay-ads.md §1`); tắt MCP `google-ads` trong settings (luật đã cấm mà config còn mở); tạo `scripts/ghi.py` (cổng ghi cưỡng chế read-back + chặn SĐT); `ops/ngay-hong.txt` + nhắc việc-đến-hạn trong `bao_cao.py`.
- **12/08 chiều — BẬT ĐO CUỘC GỌI TỪ QUẢNG CÁO** (phát hiện audit: call asset để `call_conversion_reporting_state=DISABLED` trong khi tuần 1 có **17 click gọi từ ad không được đo** vs 3 lead form đo được): tạo action `7718436367` AD_CALL >=60s **SECONDARY** (không đổi định nghĩa cột conversions giữa kỳ), trỏ asset vào, verify read-back. Cửa sổ click 60 ngày (90 bị TOO_HIGH — bẫy #15).
- **⚠️ Luật đọc số mới (audit đo lường)**: CVR/CPL CHỈ đọc từ Ads. GA4 `gui_form_beachtro_tower` bắn theo MỖI pageview trang cám ơn → tuần 1 GA4 đếm 5 vs Ads 3 vs khách thật 2 (thổi +67%). Ca 10/08: 1 lượt trang cám ơn nguồn `infusionsoft.com/referral`, 0 conv Ads — cần tra Keap ngày 10/08 để phân định lead-mất-attribution vs conversion-ma.

### 2026-08-14 — Auction Insights đầu tiên (kỳ 30/07–13/08, file `data/ads/auction-insights-2026-08-14.csv`)
- Mình: IS 67,81% · đầu-trang 78,52% · abs-top 37,78%. **6 domain đang đấu brand Blanca City.**
- **pqr.vn là đối thủ nặng nhất** (user xác nhận 14/08: KHÔNG liên quan gì đến mình): IS 32,80%, trùng lặp 39,78%, khi cùng hiển thị thì **đứng trên mình 92,18%**, abs-top 64,78% (gần gấp đôi mình) — họ bid mạnh hơn hẳn.
- Còn lại 4 domain sàn phân phối nhỏ (IS <10–17%): vungtaublancacity.com, vungtau-sungroup.com.vn, sungroupblancacity.com.vn, sunmiennam.vn, blanca-vungtau.vn — bình thường với brand CĐT lớn, chưa cần phản ứng.
- Bối cảnh đọc số: pos-above của đối thủ cao một phần là hệ quả **mình hạ bid 12/08** — kỳ này trộn 2 chế độ bid (35k trước 12/08, 28k sau), so kỳ sau phải nhớ.
- **Phát hiện đổi chiến lược:** Sun World Vũng Tàu khai trương **12/02/2026**, tại trung tâm Blanca City — đã vận hành 6 tháng. Đây là Sinatra Test mạnh nhất (khách tự kiểm được), vá lỗ hổng **0/30 headline cũ có bằng chứng đang tồn tại**. Chi tiết: `research-du-an-2026-08-12.md`.
- ⚠️ **Hai thay đổi trong cùng ngày** (bid + RSA) → không tách được tác động riêng của từng cái. Khi đọc số tuần này phải nhớ điều đó; kỳ đo mới bắt đầu từ 13/08.

### 2026-08-15 — TẮT MẠNG DISPLAY: rò ~50% ngân sách suốt 2 ngày, 0 lead

- **Triệu chứng (14/08)**: impr nhảy 389 → 2.488 (×6), CTR tụt 4,4% → 1,9%, chi chạm 1,14tr. Ban đầu tưởng hệ quả nâng bid 35k.
- **Chẩn đoán (15/08)**: search terms ngày 14/08 chỉ giải thích **249/2.488 impr** (10%). Soi `segments.ad_network_type` → campaign đang chạy CẢ mạng CONTENT vì `network_settings.target_content_network=True` (Display Expansion — mặc định của Google khi dựng Search campaign).
- **Thiệt hại**: CONTENT 54 click · **1.027.734 ₫** · **0 conversion** (toàn bộ rơi vào 14-15/08, impr dồn 5-6h sáng). SEARCH cùng kỳ: 164 click · 4,29tr · **4/4 conversion**. → Display = 0 lead, ~19k/click rác.
- **Hành động**: `target_content_network=False` qua API, read-back xác minh `search=True display=False`. Ghi `ops/change-log.jsonl` (review **22/08**, guardrail: conv 7 ngày giảm >20% thì xem lại). Không đụng bid.
- **Bẫy kỹ thuật mới (SETUP.md #17)**: `protobuf_helpers.field_mask()` **bỏ qua field set về `False`** (proto3 default) → lần mutate đầu Google trả OK nhưng read-back vẫn `display=True`. Phải tự `op.update_mask.paths.append(...)`. Cổng `ghi()` bắt được nhờ read-back bắt buộc — nếu không có nó thì đã báo "xong" sai.
- **Hệ quả đọc số**: 14/08 và 15/08 nhiễm Display → chỉ đọc phần SEARCH (14/08 thật: 290 impr · 22 click · 623k · 1 conv). Đã ghi `ops/ngay-hong.txt`.
- **Vá hệ thống**: `bao_cao.py` in thêm khối **MẠNG HIỂN THỊ 7 NGÀY** (cảnh báo ⛔ nếu có dòng CONTENT); skill `phan-tich` thêm luật "lệch chi search-terms >30% → soi ad_network_type" + "impr bùng + CTR tụt = pha loãng mạng, không phải ad kém".

### 2026-08-17 — USER TẮT CAMPAIGN (PAUSED). Đóng sổ kỳ chạy đầu 06–17/08

- Trạng thái verify qua API: `status=PAUSED`, `primary_status_reasons=['CAMPAIGN_PAUSED', ...]`.
- **Tổng kỳ 12 ngày**: 7.925 impr · 269 click · **6.997.549 ₫** · **4 lead form** (Ads). CPL trên tổng chi **1.749.387 ₫**; CPL trên riêng chi Search **1.498.740 ₫**.
- Tách mạng: SEARCH 217 click · 5.994.960 ₫ · **4/4 conv** (CTR 6,8%, CPC 27.626 ₫) — CONTENT 52 click · 1.002.590 ₫ · **0 conv** (rò 14-15/08, đã tắt).
- Tách nhóm: `brand-beachtro-tower` 28 click · 658.572 ₫ · 2 conv → **CPL 329.286 ₫** · `brand-blanca-city` 241 click · 6.338.977 ₫ · 2 conv → **CPL 3.169.489 ₫**. → Nhóm beachtro rẻ hơn ~10 lần nhưng gần như không có volume (trần cầu).
- Lead rơi vào 09/08 (1) · 11/08 (2) · 14/08 (1). Không có lead từ 15/08.
- Ba review đang chờ **đóng sổ ở trạng thái CHƯA KẾT LUẬN** (bid 35k 21/08, tắt Display 22/08, RSA v4 26/08) — campaign dừng trước hạn, không đủ dữ liệu phán.
- ⚠️ Bật lại = **kỳ đo mới**, không nối số với kỳ này.

### 2026-08-19 — Nghiệm thu lead từ CRM (2 kỳ báo cáo)

| | 06–10/08 | 11–18/08 | **Lũy kế 06–18/08** |
|---|---|---|---|
| Chi (tổng) | 2.292.727 ₫ | 4.858.607 ₫ | **7.151.334 ₫** |
| Chi (chỉ Search, bỏ Display rò) | 2.292.727 ₫ | 3.856.017 ₫ | **6.148.745 ₫** |
| Lead (CRM) | 2 | 4 | **6** |
| F1 | 1 | 1 | **2** |
| CPL (tổng chi) | 1.146.364 ₫ | 1.214.652 ₫ | **1.191.889 ₫** |
| CPL (chi Search) | 1.146.364 ₫ | 964.004 ₫ | **1.024.791 ₫** |
| Chi/F1 | 2.292.727 ₫ | 4.858.607 ₫ | **3.575.667 ₫** |
| Qualify | 50% | 25% | **33%** |
| Booking / Deal | 0 / 0 | — cần user | **0 / 0** |

- **CRM 6 lead > Ads 4 conv** — không phải lệch đo: hệ **KHÔNG đo** lead qua hotline/Zalo (quyết định không sửa GTM, `audit-lp.md`). Ads gán 4: 09/08 ×1 · 11/08 ×2 · 14/08 ×1. Chênh 2 lead = kênh ngoài form. **Cấm cộng chéo 2 hệ**; CRM là bản nghiệm thu thật, Ads chỉ dùng chẩn đoán delivery.
- Người chạy trên báo cáo công ty: **Tường Đặng MKT**.
- Toàn kỳ: 8.027 impr · 274 click.
- ⚠️ Còn phát sinh chi ngày 18/08 (102 impr · 5 click · 153.785 ₫) SAU khi user tắt campaign 17/08 — **chưa xác minh nguyên nhân** (lệnh kiểm change_event bị dừng giữa chừng). Việc còn treo: kiểm `campaign.status` + `change_event`, hoặc user xem trạng thái trên UI.

### 2026-08-19 — BẬT LẠI campaign (kỳ đo 2)

- Verify API: `status=ENABLED`, `target_content_network=False` (Display vẫn tắt ✓), trần CPC 35k giữ nguyên. `primary_status=LIMITED` vì `BIDDING_STRATEGY_LEARNING` — bình thường sau khi bật lại, tự hết sau 2–3 ngày.
- Chi đã phát sinh: 18/08 **153.785 ₫** (102 impr · 5 click) · 19/08 **169.149 ₫** (131 impr · 5 click) → giải thích luôn khoản chi 18/08 từng bị treo nghi vấn ở mục trên: **campaign được bật lại**, không phải PAUSED mà vẫn tiêu tiền.
- **Kỳ đo 2 tính từ 18/08**, không nối số với kỳ 1.
- Skill `phan-tich` cập nhật cùng ngày theo phản hồi user *"quá chặt, độ phủ định quá cao"*: thay luật "CẤM phán" bằng **3 mức tin cậy CHỐT / NGHIÊNG / KHÔNG ĐỌC ĐƯỢC** (chỉ mức 3 mới được từ chối kết luận) + luật cân bằng giọng (mỗi báo cáo ≥1 kết luận có hướng, tối đa 1 dòng cảnh báo, >2 câu phủ định là phải viết lại). §4b làm rõ **khối trên = kỳ, khối dưới = lũy kế**.

### 2026-08-21 — Chẩn đoán nút thắt kỳ 2: **QS thấp do TRANG ĐÍCH**, không phải ad
- Kỳ 2 chốt 18–20/08: chi **1.325.924 ₫** · 40 click · **2 conv (Ads)** → **CPL 662.962 ₫** (kỳ 1: 1,19tr) — rẻ nhất từ đầu chiến dịch, n=2 nên còn là *nghiêng tốt*, chốt ở ~120 click.
- IS 19–20/08 chỉ **54–55%**, **mất-rank 45%**, mất-budget **0%** → nút thắt **thiếu CHẤT** (không phải thiếu tiền).
- Bóc thành phần QS từng keyword (`quality_info.*`, 18–21/08): **ad relevance ABOVE_AVERAGE gần như toàn bộ**, nhưng **post_click (trang đích) chỉ AVERAGE, riêng mọi keyword có chữ "giá" đều BELOW_AVERAGE**. Không keyword nào đạt LP ABOVE_AVERAGE. QS brand: `blanca city` 5 · `căn hộ blanca city` 2 · `giá bán blanca city` 3.
- Kết luận: LP không có khối GIÁ cụ thể trong khi truy vấn hỏi-giá là nguồn lead thật (2/2 lead 20/08 đến từ term có chữ "giá"). Đòn tiếp theo: **thêm khối bảng giá / "giá từ …" + chính sách thanh toán vào LP** → kéo post_click lên, hạ CPC 33k, lấy lại phần mất-rank 45% mà không tăng ngân sách.
- Dòng CONTENT trong khối MẠNG HIỂN THỊ của `bao_cao.py` là **dư âm 14–15/08** (Display vẫn tắt, `target_content_network=False`); rơi khỏi cửa sổ 7 ngày sau 22/08.

### 2026-08-23 — Quyết định: CHỜ ĐỦ 120 CLICK mới xử
- CPL kỳ 2 (18→23/08 13h): 3.745.529₫ / 95 click / 2 lead = **1.872.765₫** — vượt guardrail 1,5tr; 55 click liên tiếp 0 lead từ sau 20/08. CPC leo 33,4k→35,7k→51,2k→~53k (vượt trần 45k — nghi bid adjustment cộng lên trần).
- User chọn **chưa hành động**, chờ đủ cổng mẫu 120 click (~1-2 ngày) rồi chốt kỳ 2 đúng luật. Hai phương án đã duyệt sẵn chờ kích hoạt: hạ trần CPC 45k→35k · gói sửa LP (section giá #bang-gia + Zalo sticky + MST footer).
- ✅ Dòng CONTENT rơi khỏi cửa sổ 7 ngày — xác nhận Display tắt hẳn.

### 2026-08-24 — KỲ 2 CHẠM CỔNG MẪU 120 CLICK: CPL 1.208.908₫ — ĐẠT SÁT BIÊN mục tiêu 1,2tr
- Chốt 18–23/08: chi **4.835.631₫** · **120 click** · **4 conv (Ads)** → CPL **1.208.908₫** (mục tiêu đăng ký ≤1,2tr — lệch +0,7%, tính trên conv Ads; số CRM do user giữ). Guardrail 1,5tr KHÔNG vỡ.
- Cảnh báo 23/08 (CPL 1,87tr giữa kỳ) tự gỡ: 23/08 về **2 conv** từ term `blanca city vũng tàu` (9 click/468.836₫) — lại đúng pattern conversion-lag, lần thứ 3 (14/08, 20/08, 23/08). Đọc CPL giữa kỳ khi chưa đủ mẫu = nhiễu.
- IS 22–23/08: 69–70% ✓ (đạt điều kiện ≥65% của kỳ đo); mất-rank còn 30–31%, CPC vẫn cao 46,5–51,2k (vượt trần 45k — nghi bid adjustment). 23/08 chi 1.675.356₫ = 168% budget ngày (overdelivery hợp lệ, Google bù trong tháng).
- Đóng mục review 24/08 (entry PAUSED 17/08 — vô hiệu do đã bật lại). Review chính thức kỳ 2: 26/08.
