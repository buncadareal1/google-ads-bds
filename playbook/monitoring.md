# Monitoring & Notification — thiết kế vòng giám sát ads tự động

Kênh: Telegram (`scripts/notify-telegram.sh`). Nguyên tắc: **báo cáo theo nhịp, cảnh báo theo ngưỡng** —
guard im lặng khi mọi thứ bình thường (chống alert fatigue). Mọi suggest đều là ĐỀ XUẤT — người bấm nút chi tiền.

## 1. Ba nhịp báo cáo định kỳ (theo yêu cầu user)

| Giờ | Tên | Nội dung |
|---|---|---|
| **08:30** | Morning brief | Spend hôm qua vs trần ngày · pacing tháng (% ngân sách đã dùng vs % thời gian) · lead qua đêm (raw + zalo/phone click) · check nhanh: ad disapproved? conversion=0 bất thường? · 1 dòng việc hôm nay |
| **12:00** | Midday pulse | Spend sáng nay vs trung bình 7 ngày cùng khung giờ · lead sáng · CPC hiện tại vs baseline · chỉ nhắn NGẮN, bất thường mới nói dài |
| **20:00** | Daily close | Bảng đủ: Spend / Click / CPC / Lead raw / Contactable / CPL · so 7 ngày · search terms mới đáng chú ý (đề xuất negative/nâng exact) · Impression Share lost (budget vs rank) · việc chờ duyệt |

> ⚠️ **CPL theo NGÀY về bản chất là NHIỄU — đọc trước khi ra quyết định từ 3 nhịp trên.**
> Google Ads quy conversion về **ngày CLICK**; GA4 quy về **ngày CONVERSION** ([Data discrepancies](https://support.google.com/google-ads/answer/7457111?hl=en)). Với BĐS chu kỳ 3-12 tháng, "Lead hôm nay" trong Daily Close có thể thuộc click **tuần trước** → chia spend hôm nay cho lead hôm nay là chia hai tập khác nhau.
> **Luật:** báo cáo ngày chỉ để **phát hiện anomaly** (spend/click/disapproved/tracking gãy). **Mọi quyết định về bid, budget, pause chỉ ra ở mức 7-30 ngày.** Thêm nữa: đừng so số trước **48h** (Google xử lý chậm 24-48h).
> **Chốt cột đang đọc:** mọi số "Lead" trong 3 nhịp = cột **`Conversions`**, KHÔNG phải `All conversions`. Cột `All conversions` gồm cả action đặt **Secondary** (3 web conversion import từ GA4) và **view-through conversions** → đọc lẫn cột là lệch to. Mẫu tin §7 phải ghi rõ cột.

## 2. Guard liên tục — cadence 30-60 phút, CHỈ nhắn khi chạm ngưỡng

| Mức | Điều kiện | Hành động kèm alert |
|---|---|---|
| 🔴 | **LP sập** (curl ≠ 200 hai lần liên tiếp) | "Pause campaign ngay" + lệnh sẵn |
| 🔴 | **Conversion = 0 trong 4h có spend** (giờ hoạt động) | Nghi tracking gãy/LP lỗi → checklist audit nhanh → **nếu xác nhận tracking gãy >24h: tạo `Data exclusion`** (thủ tục ở §2.1) |
| 🔴 | **Spend đột biến >150%** nhịp giờ bình thường hoặc dự phóng vượt trần ngày | Nghi click tặc/bid war → xem invalid clicks + IP |
| 🔴 | Ad **disapproved / account limited** | Lý do policy + cách khắc phục theo research §7.3 |
| 🔴 | **Yêu cầu advertiser verification chưa hoàn thành** (30 ngày không nộp = TẠM NGƯNG cả tài khoản) | Đếm ngược ngày còn lại; alert mỗi ngày từ D-10, KHÔNG áp cooldown 2h. QA chốt cách thực thi: chưa xác nhận GAQL expose trạng thái verification → khởi đầu là **mục kiểm tay thứ 2 hàng tuần** (`Quản trị → Xác minh`), nâng thành alert tự động nếu API cho phép |
| 🟡 | **CPC tăng >2×** baseline 7 ngày trên nhóm brand | Đối thủ mới vào đấu giá? → check Auction Insights |
| 🟡 | **CTR tăng >2× mà conversion phẳng** (war-game round 3) | Dấu hiệu click tặc dạng crowding-out: ngân sách chặn cứng nên KHÔNG có alert chi tiêu — thiệt hại là mất impression khách thật. Check Invalid clicks + phân bố IP/giờ |
| 🟡 | **Budget cạn trước 20h** (limited by budget) | Suggest tăng/không kèm điều kiện (mục 3) |
| 🟡 | GA4 event ngừng bắn dù có traffic (đối chiếu realtime) | GTM/LP vừa deploy gì không? |
| 🟡 | **Learning phase guard**: có thay đổi lớn nào vừa thực hiện trên campaign đang learning | "Đừng đụng thêm, còn N ngày" |
| Cooldown | Mỗi loại alert tối đa 1 lần/2h, gộp nhiều alert thành 1 tin | |

### 2.1 Tracking gãy → `Data exclusion` (thủ tục bắt buộc)

Nguồn: [About data exclusions](https://support.google.com/google-ads/answer/10370710?hl=en) · [Use data exclusions for conversion data outages](https://support.google.com/google-ads/answer/10276486?hl=en) · [API docs](https://developers.google.com/google-ads/api/docs/campaigns/bidding/data-exclusions).

**Vì sao bắt buộc:** tracking gãy 1 ngày mà không khai data exclusion → Smart Bidding học rằng traffic ngày đó **không convert** và sẽ **tránh traffic tốt đó hàng tuần sau**. Đây là thiệt hại vô hình, không có alert nào bắt được sau khi đã xảy ra.

| # | Bước | Chi tiết |
|---|---|---|
| 1 | **Điều kiện áp dụng** | Campaign đang chạy Smart Bidding **theo conversion hoặc conversion value** (tCPA/tROAS/Max Conversions/Max Conv Value). Google: "can only be used with conversions and conversion value based Smart Bidding strategies". ⛔ Ở bậc **Max Clicks (ngày 1) thì KHÔNG áp dụng được và cũng không cần** — bidding không học từ conversion. Hỗ trợ Search/Display/Shopping/PMax; **không** hỗ trợ Hotel/Travel |
| 2 | **Tạo càng SỚM càng tốt** | "Apply data exclusions as quickly as possible at the time you've identified a conversion data issue". Google **không** đặt ngưỡng thời lượng tối thiểu — hệ tự đặt ngưỡng **>24h** để tránh tạo exclusion cho mọi nhiễu nhỏ *(luật nội bộ)* |
| 3 | **Chọn khoảng ngày theo CLICK, không theo ngày outage** | Exclusion tác động lên **clicks**. "make sure to consider your conversion delay and exclude any days of clicks that may have been impacted" → phải kéo lùi thêm đủ số ngày conversion delay của hệ. Với BĐS, lead thường về trong vài ngày → lùi thêm **≥3 ngày** trước ngày tracking gãy |
| 4 | **Phủ ≥90% click bị ảnh hưởng** | "It's a best practice to exclude **at least 90%** of clicks associated with impacted conversion data" |
| 5 | **Trần thời lượng** | API docs: "The date range should be **less than 14 days**". Dùng thường xuyên hoặc kéo dài → "could negatively impact Smart Bidding performance" |
| 6 | **Backdate được** | Phát hiện muộn vẫn tạo được cho ngày đã qua: "Data exclusions created for past dates should see performance fluctuations begin to stabilize after a few days" |
| 7 | **Sau khi áp** | Chỉnh tCPA/tROAS về mức mong muốn + kiểm budget. Nếu **≥1 tuần** click bị ảnh hưởng: "performance fluctuations may continue for **1-2 conversion cycles**" → **không phán xét hiệu suất** trong khoảng đó, và không chồng thêm thay đổi khác |
| 8 | **Cấp áp dụng** | Được ở cấp **Manager account (MCC)** hoặc sub-account — 1 lần cho nhiều account con |
| 9 | **Ghi lại** | 1 dòng vào `ops/audit-log.jsonl` + 1 dòng vào audit tháng (`tracking/audit-monthly.md` §4): ngày outage, khoảng exclusion, nguyên nhân gốc |

**UI:** `Công cụ` → `Chiến lược giá thầu` (Bid strategies) → tab `Điều chỉnh nâng cao` (Advanced controls) → `Loại trừ dữ liệu` (Data exclusions) → `+`.

⚠️ **Đừng lẫn với Seasonality adjustment.** Data exclusion = dữ liệu **SAI/HỎNG**, nói "đừng học khoảng này". Seasonality adjustment = conversion rate **DỰ KIẾN thay đổi**, nói "khoảng này CVR sẽ khác". Hai công cụ khác mục đích, không thay nhau.

⚠️ **Exclusion áp cho CẢ phân tích, không chỉ máy học.** Mọi báo cáo/audit/trung bình (CPL tuần, CVR kỳ, so sánh giai đoạn) phải **loại các ngày outage khỏi mẫu số** và ghi chú "đã loại N ngày tracking gãy". Sửa xong nguyên nhân + khai data exclusion mà vẫn tính trung bình gộp cả ngày hỏng = kết luận sai lệch âm thầm. *(Bài học war-game Vinhomes: 5/5 agent truy đúng nguyên nhân GTM nhưng chỉ 1 nêu exclusion, 0 agent loại 3 ngày khỏi phép tính trung bình.)*

## 3. Suggest engine — luật đề xuất (đi kèm báo cáo 20:00 hoặc alert)

Mọi suggest phải kèm: con số căn cứ + hành động cụ thể + rủi ro. Luật lấy từ research/journey-plan:

| Suggest | Điều kiện kích hoạt | Giới hạn |
|---|---|---|
| **Tăng budget** | IS lost (budget) ≥10% liên tục 3 ngày VÀ CPL ≤ trần VÀ contact rate đạt | +≤20%/lần, cách ≥3-4 ngày |
| **Giảm budget / pause nhánh** | CPL > trần 3 ngày liên tiếp sau khi đã hết learning | -≤20%/lần; pause = đề xuất kèm dữ liệu nhánh |
| **Negative mới** | Search term ≥30 click 0 conversion, hoặc lệch intent rõ | Soạn sẵn file import |
| **Nâng exact** | Search term có ≥1 conversion | Kèm bid đề xuất |
| **Chỉnh tCPA** | Đủ 30 conv/30 ngày + chênh CPL thực vs target >15% | ±15%/lần |
| **Seasonality adjustment** | Trước đợt mở bán/event (user khai lịch) **VÀ** campaign đang chạy **tCPA/tROAS** | Chỉ event 1-7 ngày. **GUARD:** xem 2 luật chặn dưới bảng |
| **Data exclusion** (§2.1) | Xác nhận tracking gãy >24h **VÀ** campaign đang chạy bidding theo conversion (tCPA/tROAS/Max Conv/Max Value) | KHÔNG vào whitelist auto-apply của approve-bot (sửa dữ liệu huấn luyện = sai là hại dài hạn — luôn làm tay). Ở bậc Max Clicks: API từ chối và cũng vô nghĩa — không suggest |
| **Seasonal budget adjustment** | Đợt mở bán **3-14 ngày** (user khai lịch), campaign Search **không** nằm trong ngân sách dùng chung | Chỉ TĂNG budget; 2 lần liên tiếp cách **≥7 ngày**; tự trả về mức cũ |
| **Data exclusion** | Đã xác nhận tracking gãy **>24h** (sau alert 🔴 "Conversion = 0 trong 4h") **VÀ** campaign đang chạy Smart Bidding theo conversion/value | Khoảng loại trừ ≤14 ngày, phủ ≥90% click bị ảnh hưởng. Xem §2 alert |
| **Chuyển giai đoạn bidding** | Đạt điều kiện lộ trình research §4.1 | Theo gates G0-G5. Ưu tiên **campaign experiment** thay vì đổi thẳng — xem §3.1 |

**GUARD bắt buộc cho suggest `Seasonality adjustment`** (không có 2 guard này thì bot đề xuất việc API sẽ từ chối, hoặc việc Google nói đừng làm):

1. **Chỉ hợp lệ khi campaign đang chạy `tCPA` hoặc `tROAS`.** Search chỉ hỗ trợ 2 chiến lược này cho seasonality adjustment. Ở bậc Max Clicks (ngày 1) → **API từ chối**, đừng suggest.
2. **CẤM suggest cho Tết và tháng 7 âm.** Google: không dùng seasonality adjustment cho seasonality **định kỳ** ("Smart Bidding already manages these") và không dùng >14 ngày. Tết = định kỳ + 2 tuần → **thao tác NGÂN SÁCH bằng tay**, và seasonal budget adjustment cũng không dùng được vì nó **chỉ tăng, không giảm**. Chi tiết bảng so sánh 2 công cụ: `research` §4.

### 3.1 Đổi bid strategy: dùng campaign experiment, đừng đổi thẳng

Google khuyên test bid strategy bằng **experiment** thay vì đổi thẳng campaign gốc ([Set up a campaign experiment](https://support.google.com/google-ads/answer/6261395?hl=en)). Với hệ: `campaign-setup.md` §4.4 hiện đổi thẳng — **giữ được**, nhưng phải biết đánh đổi.

| | Đổi thẳng (cách hiện tại) | Campaign experiment |
|---|---|---|
| Rủi ro | Toàn bộ campaign vào learning; sai thì mất 2-4 tuần | Chỉ % traffic được chia vào nhánh thử |
| Thời gian có kết luận | 4 tuần (luật nội bộ) | **4-6 tuần trở lên**, cộng 1-2 conversion cycle; **7 ngày đầu bị loại** khỏi tính significance |
| Ở volume của hệ (12-29 lead/tháng) | Kết luận nhanh nhưng dựa trên mẫu nhỏ | Chia 50/50 → mỗi nhánh 6-15 lead/tháng → **gần chắc chắn "inconclusive"** trong 4-6 tuần |

**Kết luận cho hệ:** ở bậc 30tr₫/tháng, experiment **chưa đủ volume để kết luận** → giữ cách đổi thẳng + guard learning phase. Mở experiment khi một campaign đơn lẻ đạt **≥30 conv/tháng ổn định** (đủ để mỗi nhánh có ~15). Chi tiết cấu hình + cách đọc significance: `research/google-official-curriculum.md` §E2.

## 4. Nhịp tuần/tháng (mở rộng — gợi ý thêm)

- **Thứ 5**: Clarity digest (4 việc trong `tracking/clarity-checklist.md` §2, dùng ≤4/10 quota) + campaign spend cao nhất có CVR thấp → replay.
- **Thứ 6**: Báo cáo tuần đầy đủ (format checklist T6) + **auto-commit đề xuất vào repo** (negative list, keyword mới qua agent `keyword-planner`) — bạn mở Cowork duyệt diff.
- **Thứ 6 — quét điểm gãy chuỗi thời gian (script, bắt buộc, ~1 phút)**: với TỪNG campaign, tính CPC / CTR / IS / Mất-IS-thứ-hạng **theo tuần** (không nhìn trung bình kỳ) và so tuần này vs trung vị 3 tuần trước. Ngưỡng alert: CPC brand +30% WoW, IS brand −15đ WoW, CTR brand −2đ WoW → mở Auction Insights ngay, nghi **đối thủ đấu giá brand**. ⚠️ **Auction Insights KHÔNG đọc được qua API** (feature allowlist của Google, đã đóng — kiểm 2026-08-05, xem `projects/beachtro-tower/nghiem-thu.md`) → thứ 6 phải **tải tay** `Chiến dịch → Thông tin chi tiết → Auction insights → Tải xuống` về `projects/<slug>/data/ads/auction-insights-<yyyy-mm-dd>.csv`. Bỏ bước này = mù đúng chỗ bẫy P7. *Bài học war-game Vinhomes 2026-08: đối thủ tấn công brand từ N52 (CPC +74%, IS sập còn 28,8%) nằm lộ thiên trong dữ liệu ngày nhưng cả 5 agent Opus đều trượt vì chỉ nhìn trung bình cả kỳ. Trung bình kỳ là thuốc mê — điểm gãy chỉ hiện khi cắt lát thời gian.*
- **Luật Simpson khi đọc bất kỳ so-sánh trước/sau nào** (đổi LP, đổi bid, thêm campaign): chỉ tiêu tổng tài khoản (CVR, CPL) **vô nghĩa nếu cơ cấu traffic đổi giữa 2 kỳ** — một campaign đầu-phễu mới bật (YT/PMax) đủ kéo tụt CVR tổng trong khi mọi campaign cũ đều cải thiện. Bắt buộc bóc theo từng campaign (hoặc chỉ Search) trước khi kết luận chiều hướng; kết luận từ số tổng khi mix đổi = cờ đỏ.
- **Thứ 2 đầu tháng**: vòng competitor (PLAYBOOK 6 bước) — alert nếu đối thủ mới xuất hiện trên brand keyword; audit tracking end-to-end (`tracking/audit-monthly.md`); nhắc quét dự án mở bán mới vào `projects.tsv`; **rà "AI tự thay đổi tài khoản"**: auto-apply recommendations còn tắt không (campaign-setup §1.5.11) + experiments sắp hết hạn (tự apply nếu "favorable"!) + **Ask Advisor/tính năng agentic mới xuất hiện chưa** (GML 2026 — chưa có trang support/ô tắt được document, thấy là báo QA tìm cách chặn trước khi dùng).
- **Hàng quý**: theo dõi trạng thái **"Future Long-Term Conversions"** (GML 2026 — dự đoán giá trị conversion tương lai, chạm đúng chu kỳ BĐS 3-12 tháng; khi GA thì đánh giá bật cho value-based bidding).
- **Insights page** (`Chiến dịch` → `Thông tin chi tiết và báo cáo` → `Thông tin chi tiết`, toggle 7/28 ngày, refresh **hằng ngày**): chia 2 nhịp, đừng xem hết mỗi tuần —
  - **Nhịp TUẦN (thứ 4, ~5 phút):** `Diagnostic insights` (lý do campaign không serving/không có conversion — bắt sớm tracking gãy & disapproval) · `Budget pacing insights` · `Performance shifts / Explanations` (chỉ có khi có biến động đủ lớn; **không có explanation nếu khoảng ngày chứa hôm nay**).
  - **Nhịp THÁNG:** `Search trends` · `Demand forecasts` (dự báo 180 ngày) · `Search terms insights` · `Audience insights` · `Auction insights`. Lý do: cả 5 cái này cần tích luỹ đủ volume/impression mới xuất hiện — ở 12-29 lead/tháng chúng **thường không xuất hiện**, xem hàng tuần là mất thời gian.
  - ⚠️ Insight **không hiện** thường chỉ là "chưa đủ dữ liệu / chưa có category nào đang trend", **không phải lỗi cấu hình** ([Why you might not have insights](https://support.google.com/google-ads/answer/10260432?hl=en)). Đừng đi tìm bug.
- **Theo lịch mùa vụ VN**: nhắc trước 2 tuần — giảm budget Tết/tháng 7 âm, tăng T3-6 & T10-12 (research §4.4).
- **Contact rate digest tuần**: đối chiếu lead Ads vs Keap, nhắc upload ECL nếu quá 7 ngày chưa chạy.
- **Báo cáo sếp** (tùy chọn): xuất bảng tuần ra Google Sheets qua MCP sheets (phase 2).

## 5. Điều kiện triển khai theo lớp

| Lớp | Chạy được khi | Ghi chú |
|---|---|---|
| Nhịp GA4 + Clarity + LP uptime | **NGAY** (credentials đã có) | Chạy trước để quen nhịp |
| Toàn bộ mục 1-3 với số ads thật | Developer token | |
| Chạy khi máy tắt (cloud `/schedule`) | git push repo + secrets cloud (TG_BOT_TOKEN, Google creds) | Máy bật thì cron/loop local chạy được trước |
| Hỏi đáp 2 chiều qua bot tele | Phase sau (webhook bot) | Hiện tại: nhận tin → mở Cowork/Claude Code để vibe |

## 6. Flow DUYỆT-LÀ-CHẠY (approve → tự động apply)

```
Suggest engine                        Telegram                       Executor
─────────────                         ────────                       ────────
phát hiện điều kiện (mục 3)
→ ghi action vào ops/pending-actions.jsonl
→ gửi tin + nút [✅ Duyệt] [❌ Bỏ]  →  bạn bấm nút
                                       callback_query  →  scripts/approve-bot.py (long-poll)
                                                          → đọc action theo id
                                                          → check guardrails
                                                          → apply qua Google Ads API
                                                          → reply kết quả + ghi ops/audit-log.jsonl
```

> 🚨 **CHỐNG LẪN TÊN — đọc trước khi tick bất cứ ô nào.** Có **hai** thứ tên gần giống nhau, hoàn toàn khác nhau:
>
> | | **Auto-apply NỘI BỘ** (mục 6 này) | **Auto-apply recommendations của GOOGLE** |
> |---|---|---|
> | Ai bấm | **Người** bấm nút Duyệt trên Telegram | **Không ai** — Google tự áp |
> | Guardrail | Có (bảng whitelist dưới + 7 luật an toàn) | Không có guardrail nào của mình |
> | Audit log | Có — `ops/audit-log.jsonl` | Chỉ có History tab của Google |
> | Trạng thái | Đây là hệ thống của mình, dùng bình thường | **ĐÃ TẮT HẾT** ở `campaign-setup.md` §1.5.11 — rà lại **hàng tháng** vì Google thêm recommendation mới liên tục |
>
> Người sau đọc "auto-apply đã có guardrail" rất dễ tưởng đã kiểm tra phía Google rồi. **Chưa.** Hai việc riêng, kiểm riêng.

**Whitelist hành động được auto-apply khi duyệt (NỘI BỘ)** (ngoài danh sách này = chỉ báo, làm tay):

| Action | Giới hạn cứng trong executor (không tin message) |
|---|---|
| `add_negative` | Chỉ thêm vào list negative account/campaign đã tồn tại |
| `budget_change` | ±20% max so với budget hiện tại đọc từ API, ≥3 ngày từ lần đổi trước (đọc audit-log) |
| `tcpa_change` | ±15% max, campaign phải ≥30 conv/30 ngày |
| `pause_entity` | Chỉ ad group/keyword, KHÔNG pause campaign (campaign = làm tay) |
| `promote_exact` | Thêm keyword exact mới từ search term có conversion |

**Luật an toàn:**
1. Chỉ nhận callback từ đúng `TG_CHAT_ID` — người lạ bấm = bỏ qua + log.
2. Action hết hạn sau 24h không duyệt (số liệu cũ = quyết định sai).
3. Idempotent: mỗi action id chạy 1 lần, bấm 2 lần không apply 2 lần.
4. Executor re-check điều kiện tại thời điểm apply (không tin điều kiện lúc suggest).
5. Mọi apply ghi `ops/audit-log.jsonl`: ai duyệt, lúc nào, giá trị cũ→mới, kết quả API.
6. Learning phase guard chạy TRƯỚC apply: campaign đang learning → từ chối kèm lý do.
7. Kill switch: nhắn bot `/pause_all_suggestions` → ngừng gửi suggest (không đụng ads).

Điều kiện chạy (✅ đủ từ 2026-08-05): credential Google Ads API `~/google-ads-smartland.yaml` + venv `.venv-ads/` (API v24) + máy/cloud chạy `approve-bot.py`. Chạy ở **máy local** — Cowork cloud không có credential nên chỉ gửi đề xuất, không apply.

⚠️ Chưa bật thật: đang chờ campaign đầu tiên (account `6918288556` hiện 0 campaign). Khi launch, bật theo thứ tự: chạy chế độ **chỉ đề xuất** 30 ngày đầu (user tự apply, đối chiếu xem đề xuất có đúng không) → mới mở apply tự động trong whitelist. Không mở apply ngay ngày 1 khi chưa hiệu chỉnh bằng dữ liệu thật.

## 7. Format tin Telegram (mẫu)

```
📊 Daily Close 28/07
Spend: 950k/1.000k (95%) · Click: 38 · CPC: 25k
Lead: 3 raw · 2 contactable · CPL-c: 475k ✅ (trần 600k)
  ⓘ cột `Conversions` (không phải All conversions) · quy về ngày CLICK
IS lost budget: 12% ⚠️ 3 ngày liên tiếp
📅 7 ngày: 19 lead · CPL-c 512k ← số này mới dùng để quyết định

💡 Suggest: tăng budget #1 lên 550k (+16%) — CPL đạt, IS hụt.
   Rủi ro: learning 0 ngày còn lại. Duyệt: mở Cowork → apply.
🧹 Negative mới: 4 term (file sẵn: keywords/pending-negatives.csv)
```


## Phụ lục: 3 luật đọc số bổ sung (Kohavi, chưng cất 2026-08-06 — `research/books/kohavi-experiments.md`)

1. **Alert đối xứng — tin TỐT đột biến cũng là alert** (Twyman's law): chỉ số đẹp bất thường >2× so trung vị 3 tuần → nghi tracking/bot/đếm trùng trước, ăn mừng sau. Hệ hiện chỉ có alert chiều xấu.
2. **Guardrail tin cậy phủ quyết**: ngày có tracking gãy / gclid mismatch / thẻ đo trùng → gạch toàn bộ số của ngày đó khỏi mọi phân tích, kể cả số đẹp (Microsoft ExP giấu luôn scorecard khi trust-guardrail rớt).
3. **2 RSA cùng ad group không phải A/B test** — Google chia impression theo dự đoán hiệu suất, chung budget, chung learning. Được phép: để Google chọn cái chạy. Cấm: kết luận headline nào "thắng" từ impression split.
