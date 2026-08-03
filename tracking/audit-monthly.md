# Audit tracking hàng tháng

Ngày 1 mỗi tháng, ~45 phút. Mục tiêu: chứng minh đường ống còn nguyên, bằng **một lead giả đi hết
tuyến**, rồi đối chiếu số 3 nguồn. Tracking hỏng âm thầm là cách đắt nhất để đốt ngân sách.

---

## 1. Bắn lead giả end-to-end

Dùng SĐT/email test cố định (`0900000001` / `qa+ecl@<domain>`) để dễ tìm và dễ xoá.

| # | Bước | Đạt khi |
|---|---|---|
| 1 | Mở `https://<lp>/?gclid=AUDIT-<YYYYMM>&gad_source=1&utm_source=audit` trên **điện thoại thật, 4G** | Trang load < 2,5s |
| 2 | Scroll qua bảng giá → mặt bằng → focus form → điền đủ → submit → bấm Zalo → bấm hotline | Không lỗi JS trong console |
| 3 | **GTM Preview**: đủ 6 event, mỗi tag fire đúng 1 lần | Không đúp, không thiếu |
| 4 | **GA4 DebugView** (trong 5'): 6 event + param `form_id`, `ngan_sach`, `muc_dich`, `cta_location` có giá trị thật | Không `(not set)` |
| 5 | **Keap**: contact mới tồn tại, custom field chứa `AUDIT-<YYYYMM>` | Có gclid — không có = pipeline ECL chết |
| 6 | **Google Ads** (sau 24h): `Form Submit Raw` / `Phone Click` / `Zalo Click` +1 | 3 action đều "Recording conversions" |
| 7 | Gắn tag `ECL - Contactable` cho contact test → chạy `python3 tracking/upload_ecl.py --dry-run` | Log có `requestId`, không có lỗi |
| 8 | Gỡ `--dry-run`, chạy thật → Google Ads (sau 6h) | `Lead Contactable` +1 |
| 9 | **Dọn**: xoá contact test trong Keap, xoá dòng `keap-<id>-contactable` khỏi `tracking/.ecl_state.json` | Không để rác trong CRM |

Bất kỳ bước nào fail → **dừng, sửa, chạy lại từ bước 1**. Không "ghi nhận rồi tính sau".

---

## 2. Đối chiếu số 3 nguồn (tháng trước)

| Chỉ số | Google Ads | GA4 | Keap | Ngưỡng chấp nhận |
|---|---|---|---|---|
| Click / Session | Clicks | Sessions (source=google, medium=cpc) | — | GA4 thấp hơn Ads **5-15%** là bình thường (bounce trước khi tag chạy). Lệch > 20% → kiểm tra tốc độ LP + redirect rớt query. |
| Lead | `Form Submit Raw` | `generate_lead` | Contact mới có gclid | Ads ≈ GA4 (±10%). **Keap là số đúng.** |
| Lead có gclid | — | — | % contact có gclid | **≥ 60%.** Dưới ngưỡng = click id đang rơi → `tracking/lp-requirements.md` §4.4. |
| Contactable | `Lead Contactable` | — | Số tag `ECL - Contactable` | Lệch > 15% = có event bị Google từ chối → đọc log cron. |
| Contact rate | — | — | Contactable / tổng lead | **> 50%.** Dưới 40% = có vấn đề nghiêm trọng (`research/google-ads-bds-vn.md` §5). |

**Luật (theo `attribution` skill + `playbook/customer-journey-plan.md` §4):**
**CRM quyết định số lượng. Google Ads và GA4 chỉ giải thích đến từ đâu. Không bao giờ cộng dồn.**
Khi ba con số đá nhau, Keap thắng.

Báo cáo chu kỳ dài: luôn đặt **first-touch cạnh last-touch**. Khoảng cách giữa hai số chính là insight.

### 2.1 Sáu nguyên nhân lệch số Ads ↔ GA4 ↔ CRM (tra bảng này TRƯỚC khi báo "tracking hỏng")

Nguồn: [Data discrepancies: Factors and troubleshooting](https://support.google.com/google-ads/answer/7457111?hl=en) + `research/google-official-curriculum.md` §B, §C2.2. Đây là câu hỏi sẽ được hỏi **mỗi tháng** — đa số "lệch số" là hành vi thiết kế, không phải lỗi.

| # | Nguyên nhân | Biểu hiện | Sửa được? |
|---|---|---|---|
| a | **Ngày quy về khác nhau** (conversion delay) | Google Ads quy conversion về **ngày CLICK**; GA4 về **ngày CONVERSION**. Click 19/7 → submit 20/7: Ads ghi 19/7, GA4 ghi 20/7 | ❌ **Không**. Chỉ có thể hiểu. Đây là nguyên nhân **số 1** và là lý do CPL theo ngày là nhiễu (`playbook/monitoring.md` §1) |
| b | **Hai model attribution riêng biệt** | GA4 default `data-driven`; Google Ads dùng model ad-centric riêng. Hai cấu hình độc lập, đổi bên này không đổi bên kia | ❌ Không hợp nhất được. Ghi rõ đang đọc model nào |
| c | **Lookback window ≠ conversion window** | GA4 `key event lookback window` (default 90) vs Ads `cửa sổ chuyển đổi lượt nhấp` (hệ đặt 90) — hai thiết lập khác nhau ở hai nơi khác nhau | ⚠️ Có: đặt cả hai = **90 ngày** cho khớp |
| d | **GA4 data thresholding** | Số nhỏ bị ẩn khi bật Google signals (hệ đang bật ON để có remarketing + demographic) → GA4 báo thiếu | ⚠️ Đánh đổi có ý thức. Né được bằng BigQuery export (đang hoãn — `ga4-setup.md` §4.1) |
| e | **Search terms report ẩn term ít volume** | Tổng click cộng theo search term **< tổng click campaign**; GAQL `search_term_view` không cộng bằng `campaign` | ❌ Không (privacy threshold). Đừng đi tìm bug (`research` §3) |
| f | **Múi giờ** | Property GA4 vs tài khoản Ads vs Keap lệch giờ → lệch ngày ở biên | ✅ Đã lo: cả 3 đặt `(GMT+07:00)` (`ga4-setup.md` §1) |
| g | **Đọc sai CỘT** | Cột `All conversions` của Ads gồm cả action đặt **Secondary** và **view-through conversions**; cột `Conversions` thì không | ✅ Chốt: mọi báo cáo của hệ đọc cột **`Conversions`** |
| h | **Xử lý chậm 24-48h** | So số sớm hơn 48h luôn thấy thiếu | ✅ Không so trước 48h |
| i | **Invalid clicks** | Site analytics ghi **mọi** traffic, kể cả click Google Ads đã loại là invalid → GA4 sessions > Ads clicks ở một số ngày | ❌ Không (đúng theo thiết kế) |

**Tin nguồn nào cho việc gì:**

| Câu hỏi | Nguồn chân lý | Vì sao |
|---|---|---|
| Keyword/campaign nào ra lead? (bid, negative, budget) | **Google Ads** | Quy về ngày click + có click ID — đây là hệ quy chiếu mà bidding học theo |
| LP hỏng ở bước nào? (funnel, CVR, bỏ form) | **GA4** | Có funnel exploration + custom dimension (`ngan_sach`, `muc_dich`, `form_id`) |
| Tổng bao nhiêu lead thật tháng này? | **CRM (Keap)** | Ads và GA4 đều là mô hình |
| Contact rate, CPL qualified | **CRM**, đối chiếu Ads | KPI chính của hệ nằm ở CRM |

---

## 3. Kiểm tra cấu hình (nhanh)

- [ ] Google Ads: **Auto-tagging vẫn ON** (hay bị tắt khi có người đổi setting)
- [ ] Đúng 3 conversion action Primary (`Lead Contactable`, `Lead Qualified`, `Dat Coc` nếu đủ volume);
      3 action web vẫn Secondary; **không có conversion nào bị đếm đúp** với import GA4
- [ ] GA4: 5 audience còn tăng size; `da_generate_lead_14d` vẫn được exclude khỏi mọi campaign remarketing
- [ ] GTM: version đang publish đúng bản mong đợi, có version name
- [ ] Cron ECL: 30 ngày qua không có ngày nào thiếu log
- [ ] Không có event lạ ngoài 6 event registry trong GA4 → Events (event lạ = LP tự ý thêm)
- [ ] `tracking/.ecl_state.json` không phình bất thường (mỗi lead tối đa 3 dòng)

---

## 4. Kết quả

Ghi 1 dòng vào scorecard tháng (`playbook/customer-journey-plan.md` §4):
`Audit YYYY-MM: PASS/FAIL · lead có gclid X% · contact rate Y% · lệch Ads↔Keap Z%`

FAIL = tạm dừng tăng ngân sách cho tới khi PASS. Scale trên tracking hỏng là nhân sai số lên.
