# BÀI THI PERFORMANCE MARKETING LEAD — VINHOMES HÓC MÔN
**Thí sinh:** Agent 1 · **Vai:** Performance Marketing Lead, An Phát Land
**Dữ liệu:** 02/03/2026 – 30/05/2026 (90 ngày × 6 chiến dịch, 486 dòng) + 13 sheet bộ đề
**Toàn bộ số trong bài truy ngược được về:** `answers/agent-1-calc.py` (chạy: `python3 agent-1-calc.py`)

---

## TÓM TẮT ĐIỀU HÀNH (đọc 60 giây)

| Chỉ số 90 ngày qua | Thực tế | KPI 90 ngày tới | Khoảng cách |
|---|---|---|---|
| Chi phí | 1.803,5 tr | ≤ 2.100 tr | +16,4% ngân sách |
| Đặt cọc | 18 | ≥ 32 | **×1,78** |
| Doanh thu HH | 3.130 tr | ≥ 6.300 tr (ROAS 3,0) | **×2,01** |
| ROAS | **1,74x** | ≥ 3,0x | **+72%** |
| CP/cọc | 100,2 tr | ≤ 60,3 tr | **−40%** |
| CP/SQL | 2,77 tr | ≤ 2,20 tr | −21% |

**Ba câu kết luận:**
1. Tài khoản không thiếu ngân sách — nó **đang phân bổ ngược**. 40,4% chi phí (728,9 tr: PMax 475,4 + Competitor 176,7 + YouTube 83,2) tạo ra **0 cọc, 0 đồng doanh thu**; trong khi chiến dịch duy nhất có ROAS 8,76x (Brand) bị bóp còn 14,4% chi phí và **mất 40,1% impression share vì hết ngân sách**.
2. Nguyên nhân gốc là **đo lường sai**, không phải kỹ năng chạy ads: 1.263/3.820 chuyển đổi (33,1%) là ảo (973 sự kiện rác + 353 lượt gọi đếm trùng). Máy học Smart Bidding của PMax đã học suốt 90 ngày theo tín hiệu rác đó.
3. Đòn bẩy lớn nhất **không tốn tiền quảng cáo**: 47% lead được gọi lại sau 2 giờ; đẩy tốc độ phản hồi lên một bậc cho mỗi nhóm ⇒ **+9,3 cọc ≈ +1.678 tr hoa hồng** mà không tăng một đồng chi phí (sheet 08A).

---

# PHẦN A — CHẨN ĐOÁN

15 vấn đề, sắp theo **tác động tài chính giảm dần**. Ký hiệu: **[ĐL]** = nhóm đo lường/kỹ thuật (yêu cầu tối thiểu 3 — bài này có 6: A3, A8, A9, A11, A12, A15).

---

### A1 — Chiến dịch Brand bị bóp ngân sách, mất 40,1% impression share vì hết tiền
**Mức độ: CAO — bỏ lỡ ước tính ~1.767 tr hoa hồng**

| Bằng chứng | Số | Nguồn |
|---|---|---|
| Impression Share Brand (bình quân gia quyền theo hiển thị, 90 ngày) | **53,4%** | sheet 02 cột `Impr_Share`, lọc `SEA_Brand_Vinhomes_HocMon` |
| Mất IS do **ngân sách** (gia quyền theo chi phí) | **40,1%** | sheet 02 cột `Mat_IS_NganSach` |
| Ngưỡng benchmark | IS tốt > 85%; mất IS ngân sách > 20% = "tiền bỏ lại trên bàn" | sheet 09 |
| Ngân sách/ngày Brand | 2,0 → 2,5 → 4,5 tr/ngày (CPC thủ công) | sheet 05 |
| Hiệu quả Brand | Chi 260,2 tr → 13/18 cọc toàn tài khoản, DT 2.280 tr, **ROAS 8,76x**, CP/SQL 0,74 tr | sheet 02 |

Mất IS ngân sách ổn định cả 3 giai đoạn (GĐ1 39,1% · GĐ2 43,8% · GĐ3 38,4%) ⇒ không phải sự cố nhất thời, là **trần ngân sách đặt sai suốt 90 ngày**.

**Ước tính bỏ lỡ:** ngoại suy tuyến tính theo tỷ lệ IS mất/IS có (40,1%/53,4% = 0,751): +643 lead, **+9,8 cọc ≈ +1.767 tr HH**, tốn thêm ~195 tr ⇒ **ROAS biên ~9,0x**.
*Cảnh báo giả định:* phép ngoại suy này **giả định tuyến tính** (lead/cọc tăng cùng tỷ lệ với impression thu thêm). Thực tế đấu giá có lợi suất giảm dần, nên coi 9,8 cọc là **cận trên**; cận dưới thận trọng ~5–6 cọc. Cần dữ liệu Auction Insights + Bid Simulator để chốt chính xác — **hiện chưa có trong bộ đề**.

---

### A2 — 47% lead được gọi lại sau 2 giờ; 275 lead không ai gọi
**Mức độ: CAO — bỏ lỡ ~1.678 tr HH, không tốn thêm đồng quảng cáo nào**

| Thời gian gọi lại lần đầu | Số lead | % | Tỷ lệ liên hệ được | Tỷ lệ đặt cọc |
|---|---|---|---|---|
| Dưới 5 phút | 281 | 11% | 87% | **1,82%** |
| 5 – 30 phút | 485 | 19% | 74% | 1,21% |
| 30 phút – 2 giờ | 588 | 23% | 58% | 0,58% |
| 2 – 12 giờ | 536 | 21% | 41% | 0,21% |
| Trên 12 giờ | 664 | **26%** | 22% | **0,04%** |

*Nguồn: sheet 08 mục A, 90 ngày.*

- Cọc kỳ vọng theo cấu trúc hiện tại = **15,8** (khớp với 18 cọc thực tế trong sheet 02 ⇒ mô hình đáng tin).
- **Kịch bản thực tế** (mỗi nhóm dịch lên 1 bậc SLA, không cần gọi 100% dưới 5 phút): **25,1 cọc → +9,3 cọc ≈ +1.678 tr HH**.
- Trần lý thuyết (100% gọi <5 phút): 46,5 cọc — nêu để tham chiếu, **không dùng làm mục tiêu**.
- Lead bị bỏ sót hoàn toàn: 118 + 96 + 61 = **275 lead** (sheet 08B) × CPL CRM 705k = **194 tr đã trả tiền rồi vứt**.
- Năng lực **không phải nút thắt**: 2.557 lead / (8 sale × 12 lead × 90 ngày = 8.640) = **29,6% công suất**. Vấn đề là quy trình phân lead, không phải nhân sự.

---

### A3 [ĐL] — Bốn hành động chuyển đổi, trong đó hai cái không phải khách hàng tiềm năng
**Mức độ: CAO — nguyên nhân gốc kéo theo A4; trực tiếp làm hỏng tối ưu trên 475,4 tr chi phí PMax**

| Sự kiện | Số lượt 90 ngày | Là KHTN? | Đang tính vào cột Chuyển đổi? |
|---|---|---|---|
| `generate_lead` | 1.715 | Có | Có ✔ |
| `click_to_call` (lượt) | 1.132 | Có, **nhưng đếm trùng** (779 người thật) | Có ⚠ |
| `view_price_page` | 612 | **KHÔNG** | Có ✘ |
| `engaged_30s` | 361 | **KHÔNG** | Có ✘ |

*Nguồn: sheet 10 mục A & E; sheet 12 mục A thẻ #5, #6, #8; sheet 05 "Hành động tính vào cột Chuyển đổi #3, #4".*

- **1.263/3.820 = 33,1% tín hiệu chuyển đổi là ảo** (973 rác + 353 trùng).
- Sai từ **v18, trước ngày 1** (sheet 12B: "Chuyển đổi bị thổi phồng ngay từ ngày đầu tiên") ⇒ toàn bộ 90 ngày Smart Bidding học sai.
- Sheet 12C ghi thẳng: *"Máy học tối ưu theo tín hiệu rác — nguyên nhân gốc của toàn bộ vấn đề PMax"*.
- Đồng thời **2 tín hiệu thật đang bị bỏ ngoài**: `zalo_click` 894 lượt và `file_download` (bảng giá PDF) 1.206 lượt — có dữ liệu từ ngày 71 nhưng chưa đánh dấu sự kiện chính, chưa nhập vào Ads (sheet 12B v26, sheet 10E).

---

### A4 — PMax đốt 475,4 tr (26,4% ngân sách), 0 cọc, ROAS 0
**Mức độ: CAO — lãng phí ~442 tr (93% chi phí)**

| Chỉ số PMax | Giá trị | Đối chiếu |
|---|---|---|
| Chi phí | **475,4 tr** (26,4% tài khoản) | sheet 02 |
| Chuyển đổi Ads / Lead CRM | 1.775 / 829 = **2,14x** | benchmark báo động > 1,8x (sheet 09) |
| SQL | 61 → **SQL/Lead 7,4%** | benchmark báo động < 12% (sheet 09) |
| Cọc / Doanh thu | **0 / 0 đ** | sheet 02 |
| CP/SQL | **7,79 tr** | KPI ≤ 2,20 tr → vượt **3,5×** |
| Thoát nhanh < 3 giây | **74,3%**, phiên trung vị **3 giây** | sheet 11B — "Bất thường, xem lại vị trí đặt" |
| Hao hụt nhấp → phiên | **28,0%** (39.701 nhấp → 28.585 phiên) | sheet 10B; Brand chỉ 9,0% |
| Lead dùng được | **7%** (trùng SĐT 31%, SĐT sai 24%, sai phân khúc 34%) | sheet 08C, mẫu 160 lead |
| Cấu hình | Tối đa hóa chuyển đổi, **không đặt tCPA**; chưa loại trừ vị trí đặt; **chưa bật brand exclusion** | sheet 05 |

**Lãng phí ước tính = 475,4 × 93% ≈ 442 tr.** Riêng 11.116 nhấp trả tiền không tạo được phiên GA4 × CPC 11.974đ = **133 tr** trả cho lưu lượng không bao giờ tới trang.

---

### A5 — 71% chi phí Search chạy đối sánh rộng; 243 tr đổ vào truy vấn lạc hoàn toàn
**Mức độ: CAO — lãng phí xác định được 243 tr, tổng vùng nghi ngờ 420 tr**

| Bằng chứng | Số | Nguồn |
|---|---|---|
| Tỷ trọng chi phí đối sánh rộng | **71%** chi phí Search | sheet 05 |
| Tỷ trọng đối sánh chính xác | 9% | sheet 05 |
| Số từ khóa phủ định toàn tài khoản | **12 từ**, không dùng danh sách chia sẻ | sheet 05 |
| Cụm từ có 0 SQL | **17/32 cụm**, chi **420 tr = 23,3% tài khoản** | sheet 04 |
| Cụm từ **lạc hoàn toàn** (11 cụm) | chi **243 tr**, 96 lead, **0 SQL** | sheet 04 |
| Điểm chất lượng bình quân | **5,2/10**, trải nghiệm trang đích "Dưới trung bình" | sheet 05 |

11 cụm lạc: `giá đất hóc môn 2026` (33,9 tr) · `bản đồ quy hoạch hóc môn` (27,1 tr) · `thuê nhà nguyên căn hóc môn` (27,1 tr) · `bán đất thổ cư hóc môn 100 triệu` (27,1 tr) · `nhà trọ hóc môn giá rẻ` (20,3 tr) · `cho thuê kho xưởng hóc môn` (20,3 tr) · `việc làm bất động sản hóc môn` (20,3 tr) · `nhà đất hóc môn lừa đảo` (20,3 tr) · `chung cư mini gò vấp` (20,3 tr) · `vinhomes hóc môn tuyển dụng` (15,6 tr) · `vinschool hóc môn học phí` (10,4 tr).

Đây là các nhóm ý định **thuê / tuyển dụng / trường học / đất giá 100 triệu** — không thể là khách mua nhà 6,8–11,5 tỷ. CPC Generic 33.070đ (benchmark: >60k báo động, 25–45k trung bình — nằm ở nửa trên) trong khi 31 từ khóa/nhóm quảng cáo, 1 mẫu RSA (sheet 05) ⇒ độ liên quan thấp là hệ quả cấu trúc.

---

### A6 — 364 tr (20,2%) chi ở khu vực ngoài tệp khách hàng, 0 cọc
**Mức độ: CAO — lãng phí ~364 tr**

| Khu vực | % chi phí | Chi phí | SQL | Cọc | CP/SQL |
|---|---|---|---|---|---|
| Hà Nội | 8,6% | 155,1 tr | 20 | **0** | 7,76 tr |
| Đà Nẵng | 4,8% | 86,6 tr | 7 | **0** | **12,37 tr** |
| Cần Thơ & ĐBSCL | 5,2% | 93,8 tr | 12 | **0** | 7,82 tr |
| Ngoài Việt Nam "quan tâm đến VN" | 1,6% | 28,9 tr | 7 | **0** | 4,12 tr |
| **Cộng 4 khu vực** | **20,2%** | **364,4 tr** | **46** | **0** | — |
| *Lõi TP.HCM (7 khu vực)* | 59,7% | 1.077 tr | **482** | **17** | **2,23 tr** |

*Nguồn: sheet 06.* Nguyên nhân cấu hình: **nhắm "Việt Nam toàn quốc" + tùy chọn vị trí "Hiện diện HOẶC quan tâm" (mặc định), không loại trừ vị trí nào** (sheet 05). CP/SQL Đà Nẵng 12,37 tr = **5,5× KPI**. Tệp mục tiêu trong sheet 01 chỉ gồm TP.HCM + Bình Dương + Long An.

---

### A7 — Chiến dịch Competitor: 176,7 tr, 3 SQL, 0 cọc
**Mức độ: CAO — lãng phí 176,7 tr (9,8% ngân sách)**

| Chỉ số | Giá trị | Đối chiếu benchmark (sheet 09) |
|---|---|---|
| Chi phí | 176,7 tr | — |
| Lead CRM / SQL / Cọc | 32 / **3** / **0** | — |
| CPL CRM | **5,52 tr** | báo động > 1,5 tr → vượt **3,7×** |
| CP/SQL | **58,92 tr** | báo động > 5 tr → vượt **11,8×** |
| CPC | **55.164đ** | báo động > 60k, sát ngưỡng |
| CTR | 2,39% | Search generic báo động < 2% |
| Thoát nhanh < 3s | **34,1%**, phiên trung vị 47s | sheet 11B: "Ý định thấp" |
| Là môi giới/đối thủ trong lead | **26%** | sheet 08C |
| Lead dùng được | **26%** | sheet 08C |

Chi 176,7 tr trong 90 ngày để mua 3 SQL. GĐ3 đã tự giảm còn 33,9 tr nhưng vẫn 0 SQL, 0 cọc.

---

### A8 [ĐL] — Lỗi JS Safari iOS + 2 lỗi UI khác CHƯA SỬA, vẫn đang chảy máu lead
**Mức độ: CAO — 370–480 lead/90 ngày = 261–339 tr chi phí, tương đương 2,6–3,4 cọc ≈ 471–612 tr HH**

| # | Điểm ma sát | Phiên ảnh hưởng | Lead mất (ước tính đội UX) | Trạng thái |
|---|---|---|---|---|
| 4 | `TypeError e.setDate is not a function` (bộ chọn ngày hẹn xem nhà), Safari iOS 17.x — **form không gửi được, không báo lỗi cho khách** | **4.196** | 280 – 340 | **CHƯA SỬA** |
| 5 | Nút "Đăng ký nhận bảng giá" bị khung chat che ở màn hình < 380px | 2.741 | 60 – 90 | **CHƯA SỬA** |
| 6 | Hotline dạng `tel:` — người dùng máy tính bấm không phản hồi, 1.847 nhấp chết | 1.204 | 30 – 50 | **CHƯA SỬA** |

*Nguồn: sheet 11 mục C.* Bằng chứng độc lập xác nhận lỗi #4 vẫn sống: **tỷ lệ phiên có lỗi JS trên di động không giảm sau khi lên LP v2 — 9,3% → 8,9%** (sheet 11A), trong khi mọi chỉ số ma sát khác giảm mạnh (rage click 18,7% → 3,1%). Chi tiết bóc tách số đo vs ước tính ở **B7**.

---

### A9 [ĐL] — GTM v23 làm gãy thẻ `generate_lead`, 3 ngày chạy mù, mất 63 lead khỏi hệ thống
**Mức độ: TRUNG BÌNH-CAO — 59,5 tr chạy mù + hỏng tín hiệu học máy + 63 lead vĩnh viễn không truy vết được**

| Bằng chứng | Số | Nguồn |
|---|---|---|
| GTM v23, **ngày 44, 09:12**, dev@ đổi class `.form-dk-v1` → `.form-register` | điều kiện kích hoạt ngừng khớp | sheet 12B |
| Chuyển đổi Ads ngày 44–46 | **0** (ngày 43 = 43, ngày 47 = 33) | sheet 02, xác minh bằng script |
| Lead CRM ngày 44–46 | **63** (lead vẫn về, chỉ là hệ đo không thấy) | sheet 02 |
| Chi phí 3 ngày đó | **59,5 tr** chạy trong trạng thái mù | sheet 02 |
| Thời gian phát hiện | **3 ngày** (v24 sửa ngày 47, 14:38) | sheet 12B |
| Nguyên nhân chậm phát hiện | **KHÔNG CÓ cảnh báo khi chuyển đổi = 0** | sheet 12A mục #18 |

Rủi ro hệ thống: điều kiện kích hoạt **dựa trên class CSS** (sheet 12A thẻ #3) ⇒ mọi lần dev đổi giao diện đều có thể lặp lại sự cố này.

---

### A10 — Trang đích v1 chạy 57/90 ngày với LCP 4,8s và form 7 trường
**Mức độ: TRUNG BÌNH-CAO — mất ~374 lead ≈ 264 tr chi phí / 476 tr HH (đã xảy ra, đã khắc phục)**

| | v1 (ngày 1–57) | v2 (ngày 58–90) | Chênh |
|---|---|---|---|
| LCP | **4,8 s** (benchmark báo động > 4s) | 1,9 s | −60% |
| Form | 7 trường (có CMND/CCCD) | 3 trường | — |
| Tỷ lệ hoàn tất form | **20,4%** | **28,0%** | **+37,3%** |
| Tỷ lệ tương tác | 34,2% | 58,7% | +71,6% |
| Cuộn 90% | 16% | 37% | +131% |
| Rage click di động | 18,7% | 3,1% | −83% |
| Dead click di động | 24,1% | 6,2% | −74% |

*Nguồn: sheet 10 mục C, sheet 11 mục A, sheet 05.* Nếu v1 đạt tỷ lệ hoàn tất của v2: 4.912 form_start × 28,0% = 1.376 lead thay vì 1.002 ⇒ **mất 374 lead** × CPL 0,71 tr = **264 tr**; quy ra cọc (tỷ lệ Lead→Cọc 0,704%) ≈ **2,6 cọc ≈ 476 tr HH**.

Bài học vận hành: **không có A/B test nào chạy** (sheet 05: "Số phiên bản đang chạy A/B: 1"). Cải tiến 37% này lẽ ra phát hiện được trong tuần 2 chứ không phải tuần 9.

---

### A11 [ĐL] — Không lưu GCLID trong CRM ⇒ không thể nhập chuyển đổi ngoại tuyến
**Mức độ: CAO (chi phí cơ hội cấu trúc) — khóa toàn bộ khả năng tối ưu theo cọc**

| Hạng mục | Trạng thái | Hệ quả |
|---|---|---|
| Biến ẩn lưu GCLID vào form | **CHƯA CÀI** | Không thể nhập chuyển đổi ngoại tuyến |
| Nhập chuyển đổi ngoại tuyến từ CRM | **CHƯA triển khai** | Ads không bao giờ biết lead nào thành cọc |
| Enhanced Conversions | **TẮT** | Mất 10–20% khả năng khớp |
| Consent Mode v2 | **CHƯA CẤU HÌNH** | Mất dữ liệu mô hình hóa |
| Vùng chứa phía máy chủ | **KHÔNG CÓ** | Phụ thuộc hoàn toàn trình duyệt + ad blocker |

*Nguồn: sheet 12A #14–17, sheet 12C, sheet 05.*

Đây là lý do **cấu trúc** khiến toàn bộ tài khoản không thể tối ưu theo chất lượng: hệ thống đấu giá đang tối ưu cho `view_price_page` (612 lượt vô giá trị) thay vì cho 18 cọc trị giá 3.130 tr. Không có GCLID thì mọi chiến lược giá thầu thông minh đều bị mù ở nửa cuối phễu.

---

### A12 [ĐL] — Mô hình phân bổ nhấp cuối đang định giá sai kênh, dùng để chia ngân sách suốt 90 ngày
**Mức độ: TRUNG BÌNH — rủi ro cắt nhầm kênh; 71 lead (4,1%) không được ghi nhận cho kênh nào**

| Kênh | Nhấp cuối (đang dùng) | Dựa trên dữ liệu | Chênh | % |
|---|---|---|---|---|
| SEA_Brand | 592 | 401 | **−191** | **−32,3%** |
| SEA_Generic | 418 | 402 | −16 | −3,8% |
| SEA_Competitor | 20 | 24 | +4 | +20,0% |
| PMAX | 510 | 466 | −44 | −8,6% |
| GDN_Remarketing | 132 | 186 | **+54** | **+40,9%** |
| YT_Video | 43 | 165 | **+122** | **+283,7%** |
| Trực tiếp / Organic (ngoài Ads) | 0 | 71 | +71 | — |

*Nguồn: sheet 10 mục D, chỉ tính `generate_lead` (1.715).*

Hai hàm ý ngược chiều nhau, **phải nói cả hai để không bị lệch**:
- Brand đang được **ghi công thừa 32%** ở lớp lead ⇒ khi bảo vệ Brand ở D1, phải dùng số **cọc** (13/18) chứ không chỉ số lead.
- YouTube đang bị **ghi công thiếu 74%** ⇒ không được cắt YouTube chỉ vì cột "Chuyển đổi" bằng 0; nhưng cũng chưa đủ căn cứ tăng, vì YT vẫn 0 cọc.

---

### A13 — 78,1% ngân sách chạy trên di động với tỷ lệ chuyển đổi bằng nửa máy tính
**Mức độ: TRUNG BÌNH — vùng tối ưu ~150–200 tr**

| Thiết bị | % chi phí | Chi phí | Lead | SQL | Cọc | Tỷ lệ CĐ | CP/SQL |
|---|---|---|---|---|---|---|---|
| Di động | **78,1%** | 1.408,6 tr | 2.106 | 463 | 11 | **2,03%** | **3,04 tr** |
| Máy tính | 16,7% | 301,2 tr | 334 | 163 | 6 | **4,02%** | **1,85 tr** |
| Máy tính bảng | 5,2% | 93,8 tr | 115 | 24 | 1 | 1,71% | 3,91 tr |

*Nguồn: sheet 07 mục B.* Máy tính có CP/SQL thấp hơn **39%** và tỷ lệ chuyển đổi gấp **1,98×** nhưng chỉ nhận 16,7% ngân sách. Không có điều chỉnh giá thầu theo thiết bị nào trong sheet 05.
**Lưu ý nhân quả:** một phần chênh lệch này là hệ quả của A8 (lỗi JS Safari iOS chỉ ảnh hưởng di động) và A10 (LP v1 form 7 trường trên màn hình nhỏ) — sửa lỗi kỹ thuật trước, đo lại, rồi mới điều chỉnh giá thầu thiết bị. Điều chỉnh giá thầu ngay bây giờ là chữa triệu chứng.

---

### A14 — 22,7% ngân sách chạy vào khung giờ sale không trực; T7-CN chi 504 tr với 2 sale
**Mức độ: TRUNG BÌNH — vùng tái phân bổ ~300–400 tr**

| Khung giờ | % chi phí | Chi phí | SQL | Cọc | Lead được gọi lại < 30 phút |
|---|---|---|---|---|---|
| 09:00–12:00 | 16,8% | 303,0 tr | 121 | 4 | **93%** |
| 14:00–17:00 | 17,1% | 308,4 tr | 117 | 4 | **91%** |
| 17:00–20:00 | 18,6% | 335,5 tr | 124 | 3 | 64% |
| **20:00–23:00** | **18,7%** | **337,3 tr** | 112 | 3 | **21%** |
| **23:00–24:00** | 4,0% | 72,1 tr | 22 | **0** | **12%** |
| **00:00–06:00** | 4,1% | 73,9 tr | 18 | **0** | 34% |

*Nguồn: sheet 07 mục A.* **22,7% ngân sách (409 tr) chạy sau 20h**, khi chỉ 12–21% lead được gọi lại trong 30 phút — cộng hưởng trực tiếp với A2. Khung 00:00–06:00 chi 73,9 tr, 0 cọc, CP/SQL 4,11 tr.

Theo ngày trong tuần (sheet 07C): **T7 + CN chi 503,8 tr với chỉ 2 sale trực** (sheet 01: "thực trạng, không phải giả định"), cho ra 4 cọc. T3 + T4 chi 520,1 tr chỉ ra **2 cọc** (CP/SQL 3,12 và 3,30 tr — hai ngày tệ nhất tuần). T2 tốt nhất: 7 cọc, CP/SQL 2,15 tr. Lịch quảng cáo hiện là **24/7 không điều chỉnh** (sheet 05).

---

### A15 [ĐL] — Vùng chứa GTM 34 thẻ / 412 KB JS bên thứ ba, có thẻ trùng lặp và thẻ không rõ nguồn gốc
**Mức độ: TRUNG BÌNH — làm chậm LCP ~0,8s (góp vào A10), số liệu GA4 sai từ ngày 31, có rủi ro bảo mật**

| Vấn đề | Bằng chứng | Nguồn |
|---|---|---|
| Trùng thẻ cấu hình GA4 | `GA4 Configuration – Copy of Main` xuất bản v22 **ngày 31** ⇒ `page_view` bắn hai lần ⇒ số phiên và tỷ lệ thoát sai từ ngày 31 | sheet 12A #2, 12B v22, 12C |
| Tải nặng | **34 thẻ, 412 KB JS bên thứ ba, ước làm chậm LCP ~0,8s** | sheet 12 header |
| Thẻ không rõ nguồn gốc | `Zalo Tracking` "không rõ ai cài, không có mô tả"; **3 thẻ đối tác sàn F2** "cần rà soát bảo mật", thêm ~0,3s LCP (v20, ngày 18) | sheet 12A #12, #13; 12B v20 |
| Không gắn ID phiên Clarity vào CRM | Không xem lại được hành trình lead đã chốt cọc | sheet 12A #10, 12C |
| Chống spam | **Không reCAPTCHA, không xác minh OTP** | sheet 05 |

Thiếu reCAPTCHA/OTP là lời giải thích cho tỷ lệ "trùng số điện thoại 31%" và "số điện thoại sai 24%" của PMax (sheet 08C).

---

### Bảng xếp hạng tác động tài chính (tổng hợp A1–A15)

| # | Vấn đề | Loại tác động | Giá trị (tr đ) | Độ tin cậy |
|---|---|---|---|---|
| A1 | Brand bị bóp ngân sách | Doanh thu bỏ lỡ | **~1.767** (cận trên; cận dưới ~900) | Trung bình (ngoại suy) |
| A2 | Lead phản hồi chậm | Doanh thu bỏ lỡ | **~1.678** | Cao (mô hình khớp thực tế 15,8 vs 18) |
| A8 | Lỗi kỹ thuật chưa sửa | DT bỏ lỡ / chi phí | **471–612** HH (261–339 chi phí) | Trung bình (ước tính UX) |
| A10 | LP v1 (đã khắc phục) | Doanh thu bỏ lỡ | **~476** HH (264 chi phí) | Trung bình |
| A4 | PMax | Chi phí lãng phí | **~442** | Cao (đo trực tiếp) |
| A6 | Địa lý ngoài tệp | Chi phí lãng phí | **~364** | Cao |
| A5 | Từ khóa rác | Chi phí lãng phí | **243** (chắc chắn) – 420 (vùng nghi ngờ) | Cao |
| A7 | Competitor | Chi phí lãng phí | **~177** | Cao |
| A9 | GTM gãy N44–46 | Chi phí chạy mù | **59,5** + hỏng tín hiệu | Cao |
| A3, A11, A12, A15 | Đo lường sai cấu trúc | *Nhân quả gốc của A4, A5, A13* | không cộng riêng (tránh đếm trùng) | Cao |
| A13, A14 | Thiết bị & khung giờ | Vùng tái phân bổ | ~450–600 | Trung bình |

**Tổng chi phí lãng phí đo được trực tiếp (A4+A5+A6+A7+A9) = 1.285,5 tr = 71,3% ngân sách 90 ngày.**
*Không cộng dồn cột doanh thu bỏ lỡ với cột chi phí lãng phí* — hai cột này chồng lấn nhau (ví dụ tiền tiết kiệm từ A4 chính là tiền dùng để bịt A1).

---

# PHẦN B — TÍNH TOÁN

> Mọi con số dưới đây do `agent-1-calc.py` sinh ra từ `du_lieu_google_ads_90_ngay_1.csv` (486 dòng = 90 ngày × 6 chiến dịch, có xác nhận `assert len(rows)==486`) và các hằng số trích từ sheet 04–12 (ghi rõ nguồn tại chỗ).

## B1. CPL Ads / CPL CRM / CP/SQL / CP/cọc

**Toàn kỳ (90 ngày):**

| Chỉ số | Giá trị | Benchmark sheet 09 | Đánh giá |
|---|---|---|---|
| Chi phí | 1.803,5 tr | — | — |
| Chuyển đổi Ads | 3.820 | — | — |
| Lead CRM | 2.557 | — | — |
| SQL | 651 | — | — |
| Cọc | 18 | — | — |
| **CPL theo Ads** | **472.130 đ** | < 500k tốt | Đẹp giả tạo (33% CĐ là ảo — xem B6) |
| **CPL theo CRM** | **705.333 đ** | 500k–1,1 tr trung bình | Trong ngưỡng trung bình |
| **CP/SQL** | **2.770.410 đ** | 1,8–3,5 tr trung bình; KPI ≤ 2,2 tr | **Vượt KPI 25,9%** |
| **CP/cọc** | **100.196.500 đ** | — | **Vượt trần ROAS 3,0 (60,3 tr) 66%** |
| Tỷ lệ SQL/Lead | 25,5% | 18–30% trung bình | Trung bình |
| CTR toàn tài khoản | 0,64% | — | Bị kéo xuống bởi Display/YouTube |
| CPC bình quân | 9.973 đ | — | — |

**Theo từng chiến dịch:**

| Chiến dịch | Chi phí (tr) | %CP | CĐ Ads | Lead | SQL | Cọc | CPL Ads | CPL CRM | CP/SQL | CP/cọc | SQL/Lead | Ads/CRM |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **SEA_Brand_Vinhomes_HocMon** | 260,2 | 14,4% | 871 | 857 | 352 | **13** | 299k | **304k** | **0,74 tr** | **20,0 tr** | **41,1%** | 1,02x |
| **SEA_Generic_NhaPho_CanHo_TayBac** | 678,0 | 37,6% | 664 | 587 | 191 | 5 | 1.021k | 1.155k | 3,55 tr | 135,6 tr | 32,5% | 1,13x |
| SEA_Competitor_DoiThu | 176,7 | 9,8% | 31 | 32 | 3 | 0 | 5.701k | 5.523k | **58,92 tr** | — | 9,4% | 0,97x |
| PMAX_VinhomesHM_Lead | 475,4 | 26,4% | 1.775 | 829 | 61 | 0 | **268k** | 573k | **7,79 tr** | — | **7,4%** | **2,14x** |
| GDN_Remarketing_Web30d | 130,0 | 7,2% | 302 | 193 | 36 | 0 | 430k | 674k | 3,61 tr | — | 18,7% | 1,56x |
| YT_Video_TVC_MoBan | 83,2 | 4,6% | 177 | 59 | 8 | 0 | 470k | 1.410k | 10,40 tr | — | 13,6% | **3,00x** |
| **TOÀN KỲ** | **1.803,5** | 100% | **3.820** | **2.557** | **651** | **18** | **472k** | **705k** | **2,77 tr** | **100,2 tr** | **25,5%** | **1,49x** |

**Ba điều bảng này nói ra ngay:**
1. **CPL Ads là chỉ số bẫy.** PMax có CPL Ads thấp nhất (268k) và CP/SQL cao thứ nhì (7,79 tr) — chênh **29 lần**. Ai quản trị bằng CPL Ads sẽ luôn đổ tiền sai chỗ (xem D3).
2. **Chỉ 2/6 chiến dịch từng tạo ra 1 đồng doanh thu.** Brand + Generic = 52,0% chi phí, 100% cọc.
3. **Brand rẻ hơn Generic 4,8 lần ở CP/SQL và 6,8 lần ở CP/cọc** nhưng chỉ nhận 14,4% ngân sách.

## B2. ROAS toàn kỳ và từng giai đoạn

| Giai đoạn | Chi phí (tr) | Doanh thu HH (tr) | Lead | SQL | Cọc | **ROAS** | CP/cọc (tr) |
|---|---|---|---|---|---|---|---|
| GĐ1 (N1–30) | 545,7 | 330,0 | 734 | 151 | 2 | **0,60x** | 272,8 |
| GĐ2 (N31–60) | 604,4 | 850,0 | 761 | 184 | 5 | **1,41x** | 120,9 |
| GĐ3 (N61–90) | 653,4 | 1.950,0 | 1.062 | 316 | 11 | **2,98x** | 59,4 |
| **TOÀN KỲ** | **1.803,5** | **3.130,0** | **2.557** | **651** | **18** | **1,74x** | **100,2** |

**ROAS theo chiến dịch (lãi/lỗ tuyệt đối):**

| Chiến dịch | ROAS | Doanh thu − Chi phí |
|---|---|---|
| SEA_Brand_Vinhomes_HocMon | **8,76x** | **+2.019,8 tr** |
| SEA_Generic_NhaPho_CanHo_TayBac | 1,25x | +172,0 tr |
| PMAX_VinhomesHM_Lead | **0,00x** | **−475,4 tr** |
| SEA_Competitor_DoiThu | 0,00x | −176,7 tr |
| GDN_Remarketing_Web30d | 0,00x | −130,0 tr |
| YT_Video_TVC_MoBan | 0,00x | −83,2 tr |

**Đọc số:**
- ROAS tăng đều 0,60 → 1,41 → 2,98 — **GĐ3 gần chạm KPI 3,0x**. Đây là bằng chứng KPI 3,0x **khả thi**, không phải mục tiêu viển vông: tài khoản đã chạy được 2,98x trong 30 ngày với cấu hình vẫn còn nguyên mọi lỗi ở phần A.
- Ba yếu tố trùng thời điểm GĐ3, phải tách khi quy công: LP v2 (từ ngày 58), SLA gọi 15 phút (sheet 08B), sự kiện mở bán. **Không đủ dữ liệu để tách riêng đóng góp từng yếu tố** — cần dữ liệu A/B hoặc holdout, hiện không có. Không nên quy toàn bộ mức tăng cho quảng cáo.
- Hoa hồng thực tế/cọc = 3.130/18 = **173,9 tr**, thấp hơn giả định đề bài 181 tr **3,9%**. Bài này dùng **181 tr** cho các phép tính hướng tới tương lai (theo đề), nhưng khi lập kế hoạch nên **dự phòng 4%**: nếu HH thực tế giữ mức 173,9 tr thì cần **36,2 cọc** thay vì 34,8 để đạt ROAS 3,0x.

## B3. Tỷ lệ chuyển đổi từng bước phễu

**Toàn kỳ và theo giai đoạn:**

| Phễu | Toàn kỳ | GĐ1 | GĐ2 | GĐ3 | Benchmark sheet 09 |
|---|---|---|---|---|---|
| Lead | 2.557 | 734 | 761 | 1.062 | — |
| **Lead → SQL** | **25,5%** | 20,6% | 24,2% | **29,8%** | >30% tốt; 18–30% TB; <12% báo động |
| SQL | 651 | 151 | 184 | 316 | — |
| **SQL → Đi xem** | **31,6%** | 25,2% | 30,4% | **35,4%** | >35% tốt; 22–35% TB |
| Đi xem | 206 | 38 | 56 | 112 | — |
| **Đi xem → Booking** | **28,6%** | 26,3% | 28,6% | 29,5% | — (không có benchmark) |
| Booking | 59 | 10 | 16 | 33 | — |
| **Booking → Cọc** | **30,5%** | 20,0% | 31,2% | 33,3% | — |
| Cọc | 18 | 2 | 5 | 11 | — |
| *Đi xem → Cọc (gộp)* | *8,7%* | *5,3%* | *8,9%* | *9,8%* | >12% tốt; 7–12% TB; <4% báo động |
| **Lead → Cọc (toàn phễu)** | **0,704%** | 0,27% | 0,66% | **1,04%** | — |

**Theo chiến dịch (nơi khác biệt lộ ra rõ nhất):**

| Chiến dịch | Lead | SQL | Xem | Book | Cọc | Lead→SQL | SQL→Xem | Xem→Book | Book→Cọc | Lead→Cọc |
|---|---|---|---|---|---|---|---|---|---|---|
| SEA_Brand | 857 | 352 | 125 | 37 | 13 | **41,1%** | 35,5% | 29,6% | 35,1% | **1,52%** |
| SEA_Generic | 587 | 191 | 62 | 18 | 5 | 32,5% | 32,5% | 29,0% | 27,8% | 0,85% |
| GDN_Remarketing | 193 | 36 | 8 | 2 | 0 | 18,7% | 22,2% | 25,0% | 0% | 0% |
| YT_Video | 59 | 8 | 1 | 0 | 0 | 13,6% | 12,5% | 0% | — | 0% |
| SEA_Competitor | 32 | 3 | 0 | 0 | 0 | 9,4% | **0%** | — | — | 0% |
| PMAX | 829 | 61 | 10 | 2 | 0 | **7,4%** | 16,4% | 20,0% | 0% | 0% |
| **2 CD Search có cọc (Brand+Generic)** | **1.444** | **543** | **187** | **55** | **18** | **37,6%** | **34,4%** | **29,4%** | **32,7%** | **1,25%** |

**Ba kết luận:**
1. **Điểm nghẽn số 1 của phễu là Lead → SQL (25,5%)**, và nó gần như hoàn toàn do cơ cấu nguồn: PMax (7,4%) + Competitor (9,4%) đóng góp 861 lead nhưng chỉ 64 SQL. Bỏ hai nguồn này ra, tỷ lệ Lead→SQL nhảy lên **37,6%** — trên ngưỡng "tốt" của benchmark. Đây **không phải vấn đề chất lượng trang đích, mà là vấn đề chọn nguồn lưu lượng**.
2. Nửa dưới phễu (SQL→Xem→Book→Cọc) đang cải thiện đều theo giai đoạn và **không phải nút thắt chính**: Xem→Book giữ 26–30% ổn định, Book→Cọc tăng 20%→33,3%.
3. Brand có Lead→Cọc = 1,52%, cao hơn Generic 79% và cao hơn PMax vô hạn lần (PMax = 0).

## B4. Ngược từ KPI 32 cọc / 2,1 tỷ

Tôi **không dùng một tỷ lệ duy nhất** vì tỷ lệ toàn kỳ bị pha loãng bởi lưu lượng rác sẽ bị loại bỏ trong kế hoạch. Ba kịch bản, nêu rõ giả định:

| Kịch bản | Nguồn tỷ lệ | Lead→SQL | SQL→Xem | Xem→Book | Book→Cọc | **SQL cần** | **Lead thô cần** | **CP/SQL tối đa** | CPL tối đa |
|---|---|---|---|---|---|---|---|---|---|
| **KB1 — Bảo thủ** | Toàn kỳ 90 ngày, cả 6 chiến dịch | 25,5% | 31,6% | 28,6% | 30,5% | **1.157** | **4.546** | **1,81 tr** | 0,46 tr |
| **KB2 — Cơ sở** | Chỉ GĐ3 (đã có SLA 15 phút + LP v2) | 29,8% | 35,4% | 29,5% | 33,3% | **919** | **3.089** | **2,28 tr** | 0,68 tr |
| **KB3 — Kế hoạch** | Chỉ Brand+Generic, GĐ3 | 38,8% | 37,4% | 30,8% | 34,4% | **809** | **2.086** | **2,60 tr** | 1,01 tr |

**Tôi chọn KB3 làm cơ sở lập kế hoạch. Lý do — 4 điểm, mỗi điểm gắn số:**
1. Kế hoạch 90 ngày tới **cắt/tái cấu trúc PMax và Competitor** (2 nguồn kéo Lead→SQL toàn kỳ từ 37,6% xuống 25,5%). Dùng tỷ lệ toàn kỳ để lập kế hoạch cho một cơ cấu nguồn khác hẳn là sai phương pháp.
2. KB3 lấy từ GĐ3 — giai đoạn đã có **LP v2** (hoàn tất form 28,0% vs 20,4%) và **SLA gọi 15 phút** (thời gian phản hồi trung vị 47 phút vs 214 phút ở GĐ1). Cả hai điều kiện này sẽ **tiếp tục tồn tại** ở 90 ngày tới, còn điều kiện GĐ1 thì không.
3. KB3 vẫn **thận trọng** ở chỗ chưa tính bất kỳ cải thiện nào từ việc sửa lỗi kỹ thuật (A8: +370–480 lead) hay siết SLA (A2: +9,3 cọc). Những khoản đó là biên an toàn, không phải giả định.
4. KB1 cho CP/SQL tối đa 1,81 tr — **thấp hơn cả KPI 2,20 tr của ban giám đốc**, tức nếu KB1 đúng thì KPI tự mâu thuẫn (không thể vừa đạt 32 cọc vừa giữ CP/SQL ≤ 2,2 tr). Nêu rõ điều này ở phần rủi ro.

**Kiểm tra chéo với ràng buộc KPI CP/SQL ≤ 2,2 tr:**

| | SQL cần | CP/SQL tối đa cho phép bởi ngân sách | So với trần KPI 2,2 tr |
|---|---|---|---|
| KB1 | 1.157 | 1,81 tr | **CĂNG — không đạt được cả hai KPI cùng lúc** |
| KB2 | 919 | 2,28 tr | Đạt, biên 3,6% |
| KB3 | 809 | 2,60 tr | Đạt, biên 18,2% |

Với trần CP/SQL 2,2 tr, 2,1 tỷ mua được **955 SQL** — đủ cho KB2 (919) và KB3 (809), **thiếu 202 SQL** cho KB1.

**Kiểm tra ràng buộc năng lực sale:** KB3 cần **2.086 lead thô / 90 ngày = 23,2 lead/ngày**, trên tổng công suất 8 × 12 × 90 = **8.640 lead** ⇒ chỉ **24,1% công suất**. 90 ngày qua đã chạy ở 29,6% công suất. **Năng lực sale không phải nút thắt — tốc độ phản hồi mới là** (A2). Ràng buộc "không tăng nhân sự" không cản trở KPI.

**Rủi ro của kịch bản KB3 (nói thẳng):** KB3 giả định lưu lượng mở rộng thêm sẽ giữ được chất lượng của Brand+Generic ở GĐ3. Brand có trần tự nhiên — nhu cầu tìm kiếm tên dự án là hữu hạn (bịt hết mất IS ngân sách chỉ thêm ~643 lead, A1). Phần còn lại phải đến từ Generic, nơi Lead→SQL chỉ 32,5%. **Kịch bản thực tế nằm giữa KB2 và KB3: cần ~850–920 SQL, ~2.400–2.900 lead thô, CP/SQL tối đa 2,28–2,47 tr.** Tôi lập kế hoạch theo KB3 và dùng KB2 làm ngưỡng cảnh báo.

## B5. Điểm hòa vốn

Hoa hồng 181 tr/cọc:

| Mức ROAS | Chi phí quảng cáo tối đa/cọc | Số cọc tối đa mua được với 2,1 tỷ |
|---|---|---|
| 1,0x (hòa vốn quảng cáo thuần) | **181,00 tr** | 11,6 |
| 2,0x | **90,50 tr** | 23,2 |
| **3,0x (KPI)** | **60,33 tr** | **34,8** |
| 3,5x (biên an toàn) | 51,71 tr | 40,6 |

**Đối chiếu thực tế:** CP/cọc 90 ngày qua = **100,2 tr** ⇒ ROAS 1,74x. Phải **giảm CP/cọc 39,8%** (từ 100,2 xuống 60,3 tr) để chạm KPI.

**Ba con số cần nhớ khi ra quyết định hằng ngày:**
- Ngưỡng ROAS 3,0x cần **34,8 cọc** với ngân sách 2,1 tỷ. KPI ban giám đốc là 32 cọc ⇒ **32 cọc chỉ cho ROAS 2,76x**. **KPI cọc và KPI ROAS không nhất quán với nhau.** Phải chốt với ban giám đốc: nếu ROAS 3,0x là ràng buộc cứng thì mục tiêu cọc thực chất là **35**, không phải 32; hoặc nếu giữ 32 cọc thì ngân sách phải hạ xuống **1.931 tr** (32 × 181 / 3,0).
- Nếu hoa hồng thực tế giữ mức 173,9 tr (B2) thì cần **36,2 cọc** cho ROAS 3,0x, hoặc chi phí tối đa/cọc chỉ còn **57,97 tr**.
- Điểm dừng cho từng chiến dịch: **bất kỳ chiến dịch nào chi > 60,3 tr mà chưa ra 1 cọc đều đang phá ROAS mục tiêu.** Áp thước này lên 90 ngày qua: PMax vượt 7,9×, Competitor vượt 2,9×, GDN vượt 2,2×, YouTube vượt 1,4×.

## B6. Đối chiếu ba nguồn số liệu — bóc tách chính xác từng thành phần

**Bước 1 — 3.820 gồm những gì** (sheet 10A + 10E, sheet 12A thẻ #3–#6, #8):

| Thành phần | Số lượt | % |
|---|---|---|
| `generate_lead` (gửi form thành công) | 1.715 | 44,9% |
| `click_to_call` (tổng lượt nhấp) | 1.132 | 29,6% |
| `view_price_page` (xem trang /bang-gia) | 612 | 16,0% |
| `engaged_30s` (ở lại trang > 30 giây) | 361 | 9,5% |
| **Cộng** | **3.820** | 100% |

*Kiểm tra: 1.715 + 1.132 + 612 + 361 = 3.820 ✔ (assert trong script)*

**Bước 2 — trừ đi phần không phải lead:**

| Khoản trừ | Số | % của 3.820 | Nguyên nhân kỹ thuật |
|---|---|---|---|
| **Đếm trùng lượt gọi** | **353** | 9,2% | 1.132 lượt / 779 người thật. Thẻ #4 GTM "đếm mọi lượt nhấp, không khử trùng theo người dùng" (sheet 12A) |
| **Sự kiện rác** | **973** | 25,5% | `view_price_page` 612 + `engaged_30s` 361 — sheet 10E ghi rõ cột "Có thực sự là khách hàng tiềm năng?" = **KHÔNG** |
| **Cộng phần ảo** | **1.326** | **34,7%** | |
| **= Lead thật đo được bằng thẻ** | **2.494** | | 1.715 form + 779 người gọi duy nhất |

**Bước 3 — cộng phần thẻ không bắt được:**

| Khoản cộng | Số | Nguyên nhân |
|---|---|---|
| **Lead mất thẻ ngày 44–46** | **63** | GTM v23 (ngày 44, 09:12) đổi class `.form-dk-v1` → `.form-register`, điều kiện kích hoạt `generate_lead` ngừng khớp. v24 sửa ngày 47, nhưng 63 lead 3 ngày đó "vĩnh viễn không có trong Google Ads/GA4" (sheet 12B) |
| **= Lead CRM** | **2.557** | ✔ khớp chính xác với sheet 02 |

**Bước 4 — phép cộng khớp (đây là phần đề bài yêu cầu chứng minh):**

```
3.820  (Google Ads = GA4 sự kiện chính, hai số luôn bằng nhau vì Ads nhập trực tiếp từ GA4)
−  353  đếm trùng click_to_call
−  973  sự kiện rác (view_price_page 612 + engaged_30s 361)
= 2.494  lead thật đo được bằng thẻ
+   63  lead mất thẻ ngày 44–46 (CRM có, hệ đo không có)
= 2.557  lead CRM  ✔
```

**Kiểm tra ngược khoảng chênh:** 3.820 − 2.557 = **1.263** = 353 (trùng) + 973 (rác) − 63 (mất thẻ) = **1.263** ✔ *(assert trong script)*

**Xác minh độc lập trên sheet 02** (không dựa vào sheet 10/12): script lọc `Ngay_thu` 44–46 cho ra **Chuyển đổi Ads = 0** trong khi **Lead CRM = 63**; ngày 43 = 43 chuyển đổi, ngày 47 = 33 chuyển đổi. Chi phí 3 ngày mù = **59,5 tr**. Ba nguồn dữ liệu độc lập (sheet 02, sheet 10, sheet 12) khớp nhau hoàn toàn.

**Diễn giải:**

| Nguồn | Con số | Đúng ở điều gì | Sai ở điều gì |
|---|---|---|---|
| Google Ads | 3.820 | Đúng theo định nghĩa nó được cấu hình | Định nghĩa được cấu hình sai — thổi phồng **1,49x** |
| GA4 | 3.820 (thô) / 2.494 (lead thật) | 2.494 là con số đo lường sạch nhất | Thiếu 63 lead do sự cố thẻ |
| **CRM** | **2.557** | **Đầy đủ nhất — đây là nguồn sự thật** | Không có GCLID nên không biết lead nào từ chiến dịch nào (sheet 12A #15) |

Tỷ lệ thổi phồng toàn tài khoản **1,49x** — nằm trong ngưỡng "trung bình 1,2–1,5x" của sheet 09, nhưng riêng **PMax là 2,14x** và **YouTube 3,00x**, đều vượt ngưỡng báo động 1,8x.

## B7. Ước tính lead mất do lỗi kỹ thuật CHƯA SỬA (sheet 11)

**Phân định rõ đâu là số đo, đâu là ước tính — theo đúng yêu cầu đề bài:**

| Loại | Nội dung | Nguồn |
|---|---|---|
| **SỐ ĐO trực tiếp** (Clarity ghi hình, lấy mẫu ~92% lưu lượng LP) | Lỗi #4: **4.196 phiên** ảnh hưởng; Lỗi #5: **2.741 phiên**; Lỗi #6: **1.204 phiên**, 1.847 nhấp chết | sheet 11C |
| **SỐ ĐO trực tiếp** | Tỷ lệ phiên có lỗi JS trên di động: v1 **9,3%** → v2 **8,9%** (không giảm) ⇒ chứng minh lỗi #4 vẫn sống ở v2 | sheet 11A |
| **SỐ ĐO trực tiếp** | Tỷ lệ hoàn tất form toàn kỳ 22,995% (1.715/7.458 form_start) | sheet 10B |
| **ƯỚC TÍNH của đội UX** (không phải của tôi) | Lỗi #4: 280–340 lead · #5: 60–90 · #6: 30–50. Tổng **370–480 lead / 90 ngày**. Phương pháp: "dựa trên tỷ lệ hoàn tất form của nhóm phiên không gặp lỗi" | sheet 11C, dòng ghi chú |
| **ƯỚC TÍNH của tôi** | Quy đổi ra tiền bằng CPL/CP-SQL/tỷ lệ cọc thực tế toàn kỳ (bảng dưới) | tính từ sheet 02 |

**Quy ra tiền — ba lớp, ba mức độ tin cậy giảm dần:**

| Lớp quy đổi | Đơn giá dùng | Nguồn đơn giá | Kết quả (370 lead) | Kết quả (480 lead) |
|---|---|---|---|---|
| **1. Chi phí quảng cáo đã trả cho lead không nhận được** | CPL CRM thực tế **705.333 đ** | 1.803,5 tr / 2.557 lead (sheet 02) | **261 tr** | **339 tr** |
| **2. Quy về SQL** | tỷ lệ SQL/Lead **25,5%** → 94–122 SQL, × CP/SQL 2,77 tr | sheet 02 | 261 tr | 339 tr |
| **3. Quy về doanh thu hoa hồng bỏ lỡ** | tỷ lệ Lead→Cọc **0,704%** → **2,6–3,4 cọc** × 181 tr | sheet 02 | **471 tr** | **612 tr** |

**Con số tôi trình lên ban giám đốc: 370–480 lead = 261–339 tr chi phí quảng cáo đã trả nhưng không thu được lead, tương đương 2,6–3,4 cọc ≈ 471–612 tr hoa hồng bỏ lỡ trong 90 ngày.**

**Bốn cảnh báo về độ tin cậy — phải nói ra:**
1. Con số 370–480 là **ước tính của đội UX, không phải số đo**. Sheet 11 ghi rõ điều này. Tôi giữ nguyên khoảng, không làm tròn thành một con số duy nhất để tránh tạo cảm giác chính xác giả.
2. Clarity chỉ lấy mẫu **~92% lưu lượng** và **gắn từ ngày 5** (sheet 11 header, sheet 12B v19) ⇒ 4 ngày đầu không có dữ liệu ⇒ con số thực có thể **cao hơn** khoảng ước tính.
3. Tỷ lệ Lead→Cọc 0,704% là tỷ lệ **toàn kỳ đã pha loãng bởi lead rác PMax**. Nếu các lead mất này thuộc nhóm Search chất lượng cao (khả năng cao, vì lỗi nằm ở nút gửi form của LP), tỷ lệ đúng phải là **1,25%** (Brand+Generic) ⇒ **4,6–6,0 cọc ≈ 838–1.086 tr HH**. Tôi báo cáo **khoảng thận trọng 471–612 tr** và ghi rõ cận trên có thể tới ~1.086 tr.
4. **Ba lỗi đã sửa ở v2** (#1 nhấp chết 90–140, #2 trường CMND 320–400, #3 dropdown ngân sách 110–150 = tổng **520–690 lead**) là tiền đã mất, **không còn chảy máu** — không tính vào con số hành động, chỉ ghi nhận để đánh giá chi phí của việc chậm sửa LP 57 ngày.

**Chi phí của việc trì hoãn:** 370–480 lead / 90 ngày = **4,1–5,3 lead/ngày**. Mỗi tuần trì hoãn sửa lỗi #4, #5, #6 tốn **29–37 lead = 20–26 tr chi phí quảng cáo lãng phí**. Chi phí sửa: một lần deploy front-end. Đây là lập luận dùng cho D6.

---

# PHẦN C — KẾ HOẠCH 90 NGÀY TIẾP THEO

**Nguyên tắc chỉ đạo, mỗi nguyên tắc gắn số từ phần A/B:**
1. **Sửa đo lường trước, tăng ngân sách sau.** 33,1% tín hiệu là ảo (B6) — mọi đồng thêm vào trước khi sửa đều được tối ưu theo tín hiệu rác.
2. **Dồn tiền về nơi đã chứng minh ra cọc.** Brand+Generic = 52,0% chi phí nhưng 100% cọc và 100% doanh thu (B1).
3. **Bịt lỗ trước khi mở vòi.** 1.285,5 tr lãng phí đo được (71,3% ngân sách cũ) đủ để tài trợ toàn bộ phần tăng trưởng mà không cần xin thêm tiền.

## C.0 — Bảng phân bổ ngân sách tổng thể (tổng đúng 2.100 tr)

| Chiến dịch | GĐ1 (N1–30) | GĐ2 (N31–60) | GĐ3 (N61–90) | **Tổng** | % | So với 90 ngày trước |
|---|---|---|---|---|---|---|
| SEA_Brand_Vinhomes_HocMon | 170 | 190 | 200 | **560** | 26,7% | 260,2 → **+115%** |
| SEA_Generic_NhaPho_CanHo_TayBac (tái cấu trúc) | 250 | 270 | 280 | **800** | 38,1% | 678,0 → +18% |
| SEA_HighIntent_DiXemNha (**mới**) | 50 | 80 | 90 | **220** | 10,5% | mới |
| PMAX_VinhomesHM_Lead (tái cấu trúc) | 60 | 100 | 120 | **280** | 13,3% | 475,4 → **−41%** |
| GDN_Remarketing_Web30d | 35 | 45 | 50 | **130** | 6,2% | 130,0 → 0% |
| YT_Video_TVC_MoBan | 0 | 20 | 30 | **50** | 2,4% | 83,2 → −40% |
| Dự phòng / thử nghiệm | 20 | 20 | 20 | **60** | 2,9% | mới |
| ~~SEA_Competitor_DoiThu~~ | **0** | **0** | **0** | **0** | 0% | 176,7 → **−100%** |
| **TỔNG (triệu đ)** | **585** | **725** | **790** | **2.100** | 100% | 1.803,5 → +16,4% |
| *Ngân sách/ngày* | *19,5 tr* | *24,2 tr* | *26,3 tr* | *23,3 tr* | | *20,0 tr/ngày trước đây* |

*(Kiểm tra tổng bằng `assert sum(tt) == 2100` trong script.)*

**Bốn quyết định phân bổ và lý do bằng số:**

| Quyết định | Số căn cứ |
|---|---|
| **Brand ×2,15 (260 → 560 tr)** | Mất IS ngân sách 40,1%, ROAS 8,76x, CP/SQL 0,74 tr (thấp nhất tài khoản, bằng 1/3 KPI). Đây là chỗ duy nhất có ROAS biên ~9x đã được chứng minh. |
| **Competitor cắt về 0** | 176,7 tr → 3 SQL, 0 cọc, CP/SQL 58,92 tr = **26,8× KPI**. 26% lead là môi giới/đối thủ. Không có dữ liệu nào biện minh cho việc giữ. |
| **PMax giảm 41% và chỉ giải ngân sau khi sạch tín hiệu** | 475,4 tr → 0 cọc; SQL/Lead 7,4% (dưới ngưỡng báo động 12%); thoát nhanh 74,3%. Giữ 280 tr để **kiểm chứng lại** sau khi có tín hiệu chuyển đổi sạch + brand exclusion + loại trừ vị trí đặt — không phải để "chạy tiếp như cũ". |
| **Ngân sách tăng dần 585 → 725 → 790** | GĐ1 cố tình thấp hơn mức chi 90 ngày qua (585 vs ~601 tr/GĐ) vì tháng đầu là tháng **sửa đo lường + học lại tín hiệu**. Đổ tiền vào lúc Smart Bidding đang học lại là cách nhanh nhất để đốt tiền. |

## C.1 — GIAI ĐOẠN 1 (Ngày 1–30): DỌN DẸP & DỰNG LẠI ĐO LƯỜNG

### Mục tiêu định lượng

| Chỉ tiêu | Mục tiêu GĐ1 | Cơ sở tính |
|---|---|---|
| Ngân sách | ≤ 585 tr (19,5 tr/ngày) | bảng C.0 |
| Lead thô | ≥ 521 | KB3 × 25% |
| SQL | ≥ 202 | KB3 × 25% |
| CP/SQL | ≤ 2,89 tr | 585/202 |
| Cọc | ≥ 8 | 32 × 25% |
| ROAS | ≥ 2,48x | 8 × 181 / 585 |
| **Tỷ lệ Chuyển đổi Ads / Lead CRM** | **≤ 1,15x** | hiện 1,49x — đây là KPI kỹ thuật quan trọng nhất của GĐ1 |
| Tỷ lệ lead gọi lại < 30 phút | ≥ 60% | hiện 30% (281+485)/2.554 |
| Impression Share Brand | ≥ 80% | hiện 53,4% |
| Mất IS ngân sách Brand | ≤ 5% | hiện 40,1% |

### Cấu trúc tài khoản đề xuất

| Chiến dịch | Nhóm quảng cáo | Loại đối sánh | Ghi chú |
|---|---|---|---|
| **SEA_Brand** | AG1 Brand core (`vinhomes hóc môn`, `vin hóc môn`, `vinhomes hoc mon`) · AG2 Brand + giá (`… giá bán`, `… bảng giá`) · AG3 Brand + dự án (`dự án vinhomes hóc môn`) | **Chính xác + Cụm từ**, bỏ hết Rộng | Bỏ Rộng vì `vinhomes hóc môn tuyển dụng` (15,6 tr, 0 SQL) và `vinschool hóc môn học phí` (10,4 tr, 0 SQL) đều lọt qua Rộng |
| **SEA_Generic** | AG1 Nhà phố (`nhà phố hóc môn`, `nhà phố dưới 8 tỷ tphcm`) · AG2 Căn hộ (`căn hộ hóc môn giá bao nhiêu`) · AG3 Shophouse/Biệt thự · AG4 Khu vực (`khu đô thị tây bắc tphcm`, `mua nhà phố quận 12`) | **Chính xác + Cụm phrase**, Rộng **chỉ** trong 1 nhóm thử nghiệm riêng có tCPA và ngân sách trần 30 tr/GĐ | Từ khóa/nhóm: **≤ 10** (hiện 31 — sheet 05). Mỗi nhóm **2 RSA + 1 trang đích riêng** (hiện 1 RSA) |
| **SEA_HighIntent_DiXemNha** (mới) | AG1 "đặt lịch xem nhà mẫu" · AG2 "nhà mẫu vinhomes hóc môn" · AG3 "chính sách thanh toán/ưu đãi" | Chính xác | Tách ra để bid riêng cho ý định cuối phễu; đích là form đặt lịch, không phải form nhận bảng giá |
| **PMAX** | 1 nhóm tài sản duy nhất, tệp tín hiệu = danh sách khách đã cọc + SQL (khách hàng tương tự) | — | Bật **brand exclusion**, loại trừ vị trí đặt (app/game/video), loại trừ tệp đã cọc |
| **GDN_Remarketing** | AG1 Web 7 ngày · AG2 Web 8–30 ngày · AG3 Đã xem /bang-gia chưa gửi form | — | Hiện chỉ có 1 nhóm gộp 30 ngày |
| **YT_Video** | Tạm dừng GĐ1 | — | Khởi động lại GĐ2 với đo lường sạch (xem C.2) |

**Cấu hình bắt buộc sửa ngay ngày 1–3 (từ sheet 05):**

| Hạng mục | Hiện tại | Đổi thành | Căn cứ |
|---|---|---|---|
| Nhắm mục tiêu vị trí | Việt Nam toàn quốc | **TP.HCM + Bình Dương + Long An** | sheet 06: HN/ĐN/CT + ngoài VN = 364 tr, **0 cọc** |
| Tùy chọn vị trí | Hiện diện HOẶC quan tâm | **Chỉ "Hiện diện"** | 28,9 tr chi cho người ngoài VN |
| Loại trừ vị trí | Không có | Loại trừ Hà Nội, Đà Nẵng, ĐBSCL ở cấp tài khoản | như trên |
| Search Partners | BẬT | **TẮT** (3 CD Search) | Chưa tách được hiệu quả — tắt để làm sạch dữ liệu, đo lại sau 30 ngày |
| Display trong CD Search | BẬT | **TẮT** | Trộn lưu lượng Display vào Search làm hỏng cả CTR lẫn tín hiệu bid |
| Từ khóa phủ định | 12 từ | **≥ 150 từ, dùng danh sách chia sẻ** | 11 cụm lạc = 243 tr (sheet 04) |
| Lịch quảng cáo | 24/7 không điều chỉnh | 06–20h chạy đủ; **20–23h giảm 40%**; 23–06h **tắt** | sheet 07A: 23–24h & 00–06h = 146 tr, **0 cọc**; gọi lại <30p chỉ 12–34% |
| Điều chỉnh giá thầu ngày | Không có | T7-CN **−30%** (chỉ 2 sale trực); T3-T4 **−15%** | sheet 07C: T7+CN 503,8 tr/4 cọc; T3+T4 520,1 tr/**2 cọc** |
| Danh sách loại trừ | Chưa loại trừ khách đã cọc/ký HĐMB | Tạo và áp cho cả 6 chiến dịch | sheet 05 |
| Tiện ích | Chỉ Sitelink (4) | + **Cuộc gọi** (giờ 08–18h), **Biểu mẫu KHTN**, **Vị trí**, **Chú thích**, **Hình ảnh** | sheet 05 liệt kê đúng 5 tiện ích đang thiếu |
| Chống spam form | Không reCAPTCHA, không OTP | **reCAPTCHA v3 + OTP số điện thoại** | sheet 08C: PMax trùng SĐT 31%, SĐT sai 24% |

### Chiến lược giá thầu GĐ1 và điều kiện chuyển đổi

| Chiến dịch | GĐ1 | Điều kiện chuyển sang chiến lược khác |
|---|---|---|
| SEA_Brand | **Tỷ lệ hiển thị mục tiêu = 90%, vị trí đầu trang**, trần CPC 20.000đ | Khi IS ổn định ≥ 85% trong 14 ngày liên tục → chuyển **tCPA 700.000đ** (= CP/SQL Brand hiện tại 0,74 tr) |
| SEA_Generic | Giữ **Tối đa hóa số nhấp CÓ trần CPC 35.000đ** trong 14 ngày đầu (dữ liệu chuyển đổi đang bị nhiễm, chưa đủ sạch để Smart Bidding học) | Sau **≥ 30 chuyển đổi sạch/30 ngày** → chuyển **tCPA 1.100.000đ** (= CPL CRM Generic hiện tại 1,155 tr). Sau đó khi có ECL, chuyển **tCPA theo SQL 2,4 tr** |
| SEA_HighIntent | **Tối đa hóa chuyển đổi**, ngân sách nhỏ 50 tr | Sau 20 chuyển đổi → tCPA |
| PMAX | **Tối đa hóa chuyển đổi + tCPA 1.200.000đ** (đặt trần thay vì thả nổi như hiện tại) | Chỉ tăng ngân sách khi **SQL/Lead ≥ 20%** (hiện 7,4%) VÀ thoát nhanh < 40% (hiện 74,3%) |
| GDN_Remarketing | CPC nâng cao → **tCPA 800.000đ** | Nếu CP/SQL > 4 tr trong 30 ngày → cắt về 0 |
| YT_Video | Tạm dừng | — |

**Nguyên tắc chống giật (không được vi phạm):** không đổi chiến lược giá thầu, không đổi tCPA quá **20%/lần** và không quá **1 lần/2 tuần** cho cùng một chiến dịch. Bài học từ GTM v23: mỗi thay đổi phải có ngày ghi nhận để truy nguyên nhân.

### KẾ HOẠCH ĐO LƯỜNG — GĐ1 (mục riêng, theo yêu cầu đề bài)

Đây là hạng mục **ưu tiên số 1 của toàn kế hoạch**. Không có mục này, mọi con số còn lại đều vô nghĩa.

#### Sửa gì trong GA4

| # | Việc | Chi tiết | Kiểm chứng sau khi sửa |
|---|---|---|---|
| G1 | **Bỏ đánh dấu sự kiện chính** cho `view_price_page` (612 lượt) và `engaged_30s` (361 lượt) | Admin → Events → tắt "Mark as key event". **Không xóa sự kiện** — vẫn giữ để phân tích, chỉ ngừng nhập vào Ads | Sau 7 ngày: cột Chuyển đổi trong Ads giảm ~25%; tỷ lệ Ads/CRM từ 1,49x về ~1,20x |
| G2 | **Khử trùng `click_to_call`** | Đổi tham số đếm sang "Một lần cho mỗi phiên" (once per session), hoặc thêm điều kiện `session_id` duy nhất | Số `click_to_call` giảm từ 1.132 về ~779 (−31,2%) |
| G3 | **Đánh dấu `zalo_click` (894 lượt) và `file_download` (1.206 lượt) là sự kiện chính phụ**, nhập vào Ads dưới dạng **chuyển đổi phụ** (secondary — không tính vào cột Chuyển đổi, chỉ để quan sát và làm tín hiệu tệp) | sheet 10E: cả hai "đang bị bỏ sót". Zalo là CTA chính theo quy ước thị trường VN | Ads hiển thị 2 hành động chuyển đổi mới ở cột "Tất cả chuyển đổi" |
| G4 | **Cấu trúc lại cột Chuyển đổi chính**: chỉ còn `generate_lead` + `click_to_call` (đã khử trùng) | 1.715 + 779 = **2.494** — khớp với con số lead thật đo được ở B6 | Chênh lệch Ads vs CRM ≤ 1,15x (KPI GĐ1) |
| G5 | Bật **Enhanced Conversions for Leads** (băm email/SĐT phía client) | sheet 12A #14 CHƯA CÀI; sheet 12C ghi hệ quả "mất 10–20% khả năng khớp" | Báo cáo Diagnostics trong Ads hiển thị trạng thái "Recording enhanced conversions" |
| G6 | Đổi **mô hình phân bổ báo cáo** từ Nhấp cuối sang **Dựa trên dữ liệu** | sheet 10D: nhấp cuối thổi Brand +32%, dìm YouTube −74% | Báo cáo phân bổ trong GA4 khớp cột "Dựa trên dữ liệu" của sheet 10D |
| G7 | Tạo **đối tượng GA4** đẩy sang Ads: đã `form_start` chưa `generate_lead` (7.458 − 1.715 = **5.743 người**), đã xem `/bang-gia` chưa gửi form | Hiện GDN chỉ có 1 tệp "Web 30 ngày" | 3 danh sách remarketing có kích thước > 1.000, đủ điều kiện chạy |

#### Sửa gì trong GTM

| # | Việc | Ưu tiên | Căn cứ | Kiểm chứng |
|---|---|---|---|---|
| T1 | **Xóa thẻ `GA4 Configuration – Copy of Main`** (#2) | **Ngày 1** | sheet 12A #2, 12B v22 (ngày 31): `page_view` bắn hai lần | Preview mode: mỗi lần tải trang chỉ 1 `page_view`; số phiên GA4 giảm ~50% ⇒ số phiên từ ngày 31 trở đi trong lịch sử phải được ghi chú là **không so sánh được** |
| T2 | **Đổi điều kiện kích hoạt `generate_lead` từ class CSS sang `dataLayer.push`** do dev bắn khi form trả về thành công | **Ngày 1–3** | sheet 12A #3 "rất dễ vỡ"; sự cố v23 mất 63 lead | Đổi giao diện thử nghiệm trên staging → thẻ vẫn kích hoạt |
| T3 | **Cài biến ẩn lưu GCLID/GBRAID/WBRAID + UTM vào form** và đẩy vào CRM | **Ngày 1–7** | sheet 12A #15 CHƯA CÀI ⇒ "KHÔNG THỂ nhập chuyển đổi ngoại tuyến" | Sau 7 ngày: **≥ 90% bản ghi CRM mới có trường gclid không rỗng** |
| T4 | **Sửa 3 lỗi LP chưa sửa** (#4 TypeError `e.setDate` Safari iOS, #5 nút bị khung chat che < 380px, #6 hotline `tel:` trên desktop) | **Ngày 1–5** | sheet 11C; 370–480 lead/90 ngày (B7) | Clarity: tỷ lệ phiên có lỗi JS di động từ **8,9% → < 2%**; tỷ lệ hoàn tất form di động từ 24,6% lên ≥ 30% |
| T5 | **Cài cảnh báo tự động khi chuyển đổi = 0** (GA4 Custom Insight + Ads Rule gửi email/Slack nếu chuyển đổi = 0 trong 6 giờ giờ hành chính) | **Ngày 1–3** | sheet 12A #18 KHÔNG CÓ ⇒ sự cố N44–46 mất 3 ngày mới phát hiện | Cố tình tắt thẻ trên staging → nhận cảnh báo trong ≤ 6 giờ |
| T6 | **Rà soát & dọn 34 thẻ**: gỡ 3 thẻ đối tác sàn F2 không rõ nguồn gốc + thẻ `Zalo Tracking` không rõ ai cài (nếu không ai nhận trong 48 giờ) | Ngày 3–7 | sheet 12A #12, #13; 412 KB JS làm chậm LCP ~0,8s | LCP LP đo lại bằng PageSpeed: từ 1,9s xuống **< 1,6s** |
| T7 | **Cấu hình Consent Mode v2** | Ngày 7–14 | sheet 12A #16 CHƯA CẤU HÌNH | Tag Assistant hiển thị `consent` state hợp lệ |
| T8 | **Gắn Clarity session ID vào bản ghi CRM** | Ngày 14–21 | sheet 12A #10, 12C | Mở 1 lead đã cọc trong CRM → xem lại được phiên Clarity |
| T9 | **Triển khai vùng chứa phía máy chủ (server-side GTM)** | GĐ2, ngày 31–45 | sheet 12A #17 KHÔNG CÓ | So sánh sự kiện client vs server: chênh lệch ≤ 5% |

#### Thứ tự triển khai (không được đảo)

```
Ngày 1     T1 (xóa thẻ trùng) + T5 (cảnh báo)      → cầm máu, chi phí gần bằng 0
Ngày 1–3   T2 (dataLayer trigger) + G1, G2, G4     → làm sạch tín hiệu chuyển đổi
Ngày 1–5   T4 (sửa 3 lỗi LP)                       → cầm máu 4,1–5,3 lead/ngày
Ngày 1–7   T3 (GCLID vào CRM)                      → mở khóa toàn bộ đường ECL
Ngày 3–7   T6 (dọn thẻ) + G5 (Enhanced Conv)
Ngày 7–14  G3, G6, G7 + T7 (Consent Mode)
Ngày 14–21 T8 + thiết lập đường ống ECL (upload cọc/SQL về Ads)
Ngày 21–30 Chạy song song 7 ngày để đối chiếu, chốt cột Chuyển đổi mới
```

**Lý do thứ tự này:** T3 (GCLID) phải xong trước ngày 7 vì đường ống chuyển đổi ngoại tuyến cần **ít nhất 30 ngày dữ liệu tích lũy** trước khi Smart Bidding dùng được — nếu bắt đầu muộn hơn thì GĐ3 không kịp chuyển sang bid theo SQL. G1/G2 phải làm cùng lúc với T2 để không tạo thêm một đứt gãy số liệu thứ hai chồng lên đứt gãy N44–46.

#### Cách kiểm tra sau khi sửa

| Việc kiểm tra | Ngưỡng đạt | Khi nào |
|---|---|---|
| **Chạy song song 7 ngày**: ghi lại cả cột chuyển đổi cũ và mới trước khi tắt cái cũ | Chênh lệch giải thích được 100% bằng công thức B6 | Ngày 7–14 |
| **Tỷ lệ Chuyển đổi Ads / Lead CRM** đo hằng tuần | ≤ **1,15x** (hiện 1,49x) | hằng tuần |
| **GTM Preview + Tag Assistant** trên 4 thiết bị (Android Chrome, iOS Safari 17, desktop Chrome, iPad) | Mọi sự kiện kích hoạt đúng 1 lần | trước & sau mỗi lần xuất bản |
| **Đối chiếu 3 nguồn hằng tuần** (Ads / GA4 / CRM), bảng như B6 | Ba cột chênh nhau ≤ 5% sau khi đã trừ khoản đã biết | thứ 2 hằng tuần |
| **Clarity**: tỷ lệ phiên có lỗi JS di động | 8,9% → **< 2%** | ngày 7 và ngày 30 |
| **Quy trình bắt buộc**: mọi thay đổi GTM phải qua Preview → xuất bản có ghi chú → thông báo cho marketing trong 24h | 100% phiên bản có ghi chú | liên tục |

### Việc cần làm với trang đích, tiện ích, đối tượng — GĐ1

| Hạng mục | Việc | Số căn cứ |
|---|---|---|
| **Trang đích** | Sửa 3 lỗi chưa sửa (T4). Bắt đầu **A/B test thật sự** (hiện có 0 test — sheet 05) | v1→v2 cho +37,3% hoàn tất form (sheet 10C) — cải tiến này lẽ ra phát hiện được ở tuần 2 |
| **Trang đích** | Tách LP theo nhóm quảng cáo: LP nhà phố (6,8–11,5 tỷ) vs LP căn hộ (2,9–4,6 tỷ) | sheet 08C: **sai phân khúc (ngân sách < 2 tỷ) chiếm 18–34%** ở mọi nguồn. Hiển thị khoảng giá ngay above-the-fold để tự lọc |
| **Trang đích** | Tối ưu di động là ưu tiên: form tối đa 3 trường, nút CTA sticky không bị che | Di động = 78,1% chi phí, CVR 2,03% vs desktop 4,02% (sheet 07B) |
| **Tiện ích** | Bật 5 tiện ích còn thiếu: Cuộc gọi (lịch 08–18h), Biểu mẫu KHTN, Vị trí, Chú thích, Hình ảnh | sheet 05 liệt kê chính xác 5 cái này |
| **Đối tượng** | Chuyển từ chế độ **Quan sát** sang **Nhắm mục tiêu + điều chỉnh giá thầu** cho tệp có dữ liệu | sheet 05: "Chỉ ở chế độ Quan sát, chưa dùng để điều chỉnh giá thầu" |
| **Đối tượng** | Tạo & loại trừ tệp **đã đặt cọc / đã ký HĐMB** trên cả 6 chiến dịch | sheet 05: chưa loại trừ |
| **Đối tượng** | Tệp Khách hàng tương tự từ 18 khách đã cọc + 651 SQL → làm tín hiệu cho PMax | thay cho tín hiệu rác hiện tại |

### Tiêu chí dừng / mở rộng — GĐ1 (ngưỡng số cụ thể)

| Chiến dịch | **DỪNG / cắt** nếu | **MỞ RỘNG +20% ngân sách** nếu |
|---|---|---|
| SEA_Brand | CP/SQL > 1,5 tr trong 14 ngày | IS < 85% **và** CP/SQL < 1,0 tr — mở đến khi mất IS ngân sách = 0% |
| SEA_Generic | CP/SQL > 4,0 tr trong 21 ngày, hoặc Lead→SQL < 20% | CP/SQL < 2,6 tr **và** có ≥ 1 cọc trong 30 ngày |
| SEA_HighIntent | CP/SQL > 3,5 tr trong 30 ngày | CP/SQL < 2,2 tr sau 20 chuyển đổi |
| PMAX | SQL/Lead vẫn < 12% sau 30 ngày kể từ khi tín hiệu sạch → **cắt về 0** | SQL/Lead ≥ 20% **và** CP/SQL < 3,0 tr |
| GDN_Remarketing | CP/SQL > 4,0 tr trong 30 ngày | CP/SQL < 2,5 tr |
| **Toàn tài khoản** | Tỷ lệ Ads/CRM vẫn > 1,3x sau ngày 21 → **đóng băng mọi việc tăng ngân sách** cho tới khi sửa xong | — |
| Từ khóa lẻ | Cụm từ chi > 15 tr / 30 ngày mà 0 SQL → thêm phủ định ngay | Cụm từ có CP/SQL < 2,0 tr → tách thành nhóm riêng, đối sánh chính xác |

## C.2 — GIAI ĐOẠN 2 (Ngày 31–60): TỐI ƯU THEO TÍN HIỆU SẠCH

### Mục tiêu định lượng

| Chỉ tiêu | Mục tiêu GĐ2 | Cơ sở |
|---|---|---|
| Ngân sách | ≤ 725 tr (24,2 tr/ngày) | bảng C.0 |
| Lead thô | ≥ 688 | KB3 × 33% |
| SQL | ≥ 267 | KB3 × 33% |
| CP/SQL | ≤ 2,72 tr | 725/267 |
| Cọc | ≥ 11 (lũy kế ≥ 19) | 32 × 33% |
| ROAS GĐ2 | ≥ 2,75x | 11 × 181 / 725 |
| Tỷ lệ Ads/CRM | ≤ 1,10x | tiếp tục siết từ 1,15x |
| Lead gọi lại < 30 phút | ≥ 75% | từ 60% GĐ1 |
| % bản ghi CRM có GCLID | ≥ 95% | điều kiện để bật ECL |

### Cấu trúc & giá thầu

| Chiến dịch | Thay đổi GĐ2 | Điều kiện chuyển chiến lược |
|---|---|---|
| SEA_Brand | Từ Tỷ lệ hiển thị mục tiêu → **tCPA 700.000đ** khi IS ≥ 85% ổn định 14 ngày | Nếu tCPA làm IS tụt < 80% trong 7 ngày → quay lại Tỷ lệ hiển thị mục tiêu |
| SEA_Generic | Từ Tối đa nhấp có trần → **tCPA 1.100.000đ** (điều kiện: ≥ 30 chuyển đổi sạch/30 ngày) | Khi ECL chạy ≥ 30 ngày → chuyển sang **tCPA theo SQL ~2,4 tr** |
| SEA_HighIntent | Tối đa chuyển đổi → **tCPA** khi đủ 20 chuyển đổi | — |
| PMAX | **Chỉ tăng lên 100 tr nếu** SQL/Lead ≥ 20%. Nếu chưa đạt: giữ 60 tr, chuyển 40 tr sang Generic | ngưỡng cứng, không thương lượng |
| GDN | Tách 3 nhóm tệp (7 ngày / 8–30 ngày / xem bảng giá chưa gửi form) | — |
| YT_Video | **Khởi động lại 20 tr** với đo lường sạch, chỉ đo bằng **view-through + brand search lift**, KHÔNG đo bằng chuyển đổi nhấp cuối | sheet 10D: nhấp cuối dìm YT −74% |

### Kế hoạch đo lường — GĐ2

| # | Việc | Kiểm chứng |
|---|---|---|
| M1 | **Bật đường ống ECL (nhập chuyển đổi ngoại tuyến)**: upload SQL + Đặt cọc kèm GCLID và giá trị (SQL = 5 tr ước tính, Cọc = 181 tr) về Ads, tần suất **hằng ngày** | Ads hiển thị 2 hành động chuyển đổi ngoại tuyến, tỷ lệ khớp ≥ 70% |
| M2 | Triển khai **server-side GTM** (T9) | Chênh lệch client vs server ≤ 5% |
| M3 | Xây **báo cáo đối chiếu 3 nguồn tự động** (Looker Studio: Ads / GA4 / CRM), cập nhật hằng ngày | Ban giám đốc xem được 1 bảng duy nhất, không phải 3 |
| M4 | Bắt đầu **A/B test LP** thứ nhất (giả thuyết ưu tiên: rút form còn 2 trường SĐT+tên vs 3 trường) | Chạy đến khi đạt ý nghĩa thống kê hoặc 30 ngày |
| M5 | Kiểm tra lại tệp Search Partners: bật lại thử nghiệm 14 ngày trên 1 chiến dịch có đo riêng | Nếu CP/SQL > 3,5 tr → tắt vĩnh viễn |

### Trang đích / tiện ích / đối tượng — GĐ2
- Triển khai LP riêng cho nhà phố và căn hộ (mỗi LP một khoảng giá rõ ràng above-the-fold) — mục tiêu giảm "sai phân khúc" từ 18–34% xuống < 15%.
- Bật **Biểu mẫu khách hàng tiềm năng (lead form extension)** cho Brand — thử nghiệm, đo CP/SQL riêng.
- Tệp Khách hàng tương tự dựa trên 18+ khách đã cọc, dùng làm tín hiệu tệp cho PMax.
- Bật điều chỉnh giá thầu theo đối tượng: người đã xem `/bang-gia` +30%, người đã `form_start` chưa gửi +50%.

### Tiêu chí dừng / mở rộng — GĐ2

| Ngưỡng | Hành động |
|---|---|
| CP/SQL toàn tài khoản > 3,0 tr sau ngày 45 | Đóng băng ngân sách GĐ3 ở mức GĐ2, rà soát lại toàn bộ |
| Cọc lũy kế < 14 vào ngày 60 (so với mục tiêu 19) | Kích hoạt kịch bản D4 rút gọn: cắt PMax + GDN + YT về 0, dồn 100% cho Brand + Generic exact |
| Brand đạt IS ≥ 90% và mất IS ngân sách = 0% | Ngừng tăng Brand (đã chạm trần nhu cầu), chuyển phần tăng sang HighIntent |
| Bất kỳ chiến dịch nào chi > 60,3 tr chưa ra cọc | Rà soát bắt buộc (ngưỡng hòa vốn B5) |

## C.3 — GIAI ĐOẠN 3 (Ngày 61–90): MỞ RỘNG CÓ KIỂM SOÁT

### Mục tiêu định lượng

| Chỉ tiêu | Mục tiêu GĐ3 | Cơ sở |
|---|---|---|
| Ngân sách | ≤ 790 tr (26,3 tr/ngày) | bảng C.0 |
| Lead thô | ≥ 876 | KB3 × 42% |
| SQL | ≥ 340 | KB3 × 42% |
| CP/SQL | ≤ 2,33 tr | 790/340 |
| Cọc | ≥ 13 (**lũy kế ≥ 32**) | 32 × 42% |
| ROAS GĐ3 | ≥ 2,98x | 13 × 181 / 790 |
| **ROAS toàn kỳ 90 ngày** | **≥ 3,0x** | 32 cọc → 2,76x; **cần 35 cọc để chạm 3,0x** (xem B5) |
| Tỷ lệ Ads/CRM | ≤ 1,05x | — |
| Lead gọi lại < 30 phút | ≥ 85% | — |

### Cấu trúc & giá thầu
- **SEA_Brand**: tCPA theo SQL (mục tiêu ~1,8 tr/SQL). Nếu đã bịt hết mất IS ngân sách mà vẫn còn ngân sách → **không đẩy thêm**, chuyển sang HighIntent (Brand có trần nhu cầu tự nhiên, xem cảnh báo B4).
- **SEA_Generic**: **tCPA theo SQL** (dữ liệu ECL đã đủ 30+ ngày). Mở rộng nhóm exact có CP/SQL < 2,2 tr; nhóm thử nghiệm Rộng chỉ giữ nếu đã ra ≥ 5 SQL với CP/SQL < 3 tr.
- **SEA_HighIntent**: mở rộng lên 90 tr nếu CP/SQL < 2,2 tr.
- **PMAX**: chỉ lên 120 tr nếu SQL/Lead ≥ 20% và CP/SQL < 3,0 tr. Nếu không → cắt về 0, chuyển sang Generic + HighIntent.
- **YT_Video** 30 tr: chỉ giữ nếu đo được lift tìm kiếm thương hiệu.

### Kế hoạch đo lường — GĐ3
- **tROAS thử nghiệm** trên Generic sau khi ECL có ≥ 30 cọc tích lũy (hiện tại 18 cọc/90 ngày là **chưa đủ** cho tROAS — nói rõ: **không đủ dữ liệu** để chạy tROAS trước điểm này).
- Đối chiếu 3 nguồn: mục tiêu ba cột chênh ≤ 3%.
- Chốt A/B test LP #1, khởi động test #2 (giả thuyết: hiển thị bảng giá trực tiếp vs gate sau form).
- Báo cáo tổng kết: bảng phễu đầy đủ theo chiến dịch × giai đoạn, dùng đúng khuôn B3 để so sánh được với 90 ngày trước.

### Tiêu chí dừng / mở rộng — GĐ3

| Ngưỡng | Hành động |
|---|---|
| Cọc lũy kế ngày 75 < 24 | Dừng mọi thử nghiệm, dồn 100% ngân sách còn lại vào Brand + Generic exact + HighIntent |
| CP/SQL < 2,0 tr và Brand IS = 90% | Đề xuất ban giám đốc **cấp thêm ngân sách** — kèm bảng ROAS biên chứng minh |
| Bất kỳ chiến dịch nào ROAS < 1,0x trong 30 ngày | Cắt về 0, không thảo luận |
| Số lead/ngày > 60 | Cảnh báo vận hành: gần chạm ngưỡng SLA của 8 sale (96 lead/ngày công suất, nhưng thực tế SLA <30 phút chỉ giữ được ở ~60/ngày) |

## C.4 — Ba rủi ro của kế hoạch này (nói trước, không giấu)

| Rủi ro | Xác suất | Giảm thiểu |
|---|---|---|
| **KPI 32 cọc và KPI ROAS 3,0x mâu thuẫn nhau** (B5: 32 cọc = 2,76x; cần 35 cọc) | Chắc chắn — đây là mâu thuẫn số học | Chốt lại với ban giám đốc ngay tuần 1: hoặc mục tiêu 35 cọc, hoặc ngân sách 1.931 tr |
| **Brand có trần nhu cầu tự nhiên** — bịt hết mất IS chỉ thêm ~643 lead (A1), không đủ cho toàn bộ mức tăng | Cao | 220 tr cho HighIntent + mở rộng Generic exact làm nguồn tăng trưởng thứ hai; theo dõi IS Brand hằng tuần, dừng đẩy khi ≥ 90% |
| **Sửa đo lường làm cột Chuyển đổi tụt ~35%**, ban giám đốc hiểu nhầm là hiệu quả giảm | Cao | Báo cáo trước ngày 1: trình bảng B6, cam kết theo dõi bằng **Lead CRM và cọc**, không bằng cột Chuyển đổi. Chạy song song 7 ngày để chứng minh |

---

# PHẦN D — XỬ LÝ TÌNH HUỐNG

## D1. "Cắt hết ngân sách brand, dồn cho từ khóa chung"

**Trả lời: Không cắt. Ngược lại, tôi đề xuất tăng Brand từ 260,2 tr lên 560 tr. Nhưng anh nói đúng một nửa, và tôi sẽ chỉ ra nửa đó.**

**Bằng chứng phản đối việc cắt:**

| Chỉ số | SEA_Brand | SEA_Generic | Brand tốt hơn |
|---|---|---|---|
| Chi phí | 260,2 tr (14,4%) | 678,0 tr (37,6%) | Brand chi bằng **38%** Generic |
| **Đặt cọc** | **13** | 5 | **×2,6** |
| Doanh thu HH | 2.280 tr | 850 tr | ×2,7 |
| **ROAS** | **8,76x** | 1,25x | **×7,0** |
| CP/SQL | **0,74 tr** | 3,55 tr | rẻ hơn **4,8×** |
| CP/cọc | **20,0 tr** | 135,6 tr | rẻ hơn **6,8×** |
| Lead→SQL | 41,1% | 32,5% | +26% |
| Lead→Cọc | 1,52% | 0,85% | +79% |
| Lead dùng được (sheet 08C) | 67% | 46% | +46% |

**Bốn lập luận, mỗi cái một con số:**

1. **Cắt Brand không chuyển được ngân sách sang Generic một cách có lãi.** Generic đang ở ROAS 1,25x — dưới ngưỡng hòa vốn 3,0x. Chuyển 260 tr từ nơi ROAS 8,76x sang nơi ROAS 1,25x là **hủy khoảng 2.020 tr hoa hồng** (chênh lệch lãi tuyệt đối giữa hai chiến dịch).

2. **Brand đang không đủ tiền, chứ không thừa tiền.** IS Brand chỉ **53,4%**, mất **40,1% impression share vì hết ngân sách** (sheet 02). Nói cách khác: **gần một nửa số người đã chủ động gõ tên dự án của mình đang nhìn thấy quảng cáo của đối thủ, không phải của mình.** Benchmark sheet 09: IS thương hiệu < 60% = "mất khách đã biết mình".

3. **"Khách đã biết mình rồi" chính là lý do phải giữ, không phải lý do để cắt.** Sheet 04 cho thấy `vinhomes hóc môn giá bán` (46,8 tr → 78 SQL, CP/SQL 600k) và `dự án vinhomes hóc môn` (36,4 tr → 59 SQL, CP/SQL 617k) — đây là những người ở **cuối phễu**, sẵn sàng xem giá. Nhường vị trí này cho đại lý F2 khác đồng nghĩa với việc mình trả tiền Facebook/Zalo/telesale để tạo nhận biết rồi tặng lead cho đối thủ ở bước cuối.

4. **Nhưng anh đúng ở chỗ này — và tôi phải nói ra:** phân bổ nhấp cuối đang **thổi công Brand lên 32%**. Theo mô hình dựa trên dữ liệu (sheet 10D), Brand chỉ xứng đáng **401 lead** thay vì 592. Vì vậy tôi **không dùng số lead để bảo vệ Brand — tôi dùng số cọc**: 13/18 cọc là con số CRM ghi nhận, không phụ thuộc mô hình phân bổ nào cả. Và tôi sẽ đổi mô hình báo cáo sang "dựa trên dữ liệu" ngay trong GĐ1 (mục G6) để lần sau chúng ta tranh luận trên số đúng.

**Điều tôi đề xuất cắt thay vào đó — cùng số tiền, không rủi ro:** Competitor 176,7 tr (3 SQL, 0 cọc) + 243 tr từ khóa lạc trong Generic (0 SQL) = **419,7 tr**, đủ để vừa tăng Brand vừa tăng phần Generic thực sự có SQL.

**Nếu anh vẫn muốn kiểm chứng:** tôi đề xuất thử nghiệm có kiểm soát — tắt Brand **7 ngày** ở nhóm địa lý chiếm ~20% ngân sách (ví dụ Bình Tân + Củ Chi, sheet 06), giữ nguyên phần còn lại, rồi so sánh lead trực tiếp/organic + tổng cọc. Đây là cách duy nhất có bằng chứng, thay vì tranh luận niềm tin. Chi phí thử nghiệm: ~10 tr. Rủi ro: mất ~1 cọc trong tuần đó.

## D2. Đối thủ bắt đầu đấu giá trên tên thương hiệu dự án

**Bối cảnh số:** IS Brand hiện chỉ 53,4%, CTR Brand 11,63% (benchmark tốt > 12% — **đã tụt xuống dưới ngưỡng tốt**, sheet 09 ghi rõ "Giảm mạnh thường do đối thủ đấu giá"). CPC Brand 13.663đ. Đây là dấu hiệu đối thủ **đã** vào rồi, không phải sắp vào.

**Trong Google Ads — 4 hành động:**

| # | Hành động | Số cụ thể | Kỳ vọng đo được |
|---|---|---|---|
| 1 | **Bịt hết mất IS ngân sách Brand**: tăng 260,2 → 560 tr, chuyển sang **Tỷ lệ hiển thị mục tiêu 90% vị trí đầu trang** | Mất IS ngân sách 40,1% → 0% | IS 53,4% → ≥ 90% trong 14 ngày. Mỗi 1% IS lấy lại ≈ 16 lead ≈ 0,24 cọc |
| 2 | **Bật Auction Insights hằng tuần** cho SEA_Brand, xác định chính xác đại lý nào đang chồng lấn, ở mức overlap rate và position-above rate bao nhiêu | Hiện **chưa có dữ liệu này trong bộ đề** — cần lấy từ tài khoản thật, đây là dữ liệu thiếu | Có danh sách đối thủ + tần suất, làm cơ sở cho hành động 3 |
| 3 | **Tăng chất lượng để giảm chi phí phòng thủ**: mỗi nhóm Brand 2 RSA có tên dự án trong tiêu đề (Google cho phép quảng cáo dùng thương hiệu trong đích đến hợp lệ), thêm 5 tiện ích còn thiếu (Cuộc gọi, Biểu mẫu KHTN, Vị trí, Chú thích, Hình ảnh) → chiếm nhiều diện tích SERP hơn | Điểm chất lượng Brand hiện nằm trong mức TB tài khoản 5,2/10 | Ad Rank cao hơn với cùng CPC; CTR 11,63% → ≥ 14% |
| 4 | **Đấu giá phòng thủ chọn lọc, không đối đầu toàn diện**: chỉ giữ nhóm Brand exact/phrase; **KHÔNG** mở lại SEA_Competitor (dữ liệu 90 ngày đã chứng minh: 176,7 tr → 0 cọc, CP/SQL 58,92 tr = 26,8× KPI). Đồng thời loại trừ tên thương hiệu đối thủ khỏi PMax bằng **brand exclusion** (hiện CHƯA bật, sheet 05) | Competitor CP/SQL 58,92 tr | Không tái lập khoản lỗ 176,7 tr |

**Ngoài Google Ads — 4 hành động:**

| # | Hành động | Lý do gắn số |
|---|---|---|
| 1 | **Gửi khiếu nại vi phạm nhãn hiệu tới Google** (nếu chủ đầu tư Vinhomes đã đăng ký nhãn hiệu và ủy quyền cho An Phát Land) — Google gỡ được tên thương hiệu trong **nội dung quảng cáo** (không gỡ được từ khóa) | Chi phí 0đ, hiệu lực toàn cầu. Cần: giấy ủy quyền F1 từ chủ đầu tư — **chưa có trong dữ liệu**, phải xin |
| 2 | **Chiếm SEO cho truy vấn thương hiệu**: 9 cụm Brand trong sheet 04 tạo 54.597+ hiển thị/90 ngày cho riêng `vinhomes hóc môn`. Xây trang nội dung cho `vinhomes hóc môn giá bán`, `dự án vinhomes hóc môn có thật không` (cụm này chi 13,0 tr, chỉ 3 SQL — dấu hiệu khách đang lo ngại uy tín) | Kết quả tự nhiên hạng 1 làm giảm phụ thuộc vào đấu giá; 71 lead/90 ngày đã đến từ trực tiếp/organic (sheet 10D) |
| 3 | **Làm chủ Google Business Profile + Maps của nhà mẫu** (mở 08–18h mỗi ngày, sheet 01) và đẩy đánh giá thật | Tiện ích Vị trí đang thiếu (sheet 05); Maps là bề mặt đối thủ khó chiếm |
| 4 | **Rút ngắn SLA phản hồi xuống < 5 phút cho lead từ Brand** | Đây là lợi thế cạnh tranh mạnh nhất và rẻ nhất: sheet 08A cho thấy gọi < 5 phút có tỷ lệ cọc **1,82% vs 0,04%** khi gọi sau 12h — **gấp 45 lần**. Đối thủ có thể copy quảng cáo, không copy được tốc độ vận hành |

## D3. "PMax có CP/chuyển đổi thấp nhất, dồn ngân sách vào đó"

**Trả lời: KHÔNG đồng ý. Kế toán đang đọc đúng một con số nhưng con số đó được định nghĩa sai.**

**Bảng chứng minh — cùng một chiến dịch, bốn thước đo, bốn kết luận trái ngược:**

| Chiến dịch | CP/CĐ Ads | CP/Lead CRM | CP/SQL | CP/cọc | ROAS | Doanh thu |
|---|---|---|---|---|---|---|
| **PMAX** | **268k 🥇 rẻ nhất** | 573k (hạng 3) | **7,79 tr (hạng 5/6)** | **∞ — chưa từng có cọc** | **0,00x** | **0 đ** |
| SEA_Brand | 299k (hạng 2) | **304k 🥇** | **0,74 tr 🥇** | **20,0 tr 🥇** | **8,76x 🥇** | 2.280 tr |
| GDN_Remarketing | 430k | 674k | 3,61 tr | ∞ | 0,00x | 0 đ |
| YT_Video | 470k | 1.410k | 10,40 tr | ∞ | 0,00x | 0 đ |
| SEA_Generic | 1.021k | 1.155k | 3,55 tr | 135,6 tr | 1,25x | 850 tr |
| SEA_Competitor | 5.701k | 5.523k | 58,92 tr | ∞ | 0,00x | 0 đ |

**PMax hạng 1 ở CP/chuyển đổi, hạng 5/6 ở CP/SQL, hạng bét ở doanh thu (0 đồng trên 475,4 tr chi phí).**

**Tại sao "chuyển đổi" của PMax rẻ — bóc tách bằng số:**

1. **PMax được ghi công 1.775 chuyển đổi nhưng CRM chỉ nhận 829 lead** ⇒ tỷ lệ thổi phồng **2,14x**, vượt ngưỡng báo động 1,8x của sheet 09.
2. Phần lớn "chuyển đổi" PMax là **sự kiện rác**: PMax một mình chiếm `view_price_page` 438/612 (71,6%) và `engaged_30s` 259/361 (71,7%) của toàn tài khoản (sheet 10B). Nghĩa là PMax đang được thưởng cho việc đưa người vào trang rồi để họ ở lại 30 giây.
3. **Chất lượng lưu lượng:** thoát nhanh < 3 giây **74,3%**, thời lượng phiên trung vị **3 giây** (sheet 11B: "Bất thường — xem lại vị trí đặt quảng cáo"). Tỷ lệ tương tác 8,7% so với Brand 62,4%.
4. **Chất lượng lead:** chỉ **7% dùng được** (trùng SĐT 31%, SĐT sai 24%, sai phân khúc 34% — sheet 08C, mẫu 160 lead). Brand là 67%.
5. **28,0% nhấp trả tiền không tạo được phiên** (39.701 → 28.585) = 11.116 nhấp × 11.974đ = **133 tr trả cho lưu lượng không bao giờ đến trang**.
6. **Hệ quả tài chính:** nếu dồn thêm 500 tr vào PMax theo đề xuất của kế toán, theo tỷ lệ hiện tại ta mua thêm ~872 lead → ~64 SQL → **0 cọc**, và ROAS toàn tài khoản tụt từ 1,74x xuống ~1,36x.

**Nguyên nhân gốc và điều tôi làm thay vào đó:** PMax không "kém" — nó đang **học đúng theo tín hiệu ta dạy nó**. Ta bảo nó rằng "xem trang bảng giá" và "ở lại 30 giây" là chuyển đổi, nên nó đi tìm chính xác loại người đó. Sheet 12C viết nguyên văn: *"Máy học tối ưu theo tín hiệu rác — nguyên nhân gốc của toàn bộ vấn đề PMax"*.

**Kế hoạch:** giảm PMax 475,4 → 280 tr (−41%), **và không giải ngân phần này cho tới khi**: (a) chỉ còn `generate_lead` + `click_to_call` khử trùng là chuyển đổi, (b) bật brand exclusion + loại trừ vị trí đặt, (c) tệp tín hiệu = khách đã cọc/SQL. Sau 30 ngày đo lại: **SQL/Lead ≥ 20% thì tăng, < 12% thì cắt về 0.**

**Câu chốt cho kế toán:** *"Chúng ta không trả lương cho chuyển đổi. Chúng ta trả lương cho cọc. PMax đã mua 1.775 chuyển đổi với giá 475 triệu và giao về 0 cọc. Brand mua 871 chuyển đổi với giá 260 triệu và giao về 13 cọc trị giá 2,28 tỷ."*

## D4. Ngân sách bị cắt còn 1,2 tỷ cho 90 ngày

**Nguyên tắc cắt: giữ theo thứ tự ROAS đã chứng minh, cắt theo thứ tự lãng phí đã đo được. Không cắt đều theo tỷ lệ %.**

**Thứ tự cắt (từ cắt trước nhất):**

| Thứ tự | Cắt gì | Số tiền | Căn cứ số |
|---|---|---|---|
| **1** | **SEA_Competitor → 0** | −176,7 tr | 3 SQL, 0 cọc, CP/SQL 58,92 tr = 26,8× KPI. 26% lead là môi giới/đối thủ |
| **2** | **11 cụm từ lạc + toàn bộ đối sánh Rộng chưa có SQL** | −243 tr | sheet 04: 0 SQL trên 243 tr |
| **3** | **YT_Video → 0** | −83,2 tr | 0 cọc. *Ghi chú trung thực: sheet 10D cho thấy YT bị dìm −74% bởi nhấp cuối, giá trị thật có thể cao hơn — nhưng với ngân sách khẩn cấp, kênh đầu phễu không đo được là kênh cắt đầu tiên* |
| **4** | **Khu vực ngoài tệp** (HN, ĐN, ĐBSCL, ngoài VN) | −364 tr | 0 cọc trên 364 tr (sheet 06) |
| **5** | **Khung giờ 23h–06h + giảm 20–23h** | −146 tr | 0 cọc, gọi lại <30p chỉ 12–34% (sheet 07A) |
| **6** | **PMax xuống mức tối thiểu 120 tr** | −355 tr | 0 cọc; giữ 120 tr chỉ để kiểm chứng sau khi sạch tín hiệu |
| **7** | **GDN_Remarketing xuống 60 tr** | −70 tr | 0 cọc nhưng CP/SQL 3,61 tr còn chấp nhận được; remarketing rẻ và bổ trợ phễu |
| **8** | **Generic: chỉ giữ nhóm exact/phrase có SQL** | −248 tr | giữ lại các cụm có CP/SQL < 3,2 tr |
| **CUỐI CÙNG** | **SEA_Brand — giữ đến đồng cuối cùng, và vẫn TĂNG** | **+160 tr** | ROAS 8,76x, CP/cọc 20,0 tr, mất IS ngân sách 40,1% |

**Phân bổ 1,2 tỷ:**

| Chiến dịch | Ngân sách | % | Lý do |
|---|---|---|---|
| **SEA_Brand** | **420 tr** | 35,0% | Bịt hết mất IS ngân sách. Đây là khoản chi cuối cùng bị cắt trong mọi kịch bản |
| **SEA_Generic** (chỉ exact/phrase có SQL) | **430 tr** | 35,8% | Nguồn lead quy mô duy nhất còn lại |
| **SEA_HighIntent_DiXemNha** | **150 tr** | 12,5% | Ý định cuối phễu, chi phí thấp, cần cho đủ khối lượng cọc |
| **PMAX** (chỉ sau khi sạch tín hiệu) | **120 tr** | 10,0% | Kiểm chứng, không phải mở rộng |
| **GDN_Remarketing** | **60 tr** | 5,0% | Bổ trợ, rẻ |
| Dự phòng | **20 tr** | 1,7% | |
| **TỔNG** | **1.200 tr** | 100% | |

**Kết quả dự kiến (tính bằng script, theo kịch bản KB3, CP/SQL mục tiêu 2,60 tr):** 1.200 / 2,60 = **462 SQL → ~18,3 cọc → ROAS 2,76x**.

**Nói thẳng với ban giám đốc — ba câu:**
1. Với 1,2 tỷ, **KPI 32 cọc là bất khả thi.** Cam kết thực tế là **18–20 cọc, ROAS 2,7–3,0x**. ROAS được giữ vì phần cắt toàn là phần ROAS = 0.
2. Nghịch lý cần nêu: cắt 43% ngân sách chỉ làm mất ~2 cọc so với 90 ngày qua (18 cọc), **vì 71,3% ngân sách cũ đang không sinh cọc**. Đây là bằng chứng mạnh nhất cho luận điểm "vấn đề là phân bổ, không phải quy mô".
3. **Hai việc phải làm ngay bất kể ngân sách bao nhiêu** vì chi phí gần bằng 0 và giá trị đã đo được: sửa 3 lỗi LP (**471–612 tr HH**, B7) và siết SLA gọi lead < 30 phút (**+9,3 cọc ≈ 1.678 tr HH**, A2). Cộng lại lớn hơn toàn bộ phần ngân sách bị cắt.

## D5. Trả lời sếp: "GA4 báo 3.820, CRM báo 2.557. Ai đúng?" *(≤ 150 từ, ngôn ngữ phi kỹ thuật)*

> Cả hai đều "đúng" — nhưng chúng đếm hai thứ khác nhau.
>
> Con số 3.820 của Google đang đếm cả những hành động **không phải khách hàng**: 612 lượt chỉ mở trang bảng giá, 361 lượt chỉ ở lại trang 30 giây, và 353 lượt là **cùng một người bấm gọi nhiều lần**. Trừ hết đi còn **2.494**. Cộng thêm 63 khách của ba ngày hệ thống bị lỗi kỹ thuật không ghi nhận được, ta ra đúng **2.557** — con số CRM.
>
> **Anh nhìn CRM.** Đó là số người thật sale gọi được. Và thực ra hãy nhìn xa hơn một bước nữa: **18 giao dịch đặt cọc và 3,13 tỷ hoa hồng**. Đó mới là thứ trả lương cho cả công ty.
>
> Trong 30 ngày tới tôi sẽ sửa để Google chỉ đếm khách thật. Cột "chuyển đổi" sẽ tụt khoảng 35% — **đó là dấu hiệu tốt**, không phải hiệu quả giảm.

*(148 từ)*

## D6. "Sửa GTM không tạo ra lead nào, để cuối quý"

**Phản biện — bốn con số, không dùng một chữ kỹ thuật nào:**

1. **Đo lường sai đang trực tiếp đốt 475,4 triệu.** Google tự động dồn tiền về nơi có nhiều "chuyển đổi". Ta đang bảo nó rằng "người mở trang bảng giá" là khách hàng, nên nó đi mua đúng loại người đó: PMax chi 475,4 tr, giao về **0 cọc**. Đó không phải lỗi của PMax — đó là lỗi của cái thước ta đưa cho nó. Sheet 12 viết nguyên văn: *"Máy học tối ưu theo tín hiệu rác — nguyên nhân gốc của toàn bộ vấn đề PMax."*

2. **Có lỗi đang chảy máu lead ngay lúc này, mỗi ngày.** Lỗi form trên iPhone Safari khiến khách bấm gửi mà form không đi, **và không hiện báo lỗi nào cho khách** — họ tưởng đã đăng ký. 4.196 phiên bị ảnh hưởng, ước tính **370–480 lead/90 ngày = 4,1–5,3 lead/ngày**. Mỗi tuần trì hoãn = **29–37 lead = 20–26 triệu tiền quảng cáo đã trả nhưng không thu được gì**. Đợi đến cuối quý (giả sử 8 tuần) = **160–208 triệu**.

3. **Chuyện này đã xảy ra rồi và ta mất 3 ngày mới biết.** Ngày 44 một thay đổi giao diện làm gãy hệ ghi nhận. Chuyển đổi về 0 suốt 3 ngày, ta vẫn chi **59,5 triệu** chạy mù, và **63 khách hàng thật vĩnh viễn không có trong hệ thống**. Không ai phát hiện vì **không có cảnh báo tự động** — thứ mất 30 phút để cài.

4. **Tăng ngân sách trước khi sửa đo lường là đổ thêm dầu vào đúng cái lỗ.** Mỗi đồng thêm vào hôm nay sẽ được phân bổ theo cùng tín hiệu sai đã tạo ra 71,3% ngân sách không sinh cọc. Trình tự đúng là: sửa thước (2 tuần) → đo lại → rồi mới tăng tiền. **Đảo trình tự này làm hỏng cả hai.**

**Nếu buộc phải nhượng bộ — tôi giữ đúng HAI hạng mục:**

| # | Hạng mục giữ lại | Công sức | Giá trị định lượng | Vì sao là hai cái này |
|---|---|---|---|---|
| **1** | **Bỏ `view_price_page` (612) và `engaged_30s` (361) khỏi danh sách chuyển đổi + khử trùng `click_to_call` (−353)** | **< 1 giờ**, làm trong giao diện GA4, **không cần dev, không cần deploy** | Làm sạch **1.326/3.820 = 34,7% tín hiệu**; trực tiếp chặn đường 475,4 tr chảy vào PMax | Đây là **nguyên nhân gốc** của khoản lãng phí lớn nhất. Không đụng vào code, không rủi ro, và một mình nó xoay chuyển cách toàn bộ ngân sách được phân bổ |
| **2** | **Cài biến ẩn lưu GCLID vào form + đẩy vào CRM** | **2–4 giờ dev**, một lần | Mở khóa toàn bộ khả năng nhập chuyển đổi ngoại tuyến ⇒ điều kiện **bắt buộc** để đấu thầu theo SQL/cọc thay vì theo lead thô | Đây là hạng mục **có độ trễ dài nhất**: cần tích lũy ≥ 30 ngày dữ liệu trước khi Smart Bidding dùng được. Hoãn 1 tuần ở đây làm trễ 1 tuần **toàn bộ** lộ trình tối ưu theo chất lượng. Mọi hạng mục khác đều có thể làm sau và bù kịp |

**Hai cái này = tổng ~5 giờ công.** Tôi chấp nhận hoãn: server-side GTM, Consent Mode, dọn 34 thẻ, gắn Clarity ID vào CRM, đổi mô hình phân bổ.

**Nhưng có một cái tôi từ chối hoãn dù ngoài phạm vi GTM:** sửa 3 lỗi trang đích (#4, #5, #6). Đó không phải "đo lường" — đó là **form đang hỏng, khách bấm gửi mà không gửi được**. 20–26 triệu mỗi tuần.

---

# PHẦN E — KẾ HOẠCH 7 NGÀY ĐẦU

10 việc, sắp theo **thứ tự ưu tiên** (= giá trị chặn được chia cho công sức). Mỗi việc có kết quả kỳ vọng **đo được** và cách kiểm chứng.

| # | Ngày | Việc | Kết quả kỳ vọng đo được | Cách kiểm chứng |
|---|---|---|---|---|
| **1** | **N1 (sáng)** | **Cắt máu ngay — 3 việc trong 2 giờ:** (a) tạm dừng `SEA_Competitor_DoiThu`; (b) thêm 11 từ khóa phủ định của các cụm lạc (`tuyển dụng`, `thuê`, `nhà trọ`, `kho xưởng`, `việc làm`, `lừa đảo`, `quy hoạch`, `học phí`, `chung cư mini`, `thổ cư`, `giá đất`) vào **danh sách phủ định chia sẻ**; (c) loại trừ địa lý Hà Nội / Đà Nẵng / ĐBSCL / ngoài VN, đổi tùy chọn vị trí sang "Chỉ hiện diện" | Ngừng chảy **~2,0 tr/ngày** (176,7+243+364 = 783,7 tr / 90 ngày = 8,7 tr/ngày, phần cắt ngay ≈ 2,0 tr/ngày sau khi trừ chồng lấn). % chi phí ngoài TP.HCM/BD/LA: 29,9% → **< 10%** trong 7 ngày | Báo cáo Vị trí + Cụm từ tìm kiếm ngày 7 |
| **2** | **N1 (chiều)** | **Xóa thẻ `GA4 Configuration – Copy of Main`** + **cài cảnh báo tự động khi chuyển đổi = 0 trong 6 giờ giờ hành chính** (GA4 Custom Insight + Ads Rule → email/Slack) | `page_view` bắn **đúng 1 lần**/trang (hiện 2 lần từ ngày 31). Có ít nhất 1 cảnh báo hoạt động — test bằng cách tắt thẻ trên staging, phải nhận cảnh báo trong ≤ 6 giờ | GTM Preview mode + email test |
| **3** | **N1–N2** | **Làm sạch cột Chuyển đổi:** bỏ đánh dấu sự kiện chính cho `view_price_page` (612) và `engaged_30s` (361); đổi `click_to_call` sang đếm **1 lần/phiên**. Ghi lại số cũ để chạy song song 7 ngày | Cột Chuyển đổi giảm ~**34,7%** (3.820 → ~2.494 quy đổi). Tỷ lệ Ads/CRM từ **1,49x → ≤ 1,20x** trong 7 ngày | Bảng đối chiếu 3 nguồn (khuôn B6) ngày 7 |
| **4** | **N1–N3** | **Brief dev sửa 3 lỗi LP chưa sửa:** #4 `TypeError e.setDate` Safari iOS 17.x (4.196 phiên), #5 nút CTA bị khung chat che < 380px (2.741 phiên), #6 hotline `tel:` trên desktop (1.204 phiên) | Tỷ lệ phiên có lỗi JS di động trên Clarity: **8,9% → < 2%**. Tỷ lệ hoàn tất form di động v2: 24,6% → **≥ 30%**. Thu lại **4,1–5,3 lead/ngày** | Clarity + GA4 `form_start`/`generate_lead` ngày 7 và ngày 14 |
| **5** | **N1–N3** | **Tăng ngân sách Brand 4,5 → 6,2 tr/ngày, đổi sang Tỷ lệ hiển thị mục tiêu 90% vị trí đầu trang, trần CPC 20.000đ**; bỏ toàn bộ từ khóa đối sánh Rộng trong Brand | Impression Share Brand **53,4% → ≥ 75%** trong 7 ngày. Mất IS ngân sách **40,1% → ≤ 10%**. CP/SQL Brand giữ **< 1,2 tr** | Cột Impr. Share + Mất IS (ngân sách) hằng ngày |
| **6** | **N2–N5** | **Cài biến ẩn lưu GCLID/GBRAID/WBRAID + UTM vào form, đẩy sang CRM** (đường ống ECL bắt đầu tích lũy) | **≥ 90% bản ghi CRM mới (từ N5) có trường `gclid` không rỗng.** Bắt đầu đếm ngược 30 ngày để bật đấu thầu theo SQL | Truy vấn CRM: đếm bản ghi có gclid / tổng bản ghi mới, ngày 7 |
| **7** | **N2–N4** | **Đổi điều kiện kích hoạt `generate_lead` từ class CSS sang `dataLayer.push`** do dev bắn khi server trả về thành công | Test đổi giao diện trên staging → thẻ **vẫn kích hoạt**. Loại bỏ vĩnh viễn nguy cơ lặp lại sự cố N44–46 (59,5 tr chạy mù + 63 lead mất) | Tag Assistant trên 4 thiết bị (Android Chrome, iOS Safari 17, desktop Chrome, iPad) |
| **8** | **N2 (họp 60 phút)** | **Họp với trưởng phòng kinh doanh — chốt SLA lead:** phân lead tự động, gọi trong **15 phút giờ hành chính**, mọi lead đều có người nhận (hiện 275 lead không ai gọi). Trình bảng sheet 08A: gọi <5 phút cọc **1,82%** vs sau 12h **0,04%** | Tỷ lệ lead gọi lại < 30 phút: **30% → ≥ 50%** trong 7 ngày. Số lead không ai gọi: **0**. Đây là đòn bẩy **+9,3 cọc ≈ 1.678 tr HH** không tốn tiền quảng cáo | Báo cáo CRM thời gian phản hồi trung vị, đo hằng ngày |
| **9** | **N3–N5** | **Tái cấu trúc PMax:** bật **brand exclusion**, thêm danh sách loại trừ vị trí đặt (app/game/nội dung video rác), đổi tệp tín hiệu sang khách đã cọc + SQL, đặt **tCPA 1,2 tr** (hiện thả nổi), giảm ngân sách xuống 2,0 tr/ngày | Thoát nhanh < 3s của PMax: **74,3% → < 50%**. Hao hụt nhấp→phiên: **28,0% → < 15%**. SQL/Lead: 7,4% → **≥ 12%** trong 30 ngày (chưa kỳ vọng đạt trong 7 ngày) | Clarity mục B + GA4 mục B, đo lại ngày 7, 14, 30 |
| **10** | **N5–N7** | **Đặt lịch quảng cáo & điều chỉnh giá thầu theo thời gian:** tắt 23h–06h; giảm 40% khung 20–23h; T7-CN **−30%**; T3-T4 **−15%**. Song song: bật 5 tiện ích còn thiếu (Cuộc gọi 08–18h, Biểu mẫu KHTN, Vị trí, Chú thích, Hình ảnh) | Giải phóng **~146 tr/90 ngày** từ khung giờ 0 cọc, tái phân bổ về 09–12h & 14–17h (2 khung có CP/SQL thấp nhất: 2,50 và 2,64 tr). CTR toàn tài khoản tăng ≥ 15% nhờ tiện ích | Báo cáo Khung giờ + Ngày trong tuần, đo ngày 14 |

### Bảng kiểm cuối tuần 1 (thứ 2 tuần 2 — báo cáo lên ban giám đốc)

| Chỉ số | Trước (baseline 90 ngày) | Mục tiêu cuối N7 | Nguồn kiểm chứng |
|---|---|---|---|
| Tỷ lệ Chuyển đổi Ads / Lead CRM | 1,49x | **≤ 1,20x** | Bảng đối chiếu 3 nguồn (khuôn B6) |
| Impression Share Brand | 53,4% | **≥ 75%** | Ads, cột Impr. Share |
| Mất IS ngân sách Brand | 40,1% | **≤ 10%** | Ads |
| % chi phí ngoài TP.HCM/BD/LA | 29,9% | **< 10%** | Báo cáo Vị trí |
| Lỗi JS trên di động (Clarity) | 8,9% | **< 2%** | Clarity |
| Lead gọi lại < 30 phút | 30% | **≥ 50%** | CRM |
| Lead không ai gọi | 275/90 ngày (~3,1/ngày) | **0** | CRM |
| % bản ghi CRM có GCLID | 0% | **≥ 90%** (từ N5) | CRM |
| Cảnh báo chuyển đổi = 0 | Không có | **Đang hoạt động, đã test** | Email/Slack |
| Chi phí/ngày | 20,0 tr | 19,5 tr (theo kế hoạch GĐ1) | Ads |

**Việc KHÔNG làm trong tuần 1 (và lý do):**
- **Không đổi chiến lược giá thầu Generic.** Dữ liệu chuyển đổi đang bị nhiễm 34,7%; đổi sang Smart Bidding lúc này là dạy máy học theo tín hiệu rác lần thứ hai. Đợi đến ngày 15 khi tín hiệu đã sạch 14 ngày.
- **Không tăng tổng ngân sách.** GĐ1 chủ động chi 19,5 tr/ngày, thấp hơn mức cũ 20,0 tr/ngày. Tăng tiền trong lúc hệ đo đang được thay là cách chắc chắn nhất để không bao giờ biết cái gì đã hiệu quả.
- **Không cắt YouTube vĩnh viễn.** Sheet 10D cho thấy nhấp cuối dìm YT −74%; tạm dừng để tiết kiệm, đánh giá lại ở GĐ2 bằng thước đo khác (view-through + brand search lift).

---

## PHỤ LỤC — DỮ LIỆU CÒN THIẾU ĐỂ KẾT LUẬN CHẮC CHẮN HƠN

Theo yêu cầu "nếu không đủ dữ liệu phải nói rõ":

| # | Thiếu gì | Cần cho việc gì | Không có thì hệ quả |
|---|---|---|---|
| 1 | **Auction Insights** (overlap rate, position above rate, outranking share) | D2 — xác định đối thủ nào đấu giá brand và mạnh đến đâu | Chỉ suy ra gián tiếp từ CTR 11,63% tụt dưới ngưỡng tốt 12% |
| 2 | **Bid Simulator / dữ liệu đường cong lợi suất giảm dần** | A1 — ước tính chính xác lợi ích của việc bịt mất IS ngân sách | Phải ngoại suy tuyến tính (+9,8 cọc), biết là cận trên, cận dưới ~5–6 cọc |
| 3 | **Dữ liệu kênh khác** (Facebook, Zalo, telesale, sàn F2) — sheet 01 nói rõ "KHÔNG nằm trong dữ liệu này" | Đánh giá đóng góp thật của Brand: bao nhiêu nhu cầu tìm kiếm tên dự án do kênh khác tạo ra | Không thể tính chi phí tạo nhu cầu thật; D1 chỉ lập luận trong phạm vi Google Ads |
| 4 | **Holdout / A/B test cấp chiến dịch** | Tách riêng đóng góp của LP v2, SLA gọi 15 phút, và sự kiện mở bán trong mức tăng ROAS GĐ3 (0,60 → 2,98x) | Không thể quy công chính xác cho quảng cáo; đã ghi rõ ở B2 |
| 5 | **Báo cáo vị trí đặt (placement) của PMax & GDN** | A4 — xác định chính xác nguồn nào tạo ra thoát nhanh 74,3% | Chỉ biết "có vấn đề", chưa biết loại trừ cái gì cụ thể |
| 6 | **Điểm chất lượng theo từng từ khóa** (chỉ có bình quân 5,2/10) | Ưu tiên tối ưu từ khóa nào trước | Phải dùng CP/SQL làm thước thay thế |
| 7 | **Giấy ủy quyền nhãn hiệu từ chủ đầu tư** | D2 — khiếu nại vi phạm nhãn hiệu lên Google | Không thể thực hiện hành động rẻ nhất trong bộ 8 hành động của D2 |
| 8 | **Cơ cấu giá của 18 cọc** (nhà phố 6,8–11,5 tỷ vs căn hộ 2,9–4,6 tỷ) | Giải thích vì sao HH thực tế 173,9 tr < 181 tr giả định; phân bổ ngân sách theo dòng sản phẩm | Phải dùng bình quân, không tối ưu được theo dòng sản phẩm có hoa hồng cao hơn |

---

**Hết bài. Mọi con số truy ngược được về `answers/agent-1-calc.py`.**
