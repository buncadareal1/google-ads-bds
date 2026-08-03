#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Bài thi Performance Marketing Lead - thí sinh 6. Mọi số trong agent-6.md sinh từ file này.
Nguồn: /home/docdang/Downloads/du_lieu_google_ads_90_ngay_1.csv (= sheet 02_DU_LIEU_NGAY)
       + sheets/*.csv (03..12)
Chạy: python3 agent-6-calc.py
"""
import csv, io, os
from collections import defaultdict

CSV = "/home/docdang/Downloads/du_lieu_google_ads_90_ngay_1.csv"
SH = "/home/docdang/Projects/google-ads/test/exam-vinhomes/sheets"
M = 1_000_000

rows = []
with io.open(CSV, encoding="utf-8-sig") as f:
    for r in csv.DictReader(f):
        for k in ("Hien_thi","Nhap_chuot","Chi_phi","ChuyenDoi_Ads","Lead_CRM","Lead_SQL",
                  "Di_Xem_Nha","Booking","Dat_Coc","DoanhThu_HoaHong","Ngay_thu","Tuan"):
            r[k] = float(r[k])
        # IS chỉ có ở 3 chiến dịch Search — PMax/GDN/YT để trống
        for k in ("Impr_Share","Mat_IS_NganSach","Mat_IS_ThuHang"):
            r[k] = float(r[k]) if r[k] not in ("", None) else None
        rows.append(r)

NUM = ["Hien_thi","Nhap_chuot","Chi_phi","ChuyenDoi_Ads","Lead_CRM","Lead_SQL",
       "Di_Xem_Nha","Booking","Dat_Coc","DoanhThu_HoaHong"]

def agg(rs):
    d = {k: sum(r[k] for r in rs) for k in NUM}
    return d

def div(a, b): return a / b if b else 0.0

def fmt_vnd(x): return f"{x:,.0f}".replace(",", ".")

out = []
def P(*a):
    s = " ".join(str(x) for x in a)
    out.append(s); print(s)

# ---------------------------------------------------------------- tổng quan
tot = agg(rows)
P("="*70); P("0. TỔNG KIỂM TRA (sheet 02 vs sheet 03)")
P(f"  ngày={len(set(r['Ngay'] for r in rows))} dòng={len(rows)} chiến dịch={len(set(r['Chien_dich'] for r in rows))}")
for k in NUM: P(f"  {k:22s} = {tot[k]:,.0f}")

camps = sorted(set(r["Chien_dich"] for r in rows))
phases = ["GĐ1","GĐ2","GĐ3"]

# ---------------------------------------------------------------- B1
P("\n"+"="*70); P("B1. CPL Ads / CPL CRM / CP-SQL / CP-cọc  — toàn kỳ & từng chiến dịch")
P(f"{'Chiến dịch':34s} {'Chi phí(tr)':>11s} {'CPLAds(tr)':>10s} {'CPLCRM(tr)':>10s} {'CP/SQL(tr)':>10s} {'CP/cọc(tr)':>11s} {'SQL/Lead':>9s} {'Ads/CRM':>8s}")
B1 = {}
for c in camps + ["TOÀN KỲ"]:
    rs = rows if c == "TOÀN KỲ" else [r for r in rows if r["Chien_dich"] == c]
    a = agg(rs)
    d = dict(cost=a["Chi_phi"], cpl_ads=div(a["Chi_phi"],a["ChuyenDoi_Ads"]),
             cpl_crm=div(a["Chi_phi"],a["Lead_CRM"]), cpsql=div(a["Chi_phi"],a["Lead_SQL"]),
             cpcoc=div(a["Chi_phi"],a["Dat_Coc"]), sqlrate=div(a["Lead_SQL"],a["Lead_CRM"]),
             adscrm=div(a["ChuyenDoi_Ads"],a["Lead_CRM"]), **a)
    B1[c] = d
    P(f"{c:34s} {a['Chi_phi']/M:11.1f} {d['cpl_ads']/M:10.3f} {d['cpl_crm']/M:10.3f} "
      f"{d['cpsql']/M:10.3f} {d['cpcoc']/M:11.1f} {d['sqlrate']:9.1%} {d['adscrm']:8.2f}")

# ---------------------------------------------------------------- B2
P("\n"+"="*70); P("B2. ROAS toàn kỳ & theo giai đoạn")
P(f"{'Giai đoạn':10s} {'Chi phí(tr)':>11s} {'Doanh thu(tr)':>13s} {'ROAS':>6s} {'Cọc':>5s} {'CP/cọc(tr)':>11s}")
for g in phases + ["Toàn kỳ"]:
    rs = rows if g == "Toàn kỳ" else [r for r in rows if r["Giai_doan"] == g]
    a = agg(rs)
    P(f"{g:10s} {a['Chi_phi']/M:11.1f} {a['DoanhThu_HoaHong']/M:13.1f} {div(a['DoanhThu_HoaHong'],a['Chi_phi']):6.2f} "
      f"{a['Dat_Coc']:5.0f} {div(a['Chi_phi'],a['Dat_Coc'])/M:11.1f}")
P("  ROAS theo chiến dịch (toàn kỳ):")
for c in camps:
    a = B1[c]
    P(f"    {c:34s} ROAS={div(a['DoanhThu_HoaHong'],a['Chi_phi']):5.2f}  DT={a['DoanhThu_HoaHong']/M:8.0f}tr  cọc={a['Dat_Coc']:.0f}")

# ---------------------------------------------------------------- B3
P("\n"+"="*70); P("B3. Tỷ lệ chuyển đổi từng bước phễu")
def funnel(a, tag):
    P(f"  [{tag}] Lead={a['Lead_CRM']:.0f} SQL={a['Lead_SQL']:.0f} Xem={a['Di_Xem_Nha']:.0f} "
      f"Book={a['Booking']:.0f} Cọc={a['Dat_Coc']:.0f}")
    P(f"      Lead→SQL {div(a['Lead_SQL'],a['Lead_CRM']):7.2%} | SQL→Xem {div(a['Di_Xem_Nha'],a['Lead_SQL']):7.2%} | "
      f"Xem→Book {div(a['Booking'],a['Di_Xem_Nha']):7.2%} | Book→Cọc {div(a['Dat_Coc'],a['Booking']):7.2%} | "
      f"Lead→Cọc {div(a['Dat_Coc'],a['Lead_CRM']):7.3%} | SQL→Cọc {div(a['Dat_Coc'],a['Lead_SQL']):7.2%}")
funnel(tot, "Toàn kỳ")
for g in phases: funnel(agg([r for r in rows if r["Giai_doan"] == g]), g)
# phễu không tính các campaign zero-coc
core = [r for r in rows if r["Chien_dich"] in ("SEA_Brand_Vinhomes_HocMon","SEA_Generic_NhaPho_CanHo_TayBac")]
funnel(agg(core), "Chỉ 2 CD Search Brand+Generic")
g3 = agg([r for r in rows if r["Giai_doan"] == "GĐ3"])

# ---------------------------------------------------------------- B4
P("\n"+"="*70); P("B4. Backsolve KPI: 32 cọc / 2,1 tỷ")
BUDGET, TARGET_COC, HH = 2_100_000_000, 32, 181_000_000
scen = {
 "A. Tỷ lệ toàn kỳ 90 ngày (đã đo)":
   (div(tot['Dat_Coc'],tot['Lead_SQL']), div(tot['Lead_SQL'],tot['Lead_CRM'])),
 "B. Tỷ lệ GĐ3 (gần nhất, LP v2 + SLA 15p)":
   (div(g3['Dat_Coc'],g3['Lead_SQL']), div(g3['Lead_SQL'],g3['Lead_CRM'])),
 "C. Chỉ 2 CD Search Brand+Generic toàn kỳ (mix đề xuất)":
   (div(agg(core)['Dat_Coc'],agg(core)['Lead_SQL']), div(agg(core)['Lead_SQL'],agg(core)['Lead_CRM'])),
}
P(f"{'Kịch bản':56s} {'SQL→Cọc':>8s} {'Lead→SQL':>9s} {'SQL cần':>8s} {'Lead cần':>9s} {'CP/SQL trần(tr)':>16s} {'CPL trần(tr)':>13s}")
B4 = {}
for k,(sq, ls) in scen.items():
    sql_need = TARGET_COC/sq if sq else 0
    lead_need = sql_need/ls if ls else 0
    B4[k] = (sq, ls, sql_need, lead_need, div(BUDGET,sql_need), div(BUDGET,lead_need))
    P(f"{k:56s} {sq:8.2%} {ls:9.2%} {sql_need:8.0f} {lead_need:9.0f} {div(BUDGET,sql_need)/M:16.2f} {div(BUDGET,lead_need)/M:13.3f}")
cpl_crm_now = div(tot["Chi_phi"], tot["Lead_CRM"])
P(f"  KPI CP/SQL trần BGĐ giao = 2,20 tr → với ngân sách 2,1 tỷ mua được tối đa {BUDGET/2_200_000:.0f} SQL")
for k,(sq,ls,sn,ln,cps,cpl) in B4.items():
    P(f"    {k[:3]}: nếu chỉ đạt CP/SQL 2,20tr → {BUDGET/2_200_000:.0f} SQL × {sq:.2%} = {BUDGET/2_200_000*sq:.1f} cọc")
# giả định TÔI CHỌN cho kế hoạch: SQL→Cọc 3,4% (làm tròn xuống từ GĐ3 3,48%), Lead→SQL 32%
SQ_SEL, LS_SEL = 0.034, 0.32
sql_sel = TARGET_COC/SQ_SEL; lead_sel = sql_sel/LS_SEL
P(f"  [GIẢ ĐỊNH CHỌN] SQL→Cọc {SQ_SEL:.1%} (GĐ3 làm tròn xuống), Lead→SQL {LS_SEL:.0%} (giữa GĐ3 29,76% và 2 CD Search 37,60%)")
P(f"    → SQL cần = 32/{SQ_SEL} = {sql_sel:.0f} ({sql_sel/90:.1f}/ngày)")
P(f"    → Lead thô cần = {sql_sel:.0f}/{LS_SEL} = {lead_sel:.0f} ({lead_sel/90:.1f}/ngày; GĐ3 thực tế 35,4/ngày)")
P(f"    → CP/SQL trần = 2,1 tỷ/{sql_sel:.0f} = {fmt_vnd(BUDGET/sql_sel)}đ (KPI giao 2.200.000đ → chênh {BUDGET/sql_sel/2_200_000-1:+.1%})")
P(f"    → CPL thô trần = 2,1 tỷ/{lead_sel:.0f} = {fmt_vnd(BUDGET/lead_sel)}đ (CPL CRM hiện tại {fmt_vnd(cpl_crm_now)}đ)")
P(f"    → % năng lực sale dùng = {lead_sel/8640:.0%} của 8.640 lead trần")
# năng lực sale
P(f"  Năng lực sale: 8×12 = 96 lead/ngày × 90 = 8.640 lead trần lý thuyết (sheet 01 mục C)")
for k,(sq,ls,sn,ln,cps,cpl) in B4.items():
    P(f"    {k[:3]}: {ln:.0f} lead / 90 ngày = {ln/90:.1f} lead/ngày (GĐ3 thực tế 35,4 - sheet 08B)")

# ---------------------------------------------------------------- B5
P("\n"+"="*70); P("B5. Điểm hòa vốn ROAS 3,0x")
P(f"  Hoa hồng/cọc = {fmt_vnd(HH)}đ → chi phí QC tối đa/cọc = {fmt_vnd(HH/3)}đ (ROAS 3,0)")
P(f"  ROAS 1,0 (hòa vốn tuyệt đối, chưa trừ 45% sale + 20% vận hành) = {fmt_vnd(HH)}đ/cọc")
P(f"  Lợi nhuận gộp còn lại sau 45%+20% = 35% × {fmt_vnd(HH)} = {fmt_vnd(HH*0.35)}đ/cọc")
P(f"  → ROAS hòa vốn LỢI NHUẬN = 1/0,35 = {1/0.35:.2f}x ⇒ mục tiêu 3,0x là có lãi thật {fmt_vnd(HH*0.35-HH/3)}đ/cọc")
P(f"  Với 32 cọc: doanh thu HH = {fmt_vnd(32*HH)}đ; ngân sách 2,1 tỷ → ROAS = {32*HH/BUDGET:.2f}x")
P(f"  → Số cọc tối thiểu để ROAS 3,0 với 2,1 tỷ = {BUDGET*3/HH:.1f} → {int(-(-BUDGET*3//HH))} cọc")
P(f"  Ngân sách tối đa cho 32 cọc @ROAS3,0 = {fmt_vnd(32*HH/3)}đ (thấp hơn 2,1 tỷ {fmt_vnd(BUDGET-32*HH/3)}đ)")
P(f"  Thực tế 90 ngày qua: {tot['Dat_Coc']:.0f} cọc, ROAS {div(tot['DoanhThu_HoaHong'],tot['Chi_phi']):.2f}x, CP/cọc {fmt_vnd(div(tot['Chi_phi'],tot['Dat_Coc']))}đ "
  f"= {div(tot['Chi_phi'],tot['Dat_Coc'])/(HH/3):.1f}× ngưỡng cho phép")

# ---------------------------------------------------------------- B6
P("\n"+"="*70); P("B6. Đối chiếu 3 nguồn (sheet 10_GA4 mục A + sheet 12_GTM mục B)")
ga = dict(generate_lead=1715, c2c_total=1132, c2c_uniq=779, view_price=612, engaged=361)
ads_conv = ga["generate_lead"]+ga["c2c_total"]+ga["view_price"]+ga["engaged"]
dup = ga["c2c_total"]-ga["c2c_uniq"]
junk = ga["view_price"]+ga["engaged"]
tag_measured = ga["generate_lead"]+ga["c2c_uniq"]
lost_tag = 2557 - tag_measured
P(f"  (1) Ads/GA4 'Chuyển đổi'         = {ga['generate_lead']}+{ga['c2c_total']}+{ga['view_price']}+{ga['engaged']} = {ads_conv}   [khớp 3.820: {ads_conv==3820}]")
P(f"  (2) − đếm trùng click_to_call    = {ga['c2c_total']} lượt − {ga['c2c_uniq']} người = −{dup}")
P(f"  (3) − sự kiện rác (không phải lead) = view_price {ga['view_price']} + engaged_30s {ga['engaged']} = −{junk}")
P(f"      ⇒ Lead THẬT đo được bằng thẻ  = {ads_conv} − {dup} − {junk} = {tag_measured}   [khớp GA4 2.494: {tag_measured==2494}]")
P(f"  (4) + lead MẤT do gãy thẻ N44-46 (GTM v23, class .form-dk-v1→.form-register) = +{lost_tag}")
P(f"      ⇒ CRM lead thật                = {tag_measured} + {lost_tag} = {tag_measured+lost_tag}   [khớp CRM 2.557: {tag_measured+lost_tag==2557}]")
P(f"  Chứng minh: 3.820 − {dup} − {junk} + {lost_tag} = {ads_conv-dup-junk+lost_tag} = 2.557 ✔")
P(f"  Tỷ trọng thổi phồng: trùng {dup/ads_conv:.1%}, rác {junk/ads_conv:.1%}, tổng {(dup+junk)/ads_conv:.1%} của cột Chuyển đổi")
P(f"  Ads báo cao hơn CRM {ads_conv-2557} chuyển đổi = {(ads_conv-2557)/2557:.1%}; hệ số Ads/CRM = {ads_conv/2557:.2f} (sheet 09: >1,8x = báo động)")
# kiểm chứng N44-46 trong sheet 02
P("  Kiểm chứng sheet 02 (ChuyenDoi_Ads vs Lead_CRM theo Ngay_thu 43-48):")
for d in range(43, 49):
    a = agg([r for r in rows if r["Ngay_thu"] == d])
    P(f"    N{d:02.0f}: ChuyenDoi_Ads={a['ChuyenDoi_Ads']:5.0f}  Lead_CRM={a['Lead_CRM']:4.0f}  Chi_phi={a['Chi_phi']/M:6.1f}tr")
lost_days = agg([r for r in rows if r["Ngay_thu"] in (44,45,46)])
P(f"    Tổng N44-46: Lead_CRM={lost_days['Lead_CRM']:.0f}, ChuyenDoi_Ads={lost_days['ChuyenDoi_Ads']:.0f}, chi phí={lost_days['Chi_phi']/M:.1f}tr")

# ---------------------------------------------------------------- B7
P("\n"+"="*70); P("B7. Lead mất do lỗi kỹ thuật CHƯA SỬA (sheet 11_CLARITY mục C, #4/#5/#6)")
cpl_crm = div(tot["Chi_phi"], tot["Lead_CRM"])
cpsql_real = div(tot["Chi_phi"], tot["Lead_SQL"])
sqlrate = div(tot["Lead_SQL"], tot["Lead_CRM"])
coc_per_sql = div(tot["Dat_Coc"], tot["Lead_SQL"])
P(f"  [ĐO ĐƯỢC - Clarity] #4 lỗi JS setDate Safari iOS: 4.196 phiên ảnh hưởng | #5 nút bị chat che <380px: 2.741 | #6 tel: dead click desktop 1.204 (1.847 nhấp chết)")
P(f"  [ƯỚC TÍNH - đội UX, không phải số đo] lead mất: #4 280-340, #5 60-90, #6 30-50 → tổng 370-480")
for lo, hi, tag in [(280,340,"#4"),(60,90,"#5"),(30,50,"#6"),(370,480,"TỔNG")]:
    mid = (lo+hi)/2
    P(f"    {tag:5s} {lo}-{hi} lead (giữa {mid:.0f}) → tiền theo CPL CRM thực tế {fmt_vnd(cpl_crm)}đ: "
      f"{fmt_vnd(lo*cpl_crm)} - {fmt_vnd(hi*cpl_crm)}đ")
mid = 425
P(f"  [SUY RA - của tôi] {mid} lead × tỷ lệ SQL toàn kỳ {sqlrate:.1%} = {mid*sqlrate:.0f} SQL")
P(f"                     {mid*sqlrate:.0f} SQL × tỷ lệ SQL→Cọc toàn kỳ {coc_per_sql:.2%} = {mid*sqlrate*coc_per_sql:.1f} cọc")
P(f"                     × hoa hồng {fmt_vnd(HH)}đ = {fmt_vnd(mid*sqlrate*coc_per_sql*HH)}đ doanh thu bỏ lỡ")
P(f"  Dải: {370*sqlrate*coc_per_sql:.1f} - {480*sqlrate*coc_per_sql:.1f} cọc = {fmt_vnd(370*sqlrate*coc_per_sql*HH)} - {fmt_vnd(480*sqlrate*coc_per_sql*HH)}đ")
P(f"  Quy theo CPL CRM: giá trị chi phí đã bỏ ra mà không thu được lead = {fmt_vnd(370*cpl_crm)} - {fmt_vnd(480*cpl_crm)}đ")
P(f"  Cộng thêm 63 lead mất do GTM v23 (số ĐO ĐƯỢC): {fmt_vnd(63*cpl_crm)}đ theo CPL")

# ---------------------------------------------------------------- PHẦN A: định lượng lãng phí
P("\n"+"="*70); P("A. ĐỊNH LƯỢNG LÃNG PHÍ")
# A1 PMax
pm = B1["PMAX_VinhomesHM_Lead"]
P(f"  [PMax] chi {pm['cost']/M:.0f}tr ({pm['cost']/tot['Chi_phi']:.1%} tài khoản), lead {pm['Lead_CRM']:.0f}, SQL {pm['Lead_SQL']:.0f} "
  f"({pm['sqlrate']:.1%}), cọc {pm['Dat_Coc']:.0f}, doanh thu {pm['DoanhThu_HoaHong']:.0f} → ROAS 0")
P(f"         CP/chuyển đổi Ads = {fmt_vnd(pm['cpl_ads'])}đ (THẤP NHẤT tài khoản) nhưng CP/SQL = {fmt_vnd(pm['cpsql'])}đ (cao gấp {pm['cpsql']/B1['SEA_Brand_Vinhomes_HocMon']['cpsql']:.1f}× Brand)")
P(f"         Clarity: thoát <3s = 74,3%, thời lượng trung vị 3s, hao hụt nhấp→phiên 28,0% (sheet 10B/11B)")
P(f"         Sheet 08C: PMax trùng SĐT 31%, SĐT sai 24%, sai phân khúc 34%, lead dùng được CHỈ 7%")
P(f"         → Lãng phí = toàn bộ {fmt_vnd(pm['cost'])}đ (0 cọc). Thận trọng: giữ 7% lead dùng được → lãng phí ≥ {fmt_vnd(pm['cost']*0.93)}đ")
# A2 Competitor
cp = B1["SEA_Competitor_DoiThu"]
P(f"  [Competitor] chi {cp['cost']/M:.0f}tr, lead {cp['Lead_CRM']:.0f}, SQL {cp['Lead_SQL']:.0f}, cọc 0, CPC TB {fmt_vnd(div(cp['cost'],cp['Nhap_chuot']))}đ")
P(f"         → lãng phí 100% = {fmt_vnd(cp['cost'])}đ")
# A3 YouTube + GDN
yt = B1["YT_Video_TVC_MoBan"]; gdn = B1["GDN_Remarketing_Web30d"]
P(f"  [YouTube] chi {yt['cost']/M:.0f}tr, lead {yt['Lead_CRM']:.0f}, SQL {yt['Lead_SQL']:.0f}, cọc 0, CP/SQL {fmt_vnd(yt['cpsql'])}đ")
P(f"  [GDN RMK] chi {gdn['cost']/M:.0f}tr, lead {gdn['Lead_CRM']:.0f}, SQL {gdn['Lead_SQL']:.0f}, cọc 0, CP/SQL {fmt_vnd(gdn['cpsql'])}đ")
P(f"           GDN hao hụt nhấp→phiên 45,0%; YT 82,0% (sheet 10B)")
# A4 Địa lý
geo_bad = [("Hà Nội",155104182,20),("Đà Nẵng",86569776,7),("Cần Thơ & ĐBSCL",93783924,12),
           ("Đồng Nai",70337943,14),("Ngoài VN",28856592,7)]
gb_cost = sum(c for _,c,_ in geo_bad); gb_sql = sum(s for _,_,s in geo_bad)
P(f"  [Địa lý] 5 vùng ngoài tệp (HN/ĐN/Cần Thơ/Đồng Nai/ngoài VN): chi {fmt_vnd(gb_cost)}đ = {gb_cost/tot['Chi_phi']:.1%} ngân sách, "
  f"{gb_sql} SQL = {gb_sql/643:.1%} SQL, 0 cọc → CP/SQL {fmt_vnd(gb_cost/gb_sql)}đ")
core_geo = 1803537000 - gb_cost
P(f"         6 quận lõi TP.HCM (Q12/HócMôn/GòVấp/BìnhTân/CủChi/TânPhú) chi {fmt_vnd(201996144+176746626+155104182+111819294+86569776+102801609)}đ "
  f"→ {97+92+76+52+40+42} SQL, {4+3+3+2+1+1} cọc")
# A5 Search terms rác
st_junk_kw = ["vinhomes hóc môn tuyển dụng","vinschool hóc môn học phí","giá đất hóc môn 2026",
  "bản đồ quy hoạch hóc môn","thuê nhà nguyên căn hóc môn","nhà trọ hóc môn giá rẻ",
  "bán đất thổ cư hóc môn 100 triệu","cho thuê kho xưởng hóc môn","việc làm bất động sản hóc môn",
  "nhà đất hóc môn lừa đảo","chung cư mini gò vấp","vinhomes hóc môn có thật không"]
st = list(csv.DictReader(io.open(f"{SH}/04_SEARCH_TERMS.csv", encoding="utf-8-sig")))
st = [r for r in st if r.get("Chi phí (đ)")]
junk_cost = sum(float(r["Chi phí (đ)"]) for r in st if r["Cụm từ tìm kiếm"] in st_junk_kw)
junk_sql = sum(float(r["Lead chất lượng (SQL)"]) for r in st if r["Cụm từ tìm kiếm"] in st_junk_kw)
st_cost = sum(float(r["Chi phí (đ)"]) for r in st)
P(f"  [Search terms rác] {len(st_junk_kw)} cụm 0 hoặc gần 0 SQL: chi {fmt_vnd(junk_cost)}đ, SQL={junk_sql:.0f} "
  f"= {junk_cost/st_cost:.1%} chi phí bảng search terms ({fmt_vnd(st_cost)}đ)")
comp_st = sum(float(r["Chi phí (đ)"]) for r in st if r["Chiến dịch"]=="SEA_Competitor_DoiThu")
P(f"         + toàn bộ 6 cụm Competitor {fmt_vnd(comp_st)}đ, 0 SQL → tổng từ khóa cần chặn ≈ {fmt_vnd(junk_cost+comp_st)}đ")
# A6 Brand mất IS do ngân sách
P("  [Brand mất Impression Share do ngân sách]")
for g in phases:
    rs = [r for r in rows if r["Giai_doan"]==g and r["Chien_dich"]=="SEA_Brand_Vinhomes_HocMon"]
    a = agg(rs)
    isb = sum(r["Impr_Share"] for r in rs)/len(rs); mb = sum(r["Mat_IS_NganSach"] for r in rs)/len(rs)
    mr = sum(r["Mat_IS_ThuHang"] for r in rs)/len(rs)
    P(f"    {g}: IS TB={isb:.1%} mất do NS={mb:.1%} mất do thứ hạng={mr:.1%} | chi {a['Chi_phi']/M:.0f}tr cọc {a['Dat_Coc']:.0f} ROAS {div(a['DoanhThu_HoaHong'],a['Chi_phi']):.1f}")
br = B1["SEA_Brand_Vinhomes_HocMon"]
rs_b = [r for r in rows if r["Chien_dich"]=="SEA_Brand_Vinhomes_HocMon"]
mb_all = sum(r["Mat_IS_NganSach"] for r in rs_b)/len(rs_b)
is_all = sum(r["Impr_Share"] for r in rs_b)/len(rs_b)
lost_impr_ratio = mb_all/is_all if is_all else 0
P(f"    Toàn kỳ Brand: IS={is_all:.1%}, mất do NS={mb_all:.1%} → nếu lấp hết phần mất do NS, lưu lượng Brand tăng ~{lost_impr_ratio:.0%}")
P(f"    Brand hiện: {br['Lead_SQL']:.0f} SQL, {br['Dat_Coc']:.0f} cọc, DT {br['DoanhThu_HoaHong']/M:.0f}tr, ROAS {div(br['DoanhThu_HoaHong'],br['cost']):.2f}")
P(f"    [TRẦN LÝ THUYẾT, giả định tuyến tính - của tôi] lấp 100% phần mất do NS: DT +{br['DoanhThu_HoaHong']*lost_impr_ratio/M:.0f}tr, chi phí +{br['cost']*lost_impr_ratio/M:.0f}tr")
P(f"    [THẬN TRỌNG - của tôi, chỉ lấp 50% và giả định lưu lượng biên kém hơn 30%]: "
  f"DT +{br['DoanhThu_HoaHong']*lost_impr_ratio*0.5*0.7/M:.0f}tr, chi phí +{br['cost']*lost_impr_ratio*0.5/M:.0f}tr → lãi ròng +{(br['DoanhThu_HoaHong']*0.7-br['cost'])*lost_impr_ratio*0.5/M:.0f}tr")
P(f"    LƯU Ý: giả định tuyến tính là điểm yếu — lưu lượng biên luôn kém hơn. Cần chạy thử tăng NS Brand 2 tuần rồi đo lại mới kết luận được.")
# A7 landing page v1
P("  [Trang đích v1 - sheet 10C]")
v1_ses, v1_lead, v2_ses, v2_lead = 52410, 1002, 42938, 713
v1_fs, v2_fs = 4912, 2546
P(f"    v1 (N1-57): {v1_ses} phiên | form_start {v1_fs} ({v1_fs/v1_ses:.2%} phiên) | lead {v1_lead} | hoàn tất form {v1_lead/v1_fs:.1%} | lead/phiên {v1_lead/v1_ses:.2%} | LCP 4,8s | tương tác 34,2%")
P(f"    v2 (N58-90): {v2_ses} phiên | form_start {v2_fs} ({v2_fs/v2_ses:.2%} phiên) | lead {v2_lead} | hoàn tất form {v2_lead/v2_fs:.1%} | lead/phiên {v2_lead/v2_ses:.2%} | LCP 1,9s | tương tác 58,7%")
P(f"    ⇒ NGHỊCH LÝ: tỷ lệ hoàn tất form +{(v2_lead/v2_fs)/(v1_lead/v1_fs)-1:.0%} nhưng tỷ lệ BẮT ĐẦU form −{1-(v2_fs/v2_ses)/(v1_fs/v1_ses):.0%} "
  f"⇒ lead/phiên {(v2_lead/v2_ses)/(v1_lead/v1_ses)-1:+.0%}")
P(f"    Theo thiết bị (sheet 10C chi tiết): mobile v1 {661/41404:.2%} → v2 {507/34350:.2%} ({(507/34350)/(661/41404)-1:+.0%}); "
  f"desktop v1 {246/8910:.2%} → v2 {173/7301:.2%} ({(173/7301)/(246/8910)-1:+.0%}) ⇒ giảm ở MỌI thiết bị, không phải do đổi mix thiết bị")
P(f"    Nhưng mix NGUỒN thay đổi giữa 2 kỳ (GĐ3 YouTube tăng 11,6tr→71,6tr, hao hụt nhấp→phiên 82%) → KHÔNG ĐỦ DỮ LIỆU để kết luận nhân quả; cần A/B test đồng thời (sheet 05: hiện chạy 1 phiên bản, không thử nghiệm)")
P(f"    Giá trị đã thu được của v2 nếu chạy từ N1 (theo tỷ lệ HOÀN TẤT form, giữ nguyên form_start v1): "
  f"{v1_fs}×{v2_lead/v2_fs:.4f} = {v1_fs*v2_lead/v2_fs:.0f} lead thay vì {v1_lead} → +{v1_fs*v2_lead/v2_fs-v1_lead:.0f} lead")
extra = v1_fs*v2_lead/v2_fs - v1_lead
P(f"    → +{extra:.0f} lead × SQL {sqlrate:.1%} × SQL→Cọc {coc_per_sql:.2%} = {extra*sqlrate*coc_per_sql:.1f} cọc = {fmt_vnd(extra*sqlrate*coc_per_sql*HH)}đ (chi phí của 57 ngày chậm trễ)")
# A8 sale ops
P("  [Vận hành sale - sheet 08A/08B]")
b = list(csv.DictReader(io.open(f"{SH}/08_CRM_VAN_HANH.csv", encoding="utf-8-sig")))
slow = 588+536+664  # >30 phút
P(f"    Lead gọi lại >30 phút: 588+536+664 = {slow} = {slow/2554:.0%} tổng lead")
P(f"    Tỷ lệ đặt cọc: <5p 1,82% vs >12h 0,04% = chênh {0.0182/0.0004:.0f} lần")
actual_slow = 588*0.0058+536*0.0021+664*0.0004
P(f"    Cọc thực tế từ {slow} lead chậm = {actual_slow:.1f} cọc")
P(f"    [TRẦN LÝ THUYẾT - không khả thi] nếu 100% gọi <5 phút: {slow}×1,82% = {slow*0.0182:.1f} cọc → +{slow*0.0182-actual_slow:.1f} cọc = {fmt_vnd((slow*0.0182-actual_slow)*HH)}đ")
P(f"    [MỤC TIÊU KHẢ THI - của tôi, SLA 30 phút cho 70% lead chậm] {slow}×0,7 dời lên nhóm 5-30p (1,21%) + 30% giữ nguyên:")
feas = slow*0.7*0.0121 + slow*0.3*0.0058
P(f"        = {slow*0.7:.0f}×1,21% + {slow*0.3:.0f}×0,58% = {feas:.1f} cọc → +{feas-actual_slow:.1f} cọc = {fmt_vnd((feas-actual_slow)*HH)}đ")
missed = 118+96+61
P(f"    Lead bị bỏ sót hoàn toàn (không ai gọi): {missed} lead = {fmt_vnd(missed*cpl_crm)}đ chi phí bốc hơi")
P("  [Cuối tuần] T7+CN: chi phí {:.0f}tr, cọc {}, chỉ 2 sale trực (sheet 07C)".format((262814000+240996000)/M, 3+1))
wkd_cost = 262814000+240996000; wkd_coc = 4
wd_cost = 258137000+259227000+260849000+259406000+262108000; wd_coc = 7+1+1+2+3
P(f"    T7+CN: {fmt_vnd(wkd_cost)}đ / {wkd_coc} cọc = {fmt_vnd(wkd_cost/wkd_coc)}đ/cọc")
P(f"    T2-T6: {fmt_vnd(wd_cost)}đ / {wd_coc} cọc = {fmt_vnd(wd_cost/wd_coc)}đ/cọc")
P(f"    Thứ 2 riêng: 258tr/7 cọc = {fmt_vnd(258137000/7)}đ/cọc (tốt nhất tuần)")
# A9 khung giờ
P("  [Khung giờ - sheet 07A] 20:00-24:00: chi {} = {:.1%} ngân sách, 0-3 cọc, gọi lại <30p chỉ 21%/12%".format(
    fmt_vnd(337261419+72141480), (337261419+72141480)/1803537000))
P(f"    00:00-06:00: {fmt_vnd(73945017)}đ, 18 SQL, 0 cọc, CP/SQL {fmt_vnd(4108056)}đ")
P(f"    → 3 khung 20:00-06:00 tổng {fmt_vnd(337261419+72141480+73945017)}đ = {(337261419+72141480+73945017)/1803537000:.1%} ngân sách, 0 cọc từ 20h-6h ngoại trừ 3 cọc khung 20-23h")
# A10 thiết bị
P("  [Thiết bị - sheet 07B] Mobile 78,1% chi phí ({}), CVR 2,03%, CP/SQL {}đ".format(fmt_vnd(1408562397), fmt_vnd(3042251)))
P(f"    Desktop 16,7% chi phí, CVR 4,02% (gấp {0.0402/0.0203:.2f}×), CP/SQL {fmt_vnd(1847795)}đ (rẻ hơn {1-1847795/3042251:.0%})")
# A11 double page_view
P("  [GTM] thẻ GA4 Config trùng từ N31 (v22) → page_view đếm đôi; 34 thẻ/412KB JS làm chậm LCP ~0,8s")

# ---------------------------------------------------------------- C: ngân sách
P("\n"+"="*70); P("C. PHÂN BỔ NGÂN SÁCH 2,1 TỶ / 90 NGÀY")
alloc = {
 "GĐ1 (N1-30)": {"SEA_Brand": 180, "SEA_Generic_Core": 210, "SEA_Generic_Longtail": 0,
                 "PMAX_Feed_BrandExcl": 60, "GDN_RMK": 30, "YT": 0, "Discovery/Demand": 0},
 "GĐ2 (N31-60)": {"SEA_Brand": 210, "SEA_Generic_Core": 260, "SEA_Generic_Longtail": 60,
                 "PMAX_Feed_BrandExcl": 90, "GDN_RMK": 40, "YT": 0, "Discovery/Demand": 40},
 "GĐ3 (N61-90)": {"SEA_Brand": 260, "SEA_Generic_Core": 310, "SEA_Generic_Longtail": 90,
                 "PMAX_Feed_BrandExcl": 110, "GDN_RMK": 50, "YT": 40, "Discovery/Demand": 60},
}
tot_alloc = 0
keys = list(alloc["GĐ1 (N1-30)"].keys())
P(f"{'Chiến dịch':26s} " + " ".join(f"{g:>14s}" for g in alloc) + f" {'Tổng(tr)':>10s} {'%':>6s}")
sums = {}
for k in keys:
    s = sum(alloc[g][k] for g in alloc); sums[k] = s; tot_alloc += s
    P(f"{k:26s} " + " ".join(f"{alloc[g][k]:14d}" for g in alloc) + f" {s:10d} {s/2100:6.1%}")
P(f"{'TỔNG (triệu đ)':26s} " + " ".join(f"{sum(alloc[g].values()):14d}" for g in alloc) + f" {tot_alloc:10d}")
assert tot_alloc == 2100, tot_alloc
P(f"  KIỂM TRA: tổng = {tot_alloc} triệu = {fmt_vnd(tot_alloc*M)}đ = ĐÚNG 2,1 tỷ ✔")
for g in alloc:
    P(f"  {g}: {sum(alloc[g].values())}tr = {sum(alloc[g].values())/30:.1f} tr/ngày")
# so sánh phân bổ cũ
P("  So sánh phân bổ CŨ (90 ngày qua) vs MỚI:")
old_map = {"SEA_Brand_Vinhomes_HocMon":"Brand","SEA_Generic_NhaPho_CanHo_TayBac":"Generic",
           "SEA_Competitor_DoiThu":"Competitor","PMAX_VinhomesHM_Lead":"PMax",
           "GDN_Remarketing_Web30d":"GDN","YT_Video_TVC_MoBan":"YouTube"}
for c in camps:
    P(f"    {old_map[c]:11s} cũ {B1[c]['cost']/M:7.0f}tr ({B1[c]['cost']/tot['Chi_phi']:5.1%})")
P(f"    MỚI: Brand {sums['SEA_Brand']}tr ({sums['SEA_Brand']/2100:.1%}), Generic {sums['SEA_Generic_Core']+sums['SEA_Generic_Longtail']}tr "
  f"({(sums['SEA_Generic_Core']+sums['SEA_Generic_Longtail'])/2100:.1%}), PMax {sums['PMAX_Feed_BrandExcl']}tr, Competitor 0tr")

# mục tiêu từng GĐ
P("  Mục tiêu định lượng từng giai đoạn (dựa tỷ lệ GĐ3 đã đo + cải thiện đo lường):")
sq3 = div(g3['Dat_Coc'], g3['Lead_SQL']); ls3 = div(g3['Lead_SQL'], g3['Lead_CRM'])
P(f"    Cơ sở: GĐ3 Lead→SQL={ls3:.1%}, SQL→Cọc={sq3:.1%}, CP/SQL GĐ3={div(g3['Chi_phi'],g3['Lead_SQL'])/M:.2f}tr")
targets = {"GĐ1 (N1-30)": (2.60, 6), "GĐ2 (N31-60)": (2.20, 11), "GĐ3 (N61-90)": (1.90, 18)}
tot_sql = tot_coc = 0
for g,(cps_t, coc_t) in targets.items():
    bud = sum(alloc[g].values())*M
    sql_t = bud/(cps_t*M)
    tot_sql += sql_t; tot_coc += coc_t
    P(f"    {g}: NS {bud/M:.0f}tr, CP/SQL mục tiêu {cps_t}tr → {sql_t:.0f} SQL, lead thô {sql_t/0.32:.0f}, cọc mục tiêu {coc_t}, "
      f"cọc/SQL cần {coc_t/sql_t:.2%}")
P(f"    TỔNG: {tot_sql:.0f} SQL, {tot_coc} cọc, doanh thu {tot_coc*HH/M:.0f}tr → ROAS {tot_coc*HH/BUDGET:.2f}x, "
  f"CP/SQL bình quân {BUDGET/tot_sql/M:.2f}tr")
P(f"    Lead thô cần/ngày = {tot_sql/0.32/90:.1f} (năng lực sale 96/ngày → dư địa)")

# ---------------------------------------------------------------- D3 PMax
P("\n"+"="*70); P("D3. PMax — CP/chuyển đổi thấp nhất nhưng...")
P(f"{'Chiến dịch':34s} {'CP/CĐ Ads':>12s} {'CP/SQL':>12s} {'CP/cọc':>13s} {'ROAS':>6s} {'lead dùng được':>15s}")
usable = {"SEA_Brand_Vinhomes_HocMon":0.67,"SEA_Generic_NhaPho_CanHo_TayBac":0.46,
          "SEA_Competitor_DoiThu":0.26,"PMAX_VinhomesHM_Lead":0.07,
          "GDN_Remarketing_Web30d":0.38,"YT_Video_TVC_MoBan":0.25}
for c in camps:
    d = B1[c]
    P(f"{c:34s} {d['cpl_ads']/M:12.3f} {d['cpsql']/M:12.2f} "
      f"{(d['cpcoc']/M if d['cpcoc'] else 0):13.1f} {div(d['DoanhThu_HoaHong'],d['cost']):6.2f} {usable[c]:15.0%}")
P(f"  PMax CP/CĐ Ads rẻ nhất ({fmt_vnd(pm['cpl_ads'])}đ) NHƯNG:")
P(f"   - trong {pm['ChuyenDoi_Ads']:.0f} 'chuyển đổi' PMax, GA4 (sheet 10B) cho: generate_lead 510, click_to_call lượt 568 "
  f"(người 299), view_price 438, engaged_30s 259 ⇒ 510+568+438+259 = {510+568+438+259} ≈ {pm['ChuyenDoi_Ads']:.0f} (lệch {pm['ChuyenDoi_Ads']-1775:.0f} do làm tròn phân bổ)")
P(f"   - lead thật PMax = 510 + 299 = 809 (không phải {pm['ChuyenDoi_Ads']:.0f}) → CP/lead thật = {fmt_vnd(pm['cost']/809)}đ")
P(f"   - CRM chỉ nhận {pm['Lead_CRM']:.0f} lead → CP/lead CRM = {fmt_vnd(pm['cpl_crm'])}đ")
P(f"   - SQL {pm['Lead_SQL']:.0f} → CP/SQL {fmt_vnd(pm['cpsql'])}đ vs Brand {fmt_vnd(br['cpsql'])}đ = đắt hơn {pm['cpsql']/br['cpsql']:.1f}×")
P(f"   - CỌC = 0 / DOANH THU = 0 → ROAS 0. Dồn 100% NS vào PMax = 0 doanh thu.")
P(f"  Nếu dồn cả 2,1 tỷ vào PMax theo tỷ lệ SQL hiện tại: {BUDGET/pm['cpsql']:.0f} SQL × 0% cọc = 0 cọc")

# ---------------------------------------------------------------- D1 Brand
P("\n"+"="*70); P("D1. Cắt Brand?")
P(f"  Brand: chi {br['cost']/M:.0f}tr ({br['cost']/tot['Chi_phi']:.1%} NS) → {br['Dat_Coc']:.0f}/{tot['Dat_Coc']:.0f} cọc "
  f"({br['Dat_Coc']/tot['Dat_Coc']:.0%}), DT {br['DoanhThu_HoaHong']/M:.0f}tr/{tot['DoanhThu_HoaHong']/M:.0f}tr "
  f"({br['DoanhThu_HoaHong']/tot['DoanhThu_HoaHong']:.0%}), ROAS {div(br['DoanhThu_HoaHong'],br['cost']):.2f}x")
ge = B1["SEA_Generic_NhaPho_CanHo_TayBac"]
P(f"  Generic: chi {ge['cost']/M:.0f}tr ({ge['cost']/tot['Chi_phi']:.1%}) → {ge['Dat_Coc']:.0f} cọc, DT {ge['DoanhThu_HoaHong']/M:.0f}tr, ROAS {div(ge['DoanhThu_HoaHong'],ge['cost']):.2f}x")
P(f"  CP/cọc: Brand {fmt_vnd(br['cpcoc'])}đ vs Generic {fmt_vnd(ge['cpcoc'])}đ → Brand rẻ hơn {1-br['cpcoc']/ge['cpcoc']:.0%}")
P(f"  CP/SQL: Brand {fmt_vnd(br['cpsql'])}đ vs Generic {fmt_vnd(ge['cpsql'])}đ")
P(f"  Nếu chuyển 260tr Brand sang Generic theo CP/cọc Generic: {260*M/ge['cpcoc']:.1f} cọc thay vì {br['Dat_Coc']:.0f} cọc → mất {br['Dat_Coc']-260*M/ge['cpcoc']:.1f} cọc "
  f"= {fmt_vnd((br['Dat_Coc']-260*M/ge['cpcoc'])*HH)}đ")
P(f"  Brand IS chỉ {is_all:.1%} + mất do NS {mb_all:.1%} → chưa phủ hết cầu sẵn có (sheet 09: IS brand <60% = báo động)")
P(f"  GA4 mục D: Brand nhấp-cuối 592 lead nhưng data-driven 401 (−32,3%) → Brand vừa là kênh CHỐT vừa được hỗ trợ; "
  f"nhưng 401 vẫn là kênh #2/6 → không phải 'chỉ ăn theo'")
P(f"  Search terms: 'vinhomes hóc môn' 78tr chi → 138 SQL, CP/SQL {fmt_vnd(565695)}đ = rẻ nhất tài khoản")

# ---------------------------------------------------------------- D4 cắt còn 1,2 tỷ
P("\n"+"="*70); P("D4. Ngân sách 1,2 tỷ")
cut = {"SEA_Brand": 400, "SEA_Generic_Core": 520, "SEA_Generic_Longtail": 60,
       "PMAX_Feed_BrandExcl": 120, "GDN_RMK": 60, "YT": 0, "Discovery/Demand": 40}
P(f"  Tổng = {sum(cut.values())}tr"); assert sum(cut.values()) == 1200
for k,v in cut.items(): P(f"    {k:26s} {v:5d}tr ({v/1200:5.1%})  [kế hoạch 2,1 tỷ: {sums[k]}tr]")
P(f"  Cắt theo thứ tự: YouTube ({sums['YT']}tr→0), Discovery ({sums['Discovery/Demand']}→40), "
  f"GDN ({sums['GDN_RMK']}→60), PMax ({sums['PMAX_Feed_BrandExcl']}→120), Generic longtail ({sums['SEA_Generic_Longtail']}→60)")
P(f"  Với 1,2 tỷ @ CP/SQL 2,2tr = {1200*M/2_200_000:.0f} SQL × SQL→Cọc GĐ3 {sq3:.1%} = {1200*M/2_200_000*sq3:.1f} cọc")
P(f"     → DT {1200*M/2_200_000*sq3*HH/M:.0f}tr, ROAS {1200*M/2_200_000*sq3*HH/(1200*M):.2f}x")
P(f"  Cam kết lại với BGĐ: {round(1200*M/2_200_000*sq3)} cọc chứ không phải 32")

# ---------------------------------------------------------------- D6 / E hỗ trợ
P("\n"+"="*70); P("D6/E. Giá trị của việc sửa đo lường (quy tiền)")
P(f"  1) Loại view_price+engaged khỏi cột chuyển đổi: {junk} tín hiệu rác/{ads_conv} = {junk/ads_conv:.1%} "
  f"→ máy học PMax/Smart Bidding đang tối ưu theo tín hiệu này. PMax chi {pm['cost']/M:.0f}tr = tiền đang bị lái sai.")
P(f"  2) GCLID vào CRM + offline conversion import: cho phép tối ưu theo SQL/cọc. "
  f"Hiện SQL/Lead toàn tài khoản {sqlrate:.1%}, PMax {pm['sqlrate']:.1%} → khoảng cách này chính là thứ ECL sửa được.")
P(f"  3) Cảnh báo chuyển đổi=0: sự cố N44-46 mất {lost_days['Lead_CRM']:.0f} lead khỏi hệ thống Ads, "
  f"chi phí 3 ngày {lost_days['Chi_phi']/M:.0f}tr chạy mù")
P(f"  4) Sửa lỗi JS #4/#5/#6: {370}-{480} lead ≈ {370*sqlrate*coc_per_sql*HH/M:.0f}-{480*sqlrate*coc_per_sql*HH/M:.0f}tr doanh thu")
P(f"  5) Khử trùng click_to_call: {dup} chuyển đổi ảo = {dup/ads_conv:.1%}")

# ---------------------------------------------------------------- tuần / xu hướng
P("\n"+"="*70); P("PHỤ LỤC: xu hướng theo tuần (toàn tài khoản)")
P(f"{'Tuần':>5s} {'Chi phí(tr)':>11s} {'CĐ Ads':>7s} {'Lead':>6s} {'SQL':>5s} {'Cọc':>4s} {'CP/SQL(tr)':>11s}")
for w in sorted(set(int(r["Tuan"]) for r in rows)):
    a = agg([r for r in rows if int(r["Tuan"]) == w])
    P(f"{w:5d} {a['Chi_phi']/M:11.1f} {a['ChuyenDoi_Ads']:7.0f} {a['Lead_CRM']:6.0f} {a['Lead_SQL']:5.0f} "
      f"{a['Dat_Coc']:4.0f} {div(a['Chi_phi'],a['Lead_SQL'])/M:11.2f}")

P("\nHoàn tất. Mọi số trong agent-6.md truy được về output này.")

with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "agent-6-calc-output.txt"), "w", encoding="utf-8") as f:
    f.write("\n".join(out))
