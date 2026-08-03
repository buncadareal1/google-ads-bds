# Research: Google Ads cho BĐS Việt Nam 2025-2026 (2026-07-28)

> **Cảnh báo nguồn:** Không có benchmark chính thức riêng cho BĐS VN. Số VN đến từ blog/bảng giá agency (tin cậy thấp–trung bình). Số đáng tin nhất: WordStream 2026 (13.474 campaign search Mỹ) + docs Google. Dùng số VN làm mốc thô, không phải KPI target.

## 1. Cấu trúc campaign

| Loại | Vai trò | Rủi ro |
|---|---|---|
| Search | Xương sống, 60-80% ngân sách tài khoản nhỏ | CPC cao, click tặc |
| PMax | CHỈ khi ≥30 conversion qualified/tháng VÀ đã import lead CRM | Spam lead + cannibalize brand |
| Demand Gen | Dự án mới chưa ai search tên. Min **kỹ thuật** thấp (~$5/ngày) nhưng **best practice Google là $100+/ngày cho maximize strategies, hoặc ≥10× tCPA/ngày** ([Demand Gen best practices](https://support.google.com/google-ads/answer/14693848?hl=en)) | Không ra lead ngay; dưới ngưỡng ngân sách thì không đủ mật độ để học |
| YouTube | Awareness dự án lớn | Đo lường khó |
| Display | **CHỈ remarketing, không bao giờ cold.** ⚠️ Từ 6/2026 Display đang bị Google migrate vào **Demand Gen** — không dựa vào việc tạo Display campaign mới (xem `playbook/customer-journey-plan.md` §3, gate G2) | Đốt tiền vào app game |

**PMax pitfalls:** tối ưu theo conversion signal đưa vào — nếu signal = form submit thì tự tìm thêm lead rác từ inventory rẻ (app game, parked domain). Bắt buộc bật: campaign-level negative keywords (giới hạn 10.000 từ 3/2025), brand exclusions, account-level placement exclusions (loại App categories/Games).

**AI Max for Search**: lớp opt-in trong Search campaign (không phải campaign type mới), an toàn hơn PMax vì giữ search terms report + negative cấp campaign. Bật SAU khi Search ổn định; tắt final URL expansion nếu site có trang không phải LP.

> ✅ **Claim "AI Max giữ search terms report" — ĐÃ XÁC NHẬN (vòng 2, 2026-07-28).** [About reporting in AI Max](https://support.google.com/google-ads/answer/16470459?hl=en): "The search terms report shows you how your ads performed when triggered by **actual searches**… You can use this report to understand AI Max automation traffic and its value". [How AI Max works](https://support.google.com/google-ads/answer/15910187?hl=en) xác nhận thêm: AI Max **thêm** vào chính báo cáo đó một match type mới `AI Max` + **cột `source`** cho biết match đến từ *broad match expansion* hay *keywordless*, cộng một view mới ghép search term ↔ headline ↔ URL. **Không có** "search categories report" thay thế như PMax. Mất granularity duy nhất là ngưỡng privacy ẩn term ít volume — **áp cho mọi Search campaign**, không phải do AI Max. → Lý do "AI Max an toàn hơn PMax" đứng vững.

**Cấu trúc theo ngân sách:**
- **<20tr/tháng**: 1 Search campaign duy nhất (ad group: tên dự án / loại hình+khu vực / chủ đầu tư), phrase+exact, account-level negative list, Display remarketing 10-15% khi list ≥100 user. KHÔNG chia 5-10 campaign nhỏ.
- **20-80tr**: tách Search Brand (tCPA thấp) / Search Generic + Demand Gen hoặc YouTube remarketing + Display remarketing.
- **>80tr**: thêm AI Max test, PMax (chỉ khi CRM import chạy + brand exclusion), portfolio bidding gộp campaign nhỏ.

## 2. Benchmark

**WordStream 2026 — Real Estate (Mỹ):** CTR 7,61% / CPC $3,22 / CVR 3,70% / CPL $102,51. Click BĐS rẻ, lead BĐS đắt (CVR chỉ ~45% mức trung bình ngành). CPC tăng mạnh nhất YoY +27%.

**VN (nguồn agency, tin cậy thấp):** CPC BĐS 20-100k₫ (đỉnh 200k), CPL công bố 200-300k (nghi vấn: ngụ ý CVR 10-25%, không thực tế — "lead" của agency = mọi form submit kể cả rác). Ngân sách tối thiểu ~15tr/tháng (SEONGON: 495k/ngày).

**Mô hình lập kế hoạch nên dùng (căn hộ/đất nền tầm trung):**

| | Thận trọng | Trung bình | Tốt |
|---|---|---|---|
| CPC | 40k | 25k | 15k |
| CVR LP | 2% | 4% | 7% |
| CPL raw | 2.000k | 625k | 214k |
| Tỷ lệ qualify | 25% | 40% | 60% |
| **CPL qualified** | **8.000k** | **1.560k** | **357k** |

Phân khúc: căn hộ (volume cao, cạnh tranh nặng), đất nền (CPC thấp, lead rác nhiều nhất), biệt thự/hạng sang (volume rất thấp — KHÔNG dùng tCPA).

**Ngân sách ra data:** cần ≥10-15 click/ngày → 250-600k/ngày = 7,5-18tr/tháng tối thiểu. tCPA cần ≥30 conversion/30 ngày → ~19-30tr/tháng. **Dưới 15tr: Maximize Clicks/Manual CPC, đừng tCPA.**

## 3. Keywords

**Intent tiers (giảm dần):** (1) tên dự án + hành động ("X bảng giá") — CVR tốt nhất; (2) tên dự án trần; (3) chủ đầu tư; (4) loại hình + khu vực — volume lớn nhất, cần lọc mạnh; (5) loại hình + thuộc tính ("căn hộ 2PN dưới 3 tỷ") — long-tail CVR tốt; (6) so sánh/đánh giá → remarketing, không ép form; (7) nghiệp vụ/tài chính ("vay mua nhà") → KHÔNG chạy Search, chỉ content; (8) tên đối thủ → được bid keyword, KHÔNG để tên trong ad text.

**Negative bắt buộc (account-level list):** cho thuê/thuê/phòng trọ (rò rỉ lớn nhất); tuyển dụng/việc làm/lương/ctv; là gì/cách/mẫu/pdf/luận văn; lừa đảo/phốt/tố cáo/tranh chấp; portal (batdongsan.com.vn, chotot...); sai ngành (game, du lịch, homestay); thanh lý/phát mãi/ký gửi (nếu chỉ bán sơ cấp); tỉnh không bán. **Biến thể không dấu là BẮT BUỘC** (cho thue, tuyen dung) — xem hộp dưới. Riêng "review": xem search terms trước, đừng phủ định mù.

> ⚠️ **Negative keyword KHÔNG khớp close variant** (khác hoàn toàn positive keyword). Nguồn: [About negative keywords](https://support.google.com/google-ads/answer/2453972?hl=en). Nghĩa là:
> - Với **positive** keyword: Google tự khớp bản không dấu ↔ có dấu → không cần tạo dòng riêng (`keywords/adgroup-map.md` §Match type, `playbook/campaign-setup.md` §2.4.5 — **đúng**).
> - Với **negative** keyword: không có close variant → `cho thuê` **không** chặn `cho thue`. Biến thể không dấu trong negative list là bắt buộc, không phải tuỳ chọn.
> Hai câu trên đọc ngược nhau nếu thiếu ghi chú này. Đừng áp luật của positive sang negative.

**Match type ("barbell" 2025-2026):** lõi Exact/Phrase bottom-funnel + Broad chỉ khi ≥30-50 conversion/30 ngày.
- <20tr/tháng: Phrase + Exact ONLY
- 20-60tr chưa import CRM: chủ yếu Phrase+Exact, test 1 ad group broad cap 15% *(cap 15% là **luật nội bộ**, Google không publish ngưỡng này)*
- >60tr + offline import ổn: barbell đầy đủ
- Tên dự án: LUÔN Exact

> 🎓 **Google chính thức khuyên gì — và vì sao hệ chưa làm** (đọc để không hiểu "broad = xấu vĩnh viễn"). Đây là **gate**, không phải lệnh cấm.
>
> Google dạy ([The ABCs of Account Structure](https://support.google.com/google-ads/answer/14752782?hl=en), [Reaching the right customers on Search](https://support.google.com/google-ads/answer/6167110?hl=en)): cấu trúc **consolidated, tightly-themed**; bỏ SKAG; gộp mọi match type vào một ad group và dùng **broad làm match type chính** ("Broad match is the only match type that uses all of the signals available"); Google nêu **62% advertiser dùng Smart Bidding lấy broad làm match type chính**. Phrase/exact chỉ hợp khi mục tiêu là metric khác (ví dụ Target impression share).
>
> Nhưng chính Google đặt điều kiện tiên quyết ([Your guide to broad match](https://support.google.com/google-ads/answer/12159290?hl=en)): "**It's critical to use Smart Bidding with broad match**" — vì mỗi query khác nhau, bid phải phản ánh signal tại thời điểm đấu giá. Cùng logic: AI Max search term matching **không hoạt động với Manual CPC**.
>
> Hệ ngày 1 chạy **Max Clicks + bid cap**, 0 conversion → **chưa thỏa điều kiện của chính Google**. Thêm nữa, conversion khai ban đầu là form raw (chất lượng thấp) → cho broad học theo tín hiệu rác là đốt tiền có phương pháp. Vì vậy Phrase+Exact ở bậc 0-1 **không phải hệ sai**, mà là "chưa tới bậc".
>
> Lộ trình 6 bậc mở khoá (bậc 2 mới bật broad): `research/google-official-curriculum.md` §C2.6, đã map sang gate G0-G5 ở `playbook/customer-journey-plan.md` §3.2.

> 📉 **Search terms report LUÔN ẩn term ít volume** (privacy threshold — [About search terms report](https://support.google.com/google-ads/answer/2472708?hl=en)). Ba hệ quả phải biết trước:
> (a) tổng click cộng theo search term **< tổng click campaign** — không phải bug, đừng đi tìm lỗi;
> (b) negative list **không bao giờ phủ hết** — luôn còn rò rỉ dư, đừng lấy "0 term rác" làm mục tiêu;
> (c) GAQL `search_term_view` sẽ không cộng bằng `campaign` — quy tắc này áp cho MCP `google-ads` và mọi báo cáo tự động (`keywords/UPDATE.md`, `playbook/monitoring.md`).

**Audience trên Search campaign — dùng ở chế độ `Observation`:** gắn cả 5 audience GA4 (`tracking/ga4-setup.md` §3) vào Search campaign ở chế độ **Observation** (quan sát), KHÔNG phải Targeting. Không đổi phân phối, không đổi bid, chỉ để đọc chênh CVR/CPL theo audience → dữ liệu cho quyết định bid adjustment sau này và cho gate G2. Miễn phí, rủi ro bằng 0, hiện chưa dùng ở đâu.

## 4. Bidding

Lộ trình: Tuần 1-3 Manual CPC/Max Clicks (bid cap) thu data + negative → Tuần 4-8 vẫn Max Clicks, đo CVR thật, bắt đầu import lead qualify → đạt 30 conv/30 ngày: Maximize Conversions 2 tuần → tCPA = CPA lịch sử +10-20% → có giá trị lead phân tầng: value-based bidding (cần ≥15 conv/30 ngày).

**Learning phase:** 1-2 tuần Search, tới 6 tuần PMax (nguồn Google: [PMax lead gen best practices](https://support.google.com/google-ads/answer/13775965?hl=en) — "at least 1-2 weeks (or up to 6 weeks for more complex setups or low conversion volume)"). Reset khi đổi bid strategy/target/conversion action/ngân sách lớn. Đổi ngân sách ±20%/lần cách ≥3-4 ngày; tCPA ±15%/lần; chờ 4 tuần mới phán xét. Max Clicks không phải chiến lược vĩnh viễn.

> 🏷️ **Luật NỘI BỘ, không phải citation Google** (Google không publish 4 con số này — đừng ghi nguồn Google cho chúng): `tCPA ±15%/lần` · `budget ±20%/lần cách ≥3-4 ngày` · `chờ 4 tuần mới phán xét` · `broad cap 15% ngân sách campaign` (§3). Giữ nguyên vì thận trọng hợp lý, nhưng phải biết chúng là quy ước của hệ. Trang [Finding success with Smart Bidding](https://support.google.com/google-ads/answer/6167140?hl=en) **không** nêu ngưỡng conversion tối thiểu, không nêu độ dài learning period, không nêu mức chỉnh target — Google chỉ khuyên dùng **experiments** + bid strategy report.

**Portfolio bidding:** gộp nhiều campaign nhỏ cùng CPA mục tiêu (sàn chạy 4-5 dự án, mỗi cái 10-15 lead/tháng). Không gộp brand với generic.

**Mùa vụ VN:** Tết (T1-2): giảm 40-60% budget 2 tuần, KHÔNG tắt hẳn (mất learning). T3-6 cao điểm mở bán đợt 1. Tháng 7 âm (~T8-9): sụt phân khúc để ở → chuyển remarketing/nurture. T10-12: cao điểm cuối năm, CPC đỉnh. Thị trường 2026: cung tăng (128k sản phẩm mới 2025, giá +24%) → dự phòng CPC +20-30% YoY.

**Hai công cụ mùa vụ KHÁC NHAU — đừng lẫn** ([Seasonality adjustments](https://support.google.com/google-ads/answer/10369906?hl=en) · [Seasonal budget adjustments](https://support.google.com/google-ads/answer/12922263?hl=en)):

| | Seasonality adjustment | Seasonal **budget** adjustment |
|---|---|---|
| Điều chỉnh gì | **Conversion rate** dự kiến (nói cho Smart Bidding) | **Average daily budget** |
| Thời lượng | Event **1-7 ngày** (Google: "may not work as well… more than 14 days") | **3-14 ngày**, tự trả về mức cũ |
| Điều kiện | Search/Shopping/Display chỉ với **tCPA/tROAS** → **KHÔNG dùng được ở bậc Max Clicks** | Chỉ **Search/Shopping**; **KHÔNG** dùng được nếu campaign trong **ngân sách dùng chung**, campaign draft, dayparting, flighted; 2 lần liên tiếp cách **≥7 ngày** |
| Hướng | Tăng/giảm CVR dự kiến | **Chỉ TĂNG** budget |
| Dùng cho hệ | Đợt mở bán ngắn 1-7 ngày, **sau khi** đã lên tCPA (§4 lộ trình) | Đợt mở bán 3-14 ngày (T3-6, T10-12): lên lịch trước, tự trả về — thay việc sửa tay rồi quên sửa lại |

> ❌ **Tết và tháng 7 âm: KHÔNG dùng seasonality adjustment.** Google nói rõ không dùng cho seasonality **định kỳ** ("Smart Bidding already manages these") và không dùng cho giai đoạn >14 ngày. Tết là định kỳ + hệ dự kiến giảm 40-60% trong 2 tuần → **xử bằng thao tác NGÂN SÁCH bằng tay/script**, và seasonal budget adjustment cũng không dùng được vì nó chỉ tăng, không giảm. Sau event, seasonality adjustment tự về trạng thái cũ — **không cần** đặt adjustment âm bù lại.
> Ràng buộc "không dùng được với ngân sách dùng chung" củng cố quyết định `playbook/campaign-setup.md` §1.5.10 (không dùng shared budget ngày 1).

## 5. Lead quality (quyết định thắng thua)

**Enhanced Conversions for Leads (ECL) = đòn bẩy #1.** LP gửi email/SĐT hash kèm form submit; CRM qualify xong upload lại conversion "Qualified" → Google khớp về keyword/campaign.
**⚠️ QUAN TRỌNG (đã hiệu lực):** từ **15/6/2026** offline conversion import + ECL upload **bắt buộc qua Data Manager API**, bị chặn trên Google Ads API. Mọi pipeline upload phải viết cho Data Manager API ngay từ đầu.

**Thang conversion actions:**

| Action | Giá trị | Loại |
|---|---|---|
| Form submit raw | **1** | Secondary (quan sát) |
| Click Zalo/hotline | 1 | Secondary |
| Lead liên hệ được | 10 | **Primary ← bid theo cái này** |
| Lead qualified | 50 | Primary |
| Đặt cọc/ký HĐ | 500 | Primary nếu đủ volume |

> **Không bao giờ đặt giá trị 0.** Google: "It's generally **not recommended** to use conversions with 0 values with value based bidding" ([Value-based Bidding Best Practices](https://support.google.com/google-ads/answer/14792795?hl=en)) — conversion không có giá trị thì **bỏ khỏi dataset**, đừng gán 0. Thang 1/10/50/500 là **proxy value** và Google cho phép: "utilize proxy values that align with your business priorities" → không cần ₫ thật để bắt đầu value-based bidding (trả lời câu hỏi treo ở `PLAN.md` §6.7). Điều kiện bật VBB: **≥15 conversion/tháng cấp TÀI KHOẢN** + đo được "2 or more unique, non-zero values".

**Conversion Value Rules — chỉnh giá trị mà KHÔNG sửa tag** ([About conversion value rules](https://support.google.com/google-ads/answer/10520545?hl=en)): điều chỉnh giá trị conversion theo **geo / device / audience** ngay trong Google Ads. Ứng dụng BĐS: lead từ đúng quận dự án > lead ngoại tỉnh; lead từ audience `xem_bang_gia_30d` > lead lạ. **Rẻ hơn nhiều** so với dựng thêm conversion action (không phải sửa GTM, không phải sửa pipeline ECL, không thêm nguồn đếm). Chỉ có nghĩa khi đã ở bậc value-based bidding (bậc 3 của lộ trình §C2.6).

**Lọc spam lead:** 2 dropdown qualifying bắt buộc trên form (Ngân sách: <2/2-4/4-7/>7 tỷ; Mục đích: ở/đầu tư/cho thuê) — giảm ~15-25% volume, tăng mạnh contact rate. reCAPTCHA v3 + honeypot + validate đầu số VN. OTP chỉ bật khi CPL qualified quá cao (giảm CVR 20-40%). Tham chiếu: chỉ ~27% lead từ ad form là qualified (MarketingSherpa).

**KPI chính: contact rate** (gọi được/tổng lead) — mục tiêu >50%, dưới 40% = có vấn đề nghiêm trọng. Báo cáo tuần đặt contact rate TRƯỚC CPL.

**Click tặc VN:** có thật, đặc biệt khi nhiều sàn đấu cùng dự án. Xử lý theo thứ tự: (1) xem cột Invalid clicks — Google tự lọc+hoàn tiền, <10% là bình thường; (2) IP exclusion (max 500, chỉ chặn click văn phòng cố định); (3) ad schedule tắt giờ đêm rác; (4) tool ClickCease/Spider AF ~$50-100/tháng CHỈ khi ngân sách >50tr. Ngân sách <30tr: sửa LP có ROI cao hơn chống click tặc.

## 6. Landing page

Benchmark: Unbounce median real estate 7,4% (LP tối ưu chủ đích) vs WordStream 3,70% (thực tế từ ads). **Đích BĐS VN: 3-6%, dưới 2% = LP hỏng.** Gửi về homepage thay LP riêng = mất 50-70% conversion.

**Bậc 1 bắt buộc:** bảng giá (lure #1) · mặt bằng từng loại căn · tiến độ + ảnh thật (chống "dự án ma") · khoảng giá hiện rõ ("từ 3,2 tỷ" — tự lọc tài chính) · **Zalo nổi cố định + click-to-call** (track làm secondary conversion) · tải <2,5s trên 4G.
**Bậc 2:** pháp lý (sổ, CĐT, ngân hàng bảo lãnh) · chính sách thanh toán/ân hạn gốc/lãi 0% · bản đồ hạ tầng kết nối · social proof · deadline thật.
**Bậc 3 (test):** exit popup — vô dụng trên mobile (75-85% traffic VN) → ưu tiên sticky bar; chatbot/Zalo OA; video flycam.

**Form chuẩn:** Họ tên + SĐT (validate đầu số) + 2 dropdown (ngân sách, mục đích) bắt buộc; email TÙY CHỌN nhưng khuyến khích ("nhận bảng giá PDF") — ECL match tốt nhất bằng email.

**Kỹ thuật bắt buộc:** capture gclid/gbraid/wbraid/gad_source/gad_campaignid → CRM (dùng skill `ad-click-attribution` có sẵn).

## 7. Chính sách

- **Housing personalized ads policy: KHÔNG áp dụng VN** (chỉ US+Canada, theo geo mà ad nhắm tới). Nhắm Việt kiều US/CA → tách campaign riêng, bỏ age/gender/parental/ZIP. Ba chi tiết thực thi khi thật sự chạy HEC: **radius targeting tối thiểu 1 km**; **predefined Google audiences vẫn dùng được** (audience tự dựng bị hạn chế rộng hơn); Canada dùng được **3 ký tự đầu postal code** (FSA).
- **Trademark:** bid tên dự án đối thủ = được phép; tên trong ad text = hạn chế (reseller hợp pháp được nhắc tên nếu không mạo nhận CĐT). Từ 2/2025 cơ chế = complaint-driven.
- 🚨 **Mạo nhận brand khác = ĐÌNH CHỈ TÀI KHOẢN NGAY, KHÔNG CẢNH BÁO.** Nó thuộc *unacceptable business practices* trong [Misrepresentation policy](https://support.google.com/adspolicy/answer/6020955?hl=en) — nặng hơn "disapproved ad" một bậc. **Ràng buộc cứng cho sàn phân phối:** headline kiểu `{Tên dự án} - Giá Gốc CĐT` (`playbook/campaign-setup.md` §3.1 #4) chỉ an toàn khi **LP nói rõ mình là đơn vị phân phối, KHÔNG phải chủ đầu tư**. Không có dòng đó trên LP → không được dùng headline đó. Tên chính thức của yêu cầu footer pháp nhân: [Business information requirements](https://support.google.com/adspolicy/answer/12499303).
- **Minh bạch chi phí** (một nhánh của misrepresentation): cấm tạo "false or misleading impression of the cost". Áp vào BĐS: mọi `Giá Từ` / `Trả Trước Từ` / `Vay X%` phải là **căn thật đang bán, có bằng chứng** (bảng giá đợt hiện tại), và **không bỏ qua phí bắt buộc**. Số "từ" của một căn đã bán hết = vi phạm, không phải marketing.
- **Disapproved thường gặp:** destination not working; "cam kết sinh lời X%" (unreliable claims — dùng "tiềm năng/dự kiến"); thiếu pháp nhân/MST/địa chỉ ở footer; LP toàn ảnh ít text; clickbait ALL-CAPS; trademark.
- **Làm advertiser verification sớm.** *(Đính chính lý do — 2026-07-28: không có nguồn Google nào nói BĐS VN bị nhắm riêng. Vertical Google nêu tên là healthcare, car rental, finance.)* Lý do đúng: Google nói "**all advertisers will eventually be required**" — và khi có yêu cầu thì **30 ngày không nộp = tài khoản bị TẠM NGƯNG**. Nộp trước là rẻ nhất; nộp sau khi bị treo là mất doanh thu trong lúc chờ 3-5 ngày duyệt.
- Lead form assets: ~~đã bỏ yêu cầu $50k spend~~ **ĐÍNH CHÍNH (QA 2026-07-28, đối chiếu doc Google):** ngưỡng $50k lifetime VẪN CÒN trong docs; cái mới là đường thay thế $1.000/account + verification. Dù sao chất lượng vẫn thấp hơn LP có qualifying question; cần tự kiểm tra khả dụng VN. **Policy nguyên văn (vòng 3, 2026-07-28):** "Only first-party advertisers or third-party agencies with a well-established, direct relationship with the products… Affiliate networks or lead generation businesses will not be allowed in our sole discretion" — sàn phân phối F1 có hợp đồng trực tiếp với CĐT = đủ điều kiện "third-party agency", nhưng là quyền quyết định đơn phương của Google → thêm lý do ưu tiên LP riêng thay vì lead form asset.

## 7b. Chống chỉ định — những thứ TRÔNG như KPI mà không phải

| Thứ | Sự thật (nguyên văn Google) | Hệ quả |
|---|---|---|
| **Optimization score** | Tính từ settings + statistics + recommendation impact. **Dismiss một recommendation cũng LÀM TĂNG score.** "Optimization score differs from Quality Score and isn't used by it." ([About optimization score](https://support.google.com/google-ads/answer/9061546)) | Score là "% recommendation đã xử lý", **không** phải thước đo chất lượng tài khoản. **Đừng theo đuổi, đừng báo cáo nó**, đừng để agency ngoài lấy nó làm bằng chứng hiệu quả. Bấm apply hàng loạt để nâng score là cách nhanh nhất phá negative list. |
| **Ad Strength** | "Ad Strength is a feedback tool for asset diversity and combination testing. **It isn't used to calculate Ad Rank, Quality Score, or auction wins.**" · "Ad Strength doesn't determine whether your ad is eligible to serve." ([About Ad Strength for RSA](https://support.google.com/google-ads/answer/9921843?hl=en)) | Là **checklist lúc tạo ad** ("đã đủ asset chưa"), **không** phải KPI hiệu suất. Con số "+15% conversion khi Poor→Excellent" là **tương quan tổng hợp** của Google trên toàn bộ advertiser, không phải nhân quả cho 1 tài khoản. Đo hiệu quả ad bằng **CTR + CVR + contact rate**. |
| **Store visits / store sales conversion** | Cần Google Business Profile đã verify + đủ volume; và **không tương thích search terms report** | **Không bật.** Mất search terms report = mất công cụ vận hành số 1 của hệ (vòng negative tuần). Củng cố quyết định §3.4 `playbook/campaign-setup.md` (chưa có GBP → bỏ qua). |
| **Quality Score** *(vòng 3, 2026-07-28)* | "Quality Score is **not a key performance indicator** and should **not be optimized or aggregated** with the rest of your data." · "Quality Score is **not an input in the ad auction**. It's a diagnostic tool…" ([About Quality Score](https://support.google.com/google-ads/answer/6167118?hl=en)) | 🚨 Hai hệ quả cứng: **(1)** cấm mọi báo cáo dạng "QS trung bình tài khoản" — chính Google nói đừng aggregate. **(2)** Mọi công thức kiểu `CPC = AdRank_dưới / QS` là **SAI** (QS không vào auction). Ad Rank là "a **set of values**" gồm bid, chất lượng ad+LP, Ad Rank thresholds, độ cạnh tranh phiên đấu, ngữ cảnh tìm kiếm, tác động dự kiến của asset — **không** phải phép nhân có QS ([About Ad Rank](https://support.google.com/google-ads/answer/1752122?hl=en)). QS dùng đúng cách = đọc **3 cột thành phần** (Exp. CTR / Ad Relevance / Landing Page Exp.) của từng keyword để biết *sửa cái gì*, không phải để chấm điểm. Ô "—" ở cột QS **không phải QS 6**, nó nghĩa là "chưa đủ search khớp exact để tính". Cửa sổ so sánh là **90 ngày**, và cột `Quality Score (hist.)` **vẫn tồn tại** trong UI. Đối chiếu đầy đủ với skill: `research/google-official-curriculum.md` §F2. |

## 8. Checklist vận hành

**Ngày (10'):** pacing · anomaly (spend đột biến, conv=0/24h, disapproved) · LP uptime · lead vào CRM chưa.
**Tuần:** T2 search terms report (thêm negative, nâng term có conv lên Exact) + invalid clicks + placement report · T3 **lead quality: contact rate (>50%), đối chiếu Ads vs CRM, đọc 10 lead gần nhất, upload ECL** · T4 CPC/CVR/CPL theo intent tier, chỉnh tCPA ±15% max · T5 Auction Insights + Impression Share lost (budget vs rank) + LP behavior · T6 báo cáo: Spend/Click/CPC/Lead raw/**contactable**/**qualified**/CPL qualified/Deal + 1 hypothesis test.
**Tháng:** audit tracking end-to-end (bắn lead giả) · attribution · đánh giá chuyển giai đoạn bidding · keyword research mới · refresh creative · tính lại CPL target từ tỷ lệ chốt.
**Quý:** audit cấu trúc · incrementality test · test kênh mới · kế hoạch mùa vụ.

## 9. Top 10 ưu tiên (ngân sách nhỏ 10-30tr/tháng)

1. LP riêng mỗi dự án (bảng giá + mặt bằng + Zalo nổi) — đòn bẩy lớn nhất
2. Account-level negative list (cho thuê + tuyển dụng trước) — tiết kiệm 20-40% ngay
3. 2 dropdown qualifying trên form
4. 1 Search campaign, Phrase+Exact, Max Clicks có bid cap
5. Capture gclid → CRM + ECL qua Data Manager API — mở khóa mọi thứ
6. Đo contact rate, không chỉ CPL
7. Tên dự án (Exact) trước generic
8. Remarketing **Demand Gen** 10-15% (list ≥100 user — `[3P: Search Engine Land, CHƯA xác nhận ở tài liệu Google]`; gate G2 của hệ đặt ≥1.000 user nên vẫn an toàn). Display campaign mới đang bị migrate vào Demand Gen từ 6/2026.
9. Mùa vụ: giảm 50% Tết + tháng 7 âm, dồn T3-6 + T10-12
10. Click tặc: chỉ xem Invalid clicks + loại app placement (tool trả phí chỉ khi >50tr)

**KHÔNG làm với ngân sách nhỏ:** PMax, broad match, YouTube awareness, Demand Gen, chia 5 campaign, đổi bid mỗi ngày, Display cold, lead form asset thay LP.

## Khoảng trống dữ liệu
1. Không có benchmark CPL BĐS VN đáng tin công khai → chạy 30 ngày tự đo.
2. Chưa xác nhận Lead form assets khả dụng VN → kiểm tra trong tài khoản. (Thu hẹp: Google nói **120+ quốc gia**, điều kiện theo **vị trí user khi xem ad** → rào chắn thật là spend threshold + verification, không phải geo.)
3. Không có case study BĐS VN kiểm chứng được.
4. 🚨 **RỦI RO POLICY chưa phân xử — đọc TRƯỚC khi đầu tư vào lead form asset.** [Lead form policy](https://support.google.com/adspolicy/answer/9472930?hl=en) ghi: "**Affiliate networks and lead generation businesses are prohibited**". Hệ chạy cho **sàn phân phối BĐS** (không phải chủ đầu tư). Chưa đủ dữ liệu để phán Google có xếp sàn vào diện này không — và câu này **có thể hàm ý rộng hơn** phạm vi lead form. Phải verify nguyên văn cả trang policy + kiểm trong tài khoản trước khi làm; nếu nghi ngờ thì hỏi Google Ads support và lưu văn bản trả lời.
5. **Customer Match: ngưỡng $50k chỉ gate "Targeting", không gate cả tính năng.** [Customer Match policy](https://support.google.com/google-ads/answer/6299717?hl=en): cần 90 ngày history + **>$50.000 lifetime spend** để mở `Targeting`; dưới ngưỡng vẫn dùng được **`Observation` + `Exclusions`**. Nghĩa là remarketing GĐ5 bằng Customer Match ở quy mô 30tr₫/tháng **chỉ loại trừ được, chưa target được** — xem `research/google-official-curriculum.md` §E5. Khả dụng tại VN: **CHƯA XÁC NHẬN** ở tài liệu Google.

## Nguồn chính
WordStream 2026 benchmarks · Google Ads Help (PMax lead gen, ECL, AI Max, housing policy, offline conversion→Data Manager API) · Unbounce conversion benchmark · Spider AF / groas.ai (PMax spam, negative 10k) · PaidMediaWorld (cannibalization) · Search Engine Land (AI Max, Demand Gen min budget, audience 100 user, lead form $50k dropped — **3 claim cuối đã bị đính chính/đánh dấu 3P bằng doc Google, xem §1, §7, §9**) · SEONGON/Medialabs/Vietnix/Quangcaosieutoc (giá VN) · optimi.vn (lead rác) · leadup.vn/Admatrix (click tặc VN) · adsplus.vn (funnel BĐS) · Nhân Dân/Thời báo Tài chính/Cushman & Wakefield (thị trường 2026) · bluepear (trademark) · AgencyAnalytics/Swydo (checklist).
