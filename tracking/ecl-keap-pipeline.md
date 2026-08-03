# Pipeline ECL: Keap → Google Data Manager API

Đây là **đòn bẩy #1** của cả hệ thống (`research/google-ads-bds-vn.md` §5). Không có nó, Google Ads
chỉ biết "có form submit" và smart bidding sẽ đi mua form submit rẻ nhất — tức lead rác.
Có nó, Google biết keyword nào ra khách **gọi được / qualified / đặt cọc** và tối ưu theo đó.

> ⚠️ **Google Ads API đã chặn offline conversion upload + ECL từ 15/6/2026.**
> Đường duy nhất còn lại là **Data Manager API**. Mọi thứ dưới đây viết cho API đó.

> 🔲 **VERIFY khi có quyền tài khoản — UI thật có thể khác doc này.** Mốc **tháng 4/2026** (đã qua): "enhanced conversions for **web and leads** will merge into **a single on/off setting**", đồng thời nhận user-provided data từ **website tag + Data Manager + API connections** cùng lúc ([About ECL](https://support.google.com/google-ads/answer/15713840?hl=en)). Doc này viết theo mô hình **hai đường riêng** (ECL web qua tag §4.4 `gtm-container-spec.md`, ECL leads qua Data Manager). Khi vào tài khoản, thứ nhìn thấy có thể là **MỘT** toggle enhanced conversions, không phải hai → đối chiếu lại §2 và §4 trước khi kết luận "cấu hình sai".

---

## 1. Kiến trúc

```
Keap (CRM — nguồn chân lý đếm lead)
  │  sales gắn tag khi lead đổi trạng thái
  │  ECL - Contactable  →  ECL - Qualified  →  ECL - Dat Coc
  ▼
tracking/upload_ecl.py   (cron 1 lần/ngày, 07:00 ICT)
  │  1. GET /crm/rest/v1/tags/{tagId}/contacts     → ai vừa đổi trạng thái
  │  2. GET /crm/rest/v1/contacts/{id}?optional_properties=custom_fields
  │                                                → gclid / gbraid / wbraid / email / phone
  │  3. chuẩn hoá + SHA-256 (hex)                  → email lowercase, phone E.164 +84…
  │  4. bỏ qua cái đã upload (state file)          → idempotent
  ▼
POST https://datamanager.googleapis.com/v1/events:ingest
  │  destination.productDestinationId = conversion action ID tương ứng
  ▼
Google Ads — 3 conversion action Primary:
  Lead Contactable (10) · Lead Qualified (50) · Dat Coc (500)
```

### 1.1 Vì sao **daily batch poll**, không phải REST hook (ponytail)

REST hook của Keap cần: endpoint HTTPS public + handshake `X-Hook-Secret` + xử lý retry 4 lần +
theo dõi trạng thái verified. Đó là một dịch vụ phải nuôi.

Offline conversion **không cần real-time** — Google Ads chấp nhận upload trong vòng 90 ngày kể từ
click và smart bidding học theo ngày, không theo phút. Một cron chạy 07:00 mỗi sáng cho kết quả
y hệt, với 0 hạ tầng.

**Khi nào nâng cấp lên REST hook:** khi lead/ngày đủ nhiều để độ trễ 24h làm chậm learning rõ rệt
(> ~50 lead/ngày), hoặc khi cần trigger việc khác ngay lúc đổi stage. Hợp đồng để sẵn ở §6.

---

## 2. Chuẩn bị phía Keap

### 2.1 Ba tag trạng thái (Admin → Settings → Tags)

| Tag | Sales gắn khi | → Conversion action | Giá trị |
|---|---|---|---|
| `ECL - Contactable` | Gọi được, người thật, đúng nhu cầu BĐS | `Lead Contactable` | 10 |
| `ECL - Qualified` | Đủ tài chính + đúng phân khúc + có thời điểm mua | `Lead Qualified` | 50 |
| `ECL - Dat Coc` | Đã chuyển tiền giữ chỗ / đặt cọc | `Dat Coc` | 500 |

Tag **cộng dồn, không thay thế**: một khách đặt cọc mang cả 3 tag → upload cả 3 conversion.
Đúng ý đồ — thang giá trị 10/50/500 phản ánh mức độ tiến triển, không phải trạng thái loại trừ.

Ghi lại **tag ID** (số) của cả 3: `GET /crm/rest/v1/tags?limit=200`.

> **Vì sao tag chứ không phải Opportunity stage?** Tag = 1 click cho sales, không cần tạo bản ghi
> Opportunity cho từng lead. Team đã dùng Opportunity pipeline sẵn thì đổi bước 1 của script sang
> `GET /crm/rest/v1/opportunities` + lọc `stage.id` — phần còn lại giữ nguyên.
> Xác nhận tên tham số filter trong Interactive REST Docs của Keap trước khi đổi.

### 2.2 Custom field chứa click id

Phải có trước khi chạy — xem `tracking/lp-requirements.md` §4.2. Hai khả năng:

| Trường hợp | Script đọc từ đâu |
|---|---|
| Đường B — có custom field `GCLID` / `GBRAID` / `WBRAID` riêng | Đọc thẳng theo `id` custom field |
| Đường A — chỉ có `Landing URL` / `inf_custom_url` chứa `?gclid=…` | **Parse query string** ra `gclid` |

Script làm **cả hai**: ưu tiên field riêng, không có thì parse URL. Không cần chọn trước.

### 2.3 Auth Keap

Admin → Settings → **Service Account Key** (admin-only, thấy toàn bộ dữ liệu).
Personal Access Token cũng chạy nhưng bị giới hạn theo quyền của user tạo ra nó → dùng SAK.

```
Authorization: Bearer <KEAP_SERVICE_ACCOUNT_KEY>
Base URL:      https://api.infusionsoft.com/crm/rest/v1
```

Key này **không bao giờ** commit vào repo — biến môi trường / secret manager.

---

## 3. Chuẩn bị phía Google

### 3.1 Cloud project + service account

1. Google Cloud Console → **Enable Data Manager API** (`datamanager.googleapis.com`).
2. Tạo service account, ví dụ `ecl-uploader@<project>.iam.gserviceaccount.com`.
3. IAM:
   - Service account cần role **Service Usage Consumer** (`roles/serviceusage.serviceUsageConsumer`).
   - Người/máy chạy script cần **Service Account Token Creator**
     (`roles/iam.serviceAccountTokenCreator`) **trên service account đó** nếu dùng impersonation.
4. **Google khuyến nghị impersonation thay vì service account key file** — key file rò rỉ là mất
   quyền ghi vào tài khoản Ads. Script hỗ trợ cả hai; mặc định impersonation.
5. **Google Ads UI → Admin → Access and security → thêm email service account** vào tài khoản Ads
   (hoặc MCC cha) với quyền Standard. Bỏ bước này = `PERMISSION_DENIED`, không phải lỗi code.

Scope: `https://www.googleapis.com/auth/datamanager`

### 3.2 Ba conversion action

Tạo theo `tracking/gtm-container-spec.md` §4.1, action #4/#5/#6:
Goal = *Submit lead form*, source = **Import → Manual (from clicks)** (type `UPLOAD_CLICKS`).

Lấy **conversion action ID** = tham số `ctId` trên URL khi mở action trong Google Ads UI.
Đây chính là `productDestinationId` trong payload.

---

## 4. Hợp đồng Data Manager API

**Endpoint**

```
POST https://datamanager.googleapis.com/v1/events:ingest
Authorization: Bearer <access_token>
Content-Type: application/json
```

**Payload mẫu — 1 lead qualified, có gclid + email + phone**

```json
{
  "destinations": [
    {
      "operatingAccount": { "accountType": "GOOGLE_ADS", "accountId": "1234567890" },
      "loginAccount":     { "accountType": "GOOGLE_ADS", "accountId": "1112223333" },
      "productDestinationId": "987654321"
    }
  ],
  "encoding": "HEX",
  "events": [
    {
      "eventTimestamp": "2026-07-28T09:15:00+07:00",
      "transactionId": "keap-48213-qualified",
      "conversionValue": 50,
      "currency": "VND",
      "adIdentifiers": { "gclid": "Cj0KCQjw...TEST" },
      "userData": {
        "userIdentifiers": [
          { "emailAddress": "973dfe463ec85785f5f95af5ba3906eedb2d931c24e69824a89ea65dba4e813b" },
          { "phoneNumber":  "ed644edf0566470f0b5a8c13c792fa8e8a489574da3aceec119b9456e870d396" }
        ]
      }
    }
  ],
  "consent": { "adUserData": "CONSENT_GRANTED", "adPersonalization": "CONSENT_GRANTED" },
  "validateOnly": false
}
```

*(hai hash trên là hash thật của `test@example.com` và `+84912345678` — dùng để tự kiểm tra)*

**Các trường quan trọng**

| Trường | Ghi chú |
|---|---|
| `operatingAccount` | Tài khoản Ads nhận dữ liệu. `accountId` = customer ID **không dấu gạch**. |
| `loginAccount` | Tài khoản mà credential thuộc về. Bỏ qua → mặc định = operating. Truy cập qua **MCC** thì đây là ID của MCC. |
| `linkedAccount` | Chỉ dùng khi login là `DATA_PARTNER`. Ta không dùng. |
| `productDestinationId` | **Conversion action ID** (`ctId`). Mỗi stage một ID → mỗi stage một request. |
| `encoding` | `HEX` (hoặc `BASE64`) — phải khớp cách encode hash. |
| `eventTimestamp` | RFC 3339 có timezone. Dùng **thời điểm đổi stage**, không phải lúc chạy script. |
| `transactionId` | Khoá khử trùng phía Google. Ta dùng `keap-<contactId>-<stage>` → chạy lại script bao nhiêu lần cũng không đếm đúp. |
| `conversionValue` + `currency` | Thang điểm 10/50/500, currency `VND` (xem cảnh báo `gtm-container-spec.md` §4.1). |
| `adIdentifiers` | Ít nhất một trong `gclid` / `gbraid` / `wbraid`, hoặc user identifier, hoặc IP. **Không có gclid mà vẫn có email hash → vẫn upload được**, Google match qua ECL. |

> 🔒 **LUẬT (Google official, curriculum 2026-07): upload TẤT CẢ conversion của event — kể cả lead
> không đến từ Google Ads** (organic, Facebook, giới thiệu...). Google dùng toàn bộ tập để hiệu chỉnh
> model match; chỉ đẩy lead có gclid làm model lệch và ECL match kém đi. Script hiện tại đã đúng
> (chỉ bỏ qua khi không có bất kỳ định danh nào) — ĐỪNG BAO GIỜ thêm filter "chỉ gửi lead có gclid".
| `userData.userIdentifiers` | Email và/hoặc phone đã SHA-256. |
| `consent` | `CONSENT_GRANTED` cho traffic VN (không thuộc EEA). |
| `validateOnly` | `true` = kiểm tra payload, không ghi. **Luôn chạy `--dry-run` trước lần upload đầu.** |

**Giới hạn**: tối đa **2.000 event / request**. Script tự chia batch.

**Chuẩn hoá trước khi hash (sai một bước là match rate = 0)**

| Loại | Quy tắc |
|---|---|
| Email | lowercase → xoá mọi khoảng trắng → SHA-256 → hex |
| Phone | về **E.164** (`0912345678` → `+84912345678`) → xoá khoảng trắng → SHA-256 → hex |

Không hash chuỗi rỗng. Không gửi giá trị chưa hash. Không hash 2 lần.

---

## 5. Mapping & tần suất

| Keap tag | Conversion action | `productDestinationId` | `conversionValue` | `transactionId` |
|---|---|---|---|---|
| `ECL - Contactable` | `Lead Contactable` | *(điền ctId)* | 10 | `keap-<contactId>-contactable` |
| `ECL - Qualified` | `Lead Qualified` | *(điền ctId)* | 50 | `keap-<contactId>-qualified` |
| `ECL - Dat Coc` | `Dat Coc` | *(điền ctId)* | 500 | `keap-<contactId>-dat_coc` |

**Tần suất:** cron **07:00 ICT hằng ngày**, lookback 7 ngày (bù cho ngày lỗi mạng — `transactionId`
lo phần khử trùng).

```cron
0 7 * * *  cd /path/to/google-ads && /usr/bin/python3 tracking/upload_ecl.py >> /var/log/ecl.log 2>&1
```

**Cửa sổ 90 ngày:** Google chỉ nhận conversion trong vòng 90 ngày kể từ click. Chu kỳ BĐS 3-12
tháng → lead đặt cọc tháng thứ 5 sẽ **bị từ chối**. Đây là giới hạn của nền tảng, không phải bug.
Hệ quả thực tế: `Lead Contactable` (vài ngày sau click) upload gần như 100%; `Dat Coc` sẽ rơi rụng
nhiều. Đó chính là lý do `PLAN.md` §0.4 chọn **`Lead Contactable` làm Primary để bid**, không phải cọc.

---

## 6. REST hook (đường nâng cấp — chưa triển khai)

Ghi lại hợp đồng để khi cần không phải research lại:

| Bước | Chi tiết |
|---|---|
| Đăng ký | `POST /crm/rest/v1/hooks` với body `{ "eventKey": "...", "hookUrl": "https://…" }` |
| Handshake | Keap trả header **`X-Hook-Secret`**. Endpoint của bạn phải **echo lại đúng header đó** trong response để hook chuyển sang `Verified`. |
| Verify trễ | `POST /crm/rest/v1/hooks/{key}/delayedVerify` với cùng cặp `X-Hook-Secret`. |
| Giao event | Chỉ gửi khi status = `Verified`. Batch, thử lại **4 lần**, lần đầu sau **30-60 giây**. Tối đa **1.000 object/lần gửi**. |
| Payload Keap gửi | `{ "event_key": …, "object_type": …, "object_keys": [ { "id": …, "apiUrl": …, "timestamp": … } ] }` |
| Event key liên quan | `contactGroup.applied` (tag được gắn — khớp thiết kế tag ở §2.1) · `opportunity.edit` (nếu chuyển sang Opportunity stage) |

Payload hook **chỉ chứa ID**, không chứa dữ liệu contact → vẫn phải gọi
`GET /crm/rest/v1/contacts/{id}?optional_properties=custom_fields` để lấy gclid.
Tức là logic trong `upload_ecl.py` dùng lại được 100%; chỉ thay phần "ai cần upload".

---

## 7. Vận hành & giám sát

**Hằng ngày (trong 10' daily check):** log cron có dòng `uploaded=N failed=0` không.

**Hằng tuần (thứ 3 — lead quality, theo `research/google-ads-bds-vn.md` §8):**

| Chỉ số | Ngưỡng báo động |
|---|---|
| % lead trong Keap **có gclid** | < 60% → click id đang rơi, kiểm tra `tracking/lp-requirements.md` §4.4 |
| % lead có **email** | < 40% → sửa copy field email ("nhận bảng giá PDF") |
| Conversion `Lead Contactable` trong Ads / số tag trong Keap | Lệch > 15% → có lead bị từ chối, xem log |
| Số event bị Google từ chối | > 0 → đọc `requestId` trong response, tra log |

**Lỗi hay gặp**

| Lỗi | Nguyên nhân thật |
|---|---|
| `PERMISSION_DENIED` | Email service account chưa được thêm vào Google Ads (§3.1 bước 5) |
| `INVALID_ARGUMENT: productDestinationId` | Dùng nhầm conversion **label** thay vì conversion **action ID** (`ctId`) |
| Upload OK nhưng Ads không thấy conversion | (a) chưa tới 3-6h xử lý, (b) `gclid` quá 90 ngày, (c) conversion action không phải type `UPLOAD_CLICKS` |
| Match rate ECL rất thấp | Hash sai chuẩn hoá — phone chưa về `+84`, hoặc email chưa lowercase |
| `Dat Coc` gần như luôn bị từ chối | Cửa sổ 90 ngày (§5). Không sửa được — báo cáo cọc bằng CRM, đừng ép vào Ads. |

**Nguồn chân lý (theo `attribution` skill + journey-plan §4):** **CRM quyết định số lượng lead.**
Google Ads chỉ giải thích lead đến từ đâu. Không bao giờ cộng dồn Ads + GA4 + Keap.

---

## 8. Cần user cung cấp

| Cần | Dùng ở |
|---|---|
| `KEAP_SERVICE_ACCOUNT_KEY` | §2.3 |
| 3 **tag ID** của `ECL - Contactable` / `Qualified` / `Dat Coc` | §2.1 |
| **ID custom field** `GCLID` / `GBRAID` / `WBRAID` / `Landing URL` trong Keap | §2.2 |
| Google Ads **customer ID** + **MCC ID** (nếu truy cập qua MCC) | §4 |
| 3 **conversion action ID** (`ctId`) | §3.2, §5 |
| Google Cloud **project ID** + email service account | §3.1 |
| Máy chạy cron (server / máy nội bộ luôn bật / Cloud Scheduler) | §5 |

## Đề xuất chờ duyệt

Chưa có event GA4 mới. Ba tag Keap (`ECL - *`) là đối tượng của CRM, **không phải event GA4** —
không đụng tới registry trong `CLAUDE.md`.
