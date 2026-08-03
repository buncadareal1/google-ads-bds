# GA4 Setup

Property: 1 property cho toàn bộ LP BĐS, 1 web data stream. Không tách property theo dự án —
dùng `page_path` / `form_id` để chia. Tách property = mất audience chung, mất so sánh dự án.

---

## 1. Cấu hình property

| Mục | Đặt là | Lý do |
|---|---|---|
| Industry category | Real Estate | |
| Reporting time zone | `(GMT+07:00) Vietnam Time` | Lệch múi giờ làm sai đối chiếu Ads↔GA4↔Keap |
| Currency | Vietnamese Dong (VND) | |
| Data retention (Event data) | **14 months** (mặc định 2 tháng) | BĐS chu kỳ 3-12 tháng — 2 tháng là vô dụng |
| Reset user data on new activity | ON | |
| Enhanced measurement | Page views · Scrolls · Outbound clicks · Site search **OFF** · File downloads · Video **OFF** | `scroll` (90%) giữ lại làm chéo với `xem_bang_gia` |
| Internal traffic filter | Thêm IP văn phòng → filter state **Active** | Không lọc = số CVR bị pha loãng bởi chính mình |
| Unwanted referrals | Thêm domain proxy Keap (`smartland.vn`, `*.infusionsoft.com`, `*.infusionsoft.app`) | Không loại → mọi lead thành "referral", mất nguồn thật |
| Reporting identity | **Blended** | |
| Google signals | **ON** | Cần cho remarketing + demographic. Đánh đổi: data thresholding khi số nhỏ. |
| Attribution model | **Data-driven** (mặc định, `Quản trị → Cài đặt phân bổ`) | Đây là model CỦA GA4 — riêng biệt với model của Google Ads, đổi bên này không đổi bên kia. Lệch số giữa 2 nguồn một phần từ đây (xem audit-monthly §2.1). |
| Key event lookback window | **90 ngày** | Khớp cửa sổ chuyển đổi 90 ngày phía Ads (`campaign-setup.md` §1.2.4) — chu kỳ BĐS 3-12 tháng. Đặt sai làm lệch mọi số đối chiếu. |

> **"EU signals" / vùng:** không có toggle riêng tên đó. Thứ liên quan là (a) Consent Mode ở LP —
> đã set EEA/UK `denied`, VN `granted` (`tracking/lp-requirements.md` §1.1), và (b) campaign Google Ads
> để **Location = Vietnam, targeting method = Presence** (không phải "Presence or interest").
> Kết quả thực tế: không thu dữ liệu quảng cáo của người ở EEA/UK, không cần CMP.
> Nếu sau này chạy campaign nhắm Việt kiều EU/UK → phải gắn CMP trước, không phải sau.

---

## 2. Key events (mark conversion)

Admin → Data display → **Events** → bật toggle *Mark as key event*.

| Event | Key event? | Vai trò |
|---|---|---|
| `generate_lead` | ✅ | Lead chính |
| `phone_click` | ✅ | CTA chính BĐS VN |
| `zalo_click` | ✅ | CTA chính BĐS VN |
| `xem_bang_gia` | ❌ | Micro — **chỉ nuôi audience**, đánh dấu key event sẽ làm loãng báo cáo conversion |
| `xem_mat_bang` | ❌ | Micro |
| `form_start` | ❌ | Micro — dùng để tính tỷ lệ bỏ form (`form_start` → `generate_lead`) |

**Chỉ import 3 key event trên vào Google Ads** (§4) — và ngay cả 3 cái đó cũng chỉ là **Secondary**
trong Google Ads theo `PLAN.md` §0.4. Primary là 3 conversion action upload từ CRM.

### 2.1 Custom dimensions (Admin → Custom definitions)

| Dimension name | Scope | Event parameter | Dùng để |
|---|---|---|---|
| `form_id` | Event | `form_id` | Form nào ra lead (hero vs footer vs modal) |
| `cta_location` | Event | `cta_location` | Nút Zalo/hotline nào đang chạy |
| `ngan_sach` | Event | `ngan_sach` | CVR theo phân khúc ngân sách |
| `muc_dich` | Event | `muc_dich` | Ở vs đầu tư — thứ dự đoán contact rate mạnh nhất |
| `section_id` | Event | `section_id` | Bảng giá vs mặt bằng |
| `has_email` | Event | `has_email` | Bao nhiêu % lead có email → tỷ lệ match ECL kỳ vọng |

Giới hạn 50 event-scoped dimension — 6 cái này còn rất xa ngưỡng.
**Không** tạo dimension cho tên/SĐT/email.

---

## 3. Audience remarketing (5 audience, đúng `playbook/customer-journey-plan.md` §2.1)

Admin → Audiences → New audience → Create a custom audience.

| # | Tên audience | Điều kiện | Membership duration | Dùng ở |
|---|---|---|---|---|
| 1 | `xem_bang_gia_30d` | Event `xem_bang_gia` ≥ 1 lần | **30 ngày** | Giai đoạn 3 — Display remarketing |
| 2 | `xem_mat_bang_30d` | Event `xem_mat_bang` ≥ 1 lần | **30 ngày** | Giai đoạn 3 |
| 3 | `engaged_60s_30d` | Metric *Average engagement time per session* **> 60** (scope: Session) | **30 ngày** | Giai đoạn 3 |
| 4 | `form_start_khong_submit_7d` | Include: `form_start` ≥ 1 · **Exclude**: `generate_lead` ≥ 1 (temporarily, cùng window) | **7 ngày** | Giai đoạn 4 — list nóng nhất |
| 5 | `da_generate_lead_14d` | Event `generate_lead` ≥ 1 | **14 ngày** | **Chỉ dùng để EXCLUDE** khỏi mọi campaign remarketing |

**Chi tiết cấu hình quan trọng:**

- **#3 `engaged_60s_30d`** dùng **metric có sẵn của GA4**, không phải event mới. Registry vẫn 6 event.
  Nếu GA4 UI không cho dùng metric đó ở scope Session, fallback: điều kiện
  `user_engagement` với parameter `engagement_time_msec > 60000`.
- **#4** phải chọn **"Temporarily exclude users when they meet these conditions"**, KHÔNG phải
  "Permanently exclude" — khách bỏ form hôm nay có thể submit tuần sau, đuổi vĩnh viễn là mất họ.
- **#5** phải được **exclude khỏi tất cả** campaign remarketing (Display, Demand Gen). Quên bước này
  = trả tiền quảng cáo cho người đã là lead, và họ thấy phiền.
- Audience mới **không hồi tố quá 30 ngày** — tạo NGAY khi LP live, đừng đợi tới lúc cần G2.
  Chờ mới tạo = mất 30 ngày dữ liệu và trễ gate G2 thêm 1 tháng.
- Ngưỡng Google Ads: list remarketing cần **≥100 user active/30 ngày** mới phân phối được —
  ⚠️ **`[3P: Search Engine Land]`, CHƯA xác nhận được ở tài liệu Google** (vòng research 2026-07).
  Đừng trích như citation Google. Gate G2 (`playbook/customer-journey-plan.md` §3.1) đặt cao hơn
  nhiều: ≥1.000 user/30 ngày → **vẫn an toàn dù con số 100 sai**.

### 3.1 Audience KHÔNG tạo

`all_visitors_30d` — GA4 đã có sẵn "All Users" và Google Ads tự tạo list "All visitors" khi link.
Tạo thêm = 2 list trùng nhau, người sau không biết chọn cái nào.

---

## 4. Link GA4 ↔ Google Ads

Admin → Product links → **Google Ads links** → Link.

| Setting | Giá trị |
|---|---|
| Google Ads account | *(điền customer ID — dùng MCC nếu có)* |
| Enable Personalized Advertising | **ON** — bắt buộc, không có thì audience không sang được Ads |
| Enable Auto-Tagging | **ON** (hoặc xác nhận đã ON sẵn trong Ads) |

Sau khi link:

1. Google Ads → Tools → **Audience manager** → xác nhận 5 audience GA4 đã xuất hiện (mất tới 24-48h).
2. Google Ads → Goals → Conversions → **Import → Google Analytics 4 → Web** → chọn
   `generate_lead`, `phone_click`, `zalo_click`.
3. **Đặt cả 3 import này = Secondary.** Chúng trùng với 3 conversion action GTM
   (`tracking/gtm-container-spec.md` §4.1) — nếu để Primary sẽ **đếm đúp** mọi lead.
   > ponytail: có thể **bỏ hẳn bước 2** và chỉ dùng 3 tag GTM. Import GA4 chỉ hữu ích khi cần
   > attribution model của GA4. Hai nguồn cùng đo một hành động là nợ kỹ thuật — nếu bạn không có
   > lý do rõ ràng cần cả hai, chọn GTM và bỏ qua import.

### 4.1 Các link khác

| Link | Bật? |
|---|---|
| Google Search Console | ✅ khi có `content/` chạy |
| BigQuery export | ❌ chưa cần ở quy mô này — **điều kiện mở lại** ở ghi chú dưới |
| Display & Video 360 / Search Ads 360 | ❌ |

> **BigQuery export — giữ quyết định hoãn. Điều kiện mở lại (một trong hai là đủ):**
> (i) cần **né data thresholding** để phân tích demographic/audience (số nhỏ bị ẩn vì Google signals đang ON — `§1`); hoặc (ii) cần **join GA4 × Keap × Ads ở cấp row** (một dòng = một lead) mà UI không làm được.
> ⚠️ Khi mở: **BigQuery export KHÔNG nhận dữ liệu từ Google signals** → số event trong BigQuery sẽ **khác** GA4 UI. Đó **không phải lỗi pipeline** — biết trước để không đi tìm bug. Free tier 1 triệu event/ngày, hệ còn rất xa ngưỡng.

---

## 5. Explorations lập sẵn (3 cái, đủ dùng)

| Tên | Loại | Trả lời câu hỏi |
|---|---|---|
| `Funnel — LP to Lead` | Funnel exploration: `session_start` → `xem_bang_gia` → `form_start` → `generate_lead` | Rớt ở bước nào |
| `Lead theo phân khúc` | Free form: dimension `ngan_sach` × `muc_dich`, metric `generate_lead` | Ngân sách/mục đích nào ra lead — feed cho negative keyword |
| `CTA nào chạy` | Free form: dimension `cta_location`, metric event count `phone_click` + `zalo_click` | Nút nào nên nhân bản, nút nào gỡ |

---

## 6. Checklist nghiệm thu

- [ ] Data retention = 14 months
- [ ] Time zone = Vietnam, currency = VND
- [ ] Internal traffic filter **Active** (không phải Testing)
- [ ] Unwanted referrals có domain proxy Keap
- [ ] 6 event xuất hiện trong Realtime + DebugView
- [ ] Đúng 3 key event: `generate_lead`, `phone_click`, `zalo_click`
- [ ] 6 custom dimension đã tạo, có giá trị thật (không phải `(not set)`)
- [ ] 5 audience đã tạo, đúng window 30/30/30/7/14
- [ ] `da_generate_lead_14d` đã exclude khỏi mọi campaign remarketing
- [ ] GA4 ↔ Google Ads đã link, Personalized Advertising ON
- [ ] Không có conversion nào bị đếm đúp giữa import GA4 và tag GTM

---

## Đề xuất chờ duyệt

Chưa có. `engaged_60s` giải quyết bằng metric sẵn có của GA4, không phát sinh event mới.
