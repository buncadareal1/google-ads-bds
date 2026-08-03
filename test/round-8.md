# Round 8 — Thắng nhưng nghẽn 30tr (căn hộ Bình Dương)

Kịch bản: 30tr₫/tháng, CPC 26k₫, campaign đang chạy TỐT (CPL qualified 1,1tr dưới trần, contact rate 57%).
Sự kiện tiêm tuần 2-3: **Search IS lost (budget) = 25% liên tục**, ngân sách cạn trước 19h hằng ngày.

## Setup tuần 0 (quyết định + căn cứ doc)

**Cấu trúc — 4 campaign, không thêm loại nào** (`journey-plan` §3 kịch bản 30tr: bottom funnel 85%):

| # | Campaign | ₫/ngày | Bid cap | Ad group | Căn cứ |
|---|---|---|---|---|---|
| 1 | `BDS_Search_Brand_DuAn` | 475.000 | 20.000 | 3 (3 dự án Bình Dương đang phân phối) | `campaign-setup` §2.1, §2.3 (475k÷20k ≈ 24 click/ngày → tối đa 3 ad group giữ ngưỡng ≥10 conv/ad group) |
| 2 | `BDS_Search_Brand_CDT` | 75.000 | 25.000 | 1 | §2.1 |
| 3 | `BDS_Search_KhuVuc_GiaoDich` | 380.000 | 35.000 | 2 (`binh-duong--gia-bang-gia`, `binh-duong--mua-ban`) | §2.1 + 30k của #8 dồn vào đây |
| 4 | `BDS_Search_TaiChinh` | 70.000 | 30.000 | 1 | §2.1 |
| 8 | `BDS_Search_NhaOXaHoi` | **0** | — | — | §2.1: chỉ bật nếu **thực sự** phân phối NOXH. Không → dồn vào #3 (Ponytail) |
| 7 | `Discovery` (broad) | **0 — hoãn** | — | — | `adgroup-map` #7 bắt buộc tCPA; ngày 1 chưa có conversion |
| — | `RMKT` Demand Gen | **0 — hoãn** | — | — | Chưa qua **G2** (`journey-plan` §3.1) |

**Bidding:** Max Clicks + bid cap toàn bộ (`research` §4 — tuần 1-3 không smart bidding). Bậc 0 của `journey-plan` §3.2.

**Conversion:** đủ 6 action theo `campaign-setup` §1.2, cửa sổ click **90 ngày**, Count = One, goal category chuẩn (§1.2.7). Ngày 1 primary = `generate_lead` + `phone_click` + `zalo_click`; `phone_click`/`zalo_click` **Secondary vĩnh viễn** khi ECL chạy (`tracking/README` luật #2).

**Negative:** 386 dòng account-level dán **ngày 1** (§1.4.1) + shared list 80 dòng campaign-level cho #1-#4. Không dán = phạt 25% ngân sách tuần 1-2 (sim-rules) — tránh được.

**LP spec chọn (quyết định CVR):** LP riêng từng dự án, message match 3 luồng ≥4/5, bảng giá above the fold, Zalo sticky + `tel:`, form 4 field + 2 dropdown qualifying (ngân sách, mục đích) + validate đầu số + honeypot + hidden `gclid`. Không homepage.

→ **CVR mô hình = 2,0 + 1,0 (message match) + 0,8 (bảng giá ATF) + 0,6 (Zalo sticky+call) + 0,4 (form 2 dropdown) = 4,8%** (trần 6,0). **Qualify 40%** (2 dropdown). **Contact 55%** (dropdown + validate + SLA gọi <5').

⚠️ **Rủi ro nằm ngoài tầm kiểm soát của hệ:** contact 55% phụ thuộc **SLA gọi <5'** — `PLAN.md` §6.6 ghi quy trình sau-lead đang **PENDING** (user chưa có quyền xem quy trình sale). SLA vỡ → contact tụt về 35% → **điều kiện tăng ngân sách không còn thoả**. Toàn bộ quyết định scale của round này treo trên một cam kết của sales, không phải trên số ads.

**Ký tự RSA — bẫy đã bắt:** `campaign-setup` §3.2 headline #1 `Căn Hộ {Quận} Giá Từ {Giá từ}` có trần `{Quận}` = 9 ký tự; "Bình Dương" = 10 → vượt (31/30). Sửa thành **`Căn Hộ Bình Dương Từ {Giá từ}` = 27** (bỏ "Giá"), giữ pin H1. Kiểm lại #3, #5 bằng script §3.5 trước khi dán.

**Đối chiếu số kịch bản ↔ công thức sim (không bịa, ghi cả hai):**

| Chỉ số | Công thức sim-rules | Kịch bản tiêm | Xử lý |
|---|---|---|---|
| CPL qualified | `26.000 ÷ (4,8% × 40%)` = **1.354k** | 1.100k | Dùng **1.354k** để vận hành (suy được từ công thức). 1.100k hàm ý CVR ~5,9% hoặc CPC thực ~21k — không có luật nào cho ra số đó |
| Contact rate | 55% | 57% | Chênh 2đ trong nhiễu; ghi 55% (công thức), nhắc số kịch bản |
| Trần CPL | `[điền]` — `journey-plan` §4 cần phí môi giới/căn + tỷ lệ booking→HĐMB (user chưa cấp) | "dưới trần" | Tạm neo vào mốc kịch bản trung bình **1.560k** (`research` §2). **Cả 1.354k và 1.100k đều dưới mốc → quyết định tăng ngân sách không đổi theo cách chọn số** |

## Nhật ký tuần 1-4

| Tuần | Chi tiêu | Click | Lead raw | Lead qual | Contact rate | CPL-q | Sự kiện | Hành động + căn cứ |
|---|---|---|---|---|---|---|---|---|
| 1 | 7.000.000 | 269 | 12,9 | 5,2 | 55% | 1.354k | — | T2 nghi thức search terms 3 lượt → negative mới (`journey-plan` §5). T3 contact rate + upload ECL. T5 đọc IS lost lần đầu (baseline). **KHÔNG đổi bid cap/ngân sách/RSA/keyword** (`campaign-setup` §4.1 tuần 1) |
| 2 | 7.684.000 | 296 | 14,2 | 5,7 <br>*(57% kịch bản)* | 1.354k | **IS lost (budget) 25%** D8-D9-D10; ngân sách cạn trước 19h | D10 (Daily Close 20:00): điều kiện `monitoring` §3 **thoả đủ 3 phần** — IS lost ≥10% ×3 ngày + CPL 1.354k ≤ mốc 1.560k + contact 57% >50%. → **Xin duyệt user cả kế hoạch 2 nhịp** (vượt ngân sách tháng đã chốt = ngoài whitelist ±20% ở §6). D11 user duyệt → **apply nhịp 1: +20% CHỈ cho #1 và #3** |
| 3 | 9.632.000 | 370 | 17,8 | 7,1 | 55% | 1.354k | IS lost vẫn 25% D12-D13-D14 | D15 = **≥4 ngày** sau D11 (`monitoring` §3 giới hạn "cách ≥3-4 ngày") → re-check điều kiện tại thời điểm apply (luật an toàn #4) → **apply nhịp 2: +20%**. Sau D15 **đóng băng** mọi thay đổi khác (learning phase guard §2). T4 xin báo cáo theo **giờ** (`campaign-setup` §4.1 tuần 3) |
| 4 | 9.632.000 | 370 | 17,8 | 7,1 | 55% | 1.354k | IS lost (budget) **< 10%** | Giữ nguyên. Năng lực mới 1.376k/1.000k = **1,376×** > **1,333×** mà 25% IS lost hàm ý → hết headroom, dừng tăng. Chờ **4 tuần** mới phán xét (`research` §4). T6 báo cáo tháng + review gate |
| **Tổng** | **33.948.000** | **1.306** | **62,7** | **25,1** | **55%** (34,5 lead liên hệ được) | **1.354k** | | |

### Hai nhịp tăng — con số áp vào từng campaign

Tăng vào **campaign đang limited**, không rải đều (whitelist `monitoring` §6: `budget_change` ±20% so budget hiện tại **của campaign đó**). Kịch bản chỉ cấp 1 số IS lost → dồn vào #1+#3 vì đó là nơi giữ **85,5% chi tiêu** và toàn bộ volume; #2/#4 ở 75k/70k giữ nguyên (Ponytail: không chi thêm vào nơi chưa chứng minh thiếu). Với số thật: đọc IS lost **từng campaign** trước khi apply.

| Campaign | Ngày 1 | Nhịp 1 (D11) | Δ | Nhịp 2 (D15) | Δ |
|---|---|---|---|---|---|
| #1 `Brand_DuAn` | 475.000 | 570.000 | +20,0% | 684.000 | +20,0% |
| #3 `KhuVuc_GiaoDich` | 380.000 | 456.000 | +20,0% | 547.000 | +20,0% |
| #2 `Brand_CDT` | 75.000 | 75.000 | — | 75.000 | — |
| #4 `TaiChinh` | 70.000 | 70.000 | — | 70.000 | — |
| **Tổng/ngày** | **1.000.000** | **1.171.000** | **+17,1%** | **1.376.000** | **+17,5%** |
| Trần tháng (×30,4) | 30,4tr | 35,6tr | | **41,8tr** | |

≤20% ở **cả hai cấp** (campaign và tài khoản) → không kích phạt learning reset của sim-rules.

**Nội dung tin xin duyệt (D10)** — phải có 3 phần theo `monitoring` §3 (số căn cứ + hành động + rủi ro):
- Căn cứ: IS lost (budget) 25% ×3 ngày · CPL-q 1.354k ≤ mốc 1.560k · contact 57% · ngân sách cạn trước 19h.
- Hành động: 2 nhịp +20% (D11, D15) chỉ vào #1+#3 → 1.376k/ngày.
- **Hai con số tiền phải nói rõ, đừng lẫn:** tháng NÀY chỉ vượt **33,9tr** (do tăng giữa tháng); **41,8tr là mức tháng LẶP LẠI** từ tháng sau → cần user chốt riêng khoản chi định kỳ, không suy ra từ 2 nhịp đã duyệt.
- Rủi ro: click biên (marginal) thường chuyển đổi kém hơn click đầu — công thức sim tuyến tính nên CPL-q giữ 1.354k, nhưng với số thật phải đo lại CPL-q sau 7-30 ngày, không đọc theo ngày (`monitoring` §1 hộp cảnh báo).
- Action hết hạn 24h không duyệt → phát lại với số mới (luật an toàn #2).

### Cái KHÔNG làm — và vì sao (kỷ luật gate)

| Việc hấp dẫn | Từ chối vì |
|---|---|
| Nhảy 1 phát 30tr → 45tr | **>±20% = learning reset** (sim-rules). Xem đối chứng dưới |
| Tăng bid cap thay vì ngân sách | `campaign-setup` §2.2: chỉ tăng cap khi **IS lost (xếp hạng) >40% VÀ chưa tiêu hết ngân sách**. Ở đây tiêu hết ngân sách → "đó là vấn đề ngân sách", không phải bid |
| `Seasonal budget adjustment` | Chỉ cho đợt 3-14 ngày rồi tự trả về mức cũ. Nghẽn ở đây là **cấu trúc**, không phải event → dùng đổi ngân sách thường (`monitoring` §3) |
| `Seasonality adjustment` | Chỉ hợp lệ với tCPA/tROAS. Đang ở Max Clicks → **API từ chối** (`monitoring` §3 GUARD 1) |
| Bật #7 Discovery broad với tiền mới | `adgroup-map` #7 bắt buộc tCPA; `research` §3: "critical to use Smart Bidding with broad match". Chưa tới bậc 2 (`journey-plan` §3.2) |
| Bật Demand Gen remarketing (quỹ 10%) | **G2 chưa mở**: cần audience ≥1.000 user/30 ngày. Tổng click/30 ngày ≈ 1.306 → `xem_bang_gia` là **tập con** của số đó nên chắc chắn <1.000 |
| Lên bộ campaign "bậc 60tr" (`campaign-setup` §5.2) | 41,8tr **không phải** bậc 60tr. Tiền mới vào campaign đang thắng, không mở campaign type mới (§5.7: một gate mỗi lần) |
| Đổi sang Maximize Conversions ngay | Đủ volume ở cấp tài khoản nhưng **không chồng đổi chiến lược lên 2 nhịp ngân sách đang settle**. Hoãn tới tuần 5+, và phải verify ≥15 conv/30 ngày **cấp campaign** (§4.4), không phải cấp tài khoản |
| Thêm dự án thứ 4 vào #1 | #1 ở 684k÷20k ≈ 34 click/ngày có chỗ cho ~5 ad group, nhưng chỉ có 3 dự án đang phân phối. Ghi nhận headroom, không hành động (Ponytail) |

### Đối chứng cái bẫy: nếu nhảy 1 phát 30tr → 45tr (D11)

45tr ÷ 30,4 = 1.480k/ngày = **+48%** → vi phạm ±20% → learning reset → **tuần kế tiếp CVR ×0,7 = 3,36%**.

| | Đường kỷ luật (tuần 3) | Nhảy 1 phát (tuần kế tiếp) |
|---|---|---|
| Chi tiêu tuần | 9.632.000 | 10.362.000 (**+7,6%**) |
| Click | 370 | 399 |
| Lead qualified | **7,1** | **5,4** |
| CPL-q | **1.354k** | **1.934k** — vượt mốc 1.560k |

→ Chi thêm tiền để nhận **ít hơn 25% lead qualified** và CPL-q xấu hơn 43%. Đây là toàn bộ lý do luật ±20% tồn tại.
*(Ghi chú trung thực: ở Max Clicks bidding không học từ conversion nên reset thực tế nhẹ hơn ở tCPA. Vẫn tuân thủ ≤20% — luật nội bộ `research` §4 và sim-rules không phân biệt bậc, và cái giá của việc sai thì bất đối xứng.)*

## Tổng kết

**Số 4 tuần** — báo cáo **contact rate trước CPL** (`research` §5):

| Chỉ số | Giá trị |
|---|---|
| Contact rate | **55%** (34,5 lead liên hệ được) — kịch bản đo 57% |
| Lead raw | **62,7** · Lead qualified **25,1** |
| Chi tiêu | **33.948.000 ₫** (30tr đã chốt + 3,9tr đã xin duyệt) |
| **CPL qualified** | **1.354k ₫** — dưới mốc kịch bản trung bình 1.560k (`research` §2). Trần thật vẫn là `[điền]` |
| CPL raw | 542k ₫ |
| Click / CPC | 1.306 / 26.000 ₫ |
| **CTR giả định** | **7,61%** → impression ≈ **17.200**. Đây là benchmark WordStream 2026 Real Estate (Mỹ, `research` §2) — **giả định, không phải số đo**; VN không có CTR BĐS đáng tin. Không dùng nó làm KPI |
| Ngân sách cuối kỳ | 1.376.000 ₫/ngày = **41,8tr/tháng lặp lại** (chờ user chốt khoản định kỳ) |

**Trạng thái gate cuối kỳ:**

| Gate | Trạng thái | Thiếu gì |
|---|---|---|
| G0 | ✅ Đạt | — |
| G1 (mở rộng T2) | ⛔ **Không kết luận được** | Ngưỡng conv/tháng của G1 vẫn là `[điền]` **và** trần CPL thật chưa có (phí môi giới/căn + booking→HĐMB, `journey-plan` §6). Không có 2 số này thì "CPL ≤ mục tiêu" là đoán |
| G2 (Demand Gen RMKT) | ⛔ Đóng | Audience `xem_bang_gia` <1.000 user/30 ngày (tổng click chỉ 1.306) |
| G3 (Search T3) | ⛔ Đóng | Cần G2 trước |
| G4 (PMax) | ⛔ Đóng | Qualified 25,1 < 30/tháng; và `campaign-setup` §5.4 QA chưa chốt (a)/(b) → không bật kể cả khi qua G4 |
| G5 (YouTube) | ⛔ Đóng | Ngân sách 41,8tr < 150tr |
| Bậc bidding (`journey-plan` §3.2) | **Bậc 0** → đề xuất lên **bậc 1** ở tuần 5 | Verify ≥15 conv/30 ngày **cấp campaign** cho #1; đảo primary sang `Lead_Contactable` **trước** khi bật Max Conversions |

**3 bài học:**

1. **"Nghẽn ngân sách" không phải giấy phép chi tự do — nó là một điều kiện trong ba.** IS lost ≥10% chỉ mở khoá khi CPL đạt **và** contact đạt. Round này cả ba đều đạt nên tăng là đúng; nhưng contact 57% đến từ **SLA gọi <5' của sales** — thứ `PLAN.md` §6.6 ghi là PENDING. Đòn bẩy quyết định của round không nằm trong tài khoản Ads.
2. **Hai nhịp +20% (1,44×) phủ được 25% IS lost (cần 1,33×) mà không mất một tuần CVR nào.** Nhảy 1 phát chi thêm 7,6% tiền để nhận ít hơn 25% lead qualified. Kiên nhẫn 4 ngày rẻ hơn một tuần learning.
3. **Tiền mới phải chảy vào chỗ đã chứng minh thắng, không mở cửa mới.** 41,8tr đi hết vào #1 và #3 — không Discovery broad, không Demand Gen, không "bậc 60tr", vì gate không mở theo ngân sách mà mở theo **dữ liệu conversion**. Kèm một bẫy giao tiếp phải nói rõ với user: tháng chuyển tiếp vượt **33,9tr**, còn **41,8tr là con số của tháng sau** — duyệt 2 nhịp không có nghĩa là đã duyệt khoản chi định kỳ.
