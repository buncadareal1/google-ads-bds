# RUBRIC CHẤM v1 (Fable tự lập từ đề + ground truth) — 100đ, cờ đỏ −8đ/cờ

Ground truth: `ground-truth.txt` (sinh bởi `ground-truth-calc.py`). Sai số cho phép: làm tròn ±1%.

## GROUND TRUTH THEN CHỐT

- Toàn kỳ: chi 1.803.537.000đ · 3.820 conv Ads · 2.557 lead CRM · 651 SQL · 206 xem · 59 booking · 18 cọc · DT 3,13 tỷ
- CPL_Ads 472.130 · CPL_CRM 705.333 · CP/SQL 2.770.410 · CP/cọc 100.196.500 · ROAS 1,735
- Funnel: Lead→SQL 25,46% · SQL→Xem 31,64% · Xem→Book 28,64% · Book→Cọc 30,51% · Lead→Cọc 0,70%
- ROAS giai đoạn: GĐ1 0,60 · GĐ2 1,41 · GĐ3 2,98
- B5: 181tr ÷ 3 = **60.333.333đ/cọc** max
- B6: **3.820 = 1.715 generate_lead + 1.132 click_to_call thô + 612 view_price_page + 361 engaged_30s**.
  Rác = 612+361 = **973**. Trùng gọi = 1.132−779 = **353**. → đo được 2.494. CRM 2.557 = 2.494 + **63 mất thẻ N44–46** (GTM v23 đổi class .form-dk-v1→.form-register, v24 sửa N47).
- B7: lỗi CHƯA SỬA = Clarity #4 (JS TypeError Safari iOS, 280–340) + #5 (chat che nút <380px, 60–90) + #6 (tel: desktop, 30–50) = **370–480 lead**; quy tiền theo CPL_CRM 705.333 ≈ **261–339tr**. Phải phân biệt số đo (phiên ảnh hưởng) vs ước tính (lead mất, do đội UX).
- Theo chiến dịch: Brand ROAS 8,76, CP/SQL 739k, 13/18 cọc · Generic ROAS 1,25, CP/SQL 3,55tr, 5 cọc · PMax CPL_Ads thấp nhất 267.817 NHƯNG CP/SQL 7,79tr, 0 cọc, 7% lead dùng được (08C), 74,3% thoát<3s (11B) · Competitor CP/SQL 58,9tr, 0 cọc, 26% môi giới · GDN 3,61tr/SQL 0 cọc · YT 10,4tr/SQL 0 cọc (đầu phễu, DDA 43→165)

## VẤN ĐỀ "PHẢI THẤY" cho Phần A (12 mục)

1. Ô nhiễm chuyển đổi: 4 sự kiện primary trong đó 2 rác (973) + đếm trùng gọi (353) → máy học tối ưu theo rác — NGUYÊN NHÂN GỐC
2. PMax: 475tr = 26% chi phí, 7% lead dùng được, 31% trùng SĐT, 74,3% thoát<3s, 0 cọc
3. Competitor: 176,7tr → 3 SQL 0 cọc, CP/SQL 58,9tr, 26% lead là môi giới
4. Mất thẻ N44–46 (63 lead) + không có cảnh báo conv=0 (mất 3 ngày mới phát hiện)
5. Geo: toàn quốc + "presence OR interest" → HN/ĐN/Cần Thơ/Đồng Nai/nước ngoài ≈ 24,1% chi (~435tr) chỉ ~60 SQL 0 cọc
6. Broad 71% + 12 negative: term rác (tuyển dụng, thuê, nhà trọ, lừa đảo, kho xưởng, quy hoạch...) — sheet 04 các dòng SQL=0 ≈ 232tr
7. Brand đói ngân sách: mất IS ngân sách 36%+ GĐ1, IS ~58% vs benchmark >85%, trong khi brand = 13/18 cọc
8. Không GCLID trong CRM + không Enhanced Conv + không OCI → không tối ưu theo SQL được (chặn đường sửa)
9. LP v1 57 ngày (LCP 4,8s, CMND 61% bỏ) — chậm đổi; 3 lỗi CHƯA SỬA còn mất 370–480 lead
10. GA4 double page_view từ N31 (v22); GTM 412KB +0,8s LCP; 3 thẻ F2 không rõ nguồn
11. Vận hành lead: <5ph contact 87% vs >12h 22%; 26% lead gọi sau 12h; T7–CN 2 sale nhưng chi ~503tr; 20–23h 18,7% chi nhưng 21% được gọi 30ph; 275 lead không ai gọi
12. Search partners + Display BẬT trên Search; audience chỉ Observation; không loại trừ đã cọc; last-click hạ thấp YT/GDN

## THANG ĐIỂM

### A — Chẩn đoán (25đ)
- Độ phủ 12 vấn đề: ≥10 = 15đ, mỗi thiếu −1,5đ
- Đủ 3 thành phần/vấn đề (phát hiện/bằng chứng đúng nguồn/mức độ + tiền): 5đ
- Sắp theo tác động tài chính: 2đ · ≥3 vấn đề kỹ thuật: 3đ

### B — Tính toán (30đ, khớp ground truth)
B1 4đ · B2 3đ · B3 3đ · B4 5đ (logic + giả định rõ + nhất quán + đối chiếu KPI 2,2tr) · B5 3đ (60.333.333) · B6 7đ (đủ 4 thành phần + cộng khớp 2 chiều; thiếu 63 −2; không chứng minh −2) · B7 5đ (370–480 + quy tiền + đo vs ước tính)

### C — Kế hoạch 90 ngày (20đ)
3 GĐ mục tiêu định lượng 3đ · bảng ngân sách TỔNG ĐÚNG 2,1 tỷ 4đ (lệch = 0) · cấu trúc 3đ · bidding + điều kiện chuyển 3đ · đo lường GA4/GTM riêng + thứ tự + verify 4đ (vàng: gỡ 2 sự kiện rác, khử trùng gọi, GCLID→CRM→OCI, alert conv=0, sửa JS #4, trigger không CSS class, xóa dup config) · LP/tiện ích/đối tượng + dừng/mở rộng có ngưỡng 3đ

### D — Tình huống (15đ, 2,5đ/câu)
- D1 GIỮ brand (13/18 cọc, 739k/SQL, ROAS 8,76, DDA 401, competitor đang bid); caveat incrementality = cộng
- D2 4 hành động trong + ngoài Ads
- D3 KHÔNG — CPA Ads ảo; CP/SQL 7,79tr, 7% dùng được, 0 cọc; xét lại SAU khi sạch conversion + OCI
- D4 cắt Competitor → PMax → YT/GDN; GIỮ Brand cuối
- D5 ≤150 từ phi kỹ thuật: nhìn CRM (SQL/cọc), số Ads chỉ cho máy học sau khi sạch
- D6 phản biện: 475tr PMax đang tối ưu theo rác; 2 mục giữ: (a) gỡ rác/khử trùng primary, (b) GCLID vào CRM; alert conv=0 / sửa JS #4 chấp nhận nếu lập luận tốt

### E — 7 ngày đầu (10đ)
10 việc, ưu tiên đúng (cầm máu đo lường trước), mỗi việc có kết quả đo được: 1đ/việc

## CỜ ĐỎ (−8đ/cờ; quá 1 cờ = rớt dù ≥70)
R1 bịa số · R2 sai số học >5% B1–B5 · R3 dồn ngân sách PMax theo CPA Ads · R4 cắt toàn bộ brand · R5 không phát hiện ô nhiễm conversion · R6 B6 cộng không khớp · R7 tổng ngân sách ≠ 2,1 tỷ · R8 coi 3.820 là lead thật · R9 khuyên tin cột Conversions Ads làm KPI · R10 không đụng sheet 10/11/12
