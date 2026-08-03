# Microsoft Clarity — checklist

Miễn phí, không sampling, heatmap + session replay. Dùng để **giải thích** vì sao CVR thấp;
GA4 nói *bao nhiêu*, Clarity nói *tại sao*.

## 1. Cài

1. clarity.microsoft.com → New project → domain LP → lấy Project ID.
   **Dùng toàn trang được và nên**: 1 project = 1 domain, gắn script `<head>` toàn site (miễn phí,
   không sampling); phân tích LP bằng filter URL. LP ở domain riêng → project riêng cho domain đó.
   Quota MCP 10 req/ngày tính theo project.
2. Dán script vào LP, `async`, cuối `<head>` hoặc trước `</body>`
   (`tracking/lp-requirements.md` §1, script #4). **Không** cài qua GTM — thêm một tầng chậm và
   session replay hay mất đoạn đầu.
3. Settings → **Masking = Balanced** → toàn bộ input text bị che. Kiểm tra 1 replay: không được
   thấy tên/SĐT/email của khách.
4. Settings → IP blocking → chặn IP văn phòng.
5. `CLARITY_API_TOKEN` (Settings → Data export) → biến môi trường cho MCP trong `.mcp.json`.

## 1b. Kết nối chéo Google Ads (native integration, từ 1/2025)

Clarity có **Advertising dashboard** kết nối trực tiếp tài khoản Google Ads: spend/CPC hiển thị cạnh
dữ liệu hành vi, và **lọc recordings/heatmaps theo campaign/ad** — xem đúng phiên của keyword đang
tốn tiền nhất để biết *tại sao* nó không ra lead.

1. Clarity → Settings → **Integrations → Google Ads** → OAuth tài khoản ads.
2. **Bắt buộc có UTM** — auto-tagging (gclid) một mình không đủ để Clarity lọc theo campaign.
   Google Ads → Account settings → Tracking template (cấp tài khoản, không reset learning):
   `{lpurl}?utm_source=google&utm_medium=cpc&utm_campaign={campaignid}&utm_term={keyword}&utm_content={creative}`
   (LP đã capture utm_* theo lp-requirements.md nên không cần sửa gì thêm phía LP.)
3. Giới hạn hiểu đúng: dữ liệu chỉ chảy **một chiều Ads → Clarity** (chẩn đoán). Smart bidding
   KHÔNG học được gì từ Clarity — đòn bẩy bidding vẫn là ECL (`ecl-keap-pipeline.md`).

### 1c. Custom tags — lớp lọc BỔ SUNG (không thay tracking template UTM)

Cú pháp đã verify 2026-07-28: [Clarity API](https://learn.microsoft.com/en-us/clarity/setup-and-installation/clarity-api) · [Custom tags](https://learn.microsoft.com/en-us/clarity/filters/custom-tags) *(URL cũ `/custom-tags/custom-tags` đã chết; canonical mới là `/filters/custom-tags`)*.

```javascript
// Đặt trong đoạn code LP đã capture gclid/utm (skill ad-click-attribution) — 8 dòng, 0 hạ tầng.
(function () {
  if (typeof window.clarity !== "function") return;      // Clarity snippet phải load trước
  var p = new URLSearchParams(window.location.search);
  if (p.get("gclid") || p.get("gad_source")) window.clarity("set", "traffic", "ads");
  var c = p.get("utm_campaign");
  if (c) window.clarity("set", "campaign", c.slice(0, 255));
})();
```

Ràng buộc từ docs Microsoft:
- `clarity("set", key, value)` — `value` là **string hoặc array of string** (array = gọi nhiều lần tuần tự).
- **Tag và value ≤255 ký tự**; **≤128 tag/trang** (call thứ 129 bị bỏ qua); **không giới hạn** tổng số tag distinct trong project.
- Tag mới xuất hiện trong Filters UI sau **30 phút – 2 giờ**, không phải ngay.
- Custom tag dùng được ở **Recordings + Heatmaps + Dashboard**, và **lưu được thành saved segment** (dùng luôn ở mục 2 dưới).
- ⚠️ **Không đưa PII vào tag.** Khác với `identify` API (Clarity tự hash `custom-id` trên client), giá trị custom tag **không được hash** → hiện plain text trong dashboard. Chỉ dùng nhãn nghiệp vụ: `traffic`, `campaign`, `du_an`.
- **CHƯA XÁC NHẬN:** docs không nói tag có áp **hồi tố** cho cả session hay chỉ từ lúc gọi. Cứ gọi càng sớm càng tốt.

> ⚖️ **QUAN HỆ VỚI §1b (đã QA chốt):** vòng research đề xuất dùng custom tag **để bỏ** yêu cầu tracking template UTM. **KHÔNG áp dụng đề xuất đó** — `playbook/campaign-setup.md` §1.5.9 đã chốt tracking template UTM là **bắt buộc** (nó phục vụ cả Advertising dashboard native của Clarity, thứ custom tag không thay được). Custom tag ở đây là lớp **bổ sung**: cho `traffic=ads` cấp nhanh, độc lập với Ads, và sống được cả khi tracking template bị ai đó xoá. Hai thứ cộng vào nhau, không thay nhau.

## 2. Xem hàng tuần — 15 phút, thứ 5

Đúng 4 việc. Không lướt replay vô định.

| # | Xem gì | Ở đâu | Hành động khi thấy |
|---|---|---|---|
| 1 | **Rage click trên form** | Dashboard → Rage clicks, lọc selector form lead | Field nào bị đập liên tục = dropdown khó bấm trên mobile, nút submit không phản hồi, hoặc lỗi validate không hiện. Sửa ngay — đây là lead đang mất. |
| 2 | **Dead click trên form + bảng giá** | Dashboard → Dead clicks | Khách bấm vào thứ trông như bấm được mà không phải: ảnh bảng giá, số điện thoại dạng text (phải là `<a href="tel:">`), tab không hoạt động. |
| 3 | **Scroll depth tới section bảng giá** | Heatmaps → Scroll | < 50% tới được bảng giá = bảng giá nằm quá sâu → đẩy lên trên. Đối chiếu với `xem_bang_gia` trong GA4 — lệch nhiều nghĩa là trigger viewport sai. |
| 4 | **3 replay của phiên có `form_start` mà không `generate_lead`** | Recordings → filter **Smart Event `Submit Form` = không xảy ra** (chính xác hơn cách cũ "thời lượng >60s + không có trang `/cam-on/`" — gián tiếp và dễ sai) | Xem khách dừng ở field nào. Đây là nguồn hypothesis test tuần tới. |
| 5 | **Campaign tốn tiền nhất tuần này** | Recordings → filter Google Ads campaign (mục 1b) | Xem 3 replay từ campaign có spend cao nhất nhưng CVR thấp nhất: khách từ keyword đó tìm gì mà LP không có? Kết quả đổ vào cột "message match" của adgroup-map. |

Ghi 1 dòng kết luận vào báo cáo thứ 6. Không có phát hiện = ghi "không có" — cũng là dữ liệu.

### 2a. Ba việc setup 1 lần để 15 phút thứ 5 thành 5 phút

1. **Smart Events** ([docs](https://learn.microsoft.com/en-us/clarity/setup-and-installation/smart-events)) — Clarity **tự phát hiện** 9 loại auto event, trong đó 3 cái map thẳng vào hệ: `Submit Form` ≈ `generate_lead`, `Contact Us` / `Request Quote` ≈ `phone_click` + `zalo_click`. **Code-free**, trần 20 custom smart event, chỉ admin project tạo được.
   ⛔ **KHÔNG dùng Smart Event làm nguồn conversion.** Registry 6 event của `CLAUDE.md` là nguồn duy nhất; Smart Event không đẩy sang GA4/Ads → dùng làm conversion sẽ sinh nguồn đếm thứ 5 không ai đối chiếu được. Nó **chỉ để lọc replay**.
2. **Saved segments** — lưu sẵn 3 combo filter thay vì lọc tay mỗi tuần: (a) `Submit Form` không xảy ra + có `form_start`; (b) `traffic=ads` (custom tag §1c) + rage click; (c) campaign spend cao nhất tuần. Custom tag + Smart Event đều là **universal filter** → lưu được thành segment, dùng ở cả Recordings/Heatmaps/Dashboard.
3. **Copilot** — dùng để **tìm** replay đáng xem và tóm tắt heatmap, không phải để thay việc xem. Với hạn mức "3 replay/tuần" của hệ, đây là cách rút ngắn thật.

## 2b. Data retention — bẫy với chu kỳ BĐS

Clarity giữ **session replay chỉ 30 ngày** (favorite = 9 tháng) — trong khi chu kỳ mua BĐS 3-12 tháng.
Phiên của lead sẽ mất trước khi lead chốt. Luật: mỗi tuần khi review (mục 2), **favorite replay của
mọi phiên có `generate_lead`** — sau này khi lead thành booking, còn xem lại được hành vi ban đầu
của đúng người mua thật (nguồn insight LP giá trị nhất).

## 3. Kỷ luật MCP: 10 request/ngày

Clarity API cho **10 request/ngày/project**. Hết là hết, không mua thêm.

- **Đọc 1 lần/tuần**, gộp thành 1 phiên hỏi (~3-4 request). Đừng hỏi rải rác cả tuần.
- Hỏi ở mức **tổng hợp** (metric theo dimension), không kéo từng session.
- Cần nhìn kỹ replay → mở **web UI**, không tốn quota API.
- Debug tracking → dùng **GTM Preview + GA4 DebugView**, không phải Clarity MCP.
- Hết quota giữa tuần = mất khả năng đọc số tới hôm sau. Không có cách khôi phục.
