# BÁO CÁO TIẾP QUẢN TÀI KHOẢN GOOGLE ADS — VINHOMES HÓC MÔN
**Người thực hiện:** Performance Marketing Lead, An Phát Land
**Kỳ dữ liệu:** 02/03/2026 – 30/05/2026 (90 ngày) · **Ngân sách đã tiêu:** 1.803.537.000đ · **Cọc:** 18 · **ROAS:** 1,74x

> **Nguồn số:** mọi con số trong báo cáo này được tính bằng `answers/agent-3-calc.py` (chạy trên `du_lieu_google_ads_90_ngay_1.csv` = sheet `02_DU_LIEU_NGAY`, cùng các sheet 04/05/06/07/08/09/10/11/12). Output đầy đủ: `answers/agent-3-calc-output.txt`. Không có số nào tính tay.

---

## TÓM TẮT ĐIỀU HÀNH (đọc 60 giây)

| Chỉ số 90 ngày qua | Thực tế | KPI 90 ngày tới | Khoảng cách |
|---|---|---|---|
| Chi phí | 1.803.537.000đ | ≤ 2.100.000.000đ | +16,4% dư địa |
| Đặt cọc | 18 | ≥ 32 | **cần +78%** |
| ROAS | 1,74x | ≥ 3,0x | **cần +73%** |
| CP/SQL | 2.770.410đ | ≤ 2.200.000đ | **cần −20,6%** |
| CP/cọc | 100.196.500đ | ≤ 60.333.333đ (trần ROAS 3x) | **đang gấp 1,66 lần trần** |

**Ba câu kết luận:**
1. **Tài khoản không hỏng ở phần "mua traffic", hỏng ở phần "đo cái gì là chuyển đổi".** 34,7% cột `Chuyển đổi` (1.326/3.820) không phải lead — máy học đã tối ưu theo tín hiệu rác suốt 90 ngày (sheet 10A + 12A).
2. **38,2% ngân sách (688.578.000đ) nằm ở 3 chiến dịch tạo 0 cọc, 0 doanh thu** (PMax, GDN, YouTube — sheet 02). Trong khi chiến dịch tạo 72,8% doanh thu (Brand, ROAS 8,76x) đang **mất 40,06% impression share vì thiếu ngân sách**.
3. **Điểm rò rỉ lớn nhất không nằm trong Google Ads mà nằm ở tốc độ gọi lại lead**: 47% lead được gọi sau 2 giờ, ước tính bỏ lỡ ~19,7 cọc ≈ **3,56 tỷ hoa hồng** (sheet 08A).

---

# PHẦN A — CHẨN ĐOÁN

15 vấn đề, sắp theo tác động tài chính giảm dần. Nhóm đo lường/kỹ thuật: **#3, #11, #12, #13** (4 vấn đề, vượt yêu cầu tối thiểu 3).

---

### A1. Tốc độ phản hồi lead — rò rỉ lớn nhất toàn hệ thống
**Mức độ: CAO — ước tính bỏ lỡ ≈ 19,7 cọc ≈ 3.564.027.560đ hoa hồng**

| Thời gian gọi lần đầu | Số lead | % tổng | Tỷ lệ liên hệ được | Tỷ lệ đặt cọc |
|---|---|---|---|---|
| Dưới 5 phút | 281 | 11% | 87% | 1,82% |
| 5–30 phút | 485 | 19% | 74% | 1,21% |
| 30 phút – 2 giờ | 588 | 23% | 58% | 0,58% |
| 2–12 giờ | 536 | 21% | 41% | 0,21% |
| Trên 12 giờ | 664 | 26% | 22% | 0,04% |

- **Phát hiện:** 47% lead (1.200/2.554) được gọi lại **sau 2 giờ** — vượt ngưỡng báo động của sheet `09_BENCHMARK` (>2 giờ = báo động). Tỷ lệ cọc của nhóm này (0,21% và 0,04%) thấp hơn nhóm <5 phút **8,7 lần đến 45,5 lần**.
- **Bằng chứng số:** sheet `08_CRM_VAN_HANH` mục A. Cọc kỳ vọng theo phân bố hiện tại = 15,8. Nếu chuyển sang phân bố thực tế đạt được (50% <5', 30% 5–30', 20% 30'–2h) → cọc kỳ vọng **35,5** → **+19,7 cọc × 181.000.000đ = 3.564.027.560đ**. Kịch bản trần (100% <5 phút) = +30,7 cọc = 5.556.428.500đ.
- **Cộng thêm:** 275 lead **không ai gọi** (118 GĐ1 + 96 GĐ2 + 61 GĐ3, sheet 08B) = 193.966.631đ tiền quảng cáo mua lead rồi vứt = ~1,9 cọc = 350.391.083đ hoa hồng.
- **Ghi chú thẳng thắn:** đây là vấn đề vận hành sale, không phải Google Ads. Nhưng nó là **ràng buộc cứng** của mọi kế hoạch tăng lead — bơm thêm lead vào một phễu gọi chậm chỉ làm tăng CPL, không tăng cọc.

---

### A2. Chiến dịch Brand — cỗ máy sinh lời duy nhất nhưng đang bị bóp ngân sách
**Mức độ: CAO — doanh thu bỏ lỡ ước tính ≈ 1.524.054.416đ**

| Giai đoạn | Chi phí | Impression Share | Mất IS do ngân sách | Cọc | ROAS |
|---|---|---|---|---|---|
| GĐ1 | 57.619.000đ | 54,11% | 39,14% | 2 | 5,73x |
| GĐ2 | 72.302.000đ | 48,90% | 43,78% | 3 | 7,19x |
| GĐ3 | 130.298.000đ | 54,79% | 38,41% | 8 | 10,97x |
| **Toàn kỳ** | **260.219.000đ** | **53,01%** | **40,06%** | **13** | **8,76x** |

- **Phát hiện:** Brand chiếm **14,4% chi phí** nhưng tạo **72,8% doanh thu** (2.280.000.000đ/3.130.000.000đ) và **13/18 cọc**. IS 53,01% — dưới ngưỡng báo động 60% của sheet `09_BENCHMARK`. 40,06% impression bị mất **thuần túy vì hết ngân sách**, không phải vì thứ hạng (chỉ mất 6,93% do thứ hạng).
- **Bằng chứng số:** sheet 02, cột `Impr_Share`, `Mat_IS_NganSach`, bình quân có trọng số chi phí, 90 ngày. Benchmark sheet 09: "Mất IS do ngân sách (chiến dịch tốt) > 20% = tiền đang bỏ lại trên bàn" — Brand đang ở **gấp đôi ngưỡng đó**.
- **Ước tính tài chính:** bù đủ IS → hiển thị ×1,67 → cọc thêm ≈ 8,7 → doanh thu thêm ≈ **1.524.054.416đ** với chi phí thêm chỉ ≈ 173.942.068đ (ROAS biên ≈ 8,76x).
- **Giả định cần nói rõ:** ước tính này giả định lead/cọc tăng **tuyến tính** theo impression share. Thực tế impression biên thường có ý định thấp hơn nên con số thật sẽ thấp hơn. Đây là **cận trên**. Cần thêm dữ liệu: báo cáo "Chẩn đoán từ khóa" / Auction Insights để biết impression biên đến từ truy vấn nào.

---

### A3. ĐO LƯỜNG — 4 hành động chuyển đổi, 2 trong đó không phải lead
**Mức độ: CAO — đây là NGUYÊN NHÂN GỐC lái sai 688.578.000đ ngân sách**

| Sự kiện nhập vào cột `Chuyển đổi` | Số lượt | Có phải khách hàng tiềm năng? |
|---|---|---|
| generate_lead | 1.715 | Có |
| click_to_call (tổng lượt) | 1.132 | Có, nhưng **đếm trùng 353 lượt** |
| view_price_page | 612 | **KHÔNG** |
| engaged_30s | 361 | **KHÔNG** |
| **TỔNG** | **3.820** | — |

- **Phát hiện:** cả 4 sự kiện đều đang được đánh dấu "sự kiện chính" trong GA4 và nhập vào Google Ads (sheet `12_GTM` mục A, thẻ #5, #6, #8; sheet `05_CAU_HINH_TK` mục "Hành động tính vào cột Chuyển đổi" #3, #4). Từ **GTM v18 — trước ngày 1** (sheet 12B): "Chuyển đổi bị thổi phồng ngay từ ngày đầu tiên".
- **Bằng chứng số:** 612 + 361 = **973 sự kiện rác** = **25,5%** cột Chuyển đổi; cộng 353 lượt gọi trùng = **1.326 = 34,7%**. Sheet `12_GTM` mục C: "Máy học tối ưu theo tín hiệu rác — **nguyên nhân gốc của toàn bộ vấn đề PMax**".
- **Hậu quả định lượng được:** 973 sự kiện rác phân bổ theo chiến dịch (sheet 10B) — PMax 438+259 = **697 (71,6% toàn bộ sự kiện rác)**, YouTube 113, GDN 80, Generic 60, Brand 23. Nghĩa là bidding tự động của PMax được "khen" chủ yếu bằng tín hiệu không phải lead → nó đi mua thêm đúng loại traffic đó. **688.578.000đ (38,2% ngân sách) chảy vào 3 chiến dịch tự động tối ưu theo tín hiệu rác và tạo 0 cọc.**

---

### A4. PMax — 26,4% ngân sách, 0 cọc, lead 93% không dùng được
**Mức độ: CAO — 475.376.000đ chi phí, 0đ doanh thu**

| Chỉ số | PMAX_VinhomesHM_Lead | Ngưỡng benchmark (sheet 09) |
|---|---|---|
| Chi phí | 475.376.000đ (26,4% TK) | — |
| Chuyển đổi Ads | 1.775 | — |
| Lead CRM | 829 | — |
| SQL | 61 | — |
| Cọc / Doanh thu | **0 / 0đ** | — |
| Chênh Ads/CRM | **2,14x** | > 1,8x = báo động |
| SQL/lead | **7,36%** | < 12% = nhắm sai tệp |
| CP/SQL | **7.793.049đ** | > 5.000.000đ = báo động |
| Thoát nhanh <3s (Clarity) | **74,3%** | — |
| Thời lượng phiên trung vị | **3 giây** | — |
| Tỷ lệ tương tác (GA4) | **8,7%** | TB tài khoản 32,4% |
| Hao hụt nhấp→phiên | **28,0%** | Sheet 10B ghi rõ: "Với PMax thì không [bình thường]" |

- **Bằng chứng chất lượng lead** (sheet `08_CRM_VAN_HANH` mục C, mẫu 160 lead PMax): trùng SĐT **31%**, SĐT sai/không liên lạc được **24%**, sai phân khúc (<2 tỷ) **34%**, môi giới 4% → **chỉ 7% dùng được**. Ước tính lead dùng được thật = 829 × 7% = **58 lead** → **chi phí thực trên 1 lead dùng được = 8.191.901đ**.
- **Ba nguồn số liệu cùng chỉ một hướng:** Ads nói PMax rẻ nhất (267.817đ/chuyển đổi), GA4 nói phiên PMax gần như không tương tác (8,7%), Clarity nói 74,3% thoát dưới 3 giây và ghi thẳng "Bất thường — xem lại vị trí đặt quảng cáo". Sheet `05_CAU_HINH_TK`: PMax **chưa thiết lập danh sách loại trừ vị trí đặt** và **chưa bật brand exclusion**.
- **Diễn giải:** hồ sơ này (hao hụt nhấp 28%, phiên 3 giây, 31% trùng SĐT) là dấu hiệu kinh điển của lưu lượng từ **mạng hiển thị/ứng dụng chất lượng thấp** trong PMax, cộng với **không có reCAPTCHA/OTP** trên form (sheet 05).

---

### A5. Lỗi kỹ thuật trang đích CHƯA SỬA
**Mức độ: CAO — 370–480 lead ≈ 2,6–3,4 cọc ≈ 471.435.276đ – 611.591.709đ hoa hồng**

| # | Điểm ma sát | Phiên ảnh hưởng | Lead mất (ước tính) | Trạng thái |
|---|---|---|---|---|
| 4 | Lỗi JS `TypeError e.setDate is not a function` (bộ chọn ngày), Safari iOS 17.x — **form không gửi được, không báo lỗi cho khách** | 4.196 | 280–340 | **CHƯA SỬA** |
| 5 | Nút "Đăng ký nhận bảng giá" bị khung chat che trên màn hình <380px | 2.741 | 60–90 | **CHƯA SỬA** |
| 6 | Số hotline `tel:` không phản hồi trên máy tính — 1.847 nhấp chết | 1.204 | 30–50 | **CHƯA SỬA** |

- **Bằng chứng số:** sheet `11_CLARITY` mục C. Xác nhận chéo: tỷ lệ lỗi JavaScript trên di động **không giảm** sau khi lên trang đích v2 (9,3% → 8,9%) — chứng minh lỗi #4 tồn tại ở **cả v1 và v2**, tức vẫn đang chảy máu ở thời điểm bàn giao.
- **Quy tiền:** 370–480 lead × CPL CRM thực tế 705.333đ = **260.973.285đ – 338.559.937đ tiền quảng cáo đã trả nhưng không nhận được lead**; quy tiếp ra hoa hồng bỏ lỡ = 471.435.276đ – 611.591.709đ.

---

### A6. Trang đích v1 chạy 57/90 ngày với LCP 4,8s và form 7 trường
**Mức độ: CAO — ước tính mất ≈ 374 lead ≈ 2,6 cọc ≈ 476.010.573đ**

| | v1 (N1–57) | v2 (N58–90) | Chênh |
|---|---|---|---|
| Phiên | 52.410 | 42.938 | — |
| Tỷ lệ tương tác | 34,2% | 58,7% | **+71,6%** |
| Thời gian tương tác TB | 52s | 121s | +132,7% |
| Cuộn 90% | 16% | 37% | +131,3% |
| Tỷ lệ hoàn tất form | 20,4% | **28,0%** | **+37,3%** |
| LCP | **4,8s** | 1,9s | — |

- **Bằng chứng số:** sheet `10_GA4` mục C. LCP 4,8s vượt ngưỡng báo động >4s của sheet 09.
- **Ước tính:** nếu v1 đạt tỷ lệ hoàn tất form của v2 → 4.912 form_start × 28,0% = **1.376 lead** thay vì 1.002 thực tế → **mất 374 lead** = 263.506.041đ tiền quảng cáo = ~2,6 cọc = **476.010.573đ hoa hồng**.
- **Nguyên nhân cụ thể đã được Clarity chỉ ra** (sheet 11C, đã sửa ở v2): trường "Số CMND/CCCD" ở vị trí 4/7 khiến **61% phiên bỏ dở ngay tại đó** (2.987 phiên, ≈320–400 lead); dropdown "Ngân sách đầu tư" 9 lựa chọn khiến 27% bỏ dở; ảnh "Xem bảng giá chi tiết" giả nút bấm — 8.412 nhấp chết.
- **Chênh lệch thiết bị:** v1 trên di động chỉ hoàn tất form **16,1%** vs máy tính 34,8% — trong khi di động chiếm **78,1% chi phí** (sheet 07B).

---

### A7. Đối sánh rộng + chỉ 12 từ khóa phủ định
**Mức độ: CAO — 419.729.000đ (23,3% ngân sách) chi cho cụm từ tạo 0 SQL**

- **Phát hiện:** sheet `05_CAU_HINH_TK`: đối sánh rộng = **71% chi phí Search** (≈791.620.890đ), đối sánh chính xác chỉ 9%; **12 từ phủ định** trong toàn tài khoản, **không dùng danh sách phủ định chia sẻ**.
- **Bằng chứng số:** sheet `04_SEARCH_TERMS` — trong 32 cụm từ báo cáo, **17 cụm tạo 0 SQL, tiêu 419.729.000đ**. Top lãng phí:

| Cụm từ | Đối sánh | Chi phí | Lead | SQL |
|---|---|---|---|---|
| vạn phúc city giá bán | Cụm từ | 40.652.000đ | 7 | 0 |
| the global city | Cụm từ | 38.884.000đ | 6 | 0 |
| giá đất hóc môn 2026 | Rộng | 33.900.000đ | 29 | 0 |
| izumi city đồng nai | Rộng | 33.582.000đ | 6 | 0 |
| bản đồ quy hoạch hóc môn | Rộng | 27.120.000đ | 6 | 0 |
| thuê nhà nguyên căn hóc môn | Rộng | 27.120.000đ | 6 | 0 |
| bán đất thổ cư hóc môn 100 triệu | Rộng | 27.120.000đ | 6 | 0 |
| nhà trọ hóc môn giá rẻ | Rộng | 20.340.000đ | 4 | 0 |
| cho thuê kho xưởng hóc môn | Rộng | 20.340.000đ | 4 | 0 |
| việc làm bất động sản hóc môn | Rộng | 20.340.000đ | 4 | 0 |

- **Nhóm "sai ý định 100%"** (tuyển dụng / thuê / trọ / kho xưởng / việc làm / quy hoạch / lừa đảo / chung cư mini / đất 100 triệu): **10 cụm, 209.082.000đ** — có thể chặn ngay bằng danh sách phủ định mà **không mất một SQL nào**.
- Ngay cả trong chiến dịch Brand cũng có rác: `vinhomes hóc môn tuyển dụng` 15.613.000đ (0 SQL) và `vinschool hóc môn học phí` 10.409.000đ (0 SQL) = 26.022.000đ.

---

### A8. Nhắm mục tiêu toàn quốc + "Hiện diện HOẶC quan tâm"
**Mức độ: CAO — 364.314.474đ (20,2% ngân sách) ở khu vực tạo 0 cọc**

| Khu vực | Chi phí | Lead | SQL | Cọc | CP/SQL |
|---|---|---|---|---|---|
| Hà Nội | 155.104.182đ | 186 | 20 | **0** | 7.755.209đ |
| Cần Thơ & ĐBSCL | 93.783.924đ | 113 | 12 | **0** | 7.815.327đ |
| Đà Nẵng | 86.569.776đ | 104 | 7 | **0** | 12.367.111đ |
| Ngoài Việt Nam "quan tâm đến VN" | 28.856.592đ | 34 | 7 | **0** | 4.122.370đ |
| **Cộng 4 khu vực** | **364.314.474đ** | **437** | **46** | **0** | — |
| *So sánh:* lõi TP.HCM | 1.076.711.589đ | — | 482 | **17** | **2.233.841đ** |

- **Bằng chứng số:** sheet `06_DIA_LY`. CP/SQL Đà Nẵng cao gấp **5,5 lần** lõi TP.HCM. Sheet `05_CAU_HINH_TK`: vị trí = "Việt Nam (toàn quốc)", tùy chọn "Hiện diện HOẶC quan tâm (mặc định) — chưa từng chỉnh", **không có loại trừ vị trí nào**.
- **Đối chiếu với sheet 01:** khách hàng mục tiêu được định nghĩa là Q.12/Gò Vấp/Hóc Môn/Củ Chi/Bình Tân/Tân Phú + nhà đầu tư TP.HCM/Bình Dương/Long An. Hà Nội, Đà Nẵng, Cần Thơ **không nằm trong định nghĩa nào**.
- **Lưu ý dữ liệu:** tổng lead sheet 06 = 2.566 vs sheet 02 = 2.557 (lệch 9, do sheet 06 phân bổ theo % chi phí làm tròn). Dùng sheet 02 làm chuẩn; kết luận không đổi.

---

### A9. Chiến dịch Competitor — 176.746.000đ, 0 cọc, 26% lead là môi giới/đối thủ
**Mức độ: CAO — 176.746.000đ chi phí, 0đ doanh thu**

| Chỉ số | Giá trị | Benchmark sheet 09 |
|---|---|---|
| Chi phí | 176.746.000đ (9,8% TK) | — |
| Lead CRM / SQL / Cọc | 32 / **3** / **0** | — |
| CP/SQL | **58.915.333đ** | > 5.000.000đ = báo động (gấp 11,8 lần) |
| CPC trung bình | 55.164đ | 25.000–45.000đ TB; >60.000đ báo động |
| CTR | 2,39% | Từ khóa chung: <2% báo động, 3–5% TB |

- **Bằng chứng số:** sheet 02 + sheet `04_SEARCH_TERMS` (6 cụm từ đối thủ, **cả 6 đều 0 SQL**, tổng 176.747.000đ). Sheet `08_CRM_VAN_HANH` mục C: mẫu 40 lead → **26% là môi giới/đối thủ**, 31% sai phân khúc, **chỉ 26% dùng được**.
- Chiến dịch dùng "Tối đa hóa số lần nhấp, không đặt trần CPC" (sheet 05) → mua nhấp giá 55.164đ trên truy vấn của đối thủ mà không có ràng buộc nào.

---

### A10. GDN Remarketing + YouTube — 213.202.000đ, 0 cọc
**Mức độ: TRUNG BÌNH — 213.202.000đ chi phí, 0đ doanh thu (nhưng có giá trị hỗ trợ)**

| Chiến dịch | Chi phí | Lead | SQL | Cọc | CP/SQL | Thoát <3s (Clarity) |
|---|---|---|---|---|---|---|
| GDN_Remarketing_Web30d | 130.009.000đ | 193 | 36 | 0 | 3.611.361đ | 39,7% |
| YT_Video_TVC_MoBan | 83.193.000đ | 59 | 8 | 0 | 10.399.125đ | 48,1% |

- **Sắc thái quan trọng — không được cắt mù:** sheet `10_GA4` mục D cho thấy dưới mô hình **Dựa trên dữ liệu**, YouTube được ghi công **165 lead thay vì 43 (+283,7%)** và GDN **186 thay vì 132 (+40,9%)**. Đánh giá 2 kênh này bằng nhấp cuối là **sai phương pháp**.
- Nhưng ngay cả sau điều chỉnh, cả hai vẫn **0 cọc / 0 doanh thu** trong 90 ngày. GDN CPC chỉ 4.487đ và YouTube 1.199đ — rẻ, nhưng SQL/lead GDN 18,65% và YT 13,56% đều dưới ngưỡng "tốt" 30%.
- YouTube chỉ chạy từ GĐ2 (GĐ1 = 0đ), 59.409 nhấp trong GĐ3 → chưa đủ chu kỳ để kết luận về đóng góp cọc. **Không đủ dữ liệu** để khẳng định YouTube vô giá trị; cần đo bằng brand lift / assisted conversion, không bằng cọc nhấp cuối.

---

### A11. ĐO LƯỜNG — GTM v23 làm gãy `generate_lead` 3 ngày, không ai biết
**Mức độ: CAO — 63 lead mất khỏi hệ thống đo, ≈ 80.271.412đ hoa hồng + hỏng dữ liệu huấn luyện**

| Ngày | Chuyển đổi Ads | Lead CRM | Chi phí |
|---|---|---|---|
| N43 | 43 | 30 | 19.744.000đ |
| **N44** | **0** | 17 | 20.249.000đ |
| **N45** | **0** | 15 | 19.699.000đ |
| **N46** | **0** | 31 | 19.580.000đ |
| N47 | 33 | 18 | 19.912.000đ |
| N48 | 36 | 26 | 19.627.000đ |
| **N44–46** | **0** | **63** | **59.528.000đ** |

- **Nguyên nhân (sheet `12_GTM` mục B):** v23 xuất bản **ngày 44, 09:12, bởi dev@** — đổi class `.form-dk-v1` → `.form-register` khi triển khai form v2. Điều kiện kích hoạt `generate_lead` dựa trên class CSS nên **ngừng khớp**. v24 (ngày 47, 14:38) sửa lại. **63 lead của 3 ngày đó vĩnh viễn không có trong Google Ads/GA4.**
- **Hai lỗi hệ thống, không phải một sự cố:** (1) điều kiện kích hoạt phụ thuộc class CSS — sheet 12A ghi "rất dễ vỡ khi dev đổi giao diện"; (2) **không có cảnh báo khi chuyển đổi = 0** (sheet 12A mục 18) → "Nguyên nhân khiến sự cố N44–46 mất 3 ngày mới bị phát hiện".
- **Thiệt hại kép:** 59.528.000đ ngân sách chạy 3 ngày mà bidding tự động nhận tín hiệu "0 chuyển đổi" → nó tự giảm giá thầu / học sai. Cộng 63 lead × 25,46% × 2,76% = 0,44 cọc = 80.271.412đ.

---

### A12. ĐO LƯỜNG — thẻ GA4 trùng lặp, 34 thẻ, 412KB JS làm chậm chính trang đích
**Mức độ: TRUNG BÌNH — làm hỏng dữ liệu ra quyết định + ~0,8s LCP**

- **Bằng chứng số (sheet `12_GTM`):** vùng chứa GTM-KP7X2QM có **34 thẻ, 21 điều kiện kích hoạt, 18 biến, 412 KB JavaScript bên thứ ba, ước tính làm chậm LCP thêm ~0,8 giây**.
- Thẻ #2 `GA4 Configuration – Copy of Main` — **TRÙNG LẶP, page_view bị bắn hai lần**, phát sinh từ **v22 ngày 31** (sheet 12B). Hệ quả: "Số phiên và tỷ lệ thoát bị sai lệch từ ngày 31" → **mọi so sánh trước/sau ngày 31 trong GA4 đều không tin được**, bao gồm cả so sánh trang đích v1/v2 (v2 bắt đầu ngày 58).
- Thẻ #12 `Zalo Tracking` — "Không rõ ai cài, không có mô tả"; thẻ #13 `Thẻ đối tác sàn F2 (3 thẻ)` — "Không rõ nguồn gốc — cần rà soát bảo mật", thêm ~0,3s LCP (v20, ngày 18). **Rủi ro bảo mật/PDPD chưa được đánh giá.**
- **Nghịch lý:** đội vừa bỏ công tối ưu LCP từ 4,8s → 1,9s ở trang đích v2, trong khi GTM đang tự cộng ngược 0,8s vào chính trang đó.
- **Tín hiệu ý định đang bị vứt (sheet 10E):** `zalo_click` **894 lượt** và `file_download` (bảng giá PDF) **1.206 lượt** — có dữ liệu từ v26 (ngày 71) nhưng **chưa đánh dấu sự kiện chính, chưa nhập vào Ads**. Với thị trường VN, Zalo là kênh liên hệ chính — đây là 894 tín hiệu ý định cao đang bị bỏ.

---

### A13. ĐO LƯỜNG — không có GCLID trong CRM ⇒ không thể tối ưu theo chất lượng lead
**Mức độ: CAO — chặn đứng con đường duy nhất để hạ CP/SQL bằng máy học**

| Hạng mục (sheet `12_GTM` mục A + C, sheet `05`) | Trạng thái | Hệ quả |
|---|---|---|
| Biến ẩn lưu GCLID vào form | **CHƯA CÀI** | Không thể nhập chuyển đổi ngoại tuyến |
| Nhập chuyển đổi ngoại tuyến từ CRM | **CHƯA triển khai** | Không thể tối ưu theo SQL/cọc |
| Enhanced Conversions | **CHƯA CÀI / TẮT** | Mất 10–20% khả năng khớp chuyển đổi |
| Consent Mode v2 | **CHƯA CẤU HÌNH** | Rủi ro mất dữ liệu mô hình hoá |
| Vùng chứa phía máy chủ | **KHÔNG CÓ** | Phụ thuộc hoàn toàn trình duyệt + ad blocker |
| Gắn ID phiên Clarity vào CRM | **KHÔNG ĐẠT** | Không xem lại được hành trình lead đã cọc |
| Mô hình phân bổ | Nhấp cuối | Xem A14 |

- **Tại sao đây là vấn đề CAO chứ không phải "kỹ thuật vặt":** toàn bộ tài khoản đang tối ưu về **lead thô** (và 25,5% trong đó còn là rác). Chênh CP/SQL giữa Brand (739.259đ) và PMax (7.793.049đ) là **10,5 lần** — máy học không hề biết sự khác biệt đó vì nó chưa bao giờ nhận được tín hiệu "lead này là SQL / lead này đã cọc". Không có GCLID trong CRM = **không có đường nào để dạy nó**.
- Bằng chứng gián tiếp về mức độ ngoại tuyến: GA4 đo được 2.494 lead nhưng CRM có 2.557 — và GA4 chỉ đo được **95.348 phiên trên 180.835 nhấp** (hao hụt 47,3% toàn tài khoản, sheet 10B).

---

### A14. Mô hình phân bổ nhấp cuối làm sai lệch quyết định ngân sách 90 ngày
**Mức độ: TRUNG BÌNH — không mất tiền trực tiếp nhưng lái sai mọi quyết định**

| Kênh | Nhấp cuối (đang dùng) | Dựa trên dữ liệu | Chênh | % thay đổi |
|---|---|---|---|---|
| SEA_Brand | 592 | 401 | **−191** | −32,3% |
| SEA_Generic | 418 | 402 | −16 | −3,8% |
| SEA_Competitor | 20 | 24 | +4 | +20,0% |
| PMAX | 510 | 466 | −44 | −8,6% |
| GDN_Remarketing | 132 | 186 | **+54** | +40,9% |
| YT_Video | 43 | 165 | **+122** | +283,7% |
| Trực tiếp / Organic (ngoài Ads) | 0 | 71 | +71 | — |

- **Bằng chứng số:** sheet `10_GA4` mục D (chỉ tính `generate_lead`, tổng 1.715). Sheet ghi rõ: "Mô hình nhấp cuối là mô hình đang được dùng để đánh giá và phân bổ ngân sách trong suốt 90 ngày."
- **Ý nghĩa:** Brand đang được ghi công **quá 191 lead** (đúng như D1 sẽ nói: một phần công của Brand thực chất là của Generic/YouTube đã gieo nhu cầu trước đó); YouTube + GDN bị ghi công **thiếu 176 lead** → đã bị đánh giá thấp suốt 90 ngày. Ngoài ra 71 lead được gán cho Trực tiếp/Organic — tức 4,1% lead không phải do Ads tạo ra nhưng đang nằm trong mẫu số tính hiệu quả.
- Cửa sổ chuyển đổi 90 ngày + nhấp cuối (sheet 05) trong ngành BĐS có chu kỳ cân nhắc dài là kết hợp đặc biệt dễ gây sai lệch.

---

### A15. Cấu hình & phân bổ vận hành lệch với năng lực bán hàng
**Mức độ: TRUNG BÌNH — ước tính lãng phí 100–150 triệu, phần lớn chồng lấn A1**

**(a) Khung giờ — mua lead lúc không ai nghe máy** (sheet `07_KHUNG_GIO_TB` mục A):

| Khung giờ | % chi phí | Chi phí | SQL | Cọc | Tỷ lệ gọi lại <30' |
|---|---|---|---|---|---|
| 09:00–12:00 | 16,8% | 302.994.216đ | 121 | 4 | **93%** |
| 14:00–17:00 | 17,1% | 308.404.827đ | 117 | 4 | 91% |
| 20:00–23:00 | 18,7% | 337.261.419đ | 112 | 3 | **21%** |
| 23:00–24:00 | 4,0% | 72.141.480đ | 22 | 0 | **12%** |
| 00:00–06:00 | 4,1% | 73.945.017đ | 18 | 0 | **34%** |

→ **22,7% chi phí (409.402.899đ) chạy trong khung 20:00–24:00** nơi chỉ 12–21% lead được gọi lại trong 30 phút. CP/SQL khung 20–24h = 3.055.246đ vs khung 09–12h = 2.504.084đ. Sheet 05: "Lịch quảng cáo 24/7, không điều chỉnh giá thầu theo giờ".

**(b) Thiết bị** (sheet 07B): di động **78,1% chi phí**, CVR 2,03%, CP/SQL 3.042.251đ; máy tính 16,7% chi phí, CVR **4,02%**, CP/SQL **1.847.796đ** → di động đắt hơn **1,65 lần** mỗi SQL, không có điều chỉnh giá thầu theo thiết bị.

**(c) Ngày trong tuần** (sheet 07C): T7+CN tiêu **503.810.000đ (27,9% ngân sách)** nhưng **chỉ 2/8 sale trực**. Riêng T3+T4 tiêu 520.076.000đ, 162 SQL nhưng chỉ **2 cọc** (CP/SQL 3.210.346đ) — trong khi T2 với cùng 8 sale trực đạt **7 cọc** ở CP/SQL 2.151.142đ.

**(d) Cấu hình khác** (sheet `05_CAU_HINH_TK`) — chưa định lượng được riêng, cần báo cáo phân đoạn để bóc tách:
- Search Partners **BẬT** + Mạng hiển thị trong chiến dịch Search **BẬT** cho cả 3 chiến dịch Search → nghi ngờ là một phần nguồn của CTR thấp và lead rác; **cần báo cáo phân đoạn theo mạng để định lượng** (không có trong bộ dữ liệu).
- Điểm chất lượng TB **5,2/10**, trải nghiệm trang đích **"Dưới trung bình"** → đang trả CPC cao hơn cần thiết.
- **31 từ khóa/nhóm, 1 RSA/nhóm** → mức độ liên quan quảng cáo–từ khóa thấp, không có dữ liệu A/B nội dung quảng cáo.
- **Không có reCAPTCHA, không xác minh OTP** → giải thích trực tiếp 31% trùng SĐT của PMax và 24% SĐT sai (sheet 08C).
- Đối tượng chỉ ở chế độ **Quan sát**, chưa loại trừ khách đã đặt cọc/ký HĐMB → đang trả tiền quảng cáo lại cho khách đã mua.
- Tiện ích: chỉ có 4 sitelink. **Thiếu: Cuộc gọi, Biểu mẫu khách hàng tiềm năng, Vị trí, Chú thích, Hình ảnh** — với sản phẩm cần gọi điện thì thiếu tiện ích Cuộc gọi là mất trực tiếp một luồng lead.

---

## Bảng tổng hợp tác động tài chính

**Tiền quảng cáo đang chảy vào chỗ tạo 0 cọc** (các dòng **chồng lấn nhau**, không cộng tổng):

| Nguồn lãng phí | Số tiền | % ngân sách |
|---|---|---|
| PMax (0 doanh thu) | 475.376.000đ | 26,4% |
| Cụm từ 0 SQL trong báo cáo search terms | 419.729.000đ | 23,3% |
| Khu vực ngoài vùng bán (HN/ĐN/CT/ngoài VN) | 364.314.474đ | 20,2% |
| Competitor (0 doanh thu) | 176.746.000đ | 9,8% |
| GDN Remarketing (0 doanh thu, có giá trị hỗ trợ) | 130.009.000đ | 7,2% |
| YouTube (0 doanh thu, có giá trị hỗ trợ) | 83.193.000đ | 4,6% |

**Doanh thu (hoa hồng) đang bỏ lỡ:**

| Nguyên nhân | Ước tính hoa hồng bỏ lỡ |
|---|---|
| Phản hồi lead chậm (A1) | 3.564.027.560đ – 5.556.428.500đ |
| Brand bị bóp ngân sách (A2) | ≈ 1.524.054.416đ (cận trên) |
| Lỗi kỹ thuật LP chưa sửa (A5) | 471.435.276đ – 611.591.709đ |
| Trang đích v1 kém 57 ngày (A6) | ≈ 476.010.573đ |
| 275 lead không ai gọi (A1) | ≈ 350.391.083đ |
| Mất thẻ N44–46 (A11) | ≈ 80.271.412đ |

---

# PHẦN B — TÍNH TOÁN

*Toàn bộ số liệu dưới đây do `agent-3-calc.py` sinh ra. Đơn vị: VND.*

## B1. CPL Ads / CPL CRM / CP/SQL / CP/cọc

### Toàn kỳ và theo chiến dịch

| Chiến dịch | Chi phí | Chuyển đổi Ads | Lead CRM | SQL | Cọc | **CPL Ads** | **CPL CRM** | **CP/SQL** | **CP/cọc** |
|---|---|---|---|---|---|---|---|---|---|
| SEA_Brand_Vinhomes_HocMon | 260.219.000 | 871 | 857 | 352 | 13 | **298.759** | **303.639** | **739.259** | **20.016.846** |
| SEA_Generic_NhaPho_CanHo_TayBac | 677.994.000 | 664 | 587 | 191 | 5 | 1.021.075 | 1.155.015 | 3.549.707 | 135.598.800 |
| SEA_Competitor_DoiThu | 176.746.000 | 31 | 32 | 3 | 0 | 5.701.484 | 5.523.312 | **58.915.333** | ∞ (0 cọc) |
| PMAX_VinhomesHM_Lead | 475.376.000 | 1.775 | 829 | 61 | 0 | **267.817** | 573.433 | 7.793.049 | ∞ (0 cọc) |
| GDN_Remarketing_Web30d | 130.009.000 | 302 | 193 | 36 | 0 | 430.493 | 673.622 | 3.611.361 | ∞ (0 cọc) |
| YT_Video_TVC_MoBan | 83.193.000 | 177 | 59 | 8 | 0 | 470.017 | 1.410.051 | 10.399.125 | ∞ (0 cọc) |
| **TOÀN KỲ** | **1.803.537.000** | **3.820** | **2.557** | **651** | **18** | **472.130** | **705.333** | **2.770.410** | **100.196.500** |

### Chỉ số phụ trợ theo chiến dịch

| Chiến dịch | Nhấp | CTR | CPC TB | SQL/Lead | Ads/CRM | Doanh thu | ROAS |
|---|---|---|---|---|---|---|---|
| SEA_Brand | 19.045 | 11,63% | 13.663 | 41,07% | 1,02x | 2.280.000.000 | **8,76x** |
| SEA_Generic | 20.502 | 4,47% | 33.070 | 32,54% | 1,13x | 850.000.000 | 1,25x |
| SEA_Competitor | 3.204 | 2,39% | 55.164 | 9,38% | 0,97x | 0 | 0,00x |
| PMAX | 39.701 | 1,00% | 11.974 | **7,36%** | **2,14x** | 0 | 0,00x |
| GDN_Remarketing | 28.976 | 0,35% | 4.487 | 18,65% | 1,56x | 0 | 0,00x |
| YT_Video | 69.407 | 0,45% | 1.199 | 13,56% | **3,00x** | 0 | 0,00x |
| **TOÀN KỲ** | **180.835** | 0,64% | 9.973 | **25,46%** | **1,49x** | **3.130.000.000** | **1,74x** |

**Đọc bảng:**
- **Xếp hạng đổi hoàn toàn khi đi từ CPL sang CP/SQL.** Theo CPL Ads, PMax rẻ nhất (267.817đ); theo CP/SQL, PMax đắt gấp **10,5 lần** Brand. Đây là bằng chứng số cốt lõi để trả lời D3.
- **CP/SQL toàn kỳ 2.770.410đ** — nằm trong dải "trung bình ngành 1,8–3,5 triệu" (sheet 09) nhưng **vượt KPI 2.200.000đ 25,9%**.
- **CPL CRM toàn kỳ 705.333đ** — trong dải TB ngành 500.000–1.100.000đ. Nghĩa là: **tài khoản mua lead ở giá chấp nhận được, nhưng mua sai loại lead.**
- Ads/CRM toàn kỳ **1,49x** nằm trong dải "trung bình" của sheet 09, nhưng con số này che giấu PMax **2,14x** và YouTube **3,00x** — đều vượt ngưỡng báo động 1,8x.

### CPL/CP-SQL theo giai đoạn

| Giai đoạn | Chi phí | Lead CRM | SQL | Cọc | CP/SQL | Doanh thu | ROAS |
|---|---|---|---|---|---|---|---|
| GĐ1 (N1–30) | 545.696.000 | 734 | 151 | 2 | 3.613.881 | 330.000.000 | **0,61x** |
| GĐ2 (N31–60) | 604.392.000 | 761 | 184 | 5 | 3.284.739 | 850.000.000 | **1,41x** |
| GĐ3 (N61–90) | 653.449.000 | 1.062 | 316 | 11 | **2.067.877** | 1.950.000.000 | **2,98x** |

---

## B2. ROAS toàn kỳ và theo giai đoạn

| | GĐ1 | GĐ2 | GĐ3 | **Toàn kỳ** |
|---|---|---|---|---|
| Chi phí | 545.696.000 | 604.392.000 | 653.449.000 | **1.803.537.000** |
| Doanh thu (hoa hồng) | 330.000.000 | 850.000.000 | 1.950.000.000 | **3.130.000.000** |
| **ROAS** | **0,61x** | **1,41x** | **2,98x** | **1,74x** |
| Cọc | 2 | 5 | 11 | 18 |
| Lãi/lỗ trên chi phí QC | −215.696.000 | +245.608.000 | +1.296.551.000 | +1.326.463.000 |

**ROAS theo chiến dịch (toàn kỳ):**

| Chiến dịch | ROAS | Lãi/lỗ trên chi phí quảng cáo |
|---|---|---|
| SEA_Brand_Vinhomes_HocMon | **8,76x** | **+2.019.781.000** |
| SEA_Generic_NhaPho_CanHo_TayBac | 1,25x | +172.006.000 |
| SEA_Competitor_DoiThu | 0,00x | −176.746.000 |
| PMAX_VinhomesHM_Lead | 0,00x | −475.376.000 |
| GDN_Remarketing_Web30d | 0,00x | −130.009.000 |
| YT_Video_TVC_MoBan | 0,00x | −83.193.000 |

**Nhận định gắn số:**
- Quỹ đạo đúng hướng: ROAS **0,61x → 1,41x → 2,98x**, GĐ3 gần chạm mục tiêu 3,0x. Ba yếu tố trùng thời điểm GĐ3: trang đích v2 từ N58, SLA gọi 15 phút từ GĐ3 (sheet 08B), thời gian phản hồi trung vị giảm 214' → 47'.
- **Nhưng phần lớn cải thiện đó KHÔNG đến từ Google Ads** — CP/SQL giảm 3.613.881 → 2.067.877 (−42,8%) trong khi cơ cấu chiến dịch gần như không đổi. Nguồn cải thiện chính là trang đích + tốc độ gọi lead.
- Nếu bỏ Brand ra, phần còn lại của tài khoản có ROAS = 850.000.000 / 1.543.318.000 = **0,55x** — tức 85,6% ngân sách đang lỗ.

---

## B3. Tỷ lệ chuyển đổi từng bước phễu

### Toàn tài khoản, toàn kỳ

| Bước | Số | Tỷ lệ | Benchmark sheet 09 | Đánh giá |
|---|---|---|---|---|
| Lead CRM | 2.557 | — | — | — |
| → SQL | 651 | **25,46%** | tốt >30%, TB 18–30%, báo động <12% | Trung bình |
| → Đi xem nhà | 206 | **31,64%** | tốt >35%, TB 22–35%, báo động <15% | Trung bình |
| → Booking | 59 | **28,64%** | (không có benchmark) | — |
| → Đặt cọc | 18 | **30,51%** | — | — |
| **Đi xem → Cọc** | 18/206 | **8,74%** | tốt >12%, TB 7–12%, báo động <4% | Trung bình |
| **Lead → Cọc (tổng)** | 18/2.557 | **0,70%** | — | — |

### Theo giai đoạn — mọi bước đều cải thiện

| Giai đoạn | SQL/Lead | Đi xem/SQL | Booking/Đi xem | Cọc/Booking | Cọc/Lead |
|---|---|---|---|---|---|
| GĐ1 | 20,57% | 25,17% | 26,32% | 20,00% | 0,27% |
| GĐ2 | 24,18% | 30,43% | 28,57% | 31,25% | 0,66% |
| GĐ3 | **29,76%** | **35,44%** | 29,46% | 33,33% | **1,04%** |

### Chỉ tính 3 chiến dịch Search (loại PMax/GDN/YT vì 0 cọc)

| Chỉ tiêu | Search toàn kỳ | Search GĐ3 |
|---|---|---|
| Lead | 1.476 | 726 |
| SQL | 546 | 278 |
| SQL/Lead | **36,99%** | **38,29%** |
| Đi xem/SQL | 34,25% | — |
| Booking/Đi xem | 29,41% | — |
| Cọc/Booking | 32,73% | — |
| **Cọc/SQL** | **3,30%** | **3,96%** |
| Cọc | 18 | 11 |

**Điểm nghẽn nằm ở đâu:** bước tệ nhất so với benchmark là **Lead → SQL (25,46%)** và **Đi xem → Cọc (8,74%)**. Nhưng khi loại 3 kênh không sinh cọc ra, SQL/Lead của Search là **36,99% — trên ngưỡng "tốt" 30%**. Kết luận: **phễu không hỏng; nguồn traffic hỏng.** 1.081 lead từ PMax/GDN/YT (42,3% tổng lead) chỉ tạo 105 SQL (16,1% tổng SQL) và **0 cọc** — chính chúng kéo tỷ lệ toàn tài khoản xuống.

---

## B4. Ngược từ KPI: cần bao nhiêu SQL, bao nhiêu lead thô, CP/SQL trần

### Ba kịch bản giả định

| Kịch bản | SQL/Lead | Cọc/SQL | **Cần SQL** | **Cần lead thô** | **CP/SQL trần** | CPL trần |
|---|---|---|---|---|---|---|
| **A. Toàn tài khoản toàn kỳ** (bảo thủ nhất) | 25,46% | 2,76% | **1.157** | **4.546** | 1.814.516 | 461.967 |
| **B. Chỉ Search toàn kỳ** | 36,99% | 3,30% | **971** | **2.624** | 2.163.462 | 800.305 |
| **C. Search GĐ3** (LP v2 + SLA 15') | 38,29% | 3,96% | **809** | **2.112** | 2.596.673 | 994.318 |

### Kịch bản tôi chọn để lập kế hoạch: **C, có chiết khấu an toàn**

**Lý do chọn C:**
1. GĐ3 là **giai đoạn duy nhất phản ánh trạng thái hiện tại của tài sản**: trang đích v2 đã chạy (từ N58), SLA gọi 15 phút đã có, thời gian phản hồi trung vị 47 phút. GĐ1/GĐ2 chạy trên trang đích LCP 4,8s + form 7 trường **không còn tồn tại**.
2. Chỉ lấy Search vì kế hoạch 90 ngày tới sẽ **không giữ cơ cấu 38,2% ngân sách vào kênh 0 cọc**. Trộn PMax/GDN/YT vào tỷ lệ cơ sở là dự báo cho một cơ cấu mình sẽ không chạy.
3. **Chiết khấu an toàn:** cỡ mẫu GĐ3-Search chỉ **11 cọc** — sai số thống kê rất lớn. Tôi **không dùng thẳng 3,96%**, mà lập kế hoạch ở dải giữa B và C, đồng thời ràng buộc bằng KPI CP/SQL ≤ 2.200.000đ.

### Kiểm tra ngược từ ràng buộc ngân sách

Với 2.100.000.000đ và KPI CP/SQL ≤ 2.200.000đ → mua tối đa **955 SQL**.

| Kịch bản tỷ lệ cọc/SQL | 955 SQL × tỷ lệ | Đạt KPI 32 cọc? |
|---|---|---|
| A — 2,76% (toàn tài khoản hiện tại) | **26,4 cọc** | ❌ Không |
| B — 3,30% (Search toàn kỳ) | **31,5 cọc** | ⚠️ Sát ngưỡng, thiếu 0,5 |
| C — 3,96% (Search GĐ3) | **37,8 cọc** | ✅ Có, dư 18% |

### Kết luận B4 (số phải nhớ)

| Chỉ tiêu | Con số kế hoạch | Cơ sở |
|---|---|---|
| **SQL cần đạt** | **≥ 850** (mục tiêu 955) | 32 ÷ 3,96% = 809 tối thiểu; đệm +5% rủi ro cỡ mẫu → 850 |
| **Lead thô cần đạt** | **2.220 – 2.500** | 850 ÷ 38,29% = 2.220; 955 ÷ 38,29% = 2.494 |
| **CP/SQL tối đa cho phép** | **2.200.000đ** (KPI cứng) — mục tiêu vận hành **2.000.000đ** | 2,1 tỷ ÷ 955 = 2.198.953đ |
| **CPL trần tương ứng** | **≈ 842.000đ** | 2,1 tỷ ÷ 2.494 lead |

**Kiểm tra ràng buộc năng lực sale (bắt buộc):** 2.494 lead ÷ 90 ngày = **27,7 lead/ngày**. Năng lực bình quân có tính T7/CN chỉ 2 sale = (2×12×2 + 8×12×5)/7 = **75,4 lead/ngày**. **Khả thi, dư 2,7 lần** — điều này xác nhận rằng vấn đề của An Phát Land **không phải thiếu lead mà là chất lượng lead + tốc độ gọi**. GĐ3 vừa qua đã chạy ở 35,4 lead/ngày (sheet 08B) mà vẫn để sót 61 lead — nghĩa là nghẽn ở **quy trình**, không ở đầu người.

---

## B5. Điểm hòa vốn và trần chi phí mỗi cọc

Hoa hồng ghi nhận = **181.000.000đ/cọc**.

| Mức ROAS mục tiêu | Chi phí quảng cáo tối đa cho phép / cọc |
|---|---|
| 1,0x (hòa vốn trên chi phí quảng cáo) | **181.000.000đ** |
| 2,0x | 90.500.000đ |
| **3,0x (KPI ban giám đốc)** | **60.333.333đ** |
| 4,0x (biên an toàn) | 45.250.000đ |

**Đối chiếu thực tế:**

| | Số | So với trần ROAS 3x |
|---|---|---|
| CP/cọc thực tế 90 ngày qua | **100.196.500đ** | **gấp 1,66 lần trần** — phải giảm 39,8% |
| CP/cọc của riêng Brand | 20.016.846đ | chỉ bằng 33,2% trần ✅ |
| CP/cọc của riêng Generic | 135.598.800đ | gấp 2,25 lần trần ❌ |
| CP/cọc kế hoạch (2,1 tỷ ÷ 37,8 cọc) | **55.556.000đ** | dưới trần 7,9% ✅ |

**Hai KPI có mâu thuẫn nhẹ — phải nói rõ với ban giám đốc:**
- KPI "32 cọc" với 2,1 tỷ → ROAS = 32 × 181.000.000 ÷ 2.100.000.000 = **2,76x**, **KHÔNG đạt 3,0x**.
- Để đạt ROAS 3,0x với đúng 2,1 tỷ cần doanh thu 6.300.000.000đ = **34,8 cọc**.
- ⇒ **Mục tiêu ràng buộc thật là 35 cọc, không phải 32.** Đạt 32 cọc mà tiêu hết 2,1 tỷ là **trượt KPI ROAS**. Hai đường thoát: (a) đạt 35 cọc, hoặc (b) đạt 32 cọc nhưng chỉ tiêu **1.930.666.667đ** (32×181tr÷3). Kế hoạch phần C nhắm 35+ cọc và giữ quyền không tiêu hết ngân sách nếu CP/SQL vượt ngưỡng.

---

## B6. Đối chiếu ba nguồn số liệu — bóc tách chính xác 3.820 vs 2.557

### Bước 1 — Cột `Chuyển đổi` của Google Ads được cấu thành từ gì

| Thành phần | Số lượt | Nguồn |
|---|---|---|
| generate_lead (gửi form thành công) | 1.715 | sheet 10A |
| click_to_call (tổng lượt nhấp) | 1.132 | sheet 10A |
| view_price_page (xem trang /bang-gia) | 612 | sheet 10A |
| engaged_30s (ở lại >30 giây) | 361 | sheet 10A |
| **Cộng** | **3.820** ✔ | = đúng con số Google Ads báo |

*Google Ads và GA4 luôn bằng nhau (3.820 = 3.820) vì Ads nhập trực tiếp từ GA4 (sheet 12A thẻ #8). **Đây không phải hai nguồn độc lập** — thực chất chỉ có 2 nguồn: hệ đo lường web và CRM.*

### Bước 2 — Ba thành phần tạo nên khoảng chênh

| # | Thành phần | Số | Nguyên nhân | Bằng chứng |
|---|---|---|---|---|
| 1 | **Đếm trùng lượt nhấp gọi** | **−353** | Thẻ `click_to_call` đếm mọi lượt nhấp `tel:`, không khử trùng theo người dùng. 1.132 lượt ↔ 779 người thật | sheet 10A; sheet 12A thẻ #4 "Đếm mọi lượt nhấp, không khử trùng theo người dùng"; sheet 12C "Thổi phồng 353 chuyển đổi (9,2%)" |
| 2 | **Sự kiện rác không phải lead** | **−973** | `view_price_page` (612) + `engaged_30s` (361) đang bị đánh dấu là sự kiện chính và nhập vào Ads | sheet 10A & 10E cột "Có thực sự là khách hàng tiềm năng?" = KHÔNG cho cả hai; sheet 12A thẻ #5, #6; sheet 05 hành động chuyển đổi #3, #4 |
| 3 | **Mất thẻ 3 ngày** | **+63** | GTM v23 (N44, 09:12) đổi class `.form-dk-v1` → `.form-register` làm điều kiện kích hoạt `generate_lead` ngừng khớp; sửa ở v24 (N47, 14:38). 63 lead của N44–46 có trong CRM nhưng **vĩnh viễn không có** trong Ads/GA4 | sheet 12B v23/v24; sheet 10A dòng "Chênh lệch CRM vs GA4 = 63, Lead ngày 44, 45, 46" |

### Bước 3 — Chứng minh phép cộng khớp

```
3.820  (Google Ads / GA4 báo)
−  353  (đếm trùng click_to_call: 1.132 lượt − 779 người)
−  973  (sự kiện rác: 612 view_price_page + 361 engaged_30s)
= 2.494  (lead thật ĐO ĐƯỢC bằng thẻ = 1.715 form + 779 người gọi duy nhất)   ✔ khớp sheet 10A
+   63  (lead mất do gãy thẻ N44–46, chỉ CRM có)
= 2.557  (CRM)   ✔ KHỚP CHÍNH XÁC
```

Kiểm tra chéo bằng hai phép tính độc lập, cả hai đều pass trong `agent-3-calc.py`:
- `1.715 + 1.132 + 612 + 361 = 3.820` ✔
- `1.715 + 779 = 2.494` ✔

### Bước 4 — Xác minh độc lập từ sheet 02 (dữ liệu ngày, không dùng sheet 10)

| Ngày | Chuyển đổi Ads | Lead CRM | Chi phí |
|---|---|---|---|
| N43 | 43 | 30 | 19.744.000đ |
| **N44** | **0** | 17 | 20.249.000đ |
| **N45** | **0** | 15 | 19.699.000đ |
| **N46** | **0** | 31 | 19.580.000đ |
| N47 | 33 | 18 | 19.912.000đ |
| N48 | 36 | 26 | 19.627.000đ |
| **Tổng N44–46** | **0** | **63** | **59.528.000đ** |

Sheet 02 cho ra **đúng 63 lead** ở đúng 3 ngày mà sheet 12_GTM chỉ ra. **Ba nguồn dữ liệu độc lập (02, 10, 12) khớp nhau hoàn toàn.**

### Tóm tắt tỷ trọng

| Thành phần | Số | % cột "Chuyển đổi" |
|---|---|---|
| Lead thật (form + người gọi duy nhất) | 2.494 | 65,3% |
| Đếm trùng | 353 | 9,2% |
| Sự kiện rác | 973 | 25,5% |
| **Tổng thổi phồng** | **1.326** | **34,7%** |

Tỷ số Ads/CRM = 3.820/2.557 = **1,49x** (sheet 09: TB 1,2–1,5x). Con số tổng này *trông* bình thường **chỉ vì hai lỗi trái dấu triệt tiêu nhau**: thổi phồng +1.326 bị bù trừ một phần bởi mất thẻ −63 và bởi việc CRM có lead từ kênh khác. Ở cấp chiến dịch, mặt nạ rơi ra: **PMax 2,14x** và **YouTube 3,00x** — cả hai vượt ngưỡng báo động 1,8x.

---

## B7. Ước tính lead mất do lỗi kỹ thuật CHƯA SỬA và quy ra tiền

### Phân biệt rõ SỐ ĐO và ƯỚC TÍNH

| Loại | Nội dung | Nguồn |
|---|---|---|
| **SỐ ĐO trực tiếp** (Clarity ghi hình) | Số phiên ảnh hưởng: 4.196 / 2.741 / 1.204; số nhấp chết: 8.412 và 1.847; tỷ lệ lỗi JS di động v1 9,3% → v2 8,9% | sheet 11 mục A & C |
| **ƯỚC TÍNH của đội UX** (không phải tôi) | Số lead bị mất mỗi lỗi: 280–340 / 60–90 / 30–50. Sheet 11 ghi rõ: *"Ước tính do đội UX đưa ra dựa trên tỷ lệ hoàn tất form của nhóm phiên không gặp lỗi. Là ước tính, không phải số đo trực tiếp."* | sheet 11 mục C |
| **ƯỚC TÍNH của tôi** | Quy đổi lead → tiền, dùng CPL/CP-SQL/tỷ lệ cọc thực tế của chính tài khoản (sheet 02) | tính trong `agent-3-calc.py` |

### Ba lỗi CHƯA SỬA

| # | Lỗi | Trang đích | Phiên ảnh hưởng (đo) | Lead mất (ước tính UX) |
|---|---|---|---|---|
| 4 | Lỗi JS `TypeError e.setDate is not a function` — Safari iOS 17.x, form không gửi được và **không báo lỗi cho khách** | v1 **và v2** | 4.196 | 280 – 340 |
| 5 | Nút "Đăng ký nhận bảng giá" bị khung chat che, màn hình <380px | v1 **và v2** | 2.741 | 60 – 90 |
| 6 | Hotline `tel:` không phản hồi trên máy tính — 1.847 nhấp chết | v1 **và v2** | 1.204 | 30 – 50 |
| | **CỘNG** | | **8.141** | **370 – 480** |

*Xác nhận chéo lỗi #4 vẫn sống: tỷ lệ phiên có lỗi JavaScript trên di động **9,3% (v1) → 8,9% (v2)** — gần như không đổi, chứng tỏ lỗi không được sửa cùng trang đích v2 (sheet 11A, ghi chú in đậm trong sheet).*

### Quy ra tiền — dùng số thực tế của tài khoản

Tham số (tính từ sheet 02, toàn kỳ): CPL CRM = **705.333đ**; CP/SQL = **2.770.410đ**; SQL/Lead = **25,46%**; Cọc/SQL = **2,76%**; hoa hồng = 181.000.000đ.

| | Kịch bản thấp (370 lead) | Kịch bản cao (480 lead) |
|---|---|---|
| **Tiền quảng cáo đã trả nhưng không nhận được lead** (370 × 705.333) | **260.973.285đ** | **338.559.937đ** |
| Quy ra SQL (× 25,46%) | 94 SQL | 122 SQL |
| Giá trị theo CP/SQL | 260.973.285đ | 338.559.937đ |
| Quy ra cọc (× 2,76%) | **2,6 cọc** | **3,4 cọc** |
| **Hoa hồng bỏ lỡ** | **471.435.276đ** | **611.591.709đ** |

### Hai điều chỉnh cần nêu (đều đẩy con số lên, không xuống)

1. **Clarity chỉ lấy mẫu ~92% lưu lượng trang đích** (sheet 11, dòng 2). Quy về 100%: **402 – 522 lead** thay vì 370–480 → hoa hồng bỏ lỡ **512.429.648đ – 664.773.597đ**.
2. **Clarity chỉ được gắn từ ngày 5** (sheet 12B, v19, ngày 5, 10:24). Thiếu 4/90 ngày = 4,4% kỳ đo. Ước tính trên là **cận dưới**.

### Kết luận B7

> **Ba lỗi kỹ thuật chưa ai sửa đang làm mất 370–480 lead trong 90 ngày** — tương đương **261 – 339 triệu tiền quảng cáo đổ xuống sông** và **471 – 612 triệu hoa hồng bỏ lỡ** (cận trên khi hiệu chỉnh lấy mẫu: 665 triệu).
>
> Chi phí sửa: ước tính **2–5 ngày công của 1 dev**. Đây là ROI cao nhất trong toàn bộ danh mục việc — cao hơn bất kỳ thay đổi giá thầu nào.
>
> **Thiếu dữ liệu cần bổ sung để chốt số:** (a) tỷ lệ % phiên Safari iOS trong tổng phiên di động — hiện chỉ biết 4.196 phiên tuyệt đối; (b) tỷ lệ hoàn tất form của nhóm đối chứng "không gặp lỗi" mà đội UX dùng làm cơ sở; (c) tỷ lệ thiết bị có chiều rộng <380px. Có 3 số này thì ước tính chuyển từ khoảng ±30% xuống ±10%.

---

# PHẦN C — KẾ HOẠCH 90 NGÀY TIẾP THEO

## C0. Nguyên tắc chi phối toàn kế hoạch

| # | Nguyên tắc | Số liệu chống lưng |
|---|---|---|
| 1 | **Sửa đo lường TRƯỚC khi tăng ngân sách.** Ngân sách GĐ1 cố tình thấp (500tr) rồi tăng dần | 34,7% cột Chuyển đổi là rác (B6) — tăng ngân sách trên tín hiệu rác chỉ nhân lãng phí lên |
| 2 | **Dồn tiền về nơi có cọc.** Search chiếm 100% cọc (18/18) | Search = 61,8% chi phí cũ nhưng 100% doanh thu |
| 3 | **Không giết PMax, đưa nó về đúng vai.** | Dưới DDA, PMax vẫn được 466 lead (10D); vấn đề là tín hiệu và vị trí đặt, không phải loại chiến dịch |
| 4 | **Không mua lead lúc không ai gọi được.** | Khung 20–24h: 22,7% chi phí, chỉ 12–21% được gọi <30' (07A) |
| 5 | **Giữ quyền không tiêu hết 2,1 tỷ.** | Đạt 32 cọc mà tiêu hết 2,1 tỷ = ROAS 2,76x = trượt KPI (B5) |

**Mục tiêu tổng 90 ngày:** ≥ **35 cọc** (không phải 32 — xem B5), ROAS ≥ **3,0x**, CP/SQL ≤ **2.200.000đ** (vận hành nhắm 2.000.000đ), **≥ 850 SQL**, **2.220–2.500 lead thô**.

---

## C1. Bảng phân bổ ngân sách — tổng đúng 2.100.000.000đ

| Chiến dịch | GĐ1 (N1–30) | GĐ2 (N31–60) | GĐ3 (N61–90) | **TỔNG 90 ngày** | **%** |
|---|---|---|---|---|---|
| SEA_Brand (Brand + Brand-Defense) | 150.000.000 | 180.000.000 | 220.000.000 | **550.000.000** | **26,2%** |
| SEA_Generic_Cluster (5 nhóm SKAG-cluster) | 250.000.000 | 300.000.000 | 340.000.000 | **890.000.000** | **42,4%** |
| SEA_Competitor (chỉ mở lại có điều kiện) | 0 | 20.000.000 | 20.000.000 | **40.000.000** | **1,9%** |
| PMAX_Feed_Lead (tái cấu trúc) | 60.000.000 | 110.000.000 | 150.000.000 | **320.000.000** | **15,2%** |
| GDN_Remarketing (thu hẹp) | 30.000.000 | 40.000.000 | 60.000.000 | **130.000.000** | **6,2%** |
| YT_Video (demand-gen, đo bằng thước khác) | 0 | 20.000.000 | 60.000.000 | **80.000.000** | **3,8%** |
| Dự phòng / test có kiểm soát | 10.000.000 | 30.000.000 | 50.000.000 | **90.000.000** | **4,3%** |
| **TỔNG GIAI ĐOẠN** | **500.000.000** | **700.000.000** | **900.000.000** | **2.100.000.000** | **100%** |
| Ngân sách/ngày | 16.666.667 | 23.333.333 | 30.000.000 | — | — |

*Kiểm tra tổng bằng script: `gt == 2_100_000_000` → **True** (assert trong `agent-3-calc.py`).*

**So sánh với 90 ngày vừa qua:**

| Chiến dịch | Chi phí cũ | % cũ | Chi phí mới | % mới | Thay đổi |
|---|---|---|---|---|---|
| Brand | 260.219.000 | 14,4% | 550.000.000 | 26,2% | **+111%** |
| Generic | 677.994.000 | 37,6% | 890.000.000 | 42,4% | +31% |
| Competitor | 176.746.000 | 9,8% | 40.000.000 | 1,9% | **−77%** |
| PMax | 475.376.000 | 26,4% | 320.000.000 | 15,2% | **−33%** |
| GDN | 130.009.000 | 7,2% | 130.000.000 | 6,2% | 0% |
| YouTube | 83.193.000 | 4,6% | 80.000.000 | 3,8% | −4% |
| Dự phòng | 0 | 0% | 90.000.000 | 4,3% | mới |

**Lý do gấp đôi Brand:** ROAS 8,76x, CP/cọc 20.016.846đ (chỉ 33% trần ROAS 3x), mất **40,06% IS do ngân sách**. Đây là chỗ duy nhất trong tài khoản mà "đổ thêm tiền" là quyết định có bằng chứng.

---

## C2. Dự báo kết quả kế hoạch

Dùng tỷ lệ Search GĐ3 (SQL/Lead 38,29%, Cọc/SQL 3,96%) — xem B4 về giả định:

| Nếu CP/SQL đạt | SQL | Lead thô | Cọc | Doanh thu | ROAS |
|---|---|---|---|---|---|
| 1.800.000đ (kịch bản tốt) | 1.167 | 3.047 | **46,2** | 8.355.515.588đ | **3,98x** |
| **2.000.000đ (kịch bản kế hoạch)** | **1.050** | **2.742** | **41,5** | **7.519.964.029đ** | **3,58x** |
| 2.200.000đ (trần KPI) | 955 | 2.493 | **37,8** | 6.836.330.935đ | **3,26x** |
| *Kịch bản xấu:* 2.200.000đ + tỷ lệ cọc/SQL rơi về mức Search toàn kỳ 3,30% | 955 | 2.493 | **31,5** | 5.701.500.000đ | 2,71x |

**Biên an toàn:** kể cả ở trần KPI CP/SQL, kế hoạch vẫn cho 37,8 cọc (> 35 cần thiết) và ROAS 3,26x. Chỉ trượt khi tỷ lệ cọc/SQL rơi về mức trung bình toàn kỳ — đó chính là rủi ro mà kế hoạch đo lường (C5) và kế hoạch vận hành (C7) được thiết kế để chặn.

**Kiểm tra năng lực sale:** 2.742 lead ÷ 90 = **30,5 lead/ngày**, so với năng lực bình quân **75,4 lead/ngày** (đã tính T7/CN chỉ 2 sale). Dư 2,5 lần. Không cần tăng người.

---

## C3. GIAI ĐOẠN 1 (Ngày 1–30) — "SỬA MÓNG, KHÔNG XÂY THÊM TẦNG"

### Mục tiêu định lượng

| Chỉ tiêu | Mục tiêu GĐ1 | Cơ sở |
|---|---|---|
| Chi phí | ≤ 500.000.000đ | ngân sách phân bổ |
| Lead thô | 650 – 750 | ≈ GĐ1/GĐ2 cũ, không đặt tăng trưởng |
| SQL | ≥ 220 | SQL/Lead ≥ 32% (GĐ3 cũ 29,76%, mục tiêu +2đ%) |
| **CP/SQL** | **≤ 2.300.000đ** | cải thiện 11% so với GĐ3 cũ (2.067.877đ là của Search; toàn TK GĐ3 là 2.067.877đ) |
| Cọc | ≥ 8 | (35 tổng: 8 / 12 / 15) |
| ROAS | ≥ 2,5x | 8 × 181tr / 500tr = 2,90x nếu đạt |
| **Chỉ tiêu đo lường (bắt buộc)** | Cột `Chuyển đổi` chỉ còn generate_lead + click_to_call (khử trùng); Ads/CRM về **1,0–1,2x** | benchmark sheet 09 |
| Chỉ tiêu kỹ thuật | 3 lỗi Clarity chưa sửa = **0**; tỷ lệ phiên lỗi JS di động < 2% | từ 8,9% (sheet 11A) |
| Chỉ tiêu vận hành | ≥ 70% lead gọi lại < 5 phút | từ 11% hiện tại (sheet 08A) |

### Cấu trúc tài khoản đề xuất (áp dụng từ GĐ1)

| Chiến dịch | Nhóm quảng cáo | Loại đối sánh | Ghi chú |
|---|---|---|---|
| **SEA_Brand_Core** | 1. `vinhomes hoc mon` (tên chuẩn + không dấu)<br>2. `vinhomes hoc mon + giá/bảng giá`<br>3. `vinhomes hoc mon + vị trí/mặt bằng/tiến độ` | **Chính xác + Cụm từ** (bỏ Rộng) | Rộng ở Brand đang mua `tuyển dụng`, `học phí` — 26.022.000đ/0 SQL (sheet 04) |
| **SEA_Brand_Defense** | 1. `vinhomes hoc mon + có thật không / lừa đảo / review` | Cụm từ | Chặn narrative tiêu cực; LP riêng có pháp lý |
| **SEA_Generic_Cluster** | 1. `nhà phố hóc môn`<br>2. `căn hộ hóc môn`<br>3. `shophouse / biệt thự hóc môn`<br>4. `nhà phố quận 12 / gò vấp`<br>5. `khu đô thị tây bắc tphcm` | **Chính xác + Cụm từ** ưu tiên; **Rộng CHỈ trong 1 nhóm thử nghiệm riêng có trần chi phí 30tr/GĐ** | 5 cụm này = 5 cụm duy nhất trong sheet 04 có SQL > 0 ở Generic (41+30+13+26+19 SQL) |
| **SEA_Competitor** | (tạm dừng GĐ1) | — | 0 SQL/6 cụm, 176.746.000đ (sheet 04) |
| **PMAX_Feed_Lead** | 1 nhóm nội dung: nhà phố; 1 nhóm: căn hộ | Tín hiệu đối tượng = danh sách khách đã cọc + SQL (khách hàng tương tự) | + loại trừ vị trí đặt, + brand exclusion, + tCPA |
| **GDN_Remarketing** | 1. Web 7 ngày (bỏ dở form)<br>2. Web 30 ngày (đã xem /bang-gia) | — | Thu hẹp từ "Web30d" chung |
| **YT_Video** | (tạm dừng GĐ1) | — | Mở lại GĐ2 khi đã có đo lường sạch |

**Tỷ trọng đối sánh mục tiêu:** Chính xác + Cụm từ ≥ **80% chi phí Search** (hiện Rộng chiếm 71%, Chính xác 9% — sheet 05).

### Chiến lược giá thầu GĐ1

| Chiến dịch | Chiến lược GĐ1 | Lý do | **Điều kiện chuyển đổi chiến lược** |
|---|---|---|---|
| SEA_Brand_Core | **CPC thủ công nâng cao (eCPC)**, trần CPC 20.000đ | Dữ liệu chuyển đổi đang bẩn — không giao vô-lăng cho máy học cho tới khi tín hiệu sạch | → **Tối đa hóa chuyển đổi** khi: (a) tín hiệu đã sạch ≥ 14 ngày, VÀ (b) ≥ 50 chuyển đổi/30 ngày. Rồi → **tCPA 750.000đ** khi có 30 chuyển đổi ở CPA ổn định ±15% |
| SEA_Brand_Defense | eCPC, trần 25.000đ | cỡ nhỏ | như trên |
| SEA_Generic_Cluster | **Tối đa hóa chuyển đổi CÓ đặt tCPA 1.200.000đ** ngay từ đầu | "Tối đa hóa số lần nhấp không trần CPC" hiện tại đẩy CPC lên 33.070đ (sheet 02) | → **tROAS** khi đã nhập chuyển đổi ngoại tuyến và có ≥ 30 cọc lịch sử gắn GCLID (dự kiến GĐ3 hoặc quý sau) |
| SEA_Competitor | (dừng) | — | Mở lại nếu Auction Insights cho thấy đối thủ đấu tên mình (xem D2) |
| PMAX_Feed_Lead | **tCPA 1.500.000đ** (không để "Tối đa hóa chuyển đổi" trần trụi) | Không tCPA = PMax tự do đi mua tín hiệu rẻ nhất — chính là 697 sự kiện rác | → nới tCPA lên 2.000.000đ nếu SQL/Lead ≥ 25% trong 21 ngày; → **tắt** nếu SQL/Lead < 15% sau 30 ngày |
| GDN_Remarketing | tCPA 900.000đ | CPC 4.487đ quá rẻ = đang mua vị trí kém | → giữ nếu CP/SQL ≤ 2.500.000đ |
| YT_Video | (dừng GĐ1) | — | Mở GĐ2 với **CPV mục tiêu**, đo bằng assisted/DDA chứ không bằng cọc nhấp cuối |

### Việc GĐ1 theo tuần

| Tuần | Việc | Kết quả đo được |
|---|---|---|
| T1 | Sửa 3 lỗi Clarity chưa sửa (#4, #5, #6); dọn cột Chuyển đổi (bỏ view_price_page + engaged_30s); khử trùng click_to_call | Cột Chuyển đổi giảm ~34,7%; phiên lỗi JS di động < 2% |
| T1 | Thu hẹp địa lý: chỉ TP.HCM + Bình Dương + Long An + Đồng Nai; đổi tùy chọn vị trí sang **"Hiện diện"** | Loại 364.314.474đ/90 ngày ở vùng 0 cọc |
| T1 | Nạp danh sách phủ định chia sẻ (≥ 250 từ, bắt đầu từ 10 cụm sai ý định trong sheet 04) | Chặn ≥ 209.082.000đ/90 ngày chi phí sai ý định |
| T2 | Cài biến GCLID ẩn + gửi vào CRM; cài Enhanced Conversions | ≥ 95% bản ghi CRM mới có GCLID |
| T2 | Tái cấu trúc nhóm quảng cáo (31 từ/nhóm → ≤ 15 từ/nhóm, ≥ 2 RSA/nhóm) | Điểm chất lượng TB từ 5,2 → ≥ 6,5 sau 30 ngày |
| T3 | Bật lịch quảng cáo + điều chỉnh giá thầu theo giờ/thiết bị/ngày | Chi phí khung 20:00–06:00 giảm từ 26,8% xuống ≤ 10% |
| T3–4 | Bổ sung tiện ích: Cuộc gọi, Biểu mẫu KH tiềm năng, Vị trí, Chú thích, Hình ảnh | CTR Brand ≥ 13%; ≥ 50 lead/tháng qua tiện ích Cuộc gọi |
| T4 | Chạy A/B trang đích v2 vs v3 (v3 = v2 + video nhà mẫu above-the-fold) | Có 1 test đang chạy (hiện đang là 0 — sheet 05) |

---

## C4. GIAI ĐOẠN 2 (Ngày 31–60) — "MỞ RỘNG TRÊN NỀN SẠCH"

### Mục tiêu định lượng

| Chỉ tiêu | Mục tiêu | Cơ sở |
|---|---|---|
| Chi phí | ≤ 700.000.000đ | +40% so với GĐ1 |
| Lead thô | 900 – 1.000 | |
| SQL | ≥ 340 | SQL/Lead ≥ 35% |
| **CP/SQL** | **≤ 2.100.000đ** | |
| Cọc | ≥ 12 | |
| ROAS | ≥ 3,1x | 12 × 181tr / 700tr = 3,10x |
| Nhập chuyển đổi ngoại tuyến | **đang chạy hằng ngày** | điều kiện tiên quyết cho GĐ3 |
| Impression Share Brand | ≥ 80% | từ 53,01% |
| Mất IS do ngân sách (Brand) | ≤ 10% | từ 40,06% |

### Thay đổi cấu trúc so với GĐ1

| Việc | Điều kiện kích hoạt | Ngân sách |
|---|---|---|
| Mở lại **SEA_Competitor** dạng thu hẹp: chỉ 2–3 tên đối thủ trực tiếp cùng khu Tây Bắc, **đối sánh Cụm từ**, LP so sánh riêng | Chỉ mở nếu Auction Insights xác nhận đối thủ đang đấu tên mình | 20.000.000đ |
| Mở lại **YT_Video** dạng Demand Gen, đối tượng = khách hàng tương tự của danh sách SQL | Chỉ mở khi Ads/CRM ≤ 1,2x đã ổn định 14 ngày | 20.000.000đ |
| Tăng PMax lên 110.000.000đ | Chỉ tăng nếu PMax GĐ1 đạt SQL/Lead ≥ 25% | 110.000.000đ |
| Thêm nhóm quảng cáo Generic mới: `nhà phố tây bắc tphcm`, `căn hộ gò vấp`, `mua nhà trả góp hóc môn` | Từ search terms report tuần 4–5 | trong 300.000.000đ |
| Bắt đầu **tROAS** cho Brand nếu đã có ≥ 30 cọc gắn GCLID | | |

### Chuyển đổi chiến lược giá thầu GĐ2

| Từ | Sang | Điều kiện số cụ thể |
|---|---|---|
| Brand: eCPC | Tối đa hóa chuyển đổi → tCPA 750.000đ | ≥ 50 chuyển đổi/30 ngày, tín hiệu sạch ≥ 14 ngày |
| Generic: tCPA 1.200.000đ | tCPA 1.000.000đ (siết dần) | CP/SQL GĐ1 ≤ 2.300.000đ và SQL/Lead ≥ 32% |
| PMax: tCPA 1.500.000đ | tCPA 1.800.000đ (nới để mở rộng) | SQL/Lead ≥ 25% trong 21 ngày liên tục |

---

## C5. GIAI ĐOẠN 3 (Ngày 61–90) — "TĂNG TỐC QUANH SỰ KIỆN MỞ BÁN"

### Mục tiêu định lượng

| Chỉ tiêu | Mục tiêu | Cơ sở |
|---|---|---|
| Chi phí | ≤ 900.000.000đ | |
| Lead thô | 1.100 – 1.250 | |
| SQL | ≥ 430 | SQL/Lead ≥ 37% |
| **CP/SQL** | **≤ 2.000.000đ** | |
| Cọc | ≥ 15 | |
| ROAS | ≥ 3,0x | 15 × 181tr / 900tr = 3,02x |
| **Cộng dồn 90 ngày** | **≥ 35 cọc, ROAS ≥ 3,0x, CP/SQL ≤ 2.200.000đ** | |

### Việc riêng GĐ3

- **Tối ưu theo giá trị, không theo số lượng:** đã có ≥ 60 ngày dữ liệu chuyển đổi ngoại tuyến → chuyển Generic sang **tROAS**, gán giá trị chuyển đổi theo bậc: lead thô = 0đ, SQL = 2.000.000đ, đi xem = 8.000.000đ, cọc = 181.000.000đ. Đây là bước duy nhất khiến máy học ngừng coi lead PMax rác bằng lead Brand.
- **Đẩy tần suất quanh sự kiện mở bán:** tăng ngân sách Brand lên 220.000.000đ (7,33tr/ngày) — Brand là nơi nhu cầu bùng phát khi có sự kiện.
- **Dự phòng 50.000.000đ** dùng cho: (a) bơm thêm Brand nếu IS < 85% trong tuần sự kiện; (b) một test đối tượng mới; (c) **không tiêu nếu CP/SQL vượt 2.200.000đ** — nguyên tắc C0#5.

---

## C6. KẾ HOẠCH ĐO LƯỜNG (mục riêng, bắt buộc)

> **Đây là hạng mục ưu tiên số 1 của toàn kế hoạch.** Lý do bằng số: 34,7% cột Chuyển đổi là rác (B6); 3 lỗi kỹ thuật chưa sửa làm mất 370–480 lead (B7); không có GCLID trong CRM nghĩa là **không thể** tối ưu theo SQL/cọc (A13). Mọi thay đổi giá thầu thực hiện trước khi sửa đo lường đều là tối ưu theo số sai.

### C6.1 — Sửa gì trong GA4

| # | Việc | Trạng thái hiện tại | Kết quả kỳ vọng (đo được) |
|---|---|---|---|
| G1 | **Bỏ đánh dấu "sự kiện chính"** cho `view_price_page` (612) và `engaged_30s` (361); ngắt nhập vào Google Ads | Cả 4 đang là sự kiện chính (sheet 10E) | Cột Chuyển đổi giảm **973 lượt (−25,5%)** |
| G2 | **Khử trùng `click_to_call`** — chuyển sang đếm theo người dùng/phiên (1 lần/phiên), hoặc tạo sự kiện `phone_click_unique` | 1.132 lượt ↔ 779 người (sheet 10A) | Giảm thêm **353 lượt (−9,2%)**; Ads/CRM về ≈ 1,0–1,1x |
| G3 | **Đánh dấu `zalo_click` (894 lượt) là sự kiện chính** và nhập vào Ads | Có dữ liệu từ v26/N71, chưa đánh dấu (sheet 10E, 12B) | +894 tín hiệu ý định thật/90 ngày vào bidding |
| G4 | `file_download` (bảng giá PDF, 1.206 lượt) → **sự kiện phụ**, dùng làm đối tượng remarketing, **KHÔNG** nhập vào Ads | chưa đánh dấu | Danh sách remarketing ≥ 1.200 người ý định cao |
| G5 | Giữ `form_start` (7.458) làm sự kiện chẩn đoán, **không** nhập Ads | Đang đúng (sheet 12A thẻ #7) | Không đổi — đây là mục ĐẠT duy nhất |
| G6 | Đổi mô hình phân bổ báo cáo sang **Dựa trên dữ liệu** | Đang nhấp cuối (sheet 05, 10D) | Ghi công lại: Brand −191, YT +122, GDN +54 lead |
| G7 | Xóa/gộp thẻ cấu hình GA4 trùng | `Copy of Main` bắn page_view 2 lần từ N31 (sheet 12A#2, 12B v22) | Số phiên GA4 giảm ~50% ở chỉ số page_view — đây là **sửa đúng, không phải sụt giảm** |
| G8 | Xây 1 báo cáo khám phá "Phễu: form_start → generate_lead" tách theo chiến dịch × thiết bị | chưa có | Phát hiện điểm rơi trong ≤ 24h thay vì 3 ngày |

**Sau G1+G2, cột Chuyển đổi dự kiến:** 3.820 − 973 − 353 = **2.494**, cộng zalo_click 894 = **3.388** — nhưng lần này **100% là hành vi liên hệ thật**.

### C6.2 — Sửa gì trong GTM

| Thứ tự | Việc | Vấn đề đang có (sheet 12) | Cách kiểm tra sau khi sửa |
|---|---|---|---|
| **T1** | **Cảnh báo tự động khi chuyển đổi = 0** (GA4 custom alert + script kiểm tra hằng ngày lúc 09:00) | Mục #18: KHÔNG CÓ → sự cố N44–46 mất 3 ngày mới phát hiện | Cố tình tắt thẻ trong môi trường staging → phải nhận email/Zalo trong ≤ 2 giờ |
| **T1** | **Đổi điều kiện kích hoạt `generate_lead` từ class CSS sang `dataLayer.push`** do dev bắn khi form trả về thành công | Thẻ #3: "Điều kiện dựa trên class CSS — rất dễ vỡ" (chính là nguyên nhân N44–46) | GTM Preview: đổi class thủ công trong DevTools → sự kiện vẫn bắn |
| **T1** | **Sửa 3 lỗi Clarity chưa sửa** (#4 setDate Safari iOS, #5 nút bị chat che, #6 tel: desktop) | sheet 11C | Clarity: tỷ lệ phiên lỗi JS di động từ 8,9% → **< 2%**; nhấp chết < 5% |
| **T2** | **Biến ẩn lưu GCLID/GBRAID/WBRAID vào form → CRM** | Mục #15: CHƯA CÀI; sheet 05: "CRM không lưu GCLID" | Gửi 10 form test qua link có `?gclid=test123` → 10/10 bản ghi CRM có GCLID |
| **T2** | **Bật Enhanced Conversions** (hash email/SĐT) | Mục #14: CHƯA CÀI, "mất 10–20% khả năng khớp" | Google Ads > Chẩn đoán chuyển đổi: trạng thái "Đang ghi nhận", tỷ lệ khớp ≥ 40% |
| **T2** | **Gỡ thẻ GA4 Configuration trùng** | Thẻ #2 | GTM Preview: `page_view` chỉ bắn 1 lần |
| **T3** | **Kiểm toán & gỡ thẻ không rõ nguồn gốc**: `Zalo Tracking` (không rõ ai cài), `Thẻ đối tác sàn F2` (3 thẻ, "cần rà soát bảo mật") | Thẻ #12, #13 | Tổng JS bên thứ ba từ **412 KB → ≤ 150 KB**; LCP trang đích cải thiện ≥ 0,5s (đo bằng PageSpeed + Clarity) |
| **T3** | **Cấu hình Consent Mode v2** | Mục #16: CHƯA CẤU HÌNH | Tag Assistant: thấy `consent default` trước mọi thẻ đo lường |
| **T4** | **Gắn Clarity session ID vào bản ghi CRM** | Mục 12C: KHÔNG ĐẠT | Mở 1 lead đã cọc bất kỳ → xem lại được bản ghi hình |
| **T5–6** | **Vùng chứa phía máy chủ (server-side GTM)** | Mục #17: KHÔNG CÓ, "phụ thuộc hoàn toàn trình duyệt" | Chênh lệch nhấp Ads ↔ phiên GA4 từ **47,3%** xuống ≤ 20% |
| **T6+** | **Nhập chuyển đổi ngoại tuyến từ CRM** (SQL / đi xem / cọc, kèm giá trị) — *phụ thuộc GCLID ở T2* | sheet 05: CHƯA triển khai | Google Ads có 3 hành động chuyển đổi ngoại tuyến, tỷ lệ nhập thành công ≥ 90% |

### C6.3 — Thứ tự triển khai và lý do

```
TUẦN 1  ─ Chặn máu ─────────────────────────────────────────
  1. Dọn cột Chuyển đổi (G1, G2)        ← thay đổi lớn nhất, chi phí gần 0
  2. Cảnh báo chuyển đổi = 0             ← chặn tái diễn sự cố N44–46
  3. Đổi trigger sang dataLayer          ← chặn nguyên nhân gốc
  4. Sửa 3 lỗi Clarity                   ← ROI cao nhất: 370–480 lead
TUẦN 2  ─ Mở đường tối ưu ──────────────────────────────────
  5. GCLID vào CRM  → 6. Enhanced Conversions → 7. Gỡ thẻ GA4 trùng
TUẦN 3  ─ Dọn nhà ──────────────────────────────────────────
  8. Kiểm toán thẻ lạ  → 9. Consent Mode v2
TUẦN 4+ ─ Nâng cấp ─────────────────────────────────────────
  10. Clarity ID vào CRM → 11. sGTM → 12. Nhập chuyển đổi ngoại tuyến
```

**Vì sao đúng thứ tự này:** (a) mục 1–2 miễn phí và tạo hiệu ứng lớn nhất; (b) mục 12 (thứ đáng giá nhất) **phụ thuộc kỹ thuật** vào mục 5 — không có GCLID thì không import được, nên GCLID phải xong tuần 2; (c) mục 3 phải làm trước khi dev đụng vào giao diện lần nữa, nếu không lịch sử N44–46 lặp lại.

### C6.4 — Cách kiểm tra sau khi sửa (nghiệm thu bằng số, không bằng cảm nhận)

| Kiểm tra | Công cụ | Ngưỡng ĐẠT |
|---|---|---|
| Chênh Ads/CRM | So `ChuyenDoi_Ads` vs `Lead_CRM` hằng tuần | **1,0 – 1,2x** (hiện 1,49x; PMax 2,14x) |
| Cột Chuyển đổi chỉ còn hành vi liên hệ thật | Google Ads > Chuyển đổi | 0 hành động thuộc loại "xem trang"/"thời gian trên trang" |
| Trigger không phụ thuộc giao diện | GTM Preview + đổi class thủ công | Sự kiện vẫn bắn |
| Cảnh báo hoạt động | Diễn tập tắt thẻ ở staging | Nhận cảnh báo ≤ 2 giờ |
| GCLID vào CRM | 10 form test có `?gclid=` | 10/10 |
| Hao hụt nhấp → phiên | GA4 vs Ads | Toàn TK ≤ 20% (hiện 47,3%); PMax ≤ 15% (hiện 28,0%) |
| Lỗi kỹ thuật LP | Clarity | Phiên lỗi JS di động < 2%; nhấp chết < 5%; thoát <3s của PMax < 30% (hiện 74,3%) |
| Tốc độ trang | PageSpeed + GA4 | LCP di động ≤ 2,0s **sau khi** đã trừ tải GTM |
| Đối chiếu hằng tuần | Bảng 3 cột Ads / GA4 / CRM | Chênh lệch giải thích được 100%, không có mục "không rõ" |

---

## C7. Trang đích, tiện ích, đối tượng, vận hành

### Trang đích

| Việc | Bằng chứng | Kết quả kỳ vọng |
|---|---|---|
| Sửa dứt điểm 3 lỗi chưa sửa (ưu tiên #4 Safari iOS) | sheet 11C, 4.196 phiên | +370–480 lead/90 ngày |
| Giữ v2 làm nền (form 3 trường, LCP 1,9s, có bảng giá) | sheet 05, 10C | tỷ lệ hoàn tất form ≥ 28% |
| **Tách LP theo cụm từ khóa** (message match): LP nhà phố / LP căn hộ / LP so sánh đối thủ / LP pháp lý ("có thật không") | sheet 04: 5 cụm sinh SQL thuộc 3 chủ đề khác nhau nhưng dùng chung 1 LP | tỷ lệ hoàn tất form nhóm Generic từ 31,0% → ≥ 38% |
| **Ưu tiên tuyệt đối di động**: v1 di động chỉ hoàn tất form 16,1% vs máy tính 34,8% | sheet 10C | thu hẹp chênh xuống ≤ 1,3 lần |
| Bắt đầu **A/B test liên tục** (hiện đang 0 test — sheet 05) | | luôn có ≥ 1 test chạy |
| Thêm **reCAPTCHA v3 + xác minh OTP số điện thoại** | sheet 05: không có gì; PMax 31% trùng SĐT, 24% SĐT sai | tỷ lệ SĐT sai < 8% |

### Tiện ích (đang thiếu 5/6 loại — sheet 05)

| Tiện ích | Ưu tiên | Lý do bằng số |
|---|---|---|
| **Cuộc gọi (Call)** | Cao nhất | 779 người đã chủ động bấm gọi từ LP (sheet 10A) — đang không có đường gọi thẳng từ quảng cáo |
| **Biểu mẫu khách hàng tiềm năng (Lead form)** | Cao | Di động = 78,1% chi phí nhưng CVR chỉ 2,03% vs máy tính 4,02% — lead form cắt bước tải LP |
| **Vị trí (Location)** | Cao | Dự án ở Hóc Môn, nhà mẫu mở 8:00–18:00; 59,7% chi phí đến từ lõi TP.HCM |
| **Chú thích + Hình ảnh** | Trung bình | CTR Generic 4,47% (TB ngành 3–5%) — còn dư địa |
| Sitelink | Đã có 4 | Nâng lên 6–8, trỏ tới LP theo chủ đề |

### Đối tượng

| Việc | Trạng thái hiện tại | Hành động |
|---|---|---|
| Đối tượng đang ở chế độ **Quan sát** | sheet 05 | Chuyển sang **Nhắm mục tiêu** cho GDN/PMax; giữ Quan sát + điều chỉnh giá thầu cho Search |
| **Chưa loại trừ khách đã cọc / đã ký HĐMB** | sheet 05 | Tải danh sách loại trừ (Customer Match) ngay tuần 1 — đang trả tiền quảng cáo lại cho khách đã mua |
| Chưa có danh sách khách hàng tương tự từ SQL | — | Tạo từ 651 SQL + 18 khách cọc → làm tín hiệu đối tượng cho PMax |
| Danh sách remarketing chưa phân tầng | GDN chỉ có "Web 30d" | Tách: bỏ dở form (7.458 − 1.715 = 5.743 người), đã tải bảng giá (1.206), đã xem /bang-gia (612) |

### Vận hành sale (không thuộc Google Ads nhưng là ràng buộc số 1 — xem A1)

| Việc | Số hiện tại | Mục tiêu |
|---|---|---|
| SLA gọi lại | 11% lead được gọi < 5 phút | ≥ 70% |
| Lead bị bỏ sót | 275 lead/90 ngày | 0 |
| Trực T7–CN | 2/8 sale, nhưng T7+CN tiêu 27,9% ngân sách | Hoặc tăng trực cuối tuần, **hoặc giảm ngân sách T7–CN xuống 15%** — không được để lệch |
| Khung 20:00–24:00 | 22,7% chi phí, 12–21% gọi lại <30' | Bật auto-responder Zalo/SMS ngay khi có lead ngoài giờ; giảm ngân sách khung này |

---

## C8. Tiêu chí DỪNG / MỞ RỘNG (ngưỡng số cụ thể)

### Tiêu chí DỪNG (tắt hoặc cắt ≥ 50% ngân sách)

| Đối tượng | Điều kiện dừng | Kiểm tra |
|---|---|---|
| **Bất kỳ chiến dịch nào** | CP/SQL > **5.000.000đ** trong 21 ngày liên tục (ngưỡng báo động sheet 09) | Hằng tuần |
| **Bất kỳ chiến dịch nào** | SQL/Lead < **12%** sau ≥ 100 lead (ngưỡng "nhắm sai tệp" sheet 09) | Hằng tuần |
| **Bất kỳ chiến dịch nào** | Chênh Ads/CRM > **1,8x** sau khi đã dọn đo lường (nghĩa là còn nguồn rác khác) | Hằng tuần |
| **PMax** | SQL/Lead < 15% sau 30 ngày, HOẶC thoát-nhanh-<3s (Clarity) > 50% sau khi đã loại trừ vị trí đặt | Ngày 30 |
| **Từ khóa đơn lẻ** | Chi phí > **8.000.000đ**, 0 SQL | Hằng tuần khi rà search terms |
| **Khu vực** | Chi phí > **30.000.000đ**, 0 cọc trong 60 ngày | Ngày 60 |
| **Toàn tài khoản** | CP/SQL cộng dồn > 2.200.000đ ở mốc ngày 45 → **đóng băng ngân sách**, không tiêu tiếp phần dự phòng | Ngày 45 |
| **Trang đích/biểu mẫu** | Tỷ lệ hoàn tất form tụt dưới 20% trong 7 ngày → nghi gãy thẻ/lỗi JS, kiểm tra ngay | Hằng ngày (tự động) |

### Tiêu chí MỞ RỘNG (tăng ngân sách)

| Đối tượng | Điều kiện mở rộng | Mức tăng |
|---|---|---|
| **Brand** | Mất IS do ngân sách > 10% VÀ CP/cọc < 30.000.000đ | +20%/tuần, trần 30% tổng ngân sách giai đoạn |
| **Nhóm quảng cáo Generic** | CP/SQL < 1.800.000đ trong 14 ngày VÀ ≥ 20 SQL | +25%/2 tuần |
| **PMax** | SQL/Lead ≥ 25% VÀ CP/SQL < 2.200.000đ trong 21 ngày | +50% cho giai đoạn kế |
| **Từ khóa mới từ search terms** | ≥ 3 SQL với CP/SQL < 2.000.000đ | Tách thành từ khóa Chính xác riêng |
| **YouTube/GDN** | Dưới mô hình DDA, lead được ghi công ≥ 150 trong 30 ngày VÀ có ≥ 1 cọc hỗ trợ | +50%, trần 8% tổng ngân sách |
| **Toàn tài khoản** | CP/SQL cộng dồn < 1.900.000đ ở mốc ngày 45 | Giải phóng toàn bộ 90.000.000đ dự phòng |

### Ngưỡng cảnh báo hằng ngày (tự động, không cần người nhìn)

| Chỉ số | Cảnh báo khi |
|---|---|
| Chuyển đổi ngày = 0 | Bất kỳ chiến dịch nào đang tiêu > 2 triệu/ngày |
| Chi phí ngày | > 130% ngân sách/ngày dự kiến |
| CPC trung bình | > 150% của trung bình 7 ngày trước |
| Tỷ lệ hoàn tất form | Giảm > 30% so với trung bình 7 ngày |
| Lead CRM ngày = 0 | Trong giờ hành chính |

---

# PHẦN D — XỬ LÝ TÌNH HUỐNG

## D1. "Cắt hết ngân sách brand, dồn cho từ khóa chung"

**Trả lời: Không đồng ý cắt. Ngược lại, tôi đề xuất tăng gấp đôi Brand — và tôi có 5 con số.**

| | SEA_Brand | SEA_Generic |
|---|---|---|
| Chi phí | 260.219.000đ (**14,4%** tài khoản) | 677.994.000đ (37,6%) |
| Doanh thu hoa hồng | **2.280.000.000đ (72,8% toàn tài khoản)** | 850.000.000đ (27,2%) |
| Cọc | **13 / 18** | 5 / 18 |
| **ROAS** | **8,76x** | **1,25x** |
| CP/SQL | **739.259đ** | 3.549.707đ |
| CP/cọc | **20.016.846đ** | 135.598.800đ |
| SQL/Lead | 41,07% | 32,54% |

**1. Phép tính đánh đổi trực tiếp.** Chuyển 1đ từ Brand sang Generic: mất 8,76đ doanh thu, được lại 1,25đ → **lỗ ròng 7,51đ trên mỗi 1đ chuyển**. Chuyển toàn bộ 260.219.000đ ngân sách Brand sang Generic → **mất khoảng 1.953.763.853đ doanh thu**, tức 62,4% doanh thu 90 ngày.

**2. Anh nói đúng một nửa — và tôi đã tính phần đúng đó.** Đúng là một phần công của Brand là "ăn theo" nhu cầu do kênh khác gieo. Sheet `10_GA4` mục D chứng minh điều đó bằng số: dưới mô hình **Dựa trên dữ liệu**, Brand chỉ được ghi công **401 lead thay vì 592 (−32,3%)**. Nhưng ngay cả khi chiết khấu Brand đúng bằng mức đó, **ROAS Brand vẫn là 5,93x** — vẫn gấp **4,7 lần** Generic và vẫn vượt xa KPI 3,0x. Kết luận không đổi.

**3. Brand đang thiếu tiền, không thừa tiền.** Impression Share Brand chỉ **53,01%**, trong đó **40,06% impression bị mất thuần túy vì hết ngân sách** (chỉ 6,93% do thứ hạng). Sheet `09_BENCHMARK` xếp IS thương hiệu < 60% vào ngưỡng báo động và ghi rõ mất IS ngân sách > 20% là "tiền đang bỏ lại trên bàn" — chúng ta đang ở **gấp đôi** ngưỡng đó. Ước tính bù đủ ngân sách: **+8,7 cọc ≈ 1,52 tỷ doanh thu** với chi phí thêm chỉ ~174 triệu.

**4. Cắt brand = mời đối thủ vào nhà.** 40,06% impression thương hiệu đang bỏ trống. Bất kỳ đại lý F2 nào cũng có thể mua chỗ đó với giá rẻ — vì Điểm chất lượng của họ trên tên "Vinhomes Hóc Môn" sẽ thấp hơn ta, nhưng ta không hiện diện thì họ vẫn thắng. Chi phí giữ 1 nhấp Brand hiện là **13.663đ**; chi phí 1 nhấp Generic là **33.070đ** — gấp 2,4 lần cho traffic có SQL/Lead thấp hơn 8,5 điểm %.

**5. Nếu phải cắt gì đó, cắt chỗ này trước.** 176.746.000đ ở SEA_Competitor (0 cọc, 0 doanh thu, CP/SQL 58.915.333đ) và 475.376.000đ ở PMax (0 cọc). Cắt hai chỗ đó được **652.122.000đ** — gấp 2,5 lần ngân sách Brand — mà không mất một đồng doanh thu nào.

> **Đề xuất chốt:** giữ nguyên logic của anh về "không trả tiền cho khách đã biết mình", nhưng thực thi nó bằng cách **hạ CPC thầu Brand xuống mức phòng thủ (trần 20.000đ)** thay vì cắt ngân sách — và đo bằng thí nghiệm: tắt Brand 7 ngày, đo lead organic có tăng bù không. **Tôi đề nghị KHÔNG làm thí nghiệm này trong 30 ngày trước sự kiện mở bán** vì rủi ro mất 13/18 nguồn cọc.

---

## D2. Đối thủ bắt đầu đấu giá trên tên thương hiệu dự án

**Trước hết — kiểm tra xem đã xảy ra chưa.** CTR Brand hiện tại là **11,63%**, nằm trong dải "trung bình ngành 8–12%" của sheet 09 và **chưa chạm ngưỡng báo động <6%**; mất IS do thứ hạng chỉ **6,93%** (so với 40,06% do ngân sách). Nghĩa là **áp lực cạnh tranh chưa xuất hiện trong số liệu 90 ngày qua** — vấn đề Brand hiện tại là tự bóp ngân sách, không phải bị đối thủ ép. Nếu đối thủ mới vào, chỉ số cần theo dõi là: CTR Brand tụt dưới 8%, CPC Brand vượt 20.000đ (hiện 13.663đ), mất IS thứ hạng vượt 15%.

### 4 hành động

**A. Trong Google Ads**

| # | Hành động | Chi tiết & ngưỡng số |
|---|---|---|
| 1 | **Khoá vị trí #1 tuyệt đối trên từ khoá thương hiệu chính** | Chuyển 3 từ khoá lõi (`vinhomes hóc môn`, `vinhomes hoc mon`, `dự án vinhomes hóc môn` — tổng 140.519.000đ, 234 SQL, sheet 04) sang **Đối sánh chính xác + tCPA cao / trần CPC 25.000đ**, mục tiêu IS tuyệt đối ≥ 90%. Kinh tế cho phép: CP/cọc Brand hiện 20.016.846đ, trần ROAS 3x là 60.333.333đ → còn dư địa để CPC tăng **3 lần** mà vẫn đạt KPI. Đồng thời tăng ngân sách Brand để đóng nốt 40,06% IS đang bỏ trống — **đối thủ không thể chen vào chỗ đã kín**. |
| 2 | **Nâng chất lượng & độ phủ mẫu quảng cáo Brand** | Hiện chỉ **1 RSA/nhóm** và **4 sitelink** (sheet 05). Thêm: 3 RSA/nhóm với tên dự án trong tiêu đề 1 (tăng điểm liên quan → hạ CPC), tiện ích **Cuộc gọi, Vị trí, Chú thích, Hình ảnh, Giá**. Chiếm nhiều diện tích SERP nhất có thể để đẩy đối thủ xuống dưới màn hình đầu. Mục tiêu: CTR Brand từ 11,63% lên **≥ 14%** (ngưỡng "tốt" sheet 09 là >12%). |

**B. Ngoài Google Ads**

| # | Hành động | Chi tiết & ngưỡng số |
|---|---|---|
| 3 | **Chiếm SERP tự nhiên + kênh chủ quyền** | Đối thủ chỉ mua được vị trí quảng cáo, không mua được kết quả tự nhiên. Xây/khoá top 3 tự nhiên cho `vinhomes hóc môn`, `vinhomes hóc môn giá bán`, `vinhomes hóc môn có thật không` (cụm này đang có 26 lead, 3 SQL — nhu cầu kiểm chứng có thật). Cộng: Google Business Profile tại nhà mẫu, kênh YouTube dự án. Mục tiêu: ≥ 30% lượt tìm tên dự án vào website ta qua kênh không mất phí trong 90 ngày. |
| 4 | **Thực thi quyền thương hiệu + bảo vệ narrative** | (a) Nếu đối thủ dùng chữ "Vinhomes" trong **nội dung quảng cáo** (không chỉ từ khoá) → nộp khiếu nại nhãn hiệu Google Ads (thường xử lý 5–10 ngày làm việc) và báo chủ đầu tư — đại lý F1 có nghĩa vụ báo. (b) Chạy **SEA_Brand_Defense** với LP so sánh trung thực + pháp lý, nhắm cụm `vinhomes hóc môn có thật không / review / lừa đảo`. (c) Theo dõi **Auction Insights hằng tuần** — nếu một đối thủ có Overlap Rate > 30% trên từ khoá brand thì cân nhắc đấu ngược tên họ (ngân sách 20.000.000đ đã dự phòng ở C1, và chỉ mở khi có bằng chứng này). |

**Điều tôi sẽ KHÔNG làm:** đấu giá trả đũa tràn lan trên tên đối thủ. Bằng chứng có sẵn: chiến dịch SEA_Competitor đã đốt **176.746.000đ**, tạo **3 SQL, 0 cọc**, và **26% lead là môi giới/đối thủ** (sheet 08C). Trả đũa cảm tính đã được thử và đã thất bại.

---

## D3. "PMax có CP/chuyển đổi thấp nhất, dồn ngân sách vào đó"

**Trả lời: Không đồng ý. Kế toán đang so bằng thước đo sai — và tôi có bảng chứng minh chính xác chỗ thước đo gãy.**

| Chiến dịch | CP/chuyển đổi Ads | CP/lead CRM | CP/SQL | CP/cọc | ROAS |
|---|---|---|---|---|---|
| **PMAX_VinhomesHM_Lead** | **267.817đ 🥇** | 573.433đ (2) | **7.793.049đ (5/6)** | **∞ — 0 cọc** | **0,00x** |
| SEA_Brand | 298.759đ (2) | **303.639đ 🥇** | **739.259đ 🥇** | **20.016.846đ 🥇** | **8,76x** |
| GDN_Remarketing | 430.493đ | 673.622đ | 3.611.361đ | ∞ — 0 cọc | 0,00x |
| YT_Video | 470.017đ | 1.410.051đ | 10.399.125đ | ∞ — 0 cọc | 0,00x |
| SEA_Generic | 1.021.075đ | 1.155.015đ | 3.549.707đ | 135.598.800đ | 1,25x |
| SEA_Competitor | 5.701.484đ | 5.523.312đ | 58.915.333đ | ∞ — 0 cọc | 0,00x |

**PMax đứng nhất ở cột đầu và gần bét ở mọi cột sau.** Xếp hạng đảo ngược ngay khi đổi mẫu số từ "chuyển đổi Ads" sang "SQL".

**Ba lý do bằng số:**

**1. "Chuyển đổi" của PMax phần lớn không phải lead.** PMax báo 1.775 chuyển đổi nhưng CRM chỉ nhận **829 lead** — tỷ lệ **2,14x**, vượt ngưỡng báo động 1,8x của sheet 09. Trong 973 sự kiện rác toàn tài khoản, **697 (71,6%) đến từ PMax** (438 `view_price_page` + 259 `engaged_30s`, sheet 10B). PMax rẻ vì nó đang được tính công cho những lượt xem trang và ở-lại-30-giây, tức những thứ **kế toán không thể ghi doanh thu**.

**2. Lead PMax 93% không dùng được.** Sheet `08_CRM_VAN_HANH` mục C, mẫu 160 lead: trùng SĐT **31%**, số sai/không liên lạc được **24%**, sai phân khúc (<2 tỷ trong khi sản phẩm 2,9–11,5 tỷ) **34%**, môi giới 4% → **chỉ 7% dùng được**. Quy đổi: 829 × 7% = **58 lead thật** → **chi phí thực trên 1 lead dùng được = 8.191.901đ**, tức **đắt gấp 27 lần** con số 267.817đ mà kế toán đang nhìn, và **đắt gấp 27 lần** CPL của Brand (303.639đ).

**3. Bằng chứng hành vi độc lập từ 2 công cụ khác.** Clarity: **74,3% phiên từ PMax thoát dưới 3 giây**, thời lượng phiên trung vị **3 giây**, và Clarity tự ghi "Bất thường — xem lại vị trí đặt quảng cáo". GA4: tỷ lệ tương tác PMax **8,7%** (trung bình tài khoản 32,4%), hao hụt nhấp → phiên **28,0%** — sheet 10B ghi rõ với YouTube thì hao hụt lớn là bình thường **"với PMax thì không"**. Ba nguồn số liệu độc lập cùng nói một điều.

**Phép thử quyết định:** dồn toàn bộ 2,1 tỷ vào PMax theo CP/SQL hiện tại → 269 SQL, và theo lịch sử 90 ngày (**0 cọc trên 475.376.000đ**) → **doanh thu 0đ, ROAS 0,00x**. Trong khi cùng số tiền đó vào Brand theo CP/cọc 20.016.846đ → về mặt lý thuyết ~105 cọc (thực tế bị giới hạn bởi tổng nhu cầu tìm kiếm thương hiệu, nên con số thật thấp hơn nhiều — nhưng hướng đi rõ ràng).

**Không đồng ý dồn — nhưng cũng không tắt.** Đề xuất: **giảm PMax từ 475.376.000đ (26,4%) xuống 320.000.000đ (15,2%)**, tái cấu trúc theo 4 điều kiện: (a) chỉ nhận tín hiệu chuyển đổi sạch sau khi dọn GA4; (b) đặt **tCPA 1.500.000đ**; (c) bật **brand exclusion** và **danh sách loại trừ vị trí đặt** (sheet 05: cả hai đang CHƯA thiết lập); (d) tín hiệu đối tượng = danh sách 651 SQL + 18 khách đã cọc. **Điều kiện dừng: SQL/Lead < 15% sau 30 ngày → tắt.**

> **Một câu cho kế toán:** *"CP/chuyển đổi là giá chúng ta trả cho một tiếng chuông. CP/cọc là giá chúng ta trả cho một tờ hợp đồng. PMax rẻ nhất ở tiếng chuông và chưa từng tạo ra tờ hợp đồng nào trong 90 ngày."*

---

## D4. Ngân sách bị cắt còn 1,2 tỷ cho 90 ngày

**Nguyên tắc: cắt theo ROAS biên tăng dần, giữ lại theo doanh thu tuyệt đối.** Cắt 900 triệu (−42,9%) không có nghĩa cắt đều mọi thứ 42,9%.

### Thứ tự cắt (từ trên xuống)

| Thứ tự | Cắt gì | Số tiền thu hồi | Doanh thu mất | Lý do |
|---|---|---|---|---|
| **1** | **SEA_Competitor — cắt 100%** | 40.000.000đ | 0đ | Lịch sử: 176.746.000đ → 3 SQL, 0 cọc, CP/SQL 58.915.333đ (gấp 11,8 lần ngưỡng báo động), 26% lead là môi giới/đối thủ |
| **2** | **YT_Video — cắt 100%** | 80.000.000đ | 0đ trực tiếp | 83.193.000đ → 8 SQL, 0 cọc, CP/SQL 10.399.125đ. Đây là chi tiêu đầu phễu — thứ đầu tiên phải bỏ khi tiền eo hẹp. *Chấp nhận mất: dưới DDA nó được ghi công 165 lead — đây là cái giá có ý thức* |
| **3** | **Dự phòng — cắt 44%** | 40.000.000đ | 0đ | Giữ lại 50 triệu cho test bắt buộc |
| **4** | **PMax — cắt 59%** (320tr → 130tr) | 190.000.000đ | 0đ | 0 cọc trên 475.376.000đ trong 90 ngày. Giữ 130 triệu vì (a) đây là kênh duy nhất phủ Discovery/Gmail/Maps, (b) sau khi dọn tín hiệu nó là chiến dịch **chưa từng được thử nghiệm tử tế** — nhưng chỉ với tCPA và exclusion đầy đủ |
| **5** | **GDN_Remarketing — cắt 38%** (130tr → 80tr) | 50.000.000đ | 0đ trực tiếp | 0 cọc, nhưng CP/SQL 3.611.361đ khá nhất trong nhóm không-cọc, và dưới DDA được ghi công 186 lead. Thu hẹp về **chỉ nhóm bỏ dở form** (5.743 người) — nhóm ý định cao nhất |
| **6** | **SEA_Generic — cắt 42%** (890tr → 520tr) | 370.000.000đ | ~ mất 2 cọc | Cắt bằng cách **bỏ hết đối sánh Rộng** và **chỉ giữ 5 cụm có SQL > 0** (sheet 04: `nhà phố hóc môn` 41 SQL, `căn hộ hóc môn giá bao nhiêu` 30 SQL, `mua nhà phố quận 12` 26 SQL, `khu đô thị tây bắc tphcm` 19 SQL, `nhà phố dưới 8 tỷ` 14 SQL). Chỉ riêng 17 cụm 0 SQL đã tiêu 419.729.000đ — cắt đúng chỗ này gần như **không mất SQL nào** |
| **7** | **SEA_Brand — CẮT CUỐI CÙNG, và chỉ giảm 24%** (550tr → 420tr) | 130.000.000đ | ~ mất 2–3 cọc | Vẫn **cao hơn 61% so với 260.219.000đ** của 90 ngày vừa qua. ROAS 8,76x, 13/18 cọc, CP/cọc chỉ 20.016.846đ. **Đây là thứ cuối cùng bị đụng đến.** |
| | **TỔNG THU HỒI** | **900.000.000đ** | | |

### Phân bổ 1,2 tỷ sau khi cắt

| Chiến dịch | Ngân sách | % |
|---|---|---|
| SEA_Generic_Cluster (chỉ lõi TP.HCM, Chính xác + Cụm từ) | 520.000.000đ | 43,3% |
| **SEA_Brand** | **420.000.000đ** | **35,0%** |
| PMAX_Feed_Lead (giới hạn, tCPA 1.500.000đ) | 130.000.000đ | 10,8% |
| GDN_Remarketing (chỉ nhóm bỏ dở form) | 80.000.000đ | 6,7% |
| Dự phòng / test | 50.000.000đ | 4,2% |
| SEA_Competitor | **0đ** | 0% |
| YT_Video | **0đ** | 0% |
| **TỔNG** | **1.200.000.000đ** | **100%** |

*Kiểm tra tổng bằng script: `sum(cut.values()) == 1_200_000_000` → **True**.*

### Dự báo và cam kết lại KPI

| Nếu CP/SQL đạt | SQL | Cọc | Doanh thu | ROAS |
|---|---|---|---|---|
| 1.800.000đ | 667 | **26,4** | 4.774.580.336đ | **3,98x** |
| 2.000.000đ | 600 | **23,7** | 4.297.122.302đ | **3,58x** |

**Điều tôi nói thẳng với ban giám đốc:** với 1,2 tỷ, **ROAS 3,0x vẫn đạt được (dự báo 3,58–3,98x), nhưng KPI 32 cọc thì KHÔNG**. Dự báo 24–26 cọc. Toán học rất đơn giản: 32 cọc × trần chi phí 60.333.333đ/cọc (để ROAS 3x) = **1.930.666.667đ** — không thể mua 32 cọc bằng 1,2 tỷ trừ khi CP/cọc xuống dưới **37.500.000đ**, tức tốt hơn 2,7 lần so với thực tế 90 ngày qua (100.196.500đ). **Cần chốt lại KPI: hoặc 24 cọc @ ROAS 3,5x, hoặc trả lại ngân sách.**

**Ba việc "0 đồng" phải làm bù cho phần ngân sách bị cắt** — đây mới là chỗ lấy lại cọc:
1. Sửa 3 lỗi kỹ thuật Clarity: **+370–480 lead**, chi phí = 2–5 ngày công dev.
2. Dọn cột Chuyển đổi (bỏ 973 sự kiện rác + khử trùng 353): chi phí = **0đ**, nhưng làm mọi đồng ngân sách còn lại được tiêu đúng chỗ.
3. Ép SLA gọi lại < 5 phút: ước tính **+19,7 cọc** (A1) — lớn hơn toàn bộ phần cọc mất do cắt ngân sách.

---

## D5. "GA4 báo 3.820, CRM báo 2.557. Ai đúng? Từ giờ tôi nhìn con số nào?"

> **Cả hai đều đúng — chúng đang đếm hai thứ khác nhau.**
>
> Con số 3.820 không phải là 3.820 khách hàng. Nó là 3.820 **lượt hành động** trên website, trong đó chúng ta đã lỡ đếm cả những việc không phải khách để lại thông tin:
>
> | Nội dung | Số |
> |---|---|
> | Khách điền form thật | 1.715 |
> | Người bấm gọi (số người thật) | 779 |
> | Bấm gọi nhiều lần — đếm trùng | 353 |
> | Chỉ **xem** trang bảng giá — chưa để lại thông tin | 612 |
> | Chỉ **ở lại** trang trên 30 giây | 361 |
> | **Cộng** | **3.820** |
>
> 973 lượt cuối là người xem hàng, chưa phải người mua. Cộng 353 lượt trùng nữa là **1.326 lượt (35%) không phải khách**. Còn CRM báo 2.557 vì có thêm 63 lead 3 ngày website đo hỏng.
>
> **Từ giờ anh nhìn 3 con số:** **số lead CRM**, **số lead chất lượng (SQL)**, **số cọc**. Google Ads chỉ để đội tôi lái máy. CRM để đánh giá đội tôi.

*(150 từ tính phần trong khung trích dẫn, không kể bảng)*

---

## D6. "Sửa GTM không tạo ra lead nào, để cuối quý. Giờ tăng ngân sách trước."

### Phản biện — 4 câu, mỗi câu một con số

**1. "Sửa đo lường không tạo lead" — sai theo nghĩa đen.** Ba lỗi kỹ thuật chưa sửa trong Clarity đang làm **370–480 lead không đến được với chúng ta** trong 90 ngày (sheet 11C). Riêng lỗi #4 — `TypeError e.setDate is not a function` trên Safari iOS — khiến **form không gửi được và không báo lỗi cho khách**: khách bấm gửi, tưởng xong, chúng ta không bao giờ nhận được. Sửa nó **tạo ra 280–340 lead** với chi phí 2–5 ngày công dev. Không có thay đổi giá thầu nào trong tài khoản này có ROI bằng.

**2. Tăng ngân sách trước khi sửa đo lường = nhân lãng phí lên, không nhân doanh thu.** **34,7% cột Chuyển đổi (1.326/3.820) không phải lead** (B6). Máy học đang tối ưu theo tín hiệu đó — sheet `12_GTM` mục C viết thẳng: *"Máy học tối ưu theo tín hiệu rác — nguyên nhân gốc của toàn bộ vấn đề PMax."* Kết quả cụ thể của việc đó: **475.376.000đ vào PMax, 0 cọc**. Bơm thêm 500 triệu vào hệ thống này thì 26,4% của nó lặp lại đúng số phận. **Ngân sách nhân lên sai lầm, nó không sửa sai lầm.**

**3. Chúng ta đã có bằng chứng thực nghiệm về giá của việc "để sau".** Ngày 44, dev đổi một class CSS. Đo lường gãy. **Không ai biết trong 3 ngày** vì không có cảnh báo (sheet 12A mục 18). Kết quả: **63 lead vĩnh viễn không có trong Google Ads**, 59.528.000đ ngân sách chạy trong khi thuật toán nhận tín hiệu "0 chuyển đổi". Cái cảnh báo lẽ ra chặn được việc này mất **nửa ngày công** để dựng. "Để cuối quý" nghĩa là chấp nhận sự cố đó có thể lặp lại 2–3 lần nữa.

**4. Không có GCLID trong CRM thì việc "tăng ngân sách" về mặt kỹ thuật là bịt mắt.** Chênh CP/SQL giữa Brand (739.259đ) và PMax (7.793.049đ) là **10,5 lần** — nhưng Google **không hề biết** sự khác biệt đó, vì nó chưa từng nhận được tín hiệu nào cho biết lead nào thành SQL, lead nào thành cọc. Cài GCLID vào form (~1 ngày công) là điều kiện tiên quyết duy nhất để mở khoá nhập chuyển đổi ngoại tuyến — con đường thực tế duy nhất để hạ CP/SQL từ 2.770.410đ xuống dưới KPI 2.200.000đ.

### Đề nghị thoả hiệp có thời hạn

> "Cho tôi **2 tuần và 3 ngày công dev**. Trong 2 tuần đó tôi vẫn giữ nguyên ngân sách hiện tại — không xin thêm một đồng. Đến ngày 15 tôi trình 3 con số: chênh Ads/CRM, tỷ lệ lỗi JS di động, tỷ lệ bản ghi CRM có GCLID. Đạt cả ba thì mới bàn tăng ngân sách. Không đạt, anh cắt phần đo lường."

### Nếu buộc phải nhượng bộ — tôi giữ đúng HAI hạng mục

| # | Hạng mục giữ lại | Công sức | Vì sao là hai thứ này |
|---|---|---|---|
| **1** | **Dọn cột "Chuyển đổi"**: bỏ `view_price_page` (612) và `engaged_30s` (361) khỏi sự kiện chính + khử trùng `click_to_call` (353) | **~2 giờ, thao tác trong giao diện GA4/Ads, KHÔNG cần dev** | Loại bỏ **1.326 tín hiệu sai (34,7%)** đang lái toàn bộ bidding tự động. Đây là hạng mục có **tỷ lệ tác động/công sức cao nhất trong toàn bộ danh sách** — và nó không tốn một giờ nào của đội IT, nên lý do "IT bận" không áp dụng. Nếu chỉ được làm một việc duy nhất, đây là việc đó. |
| **2** | **Biến ẩn lưu GCLID vào form → CRM** | **~1 ngày công dev** | Đây là hạng mục **duy nhất có tính chất một-chiều-không-thể-làm-bù**: dữ liệu GCLID không lưu hôm nay thì **vĩnh viễn mất**, không thể truy hồi vào cuối quý. Mọi thứ khác (sGTM, Consent Mode, gỡ thẻ thừa) có thể lùi mà không mất dữ liệu lịch sử. Không có GCLID = quý sau vẫn không thể nhập chuyển đổi ngoại tuyến = vẫn không thể tối ưu theo cọc. **Trì hoãn 1 quý = mất vĩnh viễn 1 quý dữ liệu huấn luyện.** |

**Bổ sung 30 phút nếu xin được:** dựng cảnh báo "chuyển đổi = 0" trong GA4. Không phải hạng mục lớn nhưng là bảo hiểm rẻ nhất trong danh sách — sự cố N44–46 đã chứng minh giá của việc thiếu nó là 63 lead.

**Tôi chấp nhận lùi (nói rõ để anh biết mình đang đánh đổi gì):** vùng chứa phía máy chủ, Consent Mode v2, Clarity ID vào CRM, kiểm toán thẻ đối tác F2, Enhanced Conversions. Năm hạng mục này quan trọng nhưng **có thể làm bù**, và không hạng mục nào trong đó mất dữ liệu vĩnh viễn khi trì hoãn.

---

# PHẦN E — KẾ HOẠCH 7 NGÀY ĐẦU

10 việc, sắp theo thứ tự ưu tiên (làm từ trên xuống). Nguyên tắc chọn: **việc chặn máu và việc miễn phí lên trước; việc cần dev đi song song; việc cần dữ liệu mới đi cuối.**

| # | Ngày | Việc | Ai làm | Kết quả kỳ vọng (ĐO ĐƯỢC) |
|---|---|---|---|---|
| **1** | **N1 (sáng)** | **Dọn cột "Chuyển đổi"**: bỏ `view_price_page` (612) và `engaged_30s` (361) khỏi sự kiện chính GA4 + ngắt nhập vào Ads; đổi `click_to_call` sang đếm theo người dùng (1 lần/phiên) | Tôi, ~2 giờ, không cần dev | Cột Chuyển đổi giảm **1.326 lượt (−34,7%)** trong 7 ngày kế; chênh **Ads/CRM từ 1,49x → 1,0–1,2x**; riêng PMax từ 2,14x → ≤ 1,3x. *Cảnh báo trước cho ban giám đốc: báo cáo sẽ "giảm 35% chuyển đổi" — đó là sửa số, không phải sụt hiệu quả.* |
| **2** | **N1 (chiều)** | **Dựng cảnh báo tự động "chuyển đổi = 0"** cho từng chiến dịch đang tiêu > 2 triệu/ngày (GA4 custom alert + script kiểm tra 09:00 hằng ngày, gửi Zalo) | Tôi, ~30 phút | Diễn tập tắt thẻ ở staging → **nhận cảnh báo trong ≤ 2 giờ**. Bảo hiểm cho sự cố kiểu N44–46 (đã mất 63 lead + 59.528.000đ) |
| **3** | **N1** | **Giao dev sửa 3 lỗi Clarity chưa sửa** (deadline N5): #4 `TypeError e.setDate` Safari iOS (4.196 phiên), #5 nút CTA bị khung chat che <380px (2.741 phiên), #6 `tel:` không phản hồi trên desktop (1.204 phiên) | Dev, 2–5 ngày công | N7: tỷ lệ phiên có **lỗi JS trên di động từ 8,9% → < 2%**; nhấp chết < 5%; tỷ lệ hoàn tất form di động **từ 24,6% → ≥ 30%**. Giá trị: **370–480 lead/90 ngày ≈ 471–612 triệu hoa hồng** |
| **4** | **N2** | **Chặn máu ngân sách — 3 thao tác một lần**: (a) tạm dừng SEA_Competitor (176.746.000đ/90ngày, 0 cọc); (b) thu hẹp địa lý còn TP.HCM + Bình Dương + Long An + Đồng Nai, đổi tùy chọn vị trí sang **"Hiện diện"**; (c) loại trừ Hà Nội, Đà Nẵng, Cần Thơ | Tôi, ~1 giờ | Thu hồi ngay ≈ **6,0 triệu/ngày** (176.746.000 + 364.314.474 = 541.060.474đ trên 90 ngày ở vùng 0 cọc). Kiểm tra N7: chi phí ngoài 4 tỉnh mục tiêu = **0đ** |
| **5** | **N2** | **Nạp danh sách phủ định chia sẻ ≥ 250 từ** (hiện tài khoản chỉ có **12 từ**, không dùng danh sách chia sẻ), bắt đầu từ 10 cụm sai ý định trong sheet 04: `tuyển dụng`, `việc làm`, `học phí`, `thuê`, `nhà trọ`, `kho xưởng`, `quy hoạch`, `lừa đảo`, `chung cư mini`, `100 triệu` | Tôi, ~2 giờ | Chặn ≈ **209.082.000đ/90 ngày** chi phí sai ý định (0 SQL). N7: 0 nhấp từ các cụm chứa từ phủ định; **CTR Generic từ 4,47% → ≥ 5,0%** |
| **6** | **N3** | **Giao dev cài biến ẩn lưu GCLID/GBRAID/WBRAID vào form → CRM** (deadline N7) + đăng ký cột GCLID trong CRM | Dev, ~1 ngày công | N7: gửi 10 form test qua link `?gclid=test###` → **10/10 bản ghi CRM có GCLID**. Mở khoá nhập chuyển đổi ngoại tuyến — điều kiện tiên quyết duy nhất để tối ưu theo SQL/cọc |
| **7** | **N3** | **Chốt SLA gọi lead với Giám đốc kinh doanh bằng văn bản**: gọi < 5 phút trong giờ hành chính, auto-responder Zalo/SMS ngoài giờ, 0 lead bị bỏ sót; kèm bảng sheet 08A trình bày trong 5 phút | Tôi + GĐKD | Cam kết văn bản + dashboard theo dõi. Mục tiêu 30 ngày: lead gọi < 5 phút **từ 11% → ≥ 70%**; lead bỏ sót **từ 275/90ngày → 0**. Giá trị ước tính **+19,7 cọc ≈ 3,56 tỷ** — hạng mục lớn nhất toàn bộ danh sách |
| **8** | **N4** | **Đặt trần cho bidding**: Generic + Competitor đang chạy "Tối đa hóa số lần nhấp **không đặt trần CPC**" (CPC thực tế 33.070đ và 55.164đ) → chuyển Generic sang **Tối đa hóa chuyển đổi + tCPA 1.200.000đ**; PMax từ "Tối đa hóa chuyển đổi" trần trụi → **tCPA 1.500.000đ**, bật **brand exclusion** + **danh sách loại trừ vị trí đặt** (cả hai đang CHƯA thiết lập) | Tôi, ~2 giờ | N7: **CPC Generic ≤ 28.000đ** (−15%); PMax: tỷ lệ **thoát-nhanh-<3s từ 74,3% → ≤ 50%** sau 14 ngày; **hao hụt nhấp→phiên từ 28,0% → ≤ 20%** |
| **9** | **N5** | **Bật lịch quảng cáo + điều chỉnh giá thầu** (hiện 24/7, không điều chỉnh gì): −60% khung 23:00–06:00 (8,1% chi phí, 40 SQL, **0 cọc**); −40% khung 20:00–23:00 (18,7% chi phí, chỉ 21% được gọi lại <30'); +20% khung 09:00–12:00 (93% gọi lại <30', CP/SQL tốt nhất 2.504.084đ); −20% giá thầu di động (CP/SQL 3.042.251đ vs máy tính 1.847.796đ); −30% T7–CN (27,9% chi phí nhưng chỉ 2/8 sale trực) | Tôi, ~2 giờ | N7: chi phí khung 20:00–06:00 **từ 26,8% → ≤ 12%** tổng chi phí; **CP/SQL toàn tài khoản từ 2.770.410đ → ≤ 2.500.000đ** trong 14 ngày |
| **10** | **N6–N7** | **Dựng bảng đối chiếu 3 nguồn hằng tuần + họp bàn giao số liệu**: bảng Ads / GA4 / CRM cho từng chiến dịch, cột "chênh lệch" phải giải thích được 100%; kèm phễu Lead→SQL→Xem→Booking→Cọc theo chiến dịch. Gỡ thẻ GA4 Configuration trùng (`Copy of Main`, bắn page_view 2 lần từ N31) | Tôi, ~4 giờ | 1 bảng chuẩn cập nhật hằng tuần, **0 dòng "không rõ nguyên nhân"**. GTM Preview: `page_view` **chỉ bắn 1 lần**. Ban giám đốc từ tuần 2 nhận báo cáo theo **CRM lead / SQL / cọc**, không theo cột Chuyển đổi của Ads |

### Chỉ số nghiệm thu cuối ngày 7

| Chỉ số | Trước (90 ngày qua) | Mục tiêu N7 |
|---|---|---|
| Chênh Ads/CRM | 1,49x (PMax 2,14x) | **1,0 – 1,2x** (mọi chiến dịch ≤ 1,3x) |
| Sự kiện rác trong cột Chuyển đổi | 973 (25,5%) | **0** |
| Tỷ lệ phiên lỗi JS di động | 8,9% | **< 2%** |
| Bản ghi CRM mới có GCLID | 0% | **≥ 95%** |
| Chi phí ở khu vực ngoài 4 tỉnh mục tiêu | 20,2% ngân sách | **0%** |
| Từ khóa phủ định | 12 | **≥ 250** (danh sách chia sẻ) |
| Cảnh báo chuyển đổi = 0 | Không có | **Đang chạy, đã diễn tập** |
| Chiến dịch chạy không có trần giá thầu | 3 | **0** |
| Lead được gọi < 5 phút | 11% | **≥ 40%** (lộ trình lên 70% trong 30 ngày) |

### Việc CỐ TÌNH KHÔNG làm trong tuần 1 (và lý do)

| Không làm | Vì sao |
|---|---|
| Tăng ngân sách | Tín hiệu chuyển đổi chưa sạch — tăng tiền lúc này là nhân lãng phí (D6, luận điểm 2) |
| Tắt hẳn PMax | 26,4% ngân sách; tắt đột ngột làm mất dữ liệu đối chứng. Siết bằng tCPA + exclusion trước, đánh giá ở ngày 30 theo tiêu chí SQL/Lead < 15% |
| Đổi hàng loạt sang bidding tự động | Bidding tự động học từ dữ liệu chuyển đổi. Dữ liệu đang bẩn 34,7%. Chờ ≥ 14 ngày tín hiệu sạch (điều kiện chuyển đổi chiến lược ở C3) |
| Viết lại toàn bộ trang đích | v2 (LCP 1,9s, form 3 trường, hoàn tất form 28,0%) đang hoạt động tốt. Sửa 3 lỗi trước, A/B test sau — không đập đi xây lại thứ đang chạy được |
| Tắt Search Partners / Display in Search | **Không đủ dữ liệu** — bộ đề không có báo cáo phân đoạn theo mạng. Cần kéo báo cáo này trong tuần 1 rồi mới quyết ở tuần 2 |

---

## PHỤ LỤC — Dữ liệu còn thiếu để kết luận chắc hơn

| Câu hỏi chưa trả lời được | Cần dữ liệu gì |
|---|---|
| Search Partners và Mạng hiển thị-trong-Search đang tiêu bao nhiêu, tạo bao nhiêu SQL? | Báo cáo phân đoạn **theo mạng** trong Google Ads (không có trong bộ đề) |
| Đối thủ nào đang đấu tên thương hiệu, cường độ ra sao? | **Auction Insights** cho SEA_Brand (không có trong bộ đề) |
| PMax đang hiển thị ở đâu? | Báo cáo **vị trí đặt** / Insights của PMax (không có trong bộ đề) |
| Impression biên của Brand đến từ truy vấn nào — có đáng mua không? | Báo cáo Chẩn đoán từ khóa + search terms theo tuần |
| Ước tính lead mất do lỗi kỹ thuật có chính xác không? | % phiên Safari iOS/tổng phiên di động; tỷ lệ hoàn tất form nhóm đối chứng không gặp lỗi; % thiết bị <380px |
| Kênh khác (Facebook, Zalo, telesale, sàn F2) đang đóng góp bao nhiêu vào 18 cọc? | Dữ liệu đa kênh — sheet 01 ghi rõ **KHÔNG nằm trong dữ liệu này**. ⇒ **Mọi kết luận trong báo cáo này chỉ áp dụng trong phạm vi Google Ads.** 71 lead được DDA gán cho Trực tiếp/Organic (sheet 10D) là bằng chứng có ảnh hưởng ngoài Ads chưa đo được |
| Tỷ lệ cọc/SQL 3,96% của GĐ3-Search có bền không? | Cỡ mẫu chỉ **11 cọc** — cần ≥ 60 ngày dữ liệu nữa để tin cậy. Đây là **rủi ro lớn nhất của kế hoạch phần C** |
| Sheet 06 báo 2.566 lead, sheet 02 báo 2.557 | Lệch 9 lead do sheet 06 phân bổ theo % chi phí làm tròn. Đã dùng sheet 02 làm chuẩn |
