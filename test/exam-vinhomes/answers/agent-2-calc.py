#!/usr/bin/env python3
# ponytail: stdlib csv only, no pandas in env. Moi so trong agent-2.md deu tu day.
import csv, collections, io

CSV = "/home/docdang/Downloads/du_lieu_google_ads_90_ngay_1.csv"
NUM = ["Hien_thi","Nhap_chuot","Chi_phi","ChuyenDoi_Ads","Lead_CRM","Lead_SQL",
       "Di_Xem_Nha","Booking","Dat_Coc","DoanhThu_HoaHong"]
RATE = ["Impr_Share","Mat_IS_NganSach","Mat_IS_ThuHang"]

rows = []
with open(CSV, encoding="utf-8-sig") as f:
    for r in csv.DictReader(f):
        for k in NUM:
            r[k] = float(r[k] or 0)
        for k in RATE:
            r[k] = float(r[k]) if r.get(k) else None
        rows.append(r)

def agg(rs):
    d = {k: sum(r[k] for r in rs) for k in NUM}
    d["n"] = len(rs)
    return d

def div(a, b):
    return a / b if b else float("nan")

def fmt(x):
    return f"{x:,.0f}" if x == x else "n/a"

def line(label, d):
    print(f"{label:42s} | chi phi {fmt(d['Chi_phi']):>15} | click {fmt(d['Nhap_chuot']):>8} | "
          f"CD_Ads {fmt(d['ChuyenDoi_Ads']):>6} | Lead {fmt(d['Lead_CRM']):>6} | SQL {fmt(d['Lead_SQL']):>5} | "
          f"Xem {fmt(d['Di_Xem_Nha']):>4} | Book {fmt(d['Booking']):>4} | Coc {fmt(d['Dat_Coc']):>3} | "
          f"DT {fmt(d['DoanhThu_HoaHong']):>15}")

def kpis(label, d):
    print(f"{label:42s} | CPL_Ads {fmt(div(d['Chi_phi'],d['ChuyenDoi_Ads'])):>10} | "
          f"CPL_CRM {fmt(div(d['Chi_phi'],d['Lead_CRM'])):>10} | "
          f"CP/SQL {fmt(div(d['Chi_phi'],d['Lead_SQL'])):>12} | "
          f"CP/coc {fmt(div(d['Chi_phi'],d['Dat_Coc'])):>13} | "
          f"ROAS {div(d['DoanhThu_HoaHong'],d['Chi_phi']):>6.2f} | "
          f"SQL/Lead {div(d['Lead_SQL'],d['Lead_CRM']):>6.1%} | "
          f"CTR {div(d['Nhap_chuot'],d['Hien_thi']):>6.2%} | "
          f"CPC {fmt(div(d['Chi_phi'],d['Nhap_chuot'])):>9}")

print("="*140); print("### TOAN KY")
tot = agg(rows); line("TOAN KY", tot); kpis("TOAN KY", tot)
print(f"So ngay: {len(set(r['Ngay'] for r in rows))}, chi phi/ngay TB = {fmt(tot['Chi_phi']/90)}")

print("\n### B1 — THEO CHIEN DICH (toan ky)")
bycd = collections.OrderedDict()
for r in rows: bycd.setdefault(r["Chien_dich"], []).append(r)
for cd, rs in bycd.items():
    d = agg(rs); line(cd, d); kpis(cd, d)
    print(f"{'':42s} | %chi phi {div(d['Chi_phi'],tot['Chi_phi']):.1%}")

print("\n### B2 — THEO GIAI DOAN")
bygd = collections.OrderedDict()
for r in rows: bygd.setdefault(r["Giai_doan"], []).append(r)
for gd in sorted(bygd):
    d = agg(bygd[gd]); line(gd, d); kpis(gd, d)

print("\n### B2b — CHIEN DICH x GIAI DOAN (ROAS)")
for cd in bycd:
    for gd in sorted(bygd):
        rs = [r for r in rows if r["Chien_dich"] == cd and r["Giai_doan"] == gd]
        if not rs: continue
        d = agg(rs)
        print(f"{cd:36s} {gd} chi phi {fmt(d['Chi_phi']):>13} coc {d['Dat_Coc']:>3.0f} "
              f"DT {fmt(d['DoanhThu_HoaHong']):>13} ROAS {div(d['DoanhThu_HoaHong'],d['Chi_phi']):>6.2f} "
              f"CP/SQL {fmt(div(d['Chi_phi'],d['Lead_SQL'])):>12}")

print("\n### B3 — PHEU TOAN KY & THEO CHIEN DICH")
def funnel(label, d):
    print(f"{label:42s} Lead {d['Lead_CRM']:>7.0f} -> SQL {d['Lead_SQL']:>5.0f} ({div(d['Lead_SQL'],d['Lead_CRM']):>6.1%}) "
          f"-> Xem {d['Di_Xem_Nha']:>4.0f} ({div(d['Di_Xem_Nha'],d['Lead_SQL']):>6.1%}) "
          f"-> Book {d['Booking']:>4.0f} ({div(d['Booking'],d['Di_Xem_Nha']):>6.1%}) "
          f"-> Coc {d['Dat_Coc']:>3.0f} ({div(d['Dat_Coc'],d['Booking']):>6.1%}) "
          f"| Lead->Coc {div(d['Dat_Coc'],d['Lead_CRM']):>6.2%} | Xem->Coc {div(d['Dat_Coc'],d['Di_Xem_Nha']):>6.1%}")
funnel("TOAN KY", tot)
for cd, rs in bycd.items(): funnel(cd, agg(rs))
for gd in sorted(bygd): funnel(gd, agg(bygd[gd]))
print(f"Doanh thu/coc thuc te = {fmt(div(tot['DoanhThu_HoaHong'],tot['Dat_Coc']))}")

print("\n### SEARCH-ONLY (3 chien dich Search) vs PHAN CON LAI")
SEARCH = [c for c in bycd if c.startswith("SEA_")]
ds = agg([r for r in rows if r["Chien_dich"] in SEARCH])
dn = agg([r for r in rows if r["Chien_dich"] not in SEARCH])
line("SEARCH", ds); kpis("SEARCH", ds)
line("PMAX+GDN+YT", dn); kpis("PMAX+GDN+YT", dn)
print(f"PMax+GDN+YT: chi phi {fmt(dn['Chi_phi'])} = {div(dn['Chi_phi'],tot['Chi_phi']):.1%} tong, coc {dn['Dat_Coc']:.0f}, DT {fmt(dn['DoanhThu_HoaHong'])}")

print("\n### B4 — KPI 32 COC / 2,1 TY")
KPI_COC, BUDGET, HH = 32, 2_100_000_000, 181_000_000
r_sql_xem = div(tot["Di_Xem_Nha"], tot["Lead_SQL"])
r_xem_book = div(tot["Booking"], tot["Di_Xem_Nha"])
r_book_coc = div(tot["Dat_Coc"], tot["Booking"])
r_sql_coc = div(tot["Dat_Coc"], tot["Lead_SQL"])
r_lead_sql = div(tot["Lead_SQL"], tot["Lead_CRM"])
print(f"Baseline lich su: SQL->Xem {r_sql_xem:.1%}, Xem->Book {r_xem_book:.1%}, Book->Coc {r_book_coc:.1%}, "
      f"SQL->Coc {r_sql_coc:.2%}, Lead->SQL {r_lead_sql:.1%}")
for name, sql_coc, lead_sql in [
        ("KB A - giu nguyen ty le lich su", r_sql_coc, r_lead_sql),
        ("KB B - SQL->Coc +25%, Lead->SQL 32%", r_sql_coc*1.25, 0.32),
        ("KB C - SQL->Coc +50%, Lead->SQL 35%", r_sql_coc*1.50, 0.35)]:
    sql_need = KPI_COC / sql_coc
    lead_need = sql_need / lead_sql
    print(f"{name:40s} SQL/Coc {sql_coc:.2%} Lead/SQL {lead_sql:.1%} => can SQL {sql_need:>7.0f}, "
          f"lead tho {lead_need:>8.0f}, lead/ngay {lead_need/90:>6.1f}, "
          f"CP/SQL toi da {fmt(BUDGET/sql_need):>12}, CPL toi da {fmt(BUDGET/lead_need):>10}")
print(f"Nang luc sale hien tai: 8 sale x 12 lead/ngay = 96 lead/ngay = {96*90} lead/90 ngay (tran ly thuyet)")
print(f"Cuoi tuan chi 2 sale: tran T7+CN = 2*12 = 24 lead/ngay")
cap = 96*65 + 24*25   # dem tu CSV cot Thu: 65 ngay thuong, 25 ngay T7/CN
print(f"Tran thuc te co tinh cuoi tuan (65 ngay thuong + 25 ngay T7/CN) = {cap} lead/90 ngay")
print(f"  KB B can 2893 lead => dung {2893/cap:.1%} nang luc")

print("\n### B5 — HOA VON")
print(f"ROAS 3,0x voi HH {fmt(HH)}/coc => chi phi QC toi da/coc = {fmt(HH/3)}")
print(f"Voi 32 coc: ngan sach toi da = {fmt(32*HH/3)} | ngan sach duyet {fmt(BUDGET)}")
print(f"Voi 2,1 ty ngan sach: DT can dat = {fmt(BUDGET*3)} => so coc can = {BUDGET*3/HH:.1f} coc")
print(f"CP/coc hien tai = {fmt(div(tot['Chi_phi'],tot['Dat_Coc']))} => gap {div(tot['Chi_phi'],tot['Dat_Coc'])/(HH/3):.2f}x nguong hoa von")
print(f"ROAS hien tai (DT thuc {fmt(tot['DoanhThu_HoaHong'])}) = {div(tot['DoanhThu_HoaHong'],tot['Chi_phi']):.2f}x")

print("\n### B6 — DOI CHIEU 3 NGUON (nguon: sheet 10_GA4 muc A + E, 12_GTM v23/v24)")
ga4 = {"generate_lead":1715, "click_to_call_luot":1132, "click_to_call_nguoi":779,
       "view_price_page":612, "engaged_30s":361}
ads_conv = ga4["generate_lead"]+ga4["click_to_call_luot"]+ga4["view_price_page"]+ga4["engaged_30s"]
dup = ga4["click_to_call_luot"]-ga4["click_to_call_nguoi"]
junk = ga4["view_price_page"]+ga4["engaged_30s"]
tag_lead = ga4["generate_lead"]+ga4["click_to_call_nguoi"]
crm = int(tot["Lead_CRM"]); missing = crm - tag_lead
print(f"Ads 'Chuyen doi' = {ads_conv} (kiem tra vs CSV: {tot['ChuyenDoi_Ads']:.0f})")
print(f"  - trung lap click_to_call (luot - nguoi) = {dup} ({dup/ads_conv:.1%})")
print(f"  - su kien rac (view_price_page {ga4['view_price_page']} + engaged_30s {ga4['engaged_30s']}) = {junk} ({junk/ads_conv:.1%})")
print(f"  = Lead that do duoc bang the = {tag_lead}   [{ads_conv} - {dup} - {junk} = {ads_conv-dup-junk}]")
print(f"  + Lead mat the N44-46 (GTM v23) = {missing}")
print(f"  = Lead CRM = {tag_lead + missing} (khop CRM {crm}: {tag_lead+missing==crm})")
print(f"Ty le thoi phong Ads/CRM = {ads_conv/crm:.3f}x (nguong bao dong sheet 09 = >1,8x; canh bao >1,5x)")

print("\n### Ngay 44-46: kiem chung tu CSV (chuyen doi = 0?)")
for d in [43,44,45,46,47,48]:
    rs = [r for r in rows if int(r["Ngay_thu"]) == d]
    a = agg(rs)
    print(f"  Ngay {d}: CD_Ads {a['ChuyenDoi_Ads']:>5.0f} | Lead_CRM {a['Lead_CRM']:>4.0f} | chi phi {fmt(a['Chi_phi'])}")
n44_46 = agg([r for r in rows if 44 <= int(r["Ngay_thu"]) <= 46])
print(f"  Tong N44-46: CD_Ads {n44_46['ChuyenDoi_Ads']:.0f}, Lead_CRM {n44_46['Lead_CRM']:.0f}, chi phi {fmt(n44_46['Chi_phi'])}")

print("\n### B7 — LEAD MAT DO LOI KY THUAT CHUA SUA (nguon 11_CLARITY muc C, loi #4/#5/#6)")
CPL_CRM = div(tot["Chi_phi"], tot["Lead_CRM"])
CP_SQL  = div(tot["Chi_phi"], tot["Lead_SQL"])
print(f"CPL_CRM thuc te = {fmt(CPL_CRM)} | CP/SQL thuc te = {fmt(CP_SQL)} | SQL/Lead = {r_lead_sql:.1%}")
for lo, hi, ten in [(280,340,"#4 loi JS date picker Safari iOS"),(60,90,"#5 nut bi khung chat che"),(30,50,"#6 tel: tren desktop")]:
    print(f"  {ten:38s} {lo}-{hi} lead ~ {fmt(lo*CPL_CRM)} - {fmt(hi*CPL_CRM)} d")
LO, HI = 370, 480
print(f"TONG chua sua: {LO}-{HI} lead => gia tri theo CPL_CRM: {fmt(LO*CPL_CRM)} - {fmt(HI*CPL_CRM)} d")
print(f"  quy ra SQL (x{r_lead_sql:.3f}): {LO*r_lead_sql:.0f}-{HI*r_lead_sql:.0f} SQL")
print(f"  quy ra coc (SQL->Coc {r_sql_coc:.2%}): {LO*r_lead_sql*r_sql_coc:.2f}-{HI*r_lead_sql*r_sql_coc:.2f} coc")
print(f"  quy ra doanh thu HH: {fmt(LO*r_lead_sql*r_sql_coc*HH)} - {fmt(HI*r_lead_sql*r_sql_coc*HH)} d")
LOa, HIa = 90+320+110, 140+400+150
print(f"Loi DA SUA o v2 (#1+#2+#3, chi anh huong N1-57): {LOa}-{HIa} lead ~ {fmt(LOa*CPL_CRM)} - {fmt(HIa*CPL_CRM)} d (da mat, khong thu hoi duoc)")

print("\n### PHAN A — CAC SO DUNG LAM BANG CHUNG")
print("-- A1: PMax --")
pm = agg(bycd["PMAX_VinhomesHM_Lead"])
print(f"PMax chi phi {fmt(pm['Chi_phi'])} ({div(pm['Chi_phi'],tot['Chi_phi']):.1%}), CD_Ads {pm['ChuyenDoi_Ads']:.0f}, "
      f"Lead {pm['Lead_CRM']:.0f}, SQL {pm['Lead_SQL']:.0f} ({div(pm['Lead_SQL'],pm['Lead_CRM']):.1%}), "
      f"Xem {pm['Di_Xem_Nha']:.0f}, Coc {pm['Dat_Coc']:.0f}, DT {fmt(pm['DoanhThu_HoaHong'])}, "
      f"CPL_Ads {fmt(div(pm['Chi_phi'],pm['ChuyenDoi_Ads']))}, CP/SQL {fmt(div(pm['Chi_phi'],pm['Lead_SQL']))}, "
      f"ty le thoi phong {div(pm['ChuyenDoi_Ads'],pm['Lead_CRM']):.2f}x")
print("-- A2: Competitor --")
co = agg(bycd["SEA_Competitor_DoiThu"])
print(f"Competitor chi phi {fmt(co['Chi_phi'])}, Lead {co['Lead_CRM']:.0f}, SQL {co['Lead_SQL']:.0f}, Coc {co['Dat_Coc']:.0f}, "
      f"CP/SQL {fmt(div(co['Chi_phi'],co['Lead_SQL']))}, CPC {fmt(div(co['Chi_phi'],co['Nhap_chuot']))}, CTR {div(co['Nhap_chuot'],co['Hien_thi']):.2%}")
print("-- A3: Brand vs cac chien dich khac --")
br = agg(bycd["SEA_Brand_Vinhomes_HocMon"])
print(f"Brand chi phi {fmt(br['Chi_phi'])} ({div(br['Chi_phi'],tot['Chi_phi']):.1%}), Coc {br['Dat_Coc']:.0f}/{tot['Dat_Coc']:.0f} "
      f"({div(br['Dat_Coc'],tot['Dat_Coc']):.0%}), DT {fmt(br['DoanhThu_HoaHong'])} ({div(br['DoanhThu_HoaHong'],tot['DoanhThu_HoaHong']):.0%}), "
      f"ROAS {div(br['DoanhThu_HoaHong'],br['Chi_phi']):.2f}x, CP/SQL {fmt(div(br['Chi_phi'],br['Lead_SQL']))}")
print("-- A4: Impression Share Brand --")
brs = [r for r in rows if r["Chien_dich"]=="SEA_Brand_Vinhomes_HocMon" and r["Impr_Share"] is not None]
if brs:
    print(f"Brand IS TB = {sum(r['Impr_Share'] for r in brs)/len(brs):.1%}, "
          f"Mat IS ngan sach TB = {sum(r['Mat_IS_NganSach'] for r in brs)/len(brs):.1%}, "
          f"Mat IS thu hang TB = {sum(r['Mat_IS_ThuHang'] for r in brs)/len(brs):.1%} (n={len(brs)} ngay)")
    for gd in sorted(bygd):
        g = [r for r in brs if r["Giai_doan"]==gd]
        if g: print(f"   {gd}: IS {sum(r['Impr_Share'] for r in g)/len(g):.1%}, "
                    f"mat IS NS {sum(r['Mat_IS_NganSach'] for r in g)/len(g):.1%}, "
                    f"mat IS TH {sum(r['Mat_IS_ThuHang'] for r in g)/len(g):.1%}")
print("-- IS cac chien dich Search khac --")
for cd in SEARCH:
    s = [r for r in rows if r["Chien_dich"]==cd and r["Impr_Share"] is not None]
    if s: print(f"   {cd}: IS {sum(r['Impr_Share'] for r in s)/len(s):.1%}, "
                f"mat NS {sum(r['Mat_IS_NganSach'] for r in s)/len(s):.1%}, "
                f"mat TH {sum(r['Mat_IS_ThuHang'] for r in s)/len(s):.1%}")

print("\n-- A5: Trang dich v1 (N1-57) vs v2 (N58-90) tren du lieu CSV --")
v1 = agg([r for r in rows if int(r["Ngay_thu"]) <= 57])
v2 = agg([r for r in rows if int(r["Ngay_thu"]) >= 58])
for nm, d, nd in [("N1-57 (LP v1)", v1, 57), ("N58-90 (LP v2)", v2, 33)]:
    print(f"{nm:16s} chi phi {fmt(d['Chi_phi']):>15} ({fmt(d['Chi_phi']/nd)}/ngay) Lead {d['Lead_CRM']:.0f} "
          f"SQL {d['Lead_SQL']:.0f} SQL/Lead {div(d['Lead_SQL'],d['Lead_CRM']):.1%} "
          f"CPL {fmt(div(d['Chi_phi'],d['Lead_CRM']))} CP/SQL {fmt(div(d['Chi_phi'],d['Lead_SQL']))} "
          f"Coc {d['Dat_Coc']:.0f} ROAS {div(d['DoanhThu_HoaHong'],d['Chi_phi']):.2f}")

print("\n-- A6: Cuoi tuan vs ngay thuong (CSV cot Thu) --")
we = agg([r for r in rows if r["Thu"] in ("Thứ 7","Chủ nhật")])
wd = agg([r for r in rows if r["Thu"] not in ("Thứ 7","Chủ nhật")])
nwe = len(set(r["Ngay"] for r in rows if r["Thu"] in ("Thứ 7","Chủ nhật")))
nwd = 90-nwe
print(f"Cuoi tuan ({nwe} ngay): chi phi {fmt(we['Chi_phi'])} ({fmt(we['Chi_phi']/nwe)}/ngay) Lead {we['Lead_CRM']:.0f} "
      f"({we['Lead_CRM']/nwe:.1f}/ngay) SQL {we['Lead_SQL']:.0f} Coc {we['Dat_Coc']:.0f} CP/SQL {fmt(div(we['Chi_phi'],we['Lead_SQL']))}")
print(f"Ngay thuong ({nwd} ngay): chi phi {fmt(wd['Chi_phi'])} ({fmt(wd['Chi_phi']/nwd)}/ngay) Lead {wd['Lead_CRM']:.0f} "
      f"({wd['Lead_CRM']/nwd:.1f}/ngay) SQL {wd['Lead_SQL']:.0f} Coc {wd['Dat_Coc']:.0f} CP/SQL {fmt(div(wd['Chi_phi'],wd['Lead_SQL']))}")
print(f"Chi phi cuoi tuan lang phi neu cat 50%: {fmt(we['Chi_phi']*0.5)}")

print("\n-- A7: Dia ly ngoai vung (sheet 06) --")
FAR = {"Hà Nội":(155104182,186,20,0),"Đà Nẵng":(86569776,104,7,0),
       "Cần Thơ & ĐBSCL":(93783924,113,12,0),"Đồng Nai":(70337943,84,14,0),
       "Ngoài Việt Nam":(28856592,34,7,0)}
fc = sum(v[0] for v in FAR.values()); fs = sum(v[2] for v in FAR.values())
print(f"5 vung xa (HN, DN, Can Tho, Dong Nai, ngoai VN): chi phi {fmt(fc)} = {fc/1803537000:.1%} tong, "
      f"SQL {fs} = {fs/643:.1%} SQL, coc 0. CP/SQL = {fmt(fc/fs)} (vs toan TK {fmt(2804878.69)})")
print(f"HN+DN+CanTho+ngoaiVN (bo Dong Nai): chi phi {fmt(155104182+86569776+93783924+28856592)}, SQL {20+7+12+7}, coc 0")

print("\n-- A8: Search terms rac (sheet 04) --")
JUNK = [("vinhomes hóc môn tuyển dụng",15613000,0),("vinschool hóc môn học phí",10409000,0),
        ("vinhomes hóc môn có thật không",13011000,3),("giá đất hóc môn 2026",33900000,0),
        ("bản đồ quy hoạch hóc môn",27120000,0),("thuê nhà nguyên căn hóc môn",27120000,0),
        ("nhà trọ hóc môn giá rẻ",20340000,0),("bán đất thổ cư hóc môn 100 triệu",27120000,0),
        ("cho thuê kho xưởng hóc môn",20340000,0),("việc làm bất động sản hóc môn",20340000,0),
        ("nhà đất hóc môn lừa đảo",20340000,0),("chung cư mini gò vấp",20340000,0),
        ("dự án bất động sản mới tphcm 2026",33900000,6)]
zero = [j for j in JUNK if j[2]==0]
print(f"Cum tu 0 SQL: {len(zero)} cum, chi phi {fmt(sum(j[1] for j in zero))} = {sum(j[1] for j in zero)/1803537000:.1%} tong TK")
COMP = 176746000
print(f"Cong ca chien dich Competitor ({fmt(co['Chi_phi'])}, 0 coc) => lang phi truc tiep = {fmt(sum(j[1] for j in zero)+co['Chi_phi'])}")

print("\n-- A9: CRM toc do phan hoi (sheet 08A) --")
resp = [("Duoi 5 phut",281,0.87,0.231,0.0182),("5-30 phut",485,0.74,0.154,0.0121),
        ("30p-2h",588,0.58,0.086,0.0058),("2-12h",536,0.41,0.042,0.0021),("Tren 12h",664,0.22,0.011,0.0004)]
tot_lead_08 = sum(r[1] for r in resp)
coc_now = sum(r[1]*r[4] for r in resp)
coc_all5 = tot_lead_08*0.0182
coc_all30 = tot_lead_08*0.0121
print(f"Tong lead sheet08 = {tot_lead_08}; coc ky vong theo mix hien tai = {coc_now:.1f}")
print(f"Neu 100% goi <5p: coc = {coc_all5:.1f} (+{coc_all5-coc_now:.1f} coc = +{fmt((coc_all5-coc_now)*HH)} d HH)")
print(f"Neu 100% goi <30p: coc = {coc_all30:.1f} (+{coc_all30-coc_now:.1f} coc = +{fmt((coc_all30-coc_now)*HH)} d HH)")
print(f"Lead phan hoi >2h = {536+664} = {(536+664)/tot_lead_08:.1%} tong lead")
print(f"Lead bi bo sot (08B): 118+96+61 = {118+96+61} lead ~ {fmt((118+96+61)*CPL_CRM)} d chi phi da tra")

print("\n-- A10: Chat luong lead theo nguon (sheet 08C) x chi phi --")
Q = {"SEA_Brand_Vinhomes_HocMon":0.67,"SEA_Generic_NhaPho_CanHo_TayBac":0.46,
     "SEA_Competitor_DoiThu":0.26,"PMAX_VinhomesHM_Lead":0.07,
     "GDN_Remarketing_Web30d":0.38,"YT_Video_TVC_MoBan":0.25}
for cd, q in Q.items():
    d = agg(bycd[cd])
    print(f"{cd:36s} dung duoc {q:.0%} | lead {d['Lead_CRM']:.0f} => lead dung duoc {d['Lead_CRM']*q:.0f} | "
          f"chi phi/lead dung duoc {fmt(div(d['Chi_phi'],d['Lead_CRM']*q))}")

print("\n-- A11: Thiet bi (sheet 07B) --")
print(f"Mobile: chi phi 1.408.562.397 (78,1%), SQL 463, CP/SQL 3.042.251 | Desktop: 301.190.679 (16,7%), SQL 163, CP/SQL 1.847.796")
print(f"CP/SQL mobile / desktop = {3042251/1847796:.2f}x")

print("\n-- A12: Khung gio (sheet 07A) --")
print(f"20:00-24:00: chi phi {fmt(337261419+72141480)} = {(0.187+0.04):.1%}, SQL {112+22}, "
      f"CP/SQL {fmt((337261419+72141480)/(112+22))}, ty le goi lai <30p 21%/12%")
print(f"00:00-06:00: chi phi {fmt(73945017)} = 4,1%, SQL 18, CP/SQL {fmt(4108056.5)}, goi lai <30p 34%")
print(f"Tong khung gio xau (00-06 + 20-24): {fmt(73945017+337261419+72141480)} = {(0.041+0.187+0.04):.1%} ngan sach")

print("\n-- A13: GA4 hao hut click->phien (sheet 10B) --")
for nm, clicks, sess in [("PMAX",39701,28585),("GDN",28976,15937),("Brand",19045,17331),("Generic",20502,18247)]:
    print(f"  {nm}: {clicks} click -> {sess} phien, hao hut {1-sess/clicks:.1%}")
print("PMax: ty le tuong tac 8,7%, 11 giay, 1,09 trang/phien, thoat nhanh <3s = 74,3% (Clarity B)")

print("\n-- A14: Su kien bo sot (sheet 10E) --")
print(f"zalo_click 894 luot + file_download 1206 luot: chua danh dau su kien chinh, chua nhap vao Ads (tu N71, GTM v26)")

print("\n-- A15: Phan bo (sheet 10D) — neu chuyen sang data-driven --")
DDA = {"Brand":(592,401),"Generic":(418,402),"Competitor":(20,24),"PMax":(510,466),"GDN":(132,186),"YT":(43,165)}
for k,(lc,dd) in DDA.items(): print(f"  {k}: last-click {lc} -> data-driven {dd} ({(dd-lc)/lc:+.1%})")

print("\n### PHAN C — KHUNG NGAN SACH DE XUAT")
plan = [
 ("SEA_Brand_Vinhomes_HocMon",  [100_000_000, 120_000_000, 150_000_000]),
 ("SEA_Generic_NhaPho_CanHo_TayBac",[220_000_000,250_000_000,280_000_000]),
 ("SEA_Competitor_DoiThu",      [0, 25_000_000, 35_000_000]),
 ("PMAX_VinhomesHM_Lead",       [60_000_000, 110_000_000, 170_000_000]),
 ("GDN_Remarketing_Web30d",     [45_000_000, 55_000_000, 65_000_000]),
 ("YT_Video_TVC_MoBan",         [0, 25_000_000, 40_000_000]),
 ("SEA_DSA_LongTail (moi)",     [40_000_000, 50_000_000, 60_000_000]),
 ("Du phong / test",            [60_000_000, 70_000_000, 70_000_000]),
]
g = [0,0,0]
for nm, b in plan:
    for i in range(3): g[i] += b[i]
    print(f"{nm:36s} GD1 {fmt(b[0]):>13} GD2 {fmt(b[1]):>13} GD3 {fmt(b[2]):>13} | tong {fmt(sum(b)):>15}")
print(f"{'TONG':36s} GD1 {fmt(g[0]):>13} GD2 {fmt(g[1]):>13} GD3 {fmt(g[2]):>13} | TONG {fmt(sum(g)):>15}")
assert sum(g) == 2_100_000_000, sum(g)
print("Kiem tra: tong dung 2.100.000.000 VND ✔")

print("\n### D3 — PMAX 'CPA thap nhat' phan bien")
print(f"PMax CPL theo Ads = {fmt(div(pm['Chi_phi'],pm['ChuyenDoi_Ads']))} (thap nhat TK sau Brand)")
print(f"Nhung CP/SQL = {fmt(div(pm['Chi_phi'],pm['Lead_SQL']))}, CP/lead-dung-duoc (7%) = {fmt(div(pm['Chi_phi'],pm['Lead_CRM']*0.07))}, coc = 0, DT = 0, ROAS = 0")
print(f"Brand CP/SQL = {fmt(div(br['Chi_phi'],br['Lead_SQL']))} => PMax dat gap {div(pm['Chi_phi'],pm['Lead_SQL'])/div(br['Chi_phi'],br['Lead_SQL']):.1f}x Brand tren don vi SQL")
print(f"Neu chuyen toan bo {fmt(pm['Chi_phi'])} cua PMax sang Brand voi CP/coc Brand {fmt(div(br['Chi_phi'],br['Dat_Coc']))}: "
      f"~{pm['Chi_phi']/div(br['Chi_phi'],br['Dat_Coc']):.1f} coc bi bo lo")

print("\n### D4 — CAT CON 1,2 TY")
cut = [("SEA_Competitor_DoiThu", co['Chi_phi'], 0),("YT_Video_TVC_MoBan", agg(bycd['YT_Video_TVC_MoBan'])['Chi_phi'], 0),
       ("PMAX (giu 15% de test)", pm['Chi_phi'], 0)]
for nm, c, _ in cut: print(f"  Cat {nm:30s} tiet kiem toan ky {fmt(c)}, coc mat = 0")
print(f"Tong 3 khoan tren = {fmt(co['Chi_phi']+agg(bycd['YT_Video_TVC_MoBan'])['Chi_phi']+pm['Chi_phi'])} "
      f"= {(co['Chi_phi']+agg(bycd['YT_Video_TVC_MoBan'])['Chi_phi']+pm['Chi_phi'])/tot['Chi_phi']:.1%} chi phi 90 ngay vua qua, 0 coc")
plan12 = [("SEA_Brand",380_000_000),("SEA_Generic",480_000_000),("GDN_Remarketing",120_000_000),
          ("PMax (nuoi tin hieu sach)",100_000_000),("DSA/long-tail",80_000_000),("Du phong",40_000_000)]
print("Phan bo 1,2 ty:")
for nm,v in plan12: print(f"  {nm:30s} {fmt(v):>13}")
print(f"  TONG {fmt(sum(v for _,v in plan12))}")
assert sum(v for _,v in plan12) == 1_200_000_000
coc12 = 1_200_000_000/ (br['Chi_phi']/br['Dat_Coc'])
print(f"Uoc coc voi 1,2 ty neu dat CP/coc muc Brand hien tai {fmt(div(br['Chi_phi'],br['Dat_Coc']))}: {coc12:.0f} coc")
print(f"Muc CP/coc can de dat ROAS 3,0x: {fmt(HH/3)} => 1,2 ty / {fmt(HH/3)} = {1_200_000_000/(HH/3):.1f} coc")

print("\n### A4b — CO HOI BRAND NEU BU MAT IS NGAN SACH")
is_now, lost_ns = 0.526, 0.404
scale = min(0.90, is_now+lost_ns)/is_now
print(f"Brand IS {is_now:.1%} + mat IS ngan sach {lost_ns:.1%} = {is_now+lost_ns:.1%} kha dung.")
print(f"Neu keo IS len 90%: he so luu luong x{scale:.2f}")
print(f"  chi phi Brand du kien {fmt(br['Chi_phi']*scale)} (+{fmt(br['Chi_phi']*(scale-1))})")
print(f"  coc du kien {br['Dat_Coc']*scale:.1f} (+{br['Dat_Coc']*(scale-1):.1f}) | DT du kien {fmt(br['DoanhThu_HoaHong']*scale)} "
      f"(+{fmt(br['DoanhThu_HoaHong']*(scale-1))})")
print("  (gia dinh tuyen tinh - la UOC TINH, khong phai so do)")

print("\n### A7b — TAI PHAN BO NGAN SACH NGOAI VUNG")
far = 364_314_474
print(f"364.314.474d (HN+DN+CanTho+ngoai VN) 0 coc. Neu dat CP/SQL vung loi HCM (~{fmt(2082434)}): "
      f"{far/2082434:.0f} SQL thay vi 46 SQL (+{far/2082434-46:.0f} SQL)")
print(f"  quy ra coc theo SQL->Coc {r_sql_coc:.2%}: +{(far/2082434-46)*r_sql_coc:.1f} coc = +{fmt((far/2082434-46)*r_sql_coc*HH)} d")

print("\n### C — MUC TIEU THEO GIAI DOAN (tinh nguoc tu ngan sach de xuat)")
for gd,(bud,cpsql,sqlcoc) in {"GD1":(525_000_000,2_600_000,0.030),
                              "GD2":(705_000_000,2_200_000,0.035),
                              "GD3":(870_000_000,1_900_000,0.042)}.items():
    sql = bud/cpsql; coc = sql*sqlcoc
    print(f"{gd}: ngan sach {fmt(bud)} | CP/SQL muc tieu {fmt(cpsql)} => SQL {sql:.0f} | "
          f"SQL->Coc {sqlcoc:.1%} => coc {coc:.1f} | DT {fmt(coc*HH)} | ROAS {coc*HH/bud:.2f}x | "
          f"lead tho (SQL/Lead 32%) {sql/0.32:.0f} = {sql/0.32/30:.1f} lead/ngay")
tsql = 525e6/2.6e6+705e6/2.2e6+870e6/1.9e6
tcoc = 525e6/2.6e6*0.030+705e6/2.2e6*0.035+870e6/1.9e6*0.042
print(f"TONG 90 ngay: SQL {tsql:.0f}, coc {tcoc:.1f} (KPI 32), DT {fmt(tcoc*HH)}, ROAS {tcoc*HH/2.1e9:.2f}x (KPI 3,0x), "
      f"CP/SQL BQ {fmt(2.1e9/tsql)} (KPI <=2.200.000)")
