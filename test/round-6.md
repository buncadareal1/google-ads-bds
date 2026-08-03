# Round 6 — Xuyên Tết 30tr

Kịch bản: 30tr₫/tháng (1.000.000₫/ngày), căn hộ **Hà Nội**, CPC kịch bản **27.000₫**, chạy tháng 1–2 dương lịch.
Sự kiện tiêm: **tuần 3–4 = 2 tuần Tết Nguyên đán** → demand −40%, CVR × 0,6.
Mốc thời gian dùng tương đối (D+0 = ngày launch, thứ 2). Tuần 1 = D+0…D+6, tuần 2 = D+7…D+13, tuần 3 = D+14…D+20 (mùng 1 rơi vào đầu tuần 3), tuần 4 = D+21…D+27.

---

## Setup tuần 0 (quyết định + căn cứ doc)

**Pre-flight (làm xong mới bật ad)** — `campaign-setup` §1, gate **G0** (`journey-plan` §3.1):
advertiser verification (Tổ chức) · billing VND + GMT+7 · 6 conversion action theo thang 1/10/50/500 (`PLAN` §0.4), count=One, cửa sổ click **90 ngày** (`tracking` luật #4), goal category chuẩn §1.2.7 · GA4↔Ads link + auto-tagging · **386 negative account-level** dán ngày 1 (§1.4.1) · 11 ô cài đặt §1.5 (Search Partners OFF, Display OFF, location **Presence**, ACA OFF, auto-apply OFF, lịch 05:00–24:00, tracking template UTM) · bắn 1 lead thật kiểm gclid tới Keap.

**Conversion primary ngày 1** = `Lead_Form_Raw` (`generate_lead`). `phone_click`/`zalo_click` để **Secondary** — theo `tracking/README` luật #2 + `PLAN` §4, KHÔNG theo bảng `campaign-setup` §1.2 (bảng đó ghi action 1–3 đều "Chính" ngày 1 → **hai doc đá nhau, đã chọn tracking/README vì nó là luật bất di bất dịch**).

**Cấu trúc campaign** (`campaign-setup` §2.1, `journey-plan` §3 — 85% bottom funnel):

| # | Campaign | ₫/ngày | Bid cap | Ad group (từ `keywords/`) | KW `uu_tien=1` |
|---|---|---|---|---|---|
| 1 | `BDS_Search_Brand_DuAn` | **505.000** | 22.000 | `brand-vinhomes-smart-city`, `brand-lumi-hanoi`, `brand-the-senique-hanoi` | 24 |
| 2 | `BDS_Search_Brand_CDT` | **75.000** | 27.000 | `brand-cdt--capitaland` | 5 |
| 3 | `BDS_Search_KhuVuc_GiaoDich` | **420.000** | 35.000 | `nam-tu-liem--gia-bang-gia`, `gia-lam--gia-bang-gia` | 30 |
| 4 | `BDS_Search_TaiChinh` | **0 — không dựng** | — | — | **0** |
| 8 | `BDS_Search_NhaOXaHoi` | **0** | — | không phân phối NOXH → dồn vào #3 (§2.1 ghi chú) | — |
| 7 | `BDS_Search_Discovery` (broad) | **0 — hoãn** | — | bắt buộc tCPA, ngày 1 có 0 conversion (§2.1) | — |
| — | Remarketing Demand Gen | **0 — hoãn** | — | chưa qua **G2** (≥1.000 user/30 ngày) | — |
| | **Tổng** | **1.000.000** | | 6 ad group | **59** |

- **3 dự án ở #1** = trần §2.3 (505k ÷ 22k ≈ 23 click/ngày, giữ ngưỡng ≥10 conv/ad group của `adgroup-map`). Chọn 2 dự án Nam Từ Liêm + 1 Gia Lâm để **khớp đúng 2 cụm địa lý** của #3 (`adgroup-map` §cụm: Tây HN / Đông HN) — 1 LP dùng được cho cả luồng brand và luồng khu vực.
- **#4 TaiChinh không dựng — phát hiện khi lọc bộ launch:** `uu_tien=1` có **0 keyword** nào thuộc `tai-chinh|phan-khuc-ngan-sach|cau-hinh-can` (toàn bộ ở `uu_tien` 2–3), mà kịch bản 30tr chỉ bật `uu_tien=1` (`journey-plan` §3). Dựng campaign rỗng = không dựng. 70k của nó + 30k của #8 → 30k cho #1, 70k cho #3.
- **Bid cap neo vào CPC kịch bản 27k** (không copy nguyên dải 20/25/35k của §2.2 vốn neo vào 25k): brand rẻ hơn nên cap dưới 27k, khu vực head term cap 35k → CPC hoà chung rơi về 27k.
- Đã lọc bỏ keyword `--generic-dat-nen`, `--generic-nha-pho`, `--generic-biet-thu` của 2 khu vực (LP là căn hộ → message match sai loại hình).
- Kiểm sau import: 0 keyword ở match type **Rộng** (§2.4.6 — broad là default, sai cột là thành broad im lặng); mỗi ad group có Final URL riêng, **không ad group nào trỏ homepage** (§2.4.7).
- RSA: 2 bộ/ad group, bộ 1 cho #1/#2, bộ 2 cho #3 (`campaign-setup` §3.1/§3.2), **pin H1 = headline #1**. Mọi `{Giá từ}`, `{Vay%}`, chiết khấu = `[điền từ bảng giá đợt hiện tại]` — chưa có bảng giá thật thì **bỏ headline chứa số**, không bịa (misrepresentation, `research` §7). Headline `Giá Gốc CĐT` chỉ dùng nếu LP có dòng "đơn vị phân phối, không phải chủ đầu tư".

**LP spec chọn (quyết định CVR theo sim-rules):** 3 LP dự án, mobile-first 390px.

| Yếu tố | Có | Điểm CVR |
|---|---|---|
| Nền | | 2,0 |
| Message match brand ≥4/5 (H1 = "{Dự án} Bảng Giá Mới Nhất" = headline #1 đã pin) | ✔ | +1,0 |
| Bảng giá/khoảng giá above the fold | ✔ | +0,8 |
| Zalo sticky + `tel:` click-to-call | ✔ | +0,6 |
| Form 4 field + 2 dropdown qualifying (ngân sách, mục đích) | ✔ | +0,4 |
| **CVR LP** | | **4,8%** (trần 6,0) |

→ **Qualify rate 40%** (có 2 dropdown) · **Contact rate 55%** (2 dropdown + validate đầu số VN + SLA gọi <5′, gồm cả **lịch trực Tết**, xem tuần 2).
Luồng khu vực dùng chung LP dự án → message match chỉ ~3,5/5 (không đủ 4/5, **không cộng điểm lần hai** — sim-rules chỉ cộng cho nhóm ad chính). Backlog: thêm section + anchor `#bang-gia-nam-tu-liem` khi #3 đủ volume.

**Kế hoạch Tết chốt từ tuần 0** (không đợi tới lúc đó mới nghĩ) — `research` §4 Mùa vụ:
1. Giảm **40–60% ngân sách, KHÔNG tắt** (tắt = mất learning).
2. Giảm bằng **thao tác ngân sách tay, theo bậc ≤20%/lần cách ≥3 ngày** (`research` §4 luật nội bộ + sim-rules phạt kỷ luật). 0,8³ = **−48,8%**.
3. Cắt **TRƯỚC Tết** (trong tuần 2) để mức thấp đã tại chỗ đúng lúc demand rơi — và để mọi lần chỉnh ngân sách rơi vào tuần bình thường, không rơi vào tuần Tết.
4. **KHÔNG dùng seasonality adjustment** — 3 lý do độc lập (`research` §4 bảng 2 công cụ): (a) Google nói không dùng cho seasonality **định kỳ**; (b) event >14 ngày; (c) nó chỉ chạy với **tCPA/tROAS**, hệ đang Max Clicks → bật cũng vô nghĩa. **Seasonal budget adjustment cũng không dùng được** vì nó **chỉ TĂNG** budget.

---

## Nhật ký tuần 1–4

Công thức: `click = chi tiêu / 27.000` (negative list dán ngày 1 → tỷ lệ click rác chưa lọc = 0, không ăn phạt 25%) · `lead raw = click × CVR` · `lead-q = lead raw × 0,40` · `CPL-q = chi tiêu / lead-q`.

| Tuần | Chi tiêu | Click | Lead raw | Lead-q | Contact rate | CPL-q | Sự kiện | Hành động + căn cứ |
|---|---|---|---|---|---|---|---|---|
| **1** | 7.000.000 | 259,3 | 12,44 (CVR 4,8%) | 4,98 | 55% (6,84 liên hệ được) | 1.406k | — | **KHÔNG đổi gì**: bid cap, ngân sách, RSA, keyword (`campaign-setup` §4.1 tuần 1 — đổi = reset learning). D+0 kiểm ad đã phê duyệt + click đầu; D+1 kiểm gclid trong Keap; D+3 negative vòng 1 chỉ cho term **rõ ràng sai ngành**. T6 báo cáo. |
| **2** | 5.120.000 | 189,6 | 9,10 (CVR 4,8%) | 3,64 | 55% (5,01) | 1.406k | Chuẩn bị Tết | **Bậc ngân sách 1: D+7 1.000k → 800k (−20%)**; **bậc 2: D+11 800k → 640k (−20%)** (cách 4 ngày ≥3 ✔, mỗi lần ≤20% ✔ → không reset learning). Nghi thức search terms **3 lượt** (`journey-plan` §5) + cập nhật `keywords/` theo `UPDATE.md`. Đọc **10 lead gần nhất**, tính contact rate lần đầu. **Chốt lịch trực Tết**: 1 người/ngày giữ SLA <5′ trên Zalo + hotline (giữ contact rate 55% — mất SLA là mất 20 điểm contact rate, đắt hơn mọi thứ khác trong tuần Tết). LP thêm dòng "Tư vấn qua Zalo cả Tết" (không cộng điểm CVR — không thuộc 4 yếu tố sim-rules). |
| **3** | 3.584.000 | 132,7 | 3,82 (CVR 2,88% = 4,8 × 0,6) | 1,53 | 55% (2,10) | **2.344k** | **Tết tuần 1**: demand −40%, CVR ×0,6 | **Bậc ngân sách 3: D+14 640k → 512k (−20%)**, cách D+11 3 ngày ✔ → tổng **−48,8%**, nằm trong dải 40–60% (`research` §4). **Sau đó ĐÓNG BĂNG**: không đổi ngân sách/bid cap/keyword/RSA/bid strategy hết Tết. **KHÔNG tắt campaign** (bẫy: tắt → tuần sau Tết CVR ×0,7). Chỉ giữ 2 việc không đụng learning: checklist ngày (pacing, disapproved, LP uptime, lead→CRM) + vòng negative. **Kiểm trần demand:** pool click Tết ≈ 259,3 × 0,6 = 155,6/tuần > 132,7 mua được → ngân sách vẫn tiêu hết ở đúng intent, không bị đẩy vào inventory rác. |
| **4** | 3.584.000 | 132,7 | 3,82 (CVR 2,88%) | 1,53 | 55% (2,10) | **2.344k** | **Tết tuần 2** | Giữ 512k, không thao tác. T3 lead quality: contact rate vẫn 55% (nhờ trực Tết) → **không có vấn đề chất lượng**. **Chẩn đoán đúng nguyên nhân CVR:** 2,88% vẫn **>2%** ⇒ theo `research` §6 đây **không phải LP hỏng**, là sụt mùa vụ → **không sửa LP, không đụng bid** giữa Tết (sửa lúc này là vừa mất learning vừa sửa sai chỗ). CPL-q 2.344k > mục tiêu nhưng **không kích kill rule**: kill rule (`journey-plan` §3.1) neo vào `CPL mục tiêu` tính từ breakeven, mà phí môi giới/căn user chưa cung cấp (`journey-plan` §6) → chưa có quyền kết luận, ghi nhận và chờ. Điền scorecard tháng 1 (`journey-plan` §4). |

**Kế hoạch bung lại sau Tết (D+28 → D+40)** — cũng ≤20%/lần, cách ≥3 ngày, và **theo đúng hình dạng đường hồi phục** (khách quay lại dần từ mùng 6, không nhảy vọt):

| Ngày | Ngân sách | Δ | Ghi chú |
|---|---|---|---|
| D+28 | 512k → **614k** | +20% | mùng 6–7, người đi làm lại |
| D+32 | 614k → **737k** | +20% | |
| D+36 | 737k → **885k** | +20% | |
| D+40 | 885k → **1.000k** | +13% | về 100% |

- Trong 12 ngày bung lại: **không đổi bid strategy song song** (một thay đổi một lúc).
- **8,71tr₫ tiết kiệm được trong Tết** (28tr kế hoạch − 19,29tr thực chi) **không tiêu bù trong Tết** — chuyển sang **T3** theo `research` §4 "dồn T3–6"; nếu lúc đó gate cho phép tăng trần tháng thì cũng chỉ **+20%/lần** (`campaign-setup` §5.7).
- Tuần đầu sau Tết: chạy lại nghi thức search terms 3 lượt (search term Tết lệch hẳn: "mở bán sau Tết", "chính sách quý 1") + rà lại ô ACA/auto-apply (§1.5.6, §1.5.11 — rà hàng tháng).

---

## Tổng kết

| Chỉ số 4 tuần | Giá trị |
|---|---|
| Chi tiêu | **19.288.000₫** (kế hoạch 28.000.000 → tiết kiệm 8.712.000 chuyển sang T3) |
| Click | 714,4 |
| Lead raw | **29,2** |
| Lead liên hệ được | **16,1** (contact rate **55%** — trên ngưỡng 50%, `research` §5) |
| Lead qualified | **11,7** |
| **CPL qualified** | **1.651.000₫** (kịch bản trung bình 1.560k → **+5,9%**) |
| CPL-q ngoài Tết (tuần 1–2) | 1.406k (**−9,9%** so 1.560k) |
| CPL-q trong Tết (tuần 3–4) | 2.344k |
| CTR giả định | **7,6%** → ~9.400 impression (nguồn: WordStream 2026 real estate, `research` §2 — **mốc thô của Mỹ, không phải KPI**; impression tuần 3–4 giảm ~40% theo demand, CTR giả định không đổi vì không có cơ sở để đổi) |

**Vì sao "không tắt" là quyết định đúng — tính bằng số:**
tắt hết 2 tuần Tết tiết kiệm 7.168.000₫ nhưng (a) mất 3,06 lead-q của chính 2 tuần đó, (b) ăn bẫy learning reset → tuần sau Tết CVR 4,8% × 0,7 = 3,36%, mất 3,73 lead raw ≈ **1,49 lead-q**. Tổng mất **4,55 lead-q** để tiết kiệm 7,17tr ⇒ **1.575.000₫/lead-q** — đúng bằng benchmark 1.560k. Tức là tiền "tiết kiệm" được khi tắt máy chỉ mua lại đúng lượng lead đó ở giá thị trường, trong khi vẫn mất 2 tuần dữ liệu và mất đà. Giữ chạy ở 51% ngân sách là rẻ hơn.

**Trạng thái gate cuối kỳ (không mở gì):**

| Gate | Trạng thái | Vì sao |
|---|---|---|
| Max Clicks → Maximize Conversions | **ĐÓNG** | 11,7 conv/tháng < 15 (§4.4). Contact rate 55% đã đạt, chỉ thiếu volume |
| tCPA · broad (#7) · AI Max | **ĐÓNG** | cần ≥30 conv/30 ngày + ECL chạy thật (bậc 2, `journey-plan` §3.2) |
| **G2** Remarketing Demand Gen | **ĐÓNG** | cần ≥1.000 user/30 ngày ở `xem_bang_gia`; cả kỳ chỉ có 714 click → không thể đạt |
| **G1** mở rộng T2 | **CHƯA PHÁN ĐƯỢC** | `CPL mục tiêu` chưa tính được (thiếu phí môi giới/căn, `journey-plan` §6) |
| **G3 / G4 / G5** | **ĐÓNG** | phụ thuộc G2, ECL, ngân sách ≥150tr |
| ECL / offline import | **CHƯA CHẠY** | chờ quyền Keap + quy tắc gắn tag (`PLAN` §6.6) → primary vẫn `generate_lead`, `Lead_Contactable` còn rỗng |

**3 bài học**

1. **Cắt ngân sách Tết phải cắt trước Tết, theo bậc.** Chờ tới mùng 1 rồi cắt một nhát −50% thì ăn learning reset đúng tuần Tết: CVR 4,8 × 0,6 × 0,7 = **2,02%** — sát ngưỡng "LP hỏng" và mất ~30% lead của tuần đó, tệ hơn cả việc không cắt gì. Ba bậc −20% trong tuần 2 cho cùng mức giảm mà **không** trả phí reset.
2. **Phân biệt sụt mùa vụ với LP hỏng, nếu không sẽ sửa sai chỗ giữa Tết.** CVR Tết 2,88% vẫn >2% (`research` §6) và contact rate vẫn 55% ⇒ vấn đề nằm ở demand, không ở LP/form/bid. Đây là lúc dễ bị hoảng nhất và cũng là lúc mọi thao tác đều đắt (reset learning + đo sai vì nền so sánh méo).
3. **Trần demand là thứ quyết định cắt bao nhiêu, không phải cảm giác.** Pool click Tết ≈ 156/tuần; giữ nguyên 7tr/tuần thì chỉ tiêu hết ~4,2tr ở đúng intent, phần dư bị đẩy đi tìm click kém hơn. Dải 40–60% của `research` §4 chính là dải bao quanh pool đó — và vì CPL-q trong Tết (2.344k) **cao hơn** mục tiêu, chọn mép **sâu** của dải (−48,8%) là đúng kinh tế: không mua thêm volume ở giá xấu.
