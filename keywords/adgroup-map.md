# Map keyword → ad group → campaign

Nguồn dữ liệu: `master-keywords.csv` (8.805 keyword, 245 dự án thật, cập nhật 2026-07-28 — số chuẩn lấy từ self-check của `gen.py` mỗi lần chạy, đừng tin số hard-code ở đây nếu hai nguồn lệch nhau).

> **Đây là kho keyword, không phải lệnh build 1:1.** File có 1.616 `nhom_adgroup` khác nhau vì mỗi dự án thật có một ad group brand riêng (alias dùng chung ad group với dự án gốc, không tạo nhóm mới). Chỉ tạo ad group cho dự án bạn **thực sự đang phân phối**. Phần còn lại là kho dự phòng khi nhận thêm rổ hàng — lọc bằng cột `nhom_adgroup`.

> **Dự án ĐANG PHÂN PHỐI (2026-08-05): Beachtro Tower — Blanca City** (Sun Group, Vũng Tàu).
> Ad group brand duy nhất cần build ở campaign #1: **`brand-blanca-city`** (110 kw — gồm cả 4 alias
> `beachtro tower`, `blanca city vũng tàu`, `sun blanca city`, `beachtro tower vũng tàu`).
> Kèm theo: `brand-cdt--sun-group` + `brand-cdt--sun-property` (campaign #2) và cụm khu vực
> `vung-tau--*` / `ba-ria-vung-tau--*` (campaign #3). Checklist LP: `landing-page/beachtro-tower-checklist.md`.
>
> ```bash
> python3 -c "
> import csv,sys
> r=csv.reader(open('master-keywords.csv')); w=csv.writer(sys.stdout)
> h=next(r); w.writerow(h)
> [w.writerow(x) for x in r if x[1].startswith(('brand-blanca-city','brand-cdt--sun-','vung-tau--','ba-ria-vung-tau--'))]
> " > beachtro-launch.csv
> ```

## Nguyên tắc cấu trúc

**Không dùng SKAG.** Từ khi Google mở rộng close-variant matching (2018→nay), một keyword exact tự khớp hàng chục biến thể, nên SKAG chỉ làm loãng dữ liệu conversion và kéo dài learning phase. Dùng **STAG (Single Theme Ad Group)**: gom keyword cùng *một* intent + *một* thông điệp landing page vào một ad group, để RSA và LP nói đúng một chuyện.

Ba điều kiện để hai keyword ở chung ad group:
1. Cùng intent tier (không trộn "mua" với "có nên mua").
2. Cùng landing page / cùng block trên LP.
3. Cùng được phục vụ bởi một bộ 15 headline RSA.

Ngưỡng khối lượng: mỗi ad group nên có **5–20 keyword**, tối thiểu ~10 conversion/tháng để smart bidding học được. Ad group dưới ngưỡng thì gộp lên cấp campaign.

## Bản đồ campaign

| # | Campaign | Intent tier | Ad group (cột `nhom_adgroup`) | Số KW | Match | Bid strategy | % ngân sách |
|---|---|---|---|---|---|---|---|
| 1 | `BDS_Search_Brand_DuAn` | T1_brand_du_an | `brand-<slug-dự-án>` (1 ad group / dự án đang bán) | 4.526 | exact + phrase | tCPA (hoặc Max Conv khi <30 conv/tháng) | **40%** |
| 2 | `BDS_Search_Brand_CDT` | T1_brand_cdt | `brand-cdt--<slug-cđt>` | 308 | phrase | tCPA | **8%** |
| 3 | `BDS_Search_KhuVuc_GiaoDich` | T2_giao_dich | `<khu-vực>--gia-bang-gia`, `--mua-ban`, `--mo-ban-moi`, `--du-an-khu-vuc`, `--generic-<loại-hình>` | 2.362 | phrase (+ exact cho head term) | Max Conversions → tCPA | **30%** |
| 4 | `BDS_Search_TaiChinh` | T2/T3 | `tai-chinh`, `<khu-vực>--tai-chinh`, `phan-khuc-ngan-sach`, `cau-hinh-can` | 449 | phrase | tCPA | **7%** |
| 5 | `BDS_Search_PhapLy_TienDo` | T3_nghien_cuu | `phap-ly`, `tien-do`, `<khu-vực>--phap-ly`, `--tien-do` | 136 | phrase | Max Clicks (giới hạn CPC) | **3%** |
| 6 | `BDS_Search_NghienCuu` | T3_nghien_cuu | `tu-van-quyet-dinh`, `dau-tu`, `<khu-vực>--tu-van-quyet-dinh` | 268 | phrase | Max Clicks | **4%** |
| 7 | `BDS_Search_Discovery` | T2_giao_dich | `discovery-broad` | 12 | **broad** | tCPA (bắt buộc) | **5%** |
| 8 | `BDS_Search_NhaOXaHoi` | T2/T3 | `nha-o-xa-hoi` + dự án NOXH (K-Home, CIC, Hoàng Quân, Eco Home) | ~200 | phrase | Max Conversions | **3%** |
| — | `BDS_PMax_FeedLess`, `BDS_RMKT_Display` | — | (xem `playbook/`) | — | — | — | ngoài 100% Search |

Tổng % Search = 100%. Với ngân sách test 3–5 triệu ₫/ngày (PLAN §A): brand dự án ~1,2–2 tr, khu vực ~0,9–1,5 tr, phần còn lại chia theo bảng.

### Vì sao brand dự án ăn 40%
Truy vấn tên dự án là intent cao nhất, Quality Score cao nhất, CPC rẻ nhất trong BĐS VN — và nếu bạn không bid thì sàn F2/môi giới tự do sẽ bid. Đây là nơi CPL thấp nhất, nên nạp đủ trước khi mở rộng.

### Vì sao Discovery chỉ 5%
Broad match trong BĐS VN kéo về "cho thuê", "tuyển dụng", "nhà trọ" rất nhanh. 12 seed broad ở campaign #7 là **cần thiết** để phát hiện truy vấn mới cho vòng update, nhưng phải: (a) gắn full negative list account-level, (b) chạy tCPA chứ không Max Clicks, (c) review search terms **hàng tuần** không sót.

## Quy tắc tách ad group cho campaign #3 (khu vực)

Cột `nhom_adgroup` đã có sẵn dạng `<slug-khu-vực>--<chủ-đề>`. Ví dụ:

```
quan-7--gia-bang-gia      → "căn hộ quận 7 giá", "căn hộ quận 7 bảng giá", "căn hộ quận 7 giá bao nhiêu"
quan-7--mua-ban           → "mua căn hộ quận 7", "bán căn hộ quận 7"
quan-7--mo-ban-moi        → "căn hộ quận 7 mở bán", "dự án căn hộ mới quận 7", "căn hộ quận 7 sắp mở bán"
thu-duc--generic-nha-pho  → "nhà phố thủ đức", "mua nhà phố thủ đức"
```

Nếu một quận không đủ 10 conversion/tháng, gộp theo cụm địa lý:
- **Cụm Đông TP.HCM**: thủ đức, quận 2, quận 9, thảo điền, an phú
- **Cụm Nam TP.HCM**: quận 7, quận 8, nhà bè, bình chánh, phú mỹ hưng
- **Cụm Tây–Bắc TP.HCM**: quận 12, bình tân, tân phú, hóc môn, củ chi
- **Cụm Đông Hà Nội**: long biên, gia lâm, đông anh
- **Cụm Tây Hà Nội**: nam từ liêm, bắc từ liêm, hoài đức, hà đông, mỹ đình
- **Cụm vệ tinh Nam**: bình dương, đồng nai, long an, BR-VT
- **Cụm biển**: đà nẵng, nha trang, phú quốc, phan thiết, hạ long, vũng tàu

## Ưu tiên triển khai (cột `uu_tien`)

| `uu_tien` | Số KW | Nghĩa | Khi nào bật |
|---|---|---|---|
| **1** | 4.538 | Intent giao dịch / brand — bộ launch | Ngày 1 |
| **2** | 3.287 | Mở rộng: cấu hình căn, ngân sách, tài chính, brand phụ | Tuần 3–4, sau khi tier 1 có conversion ổn định |
| **3** | 687 | Nghiên cứu / top-funnel — chủ yếu nuôi remarketing audience | Chỉ bật khi tier 1+2 đã đạt tCPA mục tiêu, hoặc dùng làm audience cho PMax/Display |

**Lọc bộ launch:**
```bash
# awk -F, vỡ vì ghi_chu có dấu phẩy trong ngoặc kép — dùng csv stdlib
python3 -c "
import csv, sys
r = csv.reader(open('master-keywords.csv')); w = csv.writer(sys.stdout)
h = next(r); w.writerow(h); i = h.index('uu_tien')
[w.writerow(row) for row in r if row[i] == '1']
" > launch-set.csv
```

## Match type

- `exact` (1.397): head term khu vực + brand dự án lõi. Kiểm soát bid riêng, CPC cao nhất nhưng intent chuẩn nhất.
- `phrase` (7.103): mặc định. Cân bằng reach/kiểm soát, phù hợp tiếng Việt vì Google tự khớp bản không dấu và biến thể thứ tự từ.
- `broad` (12): chỉ campaign #7.

Không cần tạo dòng riêng cho keyword không dấu — Google match không dấu ↔ có dấu tự động. Bộ này để nguyên tiếng Việt có dấu, lowercase.

> ⚠️ **Câu trên CHỈ đúng cho POSITIVE keyword.** **Negative keyword KHÔNG khớp close variant** ([About negative keywords](https://support.google.com/google-ads/answer/2453972?hl=en)) → `cho thuê` **không** chặn `cho thue`. Vì vậy biến thể **không dấu trong negative list là BẮT BUỘC**, không phải tuỳ chọn (`research/google-ads-bds-vn.md` §3). Đừng áp luật của positive sang negative — đây là chỗ dễ hiểu ngược nhất trong cả bộ tài liệu.
>
> **Broad là match type MẶC ĐỊNH của Google Ads** ([About keyword matching options](https://support.google.com/google-ads/answer/7478529?hl=en): "Broad match is the default match type that all your keywords are assigned"). → mọi dòng import thiếu/sai cột `Match type` sẽ thành **broad im lặng**, không báo lỗi. Bắt buộc kiểm sau import: `playbook/campaign-setup.md` §2.4.6.

> 🧭 **Gộp là mặc định, tách là ngoại lệ.** Google khuyên cấu trúc **consolidated, themed ad group** và bỏ SKAG ([The ABCs of Account Structure](https://support.google.com/google-ads/answer/14752782?hl=en)). Bản đồ dưới đây liệt kê cấu trúc **mịn nhất có thể**, không phải cấu trúc phải dựng ngày 1. **Luật:** một ad group chỉ được tách riêng khi nó đạt **≥10 conversion/tháng**; chưa đạt thì **gộp** theo cụm chủ đề/địa lý. Ngưỡng bật thực tế ngày 1: `playbook/campaign-setup.md` §2.3 (tối đa 3 ad group cho #1, 2 cho #3).

## Message match (bắt buộc — QA điểm A↔B trong PLAN)

| Ad group | Headline RSA phải chứa | LP phải scroll tới block |
|---|---|---|
| `brand-<dự-án>` (mod: bảng giá) | tên dự án + "Bảng Giá Mới Nhất" | bảng giá + form tải bảng giá |
| `brand-<dự-án>` (mod: nhà mẫu) | tên dự án + "Đặt Lịch Xem Nhà Mẫu" | form đặt lịch + hình nhà mẫu |
| `brand-<dự-án>` (mod: chính sách bán hàng) | tên dự án + "Chính Sách & Chiết Khấu" | chính sách bán hàng |
| `*--gia-bang-gia` | loại hình + khu vực + "Giá Từ … ₫" | bảng giá |
| `*--mo-ban-moi` | "Mở Bán Đợt Mới" + khu vực | tiến độ + giữ chỗ |
| `tai-chinh` | "Trả Góp – Hỗ Trợ Vay …%" | chính sách vay |
| `phap-ly` | "Pháp Lý Sổ Hồng Đầy Đủ" | pháp lý |
| `tu-van-quyet-dinh` | "Tư Vấn Miễn Phí – So Sánh Dự Án" | bài SEO so sánh (`content/`) |

Mọi ad group đều dùng CTA gọi/Zalo (event `phone_click`, `zalo_click`) + form (`generate_lead`) theo `tracking/`.

## Negative keyword — nơi gắn

`negative-keywords.csv` có **465 dòng** (382 account / 83 campaign — số chuẩn: đếm bằng csv, đừng tin số hard-code):
- **382 dòng `cap_do=account`** → dán vào **từ khoá phủ định cấp tài khoản** (`Quản trị → Cài đặt tài khoản` — QA chốt 2026-07-28, tự áp mọi campaign type kể cả PMax; trần 1.000).
- **83 dòng `cap_do=campaign`** → apply chọn lọc:

| Nhóm negative | Chặn ở | KHÔNG chặn ở |
|---|---|---|
| `giá rẻ`, `rẻ nhất`, `dưới 1 tỷ`, `nhà ở xã hội` | #1–#7 | **#8 NhaOXaHoi** |
| `chính chủ`, `bán lại`, `cắt lỗ`, `nhà cũ`, `ký gửi` | tất cả (nếu chỉ bán sơ cấp) | — |
| `phát mãi`, `đấu giá`, `thanh lý ngân hàng` | tất cả | — |
| `môi giới`, `đại lý phân phối`, `tuyển đại lý` | tất cả | — |
| `năm 2020`–`năm 2023` | tất cả | — |

Negative nên set **phrase match** mặc định (Google Ads UI: `"cho thuê"`). Chỉ dùng exact negative khi cần chừa lại biến thể — ví dụ negative `[review]` để vẫn giữ được "review dự án X" nếu bạn có LP so sánh.

## Cảnh báo xung đột đã xử lý

`cho thuê` là negative **account-level** — nó sẽ chặn mọi keyword chứa cụm này. Vì vậy trong master list không có keyword nào chứa "cho thuê"; truy vấn đầu tư dùng cụm thay thế "đầu tư căn hộ dòng tiền", "căn hộ khai thác dòng tiền tốt". Nếu sau này muốn chạy tệp đầu tư cho thuê, phải **hạ `cho thuê` xuống campaign-level** trước, không thì keyword sẽ ở trạng thái eligible nhưng không bao giờ served.
