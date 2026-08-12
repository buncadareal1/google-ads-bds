#!/usr/bin/env python
"""Báo cáo nhanh 1 lệnh: kéo toàn bộ chỉ số Ads của campaign Beachtro.
Chạy: .venv-ads/bin/python scripts/bao_cao.py
GA4 kéo riêng qua MCP analytics-ga4 (xem skill phan-tich)."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from ads_client import client, ACCOUNT, M, retry

CAMPAIGN = 24103805490  # ponytail: hardcode Beachtro; tham số hóa khi có dự án 2

c = client()
svc = c.get_service("GoogleAdsService")
def q(query): return list(retry(lambda: svc.search(customer_id=ACCOUNT, query=query)))

print("=== NGÀY (7 ngày, IS chỉ tin ngày ĐÃ CHỐT) ===")
for r in q(f"""SELECT segments.date, metrics.impressions, metrics.clicks, metrics.ctr,
  metrics.average_cpc, metrics.cost_micros, metrics.conversions,
  metrics.search_impression_share, metrics.search_rank_lost_impression_share,
  metrics.search_budget_lost_impression_share, metrics.absolute_top_impression_percentage
FROM campaign WHERE segments.date DURING LAST_7_DAYS AND campaign.id={CAMPAIGN} ORDER BY segments.date"""):
    m = r.metrics
    print(f"{r.segments.date} | impr {m.impressions} | click {m.clicks} | CTR {m.ctr*100:.1f}% | "
          f"CPC {m.average_cpc/M:,.0f}đ | chi {m.cost_micros/M:,.0f}đ | conv {m.conversions} | "
          f"IS {m.search_impression_share*100:.0f}% | mất-rank {m.search_rank_lost_impression_share*100:.0f}% | "
          f"mất-budget {m.search_budget_lost_impression_share*100:.0f}% | abs-top {m.absolute_top_impression_percentage*100:.0f}%")

print("\n=== HÔM NAY THEO GIỜ ===")
ti = tc = tcost = 0
for r in q(f"""SELECT segments.hour, metrics.impressions, metrics.clicks, metrics.cost_micros
FROM campaign WHERE segments.date DURING TODAY AND campaign.id={CAMPAIGN} AND metrics.impressions>0 ORDER BY segments.hour"""):
    m = r.metrics; ti += m.impressions; tc += m.clicks; tcost += m.cost_micros
    print(f"{r.segments.hour:02d}h | impr {m.impressions} | click {m.clicks} | chi {m.cost_micros/M:,.0f}đ")
print(f"TỔNG HÔM NAY: impr {ti} | click {tc} | chi {tcost/M:,.0f}đ")

print("\n=== SEARCH TERMS 7 NGÀY (lệch tổng chi = term ẩn) ===")
st_cost = 0
for r in q(f"""SELECT search_term_view.search_term, metrics.impressions, metrics.clicks, metrics.cost_micros
FROM search_term_view WHERE segments.date DURING LAST_7_DAYS AND campaign.id={CAMPAIGN} ORDER BY metrics.impressions DESC"""):
    m = r.metrics; st_cost += m.cost_micros
    print(f"{r.search_term_view.search_term} | impr {m.impressions} | click {m.clicks} | chi {m.cost_micros/M:,.0f}đ")
print(f"(tổng chi search terms nhìn thấy: {st_cost/M:,.0f}đ)")

print("\n=== TRẠNG THÁI AD + POLICY ===")
for r in q(f"""SELECT campaign.primary_status, campaign.primary_status_reasons FROM campaign WHERE campaign.id={CAMPAIGN}"""):
    print(f"campaign primary: {r.campaign.primary_status.name} | reasons: {[x.name for x in r.campaign.primary_status_reasons]}")
for r in q(f"""SELECT ad_group.name, ad_group_ad.ad.id, ad_group_ad.status, ad_group_ad.policy_summary.approval_status,
  ad_group_ad.policy_summary.policy_topic_entries, ad_group_ad.ad_strength
FROM ad_group_ad WHERE campaign.id={CAMPAIGN} AND ad_group_ad.status != 'REMOVED'"""):
    print(f"{r.ad_group.name} | ad {r.ad_group_ad.ad.id} | {r.ad_group_ad.status.name} | duyệt: {r.ad_group_ad.policy_summary.approval_status.name} | strength: {r.ad_group_ad.ad_strength.name}")
    for e in r.ad_group_ad.policy_summary.policy_topic_entries:
        print(f"  ⛔ POLICY: {e.topic} ({e.type_.name})")
