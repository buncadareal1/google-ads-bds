# Yêu cầu Landing Page — HANDOFF cho người làm LP

> Đọc file này như một **hợp đồng kỹ thuật**. LP tự làm cũng được (Astro / WordPress / HTML thuần),
> nhưng phải khớp đúng: **tên event**, **tên field**, **cách submit form**. Sai một trong ba thì
> tracking hỏng và mọi thứ phía sau (`tracking/gtm-container-spec.md`, `tracking/ga4-setup.md`,
> `tracking/ecl-keap-pipeline.md`) không chạy.

**Registry event GA4 — nguồn chân lý duy nhất (`CLAUDE.md`), 6 event, không thêm không bớt:**

```
generate_lead · phone_click · zalo_click · xem_bang_gia · xem_mat_bang · form_start
```

Cần event thứ 7? → ghi vào mục **"Đề xuất chờ duyệt"** cuối file này, **không tự đẩy lên dataLayer**.
GTM chỉ có trigger cho 6 cái trên; event lạ = im lặng rơi.

---

## 1. Thứ tự script trong `<head>` / `<body>`

| # | Script | Đặt ở đâu | Ghi chú |
|---|---|---|---|
| 1 | `dataLayer` khởi tạo + Consent Mode default | **Dòng đầu tiên** trong `<head>`, TRƯỚC GTM | Bắt buộc trước GTM, nếu không consent default không có tác dụng |
| 2 | GTM container `<script>` | Ngay sau #1, trong `<head>` | `GTM-XXXXXXX` — lấy từ GTM |
| 3 | GTM `<noscript>` iframe | Ngay sau `<body>` | |
| 4 | Microsoft Clarity | Cuối `<head>` hoặc trước `</body>`, `async` | Xem `tracking/clarity-checklist.md` |
| 5 | Script attribution (mục 4) | Trước `</body>`, sau khi form đã tồn tại trong DOM | Astro: `<script>` global trong `Layout.astro` |

### 1.1 Snippet #1 — dataLayer + Consent Mode (copy nguyên văn)

```html
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}

  // Mặc định cho EEA/UK: từ chối tới khi có consent (bảo hiểm — ta không nhắm EU).
  gtag('consent', 'default', {
    ad_storage: 'denied', ad_user_data: 'denied', ad_personalization: 'denied',
    analytics_storage: 'denied',
    region: ['AT','BE','BG','HR','CY','CZ','DK','EE','FI','FR','DE','GR','HU','IE','IT',
             'LV','LT','LU','MT','NL','PL','PT','RO','SK','SI','ES','SE','IS','LI','NO','GB','CH'],
    wait_for_update: 500
  });
  // Mặc định toàn cầu (gồm VN — thị trường duy nhất ta chạy ads): cho phép.
  gtag('consent', 'default', {
    ad_storage: 'granted', ad_user_data: 'granted', ad_personalization: 'granted',
    analytics_storage: 'granted'
  });
</script>
<!-- GTM container snippet dán NGAY DƯỚI đây -->
```

> ponytail: không cài CMP (cookie banner). VN không có luật bắt buộc consent banner, traffic 100% VN.
> Cần banner khi bắt đầu nhắm Việt kiều EU/UK → lúc đó gắn CMP và cho nó gọi `gtag('consent','update',…)`.

---

## 2. Registry event → dataLayer snippet + định nghĩa trigger

Mọi push đều theo dạng `window.dataLayer.push({ event: '<tên>', ... })`.
**Mỗi event chỉ bắn 1 lần / phiên** trừ khi ghi rõ khác — dùng cờ trong `sessionStorage`.

### 2.1 `xem_bang_gia` — khách đọc bảng giá

**Định nghĩa trigger (2 đường, bắn 1 lần/phiên, cái nào tới trước):**
1. Section bảng giá **vào viewport ≥ 50% chiều cao section, liên tục ≥ 2 giây** (IntersectionObserver), HOẶC
2. Khách **click tab / accordion "Bảng giá"** (kể cả khi section đã ở trong viewport sẵn).

Yêu cầu markup: `<section id="bang-gia" data-track="xem_bang_gia">`, tab bấm: `<button data-track-click="xem_bang_gia">`.

```html
<script>
(function () {
  var dl = (window.dataLayer = window.dataLayer || []);
  function once(name, params) {
    var k = 'fired_' + name;
    if (sessionStorage.getItem(k)) return;
    try { sessionStorage.setItem(k, '1'); } catch (e) {}
    dl.push(Object.assign({ event: name }, params || {}));
  }

  // (1) vào viewport ≥50% trong ≥2s
  document.querySelectorAll('[data-track]').forEach(function (el) {
    var name = el.getAttribute('data-track'), timer = null;
    new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting && e.intersectionRatio >= 0.5) {
          timer = setTimeout(function () { once(name, { section_id: el.id || '' }); }, 2000);
        } else { clearTimeout(timer); }
      });
    }, { threshold: [0.5] }).observe(el);
  });

  // (2) click tab
  document.addEventListener('click', function (ev) {
    var t = ev.target.closest('[data-track-click]');
    if (t) once(t.getAttribute('data-track-click'), { trigger: 'tab_click' });
  });
})();
</script>
```

Payload:

```js
{ event: 'xem_bang_gia', section_id: 'bang-gia', trigger: 'viewport' | 'tab_click' }
```

### 2.2 `xem_mat_bang` — khách xem mặt bằng layout

Trigger: **giống hệt** `xem_bang_gia` — dùng chung script trên, chỉ cần đánh dấu markup:
`<section id="mat-bang" data-track="xem_mat_bang">` và tab `data-track-click="xem_mat_bang"`.
Click vào **thumbnail mặt bằng từng loại căn** (mở lightbox) cũng gắn `data-track-click="xem_mat_bang"`.

```js
{ event: 'xem_mat_bang', section_id: 'mat-bang', trigger: 'viewport' | 'tab_click' }
```

### 2.3 `form_start` — khách bắt đầu điền form

Trigger: **`focus` lần đầu vào bất kỳ input/select nào của form lead**, 1 lần/phiên.
KHÔNG bắn khi form chỉ hiện ra màn hình. KHÔNG bắn khi focus vào honeypot.

```html
<script>
(function () {
  var dl = (window.dataLayer = window.dataLayer || []);
  var fired = false;
  document.querySelectorAll('form[data-lead-form]').forEach(function (f) {
    f.addEventListener('focusin', function (e) {
      if (fired || e.target.name === 'website') return;   // 'website' = honeypot
      fired = true;
      dl.push({ event: 'form_start', form_id: f.getAttribute('data-lead-form') });
    });
  });
})();
</script>
```

```js
{ event: 'form_start', form_id: 'hero' | 'bang-gia' | 'footer' | 'modal' }
```

### 2.4 `phone_click` — bấm số hotline

Trigger: click bất kỳ `<a href="tel:...">`. Bắn **mỗi lần click** (không dedupe — 1 người gọi 2 lần
là 2 tín hiệu quan tâm thật). GTM sẽ khử trùng phía conversion.

```html
<a href="tel:+84901234567" data-cta="hotline-sticky">Gọi ngay 0901 234 567</a>
```

```html
<script>
document.addEventListener('click', function (e) {
  var a = e.target.closest('a[href^="tel:"]');
  if (!a) return;
  (window.dataLayer = window.dataLayer || []).push({
    event: 'phone_click',
    phone_number: a.getAttribute('href').replace('tel:', ''),
    cta_location: a.dataset.cta || 'unknown'
  });
});
</script>
```

### 2.5 `zalo_click` — bấm nút Zalo

Trigger: click link tới `zalo.me` / `zalo://` (nút nổi cố định, nút trong section, QR).

```html
<a href="https://zalo.me/84901234567" data-cta="zalo-float">Chat Zalo</a>
```

```html
<script>
document.addEventListener('click', function (e) {
  var a = e.target.closest('a[href*="zalo.me"], a[href^="zalo://"]');
  if (!a) return;
  (window.dataLayer = window.dataLayer || []).push({
    event: 'zalo_click',
    cta_location: a.dataset.cta || 'unknown'
  });
});
</script>
```

`cta_location` bắt buộc có giá trị thật (`zalo-float`, `zalo-bang-gia`, `hotline-sticky`, `hotline-header`…)
— đây là thứ duy nhất cho biết nút nào đang chạy.

### 2.6 `generate_lead` — form gửi thành công

Trigger: **trong handler `submit` của form**, sau khi validate pass, **trước khi trình duyệt điều hướng**.
KHÔNG bắn khi hiện popup "Cảm ơn" mà không có POST thật (xem mục 5 — bẫy kinh điển của Keap).
KHÔNG `preventDefault()`.

Push này nằm **trong script attribution ở mục 4** (nó cần kèm click id) — đừng viết trùng.

```js
{
  event: 'generate_lead',
  form_id: 'hero',
  ngan_sach: 'duoi-2-ty' | '2-4-ty' | '4-7-ty' | 'tren-7-ty',
  muc_dich: 'de-o' | 'dau-tu' | 'cho-thue',
  has_email: true | false,
  gclid: '…', gbraid: '…', wbraid: '…', gad_source: '…', gad_campaignid: '…',
  utm_source: '…', utm_medium: '…', utm_campaign: '…', utm_term: '…', utm_content: '…'
}
```

> `ngan_sach` / `muc_dich` gửi kèm để GA4 chia CVR theo phân khúc.
> **Tuyệt đối không** đẩy tên / SĐT / email vào dataLayer — PII, vi phạm ToS GA4.

### 2.7 Bảng tổng hợp (dán vào ticket cho dev)

| Event | Trigger chính xác | Dedupe | Params bắt buộc |
|---|---|---|---|
| `xem_bang_gia` | section `#bang-gia` ≥50% viewport trong ≥2s **HOẶC** click tab bảng giá | 1×/phiên | `section_id`, `trigger` |
| `xem_mat_bang` | section `#mat-bang` ≥50% viewport trong ≥2s **HOẶC** click tab/thumbnail mặt bằng | 1×/phiên | `section_id`, `trigger` |
| `form_start` | `focusin` đầu tiên vào field của form lead (bỏ qua honeypot) | 1×/phiên | `form_id` |
| `phone_click` | click `a[href^="tel:"]` | không | `phone_number`, `cta_location` |
| `zalo_click` | click `a[href*="zalo.me"]` hoặc `a[href^="zalo://"]` | không | `cta_location` |
| `generate_lead` | trong `submit` handler, sau validate, trước khi navigate | 1×/lần submit | `form_id`, `ngan_sach`, `muc_dich`, `has_email`, click ids |

---

## 3. Form lead — cấu trúc bắt buộc

**4 field + 2 dropdown qualifying** (theo `research/google-ads-bds-vn.md` §6):

| # | Loại | `name=` | Nhãn hiển thị | Bắt buộc | Ghi chú |
|---|---|---|---|---|---|
| 1 | `text` | `name` | Họ và tên | ✅ | ≥2 ký tự |
| 2 | `tel` | `phone` | Số điện thoại | ✅ | validate đầu số VN — mục 3.2 |
| 3 | `email` | `email` | Email (để nhận bảng giá PDF) | ❌ **tùy chọn** | **Nhưng khuyến khích mạnh** — ECL match bằng email tốt nhất |
| 4 | `text` | `biet_qua_dau` | Anh/chị biết dự án qua đâu? | ❌ tùy chọn | Self-reported attribution — thứ duy nhất bắt được truyền miệng & Zalo group (`attribution` skill §4) |
| 5 | `select` | `ngan_sach` | Ngân sách dự kiến | ✅ | `duoi-2-ty` / `2-4-ty` / `4-7-ty` / `tren-7-ty` |
| 6 | `select` | `muc_dich` | Mục đích mua | ✅ | `de-o` / `dau-tu` / `cho-thue` |

2 dropdown này giảm ~15-25% volume nhưng tăng mạnh contact rate — **không được bỏ để "tăng CVR"**.
`<select>` phải có `<option value="" disabled selected>— Chọn —</option>` để không có default lén.

### 3.1 Honeypot (bắt buộc, thay reCAPTCHA ở bước 1)

```html
<div aria-hidden="true" style="position:absolute;left:-9999px;top:auto;width:1px;height:1px;overflow:hidden">
  <label>Website<input type="text" name="website" tabindex="-1" autocomplete="off"></label>
</div>
```

- **KHÔNG** dùng `display:none` (bot hiện đại bỏ qua field ẩn kiểu này).
- Trong `submit` handler: `if (form.website.value) { e.preventDefault(); return; }` — chặn im lặng,
  **không** hiện lỗi (đừng dạy bot).
- Bỏ qua `website` khi bắn `form_start` (mục 2.3).
- reCAPTCHA v3 chỉ thêm khi honeypot không đủ (đo bằng số lead rác thật/tuần), không thêm sẵn.

### 3.2 Validate số điện thoại VN (client-side, chặn trước khi POST)

Đầu số di động VN hợp lệ sau chuẩn hoá 10 số: `03x 05x 07x 08x 09x`.

```js
function normalizePhoneVN(raw) {
  var d = String(raw).replace(/\D/g, '');          // bỏ khoảng trắng, dấu chấm, gạch
  if (d.startsWith('84'))  d = '0' + d.slice(2);   // 84912… → 0912…
  if (d.startsWith('840')) d = '0' + d.slice(3);   // 840912… → 0912…
  return d;
}
function isValidPhoneVN(raw) {
  return /^0(3|5|7|8|9)[0-9]{8}$/.test(normalizePhoneVN(raw));
}
```

- Chuẩn hoá **ghi ngược lại vào input** trước khi submit → Keap luôn nhận `0xxxxxxxxx` 10 số.
  Đây là điều kiện để pipeline ECL hash SĐT ra đúng E.164 (`+84…`) sau này.
- Số bàn (`02x`) → **cho qua nhưng cảnh báo mềm**: "Anh/chị nhập số di động để em gọi/Zalo nhanh hơn".
  Đừng chặn cứng — có khách thật dùng số bàn.
- Chặn cứng: rỗng, sai định dạng, hoặc 10 số giống nhau (`0000000000`, `0999999999`).

### 3.3 Trang cảm ơn

Redirect (không phải popup) tới `/cam-on/` — cần cho: (a) đo `generate_lead` chắc chắn,
(b) peak-end theo `playbook/customer-journey-plan.md` §2.2 giai đoạn 5.
Trang cảm ơn ghi rõ **bước tiếp theo + SLA gọi lại** ("Chuyên viên gọi trong 15 phút, từ số 0901…").

---

## 4. Bắt click id → Keap (bắt buộc — skill `ad-click-attribution`)

Không có bước này thì **không có ECL, không có offline conversion, Data Manager API vô dụng**,
và Google Ads không bao giờ biết keyword nào ra khách thật.

### 4.1 Danh sách param phải bắt

```
Google Ads (auto-tagging):  gclid · gbraid · wbraid · gad_source · gad_campaignid
Manual tag:                 utm_source · utm_medium · utm_campaign · utm_term · utm_content
Fallback:                   document.referrer (chỉ khi khác host)
```

`gbraid`/`wbraid` là bản iOS/app của `gclid` — **thiếu chúng là mất mảng traffic iOS**, không bỏ.

> **Điều kiện tiên quyết:** Google Ads → Settings → Account settings → **Auto-tagging = ON**.
> Không bật thì URL không bao giờ có `gclid` và mọi thứ dưới đây là số 0.

### 4.2 Hidden field trên form

```html
<input type="hidden" name="form_url"        value="">  <!-- LP URL + query click id -->
<input type="hidden" name="gclid"           value="">
<input type="hidden" name="gbraid"          value="">
<input type="hidden" name="wbraid"          value="">
<input type="hidden" name="gad_source"      value="">
<input type="hidden" name="gad_campaignid"  value="">
<input type="hidden" name="utm_source"      value="">
<input type="hidden" name="utm_medium"      value="">
<input type="hidden" name="utm_campaign"    value="">
<input type="hidden" name="utm_term"        value="">
<input type="hidden" name="utm_content"     value="">
<input type="hidden" name="page_referrer"   value="">
```

**Hai đường vào Keap — chọn theo hạ tầng của bạn:**

| Đường | Khi nào | Ưu / nhược |
|---|---|---|
| **A. `form_url` (mặc định — ponytail)** | Dùng proxy WordPress SmartLand `form-dang-ky/<slug>` | Không đổi backend. Proxy map `form_url` → Keap `inf_custom_url`, giữ nguyên query. Pipeline ECL parse `gclid` ra từ URL này. **Chọn cái này nếu đang dùng SmartLand.** |
| **B. Custom field riêng** | Có server proxy tự viết, hoặc gọi Keap REST API trực tiếp | Query được, sạch hơn. **Nhưng nếu endpoint không nhận field → im lặng rơi mất.** Phải test bằng lead thật. |

Đường B cần tạo trước trong Keap (Admin → Settings → Custom Fields → Contact):

| Custom field Keap | Kiểu | Nhận từ |
|---|---|---|
| `GCLID` | Text (255) | `gclid` |
| `GBRAID` | Text (255) | `gbraid` |
| `WBRAID` | Text (255) | `wbraid` |
| `Gad Source` | Text | `gad_source` |
| `Gad Campaign ID` | Text | `gad_campaignid` |
| `UTM Source` / `UTM Medium` / `UTM Campaign` / `UTM Term` / `UTM Content` | Text | `utm_*` |
| `Landing URL` | Text (255) | `form_url` |
| `Ngan Sach` | Dropdown | `ngan_sach` |
| `Muc Dich` | Dropdown | `muc_dich` |
| `Biet Qua Dau` | Text | `biet_qua_dau` |

> **Ghi lại ID số của từng custom field** sau khi tạo (`GET /crm/rest/v1/contacts/model` trả về `custom_fields[].id`).
> `tracking/upload_ecl.py` cần đúng ID đó — không có thì script không tìm được gclid.

### 4.3 Script attribution (dán trước `</body>`)

Bắt click id lúc landing → giữ trong `sessionStorage` (first-touch, không ghi đè) → gắn vào form
lúc submit + push `generate_lead`. **Không `preventDefault`, không `fetch`** — form submit native
(bắt buộc, xem mục 5).

```html
<script>
(function () {
  // ── CONFIG ────────────────────────────────────────────────────────────
  var KEYS = ['gclid','gbraid','wbraid','gad_source','gad_campaignid',
              'utm_source','utm_medium','utm_campaign','utm_term','utm_content'];
  var FORM_SELECTOR = 'form[data-lead-form]';
  var URL_FIELD = 'form_url';
  var STORE = 'attribution';
  // ──────────────────────────────────────────────────────────────────────

  var params = new URLSearchParams(location.search);
  var attribution = {};
  try { attribution = JSON.parse(sessionStorage.getItem(STORE) || '{}'); } catch (e) {}

  var fresh = {};
  KEYS.forEach(function (k) { var v = params.get(k); if (v) fresh[k] = v; });
  var extRef = (document.referrer && document.referrer.indexOf(location.host) === -1)
    ? document.referrer : '';

  // First-touch: URL có click id → đó là nguồn của phiên, không ghi đè bởi lần sau.
  if (Object.keys(fresh).length) {
    if (extRef) fresh.referrer = extRef;
    attribution = fresh;
    try { sessionStorage.setItem(STORE, JSON.stringify(attribution)); } catch (e) {}
  } else if (!sessionStorage.getItem(STORE)) {
    if (extRef) attribution.referrer = extRef;
    try { sessionStorage.setItem(STORE, JSON.stringify(attribution)); } catch (e) {}
  }

  var qs = new URLSearchParams();
  Object.keys(attribution).forEach(function (k) {
    if (k !== 'referrer') qs.set(k, attribution[k]);
  });

  var dl = (window.dataLayer = window.dataLayer || []);

  document.querySelectorAll(FORM_SELECTOR).forEach(function (form) {
    // Điền hidden field ngay khi load (đường B) — không đợi tới submit.
    Object.keys(attribution).forEach(function (k) {
      var el = form.querySelector('input[name="' + k + '"]');
      if (el) el.value = attribution[k];
    });
    var refEl = form.querySelector('input[name="page_referrer"]');
    if (refEl && attribution.referrer) refEl.value = attribution.referrer;

    form.addEventListener('submit', function (e) {
      // honeypot — chặn im lặng
      var hp = form.querySelector('input[name="website"]');
      if (hp && hp.value) { e.preventDefault(); return; }

      // chuẩn hoá + validate SĐT (mục 3.2) — hàm khai báo ở script form
      var ph = form.querySelector('input[name="phone"]');
      if (ph) {
        ph.value = normalizePhoneVN(ph.value);
        if (!isValidPhoneVN(ph.value)) { e.preventDefault(); /* hiện lỗi */ return; }
      }

      // đường A: gắn click id vào form_url mà Keap lưu
      var fu = form.querySelector('input[name="' + URL_FIELD + '"]');
      if (fu) {
        var base = (fu.value || location.origin + location.pathname).split('?')[0];
        fu.value = qs.toString() ? base + '?' + qs.toString() : base;
      }

      var em = form.querySelector('input[name="email"]');
      var ns = form.querySelector('[name="ngan_sach"]');
      var md = form.querySelector('[name="muc_dich"]');

      dl.push(Object.assign({
        event: 'generate_lead',
        form_id: form.getAttribute('data-lead-form') || 'unknown',
        ngan_sach: ns ? ns.value : '',
        muc_dich:  md ? md.value : '',
        has_email: !!(em && em.value)
      }, attribution));
      // KHÔNG preventDefault — form đi tiếp bằng native POST.
    });
  });
})();
</script>
```

### 4.4 Cách tự kiểm tra (không tin code, chỉ tin lead thật)

1. Mở `https://<lp>/?gclid=TEST123&gad_source=1&utm_source=test` → submit form thật.
2. Vào Keap, mở contact vừa tạo → field `Landing URL` (hoặc `GCLID`) phải chứa `TEST123`.
3. Nếu trống: (a) auto-tagging tắt, (b) URL bị 301 rớt query trước khi JS chạy, hoặc
   (c) endpoint không nhận hidden field → chuyển sang đường A (`form_url`).
   **Không phải bug code** cho tới khi loại trừ hết 3 nguyên nhân này.

---

## 5. Gửi form vào Keap — 6 luật không được phá (skill `keap-lead-form`)

Lỗi kinh điển: **form submit, user thấy "Cảm ơn", Keap không có contact nào.**

1. **Form là `<form method="POST" action="…">` native.** Không `fetch`, không `preventDefault`,
   không `mode:'no-cors'`. Proxy SmartLand trả về HTML tự-submit — chỉ **trình duyệt** chạy được
   script đó, `fetch` nhận HTTP 200 rồi lead **rơi im lặng**.
2. **HTTP 200 ≠ đã gửi.** Chỉ tính là thành công khi contact **xuất hiện trong Keap**.
3. Dùng proxy SmartLand → field name là `name` / `phone` / `email` (**không** `inf_field_*`),
   kèm hidden: `form_action=1`, `form_id` (Keap xid), `form_name`, `form_version`, `form_url`.
   Slug trong action URL phải khớp permalink trang proxy.
4. Nhúng Keap trực tiếp (không proxy) → phải có đủ `inf_form_xid`, `inf_form_name`,
   `infusionsoft_version`, `inf_custom_url`, `inf-sbt` (rỗng), **`timeZone`**, + script Keap.
   Thiếu → Keap coi là bot và bỏ. **Mỗi trang chỉ 1 form Keap** (script key theo `inf_form_xid`)
   → nhiều CTA thì dồn hết vào 1 modal.
5. **Không React controlled form** cho form Keap. Astro/HTML tĩnh, hoặc form uncontrolled trong
   `useEffect`. React re-render xoá mất field Keap inject.
6. Màn "Cảm ơn" **chỉ hiện sau POST thật** (redirect `/cam-on/`), không bao giờ là state flip.

---

## 6. Tốc độ & kỹ thuật

| Chỉ số | Ngưỡng | Vì sao |
|---|---|---|
| LCP trên 4G mobile | **< 2,5s** | 75-85% traffic BĐS VN là mobile; chậm = mất lead + Quality Score tụt |
| Tổng trang (nén) | < 1,5 MB | Ảnh dự án là thủ phạm số 1 |
| CLS | < 0,1 | Sticky CTA/Zalo float phải `position:fixed`, không đẩy layout |
| Ảnh | WebP/AVIF, `width`+`height` cố định, `loading="lazy"` từ ảnh thứ 2 | |
| Font | 1 font family, ≤2 weight, `font-display:swap`, self-host | Font Google chặn render |
| Script bên thứ 3 | GTM + Clarity. **Hết.** | Mỗi script thêm = 100-300ms |
| Bảng giá / mặt bằng | **HTML thật, không phải ảnh chụp** | Ảnh → không track được viewport chính xác + không đọc được trên mobile + Google Ads hay disapprove "LP toàn ảnh ít text" |
| Footer | Pháp nhân + MST + địa chỉ + hotline | Thiếu là lý do disapprove phổ biến ở BĐS VN |

Đo bằng PageSpeed Insights **mobile**, không phải desktop. Chưa đạt <2,5s thì chưa được bật ads
(gate G0 trong `playbook/customer-journey-plan.md` §3.1).

---

## 6b. Privacy policy — yêu cầu pháp lý (thêm 2026-07-28, vòng 2 curriculum)

LP phải có link **Chính sách bảo mật** (footer), và nội dung phải khai rõ: thông tin khách
(SĐT/email) được **chia sẻ với bên thứ ba (Google) cho mục đích quảng cáo và đo lường** — đây là
điều kiện bắt buộc của Enhanced Conversions và Customer Match, thiếu nó thì upload dữ liệu hash
là vi phạm điều khoản Google. ⚖️ Câu chữ cuối cùng nên qua tư vấn pháp lý (Nghị định 13/2023 PDPL) —
yêu cầu ở đây là *phải có và phải khai đúng thực tế*, không phải template pháp lý.

## 7. Checklist nghiệm thu (tick hết mới bàn giao)

- [ ] 6 event trong registry bắn đúng, xem được trong **GTM Preview** + **GA4 DebugView**
- [ ] Không có event nào ngoài registry trên dataLayer
- [ ] `xem_bang_gia` / `xem_mat_bang` / `form_start` chỉ bắn **1 lần/phiên**
- [ ] `phone_click` / `zalo_click` có `cta_location` thật, không phải `unknown`
- [ ] `generate_lead` bắn **trong** submit handler, không phải trên trang cảm ơn (tránh mất khi user thoát sớm)
- [ ] Không có tên/SĐT/email trong bất kỳ dataLayer push nào
- [ ] Form có đủ 4 field + 2 dropdown; 2 dropdown `required`, email `optional`
- [ ] Honeypot `website` hoạt động (điền tay → submit → không có contact trong Keap)
- [ ] `0912345678`, `84912345678`, `0912 345 678` đều pass; `0212345678` cảnh báo mềm; `0000000000` chặn
- [ ] Test `?gclid=TEST123` → Keap contact có `TEST123`
- [ ] **1 lead thật đi hết đường LP → Keap** (không phải chỉ HTTP 200)
- [ ] PageSpeed mobile LCP < 2,5s
- [ ] Trang `/cam-on/` tồn tại, có SLA gọi lại
- [ ] Footer đủ pháp nhân + MST + địa chỉ

---

## Đề xuất chờ duyệt

Chưa có. Toàn bộ nhu cầu đo lường hiện tại phủ được bằng 6 event trong registry `CLAUDE.md`.

Ghi chú giải toả cho `playbook/customer-journey-plan.md` §2 (điểm QA A↔C):
`xem_bang_gia`, `xem_mat_bang`, `form_start` **đã nằm trong registry `CLAUDE.md`** → không cần
fallback về `scroll` / `user_engagement`. Audience `engaged_60s` dùng **metric có sẵn của GA4**
(average engagement time per session), **không** cần event mới — xem `tracking/ga4-setup.md` §3.

Nếu sau này cần thêm, đề xuất theo mẫu: `<tên event>` · trigger chính xác · quyết định nào sẽ đổi
khi có số này · vì sao 6 event hiện có không trả lời được. Không có cột 3 thì không duyệt.
