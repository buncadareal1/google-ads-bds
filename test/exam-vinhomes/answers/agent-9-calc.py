#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Bài thi Performance Marketing Lead - thí sinh 9.
Mọi con số trong answers/agent-9.md truy ngược được về script này.
Nguồn: CSV 90 ngày (sheet 02) + các sheet CSV trong ../sheets/.
Chạy: python3 agent-9-calc.py
"""
import csv, os
from collections import defaultdict

CSV = "/home/docdang/Downloads/du_lieu_google_ads_90_ngay_1.csv"
SHEETS = "/home/docdang/Projects/google-ads/test/exam-vinhomes/sheets"

NUM = ["Hien_thi","Nhap_chuot","Chi_phi","ChuyenDoi_Ads","Lead_CRM","Lead_SQL",
       "Di_Xem_Nha","Booking","Dat_Coc","DoanhThu_HoaHong"]
FLT = ["Impr_Share","Mat_IS_NganSach","Mat_IS_ThuHang"]

rows = list(csv.DictReader(open(CSV, encoding="utf-8-sig")))
for r in rows:
    for k in NUM: r[k] = float(r[k] or 0)
    for k in FLT: r[k] = float(r[k]) if r[k] else float("nan")
    r["Ngay_thu"] = int(r["Ngay_thu"])

def agg(rs):
    d = {k: sum(r[k] for r in rs) for k in NUM}
    d["n"] = len(rs)
    return d

def div(a, b): return a / b if b else float("nan")

def fmt(x):
    if x != x: return "n/a"
    return f"{x:,.0f}".replace(",", ".")

OUT = []
def P(*a):
    s = " ".join(str(x) for x in a)
    OUT.append(s); print(s)

# ---------------------------------------------------------------- B1
P("="*90); P("B1. CPL/CP-SQL/CP-COC — TOAN KY & TUNG CHIEN DICH")
tot = agg(rows)
camps = sorted(set(r["Chien_dich"] for r in rows))
P(f"{'Chien dich':34}{'ChiPhi':>14}{'CPL_Ads':>12}{'CPL_CRM':>12}{'CP/SQL':>13}{'CP/Coc':>14}{'ROAS':>7}")
B1 = {}
for c in camps + ["TOAN KY"]:
    rs = rows if c == "TOAN KY" else [r for r in rows if r["Chien_dich"] == c]
    a = agg(rs)
    d = dict(cost=a["Chi_phi"],
             cpl_ads=div(a["Chi_phi"], a["ChuyenDoi_Ads"]),
             cpl_crm=div(a["Chi_phi"], a["Lead_CRM"]),
             cpsql=div(a["Chi_phi"], a["Lead_SQL"]),
             cpcoc=div(a["Chi_phi"], a["Dat_Coc"]),
             roas=div(a["DoanhThu_HoaHong"], a["Chi_phi"]), **a)
    B1[c] = d
    P(f"{c:34}{fmt(d['cost']):>14}{fmt(d['cpl_ads']):>12}{fmt(d['cpl_crm']):>12}"
      f"{fmt(d['cpsql']):>13}{fmt(d['cpcoc']):>14}{d['roas']:>7.2f}")
P("Kiem tra tong: chi phi =", fmt(tot["Chi_phi"]), "| ChuyenDoi_Ads =", fmt(tot["ChuyenDoi_Ads"]),
  "| Lead_CRM =", fmt(tot["Lead_CRM"]), "| SQL =", fmt(tot["Lead_SQL"]),
  "| Coc =", fmt(tot["Dat_Coc"]), "| DoanhThu =", fmt(tot["DoanhThu_HoaHong"]))

# ---------------------------------------------------------------- B2
P("="*90); P("B2. ROAS TOAN KY & TUNG GIAI DOAN")
P(f"{'GD':10}{'ChiPhi':>16}{'DoanhThu':>16}{'ROAS':>8}{'Coc':>6}{'CP/Coc':>14}")
B2 = {}
for g in ["GĐ1", "GĐ2", "GĐ3", "TOÀN KỲ"]:
    rs = rows if g == "TOÀN KỲ" else [r for r in rows if r["Giai_doan"] == g]
    a = agg(rs); roas = div(a["DoanhThu_HoaHong"], a["Chi_phi"])
    B2[g] = dict(cost=a["Chi_phi"], rev=a["DoanhThu_HoaHong"], roas=roas, coc=a["Dat_Coc"])
    P(f"{g:10}{fmt(a['Chi_phi']):>16}{fmt(a['DoanhThu_HoaHong']):>16}{roas:>8.2f}"
      f"{a['Dat_Coc']:>6.0f}{fmt(div(a['Chi_phi'],a['Dat_Coc'])):>14}")
# ROAS theo chien dich x giai doan
P("-- ROAS chien dich x giai doan --")
for c in camps:
    line = f"{c:34}"
    for g in ["GĐ1", "GĐ2", "GĐ3"]:
        a = agg([r for r in rows if r["Chien_dich"] == c and r["Giai_doan"] == g])
        line += f"{div(a['DoanhThu_HoaHong'],a['Chi_phi']):>8.2f}"
    P(line)

# ---------------------------------------------------------------- B3
P("="*90); P("B3. TY LE CHUYEN DOI TUNG BUOC PHEU (toan ky + tung chien dich)")
def funnel(a):
    return dict(sql=div(a["Lead_SQL"], a["Lead_CRM"]),
                xem=div(a["Di_Xem_Nha"], a["Lead_SQL"]),
                book=div(a["Booking"], a["Di_Xem_Nha"]),
                coc=div(a["Dat_Coc"], a["Booking"]),
                coc_xem=div(a["Dat_Coc"], a["Di_Xem_Nha"]),
                lead2coc=div(a["Dat_Coc"], a["Lead_CRM"]))
F = funnel(tot)
P(f"Lead_CRM {tot['Lead_CRM']:.0f} -> SQL {tot['Lead_SQL']:.0f} -> DiXem {tot['Di_Xem_Nha']:.0f}"
  f" -> Booking {tot['Booking']:.0f} -> Coc {tot['Dat_Coc']:.0f}")
P(f"Lead->SQL {F['sql']*100:.2f}% | SQL->DiXem {F['xem']*100:.2f}% | DiXem->Booking {F['book']*100:.2f}%"
  f" | Booking->Coc {F['coc']*100:.2f}% | DiXem->Coc {F['coc_xem']*100:.2f}% | Lead->Coc {F['lead2coc']*100:.3f}%")
P(f"{'Chien dich':34}{'L>SQL':>9}{'SQL>Xem':>9}{'Xem>Bk':>9}{'Bk>Coc':>9}")
for c in camps:
    f = funnel(agg([r for r in rows if r["Chien_dich"] == c]))
    P(f"{c:34}{f['sql']*100:>8.1f}%{f['xem']*100:>8.1f}%{f['book']*100:>8.1f}%{f['coc']*100:>8.1f}%")
P("-- pheu theo giai doan --")
for g in ["GĐ1", "GĐ2", "GĐ3"]:
    f = funnel(agg([r for r in rows if r["Giai_doan"] == g]))
    P(f"{g:8}{f['sql']*100:>8.1f}%{f['xem']*100:>8.1f}%{f['book']*100:>8.1f}%{f['coc']*100:>8.1f}%"
      f" | Lead->Coc {f['lead2coc']*100:.3f}%")

# ---------------------------------------------------------------- B4
P("="*90); P("B4. NGUOC TU KPI 32 COC / NGAN SACH 2,1 TY")
BUDGET = 2_100_000_000; TARGET_COC = 32
# Kich ban 1: giu nguyen ty le lich su toan ky
sc = {}
sc["A_lichsu_toanky"] = dict(xem_coc=F["coc_xem"], sql_xem=F["xem"], l_sql=F["sql"])
# Kich ban 2: ty le GD3 (gan nhat, da co LP v2 + SLA sale)
f3 = funnel(agg([r for r in rows if r["Giai_doan"] == "GĐ3"]))
sc["B_GD3"] = dict(xem_coc=f3["coc_xem"], sql_xem=f3["xem"], l_sql=f3["sql"])
# Kich ban 3: ke hoach - loai bo PMax rac, ty le SQL/lead theo nhom Search Brand+Generic
srch = agg([r for r in rows if r["Chien_dich"] in
            ("SEA_Brand_Vinhomes_HocMon", "SEA_Generic_NhaPho_CanHo_TayBac")])
fs = funnel(srch)
sc["C_ChiSearchBrand+Generic"] = dict(xem_coc=fs["coc_xem"], sql_xem=fs["xem"], l_sql=fs["sql"])
P(f"{'Kich ban':30}{'Xem>Coc':>10}{'SQL>Xem':>10}{'Lead>SQL':>10}{'SQL can':>10}{'Lead can':>10}{'CP/SQL max':>14}{'CPL max':>12}")
B4 = {}
for k, v in sc.items():
    xem = TARGET_COC / v["xem_coc"]
    sql = xem / v["sql_xem"]
    lead = sql / v["l_sql"]
    B4[k] = dict(xem=xem, sql=sql, lead=lead,
                 cpsql=BUDGET / sql, cpl=BUDGET / lead, cpcoc=BUDGET / TARGET_COC, **v)
    P(f"{k:30}{v['xem_coc']*100:>9.1f}%{v['sql_xem']*100:>9.1f}%{v['l_sql']*100:>9.1f}%"
      f"{sql:>10.0f}{lead:>10.0f}{fmt(BUDGET/sql):>14}{fmt(BUDGET/lead):>12}")
P("Nhu cau di xem nha theo kich ban:", {k: round(v["xem"]) for k, v in B4.items()})
P("Nang luc sale: 8 sale x 12 lead/ngay x 90 ngay =", fmt(8*12*90), "lead thô tối đa")
P("Lead can/ngay theo kich ban:", {k: round(v["lead"]/90, 1) for k, v in B4.items()})

# ---------------------------------------------------------------- B5
P("="*90); P("B5. DIEM HOA VON / TRAN CHI PHI MOI COC")
HH = 181_000_000
for roas in [3.0, 2.5, 2.0, 1.0]:
    P(f"ROAS {roas:.1f}x -> chi phi QC toi da/coc = {fmt(HH/roas)} d"
      f" | so coc toi thieu voi NS 2,1 ty = {BUDGET/(HH/roas):.1f}")
P(f"Voi 2,1 ty & 32 coc: CP/coc thuc te = {fmt(BUDGET/TARGET_COC)} d;"
  f" ROAS = {32*HH/BUDGET:.2f}x; doanh thu = {fmt(32*HH)} d")
P(f"So coc toi thieu de dat ROAS 3,0x voi 2,1 ty = {BUDGET*3.0/HH:.1f} -> lam tron 35 coc")
P(f"Hoa von tuyet doi (ROAS 1,0x) = {BUDGET/HH:.1f} coc")
P(f"Thuc te 90 ngay qua: {tot['Dat_Coc']:.0f} coc, CP/coc = {fmt(div(tot['Chi_phi'],tot['Dat_Coc']))},"
  f" ROAS = {div(tot['DoanhThu_HoaHong'],tot['Chi_phi']):.2f}x -> "
  f"thieu {(BUDGET*3.0/HH)-tot['Dat_Coc']:.1f} coc so nguong 3,0x (quy ve NS 2,1 ty)")

# ---------------------------------------------------------------- B6
P("="*90); P("B6. DOI CHIEU 3 NGUON SO LIEU (sheet 10_GA4 muc A + 12_GTM muc B)")
ads = 3820; gl = 1715; ctc_hit = 1132; ctc_user = 779; vpp = 612; e30 = 361
crm = 2557
dup = ctc_hit - ctc_user           # 353
junk = vpp + e30                   # 973
missing = 63                       # lead N44-46 mat the (GTM v23)
P(f"Kiem tra cau thanh 3.820: {gl}+{ctc_hit}+{vpp}+{e30} = {gl+ctc_hit+vpp+e30}  (khop: {gl+ctc_hit+vpp+e30==ads})")
P(f"(1) Dem trung luot goi        : -{dup}")
P(f"(2) Su kien rac (khong phai lead): -{junk}  (view_price_page {vpp} + engaged_30s {e30})")
P(f"=> Lead that do duoc bang the : {ads-dup-junk}  (khop GA4 2.494: {ads-dup-junk==2494})")
P(f"(3) Lead mat the N44-46 (GTM v23, khoi phuc v24): +{missing}")
P(f"=> CRM = {ads-dup-junk+missing}  (khop CRM {crm}: {ads-dup-junk+missing==crm})")
P(f"Chenh lech tong = {ads-crm} = {dup} (trung) + {junk} (rac) - {missing} (mat the) = {dup+junk-missing}")
P(f"Ty le thoi phong Ads/CRM = {ads/crm:.3f}x ; nguong bao dong sheet 09 = >1,8x;"
  f" nhung neu so voi SQL that: {ads}/{tot['Lead_SQL']:.0f} = {ads/tot['Lead_SQL']:.2f}x")
P(f"% chi phi Ads dang toi uu theo tin hieu KHONG phai lead = {(dup+junk)/ads*100:.1f}%")
# chi phi quy doi cho tin hieu rac
cost_junk = tot["Chi_phi"] * (dup + junk) / ads
P(f"Quy doi chi phi bam theo tin hieu sai (theo ty trong chuyen doi) ~ {fmt(cost_junk)} d")

# ---------------------------------------------------------------- B7
P("="*90); P("B7. LEAD MAT DO LOI KY THUAT CHUA SUA (sheet 11_CLARITY muc C)")
clar = [("#4 Loi JS e.setDate (Safari iOS) - form khong gui duoc", 4196, 280, 340),
        ("#5 Nut CTA bi khung chat che (<380px)", 2741, 60, 90),
        ("#6 tel: link tren desktop khong phan hoi", 1204, 30, 50)]
lo = sum(x[2] for x in clar); hi = sum(x[3] for x in clar)
cpl_crm = div(tot["Chi_phi"], tot["Lead_CRM"])
cpsql = div(tot["Chi_phi"], tot["Lead_SQL"])
sql_rate = F["sql"]; coc_per_sql = div(tot["Dat_Coc"], tot["Lead_SQL"])
P(f"{'Loi':52}{'Phien':>8}{'LeadMat_lo':>12}{'LeadMat_hi':>12}")
for n, s, a, b in clar: P(f"{n:52}{s:>8}{a:>12}{b:>12}")
P(f"TONG (do UX Clarity uoc tinh, KHONG phai so do): {lo} - {hi} lead")
P(f"CPL_CRM thuc te toan ky = {fmt(cpl_crm)} d -> gia tri lead mat = {fmt(lo*cpl_crm)} - {fmt(hi*cpl_crm)} d")
P(f"Quy ra SQL (ty le SQL/lead {sql_rate*100:.1f}%): {lo*sql_rate:.0f} - {hi*sql_rate:.0f} SQL")
P(f"Quy ra coc (coc/SQL {coc_per_sql*100:.2f}%): {lo*sql_rate*coc_per_sql:.1f} - {hi*sql_rate*coc_per_sql:.1f} coc")
P(f"Doanh thu hoa hong bo lo = {fmt(lo*sql_rate*coc_per_sql*HH)} - {fmt(hi*sql_rate*coc_per_sql*HH)} d")
# them: 63 lead mat the N44-46
P(f"[Rieng] 63 lead N44-46 khong vao Ads/GA4 -> may hoc mat tin hieu; gia tri media = {fmt(63*cpl_crm)} d")

# ---------------------------------------------------------------- PHAN A: bang chung
P("="*90); P("PHAN A — BANG CHUNG SO")
# A1 PMax
pm = B1["PMAX_VinhomesHM_Lead"]
P(f"PMax: chi phi {fmt(pm['cost'])} ({pm['cost']/tot['Chi_phi']*100:.1f}% TK), "
  f"ChuyenDoi_Ads {pm['ChuyenDoi_Ads']:.0f}, Lead_CRM {pm['Lead_CRM']:.0f}, SQL {pm['Lead_SQL']:.0f}, "
  f"DiXem {pm['Di_Xem_Nha']:.0f}, Coc {pm['Dat_Coc']:.0f}, DoanhThu 0 -> ROAS 0")
P(f"PMax CPL_Ads {fmt(pm['cpl_ads'])} (thap nhat TK) NHUNG CP/SQL {fmt(pm['cpsql'])}; "
  f"SQL/Lead {pm['Lead_SQL']/pm['Lead_CRM']*100:.1f}% (nguong bao dong sheet 09 <12%)")
# A2 Competitor
cp = B1["SEA_Competitor_DoiThu"]
P(f"Competitor: chi phi {fmt(cp['cost'])}, Lead_CRM {cp['Lead_CRM']:.0f}, SQL {cp['Lead_SQL']:.0f}, "
  f"Coc 0, ROAS 0 -> lang phi 100% = {fmt(cp['cost'])}")
# A3 YouTube
yt = B1["YT_Video_TVC_MoBan"]
P(f"YouTube: chi phi {fmt(yt['cost'])}, SQL {yt['Lead_SQL']:.0f}, Coc 0, CP/SQL {fmt(yt['cpsql'])}")
gdn = B1["GDN_Remarketing_Web30d"]
P(f"GDN: chi phi {fmt(gdn['cost'])}, SQL {gdn['Lead_SQL']:.0f}, Coc 0, CP/SQL {fmt(gdn['cpsql'])}")
# A4 Brand bi bop ngan sach
br = [r for r in rows if r["Chien_dich"] == "SEA_Brand_Vinhomes_HocMon"]
a = agg(br)
P(f"BRAND: chi phi {fmt(a['Chi_phi'])} = {a['Chi_phi']/tot['Chi_phi']*100:.1f}% TK; "
  f"coc {a['Dat_Coc']:.0f}/{tot['Dat_Coc']:.0f} = {a['Dat_Coc']/tot['Dat_Coc']*100:.0f}% so coc; "
  f"doanh thu {fmt(a['DoanhThu_HoaHong'])} = {a['DoanhThu_HoaHong']/tot['DoanhThu_HoaHong']*100:.0f}% doanh thu; "
  f"ROAS {div(a['DoanhThu_HoaHong'],a['Chi_phi']):.2f}x")
P(f"BRAND IS TB = {sum(r['Impr_Share'] for r in br)/len(br)*100:.1f}%; "
  f"mat IS ngan sach TB = {sum(r['Mat_IS_NganSach'] for r in br)/len(br)*100:.1f}%; "
  f"mat IS thu hang TB = {sum(r['Mat_IS_ThuHang'] for r in br)/len(br)*100:.1f}%")
for g in ["GĐ1", "GĐ2", "GĐ3"]:
    rs = [r for r in br if r["Giai_doan"] == g]
    P(f"  BRAND {g}: IS {sum(r['Impr_Share'] for r in rs)/len(rs)*100:.1f}%, "
      f"mat IS NS {sum(r['Mat_IS_NganSach'] for r in rs)/len(rs)*100:.1f}%, "
      f"chi phi {fmt(sum(r['Chi_phi'] for r in rs))}, coc {sum(r['Dat_Coc'] for r in rs):.0f}, "
      f"ROAS {div(sum(r['DoanhThu_HoaHong'] for r in rs), sum(r['Chi_phi'] for r in rs)):.2f}x")
# uoc tinh doanh thu bo lo do brand mat IS ngan sach
rev_per_cost_brand = a["DoanhThu_HoaHong"] / a["Chi_phi"]
lost_is = sum(r["Mat_IS_NganSach"] for r in br) / len(br)
extra_cost = a["Chi_phi"] * lost_is / max(1e-9, sum(r["Impr_Share"] for r in br)/len(br))
P(f"UOC TINH: mo rong brand theo ty le IS mat do NS ({lost_is*100:.1f}%) "
  f"~ can them {fmt(extra_cost)} d chi phi -> doanh thu tang ~ {fmt(extra_cost*rev_per_cost_brand)} d "
  f"(gia dinh ROAS bien = ROAS TB brand {rev_per_cost_brand:.2f}x — la UOC TINH, khong phai so do)")

# A5 Search terms rac
st = list(csv.DictReader(open(os.path.join(SHEETS, "04_SEARCH_TERMS.csv"), encoding="utf-8-sig")))
st = [r for r in st if r.get("Chi phí (đ)") and r["Chi phí (đ)"].replace(".","").isdigit()]
waste = [r for r in st if float(r["Lead chất lượng (SQL)"]) == 0]
wc = sum(float(r["Chi phí (đ)"]) for r in waste)
P(f"SEARCH TERMS: {len(waste)}/{len(st)} cum tu co 0 SQL, tieu {fmt(wc)} d "
  f"= {wc/tot['Chi_phi']*100:.1f}% tong chi phi TK")
P("  Top cum tu 0 SQL:", "; ".join(f"{r['Cụm từ tìm kiếm']} {fmt(float(r['Chi phí (đ)']))}"
   for r in sorted(waste, key=lambda x: -float(x["Chi phí (đ)"]))[:8]))
broad = [r for r in st if r["Loại đối sánh khớp"] == "Rộng"]
bc = sum(float(r["Chi phí (đ)"]) for r in broad)
bsql = sum(float(r["Lead chất lượng (SQL)"]) for r in broad)
P(f"  Doi sanh RONG trong bang search terms: {fmt(bc)} d, {bsql:.0f} SQL -> CP/SQL {fmt(div(bc,bsql))}")

# A6 Dia ly
geo = list(csv.DictReader(open(os.path.join(SHEETS, "06_DIA_LY.csv"), encoding="utf-8-sig")))
geo = [g for g in geo if g["Khu vực"] and g["Khu vực"] != "TỔNG" and g["Chi phí (đ)"]]
outreg = ["Hà Nội", "Đà Nẵng", "Cần Thơ & ĐBSCL", "Người dùng ngoài Việt Nam quan tâm đến Việt Nam"]
oc = sum(float(g["Chi phí (đ)"]) for g in geo if g["Khu vực"] in outreg)
osql = sum(float(g["Lead chất lượng (SQL)"]) for g in geo if g["Khu vực"] in outreg)
ococ = sum(float(g["Đặt cọc"]) for g in geo if g["Khu vực"] in outreg)
P(f"DIA LY: HN+DN+DBSCL+ngoai VN tieu {fmt(oc)} d ({oc/tot['Chi_phi']*100:.1f}%), "
  f"{osql:.0f} SQL, {ococ:.0f} coc -> CP/SQL {fmt(div(oc,osql))}")
core = ["TP.HCM — Quận 12", "TP.HCM — Hóc Môn", "TP.HCM — Gò Vấp", "TP.HCM — Bình Tân", "TP.HCM — Củ Chi"]
cc = sum(float(g["Chi phí (đ)"]) for g in geo if g["Khu vực"] in core)
csql = sum(float(g["Lead chất lượng (SQL)"]) for g in geo if g["Khu vực"] in core)
ccoc = sum(float(g["Đặt cọc"]) for g in geo if g["Khu vực"] in core)
P(f"  Loi 5 quan huyen: {fmt(cc)} d ({cc/tot['Chi_phi']*100:.1f}%), {csql:.0f} SQL, {ccoc:.0f} coc,"
  f" CP/SQL {fmt(div(cc,csql))} -> tot hon vung ngoai {div(oc,osql)/div(cc,csql):.1f} lan")

# A7 Khung gio / thiet bi / ngay trong tuan
P("KHUNG GIO 20:00-24:00: chi phi 337.261.419 + 72.141.480 = "
  f"{fmt(337261419+72141480)} d = {(337261419+72141480)/tot['Chi_phi']*100:.1f}% TK; "
  f"ty le goi lai <30' chi 21% va 12% (sheet 07A)")
P(f"CUOI TUAN T7+CN: chi phi {fmt(262814000+240996000)} = "
  f"{(262814000+240996000)/tot['Chi_phi']*100:.1f}% TK, chi 2/8 sale truc; "
  f"lead {364+358} nhung nang luc chi 2x12x2 = 48 lead/2 ngay")
P("DI DONG: 78,1% chi phi (1.408.562.397 d), CVR 2,03%, CP/SQL 3.042.251 vs "
  "may tinh CVR 4,02%, CP/SQL 1.847.796 -> di dong dat hon 1,65 lan")

# A8 Toc do phan hoi lead -> coc bo lo
crm8 = [("Duoi 5 phut", 281, .0182), ("5-30 phut", 485, .0121), ("30' - 2h", 588, .0058),
        ("2-12h", 536, .0021), (">12h", 664, .0004)]
cur = sum(n*r for _, n, r in crm8)
best = sum(n for _, n, _ in crm8) * .0182
P(f"CRM toc do phan hoi: coc ky vong hien tai = {cur:.1f}; neu 100% goi <5' = {best:.1f} "
  f"-> bo lo {best-cur:.1f} coc = {fmt((best-cur)*HH)} d hoa hong (UOC TINH tu sheet 08A)")
miss = 118+96+61
P(f"Lead bi bo sot khong ai goi: {miss} lead (sheet 08B) -> gia tri media {fmt(miss*cpl_crm)} d;"
  f" quy ra coc theo ty le TB {div(tot['Dat_Coc'],tot['Lead_CRM'])*100:.3f}%: {miss*div(tot['Dat_Coc'],tot['Lead_CRM']):.1f} coc")

# A9 Landing page v1 vs v2
P("LP v1 (N1-57): 52.410 phien, hoan tat form 20,4%, LCP 4,8s | "
  "LP v2 (N58-90): 42.938 phien, 28,0%, LCP 1,9s -> +37,3% ty le hoan tat (sheet 10C)")
gap_leads = 52410 * (0.280047132757266 - 0.203990228013029) * (4912/52410)
P(f"UOC TINH lead bo lo do chay LP v1 57 ngay: neu form_start giu nguyen 4.912, "
  f"ap ty le hoan tat v2 (28,0%) -> {4912*0.280047132757266:.0f} lead thay vi 1.002 "
  f"=> +{4912*0.280047132757266-1002:.0f} lead ~ {fmt((4912*0.280047132757266-1002)*cpl_crm)} d")

# A10 Ngay 44-46 chuyen doi 0
P("-- Ngay 44,45,46 (su co GTM v23) --")
for d in [43, 44, 45, 46, 47, 48]:
    rs = [r for r in rows if r["Ngay_thu"] == d]
    a2 = agg(rs)
    P(f"  N{d}: chi phi {fmt(a2['Chi_phi'])}, ChuyenDoi_Ads {a2['ChuyenDoi_Ads']:.0f}, "
      f"Lead_CRM {a2['Lead_CRM']:.0f}")
c446 = sum(r["Chi_phi"] for r in rows if r["Ngay_thu"] in (44, 45, 46))
P(f"  Tong chi phi 3 ngay su co: {fmt(c446)} d, chuyen doi Ads = "
  f"{sum(r['ChuyenDoi_Ads'] for r in rows if r['Ngay_thu'] in (44,45,46)):.0f}, "
  f"Lead_CRM = {sum(r['Lead_CRM'] for r in rows if r['Ngay_thu'] in (44,45,46)):.0f}")

# A11 GA4 hao hut nhap -> phien
P("HAO HUT NHAP->PHIEN (sheet 10B): PMax 28,0% (39.701 nhap -> 28.585 phien), "
  "GDN 45,0%, YT 82,0%; Clarity: PMax thoat nhanh <3s = 74,3%, thoi luong phien trung vi 3 giay")
pm_cost = pm["cost"]
P(f"  => uoc tinh chi phi PMax roi vao luu luong khong thuc: 74,3% x {fmt(pm_cost)} = "
  f"{fmt(pm_cost*0.743)} d (UOC TINH, dung ty le thoat nhanh Clarity lam proxy)")

# A12 Ngan sach vs KPI moi
P(f"NGAN SACH: da tieu {fmt(tot['Chi_phi'])} trong 90 ngay = {fmt(tot['Chi_phi']/90)} d/ngay; "
  f"KPI moi 2,1 ty = {fmt(BUDGET/90)} d/ngay (+{BUDGET/tot['Chi_phi']*100-100:.1f}%)")
P(f"KPI can 32 coc vs thuc te {tot['Dat_Coc']:.0f} coc -> phai tang {32/tot['Dat_Coc']:.2f} lan "
  f"trong khi ngan sach chi tang {BUDGET/tot['Chi_phi']:.2f} lan "
  f"=> hieu suat/dong phai tang {32/tot['Dat_Coc']/(BUDGET/tot['Chi_phi']):.2f} lan")
P(f"CP/SQL hien tai {fmt(cpsql)} vs KPI <=2.200.000 -> phai giam {(1-2_200_000/cpsql)*100:.1f}%")

# ---------------------------------------------------------------- PHAN C: phan bo ngan sach
P("="*90); P("PHAN C — PHAN BO NGAN SACH 2,1 TY / 3 GIAI DOAN")
alloc = {
 "GĐ1 (N1-30)": {"SEA_Brand": 130_000_000, "SEA_Generic_Core": 190_000_000,
                 "PMAX_Feed_Lead": 90_000_000, "GDN_RMK": 40_000_000,
                 "Demand/YT_RMK": 0, "Du_phong_test": 30_000_000},
 "GĐ2 (N31-60)": {"SEA_Brand": 160_000_000, "SEA_Generic_Core": 250_000_000,
                  "PMAX_Feed_Lead": 130_000_000, "GDN_RMK": 45_000_000,
                  "Demand/YT_RMK": 35_000_000, "Du_phong_test": 30_000_000},
 "GĐ3 (N61-90)": {"SEA_Brand": 230_000_000, "SEA_Generic_Core": 340_000_000,
                  "PMAX_Feed_Lead": 180_000_000, "GDN_RMK": 60_000_000,
                  "Demand/YT_RMK": 45_000_000, "Du_phong_test": 45_000_000},
}
gt = 0
for g, d in alloc.items():
    s = sum(d.values()); gt += s
    P(f"{g}: " + ", ".join(f"{k} {fmt(v)}" for k, v in d.items()) + f" | TONG {fmt(s)}")
P(f"TONG 3 GIAI DOAN = {fmt(gt)} (kiem tra = 2.100.000.000: {gt == BUDGET})")
by_c = defaultdict(int)
for d in alloc.values():
    for k, v in d.items(): by_c[k] += v
P("Theo chien dich:", ", ".join(f"{k} {fmt(v)} ({v/BUDGET*100:.1f}%)" for k, v in by_c.items()))
# muc tieu tung giai doan (dung ty le kich ban B, cai thien dan)
P("-- Muc tieu dinh luong tung GD (gia dinh CP/SQL cai thien dan) --")
targets = [("GĐ1", 470_000_000, 2_600_000, 6), ("GĐ2", 650_000_000, 2_200_000, 10),
           ("GĐ3", 980_000_000, 1_900_000, 16)]
tot_sql = tot_coc = 0
for g, b, cps, coc in targets:
    sql = b / cps; tot_sql += sql; tot_coc += coc
    P(f"{g}: NS {fmt(b)}, CP/SQL muc tieu {fmt(cps)} -> {sql:.0f} SQL, muc tieu {coc} coc, "
      f"doanh thu {fmt(coc*HH)}, ROAS {coc*HH/b:.2f}x")
P(f"CONG: {tot_sql:.0f} SQL, {tot_coc} coc, doanh thu {fmt(tot_coc*HH)}, "
  f"ROAS toan ky {tot_coc*HH/BUDGET:.2f}x, CP/SQL binh quan {fmt(BUDGET/tot_sql)}")
P(f"Lead tho tuong ung (SQL/lead muc tieu 38%): {tot_sql/0.38:.0f} lead = "
  f"{tot_sql/0.38/90:.1f} lead/ngay (nang luc sale 96/ngay -> {tot_sql/0.38/90/96*100:.0f}% cong suat)")

# ---------------------------------------------------------------- PHAN D3
P("="*90); P("PHAN D3 — PMAX: CPA THAP NHAT NHUNG...")
P(f"PMax CPL_Ads {fmt(pm['cpl_ads'])} (thap nhat) | Brand CPL_Ads {fmt(B1['SEA_Brand_Vinhomes_HocMon']['cpl_ads'])}")
P(f"Nhung CP/SQL: PMax {fmt(pm['cpsql'])} vs Brand {fmt(B1['SEA_Brand_Vinhomes_HocMon']['cpsql'])} "
  f"-> PMax dat gap {pm['cpsql']/B1['SEA_Brand_Vinhomes_HocMon']['cpsql']:.1f} lan")
P(f"PMax: {pm['Dat_Coc']:.0f} coc, doanh thu {fmt(pm['DoanhThu_HoaHong'])}, ROAS 0 sau {fmt(pm['cost'])} chi phi")
P("Sheet 08C: PMax 31% trung SDT, 24% SDT sai, 34% sai phan khuc, chi 7% lead dung duoc")
P(f"  -> 160 lead kiem tra x 7% = {160*0.07:.0f} lead dung duoc; ap cho toan bo "
  f"{pm['Lead_CRM']:.0f} lead PMax -> {pm['Lead_CRM']*0.07:.0f} lead dung duoc")
P("Sheet 11B: PMax thoat nhanh <3s 74,3%, thoi luong trung vi 3 giay, 6,1% phien >2 trang")
P(f"Neu dồn 500 trieu vao PMax voi CP/SQL hien tai -> {500_000_000/pm['cpsql']:.0f} SQL; "
  f"cung so tien vao Brand -> {500_000_000/B1['SEA_Brand_Vinhomes_HocMon']['cpsql']:.0f} SQL")

# ---------------------------------------------------------------- PHAN D4
P("="*90); P("PHAN D4 — NGAN SACH CAT CON 1,2 TY")
cut = {"SEA_Brand": 300_000_000, "SEA_Generic_Core": 560_000_000,
       "PMAX_Feed_Lead": 200_000_000, "GDN_RMK": 90_000_000, "Du_phong": 50_000_000}
P(", ".join(f"{k} {fmt(v)}" for k, v in cut.items()), "| TONG", fmt(sum(cut.values())))
P(f"Coc ky vong voi 1,2 ty & CP/SQL 2,1tr: {1_200_000_000/2_100_000:.0f} SQL x "
  f"ty le SQL->coc muc tieu 3,0% = {1_200_000_000/2_100_000*0.03:.1f} coc, "
  f"ROAS = {1_200_000_000/2_100_000*0.03*HH/1_200_000_000:.2f}x")

# ---------------------------------------------------------------- self-check
P("="*90); P("SELF-CHECK")
assert abs(tot["Chi_phi"] - 1_803_537_000) < 1, tot["Chi_phi"]
assert tot["ChuyenDoi_Ads"] == 3820 and tot["Lead_CRM"] == 2557
assert tot["Lead_SQL"] == 651 and tot["Dat_Coc"] == 18
assert gl + ctc_hit + vpp + e30 == ads
assert ads - dup - junk == 2494
assert ads - dup - junk + missing == crm
assert gt == BUDGET
assert sum(cut.values()) == 1_200_000_000
P("OK — tat ca kiem tra dat.")

open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "agent-9-output.txt"), "w",
     encoding="utf-8").write("\n".join(OUT))
