# BÀI THI PERFORMANCE MARKETING LEAD — VINHOMES HÓC MÔN
**Thí sinh:** số 6 · **Vai trò:** Performance Marketing Lead, An Phát Land
**Dữ liệu:** 02/03/2026 – 30/05/2026 (90 ngày × 6 chiến dịch, 486 dòng)
**Script tính:** `answers/agent-6-calc.py` → output `answers/agent-6-calc-output.txt`. Mọi con số dưới đây truy ngược được về script này, không có số nào tính tay.

## Kiểm tra dữ liệu đầu vào (đối chiếu sheet 02 ↔ sheet 03)

| Chỉ số | Tổng từ sheet 02 (script) | Sheet 03 dòng "TỔNG 90 NGÀY" | Khớp |
|---|---:|---:|:--:|
| Chi phí | 1.803.537.000đ | 1.803.537.000đ | ✔ |
| Nhấp chuột | 180.835 | 180.835 | ✔ |
| ChuyenDoi_Ads | 3.820 | 3.820 | ✔ |
| Lead_CRM | 2.557 | 2.557 | ✔ |
| Lead_SQL | 651 | 651 | ✔ |
| Đi xem / Booking / Cọc | 206 / 59 / 18 | 206 / 59 / 18 | ✔ |
| Doanh thu HH | 3.130.000.000đ | 3.130.000.000đ | ✔ |

**Lưu ý sai lệch nội bộ bộ đề (không phải lỗi của tôi, nêu để minh bạch):** sheet 06_DIA_LY tổng Lead CRM = 2.566 và SQL = 643, trong khi sheet 02/03 cho 2.557 và 651. Chênh +9 lead / −8 SQL. Tôi dùng sheet 02 làm nguồn chuẩn cho mọi phép tính; sheet 06 chỉ dùng để đọc **cơ cấu theo vùng** (tỷ trọng), không dùng để cộng tổng.

---

# PHẦN A — CHẨN ĐOÁN

12 vấn đề, xếp theo tác động tài chính giảm dần. Nhóm đo lường/kỹ thuật: **A2, A3, A9, A11** (4 vấn đề, vượt yêu cầu tối thiểu 3).

## Bảng tóm tắt

| # | Vấn đề | Tiền lãng phí / doanh thu bỏ lỡ (90 ngày) | Mức độ | Nhóm |
|---|---|---:|:--:|---|
| A1 | 4 chiến dịch chiếm 48% ngân sách nhưng 0 cọc | 865.324.000đ | Cao | Cấu trúc |
| A2 | Cột "Chuyển đổi" nuốt 2 sự kiện rác + đếm trùng → máy học tối ưu sai | 973 + 353 tín hiệu sai (34,7% cột chuyển đổi) — là **nguyên nhân gốc** của A1 | Cao | **Đo lường** |
| A3 | Không có GCLID trong CRM ⇒ không thể nhập chuyển đổi ngoại tuyến | khoá trần tối ưu ở mức lead thô; SQL/lead PMax 7,4% vs Brand 41,1% | Cao | **Đo lường** |
| A4 | Nhắm mục tiêu toàn quốc — 24,1% ngân sách bắn ra ngoài tệp | 434.652.417đ | Cao | Nhắm mục tiêu |
| A5 | Từ khóa rác + đối sánh rộng 71% chi phí Search | 432.740.000đ | Cao | Từ khóa |
| A6 | Brand bị bóp ngân sách: IS 52,6%, mất 40,4% IS do ngân sách | doanh thu bỏ lỡ 613tr (thận trọng) – 1.752tr (trần) | Cao | Ngân sách |
| A7 | Vận hành sale: 70% lead gọi lại sau 30 phút, 275 lead không ai gọi | 2.435.152.280đ (khả thi) + 193.966.631đ chi phí bốc hơi | Cao | Vận hành |
| A8 | Trang đích v1 chạy 57/90 ngày với LCP 4,8s, form 7 trường | 476.011.404đ | Cao | Trang đích |
| A9 | 3 lỗi kỹ thuật trên LP **chưa được sửa** (Clarity #4/#5/#6) | 471.435.276 – 611.591.709đ | Cao | **Đo lường/KT** |
| A10 | Lịch quảng cáo 24/7 lệch hoàn toàn khỏi lịch trực của sale | 483.347.916đ chi ở khung 20h–6h, gần như 0 cọc | Trung bình | Lịch/vận hành |
| A11 | GTM: thẻ gãy N44–46, config trùng, không cảnh báo, 412KB JS | 63 lead mất vĩnh viễn + 59,5tr chạy mù + LCP +0,8s | Trung bình | **Đo lường** |
| A12 | 78,1% ngân sách vào mobile trong khi desktop chuyển đổi gấp 1,98× | chênh CP/SQL 39% giữa 2 thiết bị | Trung bình | Thiết bị |

---

## A1 — Bốn chiến dịch chiếm 48% ngân sách, tạo 0 cọc và 0 doanh thu

**Phát hiện.** PMax, Competitor, GDN Remarketing và YouTube cùng nhau tiêu gần một nửa tài khoản và không tạo ra một giao dịch đặt cọc nào trong 90 ngày. Toàn bộ 18 cọc và 3,13 tỷ doanh thu đến từ đúng 2 chiến dịch Search.

**Bằng chứng số** (sheet 02, cột `Chi_phi` / `Dat_Coc` / `DoanhThu_HoaHong`, toàn kỳ):

| Chiến dịch | Chi phí | % NS | Lead CRM | SQL | Cọc | Doanh thu | ROAS | CP/SQL |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| SEA_Brand_Vinhomes_HocMon | 260.219.000đ | 14,4% | 857 | 352 | **13** | 2.280.000.000đ | **8,76** | 739.259đ |
| SEA_Generic_NhaPho_CanHo_TayBac | 677.994.000đ | 37,6% | 587 | 191 | **5** | 850.000.000đ | 1,25 | 3.549.707đ |
| PMAX_VinhomesHM_Lead | 475.376.000đ | 26,4% | 829 | 61 | 0 | 0 | **0** | 7.793.049đ |
| SEA_Competitor_DoiThu | 176.746.000đ | 9,8% | 32 | 3 | 0 | 0 | **0** | 58.915.333đ |
| GDN_Remarketing_Web30d | 130.009.000đ | 7,2% | 193 | 36 | 0 | 0 | **0** | 3.611.361đ |
| YT_Video_TVC_MoBan | 83.193.000đ | 4,6% | 59 | 8 | 0 | 0 | **0** | 10.399.125đ |
| **Tổng 4 CD không cọc** | **865.324.000đ** | **48,0%** | 1.113 | 108 | **0** | **0** | **0** | 8.012.259đ |

Đối chiếu chất lượng lead (sheet 08C, mẫu 600 lead): PMax có **7% lead dùng được** (trùng SĐT 31%, SĐT sai 24%, sai phân khúc 34%) so với Brand 67%. Clarity (sheet 11B): PMax **74,3% phiên thoát dưới 3 giây**, thời lượng phiên trung vị **3 giây** — đây không phải người quan tâm, đây là nhấp chuột từ vị trí đặt kém.

**Mức độ: CAO.** Lãng phí trực tiếp **865.324.000đ** (48% ngân sách). Thận trọng hơn: giữ lại phần lead dùng được của mỗi kênh thì vẫn lãng phí ≥ 700tr. Với CP/cọc của Brand (20,0tr/cọc), 865tr này lẽ ra mua được ~43 cọc.

## A2 — Cột "Chuyển đổi" đang đếm 2 sự kiện không phải khách hàng tiềm năng + đếm trùng lượt gọi *(đo lường)*

**Phát hiện.** Cả 4 sự kiện `generate_lead`, `click_to_call`, `view_price_page`, `engaged_30s` đều được đánh dấu là sự kiện chính và nhập vào cột Chuyển đổi của Google Ads. Hai sự kiện cuối chỉ là hành vi duyệt trang. `click_to_call` đếm **lượt nhấp** chứ không khử trùng theo người. Kết quả: Smart Bidding của PMax và tất cả chiến lược tự động đang được huấn luyện bằng tín hiệu rác.

**Bằng chứng số** (sheet 10_GA4 mục A + mục E; sheet 12_GTM mục A thẻ #5, #6, #8):

| Thành phần cột "Chuyển đổi" | Số lượt | % | Có phải lead? |
|---|---:|---:|---|
| generate_lead | 1.715 | 44,9% | Có |
| click_to_call (tổng lượt) | 1.132 | 29,6% | Có, nhưng 353 lượt là trùng người |
| view_price_page | 612 | 16,0% | **KHÔNG** |
| engaged_30s | 361 | 9,5% | **KHÔNG** |
| **Tổng** | **3.820** | 100% | |
| **Tín hiệu sai (rác 973 + trùng 353)** | **1.326** | **34,7%** | |

Hệ quả đo được: hệ số Ads/CRM toàn tài khoản = 3.820/2.557 = **1,49** (sheet 09 xếp 1,2–1,5 là "trung bình ngành", nhưng riêng PMax = 1.775/829 = **2,14** và YouTube = **3,00**, đều vượt ngưỡng báo động 1,8x). PMax là chiến dịch hưởng lợi nhiều nhất từ tín hiệu rác: theo sheet 10B, PMax một mình tạo 438/612 view_price_page (71,6%) và 259/361 engaged_30s (71,7%) của toàn tài khoản. Nghĩa là **thuật toán được dạy rằng PMax hiệu quả, nên nó bơm thêm tiền vào PMax** — chính là A1.

**Mức độ: CAO.** Đây là **nguyên nhân gốc**, không phải triệu chứng. Không quy được thành một con số tiền riêng vì tác động của nó đã nằm trong A1; quy sai sẽ là đếm trùng. Con số đo được: 34,7% tín hiệu tối ưu là sai, và 475.376.000đ ngân sách PMax bị lái theo tín hiệu này.

## A3 — CRM không lưu GCLID ⇒ không thể nhập chuyển đổi ngoại tuyến *(đo lường)*

**Phát hiện.** Google Ads chỉ nhìn thấy đến bước "có người điền form". Nó không bao giờ biết lead nào thành SQL, lead nào đi xem nhà, lead nào đặt cọc. Vì vậy mọi chiến lược giá thầu tự động đều đang tối ưu cho **lead rẻ**, chứ không phải **lead đúng**.

**Bằng chứng số** (sheet 05 dòng "Nhập chuyển đổi ngoại tuyến từ CRM: CHƯA triển khai — CRM không lưu GCLID"; sheet 12_GTM mục A #15 "Biến ẩn lưu GCLID vào form: CHƯA CÀI", mục C "Lưu GCLID vào CRM: KHÔNG ĐẠT"; sheet 05 "Chuyển đổi nâng cao: TẮT"):

| Chiến dịch | CPL Ads (Ads "thấy") | CP/SQL (thực tế) | Bội số |
|---|---:|---:|---:|
| PMAX_VinhomesHM_Lead | **267.817đ** (rẻ nhất TK) | 7.793.049đ | 29,1× |
| SEA_Brand_Vinhomes_HocMon | 299.052đ | **739.259đ** (rẻ nhất TK) | 2,5× |
| GDN_Remarketing_Web30d | 429.746đ | 3.611.361đ | 8,4× |
| YT_Video_TVC_MoBan | 470.017đ | 10.399.125đ | 22,1× |
| SEA_Generic | 1.020.955đ | 3.549.707đ | 3,5× |

Xếp hạng theo CPL Ads và xếp hạng theo CP/SQL **đảo ngược gần như hoàn toàn**. Tỷ lệ SQL/lead: PMax 7,4% vs Brand 41,1% (sheet 02, `Lead_SQL`/`Lead_CRM`) — chênh 5,6 lần, và Google Ads hoàn toàn mù với khoảng chênh này.

**Mức độ: CAO.** Đây là thứ khoá trần hiệu quả của toàn bộ tài khoản. Không định lượng riêng được bằng dữ liệu hiện có (cần chạy ECL 60–90 ngày rồi so sánh mới có số) — nhưng nếu Ads được dạy bằng tín hiệu SQL thay vì lead thô, khoảng chênh 29,1× ở PMax là dư địa tối ưu trực tiếp.

## A4 — Nhắm mục tiêu toàn quốc: 24,1% ngân sách bắn ra ngoài tệp khách hàng

**Phát hiện.** Cả 6 chiến dịch nhắm "Việt Nam (toàn quốc)", tuỳ chọn vị trí để mặc định "Hiện diện HOẶC quan tâm", không có loại trừ vị trí nào. Trong khi tệp khách hàng theo sheet 01 là Q.12, Gò Vấp, Hóc Môn, Củ Chi, Bình Tân, Tân Phú + nhà đầu tư TP.HCM/Bình Dương/Long An.

**Bằng chứng số** (sheet 05 "Nhắm mục tiêu vị trí / Loại trừ vị trí: Không có"; sheet 06_DIA_LY):

| Vùng | Chi phí | SQL | Cọc | CP/SQL |
|---|---:|---:|---:|---:|
| Hà Nội | 155.104.182đ | 20 | 0 | 7.755.209đ |
| Cần Thơ & ĐBSCL | 93.783.924đ | 12 | 0 | 7.815.327đ |
| Đà Nẵng | 86.569.776đ | 7 | 0 | **12.367.111đ** |
| Đồng Nai | 70.337.943đ | 14 | 0 | 5.024.139đ |
| Ngoài Việt Nam | 28.856.592đ | 7 | 0 | 4.122.370đ |
| **Tổng 5 vùng ngoài tệp** | **434.652.417đ (24,1% NS)** | **60 (9,3% SQL)** | **0** | **7.244.207đ** |
| — so với 6 quận lõi TP.HCM | 835.037.631đ (46,3%) | 399 (62,1%) | **14** | 2.093tr trung bình |

Ngưỡng báo động CP/SQL của sheet 09 là 5 triệu — Hà Nội, Đà Nẵng, Cần Thơ đều vượt gấp 1,5–2,5 lần và không đóng góp cọc nào.

**Mức độ: CAO.** Lãng phí **434.652.417đ**. Chuyển số này về 6 quận lõi (CP/SQL bình quân 2,09tr) sẽ mua thêm ~208 SQL. Riêng "Ngoài Việt Nam quan tâm đến VN" 28,8tr là lỗi cấu hình thuần tuý — chỉ cần đổi tuỳ chọn vị trí sang "Hiện diện" là hết.

## A5 — Đối sánh rộng chiếm 71% chi phí Search, chỉ 12 từ phủ định trong toàn tài khoản

**Phát hiện.** Từ khoá đối sánh rộng ăn 71% chi phí Search trong khi chính xác chỉ 9%. Tài khoản có đúng 12 từ phủ định, không dùng danh sách phủ định chia sẻ. Hệ quả là tiền chảy vào các cụm từ hoàn toàn không liên quan tới việc bán nhà 6,8–11,5 tỷ.

**Bằng chứng số** (sheet 05 "Tỷ trọng chi phí theo đối sánh rộng: 71%", "Số từ khóa phủ định: 12 từ"; sheet 04_SEARCH_TERMS):

| Cụm từ tìm kiếm | Chi phí | Lead CRM | SQL | Vấn đề |
|---|---:|---:|---:|---|
| vinhomes hóc môn tuyển dụng | 15.613.000đ | 11 | 0 | tìm việc |
| vinhomes hóc môn có thật không | 13.011.000đ | 26 | 3 | hoài nghi, CP/SQL 4,34tr |
| vinschool hóc môn học phí | 10.409.000đ | 4 | 0 | tìm trường học |
| giá đất hóc môn 2026 | 33.900.000đ | 29 | 0 | đất nền, sai sản phẩm |
| bản đồ quy hoạch hóc môn | 27.120.000đ | 6 | 0 | tra cứu |
| thuê nhà nguyên căn hóc môn | 27.120.000đ | 6 | 0 | thuê, không mua |
| bán đất thổ cư hóc môn 100 triệu | 27.120.000đ | 6 | 0 | sai ngân sách |
| cho thuê kho xưởng hóc môn | 20.340.000đ | 4 | 0 | sai sản phẩm |
| nhà trọ hóc môn giá rẻ | 20.340.000đ | 4 | 0 | sai phân khúc |
| việc làm bất động sản hóc môn | 20.340.000đ | 4 | 0 | tìm việc |
| nhà đất hóc môn lừa đảo | 20.340.000đ | 4 | 0 | ý định tiêu cực |
| chung cư mini gò vấp | 20.340.000đ | 18 | 0 | sai sản phẩm |
| **Cộng 12 cụm rác** | **255.993.000đ** | 122 | **3** | 23,0% chi phí bảng search terms |
| **+ toàn bộ 6 cụm Competitor** | **176.747.000đ** | 32 | **0** | CPC TB 46.000–60.756đ |
| **TỔNG cần chặn** | **432.740.000đ** | | **3** | |

Riêng CPC của Competitor 46.028–60.756đ, vượt ngưỡng báo động của sheet 09 (>60.000đ) và cao gấp 4–5 lần CPC Brand (11.959–13.671đ), để đổi lấy 0 SQL.

**Mức độ: CAO.** Lãng phí **432.740.000đ**, tương đương 24% ngân sách.

## A6 — Chiến dịch có ROAS 8,76x đang bị bóp ngân sách suốt 90 ngày

**Phát hiện.** SEA_Brand là chiến dịch duy nhất đạt ROAS vượt xa mục tiêu 3,0x, tạo 72% số cọc bằng 14,4% ngân sách — nhưng bị giới hạn ngân sách nặng, mất trung bình 40,4% impression share vì hết tiền, mỗi ngày, suốt 90 ngày.

**Bằng chứng số** (sheet 02, cột `Impr_Share`, `Mat_IS_NganSach`, chiến dịch SEA_Brand; sheet 05 "ngân sách 2,0 → 2,5 → 4,5 triệu/ngày"; sheet 09 "Mất IS do ngân sách (chiến dịch tốt): >20% = báo động", "IS thương hiệu <60% = báo động"):

| Giai đoạn | IS TB | Mất IS do NS | Mất IS do thứ hạng | Chi phí | Cọc | ROAS |
|---|---:|---:|---:|---:|---:|---:|
| GĐ1 | 54,1% | 39,2% | 6,8% | 57,6tr | 2 | 5,73 |
| GĐ2 | 48,9% | **43,8%** | 7,3% | 72,3tr | 3 | 7,19 |
| GĐ3 | 54,8% | 38,4% | 6,8% | 130,3tr | 8 | **10,97** |
| **Toàn kỳ** | **52,6%** | **40,4%** | 6,9% | 260,2tr | 13 | **8,76** |

Chi tiết đối chiếu: cụm "vinhomes hóc môn" (đối sánh chính xác) chi 78.066.000đ → 138 SQL, **CP/SQL 565.695đ — rẻ nhất toàn tài khoản** (sheet 04). Trong khi đó Generic được cấp 677.994.000đ (2,6× Brand) để tạo CP/SQL 3.549.707đ (6,3× đắt hơn).

**Mức độ: CAO.**
- *Trần lý thuyết* (giả định tuyến tính, lấp 100% phần mất IS do ngân sách → lưu lượng +77%): doanh thu bỏ lỡ **1.752tr**, chi phí thêm 200tr.
- *Ước tính thận trọng của tôi* (chỉ lấp 50% và giả định lưu lượng biên kém hơn 30%): doanh thu bỏ lỡ **613tr**, chi phí thêm 100tr → **lãi ròng bỏ lỡ ~513tr**.
- **Điểm yếu của ước tính này:** giả định tuyến tính là sai về nguyên tắc — lưu lượng biên luôn chuyển đổi kém hơn lưu lượng lõi. Cần tăng ngân sách Brand 2 tuần rồi đo lại CP/SQL biên mới kết luận chắc chắn được. Đây là hạng mục đầu tiên tôi làm trong tuần 1 (xem phần E).

## A7 — Vận hành sale: 70% lead được gọi lại sau 30 phút, 275 lead không ai gọi

**Phát hiện.** Marketing đang mua lead rồi để chúng nguội. Dữ liệu CRM cho thấy tốc độ phản hồi là biến số mạnh nhất trong toàn bộ phễu — mạnh hơn mọi thứ có thể tối ưu trong Google Ads.

**Bằng chứng số** (sheet 08A, mẫu 2.554 lead; sheet 08B):

| Thời gian gọi lại | Số lead | % | Liên hệ được | Đồng ý đi xem | **Tỷ lệ cọc** |
|---|---:|---:|---:|---:|---:|
| Dưới 5 phút | 281 | 11% | 87% | 23,1% | **1,82%** |
| 5 – 30 phút | 485 | 19% | 74% | 15,4% | 1,21% |
| 30 phút – 2 giờ | 588 | 23% | 58% | 8,6% | 0,58% |
| 2 – 12 giờ | 536 | 21% | 41% | 4,2% | 0,21% |
| Trên 12 giờ | 664 | 26% | 22% | 1,1% | **0,04%** |

Chênh lệch tỷ lệ cọc giữa nhóm nhanh nhất và chậm nhất: **46 lần**. Nhóm chậm (>30 phút) = 1.788 lead = **70% tổng lead**, hiện chỉ tạo 4,8 cọc.

Sheet 08B: lead bị bỏ sót hoàn toàn 118 + 96 + 61 = **275 lead** — tiền đã trả, không ai nhấc máy. Theo CPL CRM thực tế 705.333đ = **193.966.631đ bốc hơi**.

**Mức độ: CAO.**
- *Trần lý thuyết* (100% gọi <5 phút — không khả thi với 8 sale): 32,5 cọc, +27,7 cọc = 5.020.940.000đ. Tôi **không** dùng con số này để cam kết.
- *Mục tiêu khả thi của tôi* (SLA 30 phút áp cho 70% nhóm chậm): 1.252×1,21% + 536×0,58% = 18,3 cọc → **+13,5 cọc = 2.435.152.280đ**.
- Ràng buộc "không tăng sale" nghĩa là con đường duy nhất là **giảm số lượng lead và tăng chất lượng** — đúng hướng với A1/A4/A5.

## A8 — Trang đích v1 chạy 57/90 ngày với LCP 4,8s và form 7 trường

**Phát hiện.** Trang đích cũ vượt ngưỡng báo động tốc độ và có form dài với 2 trường gây bỏ dở nghiêm trọng. Bản v2 chỉ được triển khai ngày 58.

**Bằng chứng số** (sheet 05; sheet 10C; sheet 11C; sheet 09 "LCP >4s = báo động"):

| Chỉ số | v1 (N1–57) | v2 (N58–90) | Chênh |
|---|---:|---:|---:|
| Phiên | 52.410 | 42.938 | |
| LCP | **4,8s** (báo động) | 1,9s (tốt) | −60% |
| Tỷ lệ tương tác | 34,2% | 58,7% | +71,6% |
| Độ sâu cuộn 90% | 16% | 37% | +131% |
| form_start | 4.912 (9,37% phiên) | 2.546 (5,93% phiên) | **−37%** |
| generate_lead | 1.002 | 713 | |
| **Tỷ lệ hoàn tất form** | 20,4% | **28,0%** | **+37%** |
| **Lead / phiên** | 1,91% | 1,66% | **−13%** |

Clarity xác nhận nguyên nhân form v1 (sheet 11C): trường "Số CMND/CCCD" (trường 4/7) khiến **61% phiên bỏ dở ngay tại đó**, 2.987 phiên ảnh hưởng, ước tính mất 320–400 lead; dropdown "Ngân sách đầu tư" 9 lựa chọn làm 27% bỏ dở, mất thêm 110–150 lead. Rage click mobile v1 18,7% → v2 3,1%; dead click 24,1% → 6,2%.

**Mức độ: CAO.** Nếu giữ nguyên form_start của v1 nhưng áp tỷ lệ hoàn tất của v2: 4.912 × 28,0% = 1.376 lead thay vì 1.002 → **+374 lead** × SQL 25,5% × SQL→Cọc 2,76% = 2,6 cọc = **476.011.404đ** doanh thu bỏ lỡ vì chậm 57 ngày.

**⚠ Phát hiện nghịch lý cần điều tra ngay:** v2 tốt hơn v1 ở **mọi** chỉ số trải nghiệm nhưng **lead/phiên lại giảm 13%**, và giảm ở cả mobile (1,60%→1,48%) lẫn desktop (2,76%→2,37%) — nên không phải do đổi mix thiết bị. Hai cách giải thích cạnh tranh: (a) v2 chôn CTA form xuống dưới nên ít người bắt đầu điền, (b) mix nguồn lưu lượng đổi ở GĐ3 (YouTube tăng từ 11,6tr lên 71,6tr chi phí, hao hụt nhấp→phiên 82%, sheet 10B) làm loãng mẫu số phiên. **Không đủ dữ liệu để tách hai nguyên nhân này** vì sheet 05 ghi rõ "Số phiên bản trang đích đang chạy A/B: 1 (không thử nghiệm)" — hai bản chạy nối tiếp chứ không song song. **Cần thêm:** báo cáo GA4 lead/phiên tách theo `session_campaign` × phiên bản LP cho cùng khung ngày, hoặc chạy A/B đồng thời 2 tuần. Đây là việc số 3 trong tuần đầu.

## A9 — Ba lỗi kỹ thuật trên trang đích **chưa được sửa**, đang chặn lead mỗi ngày *(đo lường/kỹ thuật)*

**Phát hiện.** Clarity đã chỉ đích danh 3 lỗi vẫn còn nguyên trên cả v1 lẫn v2. Lỗi nặng nhất khiến form **không gửi được mà không báo lỗi cho khách** — khách nghĩ đã đăng ký xong, sale không bao giờ nhận được lead.

**Bằng chứng số** (sheet 11_CLARITY mục C; sheet 11A "tỷ lệ lỗi JS trên di động KHÔNG giảm sau v2: 9,3% → 8,9%"):

| # | Lỗi | Phiên ảnh hưởng (ĐO ĐƯỢC) | Lead mất (ƯỚC TÍNH của đội UX) | Trạng thái |
|---|---|---:|---:|---|
| 4 | `TypeError: e.setDate is not a function` (bộ chọn ngày hẹn xem nhà) trên Safari iOS 17.x — form không gửi được, không báo lỗi | 4.196 | 280 – 340 | **CHƯA SỬA** |
| 5 | Nút "Đăng ký nhận bảng giá" bị khung chat che trên màn hình <380px | 2.741 | 60 – 90 | **CHƯA SỬA** |
| 6 | Hotline dạng `tel:` — desktop bấm không phản hồi, 1.847 nhấp chết | 1.204 | 30 – 50 | **CHƯA SỬA** |
| | **Tổng** | **8.141** | **370 – 480** | |

**Mức độ: CAO.** Quy tiền chi tiết ở B7: **471.435.276 – 611.591.709đ** doanh thu bỏ lỡ. Lỗi #4 là lỗi nghiêm trọng nhất trong toàn bộ tài khoản xét trên tỷ số (chi phí sửa) / (giá trị thu hồi) — sửa mất vài giờ dev.

## A10 — Lịch quảng cáo 24/7 lệch hoàn toàn khỏi lịch trực của đội sale

**Phát hiện.** Quảng cáo chạy đều 24/7 không điều chỉnh giá thầu theo giờ, trong khi tỷ lệ sale gọi lại trong 30 phút sụt từ 93% (9–12h) xuống 21% (20–23h) và 12% (23–24h). Tiền đổ vào đúng những khung giờ không có ai trực máy.

**Bằng chứng số** (sheet 05 "Lịch quảng cáo: 24/7, không điều chỉnh giá thầu theo giờ"; sheet 07A; sheet 07C):

| Khung giờ | % chi phí | Chi phí | SQL | Cọc | CP/SQL | Gọi lại <30 phút |
|---|---:|---:|---:|---:|---:|---:|
| 09:00–12:00 | 16,8% | 302.994.216đ | 121 | 4 | **2.504.084đ** | **93%** |
| 14:00–17:00 | 17,1% | 308.404.827đ | 117 | 4 | 2.635.939đ | 91% |
| 06:00–09:00 | 9,5% | 171.336.015đ | 57 | 2 | 3.005.895đ | 81% |
| 20:00–23:00 | **18,7%** | 337.261.419đ | 112 | 3 | 3.011.263đ | **21%** |
| 23:00–24:00 | 4,0% | 72.141.480đ | 22 | 0 | 3.279.158đ | **12%** |
| 00:00–06:00 | 4,1% | 73.945.017đ | 18 | 0 | **4.108.057đ** | 34% |
| **Cộng 20:00–06:00** | **26,8%** | **483.347.916đ** | 152 | 3 | 3.180.000đ | 12–34% |

Theo ngày trong tuần (sheet 07C): T7 + CN chi 503.810.000đ để đổi 4 cọc = **125.952.500đ/cọc**, trong khi T2–T6 chi 1.299.727.000đ đổi 14 cọc = 92.837.643đ/cọc. Riêng thứ 2 là 36.876.714đ/cọc — tốt nhất tuần. Chênh lệch này khớp chính xác với việc "chỉ 2 sale trực T7–CN" (sheet 01C).

**Mức độ: TRUNG BÌNH.** 26,8% ngân sách (483tr) nằm ở khung giờ có tỷ lệ phản hồi 12–34%. Không nên cắt sạch (nhà mẫu mở 8–18h, khách BĐS có tìm kiếm buổi tối), nhưng cần giảm giá thầu và bật biểu mẫu khách hàng tiềm năng cho khung đêm.

## A11 — GTM: thẻ gãy 3 ngày không ai biết, thẻ trùng, 412KB JavaScript *(đo lường)*

**Phát hiện.** Vùng chứa GTM là nguồn của bốn lỗi độc lập, và không có bất kỳ cơ chế cảnh báo nào.

**Bằng chứng số** (sheet 12_GTM mục A, B, C; đối chiếu sheet 02):

| Sự cố | Bằng chứng | Hệ quả |
|---|---|---|
| Thẻ `generate_lead` gãy N44–46 | GTM v23 (N44 09:12, dev@) đổi class `.form-dk-v1` → `.form-register`, điều kiện kích hoạt ngừng khớp. Sheet 02: `ChuyenDoi_Ads` = **0** đúng 3 ngày N44/45/46 trong khi `Lead_CRM` = 17/15/31 = **63 lead** | 63 lead **vĩnh viễn** không có trong Ads/GA4; **59.500.000đ** chi phí 3 ngày chạy mù, Smart Bidding học sai |
| Không có cảnh báo chuyển đổi = 0 | GTM mục A #18 "KHÔNG CÓ" | Sự cố trên mất **3 ngày** mới phát hiện (v24 sửa ngày 47) |
| Thẻ GA4 Config trùng | GTM v22 (N31) thêm "GA4 Configuration – Copy of Main" | `page_view` đếm đôi từ N31 → số phiên và tỷ lệ thoát sai lệch từ N31 trở đi. **Lưu ý:** điều này làm bảng so sánh LP ở A8 kém tin cậy vì v1 (N1–57) chứa cả kỳ chưa lỗi lẫn kỳ đã lỗi |
| Điều kiện kích hoạt dựa trên class CSS | GTM #3 "rất dễ vỡ khi dev đổi giao diện" | Mọi lần đổi giao diện đều có thể gãy lại |
| 34 thẻ / 412KB JS bên thứ ba | Header sheet 12 | LCP chậm thêm **~0,8s**; v20 (N18) thêm thẻ đối tác sàn F2 làm LCP +0,3s |
| 3 thẻ đối tác F2 + Zalo Tracking không rõ nguồn gốc | GTM #12, #13 "Không rõ ai cài" | Rủi ro bảo mật/rò rỉ dữ liệu khách hàng, cần rà soát |
| Sự kiện có giá trị nhưng không được nhập vào Ads | GTM v26 (N71) + sheet 10E: `zalo_click` **894 lượt**, `file_download` bảng giá PDF **1.206 lượt** | 2.100 tín hiệu ý định mua đang bị bỏ không — Zalo là CTA chính ở thị trường VN |

**Mức độ: TRUNG BÌNH** (xét riêng; nhưng cộng với A2/A3 thì nhóm đo lường là mức Cao). Thiệt hại đo được: 63 lead + 59,5tr chạy mù + LCP +0,8s + 2.100 tín hiệu bỏ không.

## A12 — 78,1% ngân sách vào mobile trong khi desktop chuyển đổi gấp gần 2 lần

**Phát hiện.** Phân bổ thiết bị chưa từng được điều chỉnh, dù desktop rẻ hơn 39% trên mỗi SQL.

**Bằng chứng số** (sheet 07B; sheet 11A):

| Thiết bị | % chi phí | Chi phí | Lead | SQL | Cọc | Tỷ lệ CĐ | CP/SQL |
|---|---:|---:|---:|---:|---:|---:|---:|
| Điện thoại | 78,1% | 1.408.562.397đ | 2.106 | 463 | 11 | **2,03%** | 3.042.251đ |
| Máy tính | 16,7% | 301.190.679đ | 334 | 163 | 6 | **4,02%** | **1.847.796đ** |
| Máy tính bảng | 5,2% | 93.783.924đ | 115 | 24 | 1 | 1,71% | 3.907.664đ |

Desktop: 16,7% chi phí → 25,0% SQL và 33,3% cọc. Nguyên nhân đã rõ từ A9: lỗi #4 (Safari iOS) và #5 (<380px) đều là lỗi **chỉ có trên mobile**, và Clarity xác nhận tỷ lệ lỗi JS trên mobile không giảm sau v2 (9,3% → 8,9%).

**Mức độ: TRUNG BÌNH.** Đây vừa là cơ hội điều chỉnh giá thầu, vừa là bằng chứng bổ sung rằng A9 phải sửa trước — nếu sửa được lỗi mobile thì mobile có thể tốt lên chứ không nên vội cắt (78% lưu lượng BĐS VN là mobile).

---

# PHẦN B — TÍNH TOÁN

Toàn bộ số trong phần này sinh từ `agent-6-calc.py`. Đơn vị VND.

## B1. CPL Ads / CPL CRM / CP/SQL / CP/cọc

**Toàn kỳ (nguồn: sheet 02, tổng 486 dòng):**

| Chỉ số | Công thức | Giá trị |
|---|---|---:|
| Chi phí | Σ `Chi_phi` | 1.803.537.000đ |
| CPL theo Ads | Chi phí / 3.820 `ChuyenDoi_Ads` | **472.130đ** |
| CPL theo CRM | Chi phí / 2.557 `Lead_CRM` | **705.333đ** |
| CP/SQL | Chi phí / 651 `Lead_SQL` | **2.770.410đ** |
| CP/cọc | Chi phí / 18 `Dat_Coc` | **100.196.500đ** |

CPL theo Ads thấp hơn CPL theo CRM **32,9%** — đó chính là mức "ảo" mà báo cáo Google Ads đang tạo ra.
So với sheet 09: CPL CRM 705.333đ nằm trong khoảng "trung bình ngành" (500k–1,1tr); CP/SQL 2.770.410đ cũng "trung bình ngành" (1,8–3,5tr) nhưng **vượt KPI 2.200.000đ được giao 25,9%**; CP/cọc 100,2tr **vượt 1,7 lần** ngưỡng hoà vốn ROAS 3,0 (60,3tr — xem B5).

**Theo từng chiến dịch:**

| Chiến dịch | Chi phí | CPL Ads | CPL CRM | CP/SQL | CP/cọc | SQL/Lead | Ads/CRM |
|---|---:|---:|---:|---:|---:|---:|---:|
| SEA_Brand_Vinhomes_HocMon | 260.219.000đ | 299.052đ | **304.339đ** | **739.259đ** | **20.016.846đ** | **41,1%** | **1,02** |
| SEA_Generic_NhaPho_CanHo_TayBac | 677.994.000đ | 1.020.955đ | 1.154.845đ | 3.549.707đ | 135.598.800đ | 32,5% | 1,13 |
| PMAX_VinhomesHM_Lead | 475.376.000đ | **267.817đ** | 573.433đ | 7.793.049đ | — (0 cọc) | 7,4% | 2,14 |
| SEA_Competitor_DoiThu | 176.746.000đ | 5.701.484đ | 5.523.313đ | **58.915.333đ** | — (0 cọc) | 9,4% | 0,97 |
| GDN_Remarketing_Web30d | 130.009.000đ | 429.746đ | 673.622đ | 3.611.361đ | — (0 cọc) | 18,7% | 1,56 |
| YT_Video_TVC_MoBan | 83.193.000đ | 470.017đ | 1.410.051đ | 10.399.125đ | — (0 cọc) | 13,6% | **3,00** |
| **TOÀN KỲ** | **1.803.537.000đ** | **472.130đ** | **705.333đ** | **2.770.410đ** | **100.196.500đ** | **25,5%** | **1,49** |

**Đọc bảng này thế nào:** cột CPL Ads xếp PMax hạng 1 (rẻ nhất). Cột CP/SQL xếp PMax hạng 5/6. Cột CP/cọc loại PMax khỏi bảng vì bằng 0. Chỉ có **một** chiến dịch tốt ở cả bốn cột: SEA_Brand.

## B2. ROAS toàn kỳ và theo giai đoạn

| Giai đoạn | Chi phí | Doanh thu HH | **ROAS** | Cọc | CP/cọc | Đạt KPI 3,0x? |
|---|---:|---:|---:|---:|---:|:--:|
| GĐ1 (N1–30) | 545.696.000đ | 330.000.000đ | **0,60** | 2 | 272.848.000đ | ✘ |
| GĐ2 (N31–60) | 604.392.000đ | 850.000.000đ | **1,41** | 5 | 120.878.400đ | ✘ |
| GĐ3 (N61–90) | 653.449.000đ | 1.950.000.000đ | **2,98** | 11 | 59.404.455đ | ✘ (sát ngưỡng) |
| **Toàn kỳ** | **1.803.537.000đ** | **3.130.000.000đ** | **1,74** | **18** | **100.196.500đ** | ✘ |

**ROAS theo chiến dịch (toàn kỳ):**

| Chiến dịch | Chi phí | Doanh thu | ROAS |
|---|---:|---:|---:|
| SEA_Brand_Vinhomes_HocMon | 260.219.000đ | 2.280.000.000đ | **8,76** |
| SEA_Generic_NhaPho_CanHo_TayBac | 677.994.000đ | 850.000.000đ | 1,25 |
| PMax / Competitor / GDN / YouTube | 865.324.000đ | 0đ | **0,00** |

**Diễn giải.** Xu hướng đi đúng hướng — ROAS tăng 0,60 → 1,41 → 2,98 qua 3 giai đoạn, và GĐ3 gần chạm mục tiêu 3,0x. Ba nguyên nhân đọc được từ dữ liệu: (1) trang đích v2 lên từ N58 (sheet 05); (2) thời gian phản hồi trung vị của sale giảm 214 → 142 → **47 phút**, có SLA gọi trong 15 phút từ GĐ3 (sheet 08B); (3) sự kiện mở bán ở GĐ3 (sheet 01D). **Cảnh báo:** ROAS 2,98 của GĐ3 là con số của một tháng có sự kiện mở bán, không được mặc định giả sử nó lặp lại. Xu hướng tuần (phụ lục script) cho thấy CP/SQL giảm đều 4,25tr (T1) → 1,88tr (T12–13), đây là tín hiệu bền hơn.

## B3. Tỷ lệ chuyển đổi từng bước phễu

| Bước | Toàn kỳ | GĐ1 | GĐ2 | GĐ3 | Chỉ Brand+Generic | Benchmark (sheet 09) |
|---|---:|---:|---:|---:|---:|---|
| Lead → SQL | **25,46%** | 20,57% | 24,18% | **29,76%** | **37,60%** | tốt >30%, TB 18–30% |
| SQL → Đi xem | **31,64%** | 25,17% | 30,43% | **35,44%** | 34,44% | tốt >35%, TB 22–35% |
| Đi xem → Booking | 28,64% | 26,32% | 28,57% | 29,46% | 29,41% | — |
| Booking → Cọc | 30,51% | 20,00% | 31,25% | 33,33% | 32,73% | — |
| Đi xem → Cọc | 8,74% | 5,26% | 8,93% | 9,82% | 9,63% | tốt >12%, TB 7–12% |
| **Lead → Cọc** | **0,704%** | 0,272% | 0,657% | **1,036%** | 1,247% | — |
| **SQL → Cọc** | **2,76%** | 1,32% | 2,72% | **3,48%** | 3,31% | — |

Số tuyệt đối toàn kỳ: 2.557 lead → 651 SQL → 206 đi xem → 59 booking → 18 cọc.

**Ba điều bảng này nói ra:**
1. Mọi bước đều cải thiện đơn điệu qua 3 giai đoạn. Bước cải thiện mạnh nhất là Lead→SQL (+9,2 điểm %) và SQL→Đi xem (+10,3 điểm %) — cả hai đều là bước phụ thuộc **chất lượng lead và tốc độ sale**, khớp với sheet 08B.
2. Nút thắt lớn nhất về mặt số học là **Lead→SQL**: 74,5% lead bị loại ngay bước đầu. Nếu chỉ tính 2 chiến dịch Search, tỷ lệ này là 37,60% (vượt ngưỡng tốt của sheet 09). Nghĩa là nút thắt không phải do sale kém — mà do 4 chiến dịch còn lại bơm lead rác vào phễu.
3. Từ SQL trở đi, phễu chạy ổn: SQL→Đi xem 31,6% và Đi xem→Cọc 8,74% đều nằm trong dải trung bình ngành. **Vấn đề của tài khoản này nằm ở đầu phễu, không phải cuối phễu.**

## B4. Backsolve KPI: cần bao nhiêu SQL và bao nhiêu lead thô cho 32 cọc

Tôi đưa 3 kịch bản để BGĐ thấy độ nhạy của con số, chứ không đưa một số duy nhất giả vờ chắc chắn.

| Kịch bản (giả định tỷ lệ) | SQL→Cọc | Lead→SQL | **SQL cần** | **Lead thô cần** | CP/SQL trần | CPL trần |
|---|---:|---:|---:|---:|---:|---:|
| **A.** Tỷ lệ toàn kỳ 90 ngày | 2,76% | 25,46% | 1.157 | 4.546 | 1.815.000đ | 462.000đ |
| **B.** Tỷ lệ GĐ3 (gần nhất) | 3,48% | 29,76% | **919** | **3.089** | **2.285.000đ** | 680.000đ |
| **C.** Chỉ 2 CD Search (mix đề xuất) | 3,31% | 37,60% | 965 | **2.567** | 2.176.000đ | 818.000đ |

**Giả định tôi chọn và lý do:**

- **Tỷ lệ SQL→Cọc: 3,4%** — dùng GĐ3 (kịch bản B) chứ không dùng trung bình 90 ngày, vì GĐ1 chứa toàn bộ giai đoạn học máy chưa ổn định, trang đích v1 lỗi, chưa có SLA sale. Ba tháng tới sẽ khởi động từ trạng thái của GĐ3 chứ không phải GĐ1. **Rủi ro của giả định này:** GĐ3 có sự kiện mở bán đẩy tỷ lệ chốt lên; tôi bù rủi ro bằng cách không dùng số cao hơn.
- **Tỷ lệ Lead→SQL: 32%** — nằm giữa GĐ3 (29,76%) và mức của riêng 2 chiến dịch Search (37,60%). Lý do: kế hoạch 90 ngày tới cắt Competitor, thu nhỏ PMax và chặn từ khóa rác, nên mix lead sẽ dịch về phía Search — nhưng chưa thể đạt ngay 37,6% vì vẫn giữ một phần PMax/GDN. Không dùng 37,6% để tránh lạc quan quá.

**Kết quả với giả định đã chọn (SQL→Cọc 3,4%, Lead→SQL 32%):**

| Cần gì | Số lượng | Kiểm tra khả thi |
|---|---:|---|
| Cọc mục tiêu | 32 | KPI BGĐ |
| **SQL cần** | **941** | 10,5 SQL/ngày |
| **Lead thô cần** | **2.941** | **32,7 lead/ngày** — GĐ3 thực tế đã đạt 35,4 lead/ngày (sheet 08B) ⇒ **khả thi, không cần tăng lượng lead** |
| Năng lực sale | 8 × 12 = 96 lead/ngày × 90 = 8.640 | Chỉ dùng 34% năng lực ⇒ ràng buộc "không tăng sale" **không phải rào cản về số lượng**, rào cản là **tốc độ phản hồi** (A7) |
| **CP/SQL trần với 2,1 tỷ** | **2.232.000đ** | Cao hơn KPI được giao (2.200.000đ) đúng 1,5% ⇒ hai KPI này gần như trùng khít, không mâu thuẫn |
| CPL thô trần | 714.000đ | Sát CPL CRM hiện tại 705.333đ ⇒ không cần CPL rẻ hơn, cần lead **đúng hơn** |

**Kiểm tra ngược (quan trọng):** nếu tiêu hết 2,1 tỷ đúng ở mức CP/SQL trần 2.200.000đ, ta mua được **955 SQL**. Nhân với các tỷ lệ SQL→Cọc:

| Nếu SQL→Cọc bằng… | Số cọc thu được | Đạt KPI 32? |
|---|---:|:--:|
| 2,76% (toàn kỳ) | 26,4 | ✘ |
| **3,48% (GĐ3)** | **33,2** | ✔ |
| 3,31% (2 CD Search) | 31,6 | ~ (thiếu 0,4) |

**Kết luận B4:** KPI 32 cọc là **khả thi nhưng biên rất mỏng** — nó đòi hỏi giữ được tỷ lệ SQL→Cọc của GĐ3 (3,48%) trong suốt 90 ngày, tức là không được để tỷ lệ tụt về mức trung bình 90 ngày. Đòn bẩy an toàn nhất không nằm ở việc mua thêm lead (năng lực còn dư 66%) mà ở việc **nâng SQL→Cọc**, và đòn bẩy mạnh nhất cho việc đó là tốc độ phản hồi sale (A7: chênh 46 lần giữa <5 phút và >12 giờ).

## B5. Điểm hoà vốn với hoa hồng 181 triệu/cọc

| Câu hỏi | Phép tính | Kết quả |
|---|---|---:|
| **Chi phí QC tối đa/cọc để ROAS = 3,0x** | 181.000.000 / 3 | **60.333.333đ** |
| Chi phí QC tối đa/cọc để ROAS = 1,0x (hoà vốn thô) | 181.000.000 / 1 | 181.000.000đ |
| Lợi nhuận còn lại sau 45% sale + 20% vận hành | 181.000.000 × 35% | 63.350.000đ |
| **ROAS hoà vốn LỢI NHUẬN THẬT** | 1 / 0,35 | **2,86x** |
| Lãi thật/cọc khi đạt đúng ROAS 3,0x | 63.350.000 − 60.333.333 | 3.016.667đ |
| Số cọc tối thiểu để 2,1 tỷ đạt ROAS 3,0x | 2.100.000.000 × 3 / 181.000.000 | **34,8 → 35 cọc** |
| Ngân sách tối đa cho 32 cọc @ROAS 3,0x | 32 × 181.000.000 / 3 | 1.930.666.667đ |
| ROAS nếu tiêu hết 2,1 tỷ và đạt đúng 32 cọc | 32 × 181.000.000 / 2.100.000.000 | **2,76x** |
| **Thực tế 90 ngày qua** | 1.803.537.000 / 18 | **100.196.500đ/cọc = 1,66× ngưỡng** |

**Ba điểm phải báo BGĐ ngay:**
1. **Hai KPI được giao mâu thuẫn nhau về mặt số học.** "32 cọc" + "tiêu hết 2,1 tỷ" cho ROAS 2,76x, thấp hơn mục tiêu 3,0x. Muốn đủ cả hai điều kiện thì hoặc **35 cọc** với 2,1 tỷ, hoặc **32 cọc với ngân sách ≤ 1,931 tỷ** (dư 169.333.333đ). Tôi đề xuất phương án hai: **cam kết 34 cọc và chỉ tiêu 2,1 tỷ nếu chỉ số dẫn dắt cho phép**, có cơ chế dừng chi ở phần D.
2. ROAS 3,0x là ngưỡng có lãi **thật nhưng rất mỏng**: chỉ 3.016.667đ lãi/cọc sau khi trả 45% sale và 20% vận hành. Điểm hoà vốn lợi nhuận là 2,86x — dưới mức đó là lỗ.
3. Khoảng cách phải vượt: CP/cọc hiện tại 100.196.500đ phải xuống 60.333.333đ, tức **giảm 39,8%**. Phần A đã chỉ ra 865tr (48% ngân sách) đang đi vào 4 chiến dịch 0 cọc — chỉ riêng việc phân bổ lại số tiền này đã đủ tạo ra mức giảm cần thiết, chưa cần tối ưu gì thêm.

## B6. Đối chiếu ba nguồn số liệu — bóc tách từng thành phần

**Nguồn:** sheet 10_GA4 mục A và mục E (số sự kiện), sheet 12_GTM mục B (lịch sử phiên bản), sheet 02 (kiểm chứng theo ngày).

### Bước 1 — Cột "Chuyển đổi" của Google Ads được cấu thành từ gì

| Sự kiện | Số lượt | % | Là khách hàng tiềm năng? |
|---|---:|---:|---|
| generate_lead | 1.715 | 44,9% | ✔ Có |
| click_to_call (tổng **lượt**) | 1.132 | 29,6% | Có, nhưng chưa khử trùng |
| view_price_page | 612 | 16,0% | ✘ Không |
| engaged_30s | 361 | 9,5% | ✘ Không |
| **Cộng** | **3.820** | 100% | |

1.715 + 1.132 + 612 + 361 = **3.820** ✔ (khớp con số Google Ads báo)

### Bước 2 — Bóc tách khoảng chênh 3.820 → 2.557

| # | Thành phần | Số lượng | Nguyên nhân kỹ thuật (nguồn) |
|---|---|---:|---|
| — | Xuất phát: Ads/GA4 báo | **3.820** | GA4 nhập trực tiếp vào Ads nên hai con số luôn bằng nhau (sheet 10A) |
| 1 | **− Đếm trùng lượt gọi** | **−353** | click_to_call 1.132 **lượt** nhưng chỉ 779 **người**. Thẻ GTM #4 "Đếm mọi lượt nhấp, không khử trùng theo người dùng" (sheet 12A) |
| 2 | **− Sự kiện rác (không phải lead)** | **−973** | view_price_page 612 + engaged_30s 361, cả hai bị đánh dấu sự kiện chính và nhập vào Ads (sheet 12A #5, #6, #8) |
| = | **Lead thật ĐO ĐƯỢC bằng thẻ** | **2.494** | = 1.715 form + 779 người gọi duy nhất ✔ (khớp sheet 10A) |
| 3 | **+ Lead MẤT do gãy thẻ** | **+63** | GTM v23 (ngày 44, 09:12, dev@) đổi class `.form-dk-v1` → `.form-register`, điều kiện kích hoạt generate_lead ngừng khớp trong 3 ngày N44–46. Sửa ở v24 ngày 47 nhưng 63 lead không hồi tố được |
| = | **CRM — lead thật đã khử trùng** | **2.557** | ✔ khớp sheet 02 và sheet 03 |

### Bước 3 — Chứng minh phép cộng khớp

```
3.820 − 353 − 973 + 63 = 2.557   ✔
```
Kiểm tra chéo hai chiều bằng script (`agent-6-calc.py`, mục B6): cả hai điểm neo trung gian đều khớp — 3.820 − 353 − 973 = **2.494** = đúng dòng "Lead thật đo được bằng thẻ" của sheet 10A; và 2.494 + 63 = **2.557** = đúng Σ`Lead_CRM` của sheet 02.

### Bước 4 — Kiểm chứng độc lập sự cố N44–46 trên dữ liệu ngày (sheet 02)

| Ngày thứ | ChuyenDoi_Ads | Lead_CRM | Chi phí | Ghi chú |
|---:|---:|---:|---:|---|
| 43 | 43 | 30 | 19.700.000đ | bình thường |
| **44** | **0** | **17** | 20.200.000đ | GTM v23 xuất bản 09:12 |
| **45** | **0** | **15** | 19.700.000đ | không ai phát hiện |
| **46** | **0** | **31** | 19.600.000đ | không ai phát hiện |
| 47 | 33 | 18 | 19.900.000đ | GTM v24 sửa lúc 14:38 |
| 48 | 36 | 26 | 19.600.000đ | bình thường |
| **Tổng N44–46** | **0** | **63** | **59.500.000đ** | |

Sheet 02 xác nhận độc lập: `ChuyenDoi_Ads` = 0 chính xác 3 ngày, `Lead_CRM` = 17+15+31 = **63** — đúng bằng con số chênh lệch mà sheet 10A ghi "Lead ngày 44, 45, 46".

### Tóm tắt mức độ thổi phồng

| Cách nhìn | Con số |
|---|---:|
| Ads báo cao hơn CRM | +1.263 chuyển đổi = **+49,4%** |
| Hệ số Ads/CRM toàn tài khoản | **1,49** (sheet 09: 1,2–1,5 = "trung bình ngành") |
| Riêng PMax | 1.775/829 = **2,14** (>1,8 = **BÁO ĐỘNG**) |
| Riêng YouTube | 3,00 (**BÁO ĐỘNG**) |
| Riêng Brand | 1,02 (ngưỡng tốt) |
| Tỷ trọng tín hiệu sai trong cột Chuyển đổi | (353+973)/3.820 = **34,7%** |

Con số 1,49 ở cấp tài khoản trông "bình thường" và đó chính là cái bẫy — nó là trung bình cộng giữa Brand rất sạch (1,02) và PMax/YouTube rất bẩn (2,14 / 3,00). **Không bao giờ đánh giá chỉ số này ở cấp tài khoản.**

## B7. Ước tính lead mất do lỗi kỹ thuật CHƯA SỬA và quy ra tiền

Tôi tách rõ ba tầng: **số đo được**, **ước tính của đội UX (có sẵn trong file)**, và **suy luận của tôi**.

### Tầng 1 — SỐ ĐO ĐƯỢC (Clarity ghi hình, mẫu ~92% lưu lượng, sheet 11C)

| # | Lỗi | Phiên ảnh hưởng | Bằng chứng bổ sung |
|---|---|---:|---|
| 4 | `TypeError: e.setDate is not a function` — bộ chọn ngày hẹn xem nhà, Safari iOS 17.x, form không gửi được và **không báo lỗi cho khách** | **4.196** | Sheet 11A: tỷ lệ lỗi JS mobile 9,3% (v1) → 8,9% (v2), **không giảm** sau khi lên LP mới |
| 5 | Nút "Đăng ký nhận bảng giá" bị khung chat che trên màn hình <380px | **2.741** | — |
| 6 | Hotline `tel:` không phản hồi trên desktop — **1.847 nhấp chết** | **1.204** | Sheet 07B: desktop là thiết bị chuyển đổi tốt nhất (4,02%) |
| | **Tổng phiên bị ảnh hưởng** | **8.141** | |

### Tầng 2 — ƯỚC TÍNH CÓ SẴN TRONG FILE (do đội UX đưa ra, sheet 11C, dựa trên tỷ lệ hoàn tất form của nhóm phiên không gặp lỗi — **không phải số đo trực tiếp**)

| # | Lead mất (thấp) | Lead mất (cao) | Giữa dải |
|---|---:|---:|---:|
| 4 | 280 | 340 | 310 |
| 5 | 60 | 90 | 75 |
| 6 | 30 | 50 | 40 |
| **Tổng** | **370** | **480** | **425** |

### Tầng 3 — SUY LUẬN CỦA TÔI: quy ra tiền

Hai cách quy, dùng đúng CPL thực tế đo được ở B1 (CPL CRM = **705.333đ**):

**Cách 1 — theo chi phí quảng cáo đã trả nhưng không thu được lead:**

| Kịch bản | Lead mất | × CPL CRM 705.333đ |
|---|---:|---:|
| Thấp | 370 | **260.973.285đ** |
| Giữa | 425 | 299.766.611đ |
| Cao | 480 | **338.559.937đ** |

**Cách 2 — theo doanh thu hoa hồng bỏ lỡ** (dùng tỷ lệ chuyển đổi toàn kỳ đo được ở B3: Lead→SQL 25,46%, SQL→Cọc 2,76%, hoa hồng 181.000.000đ/cọc):

| Kịch bản | Lead mất | → SQL | → Cọc | → Doanh thu HH |
|---|---:|---:|---:|---:|
| Thấp | 370 | 94 | 2,6 | **471.435.276đ** |
| Giữa | 425 | 108 | 3,0 | 541.513.492đ |
| Cao | 480 | 122 | 3,4 | **611.591.709đ** |

**Cộng thêm khoản đo được chắc chắn (không phải ước tính):** 63 lead mất do gãy thẻ GTM v23 = 44.435.992đ theo CPL, tương đương 0,44 cọc = 80.271.000đ doanh thu.

### Kết luận B7

| Loại số | Giá trị |
|---|---|
| **ĐO ĐƯỢC** | 8.141 phiên gặp 3 lỗi chưa sửa; 1.847 nhấp chết trên hotline; 63 lead mất do gãy thẻ; CPL CRM thực tế 705.333đ |
| **ƯỚC TÍNH CÓ TRONG FILE (đội UX)** | 370–480 lead mất |
| **SUY LUẬN CỦA TÔI** | Chi phí đã trả không thu được lead: **261 – 339 triệu**. Doanh thu hoa hồng bỏ lỡ: **471 – 612 triệu**. Con số dùng để trình BGĐ: **≈ 540 triệu** (giữa dải) |
| **Độ tin cậy** | Trung bình. Ước tính 370–480 dựa trên giả định "phiên gặp lỗi sẽ chuyển đổi bằng phiên không gặp lỗi" — giả định này thường **lạc quan** vì nhóm gặp lỗi có thể vốn đã ít ý định hơn. Chi phí sửa cả 3 lỗi ước chừng 1–2 ngày công dev, nên kể cả nếu con số thật chỉ bằng 1/3 ước tính thì ROI của việc sửa vẫn trên 100 lần. |
| **Cần thêm dữ liệu gì** | Bản ghi Clarity lọc theo `Phiên có lỗi JavaScript = có` × `đã có generate_lead`, và tỷ lệ hoàn tất form của nhóm Safari iOS 17.x so với nhóm trình duyệt khác — hai số này biến ước tính thành số đo. |
