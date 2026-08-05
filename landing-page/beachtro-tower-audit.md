# Audit LP — Beachtro Tower (Blanca City, Sun Group, Vũng Tàu)

**URL:** https://smartrealtors.vn/beachtro-tower-blanca-city/ · **Audit:** 2026-08-05 (Cowork)
**Ad group brand:** `brand-blanca-city` (110 kw) · Khung chấm: `landing-page/README.md`

> ⚠️ **Phạm vi audit.** Sandbox Cowork bị chặn egress tới `smartrealtors.vn`
> (`x-deny-reason: host_not_allowed`) → chỉ đọc được **nội dung render**, KHÔNG đọc được HTML thô.
> Mọi mục về `dataLayer`, hidden field, widget Zalo, footer pháp nhân, tốc độ tải đều đánh dấu
> **[CHƯA KIỂM]** — phải verify local bằng GTM Preview + PageSpeed trước khi launch.
> Không mục nào được suy đoán thành "đạt".

## 0. Bối cảnh quyết định tất cả: đây là LP GIAI ĐOẠN GIỚI THIỆU

LP tự khai, hai lần: *"Bảng giá và chính sách bán hàng chính thức chưa được công bố."*
Timeline trên trang: hiện tại → 08/2026 là "giai đoạn giới thiệu, chưa công bố bảng giá";
dự kiến ký HĐMB 08/2026; bàn giao 08/2028.

Đây **không phải LP hỏng** — đây là LP thu booking trước mở bán. Nhưng nó xung đột trực tiếp với
một hard gate của README (§Hard gates: *"không có khoảng giá/bảng giá ở bất kỳ đâu"* = KHÔNG launch).
Hard gate đó viết cho LP bán hàng bình thường. Xem §4 để quyết.

## 1. Dữ kiện đã CHỐT (thay bảng "chờ xác nhận" của bản trước)

LP là nguồn của đơn vị phân phối chính thức → thay thế mọi con số báo chí em ghi hôm nay.

| Dữ kiện | Chốt |
|---|---|
| Số căn | **1.785** — E6 506 · E7 379 · E8 363 · E9 537 (cộng lại = 1.785 ✔ nội bộ nhất quán) |
| → Chỉnh lại | Dân trí "gần 2.000" là ước lệ. **1.785 đúng.** |
| Số tầng | E6 34 · E7 38 · E8 40 · E9 36 |
| Bàn giao | **E6 hoàn thiện** (506 căn, ~28%) · **E7/E8/E9 bàn giao thô + gói DyHome** (1.279 căn, ~72%) |
| Sở hữu | Lâu dài — tòa căn hộ SHLD **cuối cùng** của Blanca City |
| Loại căn | Studio · 1BR/1BR+ · 2BR/2BR+ · 3BR/3BR+ |
| Vị trí | Mặt tiền đường 3/2, **P.10 & P.11** (khu du lịch Chí Linh – Cửa Lấp), TP. Vũng Tàu |
| Bàn giao dự kiến | **08/2028** · ký HĐMB dự kiến 08/2026 |
| Chính sách | HTLS 30 tháng · giãn thanh toán 48 tháng · miễn phí QL 2 năm · CK Early Bird 5% · gói Sun Early 70% → nhận nhà. **Nguồn: ấn phẩm SmartRealtors, chưa phải CĐT** |
| Giá | **CHƯA CÔNG BỐ** |
| Phân phối | SmartRealtors & Partners / Smartland — chứng nhận Sun Property cấp **20/09/2025** |
| Hosting | WordPress, theme `smr` → khớp phương án "SmartLand pattern" (PLAN §6.5) |
| GTM | `GTM-TKDNJXJ9` (đã ghi vào SETUP.md) |

## 2. Chấm theo ma trận CRO (README §Ma trận)

| # | Tiêu chí | TS | Điểm | Căn cứ |
|---|---|---|---|---|
| 1 | Message match | 25% | **3** | H1 = *"Bốn tòa căn hộ sở hữu lâu dài trong Blanca City"* — **không chứa chữ "Beachtro Tower"**. Tên chỉ nằm ở title/nav/logo. Luồng `bảng giá` được phục vụ tốt (form "Nhận bảng giá ngay khi công bố" ngay hero); luồng `giá bao nhiêu` không có câu trả lời. Thiếu anchor `#bang-gia` |
| 2 | Above the fold | 20% | **3** | Có: hero, stat bar 4 số (Lâu dài · 04 tòa · 1.785 căn · 8/2028 — USP số rất mạnh), H1, `tel:+84937837888` đúng chuẩn, trust bar. Thiếu: khoảng giá (bất khả kháng), **không thấy Zalo sticky** |
| 3 | Form & qualifying | 15% | **2** | 6 form, đa số chỉ **Họ tên + SĐT**; 1 form có thêm Email (không bắt buộc). **0 dropdown qualifying.** Anchor 1 điểm của README là *"chỉ tên + SĐT — hút rác"*. Điểm cộng: có honeypot ("Để trống ô này") ✔. gclid/utm **[CHƯA KIỂM]** |
| 4 | Offer & con số | 15% | **3** | 5 con số chính sách rõ ràng. Nhưng không có giá để neo, nên không quy đổi được "chỉ X triệu/tháng". Deadline DyHome 31/08/2027 là deadline **thật** ✔ |
| 5 | Objection & trust | 10% | **5** | Xuất sắc. Phân biệt rõ "ảnh chụp thực tế" vs "phối cảnh"; gắn nhãn **dự kiến** cho mọi mốc hạ tầng + câu miễn trừ; mục *"Chưa phù hợp nếu anh/chị…"*; FAQ **từ chối** đưa số lợi nhuận cho thuê; chứng nhận phân phối có ngày. Footer MST **[CHƯA KIỂM]** |
| 6 | Tốc độ & kỹ thuật | 5% | **[CHƯA KIỂM]** | ~40 ảnh (webp + jpg), có cache-buster `?v=0c6558f9`. Rủi ro nặng trang. Phải đo PageSpeed 4G |
| 7 | Đo lường | 10% | **[CHƯA KIỂM]** | GTM `GTM-TKDNJXJ9` có mặt. Nhưng xem §3 — 2/6 event registry **không có gì để bắn** |

**Chưa chấm được điểm tổng** vì 2 tiêu chí (15% trọng số) chưa verify được. Phần chấm được
(1–5, 85% trọng số) quy về thang 100% ≈ **3,1/5 → mức "Đạt, launch được, mục <3 vào backlog"** —
*với điều kiện* 3 hard gate chưa kiểm đều pass.

## 3. Registry 6 event — 2 event không có chỗ bắn

Registry CLAUDE.md là nguồn chân lý, **không đặt tên mới**. Đối chiếu với LP thật:

| Event | Có chỗ bắn trên LP? |
|---|---|
| `form_start` | ✔ 6 form |
| `generate_lead` | ✔ 6 form submit |
| `phone_click` | ✔ `tel:+84937837888` |
| `xem_mat_bang` | ⚠️ chỉ có **form** "Nhận mặt bằng chi tiết", không có mặt bằng để xem trên trang → event này thực chất trùng `generate_lead` |
| `xem_bang_gia` | ❌ **không có block bảng giá** → không có gì để bắn |
| `zalo_click` | ❌ **không thấy Zalo trên trang** |

→ Hai lựa chọn, phải chọn 1 (đừng đổi tên event):
- **(a)** Bổ sung phần tử LP: nút Zalo sticky + block bảng giá (kể cả dạng "khoảng giá dự kiến" hoặc
  bảng so sánh loại căn không giá) → đủ 6/6.
- **(b)** Chấp nhận 4/6 giai đoạn này, ghi rõ trong `tracking/` là 2 event chờ mở, bật lại khi CĐT
  công bố giá. Không xoá khỏi registry.

Khuyến nghị: **Zalo sticky làm ngay** (CTA chính của khách VN theo CLAUDE.md, đang thiếu hẳn một
kênh liên hệ); `xem_bang_gia` để (b).

## 4. Bốn việc nên sửa, xếp theo tác động

**1. Thêm "Beachtro Tower" vào H1** — rẻ nhất, tác động lớn nhất (25% trọng số).
Hiện: *"Bốn tòa căn hộ sở hữu lâu dài trong Blanca City"*.
Đề xuất: *"Beachtro Tower — bốn tòa căn hộ sở hữu lâu dài cuối cùng của Blanca City"*.
Lý do: 110/110 keyword của ad group chứa "beachtro tower" hoặc "blanca city"; H1 hiện chỉ khớp một nửa.

**2. Sửa canonical.** Trang khai `canonical: https://smartrealtors.vn/sun-blanca-city/` và
`og:url` cũng trỏ về đó — tức tự khai mình là **bản trùng lặp** của trang Blanca City.
Không chặn quảng cáo, nhưng sai về SEO và làm lệch mọi báo cáo có gộp theo canonical.
Phải trỏ về chính nó: `https://smartrealtors.vn/beachtro-tower-blanca-city/`.

**3. Form: thêm 2 dropdown qualifying** (`tracking/lp-requirements.md`).
Đây là chỗ đánh đổi thật, cần anh quyết:
- *Giữ 2 field*: volume lead cao nhất — hợp lý ở giai đoạn gom booking chưa có giá.
- *Thêm 2 dropdown*: lead ít hơn nhưng qualify được, và **contact rate >50% là KPI chính của PLAN §0.4**,
  không phải CPL raw. Không có dropdown thì ECL/Keap không có gì để chấm điểm lead.

Thang ngân sách căn hộ chuẩn `<2 / 2–4 / 4–7 / >7 tỷ` — **nhưng chưa có giá thì chưa chốt được thang**.
Đề xuất: giai đoạn này dùng dropdown **mục đích** (ở thực / đầu tư / nghỉ dưỡng cuối tuần) +
**hình thức bàn giao** (hoàn thiện E6 / bàn giao thô DyHome). Cái thứ hai là dropdown qualify tự nhiên
nhất của dự án này — 72% quỹ hàng là bàn giao thô, khách không chấp nhận điều đó thì chỉ còn 28% để bán.

**4. Zalo sticky** — xem §3.

## 5. Ảnh hưởng ngược lại bộ từ khóa

LP có nhiều nội dung mà bộ kw hiện **chưa phủ**: `dyhome`, `bàn giao thô`, `sở hữu lâu dài`,
`e6 e7 e8 e9`, `tro collection`, `whale park`.

Chưa thêm — đúng luật ponytail + UPDATE.md: chờ **search terms report thật** rồi mới thêm, đừng đoán
volume. Ghi lại đây để đối chiếu ở vòng update tuần đầu tiên sau khi chạy.

Ngoại lệ đáng cân nhắc sớm: **`beachtro tower sở hữu lâu dài`** — đây là USP số 1 của dự án và bộ
GENERIC đã có sẵn `sổ hồng lâu dài hay 50 năm`, `condotel có sổ hồng không` (chứng tỏ objection này
có volume thật ở BĐS biển). Không thêm vào `MOD_PROJECT` (sẽ nhân ra 246 dự án, sai) — nếu thêm thì
thêm tay vào `GENERIC` hoặc tạo khối modifier riêng cho dự án đang phân phối.

## 6. Đã trả lời câu hỏi mở của PR #1

**Negative sibling: KHÔNG thêm.** LP ghi SmartRealtors là *"đại lý phân phối chính thức các dự án
Blanca City"* (số nhiều) và có hẳn FAQ so sánh Beachtro vs Beacon Tower. Chặn `beacon tower` sẽ tự
chặn hàng của chính mình. → Đề xuất ngược lại: cân nhắc thêm `beacon tower` thành **dòng dự án riêng**
trong `projects.tsv` khi anh xác nhận đang bán, vì nó khác hẳn về hình thức bàn giao (message match khác).

## 7. Hard gate — chưa cái nào certify được từ cloud

| Hard gate | Trạng thái |
|---|---|
| Tiêu chí 7 (Đo lường) ≥3 | **[CHƯA KIỂM]** — cần GTM Preview |
| Có khoảng giá/bảng giá | ❌ **KHÔNG CÓ** — bất khả kháng, cần anh quyết theo §0 |
| Load ≤4s trên 4G | **[CHƯA KIỂM]** — cần PageSpeed |
| Pháp nhân/MST ở footer | **[CHƯA KIỂM]** — rủi ro disapproved "Unclear relevance" |
| gclid tới Keap | **[CHƯA KIỂM]** — hỏng cái này là mất toàn bộ chuỗi ECL |

**Kết luận:** Cowork **không certify launch** được. 4 mục cần chạy local (GTM Preview, PageSpeed,
xem footer, test gclid→Keap); 1 mục là quyết định kinh doanh của anh, không phải lỗi kỹ thuật.
