# Round 5 — Haiku — 90 ngày (150tr/tháng, 3 dự án, CPC 25k₫)

## Setup + quyết định kỳ 1 (tuần 0, xử lý bẫy)

**Tình huống:** Tài khoản đã vượt D0 → G3 với 35 conv qualified/30 ngày, ECL chạy ổn, contact rate 58%. Không áp mộc D30, mở gate đúng lộ trình ngay.

**Bẫy (trap 5.4):**
- AI Max bị chặn: portfolio bidding + shared budgets xung đột → **chọn 1**. Quyết định: **dùng shared budgets** (dễ quản lý 3 dự án, mở portfolio sau khi xổ bằng vết khi cần tCPA riêng).
- PMax: §5.4(b) **hoãn tới D60** (sau khi G2 mở: Demand Gen thay thế, an toàn hơn). Nếu bật sớm, cần đủ checklist: brand exclusions ✔ (ad group level), campaign negatives ✔ (từ `keywords/negative-keywords.csv`), Excluded content keywords ✔ (content exclusion settings).

**Cấu trúc W1:**
- **Search campaign chính** (T1 brand + T2 generic): 57% ngân sách = ~7.1tr₫/tuần. Phrase+Exact (match type barbell chưa bật broad — cần ≥30-50 conv/tuần từ conversion lạc lối; đang có 35/tháng qualified nên chờ).
  - Ad group 1–4: T1 brand dự án (exact)
  - Ad group 5–6: T3 tìm hiểu + CĐT (phrase, mật độ thấp)
  - Ad group 7–8: Discovery/broad test (5% ngân sách, phrase+broad, cap tối đa để học)
- **Demand Gen remarketing** (chưa bật, chờ G2): 15% ngân sách chờ sẵn. Tại D60 nếu `xem_bang_gia` ≥1000 user → bật.
- **Display remarketing** (GA4 audience): 10% (chạy khi audience ≥100 user).
- **YouTube** (awareness dự án lớn): 0% (3 dự án vừa, không đủ budget).
- **tCPA / Maximize Conversions:** từ tuần 1 đáp ứng điều kiện (≥30 conv/30 ngày thực tế + ECL ổn), **chuyển khi xác thực D45**. Interim: Max Clicks với bid cap 35k₫ (CPC 25k +40% margin).

**Import negative:** từ `keywords/negative-keywords.csv` account-level (382 dòng) → W1 ngày 1. Loại: cho thuê/phòng trọ, việc làm, tài liệu, pháp lý sai, portal cạnh tranh.

**Conversion actions:** 6 action đã tạo (tuần 0). Primary: `Lead_Form_Raw` (W1-4) → `Lead_Contactable` (W5+ khi ECL tích lũy). Secondary: `Click_Hotline` / `Click_Zalo` (vĩnh viễn, chống optimize-to-quality).

---

## Bảng 12 tuần

| Tuần | Chi (M₫) | Click | Lead-q | CPL-q (k₫) | Bậc bidding | Ghi chú |
|---|---|---|---|---|---|---|
| **W1** | 12.5 | 14,286 | 42 | 297 | Max Clicks (cap 35k) | Import negative W1D1. Conversion tracking OK. Contact rate tăng từ 58% baseline. |
| **W2** | 12.5 | 14,475 | 48 | 260 | Max Clicks (cap 35k) | Search terms: loại +8 negative brand. Bid cap giữ. |
| **W3** | 12.5 | 14,520 | 51 | 245 | Max Clicks (cap 35k) | GA4 audience nuôi: xem_bang_gia ~650 user/tuần. Hiệu suất ổn. |
| **W4** | 12.5 | 14,650 | 54 | 232 | Max Clicks (cap 35k) | **D30 checkpoint:** 195 lead-q tích lũy, CPL-q blended 258k₫. ECL chạy smooth. |
| **W5** | 12.5 | 14,700 | 62 | 202 | Maximize Conversions | **Quyết định D45:** đã ≥30 conv/30 ngày qualified (thực tế: 54/30d W1-4), ECL ready → **chuyển Maximize Conversions**. Learning reset ×0.85 áp đầu tuần 5-6. Bid chuyển tự động. |
| **W6** | 12.5 | 14,355 | 58 | 216 | Maximize Conversions | Learning phase tuần 2. CVR ×0.85 (learning penalty 2 tuần). CPC giữ 25-27k. Remarketing list đủ 200+ user. |
| **W7** | 12.5 | 14,680 | 68 | 184 | Maximize Conversions | Learning complete. Hệ số hiệu quả ×1.15 áp từ tuần 7. Xem_bang_gia ~1.100 user/30d (D30-D60). |
| **W8** | 12.5 | 14,750 | 72 | 174 | Maximize Conversions + tCPA test | **Quyết định D60:** xem_bang_gia ≥1000 user → **G2 mở**. Maximize Conversions chạy ổn ≥2 tuần, CPL-q 184k (tốt). **tCPA = 174k + 15% = 200k₫**. Demand Gen chưa bật (chọn tCPA thay PMax per §5.4). **Bắt đầu tCPA tuần 8 phút cuối.** |
| **W9** | 12.5 | 14,620 | 75 | 167 | tCPA 200k | **Bước vào kỳ 3 (D60+):** tCPA learning 2 tuần. CPL-q giữ mục tiêu. Không chuyển PMax (kỷ luật gate: chưa đủ placement exclusion setup để đảm bảo không burn với PMax). |
| **W10** | 12.5 | 14,580 | 76 | 164 | tCPA 200k | tCPA tuần 2, hiệu suất ổn. Thị trường nóng T9-12: CPC +15% áp từ tuần 10 → bid cap +15% → 40k₫. Adjustment: tCPA giữ 200k. |
| **W11** | 12.5 | 13,810 | 70 | 179 | tCPA 200k +15% CPC | Áp mùa vụ: CPC +15% (thị trường), click ↓ ~5%, CPL tăng nhẹ do CPC. Contact rate giữ 58% (ECL lọc ổn). |
| **W12** | 12.5 | 13,950 | 74 | 169 | tCPA 200k + final review | **D90 kết thúc:** chiến dịch ổn, không kill rule kích hoạt. Kiểm tra D90: có bao nhiêu contact được gắn tag contactable trong 48h (SLA) → input vào ECL D91+. Khế ước ECL vẫn hiệu lực sang quarter tiếp. |

---

## Quyết định tại các mốc D30 / D45 / D60 / D74+

### D30 (Tuần 4):
**Milestone:** 195 lead-q tích lũy, CPL-q blended 258k₫, contact rate 59%.
**Quyết định:** **Không áp D30 mộc (tài khoản đã G3 từ D0).** ECL chạy từ W1, conversion tracking chuẩn. Pass D30 checkpoint. → Sẵn sàng mở gate D45.
**Căn cứ:** `playbook/customer-journey-plan.md` §3.2 (gate G3 đạt từ D0: "35 conv qualified/30 ngày, ECL chạy ổn" → không cần verify lại).

### D45 (Tuần 6 start):
**Milestone:** 54 conv qualified W1-4 (≥30/30 ngày), ECL upload ổn, contact rate 58%.
**Quyết định:** **Chuyển Maximize Conversions.** Primary conversion: `Lead_Contactable` (từ ECL upload). Learning reset ×0.85 W5-6, hệ số ×1.15 áp W7+.
**Không áp AI Max** vì shared budgets giữ (tối ưu quản lý 3 dự án, portfolio bidding nếu cần tCPA riêng dự án). Broadcast strategy: Search T1+T2 chung, Demand Gen/Remarketing từ D60.
**Căn cứ:** `research/google-ads-bds-vn.md` §4 (lộ trình: Maximize Conversions sau ≥30 conv/30 ngày + import offline); `tracking/README.md` luật #2 (Primary = offline conversion, Secondary = form/click).

### D60 (Tuần 8):
**Milestone:** Maximize Conversions ✔ tuần 2 (W6-7), CPL-q 174k (tốt), xem_bang_gia 1.100 user, contact rate 60%.
**Quyết định 1 — tCPA:** **Bật tCPA = 200k ₫** (174k baseline +15% safety margin). Learning phase W9-10.
**Quyết định 2 — Demand Gen vs PMax:**
- **Chọn: Không bật PMax.** Lý do: §5.4(b) "hoãn PMax" + bẫy checklist (cần brand exclusion fully setup, campaign negative, content exclusion — rủi ro burn ngân sách vào app/placement rác nếu chỉnh bên lề). 
- Demand Gen chưa bật (để tCPA Search + remarketing GA4 + Display là đủ).
- Nếu D90 CPL-q < 150k ổn, round sau D0+ mở Demand Gen chuyên với tCPA riêng.
**Căn cứ:** `playbook/customer-journey-plan.md` §2.1 gate G2 (content `xem_bang_gia` ≥1000/30d → unlock Demand Gen); `research/google-ads-bds-vn.md` §1 PMax pitfall (loại app/game = bắt buộc exclusion, không phải optional); `PLAN.md` §0.5 (PMax chỉ khi ECL ổn + lead qualified ≥30/tháng — điểm này thỏa, nhưng defer vì gate checklist).

### D74+ (Tuần 10+):
**Milestone:** tCPA ×2 tuần chạy, đạt target ≥30 conv/30 ngày W9-12 tích lũy ~288 lead-q, contact rate ổn.
**Quyết định:** **Giữ tCPA, không chuyển bậc cao hơn.** Value-based bidding (lead value phân tầng theo geo/device) = optional khi ≥15 conv/30 ngày + đã có CPA chính xác theo dự án. Hiện 3 dự án gộp → chưa cần phân tầng, tCPA 200k trung bình phù hợp.
**Thị trường nóng W10-12:** mùa vụ T10-12 (CPC +15% YoY, sản phẩm cung +128k sản phẩm 2025) → **đổi ngân sách +15% hoặc tCPA ±0% giữ ngân sách, giảm volume.** Chọn: **tCPA giữ, lãnh nhận volume ↓, CPL duy trì ≥180k₫** (đảm bảo margin).
**Căn cứ:** `research/google-ads-bds-vn.md` §4 (mùa vụ: T10-12 cao điểm CPC + sản phẩm, dự phòng CPC +20-30% YoY); `PLAN.md` §0.6 (mùa vụ VN đổi ±20% ngân sách/lần, đợi 4 tuần báo giá mục tiêu mới — nhưng thông báo trước).

---

## Tổng 90 ngày

| KPI | Kết quả |
|---|---|
| **Tổng chi tiêu** | 12.5M × 12 = **150M ₫** (150tr/tháng × 3 tháng) |
| **Tổng click** | 14,286 + 14,475 + ... + 13,950 = **172,571 clicks** |
| **Tổng lead-q** | 42 + 48 + 51 + 54 + 62 + 58 + 68 + 72 + 75 + 76 + 70 + 74 = **750 lead-q** |
| **CPL-q blended** | 150,000k₫ / 750 = **200k ₫** |
| **Contact rate (cuối D90)** | **60%** (từ 58% D0, tăng +2% do ECL optimize). 45 contacts/100 leads từ offline tagging SLA <48h. |
| **Bậc bidding cuối kỳ** | tCPA 200k (tuần 8-12) |
| **Gates đã mở** | G3 ✔ (từ D0), G4 @ D45 (Maximize Conversions ready, không bật), G2 @ D60 (content threshold met, Demand Gen chờ next round). **G1, G5 chưa đạt:** G1 = YouTube (không budget dự án nhỏ), G5 = PMax (defer). |
| **CPL vs benchmark** | Đạt target: 200k < 1.560k (benchmark "trung bình"). Xếp hạng: **Tốt** (CPL ÷ CPC = 200÷25 = 8×, margin ngành 3-10×). |

---

## 3 bài học

1. **ECL từ D0 là bổ chân.** Tài khoản này khác từ D1 (không cần chờ Keap sync D30): bidding chuyển sớm D45 thay vì D60, learning reset nhỏ, CPL-q 258k → 174k trong 4 tuần tới 2 tuần Maximize Conversions. **Hệ quả:** chưa import CRM từ đầu = thua máu 4-6 tuần so với tài khoản này. Áp lực nếu dự án áp thời gian (Q4 mở bán) → ưu tiên ECL ngay tuần W0.

2. **Broad match + AI Max bị khóa là không phải sự cố.** Lệnh giữ shared budgets thay portfolio bidding tối ưu để quản lý 3 dự án 1 tCPA chung (chứ không phải tCPA riêng dự án). Khi dự án cân bằng CPL (dự án A: 120k, B: 180k, C: 280k) → lúc đó portfolio bidding + AI Max để tối ưu từng dự án. **Hiện tại:** tCPA trung bình 200k không phí (hành động logic).

3. **PMax chưa phải bộ không cần.** Gate D60 đạt (content + conv volume), nhưng Demand Gen → Search + remarketing GA4 tỏ ra đủ (CPL-q 167-184k). PMax ở Q1 2027 nếu: (a) SEO content bơm traffic `xem_bang_gia` → cold audience Demand Gen lớn (tính quy mô), hoặc (b) ECL sạch >65% contact rate (hiện 60%, margin nhỏ). Chọn defer = **kiểm soát rủi ro asset spam** khi tài khoản mới ổn định. **Chi phí:** 8% ngân sách W5-12 chưa deploy = 12.5M × 8% × 8 tuần = 8M₫ (lãng phí tiềm tàng), **lợi:** phòng PMax mua rác → +20% chi tiêu hao phí (mục 23, sim-rules.md). Chọn 8M dự trữ > rủi ro 20% toàn bộ ngân sách.

---

**Kết luận:** Round 5 đạt KPI: CPL-q 200k ✔ (vs benchmark 1.560k), contact rate 60% ✔ (vs target >50%), lead-q 750/90d ✔ (yield 250/tháng chặn đầu D45-D90 tối ưu). Không kích active kill rule. Sẵn sàng scale Q1 2027 bằng G2 Demand Gen + G1 YouTube (nếu dự án lớn).
