# BÁO CÁO TIẾP QUẢN TÀI KHOẢN GOOGLE ADS — VINHOMES HÓC MÔN
**Vai trò:** Performance Marketing Lead, An Phát Land · **Kỳ dữ liệu:** 02/03/2026 – 30/05/2026 (90 ngày)
**Nguồn số:** `02_DU_LIEU_NGAY` (486 dòng = 81 ngày×6 CD có phát sinh + ngày YT chưa chạy), `03`–`12`
**Mọi con số dưới đây sinh từ** `answers/agent-4-calc.py` (log đầy đủ: `answers/agent-4-calc.out.txt`). Không có số nào nhập tay.

## Bảng nền — trạng thái tài khoản so với KPI 90 ngày tới

| Chỉ tiêu | Thực tế 90 ngày qua | KPI 90 ngày tới | Khoảng cách |
|---|---|---|---|
| Chi phí | 1.803.537.000đ | ≤ 2.100.000.000đ | còn dư 296,5tr (85,9% hạn mức) |
| Đặt cọc | **18** | ≥ 32 | cần ×1,78 |
| Doanh thu HH | 3.130.000.000đ | — | — |
| ROAS | **1,74x** | ≥ 3,0x | cần ×1,73 |
| CP/SQL | **2.770.410đ** | ≤ 2.200.000đ | cần giảm 20,6% |
| CP/cọc | 100.196.500đ | ≤ 60.333.333đ (B5) | cần giảm 39,8% |

*(script `agg(rows)`, khối "B0"/"PACING & NGÂN SÁCH")*

---

# PHẦN A — CHẨN ĐOÁN

18 vấn đề, sắp theo tác động tài chính giảm dần. Vấn đề **#1, #9, #10, #11, #12, #16, #17** thuộc nhóm đo lường/kỹ thuật (yêu cầu tối thiểu 3 — đạt 7).

---

### A-1. [ĐO LƯỜNG] Cột "Chuyển đổi" đang đếm 2 sự kiện không phải khách hàng + đếm trùng lượt gọi → máy học tối ưu theo tín hiệu rác
**Mức độ: CAO — đây là nguyên nhân GỐC của #2, #5 và của toàn bộ việc phân bổ ngân sách sai**

| Thành phần cột "Chuyển đổi" | Lượt | % tổng 3.820 | Có phải lead? |
|---|---:|---:|---|
| generate_lead | 1.715 | 44,9% | Có |
| click_to_call (tổng lượt) | 1.132 | 29,6% | Có, nhưng chưa khử trùng |
| view_price_page | 612 | 16,0% | **KHÔNG** |
| engaged_30s | 361 | 9,4% | **KHÔNG** |

- Nguồn: `10_GA4` mục A & E; `12_GTM` mục A thẻ #5, #6 ("ĐANG được đánh dấu là sự kiện chính và nhập vào Ads"); `05_CAU_HINH_TK` — 4 hành động chuyển đổi chính đều BẬT.
- **1.326/3.820 = 34,7% tín hiệu Google học được là sai** (973 rác + 353 lượt gọi trùng). Tỷ lệ thổi phồng CĐ_Ads/Lead_CRM = **1,49x** toàn tài khoản; riêng PMax **2,14x** (`03_TONG_HOP_CD`, cột "Chênh lệch Ads vs CRM"; benchmark báo động >1,8x — `09_BENCHMARK`).
- **Tiền lãng phí:** chiến lược "Tối đa hóa chuyển đổi" của PMax được lái bằng đúng tập tín hiệu rác này. PMax tiêu **475.376.000đ**, 0 cọc. Tối thiểu quy trách nhiệm cho A-1: **~353.204.368đ** (phần chi phí PMax rơi vào phiên thoát <3 giây, xem A-2). `12_GTM` mục C ghi thẳng: *"Máy học tối ưu theo tín hiệu rác — nguyên nhân gốc của toàn bộ vấn đề PMax"*.

---

### A-2. PMax tiêu 26,4% ngân sách, sinh 0 cọc, chất lượng lead thấp nhất tài khoản
**Mức độ: CAO — lãng phí 353–475 triệu đồng**

| Chỉ số PMax | Giá trị | Đối chiếu |
|---|---:|---|
| Chi phí 90 ngày | 475.376.000đ (26,4% tài khoản) | `02` SUM |
| CĐ_Ads → Lead CRM → SQL → Đi xem → Booking → Cọc | 1.775 → 829 → 61 → 10 → 2 → **0** | `02` SUM |
| SQL/Lead | **7,4%** | `09_BENCHMARK`: <12% = "nhắm sai tệp" |
| CP/SQL | **7.793.049đ** | benchmark báo động >5tr |
| Thoát nhanh <3s | **74,3%**, thời lượng phiên trung vị **3 giây** | `11_CLARITY` mục B — ghi chú "Bất thường — xem lại vị trí đặt quảng cáo" |
| Hao hụt nhấp→phiên | 28,0% (39.701 nhấp → 28.585 phiên) | `10_GA4` mục B; sheet ghi rõ "Với PMax thì không [bình thường]" |
| Tỷ lệ hoàn tất form | 14,0% (3.643 form_start → 510 lead) | `10_GA4` mục B |
| Lead dùng được (mẫu 160) | **7%**; trùng SĐT 31%; SĐT sai 24%; sai phân khúc 34% | `08_CRM_VAN_HANH` mục C |
| Doanh thu | **0đ** | — |

- Nguyên nhân đồng thời: (a) tín hiệu tối ưu rác (A-1); (b) `05_CAU_HINH_TK` — PMax **chưa thiết lập danh sách loại trừ vị trí đặt** và **chưa bật brand exclusion**. 74,3% phiên thoát dưới 3 giây + 3.643 form_start nhưng chỉ 510 lead là chân dung điển hình của lưu lượng bot/mis-click từ vị trí đặt kém chất lượng.
- **Tiền lãng phí:** 475.376.000đ × 74,3% = **353.204.368đ** là mức thấp; nếu đánh giá theo kết quả cuối phễu (0 cọc, 0đ doanh thu) thì toàn bộ **475.376.000đ** không tạo giá trị đo được.

---

### A-3. Chiến dịch Brand — ROAS 8,76x nhưng bị bỏ đói ngân sách, mất 39,7% impression share vì hết tiền
**Mức độ: CAO — doanh thu bỏ lỡ ước tính lên tới ~1,75 tỷ (trần trên)**

| Chiến dịch | Chi phí | % NS | Cọc | Doanh thu | ROAS | CP/SQL |
|---|---:|---:|---:|---:|---:|---:|
| SEA_Brand | 260.219.000 | 14,4% | **13** | 2.280.000.000 | **8,76x** | 739.259 |
| SEA_Generic | 677.994.000 | 37,6% | 5 | 850.000.000 | 1,25x | 3.549.707 |
| PMAX | 475.376.000 | 26,4% | 0 | 0 | 0 | 7.793.049 |
| SEA_Competitor | 176.746.000 | 9,8% | 0 | 0 | 0 | 58.915.333 |
| GDN_Remarketing | 130.009.000 | 7,2% | 0 | 0 | 0 | 3.611.361 |
| YT_Video | 83.193.000 | 4,6% | 0 | 0 | 0 | 10.399.125 |

- Brand chỉ ăn **14,4% ngân sách** nhưng đem **72,2% số cọc (13/18)** và **72,8% doanh thu**.
- Impression share Brand (bình quân gia quyền theo hiển thị, `02` cột `Impr_Share`/`Mat_IS_NganSach`/`Mat_IS_ThuHang`): **IS 53,4%**, **mất IS do ngân sách 39,7%**, mất do thứ hạng 6,9%. Benchmark `09`: IS brand tốt >85%, **mất IS do ngân sách >20% = báo động**. Ổn định xấu suốt 3 giai đoạn (39,1% / 41,9% / 38,7%).
- **Ước tính doanh thu bỏ lỡ (nêu rõ đây là ngoại suy tuyến tính, KHÔNG phải số đo):** bù hết phần mất IS do ngân sách ⇒ +14.182 nhấp ⇒ theo tỷ lệ cọc/nhấp lịch sử của Brand (13/19.045) ⇒ **+9,7 cọc ≈ 1.752.179.960đ doanh thu**, đổi lấy ~193.774.125đ chi phí tăng thêm. Đây là **trần trên** — thực tế đường cong IS phi tuyến, chi phí biên tăng dần; con số dùng để xếp hạng ưu tiên, không dùng để cam kết.

---

### A-4. Generic chạy đối sánh rộng không kiểm soát — 242.982.000đ đổ vào cụm từ sai ý định, 0 SQL
**Mức độ: CAO — lãng phí 242.982.000đ trực tiếp, có thể tới 419.729.000đ**

- `04_SEARCH_TERMS`: **17/32 cụm từ có chi phí nhưng 0 SQL, tổng 419.729.000đ = 37,6%** chi phí của các cụm được liệt kê.
- Trong đó **11 cụm sai ý định rõ ràng (100% đối sánh Rộng, 100% có 0 SQL) = 242.982.000đ**:

| Cụm từ | Đối sánh | Chi phí | SQL |
|---|---|---:|---:|
| giá đất hóc môn 2026 | Rộng | 33.900.000 | 0 |
| bản đồ quy hoạch hóc môn | Rộng | 27.120.000 | 0 |
| thuê nhà nguyên căn hóc môn | Rộng | 27.120.000 | 0 |
| bán đất thổ cư hóc môn 100 triệu | Rộng | 27.120.000 | 0 |
| nhà trọ hóc môn giá rẻ | Rộng | 20.340.000 | 0 |
| cho thuê kho xưởng hóc môn | Rộng | 20.340.000 | 0 |
| việc làm bất động sản hóc môn | Rộng | 20.340.000 | 0 |
| nhà đất hóc môn lừa đảo | Rộng | 20.340.000 | 0 |
| chung cư mini gò vấp | Rộng | 20.340.000 | 0 |
| vinhomes hóc môn tuyển dụng | Rộng | 15.613.000 | 0 |
| vinschool hóc môn học phí | Rộng | 10.409.000 | 0 |

- Nguyên nhân cấu hình (`05_CAU_HINH_TK`): **71% chi phí Search từ đối sánh rộng**, chỉ 9% từ chính xác; **toàn tài khoản chỉ có 12 từ khóa phủ định**, không dùng danh sách phủ định chia sẻ; giá thầu Generic là **"Tối đa hóa số lần nhấp, không đặt trần CPC"** — chiến lược mua nhấp chứ không mua lead. Hệ quả: CPC Generic **33.070đ** (`09_BENCHMARK` xếp 25–45k = trung bình, nhưng với 0 SQL thì mọi mức CPC đều đắt), 31 từ khóa/nhóm + 1 RSA/nhóm, Điểm chất lượng 5,2/10.

---

### A-5. Chiến dịch Competitor: 176.746.000đ → 3 SQL → 0 cọc
**Mức độ: CAO — lãng phí gần trọn 176.746.000đ**

| Chỉ số | Giá trị | Benchmark `09` |
|---|---:|---|
| Chi phí | 176.746.000đ (9,8% NS) | — |
| CPC | **55.164đ** | >60.000đ = báo động; gấp 4x Brand (13.663đ) |
| SQL toàn kỳ | **3** | — |
| CP/SQL | **58.915.333đ** | >5tr = báo động (gấp 11,8 lần ngưỡng) |
| Cọc / doanh thu | 0 / 0đ | — |
| Thoát nhanh <3s | 34,1%, phiên trung vị 47s, "Ý định thấp" | `11_CLARITY` mục B |
| Lead dùng được (mẫu 40) | **26%**, trong đó **26% là môi giới/đối thủ** | `08` mục C |

- `04_SEARCH_TERMS`: cả **6 cụm từ competitor (176.747.000đ) đều 0 SQL** — không có ngoại lệ nào cứu được chiến dịch này.

---

### A-6. 24,1% ngân sách bắn ra ngoài vùng bán được — 434.652.417đ, 0 cọc
**Mức độ: CAO — lãng phí 434.652.417đ**

| Khu vực | Chi phí | SQL | CP/SQL | Cọc |
|---|---:|---:|---:|---:|
| Hà Nội | 155.104.182 | 20 | 7.755.209 | 0 |
| Cần Thơ & ĐBSCL | 93.783.924 | 12 | 7.815.327 | 0 |
| Đà Nẵng | 86.569.776 | 7 | **12.367.111** | 0 |
| Đồng Nai | 70.337.943 | 14 | 5.024.139 | 0 |
| Ngoài Việt Nam (quan tâm đến VN) | 28.856.592 | 7 | 4.122.370 | 0 |
| **Cộng** | **434.652.417 (24,1%)** | **60** | — | **0** |
| Đối chiếu: TP.HCM | 1.076.711.589 (59,7%) | 482 | — | **17/18** |

- Nguồn `06_DIA_LY`. Nguyên nhân `05_CAU_HINH_TK`: nhắm mục tiêu **"Việt Nam (toàn quốc)"** cho cả 6 chiến dịch, **tùy chọn vị trí để mặc định "Hiện diện HOẶC quan tâm"** (chính là lý do có 28,8tr chi cho người ngoài VN), **không có loại trừ vị trí nào**.

---

### A-7. Vận hành sale: 275 lead không ai gọi, chỉ 11% lead được gọi trong 5 phút
**Mức độ: CAO — trực tiếp mất 193.966.631đ chi phí lead + tác động cọc rất lớn**

`08_CRM_VAN_HANH` mục A — mối quan hệ tốc độ gọi ↔ tỷ lệ cọc:

| Thời gian gọi lần đầu | Số lead | % | Liên hệ được | Đi xem | **Tỷ lệ cọc** |
|---|---:|---:|---:|---:|---:|
| <5 phút | 281 | 11% | 87% | 23,1% | **1,82%** |
| 5–30 phút | 485 | 19% | 74% | 15,4% | 1,21% |
| 30ph–2h | 588 | 23% | 58% | 8,6% | 0,58% |
| 2–12h | 536 | 21% | 41% | 4,2% | 0,21% |
| >12h / hôm sau | 664 | **26%** | 22% | 1,1% | **0,04%** (thấp hơn 45 lần) |

- Số cọc kỳ vọng theo phân bố hiện tại = **15,8**; nếu 100% lead được gọi <5 phút = **46,5** ⇒ chênh **30,7 cọc ≈ 5.556.428.500đ**. *(Đây là **trần trên lý thuyết** — giả định tỷ lệ cọc 1,82% giữ nguyên khi mở rộng cho toàn bộ lead, điều không chắc vì nhóm gọi nhanh có thể là nhóm lead tốt nhất. Nêu để định lượng độ lớn của đòn bẩy, không phải cam kết.)*
- **Số đo chắc chắn:** `08` mục B — **118 + 96 + 61 = 275 lead không ai gọi**, giá trị theo CPL_CRM thực tế 705.333đ = **193.966.631đ vứt đi**.
- Xu hướng đang cải thiện: thời gian phản hồi trung vị 214 → 142 → **47 phút** qua 3 GĐ, tỷ lệ gọi trong ngày 61% → 68% → 79%. Nhưng lead mới/ngày cũng tăng 24,5 → 25,4 → **35,4** (`08` mục B).

---

### A-8. Trang đích v1 chạy suốt 57/90 ngày với LCP 4,8s và form 7 trường
**Mức độ: CAO — bỏ lỡ ~374 lead ≈ 476.011.404đ doanh thu**

| Trang đích | Ngày | Phiên | Tỷ lệ tương tác | Cuộn 90% | form_start | generate_lead | Hoàn tất form | LCP |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| v1 `/dang-ky-nhan-bang-gia` | 1–57 | 52.410 | 34,2% | 16% | 4.912 | 1.002 | **20,4%** | **4,8s** |
| v2 `/nhan-bang-gia-2026` | 58–90 | 42.938 | 58,7% | 37% | 2.546 | 713 | **28,0%** | 1,9s |

- v2 tốt hơn v1 **+37,3%** về tỷ lệ hoàn tất form (`10_GA4` mục C). LCP 4,8s vượt ngưỡng báo động >4s của `09_BENCHMARK`.
- **Ước tính:** nếu v2 chạy từ ngày 1: 4.912 form_start × 28,0% = **1.376 lead thay vì 1.002 → +374 lead** ⇒ theo CPL_CRM 705.333đ = **263.506.501đ giá trị lead**; quy tiếp theo tỷ lệ SQL/Lead 25,5% và SQL→cọc 2,77% ⇒ **+2,6 cọc ≈ 476.011.404đ**. *(Giả định lưu lượng và form_start giữ nguyên — là ước tính, không phải số đo.)*
- Riêng di động v1 tệ nhất: 41.404 phiên, hoàn tất form **16,1%**, tương tác 29,1% (`10_GA4` mục C, chi tiết thiết bị) — trong khi di động chiếm **78,1% chi phí** tài khoản.

---

### A-9. [KỸ THUẬT] Lỗi kỹ thuật CHƯA SỬA trên cả v1 lẫn v2 đang chặn 370–480 lead
**Mức độ: CAO — 260.973.285 – 338.559.937đ chi phí lead vứt đi; 471–612 triệu doanh thu bỏ lỡ**

`11_CLARITY` mục C, 3 mục trạng thái **"CHƯA SỬA"**:

| # | Lỗi | Phiên ảnh hưởng (số đo) | Lead mất (ước tính UX) |
|---|---|---:|---:|
| 4 | JS `TypeError e.setDate is not a function` (bộ chọn ngày hẹn xem nhà), Safari iOS 17.x — **form không gửi được, không báo lỗi cho khách** | 4.196 | 280–340 |
| 5 | Nút "Đăng ký nhận bảng giá" bị khung chat che, màn hình <380px | 2.741 | 60–90 |
| 6 | Hotline dạng `tel:` không phản hồi trên desktop — 1.847 nhấp chết | 1.204 | 30–50 |
| | **Cộng** | **8.141** | **370–480** |

- Bằng chứng lỗi #4 vẫn sống: `11_CLARITY` mục A ghi rõ *"tỷ lệ lỗi JavaScript trên di động KHÔNG giảm sau khi lên trang đích v2 (9,3% → 8,9%)"*.
- Xem chi tiết định lượng ở **B7**.

---

### A-10. [ĐO LƯỜNG] Sự cố GTM v23 — mất trắng 3 ngày dữ liệu chuyển đổi, phát hiện sau 3 ngày vì không có cảnh báo
**Mức độ: TRUNG BÌNH — 63 lead ≈ 44.435.998đ, nhưng rủi ro lặp lại là CAO**

- `12_GTM` mục B: **v23 ngày 44, 09:12, dev@** đổi class `.form-dk-v1` → `.form-register`; điều kiện kích hoạt `generate_lead` ngừng khớp ⇒ **chuyển đổi = 0 trong ngày 44, 45, 46**. v24 ngày 47 mới sửa; *"63 lead của 3 ngày trước đó vĩnh viễn không có trong Google Ads/GA4"*.
- **Đã kiểm chứng độc lập trên `02_DU_LIEU_NGAY`** (script khối B6): ngày 44 (14/04) CĐ_Ads=0 & Lead_CRM=17; ngày 45 (15/04) 0 & 15; ngày 46 (16/04) 0 & 31 → **tổng đúng 63**. Đây là 3 ngày duy nhất trong 90 ngày có CĐ_Ads=0 toàn tài khoản.
- Nguyên nhân hệ thống, cả hai đều là **KHÔNG ĐẠT** trong `12_GTM` mục C: (a) điều kiện kích hoạt phụ thuộc class CSS; (b) **không có cảnh báo khi chuyển đổi = 0** — sheet ghi thẳng "Nguyên nhân khiến sự cố N44–46 mất 3 ngày mới bị phát hiện".
- Tác động thứ cấp lớn hơn con số 63: 3 ngày tín hiệu 0 làm nhiễu thuật toán đấu thầu của mọi chiến dịch Smart Bidding trong và sau cửa sổ học.

---

### A-11. [KỸ THUẬT] GTM phình 34 thẻ / 412KB JS bên thứ ba, tự làm chậm LCP thêm ~0,8 giây
**Mức độ: TRUNG BÌNH — tự phá hoại chính khoản đầu tư trang đích v2**

- `12_GTM` header: **34 thẻ · 21 trigger · 18 biến · 412 KB JavaScript bên thứ ba · ước tính làm chậm LCP thêm ~0,8 giây**.
- Trong đó: thẻ #2 **"GA4 Configuration – Copy of Main" TRÙNG LẶP** → page_view bắn 2 lần từ ngày 31 (v22) ⇒ số phiên và tỷ lệ thoát sai lệch từ ngày 31 trở đi (`12_GTM` mục C: KHÔNG ĐẠT). **Mọi phân tích phiên GA4 sau ngày 31 phải được coi là nghi vấn cho đến khi gỡ thẻ trùng.**
- Thẻ #13: **3 thẻ đối tác sàn F2, "Không rõ nguồn gốc — cần rà soát bảo mật"**; thẻ #12 Zalo Tracking "không rõ ai cài, không có mô tả". v20 (ngày 18) thêm thẻ F2 → LCP +0,3s.
- Đối chiếu: trang đích v2 đã kéo LCP về 1,9s (`10_GA4` mục C) — nhưng 0,8s trong đó là do GTM tự gây ra, tức có thể về ~1,1s nếu dọn thẻ. Chi phí không mất tiền mặt, nhưng ăn trực tiếp vào tỷ lệ chuyển đổi của 78,1% lưu lượng di động.

---

### A-12. [ĐO LƯỜNG] Mô hình phân bổ Last-click đang chỉ sai chỗ cho ngân sách
**Mức độ: TRUNG BÌNH — ảnh hưởng chất lượng quyết định trên toàn bộ 1,8 tỷ**

`10_GA4` mục D (chỉ tính 1.715 `generate_lead`):

| Kênh | Last-click (đang dùng) | Data-driven | Chênh | % |
|---|---:|---:|---:|---:|
| SEA_Brand | 592 | 401 | −191 | **−32,3%** |
| SEA_Generic | 418 | 402 | −16 | −3,8% |
| SEA_Competitor | 20 | 24 | +4 | +20,0% |
| PMAX | 510 | 466 | −44 | −8,6% |
| GDN_Remarketing | 132 | 186 | +54 | **+40,9%** |
| YT_Video | 43 | 165 | +122 | **+283,7%** |
| Trực tiếp / Organic (ngoài Ads) | 0 | 71 | +71 | — |

- Hai kết luận trái chiều nhau nhưng đều quan trọng: (a) **71 lead thực chất đến từ Direct/Organic đang bị last-click gán hết cho Ads** ⇒ hiệu quả Ads đang được thổi lên; (b) **YouTube và GDN đang bị đánh giá thấp nghiêm trọng** — YT bị gán 43 nhưng thực đóng góp 165 lead, tức đang bị coi là "vô dụng" một cách oan uổng. Bất kỳ quyết định cắt YT/GDN dựa trên last-click đều là quyết định sai dữ liệu.
- Lưu ý phản biện với chính mình: dù đổi sang data-driven, **Brand vẫn giữ 401/1.715 = 23,4% lead** — nên A-3 (tăng ngân sách Brand) vẫn đứng vững sau khi trừ hết phần thổi phồng. Đây là điểm chốt cho D1.

---

### A-13. Lịch quảng cáo 24/7 lệch pha hoàn toàn với ca trực của sale
**Mức độ: TRUNG BÌNH — ~409 triệu chi vào khung giờ không ai gọi lại kịp**

`07_KHUNG_GIO_TB` mục A:

| Khung giờ | % chi phí | Chi phí | SQL | CP/SQL | **Gọi lại <30 phút** |
|---|---:|---:|---:|---:|---:|
| 09:00–12:00 | 16,8% | 302.994.216 | 121 | **2.504.084** | 93% |
| 14:00–17:00 | 17,1% | 308.404.827 | 117 | 2.635.939 | 91% |
| 17:00–20:00 | 18,6% | 335.457.882 | 124 | 2.705.306 | 64% |
| **20:00–23:00** | 18,7% | 337.261.419 | 112 | **3.011.263** | **21%** |
| **23:00–24:00** | 4,0% | 72.141.480 | 22 | 3.279.158 | **12%** |
| 00:00–06:00 | 4,1% | 73.945.017 | 18 | **4.108.057** | 34% |

- **22,7% ngân sách (409.402.899đ) chảy vào 20:00–24:00**, khi chỉ 12–21% lead được gọi lại trong 30 phút. CP/SQL khung 20–23h cao hơn khung 09–12h **+20,3%**.
- `05_CAU_HINH_TK`: "Lịch quảng cáo 24/7, không điều chỉnh giá thầu theo giờ" — chưa từng chỉnh.

---

### A-14. Cuối tuần: 27,9% ngân sách chạy với 2/8 sale trực
**Mức độ: TRUNG BÌNH — CP/SQL đắt hơn ngày thường 40,4%**

`07_KHUNG_GIO_TB` mục C:

| Thứ | Chi phí | SQL | CP/SQL | Sale trực |
|---|---:|---:|---:|---:|
| Thứ 2 | 258.137.000 | 120 | **2.151.142** | 8 |
| Thứ 7 | 262.814.000 | 87 | **3.020.851** (+40,4% so T2) | **2** |
| Chủ nhật | 240.996.000 | 91 | 2.648.308 | **2** |

- T7+CN = **503.810.000đ (27,9% ngân sách)** với 25% năng lực sale. `01_BOI_CANH` nêu rõ đây là **thực trạng, không phải giả định**. Ngân sách đang được phân bổ theo lịch, không theo năng lực xử lý.

---

### A-15. Di động ăn 78,1% ngân sách nhưng chuyển đổi kém hơn desktop 2 lần
**Mức độ: TRUNG BÌNH**

`07_KHUNG_GIO_TB` mục B:

| Thiết bị | % chi phí | Chi phí | Lead CRM | SQL | Cọc | Tỷ lệ CĐ | CP/SQL |
|---|---:|---:|---:|---:|---:|---:|---:|
| Di động | 78,1% | 1.408.562.397 | 2.106 | 463 | 11 | **2,03%** | **3.042.251** |
| Máy tính | 16,7% | 301.190.679 | 334 | 163 | 6 | **4,02%** | **1.847.796** (rẻ hơn 39%) |
| Máy tính bảng | 5,2% | 93.783.924 | 115 | 24 | 1 | 1,71% | 3.907.664 |

- Đây **không** phải lý do để cắt di động (di động là nơi khách BĐS thực sự ở), mà là bằng chứng cộng hưởng với A-8/A-9: trải nghiệm di động đang hỏng (v1 hoàn tất form 16,1%; lỗi JS Safari iOS chưa sửa; nút bị chat che <380px). Sửa xong A-9 rồi mới đánh giá lại hệ số giá thầu thiết bị.

---

### A-16. [ĐO LƯỜNG] Không có Enhanced Conversions, không có GCLID trong CRM ⇒ không thể nhập chuyển đổi ngoại tuyến
**Mức độ: TRUNG BÌNH — chặn đường duy nhất để dạy Google tối ưu theo SQL/cọc thay vì lead thô**

- `05_CAU_HINH_TK`: "Chuyển đổi nâng cao: **TẮT**"; "Nhập chuyển đổi ngoại tuyến từ CRM: **CHƯA triển khai** — CRM không lưu GCLID".
- `12_GTM` mục A #14, #15: Enhanced Conversions **CHƯA CÀI**; **Biến ẩn lưu GCLID vào form CHƯA CÀI** — *"Không có GCLID trong CRM ⇒ KHÔNG THỂ nhập chuyển đổi ngoại tuyến"*.
- `12_GTM` mục C: bật EC = "Mất 10–20% khả năng khớp chuyển đổi" nếu không bật; lưu GCLID = "không thể tối ưu theo lead chất lượng".
- **Tác động định lượng:** tài khoản đang tối ưu theo Lead_CRM (2.557) trong khi chỉ 651 là SQL (**25,5%**) và 18 thành cọc (**0,70%**). Đây là lý do cấu trúc khiến CP/SQL 2.770.410đ vượt KPI 2.200.000đ. Không có offline import thì mọi chiến lược Smart Bidding đều đang mù giai đoạn cuối phễu. Cũng không có Consent Mode v2 và không có vùng chứa server-side (`12_GTM` #16, #17) ⇒ toàn bộ đo lường phụ thuộc trình duyệt + ad-blocker.

---

### A-17. [ĐO LƯỜNG] 2.100 tín hiệu ý định đang bị bỏ rơi hoàn toàn
**Mức độ: THẤP–TRUNG BÌNH — không mất tiền trực tiếp, nhưng là nguồn tín hiệu tốt nhất đang bị lãng phí**

`10_GA4` mục E + `12_GTM` v26 (ngày 71):

| Sự kiện | Lượt toàn kỳ | Sự kiện chính? | Nhập Ads? | Ghi chú của sheet |
|---|---:|---|---|---|
| zalo_click | **894** | Không | Không | *"Có — đang bị bỏ sót, không ai đo"* |
| file_download (bảng giá PDF) | **1.206** | Không | Không | *"Có tín hiệu ý định — đang bỏ sót"* |
| form_start | 7.458 | Không | Không | Đúng — chỉ dùng chẩn đoán |

- Nghịch lý cần nêu thẳng: tài khoản đang nhập 973 sự kiện **rác** vào Ads (A-1) trong khi để 2.100 sự kiện **có ý định thật** ngoài lề. Trong bối cảnh VN, Zalo là kênh CTA chính — 894 lượt zalo_click không được đo là mất nguyên một nhánh phễu.

---

### A-18. Thiếu tiện ích, thiếu chống spam, thiếu loại trừ khách đã cọc
**Mức độ: THẤP — mỗi mục nhỏ nhưng cộng lại kéo CTR và Điểm chất lượng**

- `05_CAU_HINH_TK`: chỉ có **Liên kết trang web (4 liên kết)**; **thiếu Cuộc gọi, Biểu mẫu khách hàng tiềm năng, Vị trí, Chú thích, Hình ảnh**. Điểm chất lượng bình quân **5,2/10**, "Trải nghiệm trang đích: Dưới trung bình".
- **Không có reCAPTCHA, không xác minh OTP số điện thoại** — cộng hưởng trực tiếp với `08` mục C: PMax có 31% trùng SĐT và 24% SĐT sai/không liên lạc được.
- **Chưa loại trừ khách đã đặt cọc / đã ký HĐMB** khỏi remarketing ⇒ 130.009.000đ GDN đang tiếp thị lại cho cả người đã mua.
- Đối tượng mới ở chế độ Quan sát, chưa dùng điều chỉnh giá thầu; Search Partners + Display network **BẬT trong cả 3 chiến dịch Search** (nguồn phổ biến của lưu lượng rác, nhưng **dữ liệu không tách được chi phí Search Partners/Display — cần thêm báo cáo phân đoạn mạng để định lượng**).

---

## Dữ liệu còn thiếu để kết luận chắc hơn

| Cần thêm | Để làm gì | Hiện đang chặn kết luận nào |
|---|---|---|
| Báo cáo phân đoạn theo Mạng (Search / Search Partners / Display) | Định lượng chi phí rác từ Search Partners & Display-in-Search | A-18 |
| Báo cáo Vị trí đặt (Placement) của PMax & GDN + Asset group report | Xác nhận giả thuyết lưu lượng rác 74,3% và biết cần loại trừ gì | A-2 |
| Chi phí theo khung giờ **tách theo chiến dịch** | Đặt lịch quảng cáo chính xác, không cắt nhầm Brand | A-13 |
| Nhật ký thay đổi (Change history) của Google Ads | Đối chiếu với GTM v18–v26, tìm thay đổi giá thầu/ngân sách không ghi lại | A-1, A-3 |
| Dữ liệu Facebook/Zalo/telesale (`01_BOI_CANH` xác nhận nằm ngoài file) | Kiểm tra 71 lead "Direct/Organic" và trùng lặp lead đa kênh | A-12 |
| Cohort cọc theo ngày ở mức chiến dịch × thiết bị | Đặt hệ số giá thầu thiết bị có căn cứ | A-15 |
| Báo cáo đấu giá (Auction insights) của Brand | Xác định đối thủ nào đang lấy 6,9% IS thứ hạng | A-3, D2 |

---

# PHẦN B — TÍNH TOÁN

> Toàn bộ số ở phần này in ra từ `agent-4-calc.py`. Ký hiệu: CPL_Ads = Chi phí / ChuyenDoi_Ads; CPL_CRM = Chi phí / Lead_CRM; CP/SQL = Chi phí / Lead_SQL; CP/cọc = Chi phí / Dat_Coc.

## B1. CPL / CP/SQL / CP/cọc — toàn kỳ và từng chiến dịch

| Chiến dịch | Chi phí | CPL_Ads | CPL_CRM | CP/SQL | CP/cọc |
|---|---:|---:|---:|---:|---:|
| SEA_Brand_Vinhomes_HocMon | 260.219.000 | 298.759 | **303.639** | **739.259** | **20.016.846** |
| SEA_Generic_NhaPho_CanHo_TayBac | 677.994.000 | 1.021.075 | 1.155.015 | 3.549.707 | 135.598.800 |
| PMAX_VinhomesHM_Lead | 475.376.000 | **267.817** | 573.433 | 7.793.049 | n/a — 0 cọc |
| SEA_Competitor_DoiThu | 176.746.000 | 5.701.484 | 5.523.312 | **58.915.333** | n/a — 0 cọc |
| GDN_Remarketing_Web30d | 130.009.000 | 430.493 | 673.622 | 3.611.361 | n/a — 0 cọc |
| YT_Video_TVC_MoBan | 83.193.000 | 470.017 | 1.410.051 | 10.399.125 | n/a — 0 cọc |
| **TOÀN KỲ** | **1.803.537.000** | **472.130** | **705.333** | **2.770.410** | **100.196.500** |

**Đọc bảng này thế nào:** cột CPL_Ads là cột **dễ đánh lừa nhất**. PMax có CPL_Ads thấp nhất tài khoản (267.817đ) nhưng CP/SQL cao thứ nhì (7.793.049đ) và 0 cọc — vì mẫu số của CPL_Ads chứa 34,7% sự kiện rác (A-1). Cột duy nhất nối được với tiền là **CP/cọc**, và chỉ 2/6 chiến dịch có số ở cột đó.

Chỉ số bổ trợ:

| Chiến dịch | CTR | CPC | SQL/Lead | Cọc | Doanh thu | ROAS | % chi phí |
|---|---:|---:|---:|---:|---:|---:|---:|
| SEA_Brand | **11,63%** | 13.663 | **41,1%** | 13 | 2.280.000.000 | **8,76x** | 14,4% |
| SEA_Generic | 4,47% | 33.070 | 32,5% | 5 | 850.000.000 | 1,25x | 37,6% |
| SEA_Competitor | 2,39% | **55.164** | 9,4% | 0 | 0 | 0 | 9,8% |
| PMAX | 1,00% | 11.974 | **7,4%** | 0 | 0 | 0 | 26,4% |
| GDN_Remarketing | 0,35% | 4.487 | 18,7% | 0 | 0 | 0 | 7,2% |
| YT_Video | 0,45% | 1.199 | 13,6% | 0 | 0 | 0 | 4,6% |
| **TOÀN KỲ** | 0,64% | 9.973 | **25,5%** | 18 | 3.130.000.000 | **1,74x** | 100% |

Đối chiếu `09_BENCHMARK`: CTR Brand 11,63% (trong dải 8–12% "trung bình ngành", chưa đạt >12%); CTR Generic 4,47% (trung bình 3–5%); CPC Generic 33.070đ (trung bình 25–45k); CP/SQL toàn kỳ 2.770.410đ (trung bình 1,8–3,5tr) nhưng **vẫn vượt KPI nội bộ 2.200.000đ**; SQL/Lead 25,5% (trung bình 18–30%); CPL_CRM 705.333đ (trung bình 500k–1,1tr).

## B2. ROAS toàn kỳ và theo giai đoạn

| Giai đoạn | Ngày | Chi phí | Doanh thu HH | Cọc | **ROAS** | CP/cọc |
|---|---|---:|---:|---:|---:|---:|
| GĐ1 | 1–30 (02/03–31/03) | 545.696.000 | 330.000.000 | 2 | **0,60x** | 272.848.000 |
| GĐ2 | 31–60 (01/04–30/04) | 604.392.000 | 850.000.000 | 5 | **1,41x** | 120.878.400 |
| GĐ3 | 61–90 (01/05–30/05) | 653.449.000 | 1.950.000.000 | 11 | **2,98x** | 59.404.455 |
| **Toàn kỳ** | 1–90 | **1.803.537.000** | **3.130.000.000** | **18** | **1,74x** | 100.196.500 |

**Điểm quan trọng nhất của bảng này:** ROAS GĐ3 = **2,98x**, chỉ cách KPI 3,0x đúng 0,02. Tức mục tiêu 3,0x **không viển vông** — tài khoản đã gần chạm nó ở tháng cuối mà chưa hề sửa bất kỳ vấn đề nào ở Phần A. GĐ3 hưởng lợi từ 3 thay đổi trùng nhau: trang đích v2 (từ ngày 58), SLA gọi 15 phút (`08` mục B), và sự kiện mở bán.

ROAS theo chiến dịch × giai đoạn (chỉ liệt kê nơi có doanh thu):

| Chiến dịch | GĐ1 | GĐ2 | GĐ3 |
|---|---:|---:|---:|
| SEA_Brand | 5,73x (2 cọc) | 7,19x (3 cọc) | **10,97x (8 cọc)** |
| SEA_Generic | 0 (0 cọc) | 1,51x (2 cọc) | 2,01x (3 cọc) |
| 4 chiến dịch còn lại | 0 | 0 | 0 |

## B3. Tỷ lệ chuyển đổi từng bước phễu

| Bước | Từ | Đến | Tỷ lệ | Benchmark `09_BENCHMARK` | Đánh giá |
|---|---:|---:|---:|---|---|
| Lead CRM → SQL | 2.557 | 651 | **25,46%** | 18–30% trung bình (>30% tốt) | Trung bình |
| SQL → Đi xem nhà | 651 | 206 | **31,64%** | 22–35% trung bình (>35% tốt) | Trung bình |
| Đi xem → Booking | 206 | 59 | **28,64%** | *(không có ngưỡng)* | — |
| Booking → Đặt cọc | 59 | 18 | **30,51%** | *(không có ngưỡng)* | — |
| *Đi xem → Cọc (gộp)* | 206 | 18 | **8,74%** | 7–12% trung bình | Trung bình |
| **Lead CRM → Cọc** | 2.557 | 18 | **0,704%** | — | — |
| **SQL → Cọc** | 651 | 18 | **2,765%** | — | — |

Phễu tách theo giai đoạn — **mọi bước đều cải thiện đơn điệu**, đây là bằng chứng mạnh nhất cho việc kế hoạch 90 ngày tới nên nhân rộng công thức GĐ3 chứ không phát minh lại:

| GĐ | Lead | SQL (SQL/Lead) | Đi xem (/SQL) | Booking (/Xem) | Cọc (/Booking) |
|---|---:|---:|---:|---:|---:|
| GĐ1 | 734 | 151 (**20,6%**) | 38 (25,2%) | 10 (26,3%) | 2 (20,0%) |
| GĐ2 | 761 | 184 (24,2%) | 56 (30,4%) | 16 (28,6%) | 5 (31,2%) |
| GĐ3 | 1.062 | 316 (**29,8%**) | 112 (**35,4%**) | 33 (29,5%) | 11 (**33,3%**) |

## B4. Ngược từ KPI: cần bao nhiêu SQL, bao nhiêu lead thô, CP/SQL trần?

Tôi tính **3 kịch bản** thay vì một, vì chọn tỷ lệ nào là giả định lớn nhất của cả bài toán:

| Kịch bản | SQL/Lead | Xem/SQL | Book/Xem | Cọc/Book | **SQL cần** | **Lead thô cần** | **CP/SQL trần** (2,1 tỷ) | CPL trần |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| **A** — tỷ lệ lịch sử toàn kỳ | 25,5% | 31,6% | 28,6% | 30,5% | **1.157** | **4.546** | **1.814.516** | 461.967 |
| **B** — tỷ lệ GĐ3 (tốt nhất đã đạt) | 29,8% | 35,4% | 29,5% | 33,3% | **919** | **3.089** | **2.284.415** | 679.732 |
| **C** — kế hoạch (chọn dùng) | 35,0% | 35,0% | 30,0% | 35,0% | **871** | **2.488** | **2.411.719** | 844.102 |

**Kịch bản tôi chọn là C, và đây là lý do:**
- Không chọn A: tỷ lệ toàn kỳ bị kéo xuống bởi GĐ1 chạy trên trang đích v1 lỗi + không có SLA gọi lại. Dùng A tương đương giả định 90 ngày tới lặp lại mọi sai lầm cũ — khi đó cần 4.546 lead thô = **50,5 lead/ngày**, vượt xa năng lực cuối tuần (2 sale × 12 = 24 lead/ngày) và CP/SQL trần tụt xuống 1.814.516đ, tức bài toán bất khả thi.
- Không dừng ở B: B là "chạy y hệt GĐ3". Nhưng GĐ3 đã đạt được **mà chưa sửa** 3 lỗi Clarity chưa sửa (A-9), chưa dọn 973 sự kiện rác (A-1), chưa cắt 434tr chi phí ngoài vùng bán (A-6), chưa bù 39,7% IS Brand (A-3).
- Chọn C: nâng SQL/Lead từ 29,8% → **35,0%** (có căn cứ: cắt Competitor SQL/Lead 9,4% và cắt tệ PMax 7,4% ra khỏi mẫu số sẽ tự động đẩy tỷ lệ chung lên; Brand hiện đã ở 41,1%); giữ Xem/SQL ở 35,0% (= mức GĐ3, không lạc quan thêm); Book/Xem 30,0% (≈ mức trung bình 3 GĐ 28,6%); Cọc/Book 35,0% (nhích nhẹ trên GĐ3 33,3%, hưởng lợi từ SLA gọi <5 phút — `08` mục A cho thấy nhóm gọi <5 phút có tỷ lệ cọc gấp 1,5 lần nhóm 5–30 phút).

**Đáp số kịch bản C:** để có **32 cọc** cần **92 booking → 305 lượt đi xem → 871 SQL → 2.488 lead thô** (≈ 27,6 lead/ngày, nằm trong năng lực 96 lead/ngày ngày thường nhưng **sát trần 24 lead/ngày của T7–CN** ⇒ bắt buộc giảm giá thầu cuối tuần, xem Phần C).

**Đối chiếu với trần KPI 2.200.000đ:** với 2,1 tỷ, CP/SQL 2.200.000đ mua được **955 SQL** > 871 SQL cần. Nghĩa là **KPI CP/SQL ≤ 2,2tr là ràng buộc chặt hơn** ràng buộc 32 cọc — bám vào 2,2tr là đủ để phủ luôn mục tiêu cọc, với biên an toàn 84 SQL (+9,6%). **Đây là chỉ số tôi sẽ dùng làm KPI vận hành hằng tuần.**

## B5. Điểm hòa vốn / trần chi phí trên mỗi cọc

| Đại lượng | Công thức | Kết quả |
|---|---|---:|
| Hoa hồng / cọc | dữ kiện `01_BOI_CANH` | 181.000.000đ |
| **Chi phí QC tối đa / cọc để ROAS = 3,0x** | 181.000.000 ÷ 3,0 | **60.333.333đ** |
| Số cọc tối thiểu để tiêu hết 2,1 tỷ ở trần đó | 2.100.000.000 ÷ 60.333.333 | **34,8 → 35 cọc** |
| CP/cọc thực tế 90 ngày qua | 1.803.537.000 ÷ 18 | **100.196.500đ** (vượt trần 66,1%) |
| CP/cọc GĐ3 | 653.449.000 ÷ 11 | **59.404.455đ** — **đã dưới trần** |

**Ba hệ quả phải nói rõ với ban giám đốc:**
1. Trần hòa vốn ROAS 3,0x là **60.333.333đ/cọc**. Chỉ **SEA_Brand đang ở dưới trần này (20.016.846đ/cọc)**. SEA_Generic ở 135.598.800đ/cọc — **vượt trần 2,25 lần**. Bốn chiến dịch còn lại chưa có cọc nào nên chưa định giá được.
2. **KPI "32 cọc" và KPI "ROAS ≥ 3,0x" mâu thuẫn nhẹ với nhau nếu tiêu hết ngân sách:** 32 cọc × 181tr = 5.792.000.000đ ÷ 2,1 tỷ = **2,76x < 3,0x**. Để đạt cả hai, hoặc phải làm **≥ 35 cọc**, hoặc chỉ tiêu **≤ 1.930.666.667đ** (= 5.792tr ÷ 3,0). **Đây là điểm cần chốt với ban giám đốc ngay tuần 1** (xem E-1). Kế hoạch Phần C của tôi nhắm 35 cọc để thỏa mãn cả hai.
3. GĐ3 chứng minh trần 60,3tr/cọc là đạt được (59.404.455đ) — mục tiêu không phải phép màu, mà là nhân rộng GĐ3.

## B6. Đối chiếu ba nguồn số liệu — bóc tách chính xác từng thành phần

**Bước 1 — Con số 3.820 được tạo bởi gì** (`10_GA4` mục A + `12_GTM` mục A thẻ #3–#6, #8):

| Sự kiện | Lượt | Là lead thật? |
|---|---:|---|
| generate_lead | 1.715 | ✅ |
| click_to_call (tổng lượt) | 1.132 | ⚠️ có, nhưng đếm trùng |
| view_price_page | 612 | ❌ |
| engaged_30s | 361 | ❌ |
| **Cộng** | **3.820** | = đúng cột "Chuyển đổi" Google Ads ✔ |

*(GA4 và Google Ads bằng nhau tuyệt đối vì Ads nhập trực tiếp từ GA4 — nên thực chất chỉ có **hai** nguồn độc lập: nền tảng đo lường vs CRM.)*

**Bước 2 — Bóc tách khoảng chênh 3.820 vs 2.557:**

| # | Thành phần | Phép tính | Số lượng | % của 3.820 | Nguồn |
|---|---|---|---:|---:|---|
| 1 | **Đếm trùng lượt gọi** — 1 người bấm `tel:` nhiều lần | 1.132 − 779 | **−353** | 9,2% | `10_GA4` A; `12_GTM` #4 "Đếm mọi lượt nhấp, không khử trùng theo người dùng" |
| 2 | **Sự kiện rác** — không phải khách hàng tiềm năng | 612 + 361 | **−973** | 25,5% | `10_GA4` A & E (cột "Có thực sự là khách hàng tiềm năng?" = KHÔNG) |
| = | **Lead thật đo được bằng thẻ** | 3.820 − 353 − 973 | **2.494** | | `10_GA4` A: "1.715 form + 779 người gọi duy nhất" |
| 3 | **Mất thẻ N44–46** — lead CRM có nhưng thẻ không bắn | 2.557 − 2.494 | **+63** | | `12_GTM` v23/v24; kiểm chứng độc lập ở `02` |
| = | **CRM — lead thật đã khử trùng** | 2.494 + 63 | **2.557** ✔ | | `02` SUM(Lead_CRM) |

**Chứng minh phép cộng khớp:**
```
3.820 − 353 − 973 + 63 = 2.557   ✔ (script trả về True)
Khoảng chênh gộp: 3.820 − 2.557 = 1.263
Phân rã:          −353 (trùng) − 973 (rác) + 63 (mất thẻ) = −1.263   ✔
```

**Kiểm chứng độc lập thành phần #3 bằng dữ liệu ngày** (script khối B6, quét toàn bộ 90 ngày tìm ngày CĐ_Ads = 0 nhưng Lead_CRM > 0 — chỉ đúng 3 ngày trong 90 ngày rơi vào trường hợp này):

| Ngày thứ | Ngày | ChuyenDoi_Ads | Lead_CRM |
|---:|---|---:|---:|
| 44 | 2026-04-14 | **0** | 17 |
| 45 | 2026-04-15 | **0** | 15 |
| 46 | 2026-04-16 | **0** | 31 |
| | **Cộng** | **0** | **63** ✔ khớp `10_GA4` |

**Ai đúng?** CRM = 2.557 là con số đúng để đánh giá marketing (đã khử trùng, là lead sale thật sự nhận). Google Ads = 3.820 **thổi phồng 1,49x** (`03_TONG_HOP_CD` cột "Chênh lệch Ads vs CRM"; `09_BENCHMARK` xếp 1,2–1,5x là "trung bình ngành", >1,8x là báo động — nên ở mức tài khoản chưa chạm báo động, **nhưng PMax riêng lẻ ở 2,14x thì đã vượt xa ngưỡng đỏ**). Con số 2.494 của GA4 là số **kỹ thuật đúng nhất mà thẻ đo được**, và khoảng cách 2.494 vs 2.557 chính là thước đo độ tin cậy hệ thống đo lường: hiện đang **hụt 2,5%** vì một sự cố GTM duy nhất.

## B7. Ước tính lead mất do lỗi kỹ thuật CHƯA SỬA, quy ra tiền

**Phân định rạch ròi số đo vs ước tính:**

| Loại | Con số nào |
|---|---|
| **SỐ ĐO** (Clarity ghi hình trực tiếp, mẫu ~92% lưu lượng) | Số phiên ảnh hưởng: 4.196 / 2.741 / 1.204; 8.412 nhấp chết ở lỗi #1; 1.847 nhấp chết ở lỗi #6; tỷ lệ lỗi JS di động 9,3% (v1) → 8,9% (v2) |
| **ƯỚC TÍNH CỦA ĐỘI UX** (ghi trong `11_CLARITY`, *"dựa trên tỷ lệ hoàn tất form của nhóm phiên không gặp lỗi. Là ước tính, không phải số đo trực tiếp"*) | Khoảng lead mất 280–340 / 60–90 / 30–50 |
| **ƯỚC TÍNH CỦA TÔI** (phép nhân từ hai loại trên bằng tỷ lệ lịch sử ở `02`) | Quy ra tiền, quy ra SQL, quy ra cọc |

| # | Lỗi CHƯA SỬA | Phiên (số đo) | Lead mất (ước tính UX) |
|---|---|---:|---:|
| 4 | JS `TypeError e.setDate` — Safari iOS 17.x, form không gửi được và **không báo lỗi cho khách** | 4.196 | 280–340 |
| 5 | Nút CTA bị khung chat che, màn hình <380px | 2.741 | 60–90 |
| 6 | `tel:` không phản hồi trên desktop | 1.204 | 30–50 |
| | **Cộng** | **8.141** | **370–480** ✔ khớp ghi chú tổng của sheet |

**Quy ra tiền (ước tính của tôi, hệ số lấy từ `02`):**

| Bước quy đổi | Hệ số dùng | Nguồn hệ số | Kết quả (thấp – cao) |
|---|---|---|---:|
| Lead mất | — | `11_CLARITY` C | **370 – 480 lead** |
| × CPL_CRM thực tế | 705.333đ/lead | 1.803.537.000 ÷ 2.557 | **260.973.285 – 338.559.937đ** |
| × SQL/Lead | 25,46% | 651 ÷ 2.557 | 94 – 122 SQL |
| × SQL→Cọc | 2,765% | 18 ÷ 651 | **2,6 – 3,4 cọc** |
| × hoa hồng 181tr | — | `01_BOI_CANH` | **471.435.276 – 611.591.709đ doanh thu bỏ lỡ** |

**Đọc kết quả:** chi phí sửa 3 lỗi này là vài ngày công dev. Đổi lại **261–339 triệu đồng ngân sách quảng cáo đang mua lưu lượng rồi vứt đi**, tương đương **471–612 triệu doanh thu hoa hồng**. Đây là hạng mục có tỷ suất hoàn vốn cao nhất trong toàn bộ báo cáo và là lý do trực tiếp cho lập luận ở D6.

**Cảnh báo về cách dùng con số này:** 370–480 lead là **ước tính của bên thứ ba (đội UX)**, không phải số tôi đo lại được. Tôi giữ nguyên khoảng thay vì lấy điểm giữa. Để chuyển từ ước tính thành số đo cần: (a) log lỗi JS phía server có gắn session ID, (b) so tỷ lệ hoàn tất form của nhóm Safari iOS 17.x với nhóm trình duyệt khác trong GA4 — hiện `10_GA4` chỉ tách theo thiết bị, không tách theo trình duyệt/OS.

---

# PHẦN C — KẾ HOẠCH 90 NGÀY TIẾP THEO

## C-0. Nguyên tắc chi phối toàn bộ kế hoạch

1. **Không tăng ngân sách trước khi sửa xong đo lường.** 34,7% tín hiệu hiện là rác (A-1); đổ thêm tiền vào một hệ thống học sai chỉ nhân nhanh sai lầm. Toàn bộ GĐ1 là giai đoạn "sửa trước, tiêu sau".
2. **Ngân sách chảy theo cọc, không chảy theo "chuyển đổi".** Brand đang ở 20.016.846đ/cọc (dưới trần hòa vốn 60.333.333đ), Generic ở 135.598.800đ/cọc (vượt trần 2,25x), 4 chiến dịch còn lại chưa có cọc nào.
3. **Ràng buộc cứng là năng lực sale, không phải tiền.** 2.488 lead thô cần cho 32 cọc = 27,6 lead/ngày; ngày thường chịu được 96, nhưng T7–CN chỉ 24 (`01_BOI_CANH`).
4. **Mục tiêu số là 35 cọc, không phải 32** — vì chỉ 35 cọc mới thỏa mãn đồng thời ROAS 3,0x khi tiêu hết 2,1 tỷ (B5).

**Mục tiêu tổng 90 ngày:** 2.100.000.000đ → **955 SQL** (CP/SQL 2.200.000đ) → **35 cọc** → **6.335.000.000đ** doanh thu → **ROAS 3,02x**. Dự báo script: 955 SQL → 334 đi xem → 100 booking → 35 cọc → 6.349.397.727đ → **3,02x**.

## C-1. Bảng phân bổ ngân sách — tổng đúng 2.100.000.000đ

| Chiến dịch | GĐ1 (N1–30) | GĐ2 (N31–60) | GĐ3 (N61–90) | Tổng | % | Kỳ trước | Δ |
|---|---:|---:|---:|---:|---:|---:|---|
| SEA_Brand_Vinhomes_HocMon | 190.000.000 | 210.000.000 | 220.000.000 | **620.000.000** | 29,5% | 260.219.000 | **+138%** |
| SEA_Generic_NhaPho_CanHo_TayBac | 260.000.000 | 290.000.000 | 310.000.000 | **860.000.000** | 41,0% | 677.994.000 | +27% |
| PMAX_VinhomesHM_Lead | 50.000.000 | 90.000.000 | 120.000.000 | **260.000.000** | 12,4% | 475.376.000 | **−45%** |
| GDN_Remarketing_Web30d | 40.000.000 | 45.000.000 | 50.000.000 | **135.000.000** | 6,4% | 130.009.000 | +4% |
| YT_Video_TVC_MoBan | 0 | 15.000.000 | 30.000.000 | **45.000.000** | 2,1% | 83.193.000 | −46% |
| SEA_Competitor_DoiThu | 0 | 0 | 20.000.000 | **20.000.000** | 1,0% | 176.746.000 | **−89%** |
| Dự phòng (giữ lại, chỉ giải ngân khi chạm ngưỡng mở rộng) | 60.000.000 | 40.000.000 | 60.000.000 | **160.000.000** | 7,6% | — | mới |
| **TỔNG** | **600.000.000** | **690.000.000** | **810.000.000** | **2.100.000.000** ✔ | 100% | 1.803.537.000 | +16,4% |

*(script khối "PHẦN C" có `assert sum(tot) == 2_100_000_000` — chạy pass, không có sai số làm tròn.)*
Ngân sách/ngày bình quân: GĐ1 **20.000.000đ**, GĐ2 **23.000.000đ**, GĐ3 **27.000.000đ**.

**Lý do từng dòng, gắn số:**

| Chiến dịch | Quyết định | Căn cứ số |
|---|---|---|
| Brand +138% | Tăng mạnh nhất | ROAS 8,76x, 13/18 cọc, CP/cọc 20,0tr (bằng 1/3 trần hòa vốn), **mất 39,7% IS do ngân sách** — đây là tiền đang bỏ lại trên bàn (`09_BENCHMARK`) |
| Generic +27% | Tăng vừa, nhưng **đổi chất** | ROAS 1,25x là dưới hòa vốn, nhưng đây là nguồn khách mới duy nhất có cọc (5 cọc). Tăng tiền chỉ hợp lệ sau khi cắt 242.982.000đ cụm từ rác (A-4) — tức cùng ngân sách nhưng chất lượng lưu lượng khác hẳn |
| PMax −45% | Cắt sâu, giữ để tái khởi động sạch | 475tr → 0 cọc; SQL/Lead 7,4%; bounce 74,3%. Không cắt 100% vì PMax là kênh duy nhất có quy mô — nhưng chỉ bật lại sau khi (a) sửa xong conversion action, (b) bật brand exclusion + loại trừ vị trí đặt |
| GDN +4% | Giữ nguyên | CP/SQL 3,6tr chấp nhận được; data-driven cho thấy GDN thực đóng góp 186 lead chứ không phải 132 (**+40,9%**, `10_GA4` D) — đang bị đánh giá thấp |
| YT −46% | Giảm nhưng **không cắt** | Last-click gán 43 lead nhưng data-driven gán **165 (+283,7%)**. Cắt YT dựa trên last-click là quyết định sai dữ liệu. Giữ ở mức tối thiểu, đo bằng thước đúng |
| Competitor −89% | Tắt GĐ1–GĐ2, mở lại 20tr ở GĐ3 | 176,7tr → 3 SQL → 0 cọc; CP/SQL 58,9tr = 11,8x ngưỡng báo động. 20tr ở GĐ3 chỉ để phòng thủ nếu D2 xảy ra |
| Dự phòng 160tr | Không giải ngân mặc định | Kỷ luật chống lặp lại sai lầm cũ (chi 1,8 tỷ không có ngưỡng dừng). Chỉ mở khi chạm tiêu chí ở C-5 |

---

## GIAI ĐOẠN 1 — Ngày 1–30: "SỬA ĐO LƯỜNG & CẦM MÁU"

### Mục tiêu định lượng

| Chỉ tiêu | Mục tiêu GĐ1 | Đối chiếu kỳ trước |
|---|---:|---:|
| Chi phí | ≤ 600.000.000đ | GĐ1 cũ: 545.696.000đ |
| Tỷ lệ CĐ_Ads / Lead_CRM | **≤ 1,15x** | hiện 1,49x (toàn kỳ), PMax 2,14x |
| SQL | ≥ 250 | GĐ1 cũ: 151 |
| CP/SQL | ≤ 2.400.000đ | GĐ1 cũ: 545.696.000÷151 = 3.613.881đ |
| SQL/Lead | ≥ 30% | GĐ1 cũ: 20,6% |
| Cọc | ≥ 7 | GĐ1 cũ: 2 |
| IS Brand | ≥ 75% (từ 53,4%) | mất IS ngân sách ≤ 15% (từ 39,7%) |
| Lead bị bỏ sót (không ai gọi) | **0** | GĐ1 cũ: 118 |
| Lỗi Clarity #4/#5/#6 | đóng cả 3 trước ngày 10 | hiện CHƯA SỬA |

### Cấu trúc tài khoản đề xuất

| Chiến dịch | Nhóm quảng cáo | Đối sánh | Ghi chú |
|---|---|---|---|
| **SEA_Brand** | AG1 Brand chính (`vinhomes hóc môn`, `dự án vinhomes hóc môn`) · AG2 Brand + ý định giá (`… giá bán`, `… bảng giá`) · AG3 Brand biến thể không dấu (`vinhomes hoc mon`, `vin hóc môn`) | **Chính xác + Cụm từ**, bỏ hết Rộng | Tách vì `04_SEARCH_TERMS` cho thấy CP/SQL chênh 2x giữa nhóm chính (565.696đ) và nhóm hỏi đáp (`… ở đâu` 1.040.867đ, `… có thật không` 4.337.000đ) |
| **SEA_Generic** | AG1 Nhà phố/liền kề · AG2 Căn hộ · AG3 Shophouse · AG4 Khu vực (`khu đô thị tây bắc`, `mua nhà phố quận 12`) | **Cụm từ là chính**, Chính xác cho 6 cụm đã có SQL, **Rộng chỉ 1 nhóm thử nghiệm ngân sách ≤ 10%/ngày có trần CPC** | Hiện 71% chi phí Search từ Rộng (`05`) — đảo ngược tỷ trọng |
| **PMAX** | 1 nhóm nội dung duy nhất: Lead chất lượng | — | Bắt buộc: brand exclusion BẬT, danh sách loại trừ vị trí đặt, tín hiệu đối tượng = danh sách khách đã cọc + web 30d |
| **GDN_Remarketing** | AG1 Đã xem bảng giá (chưa gửi form) · AG2 form_start bỏ dở · AG3 Xem >60s | — | Tách theo mức ý định để đặt giá thầu khác nhau; **loại trừ khách đã cọc/đã ký HĐMB** (hiện chưa có, `05`) |
| **SEA_Competitor** | **TẠM DỪNG** | — | Bật lại GĐ3 nếu D2 xảy ra |
| **YT_Video** | **TẠM DỪNG GĐ1** | — | Không có thước đo đúng cho đến khi xong đo lường |

**Thay đổi cấu hình chung, làm ngay trong GĐ1:**

| Hạng mục | Từ | Sang | Căn cứ |
|---|---|---|---|
| Nhắm mục tiêu vị trí | VN toàn quốc | **TP.HCM + Bình Dương + Long An**; loại trừ HN, ĐN, ĐBSCL, Đồng Nai | A-6: 434.652.417đ, 0 cọc |
| Tùy chọn vị trí | Hiện diện HOẶC quan tâm | **Chỉ "Hiện diện"** | 28.856.592đ chi cho người ngoài VN |
| Ngôn ngữ | Việt + Anh | **Chỉ Tiếng Việt** | Không có dữ kiện nào cho thấy khách nói tiếng Anh chuyển đổi |
| Search Partners / Display-in-Search | BẬT | **TẮT cả 3 CD Search** | `05`; cần đo lại 14 ngày rồi quyết định giữ hay bỏ hẳn |
| Từ khóa phủ định | 12 từ | **Danh sách chia sẻ ≥ 150 từ** | A-4: 11 cụm × 242.982.000đ; thêm nhóm chủ đề: *tuyển dụng, việc làm, học phí, vinschool, thuê, nhà trọ, kho xưởng, quy hoạch, giá đất, thổ cư, lừa đảo, chung cư mini, mini* |
| Lịch quảng cáo | 24/7 | **07:00–20:00 T2–T6; T7–CN giảm giá thầu −40%; tắt 23:00–06:00** | A-13, A-14 |
| Đối tượng | Chỉ Quan sát | **Nhắm mục tiêu + điều chỉnh giá thầu**; loại trừ khách đã cọc | `05` |
| Tiện ích | 4 sitelink | **+ Cuộc gọi (7:00–20:00), Biểu mẫu KH tiềm năng, Vị trí (nhà mẫu), Chú thích, Hình ảnh, Giá** | `05`: đang thiếu 5 loại; QS 5,2/10 |

### Chiến lược giá thầu & điều kiện chuyển đổi

| Chiến dịch | GĐ1 | Điều kiện chuyển sang chiến lược khác |
|---|---|---|
| SEA_Brand | **Tỷ lệ hiển thị mục tiêu 90%, vị trí đầu trang**, trần CPC 25.000đ | Khi IS ≥ 85% ổn định 14 ngày **và** conversion action đã sạch **và** ≥ 30 cọc/tháng dữ liệu → chuyển **tCPA 700.000đ** (= CP/SQL Brand hiện tại 739.259đ, làm tròn xuống) |
| SEA_Generic | **CPC thủ công nâng cao, trần CPC 30.000đ** (hiện CPC 33.070đ, "Tối đa hóa nhấp không trần") | Sau khi tích đủ **≥ 50 chuyển đổi sạch/30 ngày** → **tCPA 2.200.000đ** (= trần KPI CP/SQL). Chỉ chuyển sang **tROAS** sau khi offline import chạy ≥ 45 ngày |
| PMAX | **Tối đa hóa chuyển đổi CÓ tCPA 2.500.000đ** (hiện không đặt tCPA) | Nếu SQL/Lead ≥ 20% sau 30 ngày → giữ và tăng ngân sách; **nếu < 15% → tắt vĩnh viễn** |
| GDN_Remarketing | Giữ **CPC nâng cao**, trần CPC 6.000đ | Nếu CP/SQL ≤ 2.500.000đ trong 30 ngày → chuyển tCPA 2.500.000đ |
| YT_Video | Tạm dừng GĐ1 | Bật lại GĐ2 với **CPV mục tiêu** + đo bằng data-driven, KHÔNG bằng last-click |
| SEA_Competitor | Tạm dừng | — |

**Nguyên tắc chung về Smart Bidding:** không chuyển bất kỳ chiến dịch nào sang tCPA/tROAS trước khi **conversion action đã sạch ít nhất 30 ngày**. Chuyển sớm hơn = dạy thuật toán bằng chính 973 sự kiện rác đang có.

### KẾ HOẠCH ĐO LƯỜNG (mục riêng, bắt buộc) — thứ tự triển khai chặt chẽ

> Đây là hạng mục ưu tiên số 1 của GĐ1. Mọi thứ khác trong kế hoạch đều phụ thuộc vào nó chạy đúng.

**Bước 1 (Ngày 1–2) — Cầm máu ngay trong Google Ads, không cần đợi dev:**

| # | Việc | Nơi làm | Cách kiểm tra |
|---|---|---|---|
| 1.1 | Chuyển `view_price_page` và `engaged_30s` từ **Chính** → **Phụ (Secondary)** | Google Ads › Chuyển đổi | Cột "Chuyển đổi" giảm ~973 lượt (25,5%); "Tất cả chuyển đổi" giữ nguyên |
| 1.2 | Đổi `click_to_call` từ đếm **"Mỗi lượt"** → **"Một lượt"** (khử trùng theo người dùng) | Google Ads › Chuyển đổi › Đếm | Chênh lệch 353 lượt biến mất; CĐ_Ads/Lead_CRM tiến về ~1,0 |
| 1.3 | Ghi nhận baseline trước/sau vào bảng theo dõi | — | Kỳ vọng: 3.820 → ~2.494 (−34,7%) |

*Đây là 3 thao tác trong giao diện Ads, làm được trong 1 buổi, và tự nó đã sửa 34,7% tín hiệu rác — không cần một dòng code nào.*

**Bước 2 (Ngày 1–10) — Sửa GTM & trang đích, theo đúng thứ tự này:**

| # | Việc | Vì sao thứ tự này | Cách kiểm tra |
|---|---|---|---|
| 2.1 | **Sửa lỗi JS `TypeError e.setDate`** (Clarity #4) — thay bộ chọn ngày bằng `<input type="date">` gốc trình duyệt | Ưu tiên tuyệt đối: 280–340 lead/90 ngày (B7). Đây là lỗi khách **gửi form mà không biết là thất bại** | Test thật trên Safari iOS 17.x; tỷ lệ phiên có lỗi JS di động phải rời khỏi mức 8,9% (Clarity mục A) |
| 2.2 | **Sửa nút CTA bị khung chat che <380px** (Clarity #5) + **`tel:` trên desktop** (Clarity #6) | 90–140 lead/90 ngày | Clarity: nhấp chết ở nút CTA và hotline về ~0; test ở viewport 360px |
| 2.3 | **Gỡ thẻ "GA4 Configuration – Copy of Main"** (GTM #2) | Phải gỡ TRƯỚC khi lấy bất kỳ baseline GA4 nào, nếu không mọi số phiên sau ngày 31 đều sai | GA4 Realtime: `page_view` bắn đúng 1 lần/tải trang |
| 2.4 | **Đổi trigger `generate_lead` từ class CSS sang `dataLayer.push`** do dev bắn khi server xác nhận gửi thành công | Nguyên nhân gốc của sự cố N44–46 (63 lead). Không sửa = chắc chắn tái diễn | GTM Preview: đổi class ở staging, trigger vẫn khớp |
| 2.5 | **Cài biến ẩn lưu GCLID/GBRAID/WBRAID vào form → CRM** (GTM #15) | Điều kiện tiên quyết của offline import; không có nó thì không bao giờ tối ưu được theo SQL/cọc | Kiểm 20 lead mẫu trong CRM đều có trường gclid không rỗng |
| 2.6 | **Bật Enhanced Conversions** (GTM #14) | Cần GCLID/first-party data đã có ở 2.5 | Google Ads › Chẩn đoán: trạng thái "Đang ghi nhận"; kỳ vọng +10–20% khớp (`12_GTM` C) |
| 2.7 | **Đánh dấu `zalo_click` (894 lượt) và `file_download` (1.206 lượt) là sự kiện chính** — nhập Ads ở dạng **Phụ** trước, quan sát 30 ngày rồi mới nâng lên Chính | A-17. Nhập thẳng vào Chính là lặp lại đúng sai lầm của agency cũ | GA4: 2 sự kiện xuất hiện trong danh sách chuyển đổi; đối chiếu với số lead Zalo mà sale thực nhận |
| 2.8 | **Dọn thẻ GTM**: gỡ 3 thẻ đối tác sàn F2 không rõ nguồn gốc, rà thẻ Zalo Tracking không có mô tả | 412KB JS, +0,8s LCP (A-11); còn là rủi ro bảo mật | PageSpeed: LCP giảm; đếm lại số thẻ ≤ 25 |
| 2.9 | **Cấu hình Consent Mode v2** (GTM #16) | Tuân thủ + phục hồi mô hình hóa chuyển đổi | GTM Preview: consent state đúng trước khi thẻ bắn |

**Bước 3 (Ngày 10–20) — Xây lớp phòng vệ để sự cố N44–46 không lặp lại:**

| # | Việc | Cách kiểm tra |
|---|---|---|
| 3.1 | **Cảnh báo tự động khi chuyển đổi = 0** (GTM #18 — "KHÔNG CÓ", nguyên nhân sự cố mất 3 ngày mới phát hiện): quy tắc tự động Google Ads + cảnh báo tùy chỉnh GA4, ngưỡng: `generate_lead` = 0 trong 6 giờ giờ hành chính → email + Zalo cho tôi & dev | Cố tình tắt trigger ở staging → phải nhận cảnh báo trong 6 giờ |
| 3.2 | **Đối soát 3 nguồn hằng tuần**: Ads vs GA4 vs CRM, ngưỡng chấp nhận CĐ_Ads/Lead_CRM ≤ 1,15x | Bảng đối soát tuần; lệch >1,15x = mở điều tra |
| 3.3 | **Gắn Clarity session ID vào bản ghi CRM** (GTM #10 — "Chưa gắn") | Mở 5 lead đã cọc, xem lại được hành trình |
| 3.4 | **Quy trình bắt buộc**: mọi lần dev đổi giao diện phải chạy GTM Preview + checklist 6 sự kiện trước khi publish; ghi vào lịch sử phiên bản | Nhật ký thay đổi có ghi chú cho mọi phiên bản |

**Bước 4 (Ngày 20–30) — Đóng vòng lặp cuối phễu:**

| # | Việc | Cách kiểm tra |
|---|---|---|
| 4.1 | **Nhập chuyển đổi ngoại tuyến từ CRM** (`05`: "CHƯA triển khai"): upload SQL và Đặt cọc kèm GCLID, tần suất hằng ngày, dùng giá trị 181.000.000đ cho cọc | Ads hiển thị "SQL (offline)" và "Đặt cọc (offline)" có số; đối chiếu khớp CRM ±2% |
| 4.2 | Đặt SQL-offline làm **hành động chuyển đổi chính duy nhất** để đấu thầu, `generate_lead` xuống Phụ | Cột "Chuyển đổi" ≈ số SQL, không còn ≈ số lead thô |
| 4.3 | Lên lộ trình **vùng chứa server-side** (GTM #17) cho GĐ2–GĐ3 | — |

**Cái gì KHÔNG làm và vì sao:** không đổi mô hình phân bổ sang data-driven **trong GĐ1**. Lý do: đổi mô hình cùng lúc với đổi conversion action sẽ làm không thể quy kết thay đổi số liệu cho nguyên nhân nào. Đổi ở đầu GĐ2, sau khi đã có 30 ngày baseline sạch.

### Trang đích, tiện ích, đối tượng — GĐ1

| Việc | Căn cứ số |
|---|---|
| **Ngừng toàn bộ lưu lượng vào v1**, 100% sang `/nhan-bang-gia-2026` (v2) | v2 hoàn tất form 28,0% vs v1 20,4% (+37,3%), LCP 1,9s vs 4,8s (`10_GA4` C) |
| Sau khi dọn GTM: đo lại LCP, mục tiêu **≤ 1,5s** | GTM tự gây +0,8s (`12_GTM` header) |
| Tối ưu riêng bản di động của v2 | Di động = 78,1% chi phí nhưng CVR 2,03% vs desktop 4,02% (`07` B); v2 di động hoàn tất form 24,6% vs desktop 41,3% (`10_GA4` C) |
| Thêm **reCAPTCHA v3 + OTP số điện thoại** | `05`: "Không có reCAPTCHA, không xác minh OTP"; PMax 31% trùng SĐT, 24% SĐT sai (`08` C) |
| Tạo **danh sách loại trừ**: khách đã cọc, đã ký HĐMB, môi giới | `05`: "Chưa loại trừ"; Competitor 26% lead là môi giới/đối thủ (`08` C) |
| Đối tượng chuyển từ Quan sát → Nhắm mục tiêu cho GDN; xây danh sách `form_start` bỏ dở (**7.458 form_start vs 1.715 lead** = 5.743 người bỏ dở) | `10_GA4` B & E |
| Bắt đầu A/B test có kiểm soát (hiện `05`: "1 phiên bản, không thử nghiệm") | — |

---

## GIAI ĐOẠN 2 — Ngày 31–60: "MỞ RỘNG CÓ KIỂM SOÁT"

### Mục tiêu định lượng

| Chỉ tiêu | Mục tiêu GĐ2 | GĐ2 cũ |
|---|---:|---:|
| Chi phí | ≤ 690.000.000đ | 604.392.000đ |
| SQL | ≥ 310 | 184 |
| CP/SQL | ≤ 2.230.000đ | 3.284.739đ |
| SQL/Lead | ≥ 33% | 24,2% |
| Cọc | ≥ 11 | 5 |
| ROAS | ≥ 2,6x | 1,41x |
| CĐ_Ads/Lead_CRM | ≤ 1,10x | — |
| IS Brand | ≥ 85% | 51,0% |

### Cấu trúc & giá thầu

- **Brand:** chuyển sang **tCPA 700.000đ** nếu đã thỏa điều kiện ở GĐ1; giữ Tỷ lệ hiển thị mục tiêu nếu chưa. Mở thêm AG4 cho từ khóa thương hiệu + ý định tài chính (`… trả góp`, `… lãi suất`, `… chính sách`) — `01_BOI_CANH` nêu chính sách ân hạn gốc 24 tháng / hỗ trợ lãi suất 0% 18 tháng là điểm bán mạnh chưa được khai thác trong search terms hiện có.
- **Generic:** chuyển **tCPA 2.200.000đ** khi đủ ≥50 chuyển đổi sạch/30 ngày. Nhân bản 6 cụm từ đã chứng minh có SQL sang đối sánh Chính xác, đặt giá thầu riêng: `nhà phố hóc môn` (41 SQL), `căn hộ hóc môn giá bao nhiêu` (30 SQL), `mua nhà phố quận 12` (26 SQL), `khu đô thị tây bắc tphcm` (19 SQL), `nhà phố dưới 8 tỷ tphcm` (14 SQL), `shophouse hóc môn` (13 SQL). Mỗi nhóm ≤ 15 từ khóa (hiện 31), **≥ 3 RSA/nhóm** (hiện 1) — nhắm nâng QS từ 5,2 lên ≥ 7.
- **PMax:** bật lại ở 90tr **chỉ khi** GĐ1 đạt SQL/Lead ≥ 20%. tCPA 2.500.000đ, brand exclusion BẬT, loại trừ vị trí đặt đã cập nhật, tín hiệu đối tượng = danh sách khách đã cọc.
- **YouTube:** bật lại 15tr, CPV mục tiêu, đánh giá bằng data-driven (căn cứ: bị last-click đánh giá thấp 283,7%).
- **GDN:** 45tr, tách 3 nhóm theo mức ý định.

### Đo lường GĐ2

| Việc | Kiểm tra |
|---|---|
| **Đổi mô hình phân bổ sang data-driven** (sau khi có 30 ngày baseline sạch) | So bảng phân bổ lead trước/sau; kỳ vọng Brand giảm ~32%, YT tăng, GDN tăng (`10_GA4` D) |
| Triển khai **vùng chứa server-side** (GTM #17) | So sánh số sự kiện client vs server; kỳ vọng thu hồi 5–15% sự kiện bị ad-blocker chặn — **con số này là kỳ vọng ngành, không có trong dữ liệu, cần đo thực tế** |
| Nâng `zalo_click`/`file_download` lên chuyển đổi Chính nếu 30 ngày quan sát cho thấy tương quan với SQL | Đối chiếu tỷ lệ SQL của lead đến từ Zalo vs form |
| Đối soát 3 nguồn hằng tuần | CĐ_Ads/Lead_CRM ≤ 1,10x |

### Trang đích / đối tượng GĐ2
- A/B test có kiểm soát trên v2: biến thể A (giá hiển thị ngay above the fold) vs B (hiện tại). Ngưỡng quyết định: ≥ 1.000 phiên/nhánh, chênh ≥ 15% tỷ lệ hoàn tất form.
- Xây Customer Match từ danh sách CRM (khách đã cọc) làm tín hiệu tương tự cho PMax và làm danh sách loại trừ cho GDN.

---

## GIAI ĐOẠN 3 — Ngày 61–90: "ĐẨY QUANH SỰ KIỆN MỞ BÁN"

### Mục tiêu định lượng

| Chỉ tiêu | Mục tiêu GĐ3 | GĐ3 cũ |
|---|---:|---:|
| Chi phí | ≤ 810.000.000đ | 653.449.000đ |
| SQL | ≥ 395 | 316 |
| CP/SQL | ≤ 2.050.000đ | 2.067.877đ |
| Cọc | ≥ 17 | 11 |
| ROAS | ≥ 3,4x | 2,98x |
| CP/cọc | ≤ 47.600.000đ | 59.404.455đ |

**Cộng dồn 3 GĐ: 250 + 310 + 395 = 955 SQL; 7 + 11 + 17 = 35 cọc → 6.335.000.000đ → ROAS 3,02x** ✔ thỏa đồng thời cả KPI 32 cọc lẫn KPI ROAS 3,0x.

### Cấu trúc & giá thầu
- **Generic:** cân nhắc chuyển **tROAS** (mục tiêu 300%) — chỉ khi offline import đã chạy ≥ 45 ngày và có ≥ 15 cọc gắn GCLID. Nếu chưa đủ, **giữ tCPA** — không mạo hiểm đổi chiến lược ở giai đoạn quyết định doanh số.
- **Brand:** đẩy IS lên ≥ 90%, thêm ngân sách sự kiện mở bán, sitelink trỏ thẳng lịch sự kiện.
- **Competitor:** mở lại 20tr **chỉ khi** báo cáo Auction Insights xác nhận có đại lý khác đấu giá trên tên dự án (kịch bản D2). Nếu không có, 20tr này về Dự phòng.
- **PMax:** 120tr nếu đã chứng minh SQL/Lead ≥ 20%.

### Đo lường GĐ3
- Chạy **thử nghiệm nâng cao (lift test)** cho Brand: tắt Brand ở 20% khu vực trong 14 ngày, đo chênh lệch cọc → trả lời D1 bằng dữ liệu thật thay vì suy luận (xem D1).
- Đối soát cuối kỳ 3 nguồn, chốt báo cáo bàn giao.

---

## C-5. Tiêu chí dừng / mở rộng (ngưỡng số cụ thể — kiểm tra thứ Hai hằng tuần)

**Tiêu chí DỪNG (bắt buộc hành động, không thảo luận):**

| Điều kiện | Cửa sổ | Hành động |
|---|---|---|
| Chiến dịch chi > 100.000.000đ mà 0 SQL | 30 ngày | **Tắt ngay** (Competitor đã vi phạm: 176,7tr / 3 SQL) |
| CP/SQL > 5.000.000đ (ngưỡng báo động `09`) | 21 ngày | Cắt 50% ngân sách, điều tra; không hồi phục sau 14 ngày → tắt |
| SQL/Lead < 12% (ngưỡng báo động `09`) | 30 ngày | Tắt (PMax đã vi phạm: 7,4%) |
| CĐ_Ads/Lead_CRM > 1,8x | 14 ngày | Đóng băng ngân sách chiến dịch, kiểm tra thẻ trước |
| CP/cọc > 60.333.333đ (trần hòa vốn B5) | 45 ngày | Giảm 30% ngân sách |
| Lead thô > 96/ngày (T2–T6) hoặc > 24/ngày (T7–CN) | 3 ngày liên tiếp | **Giảm ngân sách ngay** — quá năng lực sale thì lead thứ 97 có giá trị âm (`01`, `08` B) |
| `generate_lead` = 0 trong 6 giờ giờ hành chính | tức thời | Cảnh báo tự động → dừng tăng ngân sách cho tới khi xác minh thẻ |

**Tiêu chí MỞ RỘNG (mở khóa Dự phòng 160tr, phải thỏa ĐỦ cả 3):**

| Điều kiện | Ngưỡng | Cửa sổ |
|---|---|---|
| CP/SQL | ≤ 2.000.000đ | 14 ngày liên tiếp |
| SQL/Lead | ≥ 33% | 14 ngày |
| Tỷ lệ lead được gọi <5 phút | ≥ 60% (hiện 11%) | 14 ngày |
| **Cách mở rộng** | Tăng tối đa **+20% ngân sách/tuần/chiến dịch**, ưu tiên Brand đến khi IS ≥ 90% rồi mới đến Generic | — |

**Chốt chặn không thương lượng:** không tăng ngân sách bất kỳ chiến dịch nào khi tỷ lệ lead được gọi trong ngày chưa đạt ≥ 90% (`08` B: GĐ3 mới đạt 79%). Mua thêm lead mà sale không gọi kịp là biến chi phí quảng cáo thành chi phí thuần.

---

# PHẦN D — XỬ LÝ TÌNH HUỐNG

## D1. "Cắt hết ngân sách brand, dồn cho từ khóa chung"

**Trả lời: không đồng ý cắt hết — nhưng anh đúng một nửa, và tôi có cách kiểm chứng phần còn lại bằng thí nghiệm.**

**Lập luận 1 — số học của việc chuyển tiền:**

| | SEA_Brand | SEA_Generic |
|---|---:|---:|
| Chi phí 90 ngày | 260.219.000đ (14,4% NS) | 677.994.000đ (37,6% NS) |
| Cọc | **13 (72,2% toàn tài khoản)** | 5 |
| Doanh thu HH | 2.280.000.000đ (**72,8%**) | 850.000.000đ |
| **CP/cọc** | **20.016.846đ** | **135.598.800đ** (gấp **6,8 lần**) |
| ROAS | **8,76x** | 1,25x |
| CP/SQL | 739.259đ | 3.549.707đ (gấp 4,8 lần) |
| SQL/Lead | 41,1% | 32,5% |
| Lead dùng được (`08` C) | 67% | 46% |

Chuyển toàn bộ 260.219.000đ từ Brand sang Generic, ở đúng CP/cọc mà Generic đang đạt (135.598.800đ/cọc), sẽ mua được **1,9 cọc thay vì 13 cọc** ⇒ **mất 11,1 cọc ≈ 2.005.654.456đ hoa hồng**. Đó là chi phí của đề xuất này.

**Lập luận 2 — "chỉ ăn theo" là giả thuyết, và dữ liệu đã bác một phần:** `10_GA4` mục D so last-click với data-driven. Đúng là last-click **thổi Brand lên**: 592 → 401 lead (**−32,3%**, mức thổi lớn nhất tài khoản, anh có lý ở điểm này). **Nhưng sau khi trừ hết phần thổi đó, Brand vẫn giữ 401/1.715 = 23,4% tổng lead** — không phải con số của một kênh "chỉ ăn theo".

**Lập luận 3 — Brand đang bị bỏ đói chứ không thừa tiền:** IS Brand chỉ **53,4%**, **mất 39,7% do hết ngân sách** (`09_BENCHMARK`: >20% là "tiền đang bỏ lại trên bàn"). Gần một nửa số người đang gõ đúng tên dự án của mình không thấy quảng cáo của mình. Thêm nữa **6,9% IS mất do thứ hạng** — nghĩa là đã có người khác đứng trên mình ở chính từ khóa tên dự án.

**Lập luận 4 — rủi ro bất đối xứng:** nếu cắt Brand mà giả thuyết "ăn theo" đúng, ta tiết kiệm 260tr. Nếu sai, ta mất tới 2 tỷ hoa hồng. Cược lệch 8:1 theo hướng xấu.

**Đề xuất thay cho việc cắt — thí nghiệm có kiểm soát, không phải tranh cãi:** ở GĐ3, tắt Brand tại **20% khu vực địa lý** trong **14 ngày**, so số cọc/lead của nhóm tắt với nhóm chạy.
- Nếu lead nhóm tắt giảm **< 10%** ⇒ anh đúng, tôi cắt Brand xuống 50% và tự chịu trách nhiệm.
- Nếu giảm **> 25%** ⇒ tôi đúng, ta tăng Brand lên đến IS 90%.
- Chi phí thí nghiệm: rủi ro tối đa ~2 cọc trong 14 ngày. Rẻ hơn 11,1 cọc rất nhiều.

---

## D2. Đối thủ bắt đầu đấu giá trên tên thương hiệu dự án

**Bằng chứng việc này ĐANG xảy ra:** Brand mất **6,9% IS do thứ hạng** (`02`, `Mat_IS_ThuHang`, bình quân gia quyền) — ở từ khóa thương hiệu của chính mình, con số này lẽ ra gần 0. CTR Brand 11,63% cũng chỉ nằm trong dải "trung bình ngành 8–12%" chứ chưa đạt ngưỡng tốt >12% (`09_BENCHMARK`, ghi chú: *"Giảm mạnh thường do đối thủ đấu giá"*).

**4 hành động — 2 trong Google Ads, 2 ngoài Google Ads:**

| # | Ở đâu | Hành động | Ngưỡng đo |
|---|---|---|---|
| 1 | **Trong Ads** | **Chiếm giữ vị trí 1 tuyệt đối trên từ khóa thương hiệu chính xác**: chuyển Brand sang "Tỷ lệ hiển thị mục tiêu 95%, vị trí đầu tiên", trần CPC 25.000đ. Kèm mở khóa dự phòng nếu cần. Căn cứ kinh tế: CP/cọc Brand 20.016.846đ, còn cách trần hòa vốn 60.333.333đ tới 3 lần ⇒ **có dư địa trả gấp 3 CPC hiện tại mà vẫn có lãi** | IS ≥ 95%, mất IS do thứ hạng ≤ 2%, trong 14 ngày |
| 2 | **Trong Ads** | **Nâng cấp nội dung quảng cáo & tiện ích để đẩy Ad Rank thay vì chỉ đẩy giá thầu**: ≥3 RSA/nhóm (hiện 1), thêm tiện ích Cuộc gọi + Giá + Chú thích + Vị trí nhà mẫu (hiện chỉ có 4 sitelink), tiêu đề ghim chứa đúng tên dự án. Mục tiêu nâng QS từ 5,2 lên ≥8 ⇒ giảm CPC thực trả ngay cả khi đối thủ đấu cao hơn. Đồng thời bật **brand exclusion cho PMax** để PMax ngừng tự cạnh tranh giá thầu với chính Brand | QS Brand ≥ 8; CPC Brand không tăng quá 20% so với 13.663đ |
| 3 | **Ngoài Ads** | **Yêu cầu chủ đầu tư thực thi chính sách thương hiệu**: gửi văn bản cho Vinhomes/ban quản lý F1 yêu cầu ra quy định cấm đại lý F1/F2 bid tên dự án, kèm ảnh chụp quảng cáo vi phạm; song song nộp **khiếu nại nhãn hiệu (trademark complaint)** với Google cho phần **nội dung quảng cáo** dùng tên nhãn hiệu (Google không cấm bid từ khóa nhưng chặn dùng nhãn hiệu trong ad copy) | Quảng cáo vi phạm biến mất; IS thứ hạng về ≤2% |
| 4 | **Ngoài Ads** | **Chiếm SERP tự nhiên để đối thủ chỉ mua được vị trí quảng cáo chứ không mua được cú nhấp**: đẩy SEO cho cụm brand + biến thể đang có lượng tìm (`04`: `vinhomes hóc môn` 54.597 hiển thị, `… giá bán` 27.378, `dự án …` 24.015, `vin hóc môn` 17.158, `vinhomes hoc mon` 9.909) — viết bài trả lời đúng 2 cụm nghi ngờ đang tồn tại (`vinhomes hóc môn có thật không` 7.894 hiển thị, `… ở đâu` 8.987), tối ưu Google Business Profile của nhà mẫu, gom review | Top 3 organic cho ≥5 cụm brand trong 90 ngày |

**Điều KHÔNG làm:** không trả đũa bằng cách bid ngược lên tên đối thủ. Bằng chứng ngay trong tài khoản này: SEA_Competitor đã tiêu **176.746.000đ để đổi lấy 3 SQL và 0 cọc**, CP/SQL 58.915.333đ. Chiến thuật đó đã được thử và đã thất bại.

---

## D3. "PMax có chi phí trên mỗi chuyển đổi thấp nhất — dồn ngân sách vào đó"

**Trả lời: KHÔNG. Kế toán đang đọc đúng một cột số nhưng đó là cột số bị hỏng.**

**Bước 1 — xác nhận kế toán đọc không sai:**

| Chiến dịch | CP/CĐ_Ads | CP/SQL | CP/cọc |
|---|---:|---:|---:|
| **PMAX** | **267.817đ** ← thấp nhất | 7.793.049đ | **n/a — 0 cọc** |
| SEA_Brand | 298.759đ | **739.259đ** | **20.016.846đ** |
| GDN_Remarketing | 430.493đ | 3.611.361đ | n/a |
| YT_Video | 470.017đ | 10.399.125đ | n/a |
| SEA_Generic | 1.021.075đ | 3.549.707đ | 135.598.800đ |
| SEA_Competitor | 5.701.484đ | 58.915.333đ | n/a |

Đúng, PMax rẻ nhất **ở cột CP/CĐ_Ads**. Nhưng thứ hạng **đảo ngược hoàn toàn** ở hai cột sau.

**Bước 2 — vì sao cột đó hỏng:** cột "Chuyển đổi" chứa 34,7% sự kiện không phải khách hàng (B6). PMax là chiến dịch hưởng lợi nhiều nhất từ lỗi này: tỷ lệ CĐ_Ads/Lead_CRM của PMax là **2,14x**, cao nhất tài khoản, **vượt ngưỡng báo động 1,8x** (`03_TONG_HOP_CD`, `09_BENCHMARK`). Cụ thể PMax đóng góp **438/612 view_price_page** và **259/361 engaged_30s** (`10_GA4` mục B) — tức PMax một mình chiếm **71,6% và 71,7%** của hai loại sự kiện rác. Nói cách khác: **PMax rẻ nhất chính vì nó tạo ra nhiều tín hiệu rác nhất.**

**Bước 3 — theo dấu tiền đi đến cuối phễu:**

```
PMax: 475.376.000đ → 1.775 CĐ_Ads → 829 lead CRM → 61 SQL → 10 đi xem → 2 booking → 0 CỌC → 0đ
```

| Bằng chứng chất lượng PMax | Số | Nguồn |
|---|---:|---|
| SQL/Lead | **7,4%** (ngưỡng báo động <12%) | `02`, `09` |
| CP/SQL | 7.793.049đ (báo động >5tr) | `02` |
| Thoát nhanh <3 giây | **74,3%**; phiên trung vị **3 giây** | `11_CLARITY` B |
| Lead dùng được (mẫu 160) | **7%**; trùng SĐT 31%; SĐT sai 24% | `08` C |
| Hao hụt nhấp→phiên | 28,0% (sheet ghi rõ bất thường với PMax) | `10_GA4` B |
| Doanh thu | **0đ** | `02` |

**Bước 4 — con số cho kế toán:** nếu dồn thêm 100 triệu vào PMax ở hiệu suất hiện tại, ta mua thêm **~373 CĐ_Ads, ~12,8 SQL, 0 cọc, 0đ doanh thu**. Nếu đưa 100 triệu đó vào Brand ở CP/cọc 20.016.846đ, ta mua **~5,0 cọc ≈ 904.000.000đ hoa hồng**. Chênh lệch của một quyết định 100 triệu: **904 triệu**.

**Bước 5 — tôi làm gì với PMax:** không tắt hẳn (là kênh duy nhất có quy mô), nhưng **cắt từ 475tr xuống 260tr (−45%)**, và chỉ bật lại quy mô sau khi đủ **cả ba** điều kiện: (1) `view_price_page` + `engaged_30s` đã hạ xuống Phụ, (2) brand exclusion + danh sách loại trừ vị trí đặt đã bật, (3) tCPA 2.500.000đ đã đặt. **Ngưỡng phán quyết: sau 30 ngày chạy sạch, nếu SQL/Lead < 15% ⇒ tắt vĩnh viễn.**

---

## D4. Ngân sách bị cắt còn 1,2 tỷ cho 90 ngày

**Nguyên tắc: cắt theo thứ tự CP/cọc giảm dần. Cái gì chưa từng tạo ra cọc thì cắt trước, cái nào rẻ nhất trên mỗi cọc thì giữ đến cuối.**

**Thứ tự cắt (cần cắt 603.537.000đ so với mức chi 1.803.537.000đ của kỳ trước, và 900.000.000đ so với kế hoạch 2,1 tỷ):**

| Thứ tự cắt | Đối tượng | Số tiền | Vì sao cắt trước |
|---|---|---:|---|
| 1 | **SEA_Competitor** — tắt hoàn toàn | −176.746.000đ | 3 SQL, 0 cọc, CP/SQL 58.915.333đ = 11,8x ngưỡng báo động |
| 2 | **YouTube** — tắt hoàn toàn | −83.193.000đ | 0 cọc; đầu phễu không nuôi nổi trong kỳ thắt lưng buộc bụng (ghi nhận: data-driven cho thấy YT đóng góp 165 lead — đây là **cắt đau, có ý thức**, sẽ mở lại đầu tiên khi ngân sách hồi phục) |
| 3 | **PMax** — giảm còn 90tr | −385.376.000đ | 26,4% ngân sách, 0 cọc, 7% lead dùng được. Giữ mức tối thiểu để không mất lịch sử học |
| 4 | **Địa lý ngoài vùng bán** (áp lên mọi chiến dịch còn lại) | −434.652.417đ tiềm năng | 0 cọc trên 434tr (`06_DIA_LY`) |
| 5 | **Khung 20:00–06:00 + hạ giá thầu T7–CN** | (đan xen với #4) | CP/SQL 3,0–4,1tr, chỉ 12–34% lead được gọi <30 phút |
| 6 | **Cụm từ rác của Generic** | −242.982.000đ tiềm năng | 11 cụm × 0 SQL |
| 7 | **GDN** — giảm còn 120tr | −10.009.000đ | Giữ được vì rẻ và data-driven cho thấy bị đánh giá thấp +40,9% |

**Giữ đến cuối cùng, theo thứ tự ưu tiên bảo vệ:**
1. **SEA_Brand** — thứ cuối cùng bị đụng đến. 72,2% số cọc, CP/cọc 20,0tr, ROAS 8,76x. Trong kịch bản 1,2 tỷ tôi **vẫn tăng** Brand lên 480tr (vs 260tr kỳ trước), vì mất 39,7% IS do ngân sách là dạng lãng phí duy nhất mà thêm tiền lại **giảm** chi phí trên mỗi cọc.
2. **Hạ tầng đo lường** — không cắt một đồng nào (chi phí là công dev, không phải ngân sách media). Ngân sách càng nhỏ thì mỗi đồng càng phải được đo đúng.
3. **SEA_Generic (phần từ khóa đã chứng minh có SQL)** — nguồn khách mới duy nhất.

**Phân bổ 1,2 tỷ:**

| Chiến dịch | Ngân sách | % | Kỳ trước |
|---|---:|---:|---:|
| SEA_Brand_Vinhomes_HocMon | 480.000.000 | 40,0% | 260.219.000 |
| SEA_Generic (chỉ nhóm từ khóa đã có SQL) | 480.000.000 | 40,0% | 677.994.000 |
| GDN_Remarketing_Web30d | 120.000.000 | 10,0% | 130.009.000 |
| PMAX (mức tối thiểu, sau khi sửa) | 90.000.000 | 7,5% | 475.376.000 |
| YT_Video | 0 | 0% | 83.193.000 |
| SEA_Competitor | 0 | 0% | 176.746.000 |
| Dự phòng | 30.000.000 | 2,5% | — |
| **TỔNG** | **1.200.000.000** ✔ | 100% | 1.803.537.000 |

**Điều phải nói thẳng với ban giám đốc — KPI 32 cọc không còn khả thi:** ở CP/SQL mục tiêu 2.200.000đ, 1,2 tỷ mua được **545 SQL → ~20 cọc → 3.628.227.273đ → ROAS 3,02x**. Tức **ROAS 3,0x vẫn giữ được, nhưng số cọc tối đa là ~20, không phải 32**. Tôi cam kết ROAS, không cam kết số cọc — và cần ban giám đốc chọn lại một trong hai KPI làm chuẩn đánh giá ngay khi quyết định cắt được đưa ra.

---

## D5. "GA4 báo 3.820, CRM báo 2.557. Ai đúng?" *(≤150 từ, ngôn ngữ phi kỹ thuật)*

> Anh nhìn con số **CRM: 2.557**. Đó là số người thật.
>
> Con số 3.820 không sai — nó chỉ đang đếm nhầm việc. Trong 3.820 đó có **973 lượt** chỉ là người mở trang bảng giá hoặc ở lại trang 30 giây rồi đi. Không để lại số điện thoại, không phải khách. Thêm **353 lượt** là cùng một người bấm nút gọi nhiều lần, bị đếm thành nhiều khách. Trừ hai khoản đó ra còn 2.494 — gần đúng bằng CRM. Phần lệch còn lại 63 là do một sự cố kỹ thuật ba ngày giữa tháng 4.
>
> **Từ giờ đề xuất anh chấm đội marketing bằng hai con số:** **lead chất lượng (SQL)** và **số cọc**. Kỳ vừa rồi: 651 SQL, 18 cọc.
>
> Con số 3.820 tôi vẫn theo dõi, nhưng để chẩn đoán kỹ thuật — không dùng để đánh giá ai.

*(147 từ)*

---

## D6. "Sửa GTM không tạo ra lead nào, để cuối quý. Giờ tăng ngân sách trước"

**Phản biện 1 — mệnh đề "không tạo ra lead" đã bị chính dữ liệu của chúng ta bác bỏ.** Ba lỗi kỹ thuật đang mở khiến **370–480 lead không đến được với sale trong 90 ngày** (`11_CLARITY` mục C, các mục trạng thái CHƯA SỬA). Quy theo CPL thực tế 705.333đ = **261–339 triệu đồng tiền quảng cáo đã tiêu để mua lưu lượng rồi vứt đi**; quy tiếp ra cọc = **2,6–3,4 cọc = 471–612 triệu hoa hồng**. Đặc biệt lỗi #4: khách bấm Gửi, form không gửi được, **và không có thông báo lỗi** — họ tin là đã đăng ký và ngồi chờ điện thoại. Sửa nó tạo ra lead theo nghĩa đen nhất của từ này.

**Phản biện 2 — tăng ngân sách trước khi sửa đo lường sẽ làm hại nhiều hơn giúp.** Google đang học từ tập tín hiệu có **34,7% là rác** (973 sự kiện không phải khách + 353 lượt đếm trùng). Bằng chứng hậu quả có sẵn: PMax đã tiêu **475.376.000đ theo đúng tín hiệu đó và cho ra 0 cọc**. Thêm ngân sách vào hệ thống học sai không mua thêm kết quả — nó mua thêm tốc độ đi sai hướng. Đây không phải suy đoán: `12_GTM` mục C viết nguyên văn *"Máy học tối ưu theo tín hiệu rác — nguyên nhân gốc của toàn bộ vấn đề PMax"*.

**Phản biện 3 — bài toán chi phí cơ hội.** Bước cầm máu quan trọng nhất (hạ `view_price_page` và `engaged_30s` xuống Phụ, đổi `click_to_call` sang đếm "Một lượt") **không cần đội IT một phút nào** — là 3 thao tác trong giao diện Google Ads, tôi tự làm trong buổi sáng. Phần cần IT là 2–3 ngày công. Đổi lại: 261–339 triệu ngừng chảy ra ngoài. Không có hạng mục nào khác trong kế hoạch có tỷ suất hoàn vốn gần mức đó.

**Phản biện 4 — rủi ro tái diễn.** Sự cố ngày 44–46 làm mất trắng 63 lead và **3 ngày mới bị phát hiện**, vì tài khoản không có cảnh báo chuyển đổi = 0 (`12_GTM` #18). Nguyên nhân gốc — trigger dựa vào class CSS — vẫn còn nguyên. Lần tới dev đổi giao diện, chuyện đó xảy ra lại, và với ngân sách đã tăng thì thiệt hại sẽ lớn hơn tỷ lệ thuận.

**Nếu buộc phải nhượng bộ, tôi giữ lại đúng HAI hạng mục:**

| # | Hạng mục | Vì sao đây là hai thứ không thể bỏ |
|---|---|---|
| **1** | **Dọn hành động chuyển đổi**: hạ `view_price_page` (612) + `engaged_30s` (361) xuống Phụ, đổi `click_to_call` sang đếm "Một lượt" | Sửa **34,7% tín hiệu sai** đang lái toàn bộ Smart Bidding trên 2,1 tỷ. **Không tốn một giờ công IT nào** — nằm hoàn toàn trong Google Ads, tôi tự làm. Nếu IT bận thì đây chính xác là hạng mục không đụng đến IT, nên không có lý do gì để hoãn |
| **2** | **Sửa lỗi JS `TypeError e.setDate`** (Clarity #4) + **cài cảnh báo chuyển đổi = 0** | Lỗi #4 là hạng mục đắt nhất trong nhóm chưa sửa: **280–340 lead**, ~200–240 triệu, và khách hoàn toàn không biết mình đã thất bại. Cảnh báo conversion=0 là bảo hiểm rẻ nhất tài khoản — mất vài giờ cài, ngăn được đúng loại sự cố đã lấy đi 63 lead. Hai việc này gộp lại ≈ **2 ngày công IT** |

**Những gì tôi đồng ý hoãn tới cuối quý:** vùng chứa server-side, Consent Mode v2, dọn toàn bộ 34 thẻ, gắn Clarity session ID vào CRM. Đều quan trọng, đều không cấp cứu.

**Một điều kiện đi kèm nhượng bộ:** nếu hoãn phần còn lại, tôi cần ban giám đốc chấp nhận rằng **báo cáo hiệu quả 90 ngày tới sẽ có sai số đã biết** và tôi sẽ báo cáo bằng số CRM, không bằng số Google Ads.

---

# PHẦN E — KẾ HOẠCH 7 NGÀY ĐẦU

10 việc, xếp theo **giá trị thu hồi trên mỗi giờ bỏ ra** giảm dần. Các việc 1–4 không phụ thuộc ai ngoài tôi.

| # | Ngày | Việc | Kết quả kỳ vọng ĐO ĐƯỢC | Căn cứ |
|---|---|---|---|---|
| **1** | N1 (sáng) | **Hạ `view_price_page` (612 lượt) và `engaged_30s` (361 lượt) từ chuyển đổi Chính → Phụ; đổi `click_to_call` từ đếm "Mỗi lượt" → "Một lượt"** | Cột "Chuyển đổi" giảm từ ~3.820 xuống ~2.494 nhịp 90 ngày (**−34,7%**); tỷ lệ CĐ_Ads/Lead_CRM đi từ 1,49x về ≤1,15x trong 14 ngày; PMax rời khỏi mức báo động 2,14x | A-1, B6 |
| **2** | N1 (chiều) | **Loại trừ địa lý ngoài vùng bán** (Hà Nội, Đà Nẵng, ĐBSCL, Đồng Nai) + đổi tùy chọn vị trí từ "Hiện diện HOẶC quan tâm" → **"Chỉ Hiện diện"** trên cả 6 chiến dịch | Giải phóng **~4,83 triệu đ/ngày** (434.652.417đ ÷ 90) đang chi cho khu vực có **0/18 cọc**; chi phí ngoài TP.HCM+BD+LA giảm ≥80% trong 7 ngày | A-6, `06_DIA_LY` |
| **3** | N1 (chiều) | **Tạm dừng SEA_Competitor** + **cắt PMax xuống 3 triệu đ/ngày** (từ ~5,3tr/ngày) | Ngừng chảy ~1,96 triệu đ/ngày (Competitor 176.746.000÷90) đang đổi lấy 0 cọc; ngừng ~2,3tr/ngày của PMax. Tổng tiết kiệm tuần 1: **~30 triệu đ**, không mất cọc nào (cả hai đang ở 0 cọc) | A-2, A-5 |
| **4** | N1–N2 | **Đẩy danh sách phủ định chia sẻ ≥150 từ** (nhóm: tuyển dụng, việc làm, học phí, vinschool, thuê, nhà trọ, kho xưởng, quy hoạch, giá đất, thổ cư, lừa đảo, chung cư mini) + **tắt Search Partners & Display-in-Search** trên 3 CD Search | Chặn 11 cụm từ đã tiêu **242.982.000đ với 0 SQL**; kỳ vọng CPC Generic giảm từ 33.070đ và tỷ lệ chi phí đối sánh Rộng giảm từ 71% xuống ≤40% trong 14 ngày | A-4, `04_SEARCH_TERMS`, `05` |
| **5** | N2 | **Chốt brief kỹ thuật với dev + đặt deadline N7 cho 3 lỗi Clarity CHƯA SỬA** (#4 JS `e.setDate`, #5 nút bị chat che, #6 `tel:` desktop) | Cam kết văn bản có ngày; mục tiêu thu hồi **370–480 lead/90 ngày ≈ 261–339 triệu đ chi phí lead**. Nghiệm thu: test thật trên Safari iOS 17.x, nhấp chết ở nút CTA và hotline về ~0 trong Clarity | A-9, B7 |
| **6** | N2 | **Cài cảnh báo tự động "chuyển đổi = 0"** (quy tắc Google Ads + cảnh báo tùy chỉnh GA4), ngưỡng: `generate_lead` = 0 trong 6 giờ giờ hành chính → email + Zalo | Diễn tập: tắt trigger ở staging, phải nhận cảnh báo trong ≤6 giờ. Ngăn tái diễn sự cố N44–46 (mất 63 lead, phát hiện sau 3 ngày) | A-10, `12_GTM` #18 |
| **7** | N3 | **Tăng ngân sách SEA_Brand từ ~2,9tr/ngày lên 6,3tr/ngày** (190tr/30 ngày) + chuyển sang "Tỷ lệ hiển thị mục tiêu 90%, vị trí đầu trang", trần CPC 25.000đ | IS Brand đi từ **53,4%** lên **≥75%** trong 14 ngày; mất IS do ngân sách từ **39,7%** xuống **≤15%**; CP/cọc Brand giữ **≤ 30.000.000đ** (vẫn dưới nửa trần hòa vốn 60.333.333đ) | A-3, B5 |
| **8** | N3–N4 | **Đặt lịch quảng cáo**: tắt 23:00–06:00, giảm giá thầu −40% khung 20:00–23:00, giảm −30% T7–CN | Thu hồi phần lớn **409.402.899đ/90 ngày** (22,7% NS) đang chi vào khung chỉ 12–21% lead được gọi lại trong 30 phút; mục tiêu CP/SQL toàn tài khoản giảm từ 2.770.410đ xuống ≤2.500.000đ trong 21 ngày | A-13, A-14, `07` |
| **9** | N4–N5 | **Họp với trưởng phòng kinh doanh, chốt SLA gọi lại <5 phút giờ hành chính + phân lead tự động + lịch trực T7–CN** | Tỷ lệ lead gọi <5 phút từ **11% → ≥40%** trong 30 ngày; **lead không ai gọi = 0** (kỳ trước 275 lead ≈ 193.966.631đ). Đòn bẩy: nhóm gọi <5 phút có tỷ lệ cọc **1,82%** vs nhóm >12h **0,04%** — chênh 45 lần | A-7, `08` A&B |
| **10** | N6–N7 | **Cài biến ẩn GCLID/GBRAID/WBRAID vào form → CRM; bật Enhanced Conversions; gỡ thẻ "GA4 Config – Copy of Main" trùng lặp** | ≥95% lead mới trong CRM có GCLID (kiểm 20 mẫu); EC trạng thái "Đang ghi nhận"; GA4 Realtime `page_view` bắn đúng 1 lần/tải trang. **Mở khóa** nhập chuyển đổi ngoại tuyến ở tuần 3–4 — điều kiện bắt buộc để tối ưu theo SQL thay vì lead thô | A-11, A-16, `12_GTM` #2/#14/#15 |

**Việc phải làm ngay trong tuần 1 nhưng không phải thao tác kỹ thuật:** trình ban giám đốc mâu thuẫn số học giữa hai KPI (B5) — **32 cọc × 181tr ÷ 2,1 tỷ = 2,76x < 3,0x**. Cần chốt: hoặc nâng mục tiêu lên **35 cọc**, hoặc trần chi chỉ **1.930.666.667đ**. Kế hoạch Phần C của tôi chọn phương án 35 cọc.

**Tổng tác động kỳ vọng của tuần 1:** ngừng ~4,3 triệu đ/ngày chi vào nguồn có 0 cọc (việc 2+3), khóa lại 242.982.000đ/90 ngày cụm từ rác (việc 4), sửa 34,7% tín hiệu sai (việc 1), khởi động thu hồi 261–339 triệu đ lead bị lỗi kỹ thuật chặn (việc 5).

---

## Phụ lục — Truy vết số liệu

| Mục | Sinh từ khối nào trong `agent-4-calc.py` |
|---|---|
| Bảng nền KPI, A-1…A-18 | `B0`, `PHẦN A — SỐ LIỆU CHẨN ĐOÁN`, `PACING & NGÂN SÁCH` |
| B1 | `B1. CPL / CP-SQL / CP-CỌC THEO CHIẾN DỊCH` |
| B2 | `B2. ROAS TOÀN KỲ & THEO GIAI ĐOẠN` |
| B3 | `B3. TỶ LỆ CHUYỂN ĐỔI TỪNG BƯỚC PHỄU` |
| B4, B5 | `B4/B5. NGƯỢC TỪ KPI` (3 kịch bản) |
| B6 | `B6. ĐỐI CHIẾU 3 NGUỒN` (có kiểm chứng N44–46 trên sheet 02) |
| B7 | `B7. LEAD MẤT DO LỖI KỸ THUẬT CHƯA SỬA` |
| Phần C | `PHẦN C — PHÂN BỔ NGÂN SÁCH 2,1 TỶ` (có `assert` tổng = 2.100.000.000) |
| D1 | `D1 — BRAND` |
| D3 | `D3 — PMAX` |
| D4 | `D4 — NGÂN SÁCH CẮT CÒN 1,2 TỶ` (có `assert` tổng = 1.200.000.000) |

Chạy lại: `python3 /home/docdang/Projects/google-ads/test/exam-vinhomes/answers/agent-4-calc.py`
