# Round 7 — Contact rate sập 30tr

Kịch bản: 30tr₫/tháng (1.000.000₫/ngày), căn hộ **Thủ Đức**, CPC kịch bản **30.000₫**. Mô phỏng 4 tuần.
Ngân sách tuần = 7.000.000₫ · Click/tuần = 7.000.000 / 30.000 = **233,3** (không có % click rác vì negative list vào ngày 1 — `sim-rules` phạt kỷ luật #3).

## Setup tuần 0 (quyết định + căn cứ doc)

**Pre-flight (`campaign-setup` §1)**
- §1.1 Advertiser verification nộp trước tiên (30 ngày không nộp = treo tài khoản, `research` §7). Footer LP có pháp nhân + MST + địa chỉ + hotline.
- §1.2 Tạo **cả 6 conversion action** ngay: `Lead_Form_Raw`/`Click_Hotline`/`Click_Zalo` = Primary ngày 1; `Lead_Contactable`(10)/`Lead_Qualified`(50)/`Dat_Coc`(500) tạo rỗng chờ ECL. Count = One, cửa sổ click **90 ngày**, goal **category** đúng chuẩn (§1.2.7). `Lead_Contactable` khai là mục tiêu chính của tài khoản để pipeline ECL không phải sửa schema.
- §1.3 Auto-tagging ON, link GA4↔Ads, bắn 1 lead thật kiểm gclid vào Keap → **điều kiện G0** (`journey-plan` §3.1).
- §1.4 **386 negative account-level ngày 1** (+ shared list 80 dòng campaign-level). Bản không dấu bắt buộc — negative không khớp close variant (`research` §3).
- §1.5 **11 ô**, trong đó ô quyết định round này: **§1.5.1 Search Partners = TẮT** · §1.5.2 Display Expansion TẮT · §1.5.4 location **Presence** · §1.5.6 ACA TẮT · §1.5.7 lịch 05:00–24:00 · §1.5.11 auto-apply TẮT HẾT · §1.5.10 không dùng shared budget.
- Call asset: lịch = **giờ trực máy**, hẹp hơn lịch campaign (§3.4). Google call forwarding TẮT (chưa hỗ trợ VN).

**Cấu trúc campaign — 3 campaign, không 5** (`journey-plan` §3: 30tr = uu_tien 1, bottom funnel 85%)

| # | Campaign | ₫/ngày | Bid cap | Ad group (từ `adgroup-map`) | kw uu_tien=1 |
|---|---|---|---|---|---|
| 1 | `BDS_Search_Brand_DuAn` | 475.000 | 20.000 | `brand-masteri-grand-view`, `brand-lumiere-midtown`, `brand-vinhomes-grand-park` (3 = trần §2.3) | 24 |
| 2 | `BDS_Search_Brand_CDT` | 75.000 | 25.000 | `brand-cdt--masterise-homes` | 5 |
| 3 | `BDS_Search_KhuVuc_GiaoDich` | **450.000** | 35.000 | `thu-duc--gia-bang-gia`, `thu-duc--mua-ban` (2 = trần §2.3) | 20 |
| | **Tổng** | **1.000.000** | | 6 ad group | **49** |

Hai lệch so với bảng §2.1, có căn cứ:
- **#8 NhaOXaHoi = 0₫** — không phân phối NOXH (§2.1 ghi chú "không thì dồn vào #3").
- **#4 TaiChinh = 0₫** — kiểm bộ kw: `thu-duc--tai-chinh` và `tai-chinh` **không có dòng nào ở `uu_tien=1`** (chỉ có ở 2/3). Ở kịch bản 30tr chỉ bật uu_tien 1 (`journey-plan` §3) → campaign sẽ rỗng. 70k+30k dồn vào #3.
- #7 Discovery (broad) và RMKT = **0₫ — hoãn** (§2.1: broad cần tCPA; G2 chưa mở).

**Bidding:** tất cả **Maximize Clicks + bid cap** (`research` §4, bậc 0 của §3.2). Không tCPA, không Max Conversions — 0 conversion ngày 1.

**LP spec (`landing-page/README.md`)** — 3 luồng H1 riêng, message match chấm **4/5** cho nhóm brand (H1 = tên dự án + bảng giá đợt này), Zalo sticky + `tel:` thật, form **4 field + 2 dropdown** (ngân sách / mục đích) + honeypot + validate đầu số VN + hidden gclid/utm. 6 event đúng registry `CLAUDE.md`.
Nghiệm thu tuần 0 **thiếu 1 mục**: bảng giá **chưa above the fold** (phải scroll mới thấy) → tiêu chí 2 chấm 3/5, tổng vẫn ≥3,0 nên được launch, mục <3 vào backlog tuần 1 (thang kết luận `landing-page/README`).

**CVR LP theo công thức `sim-rules`:** 2,0 nền + 1,0 (message match ≥4/5) + 0,6 (Zalo sticky + click-to-call) + 0,4 (form 2 dropdown) = **4,0%** tuần 1; **+0,8 = 4,8%** từ tuần 2 sau khi vá bảng giá above the fold. Trần 6,0 chưa chạm.
**Qualify rate 40%** (2 dropdown). **Contact rate mô hình 55%** (dropdown + validate đầu số + SLA <5').

## Nhật ký tuần 1-4

| Tuần | Chi tiêu | Click | Lead raw | Lead qualified | Contact rate | CPL-q | Sự kiện | Hành động + căn cứ |
|---|---|---|---|---|---|---|---|---|
| 1 | 7.000.000 | 233 | **9,3** (CVR 4,0%) | 3,7 | 55% | **1.875k** | — | **Không đổi gì**: bid cap, ngân sách, RSA, keyword (`campaign-setup` §4.1 "Tuần 1 KHÔNG đổi"). Chỉ 2 việc được phép: D+3 negative cho term rõ sai ngành; **backlog LP** → yêu cầu user đưa bảng giá lên above the fold (`landing-page/README` yếu tố 2). D+1 kiểm gclid trong Keap ✔ |
| 2 | 7.000.000 | 233 | **11,2** (CVR 4,8% — LP đã vá) | 4,5 | **25%** ⚠️ | 1.563k | **Contact rate 55%→25%, volume lead TĂNG** | Chẩn đoán 3 bước §8-T3 (bảng dưới) → **nguyên nhân là SLA vỡ, không phải lead rác** → xử phía process, **không đụng Ads**. Vòng negative đầy đủ 3 lượt + cập nhật `keywords/` vẫn chạy như thường lệ (`journey-plan` §5) |
| 3 | 7.000.000 | 233 | 11,2 | 4,5 | 55% (hồi) | 1.563k | 8,4 lead nguội tuần 2 | Gọi cứu 8,4 lead nguội — kết quả `[điền — không có công thức trong sim-rules]`, **ghi riêng, không cộng vào contact rate tuần 3**. Việc riêng tuần 3 (§4.1): báo cáo theo giờ/thiết bị, cột **Lượt nhấp không hợp lệ** (<10% = bình thường, `research` §5), thêm **RSA thứ 2** vào 6 ad group (đổi 1 biến: góc offer) |
| 4 | 7.000.000 | 233 | 11,2 | 4,5 | 55% | 1.563k | — | Đo CVR LP thật = 4,8% (>2% → LP không hỏng, `research` §6). **Quyết định bidding: GIỮ Max Clicks** (bảng dưới). Rà gate G1–G5: không mở gate nào. Điền tháng 1 vào scorecard `journey-plan` §4 |

### Chẩn đoán tuần 2 — đúng thứ tự `research` §8 (T3)

**Bước 1 — đối chiếu Ads vs Keap (trước khi đọc lead, trước khi kết luận)**

| Kiểm | Số | Đọc ra gì |
|---|---|---|
| Ads: click / chi tiêu | 233 / 7.000.000₫ | Không có spike, pacing bình thường |
| Ads: **Phân đoạn → Mạng (Network)** | **100% "Tìm kiếm của Google", 0 impression/click từ Đối tác tìm kiếm** | ✅ **§1.5.1 tuần 0 đã tắt Search Partners** → **loại bỏ giả thuyết lead rác đến từ Search Partners**. Đây là bước phân định hai nhánh nguyên nhân, phải làm TRƯỚC khi đọc lead |
| Ads: Lượt nhấp không hợp lệ | <10% | Bình thường (`research` §5) |
| Ads: `generate_lead` (import GA4) | 11 | — |
| Keap: lead mới cùng kỳ | 11 | **Khớp — không lệch nguồn**, không phải lỗi tracking/dedup. CRM là nguồn chân lý (`journey-plan` §4) |
| Keap: lead có gclid | 11/11 | Attribution nguyên vẹn |
| Keap: lead điền đủ 2 dropdown + đầu số VN hợp lệ | 11/11 | **Chất lượng đầu vào KHÔNG đổi** so với tuần 1 |
| Search terms tuần 2 | 0 term sai intent ≥3 click | Negative list còn hiệu lực (biết trước là không phủ hết — `research` §3 hộp privacy threshold) |

Kết luận bước 1: **volume tăng đúng bằng mức LP vá above the fold dự đoán (CVR 4,0→4,8%), không có nguồn traffic mới nào, chất lượng đầu vào không đổi.** Nếu là lead rác thì phải thấy: có chi tiêu ở mạng đối tác, hoặc lead thiếu gclid, hoặc đầu số/dropdown rác. **Không thấy cái nào.**

**Bước 2 — đọc 10 lead gần nhất (`research` §8 T3, `campaign-setup` §4.1 tuần 2)**

| Quan sát trên 10 lead | Số |
|---|---|
| Nội dung lead hợp lý (ngân sách 2–4 tỷ, mục đích ở, khu vực Thủ Đức/Q9/Bình Thạnh) | 10/10 |
| Có **activity gọi ra** trong Keap | **2–3/10** |
| Lead tạo trong cửa sổ **31/12 – 2/1** không có activity nào | **8/10** |
| Lead ĐƯỢC gọi thì có liên hệ được không | **3/3 = 100%** |

🔎 **Bằng chứng quyết định:** contact rate **trên số lead được bấm gọi = 100%**, contact rate **trên tổng lead = 25%**. Mẫu số vỡ, không phải tử số. Lead không xấu — **lead không được gọi**.

**Bước 3 — kết luận + hành động**

> **Nguyên nhân gốc: SLA gọi vỡ — sale nghỉ Tết dương 3 ngày (31/12–2/1), không ai trực máy.** Xử lý **phía process**, không phải phía Ads.

Vì sao KHÔNG được xử phía Ads (kỷ luật, `campaign-setup` §4.2–4.3 · `journey-plan` §3.1):
- Không cắt ngân sách, không hạ bid, không pause keyword: chỉ số vỡ nằm **sau** lead, kill rule neo vào CPL vs mục tiêu và contact rate **như tín hiệu chất lượng lead** — chất lượng lead ở đây nguyên vẹn.
- Không cắt >20% ngân sách cho 3 ngày nghỉ: `sim-rules` phạt learning reset (CVR ×0,7 tuần sau) và `research` §4 — đổi ngân sách ±20%/lần. Cũng **không tắt** (mất learning). Tết dương lịch **không phải** sự kiện mùa vụ của §4 (Tết âm + tháng 7 âm mới là).
- `Seasonal budget adjustment` không dùng được: chỉ **tăng** budget, và **không dùng được khi campaign có dayparting** — hệ đang chạy lịch 05:00–24:00 (§1.5.7). `Seasonality adjustment` cũng không: chỉ chạy với tCPA/tROAS (`research` §4 bảng).

Hành động phía process (rẻ nhất, đúng gốc):
1. **Lịch trực luân phiên gắn với lịch nghỉ** — ngày không có người trực thì không mua click mình không trả lời được. Việc Ads duy nhất được phép: **Call asset schedule = giờ trực máy** (§3.4) và tắt/chuyển hotline trong ngày nghỉ — không đụng bid/budget/learning.
2. **Điền SLA vào `journey-plan` §5 nhịp ngày mục 4** (ô đang `[điền SLA — giờ]`): **5 phút trong giờ trực, 30 phút ngoài giờ, 100% lead có người bấm gọi trong 24h**. Đây là ô doc đang trống mà round này chứng minh là tốn tiền nhất.
3. **Keap automation** (không cần người): auto-assign lead + auto Zalo/SMS phản hồi ngay khi submit + task nhắc 15' + escalate nếu 60' chưa có activity. Giữ được "khách được ai đó trả lời" khi không có người trực.
4. **Rescue 8,4 lead nguội** ở tuần 3, ghi kết quả riêng.
5. **Nối vào ECL (PLAN §6.6):** 3 ngày không gắn tag = 3 ngày không có `Lead_Contactable`. Nếu lúc đó đã ở smart bidding, bidding sẽ học "keyword này không ra lead contactable" từ một lỗi nhân sự → **thêm một lý do giữ Max Clicks** và siết SLA gắn tag ≤48h (muộn nhất 7 ngày).

*(Nhánh còn lại, để lại dấu vết quyết định: nếu bước 1 thấy có chi tiêu ở **Đối tác tìm kiếm** thì kết luận ngược — lead rác từ Search Partners, xử phía Ads: tắt §1.5.1 ngay, lọc lead theo network, bổ negative, và **không** đổ lỗi cho sale. Ở round này bước 1 đã loại nhánh đó bằng số.)*

### Quyết định bidding tuần 4 — GIỮ Max Clicks

| Điều kiện §4.4 (Max Clicks → Maximize Conversions, phải ĐỦ CẢ) | Thực tế 30 ngày | |
|---|---|---|
| Campaign ≥15 conversion/30 ngày | #1 = 20,4 · #3 = 19,3 · #2 = 3,2 | ✅ (#1, #3) |
| Đã chạy ≥4 tuần | 4 tuần | ✅ |
| **Contact rate >50%** | **47,2%** | ❌ |

→ **Không chuyển.** Tuần Tết dương kéo cửa sổ 30 ngày xuống dưới ngưỡng; 14 ngày gần nhất là 55% nhưng doc ghi **30 ngày** — không "làm sạch" số bằng cách loại bỏ tuần xấu (`journey-plan` Q3/Q8). Chạy lại gate cuối tuần 5–6 khi cửa sổ 30 ngày sạch. #2 dưới 15 conv → theo `journey-plan` §3 thì **gộp, không tách** (ứng viên gộp vào #1 ở tháng 2).
Hệ quả kéo theo: bậc 2 (`tCPA` + test broad) cần **ECL chạy thật** — chưa có credentials/tag Keap → **#7 Discovery giữ 0₫**. Không nhảy bậc (`journey-plan` §3.2).

## Tổng kết

| Chỉ số | 4 tuần |
|---|---|
| Chi tiêu | **28.000.000₫** (4×7tr; trần tháng 30,4tr) |
| Click | **933** |
| **Contact rate (KPI #1, báo cáo trước CPL — `research` §5)** | **47,2%** (20,2/42,9) — dưới mốc 50%, **toàn bộ khoảng cách nằm ở tuần 2**; 3 tuần còn lại = 55% |
| Lead raw | **42,9** |
| Lead contactable | **20,2** |
| Lead qualified | **17,2** (qualify 40%) |
| **CPL qualified** | **1.630.000₫** |
| CPL raw | 652.000₫ |
| CVR LP | 4,0% tuần 1 → **4,8%** tuần 2–4 (đích `research` §6: 3–6%) |
| CTR **giả định** | **7,6%** → ~12.300 impression/tháng. `sim-rules` không có công thức CTR; số này lấy từ WordStream 2026 Real Estate (`research` §2, Mỹ) làm **mốc lập kế hoạch**, không phải số đo — theo luật "không bịa số" (`tracking/README` #5) |
| Trạng thái gate cuối kỳ | **G0 ✅** · **G1 ❌** (CPL mục tiêu chưa tính được — thiếu phí môi giới/căn, `journey-plan` §6) · **G2 ❌** (933 click/tháng → audience `xem_bang_gia_30d` không thể đạt ≥1.000 user/30 ngày) · **G3/G4/G5 ❌** · Bidding: **bậc 0** (Max Clicks), bậc 1 khoá bởi contact rate 47,2% |

So kịch bản trung bình `research` §2 (CPL qualified 1.560k): **1.630k, cao hơn 4,5%** — chênh lệch đúng bằng tuần 1 chạy ở CVR 4,0% trước khi vá LP. Nếu 4 tuần đều 4,8% thì CPL-q = 1.563k, khớp mô hình.

**3 bài học**

1. **Contact rate là chỉ số phân số — luôn kiểm mẫu số trước tử số.** "Contact rate 25%" có thể là lead xấu (tử số) hoặc lead không được gọi (mẫu số). Số phân định là **contact rate trên số lead ĐƯỢC bấm gọi**: ở đây 100% vs 25% → chốt ngay là process. Thêm cột này vào digest tuần của `playbook/monitoring.md` §4.
2. **Bước "Phân đoạn → Mạng" phải nằm TRƯỚC bước đọc lead.** Nó là thứ duy nhất phân định "lead rác từ Search Partners" với "lead tốt không ai gọi" — hai nguyên nhân có triệu chứng giống nhau nhưng hành động ngược nhau (một sửa Ads, một sửa process). Chẩn đoán sai thứ tự = cắt ngân sách một campaign đang chạy tốt.
3. **Ô `[điền SLA — giờ]` bỏ trống trong doc là ô đắt nhất của hệ.** 3 ngày không ai gọi = 8,4 lead (≈1,2tr₫ CPL-q mỗi cái) nguội + gate Maximize Conversions bị khoá thêm 2 tuần vì cửa sổ 30 ngày bẩn. Volume lead tăng che mất việc này trong mọi báo cáo chỉ đọc CPL — đúng lý do `research` §5 buộc contact rate đứng trước CPL.
