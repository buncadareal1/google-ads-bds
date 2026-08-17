#!/usr/bin/env python
"""Báo cáo nhanh 1 lệnh: kéo toàn bộ chỉ số Ads của campaign Beachtro.
Chạy: .venv-ads/bin/python scripts/bao_cao.py
GA4 kéo riêng qua MCP analytics-ga4 (xem skill phan-tich)."""
import sys, os, json, datetime
sys.path.insert(0, os.path.dirname(__file__))
from ads_client import client, ACCOUNT, M, retry

CAMPAIGN = 24103805490  # ponytail: hardcode Beachtro; tham số hóa khi có dự án 2
REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

c = client()
svc = c.get_service("GoogleAdsService")
def q(query): return list(retry(lambda: svc.search(customer_id=ACCOUNT, query=query)))

STATUS = q(f"SELECT campaign.status FROM campaign WHERE campaign.id={CAMPAIGN}")[0].campaign.status.name
NGHI = STATUS != "ENABLED"
if NGHI:
    print(f"⏸️  CAMPAIGN {STATUS} — không chi tiền, mọi review đóng băng. Bật lại = KỲ ĐO MỚI, cấm nối số với kỳ cũ.\n")

print("=== THAY ĐỔI ĐANG CHÍN (chưa tới hạn = CẤM phán tác động) ===")
today = datetime.date.today()
try:
    for line in open(os.path.join(REPO, "ops/change-log.jsonl")):
        e = json.loads(line)
        if e.get("reviewed"): continue
        left = (datetime.date.fromisoformat(e["review_sau"]) - today).days
        tag = f"còn {left} ngày" if left > 0 else "⏰ TỚI HẠN REVIEW"
        print(f"{e['date']} | {e['thay_doi']} | review {e['review_sau']} ({tag})")
except FileNotFoundError:
    print("(chưa có ops/change-log.jsonl)")

HONG = set()
try:
    for line in open(os.path.join(REPO, "ops/ngay-hong.txt")):
        if line.strip() and not line.startswith("#"): HONG.add(line.split("|")[0].strip())
except FileNotFoundError: pass

print("\n=== 📌 VIỆC ĐẾN HẠN ===")
import subprocess
ahead = subprocess.run(["git", "-C", REPO, "rev-list", "--count", "origin/main..HEAD"],
                       capture_output=True, text=True).stdout.strip()
if ahead not in ("", "0"): print(f"⚠️ {ahead} commit chưa push — push ngay (mất máy = mất hệ)")
if today.weekday() == 4 and not NGHI:  # thứ 6
    import glob
    aif = glob.glob(os.path.join(REPO, "projects/beachtro-tower/data/ads/auction-insights-*.csv"))
    latest = max((os.path.basename(f) for f in aif), default="CHƯA CÓ FILE NÀO")
    print(f"📥 THỨ 6: tải tay Auction Insights → data/ads/ (mới nhất: {latest}) + quét search terms (UPDATE.md)")
if today.weekday() == 0 and today.day <= 7:
    print("🔍 T2 ĐẦU THÁNG: rà auto-apply recommendations còn TẮT không (Google tự bật lại)")
for moc, viec in [("2026-09-03", "Tuần 4: CHỐT CPL MỤC TIÊU (plan-chay-ads §5) + quyết định bidding")]:
    d = (datetime.date.fromisoformat(moc) - today).days
    if 0 <= d <= 7 and not NGHI: print(f"🎯 {viec} — còn {d} ngày ({moc})")

print("\n=== NGÀY (7 ngày, IS chỉ tin ngày ĐÃ CHỐT) ===")
days = []
for r in q(f"""SELECT segments.date, metrics.impressions, metrics.clicks, metrics.ctr,
  metrics.average_cpc, metrics.cost_micros, metrics.conversions,
  metrics.search_impression_share, metrics.search_rank_lost_impression_share,
  metrics.search_budget_lost_impression_share, metrics.absolute_top_impression_percentage
FROM campaign WHERE segments.date DURING LAST_7_DAYS AND campaign.id={CAMPAIGN} ORDER BY segments.date"""):
    m = r.metrics
    days.append((str(r.segments.date), m.clicks, m.search_impression_share))
    if str(r.segments.date) in HONG: print("⛔ NGÀY ĐÁNH DẤU (ops/ngay-hong.txt) — loại khỏi trung bình/so sánh:")
    print(f"{r.segments.date} | impr {m.impressions} | click {m.clicks} | CTR {m.ctr*100:.1f}% | "
          f"CPC {m.average_cpc/M:,.0f}đ | chi {m.cost_micros/M:,.0f}đ | conv {m.conversions} | "
          f"IS {m.search_impression_share*100:.0f}% | mất-rank {m.search_rank_lost_impression_share*100:.0f}% | "
          f"mất-budget {m.search_budget_lost_impression_share*100:.0f}% | abs-top {m.absolute_top_impression_percentage*100:.0f}%")
closed = [d for d in days if d[0] != str(today)]
if closed and closed[-1][2] > 0:
    is_ = closed[-1][2]; clicks7 = sum(d[1] for d in closed)
    print(f"→ TRẦN VOLUME: IS chốt {is_*100:.0f}% → tối đa còn +{clicks7*(1/is_-1):,.0f} click/tuần "
          f"nếu IS 100% (kèm luật giảm dần: 2× tiền ≈ 1,5-1,7× conv)")

print("\n=== HÔM NAY THEO GIỜ ===")
ti = tc = tcost = 0
for r in q(f"""SELECT segments.hour, metrics.impressions, metrics.clicks, metrics.cost_micros
FROM campaign WHERE segments.date DURING TODAY AND campaign.id={CAMPAIGN} AND metrics.impressions>0 ORDER BY segments.hour"""):
    m = r.metrics; ti += m.impressions; tc += m.clicks; tcost += m.cost_micros
    print(f"{r.segments.hour:02d}h | impr {m.impressions} | click {m.clicks} | chi {m.cost_micros/M:,.0f}đ")
print(f"TỔNG HÔM NAY: impr {ti} | click {tc} | chi {tcost/M:,.0f}đ")

print("\n=== MẠNG HIỂN THỊ 7 NGÀY (campaign Search KHÔNG được có dòng CONTENT — bẫy #18) ===")
for r in q(f"""SELECT segments.ad_network_type, metrics.impressions, metrics.clicks, metrics.cost_micros, metrics.conversions
FROM campaign WHERE segments.date DURING LAST_7_DAYS AND campaign.id={CAMPAIGN}"""):
    m = r.metrics; net = r.segments.ad_network_type.name
    warn = "  ⛔ RÒ TIỀN — tắt target_content_network" if net == "CONTENT" else ""
    print(f"{net} | impr {m.impressions} | click {m.clicks} | chi {m.cost_micros/M:,.0f}đ | conv {m.conversions:.1f}{warn}")

print("\n=== SEARCH TERMS 7 NGÀY (lệch tổng chi = term ẩn) ===")
st_cost = 0; n = 0
for r in q(f"""SELECT search_term_view.search_term, metrics.impressions, metrics.clicks, metrics.cost_micros
FROM search_term_view WHERE segments.date DURING LAST_7_DAYS AND campaign.id={CAMPAIGN} ORDER BY metrics.impressions DESC"""):
    m = r.metrics; st_cost += m.cost_micros; n += 1
    print(f"{r.search_term_view.search_term} | impr {m.impressions} | click {m.clicks} | chi {m.cost_micros/M:,.0f}đ")
print("(0 dòng — phân biệt với query hỏng: query hỏng thì raise, không im lặng)" if n == 0
      else f"(tổng chi search terms nhìn thấy: {st_cost/M:,.0f}đ)")

print("\n=== TOP KEYWORD CẦN SỬA QS (xếp theo chi × (5−QS), 7 ngày) ===")
prio = []
for r in q(f"""SELECT ad_group.name, ad_group_criterion.keyword.text, ad_group_criterion.quality_info.quality_score,
  metrics.cost_micros FROM keyword_view WHERE segments.date DURING LAST_7_DAYS AND campaign.id={CAMPAIGN}"""):
    qs = r.ad_group_criterion.quality_info.quality_score
    if qs and qs < 8 and r.metrics.cost_micros:
        prio.append((r.metrics.cost_micros*(5-qs) if qs < 5 else r.metrics.cost_micros*(8-qs)*0.2,
                     r.ad_group_criterion.keyword.text, qs, r.metrics.cost_micros))
for _, kw, qs, cost in sorted(prio, reverse=True)[:5]:
    print(f"{kw} | QS {qs} | chi {cost/M:,.0f}đ (brand kw chuẩn phải QS 8-10; QS 6 ≈ +17% CPC)")
if not prio: print("(0 dòng — mọi keyword có chi đều QS ≥ 8)")

print("\n=== CONVERSION ACTION (lead-gen phải là ONE_PER_CLICK) ===")
for r in q("""SELECT conversion_action.name, conversion_action.counting_type, conversion_action.primary_for_goal,
  conversion_action.status FROM conversion_action WHERE conversion_action.status = 'ENABLED'"""):
    ca = r.conversion_action
    flag = "" if ca.counting_type.name == "ONE_PER_CLICK" else " ⚠️ KHÔNG PHẢI ONE_PER_CLICK — kiểm ngay (đếm trùng thổi phồng conv)"
    print(f"{ca.name} | {ca.counting_type.name} | primary: {ca.primary_for_goal}{flag}")

print("\n=== TRẠNG THÁI AD + POLICY ===")
for r in q(f"""SELECT campaign.primary_status, campaign.primary_status_reasons FROM campaign WHERE campaign.id={CAMPAIGN}"""):
    print(f"campaign primary: {r.campaign.primary_status.name} | reasons: {[x.name for x in r.campaign.primary_status_reasons]}")
for r in q(f"""SELECT ad_group.name, ad_group_ad.ad.id, ad_group_ad.status, ad_group_ad.policy_summary.approval_status,
  ad_group_ad.policy_summary.policy_topic_entries, ad_group_ad.ad_strength
FROM ad_group_ad WHERE campaign.id={CAMPAIGN} AND ad_group_ad.status != 'REMOVED'"""):
    print(f"{r.ad_group.name} | ad {r.ad_group_ad.ad.id} | {r.ad_group_ad.status.name} | duyệt: {r.ad_group_ad.policy_summary.approval_status.name} | strength: {r.ad_group_ad.ad_strength.name}")
    for e in r.ad_group_ad.policy_summary.policy_topic_entries:
        print(f"  ⛔ POLICY: {e.topic} ({e.type_.name})")
