# Plan chạy ads — Beachtro Tower (Blanca City)

Duyệt 2026-08-06. Tài liệu **thực thi**: mở Google Ads UI làm từ trên xuống. Chiến lược nền ở `playbook/campaign-setup.md` + `playbook/customer-journey-plan.md` — file này chỉ ghi phần riêng của dự án.

**Quyết định của user:** chạy **duy nhất 1 campaign brand** · ngân sách **1.000.000 ₫/ngày** · **chưa đặt CPL mục tiêu**, chạy 30 ngày rồi chốt.

**Mọi thao tác trên tài khoản Ads do user tự làm trên UI.** Repo chỉ chuẩn bị dữ liệu và file import.

---

## 1. Cấu trúc — 1 campaign, 2 ad group

| Campaign | Ad group | KW | Ngân sách | CPC cap | Bidding |
|---|---|---|---|---|---|
| `BDS_Search_Brand_DuAn` | `brand-beachtro-tower` (40) · `brand-blanca-city` (41) | **81** | **1.000.000 ₫/ngày** | **28.000 ₫** (nâng từ 20k, lệnh user 2026-08-06 ngày bật) | Maximize Clicks + cap |

**Trần CPC thủ công — chiến lược có mục đích, không phải mặc định vĩnh viễn** (chốt 12/08):
- *Mục đích*: kiểm soát chi khi tracking conversion chưa đủ tin (mới vá trang cám ơn 09/08, chưa đo phone/zalo).
- *Điều kiện thoát* (→ cân nhắc tCPA): conversion ổn định ≥15-20/tháng **và** đã đối chiếu với lead nghiệm thu CRM ≥2 kỳ **và** tracking phone/zalo được vá hoặc chấp nhận bỏ. Chưa đủ cả 3 thì giữ manual.
- *Rủi ro nếu chuyển sớm*: tCPA học trên signal mỏng/rác → bid loạn. (Lưu ý: skill `google-ads` kostja dạy ngưỡng "30 conv/tháng" — dùng làm định hướng, không phải luật; quyết theo chất lượng signal, không theo con số phổ quát.)

File import sẵn: **`keywords/launch-uu-tien-1.tsv`** — 81 dòng, 4 cột `Campaign / Ad group / Keyword / Match type`, 40 exact + 41 phrase, **0 broad**. Lọc theo `uu_tien=1` **hoặc** volume thật > 0.

Final URL cả 2 ad group: `https://smartrealtors.vn/beachtro-tower-blanca-city/`. RSA: 2 bộ trong `ad-copy.md`, mỗi ad group 1 bộ, ghim H1 = headline #1.

Không chạy: brand CĐT Sun Group · khu vực Vũng Tàu · săn brand đối thủ · tài chính/trả góp · remarketing. Bộ keyword của chúng vẫn nằm sẵn trong `keywords/brand.csv` và `master-keywords.csv`, mở khi cần.

### 📊 Search volume thật (Keyword Planner API, 2026-08-06, VN + tiếng Việt)

Volume đã ghi thẳng vào `keywords/brand.csv` (cột `vol_thang`, `canh_tranh`, `bid_thap_d`, `bid_cao_d`, `ngay_do_volume`). Bản chụp rời: `keywords/volume-2026-08-06.csv` · `keywords/keyword-ideas-2026-08-06.csv` (505 ý tưởng).

**Chỉ 9/220 keyword có volume — và toàn bộ nằm ở "blanca city", không phải "beachtro".**

| Keyword | Vol/tháng | Cạnh tranh | Bid đầu trang (thấp–cao) |
|---|---|---|---|
| blanca city | **12.100** | LOW | 8.897 – 30.582 ₫ |
| blanca city vũng tàu | **4.400** | LOW | 9.041 – 37.392 ₫ |
| sun blanca city | 1.300 | LOW | 9.867 – 37.059 ₫ |
| blanca city sun group | 480 | LOW | 11.054 – 42.616 ₫ |
| blanca city giá | 110 | LOW | 7.991 – 37.532 ₫ |
| blanca city vũng tàu giá | 70 | MEDIUM | 9.041 – 39.513 ₫ |
| blanca city vị trí | 30 | LOW | `uu_tien=2` — thêm vào launch vì có volume thật |
| blanca city mở bán | 20 | MEDIUM | 6.493 – 60.890 ₫ |
| blanca city giá bao nhiêu | 10 | MEDIUM | 5.104 – 29.584 ₫ |
| **Tổng** | **18.520** | | |

Ba điều rút ra, ảnh hưởng thẳng tới cách chạy:

**1. Toàn bộ 40 keyword `brand-beachtro-tower` = 0 volume.** Tên "Beachtro" mới ra mắt, chưa ai gõ. Ad group này sẽ gần như **0 impression**. Vẫn **giữ lại** — exact match trên term 0 volume không tốn gì, và đây là bộ hứng sẵn khi CĐT bắt đầu truyền thông tên tòa. Nhưng **đừng chờ traffic từ nó**, và đừng kết luận "ads không chạy" khi thấy ad group này trống.

**2. Ngân sách 1tr₫/ngày là hợp lý hơn tôi ước lượng ban đầu.** Với 18.520 lượt tìm/tháng và bid đầu trang thấp ~9.000 ₫, campaign có khả năng tiêu **khoảng 300–500k₫/ngày**, không phải "nằm chết" như tôi nói trước khi có số. Vẫn theo dõi `budget lost IS`: ≈0% suốt 14 ngày → hạ ngân sách; >0% → ngân sách mới thật sự là nút thắt. **Tuyệt đối không tăng bid chỉ để tiêu cho hết.**

**3. ⚠️ "Blanca City" là brand của Sun Group, KHÔNG phải của riêng Beachtro.** Blanca City là đại đô thị 96 ha gồm nhiều dòng sản phẩm; LP của ta chỉ nói về **4 tòa căn hộ E6–E9**. Người gõ "blanca city" có thể đang tìm biệt thự / shophouse / nhà phố → vào LP căn hộ là lệch nhu cầu, tốn click mà không ra lead.

→ **Đã chốt 2026-08-06** (xác nhận với user): chỉ bán **căn hộ Beachtro**, không bán biệt thự / shophouse / nhà phố. **15 dòng negative cấp campaign** trong `keywords/negative.csv`, dán vào campaign khi dựng:

`biệt thự` · `biet thu` · `shophouse` · `shop house` · `nhà phố` · `nha pho` · `liền kề` · `lien ke` · `đất nền` · `dat nen` · `condotel` · `villa` · `townhouse` · `dưới 1 tỷ` · `duoi 1 ty`

Đã rà chéo: **0 xung đột** với 81 keyword launch và 220 keyword dự phòng của dự án.

⚠️ **Phải ở cấp campaign, KHÔNG được đưa lên account-level** — repo là nền tảng đa dự án, dự án khác có thể bán đúng những dòng sản phẩm này. Đưa lên account là chặn nhầm cả hệ.

⚠️ Mỗi negative đều có **bản không dấu** đi kèm: negative **không khớp close variant** như positive keyword (`research §3`) — thiếu bản không dấu là thủng lưới.

`cho thuê` / `thuê` không có ở đây vì đã nằm sẵn trong 382 dòng negative account-level.

---

## 2. Cài đặt bắt buộc

Đủ 11 ô của `campaign-setup.md §1.5`. Những ô hay bị bỏ sót nhất:

- Mạng đối tác tìm kiếm **TẮT** · Mạng hiển thị / Display Expansion **TẮT**
- Vị trí **Việt Nam**, tuỳ chọn **"Sự hiện diện"** — không phải "sự hiện diện hoặc mối quan tâm"
- Ngôn ngữ **Tiếng Việt + Tiếng Anh** (nhiều máy VN cài trình duyệt EN)
- Tài sản do AI tạo (ACA) **TẮT** · Dynamic sitelinks **TẮT**
- Lịch quảng cáo **05:00–24:00**
- **Auto-apply recommendations TẮT HẾT** (cấp tài khoản) — nguy hiểm nhất là `Remove conflicting negative keywords` (phá negative list) và `Use Display expansion` (bật lại thứ vừa tắt)
- **Tracking template UTM** cấp tài khoản (`§1.5.9`) — ✅ XONG 06/08
- **Negative account-level 382 dòng** — ✅ XONG 06/08. Lệnh xuất ở `campaign-setup.md §1.4`. Đã rà chéo với 81 keyword launch: **0 xung đột**
- RSA: **2 RSA/ad group** ngày 1, chừa 1 slot cho biến thể tuần 3

---

## 3. Lịch triển khai

| Mốc | Việc |
|---|---|
| **D-2** | Nộp xác minh nhà quảng cáo (Tổ chức, chờ 3–5 ngày) · import 382 negative · gắn tracking template UTM |
| **D-1** | **GATE G0** — submit 1 lead test trên LP, xác nhận: Ads có conversion ≤24h **và** Keap có `gclid`. **Trượt G0 = không bật, không ngoại lệ** |
| **D-1** | Dựng campaign + 2 ad group + RSA + 6 sitelink + callout + call asset → để **Tạm dừng** |
| **D+0 06:00** | Bật campaign |
| **D+0 10:00** | Mọi ad ở trạng thái `Đã phê duyệt`? Bị từ chối → sửa và gửi duyệt lại trong ngày |
| **D+0 18:00** | Đã có click chưa? 12h không click → kiểm `Chẩn đoán quảng cáo` ở dòng keyword |
| **D+1** | Lead thật đầu tiên có `gclid` trong Keap? Trống = tracking hỏng → **tạm dừng**, sửa xong mới bật lại |
| **D+3** | Search terms lần 1 — chỉ thêm negative cho term **rõ ràng sai ngành**. Chưa cắt keyword |
| **Tuần 1** | **KHÔNG đổi** bid cap / ngân sách / RSA / keyword. Chỉ thêm negative. Đổi = reset learning |
| **Tuần 2** | Vòng negative đầy đủ theo `keywords/UPDATE.md` · đọc 10 lead gần nhất |
| **Tuần 3** | RSA thứ 2 cho ad group nào mới có 1 · báo cáo theo giờ + thiết bị · kiểm cột `Lượt nhấp không hợp lệ` |
| **Tuần 4** | **Chốt CPL mục tiêu** (§5) · quyết định bidding · điền scorecard `journey-plan §4` · quyết định có mở campaign #2 không |
| **Thứ 6 hằng tuần** | **Tải tay Auction Insights** → `data/ads/auction-insights-<yyyy-mm-dd>.csv`. API không đọc được (allowlist Google đã đóng). Bỏ bước này = mù đúng chỗ bẫy P7 |

---

## 4. Kill rule tháng 1 — cấu trúc, không kinh tế

Chưa có CPL mục tiêu thì mọi lệnh pause theo giá đều là cảm tính. Tháng 1 cắt theo **độ liên quan** và **chất lượng**, cộng một phanh cứng tuyệt đối.

| Tín hiệu | Ngưỡng | Hành động |
|---|---|---|
| Search term sai ngành / sai địa bàn | bất kỳ | → negative ngay, ghi lý do + cấp độ vào `negative-keywords.csv` |
| Quality Score | ≤ 4 sau ≥100 impression | Sửa RSA / chuyển ad group cho khớp chủ đề; không sửa được → pause |
| `post_click_quality_score` | BELOW_AVERAGE | **Lỗi LP, không phải lỗi keyword** → sang `landing-page/`, đừng đụng bid |
| `budget lost IS` | ≈ 0% suốt 14 ngày | **Hạ ngân sách** — brand đã phủ hết. Không tăng bid |
| `rank lost IS` | > 40% **và** chưa tiêu hết ngân sách | Tăng CPC cap **+20%/lần, cách ≥3 ngày** |
| Toàn tài khoản | chi chạm **30tr₫/tháng** | **Phanh cứng** — dừng, review, không tự động tăng |

⚠️ Tháng 1 **không pause keyword vì "đắt"** — chưa có gì định nghĩa được thế nào là đắt.

---

## 5. Chốt CPL mục tiêu ở tuần 4

Cuối tháng 1 có đủ số thật để tính:

```
CPC thực     ← Google Ads
CVR_lp thực  ← GA4 property 548678683
CPL thực     = CPC / CVR_lp
```

Đối chiếu trần kinh tế — **cần user cung cấp 2 số**: phí môi giới TB/căn và tỷ lệ lead→booking.

```
Giá trị 1 booking = phí môi giới TB/căn × (booking → HĐMB %)
Breakeven CPL     = giá trị 1 booking × (lead → booking %)
CPL mục tiêu      = Breakeven CPL × (1 − biên lợi nhuận yêu cầu)
```

`CPL thực > CPL mục tiêu` → tháng 2 chuyển sang cắt theo kinh tế. Ngược lại → scale **≤20%/lần, cách 3–5 ngày**.

⚠️ **Luật Simpson:** khi CĐT công bố bảng giá, LP đổi bản chất → **không so CPL trước/sau**. So cùng campaign, cùng khung ngày. Ghi mốc đổi LP vào nhật ký `PROJECT.md`. Bản nâng cấp (Kohavi): ngày công bố giá = **bắt đầu kỳ đo mới**, hoặc diff-in-diff với một campaign không đổi.

### Kỷ luật đọc số (Kohavi + Binet-Field, chưng cất 2026-08-06 — chi tiết `research/books/`)

1. **CPL tuần 4 chỉ để đặt kill rule.** CẤM dùng nó so "kênh/bộ ad nào tốt hơn về dài hạn" — mọi phép đo dưới ~6 tháng nghiêng hẳn về activation (Binet-Field: hai đường profit cắt nhau ở ~6 tháng).
2. **2 RSA trong cùng ad group KHÔNG phải A/B test.** Google chia impression theo *dự đoán hiệu suất* (assignment phụ thuộc chính thứ đang đo), chung ngân sách, chung mô hình học → không SRM check nào cứu được. Chỉ dùng để Google chọn cái chạy; **cấm kết luận "headline X thắng headline Y"** từ số liệu này.
3. **Cỡ mẫu là con số, không phải cảm tính**: CVR ~3% cần **~12.900 click/nhánh** mới bắt được chênh +20% (n≈16σ²/δ²). Hệ có vài trăm click/tháng → không có A/B hợp lệ nào tồn tại ở quy mô này; công cụ đúng là **user test + thay đổi táo bạo** (making-websites-win) và **fixed-period, không peeking** — chốt khung ngày trước, đọc một lần khi hết kỳ.
4. **Twyman's law**: chỉ số ĐẸP đột biến (CVR ×2, CPL giảm nửa) đáng ngờ ngang chỉ số xấu — kiểm tracking/bot/đếm trùng trước khi ăn mừng.
5. **Guardrail tin cậy có quyền phủ quyết**: ngày nào `gclid` mismatch / tracking gãy → **cấm đọc mọi số khác của ngày đó** (kể cả số đẹp).

---

## 6. Cơ hội đang bỏ trống (số thật, để user quyết sau)

Từ `keywords/keyword-ideas-2026-08-06.csv` — không nằm trong plan hiện tại, ghi lại để tuần 4 cân nhắc:

| Nhóm | Vol/tháng | Bid đầu trang thấp | Ghi chú |
|---|---|---|---|
| `căn hộ vũng tàu` + `chung cư vũng tàu` + biến thể | ~2.500 | **2.060 ₫** | Rẻ hơn brand ~4 lần. Nhưng LP chưa có giá → khách không-brand dễ bỏ đi |
| `căn hộ biển / view biển / gần biển vũng tàu` | ~400 | 1.974–7.381 ₫ | Đúng USP của dự án (1 km bờ biển) |
| Tên tòa đối thủ: `csj tower` 8.100 · `melody` 2.900 · `gateway` 2.900 · `vũng tàu pearl` 720 | ~15.000 | 500–3.000 ₫ | Volume rất lớn, bid rất rẻ — nhưng vướng luật trademark ở ad text (xem `ad-copy.md`) |

Rác đã lộ diện trong dữ liệu, xác nhận giá trị của negative list: `thuê căn hộ vũng tàu` 260 · `căn hộ cho thuê vũng tàu` 170 · `chung cư vũng tàu dưới 1 tỷ` 90.

## 7. Kích hoạt khi CĐT công bố bảng giá

Bước ngoặt lớn nhất của dự án — chuẩn bị trước để không lỡ nhịp:

1. **LP**: thêm khoảng giá vào above-the-fold + **2 dropdown qualifying** — ngân sách theo phân khúc căn hộ (`<2 / 2-4 / 4-7 / >7 tỷ`) + mục đích. Không thêm = hút rác đúng lúc traffic đắt nhất.
2. **`ad-copy.md`**: gỡ lệnh cấm câu có giá, viết lại headline với `Giá Từ …`, `Trả Trước Từ …`.
3. Cân nhắc mở campaign thứ 2 (khu vực Vũng Tàu hoặc tài chính) — lúc này LP mới trả lời được câu hỏi giá của khách không-brand.
4. Ghi mốc vào nhật ký `PROJECT.md` để chặn so sánh sai.
