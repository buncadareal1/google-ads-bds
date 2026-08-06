# Trustworthy Online Controlled Experiments — Kohavi, Tang, Xu (Cambridge, 2020)

> Chưng cất cho hệ Google Ads BĐS VN. Đây là tầng **kỷ luật thống kê** đứng trên `making-websites-win.md`
> (đã chốt: traffic thấp → user test, chống meek tweaking). Cuốn Kohavi trả lời câu khác: *khi đọc số,
> lúc nào được kết luận và lúc nào không*. Ưu tiên pitfalls; giữ tên tiếng Anh. Mọi ví dụ/con số là của
> sách (Bing/Google/LinkedIn/Amazon), **không phải benchmark BĐS VN**.
>
> ⚠️ Bối cảnh hệ: GA4 + Google Ads, vài trăm click/tháng giai đoạn đầu, **không có hạ tầng A/B server-side**,
> "thí nghiệm" thực tế = đổi RSA rồi so trước/sau · thêm RSA thứ 2 để Google tự chia · đổi LP rồi so CVR.

---

## 1. Twyman's law + hierarchy of evidence

**Twyman's law:** *"Any figure that looks interesting or different is usually wrong."* Sách coi đây là luật
quan trọng nhất của phân tích dữ liệu. Phản xạ đúng: số đẹp bất thường → **nghi lỗi đo trước, mừng sau**.
Bing từng có alert "revenue-too-high" tự bắn khi doanh thu tăng quá nhanh, vì 99% những lần như thế là
log trùng hoặc trang vỡ. Mặt trái: số xấu thì người ta lại đi tìm lý do để bác bỏ — cùng một thiên kiến.

**Hierarchy of evidence** (Guyatt 1995 / Greenhalgh, sách dịch sang ngôn ngữ online), từ mạnh → yếu:

| Bậc | Loại bằng chứng | Hệ này có gì |
|---|---|---|
| 1 | Meta-analysis nhiều controlled experiment | ❌ |
| 2 | **Randomized controlled experiment (A/B)** — gold standard | ❌ chưa có hạ tầng |
| 3 | **Observational causal study / quasi-experiment** (ITS, diff-in-diff, RDD, IV) | ⚠️ đây là **trần** của hệ hiện tại |
| 4 | Logs-based / retrospective analysis | ✅ GA4 + Ads report |
| 5 | UER, survey, focus group, human evaluation | ✅ (nối `making-websites-win.md` §2) |
| 6 | Ý kiến chuyên gia — HiPPO | ✅ và đây là thứ đang phải cạnh tranh |

Sách rất gay gắt với bậc 3: Young & Karr so 52 claim từ observational study với RCT → **0 cái replicate**,
và **5 cái ngược chiều có ý nghĩa thống kê**. Ioannidis: 5/6 observational study được trích dẫn nhiều thất bại
khi lặp lại. Ví dụ đúng ngành: Lewis–Rao–Reiley đo hiệu quả display ads bằng observational study ra lift
**871–1198%**; cùng nghiệm đó bằng controlled experiment ra **5,4%**. Confound: người vào Yahoo! hôm đó vừa
dễ thấy quảng cáo vừa dễ search — usage là **common cause**, không phải quảng cáo gây ra search.

**Bài học nền:** Tenet 3 — *tổ chức nào cũng dở trong việc đánh giá giá trị của ý tưởng*. Chỉ ~1/3 ý tưởng ở
Microsoft cải thiện đúng chỉ số nó nhắm; ở miền đã tối ưu kỹ như Bing/Google chỉ 10–20%; Slack ~30% với
monetization. Nếu hệ này thấy "đổi cái gì cũng thắng" thì đó là dấu hiệu đo sai, không phải giỏi.

### 1.1 Pitfalls hệ NÀY dễ dính nhất khi "so trước/sau"

| # | Pitfall (tên sách) | Nó biểu hiện thế nào ở đây | Chống bằng gì |
|---|---|---|---|
| 1 | **Novelty effect** | RSA mới lạ mắt → CTR bật lên 1–2 tuần rồi tụt. Sách: MSN đổi link Outlook, click **+28%** — hoá ra người dùng *bối rối bấm nhiều lần*, không phải thích | **Vẽ treatment effect theo thời gian**, không nhìn trung bình kỳ. Xu hướng dốc xuống = cờ đỏ, phải chạy dài hơn |
| 2 | **Primacy effect** | Đổi LP → khách quen bản cũ, số xấu tạm thời; **và Smart Bidding phải học lại** (learning phase = primacy của máy) | Bỏ tuần đầu khỏi mọi kết luận (đã trùng luật learning-phase guard) |
| 3 | **"SRM tương đương"** khi Google tự chia traffic giữa 2 RSA | **KHÔNG có tỷ lệ thiết kế.** Ad rotation "optimize" phân bổ impression theo *dự đoán hiệu suất* → assignment **không ngẫu nhiên và phụ thuộc chính cái đang đo**. Sách gọi đúng lỗi này: *"triggering based on attributes impacted by the experiment"* và *"no factor should be allowed to influence variant assignment"* | ⛔ 2 RSA cùng ad group **chỉ dùng để Google CHỌN cái chạy, tuyệt đối không dùng để KẾT LUẬN cái nào tốt hơn**. Không có SRM check nào cứu được vì không tồn tại tỷ lệ kỳ vọng |
| 4 | **Interference / SUTVA violation** | 2 RSA (hoặc 2 campaign) **chung ngân sách và chung phiên đấu giá**. Sách nêu đích danh: *"budget on a given campaign is shared between Treatment and Control → delta is overestimated"*. Thêm: Smart Bidding **học từ dữ liệu của cả hai** (relevance-model-training leakage) | Muốn tách thật thì phải tách campaign + tách ngân sách; ở quy mô này thường không đáng → **khai báo là giới hạn, đừng giả vờ đã kiểm soát** |
| 5 | **Simpson's paradox** | Đã có luật trong `monitoring.md`. Sách bổ sung **cơ chế gốc**: nghịch lý sinh ra khi **tỷ lệ phân bổ đổi giữa các kỳ** (ramp-up). Ở hệ này tỷ lệ *luôn* đổi vì Google tự phân bổ lại mỗi ngày | Không gộp số qua các giai đoạn có cơ cấu phân bổ khác nhau |
| 6 | **Lack of power** | "p > 0,05" bị đọc thành "không có tác dụng". Sách: *"a non-significant difference means there is no difference"* là hiểu sai kinh điển | Chốt **practical significance** trước; kết quả không kết luận được thì gọi thẳng là **inconclusive** |
| 7 | **Peeking at p-values** | Nhìn số mỗi ngày rồi dừng khi thấy đẹp → sai lệch **5–10×** tỷ lệ dương tính giả (Optimizely đời đầu khuyến khích điều này, gây ra bài *"How Optimizely (Almost) Got Me Fired"*) | **Fixed-period**: chốt trước ngày kết thúc, chỉ đọc kết luận 1 lần |
| 8 | **Multiple hypothesis testing** | Battery alert của `monitoring.md` quét ~10 chỉ số × nhiều campaign × mỗi ngày. Với ngưỡng 0,05, **k=10 chỉ số độc lập → 40%** cơ hội có ít nhất 1 cái "bất thường" dù chẳng có gì | Phân tầng: metric bậc 1 dùng 0,05 · bậc 2 dùng 0,01 · bậc 3 dùng 0,001 (rule-of-thumb của sách). Giới hạn **≤5 key metrics** |
| 9 | **Seasonality / day-of-week** | Tết, tháng 7 âm, cuối tuần. Đây là **confound số 1 của Interrupted Time Series** — thiết kế duy nhất hệ này thực sự đang dùng | Tối thiểu **1 tuần trọn**; so cùng thứ trong tuần; đảo đi đảo lại nhiều lần (§3) |
| 10 | **Outliers** | 1 click CPC đắt bất thường, 1 bot, 1 ngày spend lệch. Sách: outlier **làm phồng variance mạnh hơn làm lệch mean** → t-statistic *tụt*, thí nghiệm mất khả năng kết luận | **Cap** giá trị ở ngưỡng hợp lý trước khi tính trung bình. Bing cap Revenue/User ở $10 → skewness 18→5, cỡ mẫu cần **giảm 10 lần** (114k → 10k) |
| 11 | **Survivorship bias / cherry-picking người thắng** | Chọn ra RSA/keyword "đang thắng" rồi coi mức thắng đó là thật. Sách (Lee & Shen): những nhánh được chọn để launch **luôn bị lệch lên**; cách chữa là **replication experiment** — Bing chỉ tính điểm cho ý tưởng sau khi chạy lại một lần độc lập | Kết quả bất ngờ → **chạy lại**. Đây là thứ rẻ nhất trong cả cuốn sách |
| 12 | **Ratio metric — analysis unit ≠ randomization unit** | CVR = conversion / click. Đơn vị phân tích là *click*, đơn vị "randomize" là *người*. Variance tính theo công thức thường bị **sai** → A/A test rớt | Ở n nhỏ thì đừng tính p-value cho CVR; nếu tính, phải dùng delta method/bootstrap |
| 13 | **Goodhart / Campbell / Lucas** | *"When a measure becomes a target, it ceases to be a good measure."* Đặt CPL làm mục tiêu → hạ cam kết form, CPL rẻ ngay, gánh nặng chuyển sang sale | §2 guardrail + §4 OEC |
| — | *"Regression to the mean"* | Sách **không** dùng thuật ngữ này; cơ chế tương đương nó mô tả là **selection bias khi chọn nhánh thắng** (#11) + Twyman's law (#0). Đừng trích sai nguồn | |

---

## 2. Guardrail metrics — hệ này nên có gì

Sách chia **hai loại**, và trộn hai loại là lỗi phổ biến:

**(a) Trust-related guardrail** — *"số này có đáng tin không"*. Nếu rớt thì **không được nhìn bất kỳ số nào khác**
(Microsoft ExP **giấu luôn scorecard** khi SRM rớt). Bản của hệ này:

| Guardrail tin cậy | Ngưỡng nghi ngờ | Vì sao |
|---|---|---|
| **Click (Ads) vs session có `gclid` (GA4)** | lệch >10% | Bản gần nhất của SRM mà hệ có thể có: mất gclid = mất một phần dân số một cách **không ngẫu nhiên** |
| **Ngày tracking gãy đã bị loại khỏi mẫu số chưa** | bất kỳ | Đã có luật ở `monitoring.md` §2.1 — sách xác nhận đây là data-quality metric hạng nhất |
| **Tỷ lệ event/session** (`form_start` / session…) | đổi đột ngột | Telemetry fidelity: web beacon là **lossy**, Treatment có thể đổi tỷ lệ mất |
| **LP uptime + Page Load Time** | 200/PLT p90 | Sách khuyến nghị **latency luôn là guardrail**: Bing 100ms ≈ **0,6% revenue**; Amazon 100ms ≈ **−1% sales** |
| **Tỷ lệ bot/invalid click** | tăng bất thường | Bing: >50% traffic US là bot; bộ lọc bot từng phân loại nhầm *khách tốt nhất* thành bot và đảo ngược kết luận |

**(b) Organizational guardrail** — *"thứ tổ chức KHÔNG chấp nhận đánh đổi"*. Sách: phải **nhạy hơn** goal metric.

| Guardrail kinh doanh | Bảo vệ khỏi điều gì |
|---|---|
| **Contact rate của lead** (gọi được / lead thô) — lấy tay từ sale hàng tuần | ⭐ Đúng câu hỏi "CVR tăng nhưng SĐT rác tăng?". Đây là guardrail quan trọng nhất của hệ, và nó **nằm ngoài GA4** → không tự động hoá được, phải làm tay |
| **Tỷ lệ lead sai địa bàn / sai ngành** | Negative list thủng, RSA lệch intent |
| **Impression Share brand** | Campaign generic mới ăn ngân sách của brand — nhánh chắc chắn nhất bị hy sinh âm thầm |
| **CPC brand** | Đối thủ vào đấu giá (đã có ở `monitoring.md` §4) |
| **Trần chi 30tr₫/tháng** | Đã có ở plan §4 — sách gọi loại này là guardrail *"cao đến mức không được phép đánh đổi"* (ví dụ an toàn hành khách trên máy bay) |

**Chống gameability (Sidebar: Gameability).** Sách đầy ví dụ đo sai sinh hành vi sai: thưởng theo đuôi chuột →
người ta **nuôi chuột**; đo "thời gian tới khi bác sĩ khám" → y tá **giữ bệnh nhân trong xe cứu thương**. Bản của
hệ: đo `generate_lead` trần trụi → cách tăng rẻ nhất là **hạ cam kết form**, và bệnh viện chuyển sang phòng sale.
Mẫu chữa của sách là **OEC email Amazon**: doanh thu từ email tăng đơn điệu theo số email gửi → spam. Họ **trừ
`unsubscribe_lifetime_loss`** vào OEC; chỉ gán *vài đô* cho mỗi unsubscribe mà **hơn một nửa chiến dịch lập tức âm**.

---

## 3. Quy tắc đọc số cho hệ KHÔNG có A/B — áp được gì, không kết luận được gì

### 3.1 Áp được ngay (sách dạy, hệ làm được)

1. **Fixed-period, không peeking.** Chốt trước: ngày bắt đầu, ngày đọc kết quả, chỉ số nào, ngưỡng nào là
   "đáng làm". Đọc 1 lần. Google/LinkedIn/Microsoft dùng đúng cách này thay vì sequential test.
2. **Chốt practical significance TRƯỚC.** Câu hỏi bắt buộc trong checklist thiết kế thí nghiệm của Google:
   *"How big of a change do you care about?"* Không có con số này thì mọi kết quả đều diễn giải được theo ý muốn.
3. **Tối thiểu 1 tuần trọn, bỏ tuần đầu** (day-of-week + novelty/primacy + learning phase).
4. **Vẽ theo lát thời gian, không đọc trung bình kỳ.** Trùng khớp 100% với luật "quét WoW điểm gãy" đã có —
   sách cho thêm *lý do thống kê*: phân tích chuẩn giả định treatment effect **không đổi theo thời gian**;
   đường dốc = giả định bị vi phạm, không phải "xu hướng đẹp".
5. **Interrupted Time Series có ĐẢO CHIỀU.** Quasi-experiment mạnh nhất hệ này với tới: đổi → đo → **đổi lại** →
   đo → đổi lần nữa. Ví dụ sách: giám sát trực thăng bật/tắt nhiều lần, mỗi lần bật trộm cắp giảm, mỗi lần tắt
   lại tăng. Lặp nhiều chu kỳ là cách duy nhất tách khỏi mùa vụ. Cảnh báo của sách: khách có khó chịu vì trải
   nghiệm nhấp nháy không?
6. **Difference-in-differences** khi có một nhánh *không đổi gì* chạy song song (ví dụ: đổi LP cho campaign
   generic, giữ nguyên campaign brand). Giả định bắt buộc: **common trend** — hai nhánh vốn đi song song.
   Phải **ghi giả định ra giấy**, vì đây chính là chỗ observational study hay chết.
7. **Triggering — chỉ tính người CÓ THỂ bị ảnh hưởng.** Đổi LP của 1 campaign → phân tích đúng campaign đó,
   không pha loãng bằng toàn tài khoản. Sách: ví dụ số học, lọc còn 10% người thực sự đi qua checkout làm cỡ
   mẫu cần giảm từ 121.600 xuống 64.000. **Kèm luật dilution:** cải thiện 3% trên 10% người **≠** 0,3% tổng —
   có thể là bất cứ đâu từ 0% đến 3%, tuỳ nhóm đó đóng góp bao nhiêu.
8. **Replication.** Kết quả bất ngờ → chạy lại. Fisher's meta-analysis cho phép gộp p-value của 2 lần chạy
   độc lập để lấy lại power — cách duy nhất trong sách hợp với hệ thiếu mẫu kinh niên.
9. **Complementary techniques (ch.10) làm bằng chứng chính, không phải phụ.** Human evaluation (rater) — bản
   của hệ là **sale chấm chất lượng từng lead**; UER/survey; external data. Sách: dùng **nhiều phương pháp để
   khoanh vùng đáp án** (triangulate) khi không có phương pháp nào đủ mạnh.
10. **Giảm variance thay vì tăng mẫu** (thứ hệ không có): dùng chỉ báo **nhị phân** thay giá trị tiền
    (Kohavi: dùng conversion rate thay purchase spend giảm cỡ mẫu cần **3,3 lần**); **cap** outlier; đo ở
    đơn vị hạt mịn hơn khi hợp lệ.

### 3.2 TUYỆT ĐỐI không kết luận được — nói thẳng

- ⛔ **"Đổi RSA làm CVR tăng X%".** Không có Control. Trong cùng khoảng đó đã đổi: mùa vụ, đối thủ trong đấu
  giá, Smart Bidding tự học lại, Google tự đổi phân bổ, cơ cấu search term. Đây là **observational causal
  study** — bậc 3, và sách vừa cho thấy loại này sai lệch tới **hai bậc độ lớn** ở đúng bài toán quảng cáo online.
- ⛔ **"RSA A tốt hơn RSA B vì A có CVR cao hơn".** Google phân bổ impression cho A *vì nó đoán A sẽ tốt hơn*.
  Đây là correlation do **common cause = thuật toán phân bổ**, đúng dạng "user thấy nhiều error thì churn ít hơn".
- ⛔ **Bất kỳ con số % nào ở n nhỏ.** Công thức cỡ mẫu của sách (power 80%, 95% CI): **n ≈ 16σ²/δ²**.
  Với CVR ~3%: σ² = 0,03·0,97 = 0,0291.
  - Muốn phát hiện **+20% tương đối** (3% → 3,6%): δ = 0,006 → n ≈ **12.900 click/nhánh**.
  - Muốn phát hiện **+50% tương đối** (3% → 4,5%): δ = 0,015 → n ≈ **2.100 click/nhánh**.
  Hệ có **vài trăm click/tháng cho toàn tài khoản**. Kết luận trung thực: ở quy mô này, **ngay cả một cải
  thiện 50% cũng cần nhiều tháng chỉ để một nhánh đủ mẫu** — và hệ không có nhánh. Đây là lý do thống kê
  đứng sau luật "chỉ đổi táo bạo" của `making-websites-win.md` và kết luận `monitoring.md` §3.1.
- ⛔ **Tác động dài hạn từ số ngắn hạn.** BĐS chu kỳ 3–12 tháng. Sách (ch.23): tác động dài hạn có thể
  **ngược dấu** ngắn hạn (tăng giá, tăng ad load, kết quả search kém → chỉ số ngắn hạn *đẹp lên*).
- ✅ **Cái được phép nói:** "Sau khi đổi X, chỉ số Y đi từ A đến B trong kỳ Z; **chưa loại trừ được** mùa vụ /
  đối thủ / phân bổ lại của Google; mức thay đổi **nằm trong / ngoài** biên chúng ta coi là đáng làm."
  Đây là câu mọi báo cáo của agent phải viết được, và là *duy nhất* dạng câu được phép.

---

## 4. OEC cho Beachtro — 3 phương án + đánh đổi

Yêu cầu của sách với một OEC: **đo được trong kỳ ngắn · quy được về variant · đủ nhạy · tin là dẫn tới mục
tiêu dài hạn · khó game · ≤5 key metric, lý tưởng là 1 số gộp có trọng số**. Ràng buộc thật: true north
(booking / HĐMB) **không đo được trong kỳ** → OEC bắt buộc là **surrogate**, và **hệ đã chốt không đo lead**
→ mọi thứ dính contact rate đều phải nhập tay.

| | **A. CPL-contactable** (lead gọi được / chi phí) | **B. `generate_lead` per click** (CVR) | **C. Weighted lead per click** ⭐ khuyến nghị |
|---|---|---|---|
| Định nghĩa | contactable lead / spend | `generate_lead` / click | `(generate_lead + w₁·(phone_click+zalo_click) − w₂·lead_không_liên_lạc_được) / click` |
| Gần tiền | ✅ nhất | ❌ bỏ qua CPC | ⚠️ vừa |
| Đo được bằng hệ hiện tại | ❌ cần contact rate từ sale (ngoài phạm vi hệ) | ✅ GA4 + Ads | ⚠️ cần w₂ nhập tay |
| Độ nhạy ở n nhỏ | ❌ **tệ nhất** — tiền là biến skew nặng, variance khổng lồ (đúng lý do Bing phải cap revenue) | ✅ tốt nhất — nhị phân, variance thấp | ✅ tốt |
| Chống game | ✅ | ❌ **hỏng** — hạ cam kết form là tăng ngay (Goodhart) | ✅ w₂ chính là `unsubscribe_lifetime_loss` của Amazon |
| Rủi ro | Không chạy được nếu sale không nhập số | Tối ưu thẳng vào lead rác | Cần user chốt w₁, w₂ |

**Chốt đề xuất:** dùng **C**, khởi đầu thô: `w₁ = 0,5` (click gọi/Zalo là ý định mạnh nhưng không phải lead),
`w₂` = ước lượng thô chi phí một lead rác (thời gian sale + hao uy tín). Theo bài học Amazon: **gán w₂ nhỏ vẫn
tốt hơn gấp bội gán 0**. Nếu tuần 4 user không cung cấp được w₂ → tạm dùng **B + 2 guardrail bắt buộc**
(contact rate, tỷ lệ lead sai địa bàn) và **ghi rõ OEC đang thiếu chân**.

**Không được dùng làm OEC:** số lead thô (không chuẩn hoá theo mẫu số → phụ thuộc lưu lượng) · CTR đơn thuần ·
`xem_bang_gia`/`xem_mat_bang`/`form_start` (đây là **driver metrics** — nhạy nhưng cục bộ và dễ game). Cảnh báo
kinh điển của sách: bug ranker của Bing làm kết quả **tệ đi** khiến queries/user **+10%** và revenue/user **+30%**.

**Metrics evolve.** Sách nhấn: OEC phải được sửa khi hiểu biết và business đổi. Mốc bắt buộc xem lại: khi CĐT
công bố bảng giá (plan §7 — LP đổi bản chất) và khi đủ 30 conv/tháng cho một campaign đơn lẻ.

---

## 5. Bảng ĐỀ XUẤT (chỉ đề xuất — không sửa file nào)

### 5a. Cho `playbook/monitoring.md`

| # | Đề xuất | Vì sao (theo sách) | Ưu tiên |
|---|---|---|---|
| 1 | **Thêm §0 "Twyman's law"**: mọi số đẹp/xấu bất thường → **kiểm tra đo lường TRƯỚC khi kể chuyện**. Alert 🔴 mới: *"chỉ số tốt đột biến >2× baseline"* — đối xứng với alert spend đột biến đang có | Bing chạy alert "revenue-too-high" vì cực trị hầu như luôn là bug | 🔴 |
| 2 | **Tách bảng chỉ số thành 2 tầng: trust-related vs organizational guardrail**, và luật cứng: *trust guardrail rớt → KHÔNG đọc chỉ số nào khác, chỉ debug* | Microsoft ExP giấu scorecard khi SRM rớt | 🔴 |
| 3 | **Guardrail "click Ads vs session có gclid"** vào nhịp Daily Close, ngưỡng lệch 10% | Bản gần nhất của SRM mà hệ có được | 🔴 |
| 4 | **Guardrail contact rate lead** vào nhịp tuần (nhập tay từ sale) — trả lời "CVR tăng nhưng SĐT rác tăng?" | Gameability + OEC Amazon | 🔴 |
| 5 | **Phân tầng ngưỡng p/alert** cho battery ~10 chỉ số: bậc 1 = 0,05 · bậc 2 = 0,01 · bậc 3 = 0,001 | k=10 → 40% cơ hội có 1 "bất thường" ngẫu nhiên | 🟡 |
| 6 | **Luật fixed-period**: mọi so sánh trước/sau phải khai trước ngày đọc + ngưỡng đáng làm, đọc 1 lần | Peeking sai lệch 5–10× | 🔴 |
| 7 | **Luật cap outlier** trước khi tính mọi trung bình (CPC, CPL, thời gian trên trang) | Outlier phồng variance hơn phồng mean → mất khả năng kết luận | 🟡 |
| 8 | **Luật replication**: kết quả bất ngờ → chạy lại rồi mới ghi vào institutional memory | Lee & Shen: nhánh được chọn luôn lệch lên | 🟡 |
| 9 | **Nhật ký thí nghiệm** (`ops/experiments.jsonl`): giả thuyết · ngày bắt đầu/kết thúc · ngưỡng chốt trước · kết quả · quyết định · **và cả cái thất bại** | Ch.8 Institutional Memory — 2/3 ý tưởng không thắng, giá trị nằm ở chỗ không lặp lại | 🟡 |
| 10 | **Bổ sung vào luật Simpson đang có**: nêu cơ chế gốc = **tỷ lệ phân bổ đổi giữa các kỳ**, mà ở đây Google đổi mỗi ngày | Ví dụ ramp-up 1%→50% của sách | 🟢 |

### 5b. Cho `projects/beachtro-tower/plan-chay-ads.md` §5

| # | Đề xuất | Vì sao | Ưu tiên |
|---|---|---|---|
| 1 | **Thêm bước 0: chốt OEC (§4 trên) trước khi chốt CPL mục tiêu** | Không có OEC thì "CPL thực > CPL mục tiêu" chỉ là một chỉ số cô đơn, dễ game | 🔴 |
| 2 | **Ghi rõ giới hạn thống kê ngay trong §5**: ở vài trăm click/tháng, `CPL thực = CPC / CVR_lp` là **ước lượng điểm không có khoảng tin cậy dùng được**; công thức 16σ²/δ² cho ~2.100 click/nhánh chỉ để bắt thay đổi +50% | Chống việc tuần 4 lấy một con số nhiễu làm luật cho tháng 2 | 🔴 |
| 3 | **Bổ sung guardrail contact rate vào công thức tuần 4**: CPL-contactable, không phải CPL thô | Hạ cam kết form làm CPL thô rẻ đi mà không tạo giá trị | 🔴 |
| 4 | **Mở rộng cảnh báo Simpson hiện có ở §5** thành: khi CĐT công bố giá → **KHÔNG so trước/sau bằng bất cứ cách nào**, mà **bắt đầu kỳ đo mới**; nếu muốn đọc tác động của LP mới, dùng diff-in-diff với một campaign không đổi | External validity: đổi LP + đổi thị trường + đổi mùa cùng lúc = không tách được | 🔴 |
| 5 | **Thêm luật cho việc thử RSA thứ 2**: ghi thẳng vào plan rằng đây **không phải A/B test**, chỉ là cơ chế để Google chọn — cấm kết luận "headline X thắng" | Assignment do thuật toán quyết + chung ngân sách + chung mô hình học | 🔴 |
| 6 | **Nếu muốn thật sự đo một thay đổi LP**: dùng ITS có đảo chiều (A→B→A→B, mỗi pha ≥1 tuần trọn) thay vì đổi một lần rồi so | Cách duy nhất tách khỏi mùa vụ khi không có Control | 🟡 |

---

## Tóm tắt — 10 dòng

1. **Twyman's law**: số đẹp/xấu bất thường → nghi lỗi đo trước. Thêm alert "tốt đột biến", đối xứng với alert spend.
2. Hệ này đứng ở **bậc 3–4 của hierarchy of evidence** (quasi-experiment / logs), không phải A/B. Sách cho thấy loại này từng sai **871% vs 5,4%** ở đúng bài toán quảng cáo online.
3. **2 RSA trong cùng ad group KHÔNG phải A/B test** — Google phân bổ theo dự đoán hiệu suất, chung ngân sách, chung mô hình học. Chỉ dùng để chọn, cấm dùng để kết luận.
4. Pitfall dễ dính nhất: novelty effect, primacy/learning phase, seasonality (confound số 1 của ITS), peeking, multiple testing trên battery alert, outlier phồng variance.
5. **Guardrail phải tách 2 tầng**: trust-related (gclid mismatch, PLT, bot, ngày tracking gãy) — rớt thì cấm đọc số khác; và organizational (contact rate, IS brand, trần chi).
6. Guardrail quan trọng nhất trả lời "CVR tăng nhưng SĐT rác tăng?" là **contact rate**, và nó **nằm ngoài GA4** → nhập tay hàng tuần từ sale.
7. **Cỡ mẫu là rào cứng**: n ≈ 16σ²/δ² → ~12.900 click/nhánh để bắt +20% CVR, ~2.100 để bắt +50%. Hệ có vài trăm click/tháng. Trung thực: phần lớn so sánh sẽ **inconclusive**, và nói thế mới là đúng.
8. Áp được ngay: fixed-period không peeking · chốt practical significance trước · bỏ tuần đầu · vẽ theo lát thời gian · **ITS có đảo chiều** · diff-in-diff có khai giả định · triggering + luật dilution · replication.
9. **OEC đề xuất: weighted lead per click** — cộng phone/zalo click, **trừ lead không liên lạc được** (đúng mẫu OEC email của Amazon, nơi gán vài đô cho unsubscribe làm hơn nửa chiến dịch âm).
10. Đề xuất chính cho repo: §0 Twyman + 2 tầng guardrail + luật fixed-period + nhật ký thí nghiệm cho `monitoring.md`; và cho plan §5: chốt OEC trước CPL, ghi rõ giới hạn thống kê, cấm so trước/sau khi CĐT công bố giá.
