# Plan chạy ads — Beachtro Tower (Blanca City)

Duyệt 2026-08-06. Tài liệu **thực thi**: mở Google Ads UI làm từ trên xuống. Chiến lược nền ở `playbook/campaign-setup.md` + `playbook/customer-journey-plan.md` — file này chỉ ghi phần riêng của dự án.

**Quyết định của user:** chạy **duy nhất 1 campaign brand** · ngân sách **1.000.000 ₫/ngày** · **chưa đặt CPL mục tiêu**, chạy 30 ngày rồi chốt.

**Mọi thao tác trên tài khoản Ads do user tự làm trên UI.** Repo chỉ chuẩn bị dữ liệu và file import.

---

## 1. Cấu trúc — 1 campaign, 2 ad group

| Campaign | Ad group | KW | Ngân sách | CPC cap | Bidding |
|---|---|---|---|---|---|
| `BDS_Search_Brand_DuAn` | `brand-beachtro-tower` (40) · `brand-blanca-city` (40) | **80** | **1.000.000 ₫/ngày** | **20.000 ₫** | Maximize Clicks + cap |

File import sẵn: **`keywords/launch-uu-tien-1.tsv`** — 80 dòng, 4 cột `Campaign / Ad group / Keyword / Match type`, 40 exact + 40 phrase, **0 broad**.

Final URL cả 2 ad group: `https://smartrealtors.vn/beachtro-tower-blanca-city/`. RSA: 2 bộ trong `ad-copy.md`, mỗi ad group 1 bộ, ghim H1 = headline #1.

Không chạy: brand CĐT Sun Group · khu vực Vũng Tàu · săn brand đối thủ · tài chính/trả góp · remarketing. Bộ keyword của chúng vẫn nằm sẵn trong `keywords/brand.csv` và `master-keywords.csv`, mở khi cần.

### ⚠️ Ngân sách sẽ KHÔNG tiêu hết — và đó là chuyện bình thường

80 keyword brand của một dự án chưa công bố giá không có đủ lượt tìm kiếm để tiêu 1tr₫/ngày. Với Maximize Clicks + CPC cap, phần thừa **không rò rỉ** sang keyword rộng (chỉ broad match mới vậy) — nó đơn giản không tiêu.

Nên **đừng đọc "chi tiêu thấp" là thất bại**, và tuyệt đối **đừng tăng bid để tiêu cho hết**. Chỉ số phải nhìn là `budget lost IS`:

- `budget lost IS` ≈ **0%** → ngân sách đang thừa. Brand đã phủ hết phần có thể phủ. **Hạ ngân sách**, hoặc mở thêm campaign khu vực nếu muốn dùng hết tiền.
- `budget lost IS` > **0%** → ngân sách đang thật sự là nút thắt, lúc đó mới tính chuyện tăng.

---

## 2. Cài đặt bắt buộc

Đủ 11 ô của `campaign-setup.md §1.5`. Những ô hay bị bỏ sót nhất:

- Mạng đối tác tìm kiếm **TẮT** · Mạng hiển thị / Display Expansion **TẮT**
- Vị trí **Việt Nam**, tuỳ chọn **"Sự hiện diện"** — không phải "sự hiện diện hoặc mối quan tâm"
- Ngôn ngữ **Tiếng Việt + Tiếng Anh** (nhiều máy VN cài trình duyệt EN)
- Tài sản do AI tạo (ACA) **TẮT** · Dynamic sitelinks **TẮT**
- Lịch quảng cáo **05:00–24:00**
- **Auto-apply recommendations TẮT HẾT** (cấp tài khoản) — nguy hiểm nhất là `Remove conflicting negative keywords` (phá negative list) và `Use Display expansion` (bật lại thứ vừa tắt)
- **Tracking template UTM** cấp tài khoản (`§1.5.9`) — hiện **rỗng**
- **Negative account-level 382 dòng** — hiện mới **1 dòng**. Lệnh xuất ở `campaign-setup.md §1.4`. Đã rà chéo với 80 keyword launch: **0 xung đột**
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

⚠️ **Luật Simpson:** khi CĐT công bố bảng giá, LP đổi bản chất → **không so CPL trước/sau**. So cùng campaign, cùng khung ngày. Ghi mốc đổi LP vào nhật ký `PROJECT.md`.

---

## 6. Kích hoạt khi CĐT công bố bảng giá

Bước ngoặt lớn nhất của dự án — chuẩn bị trước để không lỡ nhịp:

1. **LP**: thêm khoảng giá vào above-the-fold + **2 dropdown qualifying** — ngân sách theo phân khúc căn hộ (`<2 / 2-4 / 4-7 / >7 tỷ`) + mục đích. Không thêm = hút rác đúng lúc traffic đắt nhất.
2. **`ad-copy.md`**: gỡ lệnh cấm câu có giá, viết lại headline với `Giá Từ …`, `Trả Trước Từ …`.
3. Cân nhắc mở campaign thứ 2 (khu vực Vũng Tàu hoặc tài chính) — lúc này LP mới trả lời được câu hỏi giá của khách không-brand.
4. Ghi mốc vào nhật ký `PROJECT.md` để chặn so sánh sai.
