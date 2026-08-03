# BÁO CÁO TIẾP QUẢN TÀI KHOẢN GOOGLE ADS — VINHOMES HÓC MÔN
**Vai trò:** Performance Marketing Lead, An Phát Land · **Kỳ dữ liệu:** 02/03/2026 – 30/05/2026 (90 ngày)
**Người làm:** Thí sinh 5 · **Script tính:** `answers/agent-5-calc.py` (chạy `python3 agent-5-calc.py`, có `assert` self-check khớp sheet 02/03/10)

> **Quy ước trích nguồn:** `[S02]` = sheet 02_DU_LIEU_NGAY (= file CSV chính), `[S03]`…`[S12]` tương ứng các sheet. Mọi số trong báo cáo đều in ra từ script; số nào là **ước tính của tôi** đều được ghi rõ `[ƯỚC TÍNH]` kèm giả định.

---

## SỐ NỀN — chốt trước khi phân tích

| Chỉ số toàn kỳ | Giá trị | Nguồn |
|---|---|---|
| Chi phí | 1.803.537.000 ₫ | [S02] cột `Chi_phi`, 486 dòng (90 ngày × 6 CD, YouTube 0đ GĐ1) |
| Hiển thị / Nhấp chuột | 28.286.633 / 180.835 | [S02] |
| Chuyển đổi Ads | 3.820 | [S02] `ChuyenDoi_Ads` |
| Lead CRM (khử trùng) | 2.557 | [S02] `Lead_CRM` |
| SQL | 651 | [S02] `Lead_SQL` |
| Đi xem nhà / Booking / Đặt cọc | 206 / 59 / **18** | [S02] |
| Doanh thu hoa hồng | 3.130.000.000 ₫ | [S02] `DoanhThu_HoaHong` |
| **ROAS toàn kỳ** | **1,74x** (KPI mới ≥3,0x) | tính |
| **CP/cọc thực tế** | **100.196.500 ₫** (trần ROAS 3x = 60.333.333 ₫) | tính |

Toàn bộ khớp 100% với sheet [S03] dòng "TỔNG 90 NGÀY" — dữ liệu không có lỗi tổng.

---

# PHẦN A — CHẨN ĐOÁN (15 vấn đề, xếp theo tác động tài chính giảm dần)

Trong đó **6 vấn đề thuộc nhóm đo lường/kỹ thuật** (A4, A8, A11, A12, A13, A14) — vượt yêu cầu tối thiểu 3.

---

### A1. Tốc độ phản hồi lead — thất thoát lớn nhất toàn hệ thống, nằm NGOÀI Google Ads
**Mức độ: CAO — ước bỏ lỡ ≈ 2.376.000.000 ₫ doanh thu (13,1 cọc)**

**Phát hiện.** 47% lead được gọi lại sau 2 giờ hoặc muộn hơn. Tỷ lệ đặt cọc rơi từ 1,82% (gọi <5 phút) xuống 0,04% (gọi sau 12h) — chênh **45 lần**.

| Thời gian gọi lại | Số lead | % | Tỷ lệ liên hệ được | Tỷ lệ đặt cọc | Cọc kỳ vọng |
|---|---|---|---|---|---|
| <5 phút | 281 | 11% | 87% | 1,82% | 5,11 |
| 5–30 phút | 485 | 19% | 74% | 1,21% | 5,87 |
| 30ph–2h | 588 | 23% | 58% | 0,58% | 3,41 |
| 2–12h | 536 | 21% | 41% | 0,21% | 1,13 |
| >12h/hôm sau | 664 | 26% | 22% | 0,04% | 0,27 |
| **Tổng** | **2.554** | 100% | — | — | **15,8** |

**Bằng chứng số.** [S08] mục A, toàn kỳ 90 ngày. Cọc kỳ vọng theo phân bố hiện tại = **15,8** (thực tế ghi nhận 18 cọc [S02] — sai lệch 2,2 do làm tròn %, sheet 08A cộng 2.554/2.557 lead). Nếu 100% lead được gọi <5 phút → 46,5 cọc. Kịch bản thực tế hơn (đưa 1.685 lead đang >30 phút về nhóm 5–30 phút, giữ nguyên nhóm 30ph–2h): **28,9 cọc → +13,1 cọc = 2.376.312.800 ₫** `[ƯỚC TÍNH — giả định tỷ lệ cọc của từng nhóm giữ nguyên khi đổi tốc độ, tức tốc độ là nguyên nhân chứ không phải hệ quả của chất lượng lead]`.

Thêm: **275 lead bị bỏ sót hoàn toàn** (118 GĐ1 + 96 GĐ2 + 61 GĐ3, [S08] mục B) = 275 × CPL CRM 705.333 ₫ = **193.966.631 ₫ đã trả tiền mà không ai gọi**, tương đương 1,94 cọc = 350.391.083 ₫ `[ƯỚC TÍNH theo tỷ lệ lead→cọc 0,704%]`.

**Vì sao đây là việc của Marketing Lead:** năng lực sale là **trần cứng** của kế hoạch ngân sách (mục C3). Đổ thêm tiền vào Ads mà không sửa SLA phản hồi = mua thêm lead để bỏ sót.

---

### A2. Chiến dịch Brand bị bóp ngân sách — đang bỏ lại tiền trên bàn ở chính kênh sinh lời nhất
**Mức độ: CAO — bỏ lỡ 876.089.980 – 1.752.179.960 ₫ doanh thu**

**Phát hiện.** Brand chỉ được cấp **14,4% ngân sách** nhưng tạo **72% số cọc** và **73% doanh thu**, ROAS **8,76x** — trong khi Impression Share chỉ 53,4% và **mất 39,7% IS do hết ngân sách**.

| Chỉ số Brand | GĐ1 | GĐ2 | GĐ3 | Toàn kỳ |
|---|---|---|---|---|
| Chi phí (₫) | 57.619.000 | 72.302.000 | 130.298.000 | 260.219.000 (14,4% TK) |
| Impression Share | 54,2% | 51,0% | 54,4% | **53,4%** |
| Mất IS do ngân sách | 39,1% | 41,9% | 38,7% | **39,7%** |
| Mất IS do thứ hạng | — | — | — | 6,9% |
| Đặt cọc | 2 | 3 | 8 | **13/18** |
| ROAS | 5,73x | 7,19x | 10,97x | **8,76x** |

**Bằng chứng số.** [S02] cột `Impr_Share`, `Mat_IS_NganSach` (bình quân trọng số theo hiển thị), lọc `Chien_dich = SEA_Brand_Vinhomes_HocMon`. Benchmark [S09]: IS thương hiệu <60% = **báo động**; mất IS do ngân sách >20% = "tiền đang bỏ lại trên bàn" — ta đang ở 39,7%, gấp đôi ngưỡng báo động.

Ngoại suy tuyến tính: hiển thị bị mất do ngân sách ≈ 163.764 × 39,7% / 53,4% = **121.948 hiển thị** → × CTR 11,63% = 14.182 nhấp → × tỷ lệ lead/nhấp 4,50% = 638 lead → × tỷ lệ lead→cọc của Brand 1,52% = **9,7 cọc = 1.752.179.960 ₫**, đổi lại chi phí thêm ≈ 193.774.125 ₫ (CPC Brand 13.663 ₫).
`[ƯỚC TÍNH — tuyến tính là CẬN TRÊN. Kịch bản thận trọng (chỉ thu hồi 50% do tồn kho tìm kiếm thương hiệu có hạn + CPC đấu giá tăng ~20%): 4,8 cọc = 876.089.980 ₫, chi phí thêm 116.264.475 ₫ → vẫn lãi gộp ~7,5x.]`

**Dữ liệu còn thiếu:** không có Auction Insights nên không biết 6,9% mất IS do thứ hạng là do đối thủ đấu giá hay do Quality Score. Cần xin báo cáo Auction Insights 90 ngày cho campaign Brand.

---

### A3. PMax đốt 475.376.000 ₫ (26,4% ngân sách) đổi lấy **0 cọc**
**Mức độ: CAO — lãng phí trực tiếp 475.376.000 ₫**

| PMAX_VinhomesHM_Lead | Giá trị | Đối chiếu benchmark [S09] |
|---|---|---|
| Chi phí | 475.376.000 ₫ (26,4% TK) | — |
| Chuyển đổi Ads | 1.775 | — |
| **CPL Ads** | **267.817 ₫ — THẤP NHẤT tài khoản** | "tốt" (<500k) |
| Lead CRM | 829 | — |
| SQL | 61 → **SQL/Lead 7,4%** | **<12% = báo động** |
| CP/SQL | **7.793.049 ₫** | **>5tr = báo động** |
| Đặt cọc / Doanh thu | **0 / 0 ₫** | ROAS 0,00x |
| Chênh Ads/CRM | **2,14x** | **>1,8x = báo động** |

**Bằng chứng số hội tụ từ 3 nguồn độc lập:**
- [S10-B] 39.701 nhấp → 28.585 phiên (**hao hụt 28,0%** — với PMax là bất thường, ghi chú sheet nói rõ), tỷ lệ tương tác **8,7%** (Brand 62,4%), thời gian tương tác TB **11 giây**, **1,09 trang/phiên**, tỷ lệ cuộn 90% = **4%**.
- [S11-B] 26.298 phiên ghi hình: **74,3% thoát nhanh dưới 3 giây**, thời lượng phiên trung vị **3 giây**. Ghi chú Clarity: "Bất thường — xem lại vị trí đặt quảng cáo".
- [S08-C] mẫu kiểm 160 lead PMax: **trùng SĐT 31%, SĐT sai/không liên lạc được 24%, sai phân khúc 34%, chỉ 7% dùng được**. → Lead dùng được ≈ 829 × 7% = **58 lead**, chi phí/lead dùng được = **8.191.901 ₫**.

**Nguyên nhân gốc (không phải lỗi PMax):** PMax đang được tối ưu theo cột `Chuyển đổi` chứa 973 sự kiện rác (A4). [S12-C] ghi thẳng: "Máy học tối ưu theo tín hiệu rác — **nguyên nhân gốc của toàn bộ vấn đề PMax**". Cộng thêm [S05]: PMax **chưa thiết lập loại trừ vị trí đặt**, **chưa bật brand exclusion**, **không đặt CPA mục tiêu** → tự do mua lưu lượng rẻ nhất trên mạng nội dung.

---

### A4. 34,7% cột "Chuyển đổi" không phải khách hàng tiềm năng — sai lệch đo lường là gốc rễ mọi vấn đề khác
**Mức độ: CAO — chi phí phân bổ cho tín hiệu rác 459.382.592 ₫ (Nhóm ĐO LƯỜNG)**

**Phát hiện.** Tài khoản đang khai **4 hành động** vào cột `Chuyển đổi`, trong đó 2 hành động **không phải lead** và 1 hành động **đếm trùng**.

| Sự kiện | Số lượt | Là khách tiềm năng? | Nguồn |
|---|---|---|---|
| generate_lead | 1.715 | Có | [S10-A/E] |
| click_to_call (lượt) | 1.132 | Có nhưng **đếm trùng** (779 người duy nhất → thừa **353**) | [S10-A] |
| view_price_page | 612 | **KHÔNG** | [S10-E] |
| engaged_30s | 361 | **KHÔNG** | [S10-E] |
| **Tổng = cột Chuyển đổi** | **3.820** | — | khớp [S02] |

**Bằng chứng số.** 973 sự kiện rác (612+361) = **25,5%** cột Chuyển đổi; 353 lượt trùng = **9,2%**; cộng lại **34,7%**. Chi phí phân bổ theo tỷ trọng chuyển đổi = 1.803.537.000 × 973/3.820 = **459.382.592 ₫** đang "mua" tín hiệu rác `[ƯỚC TÍNH theo phân bổ tỷ trọng — không phải chi phí trực tiếp đo được]`.

Vi phạm luật đo lường của chính hệ nội bộ (`tracking/README.md` luật #2): *"phone_click/zalo_click = Secondary vĩnh viễn"* và *"Khai 'form submit' là conversion → Google tìm thêm người-điền-form-rẻ-nhất = SĐT rác"*. Ở đây còn tệ hơn: khai cả **xem trang** và **ở lại 30 giây** là conversion chính.

**Hệ quả dây chuyền:** Smart Bidding của PMax (Tối đa hóa chuyển đổi, không CPA mục tiêu — [S05]) học rằng "phiên 3 giây có view_price_page" là thành công → mua đúng loại lưu lượng đó → 74,3% thoát <3 giây [S11-B]. **A3 là hệ quả, A4 là nguyên nhân.**

---

### A5. 419.729.000 ₫ chi cho cụm từ tìm kiếm **không ra một SQL nào**
**Mức độ: CAO — lãng phí 419.729.000 ₫ (23,3% ngân sách)**

**Phát hiện.** 17/32 cụm từ trong báo cáo có SQL = 0. Đối sánh rộng chiếm **71% chi phí Search** trong khi đối sánh chính xác chỉ 9% [S05].

| Cụm từ (SQL=0) | Đối sánh | Chi phí (₫) | Nhấp | Lead | SQL |
|---|---|---|---|---|---|
| vạn phúc city giá bán | Cụm từ | 40.652.000 | 704 | 7 | 0 |
| the global city | Cụm từ | 38.884.000 | 640 | 6 | 0 |
| giá đất hóc môn 2026 | Rộng | 33.900.000 | 1.025 | 29 | 0 |
| izumi city đồng nai | Rộng | 33.582.000 | 576 | 6 | 0 |
| bản đồ quy hoạch hóc môn | Rộng | 27.120.000 | 820 | 6 | 0 |
| thuê nhà nguyên căn hóc môn | Rộng | 27.120.000 | 820 | 6 | 0 |
| bán đất thổ cư hóc môn 100 triệu | Rộng | 27.120.000 | 820 | 6 | 0 |
| aqua city có nên mua | Rộng | 24.744.000 | 480 | 5 | 0 |
| khu đô thị sinh thái tây bắc củ chi | Rộng | 21.210.000 | 416 | 4 | 0 |
| nhà trọ hóc môn giá rẻ / cho thuê kho xưởng / việc làm BĐS | Rộng | 61.020.000 | 1.845 | 12 | 0 |
| …và 6 cụm khác | | | | | |
| **TỔNG 17 cụm** | | **419.729.000** | | | **0** |

**Bằng chứng số.** [S04] toàn bộ 90 ngày, cột `Lead chất lượng (SQL)` = 0. Trong đó **10 cụm sai ý định rõ ràng** (tuyển dụng, học phí, thuê nhà, nhà trọ, kho xưởng, việc làm, lừa đảo, quy hoạch, chung cư mini, "100 triệu") = **209.082.000 ₫ = 11,6% ngân sách** — đây là phần **chặn được ngay bằng từ khóa phủ định**, không cần bàn cãi.

Riêng "bán đất thổ cư hóc môn **100 triệu**" và "nhà trọ hóc môn **giá rẻ**" đang chạy cho sản phẩm 2,9–11,5 tỷ — lệch phân khúc hoàn toàn, khớp với [S08-C] "sai phân khúc (ngân sách <2 tỷ)" 18–34% tùy campaign.

**Nguyên nhân cấu hình:** [S05] chỉ có **12 từ khóa phủ định** trong toàn tài khoản, **không dùng danh sách phủ định chia sẻ**, 31 từ khóa/nhóm quảng cáo (quá loãng để viết ad copy khớp thông điệp), Điểm chất lượng bình quân **5,2/10**, trải nghiệm trang đích "Dưới trung bình".

---

### A6. 364.314.474 ₫ chi cho khu vực địa lý **không thể bán được hàng**
**Mức độ: CAO — lãng phí 364.314.474 ₫ (20,2% ngân sách)**

| Khu vực | Chi phí (₫) | SQL | Cọc | CP/SQL (₫) |
|---|---|---|---|---|
| Hà Nội | 155.104.182 | 20 | 0 | 7.755.209 |
| Đà Nẵng | 86.569.776 | 7 | 0 | **12.367.111** |
| Cần Thơ & ĐBSCL | 93.783.924 | 12 | 0 | 7.815.327 |
| Ngoài Việt Nam | 28.856.592 | 7 | 0 | 4.122.370 |
| **Cộng 4 nhóm** | **364.314.474 (20,2%)** | **46** | **0** | **7.919.880** |
| *Đối chiếu:* TP.HCM – Quận 12 | 201.996.144 | 97 | 4 | **2.082.434** |
| *Đối chiếu:* TP.HCM – Hóc Môn | 176.746.626 | 92 | 3 | **1.921.159** |

**Bằng chứng số.** [S06] toàn kỳ. TP.HCM chiếm 59,7% chi phí nhưng tạo **17/18 cọc**. CP/SQL Đà Nẵng cao gấp **6,4 lần** Hóc Môn. Nguyên nhân cấu hình: [S05] nhắm mục tiêu **"Việt Nam (toàn quốc)"** cho cả 6 chiến dịch, tùy chọn vị trí để mặc định **"Hiện diện HOẶC quan tâm"** (chưa từng chỉnh), **không có loại trừ vị trí** → quảng cáo hiển thị cho người ở Hà Nội chỉ vì họ "quan tâm đến TP.HCM".

---

### A7. Lịch chạy quảng cáo không khớp năng lực sale — 26,8% ngân sách rơi vào khung giờ không ai nghe máy
**Mức độ: CAO — 483.347.916 ₫ khung giờ yếu + 503.810.000 ₫ cuối tuần**

**A7a — Theo khung giờ** [S07-A]:

| Khung giờ | % chi phí | Chi phí (₫) | SQL | Cọc | CP/SQL (₫) | **Tỷ lệ gọi lại <30 phút** |
|---|---|---|---|---|---|---|
| 09:00–12:00 | 16,8% | 302.994.216 | 121 | 4 | 2.504.084 | **93%** |
| 14:00–17:00 | 17,1% | 308.404.827 | 117 | 4 | 2.635.939 | **91%** |
| 06:00–09:00 | 9,5% | 171.336.015 | 57 | 2 | 3.005.895 | 81% |
| 17:00–20:00 | 18,6% | 335.457.882 | 124 | 3 | 2.705.306 | 64% |
| **20:00–23:00** | **18,7%** | **337.261.419** | 112 | 3 | 3.011.263 | **21%** |
| **23:00–24:00** | 4,0% | 72.141.480 | 22 | **0** | 3.279.158 | **12%** |
| **00:00–06:00** | 4,1% | 73.945.017 | 18 | **0** | 4.108.057 | **34%** |

Khung 20:00–06:00 = **483.347.916 ₫ (26,8% ngân sách)** → chỉ **3/18 cọc**, CP/SQL cao hơn khung 09–12h từ 20% đến 64%.

**A7b — Theo ngày trong tuần** [S07-C]: T7+CN chi **503.810.000 ₫ (27,9%)** với chỉ **2/8 sale trực** → chỉ **4/18 cọc**. CP/SQL Thứ 7 = 3.020.851 ₫ vs Thứ 2 = 2.151.142 ₫ (**+40%**). Lượng lead cuối tuần thực nhận (364+358)/26 ngày-cuối-tuần ≈ **27,8 lead/ngày**, trong khi trần xử lý cuối tuần chỉ **2 sale × 12 = 24 lead/ngày** → **quá tải cấu trúc**, khớp với 275 lead bị bỏ sót ở A1.

**A7c — Theo thiết bị** [S07-B]: Di động **78,1% chi phí (1.408.562.397 ₫)**, CVR 2,03%, CP/SQL 3.042.251 ₫ · Máy tính 16,7% chi phí, CVR **4,02%**, CP/SQL **1.847.796 ₫**. Máy tính rẻ hơn **65%** trên mỗi SQL nhưng chỉ nhận 16,7% ngân sách. Không có điều chỉnh giá thầu theo thiết bị ([S05] "Lịch quảng cáo 24/7, không điều chỉnh giá thầu theo giờ").

---

### A8. Lỗi kỹ thuật trên trang đích **chưa được sửa** đang chặn 370–480 lead
**Mức độ: CAO — 260.973.285 – 338.559.937 ₫ CPL + 471.435.276 – 611.591.709 ₫ doanh thu bỏ lỡ (Nhóm ĐO LƯỜNG/KỸ THUẬT)**

| # | Điểm ma sát (CHƯA SỬA) | Vị trí | Phiên ảnh hưởng | Lead mất |
|---|---|---|---|---|
| 4 | **Lỗi JS `TypeError e.setDate is not a function`** (bộ chọn ngày hẹn xem nhà), Safari iOS 17.x — form **không gửi được, không báo lỗi cho khách** | Form, nút gửi | 4.196 | 280–340 |
| 5 | Nút "Đăng ký nhận bảng giá" bị **khung chat che** trên màn hình <380px | Cuối trang | 2.741 | 60–90 |
| 6 | Số hotline `tel:` — người dùng máy tính bấm không phản hồi, 1.847 nhấp chết | Đầu trang | 1.204 | 30–50 |
| | **Tổng** | | **8.141** | **370–480** |

**Bằng chứng số.** [S11-C] cột "Trạng thái = CHƯA SỬA". Xác nhận chéo [S11-A]: tỷ lệ phiên có lỗi JavaScript trên di động **9,3% (v1) → 8,9% (v2)** — **không giảm** sau khi lên trang đích mới, chứng tỏ lỗi #4 sống sót qua cả hai phiên bản. Lỗi #4 đánh vào Safari iOS trong khi di động chiếm 78,1% chi phí [S07-B] → đây là lỗ thủng lớn nhất.

Quy tiền, xem chi tiết ở **B7**.

---

### A9. Chiến dịch Competitor: 176.746.000 ₫ → 3 SQL, 0 cọc
**Mức độ: CAO — lãng phí 176.746.000 ₫ (9,8% ngân sách)**

| SEA_Competitor_DoiThu | Giá trị | Benchmark [S09] |
|---|---|---|
| Chi phí | 176.746.000 ₫ | — |
| Nhấp / CPC | 3.204 / **55.164 ₫** | >60.000 = báo động (sát ngưỡng) |
| CTR | 2,39% | <2% báo động (chỉ nhỉnh hơn) |
| Lead CRM / SQL / Cọc | 32 / **3** / **0** | — |
| CPL CRM | **5.523.312 ₫** | >1.500.000 = **báo động** |
| CP/SQL | **58.915.333 ₫** | >5tr = **báo động (gấp 11,8 lần)** |

**Bằng chứng số.** [S02] lọc campaign. [S04]: cả **6 cụm từ đối thủ** (vạn phúc city, the global city, izumi city, aqua city, khu đô thị sinh thái tây bắc củ chi, so sánh dự án) đều có **SQL = 0** trên tổng 176.747.000 ₫. [S08-C] mẫu 40 lead: **26% là môi giới/đối thủ**, chỉ 26% dùng được — tỷ lệ dùng được thấp nhì tài khoản.
**Kết luận: dừng ngay, không cần thử nghiệm thêm.** 90 ngày và 176 triệu là quá đủ dữ liệu để kết luận.

---

### A10. Trang đích v1 chạy tới ngày 57 mới thay — mất 374 lead
**Mức độ: TRUNG BÌNH-CAO — 476.011.404 ₫ doanh thu bỏ lỡ**

| Trang đích | Khoảng ngày | Phiên | form_start | generate_lead | **Tỷ lệ hoàn tất form** | Tỷ lệ tương tác | LCP |
|---|---|---|---|---|---|---|---|
| /dang-ky-nhan-bang-gia (v1) | N1–57 | 52.410 | 4.912 | 1.002 | **20,4%** | 34,2% | **4,8s** |
| /nhan-bang-gia-2026 (v2) | N58–90 | 42.938 | 2.546 | 713 | **28,0%** | 58,7% | **1,9s** |
| Chênh | | | | | **+37,3%** | +71,6% | −60% |

**Bằng chứng số.** [S10-C]. LCP 4,8s vượt ngưỡng báo động [S09] (>4s). Nếu v2 chạy từ ngày 1, trên cùng 4.912 `form_start` của v1 sẽ có thêm 4.912 × (28,0%−20,4%) = **374 lead** → 95 SQL → **2,63 cọc = 476.011.404 ₫** `[ƯỚC TÍNH — giả định lưu lượng và tỷ lệ SQL/lead không đổi]`.

Nặng nhất là di động: v1 tỷ lệ hoàn tất form **16,1%** vs máy tính 34,8% [S10-C chi tiết theo thiết bị] — trong khi di động ăn 78,1% ngân sách.

---

### A11. GTM v23 làm gãy đo lường 3 ngày — 63 lead vĩnh viễn không có trong Ads/GA4, và không có cảnh báo nào
**Mức độ: TRUNG BÌNH-CAO — 44.435.992 ₫ chi phí không được ghi nhận + thiệt hại vô hình cho Smart Bidding (Nhóm ĐO LƯỜNG)**

**Phát hiện.** Ngày 44 (14/04) lúc 09:12, dev@ xuất bản GTM v23 đổi class `.form-dk-v1` → `.form-register`. Điều kiện kích hoạt `generate_lead` **ngừng khớp**. Sự cố kéo dài đến ngày 47 (v24, 14:38) mới sửa.

**Bằng chứng số — kiểm chứng ngược trên [S02]:**

| Ngày | Chuyển đổi Ads (toàn TK) | Lead CRM (toàn TK) | Chi phí (₫) |
|---|---|---|---|
| N41 (11/04) | 33 | 19 | 19.577.000 |
| N42 (12/04) | 37 | 24 | 19.517.000 |
| N43 (13/04) | 43 | 30 | 19.744.000 |
| **N44 (14/04)** | **0** | **17** | **20.249.000** |
| **N45 (15/04)** | **0** | **15** | **19.699.000** |
| **N46 (16/04)** | **0** | **31** | **19.580.000** |
| N47 (17/04) | 33 | 18 | 19.912.000 |
| N48 (18/04) | 36 | 26 | 19.627.000 |
| N49 (19/04) | 55 | 37 | 19.766.000 |
| **Cộng N44–46** | **0** | **63** | **59.528.000** |

Trung bình 6 ngày kề cận (N41–43, N47–49): **39,5 chuyển đổi/ngày** → 3 ngày đáng lẽ ~118 chuyển đổi, thực tế **0**. 63 lead thật vẫn về CRM. Chi phí 3 ngày đó = **59.528.000 ₫** chạy trong tình trạng bidding mù.

**Ba lỗi hệ thống gộp lại** [S12-A]:
1. Thẻ #3 dùng **điều kiện kích hoạt dựa trên class CSS** — "rất dễ vỡ khi dev đổi giao diện".
2. Mục #18: **KHÔNG CÓ cảnh báo khi chuyển đổi = 0** → "Nguyên nhân khiến sự cố N44–46 mất 3 ngày mới bị phát hiện".
3. Không có quy trình review GTM trước khi publish (dev@ tự publish 09:12 sáng ngày làm việc).

**Thiệt hại thứ cấp không đo được nhưng có thật:** theo `playbook/monitoring.md` §2.1 (dẫn Google *About data exclusions*), tracking gãy mà không khai `Data exclusion` → Smart Bidding học rằng lưu lượng 3 ngày đó không convert và **né loại lưu lượng tốt đó trong nhiều tuần sau**. Không có bằng chứng data exclusion nào được tạo. **Cần thêm dữ liệu:** lịch sử thay đổi cấp campaign trong Google Ads để xác nhận.

---

### A12. Không có GCLID trong CRM → không thể nhập chuyển đổi ngoại tuyến → không bao giờ tối ưu được theo chất lượng lead
**Mức độ: TRUNG BÌNH-CAO — chặn toàn bộ lộ trình tối ưu (Nhóm ĐO LƯỜNG)**

| Hạng mục [S12-A/C] & [S05] | Trạng thái | Tác động |
|---|---|---|
| Biến ẩn lưu GCLID vào form (#15) | **CHƯA CÀI** | "Không có GCLID trong CRM ⇒ **KHÔNG THỂ** nhập chuyển đổi ngoại tuyến" |
| Nhập chuyển đổi ngoại tuyến từ CRM | **CHƯA triển khai** | Bidding không bao giờ biết lead nào ra cọc |
| Enhanced Conversions (#14) | **CHƯA CÀI** | "Mất **10–20%** khả năng khớp chuyển đổi" |
| Consent Mode v2 (#16) | **CHƯA CẤU HÌNH** | Rủi ro pháp lý + mất mô hình hóa |
| Vùng chứa phía máy chủ (#17) | **KHÔNG CÓ** | Phụ thuộc hoàn toàn trình duyệt/ad blocker |
| Gắn ID phiên Clarity vào CRM (#10) | **CHƯA** | Không xem lại được hành trình lead đã cọc |

**Vì sao đây là vấn đề tiền, không phải vấn đề kỹ thuật:** tài khoản có **651 SQL và 18 cọc** [S02] — đó là tín hiệu chất lượng quý nhất, và nó **đang nằm chết trong CRM**. Chừng nào chưa đẩy ngược vào Google Ads, Smart Bidding chỉ có thể tối ưu theo lead thô (mà 34,7% trong đó còn là rác — A4). Đây là điều kiện tiên quyết để chuyển sang tCPA/tROAS.

**Định lượng gián tiếp:** chỉ riêng Enhanced Conversions mất 10–20% khớp × 2.494 lead đo được = **249–499 lead** không được quy về đúng nguồn.

---

### A13. Mô hình phân bổ nhấp cuối đang bóp méo quyết định ngân sách
**Mức độ: TRUNG BÌNH (Nhóm ĐO LƯỜNG)**

| Kênh | Nhấp cuối (đang dùng) | Dựa trên dữ liệu | Chênh | % thay đổi |
|---|---|---|---|---|
| SEA_Brand | 592 | 401 | **−191** | **−32,3%** |
| SEA_Generic | 418 | 402 | −16 | −3,8% |
| SEA_Competitor | 20 | 24 | +4 | +20,0% |
| PMAX | 510 | 466 | −44 | −8,6% |
| GDN_Remarketing | 132 | 186 | **+54** | **+40,9%** |
| **YT_Video** | 43 | **165** | **+122** | **+283,7%** |
| Trực tiếp/Tự nhiên | 0 | 71 | +71 | — |

**Bằng chứng số.** [S10-D], tổng 1.715 `generate_lead`, ghi chú: "Mô hình nhấp cuối là mô hình **đang được dùng để đánh giá và phân bổ ngân sách** trong suốt 90 ngày".

**Đọc đúng:** YouTube và GDN đang tạo ảnh hưởng đầu phễu bị nhấp cuối phủ nhận (YT thực tế 165 lead chứ không phải 43). Brand bị **thổi phồng 32,3%** vì nó là điểm chạm cuối cùng của hành trình mà kênh khác đã khởi xướng. **Lưu ý quan trọng cho D1:** ngay cả sau khi hạ 32,3%, Brand vẫn giữ **401/1.715 lead (23,4%)** — ngang Generic (402) và vẫn là kênh có tỷ lệ ra cọc cao nhất. Attribution làm Brand *bớt* to, không làm Brand *hết* giá trị.

---

### A14. Vùng chứa GTM phình 34 thẻ / 412 KB JS — chính công cụ đo lường đang làm hỏng thứ nó đo
**Mức độ: TRUNG BÌNH (Nhóm ĐO LƯỜNG/KỸ THUẬT)**

**Bằng chứng số [S12].** 34 thẻ · 21 điều kiện kích hoạt · 18 biến · **412 KB JavaScript bên thứ ba** · ước tính **làm chậm LCP thêm ~0,8 giây**. Trong đó:
- Thẻ #2 `GA4 Configuration – Copy of Main` **TRÙNG LẶP** → **page_view bị bắn hai lần từ ngày 31** (v22) → số phiên và tỷ lệ thoát sai lệch từ N31 trở đi. **Cảnh báo đọc số:** mọi so sánh phiên GA4 trước/sau N31 đều không đáng tin.
- Thẻ #13 "Thẻ đối tác sàn F2 (3 thẻ)" — **"Không rõ nguồn gốc — cần rà soát bảo mật"**, thêm ~0,3s LCP (v20, ngày 18).
- Thẻ #12 "Zalo Tracking" — **"Không rõ ai cài, không có mô tả"**.

**Đối chiếu chi phí:** LCP trang v2 là 1,9s [S10-C]; nếu GTM đang cộng 0,8s thì bản thân trang chỉ ~1,1s — tức **42% thời gian tải là do thẻ đo lường và thẻ đối tác**, phần lớn không phục vụ mục tiêu kinh doanh nào của An Phát Land.

---

### A15. Tín hiệu ý định giá trị cao đang bị bỏ rơi hoàn toàn
**Mức độ: THẤP-TRUNG BÌNH (Nhóm ĐO LƯỜNG)**

| Sự kiện | Số lượt | Là khách tiềm năng? | Đang nhập vào Ads? |
|---|---|---|---|
| `zalo_click` | **894** | **"Có — đang bị bỏ sót, không ai đo"** | Không |
| `file_download` (bảng giá PDF) | **1.206** | **"Có tín hiệu ý định — đang bỏ sót"** | Không |
| `form_start` | 7.458 | Không, nhưng hữu ích chẩn đoán | Không (đúng) |

**Bằng chứng số.** [S10-E] + [S12-B] v26 (ngày 71): "Thêm sự kiện zalo_click và file_download — **Có dữ liệu nhưng chưa đánh dấu là sự kiện chính, chưa nhập vào Ads**".

**Nghịch lý cần nói thẳng:** tài khoản đang nhập 973 sự kiện KHÔNG phải lead (view_price_page, engaged_30s) vào cột Chuyển đổi, đồng thời bỏ ngoài 2.100 lượt tín hiệu ý định thật (894 zalo + 1.206 tải bảng giá). Ở thị trường BĐS Việt Nam, Zalo là kênh liên hệ chính (`CLAUDE.md`: "số điện thoại/Zalo là CTA chính"). Đây là sửa gần như miễn phí.

Đồng thời `form_start` = 7.458 nhưng `generate_lead` = 1.715 → **tỷ lệ hoàn tất form toàn kỳ chỉ 23,0%**, tức **5.743 người bắt đầu điền rồi bỏ**. Đây là kho lead lớn nhất chưa khai thác, và nguyên nhân đã được chỉ mặt ở A8.

---

## Bảng tổng hợp tác động tài chính Phần A

| # | Vấn đề | Nhóm | Tiền lãng phí / DT bỏ lỡ (₫) | Mức |
|---|---|---|---|---|
| A1 | Phản hồi lead chậm + 275 lead bỏ sót | Vận hành | **2.570.279.431** (DT bỏ lỡ) | Cao |
| A2 | Brand bị bóp ngân sách (mất 39,7% IS) | Ngân sách | **876.089.980 – 1.752.179.960** (DT bỏ lỡ) | Cao |
| A8 | Lỗi JS/CTA/tel chưa sửa trên LP | **Kỹ thuật** | 260.973.285 chi phí + **471.435.276 – 611.591.709** DT | Cao |
| A3 | PMax 0 cọc | Chiến dịch | **475.376.000** (lãng phí) | Cao |
| A4 | 34,7% chuyển đổi là rác/trùng | **Đo lường** | **459.382.592** (phân bổ) | Cao |
| A5 | 17 cụm từ SQL=0 | Từ khóa | **419.729.000** (lãng phí) | Cao |
| A10 | LP v1 chậm thay 57 ngày | Kỹ thuật | **476.011.404** (DT bỏ lỡ) | TB-Cao |
| A7 | Lịch chạy lệch năng lực sale | Cấu hình | **483.347.916** giờ yếu + 503.810.000 cuối tuần (hiệu suất kém) | Cao |
| A6 | Địa lý ngoài vùng bán | Cấu hình | **364.314.474** (lãng phí) | Cao |
| A9 | Competitor 0 cọc | Chiến dịch | **176.746.000** (lãng phí) | Cao |
| A11 | GTM v23 gãy 3 ngày, không cảnh báo | **Đo lường** | 59.528.000 chi phí mù + 44.435.992 lead mất thẻ | TB-Cao |
| A12 | Không GCLID/ECL/Enhanced Conv | **Đo lường** | Chặn 249–499 lead khớp; chặn toàn bộ lộ trình tCPA | TB-Cao |
| A13 | Attribution nhấp cuối | **Đo lường** | Sai lệch phân bổ (Brand +32,3%, YT −74%) | TB |
| A14 | GTM 34 thẻ / 412 KB / +0,8s LCP | **Kỹ thuật** | Gián tiếp qua CVR; rủi ro bảo mật 3 thẻ lạ | TB |
| A15 | Bỏ 894 zalo_click + 1.206 file_download | **Đo lường** | 2.100 tín hiệu ý định không dùng | Thấp-TB |

> **Cảnh báo không cộng dồn:** các con số trên **chồng lấn nhau** (A4 là nguyên nhân của A3; A5 và A6 giao nhau ở cùng những nhấp chuột; A1 và A8 cùng nói về lead thất thoát). Không được cộng tất cả thành một con số "tổng thiệt hại". Con số an toàn để báo cáo ban giám đốc: **chi phí có thể cắt ngay mà không mất cọc nào = 865.324.000 ₫ (48,0% ngân sách 90 ngày)** — chứng minh ở D4.

---

# PHẦN B — TÍNH TOÁN

Toàn bộ số dưới đây in ra từ `agent-5-calc.py`. Tất cả tổng đều khớp sheet [S03].

## B1. CPL Ads / CPL CRM / CP/SQL / CP/cọc

**Toàn kỳ và từng chiến dịch** (nguồn: [S02], xếp theo chi phí giảm dần):

| Chiến dịch | Chi phí (₫) | CĐ Ads | Lead CRM | SQL | Cọc | CPL Ads (₫) | CPL CRM (₫) | CP/SQL (₫) | CP/cọc (₫) | SQL/Lead | Ads/CRM |
|---|---|---|---|---|---|---|---|---|---|---|---|
| SEA_Generic_NhaPho_CanHo_TayBac | 677.994.000 | 664 | 587 | 191 | 5 | 1.021.075 | 1.155.015 | 3.549.707 | 135.598.800 | 32,5% | 1,13x |
| PMAX_VinhomesHM_Lead | 475.376.000 | 1.775 | 829 | 61 | **0** | **267.817** | 573.433 | **7.793.049** | — | **7,4%** | **2,14x** |
| SEA_Brand_Vinhomes_HocMon | 260.219.000 | 871 | 857 | 352 | **13** | 298.759 | 303.639 | **739.259** | **20.016.846** | **41,1%** | **1,02x** |
| SEA_Competitor_DoiThu | 176.746.000 | 31 | 32 | 3 | **0** | 5.701.484 | 5.523.312 | **58.915.333** | — | 9,4% | 0,97x |
| GDN_Remarketing_Web30d | 130.009.000 | 302 | 193 | 36 | **0** | 430.493 | 673.622 | 3.611.361 | — | 18,7% | 1,56x |
| YT_Video_TVC_MoBan | 83.193.000 | 177 | 59 | 8 | **0** | 470.017 | 1.410.051 | 10.399.125 | — | 13,6% | **3,00x** |
| **TOÀN KỲ** | **1.803.537.000** | **3.820** | **2.557** | **651** | **18** | **472.130** | **705.333** | **2.770.410** | **100.196.500** | **25,5%** | **1,49x** |

**Đối chiếu benchmark [S09]:**

| Chỉ số | Thực tế | Ngưỡng tốt | TB ngành | Báo động | Kết luận |
|---|---|---|---|---|---|
| CPL thô (CRM) toàn kỳ | 705.333 ₫ | <500k | 500k–1,1tr | >1,5tr | Trung bình ngành |
| CP/SQL toàn kỳ | 2.770.410 ₫ | <1,8tr | 1,8–3,5tr | >5tr | Trung bình — nhưng **KPI mới là ≤2,2tr → đang vượt 26%** |
| SQL/lead thô | 25,5% | >30% | 18–30% | <12% | Trung bình ngành |
| Chênh Ads/CRM | 1,49x | 1,0–1,2 | 1,2–1,5 | >1,8 | Sát mép trên TB |

**Đọc số quan trọng:** Brand có CP/SQL **739.259 ₫** — rẻ hơn Generic (3.549.707 ₫) **4,8 lần** và là chiến dịch duy nhất **dưới ngưỡng "tốt" 1,8 triệu** của benchmark. Còn PMax có CPL Ads thấp nhất tài khoản (267.817 ₫) nhưng CP/SQL cao thứ nhì (7.793.049 ₫) — **đây chính là cái bẫy sẽ trả lời D3**.

## B2. ROAS toàn kỳ và từng giai đoạn

| Giai đoạn | Chi phí (₫) | Doanh thu HH (₫) | Cọc | **ROAS** | CP/cọc (₫) |
|---|---|---|---|---|---|
| GĐ1 (N1–30) | 545.696.000 | 330.000.000 | 2 | **0,60x** | 272.848.000 |
| GĐ2 (N31–60) | 604.392.000 | 850.000.000 | 5 | **1,41x** | 120.878.400 |
| GĐ3 (N61–90) | 653.449.000 | 1.950.000.000 | 11 | **2,98x** | 59.404.455 |
| **TOÀN KỲ** | **1.803.537.000** | **3.130.000.000** | **18** | **1,74x** | **100.196.500** |

**ROAS theo chiến dịch:**

| Chiến dịch | Chi phí (₫) | Doanh thu (₫) | ROAS |
|---|---|---|---|
| **SEA_Brand_Vinhomes_HocMon** | 260.219.000 | 2.280.000.000 | **8,76x** |
| SEA_Generic_NhaPho_CanHo_TayBac | 677.994.000 | 850.000.000 | 1,25x |
| PMAX / Competitor / GDN / YT | 865.324.000 | **0** | **0,00x** |

**ROAS Brand × Generic theo giai đoạn** (đường xu hướng quan trọng nhất trong bộ dữ liệu):

| | GĐ1 | GĐ2 | GĐ3 |
|---|---|---|---|
| Brand | 5,73x (2 cọc) | 7,19x (3 cọc) | **10,97x (8 cọc)** |
| Generic | 0,00x (0 cọc) | 1,51x (2 cọc) | 2,01x (3 cọc) |

**Ba kết luận từ bảng này:**
1. Quỹ đạo đang đi đúng hướng: ROAS 0,60 → 1,41 → **2,98x**. GĐ3 gần chạm KPI 3,0x mà **chưa sửa gì về đo lường**.
2. GĐ3 tốt lên do 3 nguyên nhân trùng thời điểm: trang đích v2 từ N58 [S10-C], SLA sale 15 phút (thời gian phản hồi trung vị 214 → 47 phút, [S08-B]), và sự kiện mở bán. **Không được quy toàn bộ cho quảng cáo.**
3. 48,0% ngân sách (865.324.000 ₫) đang chạy ở ROAS **0,00x**.

## B3. Tỷ lệ chuyển đổi từng bước phễu

| Phễu | Lead | → SQL | → Đi xem | → Booking | → Cọc | Lead→Cọc | SQL→Cọc |
|---|---|---|---|---|---|---|---|
| **TOÀN KỲ** | 2.557 | 651 (**25,5%**) | 206 (**31,6%**) | 59 (**28,6%**) | 18 (**30,5%**) | **0,70%** | **2,76%** |
| GĐ1 | 734 | 151 (20,6%) | 38 (25,2%) | 10 (26,3%) | 2 (20,0%) | 0,27% | 1,32% |
| GĐ2 | 761 | 184 (24,2%) | 56 (30,4%) | 16 (28,6%) | 5 (31,2%) | 0,66% | 2,72% |
| **GĐ3** | 1.062 | 316 (**29,8%**) | 112 (**35,4%**) | 33 (29,5%) | 11 (**33,3%**) | **1,04%** | **3,48%** |

**Theo chiến dịch:**

| Chiến dịch | Lead | SQL/Lead | Xem/SQL | Booking/Xem | Cọc/Booking | Lead→Cọc |
|---|---|---|---|---|---|---|
| SEA_Brand | 857 | **41,1%** | 35,5% | 29,6% | 35,1% | **1,52%** |
| SEA_Generic | 587 | 32,5% | 32,5% | 29,0% | 27,8% | 0,85% |
| GDN_Remarketing | 193 | 18,7% | 22,2% | 25,0% | 0% | 0% |
| YT_Video | 59 | 13,6% | 12,5% | 0% | — | 0% |
| SEA_Competitor | 32 | **9,4%** | 0% | — | — | 0% |
| PMAX | 829 | **7,4%** | 16,4% | 20,0% | 0% | 0% |

**Đối chiếu benchmark [S09]:**
- SQL/lead toàn kỳ 25,5% = TB ngành (18–30%). GĐ3 29,8% sắp chạm "tốt" (>30%). PMax 7,4% và Competitor 9,4% **dưới ngưỡng báo động 12%** → "dấu hiệu nhắm sai tệp" đúng như ghi chú sheet.
- SQL→đi xem 31,6% = TB ngành (22–35%). GĐ3 35,4% chạm mép "tốt".
- Đi xem→cọc: **18/206 = 8,7%** = TB ngành (7–12%). Bước này KHÔNG phải nút thắt.

**Nút thắt thật nằm ở đâu:** nếu tính từ nhấp chuột, phễu là 180.835 nhấp → 95.348 phiên GA4 (**hao hụt 47,3%**, [S10-B]) → 7.458 form_start → 1.715 generate_lead (**hoàn tất form chỉ 23,0%**) → 2.557 lead CRM → 651 SQL. **Hai chỗ rò rỉ lớn nhất là hao hụt nhấp→phiên (47,3%) và bỏ dở form (77,0%)** — cả hai đều là vấn đề kỹ thuật/trang đích, không phải vấn đề giá thầu.

## B4. Ngược từ KPI: cần bao nhiêu SQL, bao nhiêu lead thô, CP/SQL tối đa

Tôi trình bày **3 kịch bản giả định** thay vì một con số, vì chọn tỷ lệ nào là quyết định quan trọng nhất của bài toán này.

| Kịch bản (giả định tỷ lệ) | SQL→Cọc | Lead→SQL | **SQL cần** | **Lead thô cần** | Lead/ngày | CP/SQL tối đa (₫) | CPL tối đa (₫) |
|---|---|---|---|---|---|---|---|
| **A. Tỷ lệ toàn kỳ 90 ngày** | 2,76% | 25,5% | **1.157** | **4.546** | 50,5 | 1.814.516 | 461.967 |
| **B. Tỷ lệ GĐ3 (khuyến nghị dùng)** | 3,48% | 29,8% | **919** | **3.089** | 34,3 | **2.284.415** | 679.732 |
| **C. Chỉ 2 CD Search có cọc** | 3,31% | 37,6% | **965** | **2.567** | 28,5 | 2.175.414 | 818.040 |

**Tôi chọn kịch bản B. Lý do:**
1. GĐ3 là 30 ngày gần nhất và là **trạng thái tài khoản sẽ kế thừa**: trang đích v2 đã chạy từ N58, SLA sale 15 phút đã có [S08-B]. Dùng tỷ lệ toàn kỳ (A) là kéo ngược về thời trang đích LCP 4,8s và thời gian phản hồi trung vị 214 phút — những thứ đã không còn tồn tại.
2. Kịch bản A quá bi quan: cần 4.546 lead = 50,5 lead/ngày, vượt trần xử lý cuối tuần (2 sale × 12 = 24/ngày) rất xa.
3. Kịch bản C quá lạc quan: giả định 100% ngân sách chảy vào 2 chiến dịch Search hoàn hảo — không có kênh đầu phễu nào, không thực tế cho một đợt mở bán.
4. Kịch bản B nằm giữa, và **34,3 lead/ngày** khớp đúng với thực tế GĐ3 (35,4 lead mới/ngày, [S08-B]) → không đòi sale làm việc ở mức chưa từng đạt được.

**Kiểm tra ngược với ràng buộc KPI CP/SQL ≤ 2.200.000 ₫:**

| Câu hỏi | Trả lời |
|---|---|
| Với 2,1 tỷ và trần CP/SQL 2,2tr, mua được tối đa bao nhiêu SQL? | **955 SQL** |
| 955 SQL ra bao nhiêu cọc? | Tỷ lệ toàn kỳ 2,76% → **26,4 cọc (TRƯỢT)** · Tỷ lệ GĐ3 3,48% → **33,2 cọc (ĐẠT)** · Tỷ lệ 2CD Search 3,31% → 31,6 cọc |
| Tỷ lệ SQL→cọc **tối thiểu** để 955 SQL ra 32 cọc | **3,35%** (hiện toàn kỳ 2,76%, GĐ3 3,48%) |

**Kết luận B4 — nói thẳng với ban giám đốc:** KPI khả thi nhưng **không có biên an toàn**. Nó chỉ đạt nếu giữ được tỷ lệ SQL→cọc ở mức GĐ3 (3,48%) hoặc cao hơn 3,35%. Mà tỷ lệ đó phụ thuộc **tốc độ phản hồi của sale** (A1) nhiều hơn phụ thuộc quảng cáo. Nếu SLA trượt về mức GĐ1 (SQL→cọc 1,32%), thì dù tiêu đúng 2,1 tỷ ở CP/SQL 2,2tr cũng chỉ ra **12,6 cọc**.

## B5. Điểm hòa vốn — trần chi phí quảng cáo trên mỗi cọc

Hoa hồng ghi nhận: **181.000.000 ₫/cọc** [S01].

| Mục tiêu ROAS | Chi phí QC tối đa/cọc (₫) | Ghi chú |
|---|---|---|
| 1,0x (hòa vốn thô trên chi phí QC) | **181.000.000** | Chưa trừ 45% hoa hồng sale + 20% vận hành |
| 2,0x | 90.500.000 | |
| **3,0x (KPI)** | **60.333.333** | **Trần bắt buộc** |
| 3,5x (biên an toàn) | 51.714.286 | |

**Đối chiếu thực tế:**

| | Giá trị |
|---|---|
| CP/cọc thực tế 90 ngày qua | **100.196.500 ₫** |
| Vượt trần ROAS 3,0x | **gấp 1,66 lần** |
| CP/cọc của Brand (chiến dịch tốt nhất) | **20.016.846 ₫** → ROAS 8,76x, dư sức |
| CP/cọc của Generic | 135.598.800 ₫ → **vượt trần 2,25 lần** |
| Số cọc tối thiểu cần đạt nếu tiêu hết 2,1 tỷ | 2.100.000.000 / 60.333.333 = **34,8 → làm tròn 35 cọc** |

**Phát hiện quan trọng — hai KPI mâu thuẫn nhau:**

> 32 cọc × 181tr = **5.792.000.000 ₫**. Chia cho 2,1 tỷ = **ROAS 2,76x — TRƯỢT mục tiêu 3,0x.**

Chỉ đạt "32 cọc" **không đủ** để đạt "ROAS ≥3,0x" nếu tiêu hết ngân sách. Có đúng **2 đường** để đạt cả hai:
- **(a)** Đạt **≥35 cọc** trong khi tiêu 2,1 tỷ, hoặc
- **(b)** Đạt đúng 32 cọc nhưng **chỉ tiêu tối đa 1.930.666.667 ₫** (giữ lại 169,3 triệu không tiêu).

Kế hoạch Phần C của tôi đi theo đường **(a)**: mục tiêu 35 cọc.

## B6. Đối chiếu ba nguồn số liệu — bóc tách chính xác 3.820 vs 2.557

**Bước 1 — cột "Chuyển đổi" của Google Ads được tạo thành từ gì:**

| Thành phần | Số lượt | Nguồn |
|---|---|---|
| generate_lead (gửi form thành công) | 1.715 | [S10-A] |
| click_to_call (tổng lượt, **chưa khử trùng**) | 1.132 | [S10-A] |
| view_price_page (xem trang /bang-gia) | 612 | [S10-A] |
| engaged_30s (ở lại >30 giây) | 361 | [S10-A] |
| **CỘNG** | **3.820** ✅ | khớp [S02] `ChuyenDoi_Ads` |

*Ghi chú: GA4 và Google Ads luôn bằng nhau (3.820 = 3.820) vì Ads nhập trực tiếp từ GA4 [S10-A]. Đây thực chất chỉ là **hai nguồn**, không phải ba — nguồn độc lập thứ hai là CRM.*

**Bước 2 — bóc tách từng thành phần của khoảng chênh 1.263:**

| Thành phần chênh lệch | Số lượng | Bản chất | Nguồn xác nhận |
|---|---|---|---|
| **(1) Đếm trùng lượt gọi** | **−353** | 1.132 lượt nhấp `tel:` − 779 người duy nhất. Một người bấm gọi nhiều lần | [S10-A]; [S12-A] thẻ #4 "Đếm mọi lượt nhấp, không khử trùng theo người dùng"; [S12-C] "Thổi phồng 353 chuyển đổi (9,2%)" |
| **(2) Sự kiện rác** | **−973** | view_price_page 612 + engaged_30s 361. [S10-E] ghi rõ cả hai: "**KHÔNG** phải khách hàng tiềm năng" | [S10-A/E]; [S12-A] thẻ #5, #6 |
| **= Lead thật ĐO ĐƯỢC bằng thẻ** | **2.494** | 1.715 form + 779 người gọi duy nhất | [S10-A] |
| **(3) Lead MẤT THẺ** | **+63** | Lead ngày 44, 45, 46 — GTM v23 làm gãy trigger `generate_lead`, "63 lead của 3 ngày trước đó **vĩnh viễn không có** trong Google Ads/GA4" | [S10-A]; [S12-B] v23/v24; kiểm chứng ngược trên [S02] ở mục A11 |
| **= Lead thật trên CRM** | **2.557** ✅ | | khớp [S02] `Lead_CRM` |

**Bước 3 — chứng minh phép cộng khớp (2 chiều):**

```
Chiều xuôi:  3.820 − 353 (trùng) − 973 (rác) = 2.494 ✓
             2.494 + 63 (mất thẻ)            = 2.557 ✓ = CRM
Chiều gộp:   3.820 − 2.557 = 1.263
             353 + 973 − 63 = 1.263          ✓ KHỚP
```
Cả 2 đẳng thức đều được `assert` trong `agent-5-calc.py` (dòng self-check).

**Diễn giải:**
- Tỷ lệ thổi phồng **3.820/2.557 = 1,494x**. Benchmark [S09]: 1,0–1,2 = tốt · 1,2–1,5 = TB · **>1,8 = báo động**. Ta đang ở mép trên của "trung bình" — **nhưng con số này đang được che giấu bởi 63 lead mất thẻ**: nếu GTM không gãy, tỷ lệ sẽ là 3.883/2.557 = **1,52x**.
- **34,7% cột Chuyển đổi (1.326/3.820) không phải lead mới.** Đây là con số Smart Bidding đang dùng để học.
- Ba nguồn không mâu thuẫn — chúng **đo ba thứ khác nhau**: Ads/GA4 đo *sự kiện trên trình duyệt*, CRM đo *người thật có số điện thoại*. Không có nguồn nào "sai"; sai là ở chỗ **khai 4 sự kiện khác loại vào cùng một cột và gọi nó là "chuyển đổi"**.
- Chiều "mất thẻ" nghiêm trọng hơn chiều "thổi phồng" về mặt tối ưu: thổi phồng làm bidding học sai; mất thẻ làm bidding **học rằng lưu lượng tốt không convert** — thiệt hại kéo dài nhiều tuần sau khi sự cố đã sửa.

## B7. Ước tính lead mất do lỗi kỹ thuật CHƯA SỬA và quy ra tiền

**Phân định rõ đâu là số đo, đâu là ước tính:**

| Loại | Nội dung |
|---|---|
| **SỐ ĐO trực tiếp** (Clarity ghi hình, ~92% lưu lượng) | 8.412 nhấp chết trên ảnh giả nút · 1.847 nhấp chết trên `tel:` · 4.196 phiên gặp lỗi JS ở nút gửi · 2.741 phiên bị khung chat che CTA · 1.204 phiên nhấp `tel:` không phản hồi · tỷ lệ lỗi JS di động 9,3% (v1) → 8,9% (v2) |
| **ƯỚC TÍNH của đội UX** (không phải số đo) | Khoảng lead mất cho từng lỗi — sheet ghi rõ: *"Ước tính do đội UX đưa ra dựa trên tỷ lệ hoàn tất form của nhóm phiên không gặp lỗi. **Là ước tính, không phải số đo trực tiếp**"* |
| **ƯỚC TÍNH của tôi** | Quy đổi lead → SQL → cọc → tiền, dùng tỷ lệ thực tế của [S02] |

**Bảng quy tiền:**

| # | Lỗi CHƯA SỬA | Phiên (số đo) | Lead mất (ước tính UX) | Giá trị theo CPL CRM 705.333 ₫ |
|---|---|---|---|---|
| 4 | Lỗi JS `e.setDate` — Safari iOS 17.x, form không gửi được, không báo lỗi | 4.196 | 280 – 340 | 197.493.297 – 239.813.289 ₫ |
| 5 | CTA bị khung chat che (<380px) | 2.741 | 60 – 90 | 42.319.993 – 63.479.990 ₫ |
| 6 | `tel:` chết trên máy tính | 1.204 | 30 – 50 | 21.159.997 – 35.266.661 ₫ |
| | **TỔNG** | **8.141** | **370 – 480** | **260.973.285 – 338.559.937 ₫** |

**Quy đổi sâu hơn** `[ƯỚC TÍNH CỦA TÔI — dùng tỷ lệ toàn kỳ [S02]: SQL/Lead 25,5%, Lead→Cọc 0,704%]`:

| Quy đổi | Cận dưới (370 lead) | Cận trên (480 lead) |
|---|---|---|
| Chi phí đã trả cho lưu lượng bị mất (× CPL 705.333 ₫) | 260.973.285 ₫ | 338.559.937 ₫ |
| Quy ra SQL (× 25,5%) | **94 SQL** | **122 SQL** |
| Giá trị theo CP/SQL 2.770.410 ₫ | 260.973.285 ₫ | 338.559.937 ₫ |
| Quy ra cọc (× 0,704%) | **2,60 cọc** | **3,38 cọc** |
| **Doanh thu hoa hồng bỏ lỡ (× 181tr)** | **471.435.276 ₫** | **611.591.709 ₫** |

**Cảnh báo về mức độ tin cậy của con số này:**
1. Clarity chỉ lấy mẫu **~92%** lưu lượng và mã theo dõi chỉ gắn **từ ngày 5** [S11 header] → các con số phiên là **thiếu ~8% + thiếu 4 ngày đầu**. Con số thật cao hơn.
2. Ước tính lead của đội UX dựa trên "tỷ lệ hoàn tất form của nhóm phiên không gặp lỗi" — phương pháp hợp lý nhưng giả định nhóm gặp lỗi và không gặp lỗi có cùng ý định mua, điều này **chưa được kiểm chứng**.
3. Tỷ lệ lead→cọc 0,704% là tỷ lệ **trung bình toàn tài khoản**, kéo xuống bởi PMax (829 lead / 0 cọc). Lỗi #4 nằm trên form đăng ký — nơi lưu lượng Search chất lượng cao đi qua. Nếu dùng tỷ lệ lead→cọc của Brand (1,52%), con số cọc mất là **5,6 – 7,3 cọc = 1,02 – 1,32 tỷ ₫**. Tôi báo cáo con số thận trọng (2,60–3,38 cọc) nhưng ban giám đốc cần biết cận trên.

**Tham chiếu — thiệt hại đã xảy ra, không thu hồi được:**
- Lỗi ĐÃ SỬA ở v2 (#1 ảnh giả nút, #2 trường CMND, #3 dropdown ngân sách): 520–690 lead trong N1–57 = **366.773.266 – 486.679.910 ₫**.
- 63 lead mất thẻ N44–46 (đây là **SỐ ĐO**, không phải ước tính — [S10-A] và [S12-B] đều ghi con số 63): chi phí tương ứng **44.435.992 ₫**, cộng 59.528.000 ₫ chi phí 3 ngày chạy mù.

**Cần thêm dữ liệu để chốt chính xác:** (1) tỷ lệ hoàn tất form phân tách theo trình duyệt/OS trong GA4 (để đo trực tiếp thiệt hại Safari iOS thay vì ước tính); (2) số phiên có `form_start` nhưng không có `generate_lead` **và** có lỗi JS — đây là phép đo trực tiếp thay cho ước tính của đội UX.

---

# PHẦN C — KẾ HOẠCH 90 NGÀY TIẾP THEO

## C0. Nguyên tắc chi phối toàn kế hoạch

1. **Sửa đo lường TRƯỚC khi tăng tiền.** 34,7% cột Chuyển đổi là rác (B6) → mọi đồng tăng thêm hôm nay đều bị Smart Bidding phân bổ theo tín hiệu sai. Đây là lý do GĐ1 chỉ tiêu 555 triệu (26,4% ngân sách) chứ không chia đều 700/700/700.
2. **Trần cứng không phải ngân sách, mà là năng lực sale.** 8 sale × 12 lead = 96 lead/ngày ngày thường, nhưng **chỉ 24 lead/ngày cuối tuần** (2 sale). Không tăng nhân sự (ràng buộc [S01]).
3. **Dồn tiền về nơi đã chứng minh ra cọc**: Brand ROAS 8,76x và Generic 2,01x (GĐ3) là 2 nguồn duy nhất tạo 18/18 cọc.
4. **Mục tiêu 35 cọc, không phải 32.** Vì 32 cọc + tiêu hết 2,1 tỷ = ROAS 2,76x, trượt KPI (chứng minh ở B5).

## C1. Bảng phân bổ ngân sách — tổng đúng 2.100.000.000 ₫

| Chiến dịch | GĐ1 (tr ₫) | GĐ2 (tr ₫) | GĐ3 (tr ₫) | Tổng (tr ₫) | % | Thay đổi vs 90 ngày qua |
|---|---|---|---|---|---|---|
| **SEA_Brand_VinhomesHocMon** (mở rộng IS) | 180 | 210 | 240 | **630** | 30,0% | 260tr → 630tr (**+142%**) |
| **SEA_Generic_NhaPho_CanHo** (tái cấu trúc) | 200 | 240 | 280 | **720** | 34,3% | 678tr → 720tr (+6%) |
| **SEA_ChinhSach_TraGop_TayBac** (MỚI) | 50 | 60 | 70 | **180** | 8,6% | 0 → 180tr |
| **PMAX_Lead_v2** (xây lại, brand exclusion) | 40 | 70 | 100 | **210** | 10,0% | 475tr → 210tr (**−56%**) |
| **GDN_Remarketing_Web30d** | 25 | 30 | 35 | **90** | 4,3% | 130tr → 90tr (−31%) |
| **YT_Video_TVC_MoBan** (chỉ GĐ2–3) | 0 | 20 | 30 | **50** | 2,4% | 83tr → 50tr (−40%) |
| **Dự phòng / test / sự kiện mở bán** | 60 | 70 | 90 | **220** | 10,5% | 0 → 220tr |
| ~~SEA_Competitor_DoiThu~~ | **0** | **0** | **0** | **0** | 0% | 177tr → **0 (DỪNG)** |
| **TỔNG** | **555** | **700** | **845** | **2.100** | **100%** | |
| Ngân sách/ngày | 18,5tr | 23,3tr | 28,2tr | | | |

*Kiểm tra: 630+720+180+210+90+50+220 = **2.100 triệu** ✅ (assert trong script).*

**Lý do 3 điều chỉnh lớn nhất:**

| Điều chỉnh | Bằng chứng |
|---|---|
| Brand +142% (260→630tr) | Mất **39,7% IS do ngân sách** [S02], ROAS 8,76x, CP/SQL 739.259 ₫ (rẻ nhất TK, dưới ngưỡng "tốt" của [S09]). Ngay cả sau khi hạ 32,3% do attribution [S10-D] vẫn là kênh sinh lời số 1. Cấp 630tr đưa mất IS ngân sách về <10%. **Trần tự nhiên**: tồn kho tìm kiếm thương hiệu có hạn — nếu IS đạt >90% mà chưa hết tiền, phần dư chuyển sang Generic (quy tắc ở C7). |
| PMax −56% (475→210tr) | 0 cọc, SQL/Lead 7,4%, 74,3% thoát <3 giây [S11-B]. Không cắt hẳn vì [S10-D] cho thấy PMax vẫn giữ 466/1.715 lead theo mô hình dựa trên dữ liệu — nó có đóng góp thật, chỉ là đang bị đo và tối ưu sai. Giữ 210tr để **chạy lại từ đầu sau khi sửa tín hiệu**, với ngân sách GĐ1 chỉ 40tr (bậc thử nghiệm). |
| Competitor → 0 | 176,7tr / 3 SQL / 0 cọc, CP/SQL 58.915.333 ₫ = **gấp 11,8 lần ngưỡng báo động [S09]**, 6/6 cụm từ SQL=0 [S04], 26% lead là môi giới/đối thủ [S08-C]. 90 ngày đủ dữ liệu. |

---

## C2. GIAI ĐOẠN 1 (Ngày 1–30) — "Cầm máu và sửa thước đo"

### Mục tiêu định lượng

| Chỉ tiêu | Mục tiêu GĐ1 | Baseline GĐ tương ứng vừa qua |
|---|---|---|
| Ngân sách | 555.000.000 ₫ (18,5tr/ngày) | 545.696.000 ₫ |
| Lead CRM | **895** (29,8/ngày) | 734 |
| CPL CRM | ≤ **620.000 ₫** | 743.455 ₫ |
| SQL | **286** (SQL/Lead ≥32%) | 151 (20,6%) |
| CP/SQL | ≤ **1.937.500 ₫** | 3.613.881 ₫ |
| Đặt cọc | **7** | 2 |
| ROAS | ≥ **2,28x** | 0,60x |
| **Chênh Ads/CRM** | **≤ 1,15x** (từ 1,49x) | 1,49x |
| **Tỷ lệ lead gọi lại <30 phút** | ≥ **70%** | 30% (11%+19%) |

### Cấu trúc tài khoản đề xuất

| Chiến dịch | Nhóm quảng cáo | Loại đối sánh | Ghi chú |
|---|---|---|---|
| **SEA_Brand_VinhomesHocMon** | AG1 `Brand-Core` (vinhomes hóc môn, vin hóc môn, vinhomes hoc mon) | **Chính xác + Cụm từ** | 3 RSA/nhóm (hiện chỉ 1 [S05]) |
| | AG2 `Brand-Gia` (…giá bán, …bảng giá, …giá bao nhiêu) | Chính xác | LP: `/nhan-bang-gia-2026` |
| | AG3 `Brand-ViTri` (…ở đâu, …vị trí, dự án…) | Cụm từ | LP: khối Vị trí |
| **SEA_Generic_NhaPho_CanHo** | AG1 `NhaPho-HocMon` | Chính xác + Cụm từ | tách nhà phố vs căn hộ để khớp thông điệp |
| | AG2 `CanHo-HocMon` | Chính xác + Cụm từ | |
| | AG3 `NhaPho-Quan12-GoVap` | Cụm từ | 2 quận có cọc [S06] |
| | AG4 `Shophouse-BietThu` | Chính xác | |
| | AG5 `Broad-Test` (đối sánh rộng có kiểm soát) | **Rộng — ngân sách trần 15%** | Chỉ mở SAU khi có ECL chạy ổn |
| **SEA_ChinhSach_TraGop_TayBac** (MỚI) | AG1 `TraGop-AnHan` · AG2 `HoTroLaiSuat` · AG3 `ThanhToan-15%` | Chính xác + Cụm từ | Khai thác chính sách "ân hạn gốc 24 tháng, LS 0% 18 tháng" [S01] — chưa có cụm từ nào trong [S04] chạm ý định này |
| **PMAX_Lead_v2** | 1 nhóm tài sản, **loại trừ thương hiệu BẬT**, loại trừ vị trí đặt đã cấu hình | — | Chỉ dùng tín hiệu đối tượng từ danh sách khách hàng CRM |
| **GDN_Remarketing_Web30d** | AG1 `Da-xem-bang-gia` · AG2 `Bo-do-form` (form_start không generate_lead) | — | Loại trừ danh sách "đã đặt cọc/đã ký HĐMB" |

**Cấu hình bắt buộc sửa ngay ngày 1** (nguồn [S05]):

| Hạng mục | Hiện tại | Sửa thành | Cơ sở |
|---|---|---|---|
| Vị trí | Việt Nam toàn quốc | **TP.HCM + Bình Dương + Long An + Đồng Nai**; loại trừ Hà Nội, Đà Nẵng, ĐBSCL, ngoài VN | [S06]: 4 nhóm loại trừ = 364,3tr, 0 cọc |
| Tùy chọn vị trí | Hiện diện HOẶC quan tâm | **Chỉ "Hiện diện"** (Presence) | Nguyên nhân trực tiếp của chi phí Hà Nội/Đà Nẵng |
| Ngôn ngữ | Tiếng Việt + Tiếng Anh | **Chỉ Tiếng Việt** | Sản phẩm bán cho khách nội địa |
| Search Partners | BẬT | **TẮT** (3 CD Search) | Không có báo cáo tách riêng để chứng minh giá trị |
| Mạng hiển thị trong CD Search | BẬT | **TẮT** | Trộn lưu lượng, làm hỏng đọc số Search |
| Từ khóa phủ định | 12 từ, không dùng danh sách chia sẻ | **Danh sách chia sẻ ≥120 từ**, áp cho cả 6 CD | [S04]: 17 cụm SQL=0 = 419,7tr |
| Lịch quảng cáo | 24/7 không điều chỉnh | **Tắt 23:00–06:00**; giảm giá thầu −30% khung 20:00–23:00; **giảm −40% T7–CN** | [S07-A/C], xem C2.6 |
| Thiết bị | Không điều chỉnh | **Máy tính +25%**, máy tính bảng −20% | [S07-B]: desktop CP/SQL rẻ hơn 65% |
| Tiện ích | Chỉ 4 Liên kết trang web | Thêm **Cuộc gọi (chỉ giờ có sale), Biểu mẫu KH tiềm năng, Vị trí, Chú thích, Hình ảnh, Giá** | [S05] "Tiện ích còn thiếu" |
| Cửa sổ chuyển đổi | 90 ngày | **Giữ nguyên 90 ngày** | Đúng — chu kỳ BĐS dài (`tracking/README.md` luật #4) |

**Danh sách phủ định ưu tiên (chặn ngay, dựa trên [S04] — 209.082.000 ₫/90 ngày):**
`tuyển dụng`, `việc làm`, `học phí`, `vinschool`, `thuê`, `cho thuê`, `nhà trọ`, `kho xưởng`, `nguyên căn`, `lừa đảo`, `quy hoạch`, `bản đồ`, `chung cư mini`, `giá rẻ`, `100 triệu`, `thổ cư`, `có thật không`, `giá đất`, + toàn bộ tên đối thủ (`vạn phúc`, `global city`, `izumi`, `aqua city`).
*Lưu ý cân nhắc: "vinhomes hóc môn có thật không" (13tr, 3 SQL) và "giá đất hóc môn 2026" (33,9tr, 29 lead, 0 SQL) — cụm đầu là ý định thẩm định dự án, tôi khuyến nghị **giữ nhưng đổi LP sang trang pháp lý** thay vì phủ định thẳng; cụm sau phủ định hẳn.*

### Chiến lược giá thầu GĐ1

| Chiến dịch | Chiến lược | Lý do |
|---|---|---|
| SEA_Brand | **CPC thủ công nâng cao (eCPC)** hoặc **Tỷ lệ hiển thị mục tiêu = 90%, vị trí đầu trang** | Mục tiêu duy nhất của GĐ1 là **lấy lại 39,7% IS đang mất**. Chưa dùng Smart Bidding vì tín hiệu chuyển đổi còn bẩn tới hết Tuần 2. |
| SEA_Generic | **Tối đa hóa số nhấp CÓ đặt trần CPC = 35.000 ₫** | [S05] hiện "không đặt trần CPC" → CPC thực tế 33.070 ₫ [S02], benchmark [S09] TB 25–45k. Đặt trần chặn đấu giá vượt kiểm soát. |
| SEA_ChinhSach (mới) | Tối đa hóa số nhấp, trần CPC 30.000 ₫ | Chưa có dữ liệu lịch sử |
| PMAX_Lead_v2 | **Tối đa hóa chuyển đổi CÓ tCPA = 1.500.000 ₫** | [S05] hiện "không đặt CPA mục tiêu" = nguyên nhân trực tiếp của lưu lượng rác. tCPA 1,5tr đặt theo CPL mục tiêu × hệ số an toàn. |
| GDN_Remarketing | Giữ CPC nâng cao | Ngân sách nhỏ, không đủ dữ liệu để Smart Bidding |
| YT | Không chạy GĐ1 | Dồn tiền cho việc sửa nền |

**Điều kiện chuyển đổi chiến lược (ngưỡng số cụ thể):**

| Từ → Sang | Điều kiện bắt buộc (đủ CẢ) |
|---|---|
| Max Clicks → **tCPA** (Generic, ChinhSach) | (1) Sự kiện rác đã gỡ khỏi cột Chuyển đổi ≥14 ngày; (2) campaign đạt **≥30 chuyển đổi/30 ngày** (chuẩn Google, `research/google-ads-bds-vn.md` §4); (3) chênh Ads/CRM ≤1,2x trong 14 ngày liên tiếp |
| tCPA → **tROAS** | (1) ECL (chuyển đổi ngoại tuyến từ CRM) chạy ổn định ≥30 ngày; (2) ≥15 chuyển đổi cọc/30 ngày ở cấp tài khoản; (3) giá trị chuyển đổi đã gắn theo thang (SQL / đi xem / cọc) |
| eCPC → **Tỷ lệ hiển thị mục tiêu** (Brand) | Áp ngay khi có ngân sách 180tr; ngưỡng: IS mục tiêu 90%, giới hạn giá thầu CPC 25.000 ₫ |
| **Rollback**: tCPA → Max Clicks | Nếu sau 21 ngày ở tCPA, khối lượng lead giảm >30% so với 21 ngày trước **và** CP/SQL không cải thiện >15% |

### KẾ HOẠCH ĐO LƯỜNG GĐ1 (mục riêng — đây là việc quan trọng nhất của 30 ngày đầu)

Thứ tự triển khai **không được đảo** — mỗi bước phụ thuộc bước trước.

#### Bước 1 (Ngày 1–2) — Dừng chảy máu tín hiệu · SỬA TRONG GA4

| # | Việc | Chi tiết | Cách kiểm tra sau khi sửa |
|---|---|---|---|
| 1.1 | Bỏ đánh dấu "sự kiện chính" cho **`view_price_page`** và **`engaged_30s`** | GA4 → Quản trị → Sự kiện → tắt "Đánh dấu là sự kiện chính" | Sau 24h, cột Chuyển đổi Ads phải giảm ≈**25,5%** (từ ~42 xuống ~31 chuyển đổi/ngày). Nếu không giảm → hành động chuyển đổi trong Ads chưa được gỡ khỏi "Chuyển đổi chính" |
| 1.2 | Trong **Google Ads** → Mục tiêu → Chuyển đổi: chuyển 2 hành động trên sang **"Phụ" (Secondary)** | Giữ lại để quan sát, không tính vào cột Chuyển đổi | Cột "Chuyển đổi" ≠ cột "Tất cả chuyển đổi" |
| 1.3 | `click_to_call` → chuyển sang **"Phụ" vĩnh viễn** | Luật `tracking/README.md` #2: phone_click/zalo_click = Secondary vĩnh viễn, tránh bẫy "bidding mua click nút rẻ" | Cột Chuyển đổi chỉ còn `generate_lead` |
| 1.4 | **Chuyển đổi chính duy nhất tạm thời = `generate_lead`** | Số nền mới ≈ 1.715/90 ngày = **19,1/ngày** | Đối chiếu với Lead CRM hằng ngày, chênh phải ≤1,1x |

> **Cảnh báo bắt buộc kèm bước 1:** cột Chuyển đổi sẽ **rơi ~55%** (3.820 → 1.715 quy đổi). Phải báo trước ban giám đốc bằng văn bản, kèm câu: *"Số giảm vì ta ngừng đếm nhầm, không phải vì hiệu quả giảm. Lead CRM là số không đổi."* Đồng thời **PMax đang chạy Smart Bidding sẽ vào lại learning phase** → chấp nhận biến động 7–14 ngày, không đụng thêm gì trong khoảng đó (`playbook/monitoring.md` §2 Learning phase guard).

#### Bước 2 (Ngày 2–3) — Khai `Data exclusion` cho sự cố cũ · TRONG GOOGLE ADS

Theo `playbook/monitoring.md` §2.1 (dẫn Google *About data exclusions*): tracking gãy N44–46 mà không khai exclusion → Smart Bidding vẫn đang né loại lưu lượng của những ngày đó. Tạo exclusion **backdate** cho khoảng nhấp **N41–N47** (lùi ≥3 ngày trước sự cố để phủ độ trễ chuyển đổi, phủ ≥90% nhấp bị ảnh hưởng, tổng <14 ngày — đúng 4 điều kiện của Google). Áp cho các campaign đang dùng Smart Bidding (PMax).

#### Bước 3 (Ngày 3–7) — SỬA TRONG GTM

| # | Việc | Chi tiết |
|---|---|---|
| 3.1 | **Xóa thẻ #2 `GA4 Configuration – Copy of Main`** | Chấm dứt page_view đếm đôi từ N31 [S12-A/B v22] |
| 3.2 | **Đổi điều kiện kích hoạt `generate_lead` từ class CSS sang `dataLayer.push`** | Nguyên nhân sự cố N44–46. LP đẩy `dataLayer.push({event:'generate_lead'})` sau khi server trả về thành công. Trigger = Custom Event, **không phụ thuộc DOM** |
| 3.3 | **Cài biến ẩn lưu `gclid` (+ `gbraid`, `wbraid`, `gad_source`, `utm_*`) vào form** | [S12-A #15]. Đây là **điều kiện tiên quyết của toàn bộ lộ trình tối ưu**. Dùng skill `ad-click-attribution` |
| 3.4 | **Bật Enhanced Conversions** (chuyển đổi nâng cao) | [S12-A #14]: thu hồi 10–20% khả năng khớp = 249–499 lead |
| 3.5 | **Đánh dấu `zalo_click` (894) và `file_download` (1.206) là sự kiện chính — nhưng nhập vào Ads ở mức PHỤ** | [S10-E]: cả hai "Có tín hiệu ý định — đang bỏ sót". Zalo là CTA chính ở thị trường VN |
| 3.6 | **Cài cảnh báo chuyển đổi = 0** | [S12-A #18]. Ngưỡng: chuyển đổi = 0 trong 4 giờ có chi tiêu, trong giờ hoạt động → Telegram/email. Đây là thứ lẽ ra đã tiết kiệm 59.528.000 ₫ |
| 3.7 | **Rà soát + gỡ 3 thẻ đối tác sàn F2 "không rõ nguồn gốc"** và thẻ Zalo Tracking "không rõ ai cài" | [S12-A #12, #13]. Rủi ro bảo mật + 412 KB JS làm chậm LCP ~0,8s. Gỡ được bao nhiêu KB đo lại bằng PageSpeed |
| 3.8 | **Cấu hình Consent Mode v2** | [S12-A #16] |
| 3.9 | **Gắn ID phiên Clarity vào bản ghi CRM** | [S12-A #10]: để xem lại hành trình của lead đã cọc — đầu vào cho tối ưu LP các giai đoạn sau |

**Quy trình mới bắt buộc:** mọi thay đổi GTM phải (1) test ở Preview mode, (2) có người thứ hai duyệt, (3) ghi vào mô tả phiên bản. [S12-B] cho thấy dev@ tự publish v22 và v23 — cả hai đều gây sự cố đo lường.

#### Bước 4 (Ngày 7–14) — Kiểm tra nghiệm thu

| Kiểm tra | Ngưỡng ĐẠT |
|---|---|
| Cột Chuyển đổi Ads / Lead CRM theo ngày | **≤ 1,15x** trong 7 ngày liên tiếp (hiện 1,49x) |
| GA4 `generate_lead` vs CRM lead (cùng ngày) | Chênh ≤ 10% |
| Tỷ lệ lead trong CRM **có `gclid`** | ≥ **85%** (hiện 0%) |
| Enhanced Conversions — trạng thái trong Ads | "Đang ghi nhận" (Recording) |
| Số thẻ GTM | ≤ 20 (từ 34) · JS bên thứ ba ≤ 200 KB (từ 412 KB) |
| Cảnh báo chuyển đổi = 0 | Test giả lập 1 lần, alert phải bắn trong ≤4h |
| GA4 page_view/phiên | ≈1,0 (hiện đang gấp đôi từ N31) |

#### Bước 5 (Ngày 14–30) — Dựng đường ống ECL (chuyển đổi ngoại tuyến)

- Tạo 3 hành động chuyển đổi ngoại tuyến trong Ads theo thang giá trị: `Lead_Contactable` · `Lead_SQL` · `Dat_Coc` (giá trị 181.000.000 ₫).
- CRM (Keap) xuất hằng ngày: `gclid` + timestamp + tag trạng thái → upload qua **Data Manager API** (Google Ads API đã chặn upload offline từ 15/6/2026 — `tracking/README.md` luật #3).
- **Chưa đổi chuyển đổi chính sang `Lead_SQL` trong GĐ1** — chỉ chạy song song để tích dữ liệu. Đổi ở GĐ2 (điều kiện ở C3).

### Trang đích / Tiện ích / Đối tượng — GĐ1

| Hạng mục | Việc | Ngưỡng nghiệm thu |
|---|---|---|
| **LP — ưu tiên #1** | Sửa lỗi JS `TypeError e.setDate` (Safari iOS 17.x). Cách nhanh nhất: **bỏ hẳn trường chọn ngày hẹn xem nhà** khỏi form (sale hỏi qua điện thoại) | Tỷ lệ phiên có lỗi JS trên di động trong Clarity: 8,9% → **<2%**. Thu hồi 280–340 lead/90 ngày (B7) |
| **LP #2** | Đẩy khung chat xuống/thu nhỏ trên màn hình <380px; nút CTA sticky không bị che | Rage click di động: 3,1% → <2% |
| **LP #3** | Số hotline trên máy tính: hiện số + nút copy thay vì chỉ `tel:` | Dead click đầu trang: 1.847 → <200 |
| **LP #4** | **Bật A/B test** (hiện [S05] "1 phiên bản, không thử nghiệm") — biến thể form 3 trường vs 2 trường (chỉ tên + SĐT) | Chạy tối thiểu tới 400 chuyển đổi/nhánh trước khi kết luận |
| **LP #5** | Thêm nút Zalo nổi (CTA chính thị trường VN) + đo `zalo_click` | ≥300 lượt zalo_click/30 ngày |
| **Tiện ích** | Thêm Cuộc gọi (lên lịch 08:00–20:00 T2–T6, 08:00–17:00 T7–CN theo ca trực), Biểu mẫu KH tiềm năng, Vị trí, Chú thích, Hình ảnh, Giá | CTR Brand ≥13% (hiện 11,63%) |
| **Đối tượng** | Chuyển 5 danh sách từ **Quan sát → Nhắm mục tiêu/Điều chỉnh giá thầu** [S05]; tạo danh sách **loại trừ "đã đặt cọc / đã ký HĐMB"** (hiện chưa có) | Danh sách khách hàng CRM ≥1.000 người khớp để dùng cho Customer Match |

### Tiêu chí dừng/mở rộng GĐ1 (ngưỡng số, đánh giá cuối Tuần 2 và Tuần 4)

| Điều kiện | Hành động |
|---|---|
| Chênh Ads/CRM vẫn >1,3x sau ngày 14 | **Dừng mọi việc tăng ngân sách**, quay lại debug GTM |
| Brand: mất IS do ngân sách vẫn >20% sau ngày 14 | Tăng ngân sách Brand thêm 30tr, lấy từ quỹ dự phòng |
| Brand: IS >90% **và** vẫn dư ngân sách | Chuyển phần dư sang Generic (tồn kho brand đã hết) |
| Bất kỳ nhóm quảng cáo nào: chi >20.000.000 ₫ mà 0 SQL | **Tạm dừng nhóm** |
| Bất kỳ cụm từ nào: chi >8.000.000 ₫ mà 0 lead | Thêm phủ định ngay |
| PMax: CP/SQL >4.000.000 ₫ sau ngày 21 | Hạ ngân sách GĐ2 từ 70tr → 40tr |
| Lead/ngày >45 trong 3 ngày liên tiếp **hoặc** tỷ lệ gọi <30 phút tụt <60% | **Giảm ngân sách 20%** — đang mua lead vượt năng lực xử lý |
| CP/SQL ≤1.900.000 ₫ **và** SQL/Lead ≥32% ở cuối Tuần 4 | Duyệt tăng ngân sách GĐ2 theo kế hoạch |

---

## C3. GIAI ĐOẠN 2 (Ngày 31–60) — "Chuyển sang Smart Bidding theo chất lượng"

### Mục tiêu định lượng

| Chỉ tiêu | Mục tiêu GĐ2 | GĐ1 |
|---|---|---|
| Ngân sách | 700.000.000 ₫ (23,3tr/ngày) | 555tr |
| Lead CRM | **1.167** (38,9/ngày) | 895 |
| CPL CRM | ≤ **600.000 ₫** | 620.000 ₫ |
| SQL (SQL/Lead ≥35%) | **408** | 286 |
| CP/SQL | ≤ **1.714.286 ₫** | 1.937.500 ₫ |
| Đặt cọc | **11** | 7 |
| ROAS | ≥ **2,84x** | 2,28x |
| Chênh Ads/CRM | ≤ 1,10x | ≤1,15x |
| % lead có gclid trong CRM | ≥ 90% | ≥85% |

### Cấu trúc — thay đổi so với GĐ1

- Tách **AG `Brand-Canho`** và **AG `Brand-Nhapho`** để khớp thông điệp theo phân khúc giá (2,9–4,6 tỷ vs 6,8–11,5 tỷ) — hai tệp khách khác nhau hoàn toàn [S01].
- Mở **AG5 `Broad-Test`** của Generic (đối sánh rộng có kiểm soát) **chỉ khi** ECL đã chạy ổn ≥14 ngày — vì đối sánh rộng chỉ an toàn khi Smart Bidding có tín hiệu chất lượng (bài học từ 71% chi phí rộng của kỳ trước, [S05]).
- Xây lại **PMAX_Lead_v2** với tín hiệu đối tượng = danh sách khách hàng CRM (những người đã thành SQL), brand exclusion BẬT, loại trừ vị trí đặt đã cấu hình.

### Giá thầu GĐ2 và điều kiện chuyển

| Chiến dịch | Chiến lược GĐ2 | Điều kiện đã thỏa để chuyển |
|---|---|---|
| SEA_Brand | Tỷ lệ hiển thị mục tiêu **95%** (nếu GĐ1 đã đạt >85%) | IS GĐ1 ≥85% |
| SEA_Generic | **tCPA = 600.000 ₫** (theo CPL mục tiêu GĐ2) | ≥30 chuyển đổi `generate_lead`/30 ngày + Ads/CRM ≤1,2x trong 14 ngày |
| SEA_ChinhSach | tCPA = 650.000 ₫ | như trên |
| PMAX_Lead_v2 | tCPA = 1.200.000 ₫ (siết từ 1,5tr) | CP/SQL GĐ1 ≤4tr |
| GDN | tCPA = 700.000 ₫ | ≥20 chuyển đổi/30 ngày |
| YT (mở lại, 20tr) | CPV mục tiêu, đo bằng **Brand Lift / tìm kiếm thương hiệu tăng thêm**, KHÔNG đo bằng CPL nhấp cuối | [S10-D]: YT thực tế đóng góp 165 lead theo mô hình dựa trên dữ liệu vs 43 theo nhấp cuối (+283,7%) |

### Kế hoạch đo lường GĐ2

| # | Việc | Kiểm tra |
|---|---|---|
| 2.1 | **Đổi mô hình phân bổ từ Nhấp cuối → Dựa trên dữ liệu** trong GA4 và Ads | [S10-D]. Cảnh báo trước: Brand sẽ giảm 32,3% lead trên báo cáo, YT tăng 283,7%. **Không được diễn giải là hiệu suất thay đổi.** Chạy song song 2 mô hình 14 ngày trước khi chuyển hẳn |
| 2.2 | **ECL chạy hằng ngày** qua Data Manager API; đổi **chuyển đổi chính sang `Lead_SQL`** | Điều kiện: ECL upload thành công ≥14 ngày liên tiếp, tỷ lệ khớp ≥70%. Sau khi đổi, Smart Bidding học từ **lead chất lượng** thay vì lead thô — đây là bước tạo ra bước nhảy CP/SQL |
| 2.3 | Gắn **giá trị chuyển đổi** theo thang: Lead_Contactable = 500.000 ₫ · Lead_SQL = 2.200.000 ₫ · Dat_Coc = 181.000.000 ₫ | Chuẩn bị nền cho tROAS ở GĐ3 |
| 2.4 | Dựng **báo cáo đối chiếu 3 nguồn hằng tuần** (Ads / GA4 / CRM) tự động | Chênh lệch từng cặp ≤10%, có cảnh báo khi vượt |
| 2.5 | Kiểm tra lại Clarity: rage click, dead click, lỗi JS sau khi sửa LP | Lỗi JS di động <2%; thoát nhanh <3s của PMax từ 74,3% → <35% |

### LP / Tiện ích / Đối tượng GĐ2

- Kết luận A/B test form GĐ1 → triển khai biến thể thắng cho 100% lưu lượng.
- Thêm trang đích riêng cho **AG `Brand-Gia`** (bảng giá trực tiếp, không gate) và **AG `TraGop`** (bảng tính trả góp) — message match theo `landing-page/README.md`.
- **Customer Match**: upload danh sách 651 SQL + 18 khách đã cọc → tạo đối tượng tương tự (Similar); tạo **danh sách loại trừ** khách đã cọc/đã ký HĐMB cho toàn tài khoản.
- Đối tượng theo giai đoạn: `Đã xem bảng giá 30d`, `Đã tải PDF 30d`, `form_start chưa hoàn tất 7d` (5.743 người/90 ngày — kho remarketing lớn nhất đang bỏ trống).

### Tiêu chí dừng/mở rộng GĐ2

| Điều kiện | Hành động |
|---|---|
| CP/SQL ≤1.700.000 ₫ **và** ≥11 cọc cuối GĐ2 | Duyệt toàn bộ 845tr cho GĐ3 |
| CP/SQL 1,7–2,2tr | Giữ nguyên kế hoạch, không mở rộng nhóm mới |
| CP/SQL >2.200.000 ₫ (vượt KPI) | **Đóng băng ngân sách ở mức GĐ2**, cắt 100% chi tiêu vào các nhóm CP/SQL >4tr |
| tCPA làm khối lượng lead giảm >30% sau 21 ngày mà CP/SQL không cải thiện >15% | **Rollback về Max Clicks có trần CPC** |
| PMax vẫn 0 cọc sau 60 ngày lũy kế | **Dừng hẳn PMax**, chuyển 100tr GĐ3 sang Brand + Generic |
| YT: không tăng được lượng tìm kiếm thương hiệu ≥15% sau 30 ngày | Dừng YT, chuyển 30tr sang Generic |

---

## C4. GIAI ĐOẠN 3 (Ngày 61–90) — "Mở rộng quanh sự kiện mở bán"

### Mục tiêu định lượng

| Chỉ tiêu | Mục tiêu GĐ3 | GĐ2 |
|---|---|---|
| Ngân sách | 845.000.000 ₫ (28,2tr/ngày) | 700tr |
| Lead CRM | **1.457** (48,6/ngày) | 1.167 |
| CPL CRM | ≤ **580.000 ₫** | 600.000 ₫ |
| SQL (SQL/Lead ≥38%) | **554** | 408 |
| CP/SQL | ≤ **1.526.316 ₫** | 1.714.286 ₫ |
| Đặt cọc | **17** | 11 |
| ROAS | ≥ **3,64x** | 2,84x |

> **Kiểm tra ràng buộc năng lực sale:** 48,6 lead/ngày < trần 96/ngày ngày thường ✅ nhưng **vượt trần cuối tuần 24/ngày** ❌. Xử lý: giảm giá thầu T7–CN −40% (từ GĐ1) + dồn lịch chạy vào 09:00–17:00 T2–T6 (khung có tỷ lệ gọi lại 91–93%, [S07-A]). Nếu vẫn vượt: bật **Biểu mẫu KH tiềm năng có xác nhận lịch hẹn tự động** để lead cuối tuần không "nguội" chờ tới T2.

### Giá thầu GĐ3 và điều kiện chuyển

| Chiến dịch | Chiến lược | Điều kiện |
|---|---|---|
| SEA_Brand | Tỷ lệ hiển thị mục tiêu 95%, giới hạn CPC 30.000 ₫ | — |
| SEA_Generic | **tROAS = 300%** | Chỉ chuyển nếu: ECL ổn ≥30 ngày + ≥15 chuyển đổi cọc/30 ngày ở cấp TK + giá trị chuyển đổi đã gắn. **Nếu chưa đủ điều kiện: giữ tCPA 580.000 ₫** — không ép tROAS khi thiếu dữ liệu |
| SEA_ChinhSach | tCPA 600.000 ₫ | — |
| PMAX_Lead_v2 | tCPA 1.000.000 ₫ | Chỉ nếu GĐ2 đạt CP/SQL ≤3tr |
| GDN + YT | Giữ tCPA/CPV | — |

### Kế hoạch đo lường GĐ3

| # | Việc |
|---|---|
| 3.1 | **Audit đo lường toàn diện** (checklist 12 mục của [S12-C] — mục tiêu: 12/12 ĐẠT, hiện 3/12) |
| 3.2 | Đối chiếu ROAS theo mô hình dựa trên dữ liệu vs nhấp cuối, chốt cách báo cáo cho ban giám đốc |
| 3.3 | Đánh giá lại điều kiện mở **server-side tagging**: chỉ mở nếu chứng minh được ad blocker/ITP làm **mất >20% chuyển đổi** khi so Ads/GA4 với CRM (`tracking/README.md` "Điều kiện mở server-side"). Hiện **chưa có bằng chứng** → **không làm** |
| 3.4 | Bàn giao tài liệu: sơ đồ đo lường, danh mục thẻ GTM đã dọn, quy trình publish, danh sách cảnh báo — chính là thứ người tiền nhiệm đã không để lại |

### LP / Tiện ích / Đối tượng GĐ3

- Trang đích **sự kiện mở bán** riêng (đếm ngược, danh sách căn còn, đăng ký giữ chỗ) — LP hiện tại không có yếu tố khan hiếm nào.
- Tiện ích Chú thích + Giá theo phân khúc; tiện ích khuyến mãi cho chính sách ân hạn gốc.
- Đối tượng: đẩy mạnh remarketing tới `form_start chưa hoàn tất` và `đã tải bảng giá` — 2 tệp có ý định cao nhất, hiện chưa dùng.

### Tiêu chí dừng/mở rộng GĐ3

| Điều kiện | Hành động |
|---|---|
| Cuối ngày 75: cọc lũy kế ≥26 | Dồn 100% quỹ dự phòng còn lại vào Brand + Generic |
| Cuối ngày 75: cọc lũy kế 20–25 | Giữ nguyên, siết mọi nhóm CP/SQL >2,5tr |
| Cuối ngày 75: cọc lũy kế <20 | **Cắt PMax + GDN + YT (tổng 165tr GĐ3)**, dồn 100% vào Brand + ChinhSach; báo cáo ban giám đốc rủi ro trượt KPI kèm nguyên nhân |
| Chi tiêu lũy kế 90 ngày dự phóng >2,05 tỷ khi cọc <30 | Hãm chi tiêu để **không vượt 1.930.666.667 ₫** — đường (b) của B5: 32 cọc + tiêu ≤1,93 tỷ vẫn đạt ROAS 3,0x |

## C5. Tổng kiểm tra kế hoạch với KPI

| KPI ban giám đốc | Kế hoạch đạt được | Kết luận |
|---|---|---|
| Ngân sách ≤ 2.100.000.000 ₫ | Đúng 2.100.000.000 ₫ | ✅ |
| Đặt cọc ≥ 32 | **35** (7 + 11 + 17) | ✅ |
| ROAS ≥ 3,0x | 35 × 181tr / 2,1 tỷ = **3,02x** | ✅ (biên rất mỏng) |
| CP/SQL ≤ 2.200.000 ₫ | 2,1 tỷ / 1.248 SQL = **1.682.146 ₫** | ✅ |
| Không tăng nhân sự sale | Kế hoạch giới hạn ở 48,6 lead/ngày, giảm giá thầu cuối tuần | ✅ có điều kiện |

**Rủi ro lớn nhất phải nói rõ:** biên ROAS chỉ 3,02x — **thiếu 1 cọc là trượt KPI**. Và cọc thứ 35 phụ thuộc vào tỷ lệ SQL→cọc đạt 3,07% ở GĐ3, tức phụ thuộc **tốc độ phản hồi của đội sale** nhiều hơn phụ thuộc quảng cáo (A1: chênh 45 lần giữa gọi <5 phút và gọi sau 12h). Nếu ban giám đốc không cam kết SLA gọi lại <30 phút cho ≥80% lead, tôi đề nghị **điều chỉnh KPI xuống 32 cọc + ngân sách trần 1,93 tỷ** (đường (b) của B5) thay vì nhận một mục tiêu mà biến số quyết định nằm ngoài tầm kiểm soát của marketing.

---

# PHẦN D — XỬ LÝ TÌNH HUỐNG

## D1. "Cắt hết ngân sách brand, dồn cho từ khóa chung"

**Trả lời: không cắt. Ngược lại, tôi đề nghị tăng Brand từ 260 triệu lên 630 triệu.** Đây là 5 con số:

| # | Bằng chứng | Số | Nguồn |
|---|---|---|---|
| 1 | Brand ăn **14,4% ngân sách** nhưng tạo **13/18 cọc (72%)** và **2,28 tỷ/3,13 tỷ doanh thu (73%)**, ROAS **8,76x** | | [S02] |
| 2 | **CP/SQL Brand 739.259 ₫ vs Generic 3.549.707 ₫** — Brand rẻ hơn **4,8 lần** trên mỗi lead chất lượng. Brand là chiến dịch duy nhất dưới ngưỡng "tốt" (<1,8tr) của [S09] | | [S02], [S09] |
| 3 | Generic — thứ anh muốn dồn tiền vào — đang chạy **ROAS 1,25x** (GĐ1 = 0,00x, 0 cọc trên 200 triệu). CP/cọc Generic **135.598.800 ₫**, vượt trần ROAS 3,0x (60,3tr) **2,25 lần** | | [S02], B5 |
| 4 | Brand **đang bị bóp**: Impression Share chỉ **53,4%**, mất **39,7% IS do hết ngân sách**. Benchmark [S09] nói IS thương hiệu <60% = báo động, mất IS ngân sách >20% = "tiền đang bỏ lại trên bàn". Có ~121.948 lượt hiển thị người đang gõ tên dự án mà ta **không xuất hiện** | | [S02] |
| 5 | Chất lượng lead Brand cao nhất tài khoản: **67% dùng được**, chỉ 4% trùng SĐT (PMax: 7% dùng được, 31% trùng) | | [S08-C] |

**Về lập luận "khách đã biết mình rồi mới search tên dự án" — đây là lập luận đúng một nửa, và tôi phản biện bằng chính dữ liệu của mình, không bằng lý thuyết:**

[S10-D] cho thấy nếu đổi sang mô hình phân bổ dựa trên dữ liệu, Brand **mất 191 lead (−32,3%)** — tức **anh nói đúng: nhấp cuối đang phóng đại Brand khoảng một phần ba**. Nhưng sau khi trừ hết phần phóng đại đó, Brand vẫn còn **401/1.715 lead = 23,4%**, ngang bằng Generic (402) trong khi chỉ tiêu **38% ngân sách của Generic**. Brand *bớt* to, chứ không *hết* giá trị.

**Rủi ro nếu cắt — cũng có số:**
- [S05] không có bằng chứng ta độc quyền tên dự án. Nếu bỏ trống, đại lý F2 hoặc đối thủ mua tên "vinhomes hóc môn" (CTR 11,86%, CPC chỉ 12.057 ₫ — quá rẻ để đối thủ bỏ qua) và **hớt trọn khách đã được các kênh khác hâm nóng**. Ta đang chạy song song Facebook Ads, Zalo Ads, telesale [S01] — mọi đồng chi ở đó đều đổ về một truy vấn thương hiệu, và Brand Search là cái phễu hứng.
- Chi phí thử nghiệm để chứng minh: rất rẻ. **Nếu anh vẫn muốn kiểm chứng, tôi đề xuất thử nghiệm có kiểm soát 14 ngày** — tắt Brand ở 2 quận (ví dụ Bình Tân + Tân Phú, chiếm 11,9% chi phí [S06]), giữ nguyên 5 quận còn lại, đo lượng lead thương hiệu tự nhiên. Nếu lead không giảm, tôi sai và ta cắt. Chi phí thử nghiệm ≈ 0, thời gian 14 ngày. Cắt mù cả tài khoản để "thử" thì chi phí là 13 cọc = 2,28 tỷ doanh thu.

---

## D2. Đối thủ bắt đầu đấu giá trên tên thương hiệu dự án — 4 hành động

**Trước hết, xác nhận bằng số** (hiện dữ liệu **chưa đủ** để khẳng định đã bị tấn công): [S02] cho thấy Brand mất **6,9% IS do thứ hạng** — nhỏ so với 39,7% mất do ngân sách. CTR Brand 11,63% vẫn ở TB ngành ([S09]: 8–12%). **Cần thêm báo cáo Auction Insights** để biết ai đang cùng đấu giá và với tỷ lệ trùng lặp bao nhiêu — đây là dữ liệu duy nhất trả lời được câu hỏi này, và tài khoản chưa có.

### Trong Google Ads

| # | Hành động | Ngưỡng/chi tiết |
|---|---|---|
| 1 | **Nâng IS thương hiệu lên 95% bằng chiến lược Tỷ lệ hiển thị mục tiêu, vị trí đầu trang tuyệt đối** | Ưu tiên tuyệt đối: mất IS do ngân sách 39,7% là lỗ hổng tự tạo, phải bịt trước khi lo đối thủ. Ngân sách Brand 630tr (C1) chính là để làm việc này. CPC Brand hiện chỉ 13.663 ₫ — còn rất nhiều dư địa giá thầu trước khi chạm CP/cọc trần |
| 2 | **Tăng Điểm chất lượng cho nhóm Brand** để đối thủ phải trả đắt hơn ta nhiều lần | Hiện QS toàn TK **5,2/10**, trải nghiệm trang đích "Dưới trung bình" [S05]. Việc cụ thể: tách 31 từ khóa/nhóm xuống ≤15, viết 3 RSA/nhóm có tên dự án trong tiêu đề, LP `/nhan-bang-gia-2026` LCP 1,9s [S10-C] khớp thông điệp. Google định giá quảng cáo theo Ad Rank — QS cao là **hàng rào chi phí** rẻ nhất |
| 3 | **Bật tiện ích đầy đủ để chiếm diện tích SERP**: Cuộc gọi, Chú thích, Vị trí, Hình ảnh, Giá, Biểu mẫu KH tiềm năng | Hiện chỉ có 4 Liên kết trang web [S05]. Quảng cáo đối thủ trên tên dự án thường mỏng — chiếm nhiều dòng SERP đẩy họ xuống dưới |
| 4 | **Giám sát Auction Insights hằng tuần + cảnh báo CPC**: nếu CPC nhóm Brand tăng >2× baseline 7 ngày → alert ngay | Theo `playbook/monitoring.md` §2 (mức 🟡 "CPC tăng >2× baseline trên nhóm brand → đối thủ mới vào đấu giá? → check Auction Insights") |

### Ngoài Google Ads

| # | Hành động | Chi tiết |
|---|---|---|
| 5 | **Khiếu nại vi phạm nhãn hiệu với Google** | Nếu đối thủ dùng "Vinhomes" trong **văn bản quảng cáo** (không chỉ làm từ khóa), chủ sở hữu nhãn hiệu có thể nộp đơn khiếu nại — Google gỡ được phần văn bản. Ta là đại lý F1, cần phối hợp với chủ đầu tư để nộp. Việc này **miễn phí** và hiệu quả hơn mọi mức tăng giá thầu |
| 6 | **Chiếm kết quả tự nhiên cho truy vấn thương hiệu** | Bài SEO + Google Business Profile nhà mẫu + kênh chính chủ. Nếu vị trí tự nhiên #1 là của ta, quảng cáo đối thủ dù đứng trên vẫn bị chia sẻ nhấp. Đây là tài sản không thể bị đấu giá |
| 7 | **Bảo vệ danh tính bán hàng** | Hotline duy nhất, mã đại lý F1 hiển thị rõ trên LP, cảnh báo "cẩn trọng với đơn vị mạo danh". Cụm từ "vinhomes hóc môn có thật không" đã có **7.894 hiển thị, 26 lead, 13 triệu chi phí** [S04] — nhu cầu thẩm định đã tồn tại sẵn, đối thủ đấu giá thương hiệu sẽ làm nó tăng |
| 8 | **Không đấu giá trả đũa trên tên đối thủ** | Ta vừa có **bằng chứng 90 ngày** rằng chiến thuật này thất bại: 176.746.000 ₫ → 3 SQL → 0 cọc, 26% lead là môi giới [S08-C], [S02]. Trả đũa chỉ đẩy CPC của cả hai bên lên |

---

## D3. "PMax có chi phí/chuyển đổi thấp nhất, dồn tiền vào đó" — đồng ý hay không?

**Không đồng ý. Kế toán đang đọc đúng một cột và cột đó đang nói dối.**

| Chiến dịch | **CPL Ads (₫)** ← cột kế toán nhìn | **CP/SQL (₫)** | **CP/cọc (₫)** | Cọc | Doanh thu (₫) |
|---|---|---|---|---|---|
| **PMAX_VinhomesHM_Lead** | **267.817 (thấp nhất)** | **7.793.049** | — | **0** | **0** |
| SEA_Brand | 298.759 | **739.259** | **20.016.846** | **13** | 2.280.000.000 |
| GDN_Remarketing | 430.493 | 3.611.361 | — | 0 | 0 |
| YT_Video | 470.017 | 10.399.125 | — | 0 | 0 |
| SEA_Generic | 1.021.075 | 3.549.707 | 135.598.800 | 5 | 850.000.000 |
| SEA_Competitor | 5.701.484 | 58.915.333 | — | 0 | 0 |

**Xếp hạng đảo ngược hoàn toàn khi đổi thước đo.** PMax hạng 1 theo CPL Ads, hạng 5/6 theo CP/SQL, hạng cuối theo doanh thu.

**Vì sao CPL Ads của PMax thấp giả tạo — 3 lớp bằng chứng độc lập:**

1. **Mẫu số bị thổi phồng.** PMax báo 1.775 chuyển đổi nhưng CRM chỉ nhận 829 lead → tỷ lệ **2,14x**, vượt ngưỡng báo động 1,8x của [S09] và cao nhất tài khoản cùng YouTube. Trong 1.775 "chuyển đổi" đó có phần lớn 612 `view_price_page` + 361 `engaged_30s` — [S10-B] cho thấy PMax một mình đóng góp **438/612 view_price_page (71,6%)** và **259/361 engaged_30s (71,7%)**. Nói cách khác: **PMax gần như chỉ tạo ra "chuyển đổi" bằng hai sự kiện không phải lead.**
2. **Lưu lượng không có ý định.** [S10-B]: tỷ lệ tương tác **8,7%** (Brand 62,4%), thời gian tương tác TB **11 giây**, **1,09 trang/phiên**, cuộn 90% chỉ **4%**. [S11-B]: **74,3% thoát dưới 3 giây**, thời lượng phiên trung vị **3 giây**, ghi chú Clarity: "Bất thường — xem lại vị trí đặt quảng cáo".
3. **Lead không dùng được.** [S08-C] mẫu 160 lead: trùng SĐT **31%**, SĐT sai **24%**, sai phân khúc **34%**, **chỉ 7% dùng được**. → 829 × 7% = **58 lead thật**, chi phí/lead thật = **8.191.901 ₫** — đắt gấp **27 lần** con số 267.817 ₫ mà kế toán đang nhìn.

**Phép thử quyết định — chuyện gì xảy ra nếu làm theo đề xuất?**

Dồn toàn bộ 2,1 tỷ vào PMax với CP/SQL hiện tại 7.793.049 ₫ → **269 SQL**. Với tỷ lệ SQL→cọc của PMax = **0%** (0/61 SQL trong 90 ngày) → **0 cọc, 0 đồng doanh thu**. Ngay cả nếu giả định rộng rãi rằng PMax đạt tỷ lệ SQL→cọc trung bình tài khoản (2,76%), thì 269 SQL × 2,76% = **7,4 cọc** — bằng **23% của KPI 32 cọc**, và CP/SQL 7,79tr **vượt KPI 2,2tr gấp 3,5 lần**.

**Đề xuất của tôi thay vì đồng ý hoặc bác bỏ hoàn toàn:** giảm PMax từ 475tr xuống **210tr (−56%)**, **xây lại từ đầu sau khi sửa tín hiệu**: chỉ `generate_lead` là chuyển đổi chính, tCPA 1.500.000 ₫, brand exclusion BẬT (hiện CHƯA — [S05]), loại trừ vị trí đặt (hiện chưa thiết lập), tín hiệu đối tượng từ danh sách khách hàng CRM. Lý do không cắt hẳn: [S10-D] cho thấy theo mô hình dựa trên dữ liệu PMax vẫn giữ 466/1.715 lead — nó có đóng góp thật, chỉ là đang bị **đo sai và tối ưu sai**. Đánh giá lại ở ngày 60 với ngưỡng cứng: **0 cọc sau 60 ngày lũy kế = dừng hẳn**.

**Câu tôi sẽ nói với kế toán:** *"Cột anh đang nhìn tính cả người xem trang bảng giá 3 giây rồi thoát. PMax giỏi nhất tài khoản ở việc mua thứ đó. Ta không bán trang bảng giá, ta bán nhà."*

---

## D4. Ngân sách bị cắt còn 1,2 tỷ cho 90 ngày — cắt gì trước, giữ gì cuối

**Nguyên tắc:** cắt theo thứ tự **chi phí trên mỗi cọc**, không theo thứ tự chi phí trên mỗi chuyển đổi. Với 1,2 tỷ và trần ROAS 3,0x (60.333.333 ₫/cọc), cần **≥19,9 → 20 cọc**.

### Thứ tự cắt (căn cứ [S02] 90 ngày)

| Thứ tự | Cắt gì | Chi phí kỳ trước (₫) | Cọc mất | SQL mất | Lý do |
|---|---|---|---|---|---|
| **1** | **SEA_Competitor_DoiThu — cắt 100%** | 176.746.000 | **0** | 3 | CP/SQL 58.915.333 ₫ = 11,8 lần ngưỡng báo động. 6/6 cụm từ SQL=0 [S04] |
| **2** | **YT_Video_TVC_MoBan — cắt 100%** | 83.193.000 | **0** | 8 | Đầu phễu, hiệu quả không thể chứng minh trong 90 ngày với ngân sách hạn chế. [S10-D] cho thấy nó có đóng góp thật (165 lead theo data-driven) nhưng **đây là thứ xa xỉ khi bị cắt tiền** |
| **3** | **PMAX — cắt 100% (nguyên trạng)** | 475.376.000 | **0** | 61 | 0 cọc / 90 ngày. Với 1,2 tỷ không còn đủ dư địa để "xây lại và chờ học" |
| **4** | **GDN_Remarketing — cắt 100%** | 130.009.000 | **0** | 36 | 0 cọc. Nếu còn dư ngân sách cuối kỳ mới mở lại ở mức 20tr/GĐ (remarketing rẻ, CPC 4.487 ₫) |
| | **Cộng cắt được, KHÔNG mất một cọc nào** | **865.324.000 (48,0%)** | **0** | 108 | |
| **5** | **Cắt trong Generic**: 17 cụm từ SQL=0 + đối sánh rộng | ~419.729.000 (giao với trên) | 0 | 0 | Giữ lại chỉ đối sánh Chính xác + Cụm từ cho các cụm đã có SQL [S04] |
| **6** | **Cắt địa lý ngoài TP.HCM+BD+LA+ĐN** | 364.314.474 (giao với trên) | 0 | 46 | [S06] |
| **7** | **Cắt khung giờ 20:00–06:00 và giảm mạnh T7–CN** | 483.347.916 (giao) | ~1 | | [S07-A/C] — đây là chỗ đầu tiên bắt đầu **có** đau |

### Giữ đến cuối cùng (thứ tự ngược)

| Ưu tiên giữ | Hạng mục | Ngân sách 1,2 tỷ | Lý do |
|---|---|---|---|
| **Cuối cùng bị đụng đến** | **SEA_Brand — nhóm `Brand-Core` đối sánh Chính xác** | **450.000.000 ₫** | CP/cọc 20.016.846 ₫ = **rẻ nhất tài khoản 6,8 lần**. ROAS 8,76x. Đây là đồng tiền cuối cùng tôi tiêu |
| Áp chót | **Việc sửa đo lường (GTM/GA4) — chi phí ≈ 0 đồng ngân sách quảng cáo** | 0 ₫ | Không tiêu tiền media. Cắt cái này là **cắt thứ làm mọi đồng còn lại hiệu quả hơn**. Xem D6 |
| Áp chót | **Sửa lỗi JS trên form (Clarity #4)** | 0 ₫ | Thu hồi 280–340 lead/90 ngày mà không tốn một đồng quảng cáo nào (B7) |
| 3 | **SEA_Generic — chỉ AG `NhaPho-HocMon` + `CanHo-HocMon`, Chính xác/Cụm từ** | **450.000.000 ₫** | Là nguồn cọc thứ 2 (5 cọc). Cắt hết đối sánh rộng và các nhóm SQL=0 |
| 4 | **SEA_ChinhSach_TraGop** (mới, quy mô nhỏ) | **150.000.000 ₫** | Ý định cao, chưa khai thác, CPC dự kiến thấp hơn Generic |
| 5 | **Dự phòng** | **150.000.000 ₫** | Giữ để mở lại GDN Remarketing nếu Brand/Generic vượt kế hoạch |
| | **TỔNG** | **1.200.000.000 ₫** | |

**Dự phóng với 1,2 tỷ:** dồn 900tr vào Brand+Generic (2 kênh duy nhất có cọc). Nếu giữ được CP/cọc bình quân của 2 kênh này ở mức GĐ3 vừa qua (Brand 16.287.250 ₫, Generic 86.386.333 ₫ [S03]) và cải thiện Generic bằng cắt rác, mục tiêu khả thi là **20–24 cọc**, ROAS **3,0–3,6x**. **Nói thẳng: KPI 32 cọc là không đạt được với 1,2 tỷ** — cần đàm phán lại KPI xuống ≈20 cọc, hoặc chấp nhận rằng ROAS sẽ cao hơn (vì cắt rác) nhưng tổng doanh thu thấp hơn.

---

## D5. "GA4 báo 3.820, CRM báo 2.557. Ai đúng? Từ giờ tôi nên nhìn con số nào?" *(≤150 từ, ngôn ngữ phi kỹ thuật)*

> Cả hai đều đúng, nhưng chúng đếm hai thứ khác nhau.
>
> **3.820** là số **lượt thao tác trên website** — gồm 1.715 lượt điền form, 1.132 lượt bấm số điện thoại (một người bấm 3 lần tính thành 3), 612 lượt chỉ mở trang bảng giá rồi đóng, và 361 lượt ở lại trang trên 30 giây. Hai nhóm sau **không phải khách hàng**, họ chỉ ghé xem.
>
> **2.557** là số **người thật có số điện thoại** mà đội sale gọi được. Đây mới là khách.
>
> **Anh hãy nhìn ba con số này, theo thứ tự:**
> 1. **Số lead chất lượng (SQL)** — sale xác nhận đúng phân khúc, có nhu cầu thật.
> 2. **Chi phí trên mỗi lead chất lượng** — hiện 2,77 triệu, KPI là 2,2 triệu.
> 3. **Số cọc và ROAS** — hiện 18 cọc, ROAS 1,74x.
>
> Con số 3.820 tôi sẽ sửa để nó ngừng đếm nhầm. Sau khi sửa, nó sẽ tụt xuống — đó là dấu hiệu tốt, không phải xấu.

*(148 từ)*

---

## D6. "Sửa GTM không tạo ra lead nào, để cuối quý. Giờ tăng ngân sách trước"

### Phản biện — bằng số, không bằng nguyên tắc

**Lập luận 1 — tăng ngân sách hôm nay là đổ tiền qua một cái thước hỏng.** 34,7% cột "Chuyển đổi" không phải lead (973 sự kiện rác + 353 lượt đếm trùng, B6). Google Smart Bidding **học từ chính cột này**. [S12-C] viết thẳng: *"Máy học tối ưu theo tín hiệu rác — nguyên nhân gốc của toàn bộ vấn đề PMax"*. Bằng chứng thực nghiệm đã có sẵn trong tài khoản: PMax được cấp **475.376.000 ₫** — nhiều hơn Brand 1,8 lần — và cho ra **0 cọc**, vì bidding được dạy rằng "phiên 3 giây có mở trang bảng giá" là thành công. **Tăng ngân sách khi tín hiệu còn bẩn = nhân bản kết quả của PMax lên quy mô lớn hơn.**

**Lập luận 2 — sửa đo lường tạo ra lead, và tôi có con số.** Việc "sửa đo lường" trong danh sách của tôi không chỉ là gắn thẻ:
- Sửa lỗi JS `TypeError e.setDate` (form không gửi được trên Safari iOS, 4.196 phiên) → **280–340 lead**, trị giá 197–240 triệu ₫ theo CPL thực tế [S11-C, B7].
- Sửa CTA bị khung chat che + `tel:` chết → thêm **90–140 lead**.
- **Tổng: 370–480 lead trong 90 ngày mà không tốn thêm một đồng quảng cáo nào** — nhiều hơn số lead mà 260 triệu ngân sách Generic mua được.
- Bật `zalo_click` (894) và `file_download` (1.206) → **2.100 tín hiệu ý định** đang bị vứt đi [S10-E].

**Lập luận 3 — không sửa thì sự cố sẽ lặp lại, và ta đã trả giá một lần.** GTM v23 ngày 44 làm gãy đo lường **3 ngày**, mất **63 lead khỏi Ads/GA4 vĩnh viễn**, **59.528.000 ₫ chạy trong tình trạng bidding mù**, và mất 3 ngày mới phát hiện **chỉ vì không có cảnh báo chuyển đổi = 0** [S12-A #18]. Điều kiện kích hoạt vẫn đang gắn vào class CSS [S12-A #3] → **lần deploy giao diện tiếp theo sẽ gây lại đúng sự cố này**. Cảnh báo mất **2 giờ** để cài.

**Lập luận 4 — "để cuối quý" nghĩa là mất luôn quý này.** Chuyển đổi ngoại tuyến cần **30 ngày dữ liệu** trước khi Smart Bidding dùng được. Cài GCLID ở ngày 1 → tCPA theo chất lượng lead chạy từ ngày 45. Cài ở ngày 60 → tối ưu theo chất lượng **không kịp diễn ra trong 90 ngày này**. Đây không phải việc trì hoãn được rồi làm bù.

**Lập luận 5 — chi phí thực của việc sửa.** Ước lượng: 3–5 ngày công dev + 2 ngày công marketing. **Không tiêu một đồng ngân sách media nào.** Đổi lại là 370–480 lead + xóa 459 triệu chi phí đang chảy vào tín hiệu rác. Không có hạng mục nào trong kế hoạch 2,1 tỷ có tỷ lệ hoàn vốn gần bằng.

### Nếu buộc phải nhượng bộ — giữ lại đúng HAI hạng mục

| # | Hạng mục giữ | Vì sao là hai cái này | Công sức | Giá trị đo được |
|---|---|---|---|---|
| **1** | **Gỡ `view_price_page` và `engaged_30s` khỏi cột Chuyển đổi + khử trùng `click_to_call`** (chuyển cả 3 sang "Phụ") | Đây là **thao tác cấu hình trong giao diện GA4/Google Ads, KHÔNG cần dev**, làm xong trong **30 phút**. Nó gỡ **34,7% tín hiệu rác** đang dạy Smart Bidding sai — tức là nó **quyết định mọi đồng ngân sách tăng thêm sẽ chảy đi đâu**. Nếu sếp muốn tăng ngân sách, đây chính xác là việc phải làm trước để tiền tăng thêm không lặp lại kết cục của PMax | 30 phút, 0 dev | Chuyển đổi từ 3.820 → 1.715 (chỉ còn lead thật); chênh Ads/CRM 1,49x → ~1,1x |
| **2** | **Cài biến ẩn lưu GCLID vào form + cảnh báo chuyển đổi = 0** | GCLID: **2 giờ dev**, nhưng là **cửa một chiều có thời hạn** — lead thu về trong lúc chưa có GCLID thì vĩnh viễn không import ngược được vào Ads. Mỗi ngày trì hoãn là mất vĩnh viễn dữ liệu chất lượng của ngày đó (kỳ trước: 651 SQL và 18 cọc **đã mất trắng** khả năng dạy cho bidding). Cảnh báo: **2 giờ**, đã chứng minh đáng giá 59.528.000 ₫ ở sự cố N44–46 | 4 giờ dev | ≥85% lead có GCLID; sự cố đo lường phát hiện trong ≤4h thay vì 3 ngày |

**Việc tôi sẵn sàng hoãn tới cuối quý:** dọn 34 thẻ GTM, Consent Mode v2, gắn Clarity ID vào CRM, đo lường phía máy chủ (cái cuối cùng thì tôi **đề nghị không làm** — chưa có bằng chứng mất >20% chuyển đổi do ad blocker, chưa đủ điều kiện mở theo `tracking/README.md`).

**Câu chốt với đội IT:** *"Hai việc, sáu tiếng, không đụng vào giao diện. Đổi lại: quảng cáo ngừng học từ dữ liệu rác, và lần sau các anh deploy làm gãy đo lường thì hệ thống báo trong 4 tiếng chứ không phải 3 ngày. Ba ngày lần trước tốn 59,5 triệu."*

---

# PHẦN E — KẾ HOẠCH 7 NGÀY ĐẦU

Nguyên tắc sắp thứ tự: **(1) cầm máu chi phí đang chảy → (2) sửa thước đo → (3) thu hồi lead đang bị chặn → (4) mở van nơi sinh lời.** Việc rẻ và nhanh nhất mà chặn được nhiều tiền nhất làm trước.

| # | Ngày | Việc | Cách làm cụ thể | Kết quả kỳ vọng ĐO ĐƯỢC | Nguồn |
|---|---|---|---|---|---|
| **1** | **N1 (sáng)** | **Dừng chiến dịch SEA_Competitor_DoiThu** | Tạm dừng campaign, chuyển ngân sách sang Brand | Giải phóng **~1.964.000 ₫/ngày** (176.746.000/90). Mất **0 cọc, 0 doanh thu** — 90 ngày qua đã chứng minh | [S02], [S04] |
| **2** | **N1 (sáng)** | **Gỡ `view_price_page` + `engaged_30s` khỏi chuyển đổi chính; `click_to_call` → Phụ** | GA4 → Sự kiện → bỏ đánh dấu; Ads → Chuyển đổi → chuyển sang "Phụ" | Cột Chuyển đổi giảm **~25,5% trong 24h** (từ ~42 xuống ~31/ngày), sau đó về ~19/ngày khi chỉ còn `generate_lead`. Chênh Ads/CRM 1,49x → mục tiêu ≤1,15x trong 7 ngày. **Báo trước ban giám đốc bằng văn bản.** | [S10-A/E], [S12-C] |
| **3** | **N1 (chiều)** | **Siết nhắm mục tiêu địa lý + tùy chọn vị trí** | Đổi từ "Việt Nam toàn quốc" → TP.HCM + Bình Dương + Long An + Đồng Nai; đổi "Hiện diện HOẶC quan tâm" → **chỉ "Hiện diện"**; loại trừ Hà Nội, Đà Nẵng, ĐBSCL, ngoài VN | Giải phóng **364.314.474 ₫/90 ngày ≈ 4.048.000 ₫/ngày**, mất **0 cọc** (4 khu vực này có 46 SQL, 0 cọc) | [S05], [S06] |
| **4** | **N1 (chiều)** | **Nạp danh sách phủ định chia sẻ ≥120 từ + tắt Search Partners + tắt Mạng hiển thị trong CD Search** | Tạo danh sách chia sẻ, áp cho cả 6 CD. Ưu tiên 20 từ ở mục C2 | Chặn **~419.729.000 ₫/90 ngày ≈ 4.664.000 ₫/ngày** chi cho cụm từ SQL=0. Đo lại sau 7 ngày: trong tổng 1.114.962.000 ₫ chi phí cụm từ được báo cáo [S04], phần chảy vào cụm có SQL>0 phải tăng từ **62,4% lên >90%** | [S04], [S05] |
| **5** | **N2** | **Tăng ngân sách Brand từ ~2,9tr → 6,0tr/ngày, đổi giá thầu sang Tỷ lệ hiển thị mục tiêu 90%** | Dùng chính tiền vừa giải phóng ở việc 1+3+4 (~10,7tr/ngày) | **Mất IS do ngân sách: 39,7% → <15% trong 7 ngày**; IS thương hiệu 53,4% → >75%. Lead Brand/ngày từ 9,5 → ≥15 | [S02] |
| **6** | **N2–N3** | **Sửa lỗi JS `TypeError e.setDate` — bỏ trường chọn ngày hẹn xem nhà khỏi form** | Việc dev nhỏ nhất giải quyết được lỗi lớn nhất. Sale hỏi lịch hẹn qua điện thoại | Tỷ lệ phiên có lỗi JS trên di động (Clarity): **8,9% → <2%**. Tỷ lệ hoàn tất form di động: 24,6% → ≥30%. Thu hồi **280–340 lead/90 ngày ≈ 3,1–3,8 lead/ngày** | [S11-A/C], B7 |
| **7** | **N3** | **Cài cảnh báo "chuyển đổi = 0 trong 4h có chi tiêu" + cảnh báo CPC brand tăng >2× baseline** | Google Ads Script hoặc quy tắc tự động → Telegram/email | Test giả lập 1 lần: alert bắn trong ≤4h. **Ngăn lặp lại sự cố N44–46** (3 ngày, 59.528.000 ₫ chạy mù, 63 lead mất) | [S12-A #18], [S12-B] |
| **8** | **N3–N4** | **Cài biến ẩn lưu `gclid`/`gbraid`/`wbraid`/`utm_*` vào form + bật Enhanced Conversions** | Dùng skill `ad-click-attribution`; đồng thời đổi trigger `generate_lead` từ class CSS sang `dataLayer.push` | **≥85% lead mới trong CRM có gclid trong vòng 7 ngày** (hiện 0%). Enhanced Conversions trạng thái "Đang ghi nhận". Mở khóa toàn bộ lộ trình ECL → tCPA theo chất lượng ở ngày ~45 | [S05], [S12-A #14/#15], `tracking/README.md` |
| **9** | **N4–N5** | **Điều chỉnh lịch chạy + thiết bị + tạo `Data exclusion` cho N41–47 của kỳ trước** | Tắt 23:00–06:00; giảm giá thầu −30% khung 20:00–23:00, −40% T7–CN; máy tính +25%, máy tính bảng −20%. Data exclusion backdate cho campaign Smart Bidding | Chuyển **~5.370.000 ₫/ngày** từ khung giờ CP/SQL 3,0–4,1tr sang khung 09–17h CP/SQL 2,5–2,6tr. Tỷ lệ lead được gọi lại <30 phút: 30% → **≥60%**. Lead cuối tuần/ngày: 27,8 → ≤24 (vừa đúng năng lực 2 sale) | [S07-A/B/C], `playbook/monitoring.md` §2.1 |
| **10** | **N5–N7** | **Họp chốt SLA phản hồi lead với trưởng phòng kinh doanh + dựng báo cáo đối chiếu 3 nguồn hằng ngày** | SLA: gọi lại <15 phút giờ hành chính (GĐ3 vừa qua đã làm được — trung vị 47 phút), phân lead tự động, không lead nào quá 12h không ai gọi. Báo cáo: Ads / GA4 / CRM cùng một bảng, chênh lệch tự tính | **Đây là việc có giá trị tiền lớn nhất tuần: +13,1 cọc = 2.376.312.800 ₫ nếu đưa được 47% lead đang >2h về nhóm <30 phút.** Chỉ tiêu tuần: 0 lead bị bỏ sót (kỳ trước 275 lead), tỷ lệ gọi trong ngày từ 79% → 95%. Báo cáo đối chiếu: chênh từng cặp nguồn ≤10% | [S08-A/B], A1 |

### Bảng tổng kết tác động Tuần 1

| Nhóm việc | Chi phí giải phóng/chuyển hướng (₫/ngày) | Lead thu hồi | Doanh thu tác động (90 ngày) |
|---|---|---|---|
| Việc 1, 3, 4 — cắt lãng phí | **~10.676.000/ngày** (= 960,8tr/90 ngày) | — | Giữ nguyên 0 cọc bị mất |
| Việc 5 — mở van Brand | Tái đầu tư 3,1tr/ngày | +5,5 lead/ngày | +876tr – 1,75 tỷ `[ƯỚC TÍNH]` |
| Việc 6 — sửa lỗi JS | 0 | +3,1–3,8 lead/ngày | +471 – 612tr `[ƯỚC TÍNH]` |
| Việc 9 — lịch chạy | Chuyển hướng 5,37tr/ngày | — | Hiệu suất CP/SQL −18% |
| Việc 10 — SLA sale | 0 | — | **+2,38 tỷ** `[ƯỚC TÍNH]` |
| Việc 2, 7, 8 — nền đo lường | 0 | — | Không tạo doanh thu trực tiếp; **quyết định chất lượng phân bổ của toàn bộ 2,1 tỷ** |

**Việc KHÔNG làm trong tuần 1 (có chủ đích):** không tăng tổng ngân sách tài khoản, không xây PMax mới, không đổi mô hình phân bổ, không chạy A/B test LP mới. Lý do: mọi thay đổi lớn về cấu trúc hoặc giá thầu trong khi tín hiệu chuyển đổi vừa bị thay đổi (việc #2) sẽ trộn lẫn nguyên nhân và làm không đọc được kết quả — đồng thời các campaign Smart Bidding đang vào lại learning phase (`playbook/monitoring.md` §2, Learning phase guard).

---

## PHỤ LỤC — Những chỗ dữ liệu KHÔNG ĐỦ để kết luận

| # | Câu hỏi chưa trả lời được | Cần thêm dữ liệu gì |
|---|---|---|
| 1 | Đối thủ nào đang đấu giá tên thương hiệu, mức trùng lặp bao nhiêu? (6,9% mất IS do thứ hạng là do ai) | **Auction Insights** 90 ngày cho campaign Brand |
| 2 | Thiệt hại thật của lỗi Safari iOS là bao nhiêu (thay vì ước tính 280–340 của đội UX)? | GA4: tỷ lệ `form_start` → `generate_lead` **tách theo trình duyệt/OS**; số phiên có `form_start` + lỗi JS nhưng không có `generate_lead` |
| 3 | PMax đang hiển thị ở đâu (74,3% thoát <3 giây từ vị trí đặt nào)? | Báo cáo **vị trí đặt (placement)** của PMax + báo cáo nhóm nội dung |
| 4 | Smart Bidding đã bị hại bao nhiêu do sự cố N44–46 không khai data exclusion? | Lịch sử thay đổi cấp campaign trong Ads; hiệu suất theo tuần trước/sau N47 tách riêng theo campaign dùng Smart Bidding |
| 5 | 5.743 người bỏ dở form (form_start 7.458 − generate_lead 1.715) bỏ ở trường nào trên **LP v2**? | Clarity ghi hình phân tách theo trường form của v2 (sheet 11 chỉ có chi tiết trường của v1) |
| 6 | Các kênh khác (Facebook, Zalo, telesale, sàn F2) đóng góp bao nhiêu vào 18 cọc? | Dữ liệu nguồn lead của CRM theo kênh — [S01] nói rõ các kênh này chạy song song nhưng **KHÔNG nằm trong dữ liệu này**. Điều này có nghĩa: **một phần trong 18 cọc quy cho Google Ads có thể là đa chạm** |
| 7 | Tỷ lệ SQL→cọc còn cải thiện được tới đâu? | Dữ liệu năng lực từng sale, kịch bản gọi, tỷ lệ chốt theo cá nhân — [S08] chỉ có dữ liệu tổng |
| 8 | 3 thẻ "đối tác sàn F2" và thẻ "Zalo Tracking" đang gửi dữ liệu đi đâu? | Rà soát mã nguồn thẻ trong GTM + xác nhận với đội IT. [S12-A] ghi "Không rõ nguồn gốc — cần rà soát bảo mật" |

---

*Hết báo cáo. Mọi con số truy ngược được về `answers/agent-5-calc.py`; script có khối `assert` self-check xác nhận khớp với sheet 02 / 03 / 10.*
