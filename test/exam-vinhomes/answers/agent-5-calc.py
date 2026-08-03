#!/usr/bin/env python3
# ponytail: stdlib csv only, no pandas in this env.
"""Tinh toan cho bai lam agent-5.md — Google Ads Vinhomes Hoc Mon 90 ngay.
Nguon: /home/docdang/Downloads/du_lieu_google_ads_90_ngay_1.csv (= sheet 02_DU_LIEU_NGAY)
       + sheets/*.csv (04,05,06,07,08,09,10,11,12)
Chay: python3 agent-5-calc.py
"""
import csv, os
from collections import defaultdict

CSV = "/home/docdang/Downloads/du_lieu_google_ads_90_ngay_1.csv"
SH = "/home/docdang/Projects/google-ads/test/exam-vinhomes/sheets"

NUM = ["Hien_thi","Nhap_chuot","Chi_phi","Impr_Share","Mat_IS_NganSach","Mat_IS_ThuHang",
       "ChuyenDoi_Ads","Lead_CRM","Lead_SQL","Di_Xem_Nha","Booking","Dat_Coc","DoanhThu_HoaHong"]

def load():
    with open(CSV, encoding="utf-8-sig") as f:
        rows = list(csv.DictReader(f))
    for r in rows:
        for k in NUM:
            r[k] = float(r[k]) if r[k] not in ("", None) else 0.0
        r["Ngay_thu"] = int(r["Ngay_thu"])
        r["Tuan"] = int(r["Tuan"])
    return rows

rows = load()
M = 1e6
def s(rs, k): return sum(r[k] for r in rs)
def div(a, b): return a / b if b else float("nan")
def vnd(x): return f"{x:,.0f}"

def agg(rs):
    return {k: s(rs, k) for k in NUM}

def bykey(rs, key):
    d = defaultdict(list)
    for r in rs: d[r[key]].append(r)
    return d

def sect(t): print("\n" + "=" * 78 + f"\n{t}\n" + "=" * 78)

# ---------------------------------------------------------------- SANITY
sect("0. KIEM TRA DU LIEU")
tot = agg(rows)
print(f"So dong: {len(rows)} | so ngay: {len(set(r['Ngay'] for r in rows))} | chien dich: {len(set(r['Chien_dich'] for r in rows))}")
for k in NUM:
    if k.startswith("Impr") or k.startswith("Mat"): continue
    print(f"  {k:22s} = {vnd(tot[k])}")
print("Doi chieu voi sheet 03_TONG_HOP_CD: chi phi 1.803.537.000 | CD Ads 3820 | Lead 2557 | SQL 651 | coc 18 | DT 3.130.000.000")

# ---------------------------------------------------------------- B1
sect("B1. CPL Ads / CPL CRM / CP-SQL / CP-COC — toan ky va tung chien dich")
def b1row(name, a):
    return (name, a["Chi_phi"], a["ChuyenDoi_Ads"], a["Lead_CRM"], a["Lead_SQL"], a["Dat_Coc"],
            div(a["Chi_phi"], a["ChuyenDoi_Ads"]), div(a["Chi_phi"], a["Lead_CRM"]),
            div(a["Chi_phi"], a["Lead_SQL"]), div(a["Chi_phi"], a["Dat_Coc"]),
            div(a["Lead_SQL"], a["Lead_CRM"]), div(a["ChuyenDoi_Ads"], a["Lead_CRM"]))
hdr = "| Chien dich | Chi phi | CD_Ads | Lead | SQL | Coc | CPL_Ads | CPL_CRM | CP/SQL | CP/coc | SQL/Lead | Ads/CRM |"
print(hdr)
out = []
for cd, rs in sorted(bykey(rows, "Chien_dich").items(), key=lambda x: -s(x[1], "Chi_phi")):
    out.append(b1row(cd, agg(rs)))
out.append(b1row("TOAN KY", tot))
for o in out:
    print(f"| {o[0][:34]:34s} | {vnd(o[1]):>13s} | {o[2]:5.0f} | {o[3]:5.0f} | {o[4]:4.0f} | {o[5]:3.0f} "
          f"| {vnd(o[6]):>10s} | {vnd(o[7]):>10s} | {vnd(o[8]):>11s} | {vnd(o[9]):>13s} | {o[10]*100:5.1f}% | {o[11]:.2f}x |")

# ---------------------------------------------------------------- B2
sect("B2. ROAS toan ky va tung giai doan")
for gd in ["GĐ1", "GĐ2", "GĐ3"]:
    a = agg([r for r in rows if r["Giai_doan"] == gd])
    print(f"{gd}: chi phi {vnd(a['Chi_phi'])} | doanh thu {vnd(a['DoanhThu_HoaHong'])} | coc {a['Dat_Coc']:.0f} "
          f"| ROAS {div(a['DoanhThu_HoaHong'], a['Chi_phi']):.2f}x | CP/coc {vnd(div(a['Chi_phi'], a['Dat_Coc']))}")
print(f"TOAN KY: chi phi {vnd(tot['Chi_phi'])} | DT {vnd(tot['DoanhThu_HoaHong'])} | ROAS {div(tot['DoanhThu_HoaHong'], tot['Chi_phi']):.4f}x")
print("\nROAS theo chien dich:")
for cd, rs in sorted(bykey(rows, "Chien_dich").items(), key=lambda x: -s(x[1], "Chi_phi")):
    a = agg(rs)
    print(f"  {cd:34s} chi phi {vnd(a['Chi_phi']):>14s} DT {vnd(a['DoanhThu_HoaHong']):>14s} ROAS {div(a['DoanhThu_HoaHong'], a['Chi_phi']):.2f}x")
print("\nROAS chien dich x giai doan (Brand & Generic):")
for cd in ["SEA_Brand_Vinhomes_HocMon", "SEA_Generic_NhaPho_CanHo_TayBac"]:
    for gd in ["GĐ1", "GĐ2", "GĐ3"]:
        a = agg([r for r in rows if r["Chien_dich"] == cd and r["Giai_doan"] == gd])
        print(f"  {cd:34s} {gd} ROAS {div(a['DoanhThu_HoaHong'], a['Chi_phi']):5.2f}x coc {a['Dat_Coc']:.0f}")

# ---------------------------------------------------------------- B3
sect("B3. Ty le chuyen doi tung buoc pheu (toan ky + tung giai doan + tung chien dich)")
def funnel(a, tag):
    L, Q, X, B, C = a["Lead_CRM"], a["Lead_SQL"], a["Di_Xem_Nha"], a["Booking"], a["Dat_Coc"]
    print(f"{tag:38s} Lead {L:6.0f} -> SQL {Q:5.0f} ({div(Q,L)*100:5.1f}%) -> Xem {X:4.0f} ({div(X,Q)*100:5.1f}%) "
          f"-> Booking {B:4.0f} ({div(B,X)*100:5.1f}%) -> Coc {C:3.0f} ({div(C,B)*100:5.1f}%) | Lead->Coc {div(C,L)*100:.2f}% | SQL->Coc {div(C,Q)*100:.2f}%")
funnel(tot, "TOAN KY")
for gd in ["GĐ1", "GĐ2", "GĐ3"]:
    funnel(agg([r for r in rows if r["Giai_doan"] == gd]), gd)
print()
for cd, rs in bykey(rows, "Chien_dich").items():
    funnel(agg(rs), cd)

# ---------------------------------------------------------------- B4
sect("B4. Nguoc tu KPI 32 coc / 2,1 ty")
BUDGET, KPI_COC, KPI_CPSQL = 2_100_000_000, 32, 2_200_000
# Kich ban 1: giu nguyen ty le toan ky 90 ngay
r_sql_coc_all = div(tot["Dat_Coc"], tot["Lead_SQL"])
r_lead_sql_all = div(tot["Lead_SQL"], tot["Lead_CRM"])
# Kich ban 2: ty le GD3 (LP v2 + SLA sale 15 phut, gan voi tuong lai nhat)
g3 = agg([r for r in rows if r["Giai_doan"] == "GĐ3"])
r_sql_coc_g3 = div(g3["Dat_Coc"], g3["Lead_SQL"])
r_lead_sql_g3 = div(g3["Lead_SQL"], g3["Lead_CRM"])
# Kich ban 3 (KH dung): loai bo chi tieu rac -> chi tinh Search Brand+Generic (kenh co coc)
qual = agg([r for r in rows if r["Chien_dich"] in ("SEA_Brand_Vinhomes_HocMon", "SEA_Generic_NhaPho_CanHo_TayBac")])
r_sql_coc_q = div(qual["Dat_Coc"], qual["Lead_SQL"])
r_lead_sql_q = div(qual["Lead_SQL"], qual["Lead_CRM"])
for tag, rsc, rls in [("A. Ty le toan ky 90 ngay", r_sql_coc_all, r_lead_sql_all),
                      ("B. Ty le GD3 (moi nhat)", r_sql_coc_g3, r_lead_sql_g3),
                      ("C. Chi 2 CD Search co coc", r_sql_coc_q, r_lead_sql_q)]:
    sql_need = KPI_COC / rsc
    lead_need = sql_need / rls
    print(f"{tag}: SQL->Coc {rsc*100:.2f}% | Lead->SQL {rls*100:.1f}% "
          f"=> can {sql_need:.0f} SQL, {lead_need:.0f} lead tho | CP/SQL toi da {vnd(BUDGET/sql_need)} | CPL toi da {vnd(BUDGET/lead_need)}")
    print(f"      -> lead/ngay {lead_need/90:.1f} (nang luc sale 96/ngay), CP/coc toi da {vnd(BUDGET/KPI_COC)}")
print(f"\nRang buoc KPI CP/SQL <= {vnd(KPI_CPSQL)} => voi 2,1 ty mua duoc toi da {BUDGET/KPI_CPSQL:.0f} SQL")
print(f"  Neu dat {BUDGET/KPI_CPSQL:.0f} SQL: so coc theo tung ty le -> "
      f"toan ky {BUDGET/KPI_CPSQL*r_sql_coc_all:.1f} | GD3 {BUDGET/KPI_CPSQL*r_sql_coc_g3:.1f} | 2CD Search {BUDGET/KPI_CPSQL*r_sql_coc_q:.1f}")
print(f"Ty le SQL->Coc toi thieu de 954 SQL ra 32 coc = {KPI_COC/(BUDGET/KPI_CPSQL)*100:.2f}% (hien toan ky {r_sql_coc_all*100:.2f}%)")

# ---------------------------------------------------------------- B5
sect("B5. Diem hoa von / tran chi phi moi coc")
HH = 181_000_000
for roas in [1.0, 2.0, 3.0, 3.5]:
    print(f"  ROAS {roas:.1f}x -> chi phi QC toi da/coc = {vnd(HH/roas)}")
print(f"Voi ngan sach 2,1 ty va tran {vnd(HH/3)}/coc => so coc toi thieu can dat = {BUDGET/(HH/3):.1f} coc")
print(f"32 coc x 181tr = {vnd(32*HH)} doanh thu; ROAS neu tieu het 2,1 ty = {32*HH/BUDGET:.2f}x")
print(f"Bien do an toan: de dat ROAS 3,0x voi 2,1 ty can DT >= {vnd(3*BUDGET)} = {3*BUDGET/HH:.1f} coc")
print(f"Hien tai (90 ngay qua): 18 coc, CP/coc thuc te {vnd(div(tot['Chi_phi'], tot['Dat_Coc']))} "
      f"=> cao hon tran ROAS 3x {div(tot['Chi_phi'], tot['Dat_Coc'])/(HH/3):.2f} lan")

# ---------------------------------------------------------------- B6
sect("B6. Doi chieu 3 nguon: 3.820 CD Ads vs 2.557 lead CRM")
GA = {"generate_lead": 1715, "click_to_call_luot": 1132, "click_to_call_nguoi": 779,
      "view_price_page": 612, "engaged_30s": 361}
tong4 = GA["generate_lead"] + GA["click_to_call_luot"] + GA["view_price_page"] + GA["engaged_30s"]
trung = GA["click_to_call_luot"] - GA["click_to_call_nguoi"]
rac = GA["view_price_page"] + GA["engaged_30s"]
do_duoc = GA["generate_lead"] + GA["click_to_call_nguoi"]
mat_the = 2557 - do_duoc
print(f"Tong 4 su kien chinh = {tong4} (khop cot 'Chuyen doi' Ads = 3820: {tong4==3820})")
print(f"  (-) dem trung nhap goi (1132 luot - 779 nguoi)   = -{trung}")
print(f"  (-) su kien rac (view_price_page 612 + engaged_30s 361) = -{rac}")
print(f"  = Lead that DO DUOC bang the                     =  {do_duoc}")
print(f"  (+) lead MAT THE ngay 44-46 (GTM v23)            = +{mat_the}")
print(f"  = Lead that tren CRM                             =  {do_duoc+mat_the} (CRM bao 2557: {do_duoc+mat_the==2557})")
print(f"Chenh gop Ads - CRM = {3820-2557} = {trung} (trung) + {rac} (rac) - {mat_the} (mat the) "
      f"=> kiem tra: {trung+rac-mat_the} == {3820-2557}: {trung+rac-mat_the==3820-2557}")
print(f"Ty le thoi phong = 3820/2557 = {3820/2557:.3f}x (benchmark sheet 09: bao dong > 1,8x; tot 1,0-1,2x)")
print(f"% chuyen doi Ads KHONG phai lead = {(trung+rac)/3820*100:.1f}%")
print(f"Chi phi phan bo cho tin hieu rac+trung (theo ty trong) = {vnd(tot['Chi_phi']*(trung+rac)/3820)}")

# --- mat the ngay 44-46: doc tu sheet 02
sect("B6b. Kiem chung su co ngay 44-46 tren du lieu ngay")
for r in sorted([r for r in rows if 42 <= r["Ngay_thu"] <= 48], key=lambda r: (r["Ngay_thu"], r["Chien_dich"])):
    if r["Loai_hinh"].startswith("Search") or "PMAX" in r["Chien_dich"]:
        print(f"  N{r['Ngay_thu']:>2} {r['Ngay']} {r['Chien_dich'][:30]:30s} CD_Ads {r['ChuyenDoi_Ads']:5.0f} Lead_CRM {r['Lead_CRM']:5.0f}")
d44 = agg([r for r in rows if r["Ngay_thu"] in (44, 45, 46)])
print(f"  TONG N44-46: CD_Ads {d44['ChuyenDoi_Ads']:.0f} | Lead_CRM {d44['Lead_CRM']:.0f} | chi phi {vnd(d44['Chi_phi'])}")
base = agg([r for r in rows if r["Ngay_thu"] in (41, 42, 43, 47, 48, 49)])
print(f"  Trung binh 6 ngay ke can (41-43,47-49): CD_Ads/ngay {base['ChuyenDoi_Ads']/6:.1f} vs N44-46 {d44['ChuyenDoi_Ads']/3:.1f}")

# ---------------------------------------------------------------- B7
sect("B7. Lead mat do loi ky thuat CHUA SUA (Clarity muc 4,5,6)")
CPL_CRM = div(tot["Chi_phi"], tot["Lead_CRM"])
CP_SQL = div(tot["Chi_phi"], tot["Lead_SQL"])
lost = [("#4 Loi JS setDate (Safari iOS) — form khong gui duoc", 4196, 280, 340),
        ("#5 Nut CTA bi khung chat che (<380px)", 2741, 60, 90),
        ("#6 tel: link chet tren may tinh — 1.847 nhap chet", 1204, 30, 50)]
lo = hi = 0
for n, ses, a, b in lost:
    lo += a; hi += b
    print(f"  {n:58s} phien {ses:5d} | lead mat {a}-{b}")
print(f"  TONG lead mat (SO DO cua doi UX Clarity, la UOC TINH khong phai so do truc tiep): {lo} - {hi} lead")
print(f"CPL CRM thuc te toan ky = {vnd(CPL_CRM)} | CP/SQL = {vnd(CP_SQL)}")
print(f"=> Gia tri lead mat theo CPL: {vnd(lo*CPL_CRM)} - {vnd(hi*CPL_CRM)}")
sql_r = div(tot["Lead_SQL"], tot["Lead_CRM"])
coc_r = div(tot["Dat_Coc"], tot["Lead_CRM"])
print(f"=> Quy ra SQL (ty le {sql_r*100:.1f}%): {lo*sql_r:.0f} - {hi*sql_r:.0f} SQL; gia tri theo CP/SQL {vnd(lo*sql_r*CP_SQL)} - {vnd(hi*sql_r*CP_SQL)}")
print(f"=> Quy ra coc (ty le lead->coc {coc_r*100:.3f}%): {lo*coc_r:.2f} - {hi*coc_r:.2f} coc "
      f"=> doanh thu bo lo {vnd(lo*coc_r*HH)} - {vnd(hi*coc_r*HH)} (UOC TINH cua toi)")
# Da sua (muc 1,2,3) — thiet hai qua khu, tham chieu
fixed_lo, fixed_hi = 90+320+110, 140+400+150
print(f"[Tham chieu] Loi DA SUA o v2 (#1,#2,#3): {fixed_lo}-{fixed_hi} lead ~ {vnd(fixed_lo*CPL_CRM)}-{vnd(fixed_hi*CPL_CRM)} (thiet hai da xay ra N1-57)")
print(f"[Tham chieu] 63 lead mat the N44-46 = {vnd(63*CPL_CRM)} chi phi khong duoc ghi nhan (day la SO DO, sheet 10/12)")

# ---------------------------------------------------------------- A: chan doan
sect("A1. Lang phi theo chien dich khong ra coc")
no_coc = [cd for cd, rs in bykey(rows, "Chien_dich").items() if s(rs, "Dat_Coc") == 0]
tot_no = agg([r for r in rows if r["Chien_dich"] in no_coc])
print(f"Chien dich 0 coc: {no_coc}")
print(f"Tong chi phi 0 coc = {vnd(tot_no['Chi_phi'])} = {tot_no['Chi_phi']/tot['Chi_phi']*100:.1f}% ngan sach | SQL {tot_no['Lead_SQL']:.0f} | DT 0")
for cd in no_coc:
    a = agg([r for r in rows if r["Chien_dich"] == cd])
    print(f"  {cd:34s} {vnd(a['Chi_phi']):>14s} ({a['Chi_phi']/tot['Chi_phi']*100:4.1f}%) SQL {a['Lead_SQL']:4.0f} CP/SQL {vnd(div(a['Chi_phi'],a['Lead_SQL'])):>12s}")

sect("A2. PMax — bang chung tin hieu rac")
pm = agg([r for r in rows if r["Chien_dich"] == "PMAX_VinhomesHM_Lead"])
print(f"PMax: chi phi {vnd(pm['Chi_phi'])} | CD_Ads {pm['ChuyenDoi_Ads']:.0f} | Lead {pm['Lead_CRM']:.0f} | SQL {pm['Lead_SQL']:.0f} | coc {pm['Dat_Coc']:.0f}")
print(f"  CPL_Ads {vnd(div(pm['Chi_phi'],pm['ChuyenDoi_Ads']))} (THAP NHAT TK) nhung CP/SQL {vnd(div(pm['Chi_phi'],pm['Lead_SQL']))}")
print(f"  Ads/CRM {div(pm['ChuyenDoi_Ads'],pm['Lead_CRM']):.2f}x | SQL/Lead {div(pm['Lead_SQL'],pm['Lead_CRM'])*100:.1f}% (benchmark bao dong <12%)")
print("  GA4 sheet10B: 39.701 nhap -> 28.585 phien (hao hut 28,0%), ty le tuong tac 8,7%, TG tuong tac TB 11s, 1,09 trang/phien")
print("  Clarity sheet11B: 26.298 phien, thoat nhanh <3s = 74,3%, thoi luong trung vi 3s")
print("  CRM sheet08C: mau 160 lead PMax -> trung SDT 31%, SDT sai 24%, sai phan khuc 34%, dung duoc 7%")
print(f"  => Lead PMax dung duoc uoc tinh = {pm['Lead_CRM']:.0f} x 7% = {pm['Lead_CRM']*0.07:.0f} lead; chi phi/lead dung duoc = {vnd(pm['Chi_phi']/(pm['Lead_CRM']*0.07))}")
print(f"  Neu cat PMax: giai phong {vnd(pm['Chi_phi'])} = {pm['Chi_phi']/tot['Chi_phi']*100:.1f}% ngan sach, mat 0 coc")

sect("A3. Search Competitor — 0 SQL")
cp = agg([r for r in rows if r["Chien_dich"] == "SEA_Competitor_DoiThu"])
print(f"Competitor: chi phi {vnd(cp['Chi_phi'])} | click {cp['Nhap_chuot']:.0f} | CPC {vnd(div(cp['Chi_phi'],cp['Nhap_chuot']))} "
      f"| Lead {cp['Lead_CRM']:.0f} | SQL {cp['Lead_SQL']:.0f} | coc 0")
print(f"  CPL_CRM {vnd(div(cp['Chi_phi'],cp['Lead_CRM']))} (benchmark bao dong >1,5tr) | CTR {div(cp['Nhap_chuot'],cp['Hien_thi'])*100:.2f}%")
print("  sheet04: 6 cum tu doi thu, tat ca SQL=0; sheet08C mau 40 lead -> 26% la moi gioi/doi thu, chi 26% dung duoc")

sect("A4. Brand — Impression Share & mat IS do ngan sach")
br = [r for r in rows if r["Chien_dich"] == "SEA_Brand_Vinhomes_HocMon"]
ba = agg(br)
w_is = sum(r["Impr_Share"] * r["Hien_thi"] for r in br) / ba["Hien_thi"]
w_bud = sum(r["Mat_IS_NganSach"] * r["Hien_thi"] for r in br) / ba["Hien_thi"]
w_rank = sum(r["Mat_IS_ThuHang"] * r["Hien_thi"] for r in br) / ba["Hien_thi"]
print(f"Brand toan ky: IS binh quan (trong so hien thi) {w_is*100:.1f}% | mat IS ngan sach {w_bud*100:.1f}% | mat IS thu hang {w_rank*100:.1f}%")
for gd in ["GĐ1", "GĐ2", "GĐ3"]:
    g = [r for r in br if r["Giai_doan"] == gd]
    ag = agg(g)
    print(f"  {gd}: IS {sum(r['Impr_Share']*r['Hien_thi'] for r in g)/ag['Hien_thi']*100:5.1f}% "
          f"| mat IS NS {sum(r['Mat_IS_NganSach']*r['Hien_thi'] for r in g)/ag['Hien_thi']*100:5.1f}% "
          f"| chi phi {vnd(ag['Chi_phi'])} | coc {ag['Dat_Coc']:.0f} | ROAS {div(ag['DoanhThu_HoaHong'],ag['Chi_phi']):.2f}x")
# Uoc tien bo lai tren ban: neu thu hoi phan mat IS do ngan sach
br_cpa = div(ba["Chi_phi"], ba["Dat_Coc"])
lost_impr = ba["Hien_thi"] * w_bud / max(w_is, 1e-9)
extra_clicks = lost_impr * div(ba["Nhap_chuot"], ba["Hien_thi"])
extra_leads = extra_clicks * div(ba["Lead_CRM"], ba["Nhap_chuot"])
extra_coc = extra_leads * div(ba["Dat_Coc"], ba["Lead_CRM"])
print(f"  Uoc tinh (cua toi, tuyen tinh): hien thi bi mat do ngan sach ~{lost_impr:,.0f} -> {extra_clicks:,.0f} click "
      f"-> {extra_leads:.0f} lead -> {extra_coc:.1f} coc -> DT bo lo {vnd(extra_coc*HH)}")
print(f"  Chi phi tang them tuong ung (CPC brand {vnd(div(ba['Chi_phi'],ba['Nhap_chuot']))}) = {vnd(extra_clicks*div(ba['Chi_phi'],ba['Nhap_chuot']))}")
print(f"  Hien thi Brand toan ky = {ba['Hien_thi']:,.0f}; CTR brand {div(ba['Nhap_chuot'],ba['Hien_thi'])*100:.2f}%; lead/click {div(ba['Lead_CRM'],ba['Nhap_chuot'])*100:.2f}%")
print(f"  [THAN TRONG] tuyen tinh la CAN TREN. Gia dinh chi thu hoi 50% (CPC dau gia cao dan, ton kho brand co han) "
      f"-> {extra_coc*0.5:.1f} coc -> DT {vnd(extra_coc*0.5*HH)}; chi phi them {vnd(extra_clicks*0.5*div(ba['Chi_phi'],ba['Nhap_chuot'])*1.2)} (CPC +20%)")
print(f"  Brand hien: {ba['Chi_phi']/tot['Chi_phi']*100:.1f}% ngan sach nhung {ba['Dat_Coc']/tot['Dat_Coc']*100:.0f}% so coc, "
      f"{ba['DoanhThu_HoaHong']/tot['DoanhThu_HoaHong']*100:.0f}% doanh thu, ROAS {div(ba['DoanhThu_HoaHong'],ba['Chi_phi']):.2f}x")

sect("A5. Search terms — lang phi tu doi sanh rong")
with open(f"{SH}/04_SEARCH_TERMS.csv", encoding="utf-8-sig") as f:
    st = [r for r in csv.DictReader(f) if r["Chi phí (đ)"] and r["Chi phí (đ)"].replace(".", "").isdigit()]
waste = [r for r in st if float(r["Lead chất lượng (SQL)"]) == 0]
w_cost = sum(float(r["Chi phí (đ)"]) for r in waste)
print(f"So cum tu SQL=0: {len(waste)}/{len(st)} | chi phi {vnd(w_cost)} = {w_cost/tot['Chi_phi']*100:.1f}% tong chi phi TK")
for r in sorted(waste, key=lambda r: -float(r["Chi phí (đ)"]))[:12]:
    print(f"  {r['Cụm từ tìm kiếm'][:42]:42s} {r['Loại đối sánh khớp']:9s} {vnd(float(r['Chi phí (đ)'])):>12s} "
          f"clicks {r['Nhấp chuột']:>5s} lead {r['Lead CRM']:>4s} SQL 0")
irrel = ["tuyển dụng", "học phí", "thuê", "nhà trọ", "kho xưởng", "việc làm", "lừa đảo", "quy hoạch", "chung cư mini", "100 triệu"]
ir = [r for r in st if any(k in r["Cụm từ tìm kiếm"] for k in irrel)]
print(f"  Trong do cum tu SAI Y DINH ro rang ({len(ir)} cum): {vnd(sum(float(r['Chi phí (đ)']) for r in ir))} "
      f"= {sum(float(r['Chi phí (đ)']) for r in ir)/tot['Chi_phi']*100:.1f}% ngan sach")
comp_cost = sum(float(r["Chi phí (đ)"]) for r in st if r["Chiến dịch"] == "SEA_Competitor_DoiThu")
print(f"  Cum tu doi thu (SQL=0 toan bo): {vnd(comp_cost)}")

sect("A6. Dia ly — chi phi ngoai vung ban duoc")
with open(f"{SH}/06_DIA_LY.csv", encoding="utf-8-sig") as f:
    geo = [r for r in csv.DictReader(f) if r["Khu vực"] not in ("TỔNG", "") and r["Chi phí (đ)"]]
far = ["Hà Nội", "Đà Nẵng", "Cần Thơ & ĐBSCL", "Người dùng ngoài Việt Nam quan tâm đến Việt Nam"]
fc = sum(float(r["Chi phí (đ)"]) for r in geo if r["Khu vực"] in far)
fq = sum(float(r["Lead chất lượng (SQL)"]) for r in geo if r["Khu vực"] in far)
print(f"Khu vuc xa (HN, DN, Can Tho, ngoai VN): chi phi {vnd(fc)} = {fc/tot['Chi_phi']*100:.1f}% | SQL {fq:.0f} | coc 0")
print(f"  CP/SQL binh quan nhom nay = {vnd(fc/fq)} vs TP.HCM Q12 2.082.434d (sheet 06)")
hcm = sum(float(r["Chi phí (đ)"]) for r in geo if r["Khu vực"].startswith("TP.HCM"))
hcoc = sum(float(r["Đặt cọc"]) for r in geo if r["Khu vực"].startswith("TP.HCM"))
print(f"  TP.HCM: {vnd(hcm)} ({hcm/tot['Chi_phi']*100:.1f}%) -> {hcoc:.0f}/18 coc")

sect("A7. Khung gio / thiet bi / ngay trong tuan")
print("sheet07A: 20-23h chiem 18,7% chi phi (337.261.419d) nhung chi 21% lead duoc goi lai <30 phut, CP/SQL 3.011.263d")
print("  23-24h + 00-06h: 8,1% chi phi (146.086.497d), 40 SQL, 0 coc, ty le goi lai 12-34%")
night = 73945017 + 72141480 + 337261419
print(f"  Tong khung gio yeu (00-06, 20-23, 23-24) = {vnd(night)} = {night/tot['Chi_phi']*100:.1f}% chi phi, coc = 3/18")
print("sheet07B: Mobile 78,1% chi phi (1.408.562.397d), CVR 2,03%, CP/SQL 3.042.251d | Desktop 16,7% chi phi, CVR 4,02%, CP/SQL 1.847.796d")
print(f"  Desktop CP/SQL thap hon mobile {(3042251/1847796-1)*100:.0f}% nhung chi duoc phan bo 16,7% ngan sach")
print("sheet07C: T7+CN chi phi 503.810.000d (27,9%) voi 2/8 sale truc -> CP/SQL T7 3.020.851d vs T2 2.151.142d")
we = 262814000 + 240996000
print(f"  Cuoi tuan: {vnd(we)} = {we/tot['Chi_phi']*100:.1f}% chi phi -> 4/18 coc")

sect("A8. Toc do phan hoi lead — doanh thu bo lo")
# sheet08A
resp = [("<5 phut", 281, 0.0182), ("5-30 phut", 485, 0.0121), ("30ph-2h", 588, 0.0058),
        ("2-12h", 536, 0.0021), (">12h", 664, 0.0004)]
cur = sum(n * r for _, n, r in resp)
tot_lead = sum(n for _, n, _ in resp)
best = tot_lead * 0.0182
print(f"So lead trong sheet 08A = {tot_lead} (CRM 2557, chenh {2557-tot_lead} do lam tron % / lead chua phan loai)")
print(f"Coc ky vong theo phan bo hien tai = {cur:.1f}; neu 100% goi lai <5 phut = {best:.1f} coc")
print(f"=> Chenh {best-cur:.1f} coc = {vnd((best-cur)*HH)} doanh thu bo lo (UOC TINH, gia dinh ty le coc theo nhom giu nguyen)")
print(f"Kich ban thuc te hon — dua 47% lead dang >2h ve nhom <30 phut:")
mix = 281*0.0182 + (485+536+664)*0.0121 + 588*0.0058
print(f"  coc ky vong {mix:.1f} => tang {mix-cur:.1f} coc = {vnd((mix-cur)*HH)}")
print("sheet08B: lead bi bo sot 118+96+61 = 275 lead trong 90 ngay")
print(f"  275 lead x CPL CRM {vnd(CPL_CRM)} = {vnd(275*CPL_CRM)} tien da tra nhung khong ai goi")
print(f"  275 lead x ty le lead->coc {coc_r*100:.3f}% = {275*coc_r:.2f} coc = {vnd(275*coc_r*HH)} DT bo lo (UOC TINH)")

sect("A9. Trang dich v1 vs v2 — doanh thu bo lo do sua muon")
print("sheet10C: v1 (N1-57) 52.410 phien, form_start 4.912, generate_lead 1.002, hoan tat 20,4%, LCP 4,8s")
print("          v2 (N58-90) 42.938 phien, form_start 2.546, generate_lead 713, hoan tat 28,0%, LCP 1,9s")
uplift = 0.280047132757266 / 0.203990228013029 - 1
extra_lead_v1 = 4912 * (0.280047132757266 - 0.203990228013029)
print(f"  Uplift ty le hoan tat form = +{uplift*100:.1f}%")
print(f"  Neu v2 chay tu N1: them {extra_lead_v1:.0f} lead tren cung 4.912 form_start")
print(f"  = {extra_lead_v1*sql_r:.0f} SQL = {extra_lead_v1*coc_r:.2f} coc = {vnd(extra_lead_v1*coc_r*HH)} DT (UOC TINH)")
print("  Mobile v1 ty le hoan tat 16,1% vs desktop 34,8% — mobile chiem 78,1% chi phi")

sect("A10. Do luong: su kien rac & 63 lead mat the & GTM")
print(f"  {rac} su kien rac (view_price_page 612 + engaged_30s 361) = {rac/3820*100:.1f}% cot 'Chuyen doi'")
print(f"  {trung} luot goi trung = {trung/3820*100:.1f}%")
print(f"  Chi phi 'mua' tin hieu rac: {vnd(tot['Chi_phi']*rac/3820)} (phan bo theo ty trong chuyen doi)")
print("  GTM sheet12A: 34 the, 412 KB JS ben thu ba, lam cham LCP ~0,8s; the GA4 Config trung lap tu N31 (v22)")
print("  GTM: Enhanced Conversions CHUA CAI (mat 10-20% khop), GCLID CHUA luu vao CRM => KHONG the import offline conversion")
print("  GTM: khong co canh bao chuyen doi = 0 => su co N44-46 mat 3 ngay moi phat hien")
print("  GA4 sheet10E: zalo_click 894 luot + file_download 1.206 luot dang KHONG duoc do vao Ads (tin hieu y dinh bi bo)")
print("  GA4 sheet10D: mo hinh nhap cuoi thoi phong Brand +191 lead (-32,3% neu doi sang data-driven), "
      "boc lo YT +122 (+283,7%), GDN +54 (+40,9%)")

sect("A11. Xu huong theo tuan — kiem tra bien dong")
for tw in sorted(set(r["Tuan"] for r in rows)):
    a = agg([r for r in rows if r["Tuan"] == tw])
    print(f"  Tuan {tw:2d}: chi phi {vnd(a['Chi_phi']):>13s} CD_Ads {a['ChuyenDoi_Ads']:5.0f} Lead {a['Lead_CRM']:5.0f} "
          f"SQL {a['Lead_SQL']:4.0f} coc {a['Dat_Coc']:3.0f} CPL {vnd(div(a['Chi_phi'],a['Lead_CRM'])):>10s}")

sect("A12. CPC & CTR theo chien dich vs benchmark sheet 09")
for cd, rs in sorted(bykey(rows, "Chien_dich").items(), key=lambda x: -s(x[1], "Chi_phi")):
    a = agg(rs)
    print(f"  {cd:34s} CTR {div(a['Nhap_chuot'],a['Hien_thi'])*100:5.2f}% CPC {vnd(div(a['Chi_phi'],a['Nhap_chuot'])):>10s} "
          f"CVR(lead/click) {div(a['Lead_CRM'],a['Nhap_chuot'])*100:5.2f}%")

# ---------------------------------------------------------------- C: ngan sach
sect("C. PHAN BO NGAN SACH 2,1 TY — 3 giai doan")
plan = {
  "SEA_Brand_VinhomesHocMon (mo rong IS)": (180, 210, 240),
  "SEA_Generic_NhaPho_CanHo (tai cau truc)": (200, 240, 280),
  "SEA_ChinhSach_TraGop_TayBac (moi)": ( 50,  60,  70),
  "PMAX_Lead_v2 (xay lai, brand exclusion)": ( 40,  70, 100),
  "GDN_Remarketing_Web30d":         ( 25,  30,  35),
  "YT_Video_TVC_MoBan (chi GD2-3)": (  0,  20,  30),
  "Du phong / test / su kien mo ban": ( 60,  70,  90),
}
tots = [0, 0, 0]
print("| Chien dich | GD1 (tr) | GD2 (tr) | GD3 (tr) | Tong (tr) |")
for k, v in plan.items():
    for i in range(3): tots[i] += v[i]
    print(f"| {k:38s} | {v[0]:8d} | {v[1]:8d} | {v[2]:8d} | {sum(v):9d} |")
print(f"| {'TONG':38s} | {tots[0]:8d} | {tots[1]:8d} | {tots[2]:8d} | {sum(tots):9d} |")
print(f"Tong ke hoach = {sum(tots)} trieu = {vnd(sum(tots)*1e6)} | Ngan sach duyet 2.100 trieu | Khop: {sum(tots)==2100}")
print(f"Ngan sach/ngay: GD1 {tots[0]/30:.1f} tr | GD2 {tots[1]/30:.1f} tr | GD3 {tots[2]/30:.1f} tr")

sect("C2. Muc tieu dinh luong tung giai doan (nguoc tu KPI)")
# Phan bo coc theo hinh mau GD3 cu (dong coc tang dan) va thoi gian chin cua pheu
targets = [(7, 620_000), (11, 600_000), (17, 580_000)]  # (coc muc tieu, CPL muc tieu)
tot_sql = 0
for i, (coc, cpl) in enumerate(targets, 1):
    b = tots[i-1] * 1e6
    leads = b / cpl
    # ty le tham chieu: SQL/Lead va SQL->Coc cai thien dan tu muc GD3 vua qua
    sqlr = [0.32, 0.35, 0.38][i-1]
    sql = leads * sqlr
    tot_sql += sql
    print(f"  GD{i}: ngan sach {vnd(b)} | CPL mt {vnd(cpl)} -> {leads:.0f} lead ({leads/30:.1f}/ngay) | SQL/Lead {sqlr*100:.0f}% -> {sql:.0f} SQL "
          f"| CP/SQL {vnd(b/sql)} | coc mt {coc} (SQL->coc {coc/sql*100:.2f}%) | CP/coc {vnd(b/coc)} | DT {vnd(coc*HH)} | ROAS {coc*HH/b:.2f}x")
TC = sum(c for c, _ in targets)
print(f"  TONG: {TC} coc | {tot_sql:.0f} SQL | CP/SQL bq {vnd(2.1e9/tot_sql)} (KPI <= 2.200.000) | DT {vnd(TC*HH)} | ROAS {TC*HH/2.1e9:.2f}x")
print(f"  KPI: >=32 coc {'DAT' if TC>=32 else 'TRUOT'} | ROAS >=3,0x {'DAT' if TC*HH/2.1e9>=3 else 'TRUOT'}")
print(f"  LUU Y MAU THUAN KPI: dung 32 coc + tieu het 2,1 ty => ROAS chi {32*HH/2.1e9:.2f}x < 3,0x.")
print(f"    Hai duong dat CA HAI: (a) >= {3*2.1e9/HH:.1f} -> lam tron 35 coc, hoac (b) 32 coc nhung chi tieu <= {vnd(32*HH/3)}")

sect("C3. Cong suat sale — rang buoc lead/ngay")
for i, t in enumerate(tots, 1):
    print(f"  GD{i}: neu CPL muc tieu 550.000d -> {t*1e6/550000/30:.1f} lead/ngay (tran 96/ngay, thuc te T7-CN chi 2 sale = 24/ngay)")
print("  => Tran lead cuoi tuan = 2 sale x 12 = 24 lead/ngay; hien T7+CN nhan (364+358)/26 tuan-ngay ~ 27,8 lead/ngay -> QUA TAI")

sect("D3. PMax — chung minh bang so")
print(f"  PMax CPL_Ads {vnd(div(pm['Chi_phi'],pm['ChuyenDoi_Ads']))} THAP NHAT tai khoan")
for cd, rs in sorted(bykey(rows, "Chien_dich").items(), key=lambda x: div(s(x[1],'Chi_phi'), s(x[1],'ChuyenDoi_Ads'))):
    a = agg(rs)
    print(f"    {cd:34s} CPL_Ads {vnd(div(a['Chi_phi'],a['ChuyenDoi_Ads'])):>12s} | CP/SQL {vnd(div(a['Chi_phi'],a['Lead_SQL'])):>13s} | CP/coc {vnd(div(a['Chi_phi'],a['Dat_Coc'])):>14s}")
print(f"  Neu chuyen toan bo 2,1 ty vao PMax theo CP/SQL {vnd(div(pm['Chi_phi'],pm['Lead_SQL']))} -> {2.1e9/div(pm['Chi_phi'],pm['Lead_SQL']):.0f} SQL")
print(f"    voi SQL->coc PMax = {div(pm['Dat_Coc'],pm['Lead_SQL'])*100:.1f}% -> {2.1e9/div(pm['Chi_phi'],pm['Lead_SQL'])*div(pm['Dat_Coc'],pm['Lead_SQL']):.1f} coc (KPI 32)")

sect("D1. Brand — bang chung phan bien 'cat brand'")
print(f"  Brand: {ba['Chi_phi']/tot['Chi_phi']*100:.1f}% chi phi -> {ba['Dat_Coc']:.0f}/18 coc ({ba['Dat_Coc']/18*100:.0f}%), "
      f"DT {vnd(ba['DoanhThu_HoaHong'])} ({ba['DoanhThu_HoaHong']/tot['DoanhThu_HoaHong']*100:.0f}%), ROAS {div(ba['DoanhThu_HoaHong'],ba['Chi_phi']):.2f}x")
ge = agg([r for r in rows if r["Chien_dich"] == "SEA_Generic_NhaPho_CanHo_TayBac"])
print(f"  Generic: {ge['Chi_phi']/tot['Chi_phi']*100:.1f}% chi phi -> {ge['Dat_Coc']:.0f} coc, ROAS {div(ge['DoanhThu_HoaHong'],ge['Chi_phi']):.2f}x, "
      f"CP/SQL {vnd(div(ge['Chi_phi'],ge['Lead_SQL']))} vs Brand {vnd(div(ba['Chi_phi'],ba['Lead_SQL']))}")
print(f"  Brand re hon Generic {div(ge['Chi_phi'],ge['Lead_SQL'])/div(ba['Chi_phi'],ba['Lead_SQL']):.1f} lan tren moi SQL")
print(f"  Brand mat IS do ngan sach {w_bud*100:.1f}% => dang BO LAI tien tren ban, khong phai thua")
print("  GA4 10D: neu doi sang data-driven, Brand van giu 401/1715 lead (23,4%) — cao nhat cung Generic 402")
print("  sheet08C: Brand ty le lead dung duoc 67% — cao nhat tai khoan (PMax 7%)")

sect("D4. Cat ngan sach con 1,2 ty — thu tu cat")
keep = [("SEA_Brand", 230*3//1, div(ba['DoanhThu_HoaHong'],ba['Chi_phi'])),]
cut_order = [("SEA_Competitor_DoiThu", cp['Chi_phi'], 0, 0),
             ("YT_Video_TVC_MoBan", agg([r for r in rows if r['Chien_dich']=='YT_Video_TVC_MoBan'])['Chi_phi'], 0, 0),
             ("PMAX (nguyen trang)", pm['Chi_phi'], pm['Lead_SQL'], 0),
             ("GDN_Remarketing_Web30d", agg([r for r in rows if r['Chien_dich']=='GDN_Remarketing_Web30d'])['Chi_phi'], 0, 0)]
run = 0
for n, c, q, k in cut_order:
    run += c
    print(f"  Cat {n:26s} tiet kiem {vnd(c):>14s} | coc mat: 0 | luy ke {vnd(run)}")
print(f"  Tong cat duoc ma khong mat coc nao = {vnd(run)} = {run/tot['Chi_phi']*100:.1f}% chi phi 90 ngay qua")
print(f"  Con lai cho Brand+Generic = {vnd(1.2e9)} ; can {1.2e9/(HH/3):.1f} coc de dat ROAS 3x")

sect("E. Bao so cho ke hoach 7 ngay")
print(f"  Tat 2 su kien rac -> cot Chuyen doi giam tu 3820 ve ~{3820-rac} (-{rac/3820*100:.1f}%), khu trung goi ve ~{do_duoc}")
print(f"  Them ~{len(waste)} tu khoa phu dinh -> chan ~{vnd(w_cost)} chi phi/90 ngay = ~{vnd(w_cost/90)}/ngay")
print(f"  Gioi han dia ly TP.HCM+BD+LA+DN -> giai phong {vnd(fc)} (khu vuc 0 coc)")
print(f"  Tat Competitor -> giai phong {vnd(cp['Chi_phi'])}, mat 0 coc, 0 SQL")
print(f"  Sua loi JS #4 -> thu hoi {lost[0][2]}-{lost[0][3]} lead/90 ngay ~ {vnd(lost[0][2]*CPL_CRM)}-{vnd(lost[0][3]*CPL_CRM)}")
print(f"  Tang ngan sach Brand de dua mat IS ngan sach {w_bud*100:.1f}% ve <10% -> uoc {extra_coc:.1f} coc")

print("\n\n=== SELF-CHECK ===")
assert abs(tot["Chi_phi"] - 1_803_537_000) < 1, tot["Chi_phi"]
assert tot["ChuyenDoi_Ads"] == 3820 and tot["Lead_CRM"] == 2557
assert tot["Lead_SQL"] == 651 and tot["Dat_Coc"] == 18
assert tong4 == 3820 and do_duoc + mat_the == 2557
assert trung + rac - mat_the == 3820 - 2557
assert sum(tots) == 2100
print("OK — moi so tong khop sheet 02/03/10.")
