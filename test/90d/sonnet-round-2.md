# Round 2 — Sonnet 5 — 90 ngày

**Kịch bản:** 60tr₫/tháng (2.000.000₫/ngày) · 2 dự án — **Eco Retreat** (Ecopark/DB Invest, Thanh Phú, Bến Lức, Long An) + **Legacy Central** (Kim Oanh Group, Thuận An, Bình Dương) · CPC kịch bản **28.000₫** (32.200₫ tuần 9-12, +15% mùa nóng, `sim-rules-90` cố định).
**Bẫy tuần 3:** Google rep mời bật PMax + auto-apply recommendations ("+20% conversion, chuyên gia miễn phí") khi tài khoản mới báo **11 conv/30 ngày** (chỉ mới chạy ~3 tuần, chưa đủ cửa sổ 30 ngày → số thấp hơn mô hình ổn định, không phải bug), ECL chưa chạy; UI có đề xuất `Remove conflicting negative keywords` chờ auto-apply.

## Setup + quyết định kỳ 1 (có xử lý bẫy)

**Cấu trúc 60tr** (`campaign-setup` §5.1, 2 dự án ≤ ngưỡng 6 dự án/#1 ở bậc này): #1 `Brand_DuAn` 583k/ngày (2 ad group `brand-eco-retreat`, `brand-legacy-central`) · #2 `Brand_CDT` 117k (Ecopark Group, Kim Oanh Group) · #3 `KhuVuc_GiaoDich` 570k+57k (#8 NOXH gộp vào vì không phân phối NOXH, §2.1) = **627k**, 4 ad group `ben-luc--gia-bang-gia/mua-ban` + `thuan-an--gia-bang-gia/mua-ban` · #4 `TaiChinh` 133k. Tổng active ngày 1 = **1.460.000₫/ngày**. #7 Discovery (100k), Demand Gen (300k), #5 PhapLy_TienDo (60k), #6 NghienCuu (80k) = **540k/ngày giữ lại (held)** — chưa qua gate (G2/G3/tCPA), không dựng campaign rỗng chờ (`campaign-setup` §2.1). Bộ kw `uu_tien 1+2` lọc theo 2 dự án (`journey-plan` §3, 7.825 kw trước lọc).

Bidding **Max Clicks + bid cap** cả 4 campaign active (bậc 0, 0 conversion — `journey-plan` §3.2). Conversion ladder đủ 6 action, Count=Một, cửa sổ 90 ngày, category chuẩn (§1.2.7); ngày 1 primary = `Lead_Form_Raw`+`Click_Hotline`+`Click_Zalo`, 3 action offline khai rỗng. Negative 382 account-level + 83 campaign-level nhập ngày 1 (không rác 25% burn). 11 ô §1.5 áp đủ, **auto-apply TẮT HẾT** (§1.5.11). G0 pass (1 lead thật → GA4 → Ads → Keap có gclid) trước khi bật.

**LP (2 dự án, `landing-page/README.md` ma trận):** Eco Retreat dùng số thật đã xác minh (`research/competitors/2026-07-eco-retreat.md`): "từ 2,5 tỷ", vay 70% miễn gốc lãi 24 tháng, CK tới 12% TT sớm 95% → đủ 4 adder (+1,0 message match · +0,8 bảng giá · +0,6 Zalo sticky/CTC · +0,4 form 2 dropdown) = **CVR 4,8%**. Legacy Central: **chưa có vòng competitor research riêng** (`research/competitors/` mới chỉ có Eco Retreat) — bảng giá dùng theo tài liệu nội bộ sàn (không phải web-scrape, không bịa số theo `CLAUDE.md`); nếu đến D-1 sàn chưa cung cấp bảng giá thật thì bỏ headline `Giá Từ X tỷ` và adder +0,8, dùng CTA "Nhận bảng giá mới nhất qua Zalo" (an toàn theo `research` §7 minh bạch chi phí). Giả định vận hành: sàn cung cấp kịp → **CVR 4,8% cả hai dự án**. Qualify 40% (2 dropdown), contact 55% (dropdown+validate đầu số+SLA gọi <5').

**🚨 Xử lý bẫy tuần 3 — TỪ CHỐI CẢ HAI:**
1. **PMax:** không đủ **bất kỳ điều kiện nào** của G4 (`journey-plan` §3.1): ECL chưa chạy (D30 chưa tới) · 11 conv/30 ngày « 30 conv/tháng yêu cầu · brand exclusion chưa dựng · đang ở bậc 0 (Max Clicks), còn cách bậc 5 (PMax) 5 bậc AI (`journey-plan` §3.2). "11 conv" thấp vì tài khoản mới <30 ngày lịch sử, không phải vì cần "chuyên gia AI" — đúng cái bẫy Google rep đang khai thác (số nhỏ trông đáng thương). Từ chối, ghi lý do vào log.
2. **Auto-apply + `Remove conflicting negative keywords`:** đã TẮT từ ngày 1 (§1.5.11 — "đặc biệt nguy hiểm với đề xuất này, phá negative list"). Rà lại: vẫn tắt, dismiss đề xuất thủ công (không apply), không có conflict thật (đã rà chéo negative×launch-set lúc setup, §1.4.4). Không đụng gì.
Căn cứ tổng: `PLAN.md` §0.1/§0.5 (không thêm công cụ khi chưa có data chứng minh cần) · `campaign-setup` §5.4/§5.5 (checklist PMax 12 bước, chưa tới lượt).

## Bảng 12 tuần

| Tuần | Chi (tr) | Click | Contact% | Lead-q | CPL-q (tr) | Bậc bidding | Ghi chú |
|---|---|---|---|---|---|---|---|
| 1 | 10,22 | 365 | 55% | 7,01 | 1,46 | Max Clicks | Setup xong, G0 pass, không đổi gì tuần 1 |
| 2 | 10,22 | 365 | 55% | 7,01 | 1,46 | Max Clicks | Search terms vòng 1 — chỉ thêm negative rõ sai ngành |
| 3 | 10,22 | 365 | 55% | 7,01 | 1,46 | Max Clicks | 🚨 Bẫy rep PMax+auto-apply — TỪ CHỐI cả hai (xem trên) |
| 4 | 10,22 | 365 | 55% | 7,01 | 1,46 | Max Clicks | RSA thứ 2/ad group; đọc 10 lead gần nhất → contact rate lần đầu 55% |
| 5 | 10,22 | 365 | 55% | 7,01 | 1,46 | Max Clicks | **D30**: Keap ký, `upload_ecl.py` chạy thật; báo thêm %SLA48h=85% |
| 6 | 10,22 | 365 | 55% | 7,01 | 1,46 | Max Clicks | Tích luỹ trailing 30 ngày hướng D45 |
| 7 | 10,22 | 365 | 55% | 5,96 | 1,72 | MaxConv (learning ×0,85) | **D45**: đảo primary→`Lead_Contactable` TRƯỚC, rồi bật Maximize Conversions |
| 8 | 10,22 | 365 | 55% | 5,96 | 1,72 | MaxConv (learning ×0,85) | Không đụng ngân sách/target trong learning |
| 9 | 12,32 | 382,6 | 55% | 8,52 | 1,45 | MaxConv (×1,15 vĩnh viễn) | **D60**: G2 mở, Demand Gen 300k/ngày (15%) + Excluded content keywords điền đủ → +5% lead-q; CPC+15% mùa nóng bắt đầu |
| 10 | 12,32 | 382,6 | 55% | 8,52 | 1,45 | MaxConv | Ổn định, chuẩn bị D74 |
| 11 | 13,02 | 404,3 | 55% | 8,90 | 1,46 | tCPA (1,21tr = CPA-q lịch sử +15%) | **D74**: chuyển tCPA đúng ±15%; bật #7 Discovery broad+tCPA 100k/ngày |
| 12 | 13,02 | 404,3 | 55% | 8,90 | 1,46 | tCPA | Ổn định kỳ 3, tổng kết |

## Quyết định tại các mốc

**D30 — chỉ bật ECL, không đổi bidding.** `Lead_Contactable`/`Lead_Qualified` bắt đầu nhận dữ liệu thật qua Data Manager API (`tracking/README` luật #3). Từ đây báo thêm **%SLA48h = 85%** (giả định sales) — 15% lead mất tag không vào được tín hiệu ECL kịp, làm smart bidding tương lai học trên mẫu hơi mỏng hơn contact rate vận hành cho thấy. Không claim CVR improvement từ Clarity kỳ này — tài khoản mới ~30 ngày, session recording chưa đủ để rút insight thật; bịa insight = 0 điểm đo lường (`sim-rules-90` luật bổ sung) nên chọn không claim thay vì đoán.

**D45 — đủ điều kiện (raw conv trailing 30 ngày ổn định ~70/tháng ≥ 30)** → chuyển ĐÚNG thứ tự (`campaign-setup` §4.4): (1) đảo primary sang `Lead_Contactable` trước, (2) bật Maximize Conversions. Learning 2 tuần CVR×0,85 (tuần 7-8), sau đó hệ số hiệu quả ×1,15 vĩnh viễn (tuần 9+). Không đổi ngân sách trong 2 tuần learning.

**D60 — G2 mở** (organic/content đẩy `xem_bang_gia` ≥1.000 user/30 ngày — tự traffic ads không đủ, đúng cảnh báo `journey-plan` §3.1 G2). Bật Demand Gen 300k/ngày = **15%** ngân sách (đúng trần), đã điền `Excluded content keywords` cấp tài khoản (negative account-level không phủ YouTube/Display của Demand Gen, `campaign-setup` §5.5 hộp cảnh báo) → +5% lead-q thay vì 10% ngân sách DG cháy vào placement rác.

**D74 — đủ điều kiện (MaxConv ổn ≥2 tuần từ D45, ≥30 conv/30 ngày)** → chuyển tCPA = CPA-q lịch sử (≈1,05tr, tính từ contactable/tuần 9-10 trước switch) **+15%** ≈ **1,21tr**, đúng biên ±15% (không phạt reset). Đồng thời bật #7 Discovery broad+tCPA 100k/ngày (`campaign-setup` §4.4 bước 2), ngân sách lấy từ pool held sẵn, không rút từ campaign đang chạy.

**#5/#6 (PhapLy_TienDo, NghienCuu) và G4 (PMax): giữ nguyên held hết 90 ngày, có chủ đích.** G3 cần tCPA ổn **2 tháng liên tiếp** — mới có ~2 tuần (D74→D90) nên chưa đủ. G4 kỹ thuật gần đủ điều kiện data (ECL chạy 60 ngày, conv > 30/tháng) nhưng brand exclusion + asset 3 tỷ lệ (20 text/7 image/1 video) chưa chuẩn bị, và `campaign-setup` §5.7 chỉ cho **mở một gate mỗi lần, chờ đủ chu kỳ đo** — kỳ này đã mở 2 (bidding bậc 1→2 + G2), không dồn thêm G4.

## Tổng 90 ngày

| Chỉ số | Giá trị |
|---|---|
| Tổng chi | **132,44tr₫** (TB 44,15tr/tháng — dưới trần 60tr **có chủ đích**: 540k/ngày held đầu kỳ giảm dần khi G2/tCPA mở, #5/#6 giữ hết kỳ vì G3 chưa đủ) |
| Tổng lead qualified | **88,8** |
| CPL qualified blended | **1,49tr₫** (tốt hơn benchmark kịch bản trung bình ~1,56tr — `research` §2) |
| Contact rate vận hành | 55% suốt kỳ · %SLA48h từ D30: 85% |
| Bậc AI cuối (`journey-plan` §3.2) | **Bậc 2** — tCPA + ECL chạy thật + Discovery broad test |
| Gate đã mở | G0 ✅ (D0) · G2 ✅ (D60, Demand Gen 15%) |
| Gate từ chối đúng lúc | **G4/PMax** — bẫy tuần 3 từ chối khi 11 conv/ECL off; vẫn chưa mở cuối kỳ dù data gần đủ, vì thiếu brand exclusion + asset và luật "một gate/lần" |
| Gate chưa mở, có lý do bằng số | G3 (cần tCPA ổn 2 tháng, mới 2 tuần) · G1 (breakeven CPL mục tiêu vẫn `[điền]`, chưa có phí môi giới/căn từ CRM) · G5 (cần ≥150tr) |

## 3 bài học

1. **"Số nhỏ" không phải lý do bật AI sớm — nó thường là chính cái bẫy.** 11 conv/30 ngày ở tuần 3 chỉ phản ánh tài khoản chưa đủ 30 ngày lịch sử, không phải bằng chứng cần PMax "cứu". Gate G4 đọc theo *đủ điều kiện dữ liệu* (ECL chạy thật + ≥30 conv/tháng + brand exclusion), không đọc theo *cảm giác tài khoản còn nhỏ, chuyên gia mời miễn phí* — hai thứ trông giống nhau nhưng ngược nhau hoàn toàn.

2. **Tắt auto-apply ngày 1 không phải "xong vĩnh viễn" — `Remove conflicting negative keywords` phải bị từ chối lại mỗi lần nó xuất hiện.** Đây là đề xuất Google tự sinh định kỳ, không phải một lần bật/tắt; kỷ luật là quy trình lặp lại (rà + dismiss thủ công), không phải một ô tick đã xong ở §1.5.11.

3. **60tr₫ ngân sách không bắt buộc chi hết 60tr₫.** Chi thực 44,15tr/tháng (74% trần) vì #5/#6/G3 chưa đạt điều kiện là kết quả đúng của kỷ luật gate, không phải vận hành kém — ép chi hết bằng cách mở campaign type chưa đủ data (đúng thứ Google rep tuần 3 mời) mới là sai.
