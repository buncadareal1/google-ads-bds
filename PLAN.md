# PLAN v2 — Hệ thống Google Ads "win" cho BĐS Việt Nam

Cập nhật 2026-07-28 sau deep research (`research/mcp-servers.md`, `research/google-ads-bds-vn.md`).
Mục tiêu: hệ thống khép kín **Ads → Landing page → Lead → CRM qualify → Đo lường → Tối ưu**, tối ưu **CPL qualified + contact rate** (không phải CPL raw).

## 0. Nguyên tắc chiến lược (chốt từ research — ponytail)

1. **Ngân sách nhỏ (<20tr/tháng) = 1 Search campaign duy nhất**, Phrase + Exact, Max Clicks có bid cap. Không PMax, không broad, không Demand Gen, không chia nhỏ campaign. *(Đây là bậc 0 của lộ trình 6 bậc — không phải luật vĩnh viễn: broad mở ở bậc 2 khi có Smart Bidding + ECL, xem journey-plan §3.2 và curriculum §C2.6.)*
2. **Đòn bẩy theo thứ tự**: LP riêng có bảng giá + mặt bằng + Zalo nổi → negative list account-level → 2 dropdown qualifying trên form → gclid vào CRM + ECL.
3. **Offline conversion upload BẮT BUỘC qua Data Manager API** (Google Ads API đã bị chặn từ 15/6/2026).
4. **KPI chính: contact rate >50%**, báo cáo trước CPL. Thang conversion: form raw (secondary) → contactable=10 (primary, bid theo cái này) → qualified=50 → cọc=500.
5. **Gate mở rộng**: chỉ bật tCPA khi ≥30 conv/30 ngày; chỉ bật broad khi ≥30-50 conv/30 ngày + import CRM ổn; chỉ bật PMax khi ECL chạy ổn + 30 lead qualified/tháng (**KHÔNG bật New Customer Acquisition goal** — bid "chỉ khách mới" loại nhà đầu tư mua căn 2-3, nhóm CVR cao nhất của sàn; loại khách đã chốt bằng audience exclusion, curriculum §F1); Display chỉ remarketing (list ≥100 user).
6. **Mùa vụ VN**: giảm 40-60% Tết + tháng 7 âm (không tắt — mất learning), dồn T3-6 và T10-12. Đổi ngân sách ±20%/lần, tCPA ±15%/lần.
7. **Benchmark lập kế hoạch**: CPC 25-40k₫, CVR LP đích 3-6%, CPL qualified kịch bản trung bình ~1,5tr₫ — tự đo lại sau 30 ngày chạy thật.

## 1. Hạ tầng

| Thành phần | Trạng thái |
|---|---|
| MCP phase 1: `google-ads` (official, read-only GAQL), `analytics-ga4`, `gtm` (Stape), `clarity` | `.mcp.json` ✔ — chờ credentials (SETUP.md). **Developer token cần apply Basic access qua MCC (1-3 ngày) — làm NGAY** |
| MCP phase 2 (bật khi cần): DataForSEO (keyword volume VN), mcp-google-sheets (reporting), mcp-gsc (Search Console), Keyword Planner (ncosentino) | Chưa cài — xem research/mcp-servers.md |
| Connector claude.ai sẵn có | Meta Ads (Pipeboard), Semrush, Google Drive, Canva |
| Skills: 34 bộ trong `.claude/skills/` (bộ suite eliasmalmsandberg: bidding, audiences, quality-score, budget-management, account-audit; + ads-budget, budget-pacing-monitor, youtube-ads) | ✔ google-ads-manager, ads-google (audit), ads, ad-creative, ads-copywriter, cro, analytics, attribution, ab-testing, marketing-psychology, offers, popups, keyword-research, competitor-research, google-search-console, landing-page-generator, google-ads-audit-leadgen; đo lường chuyển đổi: **data-manager-api-event-ingestion (Google official)**, ads-server-side-tracking, conversion-signal-qa, google-ads-conversion-tracking + có sẵn: no-code-landing-re, ad-click-attribution, seo-machine, keap/cf7-lead-form |

## 2. Tài sản đã hoàn thành

| Tài sản | Trạng thái QA |
|---|---|
| `research/mcp-servers.md` — bản đồ cổng kết nối | ✔ |
| `research/google-ads-bds-vn.md` — best practices BĐS VN, nguồn kiểm chứng | ✔ |
| `keywords/` — **8.512 kw** (4.526 brand dự án từ 239 dự án thật / 3.225 giao dịch / 453 nghiên cứu / 308 CĐT), 256 negative, adgroup-map STAG, UPDATE.md (GAQL mẫu), gen.py tái sinh | ✔ QA pass: 0 trùng (kw,match), 0 field rỗng, spot-check tên dự án thật |

Bộ từ khóa là **tài sản sống**: tuần → search terms report qua MCP thêm kw/negative; tháng → quét dự án mới, chạy lại `gen.py`. Có thể tự động hóa bằng `/schedule` (cloud, chạy cả khi tắt máy) sau khi có credentials.

## 3. Đang chạy (subagent Opus, Fable QA)

- **Journey plan** → `playbook/customer-journey-plan.md`: 5 giai đoạn hành trình khách BĐS → campaign/thông điệp/offer/audience/KPI, ngân sách 3 kịch bản có gate.
- **Competitor research** → `research/competitors/`: playbook lặp lại hàng tháng (Ads Transparency Center, LP teardown, keyword overlap, trademark rules) + vòng thật case Eco Retreat.

## 4. Workstreams — hoàn thành 2026-07-28, QA pass

- ✅ **Journey plan** → `playbook/customer-journey-plan.md` (5 giai đoạn, gates G0-G5, KPI tree, 8 tiêu chí QA).
- ✅ **A'. Campaign setup** → `playbook/campaign-setup.md` (pre-flight, campaign 30tr, 3 bộ RSA đã verify ký tự, tuần 1-4, scale delta).
- ✅ **C. Tracking** → `tracking/` 7 file (lp-requirements handoff, GTM spec, GA4 audiences, ECL Keap → Data Manager API + `upload_ecl.py` selftest pass, Clarity, audit tháng).
- ✅ **D. SEO content** → `content/` 2 bài (7,8k từ, nguồn kiểm chứng, sạch policy).
- ✅ **Competitor** → `research/competitors/` (playbook tháng + vòng thật Eco Retreat; đã vá bộ kw: +22 `brand-eco-retreat`).
- 🔲 **B. Landing page** — USER TỰ LÀM theo `tracking/lp-requirements.md` (skills hỗ trợ: no-code-landing-re, keap-lead-form, ad-click-attribution, frontend-design).

**Quyết định QA đã chốt:** `phone_click`/`zalo_click` = Secondary (chống optimize-to-quality trap); primary ban đầu = `generate_lead`, đảo sang `Lead_Contactable` khi ECL chạy.

## 4b. Kiểm định năng lực — 3 war-game + 1 kỳ thi ngoài (chốt 2026-08-03)

| Đợt | Model/effort | Điểm | Ghi chú |
|---|---|---|---|
| War-game 4 tuần (10 vòng) | Opus | 95,0 | test/SCORECARD.md |
| War-game 90 ngày | Sonnet / Haiku | 95,0 / 84,9 | test/SCORECARD-90D.md — chốt model policy |
| **Kỳ thi ngoài Vinhomes Hóc Môn** (đề + đáp án độc lập của user) | Opus **effort medium** | gốc TB **94,6/100**, +thưởng → 103–105/110, **0/15 cờ đỏ × 5 bài** | test/exam-vinhomes/ — cả 5 Xuất sắc (ngưỡng 85) |

3 điểm mù hệ thống lộ ra ở kỳ thi ngoài (cả 5 agent trượt giống nhau) đã vá vào tài liệu 2026-08-03: quét điểm gãy chuỗi thời gian (monitoring §4), luật Simpson (monitoring §4 + landing-page/README), exclusion-áp-cho-cả-phân-tích (monitoring §2.1). Chi tiết: `test/exam-vinhomes/LESSONS.md`.

**Verdict production (Fable QA, 2026-08-03): ĐẠT CÓ ĐIỀU KIỆN.** Lớp kiến thức + quy trình + kỷ luật quyết định đã production-ready (4 đợt kiểm định độc lập, kể cả đề ngoài không do hệ tự ra, 0 cờ đỏ; effort medium đủ cho vòng lặp tuần). Điều kiện còn lại đều **ngoài hệ**: (1) tài khoản Google Ads + developer token, (2) LP thật theo lp-requirements, (3) số kinh doanh, (4) quyền xem quy trình sau-lead. Chế độ vận hành khi lên sóng: tự động trong whitelist approve-flow (monitoring §6), Fable QA giám sát, hiệu chỉnh bằng dữ liệu thật 30 ngày đầu trước khi nới quyền.

## 5. Vòng lặp vận hành (khi có credentials)

Checklist ngày/tuần/tháng/quý chi tiết: `research/google-ads-bds-vn.md` mục 8. Tuần: T2 search terms → negative; T3 lead quality (contact rate, ECL upload); T4 hiệu suất theo intent tier; T5 auction insights + LP; T6 báo cáo + 1 hypothesis.

## 6. User cần cung cấp / quyết định

1. **Apply developer token Basic access ngay** (bottleneck 1-3 ngày) + credentials theo SETUP.md.
2. ~~Dự án cụ thể đang phân phối~~ **ĐÃ CHỐT (2026-08-05): repo là nền tảng ĐA DỰ ÁN; dự án active đầu tiên = BEACHTRO TOWER — Blanca City (Sun Group, Vũng Tàu)** — kiểm tra/thêm vào keywords/projects.tsv + sinh bộ kw brand (việc đầu tiên của Cowork, xem COWORK.md). Dự án sau: lặp lại đúng quy trình đó, không fork repo.
3. ~~CRM đang dùng~~ **ĐÃ CHỐT (2026-08-05): bỏ Keap API, hệ KHÔNG đo lead** — user tự quản lý lead riêng. Hệ chỉ đo chỉ số nền tảng (Ads/GA4/Clarity). Hệ quả: pipeline ECL + thang conversion contactable/qualified/cọc (§0.4) đóng băng; KPI vận hành tạm thời = CPL raw (`generate_lead`) + chất lượng traffic, cho tới khi user mở lại đo lead.
4. **Ngân sách tháng + mục tiêu booking** — để chốt kịch bản và KPI tree.
5. **Hosting LP**: WordPress SmartLand pattern (nhúng static build) hay Vercel?
6. ⏸️ **Quy trình sau lead (`playbook/sau-lead.md`) — PENDING** (2026-07-28): user chưa có quyền xem quy trình sale. Hệ quả cần biết: contact rate >50% và pipeline ECL phụ thuộc việc **sales gắn tag trong Keap** (contactable/dat-coc) — cần người có quyền Keap thống nhất quy tắc gắn tag trước khi ECL chạy thật. **Ràng buộc mới từ curriculum Google (2026-07): conversion adjustment nên upload trong ≤7 ngày sau click → SLA cho sales: gắn tag `Lead_Contactable` trong tối đa 48h, muộn nhất 7 ngày** — đưa vào thỏa thuận khi có quyền. Thêm từ vòng 2 curriculum: **Customer Match ở quy mô hệ chỉ dùng được Exclusion/Observation** ($50k spend mới mở Targeting) → thỏa thuận Keap cần thêm (a) xuất list khách đã cọc/đã mua để LOẠI khỏi campaign acquisition (list Customer Match giữ member tối đa 540 ngày — dài hơn hẳn audience GA4 14 ngày; ⚠️ vòng 3: exclusion chỉ gắn được SAU khi campaign publish, không có trong luồng tạo campaign — thêm bước hậu kiểm; kiểm khả dụng Customer Match VN trong `Tools → Audience manager` TRƯỚC khi thoả thuận); (b) privacy policy trên LP phải khai có chia sẻ dữ liệu khách với bên thứ 3 trước lần upload đầu. Mở lại khi có quyền.
7. **Từ tracking/ (chờ chốt):** ~~thang giá trị điểm hay ₫ thật~~ **ĐÃ ĐÓNG (vòng 2): Google chính thức cho phép proxy value** ("utilize proxy values that align with your business priorities") → thang điểm 1/10/50/500 hợp lệ để bắt đầu value-based bidding ngay; chuyển ₫ thật khi có phí môi giới TB/căn là tối ưu thêm, không phải điều kiện · `Dat Coc` Primary khi ≥15 lượt/tháng · đường gửi click id vào Keap: SmartLand proxy (`form_url`) hay custom field + server proxy · danh sách credentials/ID: GTM-, G-, AW-, conversion labels, Keap SAK, GCP service account (chi tiết trong tracking/ecl-keap-pipeline.md).
