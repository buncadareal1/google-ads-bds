# GTM Container Spec

Container web duy nhất cho mọi LP dự án. LP cung cấp dataLayer theo `tracking/lp-requirements.md`;
container này biến chúng thành GA4 event + Google Ads conversion.

**Convention đặt tên (bắt buộc, để MCP `gtm` và người sau đọc được):**

| Loại | Mẫu | Ví dụ |
|---|---|---|
| Tag GA4 | `[GA4] - <event>` | `[GA4] - xem_bang_gia` |
| Tag Google Ads | `[GAds] - <action>` | `[GAds] - Form Submit Raw` |
| Tag hạ tầng | `[Setup] - <mô tả>` | `[Setup] - Conversion Linker` |
| Trigger | `CE - <event>` (Custom Event) | `CE - generate_lead` |
| Variable | `DLV - <key>` (Data Layer Variable) | `DLV - cta_location` |
| Constant | `CONST - <tên>` | `CONST - GA4 Measurement ID` |

---

## 1. Variables

### 1.1 Built-in cần bật

`Page URL` · `Page Path` · `Page Hostname` · `Referrer` · `Click Element` · `Click URL` ·
`Click Text` · `Event` · `Debug Mode`

### 1.2 Constant

| Tên | Giá trị |
|---|---|
| `CONST - GA4 Measurement ID` | `G-XXXXXXXXXX` *(điền)* |
| `CONST - GAds Conversion ID` | `AW-XXXXXXXXX` *(điền)* |

### 1.3 Data Layer Variable

| Tên | Data Layer Variable Name | Default | Dùng ở |
|---|---|---|---|
| `DLV - form_id` | `form_id` | `unknown` | `form_start`, `generate_lead` |
| `DLV - section_id` | `section_id` | *(rỗng)* | `xem_bang_gia`, `xem_mat_bang` |
| `DLV - trigger` | `trigger` | `viewport` | `xem_bang_gia`, `xem_mat_bang` |
| `DLV - cta_location` | `cta_location` | `unknown` | `phone_click`, `zalo_click` |
| `DLV - phone_number` | `phone_number` | *(rỗng)* | `phone_click` |
| `DLV - ngan_sach` | `ngan_sach` | *(rỗng)* | `generate_lead` |
| `DLV - muc_dich` | `muc_dich` | *(rỗng)* | `generate_lead` |
| `DLV - has_email` | `has_email` | `false` | `generate_lead` |
| `DLV - gclid` | `gclid` | *(rỗng)* | debug / QA |
| `DLV - gad_source` | `gad_source` | *(rỗng)* | debug / QA |

> Không tạo DLV cho tên/SĐT/email của khách. PII không vào GA4.
> `DLV - phone_number` là **số hotline của mình** (đích của `tel:`), không phải số khách — an toàn.

---

## 2. Triggers

| Tên | Loại | Cấu hình |
|---|---|---|
| `All Pages` | Page View | (built-in) |
| `CE - generate_lead` | Custom Event | Event name = `generate_lead` |
| `CE - phone_click` | Custom Event | Event name = `phone_click` |
| `CE - zalo_click` | Custom Event | Event name = `zalo_click` |
| `CE - xem_bang_gia` | Custom Event | Event name = `xem_bang_gia` |
| `CE - xem_mat_bang` | Custom Event | Event name = `xem_mat_bang` |
| `CE - form_start` | Custom Event | Event name = `form_start` |
| `CE - Consent Update` | Custom Event | Event name = `consent_update` — **chỉ tạo khi gắn CMP**, hiện chưa cần |

Tất cả dùng **Regex matches** = OFF (exact match) — tránh `xem_bang_gia` bắt nhầm event tương lai.

---

## 3. Tags — GA4

### 3.1 `[Setup] - Google tag (GA4)`

| | |
|---|---|
| Loại | Google Tag |
| Tag ID | `{{CONST - GA4 Measurement ID}}` |
| Trigger | `All Pages` |
| Tag firing priority | `100` (chạy trước mọi tag khác) |
| Consent settings | Additional consent → `analytics_storage` |

Configuration parameters:

| Param | Value |
|---|---|
| `send_page_view` | `true` |
| `allow_google_signals` | `true` |
| `allow_ad_personalization_signals` | `true` |

> `[Setup] - Google tag (GA4)` **cũng nạp Google Ads conversion nếu bạn khai `AW-` trong Google tag
> destinations** — nhưng ta vẫn dùng tag Conversion riêng (mục 4) để kiểm soát giá trị từng action.

### 3.2 Sáu tag event

Tất cả: Type = **Google Analytics: GA4 Event**, Measurement ID = `{{CONST - GA4 Measurement ID}}`,
Consent = `analytics_storage`.

| Tag | Trigger | Event Name | Event Parameters |
|---|---|---|---|
| `[GA4] - generate_lead` | `CE - generate_lead` | `generate_lead` | `form_id`={{DLV - form_id}} · `ngan_sach`={{DLV - ngan_sach}} · `muc_dich`={{DLV - muc_dich}} · `has_email`={{DLV - has_email}} |
| `[GA4] - phone_click` | `CE - phone_click` | `phone_click` | `cta_location`={{DLV - cta_location}} · `phone_number`={{DLV - phone_number}} |
| `[GA4] - zalo_click` | `CE - zalo_click` | `zalo_click` | `cta_location`={{DLV - cta_location}} |
| `[GA4] - xem_bang_gia` | `CE - xem_bang_gia` | `xem_bang_gia` | `section_id`={{DLV - section_id}} · `trigger`={{DLV - trigger}} |
| `[GA4] - xem_mat_bang` | `CE - xem_mat_bang` | `xem_mat_bang` | `section_id`={{DLV - section_id}} · `trigger`={{DLV - trigger}} |
| `[GA4] - form_start` | `CE - form_start` | `form_start` | `form_id`={{DLV - form_id}} |

**Không** đặt `value` / `currency` trên tag GA4 — giá trị tiền chỉ sống ở Google Ads conversion
action (mục 4) và ở CRM. Hai chỗ cùng gán giá trị = báo cáo đá nhau.

---

## 4. Tags — Google Ads

### 4.1 Thang conversion action (theo `PLAN.md` §0.4)

| # | Conversion action (đặt trong Google Ads UI) | Giá trị | Primary / Secondary | Nguồn bắn | Count | Window |
|---|---|---|---|---|---|---|
| 1 | `Form Submit Raw` | **1** | **Secondary** (quan sát) | GTM — `CE - generate_lead` | One | 30 ngày |
| 2 | `Phone Click` | **1** | **Secondary** | GTM — `CE - phone_click` | One | 30 ngày |
| 3 | `Zalo Click` | **1** | **Secondary** | GTM — `CE - zalo_click` | One | 30 ngày |
| 4 | `Lead Contactable` | **10** | **PRIMARY ← smart bidding học cái này** | Upload (Data Manager API) | One | 90 ngày |
| 5 | `Lead Qualified` | **50** | **Primary** | Upload (Data Manager API) | One | 90 ngày |
| 6 | `Dat Coc` | **500** | Primary **chỉ khi ≥15 lượt/tháng**, còn lại Secondary | Upload (Data Manager API) | One | 90 ngày |

Action #4–#6: tạo với **Goal = Submit lead form**, **Conversion source = Import → Manual (from clicks)**
(type `UPLOAD_CLICKS`). Ghi lại **conversion action ID** của từng cái — chính là `ctId` trên URL
Google Ads UI khi mở action. `tracking/ecl-keap-pipeline.md` cần đúng 3 ID này.

> ⚠️ **Giá trị 1/10/50/500 là ĐIỂM tương đối, không phải ₫.** Tài khoản để currency VND nên báo cáo
> sẽ hiện "Conv. value 500 ₫" — trông vô lý nhưng đúng thiết kế: smart bidding chỉ dùng **tỷ lệ**
> giữa các action. Đừng "sửa" thành giá trị tiền thật rồi trộn với thang điểm — hoặc toàn điểm,
> hoặc toàn tiền. Nếu về sau muốn tROAS theo tiền thật, đổi cả 6 dòng cùng lúc sang ₫ (phí môi
> giới × tỷ lệ chuyển) và reset kỳ vọng learning phase.
>
> ⚠️ **Xung đột cần user chốt:** `PLAN.md` §0.4 xếp Phone/Zalo Click là **Secondary**;
> `playbook/customer-journey-plan.md` §2.3 xếp chúng **Primary ở giai đoạn 4**. Spec này theo
> `PLAN.md` (Secondary) — vì để Primary thì smart bidding sẽ mua click rẻ vào nút Zalo, đúng cái
> bẫy "optimize-to-quality" mà chính journey-plan §2.3 cảnh báo. Xem §7.

### 4.2 Tag hạ tầng

| Tag | Loại | Trigger | Ghi chú |
|---|---|---|---|
| `[Setup] - Conversion Linker` | Conversion Linker | `All Pages` | **Bắt buộc.** Ghi `gclid`/`gbraid`/`wbraid` vào first-party cookie `_gcl_*`. Thiếu nó → mất conversion trên Safari/ITP và ECL không match. Enable linking across all page URLs = ON. |
| `[Setup] - Google Ads Remarketing` | — | — | **KHÔNG tạo.** Audience remarketing lấy từ GA4 import (`tracking/ga4-setup.md` §3). Một nguồn audience là đủ. |

### 4.3 Ba tag conversion (chỉ 3 — #4/#5/#6 là upload, không có tag)

Tất cả: Type = **Google Ads Conversion Tracking**, Conversion ID = `{{CONST - GAds Conversion ID}}`,
Consent = `ad_storage` + `ad_user_data`.

| Tag | Trigger | Conversion Label | Value | Currency | Transaction ID |
|---|---|---|---|---|---|
| `[GAds] - Form Submit Raw` | `CE - generate_lead` | *(điền từ action #1)* | `1` | `VND` | *(để trống)* |
| `[GAds] - Phone Click` | `CE - phone_click` | *(điền từ action #2)* | `1` | `VND` | *(để trống)* |
| `[GAds] - Zalo Click` | `CE - zalo_click` | *(điền từ action #3)* | `1` | `VND` | *(để trống)* |

### 4.4 Enhanced Conversions cho `[GAds] - Form Submit Raw`

Bật trong Google Ads UI: conversion action `Form Submit Raw` → **Enhanced conversions for leads** → ON,
phương thức **Google Tag Manager**.

Trong tag `[GAds] - Form Submit Raw` → Include user-provided data → chọn **Code** →
tạo variable `UPD - Lead` (type: *User-Provided Data*) với **Manual configuration**:

| Field | Nguồn |
|---|---|
| Email | `{{DLV - user_email}}` |
| Phone Number | `{{DLV - user_phone_e164}}` |

> **Điều kiện:** LP phải push thêm 2 key này vào dataLayer **chỉ trong `generate_lead`**, dạng đã
> chuẩn hoá (`email` lowercase trim; `phone` dạng `+84…`). GTM tự SHA-256 trước khi gửi — dữ liệu
> **không** vào GA4, chỉ vào Google Ads.
>
> **ponytail: bước này là TÙY CHỌN, không làm ở phase 1.** Pipeline offline upload
> (`tracking/ecl-keap-pipeline.md`) đã gửi email/phone hash kèm `gclid` cho action #4–#6, mạnh hơn
> nhiều vì có tín hiệu chất lượng từ CRM. Chỉ bật ECL-on-page khi tỷ lệ lead có `gclid` trong Keap
> < 60% (nghĩa là click id đang rơi ở đâu đó) — lúc đó nó là lưới an toàn.
> Nếu bật: `tracking/lp-requirements.md` §2.6 phải sửa để cho phép 2 key PII này, và **chỉ** chúng.

---

## 5. Consent Mode

Cấu hình cơ bản, đủ cho traffic 100% VN:

| Bước | Nơi làm |
|---|---|
| `gtag('consent','default',…)` — EEA/UK denied, phần còn lại granted | **LP**, trước GTM snippet — `tracking/lp-requirements.md` §1.1 |
| Container → Admin → **Container Settings → Enable consent overview** | GTM |
| Mỗi tag → Consent Settings → Additional consent required | Bảng dưới |

| Tag | Consent bắt buộc |
|---|---|
| `[Setup] - Google tag (GA4)`, 6 tag `[GA4] - *` | `analytics_storage` |
| `[Setup] - Conversion Linker`, 3 tag `[GAds] - *` | `ad_storage`, `ad_user_data` |

Chưa cài CMP/cookie banner. Cần khi: nhắm Việt kiều EU/UK, hoặc Google bắt đầu ép consent mode ở VN.
Lúc đó CMP gọi `gtag('consent','update',…)` + push `consent_update` → tạo trigger `CE - Consent Update`.

---

## 6. Publish & QA

1. **Preview** → mở LP thật với `?gclid=TEST123&gad_source=1`.
2. Đi hết kịch bản: scroll bảng giá → scroll mặt bằng → focus form → điền → submit → bấm Zalo → bấm hotline.
3. Đối chiếu: GTM Preview thấy đủ 6 custom event, mỗi tag fire **đúng 1 lần**.
4. GA4 **DebugView** thấy đủ 6 event với đúng param.
5. Google Ads → Conversions → 3 action web chuyển sang **"Recording conversions"** trong 24h.
6. Publish với **version name** dạng `2026-07-28 – 6 event registry + 3 GAds conv` **và version NOTE**
   (thêm/sửa/xoá tag nào, vì sao, ai yêu cầu). Container không đặt tên version = không rollback được;
   có tên mà không có note = biết rollback về đâu nhưng không biết vì sao. Đây là **cách duy nhất**
   khôi phục khi alert 🟡 "GA4 event ngừng bắn dù có traffic" nổ (`playbook/monitoring.md` §2) —
   câu hỏi đầu tiên luôn là "GTM vừa publish gì?". **Không bao giờ publish mà chưa qua Preview** (bước 1-5).

**Bẫy hay gặp:**

| Triệu chứng | Nguyên nhân |
|---|---|
| Event đúp | GTM container gắn 2 lần trên trang, hoặc LP push trong cả submit handler lẫn trang cảm ơn |
| `cta_location` = `unknown` | Thiếu `data-cta` trên `<a>` — lỗi LP, không phải GTM |
| Conversion 0 dù GA4 có event | Sai Conversion Label, hoặc thiếu `[Setup] - Conversion Linker` |
| Conversion tụt trên iOS/Safari | Conversion Linker chưa bật, hoặc thiếu `gbraid`/`wbraid` trong `KEYS` của LP |
| `generate_lead` có nhưng Keap trống | Form dùng `fetch` — lỗi LP, xem `tracking/lp-requirements.md` §5 |

---

## 7. Cần user quyết

1. **Phone/Zalo Click = Primary hay Secondary?** Spec theo `PLAN.md` = Secondary. Đổi thành Primary
   sẽ khiến smart bidding tối ưu vào click nút, không phải lead gọi được.
2. **`Dat Coc` (500)** — Primary hay Secondary? Chỉ để Primary khi ≥15 lượt cọc/tháng, dưới ngưỡng
   đó nó chỉ làm nhiễu.
3. **Thang điểm 1/10/50/500 hay giá trị ₫ thật?** Nếu có phí môi giới trung bình/căn +
   tỷ lệ booking→HĐMB (`playbook/customer-journey-plan.md` §6) thì chuyển sang ₫ thật được ngay
   và mở đường cho tROAS.
4. **`GTM-XXXXXXX`, `G-XXXXXXXXXX`, `AW-XXXXXXXXX`, 6 conversion label/ID** — chưa có, đang để placeholder.

---

## Đề xuất chờ duyệt

| Tên | Loại | Trạng thái |
|---|---|---|
| `consent_update` | **Không phải event đo lường GA4** — chỉ là tín hiệu dataLayer để GTM biết CMP đã cập nhật consent. Không có tag GA4 nào gắn vào nó. | Chưa triển khai. Chỉ tạo khi gắn CMP (nhắm Việt kiều EU/UK). Registry 6 event trong `CLAUDE.md` không đổi. |

Không có đề xuất event đo lường mới nào. 6 event registry phủ đủ nhu cầu hiện tại.
