# BÁO CÁO TIẾP QUẢN TÀI KHOẢN GOOGLE ADS — VINHOMES HÓC MÔN
**Vai trò:** Performance Marketing Lead, An Phát Land · **Kỳ dữ liệu:** 02/03/2026 – 30/05/2026 (90 ngày)
**Script tính:** `answers/agent-2-calc.py` (stdlib `csv`, không pandas — mọi số dưới đây truy ngược được về output của script này)

---

## TÓM TẮT ĐIỀU HÀNH (6 dòng)

| Chỉ số 90 ngày qua | Thực tế | KPI 90 ngày tới | Khoảng cách |
|---|---|---|---|
| Chi phí | 1.803.537.000đ | 2.100.000.000đ | +16,4% ngân sách |
| Đặt cọc | **18** | ≥ 32 | **+78%** |
| ROAS | **1,74x** | ≥ 3,0x | **+72%** |
| CP/SQL | **2.770.410đ** | ≤ 2.200.000đ | **−20,6%** |
| CP/cọc | 100.196.500đ | ≤ 60.333.333đ (hòa vốn ROAS 3,0x) | −39,8% |

Ba câu chốt:
1. **38,2% ngân sách (688.578.000đ) chảy vào PMax + GDN + YouTube — 3 kênh này tạo ra 0 cọc, 0 doanh thu.** Nguồn: CSV `Chi_phi`/`Dat_Coc`/`DoanhThu_HoaHong`, gộp theo `Chien_dich`, toàn kỳ.
2. **Nguyên nhân gốc là đo lường, không phải đấu thầu.** 1.326/3.820 chuyển đổi Ads (34,7%) là sự kiện rác hoặc đếm trùng (sheet `10_GA4` mục A) — máy học của PMax đang được huấn luyện bằng tín hiệu sai từ ngày đầu (GTM v18, sheet `12_GTM` mục B).
3. **Chiến dịch tốt nhất đang bị bóp ngân sách.** Brand ăn 14,4% chi phí nhưng tạo 13/18 cọc (72%) và 2,28/3,13 tỷ doanh thu (73%), ROAS 8,76x — mà mất 40,4% Impression Share vì hết ngân sách (CSV cột `Mat_IS_NganSach`, TB 90 ngày).

---

# PHẦN A — CHẨN ĐOÁN

**18 vấn đề, sắp theo tác động tài chính giảm dần.** Trong đó 6 vấn đề thuộc nhóm đo lường/kỹ thuật (A2, A7, A10, A13, A14, A15) — vượt yêu cầu tối thiểu 3.

> Quy ước: "lãng phí" = tiền đã chi không tạo SQL/cọc. "Bỏ lỡ" = doanh thu hoa hồng ước tính không thu được. Mọi ước tính đều ghi rõ giả định.

---

### A1 — PMax là hố đen ngân sách: 475,4 triệu, 0 cọc, tỷ lệ SQL 7,4%
**Mức độ: CAO — lãng phí trực tiếp ≈ 400–475 triệu đồng**

| Chỉ số PMax (toàn kỳ) | Giá trị | Đối chiếu |
|---|---|---|
| Chi phí | 475.376.000đ (26,4% tài khoản) | lớn thứ 2 tài khoản |
| Chuyển đổi Ads báo | 1.775 | — |
| Lead CRM thật | 829 | tỷ lệ thổi phồng **2,14x** (ngưỡng báo động sheet `09` = >1,8x) |
| SQL | **61** → SQL/Lead **7,4%** | ngưỡng báo động sheet `09` = <12% |
| Đi xem nhà / Booking / **Cọc** | 10 / 2 / **0** | — |
| CP/SQL | **7.793.049đ** | ngưỡng báo động sheet `09` = >5.000.000đ |
| CP/lead dùng được (7% theo sheet `08C`) | **8.191.901đ** | Brand: 453.193đ → **gấp 18x** |

Ba bằng chứng độc lập xác nhận traffic PMax là rác, không phải vấn đề "chưa đủ thời gian học":
- `11_CLARITY` mục B: PMax **74,3% phiên thoát dưới 3 giây**, thời lượng phiên trung vị **3 giây** — Clarity tự ghi chú "Bất thường — xem lại vị trí đặt quảng cáo".
- `10_GA4` mục B: tỷ lệ tương tác **8,7%** (Brand 62,4%), **1,09 trang/phiên**, cuộn 90% chỉ **4%**, hao hụt click→phiên **28,0%** (39.701 click → 28.585 phiên).
- `08C`: 31% lead PMax trùng số điện thoại, 24% số sai — chỉ **7% lead dùng được** (thấp nhất tài khoản).

PMax cũng chưa bật brand exclusion và chưa có danh sách loại trừ vị trí đặt (sheet `05`) → đang tự ăn traffic Brand và chạy trên app rác.

---

### A2 — [ĐO LƯỜNG] 4 hành động chuyển đổi, 2 trong đó không phải khách hàng tiềm năng — nguyên nhân gốc của A1
**Mức độ: CAO — điều khiển sai 688.578.000đ ngân sách máy học (PMax+GDN+YT)**

Sheet `05_CAU_HINH_TK` + `10_GA4` mục E + `12_GTM` mục A (thẻ 5, 6, 8):

| Sự kiện nhập vào cột "Chuyển đổi" | Số lượt | Có phải KH tiềm năng? | Tỷ trọng |
|---|---|---|---|
| generate_lead | 1.715 | Có | 44,9% |
| click_to_call (tổng lượt) | 1.132 | Có, nhưng **đếm trùng 353 lượt** | 29,6% |
| **view_price_page** | **612** | **KHÔNG** | 16,0% |
| **engaged_30s** | **361** | **KHÔNG** | 9,4% |
| **Tổng** | **3.820** | tín hiệu rác/trùng = **1.326 (34,7%)** | |

`12_GTM` mục C ghi thẳng: *"Máy học tối ưu theo tín hiệu rác — nguyên nhân gốc của toàn bộ vấn đề PMax"*. Và `12_GTM` mục B v18 (**trước ngày 1**): *"Chuyển đổi bị thổi phồng ngay từ ngày đầu tiên"*.

Cơ chế: `view_price_page` và `engaged_30s` cực dễ đạt trên traffic rác — PMax gom 438 view_price_page + 259 engaged_30s (`10_GA4` mục B) = 697/1.775 chuyển đổi PMax (39,3%) là sự kiện không phải lead. Smart bidding "Tối đa hóa chuyển đổi, không đặt CPA mục tiêu" (sheet `05`) vì thế được thưởng khi mua traffic bounce-3-giây. **Không sửa hạng mục này thì mọi tối ưu đấu thầu đều vô nghĩa.**

---

### A3 — Brand bị bóp ngân sách trong khi là nguồn cọc duy nhất có ý nghĩa
**Mức độ: CAO — doanh thu bỏ lỡ ước tính ≈ 1,62 tỷ đồng**

| | Brand | Toàn tài khoản | Tỷ lệ |
|---|---|---|---|
| Chi phí | 260.219.000đ | 1.803.537.000đ | **14,4%** |
| Đặt cọc | **13** | 18 | **72,2%** |
| Doanh thu HH | 2.280.000.000đ | 3.130.000.000đ | **72,8%** |
| ROAS | **8,76x** | 1,74x | 5,0x tốt hơn |
| CP/cọc | 20.016.846đ | 100.196.500đ | rẻ hơn 5,0x |
| CP/SQL | 739.259đ | 2.770.410đ | ngưỡng "tốt" sheet `09` = <1,8tr ✔ |

Nhưng (CSV cột `Impr_Share`, `Mat_IS_NganSach`, TB 90 ngày):

| Chiến dịch | Impression Share | Mất IS do ngân sách | Mất IS do thứ hạng |
|---|---|---|---|
| **SEA_Brand** | **52,6%** | **40,4%** | 7,0% |
| SEA_Generic | 71,2% | 23,7% | 5,1% |
| SEA_Competitor | 57,7% | 35,9% | 6,4% |

Ngưỡng sheet `09`: IS thương hiệu <60% là "báo động"; mất IS do ngân sách >20% ở chiến dịch tốt là "tiền đang bỏ lại trên bàn". Brand đang ở **52,6% / 40,4%** — vi phạm cả hai, và tệ nhất ở GĐ2 (IS 48,9%, mất NS 43,8%).

**Ước tính cơ hội (giả định tuyến tính — là ƯỚC TÍNH, không phải số đo):** kéo IS Brand từ 52,6% lên 90% = hệ số lưu lượng ×1,71 → chi phí Brand tăng lên ~445,2 triệu (+185,0 triệu), cọc ~22,2 (+9,2 cọc), doanh thu ~3,90 tỷ (+1,62 tỷ). Cần thêm dữ liệu: đường cong CPC theo IS ở dải 52%→90% để biết chi phí biên có tuyến tính không.

---

### A4 — Từ khóa đối sánh rộng mua traffic sai mục đích: 242,98 triệu, 0 SQL
**Mức độ: CAO — lãng phí 242.982.000đ (13,5% tài khoản)**

Sheet `04_SEARCH_TERMS`, 11 cụm từ có ≥40 click và **0 SQL**:

| Cụm từ | Đối sánh | Chi phí | Lead | SQL |
|---|---|---|---|---|
| giá đất hóc môn 2026 | Rộng | 33.900.000đ | 29 | 0 |
| bản đồ quy hoạch hóc môn | Rộng | 27.120.000đ | 6 | 0 |
| thuê nhà nguyên căn hóc môn | Rộng | 27.120.000đ | 6 | 0 |
| bán đất thổ cư hóc môn 100 triệu | Rộng | 27.120.000đ | 6 | 0 |
| nhà trọ hóc môn giá rẻ | Rộng | 20.340.000đ | 4 | 0 |
| cho thuê kho xưởng hóc môn | Rộng | 20.340.000đ | 4 | 0 |
| việc làm bất động sản hóc môn | Rộng | 20.340.000đ | 4 | 0 |
| nhà đất hóc môn lừa đảo | Rộng | 20.340.000đ | 4 | 0 |
| chung cư mini gò vấp | Rộng | 20.340.000đ | 18 | 0 |
| **vinhomes hóc môn tuyển dụng** | Rộng | 15.613.000đ | 11 | 0 |
| **vinschool hóc môn học phí** | Rộng | 10.409.000đ | 4 | 0 |
| **TỔNG** | | **242.982.000đ** | 96 | **0** |

Đây là các cụm từ **không thể mua nhà 6,8–11,5 tỷ**: tuyển dụng, học phí, nhà trọ, kho xưởng, đất 100 triệu. 2 cụm cuối còn ăn ngân sách Brand. Cấu hình gây ra (sheet `05`): **71% chi phí Search là đối sánh rộng**, chỉ **12 từ khóa phủ định** toàn tài khoản, **không dùng danh sách phủ định chia sẻ**, 31 từ khóa/nhóm quảng cáo.

---

### A5 — Chiến dịch Competitor: 176,75 triệu, 3 SQL, 0 cọc
**Mức độ: CAO — lãng phí 176.746.000đ (9,8% tài khoản)**

| Chỉ số | Competitor | Chuẩn tham chiếu |
|---|---|---|
| Chi phí | 176.746.000đ | — |
| Lead CRM | 32 | — |
| SQL | **3** (SQL/Lead 9,4%) | ngưỡng báo động <12% |
| Đặt cọc / Doanh thu | **0 / 0đ** | — |
| CP/SQL | **58.915.333đ** | ngưỡng báo động >5tr → **gấp 11,8x** |
| CPC TB | 55.164đ | ngưỡng báo động sheet `09` >60.000đ (sát) |
| CTR | 2,39% | ngưỡng báo động Search generic <2% |

`11_CLARITY` mục B: Competitor thoát nhanh <3s **34,1%**, phiên trung vị 47 giây, chỉ 22,4% xem >2 trang — "Ý định thấp". `08C`: **26% lead là môi giới/đối thủ** (cao nhất tài khoản), chỉ 26% lead dùng được.

Đáng chú ý: 4/6 cụm từ Competitor là đối sánh **Rộng** trên tên dự án đối thủ ("izumi city đồng nai", "aqua city có nên mua") — traffic Đồng Nai, sai địa bàn hoàn toàn.

---

### A6 — Nhắm mục tiêu toàn quốc: 364,3 triệu chảy ra ngoài vùng bán được, 0 cọc
**Mức độ: CAO — lãng phí 364.314.474đ; cơ hội tái phân bổ ≈ 645 triệu doanh thu**

Sheet `06_DIA_LY`:

| Khu vực | Chi phí | SQL | Cọc | CP/SQL |
|---|---|---|---|---|
| Hà Nội | 155.104.182đ | 20 | **0** | 7.755.209đ |
| Cần Thơ & ĐBSCL | 93.783.924đ | 12 | **0** | 7.815.327đ |
| Đà Nẵng | 86.569.776đ | 7 | **0** | **12.367.111đ** |
| Ngoài Việt Nam | 28.856.592đ | 7 | **0** | 4.122.370đ |
| **Cộng 4 vùng** | **364.314.474đ (20,2%)** | **46 (7,2% SQL)** | **0** | **7.919.880đ** |
| — so sánh: TP.HCM Q.12 | 201.996.144đ | 97 | 4 | 2.082.434đ |

Nếu 364,3 triệu này chạy ở vùng lõi HCM với CP/SQL 2.082.434đ → ~175 SQL thay vì 46 (**+129 SQL**), quy theo SQL→Cọc lịch sử 2,76% = **+3,6 cọc ≈ +645 triệu hoa hồng** (ước tính, giả định CP/SQL vùng lõi giữ nguyên khi tăng lưu lượng).

Nguyên nhân cấu hình (sheet `05`): vị trí = **Việt Nam toàn quốc**, tùy chọn = **"Hiện diện HOẶC quan tâm"** (mặc định, chưa từng chỉnh), **không có loại trừ vị trí** nào. Đà Nẵng CP/SQL 12,4 triệu = gấp 4,4x toàn tài khoản.

---

### A7 — [ĐO LƯỜNG] Lỗi kỹ thuật CHƯA SỬA đang chặn 370–480 lead
**Mức độ: CAO — chi phí đã trả cho lead không nhận được 261–339 triệu; doanh thu bỏ lỡ 471–612 triệu**

Sheet `11_CLARITY` mục C, 3 lỗi trạng thái "CHƯA SỬA" (áp dụng cho **cả v1 và v2**, tức vẫn đang chảy máu hôm nay):

| # | Lỗi | Phiên ảnh hưởng | Lead mất (ước tính đội UX) | Giá trị theo CPL_CRM 705.333đ |
|---|---|---|---|---|
| 4 | `TypeError: e.setDate is not a function` — bộ chọn ngày hẹn xem nhà, Safari iOS 17.x, **form không gửi được và không báo lỗi** | 4.196 | 280–340 | 197,5 – 239,8 triệu |
| 5 | Nút "Đăng ký nhận bảng giá" bị khung chat che ở màn hình <380px | 2.741 | 60–90 | 42,3 – 63,5 triệu |
| 6 | Hotline `tel:` không phản hồi trên máy tính — 1.847 nhấp chết | 1.204 | 30–50 | 21,2 – 35,3 triệu |
| | **TỔNG CHƯA SỬA** | | **370–480** | **261,0 – 338,6 triệu** |

Xác nhận chéo: `11_CLARITY` mục A ghi rõ *"tỷ lệ lỗi JavaScript trên di động KHÔNG giảm sau khi lên trang đích v2 (9,3% → 8,9%)"* — tức lỗi #4 sống sót qua cả lần thay landing page. Di động chiếm 78,1% chi phí (sheet `07B`) nên đây là lỗi trên bề mặt đắt nhất. Chi tiết quy đổi tiền ở **B7**.

---

### A8 — Vận hành CRM: 47% lead được gọi lại sau 2 giờ, 275 lead không ai gọi
**Mức độ: CAO — 275 lead bỏ sót ≈ 194 triệu chi phí đã trả; trần cơ hội ≈ 2,74 tỷ hoa hồng**

Sheet `08_CRM_VAN_HANH` mục A (2.554 lead):

| Thời gian gọi lần đầu | Số lead | % | Liên hệ được | Đồng ý đi xem | **Tỷ lệ cọc** |
|---|---|---|---|---|---|
| Dưới 5 phút | 281 | 11% | 87% | 23,1% | **1,82%** |
| 5–30 phút | 485 | 19% | 74% | 15,4% | 1,21% |
| 30 phút–2 giờ | 588 | 23% | 58% | 8,6% | 0,58% |
| 2–12 giờ | 536 | 21% | 41% | 4,2% | 0,21% |
| **Trên 12 giờ** | **664** | **26%** | **22%** | 1,1% | **0,04%** |

Lead gọi <5 phút cọc **gấp 45,5 lần** lead gọi sau 12 giờ. **47,0% lead (1.200) đang rơi vào 2 nhóm tệ nhất.**

Mô hình hóa (dùng đúng tỷ lệ cọc từ bảng trên, áp lên 2.554 lead):
- Mix hiện tại → 15,8 cọc kỳ vọng (thực tế 18 — sai lệch 12%, chấp nhận được cho mô hình).
- Nếu 100% gọi trong 30 phút → 30,9 cọc (**+15,1 cọc ≈ +2,74 tỷ hoa hồng**).
- Nếu 100% gọi trong 5 phút → 46,5 cọc (**+30,7 cọc ≈ +5,56 tỷ**) — đây là **trần lý thuyết**, không đạt được thực tế.

Sheet `08B`: **275 lead bị bỏ sót hoàn toàn** (118+96+61) qua 3 giai đoạn = 193.966.631đ chi phí đã trả không có ai gọi. Tin tốt: thời gian phản hồi trung vị đã giảm 214 → 142 → **47 phút** qua 3 giai đoạn nhờ SLA 15 phút ở GĐ3 — nhưng vẫn gấp 9,4x ngưỡng "tốt" (<5 phút, sheet `09`).

---

### A9 — Landing page v1 chạy 57/90 ngày (63% thời gian) với LCP 4,8s và form 7 trường
**Mức độ: CAO — chênh lệch hiệu suất v1 vs v2 đã đo được; ước tính lãng phí 367–487 triệu**

Sheet `10_GA4` mục C + `11_CLARITY` mục A, và cắt CSV theo `Ngay_thu`:

| | v1 (N1–57) | v2 (N58–90) | Chênh |
|---|---|---|---|
| LCP | **4,8s** (ngưỡng báo động >4s) | 1,9s (ngưỡng tốt <2,5s) | −60% |
| Số trường form | 7 | 3 | −57% |
| Tỷ lệ tương tác | 34,2% | 58,7% | **+71,6%** |
| Thời gian tương tác TB | 52s | 121s | +132,7% |
| Cuộn 90% | 16% | 37% | +131% |
| Tỷ lệ hoàn tất form | 20,4% | 28,0% | **+37,3%** |
| Rage click di động (Clarity) | 18,7% | 3,1% | −83% |
| Dead click di động | 24,1% | 6,2% | −74% |
| **CP/SQL (CSV)** | **3.402.445đ** | **2.163.123đ** | **−36,4%** |
| **SQL/Lead (CSV)** | 22,8% | **28,7%** | +25,9% |
| **ROAS (CSV)** | 1,09x | **2,72x** | +150% |
| Cọc | 7 (trên 1.085,4 triệu) | 11 (trên 718,2 triệu) | — |

3 lỗi đã sửa ở v2 (Clarity #1, #2, #3) ước tính đã ngốn **520–690 lead** trong 57 ngày đầu ≈ **366,8 – 486,7 triệu đồng** — số này **không thu hồi được**, nhưng chứng minh: mỗi ngày trì hoãn sửa LP là tiền mất. Đáng chú ý: trường **"Số CMND/CCCD" ở vị trí 4/7 làm 61% phiên bỏ dở** — một trường không cần thiết ở bước đăng ký nhận bảng giá.

Cấu hình bổ trợ (sheet `05`): Điểm chất lượng TB **5,2/10**, Trải nghiệm trang đích = "Dưới trung bình", **1 phiên bản LP, không A/B test**.

---

### A10 — [ĐO LƯỜNG] Sự cố GTM ngày 44–46: 3 ngày mù, 63 lead vĩnh viễn mất khỏi Ads/GA4
**Mức độ: TRUNG BÌNH — 59.528.000đ chi phí 3 ngày chạy mù + méo mó dữ liệu huấn luyện**

Kiểm chứng trực tiếp trên CSV (cột `ChuyenDoi_Ads` vs `Lead_CRM`, gộp theo ngày):

| Ngày thứ | Chuyển đổi Ads | Lead CRM | Chi phí |
|---|---|---|---|
| 43 | 43 | 30 | 19.744.000đ |
| **44** | **0** | **17** | 20.249.000đ |
| **45** | **0** | **15** | 19.699.000đ |
| **46** | **0** | **31** | 19.580.000đ |
| 47 | 33 | 18 | 19.912.000đ |
| **Cộng N44–46** | **0** | **63** | **59.528.000đ** |

Nguyên nhân (sheet `12_GTM` mục B): v23 ngày 44, 09:12, `dev@` đổi class `.form-dk-v1` → `.form-register`, **điều kiện kích hoạt `generate_lead` ngừng khớp**. Sửa ở v24 ngày 47, 14:38 — **mất 3 ngày 5 giờ mới phát hiện**.

Hai lỗi hệ thống lộ ra:
1. Điều kiện kích hoạt **dựa trên class CSS** (thẻ #3, `12_GTM` mục A) → mọi lần dev đổi giao diện đều có thể làm gãy đo lường.
2. **KHÔNG CÓ cảnh báo khi chuyển đổi = 0** (mục #18, `12_GTM`) → `12_GTM` mục C ghi thẳng: *"Nguyên nhân khiến sự cố N44–46 mất 3 ngày mới bị phát hiện"*.

Trong 3 ngày đó Smart Bidding của PMax/GDN nhìn thấy "0 chuyển đổi" và tự giảm giá thầu, kéo theo méo mó học máy vượt ra ngoài 3 ngày.

---

### A11 — 26,8% ngân sách chạy vào khung giờ sale không trực
**Mức độ: TRUNG BÌNH — 483.347.916đ ở khung có tỷ lệ gọi lại 12–34%**

Sheet `07_KHUNG_GIO_TB` mục A:

| Khung giờ | % chi phí | Chi phí | SQL | CP/SQL | **Gọi lại <30 phút** |
|---|---|---|---|---|---|
| **20:00–23:00** | 18,7% | 337.261.419đ | 112 | 3.011.263đ | **21%** |
| **23:00–24:00** | 4,0% | 72.141.480đ | 22 | 3.279.158đ | **12%** |
| **00:00–06:00** | 4,1% | 73.945.017đ | 18 | 4.108.057đ | **34%** |
| **Cộng 3 khung xấu** | **26,8%** | **483.347.916đ** | 152 | 3.180.000đ | 12–34% |
| — so sánh 09:00–12:00 | 16,8% | 302.994.216đ | 121 | **2.504.084đ** | **93%** |
| — so sánh 14:00–17:00 | 17,1% | 308.404.827đ | 117 | 2.635.939đ | **91%** |

Khung 20:00–24:00 ăn **22,7% ngân sách** — nhiều hơn cả khung 09:00–12:00 — nhưng lead sinh ra ở đó chỉ 12–21% được gọi trong 30 phút, và theo A8 lead gọi >2h có tỷ lệ cọc 0,04–0,21%.

Cấu hình gây ra (sheet `05`): **lịch quảng cáo 24/7, không điều chỉnh giá thầu theo giờ**.

Cuối tuần: chi 503.810.000đ (25 ngày, 20,15 triệu/ngày) — **bằng ngày thường (19,99 triệu/ngày)** — trong khi chỉ có **2/8 sale trực** (sheet `01C`, `07C`). CSV cột `Thu`: T7+CN tạo 722 lead (28,9/ngày) với chỉ 24 lead/ngày năng lực xử lý → cấu trúc bảo đảm bỏ sót lead.

---

### A12 — Di động ăn 78,1% ngân sách với CP/SQL gấp 1,65x máy tính
**Mức độ: TRUNG BÌNH — chênh lệch hiệu suất ~ 220 triệu nếu cân bằng lại**

Sheet `07_KHUNG_GIO_TB` mục B:

| Thiết bị | % chi phí | Chi phí | SQL | Cọc | **CP/SQL** | Tỷ lệ CĐ |
|---|---|---|---|---|---|---|
| Di động | **78,1%** | 1.408.562.397đ | 463 | 11 | **3.042.251đ** | 2,03% |
| Máy tính | 16,7% | 301.190.679đ | 163 | 6 | **1.847.796đ** | **4,02%** |
| Máy tính bảng | 5,2% | 93.783.924đ | 24 | 1 | 3.907.664đ | 1,71% |

Máy tính: CP/SQL đạt ngưỡng "tốt" (<1,8 triệu, sheet `09`), tỷ lệ chuyển đổi gấp đôi di động, và cọc/chi phí = 6/301,2tr vs 11/1.408,6tr (**máy tính hiệu quả gấp 2,6x trên đồng chi phí**).

Nhưng chưa vội cắt di động: đây là **hệ quả của A7/A9**, không phải bản chất thiết bị. Lỗi #4 (Safari iOS) và #5 (<380px) chỉ ảnh hưởng di động; `10_GA4` mục C cho thấy sau khi lên v2, tỷ lệ hoàn tất form di động đã tăng 16,1% → 24,6% (+52,6%). **Sửa lỗi trước, điều chỉnh giá thầu thiết bị sau** — nếu cắt di động ngay sẽ cắt luôn 78% thị trường.

---

### A13 — [ĐO LƯỜNG] Không có GCLID trong CRM ⇒ không thể nhập chuyển đổi ngoại tuyến
**Mức độ: TRUNG BÌNH — chặn toàn bộ khả năng tối ưu theo SQL/cọc**

Sheet `12_GTM` mục A #15: *"Biến ẩn lưu GCLID vào form — CHƯA CÀI. Không có GCLID trong CRM ⇒ KHÔNG THỂ nhập chuyển đổi ngoại tuyến"*. Sheet `05` xác nhận: *"Nhập chuyển đổi ngoại tuyến từ CRM: CHƯA triển khai — CRM không lưu GCLID"*. Enhanced Conversions **TẮT** (`05` + `12_GTM` #14: "mất 10–20% khả năng khớp chuyển đổi").

Hậu quả định lượng: Google chỉ nhìn thấy 3.820 "chuyển đổi" mà **34,7% là rác** (A2), và **không bao giờ** nhìn thấy 651 SQL / 18 cọc / 3,13 tỷ doanh thu. Tức máy học đang tối ưu cho một chỉ số **không tương quan với tiền**: tương quan giữa xếp hạng CPL_Ads và xếp hạng CP/cọc theo chiến dịch là **ngược dấu** — PMax có CPL_Ads rẻ nhất (267.817đ) nhưng 0 cọc; Brand CPL_Ads 298.759đ nhưng 13 cọc.

Bổ sung: `12_GTM` #10 — Clarity **chưa gắn ID phiên vào bản ghi CRM** → không xem lại được hành trình của lead đã cọc để nhân bản.

---

### A14 — [ĐO LƯỜNG] 894 zalo_click + 1.206 file_download đang bị bỏ ngoài phép đo
**Mức độ: TRUNG BÌNH — mất 2.100 tín hiệu ý định, chưa lượng hóa được thành tiền**

Sheet `10_GA4` mục E:

| Sự kiện | Số lượt | Là sự kiện chính? | Nhập vào Ads? | Ghi chú của GA4 |
|---|---|---|---|---|
| zalo_click | **894** | Không | Không | *"Có — đang bị bỏ sót, không ai đo"* |
| file_download (bảng giá PDF) | **1.206** | Không | Không | *"Có tín hiệu ý định — đang bỏ sót"* |
| form_start | 7.458 | Không | Không | Đúng — chỉ dùng chẩn đoán |

Zalo là CTA chính của BĐS Việt Nam. 894 lượt bấm Zalo đang không được tính là lead trong khi 612 lượt xem trang bảng giá **lại được tính**. Hai sự kiện này chỉ mới có từ **ngày 71** (GTM v26) nên chỉ có 20 ngày dữ liệu.

**Thiếu dữ liệu:** không thể tính CP/lead Zalo vì (a) không biết bao nhiêu trong 894 lượt là người dùng duy nhất, (b) không có phân rã theo chiến dịch, (c) không biết bao nhiêu lượt đã chuyển thành lead CRM (có thể trùng với 2.557). **Cần thêm:** báo cáo GA4 zalo_click theo `session_campaign` + user-scoped, và mapping Zalo OA → CRM.

---

### A15 — [ĐO LƯỜNG] GTM phình 34 thẻ / 412KB JS, GA4 config trùng lặp từ ngày 31
**Mức độ: TRUNG BÌNH — làm chậm LCP ~0,8s, méo số phiên từ N31**

Sheet `12_GTM` header + mục A + B:

| Vấn đề | Bằng chứng | Hậu quả |
|---|---|---|
| 34 thẻ, 21 trigger, **412 KB JS bên thứ ba** | header `12_GTM` | **làm chậm LCP thêm ~0,8 giây** |
| Thẻ #2 "GA4 Configuration – Copy of Main" | v22, ngày 31, `dev@` | **page_view đếm đôi từ ngày 31** → số phiên & tỷ lệ thoát sai |
| 3 thẻ đối tác sàn F2 | v20, ngày 18, `dev@` | *"LCP tăng thêm ~0,3 giây"*, *"Không rõ nguồn gốc — cần rà soát bảo mật"* |
| Thẻ Zalo Tracking #12 | — | *"Không rõ ai cài, không có mô tả"* |
| Consent Mode v2 | CHƯA CẤU HÌNH | rủi ro pháp lý + mất modeled conversions |
| Vùng chứa phía máy chủ | KHÔNG CÓ | *"Toàn bộ đo lường phụ thuộc trình duyệt"* + trình chặn quảng cáo |

0,8 giây LCP không phải chuyện nhỏ khi LP v1 đã ở 4,8s (ngưỡng báo động >4s) — tức riêng GTM đóng góp ~17% thời gian tải. **Cảnh báo:** số liệu phiên GA4 từ ngày 31 trở đi (v22) bị đếm đôi page_view — mọi so sánh v1/v2 dựa trên *phiên* cần được đọc thận trọng; tôi đã ưu tiên dùng số CSV (Ads/CRM) làm gốc cho các kết luận tài chính.

---

### A16 — Mô hình phân bổ nhấp cuối đang gán sai công cho Brand, che khuất giá trị GDN/YouTube
**Mức độ: THẤP–TRUNG BÌNH — ảnh hưởng quyết định phân bổ ngân sách 2,1 tỷ**

Sheet `10_GA4` mục D (chỉ trên 1.715 `generate_lead`):

| Kênh | Nhấp cuối (đang dùng) | Dựa trên dữ liệu | Chênh | % |
|---|---|---|---|---|
| SEA_Brand | 592 | 401 | **−191** | **−32,3%** |
| SEA_Generic | 418 | 402 | −16 | −3,8% |
| PMAX | 510 | 466 | −44 | −8,6% |
| SEA_Competitor | 20 | 24 | +4 | +20,0% |
| **GDN_Remarketing** | 132 | **186** | +54 | **+40,9%** |
| **YT_Video** | 43 | **165** | +122 | **+283,7%** |
| Trực tiếp/Organic (ngoài Ads) | 0 | **71** | +71 | — |

Đọc đúng: Brand **không tạo ra 592 lead từ đầu**, nó đóng dấu ở bước cuối cho lead mà GDN/YouTube đã khơi mào. Điều này **không phủ nhận A3** (Brand vẫn là nơi cọc thật rơi vào, và cọc đo bằng CRM chứ không bằng attribution model) nhưng cảnh báo: đừng cắt sạch GDN/YT dựa trên "0 cọc last-click". Ngược lại YT vẫn phải chứng minh bằng số cọc — 83,2 triệu cho 8 SQL là quá đắt bất kể mô hình nào.

**Thiếu dữ liệu:** không có phân bổ data-driven cho *cọc* (chỉ có cho generate_lead) → không kết luận được GDN/YT đóng góp bao nhiêu vào 18 cọc. **Cần thêm:** đường dẫn chuyển đổi (conversion path) của 18 giao dịch cọc.

---

### A17 — Search Partners + Display Network bật trong chiến dịch Search; không loại trừ khách đã cọc
**Mức độ: THẤP–TRUNG BÌNH — chưa lượng hóa riêng được**

Sheet `05_CAU_HINH_TK`:
- **Search Partners: BẬT** cho cả 3 chiến dịch Search.
- **Mạng hiển thị trong chiến dịch Search: BẬT** — đây là mạng hiển thị trộn vào ngân sách Search, chất lượng thấp hơn hẳn.
- Đối tượng **chỉ ở chế độ Quan sát**, chưa dùng điều chỉnh giá thầu.
- **Chưa loại trừ khách đã đặt cọc / đã ký HĐMB** — tiền remarketing đang bám theo 18 khách đã mua.
- Tiện ích: **chỉ có Sitelink (4 liên kết)**. Thiếu **Cuộc gọi, Biểu mẫu khách hàng tiềm năng, Vị trí, Chú thích, Hình ảnh** — với BĐS mà thiếu tiện ích Cuộc gọi và Vị trí (nhà mẫu mở 8:00–18:00) là mất CTR và mất lead gọi trực tiếp.
- **Ngân sách chia sẻ: Không dùng** — nên Brand không thể mượn ngân sách thừa của Competitor.

**Thiếu dữ liệu:** báo cáo phân đoạn "Mạng" (Google Search / Search Partners / Display) không có trong bộ đề → **không tách được** bao nhiêu trong 1.114.959.000đ chi phí Search rơi vào Search Partners/Display. **Cần thêm:** segment Network trong Google Ads UI, 90 ngày.

---

### A18 — Không có reCAPTCHA / xác minh OTP: 4–31% lead là số trùng, 6–24% số sai
**Mức độ: THẤP–TRUNG BÌNH — nhiễu chất lượng lead ở đầu nguồn**

Sheet `05`: *"Chống spam biểu mẫu: Không có reCAPTCHA, không xác minh OTP số điện thoại"*. Hậu quả đo được ở sheet `08C` (mẫu 600 lead):

| Chiến dịch | Trùng SĐT | SĐT sai | Sai phân khúc (<2 tỷ) | Môi giới/đối thủ | **Lead dùng được** | Chi phí/lead dùng được |
|---|---|---|---|---|---|---|
| SEA_Brand | 4% | 6% | 18% | 5% | **67%** | **453.193đ** |
| SEA_Generic | 7% | 11% | 29% | 7% | 46% | 2.510.903đ |
| GDN_Remarketing | 12% | 17% | 27% | 6% | 38% | 1.772.689đ |
| SEA_Competitor | 5% | 12% | 31% | **26%** | 26% | 21.243.510đ |
| YT_Video | 16% | 21% | 33% | 5% | 25% | 5.640.203đ |
| **PMAX** | **31%** | **24%** | **34%** | 4% | **7%** | **8.191.901đ** |

Cột cuối là chỉ số xếp hạng chiến dịch trung thực nhất hiện có: Brand rẻ hơn PMax **18,1 lần** trên mỗi lead dùng được. Ngoài ra "sai phân khúc (ngân sách <2 tỷ)" 18–34% ở mọi nguồn cho thấy **quảng cáo và landing page không lọc giá** — sheet `05` ghi LP v1 "không hiện giá", và v2 mới có bảng giá từ ngày 58.

---

## Bảng tổng hợp Phần A — xếp theo tác động tài chính

| # | Vấn đề | Nhóm | Mức | Lãng phí đã xảy ra | Cơ hội bỏ lỡ |
|---|---|---|---|---|---|
| A1 | PMax 0 cọc | Cấu trúc | Cao | 400–475 tr | — |
| A2 | 4 hành động chuyển đổi, 2 là rác | **Đo lường** | Cao | điều khiển sai 688,6 tr | — |
| A3 | Brand mất 40,4% IS do ngân sách | Ngân sách | Cao | — | ~1.621 tr |
| A4 | Từ khóa rộng rác, 0 SQL | Từ khóa | Cao | 243,0 tr | — |
| A5 | Competitor 0 cọc | Cấu trúc | Cao | 176,7 tr | — |
| A6 | Toàn quốc, 4 vùng xa 0 cọc | Nhắm mục tiêu | Cao | 364,3 tr | ~645 tr |
| A7 | 3 lỗi LP chưa sửa | **Đo lường/KT** | Cao | 261–339 tr | 471–612 tr |
| A8 | 47% lead gọi sau 2h, 275 lead bỏ sót | Vận hành | Cao | 194,0 tr | ~2.740 tr (trần) |
| A9 | LP v1 chạy 63% thời gian | Trang đích | Cao | 367–487 tr | — |
| A10 | GTM gãy N44–46 | **Đo lường** | TB | 59,5 tr | — |
| A11 | 26,8% ngân sách ngoài giờ sale | Lịch | TB | ~483,3 tr chạy sai giờ | — |
| A12 | Di động CP/SQL 1,65x desktop | Thiết bị | TB | — | ~220 tr |
| A13 | Không GCLID, Enhanced Conv tắt | **Đo lường** | TB | chặn tối ưu theo tiền | 10–20% khớp CĐ |
| A14 | zalo_click/file_download bỏ sót | **Đo lường** | TB | 2.100 tín hiệu | không lượng hóa được |
| A15 | GTM 34 thẻ, +0,8s LCP, config trùng | **Đo lường** | TB | — | qua tốc độ tải |
| A16 | Mô hình nhấp cuối | **Đo lường** | Thấp–TB | phân bổ sai | — |
| A17 | Search Partners/Display bật | Cấu hình | Thấp–TB | không tách được | — |
| A18 | Không reCAPTCHA/OTP | Chất lượng | Thấp–TB | qua CP/lead dùng được | — |

---

# PHẦN B — TÍNH TOÁN

*Mọi số trong phần này là output trực tiếp của `agent-2-calc.py`, tính từ `du_lieu_google_ads_90_ngay_1.csv` (486 dòng ngày × chiến dịch).*

## B1. CPL Ads / CPL CRM / CP/SQL / CP/cọc

### Toàn kỳ

| Chỉ số | Giá trị | Ngưỡng sheet `09` | Đánh giá |
|---|---|---|---|
| Chi phí | 1.803.537.000đ (20.039.300đ/ngày) | — | — |
| Chuyển đổi Ads | 3.820 | — | — |
| Lead CRM | 2.557 | — | — |
| SQL | 651 | — | — |
| Đặt cọc | 18 | — | — |
| Doanh thu HH | 3.130.000.000đ | — | — |
| **CPL theo Ads** | **472.130đ** | tốt <500k | ✔ nhưng là số giả (A2) |
| **CPL theo CRM** | **705.333đ** | TB 500k–1,1tr | ⚠ trung bình |
| **CP/SQL** | **2.770.410đ** | TB 1,8–3,5tr | ⚠ **vượt KPI 2,2tr là 25,9%** |
| **CP/cọc** | **100.196.500đ** | hòa vốn 60.333.333đ | ✘ **gấp 1,66x** |
| ROAS | 1,74x | KPI ≥3,0x | ✘ |

Doanh thu thực tế/cọc = 3.130.000.000 / 18 = **173.888.889đ** — thấp hơn 181 triệu giả định 4,0%. **Tôi dùng 181 triệu cho mọi tính toán forward-looking theo đề bài, và ghi nhận rủi ro 4% này.**

### Theo chiến dịch (toàn kỳ) — sắp theo CP/SQL

| Chiến dịch | Chi phí | % NS | CĐ Ads | Lead CRM | SQL | Cọc | **CPL Ads** | **CPL CRM** | **CP/SQL** | **CP/cọc** | ROAS |
|---|---|---|---|---|---|---|---|---|---|---|---|
| **SEA_Brand** | 260.219.000đ | 14,4% | 871 | 857 | 352 | **13** | 298.759đ | **303.639đ** | **739.259đ** | **20.016.846đ** | **8,76x** |
| SEA_Generic | 677.994.000đ | 37,6% | 664 | 587 | 191 | 5 | 1.021.075đ | 1.155.015đ | 3.549.707đ | 135.598.800đ | 1,25x |
| GDN_Remarketing | 130.009.000đ | 7,2% | 302 | 193 | 36 | 0 | 430.493đ | 673.622đ | 3.611.361đ | — | 0,00x |
| PMAX | 475.376.000đ | 26,4% | 1.775 | 829 | 61 | 0 | **267.817đ** | 573.433đ | **7.793.049đ** | — | 0,00x |
| YT_Video | 83.193.000đ | 4,6% | 177 | 59 | 8 | 0 | 470.017đ | 1.410.051đ | 10.399.125đ | — | 0,00x |
| SEA_Competitor | 176.746.000đ | 9,8% | 31 | 32 | 3 | 0 | 5.701.484đ | 5.523.312đ | **58.915.333đ** | — | 0,00x |
| **TỔNG** | **1.803.537.000đ** | 100% | 3.820 | 2.557 | 651 | **18** | 472.130đ | 705.333đ | 2.770.410đ | 100.196.500đ | **1,74x** |

**Phát hiện then chốt:** thứ hạng theo `CPL Ads` (PMax #1 rẻ nhất) **ngược hoàn toàn** với thứ hạng theo `CP/cọc` (PMax không có cọc). Đây là bằng chứng số học của A2/A13 và là câu trả lời cho D3.

### Cắt Search vs không-Search

| Nhóm | Chi phí | % | SQL | Cọc | Doanh thu | CP/SQL | ROAS |
|---|---|---|---|---|---|---|---|
| 3 chiến dịch Search | 1.114.959.000đ | 61,8% | 546 | **18** | 3.130.000.000đ | 2.042.049đ | **2,81x** |
| PMax + GDN + YT | **688.578.000đ** | **38,2%** | 105 | **0** | **0đ** | 6.557.886đ | **0,00x** |

## B2. ROAS toàn kỳ và từng giai đoạn

| Giai đoạn | Chi phí | Lead | SQL | Cọc | Doanh thu HH | **ROAS** | CP/SQL | CP/cọc |
|---|---|---|---|---|---|---|---|---|
| GĐ1 (N1–30) | 545.696.000đ | 734 | 151 | 2 | 330.000.000đ | **0,60x** | 3.613.881đ | 272.848.000đ |
| GĐ2 (N31–60) | 604.392.000đ | 761 | 184 | 5 | 850.000.000đ | **1,41x** | 3.284.739đ | 120.878.400đ |
| GĐ3 (N61–90) | 653.449.000đ | 1.062 | 316 | 11 | 1.950.000.000đ | **2,98x** | 2.067.877đ | 59.404.455đ |
| **Toàn kỳ** | **1.803.537.000đ** | 2.557 | 651 | **18** | 3.130.000.000đ | **1,74x** | 2.770.410đ | 100.196.500đ |

**Xu hướng rất tích cực và có nguyên nhân rõ ràng:** ROAS 0,60 → 1,41 → **2,98x** (gần chạm KPI 3,0x ở GĐ3). CP/SQL 3,61tr → 3,28tr → **2,07tr** (đã dưới KPI 2,2tr). Ba nguyên nhân trùng khớp thời điểm:
1. LP v2 lên ngày 58 (GTM v25) — nằm trong GĐ3.
2. SLA gọi lại 15 phút áp dụng ở GĐ3 (`08B`), trung vị phản hồi 214 → 142 → **47 phút**.
3. Sự kiện mở bán trong GĐ3 (`01D`).

**Đây là bằng chứng mạnh nhất cho kế hoạch Phần C:** không cần phát minh gì mới, chỉ cần nhân rộng đúng những gì GĐ3 đã làm + sửa những gì GĐ3 vẫn chưa sửa.

### ROAS chiến dịch × giai đoạn (chỉ chiến dịch có doanh thu)

| Chiến dịch | GĐ1 | GĐ2 | GĐ3 |
|---|---|---|---|
| SEA_Brand | 5,73x (2 cọc, 57,6tr) | 7,19x (3 cọc, 72,3tr) | **10,97x (8 cọc, 130,3tr)** |
| SEA_Generic | 0,00x (0 cọc, 200,4tr) | 1,51x (2 cọc, 218,5tr) | 2,01x (3 cọc, 259,2tr) |
| PMax / GDN / YT / Competitor | 0,00x | 0,00x | 0,00x |

Brand ở GĐ3: tăng chi phí 80% (72,3 → 130,3 triệu) mà ROAS **tăng** từ 7,19x lên 10,97x — bằng chứng trực tiếp Brand chưa bão hòa và việc mất 40,4% IS do ngân sách (A3) đang là ràng buộc chính.

## B3. Tỷ lệ chuyển đổi từng bước phễu

### Toàn kỳ

| Bước | Số lượng | Tỷ lệ bước | Ngưỡng sheet `09` |
|---|---|---|---|
| Lead CRM | 2.557 | — | — |
| → SQL | 651 | **25,5%** | TB 18–30% ✔ |
| → Đi xem nhà | 206 | **31,6%** | TB 22–35% ✔ (sát dưới) |
| → Booking giữ chỗ | 59 | **28,6%** | không có ngưỡng |
| → Đặt cọc | 18 | **30,5%** | không có ngưỡng |
| **Lead → Cọc (toàn phễu)** | | **0,70%** | — |
| **Đi xem → Cọc** | | **8,7%** | TB 7–12% ✔ |
| **SQL → Cọc** | | **2,76%** | — |

**Kết luận quan trọng:** từ bước "Đi xem nhà" trở đi, tỷ lệ đều **đạt chuẩn ngành**. Điểm gãy nằm ở **đầu phễu** (Lead→SQL 25,5%, kéo xuống bởi PMax 7,4%) và **bước SQL→Đi xem 31,6%** (phụ thuộc năng lực sale — A8). Nói cách khác: *sale không phải vấn đề khi họ gặp được khách; vấn đề là lấy đúng khách và gọi kịp.*

### Theo chiến dịch

| Chiến dịch | Lead | →SQL | →Đi xem | →Booking | →Cọc | Lead→Cọc |
|---|---|---|---|---|---|---|
| SEA_Brand | 857 | **41,1%** | 35,5% | 29,6% | 35,1% | **1,52%** |
| SEA_Generic | 587 | 32,5% | 32,5% | 29,0% | 27,8% | 0,85% |
| GDN_Remarketing | 193 | 18,7% | 22,2% | 25,0% | 0% | 0,00% |
| YT_Video | 59 | 13,6% | 12,5% | 0% | — | 0,00% |
| **PMAX** | 829 | **7,4%** | 16,4% | 20,0% | 0% | **0,00%** |
| SEA_Competitor | 32 | 9,4% | 0% | — | — | 0,00% |

### Theo giai đoạn — phễu đang cải thiện ở mọi bước

| Giai đoạn | Lead | →SQL | →Đi xem | →Booking | →Cọc | Lead→Cọc |
|---|---|---|---|---|---|---|
| GĐ1 | 734 | 20,6% | 25,2% | 26,3% | 20,0% | 0,27% |
| GĐ2 | 761 | 24,2% | 30,4% | 28,6% | 31,2% | 0,66% |
| **GĐ3** | 1.062 | **29,8%** | **35,4%** | 29,5% | 33,3% | **1,04%** |

Lead→Cọc tăng **3,85 lần** từ GĐ1 sang GĐ3. Đây là cơ sở để tôi dám giả định cải thiện tỷ lệ ở B4/Phần C.

## B4. KPI 32 cọc / 2,1 tỷ — cần bao nhiêu SQL và lead thô?

**Giả định nền (đo được từ CSV toàn kỳ):** SQL→Cọc = 2,76%; Lead→SQL = 25,5%.
**Vấn đề của việc dùng nguyên tỷ lệ lịch sử:** tỷ lệ toàn kỳ bị PMax (7,4% SQL/Lead, 0 cọc) kéo xuống — mà PMax sẽ bị cắt/tái cấu trúc trong kế hoạch. Nên tôi trình bày 3 kịch bản:

| Kịch bản | SQL→Cọc | Lead→SQL | **SQL cần** | **Lead thô cần** | Lead/ngày | **CP/SQL tối đa** | CPL tối đa |
|---|---|---|---|---|---|---|---|
| **A** — giữ nguyên tỷ lệ toàn kỳ | 2,76% | 25,5% | **1.157** | **4.546** | 50,5 | 1.814.516đ | 461.967đ |
| **B** — SQL→Cọc +25%, Lead→SQL 32% | 3,46% | 32,0% | **926** | **2.893** | 32,1 | **2.268.145đ** | 725.806đ |
| **C** — SQL→Cọc +50%, Lead→SQL 35% | 4,15% | 35,0% | **772** | **2.204** | 24,5 | 2.721.774đ | 952.621đ |

### Tôi chọn **Kịch bản B** làm mục tiêu cam kết. Lý do — từng giả định có căn cứ số:

**Giả định 1 — Lead→SQL đạt 32%.** GĐ3 đã đạt **29,8%** với PMax vẫn còn nguyên. Chiến dịch Search thuần đã đạt **37,0%** (Brand 41,1%, Generic 32,5%). Cắt PMax + Competitor (861 lead, 64 SQL, tỷ lệ 7,4%) khỏi mẫu là đủ để đẩy tỷ lệ tài khoản lên >32% mà **không cần cải thiện gì thêm** — đây là giả định bảo thủ.

**Giả định 2 — SQL→Cọc tăng 25% (2,76% → 3,46%).** Căn cứ: `08A` cho thấy chuyển toàn bộ lead sang nhóm "gọi lại <30 phút" nâng tỷ lệ cọc từ mix hiện tại 0,62% lên 1,21% (+95%). Tôi chỉ giả định thu được **1/4** mức cải thiện lý thuyết đó, vì (a) SLA 15 phút đã áp dụng ở GĐ3 nên một phần lợi ích đã nằm trong baseline, (b) chỉ 2 sale trực cuối tuần là ràng buộc cứng không giải quyết được bằng tiền quảng cáo.

**Giả định 3 — không giả định gì về giá bất động sản, chính sách bán hàng hay mùa vụ.** Không có dữ liệu.

### Kiểm tra khả thi với năng lực sale (ràng buộc "không tăng nhân sự")

| | Số |
|---|---|
| Lead thô cần (KB B) | **2.893** trong 90 ngày = **32,1 lead/ngày** |
| Lead thực tế 90 ngày qua | 2.557 = 28,4/ngày |
| Trần lý thuyết 8 sale × 12 lead | 96/ngày = 8.640/90 ngày |
| **Trần thực tế** (65 ngày thường × 96 + 25 ngày T7/CN × 24) | **6.840 lead/90 ngày** |
| **Tỷ lệ dùng năng lực ở KB B** | **2.893 / 6.840 = 42,3%** ✔ |

Năng lực **không phải** ràng buộc về khối lượng. Ràng buộc thật là **tốc độ và phân bổ**: GĐ3 đã ở 35,4 lead/ngày mà vẫn có 61 lead bị bỏ sót (`08B`) và 21% lead khung 20–23h được gọi trong 30 phút. **Không tăng người ⇒ phải giảm lead rác và dồn lead vào giờ có người trực** (giải pháp ở Phần C).

**Đối chiếu KPI CP/SQL:** KB B cho CP/SQL tối đa **2.268.145đ**, KPI của ban giám đốc là ≤ 2.200.000đ. Hai con số cách nhau 3,0% — tức **KPI 32 cọc và KPI CP/SQL 2,2 triệu là nhất quán với nhau** dưới giả định KB B. Nếu chỉ đạt tỷ lệ KB A thì CP/SQL phải xuống 1.814.516đ (dưới cả ngưỡng "tốt" 1,8tr của sheet `09`) — bất khả thi. **Kết luận: 32 cọc chỉ đạt được nếu cải thiện tỷ lệ chuyển đổi, không thể đạt bằng mua thêm lead.**

## B5. Điểm hòa vốn

| Câu hỏi | Phép tính | Kết quả |
|---|---|---|
| Chi phí QC tối đa/cọc để ROAS = 3,0x | 181.000.000 / 3 | **60.333.333đ** |
| Ngân sách tối đa cho 32 cọc ở ROAS 3,0x | 32 × 60.333.333 | 1.930.666.667đ |
| Với ngân sách 2,1 tỷ, doanh thu cần đạt | 2.100.000.000 × 3 | 6.300.000.000đ |
| ⇒ Số cọc cần với 2,1 tỷ | 6.300.000.000 / 181.000.000 | **34,8 cọc** |
| CP/cọc hiện tại | 1.803.537.000 / 18 | 100.196.500đ |
| **Khoảng cách** | 100.196.500 / 60.333.333 | **gấp 1,66x ngưỡng hòa vốn** |

**Hai KPI của ban giám đốc mâu thuẫn nhẹ:** tiêu hết 2,1 tỷ mà chỉ đạt đúng 32 cọc → ROAS = 32×181tr/2,1tỷ = **2,76x < 3,0x**. Để thỏa **cả hai** KPI, có 2 đường:
- (a) đạt **≥ 34,8 cọc** với 2,1 tỷ, hoặc
- (b) đạt **32 cọc với ≤ 1,93 tỷ** (tiêu 92% ngân sách).

**Khuyến nghị: đường (a), mục tiêu 36 cọc.** Kế hoạch Phần C được tính ngược để ra **36,5 cọc / ROAS 3,15x**, tức có đệm 14% so với KPI 32 cọc — cần đệm này vì doanh thu thực tế/cọc là 173,9 triệu chứ không phải 181 triệu (−4,0%). Ở mức 173,9 triệu/cọc, 36,5 cọc vẫn cho ROAS **3,02x** ✔.

## B6. Đối chiếu ba nguồn số liệu — bóc tách chính xác 3.820 vs 2.557

**Nguồn:** `10_GA4` mục A và E (số lượt sự kiện), `12_GTM` mục B v23/v24 (sự cố), CSV cột `ChuyenDoi_Ads`/`Lead_CRM` (kiểm chứng).

### Bước 1 — 3.820 được tạo thành từ gì

| Sự kiện | Số lượt | Là lead thật? |
|---|---|---|
| generate_lead | 1.715 | ✔ |
| click_to_call (tổng lượt) | 1.132 | ✔ nhưng đếm trùng |
| view_price_page | 612 | ✘ |
| engaged_30s | 361 | ✘ |
| **Cộng** | **3.820** | khớp cột `ChuyenDoi_Ads` CSV = 3.820 ✔ |

### Bước 2 — Ba thành phần của khoảng chênh

| Thành phần | Số | % của 3.820 | Nguồn |
|---|---|---|---|
| **(1) Đếm trùng** — click_to_call: 1.132 lượt vs 779 người dùng duy nhất | **−353** | **9,2%** | `10_GA4` A: *"Chênh 353 lượt là do một người bấm nhiều lần"*; `12_GTM` C: *"Thổi phồng 353 chuyển đổi (9,2%)"* |
| **(2) Sự kiện rác** — view_price_page 612 + engaged_30s 361 | **−973** | **25,5%** | `10_GA4` E: cả hai ghi *"Có thực sự là KH tiềm năng? KHÔNG"* |
| **= Lead thật đo được bằng thẻ** | **2.494** | | 1.715 form + 779 người gọi duy nhất |
| **(3) Mất thẻ** — GTM v23 làm gãy trigger `generate_lead` ngày 44–46 | **+63** | 1,6% | `12_GTM` v24: *"63 lead của 3 ngày trước đó vĩnh viễn không có trong Google Ads/GA4"* |
| **= Lead CRM** | **2.557** | | ✔ **khớp chính xác** |

### Chứng minh phép cộng khớp

```
3.820 − 353 (trùng) − 973 (rác)          = 2.494   ← lead đo được bằng thẻ
2.494 + 63 (mất thẻ N44–46)              = 2.557   ← khớp CRM ✔
```
Chiều ngược lại:  `2.557 = 1.715 + 779 + 63` và `1.715 + 1.132 + 612 + 361 = 3.820` ✔

### Kiểm chứng độc lập thành phần (3) từ CSV — không chỉ tin sheet GTM

| Ngày thứ | Chuyển đổi Ads | Lead CRM |
|---|---|---|
| 43 | 43 | 30 |
| **44** | **0** | 17 |
| **45** | **0** | 15 |
| **46** | **0** | 31 |
| 47 | 33 | 18 |
| **Tổng N44–46** | **0** | **63** |

Cột `ChuyenDoi_Ads` = 0 tuyệt đối trong đúng 3 ngày đó trên **cả 6 chiến dịch**, trong khi `Lead_CRM` = 63 vẫn chạy bình thường. Con số 63 trong `10_GA4` không phải giả định — nó được xác nhận độc lập bằng CSV.

### Kết luận B6

Tỷ lệ thổi phồng Ads/CRM = **1,494x**. Sheet `09` xếp 1,2–1,5x là "trung bình ngành", >1,8x là "báo động" — tài khoản đang **sát mép trên của vùng trung bình**, nhưng con số 1,494x này *che giấu* một thực tế tệ hơn: nếu tách theo chiến dịch, PMax là **2,14x** (vượt ngưỡng báo động) trong khi Brand chỉ **1,02x** (gần như hoàn hảo). **Vấn đề không phân bố đều — nó tập trung ở PMax.**

## B7. Ước tính lead mất do lỗi kỹ thuật chưa sửa

### Phân định rõ: đâu là SỐ ĐO, đâu là ƯỚC TÍNH

| Loại | Nội dung | Nguồn |
|---|---|---|
| **SỐ ĐO (Clarity ghi trực tiếp)** | 4.196 phiên gặp lỗi JS #4; 2.741 phiên gặp lỗi #5; 1.204 phiên gặp lỗi #6; 8.412 nhấp chết ở ảnh bảng giá; 1.847 nhấp chết ở hotline `tel:`; tỷ lệ lỗi JS di động 9,3% (v1) / 8,9% (v2) | `11_CLARITY` A, C |
| **ƯỚC TÍNH của đội UX (không phải của tôi)** | 370–480 lead mất do 3 lỗi chưa sửa. Sheet ghi rõ: *"Ước tính do đội UX đưa ra dựa trên tỷ lệ hoàn tất form của nhóm phiên không gặp lỗi. Là ước tính, không phải số đo trực tiếp."* | `11_CLARITY` C |
| **ƯỚC TÍNH của tôi** | Quy đổi 370–480 lead ra tiền, ra SQL, ra cọc và ra doanh thu (dưới đây) | tính bằng script |
| **Cảnh báo lấy mẫu** | Clarity chỉ lấy mẫu **~92%** lưu lượng và mã theo dõi chỉ gắn **từ ngày 5** → con số thật có thể **cao hơn** 370–480 | `11_CLARITY` header |

### Quy ra tiền

Đơn giá dùng: **CPL_CRM thực tế toàn kỳ = 705.333đ** (= 1.803.537.000 / 2.557). Đây là chi phí đã trả để có 1 lead — lead bị lỗi chặn là lead đã trả tiền mà không nhận được.

| Lỗi (chưa sửa) | Lead mất | Chi phí đã trả tương ứng |
|---|---|---|
| #4 — JS `e.setDate`, Safari iOS 17.x (4.196 phiên) | 280–340 | **197.493.297 – 239.813.289đ** |
| #5 — nút bị khung chat che <380px (2.741 phiên) | 60–90 | 42.319.992 – 63.479.988đ |
| #6 — `tel:` không phản hồi trên desktop (1.204 phiên) | 30–50 | 21.159.996 – 35.266.660đ |
| **TỔNG** | **370–480** | **260.973.285 – 338.559.937đ** |

### Quy tiếp xuống cuối phễu (ước tính của tôi, dùng tỷ lệ toàn kỳ)

| Bước | Tỷ lệ dùng | Kết quả |
|---|---|---|
| Lead mất | — | 370 – 480 |
| → SQL mất | ×25,5% (SQL/Lead toàn kỳ) | **94 – 122 SQL** |
| → Cọc mất | ×2,76% (SQL→Cọc toàn kỳ) | **2,6 – 3,4 cọc** |
| → **Doanh thu hoa hồng bỏ lỡ** | ×181.000.000đ | **471.435.276 – 611.591.709đ** |

### Đối chiếu ngân sách sửa lỗi

Chi phí sửa 3 lỗi này ước tính **1–3 ngày công dev** (thay date picker bằng `<input type="date">` native + tăng z-index/padding-bottom cho nút + đổi `tel:` thành copy-to-clipboard trên desktop). Kể cả tính 20 triệu đồng chi phí dev, **ROI là 13–17 lần chỉ tính chi phí lead, hoặc 24–31 lần nếu tính doanh thu hoa hồng.** Và vì lỗi vẫn đang chảy máu, mỗi 30 ngày trì hoãn = thêm ~123–160 lead (370–480 × 30/90) ≈ **87–113 triệu đồng**.

### Bonus — 3 lỗi ĐÃ SỬA ở v2 cho thấy quy mô vấn đề

| Lỗi đã sửa (chỉ ảnh hưởng N1–57) | Lead mất |
|---|---|
| #1 Ảnh "Xem bảng giá" trông như nút — 8.412 nhấp chết | 90–140 |
| #2 Trường "Số CMND/CCCD" — 61% phiên bỏ dở tại đây | 320–400 |
| #3 Dropdown "Ngân sách đầu tư" 9 lựa chọn trên di động — 27% bỏ dở | 110–150 |
| **Cộng** | **520–690 lead ≈ 366,8 – 486,7 triệu đồng** (đã mất, không thu hồi) |

**Tổng thiệt hại kỹ thuật trên trang đích trong 90 ngày: 890 – 1.170 lead ≈ 628 – 825 triệu đồng chi phí quảng cáo.** Đây là khoản lớn thứ hai sau PMax — và là khoản duy nhất sửa được trong vòng 1 tuần.

---

# PHẦN C — KẾ HOẠCH 90 NGÀY TIẾP THEO

## C0. Nguyên tắc điều hành

**Thứ tự bắt buộc: SỬA ĐO LƯỜNG → SỬA TRANG ĐÍCH → SỬA PHÂN BỔ → MỚI TĂNG NGÂN SÁCH.**

Căn cứ số: máy học đang chạy trên tín hiệu có 34,7% là rác (B6). Bơm thêm tiền vào hệ thống này chỉ khuếch đại sai — bằng chứng là PMax đã được cấp 475,4 triệu (26,4% ngân sách) và trả về 0 cọc. Đồng thời GĐ3 đã chứng minh công thức đúng: LP tốt + SLA gọi nhanh → ROAS 2,98x (B2). Kế hoạch này = **nhân rộng GĐ3 + sửa những gì GĐ3 chưa sửa**.

Do đó ngân sách **tăng dần** (525 → 705 → 870 triệu), không chia đều 700/700/700: GĐ1 là giai đoạn sửa nền, tiêu ít, không được phép scale trên nền hỏng.

## C1. Bảng phân bổ ngân sách — tổng đúng 2.100.000.000đ

| Chiến dịch | GĐ1 (N1–30) | GĐ2 (N31–60) | GĐ3 (N61–90) | **Tổng** | % | So với 90 ngày qua |
|---|---|---|---|---|---|---|
| SEA_Brand_Vinhomes_HocMon | 100.000.000đ | 120.000.000đ | 150.000.000đ | **370.000.000đ** | 17,6% | 260,2tr → **+42,2%** |
| SEA_Generic_NhaPho_CanHo_TayBac | 220.000.000đ | 250.000.000đ | 280.000.000đ | **750.000.000đ** | 35,7% | 678,0tr → +10,6% |
| PMAX_VinhomesHM_Lead *(tái khởi động)* | 60.000.000đ | 110.000.000đ | 170.000.000đ | **340.000.000đ** | 16,2% | 475,4tr → **−28,5%** |
| GDN_Remarketing_Web30d | 45.000.000đ | 55.000.000đ | 65.000.000đ | **165.000.000đ** | 7,9% | 130,0tr → +26,9% |
| **SEA_DSA_LongTail** *(mới)* | 40.000.000đ | 50.000.000đ | 60.000.000đ | **150.000.000đ** | 7,1% | — |
| YT_Video_TVC_MoBan | **0đ** | 25.000.000đ | 40.000.000đ | **65.000.000đ** | 3,1% | 83,2tr → −21,9% |
| SEA_Competitor_DoiThu | **0đ** | 25.000.000đ | 35.000.000đ | **60.000.000đ** | 2,9% | 176,7tr → **−66,1%** |
| Dự phòng / test | 60.000.000đ | 70.000.000đ | 70.000.000đ | **200.000.000đ** | 9,5% | — |
| **TỔNG** | **525.000.000đ** | **705.000.000đ** | **870.000.000đ** | **2.100.000.000đ** | 100% | +16,4% |
| *Ngân sách/ngày* | *17.500.000đ* | *23.500.000đ* | *29.000.000đ* | *23.333.333đ* | | |

*(Kiểm tra tổng bằng `assert` trong `agent-2-calc.py` — dòng "Kiem tra: tong dung 2.100.000.000 VND ✔")*

**Bốn quyết định phân bổ và căn cứ số của từng quyết định:**

| Quyết định | Căn cứ |
|---|---|
| Brand +42,2% | Mất **40,4%** IS do ngân sách (A3), ROAS 8,76x toàn kỳ và **10,97x ở GĐ3**, CP/cọc 20,0tr = **1/5 mức hòa vốn 60,3tr** (B5). Đây là chỗ duy nhất trong tài khoản mà mỗi đồng thêm gần như chắc chắn có lãi. |
| PMax −28,5% và **tắt 30 ngày đầu** | 0 cọc / 475,4tr; CP/SQL 7,79tr = 1,56x ngưỡng báo động; 74,3% thoát <3s (A1). Không tắt vĩnh viễn vì tín hiệu đầu vào đang sai (A2) — phải cho nó cơ hội chạy lại với tín hiệu sạch. |
| Competitor −66,1% và **tắt 30 ngày đầu** | 0 cọc / 176,7tr, CP/SQL 58,9tr = 11,8x ngưỡng báo động (A5). Giữ 60tr để phòng thủ khi bị đối thủ đấu giá (D2), không phải để tấn công. |
| Dự phòng 200tr (9,5%) | Ngân sách này **không được duyệt tự động** — chỉ giải ngân khi một chiến dịch chạm ngưỡng mở rộng ở C6. Tránh lặp lại lỗi của người tiền nhiệm: dồn tiền vào chiến dịch có CPA đẹp mà không có cọc. |

## C2. Mục tiêu định lượng từng giai đoạn (tính ngược từ ngân sách)

| | GĐ1 (N1–30) | GĐ2 (N31–60) | GĐ3 (N61–90) | **Tổng 90 ngày** | KPI |
|---|---|---|---|---|---|
| Ngân sách | 525.000.000đ | 705.000.000đ | 870.000.000đ | **2.100.000.000đ** | ≤ 2,1 tỷ ✔ |
| **CP/SQL mục tiêu** | 2.600.000đ | 2.200.000đ | **1.900.000đ** | **2.142.262đ** | ≤ 2.200.000đ ✔ |
| **SQL** | 202 | 320 | 458 | **980** | — |
| Lead thô (SQL/Lead 32%) | 631 (21,0/ngày) | 1.001 (33,4/ngày) | 1.431 (47,7/ngày) | **3.063** | — |
| SQL→Cọc mục tiêu | 3,0% | 3,5% | 4,2% | 3,72% | — |
| **Đặt cọc** | 6,1 | 11,2 | 19,2 | **36,5** | ≥ 32 ✔ (+14%) |
| Doanh thu HH | 1.096.442.308đ | 2.030.079.545đ | 3.480.915.789đ | **6.607.437.643đ** | — |
| **ROAS** | 2,09x | 2,88x | **4,00x** | **3,15x** | ≥ 3,0x ✔ |

**Đối chiếu với baseline 90 ngày qua để chứng minh mục tiêu không viển vông:**

| Chỉ số | Toàn kỳ qua | **GĐ3 qua** | GĐ1 tới (mục tiêu) | GĐ3 tới (mục tiêu) |
|---|---|---|---|---|
| CP/SQL | 2.770.410đ | **2.067.877đ** | 2.600.000đ *(dễ hơn GĐ3 qua)* | 1.900.000đ *(−8,1% so GĐ3 qua)* |
| SQL/Lead | 25,5% | 29,8% | 32% *(Search thuần đã 37,0%)* | 32% |
| ROAS | 1,74x | **2,98x** | 2,09x | 4,00x |

Mục tiêu GĐ1 **thấp hơn** thành tích thực tế của GĐ3 vừa qua ở cả CP/SQL lẫn ROAS — chủ ý, vì GĐ1 là tháng sửa hạ tầng và sẽ có xáo trộn khi đổi conversion actions (Smart Bidding cần 7–14 ngày học lại). Mục tiêu GĐ3 tới (CP/SQL 1,9tr) chỉ đòi hỏi cải thiện **8,1%** so với GĐ3 vừa qua — trong khi riêng việc cắt PMax/Competitor (652,1 triệu chi phí cho 64 SQL) đã đủ tạo ra mức đó về mặt số học.

**Kiểm tra ràng buộc sale:** GĐ3 cần 47,7 lead thô/ngày. Trần thực tế 6.840 lead/90 ngày (B4) → GĐ3 cần 1.431/2.280 công suất giai đoạn = **62,8%**. Còn dư, nhưng đây là mức cần theo dõi sát — xem C7 (tiêu chí dừng #6).

## C3. Cấu trúc tài khoản đề xuất

| Chiến dịch | Nhóm quảng cáo | Đối sánh | Ghi chú |
|---|---|---|---|
| **SEA_Brand_Core** | AG1 `vinhomes hoc mon` (thuần)<br>AG2 `+ giá/bảng giá`<br>AG3 `+ vị trí/mặt bằng`<br>AG4 `+ chính sách/thanh toán` | **Chính xác + Cụm từ** *(bỏ Rộng)* | Tách theo ý định để viết RSA và LP khớp. Căn cứ: `04` cho thấy "vinhomes hóc môn giá bán" CP/SQL 600.500đ vs "vinhomes hóc môn ở đâu" 1.040.867đ — ý định khác nhau, giá khác nhau |
| **SEA_Brand_Defense** | AG1 các biến thể sai chính tả/không dấu | Cụm từ | `vinhomes hoc mon` (không dấu) CTR 15,4% — cao nhất `04` |
| **SEA_Generic_NhaPho** | AG1 nhà phố + địa bàn<br>AG2 shophouse<br>AG3 biệt thự | **Chính xác + Cụm từ**, Rộng chỉ trong nhóm riêng có tCPA | — |
| **SEA_Generic_CanHo** | AG1 căn hộ + địa bàn<br>AG2 căn hộ + tầm giá | Chính xác + Cụm từ | Tách khỏi nhà phố vì tầm giá 2,9–4,6 tỷ vs 6,8–11,5 tỷ ⇒ LP và ad copy khác nhau |
| **SEA_DSA_LongTail** *(mới)* | AG1 DSA theo trang LP | Dynamic | Thay thế vai trò "khám phá từ khóa mới" mà đối sánh Rộng đang làm sai. Chạy tCPA cứng để không phình |
| **PMAX_Lead_Clean** *(dựng lại)* | 1 asset group: nhóm Ở thực<br>1 asset group: nhóm Đầu tư | — | **Bắt buộc trước khi bật:** brand exclusion ON, danh sách loại trừ vị trí đặt, chỉ nhận conversion `qualified_lead` |
| **GDN_RMK_Segmented** | AG1 form_start chưa submit (30d)<br>AG2 xem `/bang-gia` (30d)<br>AG3 tải PDF bảng giá (60d) | — | Hiện đang gộp chung "Web30d". `10_GA4` mục D: GDN data-driven +40,9% vs last-click ⇒ có giá trị thật, đang bị đo sai |
| **YT_Video_MoBan** | AG1 remarketing video (bật từ GĐ2) | — | Chỉ đối tượng remarketing, không prospecting |

**Danh sách phủ định chia sẻ (áp cho toàn tài khoản) — dựng ngay ngày 1**, tối thiểu 5 nhóm, nguồn `04_SEARCH_TERMS`:

| Nhóm phủ định | Từ mẫu | Chi phí cứu được (90 ngày qua) |
|---|---|---|
| Tuyển dụng/việc làm | tuyển dụng, việc làm, tuyển, lương | 35.953.000đ |
| Thuê | thuê, cho thuê, nhà trọ, kho xưởng, nguyên căn | 67.800.000đ |
| Giáo dục | vinschool, học phí, trường | 10.409.000đ |
| Phân khúc sai | 100 triệu, giá rẻ, chung cư mini, thổ cư | 40.680.000đ |
| Thông tin/tiêu cực | quy hoạch, bản đồ, lừa đảo, có thật không | 60.472.000đ |
| **Cộng** | | **215.314.000đ** *(11,9% ngân sách kỳ qua)* |

**Thay đổi nhắm mục tiêu (áp ngày 1):**
- Vị trí: **chỉ TP.HCM + Bình Dương + Long An** (giữ vì có 59 SQL, CP/SQL 3,07–3,36tr, còn cứu được). **Loại trừ**: Hà Nội, Đà Nẵng, Cần Thơ & ĐBSCL, ngoài Việt Nam → cứu 364.314.474đ (A6).
- Tùy chọn vị trí: đổi từ "Hiện diện HOẶC quan tâm" → **"Hiện diện"**.
- Ngôn ngữ: bỏ Tiếng Anh.
- **Tắt Search Partners + Display Network** trong 3 chiến dịch Search (A17).
- Lịch quảng cáo: giảm giá thầu **−40% khung 23:00–06:00**, **−25% khung 20:00–23:00** (tỷ lệ gọi lại 12–21%, `07A`); **+15% khung 09:00–12:00 và 14:00–17:00** (gọi lại 91–93%). Cuối tuần T7/CN: **−35%** trên toàn tài khoản trừ Brand (2/8 sale trực, `01C`).
- Đối tượng: chuyển từ **Quan sát → Nhắm mục tiêu/Điều chỉnh giá thầu**; thêm danh sách loại trừ "đã cọc / đã ký HĐMB".
- Tiện ích bổ sung ngay: **Cuộc gọi** (giờ 08:00–20:00), **Biểu mẫu khách hàng tiềm năng**, **Vị trí** (nhà mẫu), **Chú thích**, **Hình ảnh**, nâng Sitelink từ 4 lên 8.

## C4. Chiến lược giá thầu và điều kiện chuyển đổi

| Chiến dịch | GĐ1 | GĐ2 | GĐ3 | **Điều kiện chuyển (ngưỡng số cụ thể)** |
|---|---|---|---|---|
| SEA_Brand | **Tỷ lệ hiển thị mục tiêu 90%, vị trí đầu trang**, trần CPC 20.000đ | tCPA 800.000đ/SQL | tCPA 750.000đ | Chuyển sang tCPA khi: IS ≥ 85% trong 14 ngày liên tục **VÀ** ≥ 30 SQL tích lũy trong 30 ngày. Quay lại IS-target nếu IS tụt <75% trong 7 ngày |
| SEA_Generic_NhaPho / _CanHo | **tCPA 2.600.000đ/SQL** (không dùng Max Clicks) | tCPA 2.200.000đ | tCPA 1.900.000đ | Siết tCPA −15% khi đạt ≥ 50 SQL/30 ngày **VÀ** CP/SQL thực ≤ 90% mục tiêu trong 14 ngày. Nới +15% nếu khối lượng SQL giảm >30% so với 30 ngày trước |
| SEA_DSA_LongTail | tCPA 2.600.000đ | tCPA 2.200.000đ | tCPA 1.900.000đ | Cụm từ nào đạt ≥ 3 SQL/30 ngày → nâng thành từ khóa Chính xác trong nhóm tương ứng |
| PMAX_Lead_Clean | **TẮT** | **tCPA 3.000.000đ** (bật ngày 31, sau khi tín hiệu sạch ≥ 30 ngày) | tCPA 2.400.000đ | Bật lại khi: conversion action đã đổi sang `qualified_lead` ≥ 30 ngày **VÀ** đã có ≥ 50 offline conversion import. Tắt lại nếu sau 30 ngày CP/SQL > 4.000.000đ **hoặc** SQL/Lead < 20% |
| GDN_Remarketing | tCPA 2.500.000đ | tCPA 2.200.000đ | tCPA 2.000.000đ | Tắt segment nào có CP/SQL > 4.000.000đ sau 45 ngày |
| YT_Video | **TẮT** | tCPV, đo bằng view-through + Brand search lift | tCPV | Bật ngày 31. Đo bằng **thí nghiệm địa lý (geo holdout)** chứ không bằng last-click — vì `10_GA4` D cho thấy YT data-driven +283,7% vs last-click. Tắt nếu geo test không cho lift ≥ 10% Brand search volume sau 30 ngày |
| SEA_Competitor | **TẮT** | Chính xác + CPC thủ công trần 35.000đ | như GĐ2 | Chỉ bật khi phát hiện đối thủ đấu giá trên brand (D2). CPC hiện 55.164đ là quá cao — trần 35.000đ |

**Nguyên tắc chung:** không có chiến lược nào được đặt tCPA cho tới khi conversion action đã đổi sang lead thật (C5 bước 1). Chạy tCPA trên tín hiệu rác chính là lỗi đang có.

## C5. KẾ HOẠCH ĐO LƯỜNG *(mục riêng — điều kiện tiên quyết của mọi thứ khác)*

### C5.1 — Sửa trong Google Ads / GA4

| # | Việc | Ngày | Chi tiết | Cách kiểm tra sau khi sửa |
|---|---|---|---|---|
| M1 | **Bỏ `view_price_page` và `engaged_30s` khỏi cột "Chuyển đổi"** | **N1** | Đổi sang "Chuyển đổi phụ" (Secondary) — giữ để phân tích, không dùng để đấu thầu | Cột "Chuyển đổi" tài khoản phải giảm ~973 lượt/90 ngày (**25,5%**). Kiểm tra: sau 7 ngày, tổng chuyển đổi ≈ 74,5% mức cũ |
| M2 | **Khử trùng `click_to_call`** | N1 | Đổi đếm từ "Mọi lượt" (Every) → **"Một lượt" (One)** trong cài đặt hành động chuyển đổi | Chênh lệch lượt vs người dùng duy nhất phải về ~0. Kiểm tra GA4: `click_to_call` event count ≈ user count (hiện 1.132 vs 779) |
| M3 | **Tạo conversion action `qualified_lead`** | N2–N5 | Nhận từ CRM qua offline import; đây là action duy nhất dùng cho tCPA từ GĐ2 | Đối chiếu số `qualified_lead` trong Ads với `Lead_SQL` trong CRM hàng tuần, sai lệch phải <5% |
| M4 | **Bật Enhanced Conversions for Leads** | N3 | Băm SHA-256 email/SĐT ở phía client | Google Ads → Chuyển đổi → cột "Trạng thái chẩn đoán" = "Đang ghi nhận". Kỳ vọng +10–20% khớp (`12_GTM` #14) |
| M5 | **Đánh dấu `zalo_click` (khử trùng theo người) và `file_download` là sự kiện chính** | N7 | Nhập vào Ads dưới dạng **chuyển đổi phụ** trước, quan sát 30 ngày mới cân nhắc nâng cấp | 894 + 1.206 lượt/90 ngày phải bắt đầu xuất hiện trong GA4 Key Events. So SL zalo_click unique với lead Zalo trong CRM |
| M6 | **Đổi mô hình phân bổ sang Data-driven** | N30 (cuối GĐ1) | Chỉ đổi **sau khi** tín hiệu đã sạch — đổi trước sẽ ra kết quả sai | So báo cáo trước/sau: kỳ vọng Brand giảm ~32%, GDN tăng ~41%, YT tăng ~284% (`10_GA4` D). Nếu lệch xa mẫu này ⇒ tín hiệu chưa sạch |
| M7 | **Bật Consent Mode v2 + modeled conversions** | N14 | — | GA4 → Admin → Consent settings hiển thị "Đã nhận tín hiệu đồng ý" |

### C5.2 — Sửa trong GTM

| # | Việc | Ngày | Chi tiết | Cách kiểm tra sau khi sửa |
|---|---|---|---|---|
| G1 | **Xóa thẻ #2 "GA4 Configuration – Copy of Main"** | **N1** | Thẻ trùng gây đếm đôi page_view từ ngày 31 (v22) | GTM Preview: mỗi lần tải trang chỉ bắn **1** `page_view`. GA4 Realtime: số phiên phải giảm về mức đúng |
| G2 | **Đổi trigger `generate_lead` từ CSS class → `dataLayer.push`** | **N1** | Dev thêm `dataLayer.push({event:'generate_lead', lead_id:'...'})` vào callback thành công của form. Bỏ hoàn toàn selector `.form-register` | GTM Preview + đổi thử class trên staging: sự kiện **vẫn phải bắn**. Đây là bài test chống lặp lại sự cố N44–46 |
| G3 | **Cài biến ẩn lưu GCLID/gbraid/wbraid vào form** | **N2** | Đọc từ URL param, lưu vào cookie 90 ngày, đổ vào hidden field, CRM ghi nhận | Gửi 1 form test có `?gclid=TEST123` → bản ghi CRM phải chứa `TEST123`. **Đây là khóa mở của toàn bộ offline conversion import** |
| G4 | **Tạo cảnh báo tự động khi chuyển đổi = 0** | **N2** | GA4 Custom Insight: `generate_lead = 0` trong 6 giờ → email + Zalo cho marketing@ và dev@ | Cố tình tắt thẻ 30 phút trên staging → phải nhận được cảnh báo |
| G5 | **Gắn Clarity session ID vào bản ghi CRM** | N5 | `clarity('identify', ...)` → hidden field | Mở 1 lead bất kỳ trong CRM → phải bấm thẳng sang được bản ghi hình Clarity |
| G6 | **Dọn container: gỡ 3 thẻ đối tác sàn F2 + thẻ Zalo Tracking không rõ nguồn** | N7 | `12_GTM` A: "Không rõ nguồn gốc — cần rà soát bảo mật", "+0,3s LCP" | Đo LCP trước/sau bằng PageSpeed/CrUX. Mục tiêu: 412 KB JS bên thứ ba xuống **< 250 KB**, LCP cải thiện ≥ 0,3s |
| G7 | **Dựng server-side GTM** | N45–N60 (GĐ2) | Việc lớn nhất, để sau vì cần hạ tầng | So `generate_lead` client vs server: chênh lệch cho biết % mất do ad-blocker. Kỳ vọng thu hồi 5–15% |

### C5.3 — Thứ tự triển khai và lý do

```
NGÀY 1   M1, M2, G1, G2        ← chặn máu: ngừng dạy máy học bằng tín hiệu rác
NGÀY 2   G3, G4                ← GCLID + cảnh báo: mở đường cho M3, chống tái phát N44-46
NGÀY 3   M4                    ← Enhanced Conversions
NGÀY 5   G5                    ← Clarity ↔ CRM
NGÀY 7   M5, G6                ← thêm tín hiệu tốt, dọn container
NGÀY 14  M7                    ← Consent Mode
NGÀY 21  M3 chạy thật          ← offline import (cần 14 ngày tích GCLID mới có dữ liệu)
NGÀY 30  M6                    ← đổi mô hình phân bổ, chỉ sau khi tín hiệu sạch 30 ngày
NGÀY 45+ G7                    ← server-side
```

**Vì sao thứ tự này không đảo được:** M3 (offline import) cần G3 (GCLID) đã chạy đủ lâu để có dữ liệu → không thể làm M3 trước G3. M6 (data-driven) đọc lịch sử chuyển đổi → nếu đổi trước M1/M2 thì mô hình học từ 34,7% dữ liệu rác. G2 phải cùng ngày với M1 vì cả hai đều làm thay đổi số chuyển đổi — gộp lại thành **một mốc gián đoạn duy nhất** để giai đoạn học lại của Smart Bidding chỉ xảy ra 1 lần.

### C5.4 — Kiểm tra tổng thể sau khi sửa (nghiệm thu ngày 14 và ngày 30)

| Chỉ số nghiệm thu | Trước | Mục tiêu sau |
|---|---|---|
| Tỷ lệ Chuyển đổi Ads / Lead CRM | **1,494x** (PMax 2,14x) | **≤ 1,15x** ở mọi chiến dịch (ngưỡng "tốt" sheet `09` = 1,0–1,2x) |
| % lead CRM có GCLID | **0%** | **≥ 85%** |
| Số hành động tính vào cột "Chuyển đổi" | 4 (2 là rác) | 2 (`generate_lead`, `click_to_call` unique) → 1 (`qualified_lead`) từ GĐ2 |
| Thẻ trong GTM container | 34 | ≤ 25 |
| JS bên thứ ba | 412 KB | < 250 KB |
| Cảnh báo chuyển đổi = 0 | Không có | Có, đã test bằng cách tắt thẻ thử |
| Số ngày phát hiện sự cố đo lường | **3 ngày 5 giờ** (N44–47) | **≤ 6 giờ** |

## C6. Trang đích, tiện ích, đối tượng

### Trang đích — ưu tiên tuyệt đối trong tuần 1

| # | Việc | Ngày | Căn cứ số | Kỳ vọng |
|---|---|---|---|---|
| L1 | **Sửa lỗi JS `e.setDate` (Safari iOS 17.x)** — thay date picker tùy chỉnh bằng `<input type="date">` native | **N1–N2** | Clarity #4: 4.196 phiên, **280–340 lead**, CHƯA SỬA, sống sót qua cả v2 | +93–113 lead/30 ngày ≈ 66–80 triệu đồng |
| L2 | **Nút CTA bị khung chat che <380px** — tăng `padding-bottom` + z-index, thu nhỏ widget chat trên mobile | **N2** | Clarity #5: 2.741 phiên, 60–90 lead | +20–30 lead/30 ngày |
| L3 | **`tel:` trên desktop** — đổi thành click-to-copy + hiện Zalo QR | N3 | Clarity #6: 1.204 phiên, 1.847 nhấp chết, 30–50 lead | +10–17 lead/30 ngày |
| L4 | **Bỏ nốt trường thừa trong form v2** | N7 | v1: trường CMND ở vị trí 4/7 làm **61% bỏ dở**. v2 đã còn 3 trường → giữ 3, thêm nút "Gọi ngay/Zalo" song song | Tỷ lệ hoàn tất form v2 28,0% → mục tiêu **≥ 33%** |
| L5 | **Tách 2 landing page theo phân khúc** | N14 | 18–34% lead "sai phân khúc, ngân sách <2 tỷ" (`08C`) → LP hiện không lọc giá | LP nhà phố (6,8–11,5 tỷ) và LP căn hộ (2,9–4,6 tỷ), **hiện giá ngay above-the-fold** để tự lọc |
| L6 | **Bật A/B test thật** | N21 | Sheet `05`: "1 phiên bản, không thử nghiệm" | Chạy liên tục, mỗi test ≥ 2 tuần hoặc ≥ 200 conversion/nhánh |
| L7 | Giữ LCP < 2,0s sau khi thêm nội dung | liên tục | v2 đang 1,9s; GTM đóng góp ~0,8s (G6 sẽ gỡ bớt) | LCP ≤ 2,0s trên mobile CrUX |

**Không được làm:** đừng redesign lại LP v2. Nó đã cho +37,3% tỷ lệ hoàn tất form và CP/SQL −36,4% (A9). Chỉ vá 3 lỗi còn lại và tách phân khúc.

### Đối tượng

| Danh sách | Dùng cho | Điều chỉnh giá thầu đề xuất |
|---|---|---|
| `form_start` chưa `generate_lead` (7.458 − 1.715 = **5.743 người** bỏ dở form) | GDN AG1 + Search bid adjustment | +30% |
| Đã tải PDF bảng giá (**1.206** lượt) | GDN AG3 + PMax audience signal | +25% |
| Đã xem `/bang-gia` không đăng ký (612) | GDN AG2 | +20% |
| **Đã đặt cọc / ký HĐMB** | **LOẠI TRỪ toàn tài khoản** | — |
| Customer Match từ CRM (2.557 lead) | Loại trừ khỏi prospecting + làm seed cho Similar | — |
| Vùng lõi Q.12/Hóc Môn/Gò Vấp (CP/SQL 1,92–2,08tr) | Bid adjustment vị trí | +20% |
| Máy tính để bàn (CP/SQL 1,85tr, CVR 4,02%) | Bid adjustment thiết bị | **+25%** |
| Máy tính bảng (CP/SQL 3,91tr, CVR 1,71%) | Bid adjustment thiết bị | **−30%** |

*(Điều chỉnh thiết bị chỉ áp dụng **sau** khi L1/L2 xong — vì chênh lệch mobile/desktop một phần do lỗi kỹ thuật, không phải bản chất thiết bị, xem A12.)*

## C7. Tiêu chí dừng / mở rộng — ngưỡng số cụ thể

### Tiêu chí DỪNG (tắt hoặc cắt 50% ngân sách trong 24 giờ)

| # | Đối tượng | Ngưỡng dừng | Cửa sổ đánh giá |
|---|---|---|---|
| 1 | Bất kỳ chiến dịch nào | CP/SQL > **5.000.000đ** (ngưỡng báo động sheet `09`) | 30 ngày liên tục |
| 2 | Bất kỳ chiến dịch nào | SQL/Lead < **12%** (ngưỡng báo động sheet `09`) | 30 ngày, tối thiểu 50 lead |
| 3 | Chiến dịch đã chi > 150 triệu | **0 cọc** | 45 ngày |
| 4 | PMax sau khi bật lại | CP/SQL > 4.000.000đ **hoặc** thoát nhanh <3s > 50% (Clarity) | 30 ngày |
| 5 | Cụm từ tìm kiếm bất kỳ | chi phí > 15.000.000đ và **0 SQL** | 30 ngày → thêm phủ định ngay |
| 6 | **Toàn tài khoản** | lead/ngày > **60** (62,5% năng lực 96/ngày) **hoặc** lead bị bỏ sót > 15/tuần | tuần |
| 7 | Toàn tài khoản | pace chi tiêu > 105% kế hoạch giai đoạn | tuần |
| 8 | Thiết bị/khung giờ/vùng | CP/SQL > 2x mức trung bình tài khoản | 30 ngày |

### Tiêu chí MỞ RỘNG (giải ngân từ quỹ dự phòng 200 triệu)

| # | Đối tượng | Ngưỡng mở rộng | Mức tăng cho phép |
|---|---|---|---|
| 1 | Bất kỳ chiến dịch nào | CP/SQL ≤ **1.800.000đ** (ngưỡng "tốt") **VÀ** ≥ 30 SQL/30 ngày | +20% ngân sách/tuần, tối đa +50%/tháng |
| 2 | SEA_Brand | mất IS do ngân sách > **10%** | tăng đến khi mất IS ngân sách < 10%, **trần 200 triệu/giai đoạn** |
| 3 | Nhóm quảng cáo | ≥ 3 cọc/30 ngày **VÀ** ROAS ≥ 3,0x | +30% |
| 4 | Cụm từ tìm kiếm | ≥ 3 SQL/30 ngày | nâng thành từ khóa Chính xác, tách nhóm riêng |
| 5 | Vùng địa lý | CP/SQL ≤ 2.200.000đ | +25% bid adjustment |

**Quy tắc chống lặp lỗi cũ:** **không** chiến dịch nào được tăng ngân sách dựa trên chỉ số `CPL theo Ads`. Chỉ 3 chỉ số được phép làm căn cứ tăng tiền: **CP/SQL**, **CP/cọc**, **ROAS**. Đây chính là sai lầm đã dẫn tới việc PMax được cấp 26,4% ngân sách (CPL Ads 267.817đ — rẻ nhất tài khoản, 0 cọc).

### Nhịp giám sát

| Tần suất | Nội dung |
|---|---|
| **Hàng ngày** | Cảnh báo chuyển đổi=0 (G4), pace ngân sách, lead/ngày vs năng lực sale |
| **Hàng tuần (T2)** | Search terms → phủ định; CP/SQL theo chiến dịch; đối chiếu Ads vs CRM (ngưỡng ≤1,15x); SLA gọi lại |
| **2 tuần/lần** | Clarity: rage/dead click, lỗi JS; kết quả A/B test LP |
| **Hàng tháng** | Đối chiếu 3 nguồn đầy đủ; xem xét mở rộng/dừng; báo cáo ROAS cho ban giám đốc |

---

# PHẦN D — XỬ LÝ TÌNH HUỐNG

## D1. "Cắt hết ngân sách brand, dồn cho từ khóa chung"

**Trả lời: không cắt — ngược lại, tôi đề xuất tăng Brand 42,2%. Nhưng anh nói đúng một nửa, và nửa đó tôi xử lý bằng cách khác.**

### Nửa anh đúng
Sheet `10_GA4` mục D: theo mô hình phân bổ dựa trên dữ liệu, Brand chỉ đáng được ghi nhận **401 lead** chứ không phải 592 — tức **32,3% công trạng của Brand là ăn theo** kênh khác (GDN +40,9%, YouTube +283,7%). Tôi ghi nhận điều này và đó là lý do tôi đổi mô hình phân bổ sang data-driven ở ngày 30 (C5, M6).

### Nửa anh chưa đúng — 5 con số

| Câu hỏi | Số | Nguồn |
|---|---|---|
| Brand ăn bao nhiêu ngân sách? | **14,4%** (260,2 triệu) | CSV, gộp `Chi_phi` |
| Brand tạo bao nhiêu cọc? | **13/18 = 72,2%** | CSV `Dat_Coc` |
| Brand tạo bao nhiêu doanh thu? | **2,28/3,13 tỷ = 72,8%** | CSV `DoanhThu_HoaHong` |
| ROAS Brand | **8,76x** (GĐ3: **10,97x**) | 2,28 tỷ / 260,2 triệu |
| CP/cọc Brand vs ngưỡng hòa vốn | **20.016.846đ** vs 60.333.333đ | rẻ hơn **3,0 lần** |

Còn "từ khóa chung" mà anh muốn dồn tiền vào — nó **đã** được dồn tiền rồi:

| | SEA_Generic | SEA_Brand |
|---|---|---|
| Chi phí | **677.994.000đ (37,6% — cao nhất tài khoản)** | 260.219.000đ (14,4%) |
| Cọc | 5 | **13** |
| CP/SQL | 3.549.707đ | **739.259đ** (rẻ hơn **4,8x**) |
| CP/cọc | 135.598.800đ | **20.016.846đ** (rẻ hơn **6,8x**) |
| ROAS | 1,25x | **8,76x** |
| Lead dùng được (`08C`) | 46% | **67%** |

**Generic đã ăn gấp 2,6 lần ngân sách Brand và trả về ROAS thấp hơn 7 lần.** Chuyển tiền từ Brand sang Generic là chuyển từ 8,76x sang 1,25x.

### Bằng chứng quyết định: Brand đang bị bóp, không phải đang thừa

CSV cột `Mat_IS_NganSach`: Brand **mất 40,4% Impression Share vì hết ngân sách** — Impression Share chỉ **52,6%** (sheet `09` xếp <60% là "báo động", và mất IS ngân sách >20% ở chiến dịch tốt là *"tiền đang bỏ lại trên bàn"*). Nghĩa là: **cứ 10 người đang gõ tên "Vinhomes Hóc Môn" trên Google thì gần 5 người không nhìn thấy quảng cáo của mình.** Họ vẫn tìm — và sheet `04` cho thấy quảng cáo đối thủ đang xuất hiện trên các cụm từ so sánh dự án.

Kiểm chứng thêm: GĐ3 Brand tăng ngân sách 80% (72,3 → 130,3 triệu) mà ROAS **tăng** từ 7,19x lên 10,97x — nếu Brand đã bão hòa, ROAS phải giảm khi tăng chi.

### Đề xuất thay thế — tôi đồng ý với tinh thần của anh, chỉ đổi nguồn tiền

Thay vì cắt Brand, tôi cắt đúng chỗ đang lãng phí thật để dồn cho từ khóa chung chất lượng cao:

| Nguồn cắt | Số tiền | Cọc mất |
|---|---|---|
| SEA_Competitor (0 cọc, CP/SQL 58,9tr) | 176.746.000đ | 0 |
| PMax 30 ngày đầu (0 cọc, 74,3% thoát <3s) | ~135.000.000đ | 0 |
| 11 cụm từ rộng 0 SQL | 242.982.000đ | 0 |
| 4 vùng địa lý 0 cọc | 364.314.474đ | 0 |
| **Tổng giải phóng** | **~919 triệu** | **0** |

**Kết luận một câu để anh mang vào họp:** Brand không "ăn theo" — nó là điểm thu hoạch, và ta đang đóng cửa quầy thu hoạch 5 tiếng mỗi ngày vì hết ngân sách. **Đề xuất kiểm chứng:** nếu anh vẫn nghi ngờ, tôi chạy **thí nghiệm brand-holdout theo địa lý** trong 21 ngày (tắt Brand ở 2 quận, giữ ở 2 quận tương đương) và đo chênh lệch lead trực tiếp/organic. Đây là cách duy nhất trả lời dứt điểm câu "khách có tự tìm đến không" bằng số — bộ dữ liệu hiện tại **không đủ** để trả lời.

---

## D2. Đối thủ bắt đầu đấu giá trên tên thương hiệu dự án

**Bối cảnh số:** Brand hiện IS 52,6%, mất IS do **thứ hạng 7,0%** (còn thấp — nghĩa là chưa bị đẩy mạnh) và mất IS do **ngân sách 40,4%** (đây mới là lỗ hổng). CTR Brand 11,63% — sheet `09` xếp 8–12% là "trung bình", >12% là "tốt". *"Giảm mạnh thường do đối thủ đấu giá"*. **Ta chưa bị tấn công nặng, nhưng cửa đang mở toang vì hết tiền.**

### 4 hành động — 2 trong Google Ads, 2 ngoài Google Ads

**Trong Google Ads:**

**1. Bịt lỗ hổng ngân sách trước khi bịt lỗ hổng giá thầu (N1, tác động lớn nhất).**
Chuyển Brand sang **"Tỷ lệ hiển thị mục tiêu 90%, vị trí đầu trang"**, nâng ngân sách 260,2 → 370 triệu (C1). Lý do thứ tự: đối thủ chỉ chiếm được chỗ mà ta bỏ trống — 40,4% IS mất do ngân sách là 40,4% cửa mở sẵn. Bịt cái này rẻ hơn nhiều so với đấu giá tay đôi. Ngưỡng theo dõi: IS ≥ 85% trong 14 ngày; cảnh báo nếu mất IS do **thứ hạng** vượt 15% (hiện 7,0%).

**2. Nộp khiếu nại nhãn hiệu + siết cấu trúc phòng thủ (N1–N3).**
- Nộp **Google Ads Trademark Complaint** cho "Vinhomes" (đại lý F1 có tư cách phối hợp với chủ đầu tư) — buộc đối thủ gỡ tên thương hiệu khỏi **nội dung quảng cáo**, đây là đòn hiệu quả nhất vì làm CTR quảng cáo của họ sụp.
- Tách **SEA_Brand_Defense** riêng cho biến thể sai chính tả/không dấu — `04` cho thấy `vinhomes hoc mon` (không dấu) có CTR **15,4%**, cao nhất tài khoản, đây là nơi đối thủ hay chen vào.
- Bật **PMax brand exclusion** (`05`: CHƯA bật) — hiện PMax của chính ta đang tự ăn traffic Brand.
- Bổ sung tiện ích **Cuộc gọi + Vị trí + Chú thích + Hình ảnh** (`05`: đang thiếu) → chiếm nhiều diện tích SERP hơn, đẩy đối thủ xuống dưới màn hình đầu.
- Bật báo cáo **Chi tiết đấu giá (Auction Insights)** hàng tuần để biết chính xác ai, tỷ lệ trùng lặp bao nhiêu, tỷ lệ vượt hạng bao nhiêu.

**Ngoài Google Ads:**

**3. Chiếm sạch SERP không mất tiền (N7–N30).**
Với truy vấn thương hiệu, quảng cáo chỉ là 1 trong nhiều ô. Cần: Google Business Profile cho nhà mẫu (đang có nhà mẫu mở 8:00–18:00 mà chưa dùng), 3–5 bài SEO cho chính các truy vấn đang chạy quảng cáo tốn tiền vô ích — `04` cho thấy **"vinhomes hóc môn có thật không"** (13.011.000đ, CP/SQL 4.337.000đ) và **"vinhomes hóc môn ở đâu"** (15.613.000đ) là truy vấn thông tin, trả lời bằng bài SEO rẻ hơn nhiều so với trả 22.786đ/click. Cộng thêm YouTube video nhà mẫu (LP v2 đã có video — tái sử dụng).

**4. Rút ngắn thời gian phản hồi xuống dưới 5 phút cho lead Brand (N1).**
Đây là hành động chống đối thủ mạnh nhất và không ai bàn tới: khách gõ tên dự án là khách nóng, họ điền form ở **3–5 sàn cùng lúc**. Ai gọi trước thì thắng, không phụ thuộc ai đứng vị trí 1 trên Google. Số: `08A` cho thấy lead gọi <5 phút có tỷ lệ cọc **1,82%** vs 0,04% khi gọi sau 12 giờ — **gấp 45,5 lần**. Hiện 47,0% lead được gọi sau 2 giờ. Hành động cụ thể: định tuyến riêng lead từ SEA_Brand vào hàng đợi ưu tiên, SLA 5 phút, cảnh báo Zalo cho sale trực.

**Điều KHÔNG làm:** không tăng ngân sách SEA_Competitor để "đánh trả". Số liệu đã trả lời: 176,7 triệu, 3 SQL, **0 cọc**, CP/SQL 58,9 triệu, 26% lead là môi giới/đối thủ. Đấu giá trên tên đối thủ là trò chơi cả hai cùng thua — ta đã thua 176,7 triệu.

---

## D3. "PMax có CPA thấp nhất, dồn ngân sách vào đó"

**Trả lời: KHÔNG. Đây chính xác là cái bẫy đã làm mất 475,4 triệu đồng trong 90 ngày qua — và kế toán đang đọc đúng con số nhưng con số đó là số giả.**

### Bước 1 — Con số kế toán nhìn thấy là đúng

| Chiến dịch | CPL theo Ads |
|---|---|
| **PMAX** | **267.817đ** ← rẻ nhất tài khoản |
| SEA_Brand | 298.759đ |
| GDN | 430.493đ |
| YT | 470.017đ |
| SEA_Generic | 1.021.075đ |
| SEA_Competitor | 5.701.484đ |

### Bước 2 — Đi xuống dưới phễu thì đảo ngược hoàn toàn

| Chỉ số | PMAX | SEA_Brand | PMax so với Brand |
|---|---|---|---|
| CPL theo Ads | **267.817đ** | 298.759đ | rẻ hơn 10% ✔ |
| CPL theo CRM | 573.433đ | 303.639đ | **đắt hơn 1,9x** |
| **CP/SQL** | **7.793.049đ** | 739.259đ | **đắt hơn 10,5x** |
| **CP/lead dùng được** (`08C`) | **8.191.901đ** | 453.193đ | **đắt hơn 18,1x** |
| SQL/Lead | 7,4% | 41,1% | — |
| **Đặt cọc** | **0** | 13 | — |
| **Doanh thu** | **0đ** | 2.280.000.000đ | — |
| **ROAS** | **0,00x** | 8,76x | — |

**PMax chi 475.376.000đ và tạo ra đúng 0 đồng doanh thu.** CPL "rẻ" không phải vì PMax giỏi mua lead — mà vì **39,3% "chuyển đổi" của PMax là sự kiện rác**: 438 lượt xem trang bảng giá + 259 lượt ở lại 30 giây = 697/1.775 (`10_GA4` mục B). Nói cách khác, ta đang trả 267.817đ để một người ở trên trang 30 giây rồi thoát, và gọi đó là "lead".

### Bước 3 — Ba nguồn độc lập xác nhận traffic PMax là rác

| Nguồn | Bằng chứng |
|---|---|
| Clarity (mục B) | **74,3% phiên thoát dưới 3 giây**; phiên trung vị **3 giây**; ghi chú của Clarity: *"Bất thường — xem lại vị trí đặt quảng cáo"* |
| GA4 (mục B) | tỷ lệ tương tác **8,7%** (Brand 62,4%); **1,09 trang/phiên**; cuộn 90% chỉ **4%**; hao hụt click→phiên **28,0%** — 11.116 click đã trả tiền mà không thành phiên |
| CRM (`08C`) | **31% lead trùng SĐT**, 24% số sai, chỉ **7% lead dùng được** — kém nhất tài khoản |

### Bước 4 — Chi phí cơ hội, tính bằng số

Nếu 475.376.000đ của PMax được chi ở Brand với CP/cọc thực tế của Brand (20.016.846đ): **≈ 23,7 cọc ≈ 4,29 tỷ doanh thu hoa hồng**. Con số này là **ước tính có giới hạn** — Brand không hấp thụ hết 475 triệu vì bị chặn bởi khối lượng tìm kiếm thương hiệu (đó là lý do C1 chỉ chuyển 110 triệu sang Brand, phần còn lại sang Generic/DSA). Nhưng ngay cả khi chỉ hấp thụ được 1/3, đó vẫn là ~8 cọc ≈ 1,45 tỷ.

### Bước 5 — Tôi đề xuất gì

**Không tắt vĩnh viễn** — vì nguyên nhân gốc là tín hiệu đầu vào sai (`12_GTM` mục C ghi thẳng: *"Máy học tối ưu theo tín hiệu rác — nguyên nhân gốc của toàn bộ vấn đề PMax"*), không phải bản chất PMax. Lộ trình:

1. **Tắt PMax 30 ngày** (GĐ1) → tiết kiệm ~135 triệu.
2. Trong 30 ngày đó: bỏ `view_price_page`/`engaged_30s` khỏi chuyển đổi (M1), khử trùng `click_to_call` (M2), cài GCLID (G3), chạy offline import `qualified_lead` (M3).
3. **Ngày 31 bật lại PMax** với: chỉ nhận `qualified_lead`, tCPA 3.000.000đ, brand exclusion ON, danh sách loại trừ vị trí đặt, ngân sách 110 triệu.
4. **Ngưỡng dừng lại:** sau 30 ngày nếu CP/SQL > 4.000.000đ **hoặc** SQL/Lead < 20% **hoặc** thoát nhanh <3s > 50% → tắt hẳn, chuyển toàn bộ sang Search.

**Câu chốt cho kế toán:** *"CPA thấp nhất tài khoản" là 267.817đ cho một chỉ số mà 39,3% là người xem trang rồi thoát trong 3 giây. Số tiền thật đã chi là 475,4 triệu. Số cọc thật nhận về là 0. Ta không thể trả lương bằng CPA — chỉ trả được bằng hoa hồng.*

---

## D4. Ngân sách bị cắt còn 1,2 tỷ cho 90 ngày

**Nguyên tắc: cắt theo thứ tự CP/cọc giảm dần, giữ đến cuối cùng thứ có ROAS cao nhất. Không cắt đều tay ngang.**

### Thứ tự cắt (từ trên xuống)

| Thứ tự | Cắt gì | Tiết kiệm (theo mức chi kỳ qua) | **Cọc mất** | Căn cứ |
|---|---|---|---|---|
| **1** | **SEA_Competitor — tắt hoàn toàn** | 176.746.000đ | **0** | 3 SQL, 0 cọc, CP/SQL 58,9tr = 11,8x ngưỡng báo động |
| **2** | **11 cụm từ rộng 0 SQL + tắt Search Partners/Display** | 242.982.000đ | **0** | `04`: 96 lead, 0 SQL |
| **3** | **4 vùng địa lý (HN, ĐN, Cần Thơ, ngoài VN)** | 364.314.474đ | **0** | `06`: 46 SQL, 0 cọc, CP/SQL 7,92tr |
| **4** | **YouTube — tắt hoàn toàn** | 83.193.000đ | **0** | 8 SQL, 0 cọc, CP/SQL 10,4tr. *Có rủi ro: `10_GA4` D cho thấy YT data-driven +283,7% — chấp nhận rủi ro này vì khi ngân sách sinh tồn, không nuôi được đầu phễu* |
| **5** | **PMax — giữ 100 triệu nuôi tín hiệu sạch, cắt 375,4 triệu** | 375.376.000đ | **0** | 0 cọc. Giữ tối thiểu để không mất lịch sử học máy |
| **6** | **Khung giờ 23:00–06:00 + T7/CN giảm 35%** | ~150.000.000đ | ≤1 | `07A`: gọi lại 12–34%; `07C`: T7/CN 4/18 cọc |
| **7** | **GDN — thu hẹp còn 3 segment intent cao** | ~50.000.000đ | 0 | `10_GA4` D: GDN data-driven +40,9% ⇒ **không cắt hết** |
| **8** | Generic — chỉ giữ Chính xác + Cụm từ có SQL | ~120.000.000đ | ≤1 | ROAS 1,25x, cần siết chứ chưa bỏ |

### Giữ đến cuối cùng — theo đúng thứ tự này

1. **SEA_Brand** — 13/18 cọc (72,2%), ROAS 8,76x, CP/cọc 20,0tr. Đây là thứ cuối cùng bị tắt, và nếu ngân sách xuống dưới 400 triệu thì chỉ còn nó.
2. **Sửa đo lường (C5) và sửa 3 lỗi LP (C6)** — chi phí gần bằng 0, tác động 261–339 triệu (B7). **Ngân sách bị cắt là lúc phải làm việc này gấp hơn, không phải hoãn.**
3. **SLA gọi lại 5 phút** — chi phí 0đ, `08A` cho thấy tỷ lệ cọc gấp 45,5x. Khi hết tiền mua lead, phải vắt kiệt lead đang có.
4. **SEA_Generic (Chính xác/Cụm từ)** — ROAS 1,25x, chưa lãi nhưng là nguồn khách mới duy nhất ngoài Brand.
5. **GDN remarketing intent cao** — rẻ, giữ lead đã có trong phễu.

### Phân bổ 1,2 tỷ

| Chiến dịch | Ngân sách | % | Ghi chú |
|---|---|---|---|
| SEA_Brand | 380.000.000đ | 31,7% | **Vẫn tăng 46% so với 260,2 triệu kỳ qua** — vì đây là chỗ duy nhất chắc chắn có lãi |
| SEA_Generic (Chính xác/Cụm từ) | 480.000.000đ | 40,0% | −29% so với 678,0 triệu |
| GDN_Remarketing (3 segment) | 120.000.000đ | 10,0% | −8% |
| PMax (nuôi tín hiệu sạch) | 100.000.000đ | 8,3% | −79% |
| DSA/long-tail | 80.000.000đ | 6,7% | mới, thay vai trò khám phá của đối sánh Rộng |
| Dự phòng | 40.000.000đ | 3,3% | — |
| **TỔNG** | **1.200.000.000đ** | 100% | *(assert trong script)* |

### Kỳ vọng và cảnh báo trung thực

Ngưỡng hòa vốn ROAS 3,0x: 1,2 tỷ / 60.333.333đ = **19,9 cọc**. Với 1,2 tỷ tôi cam kết **20–22 cọc** (không phải 32) — ROAS ~3,0–3,3x. **Đây là ROAS tốt hơn kế hoạch 2,1 tỷ nhưng số cọc tuyệt đối thấp hơn 38%.**

**Cảnh báo phải nói thẳng với ban giám đốc:** 1,2 tỷ **không thể** đạt 32 cọc. 32 cọc với 1,2 tỷ đòi hỏi CP/cọc 37,5 triệu — bằng 37% mức hiện tại (100,2 triệu) và thấp hơn cả CP/cọc của chiến dịch tốt nhất nếu Brand phải scale gấp đôi khối lượng. **Nếu ban giám đốc giữ nguyên KPI 32 cọc với ngân sách 1,2 tỷ, tôi từ chối cam kết và đề nghị đàm phán lại KPI xuống 20 cọc.** Ràng buộc thật không phải kỹ năng chạy quảng cáo — là khối lượng tìm kiếm thương hiệu có hạn (Brand chỉ hấp thụ được ~370–400 triệu trước khi CP/cọc tăng vọt).

---

## D5. "GA4 báo 3.820, CRM báo 2.557. Ai đúng? Từ giờ tôi nên nhìn con số nào?"

> **Cả hai đều đúng — nhưng chúng đang đếm hai thứ khác nhau.**
>
> Con số 3.820 không phải là 3.820 khách hàng. Nó là tổng của 4 loại hành động trên website, trong đó **2 loại không phải khách hàng**: 612 lượt bấm xem trang bảng giá và 361 lượt ở lại trang trên 30 giây. Cộng thêm 353 lượt bấm gọi bị đếm trùng — một người bấm 3 lần thì máy tính là 3 khách.
>
> Bóc ra: **3.820 − 353 trùng − 973 không phải khách = 2.494 khách thật**. Cộng 63 khách của ba ngày 44–46 mà hệ thống đo bị hỏng nên không ghi nhận được, ra đúng **2.557 — bằng CRM**.
>
> **Từ giờ anh nhìn 3 con số này, theo thứ tự:**
>
> | | Con số | Nghĩa là gì |
> |---|---|---|
> | 1 | **Số cọc và doanh thu hoa hồng** | Tiền thật về túi. 90 ngày qua: 18 cọc, 3,13 tỷ |
> | 2 | **Chi phí trên mỗi lead chất lượng (CP/SQL)** | Sale xác nhận đúng khách. Hiện 2,77 triệu, mục tiêu ≤2,2 triệu |
> | 3 | **ROAS** | Bỏ 1 đồng thu về mấy đồng. Hiện 1,74x, mục tiêu 3,0x |
>
> Con số 3.820 từ nay chỉ dùng để chẩn đoán kỹ thuật, không dùng để đánh giá đội marketing. Trong 30 ngày tới tôi sẽ sửa hệ thống đo để hai con số này chênh nhau dưới 15% — khi đó anh nhìn con số nào cũng ra cùng một câu chuyện.

*(147 từ)*

---

## D6. "Sửa GTM không tạo ra lead nào, để cuối quý. Giờ tăng ngân sách trước"

### Phản biện — 4 con số

**1. Đo lường sai đang trực tiếp đốt 688,6 triệu đồng.**
34,7% tín hiệu chuyển đổi là rác hoặc trùng (1.326/3.820). Máy học của Google dùng đúng tín hiệu đó để quyết định mua traffic nào. Kết quả: PMax 475,4 triệu + GDN 130,0 triệu + YouTube 83,2 triệu = **688,6 triệu (38,2% ngân sách) cho 0 cọc**. Sheet `12_GTM` mục C ghi chính lời của đội IT: *"Máy học tối ưu theo tín hiệu rác — nguyên nhân gốc của toàn bộ vấn đề PMax"*.

**2. Tăng ngân sách trên hệ thống hỏng làm mất tiền nhanh hơn, không phải kiếm tiền nhanh hơn.**
Tài khoản đang ở ROAS 1,74x — dưới hòa vốn 3,0x. Bơm thêm 300 triệu vào cấu trúc hiện tại, theo phân bổ hiện tại, thì 38,2% (114,6 triệu) chảy thẳng vào 3 kênh 0 cọc. **Đề nghị của IT tương đương: "xe đang thủng lốp, đừng vá, đạp ga mạnh hơn đi."**

**3. Chính sự cố ngày 44–46 chứng minh rủi ro không sửa.**
Trigger `generate_lead` gãy vì dev đổi class CSS, **3 ngày 5 giờ mới phát hiện** vì không có cảnh báo. Mất 63 lead khỏi Ads/GA4 vĩnh viễn, 59,5 triệu chi phí chạy mù, và Smart Bidding thấy "0 chuyển đổi" nên tự hạ giá thầu — méo mó kéo dài quá 3 ngày đó. **Trigger vẫn đang dựa trên CSS class ngày hôm nay.** Lần sau dev đổi giao diện, chuyện này lặp lại — và lần này ngân sách sẽ lớn hơn nên thiệt hại lớn hơn.

**4. Đo lường tạo ra lead — trực tiếp, đo được, 261–339 triệu.**
Ba lỗi kỹ thuật trên trang đích **CHƯA SỬA** đang chặn **370–480 lead** (`11_CLARITY` mục C), trị giá 261–339 triệu chi phí đã trả và 471–612 triệu doanh thu hoa hồng bỏ lỡ. Lỗi lớn nhất — `TypeError: e.setDate is not a function` trên Safari iOS — khiến form **không gửi được và không báo lỗi cho khách**, ảnh hưởng 4.196 phiên trên nền tảng chiếm 78,1% ngân sách. Sửa mất 1–2 ngày công dev. **ROI 13–17 lần.** Nói "đo lường không tạo ra lead" là sai về mặt số liệu.

**Đề nghị đổi khung thời gian, không đổi ưu tiên:** tôi không xin cả quý. Tôi xin **7 ngày công dev** để làm xong M1, M2, G1, G2, G3, G4, L1, L2. Sau 7 ngày, tăng ngân sách bao nhiêu cũng được — và mỗi đồng tăng thêm sẽ hiệu quả hơn ít nhất 38% vì không còn chảy vào 3 kênh 0 cọc.

### Nếu buộc phải nhượng bộ — giữ lại đúng **2** hạng mục

**Hạng mục 1 — Gỡ `view_price_page` và `engaged_30s` khỏi cột "Chuyển đổi" (M1).**
Công sức: **15 phút, trong giao diện Google Ads, không cần dev, không đụng vào GTM.** Tác động: loại bỏ ngay 973/3.820 tín hiệu rác (25,5%) khỏi dữ liệu huấn luyện của mọi chiến dịch Smart Bidding. Đây là hạng mục có tỷ lệ tác động/công sức cao nhất trong toàn bộ kế hoạch, và nó **không cần đội IT** — nên nó không thể bị hoãn vì lý do IT bận. Kèm theo (thêm 5 phút): đổi `click_to_call` từ đếm "Mọi lượt" sang "Một lượt" để bỏ 353 lượt trùng.

**Hạng mục 2 — Cảnh báo tự động khi chuyển đổi = 0 (G4).**
Công sức: **1 giờ**, tạo Custom Insight trong GA4, không cần code, không cần deploy. Tác động: đây là **bảo hiểm**. Sự cố N44–46 mất 3 ngày 5 giờ và 59,5 triệu để phát hiện; với cảnh báo thì phát hiện trong 6 giờ. Nếu ta tăng ngân sách lên 29 triệu/ngày như kế hoạch GĐ3, một sự cố 3 ngày tương tự sẽ tốn **87 triệu đồng** thay vì 59,5 triệu. Chi 1 giờ để bảo hiểm cho 2,1 tỷ ngân sách là thương vụ dễ nhất trong bản kế hoạch này.

**Hai hạng mục này cộng lại: 1 giờ 20 phút, không cần dev, bảo vệ 688,6 triệu ngân sách đang chảy sai và 2,1 tỷ sắp chi.** Nếu IT vẫn nói không có thời gian cho 1 giờ 20 phút, thì vấn đề không phải thời gian.

---

# PHẦN E — KẾ HOẠCH 7 NGÀY ĐẦU

**10 việc, sắp theo thứ tự ưu tiên (= thứ tự thực hiện). Nguyên tắc xếp hạng: chặn máu trước, mở van sau.**

| # | Ngày | Việc | Chi tiết thực hiện | **Kết quả kỳ vọng đo được** |
|---|---|---|---|---|
| **1** | **N1 sáng** | **Ngừng đốt tiền có thể dừng bằng 1 click** | Tắt SEA_Competitor; tắt PMax; tắt Search Partners + Display Network trong 3 chiến dịch Search; loại trừ vị trí Hà Nội / Đà Nẵng / Cần Thơ & ĐBSCL / ngoài Việt Nam; đổi tùy chọn vị trí sang "Hiện diện" | **Giải phóng ~9,1 triệu đồng/ngày** (Competitor 1,96tr + PMax 5,28tr + địa lý ~4,05tr, tính theo mức chi kỳ qua). Kiểm tra N2: chi phí/ngày giảm ≥ 35% mà lead/ngày giảm ≤ 15% |
| **2** | **N1 sáng** | **Dọn cột "Chuyển đổi"** *(M1 + M2 — 20 phút, không cần dev)* | `view_price_page` và `engaged_30s`: chuyển sang chuyển đổi phụ. `click_to_call`: đổi đếm "Mọi lượt" → "Một lượt" | Sau 7 ngày: cột Chuyển đổi giảm **~34,7%** (từ ~42/ngày xuống ~28/ngày); tỷ lệ Chuyển đổi Ads / Lead CRM giảm từ 1,494x về **≤ 1,15x** |
| **3** | **N1 chiều** | **Sửa lỗi JS `e.setDate` — Safari iOS 17.x** *(L1)* | Thay date picker tùy chỉnh bằng `<input type="date">` native; thêm try/catch + thông báo lỗi hiển thị cho khách; test trên Safari iOS 17 thật | Clarity: tỷ lệ phiên có lỗi JS di động giảm từ **8,9%** xuống **< 2%** trong 14 ngày. Tỷ lệ hoàn tất form di động v2 tăng từ 24,6% lên **≥ 29%**. Ước tính **+93–113 lead/30 ngày** |
| **4** | **N1 chiều** | **Sửa trigger `generate_lead` — bỏ phụ thuộc CSS class** *(G2)* | Dev push `dataLayer.push({event:'generate_lead', lead_id, value})` trong callback thành công của form; GTM đổi trigger sang Custom Event; xóa selector `.form-register` | Test nghiệm thu: đổi class form trên staging → sự kiện **vẫn bắn**. Đây là điều kiện để sự cố N44–46 không lặp lại |
| **5** | **N2** | **Cài cảnh báo chuyển đổi = 0 + xóa thẻ GA4 trùng** *(G4 + G1)* | GA4 Custom Insight: `generate_lead = 0` trong 6 giờ → email + Zalo tới marketing@ và dev@. Xóa thẻ #2 "GA4 Configuration – Copy of Main" | Test: tắt thẻ 30 phút trên staging → nhận được cảnh báo. GTM Preview: mỗi lần tải trang chỉ **1** `page_view` (hiện 2 từ ngày 31). **Thời gian phát hiện sự cố: 3 ngày 5 giờ → ≤ 6 giờ** |
| **6** | **N2** | **Cài GCLID vào form và CRM** *(G3)* | Biến GTM đọc `gclid`/`gbraid`/`wbraid` từ URL → cookie 90 ngày → hidden field; CRM thêm trường `gclid`; sửa nút CTA bị khung chat che (L2) cùng lượt deploy | Gửi form test `?gclid=TEST123` → CRM ghi nhận `TEST123`. Sau 7 ngày: **≥ 85% lead mới có GCLID** (hiện 0%). Mở khóa toàn bộ offline conversion import |
| **7** | **N2–N3** | **Dựng danh sách phủ định chia sẻ + chuyển đối sánh** | 5 nhóm phủ định (tuyển dụng, thuê, giáo dục, phân khúc sai, thông tin/tiêu cực) từ `04`; hạ tỷ trọng đối sánh Rộng từ 71% xuống **< 30%** chi phí Search; giữ Rộng chỉ trong nhóm riêng có tCPA | Sau 14 ngày: **0đ** chi cho 11 cụm từ đã liệt kê (kỳ qua: 242.982.000đ). Tỷ lệ SQL/Lead của SEA_Generic tăng từ 32,5% lên **≥ 38%** |
| **8** | **N3** | **Áp SLA gọi lại 5 phút cho lead Brand + định tuyến ưu tiên** | Lead từ SEA_Brand vào hàng đợi riêng, cảnh báo Zalo cho sale trực; dựng bảng theo dõi thời gian phản hồi theo nguồn; xử lý tồn 275 lead bị bỏ sót | Trung vị phản hồi lead Brand: **47 phút → ≤ 10 phút** trong 14 ngày. Tỷ lệ lead gọi trong 30 phút: 30% → **≥ 60%**. `08A` dự báo tỷ lệ cọc tăng từ 0,62% lên ~1,0% |
| **9** | **N4–N5** | **Chuyển giá thầu Brand sang "Tỷ lệ hiển thị mục tiêu 90%" + nâng ngân sách; chuyển Generic từ Max Clicks sang tCPA** | Brand: 2,89tr/ngày → **3,33tr/ngày**, trần CPC 20.000đ. Generic: bỏ "Tối đa hóa số lần nhấp", đặt tCPA 2.600.000đ/SQL. Thêm tiện ích Cuộc gọi + Vị trí + Chú thích + Hình ảnh, nâng Sitelink 4→8 | Impression Share Brand: **52,6% → ≥ 80%** trong 14 ngày; mất IS do ngân sách **40,4% → ≤ 15%**. CTR Brand từ 11,63% lên **≥ 13%** nhờ tiện ích |
| **10** | **N6–N7** | **Điều chỉnh lịch/thiết bị/vùng + dựng dashboard đối chiếu 3 nguồn** | Giá thầu: −40% khung 23:00–06:00, −25% khung 20:00–23:00, +15% khung 09–12h và 14–17h, −35% T7/CN (trừ Brand); +25% desktop, −30% tablet; +20% vùng lõi Q.12/Hóc Môn/Gò Vấp. Dashboard: Ads / GA4 / CRM cạnh nhau theo ngày × chiến dịch | Chi phí khung 20:00–06:00 giảm từ **26,8% → ≤ 15%** ngân sách. Dashboard chạy hàng ngày, tự tính tỷ lệ Ads/CRM và cảnh báo khi > 1,3x. Bàn giao cho ban giám đốc trong buổi họp cuối tuần 1 |

### Kết quả kỳ vọng tổng hợp sau 7 ngày

| Chỉ số | Trước (baseline 90 ngày) | Mục tiêu cuối tuần 1 | Mục tiêu cuối GĐ1 (N30) |
|---|---|---|---|
| Tỷ lệ Chuyển đổi Ads / Lead CRM | 1,494x | ≤ 1,20x | **≤ 1,15x** |
| % lead có GCLID | 0% | ≥ 85% | ≥ 90% |
| Impression Share Brand | 52,6% | ≥ 70% | **≥ 85%** |
| Mất IS Brand do ngân sách | 40,4% | ≤ 20% | **≤ 10%** |
| Tỷ lệ lỗi JS di động (Clarity) | 8,9% | ≤ 4% | **< 2%** |
| Trung vị phản hồi lead | 47 phút | ≤ 20 phút | **≤ 10 phút** |
| Chi phí khung 20:00–06:00 | 26,8% | ≤ 18% | **≤ 15%** |
| Thời gian phát hiện sự cố đo lường | 3 ngày 5 giờ | **≤ 6 giờ** | ≤ 6 giờ |
| CP/SQL | 2.770.410đ | — *(quá sớm để đo)* | **≤ 2.600.000đ** |

---

## PHỤ LỤC — Những chỗ dữ liệu KHÔNG đủ để kết luận

| # | Câu hỏi không trả lời được | Vì sao thiếu | **Cần thêm dữ liệu gì** |
|---|---|---|---|
| 1 | GDN và YouTube đóng góp bao nhiêu vào 18 cọc? | `10_GA4` D chỉ có phân bổ data-driven cho `generate_lead`, không có cho cọc | Báo cáo đường dẫn chuyển đổi (conversion path) của 18 giao dịch cọc; hoặc geo holdout test 21 ngày |
| 2 | Bao nhiêu chi phí Search rơi vào Search Partners và Display? | Bộ đề không có phân đoạn "Mạng" | Google Ads → segment Network, 90 ngày, theo chiến dịch |
| 3 | 894 lượt `zalo_click` tương ứng bao nhiêu người và bao nhiêu lead CRM? | `10_GA4` E chỉ có event count, không có user count, không phân rã theo chiến dịch, chỉ có từ ngày 71 | GA4 report `zalo_click` theo `session_campaign` + user-scoped; mapping Zalo OA ↔ CRM |
| 4 | Khách có tự tìm đến khi tắt Brand không? (câu hỏi của D1) | Không có dữ liệu holdout | Thí nghiệm brand-holdout theo địa lý 21 ngày (tắt Brand ở 2 quận, giữ ở 2 quận tương đương), đo lead trực tiếp/organic |
| 5 | Đường cong CPC của Brand ở dải IS 52% → 90% có tuyến tính không? | Chỉ có 1 điểm dữ liệu | Báo cáo mô phỏng ngân sách/giá thầu (Bid Simulator) cho SEA_Brand |
| 6 | 4 kênh khác (Facebook, Zalo Ads, telesale, sàn F2) đóng góp bao nhiêu vào 18 cọc? | `01C` ghi rõ "KHÔNG nằm trong dữ liệu này" | Dữ liệu chi phí + lead của 4 kênh này để tính blended CAC — nếu không có, mọi kết luận về ROAS chỉ đúng ở phạm vi Google Ads |
| 7 | Vì sao doanh thu thực/cọc là 173,9 triệu thay vì 181 triệu? | Không có phân rã hoa hồng theo giao dịch | Bảng chi tiết 18 giao dịch cọc: sản phẩm, giá bán, hoa hồng, chiết khấu khách |
| 8 | Số phiên GA4 từ ngày 31 có bị đếm đôi bao nhiêu? | Thẻ GA4 config trùng (v22) chưa được gỡ nên chưa có mốc so sánh sạch | Sau khi gỡ thẻ #2, so số phiên 14 ngày trước/sau để hiệu chỉnh lại toàn bộ báo cáo phiên từ N31 |
| 9 | Chất lượng traffic PMax đến từ placement nào? | `05` ghi "Chưa thiết lập danh sách loại trừ vị trí đặt", bộ đề không có báo cáo placement | Báo cáo Placement của PMax (Insights → Content) để biết bao nhiêu chi phí vào app/game rác |
| 10 | Clarity có bỏ sót gì trong 4 ngày đầu? | Mã theo dõi chỉ gắn **từ ngày 5** (GTM v19), lấy mẫu ~92% | Không thu hồi được. Mọi ước tính lead mất ở B7 vì thế là **cận dưới**, không phải cận trên |

---

*Báo cáo kết thúc. Mọi con số truy ngược được về `answers/agent-2-calc.py` (chạy: `python3 agent-2-calc.py`).*
