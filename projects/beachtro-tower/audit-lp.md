# Audit LP Beachtro Tower — 2026-08-06

URL: `https://smartrealtors.vn/beachtro-tower-blanca-city/` · Trang cảm ơn: `/thank-you/cam-on-dang-ky-beachtro-tower-blanca-city/`
Kiểm bằng: tải HTML thật + bundle JS + đọc container GTM qua API + đọc GA4 qua API. Không suy đoán.

## 0. Bản chất LP — đọc trước khi chấm

LP này **không phải LP bán hàng có giá**, mà là **LP đăng ký nhận bảng giá trước khi mở bán**. Chính LP ghi: *"Bảng giá và chính sách bán hàng chính thức chưa được công bố. Chúng tôi gửi ngay khi chủ đầu tư công bố."*

Vì vậy hard gate *"không có khoảng giá ở bất kỳ đâu → không launch"* trong `landing-page/README.md` **không áp dụng như một lỗi**, mà là **đánh đổi có ý thức của giai đoạn pre-launch**. Hệ quả phải chấp nhận và theo dõi:
- CPL raw sẽ **rẻ giả tạo** — rào tài chính bị gỡ, ai cũng để lại số.
- LP **không tự lọc khách theo ngân sách** → gánh nặng lọc dồn hết sang sale.
- Không được so CPL giai đoạn này với CPL sau khi có bảng giá (2 mẫu khác nhau — luật Simpson).

## 1. Kỹ thuật đo lường (thực tế đang chạy)

| Thành phần | Giá trị thật | Đánh giá |
|---|---|---|
| GTM container | `GTM-TKDNJXJ9` (account `6353959536` / container `260355978`, workspace `6`) | ✅ đã publish, live |
| Thẻ Google Ads | `AW-18359425041` | ✅ khớp conversion tracking id của account `6918288556` |
| Thẻ GA4 | `G-RRXWDGQ206` → property `548678683` | ✅ có dữ liệu chảy về |
| Conversion Linker | có, `enableUrlPassthrough` = false | ✅ (auto-tagging account đã bật) |
| Conversion Ads | tag `awct` id `18359425041` label `rRYqCK3SoNwcEJGwurJE` | ✅ có |
| **Trigger conversion** | **pageview trang cảm ơn** `/thank-you/cam-on-dang-ky-beachtro-tower-blanca-city/` (HTTP 200) | ⚠️ xem lỗi #1 |
| Event GA4 khi lead | `gui_form_beachtro_tower` | ❌ **SAI registry** |
| Clarity | không có tag nào | ❌ chưa cài |

**LP tự bắn dataLayer** (đọc từ bundle JS): `view_content` (page load), `form_start` (focusin), `generate_lead` (submit, kèm đủ `gclid/gbraid/wbraid/gad_source/gad_campaignid/utm_*/fbclid/msclkid/ttclid` + phone + email + `event_id` chống trùng).

### ⚖️ Quyết định 2026-08-06: KHÔNG sửa GTM

User chốt giữ nguyên container. Chuỗi đo hiện tại **vẫn chạy được**: khách submit → Keap redirect sang trang cảm ơn → thẻ `awct` bắn conversion thẳng về Ads. **Không đi qua GA4**, nên việc GA4 chưa có key event **không chặn launch**.

Ba cái giá phải trả, chấp nhận có ý thức:
1. ~~Đếm trùng nếu khách F5 trang cảm ơn~~ → **KHÔNG phải vấn đề.** Kiểm API 2026-08-06: conversion action `7709665581` đã ở `counting_type = ONE_PER_CLICK`. Một lượt nhấp quảng cáo chỉ sinh tối đa 1 conversion, trang cảm ơn load lại bao nhiêu lần cũng vậy. Không cần sửa gì.
2. **Không dùng được Enhanced Conversions** dù LP đã có sẵn phone/email trong payload → mất một phần khả năng ghép chuyển đổi trên iOS/trình duyệt chặn cookie.
3. **Mất ngữ cảnh lead**: không biết lead đến từ form nào (7 form dùng chung 1 xid), tòa nào khách quan tâm, `src` nào. Muốn phân tích chuyện đó thì đọc bên Keap, không đọc được từ Ads/GA4.

Ba mục dưới đây giữ lại làm **hồ sơ kỹ thuật** — mở lại khi user đổi ý.

### 3 lỗi đo lường (đã quyết định không sửa)

**#1 — Ba event dataLayer của LP KHÔNG có tag nào nhận.** Container chỉ có đúng 1 trigger, là pageview trang cảm ơn. Nghĩa là `generate_lead` — event giàu dữ liệu nhất, có sẵn `event_id` chống trùng và đủ tham số attribution — **rơi vào hư không**. Conversion hiện đếm bằng lượt xem trang cảm ơn: đúng số trong điều kiện bình thường, nhưng **đếm sai khi khách F5 hoặc quay lại trang cảm ơn** và **mất hết ngữ cảnh** (form nào, tòa nào, nguồn nào). Đây cũng là lý do không dùng được Enhanced Conversions dù LP đã có sẵn phone/email trong payload.

**#2 — Tên event lệch registry.** Registry (`CLAUDE.md`) có 6 event: `generate_lead`, `phone_click`, `zalo_click`, `xem_bang_gia`, `xem_mat_bang`, `form_start`. Đang chảy về GA4: `gui_form_beachtro_tower` (từ GTM) và `view_content` (từ LP) — **cả hai đều ngoài registry**. Mọi audience, báo cáo, và conversion import về sau sẽ lệch tên.

**#3 — Thiếu 3/6 event.** Không có `phone_click` (dù LP có `tel:+84937837888`), không có `zalo_click` (**LP không có link Zalo nào** — CTA chính của khách VN đang thiếu hẳn), không có `xem_bang_gia`/`xem_mat_bang`.

Kiểm GA4 7 ngày gần nhất (property `548678683`): `page_view` 11 · `user_engagement` 6 · `first_visit` 4 · `form_start` 4 · `session_start` 4 · `form_submit` 3 · `scroll` 2 · `view_content` 1. `form_start`/`form_submit`/`scroll` là **enhanced measurement tự động của GA4**, không phải event của ta. **Chưa có key event nào được đánh dấu.**

## 2. Form (7 form, tất cả POST thẳng Keap)

Endpoint `rhq551.infusionsoft.com/app/form/process/c661fd73838c0b58bfab553297fd79fd` — cùng 1 form xid cho cả 7 vị trí (`S1c-TongQuan`, `S5-DyHome`, `S6-BonToa`, `S8-HeSinhThai`, `S14-SmartRealtors`, `Modal-CTA`, `ExitIntent`), phân biệt bằng `data-form-label` + `data-src`.

| Mục | Thực tế | Đối chiếu `lp-requirements.md` |
|---|---|---|
| Field | Họ tên + SĐT (+ email không bắt buộc ở 2 form) | ❌ thiếu 2 dropdown qualifying |
| Honeypot | 2 lớp (`inf-sbt` + `website`) | ✅ |
| Chặn submit quá nhanh | có (<2s → chặn) | ✅ tốt hơn spec |
| Chuẩn hóa số ĐT | có | ✅ |
| gclid/UTM tới CRM | **có** — nhét vào `inf_custom_url` qua sessionStorage `bt_attr` | ✅ đường vòng nhưng chạy |

⚠️ Dropdown ngân sách/mục đích **cố ý không có** cũng hợp lý ở giai đoạn này: chưa có bảng giá thì thang ngân sách không neo vào đâu. Nhưng **phải thêm ngay khi có giá**, nếu không LP sẽ hút rác đúng lúc traffic đắt nhất.

## 3. Chấm theo ma trận CRO (`landing-page/README.md`)

| Tiêu chí | Trọng số | Điểm | Vì sao |
|---|---|---|---|
| 1. Message match | 25% | **4** | H1 "Bốn tòa căn hộ sở hữu lâu dài trong Blanca City" khớp brand + USP mạnh nhất. Trừ điểm: luồng "bảng giá" chỉ tới được form đăng ký, không tới bảng giá thật (bất khả kháng) |
| 2. Above the fold | 20% | **3** | Có H1, trust bar (Lâu dài · 4 tòa · 1.785 căn · 8/2028), CTA, hotline. **Thiếu khoảng giá** (bất khả kháng) và **thiếu Zalo sticky** (khắc phục được ngay) |
| 3. Form & qualifying | 15% | **4** | Honeypot, chống bot, chuẩn hóa SĐT, gclid tới CRM đầy đủ. Trừ điểm: chưa có dropdown qualifying |
| 4. Offer & con số | 15% | **3** | Nhiều con số thật (1.785 căn, E6 34–E9 40 tầng, 96 ha, 1 km biển, 8/2028) nhưng **offer chỉ là "chờ bảng giá"** — không có gì để quyết ngay |
| 5. Objection & trust | 10% | **3** | Xử lý thẳng "bàn giao 8/2028" bằng section lộ trình, có mục "phù hợp với ai / không phù hợp với ai" (rất tốt). Nhận diện doanh nghiệp có sẵn trong section SmartRealtors (không chạy footer — chốt 2026-08-06) |
| 6. Tốc độ & kỹ thuật | 5% | **5** | HTML 70 KB, TTFB 0,24s, Astro build tĩnh, JS bundle 9 KB |
| 7. Đo lường | 10% | **2** | Xem 3 lỗi mục 1 |

**Điểm tổng = 3,50 / 5** → thang kết luận: **Đạt — được launch, các mục dưới 3 vào backlog tuần đầu.**

⚠️ Rớt **1 hard gate**: **tiêu chí 7 (Đo lường) = 2 < 3**. Xử lý bằng quyết định giữ nguyên GTM ở mục trên — chuỗi đo qua trang cảm ơn vẫn ghi nhận conversion, chỉ cần chặn đếm trùng bằng `Count = Một`.


## 4. Việc phải làm trước khi bật quảng cáo (theo thứ tự)

| # | Việc | Ai làm | Chặn launch? |
|---|---|---|---|
| 1 | Bắn 1 lead test thật → Ads có conversion ≤24h · Keap có `gclid` (**gate G0**) | user | 🔴 **CÓ** |
| 2 | Thêm **link Zalo** + sticky bar Zalo/hotline trên mobile | user (LP) | 🟡 không, nhưng mất CTA chính của khách VN |
| 3 | Đánh dấu key event trong GA4 `548678683` | user (GA4 UI) | 🟡 không — Ads không phụ thuộc, chỉ để báo cáo GA4 đọc được |
| 4 | Gắn Clarity · sửa GTM về registry · event `xem_bang_gia`/`xem_mat_bang` | hoãn | không |

**Footer: không làm** (chốt 2026-08-06) — LP đã nhận diện được doanh nghiệp qua section "SmartRealtors & Partners" + dòng "Phân phối chính thức… đối tác chiến lược của Sun Group" + hotline + link Chính sách bảo mật. Chi tiết và lý do trong `PROJECT.md`.

Việc phía tài khoản Ads (negative 382 dòng, tracking template UTM, conversion action còn thiếu, dựng campaign): xem `PROJECT.md`.
