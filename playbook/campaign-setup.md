# Checklist dựng campaign — NGÀY 1

Tài liệu **thực thi**. Mở Google Ads UI, làm từ trên xuống, tick từng ô. Không giải thích lại chiến lược.

**Điều kiện tiên quyết:** đã qua **G0** (`playbook/customer-journey-plan.md` §3.1). Chưa qua G0 thì không bật quảng cáo — dừng ở §1.

## 0. Trỏ nguồn — đừng đọc lại ở đây

| Cần gì | Đọc ở |
|---|---|
| Vì sao cấu trúc như vậy, benchmark CPC/CVR/CPL | `research/google-ads-bds-vn.md` §1, §2 |
| Intent tier, negative bắt buộc, match type theo ngân sách | `research/google-ads-bds-vn.md` §3 |
| Lộ trình bidding, learning phase, mùa vụ | `research/google-ads-bds-vn.md` §4 |
| Lead quality, thang conversion, click tặc | `research/google-ads-bds-vn.md` §5 · `PLAN.md` §0.4 |
| Checklist vận hành ngày/tuần/tháng/quý | `research/google-ads-bds-vn.md` §8 |
| % ngân sách 3 kịch bản, gate G0–G5, kill rule | `playbook/customer-journey-plan.md` §3, §3.1 |
| KPI tree, breakeven CPL | `playbook/customer-journey-plan.md` §4 |
| Nhịp tuần/tháng, tiêu chí QA | `playbook/customer-journey-plan.md` §5 |
| Campaign ↔ ad group ↔ keyword, message match, nơi gắn negative | `keywords/adgroup-map.md` |

---

## 1. Pre-flight (D-7 → D-1) — làm xong hết mới sang §2

### 1.1 Advertiser verification — làm ĐẦU TIÊN (3–5 ngày chờ)

Lý do (đã đính chính 2026-07-28 theo doc Google — **không** phải "BĐS VN bị nhắm riêng", claim đó không có nguồn): Google nói **"all advertisers will eventually be required"**, và khi đã có yêu cầu thì **30 ngày không nộp = tài khoản bị TẠM NGƯNG** (`research` §7). Nộp trước khi dựng campaign là rẻ nhất; nộp sau khi bị treo là mất doanh thu trong lúc chờ duyệt.

| # | Việc | Đường dẫn UI | Xong |
|---|---|---|---|
| 1.1.1 | Nộp xác minh nhà quảng cáo | `Quản trị` (Admin) → `Xác minh` (Verification) → `Xác minh nhà quảng cáo` → chọn **Tổ chức** (Organization) | ☐ |
| 1.1.2 | Upload giấy ĐKKD + MST. **Tên pháp nhân phải khớp 100%** với tên trên hồ sơ thanh toán | cùng trang | ☐ |
| 1.1.3 | Xác minh danh tính người đại diện (CCCD) | cùng trang | ☐ |
| 1.1.4 | LP có footer: tên pháp nhân + MST + địa chỉ + hotline (thiếu = disapproved, `research` §7) | ngoài Ads | ☐ |
| 1.1.5 | Hồ sơ thanh toán: loại **Doanh nghiệp**, tiền tệ **VND**, múi giờ **(GMT+07:00) Việt Nam** — **cả hai KHÔNG đổi được về sau** | `Thanh toán` (Billing) → `Cài đặt` | ☐ |

### 1.2 Conversion actions — tạo TRƯỚC khi có campaign

Thang giá trị theo `PLAN.md` §0.4. Tạo cả 6, kể cả 3 cái chưa có dữ liệu.

| # | Tên action | Nguồn | Giá trị | Ngày 1 | Sau khi có ECL |
|---|---|---|---|---|---|
| 1 | `Lead_Form_Raw` | Nhập từ GA4 — event `generate_lead` | 1 | **Chính** (Primary) | → Phụ (Secondary) |
| 2 | `Click_Hotline` | Nhập từ GA4 — event `phone_click` | 1 | **Phụ** (QA 2026-07-28: khớp tracking/README luật #2 — Secondary vĩnh viễn, xem ở cột "All conversions") | Phụ |
| 3 | `Click_Zalo` | Nhập từ GA4 — event `zalo_click` | 1 | **Phụ** (như trên) | Phụ |
| 4 | `Lead_Contactable` | Nhập offline (Data Manager API) | 10 | Phụ (rỗng) | → **Chính — bid theo cái này** |
| 5 | `Lead_Qualified` | Nhập offline | 50 | Phụ (rỗng) | → **Chính** |
| 6 | `Dat_Coc` | Nhập offline | 500 | Phụ (rỗng) | → Chính khi ≥10 cọc/tháng |

> Ngày 1 để 1–3 làm Chính chỉ để **nhìn thấy số trong cột Conversions**. Max Clicks không đấu giá theo conversion nên không hại. Đảo vai trò khi chuyển sang smart bidding (§4.4).

| # | Việc | Đường dẫn UI | Xong |
|---|---|---|---|
| 1.2.1 | Tạo action 1–3 | `Mục tiêu` (Goals) → `Chuyển đổi` → `Tóm tắt` → `+ Hành động chuyển đổi mới` → **Nhập** (Import) → `Thuộc tính Google Analytics 4` → `Web` | ☐ |
| 1.2.2 | Tạo action 4–6 | cùng luồng → **Nhập** → `CRM, tệp hoặc nguồn dữ liệu khác` → `Theo dõi chuyển đổi từ lượt nhấp` | ☐ |
| 1.2.3 | Mỗi action: `Số lượng` (Count) = **Một** (One), không phải Every | trong từng action | ☐ |
| 1.2.4 | `Cửa sổ chuyển đổi lượt nhấp` = **90 ngày** (tối đa). Chu kỳ BĐS 3–12 tháng — để mặc định 30 ngày là mất conversion | trong từng action | ☐ |
| 1.2.5 | `Cửa sổ xem qua` = 30 ngày · `Mô hình phân bổ` = Dựa trên dữ liệu (mặc định) | trong từng action | ☐ |
| 1.2.6 | Đặt action 4 `Lead_Contactable` là **Mục tiêu chính của tài khoản** ngay từ đầu (không tick "chính" cho campaign, chỉ khai báo) để pipeline ECL không phải sửa schema sau | cùng trang | ☐ |
| 1.2.7 | **Chọn đúng `Danh mục` (goal category) chuẩn của Google cho từng action**, không chỉ đặt tên tự do — PMax/AI Max và mọi recommendation đọc theo **category**, không đọc tên: `Lead_Form_Raw` → `Gửi biểu mẫu khách hàng tiềm năng` (Submit lead form) · `Click_Hotline`/`Click_Zalo` → `Liên hệ` (Contact) · `Lead_Contactable` → `Liên hệ` hoặc `Khách hàng tiềm năng đủ điều kiện` (Qualified lead) · `Lead_Qualified` → **`Khách hàng tiềm năng đủ điều kiện`** (Qualified lead) · `Dat_Coc` → **`Khách hàng tiềm năng đã chuyển đổi`** (Converted lead) | trong từng action → `Danh mục mục tiêu` | ☐ |
| 1.2.8 | **Conversion Value Rules — chưa làm gì ngày 1, chỉ biết là có.** Khi đã ở bậc value-based bidding, dùng nó để chỉnh giá trị theo geo/device/audience **mà không sửa tag/pipeline** (lead đúng quận dự án > lead ngoại tỉnh; lead từ `xem_bang_gia_30d` > lead lạ). Rẻ hơn dựng thêm conversion action (`research` §5) | `Mục tiêu` → `Chuyển đổi` → `Quy tắc giá trị` | — |

### 1.3 Liên kết GA4 ↔ Google Ads

| # | Việc | Đường dẫn UI | Xong |
|---|---|---|---|
| 1.3.1 | **Bật gắn thẻ tự động** (auto-tagging) — không có nó thì không có `gclid` | Ads: `Quản trị` → `Cài đặt tài khoản` → `Gắn thẻ tự động` → ✅ | ☐ |
| 1.3.2 | Liên kết từ phía GA4 | GA4: `Quản trị` → `Liên kết sản phẩm` → `Liên kết Google Ads` → `Liên kết` → chọn tài khoản Ads | ☐ |
| 1.3.3 | Bật `Cá nhân hoá quảng cáo` + `Xuất đối tượng` trong hộp thoại liên kết (cần cho remarketing ở G2) | cùng hộp thoại | ☐ |
| 1.3.4 | Duyệt liên kết ở phía Ads | Ads: `Công cụ` → `Tài khoản được liên kết` → `Google Analytics (GA4)` → `Liên kết` | ☐ |
| 1.3.5 | Nhập 3 event GA4 (§1.2) — chỉ hiện sau khi event đã bắn ≥1 lần thật | Ads: `Mục tiêu` → `Chuyển đổi` → `+` → `Nhập` → GA4 | ☐ |
| 1.3.6 | Bắn **1 lead thật** từ LP → kiểm tra: GA4 Realtime thấy `generate_lead` · Ads thấy conversion trong 24h · CRM có `gclid` (điều kiện G0) | — | ☐ |

### 1.4 Import negative list từ `keywords/negative-keywords.csv`

**382 dòng** `cap_do=account` → **từ khoá phủ định cấp tài khoản** (tự áp mọi campaign, kể cả PMax sau này). **91 dòng** `cap_do=campaign` (12/08: sửa CRLF làm awk sót 8 dòng) → áp chọn lọc theo bảng trong `keywords/adgroup-map.md` §"Negative keyword — nơi gắn".

Xuất danh sách account-level, đóng ngoặc kép để thành **phrase match** (mặc định theo `adgroup-map.md`):

```bash
cd /home/docdang/Projects/google-ads
awk -F, 'NR>1 && $3=="account" {print "\"" $1 "\""}' keywords/negative-keywords.csv
# → 382 dòng, copy toàn bộ
```

Campaign-level (83 dòng, dán riêng cho từng campaign — **trừ #8 NhaOXaHoi**, xem bảng loại trừ trong `adgroup-map.md`):

```bash
awk -F, 'NR>1 && $3=="campaign" {print "\"" $1 "\""}' keywords/negative-keywords.csv
```

| # | Việc | Đường dẫn UI | Xong |
|---|---|---|---|
| 1.4.1 | Dán 382 dòng vào **Từ khoá phủ định cấp TÀI KHOẢN** (trần 1.000 — hiện dùng 382) | `Quản trị` → `Cài đặt tài khoản` → `Từ khoá phủ định` | ☐ |
| 1.4.2 | Kiểm chứng: trang đó hiển thị đủ 382 dòng, dạng `"phrase"` trong ngoặc kép | cùng trang | ☐ |
| 1.4.3 | 83 dòng campaign-level → tạo **1 shared list `NEG_BDS_Campaign_v1`** rồi gắn cho #1–#7 (bỏ qua #8) — đỡ dán 7 lần, sửa 1 chỗ áp cả 7. Làm sau khi dựng §2. Lưu ý F3: shared list (như mọi negative) chỉ phủ **Search+Shopping** — đủ cho 8 campaign Search hiện tại | `Công cụ` → `Thư viện dùng chung` → `Danh sách từ khoá phủ định` → `+` → gắn 7 campaign | ☐ |
| 1.4.4 | **RÀ CHÉO negative × launch set** (war-game 2026-07-28 bắt được negative `bao` chặn 599 kw launch): chạy script dưới, kết quả phải = rỗng hoặc chỉ conflict đã chấp nhận có ghi chú | script trong hộp dưới | ☐ |

```bash
# Rà chéo: negative account-level nào chặn keyword uu_tien=1?
python3 -c "
import csv
negs=[r for r in csv.DictReader(open('keywords/negative-keywords.csv')) if r['cap_do']=='account']
kws=[r['keyword'] for r in csv.DictReader(open('keywords/master-keywords.csv')) if r['uu_tien']=='1']
def b(n,k):
    nw,kw=n.split(),k.split()
    return any(kw[i:i+len(nw)]==nw for i in range(len(kw)-len(nw)+1))
for n in negs:
    hit=[k for k in kws if b(n['keyword'],k)]
    if hit: print(n['keyword'],'chặn',len(hit),'kw — vd:',hit[0])
"
# Conflict đã chấp nhận: 'miễn phí' chặn 1 kw long-tail (lọc rác > 1 kw)
```

> **QA chốt 2026-07-28 (đổi so với bản đầu):** dùng **account-level** làm nơi duy nhất cho 382 dòng account thay vì shared list. Lý do: account-level **tự áp cho mọi campaign type** — Search hôm nay, PMax ở G4 — không có bẫy "quên gắn cho campaign mới" (Google không kế thừa shared list tự động). Lý do cũ "shared list thắng vì áp được cho PMax" là **SAI** (chính account-level mới tự áp PMax — curriculum §A12). Shared list chỉ quay lại khi vượt trần 1.000 hoặc cần bật/tắt nhóm negative theo campaign.

### 1.5 Cài đặt tài khoản & mặc định campaign

Áp cho **mọi** campaign tạo ở §2. Sai một ô là đốt tiền ngày 1.

| # | Cài đặt | Giá trị bắt buộc | Đường dẫn UI |
|---|---|---|---|
| 1.5.1 | Mạng tìm kiếm đối tác | **TẮT** (bỏ tick `Bao gồm đối tác tìm kiếm của Google`) | Campaign → `Cài đặt` → `Mạng` |
| 1.5.2 | Mạng hiển thị / Display Expansion | **TẮT** (bỏ tick `Bao gồm Mạng hiển thị của Google`) | cùng chỗ |
| 1.5.3 | Vị trí | **Việt Nam** (thêm loại trừ tỉnh không bán nếu có) | Campaign → `Cài đặt` → `Vị trí` |
| 1.5.4 | Tuỳ chọn vị trí | **`Sự hiện diện: Những người ở hoặc thường xuyên ở khu vực nhắm mục tiêu`** — KHÔNG chọn "sự hiện diện hoặc mối quan tâm" | `Vị trí` → `Tuỳ chọn vị trí` |
| 1.5.5 | Ngôn ngữ | **Tiếng Việt + Tiếng Anh** (nhiều máy VN cài trình duyệt EN) | Campaign → `Cài đặt` → `Ngôn ngữ` |
| 1.5.6 | Tài sản do AI tạo tự động (ACA) | **TẮT** (`Tài sản tự động tạo`, `Văn bản quảng cáo động`) — không kiểm soát được copy → rủi ro policy. ⚠️ **Mốc cần theo dõi:** từ **9/2026** Google auto-upgrade ACA + campaign-level broad match setting thành **AI Max**; **2/2027 DSA sunset**. Rà lại ô này **mỗi tháng** — "đã tắt" hôm nay không đảm bảo còn tắt sau auto-upgrade. Nếu buộc phải sống với AI-generated text, cơ chế Google cấp để khoá text bắt buộc (pháp nhân/MST/miễn trừ) là **text disclaimers**, không phải pinning | Campaign → `Cài đặt` → `Cài đặt khác` → `Tài sản tự động` |
| 1.5.7 | Lịch quảng cáo | **05:00 – 24:00** hằng ngày (cắt rác đêm, giữ nguyên khung giờ có data) | Campaign → `Cài đặt` → `Lịch quảng cáo` |
| 1.5.8 | Phương thức phân phối | Chuẩn (Standard) | Campaign → `Cài đặt` → `Cài đặt khác` |
| 1.5.9 | URL theo dõi cấp tài khoản | **Tracking template UTM** (bắt buộc cho tích hợp Clarity↔Ads, xem `tracking/clarity-checklist.md` §1b): `{lpurl}?utm_source=google&utm_medium=cpc&utm_campaign={campaignid}&utm_term={keyword}&utm_content={creative}` | `Quản trị` → `Cài đặt tài khoản` → `Tuỳ chọn URL theo dõi` |
| 1.5.10 | Ngân sách dùng chung | **KHÔNG dùng** ngày 1 — cần đọc pacing riêng từng campaign | — |
| 1.5.11 | **Auto-apply recommendations** | **TẮT HẾT** — chỉ có cấp tài khoản, không loại trừ được campaign. Đặc biệt nguy hiểm với hệ: `Remove conflicting negative keywords` (phá negative list) và `Use Display expansion` (bật lại thứ 1.5.2 vừa tắt). Google tự bật một số mục theo mặc định — kiểm tra lại mỗi tháng | `Đề xuất` (Recommendations) → `Tự động áp dụng` → bỏ tick toàn bộ |

---

## 2. Dựng campaign — kịch bản 30tr ₫/tháng

### 2.1 Ngân sách ngày

> ⚠️ **THỨ TỰ BẮT BUỘC (war-game 2026-07-28, 3 round vấp cùng chỗ): chạy script lọc keyword §2.4 TRƯỚC, chốt bảng ngân sách SAU.** Với nhiều dự án, campaign #4 `TaiChinh` và #8 `NhaOXaHoi` **không có keyword nào ở `uu_tien=1`** (toàn bộ ở tier 2-3) → dựng theo bảng mẫu là tạo campaign rỗng với 100k/ngày nằm chết. Campaign nào 0 keyword launch → KHÔNG tạo, dồn % của nó vào #3 (ưu tiên) hoặc #1, ghi chú lại để mở khi bật tier 2.

Google tính trần tháng = **ngân sách ngày × 30,4**. Tổng 1.000.000 ₫/ngày → trần 30,4tr (+1,3%). Cần đúng 30tr thì nhân mọi con số dưới đây với **0,985**.

Phân bổ % lấy từ `customer-journey-plan.md` §3, chia nhỏ trong khối Search theo tỷ trọng `adgroup-map.md`.

| # | Campaign | % §3 | ₫/ngày **Ngày 1** | Ghi chú lệch so với §3 |
|---|---|---|---|---|
| 1 | `BDS_Search_Brand_DuAn` | 45% (cùng #2) | **475.000** | 375k theo tỷ trọng + **100k mượn từ quỹ Remarketing** |
| 2 | `BDS_Search_Brand_CDT` | ↑ | **75.000** | — |
| 3 | `BDS_Search_KhuVuc_GiaoDich` | 40% (cùng #4, #8) | **350.000** | 300k + **50k mượn từ quỹ Discovery** |
| 4 | `BDS_Search_TaiChinh` | ↑ | **70.000** | — |
| 8 | `BDS_Search_NhaOXaHoi` | ↑ | **30.000** | Chỉ bật nếu **thực sự** phân phối NOXH; không thì dồn vào #3 |
| 7 | `BDS_Search_Discovery` (broad) | 5% | **0 — hoãn** | `adgroup-map` #7 bắt buộc tCPA; ngày 1 chưa có conversion nên không đủ điều kiện. Truy vấn mới lấy từ search terms của phrase match là đủ. Bật khi đạt điều kiện broad của journey-plan §3.2 (bậc 2: Smart Bidding + ECL ổn — tức mốc tCPA, KHÔNG phải mốc Maximize Conversions; QA war-game 90d chốt theo gate nghiêm hơn) |
| — | `BDS_RMKT_Display` | 10% | **0 — hoãn** | Chưa qua gate **G2** (`journey-plan` §3.1) |
| 5, 6 | Search T3 | 0% | **0** | §3 đã tắt ở kịch bản 30tr |
| | **Tổng** | 100% | **1.000.000** | |

Khi G2 mở → rút 100k khỏi #1 lập `BDS_RMKT_Display`. Khi chuyển tCPA → rút 50k khỏi #3 lập #7. Không tăng tổng.

### 2.2 Bidding khởi điểm

Tất cả campaign: **`Số lượt nhấp tối đa` (Maximize Clicks) + Giá thầu CPC tối đa** (`research` §4 — tuần 1–3 không dùng smart bidding).

Dải CPC lập kế hoạch từ `research` §2: 15k (tốt) / 25k (trung bình) / 40k (thận trọng). Cap khởi điểm neo vào mức đó, hạ thấp hơn cho brand vì Quality Score cao → CPC thực rẻ hơn.

| Campaign | Bid cap khởi điểm | Lý do |
|---|---|---|
| #1 Brand_DuAn | **20.000 ₫** | Intent cao nhất, QS cao nhất, CPC thực rẻ nhất (`research` §3) |
| #2 Brand_CDT | **25.000 ₫** | Mức "trung bình" của dải |
| #3 KhuVuc_GiaoDich | **35.000 ₫** | Head term khu vực đắt nhất, chưa tới mức thận trọng 40k |
| #4 TaiChinh | **30.000 ₫** | — |
| #8 NhaOXaHoi | **20.000 ₫** | Phân khúc thấp, không trả giá cao |

**Đường dẫn UI:** Campaign → `Cài đặt` → `Đặt giá thầu` → `Chọn chiến lược giá thầu trực tiếp` → `Số lượt nhấp tối đa` → tick `Đặt giới hạn giá thầu CPC tối đa` → nhập số.

**Quy tắc chỉnh cap tuần 1–3:** chỉ chỉnh khi `Tỷ lệ hiển thị bị mất (xếp hạng)` > 40% **và** campaign chưa tiêu hết ngân sách → tăng cap **+20%/lần, cách nhau ≥3 ngày** (`research` §4). Nếu tiêu hết ngân sách mà cap chưa chạm → **không** tăng cap, đó là vấn đề ngân sách.

### 2.3 Ad group — bao nhiêu là đủ ngày 1

Ngưỡng `adgroup-map.md`: mỗi ad group cần **≥10 conversion/tháng**. Tính ngược:

- #1: 475k/ngày ÷ cap 20k ≈ 24 click/ngày ≈ 720 click/tháng. CVR 4% (mô hình "trung bình", `research` §2) ≈ 29 lead/tháng → **tối đa 3 ad group** = tối đa **3 dự án** bật ngày 1.
- #3: 350k/ngày ÷ cap 35k = 10 click/ngày ≈ 300 click/tháng ≈ 12 lead/tháng → **tối đa 2 ad group**. Chọn `<khu-vực>--gia-bang-gia` và `<khu-vực>--mua-ban` của đúng khu vực dự án đang bán. Không đủ 10 conv thì gộp theo cụm địa lý trong `adgroup-map.md`.
- #2, #4, #8: **1 ad group mỗi campaign**.

Muốn chạy >3 dự án ở mức 30tr thì gộp, không tách — hoặc lên 60tr (§5).

### 2.4 Import keyword từ `master-keywords.csv`

> ⚠️ Lệnh `awk -F,` trong `adgroup-map.md` §"Lọc bộ launch" **cho sai kết quả** (2.850 thay vì 4.538): một số ô `ghi_chu` có dấu phẩy và được bọc ngoặc kép, awk cắt nhầm cột. Dùng script dưới đây.

Lưu tạm thành `/tmp/mk.py`:

```python
import csv, sys, re
UU  = set(sys.argv[1].split(','))   # "1" cho 30tr | "1,2" cho 60tr | "1,2,3" cho 150tr
ADG = re.compile(sys.argv[2])       # regex lọc nhom_adgroup của dự án/khu vực đang phân phối
def camp(g):
    if g.startswith('brand-cdt--'): return 'BDS_Search_Brand_CDT'
    if g.startswith('brand-'):      return 'BDS_Search_Brand_DuAn'
    if 'nha-o-xa-hoi'   in g:       return 'BDS_Search_NhaOXaHoi'
    if 'discovery-broad' in g:      return 'BDS_Search_Discovery'
    if re.search(r'tai-chinh|phan-khuc-ngan-sach|cau-hinh-can', g): return 'BDS_Search_TaiChinh'
    if re.search(r'phap-ly|tien-do', g):                            return 'BDS_Search_PhapLy_TienDo'
    if re.search(r'tu-van-quyet-dinh|dau-tu', g):                   return 'BDS_Search_NghienCuu'
    return 'BDS_Search_KhuVuc_GiaoDich'
w = csv.writer(sys.stdout, delimiter='\t')
w.writerow(['Campaign', 'Ad group', 'Keyword', 'Match type'])
n = 0
for r in csv.DictReader(open('keywords/master-keywords.csv')):
    if r['uu_tien'] in UU and ADG.search(r['nhom_adgroup']):
        w.writerow([camp(r['nhom_adgroup']), r['nhom_adgroup'],
                    r['keyword'], r['match_type'].capitalize()]); n += 1
print(f'-- {n} keyword', file=sys.stderr)
```

Chạy — thay slug bằng **dự án đang thực sự phân phối** (`PLAN.md` §6.2) và khu vực của chúng:

```bash
cd /home/docdang/Projects/google-ads
python3 /tmp/mk.py 1 '^(brand-the-global-city|brand-lumiere-midtown|brand-cdt--masterise-homes|quan-2--|thu-duc--)' > /tmp/launch-kw.tsv
# kiểm tra trước khi dán
cut -f1 /tmp/launch-kw.tsv | sort | uniq -c
cut -f2 /tmp/launch-kw.tsv | sort | uniq -c   # số ad group — phải ≤ ngưỡng §2.3
```

Tìm slug có thật:

```bash
python3 -c "
import csv
s={r['nhom_adgroup'] for r in csv.DictReader(open('keywords/master-keywords.csv'))
   if r['nhom_adgroup'].startswith('brand-')}
print('\n'.join(sorted(x for x in s if 'global' in x or 'masterise' in x)))"
```

| # | Việc | Cách làm | Xong |
|---|---|---|---|
| 2.4.1 | Chạy script, kiểm số ad group ≤ ngưỡng §2.3 | bash ở trên | ☐ |
| 2.4.2 | **Cách A (khuyến nghị)** — Google Ads Editor: `Tài khoản` → `Nhận thay đổi gần đây` → chọn `Từ khoá` → `Thực hiện nhiều thay đổi` → dán nội dung `/tmp/launch-kw.tsv` (có dòng tiêu đề) → `Xử lý` → `Đăng` | Editor | ☐ |
| 2.4.3 | **Cách B** — UI: `Công cụ` → `Tác vụ hàng loạt` → `Tải lên` → kéo file `.tsv` → `Xem trước` → `Áp dụng` | UI | ☐ |
| 2.4.4 | Kiểm tra: tất cả keyword ở trạng thái `Đủ điều kiện`. Có `Ít lượt tìm kiếm` (Low search volume) → để nguyên, Google tự bật lại khi có volume | Campaign → `Từ khoá` | ☐ |
| 2.4.5 | Không tạo dòng riêng cho biến thể không dấu — Google tự khớp. ⚠️ **Câu này CHỈ đúng cho POSITIVE keyword.** Negative keyword **không khớp close variant** → biến thể không dấu trong negative list là **bắt buộc** (`research` §3 hộp cảnh báo, `adgroup-map.md` §Match type) | — | ☐ |
| 2.4.6 | **Kiểm chứng: 0 keyword nào ở match type `Rộng` (Broad).** Broad là **default** của Google Ads — bất kỳ dòng import thiếu/sai cột `Match type` sẽ thành broad **im lặng**, không báo lỗi. Lọc cột `Loại đối sánh` = Rộng, phải trả về rỗng (trừ campaign #7 khi đã bật) | Campaign → `Từ khoá` → thêm cột `Loại đối sánh` → lọc | ☐ |
| 2.4.7 | Đặt Final URL của **mỗi ad group** về đúng LP dự án/khu vực. **Không ad group nào trỏ homepage** (QA Q2) | Ad group → `Cài đặt` | ☐ |

### 2.5 Thứ tự thao tác dựng campaign (lặp cho mỗi campaign)

1. `+ Chiến dịch mới` → `Tạo chiến dịch không có mục tiêu hướng dẫn` → loại **Tìm kiếm** → mục tiêu `Khách hàng tiềm năng` → bỏ tick mọi cách chuyển đổi (Lượt truy cập trang web) — LP xử lý chuyển đổi qua GA4.
2. Đặt tên đúng bảng §2.1 (giữ nguyên chuỗi, không thêm ngày tháng — vẫn dò được bằng script).
3. Ngân sách ngày (§2.1) → Bidding Max Clicks + cap (§2.2).
4. Áp toàn bộ §1.5 (**11 ô** — 1.5.11 tắt auto-apply là ô cấp tài khoản, làm 1 lần rồi rà lại hàng tháng).
5. Tạo ad group theo §2.3, đặt Final URL.
6. Import keyword (§2.4).
7. Dán RSA (§3) — **2 RSA/ad group** ngày 1, chừa 1 slot cho biến thể test tuần 3 (trần Google là 3 RSA/ad group).
8. Gắn extensions (§3.4) ở **cấp tài khoản** cho callout/call/location, **cấp campaign** cho sitelink.
9. Kiểm account-level negatives đã hoạt động (tự áp, §1.4.1) + dán negative campaign-level (§1.4.3).
10. Campaign để **Tạm dừng**. Bật đồng loạt tất cả vào 06:00 ngày launch — dữ liệu ngày đầu mới so sánh được.

---

## 3. RSA mẫu tiếng Việt (3 bộ)

**Placeholder** — thay bằng số/tên **thật** trước khi dán:

| Placeholder | Ví dụ dùng để đếm ký tự | Độ dài ví dụ |
|---|---|---|
| `{Tên dự án}` | `Eco Retreat` | 11 |
| `{Quận}` | `Quận 7` | 6 |
| `{Giá từ}` | `3,2 tỷ` | 6 |
| `{Vay%}` | `70%` | 3 |

Cột **Trần** = số ký tự tối đa của `{Tên dự án}` / `{Quận}` trong headline đó. Vượt trần → dùng tên rút gọn khách hay gõ (`The Global City` → `Global City`) hoặc bỏ headline đó.

**Tuân thủ policy** (`research` §7) — đã kiểm: không có từ cam kết sinh lời/lợi nhuận, không ALL-CAPS, không tên đối thủ, không "#1/tốt nhất/duy nhất", không countdown giả. Mọi con số (`{Vay%}`, `{Giá từ}`, chiết khấu) phải là chính sách thật của CĐT đợt hiện tại — số giả làm hỏng QA Q7 (`journey-plan` §5).

> 🚨 **RÀNG BUỘC CỨNG — mạo nhận CĐT = đình chỉ tài khoản NGAY, không cảnh báo** (*unacceptable business practices*, `research` §7). Headline `{Tên dự án} - Giá Gốc CĐT` (§3.1 #4) và mọi biến thể "Giá Gốc CĐT" **chỉ được dùng khi LP có dòng nói rõ mình là đơn vị PHÂN PHỐI, không phải chủ đầu tư** (footer pháp nhân + 1 dòng ở đầu trang). Không có dòng đó trên LP → **bỏ headline #4** khỏi bộ. Đây là ô kiểm bắt buộc, không phải khuyến nghị.
> Kèm theo: mọi `Giá Từ` / `Trả Trước Từ` phải là **căn thật đang bán, có bảng giá đợt hiện tại làm bằng chứng** (misrepresentation — nhánh minh bạch chi phí).

**Rubric review 3 bộ RSA — khung ABCD của Google** (dùng thay vì chỉ đếm ký tự):

| | Nghĩa | Trạng thái 3 bộ hiện tại |
|---|---|---|
| **A** — Attract | Thu hút ngay headline đầu | ✔ headline #1 = tên dự án + "Bảng Giá Mới Nhất" |
| **B** — Brand | Gắn brand tự nhiên | ✔ tên dự án ở nhiều headline |
| **C** — Connect | Kết nối cảm xúc / kể chuyện | ⚠️ **yếu nhất** — 3 bộ toàn thông tin & chính sách. BĐS để ở là quyết định cảm xúc → đã bổ sung 1 headline nhóm C vào bộ 1 (#9) và bộ 2 (#4) |
| **D** — Direct | Nói rõ muốn họ làm gì | ✔ "Gọi Ngay Nhận Bảng Giá", "Đặt Lịch Xem Nhà Mẫu" |

Khi viết bộ RSA cho dự án mới: chấm ABCD trước khi chạy script đếm ký tự §3.5. Thiếu **C** là lỗi hay gặp nhất và cũng làm giảm asset diversity (đầu vào của Ad Strength).

> 🔧 **ĐỔI LUẬT GHIM (2026-08-06, kiểm chứng thật trên campaign Beachtro):** bản cũ của file này dạy "ghim H1 = headline #1 để khoá message match" — làm đúng như vậy thì Google chấm Ad Strength **POOR** ngay (ghim là hình phạt nặng nhất trong cách chấm). Bỏ ghim + đa dạng hoá headline → **GOOD**. Luật mới:
> 1. **Mặc định KHÔNG ghim.** Message match giữ bằng cách khác: *mọi* headline trong bộ đều phải hợp lệ để đứng vị trí 1 — không viết câu chỉ hợp làm câu phụ.
> 2. Tên dự án xuất hiện ~3/15 headline là đủ nhận brand; 7/15 câu mở đầu bằng tên dự án = Google chấm "thiếu đa dạng".
> 3. Chỉ ghim khi buộc phải có câu không đứng đầu được (disclaimer, số hiệu giấy phép) — và chấp nhận Ad Strength tụt.
> 4. Ad Strength **GOOD là đích, đừng đuổi Excellent** — muốn lên nữa phải nhồi keyword vào description làm câu gượng, trong khi Ad Strength không vào Ad Rank/QS (`research §7b`).
> 5. Đọc điểm + gợi ý qua API: `ad_group_ad.ad_strength` + `ad_group_ad.action_items`.

> 📚 **BỔ SUNG TỪ 3 CUỐN SÁCH ĐÃ CHƯNG CẤT (2026-08-06 — chi tiết `research/books/`):**
> - **Bước 0 trước khi viết bất kỳ bộ RSA nào** (Schwartz): khai 2 số ở đầu bộ — `Mức nhận thức khách = 1–5` (họ biết gì về SẢN PHẨM MÌNH — lưu ý: cùng truy vấn có thể mức 1 với brand mẹ nhưng mức 3 với brand con) và `Mức sophistication thị trường = 1–5`. Thị trường căn hộ VN 2026 ≈ mức 3½–4 → claim trần (`giá tốt`, `ưu đãi`) vô hiệu, chỉ **cơ chế** ("sổ hồng lâu dài") và **gỡ giới hạn** ("X mà không phải chịu Y") còn ăn. Một bộ RSA = một mức nhận thức, không trộn.
> - **Rubric ABCD → ABCD-M**: thêm hàng **M — Mechanism**: mỗi bộ ≥1 headline nói *bằng cách nào*, không chỉ *được gì*.
> - **Chữ C (Connect) — định nghĩa ĐO ĐƯỢC thay cảm tính** (Cashvertising): headline nhóm C = câu **không chứa dữ kiện sản phẩm**, mô tả *trạng thái khách sau khi mua* hoặc *con người khách muốn thành*, và phải chỉ đích danh **LF8 số mấy** (mạnh nhất cho BĐS ở/nghỉ dưỡng: #7 người thân, #3 thoát sợ hãi pháp lý). Định mức **≥3/15 nhóm C** và **≥2/15 có đại từ ngôi hai** (`bạn`/`cả nhà`). `Sống Cạnh Biển Mỗi Ngày` KHÔNG phải C — nó vẫn mô tả sản phẩm; bản C thật: `Sáng Mở Mắt Đã Thấy Biển`.
> - Cụ thể thắng chung chung: con số có nguồn (`1.785 căn`, `bàn giao 8/2028`) vừa là chi tiết vừa tăng độ tin — kỹ thuật hợp policy nhất. Khi ad không ra lead: **đổi offer trước khi kết luận thị trường không có nhu cầu**.

### 3.1 Bộ 1 — Brand dự án (ad group `brand-<slug>`, modifier *bảng giá*)

Message match `adgroup-map.md`: headline chứa **tên dự án + "Bảng Giá Mới Nhất"** → LP scroll tới block **bảng giá + form tải bảng giá**.
Final URL: `https://<lp>/<slug-du-an>/` · Path1: `bang-gia` · Path2: `2026` · Pinning: **KHÔNG ghim** (đổi luật 2026-08-06, xem hộp dưới §3).

| # | Headline | Ký tự | Trần |
|---|---|---|---|
| 1 | `{Tên dự án} Bảng Giá Mới Nhất` | 29 | 12 |
| 2 | `Bảng Giá {Tên dự án} 2026` | 25 | 16 |
| 3 | `{Tên dự án} Giá Từ {Giá từ}` | 25 | 16 |
| 4 | `{Tên dự án} - Giá Gốc CĐT` | 25 | 16 |
| 5 | `Nhận Bảng Giá Qua Zalo` | 22 | — |
| 6 | `{Tên dự án} Mặt Bằng Căn Hộ` | 27 | 14 |
| 7 | `Chính Sách Bán Hàng Đợt Mới` | 27 | — |
| 8 | `{Tên dự án} Chiết Khấu Mới` | 26 | 15 |
| 9 | `Chọn Căn Cho Gia Đình 4 Người` | 29 | — |
| 10 | `{Tên dự án} Pháp Lý Rõ Ràng` | 27 | 14 |
| 11 | `Tư Vấn Chọn Căn Miễn Phí` | 24 | — |
| 12 | `Đặt Lịch Xem Nhà Mẫu` | 20 | — |
| 13 | `{Tên dự án} Tiến Độ Mới Nhất` | 28 | 13 |
| 14 | `Trả Góp - Hỗ Trợ Vay Vốn` | 24 | — |
| 15 | `Gọi Ngay Nhận Bảng Giá` | 22 | — |

| # | Description | Ký tự |
|---|---|---|
| 1 | `Bảng giá gốc chủ đầu tư {Tên dự án}, cập nhật mới nhất. Nhận qua Zalo trong 2 phút.` | 87 |
| 2 | `Mặt bằng từng loại căn, tiến độ ảnh thật, pháp lý rõ ràng. Tư vấn chọn căn miễn phí.` | 84 |
| 3 | `Chính sách đợt này: chiết khấu thanh toán sớm, hỗ trợ vay. Gọi để nhận chi tiết.` | 80 |
| 4 | `Đặt lịch xem nhà mẫu {Tên dự án}. Xem quỹ căn còn lại thật trước khi quyết định.` | 84 |

### 3.2 Bộ 2 — Giao dịch khu vực (ad group `<khu-vực>--gia-bang-gia`)

Message match: **loại hình + khu vực + "Giá Từ … ₫"** → LP block **bảng giá**.
Final URL: `https://<lp>/can-ho-<slug-khu-vuc>/` · Path1: `can-ho` · Path2: `bang-gia` · Pinning: **KHÔNG ghim**.

| # | Headline | Ký tự | Trần `{Quận}` |
|---|---|---|---|
| 1 | `Căn Hộ {Quận} Giá Từ {Giá từ}` | 27 | 9 |
| 2 | `Bảng Giá Căn Hộ {Quận}` | 22 | 14 |
| 3 | `Căn Hộ {Quận} Mở Bán Đợt Mới` | 28 | 8 |
| 4 | `Nhà Mới Cho Gia Đình Trẻ` | 24 | — |
| 5 | `Căn Hộ {Quận} 2PN Giá Tốt` | 25 | 11 |
| 6 | `Giá Gốc CĐT - Không Chênh` | 25 | — |
| 7 | `Nhận Bảng Giá + Mặt Bằng` | 24 | — |
| 8 | `Căn Hộ {Quận} Sổ Hồng` | 21 | 15 |
| 9 | `So Sánh 3 Loại Căn Nhanh` | 24 | — |
| 10 | `Xem Quỹ Căn Còn Lại` | 19 | — |
| 11 | `Căn Hộ {Quận} Trả Góp` | 21 | 15 |
| 12 | `Tư Vấn Miễn Phí Qua Zalo` | 24 | — |
| 13 | `Chọn Căn Theo Ngân Sách` | 23 | — |
| 14 | `Đặt Lịch Xem Nhà Mẫu` | 20 | — |
| 15 | `Gọi Ngay - Có Giá Đợt Này` | 25 | — |

Khu vực dài (`Bình Dương` 10, `Thủ Đức` 7, `Long Biên` 9) → kiểm lại headline #1, #3, #5 bằng script §3.5. Đổi `Căn Hộ` sang `Nhà Phố`/`Đất Nền`/`Biệt Thự` theo `loai_hinh` của ad group.

| # | Description | Ký tự |
|---|---|---|
| 1 | `Căn hộ {Quận} giá từ {Giá từ}. Bảng giá gốc CĐT, không chênh. Nhận bảng giá qua Zalo.` | 83 |
| 2 | `So sánh 3 loại căn theo ngân sách, xem mặt bằng và quỹ căn còn lại. Tư vấn miễn phí.` | 84 |
| 3 | `Dự án mở bán đợt mới tại {Quận}: pháp lý sổ hồng, ngân hàng bảo lãnh. Gọi xem chi tiết.` | 87 |
| 4 | `Đặt lịch xem nhà mẫu cuối tuần. Nhận bảng giá và tiến độ thanh toán qua Zalo.` | 77 |

### 3.3 Bộ 3 — Tài chính / trả góp (ad group `tai-chinh`, `<khu-vực>--tai-chinh`)

Message match: **"Trả Góp – Hỗ Trợ Vay …%"** → LP block **chính sách vay**.
Final URL: `https://<lp>/<slug>/tra-gop/` · Path1: `tra-gop` · Path2: `ho-tro-vay` · Pinning: **KHÔNG ghim**.

| # | Headline | Ký tự | Trần |
|---|---|---|---|
| 1 | `Trả Góp - Hỗ Trợ Vay {Vay%}` | 24 | 9 |
| 2 | `Mua Căn Hộ Trả Góp {Quận}` | 25 | 11 |
| 3 | `Vay {Vay%} - Ân Hạn Gốc Lãi` | 24 | 9 |
| 4 | `Trả Trước Từ {Giá từ}` | 19 | 17 |
| 5 | `Tính Khoản Vay Trong 1 Phút` | 27 | — |
| 6 | `Xem Lãi Suất Ưu Đãi Đợt Này` | 27 | — |
| 7 | `{Tên dự án} Trả Góp Dài Hạn` | 27 | 14 |
| 8 | `Ngân Hàng Bảo Lãnh Dự Án` | 24 | — |
| 9 | `Nhận Bảng Tính Vay Chi Tiết` | 27 | — |
| 10 | `Trả Mỗi Tháng Bao Nhiêu?` | 24 | — |
| 11 | `Tiến Độ Thanh Toán Linh Hoạt` | 28 | — |
| 12 | `Tư Vấn Vay Miễn Phí Qua Zalo` | 28 | — |
| 13 | `Vốn Ban Đầu Từ {Giá từ}` | 21 | 15 |
| 14 | `Xem Chính Sách Thanh Toán` | 25 | — |
| 15 | `Gọi Ngay Để Tính Khoản Vay` | 26 | — |

| # | Description | Ký tự |
|---|---|---|
| 1 | `Mua căn hộ trả góp, hỗ trợ vay tới {Vay%} giá trị căn. Nhận bảng tính khoản vay chi tiết.` | 86 |
| 2 | `Vốn ban đầu từ {Giá từ}, ân hạn gốc lãi theo chính sách CĐT. Tư vấn vay miễn phí qua Zalo.` | 88 |
| 3 | `Xem tiến độ thanh toán từng đợt và lãi suất ưu đãi hiện hành. Gọi để tính thử khoản vay.` | 88 |
| 4 | `Ngân hàng bảo lãnh dự án, pháp lý rõ ràng. Đặt lịch tư vấn tài chính trong hôm nay.` | 83 |

> Headline #8 "Ngân Hàng Bảo Lãnh Dự Án" và description #4 chỉ dùng khi dự án **thật sự** có bảo lãnh ngân hàng — có văn bản. Không có thì thay bằng `Pháp Lý Sổ Hồng Đầy Đủ` (22).

### 3.3b Bộ 4 — Pre-launch, CĐT CHƯA công bố giá (template dùng chung, thêm 2026-08-06)

Mọi dự án đều đi qua giai đoạn này; Beachtro là ca đầu (bản chạy thật: `projects/beachtro-tower/ad-copy.md`). Luật:

1. **Cấm mọi câu có giá/ưu đãi/chiết khấu** — `{Giá từ}`, `Giá Gốc CĐT`, `{Vay%}` đều là bịa khi chưa công bố = misrepresentation. Bộ 1–3 ở trên KHÔNG dùng được nguyên trạng.
2. Offer hợp lệ duy nhất = **bán thông tin**: "Nhận Bảng Giá Khi Công Bố", bộ mặt bằng, lịch bàn giao. Đây là đúng loại headline cho mức nhận thức 2–3, không phải giải pháp tạm (Schwartz cách #25).
3. **Deadly Sincerity**: 1 description nói thẳng "Chủ đầu tư chưa công bố giá..." — tự nêu khuyết điểm làm phần còn lại được tin gấp bội, và tuyệt đối an toàn policy vì không có số nào.
4. Khi không nói được giá, vũ khí mạnh nhất = **gỡ giới hạn** ("Sở Hữu Lâu Dài, Không Thời Hạn" — X mà không phải chịu Y) + **con số có nguồn** (quy mô, mốc bàn giao).
5. **Headline có hạn sử dụng**: ngày CĐT công bố giá, thị trường nhảy sang mức nhận thức 1 → toàn bộ headline "khi công bố" chết trong 24h. Mốc biết trước — bộ thay phải viết sẵn, và ngày đó = bắt đầu kỳ đo mới (cấm so CPL trước/sau).
6. **Description = lead** (Great Leads): một bộ RSA = một kiểu lead, khai kiểu lead ở đầu bộ (Offer/Promise/Problem-Solution/Secret/Proclamation/Story — ánh xạ theo mức nhận thức trong `research/books/great-leads.md §3`). Proclamation không viết được thì đừng bịa — nó phải *tìm* được từ research.

### 3.4 Extensions (tài sản)

**Sitelink (6)** — cấp campaign. `Campaign → Tài sản → + → Liên kết trang web`. Tiêu đề ≤25, mỗi dòng mô tả ≤35.

| Tiêu đề | Ký tự | Mô tả 1 | Mô tả 2 | URL |
|---|---|---|---|---|
| `Bảng Giá Mới Nhất` | 17 | `Giá gốc CĐT từng loại căn` (25) | `Cập nhật đợt mở bán hiện tại` (28) | `/<slug>/#bang-gia` |
| `Mặt Bằng & Loại Căn` | 19 | `Layout 1PN, 2PN, 3PN chi tiết` (29) | `Chọn căn theo hướng và tầng` (27) | `/<slug>/#mat-bang` |
| `Tiến Độ & Pháp Lý` | 17 | `Ảnh thi công có ngày chụp` (25) | `Sổ hồng, ngân hàng bảo lãnh` (27) | `/<slug>/#phap-ly` |
| `Chính Sách Trả Góp` | 18 | `Hỗ trợ vay, ân hạn gốc lãi` (26) | `Bảng tính khoản vay theo căn` (28) | `/<slug>/#tra-gop` |
| `Vị Trí & Kết Nối` | 16 | `Bản đồ hạ tầng quanh dự án` (26) | `Thời gian tới trung tâm thật` (28) | `/<slug>/#vi-tri` |
| `Tiện Ích Nội Khu` | 16 | `Hồ bơi, trường, TTTM nội khu` (28) | `Ảnh thật khu tiện ích` (21) | `/<slug>/#tien-ich` |

Sitelink phải trỏ **anchor trên chính LP**, không sang trang khác — giữ scent và không mất `gclid`.

> **Vì sao 6 chứ không 4:** Google yêu cầu **≥6 sitelink** (tính gộp cả 3 cấp ad group + campaign + account) để RSA đạt Ad Strength `Good`+ ([Ad Strength for RSA](https://support.google.com/google-ads/answer/9921843?hl=en)). 2 sitelink thêm vào vẫn là anchor trên chính LP → đạt 6 **mà không phá luật "chỉ anchor trên LP"**.
> **Dynamic sitelinks: KHÔNG bật** — cùng lý do đã tắt ACA (§1.5.6): không kiểm soát được text → rủi ro policy với BĐS. Đây là **đánh đổi có ý thức**: Ad Strength sẽ thấp hơn mức Google khuyên. Chấp nhận được vì Ad Strength **không vào Ad Rank/Quality Score** (`research` §7b).

**Callout (4+)** — cấp tài khoản. `Quản trị → Tài sản → + → Chú thích`. Mỗi cái ≤25.

| Callout | Ký tự |
|---|---|
| `Bảng giá gốc CĐT` | 16 |
| `Tư vấn Zalo miễn phí` | 20 |
| `Xem nhà mẫu cuối tuần` | 21 |
| `Pháp lý sổ hồng đầy đủ` | 22 |
| `Hỗ trợ vay ngân hàng` (dự phòng) | 20 |

**Call (1)** — cấp tài khoản. `Quản trị → Tài sản → + → Cuộc gọi`.

| Trường | Giá trị |
|---|---|
| Quốc gia | Việt Nam |
| Số | Hotline sàn (đầu số VN, người trực máy thật) |
| Số chuyển tiếp của Google | **TẮT** — chưa hỗ trợ VN → không có conversion "Cuộc gọi từ quảng cáo". Đếm qua `phone_click` trên LP (`CLAUDE.md` registry) |
| Lịch | Đúng **giờ trực máy**, hẹp hơn lịch campaign (§1.5.7). Quảng cáo hiện ngoài giờ trực = lead mất |

**Location (1)** — cấp tài khoản. `Quản trị → Tài sản → + → Vị trí` → liên kết **Hồ sơ doanh nghiệp** (Google Business Profile) đã xác minh của văn phòng/nhà mẫu.
Chưa có GBP đã xác minh → **bỏ qua**, không tạo hồ sơ ảo (rủi ro đình chỉ). Tạo GBP thật rồi quay lại gắn.

*Price, Promotion asset: bỏ qua ngày 1 — thêm khi có chính sách bán hàng cố định ≥1 tháng.*

**Structured snippet — dùng được ngày 1**, nhưng header phải thuộc danh sách Google định sẵn. Header **hợp lệ cho tiếng Việt** (probe API 2026-08-06): `Tiện nghi`, `Thương hiệu`, `Điểm đến`, `Chương trình`, `Khóa học`, `Khách sạn nổi bật`. `Loại hình` / `Kiểu dáng` / `Khu dân cư` / `Danh mục dịch vụ` bị từ chối — đừng thử lại.

### 3.5 Kiểm ký tự sau khi điền placeholder (bắt buộc trước khi dán)

```python
# /tmp/chk.py  — dán headline/description đã điền thật vào 2 list, chạy: python3 /tmp/chk.py
import unicodedata as u
H = ["Eco Retreat Bảng Giá Mới Nhất", "..."]     # 15 headline đã điền
D = ["Bảng giá gốc chủ đầu tư Eco Retreat, ...", "..."]  # 4 description đã điền
bad = 0
for lst, lim, tag in ((H, 30, 'H'), (D, 90, 'D')):
    for i, s in enumerate(lst, 1):
        n = len(u.normalize('NFC', s))
        if n > lim: bad += 1; print(f'{tag}{i} VUOT {n}/{lim}: {s}')
assert len(H) == 15 and len(D) == 4, 'phai du 15 headline + 4 description'
assert not any(s.isupper() for s in H + D), 'co ALL-CAPS'
# 2 dòng kiểm định mức C (Cashvertising C.4/C.5): >=2/15 co dai tu ngoi hai; >=3/15 khong chua du kien san pham
nyou = sum(1 for s in H if any(w in s.lower() for w in ('bạn','cả nhà','gia đình')))
nc   = sum(1 for s in H if not any(ch.isdigit() for ch in s))
print(f'headline co "ban/ca nha": {nyou}/15 (can >=2) | khong chua chu so (proxy nhom C): {nc}/15')
print('OK' if not bad else f'{bad} loi')
```

---

## 4. Tuần 1–4 sau launch

Checklist nền ngày/tuần: `research/google-ads-bds-vn.md` §8. Nhịp PM/QA: `journey-plan` §5. Dưới đây **chỉ là phần riêng của giai đoạn launch**.

### 4.1 Việc riêng theo mốc

| Mốc | Việc riêng của launch | Xong |
|---|---|---|
| **D+0, 10:00** | Mọi ad ở trạng thái `Đã phê duyệt`. Có `Bị từ chối` → xử theo `research` §7, sửa và gửi duyệt lại trong ngày | ☐ |
| **D+0, 18:00** | Click đầu tiên đã về? Không có click sau 12h → kiểm `Chẩn đoán quảng cáo` (Ad Diagnosis) ở dòng keyword | ☐ |
| **D+1** | Lead thật đầu tiên (hoặc lead test) có `gclid` trong CRM. Trống = tracking hỏng → **tạm dừng toàn bộ**, sửa xong mới bật lại | ☐ |
| **D+3** | Search terms lần 1 (dù ít data): chỉ thêm negative cho term **rõ ràng sai ngành**. Chưa cắt keyword | ☐ |
| **Tuần 1** | **KHÔNG đổi**: bid cap, ngân sách, RSA, keyword. Chỉ thêm negative + sửa LP. Đổi = reset learning (`research` §4) | ☐ |
| **Tuần 2** | Vòng negative đầy đủ theo nghi thức 3 lượt (`journey-plan` §5 tuần). Cập nhật `keywords/` theo `keywords/UPDATE.md` | ☐ |
| **Tuần 2** | Đọc **10 lead gần nhất**, tính contact rate lần đầu (`research` §5 — mục tiêu >50%) | ☐ |
| **Tuần 3** | Báo cáo theo **giờ** và **thiết bị** → siết `Lịch quảng cáo` nếu có khung giờ rác rõ rệt. Kiểm cột `Lượt nhấp không hợp lệ` (<10% là bình thường, `research` §5) | ☐ |
| **Tuần 3** | Thêm **RSA thứ 2** vào ad group nào chỉ có 1 (tối đa 3/ad group) — đổi **một** biến: góc offer hoặc CTA | ☐ |
| **Tuần 4** | Đo CVR LP thật. <2% = LP hỏng (`research` §6) → sửa LP **trước**, đừng đụng bid | ☐ |
| **Tuần 4** | Quyết định bidding (§4.4). Rà `journey-plan` §3.1: gate nào mở được? | ☐ |
| **Tuần 4** | Điền tháng 1 vào scorecard `journey-plan` §4. Không có số CRM = không kết luận được gì | ☐ |

### 4.2 Ngưỡng dừng / kill rule

Không chép lại ngưỡng ở đây — nguồn duy nhất là **`journey-plan` §3.1 "Gate ngược"**. Nhắc nơi tra và khi nào tra:

| Đối tượng | Tra ở | Khi nào |
|---|---|---|
| Keyword / RSA mới | `journey-plan` §3.1 (pause khi chi 2–3× CPL mục tiêu, 0 conversion) | Rà mỗi thứ 4 hàng tuần |
| Ad chạy >7–14 ngày | `journey-plan` §3.1 (CPL 1,5–2× trên mục tiêu) | Từ tuần 3 |
| Cả campaign | `journey-plan` §3.1 + không pause producer khi chưa có bản thay thế | Rà tháng |
| Chất lượng lead | `research` §5 — contact rate <40% = vấn đề nghiêm trọng, sửa form/LP trước khi sửa Ads | Từ tuần 2, hàng tuần |

`CPL mục tiêu` phải tính từ breakeven `journey-plan` §4 **trước** khi dùng kill rule. Chưa có phí môi giới/căn và tỷ lệ booking→HĐMB thì mọi kill rule là đoán — đây là số user phải điền (`journey-plan` §6).

### 4.3 Ngưỡng "dừng khẩn" (kiểm hàng ngày, ngoài kill rule)

| Triệu chứng | Hành động ngay |
|---|---|
| Conversion = 0 trong 24h mà hôm trước có | Kiểm GA4 → tracking hỏng, **không** đổi bid |
| Spend ngày > 2× ngân sách ngày | Bình thường (Google cho vượt tới 2×/ngày, cân bằng trong tháng). Chỉ lo nếu trần tháng vượt |
| LP down / chậm >3s mobile | Tạm dừng campaign đến khi sửa xong — đốt tiền vào trang không load |
| Lead trong CRM không có `gclid` | Tạm dừng, sửa attribution (skill `ad-click-attribution`) |

### 4.4 Khi nào chuyển bidding

Lộ trình gốc: `research` §4 · bảng ngưỡng volume: `journey-plan` §3. Điều kiện thực thi:

| Từ → Đến | Điều kiện (ĐỦ CẢ) | Đường dẫn UI |
|---|---|---|
| Max Clicks → **Maximize Conversions** | Tiêu chí CHUẨN DUY NHẤT: `projects/beachtro-tower/plan-chay-ads.md §1` (contact rate đã đóng băng cùng ECL — không dùng làm điều kiện) | Campaign → `Cài đặt` → `Đặt giá thầu` → `Chuyển đổi` → `Số chuyển đổi tối đa`, **không** đặt tCPA |
| Maximize Conversions → **tCPA** | ≥30 conversion/30 ngày ổn định · đã chạy Max Conversions ≥2 tuần · **đã có ECL/offline import chạy thật** | cùng chỗ → tick `Đặt CPA mục tiêu` = CPA thực 30 ngày **+10–20%** |
| tCPA → **tROAS** | Giá trị lead phân tầng thật đang chảy về (action 4/5/6 §1.2) · ≥15 conversion/30 ngày | cùng chỗ → `Giá trị chuyển đổi` |

**Cùng lúc chuyển sang Maximize Conversions, làm 3 việc:**
1. Đảo primary/secondary conversion theo cột phải bảng §1.2 — nếu không, smart bidding học theo form thô và sẽ mua lead rác (`journey-plan` §2.3).
2. Bật `BDS_Search_Discovery` (#7) với **tCPA**, ngân sách 50k/ngày rút từ #3 (§2.1) — CHỈ sau khi tCPA đã ổn ≥2 tuần (journey-plan §3.2 bậc 2; không bật kèm bước Maximize Conversions). Account-level negatives (§1.4.1) tự phủ — không cần gắn gì thêm.
3. Không đổi ngân sách trong 2 tuần sau khi đổi chiến lược — learning phase 1–2 tuần (`research` §4).

**Sau khi đổi:** chờ **4 tuần** mới phán xét. tCPA chỉnh ±15%/lần, ngân sách ±20%/lần cách ≥3–4 ngày.

---

## 5. Scale lên 60tr / 150tr — chỉ ghi delta

Không dựng lại từ đầu. Giữ nguyên §1 (pre-flight) và toàn bộ campaign đang chạy.

### 5.1 Ngân sách ngày (₫), tính từ % `journey-plan` §3

| Campaign | 30tr (1tr/ngày) | 60tr (2tr/ngày) | 150tr (5tr/ngày) |
|---|---|---|---|
| #1 `Brand_DuAn` | 475.000¹ | 583.000 | 1.042.000 |
| #2 `Brand_CDT` | 75.000 | 117.000 | 208.000 |
| #3 `KhuVuc_GiaoDich` | 350.000¹ | 570.000 | 1.200.000 |
| #4 `TaiChinh` | 70.000 | 133.000 | 280.000 |
| #8 `NhaOXaHoi` | 30.000 | 57.000 | 120.000 |
| #7 `Discovery` (broad) | 0 (hoãn) | 100.000 | 250.000 |
| `RMKT_Display` / Demand Gen | 0 (hoãn) | 300.000 | 750.000 |
| #5 `PhapLy_TienDo` | 0 | 60.000 | 214.000 |
| #6 `NghienCuu` | 0 | 80.000 | 286.000 |
| `PMax_FeedLess` | 0 | 0 | 400.000 |
| YouTube | 0 | 0 | 250.000 |
| **Tổng** | **1.000.000** | **2.000.000** | **5.000.000** |

¹ đã gồm phần mượn tạm từ quỹ Remarketing/Discovery (§2.1) — trả lại khi mở G2 / bật #7.

### 5.2 Delta khi lên 60tr

| Delta | Chi tiết | Gate mở khoá |
|---|---|---|
| Bộ keyword | Chạy lại script §2.4 với `1,2` (7.825 kw trước khi lọc dự án) | **G1** — `journey-plan` §3.1 |
| Campaign mới | `BDS_Search_PhapLy_TienDo` (#5), `BDS_Search_NghienCuu` (#6) — Max Clicks + cap 25k | **G3** |
| Campaign mới | `BDS_RMKT_Display` — audience `xem_bang_gia` / `engaged_60s`, loại trừ `da_generate_lead_14d` | **G2** |
| Campaign mới | `BDS_Search_Discovery` (#7) broad + tCPA | §4.4 (đã có tCPA) |
| Match type | Test **1 ad group broad** trong #3, trần 15% ngân sách campaign (`research` §3) | ≥30 conv/30 ngày |
| Ad group | #1 lên tối đa **6 dự án** (583k ÷ cap 20k ≈ 29 click/ngày, giữ ngưỡng ≥10 conv/ad group) | — |
| Cấu trúc | Tách brand khỏi generic bằng **portfolio bidding** nếu ≥4 campaign cùng CPA mục tiêu (`research` §4). **Không** gộp brand với generic | — |
| Bidding | #1, #2, #3 chuyển tCPA (§4.4) | ≥30 conv/30 ngày |

### 5.3 Delta khi lên 150tr

| Delta | Chi tiết | Gate mở khoá |
|---|---|---|
| Bộ keyword | Script §2.4 với `1,2,3` (8.512 kw trước khi lọc) | **G3** đã chạy ổn |
| Campaign mới | `BDS_PMax_FeedLess` — dựng theo **checklist 12 bước §5.5** (bắt buộc, không tự ứng biến) | **G4** — offline import đã chạy thật |
| Campaign mới | YouTube — video dự án tự sản xuất, **không** để Google tự sinh. Đo bằng **brand search lift**, không đo bằng CPL | **G5** |
| Match type | Barbell đầy đủ: Exact/Phrase lõi + Broad có tCPA (`research` §3) | ≥60tr + offline import ổn |
| Bidding | tROAS cho campaign có giá trị lead phân tầng (§4.4) | — |
| AI Max for Search | Bật **sau khi** Search ổn định; tắt final URL expansion nếu site có trang không phải LP (`research` §1). **3 điều kiện cứng — xem §5.6** | sau G4 ≥6 tuần |
| Chống click tặc | Cân nhắc ClickCease/Spider AF (~$50–100/tháng) — chỉ ở mức chi tiêu này (`research` §5) | >50tr/tháng |

### 5.4 Ngân sách PMax 8% ở 150tr — ✅ QA CHỐT phương án (b) (war-game round 5, 2026-07-28): HOÃN PMax, chuyển 8% (400k/ngày) sang Demand Gen remarketing cho tới khi checklist G4 đầy đủ VÀ Excluded content keywords đã điền. Không bật = không thể quên brand exclusions.

`PMax_FeedLess` = 400.000₫/ngày (~$15/ngày) chạy trên **6 kênh** là rất mỏng. Google **không** publish ngưỡng ngân sách PMax (đây là suy luận, không phải citation) nhưng so sánh gần nhất là Demand Gen $100+/ngày, và PMax phủ nhiều kênh hơn Demand Gen. Hai lựa chọn để QA chốt **trước khi** dựng:

- **(a)** Giữ 8% nhưng dồn toàn bộ vào **1 asset group / 1 dự án duy nhất** để có mật độ (không rải nhiều dự án).
- **(b)** **Hoãn PMax thêm một bậc**, chuyển 8% đó sang Demand Gen remarketing — nơi đã có audience thật từ GA4.

Chưa chốt thì **không bật PMax**, kể cả khi đã qua G4. Ghi quyết định + ngày vào `playbook/customer-journey-plan.md` §3.1.

### 5.5 Checklist dựng PMax — 12 bước (dùng khi qua G4)

Nguồn: [About PMax](https://support.google.com/google-ads/answer/10724817?hl=en) · [PMax lead gen best practices](https://support.google.com/google-ads/answer/13775965?hl=en) · [How PMax interacts with other campaigns](https://support.google.com/google-ads/answer/13810170?hl=en).

| # | Bước | Xong |
|---|---|---|
| 1 | Conversion goal = **`Qualified lead`** / `Converted lead` (goal **category** chuẩn Google, §1.2.7), **không** phải form raw. Goal phải có ≥15 conv/30 ngày | ☐ |
| 2 | Bidding: `Maximize conversion value` (+tROAS khi đã có giá trị phân tầng); chỉ cần volume thì `Maximize conversions` | ☐ |
| 3 | **1 asset group = 1 dự án.** Asset tối thiểu: **≥20 text (15 headline + 5 description)**, **≥7 image (3 landscape + 3 square + 1 portrait)**, **≥1 video**. → Ảnh flycam/nhà mẫu phải chuẩn bị đúng **3 tỷ lệ TRƯỚC** khi bật, không phải sau | ☐ |
| 4 | **TẮT `URL expansion`.** Bật = Google có thể thay Final URL bằng LP khác + tự sinh headline/description → LP dự án A bị thay bằng LP dự án B, mất message match và mất chính sách giá đúng | ☐ |
| 5 | Brand exclusions: tên các CĐT/dự án **không** phân phối (chống ăn brand người khác) + brand của chính mình nếu muốn brand về Search | ☐ |
| 6 | Negative: **account-level negatives (§1.4.1) TỰ PHỦ PMax** — kiểm chứng hiển thị trong campaign, không cần gắn tay. ⚠️ **Chỉ phủ Search + Shopping inventory** — xem hộp dưới bảng | ☐ |
| 7 | Account-level placement exclusion: loại **`App categories` / `Games`** | ☐ |
| 8 | Audience signal: `xem_bang_gia_30d`, `da_generate_lead_14d` (để **loại trừ**), Customer Match khách đã mua. ⚠️ **Audience signal chỉ là GỢI Ý** — "function as performance hints rather than strict targeting controls… don't restrict ad delivery". Muốn giới hạn thật thì phải dùng exclusion — và **exclusion là bước riêng SAU khi campaign đã tồn tại** (xem hộp dưới bảng) | ☐ |
| 9 | Search themes: chỉ theme sát dự án. Biết rằng nó ở tầng **phrase/broad**, **không đè exact** | ☐ |
| 10 | ✅ **Lá chắn chống cannibalize brand:** giữ **tên dự án ở Exact** trong Search campaign. Google: "If a search query matches to an **exact match keyword** in your Search campaign, Google Ads **prioritizes the Search campaign** over Performance Max." Điều kiện: keyword phải **exact và identical**, không phải phrase → giải toả lo ngại ở `research` §1 | ☐ |
| 11 | Learning **1-2 tuần** (tới 6 tuần nếu volume thấp) — **không đụng gì** trong thời gian đó | ☐ |
| 12 | Tuần đầu: đọc **search terms report + placement report**, cắt ngay app/game/parked domain | ☐ |

> ⚠️ **Negative keyword trong PMax chỉ chặn được MỘT NỬA campaign** (vòng 3, 2026-07-28 — [Negative keywords in PMax](https://support.google.com/google-ads/answer/15726455?hl=en), [Account-level negative keywords](https://support.google.com/google-ads/answer/11396330?hl=en)):
> - Nguyên văn: "Performance Max negative keywords are applicable to **Search and Shopping inventory only**." Account-level cũng vậy: "Negative keywords automatically apply to all **Search and Shopping** inventory, **including in your Performance Max campaigns**" (áp cho Search, PMax, App, Shopping, Smart, Local).
> - → **Phần Display + YouTube của PMax KHÔNG bị negative account-level của hệ chặn.** Công cụ đúng cho phần đó là **`Excluded content keywords`** (feature riêng, cấp tài khoản): "apply to all campaigns running on **YouTube or Display Networks**". Đây là ô **thứ hai** phải điền ở G4, ngoài §1.4.1. Chưa điền = ad BĐS có thể chạy trên video/site rác mà negative list không cứu.
> - Trần dung lượng ([Account limits](https://support.google.com/google-ads/answer/6372658?hl=en)): **10.000 negative/campaign** · **5.000 keyword/negative list** · manager account tối đa **20 list**, mỗi child account **20 list** · **1.000 negative/account** ở ô account-level (382 dòng của hệ vẫn thoải mái) · Display/Video campaign: tối đa **1.000 negative**.
> - Tương tác **brand exclusions ↔ negative keywords: CHƯA XÁC NHẬN** — vòng 3 không truy cập được trang riêng về brand exclusions (4 URL thử đều 404) và trang "How PMax interacts with other campaigns" không nhắc. Vẫn giữ bước 5, nhưng **đừng giả định** brand exclusion và negative bù cho nhau; rà tay như §5.6 mục 3.
>
> ⚠️ **Audience exclusion KHÔNG cài được lúc tạo campaign** ([About Exclusions](https://support.google.com/google-ads/answer/2549058?hl=en)): "Audience exclusions **aren't available during campaign creation**, but you can add exclusions to an existing campaign." Exclusion hỗ trợ ở "Search, Display, Demand Gen, Standard Shopping, Video, and **Performance Max**". Đường đi: `Audiences` → mục `Exclusions` → drop-down **`Exclude from`** = `Campaign` hoặc `Ad group` → tick segment → **`Save Audience Segment Exclusions`**. → Với mọi campaign (kể cả Search hôm nay), exclusion là **bước 13 sau khi bấm Publish**, không phải ô trong luồng tạo.

> ⛔ **`New customer acquisition goal`: KHÔNG bật ở G4** (vòng 3, 2026-07-28 — [Customer lifecycle goals](https://support.google.com/google-ads/answer/12080169?hl=en)). Ba lý do, theo thứ tự nặng dần:
> 1. **New Customer Value Mode** cần value-based bidding (tROAS / Max conversion value) **và** "At least one **Purchase** conversion goal is required". Hệ đo `Qualified lead`, **không có** Purchase goal → mode này không đủ điều kiện.
> 2. **New Customer Only Mode** chạy với "**all bid strategies**" và Purchase goal "isn't required, but recommended" → *về kỹ thuật* bật được. Nhưng nó "optimized to bid **exclusively** for new customers", và Google chỉ biết ai là khách cũ qua **Customer Match list** ("Existing customer lists that you share through Customer Match and label in the Conversions Summary Acquisition panel") — tức phải có pipeline upload CRM trước, thứ hệ chưa có ở G4.
> 3. ⚠️ **Lý do BĐS, quan trọng nhất:** giả định "khách mua 1 lần nên chỉ cần khách mới" là **sai với thị trường này**. Nhà đầu tư mua căn thứ 2-3 và khách đã cọc dự án A quay lại dự án B là nhóm **CVR cao nhất, chi phí thuyết phục thấp nhất**. `New Customer Only` sẽ **bid loại chính nhóm đó**. → Muốn tránh trả tiền cho khách đã chốt thì dùng **audience exclusion** (hộp trên) — chính xác hơn, có thể bật/tắt từng campaign, và **không đụng vào bidding**.
> *(Lookback "540 ngày" từng ghi ở `research/google-official-curriculum.md` §E5 là **suy luận, không có nguồn** — vòng 3 đọc lại cả trang NCA và trang store-goals đều không nêu cửa sổ nào.)*

### 5.6 AI Max — 3 điều kiện cứng trước khi bật

1. **Bắt buộc conversion-based bidding.** Google: "The Search Term Matching feature in AI Max **will not work with manual CPC bidding**." → ở bậc Max Clicks/Manual CPC thì **bật cũng vô nghĩa**, phải qua tCPA/tROAS trước (§4.4).
2. **Pinning H1 bị BỎ QUA** nếu bật cả `text customization` + `final URL expansion`, hoặc khi có URL inclusions. ~~Message match của hệ khoá bằng pinning H1~~ (luật ghim đã bỏ 2026-08-06 — message match giờ khoá bằng "mọi headline đều on-message", xem hộp §3) → **vẫn giữ quyết định TẮT final URL expansion** vì lý do "không lạc trang".
3. **Rà chéo negative account-level ↔ brand inclusions TRƯỚC khi bật** — Google cảnh báo negative trùng brand inclusion làm giảm hiệu suất. Negative keyword vẫn được tôn trọng khi bật AI Max ("Negative keywords will be respected even with AI Max turned on"), nhưng trùng lặp với brand inclusion thì tự chặn mình.

Báo cáo sau khi bật: search terms report **vẫn đầy đủ** + có match type mới `AI Max` và cột `source` (broad expansion vs keywordless) — xem `research` §1.

### 5.7 Quy tắc chung khi scale

- Tăng ngân sách **≤20%/lần, cách ≥3–5 ngày** (`journey-plan` §3). Nhảy thẳng 30tr → 60tr trong 1 lần = reset learning toàn tài khoản.
- Mở **một** gate mỗi lần, chờ đủ chu kỳ đo trước khi mở gate tiếp theo.
- Mùa vụ ghi đè mọi kế hoạch scale: giảm 40–60% Tết và tháng 7 âm, **không tắt hẳn**; dồn T3–6 và T10–12 (`research` §4).
- Mỗi lần tạo campaign mới: quay lại **§1.4.3** áp negative list và **§1.5** áp 11 ô cài đặt. Google không kế thừa tự động.
