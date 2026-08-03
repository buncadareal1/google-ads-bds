# Giáo trình CHÍNH THỨC của Google — đối chiếu với hệ Google Ads BĐS VN

**Ngày truy cập toàn bộ nguồn: 2026-07-28.** Mọi link là bản EN (`?hl=en`) vì bản VI thường chậm cập nhật hơn.

## Cách đọc file này

| Nhãn | Nghĩa |
|---|---|
| **KHỚP** | Hệ hiện tại (`research/google-ads-bds-vn.md`, `playbook/`, `tracking/`) đã đúng theo Google. Không cần làm gì. |
| **MỚI** | Google dạy, hệ chưa có. Đề xuất bổ sung ở §D. |
| **MÂU THUẪN** | Google nói khác cái hệ đã ghi. Trích cả 2 phía để QA phân xử. |

**Luật nguồn đã tuân thủ:** phần "Google dạy" chỉ lấy từ `support.google.com`, `blog.google`, `developers.google.com`. Nội dung syllabus chứng chỉ Skillshop: trang khóa học là JS shell (không fetch được) → syllabus lấy từ **study guide bên thứ 3, tin cậy THẤP**, được đánh dấu rõ `[3P]`; mọi điểm kiến thức trong syllabus đó đều đã được **học lại từ tài liệu Google chính thức** và ghi nguồn Google.

**Mục lục:**
- **Phần A** — Google Ads Help, 15 chủ đề đào sâu (A1 optimization score/auto-apply · A2 Ad Strength · A3 pinning · A4 account structure · A5 match type · A6 Smart Bidding/seasonality · A7 value-based bidding · A8 lead gen · A9 lead form · A10 ECL/Data Manager · A11 AI Max · A12 PMax · A13 Demand Gen/Display/Video migration · A14 search terms/limits · A15 policy)
- **Phần B** — GA4 chính thức (B1 key events · B2 audiences · B3 attribution · B4 thresholding · B5 BigQuery)
- **Phần C** — Chứng chỉ & khóa Skillshop: **SÂU** (Search · Measurement · AI-Powered Performance Ads · Grow Offline Sales · Search Ads Optimization · AI-Powered Search track · Google Analytics · PMax · **Privacy & Durable Measurement** · **Google Tag/GTM**) · **VỪA** (Display · Video+Reach Planner · Creative · Discovery→Demand Gen · **Microsoft Clarity**) · **LƯỚT** (Shopping · AI-Powered Shopping · Apps · SA360)
- **Phần D** — Bảng "Skill nào cần vá" (52 mục đề xuất, chia 3 mức rủi ro)
- **Phần E-0** — Danh sách "chưa đào hết" lập ở vòng 1
- **Phần E** — **VÒNG 2 (2026-07-28):** 7 chủ đề đã đào sâu (E1 data exclusions · E2 campaign experiments · E3 Insights page · E4 verify claim AI Max search terms · E5 Customer Match · E6 consent mode basic vs advanced · E7 Clarity custom tags API)
- **Changelog vòng 2** + **Chờ QA** — ở cuối file

**Cảnh báo diễn giải quan trọng — đọc trước §A4/A5:** phần lớn "best practice" Google publish được viết cho advertiser **đã có Smart Bidding + ≥15-30 conversion/30 ngày**. Hệ này khởi động ở 30tr₫/tháng, ~12-29 lead/tháng, chưa có ECL. Nhiều MÂU THUẪN dưới đây **không phải hệ sai** — mà là "Google khuyên cho advertiser trưởng thành". Mỗi MÂU THUẪN đều ghi rõ context này.

---

# PHẦN A — Google Ads Help: các chủ đề đào sâu

## A1. Optimization score & auto-apply recommendations

Nguồn: [About optimization score](https://support.google.com/google-ads/answer/9061546) · [About applying recommendations automatically](https://support.google.com/google-ads/answer/10279006?hl=en) · [Manage auto-apply recommendations](https://support.google.com/google-ads/answer/10276359?hl=en) (2026-07-28)

**Google dạy:**
- Optimization score 0-100%, tính real-time từ settings + statistics + recommendation impact + history. Chỉ hiện cho Search, Display, Video Action, App, PMax, Demand Gen, Shopping.
- **Dismiss recommendation LÀM TĂNG score** — score không phải thước đo chất lượng, nó là "% recommendation đã xử lý". Dismiss all vẫn khiến chúng quay lại sau.
- "Optimization score differs from Quality Score and isn't used by it."
- Auto-apply: **>17 recommendation** có thể tự bật, gom thành 2 bundle "Maintain your ads" / "Grow your business". Danh sách bao gồm những cái **rất nguy hiểm với lead gen BĐS**:
  - `Add broad match keywords`, `Add keywords (Smart bidding)`, `Use targeting expansion`, `Use Display expansion`, `Expand reach with Google search partners`
  - `Remove conflicting negative keywords` ← có thể **xóa negative** của mình
  - `Adjust CPA targets`, `Adjust ROAS targets`, `Set target CPA`, `Set bidding strategy target`, `Bid more efficiently with Maximize conversions`
  - `Improve Responsive Search Ads`, `Use optimized ad rotation`, `Add dynamic search ads`
  - `Upgrade conversion tracking`
- **Chỉ có auto-apply cấp TÀI KHOẢN** — "Only account-level auto-apply is available—campaign or ad group level automation doesn't exist." Không thể loại trừ 1 campaign.
- "Auto-applying recommendations won't increase your budget" — nhưng nó có thể mở rộng targeting trong cùng ngân sách → loãng.
- Cảnh báo DKI: ad group dùng Dynamic Keyword Insertion sẽ không auto-apply keyword; nếu negative chưa phủ hết, search term chưa duyệt có thể lọt vào ad text.
- **Recommendation áp dụng có tôn trọng pinned asset** ("Asset recommendations will honor existing pinned preferences").
- **Từ 26/01/2026**: recommendation `Add responsive search ads` không còn tự đề xuất/áp dụng RSA mới nữa.
- Xác minh: `Recommendations → Auto-apply settings`, và `Account Settings → Auto-apply` xem đang subscribe cái gì; `History tab` xem đã apply mấy lần, ai bật, lúc nào; có email tổng kết tuần.
- Tài liệu **không nói** Google tự bật giúp mà không có hành động của advertiser (chỉ mô tả luồng opt-in).

**So với hệ hiện tại:**

| Điểm | Nhãn | Chi tiết |
|---|---|---|
| Optimization score không phải KPI | **MỚI** | Hệ chưa nhắc optimization score ở đâu. Rủi ro: người vận hành (hoặc agency bên ngoài) thấy score thấp rồi bấm apply hàng loạt. Cần một dòng chống chỉ định. |
| Pre-flight tắt auto-apply | **MỚI** | `playbook/campaign-setup.md` §1.5 có 10 ô cài đặt nhưng **không có ô nào tắt auto-apply**. Đây là lỗ hổng thật: `Remove conflicting negative keywords` có thể xóa dần 216 negative account-level, `Use Display expansion` phá luật "Display chỉ remarketing" (`research` §1). |
| Auto-apply chỉ có cấp account | **MỚI** | Hệ dự kiến 5-9 campaign; không thể bật auto-apply cho 1 campaign test. → chính sách phải là "tắt tất, làm tay". |
| Whitelist auto-apply của hệ ≠ auto-apply của Google | **KHỚP (cần ghi rõ để không lẫn)** | `playbook/monitoring.md` §6 có "Whitelist hành động được auto-apply khi duyệt" — đó là **executor riêng của hệ, có người bấm nút, có guardrail, có audit log**. Hoàn toàn khác `Auto-apply recommendations` của Google (không người duyệt, không guardrail của mình). Hai thứ trùng tên → phải phân biệt trong doc, không thì có người tưởng đã tắt rồi. |
| Pinning được recommendation tôn trọng | **KHỚP** | Playbook §3 ghim H1 — recommendation sẽ không phá. (Nhưng AI Max thì có — xem A11.) |

---

## A2. Ad Strength — ảnh hưởng gì THẬT

Nguồn: [About Ad Strength for responsive search ads](https://support.google.com/google-ads/answer/9921843?hl=en) · [About Ad Strength](https://support.google.com/google-ads/answer/9142254?hl=en) · [About Ad Strength for Demand Gen](https://support.google.com/google-ads/answer/13720855?hl=en) (2026-07-28)

**Google dạy (trích nguyên văn):**
> "Ad Strength is a feedback tool for asset diversity and combination testing. **It isn't used to calculate Ad Rank, Quality Score, or auction wins.**"

> "Advertisers who improve Ad strength for their Responsive Search Ads and Sitelinks from 'Poor' to 'Excellent' see **15% more conversions on average**."

- 5 mức: Incomplete / Poor / Average / Good / Excellent. "Ad Strength doesn't determine whether your ad is eligible to serve."
- Áp dụng cho: RSA, Responsive Display, App, Demand Gen, PMax.
- Muốn Good+: **maximize 15 headline** nếu ad group nhiều keyword; và **≥6 sitelink** (tính gộp ad group + campaign + account level) + opt-in dynamic sitelinks.
- PMax: Ad Strength "Excellent" ≈ **6% more conversions** ([PMax lead gen best practices](https://support.google.com/google-ads/answer/13775965?hl=en)).
- Khuyến nghị: **≥2 RSA có Ad Strength Good/Excellent mỗi ad group**. RSA thứ 2 = **+6,6% conversion**, RSA thứ 3 = **+3,7%** ([About RSA](https://support.google.com/google-ads/answer/7684791?hl=en)).

**So với hệ hiện tại:**

| Điểm | Nhãn | Chi tiết |
|---|---|---|
| Ad Strength KHÔNG vào Ad Rank/QS | **MỚI** | Hệ chưa ghi ở đâu. Quan trọng vì `research/competitors/2026-07-eco-retreat.md:241` dùng "Ad Strength" làm **thước đo hiệu quả** — sai bản chất: nó là feedback tool lúc tạo ad, không phải KPI hiệu suất. Con số 15%/6,6% là **tương quan tổng hợp của Google**, không phải nhân quả cho 1 tài khoản. |
| 15 headline + 4 description | **KHỚP** | Playbook §3 đã đúng 15/4 cả 3 bộ. Script §3.5 assert đúng `len(H)==15 and len(D)==4`. |
| ≥2 RSA/ad group | **KHỚP** | Playbook §2.5 bước 7: "2 RSA/ad group ngày 1, chừa 1 slot cho biến thể tuần 3". Giới hạn 3 RSA/ad group đúng ([account limits](https://support.google.com/google-ads/answer/6372658?hl=en): "3 enabled responsive search ads per ad group"). |
| **≥6 sitelink** để đạt Good+ | **MÂU THUẪN** | Google: "you should provide **at least 6 sitelinks**" (tính gộp 3 cấp) + opt-in dynamic sitelinks. Hệ: `playbook/campaign-setup.md` §3.4 chỉ có **4 sitelink** cấp campaign, và không nhắc dynamic sitelinks. → hoặc thêm 2 sitelink, hoặc ghi rõ "chấp nhận Ad Strength thấp hơn vì cả 4 sitelink phải là anchor trên chính LP" (lý do hệ đưa ra ở §3.4 là giữ scent + không mất gclid — lý do hợp lệ, nhưng phải ghi ra là đánh đổi có ý thức). |

---

## A3. RSA pinning — trade-off thật

Nguồn: [About responsive search ads](https://support.google.com/google-ads/answer/7684791?hl=en) · [Ad Strength RSA](https://support.google.com/google-ads/answer/9921843?hl=en) · [AI Max FAQ](https://support.google.com/google-ads/answer/15913066?hl=en) (2026-07-28)

**Google dạy:**
- "Pinning reduces the overall number of headlines or descriptions that can be matched to a potential customer's search, **pinning isn't recommended for most advertisers and can affect ad strength.**"
- "Avoid pinning headlines or descriptions unless necessary, as it limits the system's ability to test combinations."
- Nhưng có nhượng bộ: "a **hybrid strategy** works best, such as when you **pin just one or 2 essential keyword headlines** while letting the rest rotate dynamically."
- **AI Max phá pinning:** "Pinning is not respected when both text customization and final URL expansion are enabled, or when URL inclusions are provided."

**So với hệ hiện tại:**

| Điểm | Nhãn | Chi tiết |
|---|---|---|
| Ghim đúng 1 headline (H1) | **KHỚP** | Playbook §3.1/§3.2/§3.3 đều "H1 = headline #1, còn lại không ghim" — đúng chuẩn hybrid Google nêu (pin 1-2). Lý do hệ đưa ra (khóa message match keyword↔ad↔LP) là chính đáng và Google không phủ định. **Kết luận: giữ nguyên**, nhưng nên ghi thêm 1 dòng "biết là hạ Ad Strength, đánh đổi có chủ đích". |
| Pinning + AI Max | **MỚI — quan trọng** | Khi bật AI Max (kế hoạch ở `campaign-setup.md` §5.3, sau G4 ≥6 tuần), **pinning H1 sẽ bị bỏ qua** nếu bật cả text customization + final URL expansion. Nghĩa là: message match khóa bằng pinning **sẽ tan** đúng lúc hệ mở AI Max. Phải chọn: bật AI Max nhưng TẮT final URL expansion (hệ đã dự kiến tắt — tốt), hoặc chấp nhận mất pinning. |

---

## A4. Cấu trúc tài khoản — "The ABCs of Account Structure"

Nguồn: [The ABCs of Account Structure](https://support.google.com/google-ads/answer/14752782?hl=en) · [Reaching the right customers on Search](https://support.google.com/google-ads/answer/6167110?hl=en) (2026-07-28)

**Google dạy (chính thức, 2026):**
- "Simpler structures with **consolidated, tightly-themed** setups unlock better performance, easier campaign management, clearer trends, and fewer errors."
- **A — Align with AI:** "Move single-keyword ad groups (SKAGs) into themed ad groups."
- **B — Bring Match Types Together:** gộp mọi match type vào **một** ad group, dùng chủ yếu **broad match**. "Broad match is the **only match type that uses all of the signals available**." Google nêu **62% advertiser dùng Smart Bidding lấy broad làm match type chính**.
- **C — Consolidate and Clean Up:** bỏ phân tách theo device (Smart Bidding đã tính device).
- Không có con số giới hạn campaign/ad group/keyword — Google cố tình nói nguyên tắc, không nói số.
- Trang "Reaching the right customers on Search": nếu bid theo conversion → **AI Max + broad + keywordless** cho reach lớn nhất; "traditional match types like phrase match or exact match" chỉ hợp "**if your bidding goals are focused on other metrics, like Target impression share**".

**So với hệ hiện tại — MÂU THUẪN LỚN NHẤT CỦA CẢ FILE:**

> **Google (2026):** consolidate, themed ad group, broad match là chính, bỏ SKAG.
> **Hệ hiện tại:** `keywords/adgroup-map.md` = **STAG** (single-theme ad group) chia rất mịn (brand-<slug> từng dự án, `<khu-vực>--gia-bang-gia`, `<khu-vực>--mua-ban`…); `research` §3 = "**<20tr/tháng: Phrase + Exact ONLY**", broad chỉ khi ≥30-50 conv/30 ngày; `PLAN.md` §0.1 = "1 Search campaign duy nhất, Phrase + Exact, Max Clicks có bid cap".

**Phân xử đề xuất (QA quyết):** đây là dạng "Google khuyên cho advertiser trưởng thành", KHÔNG phải hệ sai. Lý do cụ thể:
1. Điều kiện tiên quyết của broad theo chính Google là Smart Bidding: "**It's critical to use Smart Bidding with broad match**" ([Your guide to broad match](https://support.google.com/google-ads/answer/12159290?hl=en)). Ngày 1 hệ chạy **Max Clicks + bid cap** → không thỏa điều kiện.
2. Chính Google nói AI Max search term matching **không hoạt động với Manual CPC** (A11) → cùng logic, broad không có smart bidding = đốt tiền.
3. Hệ có ngưỡng riêng cho lead gen: contact rate, CPL qualified. Google tối ưu theo conversion đã khai — mà conversion khai ban đầu của hệ là form raw (chất lượng thấp).

**Nhưng hệ phải sửa 2 chỗ:**
- Ad group **quá mịn** đang đối đầu chính khuyến nghị "themed ad group" và ngưỡng ≥10 conv/ad group của chính hệ. `campaign-setup.md` §2.3 đã tự giới hạn (tối đa 3 ad group cho #1, 2 cho #3) — tốt, nhưng `adgroup-map.md` vẫn liệt kê cấu trúc mịn hơn nhiều. Cần một dòng "gộp là mặc định, tách chỉ khi ad group đủ ≥10 conv/tháng".
- Cần ghi **lộ trình leo thang tới AI-first** (xem A11 + §C2.6) chứ không phải "broad = xấu". Hiện `research` §3 đọc như một lệnh cấm, không phải một gate.

| Điểm | Nhãn |
|---|---|
| Consolidate > segment; kill SKAG | **MÂU THUẪN có context** (đã phân xử ở trên) |
| Broad là default match type của Google Ads (không khai match type = broad) | **MỚI** | [About keyword matching options](https://support.google.com/google-ads/answer/7478529?hl=en): "Broad match is the default match type that all your keywords are assigned". → Import TSV ở `campaign-setup.md` §2.4 **bắt buộc có cột `Match type`**; script `/tmp/mk.py` đã ghi cột đó (`r['match_type'].capitalize()`) — OK, nhưng phải có bước kiểm chứng "0 keyword nào ở Broad" sau import. |
| Bỏ phân tách theo device | **KHỚP** | Hệ không chia campaign theo device. |

---

## A5. Match type hiện hành 2025-2026

Nguồn: [About keyword matching options](https://support.google.com/google-ads/answer/7478529?hl=en) · [Your guide to broad match](https://support.google.com/google-ads/answer/12159290?hl=en) · [Google Ads keyword matching](https://support.google.com/google-ads/answer/14996023?hl=en) (2026-07-28)

**Google dạy — quy tắc hiện hành (không còn Broad Match Modifier):**

| Match type | Cú pháp | Quy tắc chính thức |
|---|---|---|
| Broad | `từ khóa` | "Ads may show on searches that are **related** to your keyword, which can include searches that **don't contain the direct meaning** of your keywords." Có tính cả search history của user, nội dung landing page, và các keyword khác trong ad group. |
| Phrase | `"từ khóa"` | "Ads may show on searches that **include the meaning** of your keyword. The meaning can be **implied**, and user searches can be a **more specific form** of the meaning." |
| Exact | `[từ khóa]` | "Ads may show on searches that have the **same meaning or same intent** as the keyword." |

- Broad **bắt buộc đi với Smart Bidding**: "It's critical to use Smart Bidding with broad match... every search query is different, and bids for each query should reflect the unique contextual signals present at auction-time."
- Broad "provides more data and flexibility for Smart Bidding" và "uses additional signals to ensure relevance and intent in expansions".

**So với hệ hiện tại:**

| Điểm | Nhãn | Chi tiết |
|---|---|---|
| Barbell Exact/Phrase lõi, broad chỉ khi ≥30-50 conv | **KHỚP về nguyên tắc điều kiện** | Điều kiện của hệ (đủ conversion) chính là hiện thân của điều kiện Google (Smart Bidding hoạt động được). Nhưng xem MÂU THUẪN ở A4 về giọng điệu. |
| "Broad match cap 15% ngân sách campaign" (research §3, campaign-setup §5.2) | **MỚI — Google không có ngưỡng này** | Không tìm thấy bất kỳ nguồn Google nào nói cap 15%. Đây là luật tự đặt của hệ. **Không sai** (thận trọng hợp lý) nhưng phải ghi rõ "luật nội bộ, không phải Google" để không bị QA sau này hiểu là citation Google. |
| Phrase match dùng cho negative | **MỚI — cần cẩn trọng** | Negative keyword có quy tắc match **riêng**, không giống positive: negative **không** khớp close variant. `campaign-setup.md` §1.4 bọc ngoặc kép thành phrase negative — đúng chủ ý, nhưng vì negative không tự khớp close variant, việc hệ **thêm biến thể không dấu** (`research` §3: "cho thue", "tuyen dung") là **bắt buộc, không phải tùy chọn**. Trong khi §2.4.5 lại ghi "Không tạo dòng riêng cho biến thể không dấu — Google tự khớp" — câu đó đúng cho **positive keyword**, sai nếu ai đó áp cho negative. → cần tách bạch trong doc. |

---

## A6. Smart Bidding, seasonality & seasonal budget adjustments

Nguồn: [About seasonality adjustments](https://support.google.com/google-ads/answer/10369906?hl=en) · [Create a seasonality adjustment](https://support.google.com/google-ads/answer/9352512?hl=en) · [About seasonal budget adjustments](https://support.google.com/google-ads/answer/12922263?hl=en) · [Finding success with Smart Bidding](https://support.google.com/google-ads/answer/6167140?hl=en) (2026-07-28)

**Google dạy — seasonality adjustments (điều chỉnh CONVERSION RATE):**
- Chỉ dùng cho **event ngắn 1-7 ngày**. "may not work as well if you use them for extended periods (**more than 14 days** at a time)".
- **KHÔNG dùng cho:** seasonality định kỳ ("Smart Bidding already manages these"), giai đoạn dài >14 ngày, và **các event kiểu Black Friday** (đã nằm trong model).
- Khả dụng: Search/Shopping/Display với **tROAS và tCPA**; PMax và App (beta) với **mọi** bid strategy. Travel không hỗ trợ.
- Sau event tự về trạng thái cũ, **không cần** đặt adjustment âm bù lại.
- Manager account có thể áp 1 adjustment cho nhiều account con.

**Google dạy — seasonal BUDGET adjustments (điều chỉnh NGÂN SÁCH — thứ khác hoàn toàn):**
- Lên lịch **tăng** average daily budget cho event giới hạn thời gian mà "unlike market seasonality, Google wouldn't be aware of".
- Chỉ **Search và Shopping**. **Loại trừ:** campaign dùng shared budget, campaign draft, dayparting, flighted, campaign đã có adjustment đang/sẽ chạy.
- Thời lượng **3-14 ngày**, tự trả về mức cũ. **Hai adjustment liên tiếp phải cách ≥7 ngày.**

**Google dạy — Smart Bidding:** trang best practice chính (6167140) **không** nêu ngưỡng conversion tối thiểu, không nêu độ dài learning period, không nêu mức chỉnh target — Google chỉ nói dùng experiments + bid strategy report. Con số duy nhất: "advertisers that switch their bid strategy from having a target CPA to a **target ROAS** can see **14% more conversion value** at a similar ROAS."

**So với hệ hiện tại:**

| Điểm | Nhãn | Chi tiết |
|---|---|---|
| "Dùng Seasonality adjustments cho event 1-7 ngày" (`research` §4) | **KHỚP chính xác** | Đúng khuyến nghị Google. `monitoring.md` §3 cũng ghi "Chỉ event 1-7 ngày" — KHỚP. |
| Tết / tháng 7 âm dùng seasonality adjustment? | **MÂU THUẪN tiềm ẩn — cần chốt** | Google: **không** dùng seasonality adjustment cho seasonality định kỳ, và không >14 ngày. Tết là định kỳ + hệ dự kiến "giảm 40-60% budget **2 tuần**" (`research` §4, `PLAN.md` §0.6) = 14 ngày, đúng biên. Hệ hiện tại không nói rõ Tết xử bằng **budget** hay bằng **seasonality adjustment**. Nếu ai đó hiểu là dùng seasonality adjustment cho Tết → **sai theo Google**. Cần ghi rõ: **Tết = đổi ngân sách bằng tay (hoặc script), KHÔNG dùng seasonality adjustment.** |
| Seasonal **budget** adjustments | **MỚI** | Hệ chưa biết công cụ này. Dùng được cho **đợt mở bán 3-14 ngày** (T3-6, T10-12): lên lịch tăng budget trước, tự trả về — thay cho việc sửa tay rồi quên sửa lại. Ràng buộc phải biết: chỉ Search/Shopping, **không dùng được nếu campaign nằm trong shared budget** → củng cố quyết định `campaign-setup.md` §1.5.10 "KHÔNG dùng ngân sách dùng chung ngày 1"; và **không** dùng được để GIẢM (Tết vẫn phải làm tay). Cách ≥7 ngày giữa 2 lần. |
| Seasonality adjustment cần tCPA/tROAS | **MỚI — chặn thực thi** | Search chỉ hỗ trợ **tROAS/tCPA**. Ngày 1 hệ chạy **Max Clicks** → `monitoring.md` §3 có suggest "Seasonality adjustment" nhưng **không thể apply được** trước khi qua §4.4 lên tCPA. Suggest engine phải có guard này, không thì bot đề xuất một việc API sẽ từ chối. |
| "Learning phase 1-2 tuần Search, tới 6 tuần PMax" | **KHỚP (nguồn khác)** | Trang Smart Bidding không nêu; nhưng [PMax lead gen best practices](https://support.google.com/google-ads/answer/13775965?hl=en) xác nhận: "at least 1-2 weeks (or **up to 6 weeks** for more complex setups or low conversion volume)". |
| "tCPA ±15%/lần, budget ±20%/lần, chờ 4 tuần" | **MỚI — không có nguồn Google** | Không tìm thấy Google publish các con số này. Là luật nội bộ của hệ (hợp lý, thận trọng). Phải ghi "luật nội bộ", không gán cho Google. |
| tCPA → tROAS +14% conversion value | **MỚI** | Bổ sung lý lẽ cho bước cuối lộ trình bidding (`campaign-setup.md` §4.4 dòng tROAS). |

---

## A7. Value-based bidding

Nguồn: [Value-based Bidding Best Practices](https://support.google.com/google-ads/answer/14792795?hl=en) · [About Smart Bidding using value-based bidding](https://support.google.com/google-ads/answer/15099424?hl=en) · [Conversion Values Best Practices](https://support.google.com/google-ads/answer/14791574?hl=en) (2026-07-28)

**Google dạy:**
- Ngưỡng: **≥15 conversion/tháng ở cấp TÀI KHOẢN**.
- Cần hệ đo "consistently track **2 or more unique, non-zero values**".
- Cho phép **proxy value**: "utilize proxy values that align with your business priorities" khi chưa định giá chính xác được.
- **Cảnh báo về value 0:** "It's generally **not recommended** to use conversions with 0 values with value based bidding." Nếu conversion không có giá trị → **bỏ nó khỏi dataset**, đừng gán 0.
- Cho lead gen: dùng Maximize conversion value / tROAS để "prioritize leads with the strongest potential for high-value sales".

**So với hệ hiện tại:**

| Điểm | Nhãn | Chi tiết |
|---|---|---|
| Thang 1/10/50/500 phân tầng | **KHỚP** | Đúng tinh thần "2+ unique non-zero values" và proxy value. `PLAN.md` §6.7 đang treo câu hỏi "điểm hay ₫ thật" — Google trả lời: **proxy value được phép**, không cần ₫ thật để bắt đầu. Đây là câu trả lời cho một open question của hệ. |
| "Form submit raw: giá trị **0-1**" (`research` §5 bảng) | **MÂU THUẪN nhẹ** | Google: đừng dùng value 0 với VBB. `campaign-setup.md` §1.2 đã đặt giá trị **1** (không phải 0) — đúng. Nhưng `research` §5 viết "0-1" → phải sửa thành **1** để không ai đặt 0. |
| Ngưỡng 15 conv là cấp **account**, không phải campaign | **MÂU THUẪN nhẹ** | Hệ: `campaign-setup.md` §4.4 "**Campaign đó** ≥15 conversion/30 ngày"; `research` §4 "value-based bidding (cần ≥15 conv/30 ngày)". Google nói **account level**. Ngưỡng cấp campaign của hệ **khắt khe hơn** Google → an toàn, nhưng có thể chặn hệ quá lâu. QA nên chốt: giữ khắt khe cho tCPA cấp campaign, dùng ngưỡng account cho quyết định bật VBB. |

---

## A8. Lead gen best practices — Google dạy gì cho chính nghề của hệ

Nguồn: [Best practices for generating high-quality leads](https://support.google.com/google-ads/answer/13489421?hl=en) (2026-07-28)

**Google dạy:**
- **Lead Journey Mapping** — công cụ có trong Google Ads để map "the steps your leads take from their first interaction to a closed sale", tối ưu theo outcome kinh doanh chứ không phải lead volume.
- Conversion goal nên dùng: `qualified lead`, `converted lead`, `book appointment`, `request quote`.
- Ngưỡng: "**at least 15 conversions in the last 30 days at the account level**".
- **Conversion delay nên trong vòng 7 ngày** kể từ ad interaction "for timely optimization".
- Upload offline conversion **thường xuyên, tốt nhất là hằng ngày**.
- Nền đo lường: Google Tag → **enhanced conversions for leads** để grounding bằng first-party data "**instead of Click ID reliance**"; dùng **Data Manager** kết nối CRM (Google nêu HubSpot, Salesforce).
- Value-based bidding + **Conversion Value Rules** (tinh chỉnh theo geo/device/audience).
- Chống lead rác: reCAPTCHA, **double opt-in**, server-side validation; content/placement exclusions + brand exclusions.

**So với hệ hiện tại:**

| Điểm | Nhãn | Chi tiết |
|---|---|---|
| Bid theo lead qualified, không theo form raw | **KHỚP hoàn toàn** | `PLAN.md` §0.4 + `campaign-setup.md` §1.2 đảo primary/secondary — đúng đích Google dạy. Đây là điểm hệ đã làm đúng trước cả khi đọc doc. |
| ECL + gclid + upload hằng ngày | **KHỚP** | `tracking/ecl-keap-pipeline.md`. Lưu ý câu Google: ECL grounding bằng first-party data **thay vì phụ thuộc Click ID** → tăng giá trị của field `email` (LP để email TÙY CHỌN, `research` §6). |
| reCAPTCHA + qualifying question | **KHỚP** | `research` §5 + 2 dropdown. |
| **Conversion delay ≤7 ngày** | **MÂU THUẪN thực chất — cần QA** | Google muốn conversion về trong 7 ngày để bidding học kịp. Hệ đặt **click conversion window = 90 ngày** (`campaign-setup.md` §1.2.4) vì "chu kỳ BĐS 3-12 tháng". Cả hai đều đúng nhưng phục vụ 2 việc khác nhau: window 90 ngày để **không mất conversion khi báo cáo**; delay ≤7 ngày để **bidding học được**. Hệ quả thực tế: **`Lead_Contactable` (giá trị 10, primary để bid) phải được sales tag + upload trong ≤7 ngày**, không phải "khi nào rảnh". `Lead_Qualified` và `Dat_Coc` chậm hơn thì chấp nhận, nhưng không nên là tín hiệu bid chính. → Đây là một **SLA cho sales**, và nó nối trực tiếp vào `PLAN.md` §6.6 (quy trình sau-lead đang PENDING vì chưa có quyền Keap). Ghi vào đó. |
| **Lead Journey Mapping** | **MỚI** | Công cụ native trong Google Ads, hệ chưa biết. Trùng mục đích với KPI tree ở `customer-journey-plan.md` §4 nhưng nằm trong UI Ads và feed thẳng vào bidding. Cần kiểm tra khả dụng VN. |
| **Conversion Value Rules** | **MỚI** | Điều chỉnh giá trị conversion theo geo/device/audience mà **không** cần đổi tag. Ứng dụng BĐS: lead từ đúng quận dự án đáng giá hơn lead ngoại tỉnh; lead từ audience `xem_bang_gia_30d` đáng giá hơn lead lạ. Rẻ hơn nhiều so với dựng thêm conversion action. Nhớ đọc thêm [Impact of conversion value rules on Smart Bidding](https://support.google.com/google-ads/answer/10520545?hl=en). |
| **Double opt-in** | **MỚI (Google khuyên, hệ nên từ chối có lý)** | Google khuyên double opt-in để lọc bot. Với BĐS VN CTA là gọi/Zalo, double opt-in email sẽ giết CVR. Đây là chỗ hệ nên **ghi rõ đã cân nhắc và từ chối**, cùng loại với quyết định về OTP (`research` §5: "OTP chỉ bật khi CPL qualified quá cao"). |
| Conversion goal chuẩn tên Google | **MỚI (nhỏ)** | Google có sẵn goal category `Qualified lead`, `Converted lead`, `Book appointment`, `Request quote`. Hệ đặt tên tự do (`Lead_Contactable`, `Lead_Qualified`, `Dat_Coc`). Nên **map** action của hệ vào goal category chuẩn của Google khi tạo (UI có chọn category) — vì PMax/AI Max và các recommendation đọc theo category, không đọc theo tên. |

---

## A9. Lead form asset — điều kiện VN & qualifying responses

Nguồn: [About lead form assets](https://support.google.com/google-ads/answer/9423234?hl=en) · [Lead form requirements (policy)](https://support.google.com/adspolicy/answer/9472930?hl=en) · [About qualifying responses in lead forms](https://support.google.com/google-ads/answer/17050941?hl=en) (2026-07-28)

**Google dạy:**
- Điều kiện: vertical đủ điều kiện (vertical nhạy cảm bị loại); **privacy policy bắt buộc** (link hiện cuối form); history tuân thủ policy tốt; phải hoàn thành **advertiser verification**.
- **Ngưỡng chi tiêu:** thêm lead form vào **Video/Display**, hoặc tạo **Search campaign mà headline mở trực tiếp lead form** → cần **>$50.000 USD tổng chi tiêu**. Ngoại lệ: "**Reputable advertisers spending more than $1,000 USD per account (or more than $15,000 USD across all accounts)**" cũng có thể đủ điều kiện, tùy thẩm định thêm về account status/good standing.
- Campaign type: **Search và Performance Max**. Expanded text ads không dùng được. RSA mở trực tiếp lead form cần conversion-based bidding + Google lead form conversion goal.
- **Lưu lead 60 ngày**; **CSV download chỉ 30 ngày**; lấy lead qua CSV / email notification / Google Ads API / **webhook** / Zapier.
- Khả dụng **120+ quốc gia**; điều kiện là **vị trí của user khi xem ad**.
- Policy: cấm dùng cho sexual content, alcohol, gambling, healthcare/medicines, political content; "**Affiliate networks and lead generation businesses are prohibited**"; dữ liệu cá nhân chỉ dùng đúng phần user đã đồng ý.

**Qualifying responses (tính năng mới, rất sát hệ):**
- Câu hỏi multiple-choice từ danh sách Google, hoặc **tự đề xuất câu hỏi riêng** ("for example, 'Which model are you interested in?'").
- Mục đích: "filter or segment leads based on user responses so you can identify users with the specific intent you're targeting".
- Có **conversion action riêng: `Lead form - Response qualified (Google-hosted)`** — hệ thống tự tag submission đạt điều kiện.
- **"Qualifying responses are available for Search campaigns only."**
- Câu hỏi qualifying **không thể** đặt optional — bắt buộc user trả lời.

**So với hệ hiện tại:**

| Điểm | Nhãn | Chi tiết |
|---|---|---|
| "Đã bỏ yêu cầu $50k spend (7/2026)" (`research` §7) | **MÂU THUẪN — hệ đang ghi sai/quá mạnh** | Doc Google **vẫn còn** ngưỡng >$50.000 cho Video/Display và cho Search-headline-mở-form. Cái tồn tại là **đường thay thế** $1.000/account (hoặc $15.000 across accounts) cho "reputable advertisers" + verification. Nghĩa là: hệ 30tr₫/tháng (~$1.100/tháng) **có thể** đủ điều kiện đường thay thế, nhưng KHÔNG phải "đã bỏ yêu cầu". Câu trong `research` §7 phải viết lại. Nguồn gốc claim cũ là Search Engine Land (bên thứ 3), không phải Google. |
| "Chưa xác nhận Lead form assets khả dụng VN" (`research` §Khoảng trống 2) | **ĐÃ TRẢ LỜI phần lớn** | Google: 120+ quốc gia, điều kiện theo **vị trí user xem ad**. Trang không liệt kê VN tường minh trong đoạn fetch được → vẫn phải kiểm trong tài khoản, nhưng khoảng trống thu hẹp: rào chắn thật là **spend threshold + verification**, không phải geo. |
| **Qualifying responses** | **MỚI — trùng đúng đòn bẩy #3 của hệ** | `PLAN.md` §0.2 và `research` §5 coi "2 dropdown qualifying trên form" là đòn bẩy thứ 3. Google giờ có **bản native**: câu hỏi bắt buộc + conversion action riêng cho lead đã qualify, ngay trong lead form asset, **Search only**. Đây là con đường ngắn nhất để có tín hiệu "qualified" **mà không cần chờ ECL/CRM**. Đánh giá cho hệ: **không thay LP** (LP vẫn thắng vì có bảng giá/mặt bằng — `research` §6, và `research` §9 "KHÔNG làm: lead form asset thay LP"), nhưng **rất đáng test song song** như kênh thứ 2, đặc biệt vì nó cấp một primary conversion sạch từ tuần 1 thay vì tuần 8. |
| "Affiliate networks and lead generation businesses are prohibited" | **MỚI — RỦI RO, cần QA/legal đọc kỹ** | Hệ chạy cho **sàn phân phối BĐS** (không phải chủ đầu tư). Nếu Google xếp sàn = "lead generation business" thì lead form asset bị cấm hẳn — và câu này còn có thể ảnh hưởng rộng hơn lead form. Chưa đủ dữ liệu để phán; **phải verify trực tiếp trên [lead form policy](https://support.google.com/adspolicy/answer/9472930?hl=en) và trong tài khoản trước khi đầu tư vào lead form asset.** Ghi vào khoảng trống dữ liệu. |
| Lưu lead 60 ngày / CSV 30 ngày | **MỚI (vận hành)** | Nếu dùng lead form asset, **bắt buộc webhook**, không dựa vào CSV — lead quá 30 ngày không tải lại được. |

---

## A10. ECL / offline conversion / Data Manager — xác nhận & 2 mốc mới

Nguồn: [About enhanced conversions for leads](https://support.google.com/google-ads/answer/15713840?hl=en) · [About offline conversion imports](https://support.google.com/google-ads/answer/2998031?hl=en) · [Data Manager với ECL](https://support.google.com/google-ads/answer/15707550?hl=en) · [ECL implementation checklist](https://support.google.com/google-ads/answer/16782203?hl=en) · [About conversion windows](https://support.google.com/analytics/../google-ads/answer/3123169?hl=en) (2026-07-28)

**Google dạy:**
- **Xác nhận nguyên văn:** "Starting **June 15, 2026**, offline conversions import and enhanced conversions for leads uploads will be **migrated to the Data Manager API and blocked in the Google Ads API**." Developer token không có request trong khoảng 1-6/2026 sẽ **không** được allowlist truy cập legacy.
- **MỐC MỚI:** "Starting **April 2026**, enhanced conversions for web and leads will merge into **a single on/off setting**", đồng thời nhận user-provided data từ website tag, Data Manager và API connections.
- Identifier: email / phone / address (hashed). **GCLID không bắt buộc nhưng**: "To maximize accuracy, include GCLIDs with your uploaded events whenever possible" — và **bắt buộc nếu không dùng tag để thu user-provided data**.
- **Luật hay bị bỏ sót:** "You must upload **ALL conversions** for the specified event, **including those not attributed to Google Ads** — this is required for enhanced conversions for leads to function correctly."
- Upload **hằng ngày** (strongly recommended). Method: Data Manager / Google Ads API / SFTP.
- Data Manager connector: Google Sheets, Zapier third-party integration, "featured products" (Google nêu HubSpot, Salesforce ở trang lead-gen best practices). **Keap không nằm trong danh sách nêu tên.**
- Conversion window: click-through **1 đến 30/60/90 ngày** tùy nguồn conversion; "Windows of at least 7 days are recommended".

**So với hệ hiện tại:**

| Điểm | Nhãn | Chi tiết |
|---|---|---|
| Data Manager API bắt buộc từ 15/6/2026 | **KHỚP — xác nhận nguyên văn** | `research` §5, `PLAN.md` §0.3, `tracking/ecl-keap-pipeline.md` đều đúng. |
| Keap không phải featured connector → gọi REST API trực tiếp | **KHỚP** | `PLAN.md` §6.3 quyết định đúng. |
| Conversion window 90 ngày | **KHỚP** | Đúng max Google cho phép. |
| **Phải upload TẤT CẢ conversion của event, kể cả không do Google Ads mang lại** | **MỚI — có thể làm ECL sai nếu bỏ qua** | Nghĩa là `tracking/upload_ecl.py` phải đẩy **mọi** lead đạt trạng thái contactable/qualified, kể cả lead từ Facebook/organic/walk-in. Nếu chỉ upload lead có gclid, model match của Google bị lệch (nó cần biết tỷ lệ nền). Đây là điểm **rất dễ làm sai** và không hiển nhiên. **Ưu tiên cao nhất trong danh sách vá của tracking/.** |
| **April 2026: ECL web + leads gộp thành 1 setting** | **MỚI** | Đã qua mốc (hôm nay 28/7/2026). Nghĩa là khi vào tài khoản, thứ nhìn thấy là **một** toggle enhanced conversions, không phải hai. `tracking/ecl-keap-pipeline.md` viết theo mô hình cũ (hai đường riêng) có thể lệch UI thật → cần verify khi có quyền tài khoản. |
| GCLID vẫn nên gửi | **KHỚP** | Skill `ad-click-attribution` + `campaign-setup.md` §4.3 (lead không có gclid = pause). Google xác nhận gclid làm tăng accuracy dù không bắt buộc khi đã có tag. |

---

## A11. AI Max for Search — trạng thái thật 2026 & các auto-upgrade

Nguồn: [About AI Max for Search](https://support.google.com/google-ads/answer/15910366?hl=en) · [How AI Max works](https://support.google.com/google-ads/answer/15910187?hl=en) · [AI Max FAQ](https://support.google.com/google-ads/answer/15913066?hl=en) · [Brand inclusions](https://support.google.com/google-ads/answer/14453047) · [blog: AI Max expands globally](https://blog.google/products/ads-commerce/google-ai-max-expands-globally/) · [blog: DSA upgrading to AI Max](https://blog.google/products/ads-commerce/dsa-upgrade-to-ai-max-2026/) (2026-07-28)

**Google dạy:**
- AI Max = **opt-in setting trong Search campaign**, không phải campaign type. Gồm 3 phần: improved search term matching (broad + keywordless), **text customization** headline/description, **final URL expansion**.
- Kiểm soát còn giữ: **negative keywords** — FAQ nói nguyên văn "Yes. Negative keywords will be respected even with AI Max turned on."; brand settings; location; URL exclusions/inclusions.
- Số Google công bố: **+14% conversion/conversion value ở CPA/ROAS tương đương** (non-retail, internal data 2025); với campaign phụ thuộc nặng exact+phrase, "the typical uplift is even higher at **27%**"; blog GA nói "**7% more** conversions or conversion value" khi dùng full feature suite.
- **CHẶN LỚN:** "The Search Term Matching feature in AI Max **will not work with manual CPC bidding**." Cần conversion-based bidding.
- **Pinning bị bỏ qua** khi bật cả text customization + final URL expansion, hoặc khi có URL inclusions.
- Asset AI Max **không customize được** grammar/special offers; ad mới có thể tái dùng copy có sẵn nếu khớp query + URL.
- **Brand inclusions upgrading vào AI Max từ 27/05/2025.** Cảnh báo: "If your Search campaign already has negative keywords that match terms from your brand inclusion, it may cause a **reduction in performance**."
- **Auto-upgrade legacy → AI Max** (blog, 2026): 3 thứ bị nâng cấp — **Dynamic Search Ads (DSA)**, **Automatically Created Assets (ACA)**, và **campaign-level broad match setting**. Timeline: nâng cấp tự nguyện ngay → **tháng 9/2026 bắt đầu auto-upgrade + ngừng tạo DSA mới** → **tháng 2/2027 DSA sunset**. "We strongly recommend transitioning to AI Max now to maintain full control over your campaign setup."
- Tính năng mới đi kèm: **AI Brief** (dùng lời của mình để steer AI, powered by Gemini), **text disclaimers** (đảm bảo text bắt buộc luôn xuất hiện kể cả khi bật final URL expansion), **text guidelines**, one-click experiments.
- Có trang riêng [About reporting in AI Max](https://support.google.com/google-ads/answer/16470459) — reporting bổ sung; trang search terms report chung **không** xác nhận tường minh cho AI Max.

**So với hệ hiện tại:**

| Điểm | Nhãn | Chi tiết |
|---|---|---|
| AI Max là lớp opt-in, không phải campaign type; giữ negative + search terms | **KHỚP** (negative: xác nhận nguyên văn) · **CHƯA XÁC NHẬN** (search terms report) | `research` §1.3 nói "an toàn hơn PMax vì **giữ search terms report** + negative cấp campaign". Negative: Google xác nhận. Search terms report cho AI Max: **không tìm được câu xác nhận tường minh** trên trang search terms report — cần verify ở trang reporting riêng của AI Max trước khi giữ claim này. |
| "Bật AI Max SAU khi Search ổn định; tắt final URL expansion" | **KHỚP + mạnh hơn** | Tắt final URL expansion còn có lợi ích thứ 2 mà hệ chưa biết: **giữ được pinning H1** (message match). |
| **AI Max không chạy với Manual CPC / Max Clicks** | **MỚI — chặn thực thi** | `campaign-setup.md` §5.3 đặt AI Max "sau G4 ≥6 tuần" — G4 đã yêu cầu offline import chạy + tCPA nên may là không xung đột. Nhưng phải ghi tường minh điều kiện "conversion-based bidding" vào dòng đó, không thì có người thử AI Max lúc còn Max Clicks và kết luận sai là "AI Max không hiệu quả". |
| **ACA auto-upgrade vào AI Max (9/2026 → 2/2027)** | **MỚI — xung đột trực tiếp với §1.5.6** | `campaign-setup.md` §1.5.6 bắt **TẮT** "Tài sản tự động tạo (ACA)" + "Văn bản quảng cáo động" vì rủi ro policy/không kiểm soát copy. Google đang **auto-upgrade ACA thành AI Max**. Cần chốt: nếu ACA đã tắt thì có bị auto-upgrade không? (khả năng là không — không có gì để nâng cấp), nhưng phải đưa mốc 9/2026 và 2/2027 vào lịch giám sát, và phải biết rằng **text disclaimers** là cơ chế Google cấp để giữ text bắt buộc (pháp nhân/MST/miễn trừ) khi buộc phải sống với AI text. |
| Brand inclusions ↔ 216 negative account-level | **MỚI — rủi ro cụ thể** | Nếu sau này bật brand inclusions/AI Max: negative hiện có trùng term trong brand inclusion sẽ **giảm hiệu suất** theo cảnh báo của Google. Hệ có 216 negative account + 40 campaign, trong đó có nhóm "portal" và "tên đối thủ" — dễ trùng. Cần một bước rà chéo trước khi bật. |
| DSA sunset 2/2027 | **KHỚP (hệ không dùng DSA)** | Không ảnh hưởng — nhưng lưu ý auto-apply có recommendation `Add dynamic search ads` (A1), nếu ai bật auto-apply thì DSA có thể tự xuất hiện rồi tự bị nâng lên AI Max. Thêm một lý do tắt auto-apply. |
| AI Brief / text guidelines / text disclaimers | **MỚI** | Công cụ steer AI bằng brand voice. Đáng biết cho lúc qua G4: thay vì "không dùng AI text vì rủi ro policy", có thể "dùng AI text + text disclaimers để khóa footer pháp nhân/miễn trừ". |

---

## A12. Performance Max cho lead gen

Nguồn: [PMax best practices for lead generation](https://support.google.com/google-ads/answer/13775965?hl=en) · [Negative keywords in PMax](https://support.google.com/google-ads/answer/15726455?hl=en) · [About account-level negative keywords](https://support.google.com/google-ads/answer/11396330) (2026-07-28)

**Google dạy:**
- Conversion goal nên dùng: Contact, Submit Lead Form, Book Appointment, Sign-up, Request Quote, **Qualified Lead**, **Converted Lead**. Chọn goal có **≥15 conversion trong 30 ngày qua**.
- Bidding: chú trọng **giá trị** lead → Maximize conversion value / tROAS; chú trọng **số lượng** → Maximize conversions.
- Asset: ≥20 text asset (15 headline + 5 description), ≥7 image (3 landscape, 3 square, 1 portrait), ≥1 video. Nhắm Ad Strength **Excellent** (≈ +6% conversion).
- Lead quality: qualifying question trên form, reCAPTCHA trên LP, server-side validation, rà **negative keywords** và **placement exclusions**.
- Learning: "at least 1-2 weeks (or up to 6 weeks for more complex setups or low conversion volume)".
- New Customer Acquisition mode: cần **Customer Match list** để Google phân biệt khách mới/cũ.
- Account-level negative keyword list: giới hạn **1.000**, tự áp cho "all search and shopping inventory in **Search, Performance Max, App, Shopping, Smart, and Local** campaigns".

**So với hệ hiện tại:**

| Điểm | Nhãn | Chi tiết |
|---|---|---|
| PMax chỉ khi ECL chạy + đủ volume | **KHỚP** | `research` §1, `PLAN.md` §0.5, gate G4. Google cũng đặt điều kiện ≥15 conv/30 ngày cho goal + khuyên offline import/ECL cho lead gen. |
| Bắt buộc negative + brand exclusion + loại App/Games | **KHỚP** | `campaign-setup.md` §5.3. |
| Negative 10.000/campaign, list 5.000, account-level 1.000 | **KHỚP** | [Account limits](https://support.google.com/google-ads/answer/6372658?hl=en): 10.000 negative/campaign, 5.000/list, tối đa **20 list per manager account**. Account-level negative = 1.000. `research` §1 nói "giới hạn 10.000 từ 3/2025" — đúng. |
| Ghi chú §1.4 của campaign-setup về nơi đặt negative | **MÂU THUẪN nhẹ — sửa câu** | Hệ viết: "Google có thêm ô `Account settings → Account negative keywords` (giới hạn 1.000). Không dùng song song... **Danh sách dùng chung thắng vì áp được cả cho PMax sau này**". Theo Google, **chính account-level negative keywords mới là cái tự áp cho PMax/App/Shopping/Smart/Local**. Shared list thì phải gắn tay vào từng campaign. Lựa chọn "1 nơi duy nhất" của hệ vẫn hợp lý (dễ quản, 216 < 1.000 nên account-level cũng chứa được), nhưng **lý do đưa ra là sai** và sẽ dẫn tới quyết định sai lúc mở G4. |
| Asset PMax 20 text / 7 image / 1 video | **MỚI** | Chưa có ở đâu trong hệ. Cần đưa vào checklist G4 — BĐS phải chuẩn bị ảnh flycam/nhà mẫu theo đúng 3 tỷ lệ trước khi bật PMax, không phải sau. |
| New Customer Acquisition cần Customer Match list | **MỚI** | Với BĐS, "khách cũ" ít giá trị loại trừ, nhưng Customer Match list từ Keap có thể dùng để **loại trừ khách đã mua** khỏi mọi campaign — hệ hiện chỉ loại trừ bằng audience GA4 `da_generate_lead_14d` (14 ngày, ngắn). |

---

## A13. Demand Gen (và số phận của Display / Video Action)

Nguồn: [About Demand Gen](https://support.google.com/google-ads/answer/13695777?hl=en) · [Demand Gen best practices](https://support.google.com/google-ads/answer/14693848?hl=en) · [Google Display Ads campaigns have a new home in Demand Gen](https://support.google.com/google-ads/answer/17051545?hl=en) · [Video Action Campaigns upgrading to Demand Gen](https://support.google.com/google-ads/answer/15110871?hl=en) (2026-07-28)

**Google dạy:**
- Discovery campaigns đã **bị nâng cấp hết thành Demand Gen cuối tháng 1/2024**; Discovery không còn tồn tại trong Google Ads.
- Demand Gen phủ YouTube (kể cả Shorts), Discover, Gmail, Maps, **và Google Display Network**.
- **Video Action Campaigns (VAC) đã bị khai tử:** 4/2025 ngừng tạo mới → 7/2025 auto-upgrade → 12/2025 khóa end date ở 31/1/2026 → **4/2026 hạn cuối auto-migrate**. Thay thế = Demand Gen. Lưu ý: một số tính năng **không được hỗ trợ trong Demand Gen**, trong đó có **lead form ads** và seasonal event targeting.
- **Google Display Ads campaigns đang được migrate vào Demand Gen:** 6/2026 bắt đầu rollout migration tool; sau đó "New Google Display Ads campaigns **can only be created within Demand Gen**"; cuối cùng auto-migrate các campaign còn lại. Migration tool port performance history 42 ngày, learning chỉ ~1-2 ngày, tránh cold start. Remarketing list vẫn được hỗ trợ trong Demand Gen.
- **Ngân sách Demand Gen (best practice):** maximize strategies → **$100+/ngày**; target strategies (tCPA/tROAS) → **≥10× target CPA/ngày**.
- Asset: 3 vertical + 3 square + 3 horizontal image; 1 vertical + 1 square + 1 horizontal video. Áp khung **ABCD** (Attention, Branding, Connection, Direction).
- Audience: bật **Optimized Targeting** cho prospecting + first-party seedlist; Remarketing cho re-engagement; NCA goal cho khách mới.
- Đo lường: tính **conversion lag**, xem trend dài hạn không xem ngày; dùng metric "Conversions (Platform Comparable)" khi so với social.

**So với hệ hiện tại:**

| Điểm | Nhãn | Chi tiết |
|---|---|---|
| **`BDS_RMKT_Display` (campaign type Display) đang bị Google khai tử** | **MÂU THUẪN — kế hoạch G2 cần viết lại** | `campaign-setup.md` §2.1/§5.1/§5.2 và `PLAN.md` §0.5 đều dựa trên **standard Display campaign** cho remarketing (10-15% ngân sách, gate G2). Google: từ 6/2026 Display migrate vào Demand Gen, và sẽ **không tạo được Display campaign mới**. → Khi hệ tới G2 (dự kiến sau ≥1-2 tháng chạy, tức Q4/2026) có thể **không còn tạo được** campaign như đã viết. Phải đổi kế hoạch sang **Demand Gen (GDN inventory) cho remarketing**, hoặc kiểm tra ngay khả dụng trong tài khoản. |
| "Demand Gen min $5/ngày bắt buộc" (`research` §1) | **MÂU THUẪN** | Google best practice: **$100+/ngày** cho maximize strategies, hoặc ≥10× tCPA/ngày. $5/ngày (nguồn Search Engine Land, bên thứ 3) có thể là **minimum kỹ thuật**, không phải mức chạy được. Với hệ 30tr₫/tháng (~1tr₫/ngày ≈ $38/ngày), Demand Gen theo chuẩn Google **không vừa ngân sách** → củng cố quyết định `research` §9 "KHÔNG làm với ngân sách nhỏ: Demand Gen", nhưng lý do phải sửa cho đúng. Với 150tr₫ (5tr₫/ngày ≈ $190/ngày) thì khả thi. |
| VAC đã chết → kế hoạch YouTube ở G5 | **MỚI** | `campaign-setup.md` §5.3 ghi "Campaign mới: YouTube — video dự án tự sản xuất, đo bằng brand search lift". Cần nói rõ hình thức: nếu là YouTube **conversion** thì đường duy nhất giờ là **Demand Gen**, không còn VAC. Nếu là awareness thuần thì vẫn có Video campaign (reach/views). |
| Demand Gen **không hỗ trợ lead form ads** | **MỚI** | Nếu sau này định dùng lead form trên YouTube/Discover → không được. Củng cố hướng "LP là nơi nhận lead". |
| Asset 3×3 image + 3 video, khung ABCD | **MỚI** | Chưa có trong hệ. Nếu G2 chuyển sang Demand Gen thì đây là **yêu cầu sản xuất creative** phải lên kế hoạch trước, không phải bật là chạy. |
| Optimized Targeting | **MỚI — cần cẩn trọng** | Google khuyên bật cho prospecting. Với BĐS lead gen ngân sách nhỏ, đây là cùng họ với "targeting expansion" mà hệ đang chủ trương tắt. Cần một quyết định tường minh, không để mặc định. |
| Conversion lag phải tính vào đánh giá | **KHỚP về tinh thần** | `research` §4 "chờ 4 tuần mới phán xét". Google nói cùng ý cho Demand Gen. |

---

## A14. Search terms report, negative keywords, account limits

Nguồn: [About the search terms report](https://support.google.com/google-ads/answer/2472708) · [Get negative keyword ideas using the search terms report](https://support.google.com/google-ads/answer/7102466?hl=en) · [About negative keywords](https://support.google.com/google-ads/answer/2453972?hl=en) · [Account limits](https://support.google.com/google-ads/answer/6372658?hl=en) (2026-07-28)

**Google dạy:**
- Search terms report chỉ hiện "search terms that **a significant number of people** have used"; "Some search terms that don't have enough query activity are **omitted**... to keep with our standards on data privacy." → **Không bao giờ thấy 100% traffic.**
- PMax **có** search terms report ("helps identify search terms that resulted in conversions"). DSA/Shopping có nhưng không trả keyword, match type luôn hiện "Exact".
- Search terms **insights** (theme/subtheme) sinh từ **56 ngày** dữ liệu gần nhất.
- Store visits / store sales conversions **không** tương thích search terms report.
- Account limits: 10.000 campaign/account · 20.000 ad group/campaign · 5 triệu ad-group targeting item/account · 10.000 negative keyword/campaign · 5.000 keyword/negative list · **20 list per manager account** · **3 enabled RSA/ad group** · 50 active text ad/ad group.

**So với hệ hiện tại:**

| Điểm | Nhãn | Chi tiết |
|---|---|---|
| Nghi thức tuần T2 đọc search terms | **KHỚP** | `research` §8, `campaign-setup.md` §4.1. |
| **Một phần search term bị ẩn vĩnh viễn** | **MỚI** | Hệ chưa ghi. Hệ quả: (a) tổng click theo search term **luôn nhỏ hơn** tổng click campaign — đừng đi tìm bug; (b) negative list không bao giờ phủ hết được → mô hình "phrase+exact + negative" của hệ vẫn còn rò rỉ dư; (c) khi Google Ads MCP query GAQL, số liệu `search_term_view` sẽ không cộng bằng `campaign` — phải nói trước cho `monitoring.md` và `keywords/UPDATE.md`. |
| Search terms insights 56 ngày | **MỚI (nhỏ)** | Nhịp tuần của hệ đọc raw terms; insights theme cần ≥56 ngày mới đủ nghĩa → đừng dùng nó ở tuần 1-4. |
| 20 negative list per manager account | **MỚI (nhỏ)** | `NEG_BDS_Account_v1` + versioning trong tương lai: đừng tạo list mới cho mỗi phiên bản, sẽ chạm 20. |

---

## A15. Chính sách — verification, misrepresentation, personalized ads (BĐS)

Nguồn: [Advertiser verification](https://support.google.com/adspolicy/answer/9703665?hl=en) · [Tasks required for Advertiser verification](https://support.google.com/adspolicy/answer/15577076?hl=en) · [Business information requirements](https://support.google.com/adspolicy/answer/12499303) · [Misrepresentation](https://support.google.com/adspolicy/answer/6020955?hl=en) · [Personalized advertising](https://support.google.com/adspolicy/answer/143465?hl=en) (2026-07-28)

**Google dạy — advertiser verification:**
- "**All advertisers will eventually be required** to complete advertiser verification." Bị chọn có thể do: hành vi tài khoản, ngành (Google nêu **financial services**), truy vấn liên quan brand, cách dùng tính năng, hoặc kháng nghị sau khi bị đình chỉ.
- Bước 1 là bộ câu hỏi "**About your business**"; câu trả lời quyết định các bước tiếp: verify identity, verify business operations, hoặc cả hai.
- Tổ chức có thể phải nộp **2 loại giấy tờ**: giấy tờ đăng ký tổ chức + **giấy tờ tùy thân do nhà nước cấp của người đại diện**.
- **Giấy phép hành nghề** bắt buộc nếu thuộc vertical phải đăng ký — Google nêu ví dụ **healthcare, car rental, finance**. **Không nêu real estate.**
- **30 ngày** để nộp câu trả lời, quá hạn thì **tài khoản bị tạm ngưng**. Cập nhật trạng thái mất **5-7 ngày làm việc** (một trang khác ghi "up to 5 business days").
- Thông tin verified xuất hiện trong ad disclosures + **Ads Transparency Center**: tên/tên tổ chức + địa điểm, lịch sử đổi tên, creative, ngày và nơi ad chạy.

**Google dạy — misrepresentation:** 5 nhóm.
- *Unreliable claims*: "Making inaccurate claims or claims that entice the user with an **improbable result**... as the likely outcome" — nêu tường minh cả **investment return claims**.
- *Unclear relevance*: quảng cáo không liên quan đích đến.
- *Misleading representation*: "Making misleading statements, **obscuring, or omitting material information** about your identity, affiliations, or qualifications"; tên doanh nghiệp phải nhận diện đúng.
- *Unacceptable business practices*: mạo nhận endorsement, bán thứ không có, mạo nhận trình độ, **impersonating other brands** → **đình chỉ tài khoản ngay, không cảnh báo trước**.
- *Coordinated deceptive practices* → đình chỉ vĩnh viễn.
- Bắt buộc minh bạch: công bố payment model, **toàn bộ chi phí**, không tạo "false or misleading impression of the cost".

**Google dạy — personalized ads / HEC (housing, employment, credit):**
- Nhóm "Access to Opportunities" (housing/employment/credit) **chỉ áp dụng US và Canada**.
- Áp theo **geography mà ad nhắm tới**, không theo nơi advertiser đặt trụ sở: "they're triggered when your ads target the United States or Canada".
- Bị cấm: gender, age, parental status, marital status, ZIP code. Được phép: **radius (tối thiểu 1 km)**, city, country. Canada được dùng **3 ký tự đầu postal code (FSA)**.
- "**Predefined Google audiences** remain usable for HEC categories" — audience tự dựng thì bị hạn chế rộng hơn.

**So với hệ hiện tại:**

| Điểm | Nhãn | Chi tiết |
|---|---|---|
| HEC không áp dụng VN, áp theo geo nhắm tới; Việt kiều US/CA → tách campaign bỏ age/gender/parental/ZIP | **KHỚP hoàn toàn** | `research` §7 đúng từng chi tiết. |
| HEC: min radius 1 km + predefined Google audiences vẫn dùng được | **MỚI (chi tiết bổ sung)** | Nếu bao giờ chạy campaign nhắm Việt kiều US/CA, hai chi tiết này quyết định campaign còn chạy được hay không. |
| "Cam kết sinh lời X%" → unreliable claims | **KHỚP** | `research` §7 + `campaign-setup.md` §3 đã kiểm copy sạch. Google xác nhận investment return claims nằm trong unreliable claims. |
| Footer pháp nhân/MST/địa chỉ | **KHỚP + có tên policy chính thức** | Google gọi là *misleading representation* ("omitting material information about your identity") và có policy riêng [Business information requirements](https://support.google.com/adspolicy/answer/12499303). Hệ ghi đúng việc phải làm nhưng chưa gán tên policy → khi bị disapproved sẽ khó tra. |
| "Không mạo nhận CĐT" (reseller) | **KHỚP + nâng mức nghiêm trọng** | Google xếp *impersonating other brands* vào **unacceptable business practices = đình chỉ NGAY, không cảnh báo**. Nặng hơn cách hệ đang ghi (chỉ nói "hạn chế"). Sàn phân phối phải cực kỳ cẩn thận với headline kiểu "{Tên dự án} - Giá Gốc CĐT" (playbook §3.1 headline #4) — nếu LP không nói rõ mình là **đơn vị phân phối**, đây là rủi ro đình chỉ ngay, không phải disapproved thường. |
| "Minh bạch toàn bộ chi phí" | **MỚI** | Áp vào BĐS: headline `Giá Từ {Giá từ}` và `Trả Trước Từ {Giá từ}` (playbook §3.2, §3.3) — nếu con số "từ" không thật tồn tại ở căn nào, hoặc bỏ qua phí bắt buộc, đó là "false or misleading impression of the cost". Playbook §3 đã yêu cầu số phải thật; cần thêm ràng buộc **"giá từ" phải là căn thật đang bán, có bằng chứng**. |
| "BĐS VN hay bị yêu cầu xác minh" (`research` §7, `campaign-setup.md` §1.1) | **MÂU THUẪN về NGUỒN, không về hành động** | Không có nguồn Google nào nói real estate là vertical bị nhắm verification. Google nêu healthcare, car rental, finance. **Hành động của hệ (nộp verification trước) vẫn đúng** vì Google nói "all advertisers will eventually be required" — nhưng lý do phải sửa từ "BĐS hay bị yêu cầu" thành "mọi advertiser rồi cũng phải làm, và hạn 30 ngày → tạm ngưng nên làm trước là rẻ nhất". |
| **30 ngày → tạm ngưng tài khoản** | **MỚI — con số vận hành quan trọng** | `campaign-setup.md` §1.1 ghi "3-5 ngày chờ" (thời gian duyệt) nhưng không ghi **deadline 30 ngày dẫn tới tạm ngưng**. Nếu verification request đến giữa lúc đang chạy campaign, đây là đồng hồ đếm ngược sống-chết. Cần vào `monitoring.md` như alert 🔴. |
| Giấy tờ: đăng ký tổ chức + CCCD người đại diện | **KHỚP** | `campaign-setup.md` §1.1.2/§1.1.3 đúng. |

---

# PHẦN B — Google Analytics (GA4) chính thức

Nguồn: [Conversions vs. key events](https://support.google.com/analytics/answer/13965727?hl=en) · [Create Google Ads conversions from GA4 key events](https://support.google.com/analytics/answer/10632359?hl=en) · [Create, edit, archive audiences](https://support.google.com/analytics/answer/9267572?hl=en) · [Select attribution settings](https://support.google.com/analytics/answer/10597962?hl=en) · [Change reporting attribution model for key events](https://support.google.com/analytics/answer/16291112?hl=en) · [Data thresholds](https://support.google.com/analytics/answer/9383630?hl=en) · [BigQuery Export](https://support.google.com/analytics/answer/9358801?hl=en) (2026-07-28)

## B1. Key events vs conversions

**Google dạy:**
- Key event = "an event that measures an action that's particularly important to the success of your business". Bất kỳ event nào cũng có thể mark là key event.
- **Google Ads conversion tạo TỪ GA4 key event nhưng "don't appear in standard Google Analytics reports"** — chúng được đánh giá riêng ở Google Ads hoặc ở mục Advertising của GA4.
- Muốn import 1 event GA4 vào Google Ads, event đó **phải được mark là key event trước**.
- Lợi ích khi tạo Google Ads conversion từ key event: khớp số giữa 2 nền tảng, đo cả kênh non-Google/organic, dùng cho bidding, tạo remarketing audience.
- Google đã hợp nhất định nghĩa 'conversion' giữa Ads và Analytics để giảm lệch số (trước đây "conversions" của GA4 đo khác Google Ads → sinh discrepancy).

**So với hệ hiện tại:**

| Điểm | Nhãn | Chi tiết |
|---|---|---|
| Đúng 3 key event (`generate_lead`, `phone_click`, `zalo_click`), 3 micro không mark | **KHỚP** | `tracking/ga4-setup.md` §2. Lý do hệ đưa ra ("mark key event làm loãng báo cáo conversion") đúng theo cơ chế. |
| Import 3 key event vào Ads = Secondary để chống đếm đúp | **KHỚP** | §4 bước 3. |
| Ghi chú ponytail "có thể bỏ hẳn import GA4, chỉ dùng 3 tag GTM" | **KHỚP + Google cho thêm lý lẽ ngược** | Google nêu 2 lợi ích mà GTM-only KHÔNG có: (a) đo được cả kênh **non-Google/organic** trong cùng conversion, (b) attribution model của GA4. Với hệ BĐS chạy cả Facebook + organic + SEO content, (a) là lợi ích thật. QA nên cân lại: giữ import GA4 nhưng Secondary (như đang viết) là lựa chọn tốt hơn là bỏ. |
| Google Ads conversion không hiện trong standard GA4 report | **MỚI** | Giải thích trước một câu hỏi chắc chắn sẽ xảy ra khi audit: "sao GA4 report không thấy conversion Ads?". Đưa vào `tracking/audit-monthly.md`. |

## B2. Audiences

**Google dạy:**
- Membership duration: **default 30 ngày, tối đa 540 ngày** (18 tháng) tính từ lần cuối user vào audience.
- **Retroactive: "When you create an audience, Analytics adds any users who have met the audience criteria during the last 30 days."** Ngoài 30 ngày đó thì không hồi tố. Populate mất **24-48h** (+1h prepopulate).

**So với hệ hiện tại:**

| Điểm | Nhãn | Chi tiết |
|---|---|---|
| "Audience mới không hồi tố quá 30 ngày — tạo NGAY khi LP live" | **KHỚP chính xác** | `ga4-setup.md` §3 đúng, và kết luận vận hành (tạo ngay, đừng đợi G2) là đúng hệ quả. |
| Window 30/30/30/7/14 của 5 audience | **KHỚP** | Trong giới hạn (max 540). |
| Max 540 ngày | **MỚI (nhỏ)** | Có ích cho BĐS chu kỳ 3-12 tháng: audience nurture dài hạn (ví dụ `xem_bang_gia_180d`) là khả thi về mặt kỹ thuật. Nhưng ngưỡng Display ≥100 user/30 ngày vẫn tính theo **active user**, nên window dài không tự giải quyết vấn đề size. |
| Google Ads cần ≥100 user active/30 ngày | **CHƯA VERIFY LẠI Ở NGUỒN GOOGLE** | `ga4-setup.md` và `research` §9 dùng con số này (nguồn Search Engine Land 12/2025, bên thứ 3). Chưa xác nhận được ở trang Google trong vòng research này → giữ nhưng đánh dấu nguồn 3P. |

## B3. Attribution trong GA4 — ảnh hưởng số import sang Ads

**Google dạy:**
- **Data-driven attribution là model mặc định** và được khuyến nghị; dùng ML đánh giá cả path có và không có conversion, cân theo thời gian tới conversion, device, số lần tương tác, thứ tự exposure, loại creative.
- **Lookback window:** key event thông thường **default 90 ngày** (chọn được 30 hoặc 60). Acquisition key events (`first_open`, `first_visit`) default **30 ngày** (chọn được 7).
- Có thể **đổi reporting attribution model theo từng key event** ([answer/16291112](https://support.google.com/analytics/answer/16291112?hl=en)).

**So với hệ hiện tại:**

| Điểm | Nhãn | Chi tiết |
|---|---|---|
| Attribution settings của GA4 | **MỚI — lỗ hổng thật trong `ga4-setup.md`** | File `tracking/ga4-setup.md` **không cấu hình attribution settings ở đâu cả**: không set model, không set lookback window. Mặc định 90 ngày là **may mà khớp** với conversion window 90 ngày ở `campaign-setup.md` §1.2.4 — nhưng "may mà khớp" không phải cấu hình. Phải đưa vào §1 bảng cấu hình property: **Attribution model = Data-driven, key event lookback = 90 ngày** (khớp Ads), và ghi lý do. |
| Đổi model theo từng key event | **MỚI** | Có thể để `generate_lead` dùng data-driven mà `phone_click` dùng last-click nếu cần đối chiếu — nhưng ponytail: chưa cần, chỉ ghi là có. |
| `campaign-setup.md` §1.2.5 "Mô hình phân bổ = Dựa trên dữ liệu (mặc định)" | **KHỚP** | Đúng phía Google Ads. Nhưng nhớ: **model GA4 và model Google Ads là hai cấu hình riêng** — sửa một bên không đổi bên kia. Chưa được nói ở đâu trong hệ. |

## B4. Data thresholding & consent

**Google dạy:**
- Threshold bật khi report/exploration chứa **demographic data** hoặc audience dựng trên demographic signal; và khi search query không đủ user.
- Mục đích: chống suy ra danh tính/thông tin nhạy cảm của user cá nhân.
- Cách né: **mở rộng date range**; hoặc **export BigQuery** — nhưng "Analytics doesn't export data from Google signals to BigQuery" nên số event sẽ khác giữa GA4 và BigQuery.

**So với hệ hiện tại:**

| Điểm | Nhãn | Chi tiết |
|---|---|---|
| "Google signals ON. Đánh đổi: data thresholding khi số nhỏ" | **KHỚP** | `ga4-setup.md` §1 ghi đúng cả cơ chế lẫn đánh đổi. |
| Consent Mode EEA/UK denied, VN granted | **KHỚP về logic** | Google không có toggle "EU signals" — `ga4-setup.md` đã tự nhận ra và giải thích đúng. |
| BigQuery không nhận data Google signals | **MỚI** | Nếu sau này bật BigQuery để né threshold, số sẽ **không khớp** GA4 UI. Phải biết trước, không thì tưởng pipeline lỗi. |

## B5. BigQuery export

**Google dạy:** 3 loại export (Daily, Fresh Daily, Streaming). Property standard giới hạn **1 triệu event/ngày** cho Daily export. Streaming tính phí **$0,05/GB**. Ưu điểm: sở hữu dữ liệu, quản quyền bằng BigQuery ACL.

| Điểm | Nhãn | Chi tiết |
|---|---|---|
| "BigQuery export ❌ chưa cần ở quy mô này" | **KHỚP** | 1 LP BĐS còn rất xa 1 triệu event/ngày; free tier dư. Quyết định hoãn là đúng ponytail. **Điều kiện mở lại (nên ghi thêm):** khi cần né thresholding cho phân tích demographic, hoặc khi cần join GA4 × Keap × Ads ở cấp row. |

---

# PHẦN C — Chứng chỉ & khóa học Skillshop

## C1. Thông tin chung & tình trạng truy cập nguồn

**Tình trạng truy cập:** mọi URL `skillshop.docebosaas.com/learn/courses/...` là **JS shell — không fetch được nội dung** (đã xác nhận: `skillshop.exceedlms.com/student/path/645553` redirect sang docebosaas; trang catalog `exceedlms` trả "No results returned"). → **Syllabus của mọi chứng chỉ dưới đây là nguồn bên thứ 3, tin cậy THẤP, đánh dấu `[3P]`.** Mọi điểm kiến thức đã được học lại từ tài liệu Google chính thức và ghi nguồn Google ở Phần A/B.

**Thông tin chứng chỉ — nguồn Google chính thức** ([About Google Ads certifications](https://support.google.com/google-ads/answer/9702955?hl=en), [Skillshop Help](https://support.google.com/skillshop/answer/14744470?hl=en), 2026-07-28):
- Pass score **80%**; thời gian **75 phút**; hiệu lực **1 năm**.
- Chứng chỉ **tính vào Google Partner badge**: Google Ads Search, Display, Video, Shopping ads, Google Ads Apps. "The Google Ads **Professional** certifications **don't** count toward the Partners badge."
- Trang Skillshop chính thức mô tả danh mục là: "get certified in **Search, Display, Video, Shopping Ads, Apps and Measurement**".
- `[3P]` bổ sung: 2026 có thêm AI-Powered Performance Ads, AI-Powered Shopping Ads, Creative, Grow Offline Sales, Google Analytics, Search Ads 360 — tổng ~9-10 cert active. Format 50 câu multiple-choice.

## C2. NHÓM SÂU NHẤT

### C2.1 Google Ads Search Certification

`[3P]` Syllabus 5 domain: (1) Fundamentals — ecosystem, account structure, campaign settings, đấu giá Search; (2) Keywords — research, match type, search terms report, negative keywords, Quality Score; (3) Ads — RSA, ad copy best practices, assets; (4) Bidding — manual, Smart Bidding, tCPA, tROAS, Maximize Conversions, bid adjustments; (5) Audiences — in-market, affinity, custom, RLSA, Customer Match, PMax.

Học từ Google chính thức: §A2 (Ad Strength), §A3 (pinning), §A4 (account structure), §A5 (match type), §A6 (Smart Bidding), §A14 (search terms, negative, limits).

| Điểm | Nhãn |
|---|---|
| Quality Score = 3 thành phần (expected CTR, ad relevance, landing page experience), thang 1-10, là **diagnostic tool** | **KHỚP** — nhưng hệ chưa ghi ở đâu rằng QS là diagnostic, không phải input đấu giá trực tiếp. Xem [Quality Score](https://support.google.com/google-ads/answer/6167118?hl=en). Có skill `google-ads-quality-score` sẵn — đối chiếu skill đó với định nghĩa này. |
| Audience trên Search: RLSA, Customer Match, in-market, affinity, custom | **MỚI** | Hệ dùng audience **chỉ cho remarketing Display/Demand Gen** (`ga4-setup.md` §3). Google dạy dùng audience **ngay trên Search** (observation mode để đọc dữ liệu, targeting để siết). Với BĐS: `xem_bang_gia_30d` làm **observation** trên Search Brand để thấy chênh CVR — miễn phí, không đổi phân phối. Đây là món rẻ nhất chưa dùng. |
| Bid adjustments | **KHỚP (hệ cố tình không dùng)** | Google dạy bid adjustment; hệ chạy Max Clicks + cap rồi lên smart bidding (smart bidding vô hiệu hoá phần lớn bid adjustment trừ device/... ). Không cần vá. |

### C2.2 Google Ads Measurement Certification

`[3P]` Syllabus: conversion tracking, attribution models, campaign optimization, KPI; financial/strategic/marketing objectives; quan hệ Google Ads ↔ Google Analytics và **các nguồn lệch số (discrepancies)**.

Học từ Google chính thức: §A10 (ECL/offline/Data Manager), §A8 (lead gen measurement), Phần B (GA4).

| Điểm | Nhãn |
|---|---|
| Ads ↔ GA4 discrepancy là chủ đề chính thức có trong giáo trình | **MỚI** | Hệ có `tracking/audit-monthly.md` nhưng chưa có **bảng nguyên nhân lệch số** chuẩn. Nguyên nhân đã xác nhận trong vòng research này: (a) Google Ads conversion không hiện trong standard GA4 report (§B1); (b) attribution model GA4 và Ads là 2 cấu hình riêng (§B3); (c) lookback/conversion window khác nhau (§B3 vs §A10); (d) data thresholding GA4 (§B4); (e) search terms report bỏ term ít volume (§A14); (f) múi giờ property vs tài khoản Ads (`ga4-setup.md` §1 đã lo). Bảng này nên nằm trong `tracking/audit-monthly.md`. |
| Google đã hợp nhất định nghĩa conversion Ads↔GA4 | **MỚI** | Giảm bớt một nguồn lệch cũ. Không cần hành động, cần biết. |

### C2.3 AI-Powered Performance Ads Certification (courses/8510)

`[3P]` Syllabus: nền tảng AI/ML trong ads; Smart Bidding (conversion-based và value-based); campaign optimization + KPI; targeting & segmentation bằng AI insight; measurement & reporting. Mục tiêu Google công bố: "describe the importance of AI throughout Google Ads campaigns and **prepare an AI automation strategy** that aligns to your business goals".

Học từ Google chính thức: §A5 (broad + Smart Bidding là một cặp), §A6, §A7 (value-based), §A11 (AI Max), §A12 (PMax), §A13 (Demand Gen), §A8 (Data Strength/first-party data).

| Điểm | Nhãn |
|---|---|
| **Data Strength** — pillar mới của Google | **MỚI** | [Data Strength](https://support.google.com/google-ads/answer/16517525?hl=en): "a foundational pillar of modern marketing, centered on building a trusted decision engine with **first-party data**". 4 hành động: connect data sources (Google Tag/GTM, Analytics, **CRM**) → maximize signals (customer data, purchase data, **consent signals**) → activate Google AI (Smart Bidding, PMax, Customer Match) → prove ROI (experiments, MMM). Hệ đang làm 3/4 (thiếu prove ROI: incrementality/experiments — `research` §8 có ở nhịp **quý**). Đáng ghi vì đây là khung Google dùng để chấm điểm sự "sẵn sàng AI" của tài khoản. |
| Value-based bidding là đích của lộ trình AI | **KHỚP** | `campaign-setup.md` §4.4 đã có nhánh tROAS. §A7 cấp thêm điều kiện định lượng. |
| "AI automation strategy" thay vì "bật/tắt từng tính năng" | **MỚI (khung tư duy)** | Giáo trình dạy lập **chiến lược automation** có gate, không phải bật hết. Hệ đã có gate G0-G5 — chính là cái Google gọi là automation strategy. Điểm hệ thiếu: gate nào **mở khoá tính năng AI nào** thì chưa được viết như một bảng. Nên có. |

### C2.4 Grow Offline Sales Certification (courses/8542)

`[3P]` Syllabus: các approach offline sales; **store visits measurement** (bao gồm panel Google Opinion Rewards để validate store visit); local inventory feed & tần suất cập nhật; PMax for store goals (input thủ công cần cung cấp); store-centric vs omnichannel approach.

| Điểm | Nhãn |
|---|---|
| Phần lớn nội dung là **retail/store visits — KHÔNG áp dụng BĐS VN** | **KHỚP (không cần vá)** | Store visits conversion cần Google Business Profile đã verify + đủ volume; `campaign-setup.md` §3.4 đã xử lý đúng (chưa có GBP verified → bỏ qua, không tạo GBP ảo). Thêm một lý do: **store visits/store sales conversion không tương thích search terms report** (§A14) → nếu bật, mất công cụ vận hành số 1 của hệ. Ghi vào doc như lý do chống chỉ định. |
| Nhưng "offline sales" theo nghĩa **offline conversion import** thì là xương sống hệ | **KHỚP** | Nội dung đó nằm ở §A10 và cert Measurement, không phải cert này. Kết luận cho main agent: **cert này giá trị thấp hơn dự đoán ban đầu** — nó là cert *retail in-store*, không phải cert *offline conversion*. Không cần đào vòng 2. |
| "Nhà mẫu / văn phòng bán hàng" như một store | **MỚI (ý tưởng, chưa verify)** | Về lý thuyết có thể coi nhà mẫu là địa điểm và đo lượt tới bằng store visits. Thực tế VN: cần GBP verified, volume đủ, và độ chính xác thấp. **Không khuyến nghị** ở quy mô 30-150tr₫. |

### C2.5 Explore Search Ads Optimization Best Practices (courses/7674)

Không có syllabus 3P riêng đáng tin. Khóa này tương ứng bộ [Google Ads Best Practices](https://support.google.com/google-ads/answer/6154846?hl=en) — đã học trực tiếp: ABCs of Account Structure (§A4), Create effective Search ads (§A2/A3), Reaching the right customers on Search (§A4/A5), Finding success with Smart Bidding (§A6), Data Strength (§C2.3).

**Đây là chỗ ra MÂU THUẪN đậm nhất với `playbook/campaign-setup.md` §4 và `research` §8.** Tổng hợp lại thành một bảng phân xử duy nhất:

| Google khuyên | Hệ đã chọn | Ai đúng, trong hoàn cảnh nào |
|---|---|---|
| Consolidate ad group, broad match là chính | STAG mịn, Phrase+Exact only <20tr | **Cả hai.** Google giả định Smart Bidding đang chạy; hệ ngày 1 chạy Max Clicks. Điều kiện chuyển đổi chính là gate của hệ. Cần sửa **giọng điệu** research §3 từ lệnh cấm → gate. |
| AI Max + keywordless cho reach lớn nhất | AI Max sau G4 ≥6 tuần | **Hệ đúng cho ngân sách nhỏ**, và có thêm chỗ dựa: AI Max search term matching **không chạy với Manual CPC** (§A11) → không thể bật sớm dù muốn. |
| Auto-apply recommendations để "optimize efficiently" | (chưa có chính sách) | **Hệ phải chọn TẮT** và ghi ra. Auto-apply chỉ có cấp account, có thể xóa negative và bật Display expansion (§A1). Đây là MỚI, không phải mâu thuẫn — hệ chưa có ý kiến. |
| Optimization score cao = tài khoản tốt | (chưa có chính sách) | **Hệ nên chống chỉ định**: dismiss cũng làm tăng score (§A1), score không vào Quality Score. |
| Ad Strength Excellent (+15% conv) | Ghim H1 → hạ Ad Strength | **Hệ đúng có điều kiện**: Google chấp nhận hybrid pin 1-2 headline (§A3). Nhưng ≥6 sitelink thì hệ nên vá (§A2). |
| ≥15 conv/30 ngày **cấp account** cho lead-gen goal | ≥15 **cấp campaign** cho Max Conversions | Hệ khắt khe hơn → an toàn nhưng chậm. QA chốt (§A7). |
| Conversion delay ≤7 ngày | Conversion window 90 ngày | **Hai việc khác nhau**, không mâu thuẫn — nhưng sinh ra **SLA 7 ngày cho sales tag `Lead_Contactable`** mà hệ chưa có (§A8). |

### C2.6 AI-Powered Search Ads track — Foundations + Intermediate, Practitioners + Strategists

4 khóa: Foundations for Practitioners (16507), Foundations for Strategists (10578), Intermediate for Strategists & Practitioners (11288). `[3P]` không có syllabus công khai đáng tin cho từng khóa (chỉ có tên khóa) → **không bịa syllabus**. Dưới đây là nội dung học từ tài liệu Google chính thức, xếp theo bậc mà Google trình bày trong bộ best practices, cộng phân biệt góc nhìn theo tên khóa (**suy luận từ tên khóa, không phải syllabus xác nhận — đánh dấu ⚠️**).

**Bậc Foundations (Google dạy — nguồn ở §A4/A5/A11):**
1. Broad match và Smart Bidding là **một cặp không tách rời**. Broad là match type duy nhất dùng **hết** signal có sẵn; nhưng không có Smart Bidding thì bid không phản ánh signal → đốt tiền.
2. Query matching bằng AI **thay thế** việc quản match type thủ công: AI Max search term matching + keywordless.
3. RSA asset automation: 15 headline để AI có tổ hợp; pinning là thứ **giới hạn** AI.
4. Account structure: themed ad group, bỏ SKAG, bỏ device segmentation.

**Bậc Intermediate ⚠️ (những thứ Google publish ở tầng sâu hơn, đúng tầm hệ khi qua G3):**
1. **Value-based bidding** (§A7) — 2+ unique non-zero value, proxy value được phép, đừng dùng value 0.
2. **Conversion Value Rules** (§A8) — điều chỉnh giá trị theo geo/device/audience mà không sửa tag.
3. **Portfolio bidding** — `research` §4 đã có (gộp campaign nhỏ cùng CPA mục tiêu, không gộp brand với generic).
4. **Seasonality adjustments + seasonal budget adjustments** (§A6) — hai công cụ khác nhau, hệ chỉ biết một.
5. **Data exclusions** ⚠️ — chưa fetch được trang Google riêng trong vòng này. Đây là công cụ nói cho Smart Bidding "khoảng thời gian này conversion tracking bị hỏng, đừng học". **Cực kỳ liên quan hệ**: `monitoring.md` có alert "Conversion = 0 trong 4h có spend"; nếu tracking gãy 1 ngày mà không khai data exclusion, Smart Bidding học rằng traffic đó không convert và sẽ tránh nó hàng tuần sau. **Chưa đào — để vòng 2.**
6. **Experiments / one-click experiments** — Google nói dùng experiments để test bid strategy thay vì đổi thẳng; `research` §8 có "incrementality test" ở nhịp quý nhưng chưa có quy trình campaign experiment.
7. **Insights page** ⚠️ — chưa đào, để vòng 2.

**Góc Practitioners vs Strategists ⚠️ (suy luận từ tên khóa):** practitioners = thao tác trong tài khoản (bật gì, cấu hình gì, đọc report nào); strategists = business case, đo giá trị, tổ chức tài khoản theo mục tiêu kinh doanh. Với hệ này: `playbook/campaign-setup.md` = tài liệu practitioner; `playbook/customer-journey-plan.md` + `PLAN.md` = tài liệu strategist. **Cấu trúc doc của hệ đã tự nhiên khớp phân tầng này** — không cần đổi.

**Lộ trình adoption AI-first cho hệ ngân sách nhỏ (<30 conv/tháng) — kết luận đề xuất:**

| Bậc | Điều kiện | Bật gì | Nguồn |
|---|---|---|---|
| 0 | Ngày 1, 0 conversion | Max Clicks + cap · Phrase+Exact · **auto-apply TẮT hết** · ACA TẮT | §A1, §A5 |
| 1 | ≥15 conv/30 ngày cấp campaign + contact rate >50% | Maximize Conversions (không tCPA) · đảo primary sang `Lead_Contactable` | §A7, §A8 |
| 2 | ≥30 conv/30 ngày + ECL chạy thật | tCPA · **giờ mới** test 1 ad group broad (đủ điều kiện "critical to use Smart Bidding with broad match") | §A5 |
| 3 | Giá trị lead phân tầng chảy về, 2+ non-zero value | Maximize conversion value / tROAS · Conversion Value Rules | §A7, §A8 |
| 4 | Search ổn định ≥6 tuần ở bậc 3 | **AI Max** — bắt buộc conversion-based bidding; TẮT final URL expansion (giữ pinning + không lạc trang) · rà negative ↔ brand inclusions trước | §A11 |
| 5 | Đã ở bậc 4, có creative 3 tỷ lệ | PMax / Demand Gen | §A12, §A13 |

Điểm mấu chốt Google dạy mà hệ nên nội hoá: **thứ mở khoá AI không phải ngân sách, mà là dữ liệu conversion chất lượng.** Vì vậy ECL không phải "việc phải làm ở tuần 8" — nó là điều kiện tiên quyết cho toàn bộ nhánh AI.

### C2.7 Google Analytics Certification (courses/18609) + "Measure Your Marketing with Google Analytics" (courses/10168)

`[3P]` Syllabus: GA4 interface, explorations, audiences, conversions/key events, attribution, data streams; **consent mode** — GA4 điều chỉnh thu thập theo consent signal; vai trò **Google Signals** trong đo lường cross-device tôn trọng quyền riêng tư. 50 câu / 75 phút / 80% / hiệu lực 12 tháng.

Học từ Google chính thức: toàn bộ **Phần B**. Tổng kết đối chiếu với `tracking/ga4-setup.md`:

| Điểm | Nhãn |
|---|---|
| 3 key event, 6 custom dimension, retroactive 30 ngày, thresholding tradeoff, BigQuery hoãn | **KHỚP** (§B1, B2, B4, B5) |
| **Attribution settings chưa được cấu hình** | **MỚI — lỗ hổng cần vá** (§B3) |
| 5 audience có đúng chuẩn Google dạy không? | **KHỚP** — cả 5 đều dùng cơ chế Google hỗ trợ: event-based condition, session-scoped metric, temporary exclude, membership duration trong giới hạn. Riêng #5 `da_generate_lead_14d` "chỉ dùng để EXCLUDE" là **đúng best practice** Google (Demand Gen/PMax best practices đều khuyên loại trừ converter). #4 dùng "Temporarily exclude" thay "Permanently" là chi tiết đúng và tinh. |
| Explorations | **KHỚP** | 3 exploration (Funnel, Free form ×2) là đúng loại Google dạy, và tối thiểu đủ dùng. |
| Data streams | **KHỚP** | 1 web stream, 1 property. |

**Bổ sung từ khóa "Measure Your Marketing with Google Analytics" (khóa nền trong learning path GA cert):** phần khóa này phủ mà cert không nhấn là **liên kết Ads↔GA4 và tại sao 2 nguồn LỆCH số**. Học từ Google chính thức: [Data discrepancies: Factors and troubleshooting](https://support.google.com/google-ads/answer/7457111?hl=en) (2026-07-28).

**Google dạy — 5 nguyên nhân lệch số Google Ads vs GA4:**
1. **Ngày quy về khác nhau (conversion delay):** Google Ads quy conversion về **ngày CLICK**; GA4 quy về **ngày CONVERSION**. Click 19/7 → submit 20/7: Ads ghi 19/7, GA4 ghi 20/7. Đây là nguyên nhân số 1 và **không thể sửa** — chỉ có thể hiểu.
2. **Attribution model khác:** GA4 default data-driven; Google Ads dùng model ad-centric.
3. **Invalid click:** site analytics ghi **mọi** traffic kể cả click Google Ads đã loại là invalid.
4. **Cột đếm khác:** cột `All conversions` của Ads gồm cả action đặt **Secondary** và **view-through conversions**; cột `Conversions` thì không. So sai cột = lệch to.
5. **Xử lý chậm 24-48h** — đừng so số trước 48h.

**Tin cái nào cho việc gì — kết luận đề xuất:**

| Câu hỏi | Tin nguồn nào | Vì sao |
|---|---|---|
| "Keyword/campaign nào ra lead?" (quyết định bid, negative, budget) | **Google Ads** | Quy về ngày click + có click ID. Đây là hệ quy chiếu mà bidding học theo. |
| "LP hỏng ở bước nào?" (funnel, CVR, form abandonment) | **GA4** | Có funnel exploration, custom dimension (`ngan_sach`, `muc_dich`, `form_id`). |
| "Tổng bao nhiêu lead thật tháng này?" | **CRM (Keap)** | Nguồn sự thật duy nhất. Ads và GA4 đều là mô hình. |
| "Contact rate, CPL qualified" | **CRM**, đối chiếu Ads | KPI chính của hệ (`PLAN.md` §0.4) nằm ở CRM, không ở Ads/GA4. |

| Điểm | Nhãn | Chi tiết |
|---|---|---|
| Hệ import 3 web conversion từ GA4 vào Ads (Secondary) | **KHỚP + có lý do mới để giữ Secondary** | Nếu để Primary, chúng vào cột `Conversions` cùng 3 tag GTM → đếm đúp (hệ đã biết). **Điều hệ chưa biết:** kể cả khi đặt Secondary, chúng **vẫn** vào cột `All conversions`. Nghĩa là báo cáo tuần phải nói rõ đang đọc cột nào. `monitoring.md` §7 mẫu tin ghi "Lead: 3 raw" — phải chốt đó là cột `Conversions` hay `All conversions`. |
| Nguyên tắc "ngày click vs ngày conversion" | **MỚI** | Chưa có ở đâu trong hệ. Hệ quả trực tiếp: `monitoring.md` báo cáo Daily Close 20:00 so "Spend hôm nay vs Lead hôm nay" — với BĐS chu kỳ dài, **lead hôm nay có thể thuộc click tuần trước**. Số CPL theo ngày của hệ về bản chất là **nhiễu**, chỉ có nghĩa ở mức 7-30 ngày. Cần một dòng cảnh báo trong `monitoring.md`. |

### C2.8 "Achieve Your Goals with Performance Max" (courses/11139)

Nguồn Google chính thức: [About Performance Max](https://support.google.com/google-ads/answer/10724817?hl=en) · [How PMax interacts with other campaigns](https://support.google.com/google-ads/answer/13810170?hl=en) · [PMax best practices for lead generation](https://support.google.com/google-ads/answer/13775965?hl=en) · [Ad group & asset group prioritization](https://support.google.com/google-ads/answer/2756257?hl=en) · [Account-level negative keywords](https://support.google.com/google-ads/answer/11396330) (2026-07-28)

**Tách rõ 2 loại nội dung như yêu cầu.**

#### (a) Setup PMax ĐÚNG — Google dạy gì (MỚI, hữu ích cho ngày qua G4)

| Thành phần | Google dạy chính xác điều gì |
|---|---|
| **Asset group** | "a collection of creatives centered on a **theme or target audience**". Google dùng nó để **sinh** ad. → 1 asset group = 1 dự án BĐS (không phải 1 asset group cho cả sàn). |
| **Audience signals** | **Là GỢI Ý, không phải targeting.** "function as performance hints rather than strict targeting controls... **don't restrict ad delivery**". → Đây là điểm bị hiểu sai nhiều nhất: đưa audience signal vào KHÔNG giới hạn PMax chỉ chạy trong audience đó. Muốn giới hạn thật thì phải dùng negative/exclusion. |
| **Search themes** | "Search themes have the **same prioritization as phrase match and broad match** keywords." → Search theme **không** đè được exact keyword của Search campaign. |
| **Ưu tiên vs Search campaign** | "If a search query matches to an **exact match keyword** in your Search campaign, Google Ads **prioritizes the Search campaign** over Performance Max." Exact keyword **identical** với search term luôn thắng. → **Đây là lá chắn chống cannibalize brand mà hệ đang lo** (`research` §1): vì `research` §3 quy định **tên dự án LUÔN Exact**, brand search sẽ tự động về Search campaign, không bị PMax ăn. Điều kiện: keyword phải **exact và identical**, không phải phrase. |
| **Brand exclusions** | Có ở **cấp campaign** — chặn ad hiện trên term brand chỉ định. |
| **Campaign-level negative keywords** | Có ở cấp campaign (trần 10.000 — §A14). |
| **Account-level negatives** | Tự áp cho PMax (§A12) — 216 negative của hệ có thể phủ PMax nếu đặt ở account level. |
| **URL expansion** | Khi bật, Google có thể **thay Final URL** bằng landing page khác + tự sinh headline/description theo intent. → **Phải TẮT** với BĐS: LP dự án A không được thay bằng LP dự án B (mất message match, mất chính sách giá đúng). |
| **Reporting** | Asset-level metrics, asset group report, channel performance, placement report, search terms report (§A14 xác nhận PMax **có** search terms report), tích hợp GA. |

**Checklist dựng PMax chuẩn cho BĐS (đề xuất, dùng khi qua G4):**
1. Conversion goal = `Qualified lead` / `Converted lead` (category chuẩn Google), **không** phải form raw. Goal phải có ≥15 conv/30 ngày.
2. Bidding: Maximize conversion value (+tROAS khi có giá trị phân tầng); nếu chỉ cần volume thì Maximize conversions.
3. **1 asset group / 1 dự án.** Asset: ≥15 headline + 5 description, ≥7 image (3 landscape + 3 square + 1 portrait), ≥1 video. Nhắm Ad Strength Excellent (+6%).
4. **TẮT URL expansion.** Final URL = LP dự án đó.
5. Brand exclusions: tên các CĐT/dự án **không** phân phối (chống ăn brand người khác) + brand của chính mình nếu muốn brand về Search.
6. Negative: áp `NEG_BDS_Account_v1` ngay ngày 1 (account-level để tự phủ) + negative campaign-level.
7. Account-level placement exclusion: loại `App categories` / `Games`.
8. Audience signal: `xem_bang_gia_30d`, `da_generate_lead_14d`(để **loại trừ**), Customer Match list khách đã mua — nhớ đây chỉ là **gợi ý**.
9. Search themes: chỉ theme sát dự án; biết rằng nó ở tầng phrase/broad, không đè exact.
10. Giữ **tên dự án ở Exact** trong Search campaign → brand không bị PMax lấy.
11. Learning 1-2 tuần (tới 6 tuần nếu volume thấp) — không đụng gì trong thời gian đó.
12. Đọc search terms report + placement report tuần đầu, cắt ngay app/game/parked domain.

#### (b) Marketing pitch — giữ nguyên gate của hệ

| Google nói | Đánh giá |
|---|---|
| PMax là "goal-based campaign type" truy cập **toàn bộ** inventory Google qua 1 campaign; dùng khi "maximizing performance without restricting ad placements" | **Pitch.** "Không giới hạn placement" chính xác là điều BĐS lead gen **không** muốn: `research` §1 đã ghi PMax tự tìm lead rác từ inventory rẻ (app game, parked domain). |
| PMax "complements Search" | **Đúng nhưng có điều kiện** — chỉ đúng khi brand đã ở Exact. Nếu không, cannibalize là thật. |
| Google không nêu ngưỡng conversion tối thiểu để **bật** PMax (chỉ nêu ≥15 conv cho goal) | **Gate của hệ khắt khe hơn và nên giữ:** G4 = ECL chạy thật + 30 lead **qualified**/tháng. Lý do: PMax tối ưu theo signal được đưa vào; đưa vào signal rác thì nó mua rác rất hiệu quả. Google không nói câu này, nhưng chính Google nói "power it with **great data**" và "use offline conversion import or enhanced conversions to correctly value conversions" — tức Google **cũng** coi dữ liệu chất lượng là tiền đề, chỉ không đặt thành gate. |

**Đối chiếu `playbook/customer-journey-plan.md` §3 — dòng PMax 8% ở kịch bản 150tr:**
`campaign-setup.md` §5.1 phân bổ `PMax_FeedLess` = 400.000₫/ngày trên tổng 5.000.000₫/ngày = **8%** — khớp §3. Nhận xét: 400k₫/ngày (~$15/ngày) cho một campaign chạy trên **6 kênh** là rất mỏng. Google không publish ngưỡng ngân sách PMax, nhưng so sánh gần nhất là Demand Gen ($100+/ngày, §A13) và PMax phủ nhiều kênh hơn. **Đề xuất QA:** ở 150tr, thay vì rải 8% cho PMax, cân nhắc (a) dồn vào 1 asset group / 1 dự án duy nhất để có mật độ, hoặc (b) hoãn PMax thêm một bậc và dùng phần đó cho Demand Gen remarketing (nơi có audience thật). Đây là quyết định chiến lược, không phải sửa doc.

| Điểm | Nhãn |
|---|---|
| Exact match keyword thắng PMax → lá chắn chống cannibalize | **MỚI — quan trọng, giải toả một lo ngại của hệ** |
| Audience signals chỉ là gợi ý, không giới hạn phân phối | **MỚI** — dễ hiểu sai nhất |
| Search themes ở tầng phrase/broad, không đè exact | **MỚI** |
| URL expansion phải tắt | **MỚI** (`campaign-setup.md` §5.3 đã ghi tắt final URL expansion cho AI Max; **chưa** ghi cho PMax) |
| Gate G4 chặt hơn Google | **KHỚP — giữ nguyên** |
| PMax 8% ở 150tr có thể quá mỏng | **MỚI (đề xuất chiến lược)** |

### C2.9 Privacy & Durable Measurement — "Privacy Resource Hub" (courses/13993) + learning plan "Privacy for Agencies and Partners"

Nguồn Google chính thức: [About consent mode](https://support.google.com/google-ads/answer/10000067?hl=en) · [Consent mode reference](https://support.google.com/google-ads/answer/13802165?hl=en) · [About consent mode modeling](https://support.google.com/google-ads/answer/10548233) · [Updates to consent mode for EEA traffic](https://support.google.com/google-ads/answer/13695607?hl=en) · [About enhanced conversions](https://support.google.com/google-ads/answer/9888656?hl=en) · [Set up enhanced conversions for web using the Google tag](https://support.google.com/google-ads/answer/13258081?hl=en) (2026-07-28)

**Google dạy — 7 tham số consent mode:**

| Tham số | Điều khiển gì |
|---|---|
| `ad_storage` | "storage (such as cookies) **related to advertising**" |
| `analytics_storage` | "storage related to **analytics** e.g. visit duration" |
| `ad_user_data` | "consent for **sending user data related to advertising to Google**. Required for measurement use cases, such as **enhanced conversions** and tag-based conversion tracking" |
| `ad_personalization` | "consent for **personalized advertising**" |
| `functionality_storage` | storage phục vụ chức năng site (ví dụ language) |
| `personalization_storage` | storage cho personalization (ví dụ video recommendations) |
| `security_storage` | storage cho bảo mật, chống gian lận |

- Khi `denied` hoặc chưa set: IP bị truncate, không đọc/ghi cookie, **cookieless ping** thay cho tracking thường.
- EEA: "you **must** collect consent... from end users based in the **EEA** and share consent signals with Google" để tiếp tục dùng tag cho measurement + ad personalization + remarketing.
- **Modeled conversions — điều kiện định lượng:** (1) đã triển khai đúng consent mode **hoặc** IAB TCF v2.0; (2) **≥700 ad click/7 ngày, tính riêng theo TỪNG cặp quốc gia × domain grouping**. Trang [About consent mode modeling](https://support.google.com/google-ads/answer/10548233) **không nêu giới hạn vùng** — chỉ nêu ngày ra mắt (4/2021) và 2 điều kiện trên.
- Không có consent mode + user từ chối → "experience a **gap in their measurement** and lose visibility into user paths... no longer able to directly tie users' ad interactions to conversions."
- Enhanced conversions: gửi first-party data đã hash để **grounding** measurement thay vì phụ thuộc Click ID (§A8, §A10) — Google định vị đây là giải pháp "durable measurement".

**Trả lời câu hỏi trọng tâm: KHÔNG có consent mode thì hệ mất gì ở VN?**

| Điều | Trả lời | Độ chắc chắn |
|---|---|---|
| Có bắt buộc consent mode ở VN? | **Không.** Yêu cầu bắt buộc của Google gắn với **user ở EEA/UK**. `tracking/ga4-setup.md` đã xử lý đúng bằng cách không thu dữ liệu quảng cáo của người EEA/UK (Consent Mode denied cho EEA + campaign Location=Vietnam, Presence). | Cao — trích trực tiếp |
| Mất modeled conversions không? | **Về nguyên tắc: có rủi ro mất.** Điều kiện #1 của modeling là "correctly implemented consent mode **or** TCF v2.0". Hệ có Consent Mode ở LP (`lp-requirements.md` §1.1) với VN = `granted` → đây **là** một triển khai consent mode, nên có thể vẫn đủ điều kiện. Nhưng điều kiện #2 (**≥700 click/7 ngày cho VN**) thì hệ **KHÔNG đạt**: 30tr₫/tháng ≈ 10-38 click/ngày ≈ 70-266 click/7 ngày. → **Kết luận: ở quy mô hiện tại hệ không đủ ngưỡng modeling bất kể consent mode làm thế nào.** Điều này thực ra là tin tốt: consent mode không phải đòn bẩy cho hệ, ECL mới là. | Cao — cả 2 điều kiện đều trích được |
| Trang modeling có nói modeling chỉ cho EEA? | **KHÔNG nói.** Trang không nêu giới hạn vùng. Nhưng vì consent-denied hầu như chỉ xảy ra ở nơi có CMP (EEA/UK), consent-mode modeling **trên thực tế** là hiện tượng EEA. Ở VN với consent `granted`, không có gap để mô hình hoá. | Trung bình — suy luận, không phải trích |
| Nghị định 13 / PDPL VN thì mức consent nào là đủ? | **Ngoài phạm vi tài liệu Google** — Google không phát biểu về luật VN. `ga4-setup.md` đặt VN = `granted` là quyết định pháp lý, không phải quyết định kỹ thuật. **Không đủ cơ sở để hệ tự phán** → cần ý kiến pháp lý, ghi vào khoảng trống. Điều Google **có** nói và áp dụng được: `ad_user_data` là tham số **bắt buộc granted** cho enhanced conversions — nếu vì lý do pháp lý VN mà set `ad_user_data=denied`, **ECL sẽ không hoạt động**. Đây là ràng buộc kỹ thuật cần biết trước khi ra quyết định pháp lý. | Cao cho phần Google |

**Chuẩn hoá & hash user-provided data — kiểm `tracking/ecl-keap-pipeline.md`:**

Google dạy (từ [enhanced conversions setup](https://support.google.com/google-ads/answer/13258081?hl=en) + [Google Ads API docs](https://developers.google.com/google-ads/api/docs/conversions/upload-offline)):
1. Xoá whitespace **đầu và cuối**; chuyển **lowercase**; phone theo **E.164**; hash **SHA-256**.
2. **Riêng gmail.com / googlemail.com: xoá mọi dấu `.` trong phần username, và xoá phần `+suffix`** — TRƯỚC khi hash.
3. Có thể gửi **chưa hash** để Google tự normalize+hash, hoặc gửi đã hash (thì phải tự normalize đúng).

| Điểm | Nhãn | Chi tiết |
|---|---|---|
| Email lowercase, phone `+84`, SHA-256 hex, không hash rỗng, không hash 2 lần | **KHỚP** | `ecl-keap-pipeline.md` §"Chuẩn hoá trước khi hash" đúng, và cảnh báo "sai một bước là match rate = 0" là đúng mức độ nghiêm trọng. |
| **Thiếu luật gmail: xoá dấu `.` và `+suffix`** | **MỚI — làm giảm match rate thật** | Hệ ghi "lowercase → xoá mọi khoảng trắng → SHA-256". Thiếu bước gmail. Ở VN gmail chiếm áp đảo trong lead form → `nguyen.van.a@gmail.com` và `nguyenvana@gmail.com` là **cùng một người** nhưng hash khác nhau. **Đây là bug làm mất match rate, không phải chi tiết nhỏ.** Sửa: nếu domain ∈ {gmail.com, googlemail.com} → xoá mọi `.` trong username + cắt từ `+` tới `@`. |
| "Xoá **mọi** khoảng trắng" (thay vì chỉ đầu/cuối) | **KHỚP trên thực tế** | Google nói xoá leading/trailing; xoá hết cũng cho kết quả giống vì email hợp lệ không có khoảng trắng giữa. Không cần sửa. |
| Có thể gửi chưa hash để Google tự hash | **MỚI (nhỏ)** | Hệ tự hash — đúng và an toàn hơn (không gửi PII thô). Giữ nguyên. Chỉ cần biết là có lựa chọn khác. |

### C2.10 Google Tag / GTM (không có chứng chỉ Skillshop 2026 — học từ tài liệu)

**Xác nhận: Skillshop không còn khóa GTM chính thức** (GTM Fundamentals cũ thuộc Analytics Academy đã đóng). Nguồn chính thống: [GTM Help](https://support.google.com/tagmanager) + [Tag Platform developers](https://developers.google.com/tag-platform). Nguồn cộng đồng uy tín nhất là **Analytics Mania — `[third-party]`, không dùng cho claim "Google dạy"**.

Nguồn dùng: [Google Tag Manager vs. gtag.js](https://support.google.com/tagmanager/answer/7582054?hl=en) · [Client-side vs server-side tagging](https://support.google.com/tagmanager/answer/13387731?hl=en) · [Intro to server-side tagging](https://developers.google.com/tag-platform/tag-manager/server-side/intro) · [Set up the Google tag with gtag.js](https://developers.google.com/tag-platform/gtagjs?hl=en) (2026-07-28)

**(a) Google khuyến nghị gtag trực tiếp hay GTM cho setup như hệ (1 LP + GA4 + Ads conversions)?**

Google dạy:
- **gtag.js một mình** hợp cho: marketer không có dev, dùng CMS, chỉ cần metric mặc định ("page views, clicks and scrolls"). "set up the Google tag once and you're all set".
- **GTM** hợp cho: quản cả tag Google **và third-party**, cần "deploy and modify both tags... **on the fly without editing code**", cần tính năng cộng tác (agency, nhiều người).
- "there is no need to deploy additional code using gtag.js on your site **if Tag Manager is already in use**".
- Có thể bắt đầu bằng Google tag rồi "**migrate your tags to Google Tag Manager at a later date**".

**Kết luận cho hệ: GTM là lựa chọn ĐÚNG, không phải over-engineering.** Lý do theo đúng tiêu chí Google: hệ có **6 custom event** (không phải metric mặc định), có **3 tag third-party** (Clarity, Keap, Facebook nếu chạy), có **nhiều LP dùng chung 1 container**, và người sửa LP ≠ người sửa tracking (`lp-requirements.md` là handoff). Cả 4 điều đều là tiêu chí Google nêu cho GTM. → **KHỚP, không cần vá.**

**(b) Server-side GTM — Google nói khi nào đáng làm?**

Google dạy 3 lợi ích: (1) **Performance** — client chỉ gửi 1 HTTP request/event, server container mới phân phối đi các vendor → ít code, ít request; (2) **Data control** — "full control over the data that is distributed to third parties", che/xoá PII trước khi gửi ra ngoài; (3) **Data quality** — sửa được sai lệch do browser/device, validate event, giảm mất dữ liệu.
Yêu cầu: **cloud environment tự host** server container (GCP App Engine hoặc Cloud Run cho traffic lớn). Google **không** nêu chi phí cụ thể.
Giới hạn Google nêu tường minh: "**Cross-domain breaks when domains send data to different container IDs**".

| Điểm | Nhãn | Chi tiết |
|---|---|---|
| Skill `ads-server-side-tracking` đã cài nhưng chưa dùng | **KHỚP với ponytail — giữ nguyên** | Không tiêu chí nào của Google được thoả ở quy mô hệ: (a) performance — 1 LP tĩnh Astro, tải <2,5s là mục tiêu đã có cách rẻ hơn; (b) data control — PII đã không vào GA4 (`gtm-container-spec.md` §1.3 "Không tạo DLV cho tên/SĐT/email"), ECL hash ở server Keap-side; (c) data quality — chưa có bằng chứng mất dữ liệu. Cộng thêm **chi phí hosting + một điểm hỏng mới**. → **Đề xuất: ghi rõ điều kiện mở** thay vì để skill lửng lơ: mở khi (i) ITP/adblock làm mất >20% conversion đo được, hoặc (ii) cần gửi PII ra vendor thứ 3 mà không muốn qua browser, hoặc (iii) ngân sách >150tr₫ và có người vận hành GCP. |
| Cross-domain + server-side | **MỚI (nhỏ)** | Nếu sau này LP nằm ở domain khác domain Keap proxy, đây là cái bẫy Google nêu tên. Hiện `ga4-setup.md` xử lý bằng Unwanted referrals — đủ. |

**(c) Đối chiếu `tracking/gtm-container-spec.md` với chuẩn Google:**

| Mục | Chuẩn Google | Hệ | Nhãn |
|---|---|---|---|
| **Google tag vs GA4 Config tag** | Từ 2023-2024 Google đã hợp nhất: loại tag là **"Google Tag"** (không còn "GA4 Configuration"), một Google tag khai `G-` có thể **đồng thời nạp cấu hình cho `AW-`** nếu 2 ID được liên kết | Hệ dùng đúng loại **"Google Tag"** (§3.1 ghi `Loại = Google Tag`) nhưng **đặt tên** `[Setup] - GA4 Configuration` | **KHỚP về kỹ thuật, tên gây hiểu sai** — tên gợi lại loại tag đã bị khai tử. Đề xuất đổi tên thành `[Setup] - Google Tag` để người sau không đi tìm loại tag không còn tồn tại. Hệ cũng đã tự nhận ra ở ghi chú "cũng nạp Google Ads conversion nếu khai `AW-`" — đúng. |
| **Conversion Linker** | Cần cho Google Ads conversion tracking (đọc/ghi cookie `_gcl_*` từ gclid) | Hệ có `[Setup] - Conversion Linker` trong convention đặt tên | **KHỚP** |
| **Thứ tự tag & consent** | Consent phải được set **trước** khi tag đọc/ghi storage; GTM có "Consent Overview" + `Additional consent required` per-tag | Hệ dùng **Tag firing priority = 100** cho Google Tag + `Additional consent → analytics_storage` | **KHỚP nhưng chưa đủ tham số** — với Google Ads conversion tag, tham số cần là **`ad_storage` + `ad_user_data`** (không phải `analytics_storage`). Hệ khai `analytics_storage` cho Google Tag; phải kiểm các tag `[GAds] - *` có khai đúng `ad_storage`/`ad_user_data` chưa. `ad_user_data` là **bắt buộc cho enhanced conversions** (§C2.9) → khai sai là ECL không chạy. |
| **Naming convention** | Google **không** publish convention bắt buộc | Hệ có convention riêng `[GA4] -` / `[GAds] -` / `[Setup] -` / `CE -` / `DLV -` / `CONST -` | **KHỚP (luật nội bộ hợp lý)** — trùng convention phổ biến của cộng đồng `[third-party: Analytics Mania]`. Không cần vá. |
| **Versions / workspaces / Preview** | Mỗi lần publish tạo version; dùng Preview mode để debug trước publish | Hệ chưa nói về version/workspace hay quy trình publish | **MỚI (nhỏ)** — thêm 1 dòng: mỗi publish phải có **version name + note** ("thêm event X", ngày), và **Preview trước publish**; đây là cách duy nhất rollback khi tracking gãy. Nối vào alert "GA4 event ngừng bắn dù có traffic — GTM/LP vừa deploy gì không?" (`monitoring.md` §2). |

## C3. NHÓM VỪA

### C3.1 Google Ads Display Certification
`[3P]` syllabus không công khai chi tiết. Nội dung Google chính thức liên quan: [Optimize your Display campaigns](https://support.google.com/google-ads/answer/6382966).
**Điểm quan trọng nhất không nằm trong syllabus mà nằm ở tin sản phẩm: campaign type Display đang bị migrate vào Demand Gen (§A13) → giá trị của cert này đang giảm, và kế hoạch G2 của hệ phải viết lại.** Với hệ: Display = **chỉ remarketing, không bao giờ cold** (`research` §1) — giữ nguyên nguyên tắc, đổi phương tiện thực thi.

### C3.2 Google Ads Video Certification
`[3P]` syllabus: brand lift study cho campaign consideration; measurement cho awareness; conversion tracking khi khách cần thêm thời gian quyết định; **tCPM**; ad format, bidding, optimization.
| Điểm | Nhãn |
|---|---|
| "Đo YouTube bằng brand search lift, không đo bằng CPL" | **KHỚP** | `campaign-setup.md` §5.3 đúng đúng tinh thần giáo trình (brand lift là công cụ chính thức cho tầng consideration). |
| Video Action Campaigns đã chết → Demand Gen | **MỚI** (§A13) |
| tCPM cho awareness | **MỚI (nhỏ)** | Nếu G5 mở, awareness dùng tCPM/reach; conversion dùng Demand Gen. Hai việc khác nhau, đừng dùng một campaign làm cả hai. |

**Bổ sung: "Plan Google Video Campaigns with Reach Planner" (courses/11036)** — nguồn Google: [About Reach Planner](https://support.google.com/google-ads/answer/9427120?hl=en) · [About forecasts in Reach Planner](https://support.google.com/google-ads/answer/9808024?hl=en) (2026-07-28). Đúng 2 ý như phạm vi đã giao:

1. **Dùng lúc nào:** Reach Planner "provides a **forecast** for how your media plan **might** perform, based on your desired audience, budget, and other settings" — tức dùng **TRƯỚC khi chi tiền**, ở bước lập kế hoạch. Forecast dựa trên trend thị trường + hiệu suất lịch sử của campaign tương tự, lấy dữ liệu gần nhất trong khoảng bằng độ dài chiến dịch, **tối đa 92 ngày**. → **Khớp đúng nguyên tắc gate của hệ**: có dự phóng rồi mới mở kênh. Đề xuất: biến Reach Planner thành **điều kiện tiên quyết của G5** — không có media plan dự phóng thì không mở YouTube.
2. **Metric nào cho giai đoạn 1 của journey-plan:** Reach Planner cho **Reach, Frequency, TrueView views, Conversions, Impressions**. Giai đoạn 1 (awareness/nhận biết) cần **reach + frequency** — đó là thứ dự phóng ĐƯỢC **trước**; còn **brand search lift** (`campaign-setup.md` §5.3) chỉ đo ĐƯỢC **sau**. → Hai thứ bổ sung nhau, không thay nhau: Reach Planner để **xin ngân sách**, brand search lift để **nghiệm thu**.
Cảnh báo Google kèm: forecast "**doesn't guarantee** performance or outcomes"; kết quả thật còn phụ thuộc ad quality, relevance, campaign settings.

### C3.3 Google Ads Creative Certification (courses/8992)
`[3P]` syllabus: hướng dẫn creative dựa trên nghiên cứu của Google cho Video, Display, App **và Search**; khung **ABCD** — **A**ttract (thu hút ngay từ đầu), **B**rand (gắn brand tự nhiên), **C**onnect (kết nối bằng cảm xúc/kể chuyện), **D**irect (nói rõ muốn họ làm gì).

| Điểm | Nhãn |
|---|---|
| Khung ABCD | **MỚI** | Có thể dùng làm **rubric review RSA** cho `playbook/campaign-setup.md` §3, thay vì chỉ đếm ký tự. Thử nhanh 3 bộ RSA hiện có: **A** ✔ (headline #1 có tên dự án + "Bảng Giá Mới Nhất" = lý do đọc tiếp); **B** ✔ (tên dự án trong nhiều headline); **C** ⚠️ **yếu nhất** — 3 bộ toàn thông tin/chính sách, không có kết nối cảm xúc nào (BĐS để ở là quyết định cảm xúc); **D** ✔ ("Gọi Ngay Nhận Bảng Giá", "Đặt Lịch Xem Nhà Mẫu"). → Đề xuất cụ thể: thêm 1-2 headline nhóm **C** vào bộ 1 và bộ 2 (kiểu "Chọn Căn Cho Gia Đình 4 Người", "Sống Gần Trường Cho Con") — cùng lúc phục vụ Ad Strength (diversity của asset). |
| RSA asset best practices + Ad Strength | **KHỚP/MỚI** | Đã ở §A2, §A3. Việc vá cụ thể: ≥6 sitelink + thêm headline nhóm C. |

### C3.4 Explore the Value of Discovery Ads (courses/10488)
**Khóa LEGACY — nội dung đã lỗi thời.** Discovery campaigns đã bị nâng cấp hết thành **Demand Gen từ cuối tháng 1/2024** và Discovery không còn tồn tại trong Google Ads ([About Demand Gen](https://support.google.com/google-ads/answer/13695777?hl=en)). **Đã verify.** → Không học nội dung Discovery; học Demand Gen hiện hành ở **§A13**. Map vào hệ: Demand Gen là phương tiện cho G2 (remarketing, sau khi Display bị migrate) và G5 (YouTube conversion, sau khi VAC chết) — nhưng ngưỡng ngân sách $100+/ngày khiến nó **không khả thi ở 30tr₫**, chỉ mở ở 150tr₫.

### C3.5 Microsoft Clarity (không có chứng chỉ chính thức — học từ docs)

Nguồn: [Clarity Overview](https://learn.microsoft.com/en-us/clarity/setup-and-installation/about-clarity) · [Smart Events](https://learn.microsoft.com/en-us/clarity/setup-and-installation/smart-events) · [Data retention](https://learn.microsoft.com/en-us/clarity/setup-and-installation/data-retention) · [Recordings overview](https://learn.microsoft.com/en-us/clarity/session-recordings/recordings-overview) (2026-07-28). Không có certification cho Clarity.

**Microsoft dạy — 5 điểm hệ chưa có:**

**(1) Smart Events — auto-detect conversion KHÔNG cần code.** "Clarity **automatically defines** smart events for you, and you can customize them or define new events–**all code-free**." 4 loại: Button Clicks, API events, Auto events, Page visits. Clarity tự phát hiện **9 auto event type**: Purchase, Add to Cart, Begin Checkout, **Contact Us**, **Submit Form**, **Request Quote**, Sign Up, Login, Download. Giới hạn: **tối đa 20 custom smart event**; chỉ admin project tạo/sửa được. API event phải sửa bằng code, không sửa/ẩn được từ UI.

| Đánh giá cho hệ | Kết luận |
|---|---|
| Smart Events có thay được event thủ công nào của hệ không? | **KHÔNG — và không nên.** `CLAUDE.md` quy định registry 6 event duy nhất, LP và `tracking/` phải khớp. Smart Event là **của Clarity, không đẩy sang GA4/Ads** → nếu dùng nó làm nguồn conversion sẽ có nguồn thứ 5 không ai đối chiếu được. |
| Nhưng dùng được để làm gì? | **Rất hữu ích cho việc lọc replay** — đúng nghề của Clarity. 3 auto event `Submit Form`, `Contact Us`, `Request Quote` map thẳng vào `generate_lead` / `phone_click`+`zalo_click`. → Thay vì lọc replay bằng "thời lượng >60s + không có trang `/cam-on/`" (cách hiện tại ở `clarity-checklist.md` §2 mục 4 — gián tiếp và dễ sai), có thể lọc bằng **smart event `Submit Form` = không xảy ra**. Chính xác hơn, không cần code. |

**(2) Segments & filter nâng cao.** Docs nêu "Create and analyze segments to customize the data to your specific needs"; smart event xuất hiện trong Recordings → More details → Events và trên playback controls, dùng được làm filter. Kết hợp filter URL pattern + smart event + custom tag.
→ Hệ hiện lọc rage click "theo selector form lead" (§2 mục 1). **Bổ sung được:** lưu sẵn **segment** thay vì lọc tay mỗi tuần — 15 phút thứ 5 sẽ thành 5 phút.

**(3) Custom tags qua JS API.** Docs Smart Events trỏ sang [Clarity API](https://learn.microsoft.com/en-us/clarity/setup-and-installation/clarity-api) cho custom event và [Identity API](https://learn.microsoft.com/en-us/clarity/setup-and-installation/identify-api). *(Trang custom-tags cụ thể trả 404 ở lần fetch này — URL đã đổi; API tồn tại và được docs Smart Events dẫn chiếu.)*
→ **Ý tưởng đáng làm, nối trực tiếp với skill `ad-click-attribution`:** LP đã capture `gclid`/`gad_source`/`utm_*`; gắn thêm 1 lệnh set custom tag Clarity (ví dụ `traffic = ads` / `campaign = <utm_campaign>`) **trên cùng đoạn code đã có** → lọc được replay "phiên đến từ Google Ads" **mà không cần** tracking template UTM. Điều này quan trọng vì `clarity-checklist.md` §1b hiện **bắt buộc phải thêm tracking template UTM cấp tài khoản** để Clarity lọc theo campaign — custom tag là đường thay thế **không đụng vào Google Ads**. ⚠️ Chưa verify được cú pháp chính xác (trang 404) → phải đọc trang API trước khi làm; và **tuyệt đối không** đưa tên/SĐT/email vào tag (cùng luật với GA4).

**(4) Clarity Copilot.** Docs xác nhận: "Chat and summarize with Copilot", "Copilot powered insights **quickly summarize recordings and heatmaps**".
→ Với việc "xem 3 replay/tuần" của hệ, Copilot summarize là cách rút ngắn thật. Không thay việc xem — thay việc **tìm** replay nào đáng xem.

**(5) Data retention — giới hạn hệ CHƯA biết:**

| Loại dữ liệu | Thời gian giữ |
|---|---|
| Recordings (thường) | **30 ngày** |
| Sau 30 ngày | giữ **1% recordings hoặc 10 recordings/ngày, lấy số lớn hơn**, tới **9 tháng** |
| Recordings được **favorite/label** | **9 tháng** |
| Heatmaps | **9 tháng** |
| Sau hạn | xoá khỏi server kể cả backup, **không phục hồi được** |

→ **Hệ quả vận hành quan trọng:** chu kỳ BĐS 3-12 tháng, nhưng replay chỉ sống **30 ngày**. Nếu tháng 10 muốn xem lại phiên của một lead đã chốt hồi tháng 7 → **đã mất**, trừ khi đã **favorite** nó. Với hệ, replay đáng giá nhất chính là phiên của **lead đã qualified/đặt cọc** (để biết hành trình thắng trông như thế nào). → Đề xuất thêm 1 thao tác vào nhịp tuần: **favorite ngay** replay của mọi lead contactable/qualified. Chi phí 1 phút, giá trị 9 tháng.

| Điểm | Nhãn |
|---|---|
| Masking Balanced, IP block, không cài qua GTM, 1 project/domain | **KHỚP** — đúng docs, và lý do "không cài qua GTM để không mất đoạn đầu replay" là đúng bản chất (script phải chạy sớm). |
| Native Google Ads integration + cần UTM | **KHỚP** — nhưng xem (3): custom tag là đường thay thế không cần UTM. |
| Quota API 10 request/ngày/project + kỷ luật dùng | **KHỚP** — kỷ luật ở §3 là đúng và nên giữ. |
| **Smart Events** để lọc replay chính xác hơn | **MỚI** |
| **Segment lưu sẵn** thay lọc tay | **MỚI** |
| **Custom tag qua JS API** (nối `ad-click-attribution`, bỏ được yêu cầu UTM) | **MỚI — cần verify cú pháp** |
| **Copilot** để tìm replay đáng xem | **MỚI** |
| **Retention 30 ngày / favorite = 9 tháng** | **MỚI — rủi ro mất dữ liệu, cần vá ngay** |

## C4. NHÓM LƯỚT

### C4.1 Shopping Ads Certification · AI-Powered Shopping Ads Certification
Về feed sản phẩm, Merchant Center, local inventory, Shopping/PMax retail. **BĐS không có SKU, không có feed sản phẩm, không có giá cố định giao dịch online** → không áp dụng. Một ghi chú duy nhất đáng biết: AI Max đang mở rộng sang Shopping và dùng Merchant Center feed để sinh dynamic ads trả lời truy vấn hội thoại ([blog](https://blog.google/products/ads-commerce/ai-max-for-shopping/)) — cho thấy hướng chung của Google là **feed-driven**, và BĐS không có feed thì phụ thuộc hoàn toàn vào chất lượng LP + text asset. Không cần đào vòng 2.

### C4.2 Google Ads Apps Certification
Về App campaign, cài đặt app, SKAdNetwork/Firebase. **Hệ không có app** → không áp dụng. Không cần đào vòng 2.

### C4.3 Search Ads 360 — "SA360 Certification" (18610) + "Build Your Campaign Strategy with SA360" (11761)

SA360 là nền tảng **enterprise** thuộc Google Marketing Platform: quản lý search đa engine (Google, Microsoft, Yahoo Japan…) trong một chỗ, mua qua sales/đối tác GMP, có phí. **Ngoài tầm** một advertiser BĐS 30-150tr₫/tháng dùng Google Ads trực tiếp. Chỉ đáng cân nhắc khi: chạy **nhiều engine** cùng lúc, ngân sách rất lớn, và cần **bid automation xuyên platform** với một bộ target chung.

`[3P]` syllabus: dựng Search campaign đa engine; gán goal/targeting/bid strategy; troubleshoot; đo tác động; optimize. Có 2 chủ đề riêng của SA360: **Bid Strategies** (loại goal target được, thay đổi nào ảnh hưởng learning period tuần đầu, lịch sử conversion cần bao nhiêu để đặt target CPA/ERS/ROAS) và **Inventory Management** (điều gì chặn inventory management sửa campaign, cách kiểm template đã tạo entity nào).

**2 khái niệm hệ nhỏ vẫn học được:**
1. **Bid strategy xuyên campaign với learning period là biến số hạng nhất.** SA360 dạy: "conversion history considerations when setting CPA/ERS/ROAS targets" và "changes that can impact the learning period during the first week". Đây chính xác là điều `campaign-setup.md` §4.1 tuần 1 ("KHÔNG đổi bid cap, ngân sách, RSA, keyword") và `monitoring.md` "Learning phase guard" đang làm. **Xác nhận hệ đúng, từ một giáo trình enterprise.**
2. **Inventory management = sinh campaign/ad group/keyword từ một feed dữ liệu bằng template.** Hệ đã có bản tự làm: `keywords/gen.py` + `master-keywords.csv` + `adgroup-map.md` sinh keyword từ `projects.tsv` (239 dự án). Khái niệm đáng nhặt: **template phải idempotent và phải kiểm được nó đã tạo entity nào** — tức cần một bước "diff giữa những gì template muốn và những gì đang có trong tài khoản" trước khi push. Hệ hiện push một chiều (Editor/Bulk upload), không có diff. Ý tưởng đáng cân nhắc khi số dự án tăng, **chưa cần bây giờ**.

Hết. Không đào sâu thêm.

---

# PHẦN D — Bảng "Skill nào cần vá" (ĐỀ XUẤT — KHÔNG tự sửa, QA duyệt)

Sắp theo mức rủi ro nếu bỏ qua. Cột "Loại" = MỚI / MÂU THUẪN / SỬA NGUỒN (claim đúng nhưng ghi sai nguồn/lý do).

## D1. Rủi ro CAO — đốt tiền hoặc làm sai dữ liệu nếu không vá

| # | File cần sửa | Loại | Google nói | Hệ đang ghi | Đề xuất sửa cụ thể |
|---|---|---|---|---|---|
| 1 | `tracking/ecl-keap-pipeline.md` + `tracking/upload_ecl.py` | **MỚI** | "You must upload **ALL conversions** for the specified event, **including those not attributed to Google Ads**" (§A10) | Pipeline mô tả upload lead từ Keap; không nói rõ phải gồm cả lead không do Ads mang lại | Thêm mục "Luật bắt buộc": query Keap lấy **mọi** contact đạt tag contactable/qualified trong kỳ, **không filter theo có gclid hay không**. Thêm assert trong `upload_ecl.py` selftest: tỷ lệ record không có gclid > 0 (nếu = 0 thì nghi đang filter sai). |
| 2 | `playbook/campaign-setup.md` §1.5 (thêm ô 1.5.11) | **MỚI** | Auto-apply có `Remove conflicting negative keywords`, `Add broad match keywords`, `Use Display expansion`, `Expand reach with Google search partners`, `Adjust CPA targets`… và **chỉ có cấp account** (§A1) | Không có ô nào tắt auto-apply | Thêm ô pre-flight: `Recommendations → Auto-apply settings` → **bỏ chọn TẤT CẢ** (cả 2 bundle + từng mục); rồi `Account Settings → Auto-apply` xác nhận rỗng; ghi ngày kiểm vào audit. **Rà lại hàng tháng** (Google thêm recommendation mới liên tục). |
| 3 | `playbook/monitoring.md` §2 (thêm alert 🔴) | **MỚI** | Advertiser verification: **30 ngày** không nộp → **tài khoản bị tạm ngưng** (§A15) | §1.1 chỉ ghi "3-5 ngày chờ" (thời gian duyệt) | Thêm alert 🔴 "Có yêu cầu verification chưa hoàn thành" + đếm ngược ngày còn lại. Đây là loại sự cố giết cả tài khoản, không chỉ 1 campaign. |
| 4 | `playbook/campaign-setup.md` §2.1/§5.1/§5.2 · `PLAN.md` §0.5 · `playbook/customer-journey-plan.md` (gate G2) | **MÂU THUẪN** | Display campaign đang được migrate vào **Demand Gen**; sẽ **không tạo được Display campaign mới** (§A13) | `BDS_RMKT_Display` là standard Display campaign, 10-15% ngân sách, mở ở G2 | **Verify ngay trong tài khoản** xem còn tạo được Display campaign không. Nếu không: đổi G2 sang Demand Gen với GDN inventory + remarketing list, và **tính lại ngân sách** — Demand Gen best practice là $100+/ngày (≈2,6tr₫), không vừa quota 10-15% của 30tr₫. Khả năng thực tế: **G2 phải hoãn tới mức ngân sách cao hơn**, hoặc chấp nhận chạy dưới ngưỡng Google khuyên. Đây là quyết định chiến lược, QA phải chốt. |
| 5 | `research/google-ads-bds-vn.md` §7 (dòng lead form assets) | **MÂU THUẪN** | Vẫn còn ngưỡng **>$50.000** cho Video/Display + Search-headline-mở-form; có đường thay thế **$1.000/account hoặc $15.000 across accounts** cho "reputable advertisers" + verification (§A9) | "đã bỏ yêu cầu $50k spend (7/2026)" | Viết lại: ngưỡng $50k **vẫn tồn tại** cho các format đó; hệ 30tr₫/tháng có thể đi đường $1.000/account nhưng phải qua verification và thẩm định good standing. Xoá cách diễn đạt "đã bỏ yêu cầu" (nguồn cũ là Search Engine Land, không phải Google). |
| 6 | `playbook/campaign-setup.md` §1.4 (ghi chú cuối) | **MÂU THUẪN nhẹ nhưng dẫn tới quyết định sai** | **Account-level negative keywords** (1.000) là cái **tự áp cho Search + PMax + App + Shopping + Smart + Local**; shared list phải gắn tay từng campaign (§A12) | "Danh sách dùng chung thắng vì áp được cả cho PMax sau này" | Sửa lý do. Quyết định "1 nơi duy nhất" giữ được, nhưng nếu mục tiêu là **tự phủ PMax ở G4** thì nơi đúng là **account-level negatives** (216 < 1.000 nên vừa). QA chốt: shared list (linh hoạt, 5.000/list, phải gắn tay) hay account-level (tự phủ mọi type, trần 1.000). |
| 7 | `tracking/ga4-setup.md` §1 | **MỚI** | GA4 có **attribution settings**: model (default data-driven) + **key event lookback window** (default 90, chọn 30/60) (§B3) | Không cấu hình attribution ở đâu | Thêm 2 dòng vào bảng §1: `Attribution model = Data-driven` · `Key event lookback window = 90 ngày` (khớp conversion window 90 ngày ở Ads). Thêm 1 dòng cảnh báo: **model GA4 và model Google Ads là 2 cấu hình riêng biệt**. |
| 8 | `PLAN.md` §6.6 (quy trình sau-lead PENDING) · `playbook/customer-journey-plan.md` | **MỚI** | Conversion delay nên **trong ≤7 ngày** kể từ ad interaction để bidding học kịp (§A8) | Chưa có SLA thời gian cho việc sales gắn tag | Thêm ràng buộc vào phần PENDING: **`Lead_Contactable` phải được tag + upload trong ≤7 ngày** kể từ click, nếu không thì nó không dùng được làm tín hiệu bid chính. `Lead_Qualified`/`Dat_Coc` chậm hơn được, nhưng khi đó vai trò của chúng là **báo cáo + value**, không phải bid signal. Đây là điều kiện phải thống nhất với người có quyền Keap **trước** khi bật ECL. |
| 8b | `tracking/ecl-keap-pipeline.md` §"Chuẩn hoá trước khi hash" + code hash | **MỚI — BUG làm mất match rate** | Với `gmail.com`/`googlemail.com` phải **xoá mọi dấu `.` trong username và cắt `+suffix`** TRƯỚC khi hash (§C2.9) | "Email: lowercase → xoá mọi khoảng trắng → SHA-256 → hex" — thiếu bước gmail | Thêm bước: nếu domain ∈ {gmail.com, googlemail.com} → xoá mọi `.` trước `@`, cắt từ `+` tới `@`. Ở VN gmail chiếm áp đảo lead form → `nguyen.van.a@gmail.com` vs `nguyenvana@gmail.com` là cùng người nhưng hash khác → **mất match rate**. Thêm case vào selftest của `upload_ecl.py`. |
| 8c | `tracking/gtm-container-spec.md` (consent settings của tag `[GAds] - *`) | **MỚI — có thể làm ECL không chạy** | `ad_user_data` là tham số **bắt buộc** cho enhanced conversions và tag-based conversion tracking; `ad_storage` cho storage quảng cáo (§C2.9) | §3.1 khai `Additional consent → analytics_storage` cho Google Tag; chưa thấy khai `ad_storage`/`ad_user_data` cho các tag Google Ads | Rà từng tag `[GAds] - *`: `Additional consent required` phải gồm **`ad_storage` + `ad_user_data`**. Khai sai/thiếu = tag bị chặn hoặc ECL không nhận user-provided data. Đây là lỗi im lặng, không báo lỗi. |
| 8d | `tracking/clarity-checklist.md` §2 (thêm thao tác) | **MỚI — mất dữ liệu không phục hồi** | Clarity giữ recording **30 ngày**; sau đó chỉ giữ 1%/10 per ngày tới 9 tháng; **favorite = 9 tháng**; hết hạn là xoá cả backup (§C3.5) | Không nhắc retention ở đâu | Thêm thao tác tuần: **favorite ngay replay của mọi lead contactable/qualified**. Chu kỳ BĐS 3-12 tháng nhưng replay sống 30 ngày — phiên của lead đã chốt là dữ liệu quý nhất và sẽ mất nếu không favorite. Chi phí 1 phút/tuần. |

## D2. Rủi ro TRUNG BÌNH — làm hệ chậm hoặc kết luận sai

| # | File cần sửa | Loại | Đề xuất sửa cụ thể |
|---|---|---|---|
| 9 | `research/google-ads-bds-vn.md` §3 (match type) + §1 | **MÂU THUẪN có context** | Đổi giọng từ lệnh cấm sang **gate**: thêm 1 khối "Google chính thức khuyên gì và vì sao hệ chưa làm" — nêu ABCs of Account Structure (consolidate + broad primary, 62% advertiser Smart Bidding dùng broad chính), rồi nêu điều kiện Google tự đặt ("critical to use Smart Bidding with broad match") và kết luận: hệ chưa thỏa điều kiện ở bậc 0-1, sẽ thỏa ở bậc 2. Kèm bảng lộ trình 6 bậc ở §C2.6. Không sửa quyết định — sửa cách lập luận, để 6 tháng sau không ai đọc thành "broad = xấu vĩnh viễn". |
| 10 | `research/google-ads-bds-vn.md` §1 (Demand Gen) | **MÂU THUẪN** | "min $5/ngày bắt buộc" → sửa thành: minimum kỹ thuật thấp, nhưng **Google best practice là $100+/ngày cho maximize strategies, hoặc ≥10× tCPA/ngày** ([Demand Gen best practices](https://support.google.com/google-ads/answer/14693848?hl=en)). Kết luận không đổi (ngân sách nhỏ không chạy Demand Gen) nhưng lý do đúng hơn và định lượng được. |
| 11 | `research/google-ads-bds-vn.md` §5 (bảng thang conversion) | **MÂU THUẪN nhẹ** | "Form submit raw \| **0-1**" → sửa thành **1**. Google: đừng dùng conversion value 0 với value-based bidding; nếu không có giá trị thì bỏ khỏi dataset. (`campaign-setup.md` §1.2 đã đặt 1 — chỉ research lệch.) |
| 12 | `research/google-ads-bds-vn.md` §7 + `playbook/campaign-setup.md` §1.1 | **SỬA NGUỒN** | "BĐS VN hay bị Google yêu cầu xác minh" — không có nguồn Google. Google nêu vertical bị nhắm là healthcare, car rental, finance; và nói "**all advertisers will eventually be required**". Sửa lý do thành: mọi advertiser rồi cũng phải làm + deadline 30 ngày dẫn tới tạm ngưng → nộp trước là rẻ nhất. Hành động không đổi. |
| 13 | `playbook/campaign-setup.md` §3.4 (sitelink) | **MÂU THUẪN** | Google: **≥6 sitelink** (gộp ad group+campaign+account) + opt-in dynamic sitelinks để đạt Good+ Ad Strength; hệ có 4. Đề xuất: thêm 2 sitelink vẫn trỏ anchor trên LP (ví dụ `Vị Trí & Kết Nối` → `#vi-tri`, `Tiện Ích Nội Khu` → `#tien-ich`) → đạt 6 mà không phá luật "chỉ anchor trên LP". Về dynamic sitelinks: **đề xuất KHÔNG bật** (cùng lý do đã tắt ACA — không kiểm soát được text) và ghi rõ đó là đánh đổi có ý thức với Ad Strength. |
| 14 | `playbook/campaign-setup.md` §3 (3 bộ RSA) | **MỚI** | Áp rubric **ABCD** của Google (§C3.3). Thiếu rõ nhất là **C — Connect**: 3 bộ RSA toàn thông tin/chính sách, không có headline cảm xúc. Đề xuất thêm 1-2 headline nhóm C vào bộ 1 và bộ 2, kèm kiểm ký tự bằng script §3.5. Vừa đúng giáo trình creative, vừa tăng asset diversity (Ad Strength). |
| 15 | `playbook/campaign-setup.md` §5.3 (dòng AI Max) | **MỚI** | Thêm 3 điều kiện/cảnh báo: (a) AI Max search term matching **không chạy với Manual CPC/Max Clicks** → bắt buộc conversion-based bidding; (b) **pinning H1 bị bỏ qua** nếu bật cả text customization + final URL expansion → giữ quyết định tắt final URL expansion, giờ có lý do thứ 2; (c) rà chéo **216 negative ↔ brand inclusions** trước khi bật (Google cảnh báo negative trùng brand inclusion làm giảm hiệu suất). |
| 16 | `playbook/monitoring.md` §3 (suggest engine) | **MỚI** | Thêm guard cho suggest `Seasonality adjustment`: chỉ hợp lệ khi campaign đang chạy **tCPA/tROAS** (Search chỉ hỗ trợ 2 cái này) — ở bậc Max Clicks thì API sẽ từ chối. Đồng thời **cấm** suggest seasonality adjustment cho Tết/tháng 7 âm (định kỳ + >14 ngày → Google nói không dùng); Tết là thao tác **ngân sách**. |
| 17 | `playbook/monitoring.md` (thêm dòng vào §3 hoặc §1) | **MỚI** | **Seasonal budget adjustments** (§A6): lên lịch tăng budget 3-14 ngày cho đợt mở bán, tự trả về mức cũ. Điều kiện: Search/Shopping, **không dùng shared budget**, 2 lần cách ≥7 ngày. Thay thế cho việc sửa tay rồi quên. Đồng thời củng cố §1.5.10 (không dùng shared budget). |
| 18 | `tracking/audit-monthly.md` | **MỚI** | Thêm bảng "6 nguyên nhân lệch số Ads ↔ GA4 ↔ CRM" (liệt kê ở §C2.2): (a) Ads conversion không hiện trong standard GA4 report; (b) 2 model attribution riêng; (c) lookback vs conversion window; (d) GA4 thresholding; (e) search terms report bỏ term ít volume; (f) múi giờ. Đây là chủ đề chính thức trong giáo trình Measurement, và là câu hỏi sẽ được hỏi mỗi tháng. |
| 18b | `playbook/monitoring.md` §1 + §7 | **MỚI** | Google Ads quy conversion về **ngày CLICK**, GA4 về **ngày CONVERSION** (§C2.7). Với BĐS chu kỳ dài, "Lead hôm nay" trong báo cáo Daily Close có thể thuộc click **tuần trước** → **CPL theo ngày về bản chất là nhiễu**. Thêm 1 dòng cảnh báo trong mẫu tin và quy định: quyết định chỉ ra ở mức **7-30 ngày**, báo cáo ngày chỉ để phát hiện anomaly. Đồng thời **chốt rõ đang đọc cột nào**: `Conversions` hay `All conversions` (action Secondary và view-through vẫn vào `All conversions`). |
| 18c | `playbook/campaign-setup.md` (checklist G4, PMax) | **MỚI** | Dựng PMax theo checklist 12 bước ở §C2.8(a). Ba điểm quan trọng nhất: **TẮT URL expansion** (chưa ghi cho PMax, chỉ ghi cho AI Max); **audience signals chỉ là gợi ý** không giới hạn phân phối; **exact keyword identical thắng PMax** → giữ tên dự án ở Exact là lá chắn chống cannibalize brand (giải toả đúng lo ngại ở `research` §1). |
| 19 | `tracking/ecl-keap-pipeline.md` | **MỚI** | Mốc **tháng 4/2026**: enhanced conversions for web + leads đã **gộp thành 1 toggle on/off**, nhận data đồng thời từ website tag / Data Manager / API. Hôm nay đã qua mốc → UI thật có thể khác doc của hệ (viết theo mô hình 2 đường riêng). Thêm bước verify khi có quyền tài khoản. |

## D3. Rủi ro THẤP — bổ sung kiến thức, chống kết luận sai

| # | File cần sửa | Loại | Đề xuất sửa cụ thể |
|---|---|---|---|
| 20 | `research/google-ads-bds-vn.md` §8 (checklist) hoặc mục mới | **MỚI** | Thêm khối "Chống chỉ định": (a) **Optimization score không phải KPI** — dismiss recommendation cũng làm tăng score, score không vào Quality Score → đừng theo đuổi, đừng báo cáo nó; (b) **Ad Strength không vào Ad Rank/Quality Score/auction wins** (trích nguyên văn) → là feedback tool lúc tạo ad, không phải KPI hiệu suất. |
| 21 | `research/competitors/2026-07-eco-retreat.md:241` | **MÂU THUẪN nhẹ** | Dòng "Đo bằng: Ad Strength + CTR ad group brand" — Ad Strength không phải thước đo hiệu suất. Đổi sang **CTR + CVR + contact rate**; giữ Ad Strength chỉ như checklist "đã đủ asset chưa". |
| 22 | `research/google-ads-bds-vn.md` §3 + `keywords/UPDATE.md` | **MỚI** | Search terms report **luôn ẩn** term ít volume vì privacy → (a) tổng click theo search term < tổng click campaign, không phải bug; (b) negative list không bao giờ phủ hết → luôn còn rò rỉ dư, đừng kỳ vọng 0; (c) GAQL `search_term_view` sẽ không cộng bằng `campaign` — nói trước cho MCP/monitoring. |
| 23 | `keywords/adgroup-map.md` (mục Match type) + `playbook/campaign-setup.md` §2.4.5 | **MỚI — chỗ dễ hiểu sai** | Tách bạch: câu "Google tự khớp biến thể không dấu" **chỉ đúng cho positive keyword**. Negative keyword **không** khớp close variant → biến thể không dấu trong negative list là **bắt buộc**, không phải tuỳ chọn. Hiện §2.4.5 và §3-research đọc ngược nhau nếu không có ghi chú này. |
| 24 | `playbook/campaign-setup.md` §1.2 | **MỚI (nhỏ)** | Khi tạo 6 conversion action, **chọn đúng goal category chuẩn của Google** (`Qualified lead`, `Converted lead`, `Book appointment`, `Request quote`, `Contact`, `Submit lead form`) chứ không chỉ đặt tên tự do — PMax/AI Max và recommendation đọc theo **category**, không đọc tên. |
| 25 | `playbook/campaign-setup.md` §2.4 (sau import) | **MỚI (nhỏ)** | Thêm bước kiểm chứng: **0 keyword nào ở match type Broad**. Vì broad là **default** của Google Ads — bất kỳ dòng import thiếu cột `Match type` sẽ thành broad im lặng. |
| 26 | `playbook/customer-journey-plan.md` (gate) hoặc `PLAN.md` §0 | **MỚI** | Thêm bảng **"gate nào mở khoá tính năng AI nào"** (bảng 6 bậc ở §C2.6). Google gọi đây là "AI automation strategy"; hệ đã có gate nhưng chưa map gate ↔ tính năng. |
| 27 | `playbook/monitoring.md` §6 | **MỚI (chống lẫn tên)** | Đổi tên/ghi chú để phân biệt tường minh: "**Auto-apply nội bộ** (executor của hệ, có người bấm nút + guardrail + audit log)" ≠ "**Auto-apply recommendations của Google** (đã TẮT hết ở §1.5.11, không có guardrail của mình)". Hai thứ trùng tên, dễ khiến người sau tưởng đã kiểm tra rồi. |
| 28 | `playbook/campaign-setup.md` §1.5.6 (ACA) + lịch giám sát | **MỚI** | Ghi mốc **9/2026 auto-upgrade** và **2/2027 DSA sunset**: ACA, DSA và campaign-level broad match setting đang bị Google nâng cấp thành AI Max. Cần rà lại xem ACA đã tắt có bị ảnh hưởng không, và biết rằng **text disclaimers** là cơ chế Google cấp để khoá text bắt buộc (pháp nhân/MST/miễn trừ) nếu buộc phải sống với AI-generated text. |
| 29 | `research/google-ads-bds-vn.md` §7 + `playbook/campaign-setup.md` §3 | **MỚI (policy, nâng mức nghiêm trọng)** | Mạo nhận brand khác thuộc *unacceptable business practices* = **đình chỉ tài khoản NGAY, không cảnh báo**. Nặng hơn cách hệ đang ghi. Với sàn phân phối: headline `{Tên dự án} - Giá Gốc CĐT` (§3.1 #4) chỉ an toàn khi **LP nói rõ mình là đơn vị phân phối, không phải CĐT**. Thêm điều kiện đó thành ràng buộc cứng. Thêm cả policy [Business information requirements](https://support.google.com/adspolicy/answer/12499303) làm tên chính thức cho yêu cầu footer pháp nhân. |
| 30 | `research/google-ads-bds-vn.md` §7 + §3 | **MỚI** | "Minh bạch chi phí" là một nhánh của misrepresentation: cấm tạo "false or misleading impression of the cost". Áp vào BĐS: mọi `Giá Từ`/`Trả Trước Từ` phải là **căn thật đang bán, có bằng chứng**, và không bỏ qua phí bắt buộc. |
| 31 | `research/google-ads-bds-vn.md` §7 (HEC) | **MỚI (nhỏ)** | Bổ sung 2 chi tiết cho trường hợp nhắm Việt kiều US/CA: **radius tối thiểu 1 km**; **predefined Google audiences vẫn dùng được** cho HEC (audience tự dựng bị hạn chế rộng hơn); Canada dùng được 3 ký tự đầu postal code (FSA). |
| 32 | `tracking/ga4-setup.md` §4.1 (BigQuery) | **MỚI (nhỏ)** | Giữ quyết định hoãn. Thêm **điều kiện mở lại**: cần né data thresholding cho phân tích demographic, hoặc cần join GA4 × Keap × Ads ở cấp row. Kèm cảnh báo: **BigQuery không nhận data từ Google signals** → số event sẽ khác GA4 UI, không phải lỗi pipeline. Free tier: 1 triệu event/ngày (còn rất xa). |
| 33 | `tracking/ga4-setup.md` §3 (audience) · `research` §9 mục 8 | **SỬA NGUỒN** | Ngưỡng "≥100 user active/30 ngày" cho Display remarketing: nguồn hiện tại là Search Engine Land (3P), **chưa xác nhận được ở tài liệu Google** trong vòng research này. Đánh dấu 3P hoặc verify lại. (Gate G2 của hệ đặt ≥1.000 user nên vẫn an toàn.) |
| 34 | `research/google-ads-bds-vn.md` §1.3 (AI Max) | **CHƯA XÁC NHẬN** | Claim "AI Max giữ **search terms report**": negative keywords đã xác nhận nguyên văn từ Google, nhưng search terms report cho AI Max **không tìm được câu xác nhận tường minh**. Cần verify tại [About reporting in AI Max](https://support.google.com/google-ads/answer/16470459) trước khi giữ claim, vì đó là lý do chính hệ coi AI Max "an toàn hơn PMax". |
| 35 | Mới — `research` §Khoảng trống | **MỚI (rủi ro cần verify)** | Thêm khoảng trống: policy lead form ghi "**Affiliate networks and lead generation businesses are prohibited**". Hệ chạy cho **sàn phân phối BĐS**. Phải verify Google có xếp sàn vào diện này không, **trước** khi đầu tư vào lead form asset — và cân nhắc xem câu này có hàm ý rộng hơn lead form. |
| 36 | `playbook/campaign-setup.md` (checklist G4) | **MỚI** | Yêu cầu asset PMax trước khi bật (§A12): ≥20 text (15 headline + 5 description), ≥7 image (**3 landscape, 3 square, 1 portrait**), ≥1 video. BĐS phải chuẩn bị ảnh flycam/nhà mẫu đúng 3 tỷ lệ **trước**, không phải sau khi bật. |
| 37 | `playbook/campaign-setup.md` §1.2 hoặc research §5 | **MỚI** | **Conversion Value Rules** — điều chỉnh giá trị conversion theo geo/device/audience **không cần sửa tag**. Ứng dụng: lead đúng quận dự án > lead ngoại tỉnh; lead từ `xem_bang_gia_30d` > lead lạ. Rẻ hơn dựng thêm conversion action. Chỉ có nghĩa khi đã ở bậc value-based bidding. |
| 38 | `research/google-ads-bds-vn.md` §3 (Search audiences) | **MỚI** | Dùng 5 audience GA4 làm **observation** trên Search campaign (không đổi phân phối, chỉ đọc số) để thấy chênh CVR theo audience. Miễn phí, không rủi ro, hiện chưa dùng ở đâu. |
| 39 | `research/google-ads-bds-vn.md` (store visits) | **MỚI (chống chỉ định)** | Không bật store visits/store sales conversion: (a) cần GBP verified + volume, (b) **không tương thích search terms report** → mất công cụ vận hành số 1 của hệ. Củng cố quyết định §3.4 (chưa có GBP → bỏ qua). |
| 41 | `tracking/clarity-checklist.md` §2 | **MỚI** | Dùng **Smart Events** (auto event `Submit Form` / `Contact Us` / `Request Quote`, code-free, trần 20 custom) để lọc replay thay cho cách gián tiếp hiện tại ("thời lượng >60s + không có trang `/cam-on/`"). Lưu sẵn **segment** thay vì lọc tay mỗi tuần. Dùng **Copilot** để tóm tắt/tìm replay đáng xem. **Không** dùng Smart Event làm nguồn conversion — registry 6 event của `CLAUDE.md` là duy nhất. |
| 42 | `tracking/clarity-checklist.md` §1b + skill `ad-click-attribution` | **MỚI — cần verify cú pháp trước** | Gắn **custom tag Clarity** (`traffic=ads`, `campaign=<utm_campaign>`) ngay trong đoạn code đã capture gclid/utm của LP → lọc replay theo nguồn ads **mà không cần** tracking template UTM cấp tài khoản (§1b hiện đang bắt buộc thêm UTM). Trang docs custom-tags trả 404 ở lần fetch này → **đọc [Clarity API](https://learn.microsoft.com/en-us/clarity/setup-and-installation/clarity-api) xác nhận cú pháp trước khi làm**. Tuyệt đối không đưa tên/SĐT/email vào tag. |
| 43 | `tracking/gtm-container-spec.md` §3.1 (tên tag) | **MỚI (nhỏ, chống hiểu sai)** | Đổi tên `[Setup] - GA4 Configuration` → `[Setup] - Google Tag`. Loại tag hệ dùng **đã đúng** ("Google Tag"), nhưng tên gợi lại loại tag "GA4 Configuration" đã bị Google khai tử → người sau đi tìm một loại tag không còn tồn tại. |
| 44 | `tracking/gtm-container-spec.md` (thêm mục quy trình publish) | **MỚI (nhỏ)** | Thêm 1 dòng: mỗi lần publish phải có **version name + note** (thêm event gì, ngày), và **Preview mode trước publish**. Đây là cách duy nhất rollback khi tracking gãy — nối vào alert 🟡 "GA4 event ngừng bắn dù có traffic" của `monitoring.md` §2. |
| 45 | Skill `ads-server-side-tracking` (ghi điều kiện mở, không cài gì) | **MỚI (chống over-engineering)** | Google nêu 3 lý do server-side: performance, data control, data quality — **không lý do nào thoả ở quy mô hệ** (§C2.10b): 1 LP tĩnh, PII đã không vào GA4, chưa có bằng chứng mất dữ liệu; đổi lại là chi phí GCP + một điểm hỏng mới. Ghi **điều kiện mở** vào `tracking/README.md`: (i) ITP/adblock làm mất >20% conversion đo được, hoặc (ii) cần gửi PII ra vendor thứ 3 không qua browser, hoặc (iii) >150tr₫/tháng + có người vận hành GCP. Cảnh báo Google nêu tên: "cross-domain breaks when domains send data to different container IDs". |
| 46 | `playbook/customer-journey-plan.md` (gate G5) | **MỚI** | Đặt **Reach Planner media plan là điều kiện tiên quyết của G5** — có dự phóng reach/frequency rồi mới mở YouTube (khớp nguyên tắc gate của hệ). Reach Planner cho reach/frequency/views/conversions/impressions dựa trên trend + campaign tương tự (dữ liệu tối đa 92 ngày), và Google nói rõ nó **không bảo đảm** kết quả. Reach Planner để **xin ngân sách**; brand search lift để **nghiệm thu** — hai thứ bổ sung, không thay nhau. |
| 47 | `playbook/customer-journey-plan.md` §3 + `campaign-setup.md` §5.1 (dòng PMax 8%) | **MỚI (đề xuất chiến lược, QA chốt)** | PMax 400.000₫/ngày (~$15) chạy trên **6 kênh** là rất mỏng — so sánh gần nhất là Demand Gen $100+/ngày và PMax phủ nhiều kênh hơn. Đề xuất 2 lựa chọn: (a) dồn toàn bộ 8% vào **1 asset group / 1 dự án** để có mật độ, hoặc (b) hoãn PMax thêm một bậc, chuyển phần đó sang Demand Gen remarketing (nơi có audience thật). Google **không** publish ngưỡng ngân sách PMax → đây là suy luận, không phải citation. |
| 48 | Nhiều file — quy ước chung | **SỬA NGUỒN** | Đánh dấu rõ các con số **luật nội bộ, không phải Google**: "tCPA ±15%/lần", "budget ±20%/lần cách ≥3-4 ngày", "chờ 4 tuần mới phán xét", "broad cap 15% ngân sách campaign", "learning phase 1-2 tuần Search". (Cái cuối có nguồn Google gián tiếp qua PMax best practices: 1-2 tuần, tới 6 tuần khi volume thấp.) Google **không** publish 4 con số đầu. Giữ chúng — nhưng đừng để QA sau này tưởng là citation Google. |

---

# PHẦN E-0 — Danh sách đề xuất vòng 2 (lập ở vòng 1)

> ✅ **7 chủ đề đã được đào ở vòng 2** — kết quả ở **Phần E** ngay sau bảng này. Các dòng đã xử lý được đánh dấu `→ E<n>`.

| Chủ đề | Vì sao đáng đào | Nguồn cần fetch |
|---|---|---|
| **Data exclusions cho Smart Bidding** → **E1** | Ưu tiên #1 vòng 2. Trực tiếp nối vào alert "conversion = 0 trong 4h" của `monitoring.md`: tracking gãy 1 ngày mà không khai data exclusion → Smart Bidding học sai và tránh traffic tốt hàng tuần sau | `support.google.com/google-ads` — "About data exclusions" |
| **Campaign experiments** (Search) → **E2** | Google dạy dùng experiment thay vì đổi thẳng bid strategy; hệ đang đổi thẳng ở §4.4. AI Max còn có one-click experiments | "About campaign experiments", "About AI Max Experiments" (answer/16450159) |
| **Insights page** → **E3** | Nguồn phát hiện search trend/demand forecast; có thể thay một phần công việc thủ công ở nhịp tuần | "About the Insights page" |
| **About reporting in AI Max** (answer/16470459) → **E4** | Để chốt claim "AI Max giữ search terms report" (D3 #34) | đã có URL |
| **Negative keywords in PMax** (answer/15726455) | Chi tiết thực thi cho G4 | đã có URL |
| **Quality Score** đầy đủ (answer/6167118) | Có skill `google-ads-quality-score` chưa đối chiếu | đã có URL |
| **Customer Match** (answer/6379332, 10010286) → **E5** | Loại trừ khách đã mua khỏi mọi campaign (audience GA4 14 ngày là quá ngắn); điều kiện cho New Customer Acquisition mode ở PMax | đã có URL |
| **Google Ads announcements 2026** (announcements/9048695) + **GML 2026** (answer/17100114) | Danh sách thay đổi sản phẩm 2026 đầy đủ — vòng này chỉ bắt được AI Max / Display→Demand Gen / VAC→Demand Gen | đã có URL |
| **Lead form policy — "lead generation businesses are prohibited"** | Rủi ro pháp lý/policy cho sàn phân phối; cần đọc nguyên văn cả trang policy | adspolicy/answer/9472930 |
| **Lead Journey Mapping** | Công cụ native trùng mục đích KPI tree của hệ; chưa có trang doc riêng được xác định | tìm trên support.google.com/google-ads |
| **Clarity custom tags API** — cú pháp chính xác → **E7** | Cần cho D3 #42 (bỏ được yêu cầu tracking template UTM). Trang `custom-tags/custom-tags` trả **404** ở vòng này | `learn.microsoft.com/en-us/clarity/setup-and-installation/clarity-api` + `identify-api` |
| **Consent mode basic vs advanced** → **E6** | Trang reference không phân biệt tường minh. Ảnh hưởng: advanced mode gửi cookieless ping khi denied (dữ liệu để model), basic thì không load tag chút nào. Với hệ (VN granted) ít ảnh hưởng, nhưng nếu bao giờ nhắm Việt kiều EU thì đây là quyết định then chốt | `support.google.com/google-ads/answer/10000067` + `14009343` (Obtain user consent) |
| **Nghị định 13 / PDPL Việt Nam** | Mức consent nào là đủ ở VN — **Google không phát biểu về luật VN**, tài liệu Google không trả lời được. Ràng buộc kỹ thuật đã biết: `ad_user_data=denied` ⇒ **ECL không chạy**. Cần ý kiến pháp lý, không phải research thêm | ngoài phạm vi nguồn Google |
| **PMax: New Customer Acquisition + Customer Match** → **E5** (một phần) | Cần cho checklist G4 (§C2.8) | `answer/6379332`, `answer/10010286`, và trang NCA của PMax |
| **Skillshop syllabus chính thức** | Toàn bộ syllabus trong Phần C là 3P tin cậy thấp. Chỉ giải quyết được bằng **đăng nhập Skillshop** — ngoài khả năng WebFetch. Ghi rõ: **cần đăng nhập, bỏ qua.** | — |
| Chứng chỉ nhóm LƯỚT (Shopping, AI-Powered Shopping, Apps, SA360) | Đã kết luận **không cần đào vòng 2** — BĐS không có feed/app, SA360 ngoài tầm ngân sách | — |

**Ghi chú về nguồn không truy cập được:**
- `skillshop.docebosaas.com/learn/courses/*` — JS shell, WebFetch không lấy được nội dung. **Cần đăng nhập, bỏ qua.**
- `skillshop.exceedlms.com/student/catalog/list?category_ids=2844-...` — trả "No results returned" (nội dung render client-side).
- `skillshop.exceedlms.com/student/path/645553` — 302 redirect sang docebosaas (cùng vấn đề).
- `support.google.com/adspolicy/answer/9848939`, `google-ads/answer/10312094`, `7684154`, `7331111`, `10193513`, `9423814` — **404**, ID article đã đổi. Các URL thay thế đúng đã dùng trong file này.

---

# PHẦN E — VÒNG 2: 7 chủ đề đã đào

**Ngày truy cập nguồn vòng 2: 2026-07-28.** Cùng luật nguồn với Phần A-D: chỉ `support.google.com`, `developers.google.com`, `blog.google` (riêng §E7 là `learn.microsoft.com` — Clarity không phải sản phẩm Google). Mọi điểm không tìm được câu xác nhận tường minh đều ghi **CHƯA XÁC NHẬN** thay vì suy diễn.

| § | Chủ đề | Kết quả một dòng | Đã vá vào |
|---|---|---|---|
| E1 | Data exclusions | Công cụ đúng cho "tracking gãy"; chỉ chạy với bidding theo conversion → **vô dụng ở bậc Max Clicks** | `playbook/monitoring.md` §2.1 (mới) |
| E2 | Campaign experiments | Cách an toàn để test bid strategy — nhưng **volume của hệ chưa đủ** để có significance | `playbook/monitoring.md` §3.1 (mới) |
| E3 | Insights page | Chia 2 nhịp: 3 insight dùng tuần, 5 insight dùng tháng | `playbook/monitoring.md` §4 |
| E4 | AI Max reporting | ✅ **Claim "giữ search terms report" ĐÚNG** — có thêm match type `AI Max` + cột `source` | `research/google-ads-bds-vn.md` §1 |
| E5 | Customer Match | ⛔ **$50k chỉ gate `Targeting`** — hệ chỉ `Observation`/`Exclusions` được → **đổi kế hoạch GĐ5** | `playbook/customer-journey-plan.md` §2.1 |
| E6 | Consent mode basic vs advanced | Hệ đang ở trạng thái **"no consent mode"** cho VN, không phải basic/advanced | §E6 (chưa vá file — xem "Chờ QA") |
| E7 | Clarity custom tags API | ✅ Cú pháp đã verify, URL docs mới `/filters/custom-tags` | `tracking/clarity-checklist.md` §1c (mới) |

---

## E1. Data exclusions cho Smart Bidding — ƯU TIÊN #1

Nguồn: [About data exclusions](https://support.google.com/google-ads/answer/10370710?hl=en) · [Use data exclusions for conversion data outages](https://support.google.com/google-ads/answer/10276486?hl=en) · [Create data exclusions (API)](https://developers.google.com/google-ads/api/docs/campaigns/bidding/data-exclusions) · [About seasonality adjustments](https://support.google.com/google-ads/answer/10369906?hl=en) (2026-07-28)

### Google dạy

**Định nghĩa (nguyên văn):**
> "Data exclusions are a tool in Google Ads that help you reduce the impact of conversion tracking issues in Smart Bidding."

Cơ chế: exclusion tác động lên **CLICKS** trong khoảng thời gian được khai, khiến Smart Bidding **không dùng các click đó làm dữ liệu học**. Nó xử lý ở tầng training data của bidding, **không** xoá/sửa số trong báo cáo.

**Điều kiện dùng — cái chặn hệ ở ngày 1:**
> "Data exclusions can only be used with **conversions and conversion value based Smart Bidding strategies**."

Campaign type hỗ trợ: **Search, Display, Shopping, Performance Max**. Không hỗ trợ **Hotel và Travel**. *(App / Demand Gen / Video: **CHƯA XÁC NHẬN** — trang chỉ liệt kê 4 loại trên, không nói loại còn lại bị loại trừ hay chỉ là không nhắc.)*

**Quy trình chính thức khi tracking gãy:**
1. > "Apply data exclusions **as quickly as possible** at the time you've identified a conversion data issue."
2. > "Exclusion dates selected will apply to **clicks**, so make sure to consider your **conversion delay** and exclude any days of clicks that may have been impacted." → phải lùi khoảng exclusion về **trước** ngày outage đủ số ngày conversion delay, không chỉ đúng ngày tag chết.
3. > "It's a best practice to exclude **at least 90% of clicks** associated with impacted conversion data." — đây là **con số % duy nhất** Google publish về "bao nhiêu dữ liệu", và nó là **ngưỡng tối thiểu** để exclusion có tác dụng, không phải trần.
4. Sau khi áp: "adjust CPA/ROAS targets to achieve desired performance, while ensuring budgets are set to acceptable levels."

**Trần thời lượng:**
- API docs (developers.google.com): > "The date range should be **less than 14 days**."
- Trang support **không** nêu số ngày, chỉ nói định tính: > "You shouldn't use data exclusions **frequently or for prolonged periods**, as this can negatively impact Smart Bidding performance."
- → Coi **14 ngày** là ngưỡng khuyến nghị thực hành (nguồn API), không phải giới hạn cứng của hệ thống bidding.

**Hậu quả nếu outage dài:**
> "In the event that a week or more of clicks are impacted, performance fluctuations may persist for **1-2 conversion cycles**."
→ Nghĩa là sau outage ≥1 tuần, **không phán xét hiệu suất** trong 1-2 chu kỳ conversion (với BĐS lead-gen: vài ngày đến vài tuần), và không chồng thêm thay đổi khác lên.

**Retroactive — CÓ.** API cho `start_date_time` và `end_date_time` trong quá khứ. Support xác nhận: > "Data exclusions created for **past dates** should see performance fluctuations begin to stabilize after a few days." → phát hiện muộn vẫn cứu được.

**Cấp áp dụng:** > "Data exclusions can be applied at the **Manager account (MCC)** or sub-account level." → 1 lần cho nhiều account con.

**Ngưỡng thời lượng tối thiểu để đáng tạo exclusion: CHƯA XÁC NHẬN.** Google **không** đặt ngưỡng tối thiểu; ngược lại nhấn mạnh tạo "as quickly as possible". Ngụ ý: kể cả outage vài giờ vẫn nên exclude nếu ảnh hưởng đáng kể % conversion. → Hệ tự đặt ngưỡng **>24h** *(luật nội bộ)* để không tạo exclusion cho mọi nhiễu nhỏ.

### Data exclusion ≠ Seasonality adjustment — hai thứ hay bị lẫn

| | **Data exclusion** | **Seasonality adjustment** |
|---|---|---|
| Nói gì với bidding | "Dữ liệu khoảng này **SAI/HỎNG**, đừng học" | "Khoảng này CVR **sẽ khác** như dự kiến" |
| Dùng khi | Tag chết, LP sập, GTM publish sai, CRM/pipeline ECL đứt | Đợt mở bán, event ngắn có CVR bất thường |
| Thời lượng | <14 ngày (API), càng ngắn càng tốt | 1-7 ngày ("may not work as well… more than 14 days") |
| Bid strategy cần | Conversion/value-based | **tCPA/tROAS** (hẹp hơn) |
| Định kỳ (Tết) | ❌ không liên quan | ❌ Google nói **đừng dùng** ("Smart Bidding already manages these") |

### So với hệ hiện tại

| Điểm | Nhãn | Chi tiết |
|---|---|---|
| Alert 🔴 "Conversion = 0 trong 4h có spend" chỉ dẫn tới "checklist audit nhanh" | **MỚI — lỗ hổng thật, ĐÃ VÁ** | Audit xong rồi sửa xong tag là **chưa hết việc**: Smart Bidding vẫn đang giữ bài học sai. Đã thêm bước "tracking gãy >24h → tạo data exclusion" + thủ tục 9 bước vào `playbook/monitoring.md` §2 và §2.1 mới. |
| Ngày 1 hệ chạy **Max Clicks** | **Chặn thực thi — phải ghi rõ** | Data exclusion **không áp dụng được** ở bậc 0-1 (không phải bidding theo conversion), **và cũng không cần** — Max Clicks không học từ conversion. → Suggest engine phải có guard này, giống guard của Seasonality adjustment (§A6). Công cụ này chỉ có giá trị **từ bậc 2** (`journey-plan` §3.2). |
| Hệ có `tracking/audit-monthly.md` bắn lead giả 9 bước | **KHỚP — bổ trợ tốt** | Audit tháng là cách **phát hiện** outage âm thầm. Data exclusion là cách **dọn hậu quả**. Đã yêu cầu ghi 1 dòng vào audit tháng §4 mỗi lần tạo exclusion. |
| Conversion delay của hệ | **Cần một con số** | Bước 3 của Google yêu cầu lùi theo conversion delay, nhưng hệ chưa đo delay thật (`journey-plan` §4 còn `[điền]`). Tạm dùng **≥3 ngày**; sau 2 tháng chạy phải thay bằng số đo thật từ CRM. |

---

## E2. Campaign experiments (Search) + AI Max experiments

Nguồn: [Campaign experiment: Definition](https://support.google.com/google-ads/answer/6318742?hl=en) · [Set up a campaign experiment](https://support.google.com/google-ads/answer/6261395?hl=en) · [About custom experiments](https://support.google.com/google-ads/answer/10683687?hl=en) · [About the Experiments page](https://support.google.com/google-ads/answer/10682377?hl=en) · [Experiments FAQs](https://support.google.com/google-ads/answer/13826584?hl=en) · [About AI Max experiments](https://support.google.com/google-ads/answer/16450159?hl=en) (2026-07-28)

### Google dạy

**Cơ chế:** > "A campaign experiment lets you test your draft's performance against the original campaign's performance. Experiments use a **portion of the original campaign's traffic and budget** and run alongside the original campaign for a specified length of time."
Luồng: **draft** (bản copy campaign gốc) → sửa draft → biến draft thành **experiment** → chạy song song.

**Traffic split:** khuyến nghị > "using **50%** to provide the best comparison between the original and experiment campaigns".
Hai kiểu split:
- **Cookie-based (recommended)** — > "randomly assigns **users**"; mỗi user chỉ thấy một phiên bản.
- **Search-based** — > "randomly assigns users… **every time a search occurs**"; cùng user có thể thấy cả hai.
→ Test bid strategy thì dùng **cookie-based** (tránh nhiễu chéo).

**Test được gì:** > experiments cho phép test "**Smart Bidding**, keyword match types, landing pages, audiences, and ad groups". Custom experiments: > "let you propose and test changes to your **Search**, Display, Demand Gen, and Video campaigns."
→ **Đổi bid strategy (Max Clicks → tCPA) là use-case chuẩn, được hỗ trợ chính thức.**
Test **budget** riêng biệt: **CHƯA XÁC NHẬN** — tài liệu không nói rõ; experiment vốn *chia* % ngân sách của campaign gốc chứ không so hai mức budget khác nhau.

**Thời lượng & significance:**
- Chạy tối thiểu **4-6 tuần**, dài hơn nếu conversion delay dài; chờ qua **1-2 conversion cycles**.
- **7 ngày đầu bị LOẠI khỏi tính significance** — "to account for the experiment ramp-up time".
- Khi kết quả "inconclusive": Google khuyên chọn "campaigns with **high volumes** and run experiments for longer".
- > "Running several experiments at once isn't recommended. They can interfere with each other."
- Số experiment đồng thời tối đa: **CHƯA XÁC NHẬN** (không có con số cứng).

**Đọc "favorable outcome":**
- Max Conversions / tCPA: favorable khi "conversions in your treatment arm are **higher** than your control arm, with **CPA being lower**".
- Max Conversion Value / tROAS: "conversion value… **higher**… with **ROAS being higher**".

**Khi Apply:** áp thay đổi vào campaign gốc, **hoặc** tách experiment thành **campaign mới riêng**. Auto-apply: > "Once experiments reach their scheduled end date, favorable results apply **automatically** to your control campaign" — **NHƯNG** > "we **don't** apply any experiments which were **ended manually**". → Dừng tay trước hạn = phải apply tay.

**Campaign type hỗ trợ:** PMax, Shopping, Search, App, Display, Demand Gen, Video.

**AI Max experiments (khác cơ chế):** chia **trong cùng campaign**, không tạo bản copy — một phần traffic với AI Max toggle **off** (control), phần còn lại **on** (trial). Google: > "AI Max experiments deliver **faster results** and reduce some of the common experimentation errors". **Không chạy được** nếu campaign có: `text customization enabled`, targets Display network, **Portfolio Bidding Strategy**, **Shared Budgets**, `Bidding exploration`, hoặc **đang có experiment khác**. Thời lượng khuyến nghị & giới hạn quốc gia: **CHƯA XÁC NHẬN**.

### So với hệ hiện tại — kết luận quan trọng: CHƯA DÙNG ĐƯỢC

| Điểm | Nhãn | Chi tiết |
|---|---|---|
| `campaign-setup.md` §4.4 **đổi thẳng** bid strategy | **MÂU THUẪN có context → GIỮ quyết định của hệ** | Google khuyên dùng experiment. Nhưng làm toán với volume thật của hệ: 12-29 lead/tháng, chia 50/50 → mỗi nhánh **6-15 lead/tháng**. Google nói significance cần "high volumes". 4-6 tuần ở mức đó → **gần chắc chắn "inconclusive"**, tức bỏ 6 tuần để không biết gì. → **Giữ đổi thẳng + learning phase guard**, và ghi rõ đây là đánh đổi có ý thức. |
| Khi nào mở experiment | **MỚI — điều kiện định lượng** | Khi **một campaign đơn lẻ** đạt **≥30 conv/tháng ổn định** (mỗi nhánh ~15/tháng). Ở 30tr₫ thì chỉ #1 `Brand_DuAn` có cơ hội. Đã ghi vào `playbook/monitoring.md` §3.1. |
| Ràng buộc "không dùng shared budget" và "không portfolio bidding" | **MỚI — nối vào quyết định cũ** | AI Max experiment bị chặn bởi **Shared Budgets** và **Portfolio Bidding Strategy**. `campaign-setup.md` §1.5.10 đã quyết không dùng shared budget → **được lợi thêm một lần nữa** (lần 1: seasonal budget adjustment §A6). Nhưng §5.2 lại dự kiến **portfolio bidding** ở mức 60tr → nếu sau này muốn AI Max experiment thì **hai thứ loại nhau**. QA cần biết khi tới đó. |
| Auto-apply khi hết hạn | **MỚI — RỦI RO im lặng** | Experiment hết hạn mà "favorable" thì Google **tự apply vào campaign gốc**. Với hệ có luật "người bấm nút chi tiền" (`monitoring.md`), đây là một đường auto-apply thứ ba chưa ai chặn (ngoài Google recommendations §A1 và executor nội bộ §6). → Nếu bao giờ chạy experiment: **kết thúc bằng tay** trước hạn để tự quyết, hoặc biết trước rằng nó sẽ tự apply. |
| `research` §8 có "incrementality test" ở nhịp **quý** | **MỚI** | Đó là khái niệm khác (đo tác động tăng thêm của cả kênh). Campaign experiment là công cụ cụ thể của Google Ads. Không thay nhau. |

---

## E3. Insights page

Nguồn: [About the Insights page](https://support.google.com/google-ads/answer/10256472?hl=en) · [Demand forecasts on the Insights page](https://support.google.com/google-ads/answer/10787044?hl=en) · [Why you might not have insights](https://support.google.com/google-ads/answer/10260432?hl=en) · [About explanations](https://support.google.com/google-ads/answer/9000655?hl=en) · [Auction insights](https://support.google.com/google-ads/answer/2579754?hl=en) (2026-07-28)

### Google dạy

Vị trí: `Campaigns` → `Insights and reports` → `Insights`. Toggle **7 ngày / 28 ngày**. > "Insights **update daily**, and you can check back frequently for new insights that may appear."

| Loại insight | Google nói gì | Điều kiện xuất hiện |
|---|---|---|
| **Search trends** | "help you understand the search volume for products and services relevant to your business" | Cần "categories related to your business that are **significantly trending**" |
| **Demand forecasts** | "predicted upcoming search demand"; dùng historical data để forecast "within the next **180 days**" | Cùng điều kiện category-trending |
| **Search terms insights** | "how your target market is searching for and engaging with your business" | Cần "**sufficient search query data** for the relevant search categories" |
| **Audience insights** | "characteristics of the people and audience segments" | Cần "sufficient impressions, interactions, and **unique converters**" |
| **Budget pacing insights** | "how your campaigns are spending their budgets" | Campaign có average daily target, đã chạy đủ lâu |
| **Diagnostic insights** | "common reasons why your campaign may **not be serving** or getting conversions" | Campaign tương thích; không nêu ngưỡng số |
| **Performance shifts** | "significant changes in your campaign's performance… explanations of the **root causes**" | Thay đổi đáng kể ở goal-aligned metric trong 7/28 ngày |
| **Auction insights** | 6 chỉ số: impression share, overlap rate, outranking share, position above rate, top of page rate, absolute top of page rate. Nay có cả trong **Report Editor** ở cấp account/manager | Đủ dữ liệu đấu giá |
| **Explanations** | "insights into large changes in your Google Ads account performance"; hover giá trị có **đường gạch xanh** | Chỉ Search/App/PMax/Demand Gen/Display/Video. ⚠️ > "You **won't** have explanations if your date range contains **today's date**" |

**Vì sao không thấy insight:** > "Your account doesn't have any campaign currently compatible with a given insight type" hoặc "Google Ads hasn't found any significant changes in your performance." → **Không thấy ≠ lỗi cấu hình.**

Insights page đã **rollout toàn cầu** *(trang [answer/10568762](https://support.google.com/google-ads/answer/10568762?hl=en-GB) — chỉ lấy được qua snippet, tin cậy thấp hơn)*.

**Demand forecasts cho VN / ngành BĐS: CHƯA XÁC NHẬN.** Trang không nêu giới hạn quốc gia hay vertical, nhưng cũng không xác nhận phủ hết. Cơ chế phụ thuộc việc Google phát hiện category "significantly trending" → nếu không có, insight **đơn giản là không xuất hiện**, không phải bị chặn cứng theo geo.

### So với hệ hiện tại — dùng ở checklist tuần nào

Đã vá vào `playbook/monitoring.md` §4 theo phân chia sau:

**Nhịp TUẦN (thứ 4, ~5 phút) — 3 insight:**
1. **Diagnostic insights** — bắt sớm "campaign không serving / không có conversion". Đây là **cái duy nhất** có thể phát hiện sự cố *trước* khi alert của hệ nổ, vì nó đọc từ phía Google (policy, bid quá thấp, LP bị chặn) chứ không phải từ số liệu.
2. **Budget pacing insights** — hệ đã tự làm pacing (`monitoring.md` §1) nhưng đây là bản của Google, đối chiếu miễn phí.
3. **Performance shifts / Explanations** — chỉ hiện khi có biến động đủ lớn; nhớ **không** chọn khoảng ngày chứa hôm nay.

**Nhịp THÁNG — 5 insight còn lại** (`Search trends`, `Demand forecasts`, `Search terms insights`, `Audience insights`, `Auction insights`): tất cả đều cần tích luỹ volume/impression/converter. Ở **12-29 lead/tháng**, `Audience insights` (cần "unique converters") gần như **không xuất hiện**. Xem hàng tuần là mất thời gian.

| Điểm | Nhãn | Chi tiết |
|---|---|---|
| Insights page thay được việc thủ công nào? | **Một phần — không nhiều** | `research` §8 nhịp tuần T5 đã có **Auction Insights** (giữ nguyên, chỉ chuyển sang nhịp tháng cho phần đọc xu hướng). `Search terms insights` **không thay** được nghi thức search terms 3 lượt (`journey-plan` §5) — nghi thức đó cần **term thô** để soạn negative, còn insight là bản tổng hợp theo category. |
| `Diagnostic insights` là bổ sung thật | **MỚI — đáng thêm** | Rẻ (5 phút/tuần), và là góc nhìn từ phía Google mà hệ không tự dựng lại được. |
| Kỳ vọng đúng | **MỚI (chống thất vọng)** | Ở quy mô này, phần lớn insight sẽ **trống**. Đã ghi 1 dòng vào `monitoring.md` để không ai đi tìm bug. |

---

## E4. Verify claim "AI Max giữ search terms report đầy đủ" — KẾT LUẬN: **ĐÚNG**

Nguồn: [About reporting in AI Max](https://support.google.com/google-ads/answer/16470459?hl=en) · [How AI Max works](https://support.google.com/google-ads/answer/15910187?hl=en) · [About AI Max](https://support.google.com/google-ads/answer/15910366?hl=en) · [AI Max FAQ](https://support.google.com/google-ads/answer/15913066?hl=en) · [About the search terms report](https://support.google.com/google-ads/answer/2472708?hl=en) (2026-07-28)

### Kết luận: **CONFIRMED, có điều kiện diễn đạt**

Google **không** có một câu nguyên văn dạng "AI Max keeps the full search terms report". Kết luận dưới đây là tổng hợp từ 3 câu xác nhận độc lập — chắc chắn về nội dung, nhưng **không được trích như một quote đơn lẻ**.

**Bằng chứng 1 — search terms report vẫn là báo cáo chính cho AI Max** (answer/16470459):
> "The search terms report shows you how your ads performed when triggered by **actual searches** within the Search Network."
> "You can use this report to **understand AI Max automation traffic and its value**, assess headline and landing page relevance to search terms, and simplify your account structure with automation insights."

**Bằng chứng 2 — AI Max THÊM chiều dữ liệu, không bớt** (answer/15910187):
> "Includes '**AI Max**' as a new **match type** for those incremental search terms and a **source column** that shows if the match is because of **broad match expansion** or **keywordless matching**."
> "[There's] a new view that shows the **combined search term, headlines and URLs** to provide a full view into customer ad journeys."
Keyword report cũng có summary row "AI Max"; và có dòng **"Total: AI Max landing page matches"** = "Total traffic from search queries that matched because of your **landing pages or assets, outside of your keywords**."

**Bằng chứng 3 — KHÔNG có "search categories report" thay thế.** Không trang nào trong 5 trang đọc được đề cập báo cáo dạng *category* cho AI Max on Search (khác PMax, nơi Google dùng search **categories**). *Đây là bằng chứng phủ định (absence of evidence) — mạnh nhưng không tuyệt đối.*

**Giới hạn granularity duy nhất — và nó KHÔNG do AI Max** (answer/2472708):
> "Some search terms that don't have enough query activity are **omitted** from the search terms report in order to keep with our standards on **data privacy**."
Đây là ngưỡng privacy chuẩn, áp cho **mọi** Search campaign.

### So với hệ hiện tại

| Điểm | Nhãn | Chi tiết |
|---|---|---|
| `research` §1.3: "AI Max an toàn hơn PMax vì giữ search terms report + negative cấp campaign" | **KHỚP — claim đứng vững, đã bỏ nhãn CHƯA XÁC NHẬN** | Cả hai nửa của lý lẽ đều có xác nhận nguyên văn: negative ("Negative keywords will be respected even with AI Max turned on" — §A11) và search terms (3 bằng chứng trên). → **Lý do chính để hệ ưu tiên AI Max trước PMax là hợp lệ.** Đã vá vào `research/google-ads-bds-vn.md` §1. |
| Cột `source` (broad expansion vs keywordless) | **MỚI — hữu ích vận hành** | Khi bật AI Max, vòng negative tuần đọc được **traffic mới đến từ đâu**: broad expansion (siết bằng negative) vs keywordless (siết bằng brand exclusion/URL exclusion). Hai loại rò rỉ khác nhau, cách chặn khác nhau. |
| View "search term ↔ headline ↔ URL" | **MỚI** | Đây là công cụ kiểm **message match** ở cấp truy vấn — đúng thứ QA Q2 (`journey-plan` §5) đang kiểm bằng tay. |
| Tab "Expanded final URL assets" | **MỚI** | Chỉ có nghĩa nếu bật final URL expansion — mà hệ đã quyết **TẮT** (§5.6). Không cần. |

---

## E5. Customer Match — điều kiện, upload, và tác động tới GĐ5 của journey-plan

Nguồn: [About Customer Match](https://support.google.com/google-ads/answer/6379332?hl=en) · [Customer Match policy](https://support.google.com/google-ads/answer/6299717?hl=en) · [Create a Customer Match list by uploading a data file](https://support.google.com/google-ads/answer/10589050?hl=en) · [Data Manager API — Customer Match](https://developers.google.com/data-manager/api/devguides/audiences/google-ads/customer-match) · [Send audience members](https://developers.google.com/data-manager/api/devguides/audiences/send-audience-members) · [UserData reference](https://developers.google.com/data-manager/api/reference/rest/v1/UserData) · [Consent reference](https://developers.google.com/data-manager/api/reference/rest/v1/Consent) (2026-07-28)

### (a) Eligibility — phát hiện quan trọng nhất của cả vòng 2

Yêu cầu chung để **truy cập** Customer Match: > "A good history of policy compliance" · > "A good payment history".

**Ngưỡng $50.000 CHƯA bị xoá — nhưng nó chỉ gate MỘT tính năng:**
> tài khoản cần "**90 days of Google Ads history and more than USD $50,000 total lifetime spend**" để mở khoá setting **`Targeting`** (target thật + bid adjustment thủ công).
Dưới ngưỡng: chỉ được **`Observation`** và **`Exclusions`**.

Yêu cầu privacy:
> "Ensure that your **privacy policy discloses that you share customer data with third parties** to perform services on your behalf."
> "Obtain consent for such sharing where required by law or any applicable Google policies."
Dữ liệu phải là **first-party**: "collected from your websites, apps, physical stores, or other situations where customers shared their information **directly with you**."

*(Ghi chú tin cậy: nội dung trang policy lấy qua WebFetch. Đây là điều khoản Google cập nhật thường xuyên → **verify lại trực tiếp trên trang live trước khi triển khai**.)*

### (b) Campaign type
> "Customer Match is currently available on **Search, the Shopping tab, YouTube, Gmail, and Display**."
Auto-inclusion (khác targeting thường): "available for YouTube, YouTube Video Action campaign, and **will soon be available** for in-feed ads and Search ads."
Rule riêng cho Search ngoài ngưỡng $50k: **CHƯA XÁC NHẬN**.

### (c) Kích thước & thời hạn list
> "Customer Match lists have a maximum membership duration of **540 days**. Any list memberships added or refreshed more than 540 days ago will no longer be eligible."
> "To stay eligible, a list must have at least **100 members** added or updated within the last 540 days."
Match rate chỉ hiện "for uploads using the new Google Ads API with at least **100 rows matched to unique users**". *(Ngưỡng serve chính xác riêng cho từng network Search/Display/YouTube/Gmail: **CHƯA XÁC NHẬN** — chỉ có 1 nguồn.)*

### (d) Đường upload

**UI:** `Tools` → **Audience manager** → `+` → **Customer list**.

**Hashing & normalization (dùng chung cho UI và API):**
- > "you can hash your customer data yourself using the **SHA256** algorithm, or Google Ads will hash it for you using the same SHA256 algorithm."
- Email: > "**Lowercase** all characters. Remove any extra spaces before and after, or in between the email address."
- Tên: > "Lowercase all characters. Remove any extra spaces before and after." (API bổ sung: "no punctuation")
- Phone: > "Include the **country code** and '+' sign" — **E.164**.
- **Country và Zip KHÔNG hash.**
- ⛔ **Luật gmail bỏ dấu `.` / cắt `+suffix`: KHÔNG áp cho Customer Match — ĐÃ CHỐT ở vòng 3.** Xem §F6(b).

**Data Manager API** — thay luồng 3 bước cũ của Google Ads API (`OfflineUserDataJob` → add operations → run) bằng **một** `IngestAudienceMembersRequest`.
- `UserIdentifier` là **union field** (chỉ 1 loại/identifier): `emailAddress` (SHA-256 sau normalize) · `phoneNumber` (SHA-256, E.164) · `address` (`givenName`/`familyName` lowercase + no punctuation + SHA-256; `regionCode` = ISO-3166-1 alpha-2; **`postalCode` không hash**).
- > "At least one identifier is required"; tối đa **10 identifiers** / AudienceMember.
- **Consent:** object `Consent` có `adUserData` và `adPersonalization`, enum `CONSENT_STATUS_UNSPECIFIED` / `CONSENT_GRANTED` / `CONSENT_DENIED`. Schema đánh dấu **"Optional"** ở tầng API. → **CHƯA XÁC NHẬN** liệu policy pháp lý có bắt buộc gửi (ví dụ user EEA/UK) độc lập với schema. Với traffic VN rủi ro thấp hơn nhưng phải rà trước khi go-live.
- `termsOfService.customerMatchTermsOfServiceStatus` (`ACCEPTED`/`REJECTED`) — cần `ACCEPTED` để dùng cho mục đích Customer Match; tài liệu reference không nói rõ tính bắt buộc (**CHƯA XÁC NHẬN**).

### (e) Dùng làm exclusion
~~**CHƯA XÁC NHẬN bằng câu trích trực tiếp.**~~ → ✅ **ĐÃ XÁC NHẬN ở vòng 3** (answer/2549058, gồm cả PMax + bẫy "không cài được lúc tạo campaign"). Xem **§F6(d)**.

### (f) Việt Nam
~~**CHƯA XÁC NHẬN.**~~ → **ĐÓNG ở vòng 3: không có nguồn để xác nhận.** Google không publish danh sách quốc gia cho Customer Match ở bất kỳ trang nào đọc được → chuyển từ "việc research" sang "việc kiểm trong tài khoản". Xem **§F6(a)**.

### PMax New Customer Acquisition (NCA)
Từ [Using new customer acquisition goal with store goals](https://support.google.com/google-ads/answer/14005976?hl=en): > "Existing customer lists that you share through **Customer Match** and label in the Conversions Summary Acquisition panel" là cách Google biết ai là khách cũ. Áp cho PMax, Search, Demand Gen. Trích trực tiếp được: > "Performance Max campaigns for **store goals** are only compatible with the **New Customer Only** mode."
⛔ **ĐÍNH CHÍNH vòng 3:** câu "user không match list + chưa convert trong **540 ngày** → new customer" là **suy diễn của agent vòng 2, KHÔNG có nguồn Google.** Vòng 3 đọc lại cả trang NCA bản chính (answer/12080169) và trang store-goals: **không trang nào nêu cửa sổ lookback nào.** Đừng trích con số này. Xem **§F1**.
→ ~~**Việc còn nợ:** fetch trang "About the new customer acquisition goal"~~ → **XONG ở §F1. Kết luận: KHÔNG bật NCA ở G4.**

### So với hệ hiện tại — PHẢI ĐỔI KẾ HOẠCH GĐ5

| Điểm | Nhãn | Chi tiết |
|---|---|---|
| `journey-plan` §2.1 GĐ5: "Demand Gen / Display **customer match** · Customer Match từ CRM: `lead_chua_booking`, `lead_qualified_chua_di_xem`" | **MÂU THUẪN THỰC CHẤT — ĐÃ VÁ** | Đây là **targeting**, cần >$50k lifetime spend. Ở 30tr₫/tháng (~$1.100) phải **nhiều năm** mới tới. → Kế hoạch GĐ5 như viết **không chạy được**. Đã thêm hộp chặn vào `journey-plan` §2.1 với 3 việc chạy được ngay: (1) **Exclusion** khách đã mua khỏi mọi campaign acquisition — việc đáng làm nhất, không bị ngưỡng chặn; (2) **Observation** để đọc chênh CVR; (3) remarketing GĐ5 thật thì đi bằng **audience GA4**, không bằng Customer Match. |
| Phần E-0 vòng 1 kỳ vọng Customer Match giải quyết "audience GA4 14 ngày là quá ngắn" | **Giải quyết một nửa** | Customer Match membership tới **540 ngày** — đúng thứ cần cho chu kỳ BĐS 3-12 tháng, và dùng được ở tier `Exclusions` **ngay bây giờ**. → **Loại trừ khách đã mua/đã cọc trong 540 ngày là làm được ngay**, đó chính là bài toán gốc. Còn *nhắm* họ thì chưa. |
| Điều kiện privacy policy | **MỚI — việc phải làm ở LP** | "privacy policy discloses that you **share customer data with third parties**". LP hiện chưa có câu này (`tracking/lp-requirements.md`). Phải thêm **trước** lần upload đầu tiên, không phải sau. |
| Đường upload trùng với pipeline ECL | **KHỚP — tái dùng được** | Cùng Data Manager API, cùng SHA-256 + normalize, cùng service account. `tracking/upload_ecl.py` đã có `normalize_email`/`hash` dùng lại được cho audience ingest → thêm Customer Match là **thêm một endpoint**, không phải dựng pipeline mới. Khác biệt: endpoint `audienceMembers:ingest` thay vì `events:ingest`, và cần `termsOfService`. |
| Mốc 15/6/2026 (Data Manager API bắt buộc) | **KHỚP — nhưng có ghi chú nguồn** | Agent vòng 2 **không tìm thấy** ngày này trên trang API upload-offline-conversions và đánh dấu CHƯA XÁC NHẬN. **Vòng 1 đã có quote nguyên văn** từ support.google.com (§A10: "Starting June 15, 2026, offline conversions import and enhanced conversions for leads uploads will be migrated to the Data Manager API and blocked in the Google Ads API"). → **Claim của hệ vẫn đúng**; chỉ là trang API docs không nhắc lại. Không cần sửa gì. |

---

## E6. Consent mode: basic vs advanced

Nguồn: [About consent mode (developers)](https://developers.google.com/tag-platform/security/concepts/consent-mode) · [Consent guides](https://developers.google.com/tag-platform/security/guides/consent) · [About consent mode (Ads)](https://support.google.com/google-ads/answer/10000067) · [Obtain user consent](https://support.google.com/google-ads/answer/14009343) · [About consent mode modeling](https://support.google.com/google-ads/answer/10548233) (2026-07-28)

### (a) Khác biệt kỹ thuật

**Basic** — tag bị chặn hoàn toàn:
> "When the user doesn't consent, **no data is transferred to Google at all – not even the consent status**. Google tags are **completely blocked** from firing."
Bản Ads: > "No data is sent before a user consents - not even the default consent status".

**Advanced** — tag load, gửi cookieless ping:
> "When consent is `denied`, the Google tags **send measurements without cookies**."
Khi denied, tag vẫn gửi **consent state + cookieless pings** → Google biết *có* event xảy ra (khối lượng, thời điểm) dù không định danh user. Đây chính là nguyên liệu cho advertiser-specific modeling.

### (b) Bốn tín hiệu — cái nào cho cái gì

| Signal | Google định nghĩa | Ảnh hưởng |
|---|---|---|
| `ad_storage` | "Enables storage, such as cookies… related to **advertising**" | Cookie/click ID cho Google Ads conversion tracking + remarketing |
| `ad_user_data` | "Sets consent for **sending user data to Google** for online advertising purposes" | **Đây là tín hiệu của enhanced conversions / ECL** — bản chất ECL là upload user-provided data (email/phone hashed) |
| `ad_personalization` | "Sets consent for **personalized** advertising" | Remarketing list, personalized ads |
| `analytics_storage` | "…related to **analytics**, for example, visit duration" | GA4 |

Cho store sales: > "you must pass store sales data with consent values for **both `ad_user_data` and `ad_personalization`**".
Hậu quả khi denied: > "When a user denies consent, their data **isn't used for measurement and ad personalization**. If you don't send consent signals, you will **lose ads personalization capabilities**."

⚠️ **CHƯA XÁC NHẬN (một phần):** không tìm được **một câu duy nhất** dạng "enhanced conversions requires `ad_user_data=granted`" trên [answer/13258081](https://support.google.com/google-ads/answer/13258081) hay [answer/11021502](https://support.google.com/google-ads/answer/11021502) — hai trang đó chỉ nói "ads cookie subject to `ad_storage` consent status" + customer data policy. Kết luận "`ad_user_data` là tín hiệu của ECL" là **suy luận có cơ sở** từ định nghĩa chính thức của signal ("sending user data to Google for online advertising purposes") + field `ad_user_data` trong Consent object của API. **Xử lý ở mức suy luận mạnh, không phải quote 1:1.**

### (c) Modeled conversions

> "You have a daily ad click threshold of **700 ad clicks over a 7 day period, per country and domain grouping**."
> Cần "correctly implemented consent mode **or** the IAB Transparency & Consent Framework (TCF v2.0)".
> "After you've implemented consent mode for at least **7 full days**, Google Ads and Google Analytics may have enough data to report the uplift."

Chất lượng model theo mode:
- **Basic** (denied → không gửi gì) → chỉ **"General model (less detailed modeling)"**.
- **Advanced** (denied → cookieless ping) → **"Advertiser-specific model (more detailed modeling)"**.

→ **Basic VẪN có modeling** (miễn đạt 700 clicks/7 ngày/country-domain), chỉ là model chung, kém chi tiết. Advanced mới có model riêng theo advertiser.

### (d) Không cài CMP, không gọi `gtag('consent',…)` → đó là **"no consent mode"**

> "The default behaviors work as if **all consent options are granted**: `ad_storage='granted'` and `analytics_storage='granted'`"
✅ **URL ĐÃ VERIFY (vòng 3, 2026-07-28):** [support.google.com/analytics/answer/9976101](https://support.google.com/analytics/answer/9976101?hl=en), tiêu đề chính thức **"Consent mode on websites and mobile apps"**, mục *Consent mode behavior*. Câu trích khớp **nguyên văn**. → Cảnh báo cũ đã gỡ, quote này **dùng được cho khách**.

→ Quan trọng: **không cài gì ≠ basic mode.** Cả basic và advanced đều là trạng thái *đã kích hoạt* consent mode với default `denied` cho tới khi user thao tác. Không triển khai gì = tag chạy như trước khi consent mode tồn tại, coi như mọi signal `granted`.

**Phạm vi áp dụng theo vị trí END-USER, không phải trụ sở advertiser:**
> "you must collect consent for use of personal data from **end users based in the EEA**"
Phạm vi chính sách: **EEA + UK + Switzerland**. → Advertiser VN quảng cáo cho khách EU **vẫn phải** tuân thủ.

### (e) Non-EEA (Việt Nam)
**CHƯA XÁC NHẬN.** Không trang Google nào nêu tên "Vietnam" hay nói rõ "consent mode is optional outside EEA". Chỉ có phạm vi chính sách EEA/UK/CH. Suy luận (không phải quote): site chỉ phục vụ traffic VN **không bị EU user consent policy của Google bắt buộc** triển khai consent mode. Nghị định 13/2023 của VN nằm **ngoài** phạm vi tài liệu Google → cần ý kiến pháp lý, không phải research thêm.

### So với hệ hiện tại

| Điểm | Nhãn | Chi tiết |
|---|---|---|
| `tracking/gtm-container-spec.md` §5 + `lp-requirements.md` §1.1: `gtag('consent','default',…)` EEA/UK **denied**, phần còn lại **granted** | **MỚI — cần đặt tên đúng** | Đây **không phải** basic mode và **cũng không phải** advanced mode theo cách Google phân loại. Đó là **consent mode đã kích hoạt, với default `granted` cho VN và `denied` cho EEA/UK**. Với traffic VN (100% hiện tại) hành vi **tương đương "no consent mode"** — tag chạy đủ. Với khách EEA/UK: hiện đang ở **hành vi basic** (denied → chặn) vì chưa có CMP để gọi `update`. **Doc của hệ nên gọi đúng tên** để người sau không nhầm là "đã có advanced mode". |
| `ad_storage` + `ad_user_data` khai cho tag `[GAds] - *` và Conversion Linker | **KHỚP — đã đúng** | `gtm-container-spec.md` §5 bảng consent đã khai đủ cả hai (D1 #8c: **đã xong**). Đây là cấu hình quyết định ECL chạy hay không, và nó **đúng**. |
| Nếu bao giờ nhắm Việt kiều EU/UK | **MỚI — quyết định then chốt, chưa cần bây giờ** | Phải chọn **basic vs advanced** trước khi gắn CMP: **basic** = an toàn pháp lý nhất, mất dữ liệu nhiều, chỉ có general model; **advanced** = giữ được modeling riêng của advertiser, nhưng tag vẫn load và gửi cookieless ping khi denied → phải chắc chắn hợp pháp ở thị trường đó. Ngưỡng để modeling hoạt động: **700 ad clicks / 7 ngày / country+domain** — với một campaign Việt kiều nhỏ, **gần chắc chắn không đạt** → chọn advanced để "có modeled conversions" là kỳ vọng sai. |
| Ràng buộc đã biết: `ad_user_data=denied` ⇒ ECL không chạy | **KHỚP (suy luận mạnh, xem cảnh báo (b))** | Giữ nguyên trong doc, nhưng nên ghi là suy luận từ định nghĩa signal, không phải quote. |
| `research`/`tracking` chưa nói modeling | **MỚI (nhỏ)** | Không cần vá: ở traffic 100% VN `granted`, **không có gì để model** — modeled conversions chỉ có nghĩa khi có consent bị denied. Ghi ở đây để không ai đi tìm "vì sao không thấy modeled conversions". |

---

## E7. Clarity custom tags API — cú pháp đã verify

Nguồn: [Clarity API](https://learn.microsoft.com/en-us/clarity/setup-and-installation/clarity-api) · [Custom tags](https://learn.microsoft.com/en-us/clarity/filters/custom-tags) · [Identify API](https://learn.microsoft.com/en-us/clarity/setup-and-installation/identify-api) · [Consent API v2](https://learn.microsoft.com/en-us/clarity/setup-and-installation/clarity-consent-api-v2) · [Consent Mode](https://learn.microsoft.com/en-us/clarity/setup-and-installation/consent-mode) · [Filters](https://learn.microsoft.com/en-us/clarity/filters/clarity-filters) (2026-07-28)

### URL docs mới (giải quyết 404 của vòng 1)

| Nội dung | URL hiện hành |
|---|---|
| Client API (custom tags, identify, event) | `learn.microsoft.com/en-us/clarity/setup-and-installation/clarity-api` |
| **Custom tags** (dùng để filter/segment) | `learn.microsoft.com/en-us/clarity/filters/custom-tags` ← **canonical mới** |
| Identify API | `…/setup-and-installation/identify-api` |
| Consent API v1 (deprecated) / **v2 (hiện hành)** | `…/clarity-consent-api-v1` / `…/clarity-consent-api-v2` |
| Consent Mode tổng quan | `…/setup-and-installation/consent-mode` |
| Filters & saved segments | `…/filters/clarity-filters` |

Microsoft đã **tái tổ chức docs**: đường dẫn `/clarity/custom-tags` có `canonicalUrl` trỏ về `/clarity/filters/custom-tags` (không 404 cứng). Đường cũ `/custom-tags/custom-tags` (hai cấp trùng tên) là cái trả 404 ở vòng 1.

### Cú pháp custom tags

```javascript
window.clarity("set", "key", "value")
window.clarity("set", "flight", ["flight1", "flight2"])   // array = gọi nhiều lần tuần tự
```
- `value`: **string hoặc array of strings**.
- > "The tag and its value **can't be longer than 255 characters**."
- > "A single page can have **no more than 128 tags**. Any other tags are ignored."
- Cấp project: > "There is **no limit** to the number of custom tags you can have." → không giới hạn tag distinct trong project, nhưng **≤128 lần gọi `set`/trang**.
- > "As you add the tag in your website code, it's updated in your project within **30 minutes to 2 hours**." (độ trễ hiện trong Filters UI, **không** phải độ trễ ghi dữ liệu)
- **CHƯA XÁC NHẬN:** docs **không** nói rõ phải gọi trước/sau khi Clarity snippet load, và **không** nói tag có áp **hồi tố** cho cả session hay chỉ từ lúc gọi. Thực hành an toàn: gọi sau khi `window.clarity` tồn tại, càng sớm càng tốt.

### Identify API
```javascript
window.clarity("identify", "custom-id", "custom-session-id", "custom-page-id", "friendly-name")
// → Promise<{ id: hash(custom-user-id), session, page, userHint }>
```
Chỉ `custom-id` là **bắt buộc**. Hashing:
> "Clarity **securely hashes** the `custom-id` on the client before being sent to Clarity servers."
> "Clarity doesn't store custom identifier as plain text… When you filter on a specific Custom user ID, Clarity hashes the input and matches it against the data."
`friendly-name` chỉ để hiển thị đẹp thay hash thô (không có thì `userHint` dạng `"Mo******************"`).

### Consent API
**v1 (deprecated nhưng còn chạy):** `clarity('consent')` / `clarity('consent', false)`.
**v2 (hiện hành):**
```javascript
window.clarity('consentv2', { ad_Storage: "granted", analytics_Storage: "granted" });
```
Cả hai field **Required**, giá trị `"granted"` | `"denied"`. Khi denied: > "no first-party and third-party cookies set… Clarity assigns a unique ID **per page view** and does not use cookies to persist session data."

🗓️ **Mốc quan trọng hệ chưa biết:** > "Starting **October 31, 2025**, Clarity begins enforcing consent signal requirements for page visits originating from the **EEA, UK, and Switzerland**. A valid consent signal is required to ensure full functionality." Và: "Consent Mode is **enabled by default** for all users originating from the EEA, UK, and CH." → Ngoài 3 vùng đó (gồm **VN**), Consent Mode của Clarity **không tự bật**.

### Filter / segment
> "Clarity's custom tags are customizable filters that allow you to analyze **recordings and heatmaps** in different directions."
> "You can create custom tags accessible through the **Recordings, Heatmaps, and Dashboard** sections… under the Filters section."
> "**Save your favorite filter combinations as a segment** so you can easily find them later."
Custom tag thuộc loại **universal filter**: > "This filter can be accessed Recordings, Dashboard, and Heatmaps vertical. You can share it and also **save it as a segment**."

### PII
- > "Clarity shouldn't be used on any websites/apps targeting users **under the age of 18**."
- Masking mặc định: > "We classify all **input box content, numbers, and email addresses** as sensitive content."
- ⚠️ **Khác với `identify` (tự hash), docs custom tags KHÔNG hề đề cập hash** → giá trị tag lưu và hiện **plain text** trong dashboard/filter UI. Microsoft không có cảnh báo tường minh "don't put PII in tags", nhưng vì thiếu cơ chế hash: **tuyệt đối không** đưa tên/SĐT/email vào giá trị tag. Chỉ nhãn nghiệp vụ.

### So với hệ hiện tại

| Điểm | Nhãn | Chi tiết |
|---|---|---|
| D3 #42 đề xuất "custom tag **thay** tracking template UTM" | ⛔ **BỎ QUA phần "thay" — mâu thuẫn với QA đã apply** | QA đã chốt `campaign-setup.md` §1.5.9: tracking template UTM là **bắt buộc**. Custom tag **không thay được** nó: template UTM phục vụ cả **Advertising dashboard native** của Clarity (spend/CPC cạnh dữ liệu hành vi), thứ custom tag không cấp. → Đã vá `tracking/clarity-checklist.md` §1c như lớp **BỔ SUNG**: cấp `traffic=ads` nhanh, độc lập với Ads, sống được cả khi tracking template bị xoá. Ghi rõ quan hệ "cộng vào nhau, không thay nhau". |
| Cú pháp | **ĐÃ VERIFY — 8 dòng code, 0 hạ tầng** | Đặt trong đúng đoạn LP đã capture gclid/utm của skill `ad-click-attribution`. Snippet đầy đủ ở `clarity-checklist.md` §1c. |
| Consent enforcement 31/10/2025 cho EEA/UK/CH | **MỚI** | Không ảnh hưởng traffic VN (Consent Mode không tự bật). Chỉ thành vấn đề nếu chạy campaign Việt kiều EU/UK — lúc đó phải gọi `consentv2` **cùng lúc** với việc gắn CMP cho Google. Ghi để không quên một nửa. |
| Skill `ad-click-attribution` cần sửa để chèn 3 dòng | **Chờ QA** | File skill nằm ngoài phạm vi được phép sửa vòng này (skill đã cài, không phải doc của hệ). Diff đề xuất ở mục "Chờ QA". |

---

# Changelog vòng 2 — 2026-07-28

Mỗi dòng = 1 lần sửa tài liệu. Phạm vi được phép: mục **rủi ro TRUNG BÌNH (D2)** và **THẤP (D3)** của Phần D, tất cả đều là file `.md`. **Không** sửa `*.py`, `*.sh`, `keywords/*.csv`, `gen.py`, `CLAUDE.md`, `PLAN.md` → xem mục **Chờ QA**.

| # D | File:dòng | Trước → Sau |
|---|---|---|
| D2-10 | `research/google-ads-bds-vn.md:11` | "Demand Gen … (min $5/ngày bắt buộc)" → "Min **kỹ thuật** thấp (~$5/ngày) nhưng **best practice Google là $100+/ngày cho maximize strategies, hoặc ≥10× tCPA/ngày**" + link doc |
| D1-4 (đồng bộ) | `research/google-ads-bds-vn.md:13` | Display row: "CHỈ remarketing" → thêm "⚠️ Từ 6/2026 Display đang bị migrate vào **Demand Gen** — không dựa vào việc tạo Display campaign mới" (khớp `journey-plan` §3 QA đã sửa) |
| D3-34 | `research/google-ads-bds-vn.md:19` | Claim AI Max search terms report **chưa xác nhận** → hộp "✅ **ĐÃ XÁC NHẬN**" với 3 quote nguyên văn (answer/16470459 + 15910187) + nêu rõ mất granularity chỉ là privacy threshold chung |
| D3-23 | `research/google-ads-bds-vn.md:50,52` | "**Thêm biến thể không dấu**" → "**Biến thể không dấu là BẮT BUỘC**" + hộp cảnh báo mới: negative **không** khớp close variant, tách bạch luật positive vs negative |
| D2-9 | `research/google-ads-bds-vn.md:59,63` | §3 match type đọc như **lệnh cấm** → thêm hộp 🎓 "Google chính thức khuyên gì — và vì sao hệ chưa làm": ABCs of Account Structure + 62% broad + điều kiện "critical to use Smart Bidding with broad match" → kết luận **gate, không phải cấm**; đánh dấu "cap 15% là luật nội bộ" |
| D3-22 | `research/google-ads-bds-vn.md:73` | (không có) → hộp 📉 "Search terms report LUÔN ẩn term ít volume" + 3 hệ quả (a) tổng click lệch (b) negative không phủ hết (c) GAQL `search_term_view` ≠ `campaign` |
| D3-38 | `research/google-ads-bds-vn.md:78` | (không có) → mục "Audience trên Search campaign — dùng ở chế độ `Observation`" (5 audience GA4, không đổi phân phối) |
| D3-48 | `research/google-ads-bds-vn.md:86` | Learning phase + 4 con số điều chỉnh ghi trung tính → thêm nguồn Google cho learning phase (PMax best practices) + hộp 🏷️ "**Luật NỘI BỘ, không phải citation Google**" cho tCPA ±15% / budget ±20% / chờ 4 tuần / broad cap 15% |
| D2-16, D2-17 | `research/google-ads-bds-vn.md:92` | "Dùng Seasonality adjustments cho event 1-7 ngày" (1 câu) → bảng so sánh **2 công cụ khác nhau** (seasonality adjustment vs seasonal **budget** adjustment) + hộp ❌ "Tết/tháng 7 âm KHÔNG dùng seasonality adjustment, xử bằng ngân sách tay" |
| D2-11 | `research/google-ads-bds-vn.md:114` | "Form submit raw \| **0-1**" → "\| **1**" |
| D2-11b | `research/google-ads-bds-vn.md:120` | (không có) → hộp "Không bao giờ đặt giá trị 0" + xác nhận **proxy value được Google cho phép** (trả lời open question `PLAN.md` §6.7) + ngưỡng VBB ≥15 conv **cấp account** |
| D3-37 | `research/google-ads-bds-vn.md:122` | (không có) → mục **Conversion Value Rules** (chỉnh giá trị theo geo/device/audience không sửa tag) |
| D3-31 | `research/google-ads-bds-vn.md:144` | Housing policy 1 dòng → thêm 3 chi tiết HEC: radius tối thiểu **1 km**, predefined Google audiences vẫn dùng được, Canada dùng 3 ký tự đầu postal code |
| D3-29 | `research/google-ads-bds-vn.md:146` | (không có) → 🚨 "Mạo nhận brand khác = **ĐÌNH CHỈ TÀI KHOẢN NGAY, KHÔNG CẢNH BÁO**" + ràng buộc cứng "LP phải nói rõ là đơn vị phân phối" + tên chính thức `Business information requirements` |
| D3-30 | `research/google-ads-bds-vn.md:147` | (không có) → mục "**Minh bạch chi phí**": `Giá Từ`/`Trả Trước Từ` phải là căn thật đang bán, không bỏ qua phí bắt buộc |
| D2-12 | `research/google-ads-bds-vn.md:149` | "**Làm advertiser verification sớm** — BĐS VN hay bị yêu cầu" → đính chính: không có nguồn Google cho claim đó; lý do đúng = "all advertisers will eventually be required" + **30 ngày không nộp = tạm ngưng** |
| D3-20, D3-39 | `research/google-ads-bds-vn.md:152` | (không có) → §7b mới "**Chống chỉ định**": Optimization score không phải KPI (dismiss cũng tăng score) · Ad Strength **không** vào Ad Rank/QS/auction wins · store visits **không** bật (mất search terms report) |
| D3-33 | `research/google-ads-bds-vn.md:176` | "Display remarketing 10-15% (list ≥100 user — ngưỡng đã hạ 12/2025)" → "Remarketing **Demand Gen** … `[3P: Search Engine Land, CHƯA xác nhận ở tài liệu Google]`; gate G2 đặt ≥1.000 nên vẫn an toàn" |
| D3-35 | `research/google-ads-bds-vn.md:186` | Khoảng trống 3 mục → thêm mục 4: 🚨 rủi ro policy "**Affiliate networks and lead generation businesses are prohibited**" cho sàn phân phối, phải verify trước khi đầu tư lead form |
| E5 | `research/google-ads-bds-vn.md:187` | (không có) → Khoảng trống mục 5: **Customer Match $50k chỉ gate `Targeting`**, dưới ngưỡng chỉ `Observation`/`Exclusions`; VN CHƯA XÁC NHẬN |
| D3-48b | `research/google-ads-bds-vn.md:190` | Nguồn chính: "Search Engine Land (… lead form $50k dropped)" → thêm "**3 claim cuối đã bị đính chính/đánh dấu 3P bằng doc Google**" |
| D2-12 | `playbook/campaign-setup.md:27` | §1.1 "BĐS VN hay bị Google yêu cầu xác minh" → lý do đúng: "all advertisers will eventually be required" + **30 ngày → TẠM NGƯNG** |
| D3-24 | `playbook/campaign-setup.md:60` | (không có) → ô **1.2.7**: chọn đúng **goal category** chuẩn Google cho cả 6 action (PMax/AI Max/recommendation đọc theo category, không đọc tên) |
| D3-37 | `playbook/campaign-setup.md:61` | (không có) → ô **1.2.8**: Conversion Value Rules — biết là có, chưa làm ngày 1 |
| D3-28 | `playbook/campaign-setup.md:113` | §1.5.6 ACA "TẮT" → thêm mốc **9/2026 auto-upgrade ACA→AI Max**, **2/2027 DSA sunset**, rà lại **hàng tháng**, và **text disclaimers** là cơ chế khoá text bắt buộc |
| D3-23 | `playbook/campaign-setup.md:227` | §2.4.5 "Google tự khớp biến thể không dấu" → thêm "⚠️ **CHỈ đúng cho POSITIVE keyword**; negative không khớp close variant → biến thể không dấu là **bắt buộc**" |
| D3-25 | `playbook/campaign-setup.md:228` | (không có) → ô **2.4.6** mới: kiểm chứng **0 keyword nào ở match type Rộng** (broad là default, import thiếu cột = broad im lặng); ô Final URL dồn xuống 2.4.7 |
| (đồng bộ 1.5.11) | `playbook/campaign-setup.md:236,581` | "Áp toàn bộ §1.5 (**10 ô**)" / "áp 10 ô cài đặt" → **11 ô** (QA đã thêm 1.5.11 nhưng chưa sửa 2 chỗ đếm) |
| D3-29 | `playbook/campaign-setup.md:261` | §3 policy 1 đoạn → thêm 🚨 **RÀNG BUỘC CỨNG**: headline "Giá Gốc CĐT" chỉ dùng khi LP nói rõ là đơn vị phân phối; mọi `Giá Từ` phải có bảng giá làm bằng chứng |
| D2-14 | `playbook/campaign-setup.md:264` | (không có) → bảng **rubric ABCD** để review RSA (A✔ B✔ **C⚠️ yếu nhất** D✔) + luật "chấm ABCD trước khi đếm ký tự" |
| D2-14b | `playbook/campaign-setup.md:290` | Bộ 1 headline #9 `Xem Bảng Giá Từng Căn` (21, trùng #1/#2/#5/#15) → `Chọn Căn Cho Gia Đình 4 Người` (29) — thêm nhóm **C**, vẫn đủ 15 headline |
| D2-14c | `playbook/campaign-setup.md:315` | Bộ 2 headline #4 `Dự Án Căn Hộ {Quận} 2026` (24, trùng #2/#3) → `Nhà Mới Cho Gia Đình Trẻ` (24) — thêm nhóm **C**, bỏ luôn ràng buộc trần `{Quận}` |
| D2-13 | `playbook/campaign-setup.md:371` | **Sitelink (4)** → **Sitelink (6)**: thêm `Vị Trí & Kết Nối` → `#vi-tri` và `Tiện Ích Nội Khu` → `#tien-ich` (vẫn anchor trên chính LP) + ghi rõ **dynamic sitelinks KHÔNG bật** là đánh đổi có ý thức |
| D3-47 | `playbook/campaign-setup.md:540` | (không có) → §5.4 mới "**Ngân sách PMax 8% ở 150tr — ⚠️ QA CHƯA CHỐT**": 2 lựa chọn (dồn 1 asset group / hoãn sang Demand Gen), **chưa chốt thì không bật PMax** |
| D2-18c, D3-36 | `playbook/campaign-setup.md:549` | §5.3 dòng PMax 1 ô → §5.5 mới **checklist 12 bước dựng PMax**: TẮT URL expansion · audience signal chỉ là gợi ý · **exact keyword identical thắng PMax** (lá chắn brand) · asset ≥20 text + ≥7 image (3 landscape/3 square/1 portrait) + ≥1 video |
| D2-15 | `playbook/campaign-setup.md:568` | §5.3 dòng AI Max 1 ô → §5.6 mới **3 điều kiện cứng**: (a) không chạy với Manual CPC/Max Clicks (b) pinning H1 bị bỏ qua nếu bật text customization + final URL expansion (c) rà chéo 216 negative ↔ brand inclusions |
| D2-18b | `playbook/monitoring.md:14` | §1 bảng 3 nhịp → thêm hộp ⚠️ "**CPL theo NGÀY về bản chất là NHIỄU**" (Ads quy về ngày CLICK, GA4 ngày CONVERSION) + luật "quyết định chỉ ra ở mức 7-30 ngày" + **chốt đọc cột `Conversions`**, không `All conversions` |
| **E1** | `playbook/monitoring.md:24` | Alert 🔴 conversion=0/4h: "→ checklist audit nhanh" → "… → **nếu xác nhận tracking gãy >24h: tạo `Data exclusion`** (thủ tục §2.1)" |
| **E1** | `playbook/monitoring.md:33` | (không có) → §2.1 mới **"Tracking gãy → Data exclusion"**: 9 bước + điều kiện bidding + phủ ≥90% click + <14 ngày + backdate được + cấp MCC + UI path + phân biệt với seasonality adjustment |
| D2-17 | `playbook/monitoring.md:67` | (không có) → 2 dòng suggest mới: **Seasonal budget adjustment** (3-14 ngày, chỉ tăng, cách ≥7 ngày, không shared budget) và **Data exclusion** |
| D2-16 | `playbook/monitoring.md:71` | Suggest `Seasonality adjustment` chỉ có "Chỉ event 1-7 ngày" → thêm **2 GUARD bắt buộc**: (1) chỉ hợp lệ khi campaign chạy tCPA/tROAS — Max Clicks thì API từ chối (2) **CẤM** suggest cho Tết/tháng 7 âm |
| **E2** | `playbook/monitoring.md:76` | (không có) → §3.1 mới "Đổi bid strategy: dùng campaign experiment, đừng đổi thẳng" — bảng đánh đổi + kết luận **volume của hệ chưa đủ** → giữ đổi thẳng, mở experiment khi 1 campaign ≥30 conv/tháng |
| **E3** | `playbook/monitoring.md:93` | (không có) → mục **Insights page** trong §4: 3 insight nhịp **tuần** (diagnostic, budget pacing, performance shifts) vs 5 insight nhịp **tháng**; "không hiện ≠ lỗi cấu hình" |
| D3-27 | `playbook/monitoring.md:125` | §6 "Whitelist hành động được auto-apply khi duyệt" → thêm bảng 🚨 **CHỐNG LẪN TÊN**: auto-apply **NỘI BỘ** (có người bấm + guardrail + audit log) ≠ auto-apply **recommendations của Google** (đã TẮT ở §1.5.11, rà hàng tháng) |
| D2-18b | `playbook/monitoring.md:163` | Mẫu tin Telegram → thêm dòng chú thích cột (`Conversions`, quy về ngày CLICK) + dòng **7 ngày** ("số này mới dùng để quyết định") |
| D2-18 | `tracking/audit-monthly.md:44` | (không có) → §2.1 mới **"9 nguyên nhân lệch số Ads ↔ GA4 ↔ CRM"** (a-i, có cột "sửa được?") + bảng "tin nguồn nào cho việc gì" |
| D2-19 | `tracking/ecl-keap-pipeline.md:10` | (không có) → hộp 🔲 VERIFY: mốc **4/2026 ECL web + leads gộp thành 1 toggle**, doc viết theo mô hình 2 đường riêng → đối chiếu UI thật trước khi kết luận cấu hình sai |
| D3-33 | `tracking/ga4-setup.md:87` | "Ngưỡng Google Ads: list Display cần ≥100 user active/30 ngày" → đánh dấu **`[3P: Search Engine Land]`, CHƯA xác nhận ở tài liệu Google**; gate G2 ≥1.000 nên vẫn an toàn |
| D3-32 | `tracking/ga4-setup.md:127` | BigQuery "❌ chưa cần" → thêm **điều kiện mở lại** (né thresholding / join row-level) + cảnh báo **BigQuery không nhận data từ Google signals** → số event khác GA4 UI, không phải lỗi pipeline |
| D3-45 | `tracking/README.md:51` | Bảng skill: `ads-server-side-tracking` → thêm "⛔ **CHƯA MỞ**" + mục mới "**Điều kiện mở server-side tagging**": 3 điều kiện định lượng (>20% mất conversion / PII ra vendor / >150tr₫ + người vận hành GCP) + cạm bẫy cross-domain |
| **E7** / D3-42 | `tracking/clarity-checklist.md:34` | (không có) → §1c mới **Custom tags**: snippet 8 dòng đã verify cú pháp `clarity("set",k,v)`, ≤255 ký tự, ≤128 tag/trang, trễ 30'-2h, không hash → **không PII** + ghi rõ **KHÔNG thay** tracking template UTM (§1.5.9 QA đã chốt), chỉ **bổ sung** |
| D3-41 | `tracking/clarity-checklist.md:68` | §2 mục 4 lọc replay "thời lượng >60s + không có trang `/cam-on/`" → lọc bằng **Smart Event `Submit Form` = không xảy ra** |
| D3-41b | `tracking/clarity-checklist.md:73` | (không có) → §2a mới: **Smart Events** (⛔ không dùng làm nguồn conversion) · **Saved segments** (3 combo lưu sẵn) · **Copilot** để tìm replay đáng xem |
| D3-44 | `tracking/gtm-container-spec.md:210` | §6 bước 6 "Publish với **version name**" → thêm **version NOTE** bắt buộc + "không bao giờ publish mà chưa qua Preview" + nối vào alert 🟡 GA4 event ngừng bắn |
| **E5** | `playbook/customer-journey-plan.md:67` | §2.1 GĐ5 "Demand Gen / Display customer match" → sửa thành "Demand Gen customer match" + hộp ⛔ **CHẶN GĐ5**: $50k gate `Targeting` → hệ chỉ làm được **Exclusion + Observation**; remarketing GĐ5 đi bằng audience GA4; + yêu cầu privacy policy phải khai chia sẻ dữ liệu bên thứ 3 |
| D3-46 | `playbook/customer-journey-plan.md:165` | G5 điều kiện → thêm "**đã có media plan từ Reach Planner**" + đoạn phân vai: Reach Planner để **xin ngân sách**, brand search lift để **nghiệm thu** |
| D3-26 | `playbook/customer-journey-plan.md:168` | (không có) → §3.2 mới **"Gate nào mở khoá tính năng AI nào"** — bảng 6 bậc (0→5) map điều kiện ↔ tính năng ↔ "vì sao không sớm hơn" + kết luận "thứ mở khoá AI là dữ liệu conversion chất lượng, không phải ngân sách" |
| D3-23 | `keywords/adgroup-map.md:87` | §Match type "Không cần tạo dòng riêng cho keyword không dấu" → thêm ⚠️ "CHỈ đúng cho POSITIVE" + negative không khớp close variant + **broad là match type mặc định** → phải kiểm sau import |
| D2-9 | `keywords/adgroup-map.md:91` | (không có) → hộp 🧭 "**Gộp là mặc định, tách là ngoại lệ**": bản đồ này là cấu trúc mịn nhất có thể, không phải cấu trúc ngày 1; tách chỉ khi ad group ≥10 conv/tháng |
| D3-22 | `keywords/UPDATE.md:39` | (không có) → hộp 📉 search terms report ẩn term ít volume + 3 hệ quả áp thẳng vào vòng lặp GAQL/MCP ("không phải bug", "đừng đặt mục tiêu 0 term rác", "không trừ 2 con số") |
| D3-21 | `research/competitors/2026-07-eco-retreat.md:241` | "**Đo bằng:** Ad Strength + CTR ad group brand" → "**CTR + CVR + contact rate**" + đính chính nêu rõ Ad Strength không vào Ad Rank/QS/auction wins |

**Tổng: 60 lần sửa trên 13 file tài liệu** (+ chính file curriculum này: Phần E vòng 2, Changelog, Chờ QA).

### Mục Phần D đã BỎ QUA (mâu thuẫn với 8 mục QA đã apply hôm nay)

| # D | Đề xuất vòng 1 | Vì sao bỏ qua |
|---|---|---|
| D3-42 (nửa "thay thế") | Dùng Clarity custom tag **để bỏ** yêu cầu tracking template UTM cấp tài khoản | QA đã chốt `campaign-setup.md` §1.5.9 tracking template UTM là **bắt buộc**. Custom tag **không thay được** — template UTM còn phục vụ **Advertising dashboard native** của Clarity (spend/CPC cạnh dữ liệu hành vi). → Đã apply phần custom tag như lớp **BỔ SUNG** và ghi rõ quan hệ trong `clarity-checklist.md` §1c. Nửa "bỏ UTM" **không apply**. |
| D1-8c | Rà tag `[GAds] - *` phải có `ad_storage` + `ad_user_data` | **ĐÃ XONG TRƯỚC** — `tracking/gtm-container-spec.md:150` và bảng §5 đã khai đủ cả hai. Không sửa gì. |
| D3-43 | Đổi tên `[Setup] - GA4 Configuration` → `[Setup] - Google Tag` | **ĐÃ ĐÚNG TRƯỚC** — tag đang tên `[Setup] - Google tag (GA4)`, loại tag = `Google Tag`. Không sửa gì. |

---

# Chờ QA — không được tự sửa vòng này

Ba nhóm: **(A)** mục rủi ro CAO còn lại của Phần D (chỉ QA apply) · **(B)** file code · **(C)** file bị khoá (`PLAN.md`, `CLAUDE.md`, `keywords/*.csv`).

## A. Rủi ro CAO (D1) chưa apply — 3 mục

### A1 — D1 #3: `playbook/monitoring.md` §2, thiếu alert 🔴 advertiser verification
Đây là loại sự cố **giết cả tài khoản**, không chỉ 1 campaign: có yêu cầu verification mà **30 ngày không nộp → tạm ngưng** (§A15). Hiện `campaign-setup.md` §1.1 chỉ nói "3-5 ngày chờ" (thời gian **duyệt**), không có ai canh **deadline**.

```diff
--- a/playbook/monitoring.md   (§2, bảng guard liên tục)
+++ b/playbook/monitoring.md
 | 🔴 | Ad **disapproved / account limited** | Lý do policy + cách khắc phục theo research §7.3 |
+| 🔴 | **Có yêu cầu advertiser verification chưa hoàn thành** (đọc `Quản trị → Xác minh`) | Đếm ngược **ngày còn lại trong 30 ngày**; quá hạn = **tài khoản bị tạm ngưng**, không chỉ 1 campaign. Alert lại mỗi ngày từ D-10, không áp cooldown 2h |
```
Ghi chú thực thi: chưa rõ Google Ads API có expose trạng thái verification qua GAQL hay không → **nếu không có**, guard này phải là **nhắc lịch thủ công** (kiểm tay mỗi thứ 2), không phải alert tự động. QA chốt cách làm.

### A2 — D1 #6: `playbook/campaign-setup.md:98`, lý do chọn shared list là **SAI**
```diff
-> Google có thêm ô `Quản trị → Cài đặt tài khoản → Từ khoá phủ định của tài khoản` (giới hạn 1.000). Không dùng song song — 1 nơi duy nhất, tránh lệch phiên bản. Danh sách dùng chung thắng vì áp được cả cho PMax sau này (G4).
+> Google có thêm ô `Quản trị → Cài đặt tài khoản → Từ khoá phủ định của tài khoản` (giới hạn **1.000**). Không dùng song song — 1 nơi duy nhất, tránh lệch phiên bản.
+>
+> ⚠️ **Lý do cũ ("danh sách dùng chung thắng vì áp được cả cho PMax") là SAI.** Sự thật: **account-level negatives** mới là cái **tự áp** cho Search + PMax + App + Shopping + Smart + Local; **shared list phải gắn tay từng campaign** (§A12). Nếu mục tiêu là tự phủ PMax ở G4 thì nơi đúng là **account-level** (216 < trần 1.000 nên vừa).
+>
+> **QA chốt một trong hai** (quyết định "1 nơi duy nhất" giữ nguyên, chỉ chọn nơi nào):
+> - **Shared list** — linh hoạt (5.000/list, nhiều list, bật/tắt theo campaign), nhưng **phải gắn tay** mỗi campaign mới, kể cả PMax.
+> - **Account-level** — **tự phủ mọi campaign type** kể cả PMax, nhưng trần **1.000** và không tách được theo campaign (40 dòng `cap_do=campaign` vẫn phải gắn riêng).
```
Ảnh hưởng dây: nếu chọn account-level thì §1.4.1–1.4.4, §2.5 bước 9, §5.5 bước 6 và `keywords/adgroup-map.md` §"Negative keyword — nơi gắn" đều phải sửa theo. **Đây là lý do không tự apply** — nó là quyết định kiến trúc, không phải sửa câu.

### A3 — D1 #7: `tracking/ga4-setup.md` §1, chưa cấu hình attribution
```diff
--- a/tracking/ga4-setup.md   (§1 bảng cấu hình property)
+++ b/tracking/ga4-setup.md
 | Google signals | **ON** | Cần cho remarketing + demographic. Đánh đổi: data thresholding khi số nhỏ. |
+| Attribution model | **Data-driven** (mặc định) | `Quản trị → Cài đặt phân bổ`. Đây là cấu hình **của GA4** |
+| Key event lookback window | **90 ngày** (default 90; chọn được 30/60) | Khớp `cửa sổ chuyển đổi lượt nhấp` = 90 ngày ở Google Ads (`campaign-setup.md` §1.2.4) — chu kỳ BĐS 3-12 tháng |
+
+> ⚠️ **Model của GA4 và model của Google Ads là HAI cấu hình riêng biệt.** Đổi bên này **không** đổi bên kia. Đây là nguyên nhân lệch số (b) trong `tracking/audit-monthly.md` §2.1 — sẽ được hỏi mỗi tháng.
```
Lý do chờ QA: đây là D1 (rủi ro CAO) vì đặt sai lookback window làm lệch mọi con số đối chiếu, và nó là **thao tác trong tài khoản GA4 thật**, không chỉ sửa doc.

## B. File code — không sửa vòng này

### B1 — D1 #1 (phần code): `tracking/upload_ecl.py`, thiếu assert "upload ALL conversions"
Phần `.md` của mục này **QA đã apply** (`ecl-keap-pipeline.md:177` có hộp 🔒 LUẬT). Phần code chưa có assert canh gác. Google: "You must upload **ALL conversions** for the specified event, **including those not attributed to Google Ads**".

Đọc code hiện tại: logic ở dòng ~203 chỉ bỏ qua contact khi **không có gclid LẪN email/phone** (tức thiếu mọi identifier) — **đúng**, không filter theo gclid. Vậy đây là **thêm lưới an toàn**, không phải sửa bug:

```diff
--- a/tracking/upload_ecl.py   (trong selftest())
+++ b/tracking/upload_ecl.py
+    # Luat Google: phai upload MOI conversion cua event, ke ca lead khong do Ads mang lai
+    # (Facebook/organic/walk-in). Neu 100% record deu co gclid -> gan chac dang filter sai.
+    batch = [ev_with_gclid, ev_email_only]          # dung 2 fixture da co trong selftest
+    no_gclid = [e for e in batch if not e.get("adIdentifiers", {}).get("gclid")]
+    assert no_gclid, "moi record deu co gclid -> nghi dang filter theo gclid, VI PHAM luat upload-all"
```
Ngoài selftest, đề xuất thêm **1 dòng cảnh báo runtime** (không chặn): nếu trong 1 lần chạy thật mà `tỷ lệ record không có gclid == 0` và tổng record ≥10 → `log.warning`. Ở VN nhiều lead đến từ Zalo/organic nên tỷ lệ 0% là dấu hiệu bất thường.

### B2 — D1 #8b (phần selftest): `tracking/upload_ecl.py`, case gmail
Hàm chuẩn hoá **đã có** luật gmail (dòng ~77-86, QA đã apply). Chưa thấy case selftest khẳng định nó:
```diff
--- a/tracking/upload_ecl.py   (trong selftest())
+++ b/tracking/upload_ecl.py
+    assert norm_email("Nguyen.Van.A+bds@Gmail.com") == norm_email("nguyenvana@gmail.com"), "gmail dot/plus"
+    assert norm_email("a.b@yahoo.com") != norm_email("ab@yahoo.com"), "chi gmail moi bo dau ."
```
*(Tên hàm thật phải đọc lại trong file trước khi apply — dòng trên là ý đồ, không phải patch chạy được ngay.)*

### B3 — E1 (mới): suggest engine cần guard `data_exclusion`
`scripts/approve-bot.py` có whitelist 5 action. `data_exclusion` **không** nên vào whitelist auto-apply (nó là hành động sửa dữ liệu huấn luyện bidding, sai là hại dài hạn) — nhưng suggest engine cần guard để **không đề xuất** khi vô nghĩa:
```
guard: chỉ suggest `data_exclusion` khi campaign.bidding_strategy_type ∈
       {TARGET_CPA, TARGET_ROAS, MAXIMIZE_CONVERSIONS, MAXIMIZE_CONVERSION_VALUE}
       (Max Clicks/Manual CPC → API từ chối, và cũng không cần)
```
Cùng dạng guard đã đề xuất cho `Seasonality adjustment` (D2 #16, phần doc **đã apply** ở `monitoring.md` §3).

## C. File bị khoá

| File | Việc | Diff đề xuất |
|---|---|---|
| `PLAN.md` §6.6 | **E5** — quy trình sau-lead đang PENDING cần thêm ràng buộc Customer Match | Thêm sau dòng SLA 48h/7d: "**Customer Match ở quy mô hệ chỉ dùng được `Exclusion`/`Observation`** ($50k gate `Targeting`) → thoả thuận với người có quyền Keap cần thêm: (a) xuất list **khách đã cọc/đã mua** để loại khỏi campaign acquisition (membership tới 540 ngày); (b) **privacy policy trên LP phải khai có chia sẻ dữ liệu khách với bên thứ 3** trước lần upload đầu tiên." |
| `PLAN.md` §0.1 | **D2-9** đồng bộ giọng điệu | "1 Search campaign duy nhất, Phrase + Exact, Max Clicks có bid cap" → thêm "(bậc 0 của lộ trình 6 bậc — `journey-plan` §3.2; **không phải luật vĩnh viễn**, broad mở ở bậc 2 khi có Smart Bidding + ECL)" |
| `PLAN.md` §6.7 | **D2-11b** — open question đã có câu trả lời | "thang giá trị điểm hay ₫ thật" → **Google đã trả lời: proxy value được phép** ("utilize proxy values that align with your business priorities") → không cần ₫ thật để bắt đầu VBB. Có thể **đóng** open question này. |
| `keywords/negative-keywords.csv` | **D3-23** kiểm tra dữ liệu | Không sửa doc — **cần chạy kiểm**: mọi negative có dấu phải có dòng biến thể **không dấu** tương ứng (vì negative không khớp close variant). Nếu thiếu thì đây là rò rỉ ngân sách thật, không phải vấn đề tài liệu. Việc này thuộc agent `keyword-planner`. |
| Skill `ad-click-attribution` | **E7** — chèn custom tag Clarity | Thêm 3 dòng `window.clarity("set", …)` vào đoạn đã capture gclid/utm (snippet đầy đủ ở `tracking/clarity-checklist.md` §1c). Là file skill đã cài, không phải doc của hệ → QA quyết có sửa vendored skill hay chỉ để LP tự thêm theo `clarity-checklist.md`. |
| `tracking/lp-requirements.md` | **E5** | Thêm yêu cầu privacy policy: phải khai **"có chia sẻ dữ liệu khách hàng với bên thứ 3 để thực hiện dịch vụ"** — điều kiện bắt buộc của Customer Match. *(File này là `.md` và ở nhóm được phép, nhưng nội dung là yêu cầu pháp lý cho LP → để QA/legal chốt câu chữ thay vì agent tự viết.)* |

## Việc research còn nợ sang vòng 3

> **TRẠNG THÁI SAU VÒNG 3 (2026-07-28): 8/10 dòng dưới đây đã ĐÓNG** — 7 mục ở **Phần F** + Lead form policy do QA làm inline (`research/google-ads-bds-vn.md` §7). Còn mở đúng 2 dòng cuối (Nghị định 13 = việc pháp lý, Skillshop = cần login) và cả hai **không phải việc research**. Bảng dưới giữ nguyên làm lịch sử.

| Việc | Vì sao còn nợ |
|---|---|
| Trang **"About the new customer acquisition goal"** (bản chính, không phải store-goals) | Cần cho checklist G4/PMax NCA; vòng 2 chỉ fetch được bản store-goals |
| **Lead form policy** — đọc nguyên văn cả trang `adspolicy/answer/9472930` | Rủi ro "lead generation businesses are prohibited" cho sàn phân phối — vòng 2 chưa đọc toàn văn |
| **Lead Journey Mapping** | Vẫn chưa xác định được trang doc riêng |
| **Quality Score** đầy đủ (`answer/6167118`) vs skill `google-ads-quality-score` | Chưa đối chiếu |
| **Negative keywords in PMax** (`answer/15726455`) | Chi tiết thực thi cho G4 |
| **Google Ads announcements 2026** (`announcements/9048695`) + **GML 2026** (`answer/17100114`) | Danh sách thay đổi sản phẩm 2026 đầy đủ |
| Verify URL `support.google.com/analytics/answer/9976101` | Quote "default behaviors work as if all consent options are granted" ở §E6(d) chưa xác nhận được article ID |
| Customer Match: khả dụng **VN**, luật gmail dot/plus, tính bắt buộc của consent field, cơ chế exclusion audience | 4 mục CHƯA XÁC NHẬN ở §E5 |
| **Nghị định 13 / PDPL Việt Nam** | Ngoài phạm vi nguồn Google — cần ý kiến pháp lý, **không phải research thêm** |
| **Skillshop syllabus chính thức** | Cần đăng nhập — **bỏ qua vĩnh viễn** |

---

# PHẦN F — VÒNG 3 (VÒNG CUỐI): 7 mục nợ đã đóng

**Ngày truy cập nguồn: 2026-07-28.** Cùng luật nguồn với Phần A-E: chỉ `support.google.com`, `developers.google.com`, `blog.google`. Điểm không có câu xác nhận tường minh → ghi **CHƯA XÁC NHẬN**, không suy diễn.

⚠️ **Hạn chế công cụ của vòng này, ghi để người sau biết:** ngân sách **WebSearch của session đã cạn (200/200)** trước khi tới mục F7. Mọi kết luận dưới đây đến từ **WebFetch trực tiếp theo URL**. Hệ quả duy nhất: mục **F7 (Lead Journey Mapping)** không chạy được lượt tìm kiếm mới như đề bài yêu cầu — xem cách xử lý ở F7.

| § | Chủ đề | Kết quả một dòng | Đã vá vào |
|---|---|---|---|
| F1 | New customer acquisition goal | ⛔ **KHÔNG bật ở G4** — cần Purchase goal (hệ không có), và `New Customer Only` **bid loại** nhà đầu tư mua căn thứ 2 = nhóm CVR cao nhất của BĐS | `playbook/campaign-setup.md` §5.5 |
| F2 | Quality Score đầy đủ | 🚨 Skill `google-ads-quality-score` có **6 điểm MÂU THUẪN** với doc chính thức, trong đó **công thức CPC và "QS 6 mặc định" là SAI thẳng** | `research/google-ads-bds-vn.md` §7b + diff skill ở "Chờ QA vòng 3" |
| F3 | Negative keywords trong PMax | ⚠️ Negative **chỉ phủ Search + Shopping inventory** → nửa Display/YouTube của PMax hở, cần `Excluded content keywords` | `playbook/campaign-setup.md` §5.5 |
| F4 | Announcements 2026 + GML 2026 | 6 thay đổi; đáng chú ý nhất là **Ask Advisor** — đường auto-recommendation **thứ 4** chưa ai chặn | §F4 (bảng) — chưa vá file, xem "Chờ QA vòng 3" |
| F5 | Verify quote consent | ✅ **URL chính danh, quote khớp nguyên văn** → §E6(d) đã gỡ cảnh báo | §E6(d) |
| F6 | Customer Match 4 điểm | (a) VN **không có nguồn** → đóng · (b) luật gmail **KHÔNG áp** · (c) consent vẫn "Optional" ở schema · (d) exclusion ✅ + **bẫy: không cài được lúc tạo campaign** | §E5(d)(e)(f) + `journey-plan` §2.1 + `campaign-setup.md` §5.5 |
| F7 | Lead Journey Mapping | ⛔ **ĐÓNG VĨNH VIỄN** — không tồn tại như doc độc lập của Google | §F7 |

---

## F1. New customer acquisition goal — bản chính (không phải store-goals)

Nguồn: [Customer lifecycle goals / new customer acquisition goal](https://support.google.com/google-ads/answer/12080169?hl=en) · [Using NCA goal with store goals](https://support.google.com/google-ads/answer/14005976?hl=en) (2026-07-28)
*(URL không tồn tại — đã thử và 404, ghi để người sau khỏi thử lại: `developers.google.com/google-ads/api/docs/campaigns/bidding/new-customer-acquisition`, `.../performance-max/customer-acquisition`, `.../bidding/new-customer-acquisition`, `support.google.com/google-ads/answer/14090613`.)*

### Google dạy

**Định nghĩa:** > "The new customer acquisition goal is geared to optimize your campaigns to acquire new customers."

**Hai mode — khác nhau ở ĐIỀU KIỆN, không chỉ ở mức độ:**

| | **New Customer Value Mode** | **New Customer Only Mode** |
|---|---|---|
| Làm gì | > "prioritizes bidding towards new customers **while maintaining your engagement with potential returning customers**" | > "your campaigns are optimized to bid **exclusively** for new customers" |
| Bid strategy | **Chỉ** value-based: `Target ROAS` / `Maximize conversion value` | > "**All bid strategies**" |
| Purchase conversion goal | > "At least one Purchase conversion goal is **required**" | > "A Purchase conversion goal **isn't required, but recommended** for accurate reporting of new vs returning conversions" |
| Campaign type | Search, Performance Max, Shopping, Demand Gen | Search, Performance Max, Shopping, Demand Gen |

Ghi chú: **Retention mode** (mode thứ ba của cùng nhóm "customer lifecycle goals") **chỉ có ở Performance Max**.
Ràng buộc riêng đã biết từ vòng 2: > "Performance Max campaigns for **store goals** are only compatible with the **New Customer Only** mode."

**Google biết ai là khách cũ bằng cách nào — chỉ 2 đường:**
1. **Past online purchase conversions** (nếu có).
2. **Customer Match:** > "Existing customer lists that you share through **Customer Match** and label in the **Conversions Summary Acquisition panel**."
Với New Customer Only + promotions: > "first-party data through a **customer list and website tag**".
> "You can upload this definition through a customer list with Customer Match to be eligible."

⛔ **ĐÍNH CHÍNH claim vòng 2:** cửa sổ **"540 ngày"** để tính "new customer" là **suy diễn, KHÔNG có nguồn Google**. Vòng 3 đọc cả trang NCA bản chính và trang store-goals: **không trang nào nêu lookback window nào**. (540 ngày là thời hạn **membership của Customer Match list** — §E5(c) — hai thứ khác nhau, vòng 2 đã trộn lẫn.) §E5 đã được sửa.

**CHƯA XÁC NHẬN:** ngưỡng conversion tối thiểu để bật NCA · kích thước list tối thiểu · cơ chế autodetect khi **không** upload Customer Match list. Không trang nào đọc được nêu con số nào.

### Có nghĩa gì với BĐS — và vì sao KHÔNG bật

Đây là mục mà đọc đúng doc **đảo ngược** trực giác ban đầu ("khách BĐS mua 1 lần → NCA hợp lý").

| Rào | Chi tiết |
|---|---|
| **1. Không có Purchase goal** | Hệ đo `Qualified lead` / `Converted lead` (goal category, §1.2.7 `campaign-setup.md`), **không** phải Purchase. → **New Customer Value Mode loại thẳng** (Purchase là *required*). |
| **2. Cần Customer Match list trước** | New Customer Only *kỹ thuật* chạy được với mọi bid strategy, nhưng Google chỉ phân biệt cũ/mới qua Customer Match list **đã label trong Acquisition panel**. Ở G4 hệ chưa có pipeline upload audience (§E5(d) — mới chỉ có `events:ingest` cho ECL). → Bật mà không có list = mode không có dữ liệu để phân biệt. |
| **3. 🚨 Giả định "mua 1 lần" là SAI với BĐS VN** | Đây là lý do nặng nhất và **không đọc ra được từ doc Google**, phải ghép với thị trường: **nhà đầu tư mua căn thứ 2-3** và **khách đã cọc dự án A quay lại dự án B** là nhóm **CVR cao nhất, chi phí thuyết phục thấp nhất** của một sàn phân phối. `New Customer Only` "bid **exclusively** for new customers" → **bid loại chính nhóm đó**. Đổi lại được gì? Không gì cả, vì rào 1-2 khiến nó không hoạt động đúng ngay từ đầu. |
| **4. Việc thật cần làm thì đã có công cụ khác** | Mục tiêu chính đáng duy nhất ở đây là "đừng trả tiền quảng cáo cho người đã chốt xong". Công cụ đúng là **audience exclusion** (§F6(d)): chính xác hơn (chọn được đúng list nào), bật/tắt được **theo từng campaign**, và **không đụng vào bidding**. |

### → Checklist G4 (đã vá vào `playbook/campaign-setup.md` §5.5)

Một dòng, dạng chặn: **`New customer acquisition goal` = KHÔNG bật**, kèm 3 lý do trên. Điều kiện mở lại nếu bao giờ đổi ý:
1. Hệ có conversion action thuộc category **Purchase** phản ánh **hợp đồng đã ký** (không phải lead) — tức phải có ECL bậc sâu hơn hiện tại; **và**
2. Đã có pipeline `audienceMembers:ingest` chạy thật với list khách đã mua; **và**
3. Có bằng chứng số từ CRM rằng **tỷ lệ khách mua lần 2 < 5%** — nếu cao hơn thì rào 3 vẫn đứng, không mode nào chữa được.

---

## F2. Quality Score đầy đủ — đối chiếu skill `google-ads-quality-score`

Nguồn: [About Quality Score](https://support.google.com/google-ads/answer/6167118?hl=en) · [Check your Quality Score](https://support.google.com/google-ads/answer/2454010?hl=en) · [About Ad Rank](https://support.google.com/google-ads/answer/1752122?hl=en) (2026-07-28)
Skill đối chiếu: `.agents/skills/google-ads-quality-score/SKILL.md` (v1.0.0) — **lưu ý đường dẫn:** skill nằm ở `.agents/skills/`, **không** phải `.claude/skills/` như đề bài ghi.

### Google dạy — 5 câu nguyên văn là xương sống của cả mục

1. > "Quality Score is a **diagnostic tool** meant to give you a sense of how well your ad quality compares to other advertisers."
2. > "This score is measured on a scale from **1-10** and available at the **keyword level**."
3. > "Quality Score is **not a key performance indicator** and should **not be optimized or aggregated** with the rest of your data."
4. > "Quality Score is **not an input in the ad auction**. It's a diagnostic tool to identify how ads that show for certain keywords affect the user experience."
5. > "If you notice a '**—**' in the Quality Score column, it means there **aren't enough searches that exactly match your keywords** to determine a keyword's Quality Score."

**Ba thành phần** (tên chính thức): > "Expected clickthrough rate (CTR): The likelihood that your ad will be clicked when shown." · > "Ad relevance: How closely your ad matches the intent behind a user's search." · > "Landing page experience: How relevant and useful your landing page is to people who click your ad."
Mỗi thành phần nhận **Above average / Average / Below average**, > "based on a comparison with other advertisers whose ads showed for the **exact same search** over the last **90 days**."

**Cột historical VẪN TỒN TẠI:** `Quality Score (hist.)`, `Landing Page Exper. (hist.)`, `Ad Relevance (hist.)`, `Exp. CTR. (hist.)`.

**Ad Rank** ([answer/1752122](https://support.google.com/google-ads/answer/1752122?hl=en)): > "Ad Rank is a **set of values** that are used to determine whether your ads are eligible to show and if eligible, where on the page your ads are shown." Các yếu tố: **bid amount** · **ad and landing page quality** · **Ad Rank thresholds** · **auction competitiveness** · **search context** (location, device, time, search terms, các ad/kết quả khác, user signals) · > "the **expected impact of assets and other ad formats**". **Quality Score KHÔNG nằm trong danh sách này** — trang nói "quality of your ads and landing page", không gọi tên Quality Score. Trang **không** publish công thức CPC; chỉ nói > "even if your competition has higher bids than yours, you can still win a higher position at a lower price by using highly relevant keywords and ads."

### Đối chiếu skill — bảng KHỚP / MỚI / MÂU THUẪN

| # | Claim của skill (dòng) | Nhãn | Doc chính thức nói gì |
|---|---|---|---|
| 1 | "QS là diagnostic tool, not a direct ranking signal" (:40) · "QS is a diagnostic tool, not a goal" (:346) | ✅ **KHỚP — mạnh** | Khớp câu 1 và 3. Đây là điểm skill làm **đúng nhất**. |
| 2 | 3 thành phần + 3 status Above/Average/Below (:50-100) | ✅ **KHỚP** | Tên và thang khớp nguyên văn. |
| 3 | "Ad Rank uses **real-time quality signals** at auction time — not the stored QS number" (:44) | ✅ **KHỚP — thậm chí Google nói mạnh hơn** | Google: "QS is **not an input in the ad auction**." Skill diễn đạt nhẹ hơn sự thật. |
| 4 | "QS only applies to Search — not Shopping, Display, PMax" (:23, :361) | ✅ **KHỚP (suy luận mạnh)** | answer/2454010 chỉ nói "Quality Score for **Search** campaigns"; QS "available at the **keyword level**". Google **không** có câu phủ định tường minh cho từng campaign type → đúng nhưng là suy luận, không phải quote. |
| 5 | 🚨 **`Actual CPC = (Ad Rank của advertiser dưới bạn / Your Quality Score) + $0.01`** (:110) | ⛔ **MÂU THUẪN — SAI, phải XOÁ** | QS "**not an input in the ad auction**" → **không thể** là số chia trong công thức tính tiền. Google **không publish** công thức CPC nào. Đây là folklore SEM lưu truyền từ thời trước, giờ trái doc trực tiếp. |
| 6 | 🚨 **Bảng "QS vs CPC multiplier"**: QS 10 = −50%, QS 1 = **+400%** (:117-128) + ví dụ "$5.00 → $3.00, giảm 40%" (:131) | ⛔ **MÂU THUẪN — KHÔNG CÓ NGUỒN** | Suy ra trực tiếp từ công thức sai ở #5. Google không publish bất kỳ hệ số CPC theo QS nào. Bảng này khiến người dùng **hứa tiết kiệm bằng số** với khách — rủi ro cam kết sai. |
| 7 | 🚨 **"New keywords start at QS 6 by default"** (:20, :274, :349) | ⛔ **MÂU THUẪN — SAI** | Google: ô "**—**" nghĩa là "**there aren't enough searches that exactly match your keywords**". Không có giá trị mặc định 6. Skill dựa vào đây để khuyên "đừng chẩn đoán trong 30 ngày đầu" — **kết luận vẫn hợp lý**, nhưng **lý do thì sai**: đúng là "chưa có QS để đọc", không phải "QS đang là 6". |
| 8 | 🚨 **Trọng số ~55% Exp. CTR / ~22% Ad Relevance / ~22% LPE** (:52, :69, :85) | ⛔ **MÂU THUẪN — KHÔNG CÓ NGUỒN** | Google **không publish trọng số** cho 3 thành phần ở bất kỳ trang nào đọc được. Con số này là ước lượng ngành. Tác hại thật: nó điều hướng ưu tiên sửa lỗi (dồn vào Exp. CTR) bằng một số bịa. |
| 9 | 🚨 **"Google removed historical QS columns from the UI in 2022"** → khuyên dùng script / Optmyzr / Adalysis (:157, :304-313) | ⛔ **MÂU THUẪN — SAI và CŨ** | answer/2454010 liệt kê rõ **`Quality Score (hist.)`**, `Landing Page Exper. (hist.)`, `Ad Relevance (hist.)`, `Exp. CTR. (hist.)` chọn được ngay trong cột UI. → Cả 3 "Option" tracking của skill (script, snapshot tay, tool 3P) là **việc không cần làm**. |
| 10 | 🚨 **"What to track: Account-level weighted average QS (weighted by impressions)"** (:317) | ⛔ **MÂU THUẪN — trái lệnh trực tiếp** | Google: QS "should not be optimized **or aggregated** with the rest of your data". Skill khuyên đúng thứ Google cấm, ở dạng bắt mắt nhất (con số 1 dòng để báo cáo). |
| 11 | "Ad Rank = QS × bid × extensions" (:371, mô tả skill `google-ads-bidding`) | ⛔ **MÂU THUẪN** | Ad Rank là "a **set of values**" từ 6 nhóm yếu tố, **không** phải phép nhân, và **không có QS** trong danh sách. |
| 12 | Cửa sổ so sánh: skill nói "Set date range: **last 30 days** minimum (QS reflects recent performance)" (:152) | ⚠️ **MÂU THUẪN nhẹ — thiếu con số quan trọng** | So sánh của Google chạy trên **90 ngày**. Export 30 ngày không sai (đó là date range của *báo cáo*), nhưng skill **không hề nhắc 90 ngày** → người dùng sẽ tưởng sửa hôm nay là mai QS đổi. |
| 13 | "Pause and restart (last resort)… pausing for 30+ days and reactivating with a new ad group **resets the quality signal**" (:209) | ⚠️ **KHÔNG CÓ NGUỒN** | Không trang Google nào nói tạm dừng reset tín hiệu chất lượng. Folklore. Nguy hiểm vừa: mất 30 ngày traffic để đổi một thứ không chắc có. |
| 14 | Chẩn đoán theo thành phần: keyword vào Headline 1, tách ad group hẹp, không pin bừa, LPE = tốc độ + mobile + đúng intent (:188-268) | ✅ **KHỚP — phần giá trị nhất của skill** | Trùng tinh thần định nghĩa 3 thành phần và các best practice RSA/LP của Google (§A3, §A4). **Giữ nguyên phần này.** |
| 15 | "Pinning headlines để 'fix' ad relevance thường làm nó **tệ hơn**" (:351) | ✅ **KHỚP** | Nhất quán với cảnh báo pinning của Google ở RSA/AI Max (§A3, §A11). |
| 16 | Ô "—" là gì | 🆕 **MỚI — skill THIẾU HẲN** | Skill không giải thích ô "—" ở đâu cả (nó thay bằng huyền thoại "QS 6"). Đây là trạng thái người vận hành gặp **nhiều nhất** ở tài khoản BĐS mới với keyword đuôi dài ít volume. |

**Tổng kết vòng 3 cho skill này: 5 KHỚP · 1 MỚI (thiếu) · 8 MÂU THUẪN**, trong đó **#5, #6, #7, #9, #10, #11 là sai/không nguồn ở mức có thể dẫn tới hành động tốn tiền hoặc hứa sai với khách.**

### So với hệ hiện tại

| Điểm | Nhãn | Chi tiết |
|---|---|---|
| `research/google-ads-bds-vn.md` §7b đã có "Ad Strength **không** vào Ad Rank/Quality Score/auction wins" | ✅ **KHỚP — hệ đã đi đúng hướng** | Nay bổ sung tầng sâu hơn: **chính QS cũng không vào auction**. Đã thêm một dòng §7b (xem Changelog vòng 3). |
| Hệ chưa có chỗ nào chốt "cấm báo cáo QS trung bình" | 🆕 **MỚI — đã vá** | Với hệ có báo cáo tuần/tháng qua Telegram (`monitoring.md`), "QS trung bình tài khoản" là loại chỉ số **rất dễ bị thêm vào** vì nó gọn. Google cấm tường minh. Đã ghi thành hệ quả cứng ở §7b. |
| Ngày 1 hệ chạy Phrase + Exact, keyword đuôi dài BĐS | 🆕 **MỚI — kỳ vọng đúng** | Phần lớn keyword của hệ sẽ hiện **"—"**, không phải QS thấp. → Đừng lập KPI QS ở ngày 1, và đừng chẩn đoán "QS kém" khi thực ra là chưa đủ search khớp exact. |
| Skill này chưa được hệ dùng ở checklist nào | ⚠️ **Rủi ro tiềm ẩn** | Skill chưa vào workflow nào của repo (`monitoring.md`/`campaign-setup.md` không gọi nó). Nghĩa là 8 điểm sai **chưa gây hại** — nhưng nó sẽ tự trigger theo description khi ai đó nói "quality score" / "CPC too high". → Diff sửa skill ở "Chờ QA vòng 3". |

---

## F3. Negative keywords trong PMax — chi tiết thực thi cho G4

Nguồn: [Negative keywords in Performance Max](https://support.google.com/google-ads/answer/15726455?hl=en) · [About account-level negative keywords](https://support.google.com/google-ads/answer/11396330?hl=en) · [About your Google Ads account limits](https://support.google.com/google-ads/answer/6372658?hl=en) (2026-07-28)

### Google dạy

**Cấp campaign (PMax):** vào `Keywords` → tab **`Negative keywords`** → nhập mỗi dòng một term; > "you can **select an existing negative keyword list**" (→ **shared list dùng được cho PMax**). Match type khai bằng ký hiệu như bình thường (`"..."` phrase, `[...]` exact).

**Cấp account:** > "Negative keywords **automatically apply** to all Search and Shopping inventory, **including in your Performance Max campaigns**." Danh sách campaign type được tự phủ: > "all search and shopping inventory in **Search, Performance Max, App, Shopping, Smart, and Local** campaigns." Trần: > "A limit of **1,000** negative keywords can be excluded for each account."

🚨 **Giới hạn phạm vi — điểm quan trọng nhất của cả mục:**
> "Performance Max negative keywords are applicable to **Search and Shopping inventory only**."
→ PMax chạy trên nhiều inventory (Search, Shopping, **Display, YouTube, Discover, Gmail, Maps**). Negative keyword — dù cấp campaign hay cấp account — **chỉ chặn được phần Search + Shopping**. Phần Display/YouTube **không bị chặn**.

**Công cụ cho phần còn lại:** `answer/11396330` phân biệt tường minh một feature **khác**: **`Excluded content keywords`** — > terms "apply to all campaigns running on **YouTube or Display Networks**". Đây là hai ô riêng, không thay nhau.

**Trần dung lượng** ([answer/6372658](https://support.google.com/google-ads/answer/6372658?hl=en)):

| Giới hạn | Số |
|---|---|
| Negative keyword / **campaign** | > "**10,000** negative keywords per campaign" |
| Keyword / **negative keyword list** | > "**5,000** keywords per negative keyword list" |
| Số list ở **manager account** | > "maximum of **20** lists, and each child account can have up to **20** lists" |
| Negative keyword ở **cấp account** | **1.000** (nguồn answer/11396330) |
| Negative áp cho **Display Network + Video campaign** | > "A maximum of **1,000** negative keywords can be applied to Display Network and Video campaigns" |

**CHƯA XÁC NHẬN:** negative keyword / **ad group** (trang limits không nêu) · **tương tác brand exclusions ↔ negative keywords** — vòng 3 thử 4 URL cho trang brand exclusions, **cả 4 đều 404** (`answer/13425629`, `13276472`, `15127680`, `9271267`), và trang [How PMax interacts with other campaigns](https://support.google.com/google-ads/answer/13810170?hl=en) đọc được nhưng **không nhắc** brand exclusions. Vòng 1 §B đã ghi brand exclusions tồn tại **ở cấp campaign** — giữ nguyên mức đó, **không suy diễn thêm**.

### So với hệ hiện tại

| Điểm | Nhãn | Chi tiết |
|---|---|---|
| `campaign-setup.md` §5.5 bước 6: "account-level negatives **TỰ PHỦ PMax**" | ✅ **KHỚP — nhưng thiếu một nửa, ĐÃ VÁ** | Câu đó **đúng** ("including in your Performance Max campaigns"), chỉ là **chưa đủ**: nó chỉ phủ **Search + Shopping inventory**. Với BĐS, phần **YouTube/Display của PMax** là nơi dễ đốt tiền nhất (video giải trí, app game, parked domain) và 216 negative **không chạm tới**. Đã thêm hộp + yêu cầu điền `Excluded content keywords` như **ô thứ hai** ở G4. |
| QA đã chốt (`campaign-setup.md`:98) dùng **account-level** làm nơi duy nhất cho 216 dòng | ✅ **CỦNG CỐ — quyết định đúng, thêm bằng chứng thứ hai** | Đây cũng là câu trả lời cho mục **A2 "Chờ QA"** của vòng 2 (đã được QA đóng): account-level là nơi duy nhất **tự áp PMax**, shared list phải gắn tay. Vòng 3 xác nhận lại bằng nguyên văn. Ghi thêm: 216 / trần **1.000** = còn **784 slot** — đủ dư cho 2-3 năm bồi negative, chưa cần lo vượt trần. |
| Bước 7 §5.5: placement exclusion loại `App categories`/`Games` | ✅ **KHỚP — và giờ hiểu vì sao nó BẮT BUỘC** | Trước đây nó trông như "làm cho chắc". Giờ rõ: vì negative keyword **không phủ** Display/YouTube, placement exclusion + excluded content keywords là **công cụ duy nhất** cho phần inventory đó. Không phải tùy chọn. |
| `keywords/negative-keywords.csv` có 40 dòng `cap_do=campaign` | ⚠️ **Ghi chú thực thi** | 40 dòng đó vẫn phải gắn tay cho **mỗi** campaign mới kể cả PMax — nhưng shared list **dùng được** cho PMax ("you can select an existing negative keyword list"), nên nếu 40 dòng này thành 1 shared list thì gắn 1 lần/campaign thay vì dán 40 dòng. Việc của `keyword-planner`, không sửa ở vòng này. |

---

## F4. Google Ads announcements 2026 + Google Marketing Live 2026

Nguồn: [Google Ads announcements](https://support.google.com/google-ads/announcements/9048695?hl=en) · [See what we announced at GML 2026](https://support.google.com/google-ads/answer/17100114?hl=en) · [blog.google — Google Marketing Live 2026](https://blog.google/products/ads-commerce/google-marketing-live-2026/) (2026-07-28)

⚠️ **Ghi chú về độ phủ:** trang announcements/9048695 chỉ trả về **một** entry cho cả năm 2026 (**20/05/2026**), và nó chỉ trỏ sang GML. Trang answer/17100114 là **landing page**, không có nội dung sản phẩm — nó đẩy sang `accelerate.withgoogle.com/googlemarketinglive` (**ngoài 3 domain được phép**, không đọc). → Bảng dưới lấy từ **blog.google**, là nguồn Google chính thức nhưng ở dạng thông cáo, **không phải tài liệu tham chiếu**. Mọi dòng đều **chưa có trang support riêng** → coi là **tín hiệu định hướng, không phải spec để cấu hình theo**.

Entry 2026 duy nhất trên trang announcements (**20/05/2026**): > "See what we announced at Google Marketing Live 2026 on Accelerate with Google" — > "powerful new AI innovations built to help you create, capture, and convert demand".

### Bảng: thay đổi | ảnh hưởng gì tới hệ | cần làm gì

| Thay đổi (GML 2026, 20/05/2026) | Ảnh hưởng tới hệ | Cần làm gì |
|---|---|---|
| **New-generation ad formats built with Gemini in Search** — > "new ad formats built with Gemini in Search", > "instantly tailored to a person's unique query"; **Direct Offers** pilot mở rộng | ⚠️ **Rủi ro kiểm soát text.** Cùng họ với ACA/AI Max: Google sinh nội dung ad theo query. Hệ khoá message match bằng **pinning H1** (`campaign-setup.md` §3.1-3.3) — format sinh theo query có thể vượt qua lớp khoá đó. BĐS = ngành có rủi ro policy về giá/cam kết sinh lời | **Rà ô §1.5.6 hàng tháng** (đã là luật của hệ). Thêm vào phạm vi rà: bất kỳ toggle mới nào có chữ *Gemini*/*generated*/*tailored*. **Direct Offers** hướng thương mại điện tử → không liên quan BĐS, bỏ qua |
| **AI Max mở rộng: `AI Max for Shopping`, `AI Max for Travel`** — > "capturing even more opportunities in the expanding Search universe" | ✅ **Không đổi gì.** Hai biến thể này là **retail và travel**, **không có** biến thể BĐS. Hệ dùng **AI Max for Search** bản chung, gate ở G4+6 tuần (§5.6) | **Không làm gì.** Ghi ở đây để không ai tưởng có "AI Max for Real Estate" cần đợi. Giữ nguyên 3 điều kiện cứng §5.6 |
| **YouTube Demand Gen: creator partnership tools + AI-powered formats** — > "easier than ever for brands to discover and partner with YouTube creators" | ⚪ **Ngoài tầm ngân sách.** Demand Gen của hệ bị chặn bởi best practice **$100+/ngày** (§A13) → chỉ mở ở mức 150tr₫ (G5) | **Không làm gì ở 30tr₫.** Khi tới G5 thì đọc lại — creator tools có thể là đường vào rẻ hơn ad format thường cho dự án lớn |
| 🚨 **`Ask Advisor`** — > "**unified agent** built with Gemini" trải **Google Ads + Analytics + Merchant Center + Marketing Platform**; > "your always-on strategic partner, connecting the dots" | 🚨 **Đây là mục đáng lo nhất.** Hệ có luật "**người bấm nút chi tiền**" và đã chặn 3 đường auto-apply: (1) Google recommendations (§1.5.11 TẮT), (2) executor nội bộ (§6 `monitoring.md`), (3) experiment auto-apply khi hết hạn (§E2). Một **agent xuyên sản phẩm** là đường **thứ 4** — và nguy hiểm hơn 3 đường kia vì nó **không nằm trong Google Ads**, nên ô "TẮT auto-apply" ở §1.5.11 **không chắc phủ được nó** | **Chưa cấu hình được gì** (chưa có trang support, chưa rõ có toggle hay không). Việc phải làm: thêm **1 dòng rà hàng tháng** — "có tính năng Gemini/agent nào tự thay đổi tài khoản mà chưa ai bật không" — và khi Ask Advisor xuất hiện trong tài khoản thì **mặc định coi là TẮT cho tới khi QA duyệt**. → Đề xuất vào `monitoring.md`, xem "Chờ QA vòng 3" |
| **`Asset Studio`** — > "new multimodal capabilities", > "turn brand guidelines into high-performing creative, faster" | ⚪ **Có thể hữu ích, không cấp bách.** Điểm chặn thật của hệ ở PMax là **ảnh đúng 3 tỷ lệ** (§5.5 bước 3: 3 landscape + 3 square + 1 portrait) — ảnh flycam/nhà mẫu phải crop trước. Asset Studio *có thể* giải đúng việc đó | **Không làm gì trước G4.** Khi dựng PMax: thử **crop tỷ lệ**, **không** dùng để sinh nội dung mới (rủi ro policy BĐS — ảnh render ≠ thực tế dự án là *misleading representation*, §A15) |
| **Measurement: `Google Analytics 360` "command center"** + **`Meridian`** (open-source MMM) + **"Future Long-Term Conversions"** | ⚠️ **Hai trong ba ngoài tầm, một cái đáng theo.** GA360 = **trả phí enterprise** → không. **Meridian** (MMM) cần volume lớn + nhiều kênh → 12-29 lead/tháng không chạy nổi (cùng lý do experiment bị loại ở §E2). **"Future Long-Term Conversions"** thì đúng bài toán gốc của BĐS: chu kỳ **3-12 tháng**, conversion về sau khi click đã cũ | **Chỉ theo dõi "Future Long-Term Conversions".** Nếu nó thành tính năng có trang support, đó là thứ đáng đọc kỹ nhất trong cả GML 2026 cho hệ này — nó có thể thay/bổ trợ cách hệ đang xử lý conversion delay (`journey-plan` §4 còn `[điền]`, tạm dùng ≥3 ngày). **Chưa đổi gì bây giờ** |
| **Commerce: `Universal Commerce Protocol` (UCP) + `Universal Cart`** | ⚪ **Không liên quan.** Thương mại điện tử/giỏ hàng | **Bỏ qua vĩnh viễn** cho hệ BĐS lead-gen |

### Kết luận mục F4

**Không có thay đổi 2026 nào buộc hệ phải sửa cấu hình ngay.** Đúng **hai** thứ cần vào nhịp theo dõi: **Ask Advisor** (rủi ro auto-apply đường thứ 4) và **Future Long-Term Conversions** (cơ hội cho conversion delay dài của BĐS). Bốn thứ còn lại là bỏ qua hoặc để dành tới G5.

---

## F5. Verify quote consent — ✅ ĐÃ XÁC NHẬN

Nguồn: [Consent mode on websites and mobile apps](https://support.google.com/analytics/answer/9976101?hl=en) (2026-07-28)

**Kết quả:** URL `support.google.com/analytics/answer/9976101` là **chính danh**. Tiêu đề chính thức: **"Consent mode on websites and mobile apps"**. Câu trích ở §E6(d) xuất hiện **nguyên văn**, trong mục *Consent mode behavior*, ngay trước hai mục con *Web* và *Mobile apps*:

> "The default behaviors work as if all consent options are granted: `ad_storage='granted'` and `analytics_storage='granted'`"

→ **§E6(d) đã được sửa:** gỡ cảnh báo "CHƯA XÁC NHẬN tính chính danh của URL", thay bằng xác nhận + tên bài. Quote này **dùng được cho khách**.

**Điều này chốt kết luận nào:** trạng thái hiện tại của hệ với traffic VN (`gtag('consent','default',…)` = granted cho non-EEA) có **hành vi tương đương "no consent mode"** — tag chạy đủ, không mất dữ liệu. Và **"không cài gì" ≠ "basic mode"**, đây là chỗ dễ nhầm nhất khi ai đó hỏi "hệ đang ở consent mode nào". Nhãn đúng đã ghi ở §E6 bảng "So với hệ hiện tại", giờ có nguồn đủ vững để dùng trong tài liệu đối ngoại.

---

## F6. Customer Match — 4 điểm CHƯA XÁC NHẬN của §E5

Nguồn: [Customer Match policy](https://support.google.com/google-ads/answer/6299717?hl=en) · [Create a Customer Match list by uploading a data file](https://support.google.com/google-ads/answer/10589050?hl=en) · [About Exclusions](https://support.google.com/google-ads/answer/2549058?hl=en) · [Data Manager API — Send audience members](https://developers.google.com/data-manager/api/devguides/audiences/send-audience-members) (2026-07-28)

### (a) Khả dụng ở Việt Nam — ⛔ ĐÓNG: không có nguồn để xác nhận

Đọc lại **cả hai** trang chuẩn (policy + upload data file): **không trang nào có danh sách quốc gia**, không có mục "availability", không nêu quốc gia bị hạn chế nào. Kết hợp với vòng 2 (cũng không tìm được) → kết luận:

**Google không publish danh sách quốc gia cho Customer Match.** Đây **không phải** "chưa research đủ" mà là **không có tài liệu để research**. → Chuyển mục này từ *việc research* sang **việc kiểm trong tài khoản**: mở `Tools → Audience manager` xem tuỳ chọn **`Customer list`** có xuất hiện hay không. Nếu có, tính năng khả dụng cho tài khoản đó; nếu không, không có doc nào giải thích được vì sao. **Không lên kế hoạch phụ thuộc Customer Match trước khi kiểm.** (Điều kiện *account-level* đã biết và vẫn đúng: good policy compliance history + good payment history + $50k gate cho `Targeting`.)

### (b) Luật gmail bỏ dấu `.` / cắt `+suffix` — ⛔ KHÔNG áp cho Customer Match

Hai trang chuẩn hoá chính thức, cả hai đều **không** có bước này:
- [answer/10589050](https://support.google.com/google-ads/answer/10589050?hl=en) (UI upload): > "Include a **domain name** for all email addresses (for example, gmail.com or hotmail.co.jp). **Remove any spaces** in between the email address." Hết. Không nhắc dấu `.`, không nhắc `+`.
- [Data Manager API](https://developers.google.com/data-manager/api/devguides/audiences/send-audience-members): > "**removing whitespace, converting to lowercase, hashing with SHA-256, and encoding using hex or Base64**." Hết.

Chi tiết chuẩn hoá khác đã xác nhận ở trang UI: phone > "Format phone numbers using the **E.164** format. Include the country code" (dấu `+` được ghi là **optional** ở trang này — khác diễn đạt "phải có dấu +" mà vòng 2 lấy từ trang khác; dùng E.164 đầy đủ là an toàn cho cả hai) · first name > "Don't include prefixes (ex: Mrs.). **Accents are allowed**" · last name > "Don't include suffixes (ex: Jr.). Accents are allowed" · country > "**ISO two-letter or three-letter** country codes", phải điền **cả khi** toàn bộ data cùng một nước · zip: nhận cả 5-digit / 5+4 của Mỹ và postal code quốc tế.

🔒 **Kết luận chốt (đóng vĩnh viễn mục này):** **KHÔNG** áp luật gmail dot/plus cho Customer Match. Nếu tái dùng `normalize_email()` của `tracking/upload_ecl.py` cho `audienceMembers:ingest`, phải có **cờ tắt bước gmail** — vì luật gmail chỉ có nguồn cho **enhanced conversions / user-provided data** (§C2.9), không phải cho Customer Match. Áp bừa = hash ra chuỗi khác chuỗi Google mong đợi → **match rate tụt mà không có lỗi nào báo**. → Việc code, xem "Chờ QA vòng 3".

**Lưu ý "Accents are allowed":** với dữ liệu VN (`Nguyễn`, `Trần`) trang UI nói **giữ dấu được**. Nhưng `UserData` reference của API (§E5(d)) yêu cầu "lowercase + **no punctuation**" — **hai trang diễn đạt khác nhau**. → **CHƯA XÁC NHẬN** cách xử lý dấu tiếng Việt cho đường API. An toàn nhất: **dùng email/phone làm identifier chính, đừng dựa vào `address`** — vốn cũng là identifier match kém nhất.

### (c) Consent field có bắt buộc trong Data Manager API — ⚠️ vẫn CHƯA XÁC NHẬN (nhưng đã rõ hơn)

Trang `send-audience-members` **có** `consent` trong request example (`adUserData` / `adPersonalization` = `CONSENT_GRANTED`), nhưng **không có câu nào nói required hay optional**. Schema `Consent` (§E5(d)) vẫn đánh **"Optional"**.

Cái vòng 3 tìm thêm được — một ràng buộc **theo vùng, tường minh**:
> "Google Ads **does not support IP address matching** for end users in the European Economic Area (**EEA**), United Kingdom (**UK**), or Switzerland (**CH**). Add logic to **conditionally exclude** sharing IP addresses from users from these regions and ensure that you provide users with clear and comprehensive information about the data you collect… and **get consent where required by law** or any applicable Google policies."

→ Đọc đúng: nghĩa vụ consent là **pháp lý theo vùng**, **không** phải ràng buộc schema. API sẽ **không từ chối** request thiếu `consent`; vi phạm nằm ở tầng policy/luật, không ở tầng HTTP. **Đây là loại lỗi tệ nhất: không có thông báo lỗi.**

`termsOfService`: > "If sending audience members for **Customer Match**, set `termsOfService` to indicate whether the user has accepted the Customer Match terms of service." Diễn đạt điều kiện ("if… set"), **không** có chữ "required" → thực tế **bắt buộc cho Customer Match**, nhưng vẫn **CHƯA XÁC NHẬN** bằng câu nói thẳng.

**Luật thực hành cho hệ (nội bộ, không phải quote Google):** traffic 100% VN → gửi `consent` với `CONSENT_GRANTED` cho cả hai field, và **không gửi IP address** trong mọi trường hợp (hệ không thu IP, nên không phát sinh việc). Nếu bao giờ có lead EEA/UK/CH: **dừng, hỏi legal** trước khi upload — đừng để pipeline tự quyết.

### (d) Cơ chế exclusion audience — ✅ ĐÃ XÁC NHẬN

Trang: [About Exclusions: Exclude specific audience segments from your targeting](https://support.google.com/google-ads/answer/2549058?hl=en).

**Làm gì:** > "you can **remove specific types of segments** (for example, affinity or **your data**) from your campaign or ad group if they're not a good match for what you're advertising." (*your data* = nhóm chứa Customer Match list và audience GA4.)

**Cách tạo — 3 bước:**
1. `Audiences` → mục **`Exclusions`**
2. Drop-down **`Exclude from`** → chọn **`Campaign`** hoặc **`Ad group`**
3. Tick segment cần loại → **`Save Audience Segment Exclusions`**

**Campaign type hỗ trợ:** > "You can exclude specific segments from **Search, Display, Demand Gen, Standard Shopping, Video, and Performance Max** campaigns." → **PMax có trong danh sách** — đúng thứ cần cho G4.

🚨 **Bẫy thực thi, đáng giá cả mục này:**
> "Audience exclusions **aren't available during campaign creation**, but you can add exclusions to an existing campaign."
→ Exclusion là **bước SAU khi Publish**, không có ô nào trong luồng tạo campaign. Ai dựng campaign theo checklist tuyến tính sẽ **đi hết luồng, không thấy ô này, và kết luận sai là "tính năng không có"**. Với hệ, đây chính là việc GĐ5 phụ thuộc vào (§E5 "Exclusion là việc đáng làm nhất") → thiếu bước này thì cả kế hoạch GĐ5 đã sửa ở vòng 2 vẫn không thực thi được.

**Giới hạn số exclusion: CHƯA XÁC NHẬN** — trang exclusions không nêu số nào, trang account limits cũng không có dòng cho audience exclusion.

### So với hệ hiện tại

| Điểm | Nhãn | Chi tiết |
|---|---|---|
| `journey-plan` §2.1 hộp ⛔ CHẶN GĐ5 (vòng 2) nói "Exclusion là việc đáng làm nhất" nhưng **không nói làm thế nào** | 🆕 **MỚI — lỗ hổng thực thi, ĐÃ VÁ** | Kế hoạch đúng mà thiếu đường đi. Đã thêm 3 bước UI + campaign type + **bẫy "không cài được lúc tạo campaign"** vào `journey-plan` §2.1 và `campaign-setup.md` §5.5. |
| Checklist dựng campaign của hệ (§2.5, §5.5) là **luồng tuyến tính tới Publish** | ⚠️ **Rủi ro cấu trúc — đã vá bằng ghi chú** | Mọi thứ liên quan exclusion **phải** là bước sau Publish. Đã ghi rõ ở §5.5 ("bước 13 sau khi bấm Publish"). Áp cho **cả Search hôm nay**, không chỉ PMax ở G4 — hệ đã dự kiến loại trừ `da_generate_lead_14d`. |
| `journey-plan` §2.1 ghi "Khả dụng tại VN: CHƯA XÁC NHẬN → verify trong tài khoản" | ✅ **KHỚP — đã nâng thành kết luận đóng** | Câu cũ đúng nhưng để ngỏ như thể sẽ research tiếp. Đã sửa thành "**ĐÓNG — không có nguồn để xác nhận**" + đường kiểm cụ thể (`Tools → Audience manager` có `Customer list` không). Không ai phải đi tìm lại. |
| `tracking/upload_ecl.py` có `normalize_email()` áp luật gmail, và §E5 nói "tái dùng được cho audience ingest" | ⛔ **MÂU THUẪN — rủi ro thật, là việc CODE** | Tái dùng **nguyên xi** sẽ áp luật gmail cho Customer Match — không có nguồn, và làm **tụt match rate im lặng**. Cần cờ tắt. Xem "Chờ QA vòng 3" B1. |

---

## F7. Lead Journey Mapping — ⛔ ĐÓNG VĨNH VIỄN

**Kết luận: "Lead Journey Mapping" không tồn tại như một trang tài liệu độc lập của Google.**

Bằng chứng, cộng dồn 3 vòng:
- **Vòng 1:** không xác định được trang doc riêng.
- **Vòng 2:** tìm lại, vẫn không có → đưa vào danh sách nợ.
- **Vòng 3:** ⚠️ **ngân sách WebSearch của session đã cạn (200/200)** trước khi tới mục này, nên **không chạy được lượt WebSearch mới** như đề bài yêu cầu. Đường thay thế đã thử: `support.google.com/google-ads/search?q=lead+journey+mapping` qua WebFetch — trang trả về **khung điều hướng của Help Center, không có bài nào tên như vậy**.

**Vì sao kết luận "không tồn tại" là đủ vững dù vòng 3 thiếu một lượt search:** cụm này không xuất hiện ở **bất kỳ** trang nào trong toàn bộ tài liệu đã đọc suốt 3 vòng (~80 URL Google, gồm mọi trang lead-gen: [Best practices for generating high-quality leads](https://support.google.com/google-ads/answer/13489421?hl=en), [About lead form assets](https://support.google.com/google-ads/answer/9423234?hl=en), [About ECL](https://support.google.com/google-ads/answer/15713840?hl=en), [PMax best practices for lead generation](https://support.google.com/google-ads/answer/13775965?hl=en)). Một khái niệm được Google dạy thành doc riêng sẽ được **liên kết chéo** từ ít nhất một trong các trang đó. Không có link nào → gần chắc chắn đây là **thuật ngữ của giới hành nghề / khoá học bên thứ 3**, không phải tên gọi của Google.

**Việc phải làm: KHÔNG CÓ.** Chức năng mà cái tên này gợi ra thì hệ **đã có, bằng nguồn Google thật**, ở hai chỗ:
- `playbook/customer-journey-plan.md` §2.1 — bản đồ 5 giai đoạn ↔ campaign ↔ audience.
- Cách Google thật sự đặt tên cho vùng kiến thức này: **`Data Strength`** (§C2.9 — connect data sources → maximize signals → activate Google AI → prove ROI) và **customer lifecycle goals** (§F1). Ai đi tìm "lead journey mapping" nên được chỉ sang hai chỗ đó.

→ **Xoá khỏi mọi danh sách nợ. Không mở lại ở vòng sau.**

---

# Changelog vòng 3 — 2026-07-28

Phạm vi được phép: file `.md` không bị khoá (không `CLAUDE.md`, không `PLAN.md`). Không sửa `*.py`, `*.sh`, `*.csv`, và **không sửa skill vendored** (theo tiền lệ vòng 2 với skill `ad-click-attribution`) → xem "Chờ QA vòng 3".

| # F | File:dòng | Trước → Sau |
|---|---|---|
| **F1** | `playbook/campaign-setup.md` §5.5 (sau bảng 12 bước) | (không có) → hộp ⛔ **`New customer acquisition goal`: KHÔNG bật ở G4** — 3 lý do xếp theo mức nặng (không có Purchase goal → Value Mode loại thẳng · cần Customer Match list trước · **New Customer Only bid loại nhà đầu tư mua căn thứ 2** = nhóm CVR cao nhất) + 3 điều kiện mở lại + đính chính "540 ngày không có nguồn" |
| **F2** | `research/google-ads-bds-vn.md` §7b | (không có) → dòng thứ 4 của bảng "Chống chỉ định": **Quality Score** — 2 quote nguyên văn ("not a KPI… not aggregated", "not an input in the ad auction") + 2 hệ quả cứng (cấm báo cáo QS trung bình · mọi công thức `CPC = AdRank/QS` là SAI) + Ad Rank là "set of values" không phải phép nhân + ô "—" **không phải QS 6** + cửa sổ **90 ngày** + cột `(hist.)` **vẫn tồn tại** |
| **F3** | `playbook/campaign-setup.md` §5.5 bước 6, 8 | Bước 6 "account-level negatives TỰ PHỦ PMax" → thêm "⚠️ **Chỉ phủ Search + Shopping inventory**"; bước 8 → thêm "exclusion là **bước riêng SAU khi campaign đã tồn tại**" |
| **F3** | `playbook/campaign-setup.md` §5.5 (sau bảng) | (không có) → hộp ⚠️ **"Negative keyword trong PMax chỉ chặn được MỘT NỬA campaign"**: quote "Search and Shopping inventory **only**" + **`Excluded content keywords`** là ô thứ hai bắt buộc ở G4 (YouTube/Display) + 5 trần dung lượng (10.000/campaign · 5.000/list · 20 list · 1.000/account · 1.000 Display+Video) + brand exclusions ↔ negative **CHƯA XÁC NHẬN** (4 URL đều 404) |
| **F6** | `playbook/campaign-setup.md` §5.5 (sau bảng) | (không có) → hộp ⚠️ **audience exclusion KHÔNG cài được lúc tạo campaign** + đường UI 3 bước + 6 campaign type hỗ trợ (có PMax) + luật "exclusion là bước 13 sau Publish, áp cho **cả Search hôm nay**" |
| **F6** | `playbook/customer-journey-plan.md` §2.1 (hộp ⛔ CHẶN GĐ5) | "Khả dụng tại VN: **CHƯA XÁC NHẬN** → verify trong tài khoản" → (1) **cách làm Exclusion** đầy đủ: đường UI 3 bước + 6 campaign type; (2) 🚨 **bẫy** "aren't available during campaign creation"; (3) VN: **ĐÓNG — không có nguồn để xác nhận**, Google không publish country list → chuyển thành việc kiểm `Tools → Audience manager` |
| **F1** | `research/google-official-curriculum.md` §E5 (mục NCA) | "user không match list + chưa convert trong **540 ngày** → new customer" (tin cậy trung bình) → ⛔ **ĐÍNH CHÍNH: suy diễn, KHÔNG có nguồn** — vòng 3 đọc cả 2 trang, không trang nào nêu lookback; 540 ngày là thời hạn **membership list**, hai thứ khác nhau. "Việc còn nợ" → **XONG ở §F1, kết luận KHÔNG bật** |
| **F6(b)** | `research/google-official-curriculum.md` §E5(d) | "⚠️ Luật gmail… **CHƯA XÁC NHẬN** cho Customer Match" → ⛔ "**KHÔNG áp** cho Customer Match — ĐÃ CHỐT ở vòng 3" + trỏ §F6(b) |
| **F6(d)** | `research/google-official-curriculum.md` §E5(e) | "**CHƯA XÁC NHẬN** bằng câu trích trực tiếp" → ✅ **ĐÃ XÁC NHẬN** (answer/2549058, có PMax + bẫy campaign creation) |
| **F6(a)** | `research/google-official-curriculum.md` §E5(f) | "**CHƯA XÁC NHẬN**… phải kiểm trong tài khoản" → **ĐÓNG: không có nguồn để xác nhận** — chuyển từ *việc research* sang *việc kiểm tài khoản* |
| **F5** | `research/google-official-curriculum.md` §E6(d) | "⚠️ **CHƯA XÁC NHẬN tính chính danh của URL**… Verify thủ công trước khi trích cho khách" → ✅ **URL ĐÃ VERIFY**, tiêu đề "**Consent mode on websites and mobile apps**", mục *Consent mode behavior*, quote khớp nguyên văn → **dùng được cho khách** |
| (trạng thái) | `research/google-official-curriculum.md` §"Việc research còn nợ sang vòng 3" | (bảng để ngỏ) → thêm hộp trạng thái: **8/10 dòng ĐÃ ĐÓNG**; 2 dòng còn mở (Nghị định 13, Skillshop) **không phải việc research** |

**Tổng: 12 lần sửa trên 3 file tài liệu** (`campaign-setup.md` ×4, `customer-journey-plan.md` ×1, `google-ads-bds-vn.md` ×1, `google-official-curriculum.md` ×6) + chính Phần F này.

### Việc vòng 3 CỐ Ý KHÔNG vá

| Việc | Vì sao không |
|---|---|
| Sửa skill `.agents/skills/google-ads-quality-score/SKILL.md` (8 điểm MÂU THUẪN) | Là **skill vendored**, sửa là làm nó lệch khỏi upstream. Tiền lệ vòng 2: skill `ad-click-attribution` được đưa vào "Chờ QA" thay vì tự sửa. Giảm nhẹ rủi ro trong lúc chờ: sự thật đã được ghi vào **doc của hệ** (`research/google-ads-bds-vn.md` §7b) — nơi người vận hành đọc. Diff đầy đủ ở "Chờ QA vòng 3" A1. |
| Thêm alert/rà "Ask Advisor" vào `playbook/monitoring.md` | Chưa có **trang support** nào cho Ask Advisor (chỉ có thông cáo blog) → chưa biết nó có toggle hay không, tên ô là gì, ở đâu. Viết guard theo thông cáo báo chí = viết ra thứ sai. Đề xuất ở "Chờ QA vòng 3" A2. |
| Thêm cờ tắt luật gmail vào `tracking/upload_ecl.py` | **File code** — ngoài phạm vi. "Chờ QA vòng 3" B1. |
| Sửa `research/google-ads-bds-vn.md` §1 bảng campaign type theo GML 2026 | Không có thay đổi 2026 nào **đổi kết luận** của bảng đó (F4). Sửa để "trông mới" = nhiễu. |

---

# Chờ QA vòng 3 — không được tự sửa

> ⚠️ **Chưa đọc lại 3 nhóm "Chờ QA" của vòng 2** (A1-A3 rủi ro cao, B1-B3 code, C file khoá) — chúng **vẫn còn hiệu lực** trừ **A2** (shared list vs account-level) đã được QA đóng: `campaign-setup.md`:98 chốt **account-level**, và **F3 xác nhận lại là lựa chọn đúng** ("automatically apply… including in your Performance Max campaigns").

## A. Tài liệu / skill — QA quyết

### A1 — F2: skill `.agents/skills/google-ads-quality-score/SKILL.md` có 6 điểm SAI cần vá

Skill vendored → QA quyết sửa tại chỗ hay để nguyên và chỉ dựa vào `research/google-ads-bds-vn.md` §7b. **Nếu sửa**, đây là 6 chỗ, xếp theo mức hại:

```diff
--- a/.agents/skills/google-ads-quality-score/SKILL.md
+++ b/.agents/skills/google-ads-quality-score/SKILL.md

@@ dòng 108-131: "How CPC is Calculated" + bảng "QS vs CPC multiplier"
-Actual CPC = (Ad Rank of advertiser below you / Your Quality Score) + $0.01
-| Quality Score | Relative CPC vs. QS 5 baseline |   (bảng 10 dòng, QS 10 = -50% … QS 1 = +400%)
-A keyword with QS 3 costs you ~$5.00/click. The same keyword at QS 7 would cost ~$3.00…
+> ⛔ CONTRADICTED BY OFFICIAL DOCS. Google: "Quality Score is not an input in the ad
+> auction." (https://support.google.com/google-ads/answer/6167118) A quantity that is not
+> an auction input cannot be a divisor in the CPC formula. Google publishes NO CPC formula
+> and NO QS-to-CPC multiplier table. Improving the three COMPONENTS improves ad/landing-page
+> quality, which IS an Ad Rank factor — but there is no published exchange rate.
+> Prioritise fixes by spend and by which component reads "Below average", not by a fabricated %.

@@ dòng 20, 274, 349: "new accounts lack CTR history — QS starts at 6 by default"
-New keywords start at QS 6 by default
+A keyword with too little matched traffic shows "—" in the Quality Score column, NOT a
+default score. Google: "If you notice a '—' in the Quality Score column, it means there
+aren't enough searches that exactly match your keywords to determine a keyword's Quality
+Score." (answer/2454010). The advice to wait ~30 days still holds — but because there is
+no score yet to read, not because the score is 6.

@@ dòng 52, 69, 85: trọng số thành phần
-### 1. Expected CTR (~55% of QS weight)
-### 2. Ad Relevance (~22% of QS weight)
-### 3. Landing Page Experience (~22% of QS weight)
+### 1. Expected CTR        <!-- Google publishes no component weights -->
+### 2. Ad Relevance
+### 3. Landing Page Experience
+> Google does not publish how the three components are weighted. Any %-split you see is a
+> third-party estimate. Diagnose from the "Below average" flags, not from assumed weights.

@@ dòng 157, 302-313: "Tracking QS Over Time"
-**Note:** Google removed historical QS columns from the UI in 2022.
-Google removed historical QS columns from the UI in 2022. To track trends:
-### Option 1 — Google Ads Script … ### Option 3 — Third-party tools (Optmyzr, Adalysis, Swydo)
+Historical Quality Score columns EXIST in the UI. In the Keywords view, the column picker
+offers "Quality Score (hist.)", "Landing Page Exper. (hist.)", "Ad Relevance (hist.)" and
+"Exp. CTR. (hist.)" (answer/2454010). Use those first; scripts and third-party tools are
+only needed for retention beyond what the UI keeps.

@@ dòng 315-318: "What to track"
-- Account-level weighted average QS (weighted by impressions)
+<!-- removed: Google says QS "should not be optimized or aggregated with the rest of your
+     data" (answer/6167118). An account-level average QS is exactly that. Track the
+     DISTRIBUTION of "Below average" component flags on your top-spend keywords instead. -->

@@ dòng 371: mô tả skill google-ads-bidding
-- **google-ads-bidding**: Ad Rank = QS × bid × extensions — improving QS reduces the bid needed
+- **google-ads-bidding**: Ad Rank is "a set of values" from bid amount, ad and landing page
+  quality, Ad Rank thresholds, auction competitiveness, search context, and the expected
+  impact of assets and ad formats (answer/1752122). It is not a product, and Quality Score
+  is not one of its inputs.
```

Hai chỗ nhỏ hơn, QA quyết có gộp vào không: (a) dòng 152 "Set date range: last 30 days minimum" → thêm "note: Google's comparison window is the **last 90 days**, so component statuses lag your fixes"; (b) dòng 209 "Pause and restart… resets the quality signal" → gắn nhãn không có nguồn Google (đang khuyên mất 30 ngày traffic cho một cơ chế chưa được xác nhận tồn tại).

### A2 — F4: `playbook/monitoring.md`, thiếu rà "AI agent tự thay đổi tài khoản" (đường auto-apply thứ 4)

Hệ đã chặn 3 đường auto-apply (Google recommendations §1.5.11 · executor nội bộ §6 · experiment auto-apply §E2). **Ask Advisor** (GML 2026) là đường **thứ 4** và nguy hiểm hơn: nó là > "unified agent built with Gemini" trải **Google Ads + Analytics + Merchant Center + Marketing Platform** → ô "TẮT auto-apply" **trong Google Ads** có thể không phủ được nó.

```diff
--- a/playbook/monitoring.md   (§ rà hàng tháng)
+++ b/playbook/monitoring.md
+| ☐ | **Rà tính năng AI/agent mới có quyền thay đổi tài khoản** | Ngoài ô `Đề xuất → Tự động áp dụng` (§1.5.11), kiểm cả **Ask Advisor** và mọi mục có chữ *Gemini* / *Advisor* / *agent* / *assistant* trong Google Ads, GA4, Merchant Center. **Mặc định: coi là PHẢI TẮT cho tới khi QA duyệt.** Lý do: agent xuyên sản phẩm không bị ô auto-apply của Google Ads phủ. Nguồn: GML 2026 (blog.google, 20/05/2026) — chưa có trang support |
```

**Lý do chờ QA, không tự vá:** chưa có trang support nào cho Ask Advisor → **chưa biết tên ô thật, chỗ thật, có toggle hay không**. Viết guard theo thông cáo báo chí là viết ra một dòng checklist mà người vận hành không tìm được ô để tick. QA chốt: thêm ngay dạng "rà định tính" như trên, hay **đợi trang support xuất hiện** rồi mới viết đúng đường đi.

### A3 — F4: một mục theo dõi đáng đặt lịch — "Future Long-Term Conversions"

Không phải việc vá. Là **việc nhớ**: trong cả GML 2026, đây là thứ **duy nhất** chạm vào điểm yếu cốt lõi của hệ — chu kỳ BĐS **3-12 tháng** khiến conversion về sau khi click đã cũ, và `journey-plan` §4 vẫn còn `[điền]` cho conversion delay thật (tạm dùng ≥3 ngày, §E1). Hiện chỉ có tên trong thông cáo GA360, **không có trang support, không biết có cần GA360 trả phí hay không**. → QA quyết có đặt vào nhịp rà quý một dòng "kiểm xem *Future Long-Term Conversions* đã có doc chưa" hay không.

## B. File code — không sửa vòng này

### B1 — F6(b): `tracking/upload_ecl.py`, `normalize_email()` KHÔNG được dùng nguyên xi cho Customer Match

§E5(d) vòng 2 ghi "cùng SHA-256 + normalize → tái dùng được cho audience ingest". **Vòng 3 cho thấy điều đó chỉ đúng một nửa.** Luật gmail (bỏ dấu `.`, cắt `+suffix`) ở dòng ~77-86 có nguồn cho **enhanced conversions / user-provided data** (§C2.9) — **không** có nguồn cho **Customer Match**. Hai trang chuẩn hoá của Customer Match chỉ yêu cầu: có domain name, bỏ space, lowercase, SHA-256 (F6(b)).

```diff
--- a/tracking/upload_ecl.py
+++ b/tracking/upload_ecl.py
-def normalize_email(e):
+def normalize_email(e, gmail_rules=True):
+    # gmail_rules=True  -> enhanced conversions / ECL (user-provided data). Co nguon: §C2.9
+    # gmail_rules=False -> Customer Match (audienceMembers:ingest). Hai trang chuan hoa cua
+    #   Customer Match KHONG neu buoc bo dau '.' / cat '+suffix' (curriculum §F6(b)).
+    #   Ap bua -> hash ra chuoi khac chuoi Google mong doi -> match rate tut, KHONG co loi bao.
```
Kèm 1 assert trong `selftest()`:
```python
assert normalize_email("a.b+x@gmail.com", gmail_rules=False) == "a.b+x@gmail.com"  # chi lowercase+strip
assert normalize_email("a.b+x@gmail.com", gmail_rules=True)  == "ab@gmail.com"     # luat ECL
```
*(Tên hàm/hành vi thật phải đọc lại trong file trước khi apply — dòng trên là ý đồ.)*
**Mức ưu tiên: THẤP cho tới khi thật sự làm Customer Match** (hệ chưa có `audienceMembers:ingest`). Nhưng phải vá **trước** lần upload audience đầu tiên, vì lỗi này **không có thông báo** — chỉ thấy match rate thấp mà không biết vì sao.

## C. File bị khoá

| File | Việc | Diff đề xuất |
|---|---|---|
| `PLAN.md` §6.6 (quy trình sau-lead, đang PENDING) | **F6(d)** — mục vòng 2 đã đề xuất thêm ràng buộc Customer Match; giờ có **đường thực thi** | Thêm vào cuối đoạn đã đề xuất ở vòng 2: "Exclusion làm ở `Audiences → Exclusions → Exclude from: Campaign` — **và đây là bước SAU khi campaign đã publish**, không có ô trong luồng tạo (`answer/2549058`). Hỗ trợ cả PMax. **Khả dụng Customer Match tại VN: Google không publish country list** → việc đầu tiên là mở `Tools → Audience manager` kiểm có `Customer list` hay không, **trước** khi thoả thuận quyền Keap." |
| `PLAN.md` (mục nào ghi lộ trình PMax/G4) | **F1** | Nếu có dòng nào gợi ý NCA cho PMax: gắn "**KHÔNG bật** — `campaign-setup.md` §5.5". Vòng 3 **không grep được** mục cụ thể vì `PLAN.md` bị khoá đọc-để-sửa; QA tự kiểm. |
| `keywords/negative-keywords.csv` | **F3** | Không sửa dữ liệu. **Việc kiểm:** 40 dòng `cap_do=campaign` nên gom thành **1 shared negative list** — Customer/PMax đều nhận list ("you can select an existing negative keyword list"), nên gắn **1 list** cho campaign mới rẻ hơn dán 40 dòng. Trần 5.000/list nên thoải mái. Việc của agent `keyword-planner`. |
| Skill `.agents/skills/google-ads-quality-score` | **F2** | Diff đầy đủ ở A1 trên. |
