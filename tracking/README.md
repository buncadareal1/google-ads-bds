# NGỮ CẢNH ĐO LƯỜNG CHUYỂN ĐỔI — đọc trước khi đụng vào bất cứ thứ gì trong tracking/

> File này cho agent (và người) hiểu VÌ SAO hệ đo lường được thiết kế như vậy.
> Spec chi tiết nằm ở các file bên cạnh — đây là bản đồ + luật, không lặp lại spec.

## Vì sao đo lường quyết định thắng thua (tóm tắt từ research/google-ads-bds-vn.md §5)

1. **Smart bidding học từ tín hiệu bạn khai.** Khai "form submit" là conversion → Google tìm thêm
   người-điền-form-rẻ-nhất = SĐT rác. Đo sai không gây lỗi hiển thị nào — tài khoản trông vẫn
   "chạy tốt" trong khi tiền chảy về phía rác.
2. **BĐS VN: click rẻ (~25-40k₫), lead qualified đắt (~1,5tr).** Chỉ ~27% lead từ ad form là
   qualified. Chỉ đo CPL raw = scale nhầm campaign đổ rác nhiều nhất.
3. **Mọi gate tối ưu khóa bằng conversion data**: tCPA cần ≥30 conv/30 ngày; broad/PMax/tROAS
   cần ECL chạy ổn. Không đo = kẹt Max Clicks vĩnh viễn.
4. **KPI số 1 là contact rate (>50%), báo cáo trước CPL.**

## Chuỗi đo lường (đường đi của 1 lead)

```
LP (user tự làm, theo lp-requirements.md)
 │  dataLayer 6 event + hidden fields gclid/gbraid/wbraid/utm_*
 ▼
GTM (gtm-container-spec.md) ──► GA4 (ga4-setup.md: key events + 5 audiences)
 │                                └─► Google Ads: 3 conversion web (import GA4)
 ▼
Keap CRM (lead + gclid + email/phone)
 │  sales gắn tag: contactable → qualified → dat-coc
 ▼
upload_ecl.py (daily cron) ──► Data Manager API /v1/events:ingest
                                └─► Google Ads: 3 conversion offline ← SMART BIDDING HỌC TỪ ĐÂY
```

## Luật bất di bất dịch (QA sẽ chặn nếu vi phạm)

| # | Luật | Lý do |
|---|---|---|
| 1 | Event GA4 chỉ được lấy từ registry trong `CLAUDE.md` (6 event). Cần event mới → đề xuất vào registry trước, code sau | Tránh LP↔GTM↔GA4 lệch tên, audience không có dữ liệu |
| 2 | `phone_click`/`zalo_click` = **Secondary** vĩnh viễn. Primary ban đầu = `generate_lead`, đảo sang `Lead_Contactable` khi ECL chạy ổn | Bẫy optimize-to-quality: bidding sẽ mua click nút rẻ thay vì lead thật (QA chốt 2026-07-28) |
| 3 | Offline upload **chỉ qua Data Manager API** — Google Ads API bị chặn upload từ 15/6/2026 | Docs đã verify, xem ecl-keap-pipeline.md |
| 4 | Cửa sổ chuyển đổi 90 ngày (không để mặc định 30) | Chu kỳ mua BĐS 3-12 tháng |
| 5 | Không bịa số: thiếu benchmark → ghi `[điền từ tuần chạy đầu]` | Nguyên tắc toàn dự án |
| 6 | Sửa gì trong tracking/ phải chạy lại `python3 upload_ecl.py --selftest` và audit-monthly nếu đổi chuỗi | Đo lường hỏng là lỗi vô hình |

## Skill nào cho việc nào (đã cài trong .claude/skills/)

| Việc | Invoke skill |
|---|---|
| Viết/sửa code upload ECL, payload Data Manager API | `data-manager-api-event-ingestion` (Google official) |
| Setup/debug conversion action, gtag, GTM, enhanced conversions, attribution | `google-ads-conversion-tracking` |
| Pre-flight QA trước launch: event firing, UTM hygiene, dedup | `conversion-signal-qa` |
| Nâng cấp server-side tagging (sGTM/CAPI) khi mất data vì ad blocker | `ads-server-side-tracking` — ⛔ **CHƯA MỞ**, xem "Điều kiện mở server-side" dưới |
| Gắn gclid/UTM vào lead form | `ad-click-attribution` + `keap-lead-form` |
| Đọc số GA4 / GTM / Clarity | MCP `analytics-ga4` / `gtm` / `clarity` (10 req/ngày!) |

## Điều kiện mở server-side tagging (sGTM) — hiện KHÔNG mở

Google nêu 3 lý do dùng server-side: **performance**, **data control**, **data quality**. Ở quy mô hệ này **không lý do nào thoả**: 1 LP tĩnh (performance đã tốt), PII đã không vào GA4 (data control đã có), chưa có bằng chứng mất dữ liệu (data quality là giả định). Đổi lại là **chi phí GCP + một điểm hỏng mới** trong chuỗi đo lường — và chuỗi này là thứ cả hệ phụ thuộc.

**Mở khi (một trong ba là đủ, phải có SỐ chứng minh):**
1. ITP/adblock làm **mất >20% conversion đo được** (so Ads/GA4 với Keap trong audit tháng — `audit-monthly.md` §2.1).
2. Cần **gửi PII ra vendor thứ 3 không qua browser** (hiện không có nhu cầu này).
3. Chi tiêu **>150tr₫/tháng** VÀ có người vận hành GCP (không phải "sẽ học").

⚠️ Cạm bẫy Google nêu tên khi làm: **"cross-domain breaks when domains send data to different container IDs"** — LP ở domain riêng + proxy Keap ở domain khác là đúng tình huống này.

## Trạng thái hiện tại (cập nhật 2026-08-05)

- ✅ **Google Ads API đã kết nối** (account `6918288556`) — nghiệm thu: `nghiem-thu-cong-ket-noi.md`.
- ✅ GA4 property Beachtro `548678683` đọc được qua API · Clarity ✅ · GTM ✅.
- ⛔ **ECL / Keap / thang giá trị lead: ĐÓNG BĂNG** — hệ không đo lead (chốt 2026-08-05).
  Spec 7 file + `upload_ecl.py` giữ nguyên, mở lại khi user yêu cầu.
- 🔲 Chặn launch: **LP thật + GTM gắn đúng 6 event registry** (hiện GA4 chỉ có 1 session test,
  bắn `view_content` — SAI registry), chưa đánh dấu key event nào, thiếu 5/6 conversion action,
  negative account-level mới 1/382 dòng, tracking template UTM còn rỗng.
