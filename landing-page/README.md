# NGỮ CẢNH CRO — đọc trước khi làm/review/audit bất kỳ landing page nào của dự án

> Bản đồ + luật cho agent về tối ưu tỷ lệ chuyển đổi. Số liệu gốc: `research/google-ads-bds-vn.md` §6.
> Teardown 4 LP đối thủ đã có: `research/competitors/2026-07-eco-retreat.md` — đừng làm lại.

## Vì sao CRO là đòn bẩy lớn nhất

BĐS VN: **click rẻ (~25-40k₫), lead đắt** — CVR real estate chỉ ~45% mức trung bình các ngành.
Đích CVR LP: **3-6%, dưới 2% = LP hỏng**. Nâng CVR 1,5% → 4% có tác dụng ngang tăng 2,5× ngân
sách — không tốn thêm đồng quảng cáo nào. Gửi traffic về homepage thay LP riêng = mất 50-70% CVR.

## Yếu tố 1: Message match (khớp thông điệp)

Chuỗi phải khớp 100%, đứt ở đâu mất tiền ở đó:

```
keyword người dùng gõ → RSA headline (đã pin H1, campaign-setup §3) → H1 của LP → hero visual → CTA đầu tiên
```

Luật:
- **Mỗi nhóm ad một đích riêng** — URL/anchor đã đặt trong campaign-setup (Path `bang-gia`...).
  Search "eco retreat bảng giá" phải rơi vào màn hình có bảng giá/form tải bảng giá, không phải hero chung chung.
- Nguồn chân lý của cặp keyword↔thông điệp↔LP block: **`keywords/adgroup-map.md` bảng message match**.
  LP mới/section mới phải đối chiếu bảng này; thêm cặp mới thì cập nhật bảng, không tự chế.
- 3 luồng traffic chính → 3 yêu cầu H1 khác nhau:
  | Nhóm ad | Người dùng vừa gõ | H1/hero phải nói về |
  |---|---|---|
  | Brand dự án | "eco retreat bảng giá" | Tên dự án + bảng giá/quỹ căn đợt này |
  | Khu vực-giao dịch | "khu đô thị bến lức" | Vị trí + loại hình + khoảng giá "từ X tỷ" |
  | Tài chính-trả góp | "eco retreat trả góp" | Con số chính sách: % thanh toán, ân hạn, lãi suất |
- Cách chấm khi audit: mỗi luồng chấm 1-5 (5 = từ khóa xuất hiện nguyên văn hoặc đồng nghĩa trực tiếp
  trong H1 + màn hình đầu trả lời đúng câu hỏi của keyword). Dưới 4 = việc phải sửa.
- Bài học đối thủ (competitor research): chính sách bán hàng mạnh nhất mà **giấu con số** khỏi LP
  (chỉ nói "ưu đãi hấp dẫn") = thua kẻ có chính sách yếu hơn nhưng trình bày đủ số.

## Yếu tố 2: Above the fold (màn hình đầu, mobile-first 390px)

75-85% traffic VN là mobile — thiết kế màn hình đầu cho mobile trước, desktop là hệ quả.

Thứ tự phần tử bắt buộc trong màn hình đầu:
1. **H1 ≤2 dòng** — khớp message match theo bảng trên
2. **Khoảng giá hiện rõ** ("từ 2,5 tỷ") — anchoring + tự lọc khách không đủ tài chính (marketing-psychology)
3. **1 USP chính sách bằng con số** (vd "25% đến khi nhận nhà · ân hạn 24 tháng") — không viết "ưu đãi khủng"
4. **CTA kép**: nút "Nhận bảng giá" (→ form/anchor) + **Zalo/hotline sticky** (CTA chính của khách VN,
   track `zalo_click`/`phone_click` — secondary conversion, xem tracking/README.md luật #2)
5. Trust bar 1 dòng: CĐT + ngân hàng bảo lãnh + pháp lý
- Deadline chỉ dùng khi **thật** (có ngày cụ thể của đợt bán); deadline giả bị khách VN nhận ra ngay.
- Exit popup: vô dụng trên mobile → dùng **sticky bar**; nếu có popup thì đổi offer ("nhận bảng giá
  qua Zalo"), không lặp lại form chính (skill `popups`).

## Luật DiPS — chẩn đoán trước, kê đơn sau (Making Websites Win, chưng cất 2026-08-06)

Ma trận 7 tiêu chí dưới đây là **danh sách best practice** — nó cho biết trang thiếu gì so với chuẩn, KHÔNG cho biết *vì sao khách của trang này không chuyển đổi*. Áp best practice mù = "marketing malpractice": mỗi objection là ổ khoá, mỗi giải pháp là chìa — chìa sai còn làm loãng đoạn duy nhất cứu được deal. Chi tiết + bộ kỹ thuật chẩn đoán: `research/books/making-websites-win.md`.

Luật khi LP đã có traffic:
1. **Chẩn đoán tối thiểu trước khi chấm điểm/sửa**: câu hỏi vàng *"Điều gì suýt khiến anh/chị KHÔNG đăng ký?"* hỏi 20–30 người ĐÃ đăng ký (sale hỏi trong cuộc gọi đầu, 0đ) + Clarity heatmap/recording (đọc web UI, không tốn quota API). Đừng hỏi người bỏ đi — câu trả lời của họ là cá trích đỏ.
2. Lập bảng **O/CO** (objection ↔ counterobjection) xếp theo tần suất → mỗi lần sửa LP nhắm đúng 1 objection mạnh nhất.
3. **Traffic thấp thì cấm "meek tweaking"**: cải thiện 10–20% mất hàng tháng mới đo ra — chỉ đổi táo bạo có mục tiêu, và khi mọi A/B test sẽ mất >6 tháng thì **chỉ dùng user test**.
4. **Future pacing cạnh form** (khoảng trống hay gặp nhất): nói rõ khách sẽ nhận gì, khi nào, qua kênh nào, SĐT được dùng thế nào — ma trận hiện dừng đúng ở nút submit.

## Yếu tố 3: Khung phân tích điểm yếu chuyển đổi (khi được yêu cầu audit)

Xếp hạng theo tác động, kiểm theo thứ tự:
1. **Message match** 3 luồng (chấm 1-5 như trên) — sai ở đây thì mọi thứ dưới vô nghĩa
2. **Above the fold** so với 5 phần tử bắt buộc
3. **Form**: 4 field + 2 dropdown qualifying đúng spec `tracking/lp-requirements.md`? Form dài hơn = rác ít
   hơn nhưng phải đúng 2 dropdown (ngân sách, mục đích), không hơn
4. **Objection lớn nhất chưa xử lý** — với Eco Retreat: bàn giao Q2/2028 (đối thủ Waterpoint có 500+ hộ
   đang ở) → biến ân hạn 24 tháng thành lý do mua sớm, block tiến độ ảnh thật + ngày tháng
5. **Bậc 1 research §6 đủ chưa**: bảng giá, mặt bằng từng loại căn, pháp lý, tốc độ <2,5s/4G
6. **Dữ liệu hành vi** (khi LP đã chạy): Clarity theo `tracking/clarity-checklist.md` §2 (rage/dead click
   form, scroll tới bảng giá, replay form_start-không-submit, lọc theo campaign spend cao nhất)

⚠️ **Luật Simpson khi so sánh LP cũ/mới**: CVR tổng tài khoản trước/sau ngày đổi LP là số **không được phép
dùng** nếu cơ cấu traffic đổi giữa 2 kỳ (campaign mới bật, mix kênh đổi) — một kênh đầu-phễu CVR≈0 bật lên
đủ kéo CVR tổng đi xuống trong khi LP mới thực chất tốt hơn ở TỪNG campaign. So sánh hợp lệ duy nhất: CVR
theo từng campaign (hoặc chỉ Search) + tỷ lệ hoàn tất form theo thiết bị, cùng khung ngày. Kiểm luôn xem
2 kỳ có ngày tracking gãy hoặc thẻ đo trùng lặp làm nhiễu mẫu số không (đối chiếu lịch sử GTM) trước khi
tin bất kỳ con số nào.

## Ma trận đánh giá CRO (chấm điểm LP — dùng khi nghiệm thu, so sánh phiên bản, hoặc audit đối thủ)

Mỗi tiêu chí chấm 1–5 theo mô tả neo. **Điểm tổng = Σ(điểm × trọng số).**
Trọng số xếp theo tác động đã chứng minh trong `research/google-ads-bds-vn.md` §6+§9.

| Tiêu chí | Trọng số | 1 điểm | 3 điểm | 5 điểm |
|---|---|---|---|---|
| **1. Message match** (3 luồng ad) | 25% | H1 chung chung, không nhắc keyword; mọi ad group đổ về cùng một hero | Khớp tên dự án/khu vực nhưng màn hình đầu không trả lời đúng câu hỏi của keyword | Cả 3 luồng ≥4/5: keyword xuất hiện trong H1, anchor riêng từng ad group, section đích đúng modifier |
| **2. Above the fold mobile** (390px) | 20% | Chỉ ảnh render + tên dự án; giá và CTA phải scroll mới thấy | Có H1 + CTA nhưng thiếu khoảng giá hoặc USP con số | Đủ 5 phần tử đúng thứ tự: H1 ≤2 dòng, khoảng giá, USP số, CTA kép + Zalo sticky, trust bar |
| **3. Form & qualifying** | 15% | Chỉ tên + SĐT ("để lại SĐT nhận ưu đãi") — hút rác | Đủ field nhưng thiếu dropdown qualifying hoặc thiếu hidden fields gclid/utm | Đúng spec lp-requirements.md: 4 field + 2 dropdown, honeypot, validate đầu số, gclid/utm đổ vào Keap |
| **4. Offer & con số chính sách** | 15% | "Ưu đãi hấp dẫn, liên hệ ngay" — không một con số | Có % thanh toán hoặc CK nhưng rời rạc, không quy đổi ("chỉ X triệu/tháng") | Con số đầy đủ + quy đổi dễ hiểu + deadline thật có ngày; offer khớp giai đoạn funnel (skill `offers`) |
| **5. Objection & trust** | 10% | Không pháp lý, không tiến độ, không pháp nhân ở footer | Có pháp lý + tiến độ nhưng objection lớn nhất (vd bàn giao Q2/2028) bị lờ đi | Objection lớn nhất được xử lý chính diện; tiến độ ảnh thật + ngày; CĐT/ngân hàng bảo lãnh/MST đầy đủ |
| **6. Tốc độ & kỹ thuật** | 5% | >4s trên 4G, ảnh 4K không nén | 2,5–4s, còn lib thừa | <2,5s/4G, ảnh nén, tel:/Zalo link đúng chuẩn |
| **7. Đo lường** | 10% | Không GTM/event nào bắn | Có GA4 nhưng thiếu event registry hoặc chưa test GTM Preview | Đủ 6 event đúng registry, bắn thử pass, Clarity cài đúng lp-requirements |

**Thang kết luận:**

| Điểm tổng | Kết luận |
|---|---|
| ≥ 4,0 | Xuất sắc — launch, chuyển sang tối ưu bằng data (Clarity/A-B test) |
| 3,0 – 3,9 | Đạt — được launch, các mục <3 vào backlog tuần đầu |
| 2,0 – 2,9 | Chưa launch — sửa các mục trọng số cao trước (message match → above the fold) |
| < 2,0 | Làm lại theo `cro-blueprint` / skill `no-code-landing-re` |

**Hard gates — rớt 1 cái là KHÔNG launch bất kể tổng điểm:** tiêu chí 7 (Đo lường) <3 · không có khoảng giá/bảng giá ở bất kỳ đâu · load >4s trên 4G · thiếu pháp nhân/MST ở footer (rủi ro disapproved "Unclear relevance") · hidden field gclid không tới Keap (mất toàn bộ chuỗi ECL).

Khi audit **đối thủ** bằng ma trận này: bỏ tiêu chí 7 (không đo được của họ), chuẩn hóa lại trọng số về 100% — điểm chênh giữa mình và đối thủ ở tiêu chí 1–4 chính là góc phản công đưa vào RSA (nối với `research/competitors/PLAYBOOK.md`).

## Checklist nghiệm thu LP (Fable dùng để QA khi user nộp LP)

| ☐ | Mục |
|---|---|
| ☐ | Message match cả 3 luồng ≥4/5; H1 khớp RSA headline đã pin |
| ☐ | Màn hình đầu mobile 390px đủ 5 phần tử theo thứ tự |
| ☐ | Khoảng giá + con số chính sách hiện rõ (không "ưu đãi hấp dẫn" chay) |
| ☐ | Zalo sticky + tel: link đúng (không phải số dạng text) |
| ☐ | Form đúng spec lp-requirements.md (field, dropdown, honeypot, validate đầu số, hidden fields gclid/utm). **Thang dropdown NGÂN SÁCH phải theo phân khúc** (war-game round 4+9: thang sai = dropdown ngừng qualify): căn hộ `<2/2-4/4-7/>7 tỷ` · đất nền `1,5-2/2-3/>3 tỷ` (bỏ ô dưới giá sàn) · biệt thự `<10/10-20/20-30/>30 tỷ`; đất nền thêm ô mục đích "mua đi bán lại" để cò tự khai |
| ☐ | 6 event dataLayer đúng registry CLAUDE.md, bắn thử bằng GTM Preview |
| ☐ | Section bảng giá + mặt bằng + tiến độ (ảnh thật, ngày) + pháp lý + footer pháp nhân/MST |
| ☐ | Objection bàn giao được xử lý; deadline (nếu có) là thật |
| ☐ | Tải <2,5s trên 4G mobile; ảnh nén; không lib thừa |
| ☐ | Mỗi ad group có URL/anchor đích riêng khớp Path trong campaign-setup |

## Skill nào cho việc nào

| Việc | Skill |
|---|---|
| Audit/cải thiện CVR trang | `cro` |
| Viết/sửa copy H1, hero, CTA | `copywriting` (+ `marketing-psychology` cho framing) |
| Thiết kế offer/ưu đãi đợt bán | `offers` |
| Popup/sticky bar | `popups` |
| Sinh LP BĐS VN từ brochure/URL | `no-code-landing-re` + `frontend-design` |
| Wiring form → Keap | `keap-lead-form` + `ad-click-attribution` |
| A/B test thay đổi lớn | `ab-testing` (1 hypothesis/tuần theo checklist vận hành) |
