#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Bài thi Performance Marketing Lead - thí sinh 4. Mọi số trong agent-4.md sinh từ file này.
Nguồn: /home/docdang/Downloads/du_lieu_google_ads_90_ngay_1.csv (= sheet 02_DU_LIEU_NGAY)
      + các sheet CSV trong ../sheets/
Chạy: python3 agent-4-calc.py
"""
import csv, os, sys
from collections import defaultdict

CSV = "/home/docdang/Downloads/du_lieu_google_ads_90_ngay_1.csv"
SH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "sheets")

def load():
    with open(CSV, encoding="utf-8-sig") as f:
        return list(csv.DictReader(f))

rows = load()
NUM = ["Hien_thi","Nhap_chuot","Chi_phi","ChuyenDoi_Ads","Lead_CRM","Lead_SQL",
       "Di_Xem_Nha","Booking","Dat_Coc","DoanhThu_HoaHong"]
FL = ["Impr_Share","Mat_IS_NganSach","Mat_IS_ThuHang"]
for r in rows:
    for k in NUM: r[k] = float(r[k])
    for k in FL: r[k] = float(r[k]) if r[k] not in ("", None) else 0.0

def agg(rs):
    d = {k: sum(r[k] for r in rs) for k in NUM}
    d["n"] = len(rs)
    return d

def div(a, b): return a / b if b else float("nan")

def money(x):
    return f"{x:,.0f}".replace(",", ".")

out = []
def P(*a):
    s = " ".join(str(x) for x in a)
    out.append(s); print(s)

P("=" * 78); P("B0. KIỂM TRA DỮ LIỆU")
P("Số dòng:", len(rows), "| Ngày:", min(r["Ngay"] for r in rows), "->", max(r["Ngay"] for r in rows))
camps = sorted({r["Chien_dich"] for r in rows})
P("Chiến dịch:", len(camps), camps)
T = agg(rows)
P("TỔNG: chi phí", money(T["Chi_phi"]), "| clicks", int(T["Nhap_chuot"]),
  "| CĐ_Ads", int(T["ChuyenDoi_Ads"]), "| Lead_CRM", int(T["Lead_CRM"]),
  "| SQL", int(T["Lead_SQL"]), "| Đi xem", int(T["Di_Xem_Nha"]),
  "| Booking", int(T["Booking"]), "| Cọc", int(T["Dat_Coc"]),
  "| DT", money(T["DoanhThu_HoaHong"]))

# ---------------- B1 ----------------
P(""); P("=" * 78); P("B1. CPL / CP-SQL / CP-CỌC THEO CHIẾN DỊCH (toàn kỳ)")
P(f"{'Chiến dịch':<34}{'Chi phí':>16}{'CPL_Ads':>12}{'CPL_CRM':>12}{'CP/SQL':>14}{'CP/cọc':>16}")
for c in camps + ["TOÀN KỲ"]:
    rs = rows if c == "TOÀN KỲ" else [r for r in rows if r["Chien_dich"] == c]
    a = agg(rs)
    P(f"{c:<34}{money(a['Chi_phi']):>16}{money(div(a['Chi_phi'],a['ChuyenDoi_Ads'])):>12}"
      f"{money(div(a['Chi_phi'],a['Lead_CRM'])):>12}{money(div(a['Chi_phi'],a['Lead_SQL'])):>14}"
      f"{(money(div(a['Chi_phi'],a['Dat_Coc'])) if a['Dat_Coc'] else 'n/a — 0 cọc'):>16}")

P(""); P("Chi tiết thêm: CTR, CPC, SQL/Lead, ROAS theo chiến dịch")
P(f"{'Chiến dịch':<34}{'CTR':>8}{'CPC':>12}{'SQL/Lead':>10}{'Cọc':>6}{'Doanh thu':>16}{'ROAS':>8}{'%chi phí':>10}")
for c in camps + ["TOÀN KỲ"]:
    rs = rows if c == "TOÀN KỲ" else [r for r in rows if r["Chien_dich"] == c]
    a = agg(rs)
    P(f"{c:<34}{div(a['Nhap_chuot'],a['Hien_thi'])*100:>7.2f}%{money(div(a['Chi_phi'],a['Nhap_chuot'])):>12}"
      f"{div(a['Lead_SQL'],a['Lead_CRM'])*100:>9.1f}%{int(a['Dat_Coc']):>6}"
      f"{money(a['DoanhThu_HoaHong']):>16}{div(a['DoanhThu_HoaHong'],a['Chi_phi']):>8.2f}"
      f"{div(a['Chi_phi'],T['Chi_phi'])*100:>9.1f}%")

# ---------------- B2 ----------------
P(""); P("=" * 78); P("B2. ROAS TOÀN KỲ & THEO GIAI ĐOẠN")
for g in ["GĐ1", "GĐ2", "GĐ3", "ALL"]:
    rs = rows if g == "ALL" else [r for r in rows if r["Giai_doan"] == g]
    a = agg(rs)
    P(f"{g:<5} chi phí {money(a['Chi_phi']):>16} | DT {money(a['DoanhThu_HoaHong']):>16} "
      f"| cọc {int(a['Dat_Coc']):>3} | ROAS {div(a['DoanhThu_HoaHong'],a['Chi_phi']):.3f}x "
      f"| CP/cọc {money(div(a['Chi_phi'],a['Dat_Coc'])) if a['Dat_Coc'] else 'n/a'}")
P("ROAS theo chiến dịch × giai đoạn (chỉ CD có doanh thu):")
for c in camps:
    for g in ["GĐ1", "GĐ2", "GĐ3"]:
        rs = [r for r in rows if r["Chien_dich"] == c and r["Giai_doan"] == g]
        a = agg(rs)
        if a["DoanhThu_HoaHong"]:
            P(f"  {c:<34}{g}  ROAS {div(a['DoanhThu_HoaHong'],a['Chi_phi']):>6.2f}x  cọc {int(a['Dat_Coc'])}")

# ---------------- B3 ----------------
P(""); P("=" * 78); P("B3. TỶ LỆ CHUYỂN ĐỔI TỪNG BƯỚC PHỄU (toàn kỳ)")
steps = [("Lead_CRM->SQL","Lead_CRM","Lead_SQL"),("SQL->Đi xem","Lead_SQL","Di_Xem_Nha"),
         ("Đi xem->Booking","Di_Xem_Nha","Booking"),("Booking->Cọc","Booking","Dat_Coc")]
for name, a_, b_ in steps:
    P(f"  {name:<18}{int(T[a_]):>6} -> {int(T[b_]):>5}  = {div(T[b_],T[a_])*100:6.2f}%")
P(f"  Lead_CRM -> Cọc     {int(T['Lead_CRM'])} -> {int(T['Dat_Coc'])}  = {div(T['Dat_Coc'],T['Lead_CRM'])*100:.3f}%")
P(f"  SQL -> Cọc          {int(T['Lead_SQL'])} -> {int(T['Dat_Coc'])}  = {div(T['Dat_Coc'],T['Lead_SQL'])*100:.3f}%")
P(f"  Đi xem -> Cọc       {int(T['Di_Xem_Nha'])} -> {int(T['Dat_Coc'])}  = {div(T['Dat_Coc'],T['Di_Xem_Nha'])*100:.2f}%")
P("Phễu theo giai đoạn:")
for g in ["GĐ1","GĐ2","GĐ3"]:
    a = agg([r for r in rows if r["Giai_doan"] == g])
    P(f"  {g}: Lead {int(a['Lead_CRM']):>4} SQL {int(a['Lead_SQL']):>4} ({div(a['Lead_SQL'],a['Lead_CRM'])*100:.1f}%) "
      f"Xem {int(a['Di_Xem_Nha']):>3} ({div(a['Di_Xem_Nha'],a['Lead_SQL'])*100:.1f}%) "
      f"Book {int(a['Booking']):>3} ({div(a['Booking'],a['Di_Xem_Nha'])*100:.1f}%) "
      f"Cọc {int(a['Dat_Coc']):>3} ({div(a['Dat_Coc'],a['Booking'])*100:.1f}%)")

# ---------------- B4 / B5 ----------------
P(""); P("=" * 78); P("B4/B5. NGƯỢC TỪ KPI: 32 CỌC / 2,1 TỶ")
BUDGET, TARGET_COC, HH, ROAS_T = 2_100_000_000, 32, 181_000_000, 3.0
P(f"Doanh thu dự kiến 32 cọc x 181tr = {money(TARGET_COC*HH)} -> ROAS trên 2,1 tỷ = "
  f"{div(TARGET_COC*HH,BUDGET):.2f}x (KPI ROAS>=3,0 {'ĐẠT' if div(TARGET_COC*HH,BUDGET)>=3 else 'KHÔNG ĐẠT'})")
P(f"B5. Chi phí QC tối đa / cọc để ROAS=3,0x: {money(HH/ROAS_T)}")
P(f"    Với 2,1 tỷ và trần đó -> số cọc tối thiểu = {BUDGET/(HH/ROAS_T):.1f} -> làm tròn lên {int(-(-BUDGET//(HH/ROAS_T)))} cọc")

# 3 kịch bản tỷ lệ
gd3 = agg([r for r in rows if r["Giai_doan"] == "GĐ3"])
scen = {
 "A_lichsu_toanky": (div(T["Lead_SQL"],T["Lead_CRM"]), div(T["Di_Xem_Nha"],T["Lead_SQL"]),
                     div(T["Booking"],T["Di_Xem_Nha"]), div(T["Dat_Coc"],T["Booking"])),
 "B_GD3_tot_nhat":  (div(gd3["Lead_SQL"],gd3["Lead_CRM"]), div(gd3["Di_Xem_Nha"],gd3["Lead_SQL"]),
                     div(gd3["Booking"],gd3["Di_Xem_Nha"]), div(gd3["Dat_Coc"],gd3["Booking"])),
 "C_ke_hoach":      (0.35, 0.35, 0.30, 0.35),
}
P("")
P(f"{'Kịch bản':<18}{'SQL/Lead':>10}{'Xem/SQL':>10}{'Book/Xem':>10}{'Cọc/Book':>10}"
  f"{'SQL cần':>10}{'Lead cần':>10}{'CP/SQL trần':>16}{'CPL trần':>14}")
for name,(s1,s2,s3,s4) in scen.items():
    book = TARGET_COC/s4; xem = book/s3; sql = xem/s2; lead = sql/s1
    P(f"{name:<18}{s1*100:>9.1f}%{s2*100:>9.1f}%{s3*100:>9.1f}%{s4*100:>9.1f}%"
      f"{sql:>10.0f}{lead:>10.0f}{money(BUDGET/sql):>16}{money(BUDGET/lead):>14}")
P(f"KPI ban giám đốc: CP/SQL <= 2.200.000đ -> với 2,1 tỷ mua được tối thiểu "
  f"{BUDGET/2_200_000:.0f} SQL")
P(f"Thực tế 90 ngày qua: CP/SQL = {money(div(T['Chi_phi'],T['Lead_SQL']))} "
  f"(gấp {div(T['Chi_phi'],T['Lead_SQL'])/2_200_000:.2f} lần trần KPI)")

# ---------------- B6 ----------------
P(""); P("=" * 78); P("B6. ĐỐI CHIẾU 3 NGUỒN (sheet 10_GA4 mục A + 12_GTM mục B)")
ads_conv = 3820; gl = 1715; ctc_all = 1132; ctc_uni = 779; vpp = 612; e30 = 361
P(f"  generate_lead {gl} + click_to_call(lượt) {ctc_all} + view_price_page {vpp} + engaged_30s {e30}"
  f" = {gl+ctc_all+vpp+e30} (khớp cột Chuyển đổi Ads = {ads_conv}: {gl+ctc_all+vpp+e30==ads_conv})")
dup = ctc_all - ctc_uni; rac = vpp + e30
P(f"  (1) Đếm trùng lượt gọi          = {ctc_all} - {ctc_uni} = {dup}  ({dup/ads_conv*100:.1f}% tổng CĐ)")
P(f"  (2) Sự kiện rác (không phải lead)= {vpp} + {e30} = {rac}  ({rac/ads_conv*100:.1f}%)")
P(f"  => Lead thật đo được bằng thẻ   = {ads_conv} - {dup} - {rac} = {ads_conv-dup-rac}")
mat_the = 2557 - (ads_conv-dup-rac)
P(f"  (3) Mất thẻ N44-46 (GTM v23)    = CRM 2557 - GA4 {ads_conv-dup-rac} = {mat_the} lead")
P(f"  KIỂM TRA: {ads_conv} - {dup} - {rac} + {mat_the} = {ads_conv-dup-rac+mat_the} = CRM 2557 "
  f"-> {ads_conv-dup-rac+mat_the==2557}")
P(f"  Khoảng chênh gộp Ads-CRM = {ads_conv-2557}; phân rã: -{dup} (trùng) -{rac} (rác) +{mat_the} (mất thẻ) "
  f"= {-dup-rac+mat_the}")
P(f"  Tỷ lệ thổi phồng: {ads_conv/2557:.2f}x (ngưỡng báo động 09_BENCHMARK: >1,8x)")

# Kiểm chứng N44-46 trong sheet 02
P("")
P("  Kiểm chứng trên dữ liệu ngày (sheet 02) — các ngày ChuyenDoi_Ads=0 nhưng Lead_CRM>0:")
byday = defaultdict(lambda: defaultdict(float))
for r in rows:
    byday[int(r["Ngay_thu"])]["ads"] += r["ChuyenDoi_Ads"]
    byday[int(r["Ngay_thu"])]["crm"] += r["Lead_CRM"]
    byday[int(r["Ngay_thu"])]["date"] = r["Ngay"]
tot0 = 0
for d in sorted(byday):
    if byday[d]["ads"] == 0 and byday[d]["crm"] > 0:
        P(f"    Ngày thứ {d} ({[r['Ngay'] for r in rows if int(r['Ngay_thu'])==d][0]}): "
          f"CĐ_Ads=0, Lead_CRM={int(byday[d]['crm'])}")
        tot0 += byday[d]["crm"]
P(f"    Tổng lead 3 ngày mất thẻ = {int(tot0)} (khớp 63 nêu ở sheet 10_GA4: {int(tot0)==63})")

# ---------------- B7 ----------------
P(""); P("=" * 78); P("B7. LEAD MẤT DO LỖI KỸ THUẬT CHƯA SỬA (sheet 11_CLARITY mục C)")
fixes = [("#4 JS TypeError e.setDate (Safari iOS) – form không gửi", 4196, 280, 340),
         ("#5 Nút CTA bị khung chat che (<380px)", 2741, 60, 90),
         ("#6 tel: link không phản hồi trên desktop", 1204, 30, 50)]
lo = sum(f[2] for f in fixes); hi = sum(f[3] for f in fixes)
cpl_crm = div(T["Chi_phi"], T["Lead_CRM"])
cp_sql = div(T["Chi_phi"], T["Lead_SQL"])
sql_rate = div(T["Lead_SQL"], T["Lead_CRM"])
P(f"{'Lỗi':<52}{'Phiên':>8}{'Lead mất':>12}")
for n, s, a, b in fixes: P(f"{n:<52}{s:>8}{f'{a}–{b}':>12}")
P(f"{'TỔNG (đo bởi Clarity: số phiên; ước tính UX: lead)':<52}{sum(f[1] for f in fixes):>8}{f'{lo}–{hi}':>12}")
P(f"  CPL_CRM thực tế toàn kỳ = {money(cpl_crm)}  -> giá trị lead mất = "
  f"{money(lo*cpl_crm)} – {money(hi*cpl_crm)}")
P(f"  Quy ra SQL (theo tỷ lệ SQL/Lead thực tế {sql_rate*100:.1f}%): {lo*sql_rate:.0f}–{hi*sql_rate:.0f} SQL")
coc_per_sql = div(T["Dat_Coc"], T["Lead_SQL"])
P(f"  Quy ra cọc (SQL->cọc {coc_per_sql*100:.2f}%): {lo*sql_rate*coc_per_sql:.1f}–{hi*sql_rate*coc_per_sql:.1f} cọc "
  f"-> doanh thu bỏ lỡ {money(lo*sql_rate*coc_per_sql*HH)} – {money(hi*sql_rate*coc_per_sql*HH)}")

# ---------------- PHẦN A: các con số chẩn đoán ----------------
P(""); P("=" * 78); P("PHẦN A — SỐ LIỆU CHẨN ĐOÁN")

pmax = agg([r for r in rows if r["Chien_dich"] == "PMAX_VinhomesHM_Lead"])
comp = agg([r for r in rows if r["Chien_dich"] == "SEA_Competitor_DoiThu"])
yt   = agg([r for r in rows if r["Chien_dich"] == "YT_Video_TVC_MoBan"])
gdn  = agg([r for r in rows if r["Chien_dich"] == "GDN_Remarketing_Web30d"])
brand= agg([r for r in rows if r["Chien_dich"] == "SEA_Brand_Vinhomes_HocMon"])
gen  = agg([r for r in rows if r["Chien_dich"] == "SEA_Generic_NhaPho_CanHo_TayBac"])

P(f"A1 Chi phí 0 cọc: PMax {money(pmax['Chi_phi'])} + Competitor {money(comp['Chi_phi'])} + "
  f"GDN {money(gdn['Chi_phi'])} + YT {money(yt['Chi_phi'])} = "
  f"{money(pmax['Chi_phi']+comp['Chi_phi']+gdn['Chi_phi']+yt['Chi_phi'])} "
  f"({(pmax['Chi_phi']+comp['Chi_phi']+gdn['Chi_phi']+yt['Chi_phi'])/T['Chi_phi']*100:.1f}% ngân sách, 0 doanh thu)")
P(f"A2 PMax: SQL/Lead {div(pmax['Lead_SQL'],pmax['Lead_CRM'])*100:.1f}% (benchmark báo động <12%), "
  f"CP/SQL {money(div(pmax['Chi_phi'],pmax['Lead_SQL']))}, CĐ_Ads/Lead_CRM {div(pmax['ChuyenDoi_Ads'],pmax['Lead_CRM']):.2f}x")
P(f"A3 Competitor: {money(comp['Chi_phi'])} / {int(comp['Lead_SQL'])} SQL / {int(comp['Dat_Coc'])} cọc; "
  f"CPC {money(div(comp['Chi_phi'],comp['Nhap_chuot']))} (benchmark báo động >60k)")
P(f"A4 Brand: ROAS {div(brand['DoanhThu_HoaHong'],brand['Chi_phi']):.2f}x, chỉ chiếm "
  f"{brand['Chi_phi']/T['Chi_phi']*100:.1f}% ngân sách nhưng đem "
  f"{brand['DoanhThu_HoaHong']/T['DoanhThu_HoaHong']*100:.1f}% doanh thu; "
  f"{int(brand['Dat_Coc'])}/{int(T['Dat_Coc'])} cọc")

# Impression share brand — weighted by impressions
def wis(rs, col):
    tot = sum(r["Hien_thi"] for r in rs)
    return sum(r[col]*r["Hien_thi"] for r in rs)/tot if tot else float("nan")
brs = [r for r in rows if r["Chien_dich"] == "SEA_Brand_Vinhomes_HocMon"]
P(f"A5 Brand IS (bình quân gia quyền theo hiển thị): {wis(brs,'Impr_Share')*100:.1f}% "
  f"| mất IS do ngân sách {wis(brs,'Mat_IS_NganSach')*100:.1f}% | do thứ hạng {wis(brs,'Mat_IS_ThuHang')*100:.1f}% "
  f"(benchmark: IS brand tốt >85%, mất IS ngân sách báo động >20%)")
for g in ["GĐ1","GĐ2","GĐ3"]:
    s = [r for r in brs if r["Giai_doan"] == g]
    P(f"    {g}: IS {wis(s,'Impr_Share')*100:.1f}% | mất NS {wis(s,'Mat_IS_NganSach')*100:.1f}% "
      f"| mất TH {wis(s,'Mat_IS_ThuHang')*100:.1f}% | chi phí {money(agg(s)['Chi_phi'])}")

# Ước lượng cơ hội brand bị mất do ngân sách
b_lost = wis(brs, "Mat_IS_NganSach")
b_is = wis(brs, "Impr_Share")
extra_click = brand["Nhap_chuot"] * (b_lost / b_is) if b_is else 0
extra_coc = extra_click * div(brand["Dat_Coc"], brand["Nhap_chuot"])
P(f"A5b Ngoại suy: nếu bù hết mất-IS-ngân sách của Brand -> +{extra_click:.0f} click "
  f"-> +{extra_coc:.1f} cọc -> ~{money(extra_coc*HH)} doanh thu bỏ lỡ "
  f"(chi phí thêm ~{money(extra_click*div(brand['Chi_phi'],brand['Nhap_chuot']))})")

# Search terms rác
P("")
st = list(csv.DictReader(open(os.path.join(SH, "04_SEARCH_TERMS.csv"), encoding="utf-8-sig")))
st = [r for r in st if r.get("Chi phí (đ)") and r["Chi phí (đ)"].replace(".","").isdigit()]
zero = [r for r in st if float(r["Lead chất lượng (SQL)"]) == 0]
P(f"A6 Search terms 0 SQL: {len(zero)}/{len(st)} cụm từ, chi phí "
  f"{money(sum(float(r['Chi phí (đ)']) for r in zero))} "
  f"({sum(float(r['Chi phí (đ)']) for r in zero)/sum(float(r['Chi phí (đ)']) for r in st)*100:.1f}% chi phí ST được liệt kê)")
irrel = ["tuyển dụng","học phí","thuê","nhà trọ","kho xưởng","việc làm","lừa đảo","chung cư mini",
         "quy hoạch","giá đất","bán đất thổ cư"]
bad = [r for r in st if any(k in r["Cụm từ tìm kiếm"] for k in irrel)]
P(f"    Trong đó cụm từ SAI Ý ĐỊNH rõ ràng ({len(bad)} cụm): "
  f"{money(sum(float(r['Chi phí (đ)']) for r in bad))} — 0 SQL toàn bộ: "
  f"{all(float(r['Lead chất lượng (SQL)'])==0 for r in bad)}")
for r in sorted(bad, key=lambda x: -float(x["Chi phí (đ)"])):
    P(f"      {r['Cụm từ tìm kiếm']:<38}{r['Loại đối sánh khớp']:<10}{money(float(r['Chi phí (đ)'])):>14}"
      f"  SQL={int(float(r['Lead chất lượng (SQL)']))}")
comp_st = [r for r in st if r["Chiến dịch"] == "SEA_Competitor_DoiThu"]
P(f"    Competitor: {len(comp_st)} cụm, {money(sum(float(r['Chi phí (đ)']) for r in comp_st))}, "
  f"SQL = {sum(float(r['Lead chất lượng (SQL)']) for r in comp_st):.0f}")

# Địa lý
P("")
geo = list(csv.DictReader(open(os.path.join(SH, "06_DIA_LY.csv"), encoding="utf-8-sig")))
geo = [g for g in geo if g["Khu vực"] and g["Khu vực"] != "TỔNG" and g["Chi phí (đ)"]]
far = ["Hà Nội","Đà Nẵng","Cần Thơ & ĐBSCL","Đồng Nai","Người dùng ngoài Việt Nam quan tâm đến Việt Nam"]
fg = [g for g in geo if g["Khu vực"] in far]
P(f"A7 Địa lý ngoài vùng bán (HN, ĐN, ĐBSCL, Đồng Nai, ngoài VN): "
  f"{money(sum(float(g['Chi phí (đ)']) for g in fg))} "
  f"({sum(float(g['% chi phí']) for g in fg)*100:.1f}% ngân sách), "
  f"SQL {sum(float(g['Lead chất lượng (SQL)']) for g in fg):.0f}, "
  f"cọc {sum(float(g['Đặt cọc']) for g in fg):.0f}")
for g in fg:
    P(f"    {g['Khu vực']:<50}{money(float(g['Chi phí (đ)'])):>14}  SQL={int(float(g['Lead chất lượng (SQL)']))}"
      f"  CP/SQL={money(float(g['CP/SQL (đ)']))}")
hcm = [g for g in geo if g["Khu vực"].startswith("TP.HCM")]
P(f"    Đối chiếu TP.HCM: chi phí {money(sum(float(g['Chi phí (đ)']) for g in hcm))} "
  f"({sum(float(g['% chi phí']) for g in hcm)*100:.1f}%), SQL {sum(float(g['Lead chất lượng (SQL)']) for g in hcm):.0f}, "
  f"cọc {sum(float(g['Đặt cọc']) for g in hcm):.0f}")

# Khung giờ / cuối tuần
P("")
P("A8 Khung giờ 20:00-24:00 (07_KHUNG_GIO_TB A): chi phí 337.261.419 + 72.141.480 = "
  + money(337261419+72141480) + f" ({(0.187+0.04)*100:.1f}% ngân sách), "
  f"tỷ lệ gọi lại <30 phút chỉ 21% và 12%")
P(f"    CP/SQL 20-23h = 3.011.263đ vs 09-12h = 2.504.084đ (chênh {3011263/2504084-1:+.1%})")
P("A9 Cuối tuần (07 mục C): T7+CN chi phí " + money(262814000+240996000) +
  f" ({(262814000+240996000)/T['Chi_phi']*100:.1f}% ngân sách) nhưng chỉ 2/8 sale trực; "
  f"CP/SQL T7 3.020.851đ vs T2 2.151.142đ (+{3020851/2151142-1:.1%})")
P(f"A10 Thiết bị (07 mục B): di động chiếm 78,1% chi phí ({money(1408562397)}) nhưng CVR 2,03% "
  f"và CP/SQL 3.042.251đ; desktop CVR 4,02%, CP/SQL 1.847.796đ (rẻ hơn {1-1847796/3042251:.0%})")

# CRM vận hành
P("")
P("A11 Tốc độ phản hồi (08 mục A): chỉ 11% lead được gọi <5 phút (tỷ lệ cọc 1,82%); "
  "26% lead gọi sau >12h (tỷ lệ cọc 0,04% — thấp hơn 45 lần)")
resp = [("Dưới 5 phút",281,0.0182),("5-30 phút",485,0.0121),("30ph-2h",588,0.0058),
        ("2-12h",536,0.0021),(">12h",664,0.0004)]
now = sum(n*r for _,n,r in resp)
best = sum(n for _,n,_ in resp) * 0.0182
P(f"    Cọc thực tế theo bảng A = {now:.1f}; nếu 100% lead gọi <5 phút = {best:.1f} "
  f"-> chênh {best-now:.1f} cọc = {money((best-now)*HH)} doanh thu bỏ lỡ")
P(f"    Lead bị bỏ sót hoàn toàn (08 mục B): 118+96+61 = {118+96+61} lead, "
  f"giá trị theo CPL_CRM = {money((118+96+61)*cpl_crm)}")
P("A12 Chất lượng lead theo nguồn (08 mục C): PMax lead dùng được chỉ 7%, trùng SĐT 31%, "
  "SĐT sai 24%; Brand 67%; Competitor 26% (26% là môi giới/đối thủ)")

# Landing page v1 vs v2
P("")
v1_rate, v2_rate = 1002/4912, 713/2546
P(f"A13 Trang đích (10_GA4 mục C): v1 hoàn tất form {v1_rate*100:.1f}% (LCP 4,8s), "
  f"v2 {v2_rate*100:.1f}% (LCP 1,9s) -> +{v2_rate/v1_rate-1:.1%}")
P(f"    Nếu v2 chạy từ ngày 1: 4.912 form_start x {v2_rate:.4f} = {4912*v2_rate:.0f} lead "
  f"thay vì 1.002 -> +{4912*v2_rate-1002:.0f} lead trong 57 ngày đầu "
  f"= {money((4912*v2_rate-1002)*cpl_crm)} theo CPL_CRM")
P(f"    Quy ra cọc: +{(4912*v2_rate-1002)*sql_rate*coc_per_sql:.1f} cọc "
  f"= {money((4912*v2_rate-1002)*sql_rate*coc_per_sql*HH)}")

# GA4 hao hut click->session
P("")
P("A14 Hao hụt nhấp -> phiên (10_GA4 mục B): PMax 28,0% (39.701 nhấp -> 28.585 phiên), "
  "GDN 45,0%, YT 82,0%. PMax bounce <3s = 74,3% (11_CLARITY mục B), thời lượng phiên trung vị 3 giây")
P(f"    PMax chi phí {money(pmax['Chi_phi'])}; nếu 74,3% phiên là rác -> "
  f"~{money(pmax['Chi_phi']*0.743)} chi phí không có giá trị")

# Attribution
P("")
P("A15 Mô hình phân bổ (10_GA4 mục D): last-click gán Brand 592 lead nhưng data-driven chỉ 401 "
  "(-32,3%); YouTube 43 -> 165 (+283,7%); GDN 132 -> 186 (+40,9%); "
  "71 lead thực tế đến từ Direct/Organic mà last-click gán hết cho Ads")

# Cấu hình
P("")
P("A16 Cấu hình (05_CAU_HINH_TK): 4 hành động chuyển đổi chính (2 trong đó là rác); "
  "Enhanced conversions TẮT; offline import CHƯA có (CRM không lưu GCLID); "
  "Search Partners + Display network BẬT trong Search; 12 từ phủ định; "
  "71% chi phí Search từ đối sánh rộng; QS 5,2/10")
P("A17 GTM (12_GTM): 34 thẻ, 412KB JS bên thứ 3, +~0,8s LCP; GA4 Config trùng lặp từ ngày 31; "
  "3 thẻ đối tác sàn F2 không rõ nguồn gốc; không có Consent Mode v2; không có server-side; "
  "không có cảnh báo chuyển đổi=0 -> sự cố N44-46 mất 3 ngày mới phát hiện")
P("A18 Sự kiện bị bỏ sót (10_GA4 mục E): zalo_click 894 lượt + file_download 1.206 lượt "
  "chưa đánh dấu sự kiện chính, chưa nhập Ads -> mất tín hiệu tối ưu")

# Ngân sách & pacing
P("")
P("=" * 78); P("PACING & NGÂN SÁCH")
P(f"Chi phí 90 ngày = {money(T['Chi_phi'])} vs ngân sách 90 ngày tới 2.100.000.000 "
  f"({T['Chi_phi']/BUDGET*100:.1f}%) -> bình quân {money(T['Chi_phi']/90)}/ngày")
P(f"KPI cọc: thực tế {int(T['Dat_Coc'])} vs mục tiêu 32 -> cần tăng {32/T['Dat_Coc']:.2f}x")
P(f"KPI ROAS: thực tế {div(T['DoanhThu_HoaHong'],T['Chi_phi']):.2f}x vs 3,0x -> cần tăng "
  f"{3.0/div(T['DoanhThu_HoaHong'],T['Chi_phi']):.2f}x")
P(f"KPI CP/SQL: thực tế {money(cp_sql)} vs 2.200.000 -> cần giảm "
  f"{1-2_200_000/cp_sql:.1%}")

# ---------------- PHẦN C: phân bổ ngân sách ----------------
P(""); P("=" * 78); P("PHẦN C — PHÂN BỔ NGÂN SÁCH 2,1 TỶ")
alloc = {
  "SEA_Brand_Vinhomes_HocMon":       (190_000_000, 210_000_000, 220_000_000),
  "SEA_Generic_NhaPho_CanHo_TayBac": (260_000_000, 290_000_000, 310_000_000),
  "PMAX_VinhomesHM_Lead":            ( 50_000_000,  90_000_000, 120_000_000),
  "GDN_Remarketing_Web30d":          ( 40_000_000,  45_000_000,  50_000_000),
  "YT_Video_TVC_MoBan":              (  0,          15_000_000,  30_000_000),
  "SEA_Competitor_DoiThu":           (  0,           0,          20_000_000),
  "Dự phòng (giữ lại, chỉ giải ngân khi đạt ngưỡng mở rộng)": (60_000_000, 40_000_000, 60_000_000),
}
P(f"{'Chiến dịch':<40}{'GĐ1':>16}{'GĐ2':>16}{'GĐ3':>16}{'Tổng':>16}{'%':>7}{'Kỳ trước':>16}")
tot = [0,0,0]
for c,(a,b,d) in alloc.items():
    old = agg([r for r in rows if r["Chien_dich"] == c])["Chi_phi"] if c in camps else 0
    tot[0]+=a; tot[1]+=b; tot[2]+=d
    P(f"{c:<40}{money(a):>16}{money(b):>16}{money(d):>16}{money(a+b+d):>16}"
      f"{(a+b+d)/BUDGET*100:>6.1f}%{money(old) if old else '—':>16}")
P(f"{'TỔNG':<40}{money(tot[0]):>16}{money(tot[1]):>16}{money(tot[2]):>16}{money(sum(tot)):>16}"
  f"{sum(tot)/BUDGET*100:>6.1f}%")
assert sum(tot) == BUDGET, f"Tổng phân bổ {sum(tot)} != {BUDGET}"
P(f"KIỂM TRA: tổng = {money(sum(tot))} = ngân sách duyệt 2.100.000.000 ✔")
P(f"Ngân sách/ngày bình quân: GĐ1 {money(tot[0]/30)}, GĐ2 {money(tot[1]/30)}, GĐ3 {money(tot[2]/30)}")

# Dự báo kết quả kế hoạch
P("")
P("DỰ BÁO KẾT QUẢ THEO KẾ HOẠCH (giả định tỷ lệ kịch bản C, CP/SQL mục tiêu 2,2tr):")
sql_plan = BUDGET / 2_200_000
s1,s2,s3,s4 = scen["C_ke_hoach"]
P(f"  SQL {sql_plan:.0f} -> đi xem {sql_plan*s2:.0f} -> booking {sql_plan*s2*s3:.0f} "
  f"-> cọc {sql_plan*s2*s3*s4:.0f} -> DT {money(sql_plan*s2*s3*s4*HH)} "
  f"-> ROAS {sql_plan*s2*s3*s4*HH/BUDGET:.2f}x")
P(f"  Lead thô cần: {sql_plan/s1:.0f} -> {sql_plan/s1/90:.1f} lead/ngày "
  f"(năng lực sale 8x12 = 96/ngày, T7-CN chỉ 2x12 = 24/ngày)")

# Năng lực sale cuối tuần
wk = sql_plan/s1/90
P(f"  Cảnh báo năng lực: T7-CN chỉ 24 lead/ngày; nếu giữ nguyên phân bổ đều "
  f"({wk:.1f} lead/ngày) thì cuối tuần vẫn trong ngưỡng, nhưng tốc độ phản hồi sẽ hỏng "
  f"(hiện T7 CP/SQL cao hơn T2 {3020851/2151142-1:.0%})")

# ---------------- D3: PMax ----------------
P(""); P("=" * 78); P("D3 — PMAX")
P(f"CP/CĐ_Ads PMax = {money(div(pmax['Chi_phi'],pmax['ChuyenDoi_Ads']))} (thấp nhất tài khoản)")
for c in camps:
    a = agg([r for r in rows if r["Chien_dich"] == c])
    P(f"  {c:<34} CP/CĐ_Ads {money(div(a['Chi_phi'],a['ChuyenDoi_Ads'])):>14} | "
      f"CP/SQL {money(div(a['Chi_phi'],a['Lead_SQL'])) if a['Lead_SQL'] else 'n/a':>16} | "
      f"CP/cọc {money(div(a['Chi_phi'],a['Dat_Coc'])) if a['Dat_Coc'] else 'n/a':>16}")
P(f"PMax: {int(pmax['ChuyenDoi_Ads'])} CĐ_Ads -> {int(pmax['Lead_CRM'])} lead CRM -> "
  f"{int(pmax['Lead_SQL'])} SQL -> {int(pmax['Di_Xem_Nha'])} đi xem -> {int(pmax['Booking'])} booking -> "
  f"{int(pmax['Dat_Coc'])} cọc. Doanh thu {money(pmax['DoanhThu_HoaHong'])}. ROAS 0.")
P(f"PMax chi phí {money(pmax['Chi_phi'])} = {pmax['Chi_phi']/T['Chi_phi']*100:.1f}% ngân sách")

# ---------------- D1: brand ----------------
P(""); P("=" * 78); P("D1 — BRAND")
P(f"Brand: chi phí {money(brand['Chi_phi'])} ({brand['Chi_phi']/T['Chi_phi']*100:.1f}%), "
  f"cọc {int(brand['Dat_Coc'])}/{int(T['Dat_Coc'])} ({brand['Dat_Coc']/T['Dat_Coc']*100:.1f}%), "
  f"DT {money(brand['DoanhThu_HoaHong'])} ({brand['DoanhThu_HoaHong']/T['DoanhThu_HoaHong']*100:.1f}%), "
  f"ROAS {div(brand['DoanhThu_HoaHong'],brand['Chi_phi']):.2f}x")
P(f"Generic: chi phí {money(gen['Chi_phi'])} ({gen['Chi_phi']/T['Chi_phi']*100:.1f}%), "
  f"cọc {int(gen['Dat_Coc'])}, DT {money(gen['DoanhThu_HoaHong'])}, "
  f"ROAS {div(gen['DoanhThu_HoaHong'],gen['Chi_phi']):.2f}x, "
  f"CP/SQL {money(div(gen['Chi_phi'],gen['Lead_SQL']))}")
P(f"Nếu chuyển toàn bộ {money(brand['Chi_phi'])} sang Generic ở CP/cọc Generic "
  f"({money(div(gen['Chi_phi'],gen['Dat_Coc']))}/cọc) -> chỉ ra "
  f"{brand['Chi_phi']/div(gen['Chi_phi'],gen['Dat_Coc']):.1f} cọc thay vì {int(brand['Dat_Coc'])} cọc "
  f"-> mất {brand['Dat_Coc']-brand['Chi_phi']/div(gen['Chi_phi'],gen['Dat_Coc']):.1f} cọc = "
  f"{money((brand['Dat_Coc']-brand['Chi_phi']/div(gen['Chi_phi'],gen['Dat_Coc']))*HH)}")
P("Data-driven vẫn gán Brand 401/1715 generate_lead = "
  f"{401/1715*100:.1f}% (10_GA4 mục D) -> brand KHÔNG chỉ 'ăn theo'")
P(f"Brand mất IS do thứ hạng {wis(brs,'Mat_IS_ThuHang')*100:.1f}% -> đã có người khác đấu giá trên tên dự án")

# ---------------- D4: cắt còn 1,2 tỷ ----------------
P(""); P("=" * 78); P("D4 — NGÂN SÁCH CẮT CÒN 1,2 TỶ")
B2 = 1_200_000_000
alloc2 = {"SEA_Brand_Vinhomes_HocMon":480_000_000,
          "SEA_Generic_NhaPho_CanHo_TayBac":480_000_000,
          "GDN_Remarketing_Web30d":120_000_000,
          "PMAX_VinhomesHM_Lead":90_000_000,
          "YT_Video_TVC_MoBan":0,
          "SEA_Competitor_DoiThu":0,
          "Dự phòng":30_000_000}
for k,v in alloc2.items():
    old = agg([r for r in rows if r["Chien_dich"]==k])["Chi_phi"] if k in camps else 0
    P(f"  {k:<36}{money(v):>16}  ({v/B2*100:>5.1f}%)   kỳ trước {money(old) if old else '—'}")
assert sum(alloc2.values()) == B2
P(f"  TỔNG {money(sum(alloc2.values()))} ✔")
# ước tính cọc ở 1,2 tỷ
P(f"  Ở CP/SQL mục tiêu 2,2tr -> {B2/2_200_000:.0f} SQL -> cọc "
  f"{B2/2_200_000*s2*s3*s4:.1f} -> DT {money(B2/2_200_000*s2*s3*s4*HH)} "
  f"-> ROAS {B2/2_200_000*s2*s3*s4*HH/B2:.2f}x (KPI 32 cọc KHÔNG khả thi, tối đa ~{B2/2_200_000*s2*s3*s4:.0f})")

P(""); P("=" * 78); P("HẾT")

with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "agent-4-calc.out.txt"),
          "w", encoding="utf-8") as f:
    f.write("\n".join(out))
