# Chiến lược từ khóa theo hành trình khách hàng

Cầu nối giữa **bộ keyword tĩnh** (`master-keywords.csv` + `adgroup-map.md`) và **hành trình động** (`playbook/customer-journey-plan.md`).

- `adgroup-map.md` trả lời: *keyword này ở campaign/ad group nào* (trục `intent_tier`).
- File này trả lời: *keyword này thuộc giai đoạn hành trình nào, bid bao nhiêu, dẫn về đâu, nuôi bằng gì*.
- Hai trục độc lập — xem `customer-journey-plan.md` §0. Một keyword `T1_brand_du_an` (campaign #1) vẫn có thể là khách giai đoạn 2.

**Nguồn số:** script aggregate ở §6 chạy trên `master-keywords.csv`. Mọi con số trong file này reproduce được; con số không có nguồn thì ghi `[điền]`.

> ⚠️ **Lệch số đã phát hiện (không sửa ở đây):** master hiện **8.534 dòng / 240 dự án**; `adgroup-map.md` và `UPDATE.md` ghi 8.512 / 239 (chênh 22 dòng = 1 dự án hạng A mới thêm). `uu_tien`: thực tế **4.546 / 3.299 / 689** vs tài liệu ghi 4.538 / 3.287 / 687. Sửa ở vòng update tới theo `UPDATE.md`, không sửa trong file này.

---

## 1. Ma trận modifier → giai đoạn hành trình

**48 modifier riêng biệt** tách được từ 8.534 dòng, phân loại hết, 0 dòng chưa xếp giai đoạn.

### 1.0 Phân bố tổng

| Giai đoạn | Số modifier | Số kw | % bộ | `uu_tien` 1 / 2 / 3 | exact / phrase / broad |
|---|---|---|---|---|---|
| 1. Nhận biết | 3 | **28** | 0,3% | 1 / 13 / 14 | 0 / 16 / 12 |
| 2. Tìm hiểu | 10 | **1.397** | 16,4% | 258 / 785 / 354 | 63 / 1.334 / 0 |
| 3. So sánh | 21 | **3.537** | 41,4% | 1.288 / 1.928 / 321 | 366 / 3.171 / 0 |
| 4. Quyết định | 14 | **3.572** | 41,9% | 2.999 / 573 / 0 | 972 / 2.600 / 0 |
| 5. Sau lead | — | **0** | 0% | — | — |

GĐ5 **không có keyword** — đúng thiết kế (`customer-journey-plan.md` §1: 100% remarketing/CRM). Đừng đi tìm keyword cho nó.

**Trục tier ≠ trục giai đoạn — bằng chứng số:**

| Giai đoạn | `T1_brand_du_an` | `T1_brand_cdt` | `T2_giao_dich` | `T3_nghien_cuu` |
|---|---|---|---|---|
| 1 | 0 | 0 | 14 | 14 |
| 2 | **956** | 88 | 235 | 118 |
| 3 | **1.794** | 0 | 1.422 | 321 |
| 4 | 1.798 | 220 | 1.554 | 0 |

→ **2.750 keyword brand dự án (60% của 4.548) là khách GĐ2–GĐ3, không phải GĐ4.** Chúng nằm trong campaign #1 (40% ngân sách) nhưng không được đối xử như intent chốt: RSA và LP phải trả lời câu hỏi của giai đoạn, không nhồi "Đặt Cọc Ngay".

Phân bố campaign theo giai đoạn (dùng để đọc lại bảng ngân sách `customer-journey-plan.md` §3):

| Giai đoạn | #1 Brand_DuAn | #2 Brand_CDT | #3 KhuVuc | #4 TaiChinh | #5 PhapLy_TienDo | #6 NghienCuu | #7 Discovery | #8 NOXH |
|---|---|---|---|---|---|---|---|---|
| 1 | — | — | — | — | — | 16 | 12 | — |
| 2 | 956 | 132 | 233 | — | 73 | — | — | 3 |
| 3 | 1.794 | — | 916 | 512 | 63 | 252 | — | — |
| 4 | 1.798 | 220 | 1.490 | 64 | — | — | — | — |

### 1.1 Bảng modifier (đầy đủ 48)

Cột **xử lý**: `Search` = bid trên Search campaign · `Content+RMKT` = không ép form, đẩy về `content/` + nuôi audience · `Negative/tắt` = loại hoặc tắt ở kịch bản ngân sách nhỏ.

#### GĐ4 — Quyết định (3.572 kw)

| Modifier | Số kw | Match hiện có | Tier chứa | Xử lý |
|---|---|---|---|---|
| `bảng giá` | 731 | 303 exact / 428 phrase | T2 447, T1dự án 240, T1cđt 44 | **Search — bid cao nhất.** Lead magnet #1 |
| `(tên trần)` | 687 | 303 exact / 384 phrase | T2 447, T1dự án 240 | **Search — exact luôn**, CPC rẻ nhất |
| `mua` | 599 | 63 exact / 536 phrase | T2 359, T1dự án 240 | **Search** |
| `mở bán` | 454 | 303 exact / 151 phrase | T2 170, T1dự án 240, T1cđt 44 | **Search** — CPL thường tốt nhất |
| `chính sách bán hàng` | 284 | phrase | T1dự án 240, T1cđt 44 | **Search** |
| `tiến độ thanh toán` | 240 | phrase | T1dự án 240 | **Search** |
| `nhà mẫu` | 240 | phrase | T1dự án 240 | **Search** — lead chất lượng cao nhất (intent đi xem) |
| `chiết khấu` | 118 | phrase | T1dự án 118 | **Search** — chỉ khi có % chiết khấu thật (Q7) |
| `sắp mở bán` | 63 | phrase | T2 63 | **Search** — giữ chỗ sớm |
| `bàn giao ngay` | 63 | phrase | T2 63 | **Search** — tệp ở ngay, chốt nhanh |
| `căn hộ` (sau tên CĐT) | 44 | phrase | T1cđt 44 | **Search** #2 |
| `chung cư` (sau tên CĐT) | 44 | phrase | T1cđt 44 | **Search** #2 |
| `GENERIC/mo-ban-moi` | 4 | phrase | T2 4 | **Search** — "đặt cọc giữ chỗ dự án", "giá gốc chủ đầu tư" |
| `GENERIC/san-sang-o` | 1 | phrase | T2 1 | **Search** — "xem nhà mẫu căn hộ" |

#### GĐ3 — So sánh / Cân nhắc (3.537 kw)

| Modifier | Số kw | Match hiện có | Tier chứa | Xử lý |
|---|---|---|---|---|
| `giá` | 687 | 303 exact / 384 phrase | T2 447, T1dự án 240 | **Search** — LP anchor bắt buộc là bảng giá |
| `giá bao nhiêu` | 599 | 63 exact / 536 phrase | T2 359, T1dự án 240 | **Search** |
| `trả góp` | 303 | phrase | T2 63, T1dự án 240 | **Search** #4 |
| `có nên mua` | 303 | phrase | T3 63, T1dự án 240 | **Chia đôi**: 240 bản brand → Search (LP có block so sánh + FAQ); 63 bản khu vực (T3) → Content+RMKT |
| `mặt bằng` | 240 | phrase | T1dự án 240 | **Search** — feeder chính của audience `xem_mat_bang_30d` |
| `tiện ích` | 240 | phrase | T1dự án 240 | **Search** bid thấp |
| `review` | 181 | phrase | T3 63, T1dự án 118 | **Chia đôi** như `có nên mua`. **Không** negative mù cụm này (`adgroup-map.md` §Negative); phải có negative `lừa đảo/phốt/tố cáo` kèm |
| `đánh giá` | 181 | phrase | T3 63, T1dự án 118 | như `review` |
| `lãi suất` | 118 | phrase | T1dự án 118 | **Search** #4 — LP block chính sách vay |
| `bán` | 107 | phrase | T2 107 | **Theo dõi 2 tuần rồi quyết**: nửa truy vấn là *người muốn bán*. Chưa xác nhận bằng search term → siết exact hoặc negative `cần bán/muốn bán/bán gấp` |
| `trả góp ngân hàng` | 63 | phrase | T2 63 | **Search** #4 |
| `cao cấp` | 63 | phrase | T2 63 | **Search** — chỉ bật nếu rổ hàng thật có phân khúc này |
| `2 phòng ngủ` | 63 | phrase | T2 63 | **Search** — long-tail CVR tốt (`research/…bds-vn.md` §3) |
| `3 phòng ngủ` | 63 | phrase | T2 63 | **Search** |
| `dưới 2 tỷ` | 63 | phrase | T2 63 | **Search** — chỉ bật nếu có sản phẩm ở mức giá đó, không thì là lead rác |
| `dưới 3 tỷ` | 63 | phrase | T2 63 | **Search** — như trên |
| `dưới 5 tỷ` | 63 | phrase | T2 63 | **Search** — như trên |
| `tiến độ` (khu vực) | 63 | phrase | T3 63 | **Content+RMKT** — phần lớn là khách đã mua |
| `ở đâu tốt` | 63 | phrase | T3 63 | **Content+RMKT** (#6, chỉ từ G3) |
| `GENERIC/tai-chinh` | 8 | phrase | T2 3, T3 5 | **Chia**: 3 dòng T2 → Search #4; 5 dòng T3 → Content. ⚠️ xem xung đột negative §1.2 |
| `GENERIC/gia-bang-gia` | 3 | phrase | T2 2, T3 1 | **Search** — "nhận bảng giá dự án mới nhất" là lead magnet |

#### GĐ2 — Tìm hiểu / Nghiên cứu (1.397 kw)

| Modifier | Số kw | Match hiện có | Tier chứa | Xử lý |
|---|---|---|---|---|
| `pháp lý` | 303 | phrase | T3 63, T1dự án 240 | **Chia**: 240 brand → Search (yếu tố tin tưởng, LP block pháp lý); 63 khu vực → #5, Max Clicks, chỉ từ G3 |
| `chủ đầu tư` | 240 | phrase | T1dự án 240 | **Search** bid thấp — LP block hồ sơ CĐT |
| `vị trí` | 240 | phrase | T1dự án 240 | **Search** bid thấp |
| `dự án` | 214 | 63 exact / 151 phrase | T2 170, T1cđt 44 | **Search** — truy vấn duyệt danh mục, `uu_tien` 1 toàn bộ |
| `tiến độ xây dựng` | 118 | phrase | T1dự án 118 | **Tắt ở kịch bản 30tr** — khách đã mua, không tạo lead mới (`UPDATE.md` §hàng tháng) |
| `bàn giao khi nào` | 118 | phrase | T1dự án 118 | **Tắt ở 30tr** như trên |
| `dự án mới` | 107 | phrase | T2 63, T1cđt 44 | **Search** |
| `có uy tín không` | 44 | phrase | T3 44 | **Content+RMKT** — truy vấn trust, bắt buộc negative `lừa đảo/phốt/tranh chấp` |
| `GENERIC/phap-ly` | 10 | phrase | T2 1, T3 9 | **Content** — trừ "người nước ngoài mua nhà tại việt nam" (T2, tệp giá trị cao → Search). ⚠️ §1.2 |
| `GENERIC/nha-o-xa-hoi` | 3 | phrase | T2 1, T3 2 | **Search chỉ ở #8** — negative `nhà ở xã hội` vẫn chặn ở #1–#7 |

#### GĐ1 — Nhận biết (28 kw)

| Modifier | Số kw | Match | Tier | Xử lý |
|---|---|---|---|---|
| `(broad seed)` | 12 | broad | T2 12 | **Xuyên giai đoạn**, không thực sự là GĐ1: 12 seed ở #7 để *dò truy vấn mới*. tCPA bắt buộc + full negative list + đọc search terms hàng tuần không sót |
| `GENERIC/tu-van-quyet-dinh` | 8 | phrase | T3 7, T2 1 | **Content+RMKT** (chỉ từ G3). Ngoại lệ: "tư vấn mua căn hộ miễn phí" (T2, `uu_tien` 1) → Search |
| `GENERIC/dau-tu` | 8 | phrase | T3 7, T2 1 | **Content+RMKT**. Ngoại lệ: "tư vấn đầu tư bất động sản" (T2) → Search |

### 1.2 Xung đột negative đã phát hiện (cùng loại với `cho thuê`)

`là gì` là negative **account-level** (`negative-keywords.csv` dòng 79). Master có **2 keyword chứa "là gì"** — "ân hạn nợ gốc là gì", "sổ hồng riêng là gì" — chúng sẽ **eligible nhưng không bao giờ served**. Đây là 2 truy vấn GĐ2–3 đúng nghĩa, giá trị nằm ở `content/` chứ không ở Search → **để nguyên negative, chuyển 2 dòng này thành đề tài bài SEO**, không hạ negative xuống campaign-level. (Đối lập với case `cho thuê` trong `adgroup-map.md` §Cảnh báo, ở đó có phương án hạ cấp.)

---

## 2. Chiến lược theo giai đoạn

Mỗi giai đoạn: nhóm kw bật · bid priority · RSA angle · LP anchor (**trỏ về `adgroup-map.md` §Message match, không lặp lại bảng đó**) · audience đổ vào / loại ra (5 audience trong `tracking/ga4-setup.md` §3) · dòng chảy sang giai đoạn sau.

### GĐ1 — Nhận biết · 28 kw

| | |
|---|---|
| **Bật** | 12 broad seed (#7) + 2 dòng "tư vấn …" T2. 14 dòng T3 còn lại: chỉ `content/`, không Search |
| **Bid** | Ưu tiên **thấp nhất**. #7 tCPA bắt buộc, trần ngân sách 5% (`customer-journey-plan.md` §3) |
| **RSA angle** | Framing theo ngân sách, không theo dự án: "Với [X] tỷ mua được gì ở [khu vực]" |
| **LP anchor** | Bài SEO `content/` + CTA mềm "nhận bảng giá khu vực" — **không** LP bán hàng. Ad group `tu-van-quyet-dinh` trong `adgroup-map.md` §Message match |
| **Audience đổ vào** | Không có audience riêng — traffic này nuôi `engaged_60s_30d` |
| **Loại ra** | `da_generate_lead_14d` |
| **KPI** | Cost/engaged session. **Không** đặt conversion (bẫy optimize-to-quality) |

### GĐ2 — Tìm hiểu · 1.397 kw

| | |
|---|---|
| **Bật** | 852 kw brand (#1/#2: `pháp lý`, `chủ đầu tư`, `vị trí`, `dự án`, `dự án mới` — tức 1.088 kw brand của GĐ2 **trừ** 236 kw `tiến độ xây dựng`/`bàn giao khi nào` tắt ở kịch bản 30tr) + 233 kw #3 + 3 kw #8. 73 kw #5 chỉ từ G3 |
| **Bid** | Trung bình. Brand version chấp nhận CPC brand (rẻ); version khu vực (#5) Max Clicks có trần CPC |
| **RSA angle** | Authority + reciprocity: pháp lý sổ hồng, tên CĐT, tiến độ có tháng. **Không** chiết khấu, không "đặt cọc" — sai giai đoạn thì QS tụt vì ad relevance |
| **LP anchor** | Dòng `phap-ly` trong `adgroup-map.md` §Message match; brand version dùng dòng `brand-<dự-án>` + block Pháp lý/Tiến độ/Hồ sơ CĐT. Form nhẹ 2 field |
| **Audience đổ vào** | `engaged_60s_30d`, `xem_mat_bang_30d` (khách GĐ2 hay xem mặt bằng trước bảng giá) |
| **Loại ra** | `da_generate_lead_14d` |
| **KPI** | **Tỷ lệ vào audience remarketing**, không phải CPL. Đây là giai đoạn *mua audience*, không mua lead |

### GĐ3 — So sánh · 3.537 kw (khối lớn nhất theo `uu_tien` 1+2: 3.216)

| | |
|---|---|
| **Bật** | Toàn bộ nhóm giá (1.286 kw `giá` + `giá bao nhiêu`), tài chính (484), cấu hình/ngân sách (315), `mặt bằng`+`tiện ích` (480), bản brand của `có nên mua`/`review`/`đánh giá` (476). **Không** Search cho 315 kw T3 khu vực (`tiến độ` 63, `ở đâu tốt` 63, bản khu vực của `có nên mua`/`review`/`đánh giá` 189) |
| **Bid** | **Cao thứ hai sau GĐ4.** Đây là nơi tiền GĐ4 được tạo ra 2–6 tháng sau |
| **RSA angle** | Anchoring + contrast: "Bảng giá gốc CĐT [tháng/năm] — [N] loại căn, từ [X] ₫/m²". Trục phản công đối thủ (§3) sống ở đây |
| **LP anchor** | Dòng `*--gia-bang-gia`, `tai-chinh` trong `adgroup-map.md` §Message match. Bắt buộc có block **bảng giá anchor giá gốc → giá sau CK**, bảng tính vay, so sánh **đúng 3** loại căn (paradox of choice) |
| **Audience đổ vào** | `xem_bang_gia_30d` (feeder chính), `xem_mat_bang_30d`, `engaged_60s_30d` — cả 3 list này là **nguyên liệu của GĐ4** |
| **Loại ra** | `da_generate_lead_14d` |
| **KPI** | CVR LP · tỷ lệ vào list nóng. `generate_lead` chỉ secondary nếu volume thấp |

### GĐ4 — Quyết định · 3.572 kw (2.999 ở `uu_tien` 1 = bộ launch)

| | |
|---|---|
| **Bật** | Toàn bộ, cho **dự án đang thực sự phân phối**. Lọc bằng `nhom_adgroup`, phần còn lại là kho dự phòng (`adgroup-map.md`) |
| **Bid** | **Cao nhất.** 972 dòng exact để kiểm soát bid riêng. `bảng giá` + `(tên trần)` + `nhà mẫu` là 3 nhóm được nạp đủ trước tiên |
| **RSA angle** | Loss aversion + scarcity **thật**: "Đợt mở bán [N] — chiết khấu [X]% thanh toán sớm. Còn [N] căn." Số phải khớp LP, lệch là mất QS + nguy cơ disapproved |
| **LP anchor** | 3 dòng `brand-<dự-án>` (bảng giá / nhà mẫu / chính sách) + `*--mo-ban-moi` trong `adgroup-map.md` §Message match. Sticky CTA gọi/Zalo + form 3 field |
| **Audience đổ vào** | — (đây là điểm đến) |
| **Audience bid-up (RLSA, observation)** | `form_start_khong_submit_7d` > `xem_bang_gia_30d` > `xem_mat_bang_30d` ≈ `engaged_60s_30d`. Khởi điểm bid modifier theo skill `google-ads-audiences`: near-converter **+50…100%**, người đã xem bảng giá **+30…50%**, engaged **+15…25%** — sau 30 ngày chỉnh theo data thật, đừng giữ số khởi điểm |
| **Loại ra** | `da_generate_lead_14d` (**-100%**) ở mọi campaign remarketing |
| **KPI** | **CPL primary** (`generate_lead`), đảo sang `Lead_Contactable` khi ECL chạy · CPQL · Search IS |

### GĐ5 — Sau lead · 0 kw

Không có keyword. Toàn bộ là Customer Match + offline conversion import. Việc duy nhất của bộ keyword ở đây: **exclude** `da_generate_lead_14d` để không trả tiền lần hai cho người đã là lead.

### 2.1 Dòng chảy giữa giai đoạn — cách khách GĐ2 quay lại ở GĐ4

Đây là lý do bộ kw GĐ2–GĐ3 tồn tại dù CPL của chúng xấu. Chuỗi phải đóng kín, hở một khâu là mất toàn bộ chi phí GĐ2:

```
GĐ2 search "<dự án> pháp lý"  ──►  LP block Pháp lý/Tiến độ
        (kw uu_tien 2–3, T3 + brand)      │  form nhẹ 2 field (tuỳ chọn)
                                          ▼
                              vào GA4 list: engaged_60s_30d
                                          │
GĐ3 search "<dự án> bảng giá"  ──►  LP block Bảng giá  ──►  xem_bang_gia_30d
        (kw uu_tien 1, khối 3.537)        │                  (+ xem_mat_bang_30d)
                                          ▼
                       ┌──── Display/Demand Gen remarketing (mở ở G2)
                       │     nội dung nuôi: bài so sánh `content/` (nhóm T3 §1.1
                       │     không bid Search — chúng chạy ở đây, không ở Search)
                       ▼
       khách search LẠI "<dự án> chính sách bán hàng" / "<dự án> nhà mẫu"
                       │
                       ▼
GĐ4 ──► RLSA observation trên #1/#3: người trong xem_bang_gia_30d được bid +30…50%,
        người trong form_start_khong_submit_7d bid +50…100%
                       ▼
                  generate_lead ──► exclude khỏi remarketing 14 ngày ──► GĐ5 CRM
```

Ba điều kiện kỹ thuật để chuỗi này chạy — thiếu bất kỳ cái nào thì tiền GĐ2 là tiền đổ đi:

1. **Audience phải tạo NGAY khi LP live**, không đợi tới lúc cần G2 — GA4 không hồi tố quá 30 ngày (`tracking/ga4-setup.md` §3).
2. **RLSA phải ở mode Observation trên campaign #1/#3 từ ngày đầu** (không downside, theo `google-ads-audiences`), để 30 ngày sau có data mà chỉnh bid — không phải bật khi đã cần.
3. **Ngưỡng list**: Display ≥100 user active/30 ngày (`ga4-setup.md` §3); Search/RLSA của Google cao hơn nhiều và trùng đúng ngưỡng gate **G2 ≥1.000 user/30 ngày** → **G2 mở là RLSA mở**, đừng coi là hai việc.

Chu kỳ BĐS 3–12 tháng nghĩa là khoảng cách GĐ2 → GĐ4 dài hơn cửa sổ 30 ngày của audience. Hệ quả bắt buộc: **khách GĐ2 phải được nuôi bằng `content/` + email/Zalo từ form nhẹ**, không chỉ bằng remarketing list — list hết hạn trước khi khách quyết. Đây cũng là lý do data retention GA4 phải 14 tháng.

---

## 3. Từ khóa đối thủ theo hành trình

Kết nối `research/competitors/PLAYBOOK.md` bước 4–5. **GĐ3 So sánh là chỗ duy nhất bid tên đối thủ có nghĩa** — khách GĐ4 đã chọn dự án (bid tên đối thủ = mua lead của người khác), khách GĐ2 chưa có shortlist (chưa so sánh gì để phản công).

### 3.1 Điều kiện mở (ALL, theo PLAYBOOK 4.2 + 4.3)

| # | Điều kiện | Đo bằng |
|---|---|---|
| 1 | **Brand IS của mình ≥90%** ở nhóm `brand-<dự-án>` | Google Ads Search IS ở cấp ad group. Brand còn hở mà đi bid tên đối thủ = đổi lead rẻ lấy lead đắt |
| 2 | Đối thủ **đắt hơn hoặc bàn giao chậm hơn rõ rệt** | Bảng so sánh PLAYBOOK bước 5, mỗi ô có URL |
| 3 | Có **LP so sánh** tử tế, không phải LP bán hàng thẳng | LP riêng, có bảng so sánh + FAQ xử lý phản đối |
| 4 | Đủ ngân sách sau khi #1 thoả | Kịch bản 60tr+ (`customer-journey-plan.md` §3) |

Cấu trúc: **campaign riêng, ngân sách trần cứng, theo dõi contact rate riêng** — lead tệp này chất lượng thấp hơn brand, trộn vào campaign #1 sẽ làm nhiễu tCPA.

### 3.2 RSA angle — phản công theo trục thắng

Lấy nguyên bảng "Mình thắng ở → Headline" của `PLAYBOOK.md` bước 5. Quy tắc riêng cho tệp này: **headline đánh vào thuộc tính so sánh, tuyệt đối không vào tên**.

| Trục thắng | Headline (≤30 ký tự) |
|---|---|
| Giá vào thấp hơn | `Từ 2,5 Tỷ – Sở Hữu Ngay` |
| Vốn ban đầu thấp hơn | `Chỉ 25% Đến Khi Nhận Nhà` |
| Bàn giao sớm hơn | `Nhận Nhà Quý 4/2026` |

### 3.3 Trademark — nhắc lại 3 dòng, chi tiết ở PLAYBOOK 4.4

- Bid **keyword** tên đối thủ: **được phép**.
- Tên đối thủ trong **ad text** (headline/description/path/sitelink/callout/business name): **KHÔNG. Không ngoại lệ.** Complaint-driven từ 2/2025 — không bị chặn tự động, nhưng bị khiếu nại là gỡ ad + flag tài khoản.
- Không "cam kết sinh lời X%" — dùng "tiềm năng/dự kiến".

### 3.4 Negative chéo sibling cùng CĐT

Dự án cùng CĐT **không phải đối thủ** — chúng cannibalize nhau (PLAYBOOK bước 1, mục "Loại bỏ"). Bắt buộc negative chéo giữa các ad group `brand-<slug>` cùng CĐT, và **brand exclusion list** nếu chạy PMax (G4).

Dữ liệu thật trong `projects.tsv`: **240 dự án / 111 CĐT**. Các cụm sibling phải xử lý trước:

| CĐT | Số dự án | Hệ quả |
|---|---|---|
| Vinhomes | 31 | 31 ad group brand cạnh tranh nội bộ |
| Sun Group | 13 | |
| Masterise Homes | 12 | |
| Đất Xanh Group / Bcons Group | 7 mỗi CĐT | |
| Ecopark + Ecopark Group | 7 (`eco retreat`, `ecopark lâm đồng`, `khu đô thị ecopark`, `sky oasis ecopark`, `solforest ecopark`, `haven park ecopark`, `ecopark grand đảo châu âu`) | Ví dụ kinh điển: `eco retreat` (Bến Lức, Long An) ↔ các dự án Ecopark Văn Giang — cùng CĐT, khác tỉnh, khách gõ "eco…" là ra chéo nhau |

⚠️ **Lỗ hổng đã kiểm**: `grep -ci ecovillage` trên `projects.tsv` và `master-keywords.csv` = **0**. Nếu đang phân phối EcoVillage (Ecopark) thì đây là lỗ hổng nghiêm trọng theo PLAYBOOK 4.1 — thêm dòng vào `projects.tsv` rồi regenerate (`UPDATE.md`), **không** thêm tay vào master.

Cách gắn: mỗi ad group `brand-<slug>` nhận negative **phrase** là tên các sibling cùng CĐT. Không dùng exact (khách gõ biến thể sẽ lọt).

---

## 4. Rollout theo gate

Bảng ngắn — điều kiện đầy đủ ở `customer-journey-plan.md` §3.1, không lặp lại ở đây.

| Gate | Nhóm kw của bộ này được mở | Số kw |
|---|---|---|
| **G0** | GĐ4 `uu_tien` 1 của **dự án đang phân phối** (#1, #3) + GĐ3 nhóm giá `uu_tien` 1 | 2.999 + 1.288 → lọc theo `nhom_adgroup` |
| **G1** | GĐ4 + GĐ3 mở rộng sang khu vực/loại hình mới; `uu_tien` 2 của GĐ3 | +1.928 |
| **G2** | Không mở kw mới — mở **remarketing** để GĐ3 có đích đến, và **RLSA bid-up** cho GĐ4 (§2.1) | 0 |
| **G3** | GĐ2 Search (#5) 73 + GĐ1 (#6) 16 + 315 kw T3 khu vực của GĐ3 (#5/#6) | +404 |
| **G4** | PMax feed-less dùng GĐ3–GĐ4 làm audience signal; 12 broad seed (#7) giữ nguyên vai trò dò | 0 kw mới |
| **G5** | GĐ1 YouTube — không dùng keyword, đo bằng brand search lift | 0 |

236 kw `tiến độ xây dựng` + `bàn giao khi nào` **không thuộc gate nào** — chúng chỉ bật khi có lý do riêng (chăm khách đã mua, upsell), không phải để lấy lead mới.

---

## 5. Nhịp update — bổ sung vào `keywords/UPDATE.md`

Quy trình đọc search terms giữ nguyên (`UPDATE.md` §Hàng tuần, Q1–Q5). Thêm **một bước phân loại** trước khi ghi vào `gen.py`:

**Bước mới, chèn sau Q2 (search term có conversion, chưa là keyword):** với mỗi search term MỚI, tách modifier và xếp vào ma trận §1 **trước khi** thêm vào `gen.py`. Xếp giai đoạn quyết định modifier đi vào list nào:

| Giai đoạn của modifier mới | List trong `gen.py` | Match type | Xử lý mặc định |
|---|---|---|---|
| GĐ4 | `MOD_CORE` | phrase + exact cho head term | Search bid cao |
| GĐ3 | `MOD_MID` | phrase | Search bid trung |
| GĐ2 | `MOD_RESEARCH` | phrase | #5/#6, `uu_tien` 3 — chỉ từ G3 |
| GĐ1 | **không thêm vào `gen.py`** | — | Đề tài `content/` + negative nếu đốt tiền |
| Modifier brand (mọi giai đoạn) | `MOD_PROJECT` (dự án B+A) hoặc `MOD_PROJECT_EXTRA` (chỉ hạng A) | theo bảng §1.1 | |

Ánh xạ hiện có của `gen.py` (đối chiếu để không xếp sai list): `MOD_CORE` ≈ GĐ4 — **trừ 3 ngoại lệ đã có**: `giá`, `giá bao nhiêu` → GĐ3 và `dự án` → GĐ2. `MOD_MID` ≈ GĐ3 trọn vẹn. `MOD_RESEARCH` ≈ GĐ2–GĐ3. `MOD_PROJECT`/`MOD_PROJECT_EXTRA` trải cả 4 giai đoạn — đây là lý do §1 tồn tại.

**Thêm 2 dòng vào Checklist tuần của `UPDATE.md`:**

- [ ] Mỗi search term mới ở Q2 đã được xếp giai đoạn (§1) và ghi vào đúng list `MOD_*`
- [ ] Modifier mới xuất hiện lần đầu → thêm dòng vào bảng §1.1 file này (kèm số kw sau regenerate)

**Hàng tháng:** chạy lại script §6, đối chiếu 4 con số phân bố giai đoạn với lần trước. Khối GĐ4 phình lên mà CPL không giảm = đang nhân bản modifier chốt cho dự án không phân phối; khối GĐ2–3 phình lên mà audience không lớn theo = chuỗi §2.1 đang hở.

---

## 6. Script aggregate (nguồn của mọi con số trên)

Đảo ngược luật sinh của `gen.py` để lấy modifier thực của từng dòng — không đoán, không đọc cả file vào context. Chạy từ `keywords/`:

```python
# python3 - <<'EOF'   (chạy trong keywords/)
import csv, re, sys; sys.path.insert(0, '.')
import gen
from collections import Counter, defaultdict

proj = {gen.slug(p[0]): p[0] for p in gen.load_projects()}
devs = sorted([d for d, _ in gen.DEVELOPERS], key=len, reverse=True)
cut = lambda s, p: (s[:s.find(p)] + ' ' + s[s.find(p)+len(p):]) if p in s else s

def modifier(kw, ag, loai, khu):
    if ag == 'discovery-broad': return '(broad seed)'
    if ag.startswith('brand-cdt--'):
        d = next((d for d in devs if kw.startswith(d)), None)
        return (kw[len(d):].strip() or '(tên trần)') if d else '(?)'
    if ag.startswith('brand-'):
        p = proj.get(ag[6:])
        return (kw[len(p):].strip() or '(tên trần)') if p and kw.startswith(p) else '(?)'
    if loai == 'tổng hợp' and khu == 'toàn quốc': return 'GENERIC/' + ag
    m = re.sub(r'\s+', ' ', cut(cut(kw, loai), khu.split(' (')[0])).strip()
    return {'nên mua ở đâu': 'ở đâu tốt'}.get(m, m) or '(tên trần)'

c, match, tier = Counter(), defaultdict(Counter), defaultdict(Counter)
for r in csv.DictReader(open('master-keywords.csv', encoding='utf-8')):
    m = modifier(r['keyword'], r['nhom_adgroup'], r['loai_hinh'], r['khu_vuc'])
    c[m] += 1; match[m][r['match_type']] += 1; tier[m][r['intent_tier']] += 1
print(len(c), 'modifier /', sum(c.values()), 'dòng')
for m, n in c.most_common():
    print(f'{m}\t{n}\t{dict(match[m])}\t{dict(tier[m])}')
# EOF
```

Bảng `STAGE` (modifier → giai đoạn) là **bảng phân loại tay ở §1.1**, không suy ra được từ dữ liệu — khi thêm modifier mới phải cập nhật cả hai chỗ.
