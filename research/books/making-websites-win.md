# Making Websites Win — Karl Blanks & Ben Jesson (Conversion Rate Experts, 2018)

> Chưng cất cho hệ Google Ads BĐS VN. Chỉ ghi những gì đọc được trong sách; ví dụ/con số đều là của
> sách (khách hàng của CRE), **không phải benchmark BĐS VN**. Khái niệm giữ tên tiếng Anh trong ngoặc.
> Áp dụng cho LP lead-gen một trang, traffic thấp, chưa có hạ tầng A/B test.

---

## 1. Phương pháp CRE — vòng lặp chẩn đoán → giả thuyết → thử nghiệm

Xương sống của sách là **DiPS: Diagnose → Problem → Solution**. Ẩn dụ gốc: bác sĩ *chẩn đoán trước, kê
đơn sau*. Marketer thông thường làm ngược — nhét sẵn testimonial + guarantee + headline mạnh vào trang
mà không biết khách phản đối cái gì. Sách gọi đó là "marketing malpractice": *"vấn đề là ổ khoá, giải
pháp là chìa khoá"* — sai khoá thì chìa đẹp mấy cũng vô dụng, và còn làm loãng đoạn văn duy nhất có thể
cứu được đơn hàng.

Ba nguyên tắc "Scientific Web Design" mà nhóm top website tuân thủ (khác hẳn phần còn lại):
1. **Thiết kế cho chức năng, không cho thẩm mỹ.** Đẹp chỉ đáng theo đuổi khi research cho thấy nó làm
   khách mua nhiều hơn. Đẹp còn có chi phí ẩn: trang càng cầu kỳ càng chậm sửa (ví dụ của sách: in
   nghiêng một từ mất 7 ngày) — mà tốc độ lặp mới là thứ sinh lời.
2. **Đo mọi thay đổi** (A/B test hoặc thí nghiệm có kiểm soát khác). Quy trình đổi từ
   `Có ý tưởng → Quyết có làm không → Làm` thành `Có ý tưởng → Làm như một test → Quyết có giữ không`.
3. **Sửa nhỏ, sửa thường xuyên; gần như không bao giờ redesign toàn site.** Work-in-progress là "nấm độc
   của doanh nghiệp": chưa lên live thì chưa sinh tiền, dự án càng dài kỳ vọng càng nặng, càng ì.

**Chống "meek tweaking" (tinh chỉnh rón rén)** — cảnh báo quan trọng nhất cho hệ traffic thấp: cải thiện
càng nhỏ càng *lâu* phát hiện, một cách phi tuyến. Với trang 300 view/ngày, sách đưa: cải thiện 80% phát
hiện trong **2 ngày**; 20% mất **23 ngày**; 10% mất **vài tháng**. Nên: thay đổi **táo bạo, có mục tiêu**
(đúng nỗi sợ/khao khát của khách), không đổi màu nút. Phần mềm test là đồng hồ bấm giờ, không phải chân
chạy: **GI → GO** (Garbage In → Garbage Out).

**Vòng lặp lặp được (chốt từ sách):**

```
1. Chẩn đoán  — chạy 2-4 kỹ thuật ở §2 cho tới khi nghe khách nói cùng một điều nhiều lần
2. Lập bảng O/CO — objection ↔ counterobjection, xếp theo tần suất được nhắc
3. Giả thuyết — chọn 1 objection mạnh nhất; giải pháp phải là "chìa khớp ổ", không phải best practice
4. Dựng bản nháp dễ sửa (wireframe/chữ trước, đẹp sau) → user test 1-2 người → sửa → test lại
5. Đo: A/B test nếu đủ traffic; nếu không → user test + micro-conversion + fixed-period testing
6. Giữ cái thắng, vứt cái thua, quay lại bước 1
```

Bài học low-traffic của sách, nguyên văn ý: nếu công cụ tính thời lượng test cho thấy **mọi** test sẽ
mất >6 tháng thì **chỉ dùng user test**, quay lại A/B khi business lớn hơn. User test hơn A/B ở ba điểm:
nhanh (10 phút), cho biết **vì sao**, và **chi tiết tới từng phần** của trang.

---

## 2. Bộ kỹ thuật CHẨN ĐOÁN "vì sao khách không chuyển đổi"

Sách nhấn: mỗi kỹ thuật là **một ngọn đèn rọi (spotlight)** vào một mặt hành vi khác nhau — dùng tổ hợp,
đừng kỳ vọng một công cụ trả lời hết. Và nhóm kỹ thuật giá trị nhất là nhóm **ultra-qualitative** (method
marketing, bán trực tiếp, gọi điện, VOC aggregator) — không ai đóng gói được thành phần mềm trả phí nên
ít ai nói tới, không vì thế mà kém giá trị.

| # | Kỹ thuật (tên sách) | Cần gì | Hệ này có sẵn? | Làm NGAY với 10 req Clarity/ngày? |
|---|---|---|---|---|
| 1 | **Web analytics** — vào từ đâu, bấm gì | GA4 | ✅ GA4 `548678683` | ✅ (không tốn quota Clarity) |
| 2 | **Click map / confetti + scroll map** — chỗ nào bị bấm dù không bấm được, cuộn tới đâu, "false bottom" | Crazy Egg/Hotjar | ✅ **Clarity heatmap** thay được | ✅ đọc trên **web UI**, 0 request API |
| 3 | **Session recording** — xem lại phiên, thấy lỗi, thấy chỗ vật lộn | Hotjar/Clicktale | ✅ Clarity (⚠️ **LP Beachtro chưa gắn Clarity**) | ✅ web UI; MCP chỉ để lọc/tổng hợp |
| 4 | **Form analytics** — rớt ở field nào, field nào bỏ trống, field nào sinh lỗi, thiết bị nào tệ | Formisimo/Hotjar | ⚠️ **KHÔNG có bản chuyên** | ⚠️ thay thế gần đúng: Clarity rage/dead click trên form + segment "có `form_start`, không submit" (đã có trong `clarity-checklist.md` §2) |
| 5 | **Live chat** — khách tự nói ra phản đối, mình thử counterobjection ngay | Tawk/Drift… | ❌ | ❌ — nhưng **Zalo/hotline là bản VN của kỹ thuật này** |
| 6 | **Survey khách hàng** + câu hỏi vàng | SurveyMonkey/Forms | ⚠️ chưa dùng | ✅ **Google Forms 0đ, hoặc sale hỏi miệng qua điện thoại** |
| 7 | **Exit survey** — 3 câu: mục đích ghé? có làm được không? cái gì cản? | Qualaroo/Hotjar | ❌ | ❌ (cần công cụ) — ghi vào backlog |
| 8 | **On-page survey** — hỏi đúng lúc khách đang nghĩ điều đó | Qualaroo/Informizely | ❌ | ❌ |
| 9 | **Nút "Give Feedback" thường trực** | Có thể chỉ là link tới form | ⚠️ chưa có | ✅ rẻ nhất: link Zalo có sẵn |
| 10 | **Site search log** — khách tìm gì mà không thấy | Search nội bộ | ❌ (LP 1 trang) | ❌ không áp dụng |
| 11 | **Theo dõi mentions** (Google Alerts…) | Miễn phí | ⚠️ chưa dùng | ✅ — group/forum BĐS VN nói gì về dự án |
| 12 | **Method marketing** — tự đi làm khách: gọi hotline dự án, đi xem nhà mẫu, để lại số cho đối thủ | 0 công cụ | ✅ làm được | ✅ **giá trị/phút cao nhất trong bảng** |
| 13 | **Method marketing với đối thủ offline** — sàn/nhà mẫu offline thường đã giải xong bài online chưa giải | 0 công cụ | ✅ | ✅ |
| 14 | **Bán trực tiếp** + bảng 2 cột Objection/Counterobjection do chính người bán ghi | 0 công cụ | ✅ | ✅ — sách nói bảng này thành "kho copy đã kiểm chứng" |
| 15 | **VOC aggregator** — nói chuyện với người cả ngày nói chuyện với khách (sale, telesale, CSKH) | 0 công cụ | ✅ có đội sale | ✅ **nhanh nhất để hiểu khách** |
| 16 | **Đọc cách người khác mô tả sản phẩm** — Wikipedia, review, tin nhắn khách giới thiệu cho bạn | 0 công cụ | ✅ | ✅ — lấy đúng từ vựng khách dùng cho headline |
| 17 | **Khuyến khích khách gọi điện** — kể cả chỉ bật số 1-2 ngày để nghiên cứu; điện thoại là "intuition pump" | Số hotline | ✅ đã có `tel:` | ✅ |
| 18 | **Knowledge base** — gom câu hỏi + câu trả lời tốt nhất | Notion/Docs | ⚠️ chưa | ✅ |
| 19 | **User test / hallway usability test** — giao nhiệm vụ, im lặng quan sát, ghi chú | 0 công cụ, người quen cũng được | ✅ | ✅ **kỹ thuật mạnh nhất sách, làm được ngay hôm nay** |
| 20 | **Retrospective moderated user test** — mời người **vừa đăng ký xong** kể lại đường đi và chỗ suýt bỏ | 0 công cụ | ✅ | ✅ |
| 21 | **Eye tracking** | Phần cứng/EyesDecide | ❌ | ❌ |
| 22 | **Pop-up survey tuyển người user test** (Ethnio) | Công cụ | ❌ | ❌ |
| 23 | **A/B test** | Optimizely/VWO | ❌ **chưa có hạ tầng** | ❌ — §1 nói rõ: traffic thấp thì dùng user test thay |
| 24 | **Phân tích đối thủ** — họ đã học được gì về khách của mình | 0 công cụ | ✅ đã có `research/competitors/` | ✅ |

**Làm được NGAY, không tốn một request Clarity nào: #12, #14, #15, #16, #19, #20, #24 — và câu hỏi vàng (#6).**

### Câu hỏi vàng của sách

> **"Điều gì suýt khiến anh/chị KHÔNG [đăng ký/mua] của chúng tôi?"**

Ba lý do sách giải thích vì sao nó mạnh — và vì sao **phải hỏi người ĐÃ chuyển đổi, không hỏi người bỏ đi**:
1. Người bỏ đi là một mớ hỗn tạp, phần lớn không đủ điều kiện mua; họ hay đổ tại giá — **cá trích đỏ**.
2. Người đã mua đã đi hết phễu, họ biết mình nói gì.
3. Họ vượt được rào nhưng **vẫn nhớ rào** — và mỗi người vượt được thì có nhiều người đã bỏ cuộc ở đúng rào đó.

Bộ 3 câu cho exit survey (khi có công cụ): *mục đích ghé trang là gì → hôm nay có làm được không → cái gì
cản anh/chị làm được điều đó?*

---

## 3. Các "win" pattern lặp lại nhiều nhất — lọc cái áp được cho LP lead-gen BĐS VN một trang

Xếp theo mức độ sách lặp lại và mức áp được cho một LP đăng ký:

1. **Trang dài là được, trang chán mới chết.** Case goHenry (+78% sign-up): trang mobile dài "2,5 m", xử
   lý **từng objection theo thứ tự mạnh → yếu**, và **rải CTA suốt trang** ngay sau mỗi objection được gỡ.
   Nguyên tắc: *ngắn nhất có thể, dài như cần thiết*.
2. **Nói trước, viết sau (speak first, write later).** Quay video người bán giỏi nhất thuyết phục trong 7
   phút → gỡ băng → dùng làm khung copy cho LP. Moz: +52% trong A/B test, tổng thể gần gấp ba.
3. **"Của cải giấu trong nhà" (hidden wealth) / proof magnet.** Bằng chứng thuyết phục đã tồn tại nhưng
   khách không thấy. goHenry đưa **Visa** to hơn cả brand của mình → xoá sạch nghi ngờ. Mobal quên nhắc
   món quà tặng kèm; nhắc vào thì doanh số tăng.
4. **Số liệu thay tính từ.** "Diệt 99,9% vi khuẩn", "8/10 chủ mèo nói…", "giao trong 30 phút hoặc miễn
   phí" — thay cho "rất tốt/ưu đãi hấp dẫn". Trùng khớp với luật đã có của hệ về "con số chính sách".
5. **Nói rõ nó LÀ CÁI GÌ, bằng ngôn ngữ thường** — "branding waffle" giết chuyển đổi. Cách kiểm nhanh:
   copy toàn bộ chữ của trang sang trình soạn thảo text trần rồi đọc lại. *Chữ mới là thứ thắng A/B test.*
6. **Future pacing — vẽ ra chuyện gì xảy ra SAU KHI khách đồng ý.** Sơ đồ/flow "đặt hàng → giao → dùng →
   nhận hoá đơn". Sách nói CRE "thường xuyên thắng" chỉ nhờ thêm khối này. **Đây là pattern áp thẳng được
   vào form nhận bảng giá.**
7. **Headline dạng spoiler/teaser, không phải categorizer.** "Media mentions" (tệ) → "Báo TIME, CNN đã viết
   về chúng tôi" (tốt). Đặt tên section theo cái người đọc lướt cần biết.
8. **Progressive disclosure bằng overlay/accordion/tooltip, không đẩy sang trang khác** — gỡ được objection
   đúng lúc mà không kéo khách ra khỏi phễu (sunshine.co.uk: "Số điện thoại của chúng tôi đâu?" trong
   overlay, là một trong các yếu tố tạo thêm ~20 triệu USD/năm).
9. **Separation of concerns** — trang dài phải như **danh bạ**, không như tiểu thuyết Nga: module rõ ràng,
   nhãn rõ ràng, nền xen kẽ/khung để phân đoạn. Khách lạc thì không bao giờ đọc tới counterobjection.
10. **Giảm cam kết của bước đầu (no-brainer / lead-gen page).** Xin ít thì cần ít chữ để thuyết phục. ⚠️
    Kèm cảnh báo ở §4.
11. **Hazelnut Trail** — phễu nhiều bước, mỗi bước là một "hạt dẻ" hấp dẫn ngay, khoảng cách đều. Đổ hết
    phần thưởng ở cuối đường thì con sóc không đi. Kèm khái niệm **readiness**: khách mua khi họ sẵn sàng;
    việc của mình là *có mặt trong đầu họ* hoặc *có mặt trong quy trình mua* lúc đó.
11b. **Giữ được liên lạc thì hết áp lực chốt trong một phiên** — lấy contact, retargeting, dễ nhớ tên.
12. **Urgency/scarcity có LÝ DO thật.** Luôn kèm *vì sao* có deadline. Framing mất mát mạnh hơn framing
    được lợi (Prospect Theory). Nhưng đây là kỹ thuật cho vấn đề "khách trì hoãn" — chỉ dùng khi chẩn
    đoán ra vấn đề đó.
13. **Trust: chọn đúng loại proof.** Quy mô & tốc độ tăng trưởng · review/testimonial (đặc biệt từ chuyên
    gia) · dữ liệu · liên kết người nổi tiếng · **demonstration** · social proof (khách hàng danh giá).
    Ngành tài chính & sức khoẻ cần trust nặng nhất — BĐS cùng nhóm rủi ro cao. **Tin công ty ≠ tin sản
    phẩm: hai bài toán riêng, phải giải cả hai.**
14. **Guarantee chỉ thắng khi có rủi ro + có hoài nghi.** Hai chức năng: giảm rủi ro *và* tự nó là bằng
    chứng ("chúng tôi dám thế thì chắc là thật"). Phải có tên riêng, viết theo hướng khẳng định ("chúng tôi
    cam kết bạn sẽ…"), nói rõ vì sao dám cam kết, dễ đòi, không ràng buộc ẩn.
15. **Niching** — thắng bằng cách thu hẹp để trở thành "tốt nhất" trong một thế giới nhỏ, thay vì đấu tổng lực.
16. **"Handover of Death"** — chương *thrive in an imperfect world*, sách nêu **đích danh môi giới BĐS**:
    phần cuối phễu do người khác nắm (đội sale/CĐT). Bảy cách chống: (1) thuyết phục xong hẳn rồi mới bàn
    giao, (2) **đảm bảo khách đủ điều kiện (qualify) trước khi bàn giao**, (3) *cố mọi giá đưa mã đo lường
    lên trang chuyển đổi cuối* — nếu chỉ đo được cú click rời đi, bạn sẽ tối ưu cho việc rời đi chứ không
    phải cho chuyển đổi, (4) là điểm đến chứ không phải nhà ga, (5) dễ nhớ, (6) cho khách lý do để đi qua
    mình, (7) mở rộng ảnh hưởng để sửa được phần không thuộc quyền mình.
17. **Mobile phải nghiên cứu RIÊNG.** goHenry: khách mobile bốc đồng hơn, biết ít hơn về sản phẩm, **lo về
    trust/bảo mật cao hơn 40%**. Cản trở thêm của mobile: mất tập trung, mạng chậm, bàn phím khó, màn hình
    nhỏ (*"người dùng đặc biệt vật lộn với form"*), đọc ngoài nắng.

---

## 4. Luật về form + friction + trust — đối chiếu form 2 field của Beachtro

Form hiện tại: **họ tên + SĐT**, không dropdown (chưa có bảng giá nên thang ngân sách không neo vào đâu),
7 vị trí cùng POST về Keap, honeypot + chặn submit <2s + chuẩn hoá số + gclid/UTM qua `inf_custom_url`.

| Luật của sách | Đối chiếu Beachtro |
|---|---|
| **Giảm cam kết thì cần ít chữ hơn để thuyết phục**; lead-gen page được sách gọi là bước-thấp-cam-kết *đặc biệt hiệu quả* | ✅ **2 field là đúng sách cho giai đoạn pre-launch.** Ma trận CRO hiện tại chấm "chỉ tên + SĐT = 1 điểm, hút rác" — đúng cho LP có giá, **sai như một luật phổ quát** |
| ⚠️ **Nhưng: hạ cam kết chỉ là HOÃN cam kết** — "coi chừng tối ưu một trang xong rồi vấn đề nhảy xuống cuối phễu" | ⚠️ Chính xác điều `audit-lp.md` §0 đã ghi: CPL rẻ giả tạo, gánh nặng lọc dồn sang sale. Sách xác nhận đây là **đánh đổi có thật**, không phải win |
| **"Đảm bảo khách qualify trước khi bàn giao"** (chống Handover of Death) | ⚠️ Hiện **không có lớp qualify nào** trên LP. Nhưng sách không bắt buộc qualify bằng *dropdown* — có thể qualify bằng **copy** (nói thẳng khoảng đầu tư dự kiến, phần "phù hợp với ai / không phù hợp với ai" — LP đã có mục này, giữ và đẩy lên gần form) |
| **Form analytics**: đo rớt theo field, field bỏ trống, field sinh lỗi, thiết bị tệ | ❌ Không có công cụ. Thay thế: Clarity rage/dead click + segment `form_start` không submit |
| **Mobile: người dùng vật lộn với form** vì màn hình nhỏ + bàn phím | ✅ 2 field là lựa chọn đúng cho 75-85% traffic mobile của VN |
| **Future pacing — nói rõ chuyện gì xảy ra sau khi bấm gửi** | ❌ **Khoảng trống lớn nhất của form này.** Khách VN để lại SĐT sợ bị gọi làm phiền; sản phẩm giao *"khi CĐT công bố"* — tức là một lời hứa mơ hồ đổi lấy số điện thoại thật |
| **Guarantee khi có rủi ro + hoài nghi, viết khẳng định, không ràng buộc ẩn** | ⚠️ Rủi ro ở đây không phải tiền mà là **bị làm phiền**. Bản BĐS của guarantee: một dòng cam kết cách dùng số ("gửi bảng giá qua Zalo, không gọi ngoài giờ, không chuyển số cho bên thứ ba") |
| **Tin công ty ≠ tin sản phẩm** | ✅ LP đã có nhận diện SmartRealtors + "đối tác chiến lược Sun Group". Theo pattern goHenry/Visa: **cân nhắc để Sun Group / Blanca City nổi hơn brand phân phối** ở màn hình đầu |
| **Proof phải khớp objection**, không rải best practice | ⚠️ Chưa có bảng O/CO nào cho dự án → hiện tại mọi phần "tăng trust" đều là phỏng đoán |

---

## 5. Bảng đề xuất sửa cụ thể (CHỈ ĐỀ XUẤT — không tự sửa file nào)

### 5a. Cho `landing-page/README.md` — khung chẩn đoán đang thiếu

| # | Đề xuất bổ sung | Vì sao (theo sách) | Ưu tiên |
|---|---|---|---|
| 1 | **Luật DiPS đứng trước ma trận**: trước khi thêm/bỏ bất kỳ phần tử nào, phải ghi được *objection nào nó trả lời và biết bằng cách nào*. Không có objection = không thêm | Ma trận 7 tiêu chí hiện tại là danh sách best practice; sách gọi việc áp best practice mù là "marketing malpractice" — nó cũng làm loãng đoạn duy nhất có thể cứu deal | 🔴 cao |
| 2 | **Bắt buộc có file `objections.md` (bảng O/CO) cho mỗi dự án**, nguồn từ sale + hotline + Zalo, xếp theo tần suất được nhắc | Bảng 2 cột này là "kho copy đã kiểm chứng" — CRE dùng nó để nhân đôi CVR của Mobal | 🔴 cao |
| 3 | **Thêm mục "Chẩn đoán tối thiểu trước khi chấm điểm"**: ≥3 user test mobile + ≥5 câu hỏi vàng với người đã đăng ký. Không có = chưa được chấm ma trận | Traffic thấp + không A/B ⇒ sách bảo **chỉ dùng user test**; đây là kỹ thuật mạnh nhất cả cuốn và tốn 0đ | 🔴 cao |
| 4 | **Sửa neo tiêu chí 3 (Form & qualifying)**: 1 điểm không phải "chỉ tên + SĐT" mà là **"mức cam kết của form không khớp giai đoạn phễu"**; thêm ghi chú: form ngắn ở giai đoạn pre-launch là đúng, nhưng phải khai báo đánh đổi và bù bằng qualify ở copy | Sách coi lead-gen page thấp-cam-kết là kỹ thuật thắng, kèm cảnh báo "cam kết chỉ bị hoãn" | 🔴 cao |
| 5 | **Thêm tiêu chí 8: "Sau khi bấm gửi" (future pacing)** — trang nói rõ nhận gì, khi nào, qua kênh nào, ai liên hệ, số điện thoại được dùng thế nào | Một trong các pattern CRE "thường xuyên thắng"; hiện ma trận dừng lại đúng ở nút submit | 🔴 cao |
| 6 | **Luật chống meek tweaking**: dưới ngưỡng traffic X, cấm A/B test thay đổi nhỏ; chỉ đổi táo bạo, 1 giả thuyết/1-2 tuần, và mặc định dùng user test + micro-conversion | Đường cong thời lượng test: 20% cải thiện mất >10× thời gian so với 80% | 🟡 vừa |
| 7 | **Thêm khối "Handover of Death"** vào khung phân tích: LP của hệ luôn bàn giao cho sale/CĐT ⇒ 3 việc bắt buộc: thuyết phục xong mới bàn giao · có lớp qualify · đưa mã đo tới điểm chuyển đổi cuối *(mục 3 là món nợ đã ghi nhận có ý thức trong `audit-lp.md`)* | Sách nêu đích danh môi giới BĐS làm ví dụ | 🟡 vừa |
| 8 | **Ghi rõ trong bảng "Skill nào cho việc nào"**: Clarity heatmap/replay thay được click-map + session recording, **nhưng KHÔNG thay được form analytics** và cũng không thay được survey/user test | Sách coi form analytics là hạng mục riêng, "cực kỳ quan trọng vì người chạm vào form rất dễ chuyển đổi" | 🟡 vừa |
| 9 | Thêm 1 dòng vào checklist nghiệm thu: **đọc lại toàn bộ chữ của LP ở dạng text trần** (bỏ hết thiết kế) | "Chữ mới là thứ thắng A/B test" | 🟢 thấp |

### 5b. Cho LP Beachtro — việc đáng làm khi có 1-2 tuần traffic thật

| # | Việc | Công sức | Vì sao đáng làm |
|---|---|---|---|
| 1 | **Gắn Clarity TRƯỚC khi traffic về** (hiện chưa có tag nào) | 15 phút | Không có replay/heatmap thì 2 tuần traffic đầu — thứ đắt nhất — trôi qua không để lại chẩn đoán nào |
| 2 | **Hỏi câu hỏi vàng với 20-30 người đăng ký đầu tiên**: *"Điều gì suýt khiến anh/chị không để lại số?"* — sale hỏi luôn trong cuộc gọi đầu, ghi vào 1 sheet | ~0 | Kỹ thuật sinh insight/phút cao nhất của sách; hợp với chốt "hệ không đo lead" vì đây là **định tính**, không phải đo lường lead |
| 3 | **5 user test mobile** với người ngoài (task: *"anh/chị muốn biết giá dự án này, thử xem"*), im lặng quan sát, ghi chỗ khựng | 1 buổi | Sách: traffic thấp + không A/B ⇒ user test là công cụ đo chính. Người **ít rành web** cho nhiều insight hơn |
| 4 | **Thêm khối future pacing ngay dưới/trong form**: (1) nhận tin nhắn xác nhận ngay, (2) bảng giá + chính sách gửi qua Zalo khi CĐT công bố, (3) cam kết cách dùng số — không gọi ngoài giờ, không chuyển cho bên thứ ba | 1-2 giờ | Đây là objection lớn nhất của một form 2 field ở VN, và là pattern sách nói "thường xuyên thắng" |
| 5 | **Thêm Zalo + sticky bar** (đã nằm trong `audit-lp.md` mục 4 #2) — và coi Zalo là **kênh chẩn đoán**, đọc log chat hàng tuần để nhặt objection | 1-2 giờ | Bản VN của "live chat" + "khuyến khích khách gọi điện" (intuition pump): khách tự nói ra cái đang cản họ |
| 6 | **Dựng bảng O/CO từ 20 cuộc gọi đầu của sale** → phản hồi ngược vào copy LP + RSA headline | ~0, làm cùng #2 | Mobal: bảng này nhân đôi CVR; Sony: nhân viên bán hàng kể ra 22 điều khách cần biết mà website không có |
| 7 | **Speak-first-write-later**: ghi âm sale giỏi nhất pitch Beachtro 7 phút → gỡ băng → viết lại hero + 2 section mạnh nhất theo đúng logic đó | nửa buổi | Moz +52%; đặc biệt hợp khi chưa có giá — thứ bán được lúc này là *lập luận*, không phải con số |
| 8 | **Thêm một "hạt dẻ" giao NGAY** cạnh lời hứa bảng giá tương lai (ví dụ: mặt bằng/quỹ căn/tiến độ gửi liền sau khi đăng ký) | 2-3 giờ | Hazelnut Trail: hạt dẻ phải hấp dẫn và **có ngay**; hiện phần thưởng duy nhất nằm ở tương lai không có ngày |
| 9 | **Đưa Sun Group / Blanca City nổi hơn brand phân phối ở màn hình đầu** — nếu user test (#3) xác nhận nghi ngờ về pháp lý/uy tín | 1 giờ | Pattern goHenry↔Visa: mượn trust của thương hiệu khách đã tin sẵn. **Chỉ làm sau khi chẩn đoán xác nhận**, đúng luật DiPS |
| 10 | **KHÔNG dựng A/B test giai đoạn này.** Đo bằng micro-conversion đã có (`form_start`, scroll tới form, `phone_click`/`zalo_click`) + so sánh theo từng campaign (luật Simpson đã có trong README) | 0 | Sách: mọi test >6 tháng ⇒ chỉ dùng user test; và nếu vẫn muốn quyết, dùng **fixed-period testing** + hạ ngưỡng ý nghĩa xuống 85-90% thay vì không test gì |
| 11 | **Urgency chỉ khi thật**: nếu đợt ưu tiên chọn căn/booking có ngày cụ thể thì nói ngày + **lý do**; không thì bỏ | 0 | Sách bắt buộc "luôn nêu vì sao có deadline"; trùng luật deadline-thật đã có của hệ |

---

## Tóm tắt — 10 phát hiện quan trọng nhất

1. **DiPS**: chẩn đoán trước, kê đơn sau. Ma trận CRO hiện tại của hệ là danh sách best practice — thiếu hẳn bước chẩn đoán đứng trước nó.
2. **Chống meek tweaking**: cải thiện 20% mất hơn **10×** thời gian phát hiện so với 80% ⇒ traffic thấp thì chỉ đổi táo bạo.
3. Traffic thấp + chưa có A/B ⇒ sách bảo thẳng: **dùng user test làm công cụ đo chính**, quay lại A/B khi lớn hơn.
4. **Câu hỏi vàng "điều gì suýt khiến anh/chị không đăng ký?" — hỏi người ĐÃ đăng ký, không hỏi người bỏ đi.** 0đ, làm được ngay tuần này.
5. Nhóm kỹ thuật mạnh nhất là **ultra-qualitative** (đóng vai khách, bán trực tiếp, nói chuyện với sale/VOC aggregator) — hệ có đủ điều kiện, 0 công cụ.
6. Clarity thay được click-map + session recording, **không thay được form analytics, survey, user test** — và LP Beachtro **hiện chưa gắn Clarity**, đây là lỗ hổng chẩn đoán lớn nhất trước khi traffic về.
7. Form 2 field của Beachtro **đúng sách** cho giai đoạn pre-launch (lead-gen thấp-cam-kết), nhưng sách cảnh báo cam kết chỉ bị **hoãn** xuống cuối phễu — trùng đúng rủi ro `audit-lp.md` §0 đã ghi.
8. Khoảng trống lớn nhất của form: **future pacing** — nói rõ nhận gì, khi nào, qua kênh nào, số điện thoại được dùng thế nào. Pattern sách nói "thường xuyên thắng".
9. Sách nêu **đích danh môi giới BĐS** trong chương "Handover of Death": phải qualify khách trước khi bàn giao và cố đưa mã đo tới điểm chuyển đổi cuối.
10. Pattern win lặp nhiều nhất áp được ngay: **trang dài xử lý objection theo thứ tự + rải CTA · nói-trước-viết-sau · phơi bằng chứng đang bị giấu (Sun Group như Visa của goHenry) · số liệu thay tính từ · headline dạng spoiler.**
