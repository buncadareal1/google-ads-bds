# Nghiệm thu 2 cổng kết nối — Beachtro Tower (2026-08-05)

Kiểm bằng lệnh gọi API thật, không suy đoán. Tài khoản Ads `6918288556` · GA4 property `548678683`.

## A. Google Ads API — v24, credential `~/google-ads-smartland.yaml`

| Nhóm chỉ số | Truy vấn | Kết quả |
|---|---|---|
| Campaign + chi phí/click/CTR/CPC/conv | `FROM campaign` + metrics | ✅ đọc được (0 dòng — chưa có campaign) |
| **Impression share** (IS, mất IS do ngân sách, do thứ hạng) | `metrics.search_*_impression_share` | ✅ |
| **Search terms** (nguồn negative hằng tuần) | `FROM search_term_view` | ✅ |
| **Keyword + Quality Score** | `FROM keyword_view` + `quality_info.quality_score` | ✅ |
| Địa lý | `FROM geographic_view` | ✅ |
| Negative keyword cấp tài khoản | `FROM customer_negative_criterion` | ✅ (hiện 1 dòng) |
| Conversion action | `FROM conversion_action` | ✅ (hiện 1 action) |
| Recommendation | `FROM recommendation` | ✅ |
| **Auction insights** | `segments.auction_insight_domain` + `metrics.auction_insight_*` | ❌ **BỊ CHẶN** — `The developer doesn't have access to metrics` |

### ❌ Auction insights — khoảng trống duy nhất, KHÔNG PHẢI do quyền token

Đã kiểm 4 dạng truy vấn (1 metric + domain, thêm `campaign.id`, `FROM ad_group`, `FROM keyword_view`) — **tất cả cùng một lỗi**, nên không phải lỗi cú pháp.

**Nguyên nhân thật:** `metrics.auction_insight_*` là **feature allowlist** của Google, tài liệu ghi rõ *"This metric is not publicly available"*. Chỉ tài khoản được Google đưa vào danh sách trắng mới gọi được, và **chương trình allowlist hiện ĐÓNG** với người xin mới. Không liên quan Basic/Standard access, không phải thứ nâng cấp được trong API Center. (Nâng Standard vẫn nên làm vì nới trần request/ngày, nhưng KHÔNG mở được auction insights.)

Hệ quả: mọi công cụ đi qua API đều mù chỗ này — kể cả Google Ads Scripts. Ai làm được auction insights là làm **trên UI**, không phải qua API.

→ **Bù bằng nghi thức tay, không có đường khác**: mỗi thứ Sáu `Chiến dịch → Thông tin chi tiết → Auction insights → Tải xuống` về `projects/beachtro-tower/data/ads/auction-insights-<yyyy-mm-dd>.csv` (luật quét điểm gãy `playbook/monitoring.md §4`). Đây là mục **bắt buộc** trong checklist tuần, không được bỏ — chính chỗ này là bẫy P7 đánh trượt 5/5 thí sinh kỳ thi Vinhomes.

### Cấu hình tài khoản (đọc từ API)

| Mục | Giá trị | Đối chiếu `campaign-setup.md §1` |
|---|---|---|
| Trạng thái tài khoản | ENABLED | ✔ |
| Tiền tệ / múi giờ | VND / Asia/Saigon | ✔ §1.1.5 |
| **Gắn thẻ tự động** (auto-tagging) | **True** | ✔ §1.3.1 — đã bật, có `gclid` |
| Tracking URL template | **rỗng** | ❌ §1.5.9 — chưa gắn UTM template (cần cho Clarity↔Ads) |
| Conversion tracking | `MANAGED_BY_SELF`, id `18359425041` | ✔ |
| Conversion action | 1/6: `7709665581` "Lượt gửi biểu mẫu khách hàng tiềm năng" (WEBPAGE · SUBMIT_LEAD_FORM · **primary**) | ❌ §1.2 — thiếu 5 action (Click_Hotline, Click_Zalo + 3 offline) |
| Negative cấp tài khoản | 1 dòng | ❌ §1.4.1 — cần import 382 dòng |
| Campaign / ngân sách | 0 / 0 | — chưa dựng (§2) |

⚠️ Bẫy GAQL đã gặp: `LAST_90_DAYS` **không** là literal hợp lệ — dùng `LAST_30_DAYS` hoặc `segments.date BETWEEN`.

## B. GA4 API — property `548678683`

| Mục | Giá trị |
|---|---|
| Tạo lúc | 2026-08-05 (mới hôm nay) |
| Ngành / múi giờ / tiền tệ | REAL_ESTATE / Asia/Saigon / VND ✔ |
| Mức dịch vụ | GOOGLE_ANALYTICS_STANDARD |
| Đọc report qua API | ✅ (`run_report`, `run_conversions_report`, realtime, funnel) |
| Liên kết Google Ads ↔ GA4 | ❌ **chưa có** (`list_google_ads_links` = rỗng) |
| Dữ liệu | **1 session duy nhất** — 4 event: `first_visit`, `page_view`, `session_start`, `view_content` |
| Key event (conversion) | **0** — chưa đánh dấu event nào là key event |

### ❌ 2 lỗi phải sửa khi dựng LP

1. **Event `view_content` không thuộc registry.** Registry duy nhất (CLAUDE.md): `generate_lead`, `phone_click`, `zalo_click`, `xem_bang_gia`, `xem_mat_bang`, `form_start`. Có event lạ = LP và tracking/ lệch nhau → báo cáo sau này không khớp. Sửa ở GTM trước khi chạy traffic thật.
2. **Chưa có key event nào.** Không đánh dấu key event thì GA4 không tính conversion, và Ads không import được action nào (§1.3.5 chỉ hiện event đã bắn ≥1 lần thật).

## C. Kết luận

**Cổng Ads: đủ chỉ số cho vòng lặp vận hành, trừ auction insights.** Cổng GA4: đường ống thông, **chưa có dữ liệu thật** vì LP chưa chạy.

Việc chặn launch, theo thứ tự: (1) LP thật + GTM gắn đúng 6 event chuẩn → (2) đánh dấu key event trong GA4 → (3) tạo đủ 6 conversion action + import từ GA4 → (4) import 382 negative cấp tài khoản → (5) gắn UTM tracking template → (6) dựng campaign theo `campaign-setup.md §2`.
