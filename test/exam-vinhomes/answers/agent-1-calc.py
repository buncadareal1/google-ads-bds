#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Toan bo phep tinh cho bai lam agent-1.md.
Nguon: /home/docdang/Downloads/du_lieu_google_ads_90_ngay_1.csv (= sheet 02)
       + sheets/04,05,06,07,08,09,10,11,12 (doc thu cong, hang so ghi ro nguon).
Chay: python3 agent-1-calc.py
"""
import csv, os
from collections import defaultdict

CSV = '/home/docdang/Downloads/du_lieu_google_ads_90_ngay_1.csv'
SH = '/home/docdang/Projects/google-ads/test/exam-vinhomes/sheets'
M = 1_000_000

rows = []
for r in csv.DictReader(open(CSV, encoding='utf-8-sig')):
    for k in ('Hien_thi','Nhap_chuot','Chi_phi','ChuyenDoi_Ads','Lead_CRM','Lead_SQL',
              'Di_Xem_Nha','Booking','Dat_Coc','DoanhThu_HoaHong','Ngay_thu','Tuan'):
        r[k] = float(r[k]) if r[k] not in ('', None) else 0.0
    for k in ('Impr_Share','Mat_IS_NganSach','Mat_IS_ThuHang'):
        r[k] = float(r[k]) if r[k] not in ('', None) else None
    rows.append(r)

NUM = ('Hien_thi','Nhap_chuot','Chi_phi','ChuyenDoi_Ads','Lead_CRM','Lead_SQL',
       'Di_Xem_Nha','Booking','Dat_Coc','DoanhThu_HoaHong')

def agg(rs):
    d = {k: sum(r[k] for r in rs) for k in NUM}
    return d

def div(a, b):
    return a / b if b else float('nan')

def out(title):
    print('\n' + '=' * 78); print(title); print('=' * 78)

TOT = agg(rows)
assert len(rows) == 486, len(rows)

# ---------------------------------------------------------------- B1
out('B1. CPL Ads / CPL CRM / CP-SQL / CP-coc  — toan ky va tung chien dich')
hdr = f"{'Chien dich':38s} {'ChiPhi(tr)':>10s} {'CD_Ads':>7s} {'Lead':>6s} {'SQL':>5s} {'Coc':>4s} {'CPL_Ads':>9s} {'CPL_CRM':>9s} {'CP/SQL':>9s} {'CP/coc':>10s}"
print(hdr)
camps = sorted({r['Chien_dich'] for r in rows})
per_camp = {}
for c in camps:
    d = agg([r for r in rows if r['Chien_dich'] == c]); per_camp[c] = d
    print(f"{c:38s} {d['Chi_phi']/M:10.1f} {d['ChuyenDoi_Ads']:7.0f} {d['Lead_CRM']:6.0f} "
          f"{d['Lead_SQL']:5.0f} {d['Dat_Coc']:4.0f} {div(d['Chi_phi'],d['ChuyenDoi_Ads'])/1000:9.0f}k "
          f"{div(d['Chi_phi'],d['Lead_CRM'])/1000:8.0f}k {div(d['Chi_phi'],d['Lead_SQL'])/M:8.2f}tr "
          f"{div(d['Chi_phi'],d['Dat_Coc'])/M:9.1f}tr")
print(f"{'TOAN KY':38s} {TOT['Chi_phi']/M:10.1f} {TOT['ChuyenDoi_Ads']:7.0f} {TOT['Lead_CRM']:6.0f} "
      f"{TOT['Lead_SQL']:5.0f} {TOT['Dat_Coc']:4.0f} {div(TOT['Chi_phi'],TOT['ChuyenDoi_Ads'])/1000:9.0f}k "
      f"{div(TOT['Chi_phi'],TOT['Lead_CRM'])/1000:8.0f}k {div(TOT['Chi_phi'],TOT['Lead_SQL'])/M:8.2f}tr "
      f"{div(TOT['Chi_phi'],TOT['Dat_Coc'])/M:9.1f}tr")
print(f"CTR toan ky = {div(TOT['Nhap_chuot'],TOT['Hien_thi'])*100:.2f}% | CPC TB = {div(TOT['Chi_phi'],TOT['Nhap_chuot']):,.0f}d")
for c in camps:
    d = per_camp[c]
    print(f"  {c:38s} CTR={div(d['Nhap_chuot'],d['Hien_thi'])*100:5.2f}%  CPC={div(d['Chi_phi'],d['Nhap_chuot']):>9,.0f}d  "
          f"%chi phi={d['Chi_phi']/TOT['Chi_phi']*100:5.1f}%  SQL/Lead={div(d['Lead_SQL'],d['Lead_CRM'])*100:5.1f}%  "
          f"Ads/CRM={div(d['ChuyenDoi_Ads'],d['Lead_CRM']):.2f}x")

# ---------------------------------------------------------------- B2
out('B2. ROAS toan ky va tung giai doan')
print(f"{'GD':6s} {'ChiPhi(tr)':>11s} {'DoanhThu(tr)':>13s} {'Coc':>4s} {'ROAS':>6s} {'CP/coc(tr)':>11s} {'Lead':>6s} {'SQL':>5s}")
for g in ('GĐ1', 'GĐ2', 'GĐ3'):
    d = agg([r for r in rows if r['Giai_doan'] == g])
    print(f"{g:6s} {d['Chi_phi']/M:11.1f} {d['DoanhThu_HoaHong']/M:13.1f} {d['Dat_Coc']:4.0f} "
          f"{div(d['DoanhThu_HoaHong'],d['Chi_phi']):6.2f} {div(d['Chi_phi'],d['Dat_Coc'])/M:11.1f} {d['Lead_CRM']:6.0f} {d['Lead_SQL']:5.0f}")
print(f"{'TONG':6s} {TOT['Chi_phi']/M:11.1f} {TOT['DoanhThu_HoaHong']/M:13.1f} {TOT['Dat_Coc']:4.0f} "
      f"{div(TOT['DoanhThu_HoaHong'],TOT['Chi_phi']):6.2f} {div(TOT['Chi_phi'],TOT['Dat_Coc'])/M:11.1f} {TOT['Lead_CRM']:6.0f} {TOT['Lead_SQL']:5.0f}")
print(f"HH TB/coc thuc te = {div(TOT['DoanhThu_HoaHong'],TOT['Dat_Coc'])/M:.1f} tr (de bai: 181tr)")
print('ROAS theo chien dich:')
for c in camps:
    d = per_camp[c]
    print(f"  {c:38s} ROAS={div(d['DoanhThu_HoaHong'],d['Chi_phi']):5.2f}  loi/lo={((d['DoanhThu_HoaHong']-d['Chi_phi'])/M):>8.1f}tr")

# ---------------------------------------------------------------- B3
out('B3. Ty le chuyen doi tung buoc pheu (toan ky + tung chien dich)')
def funnel(d, name):
    print(f"{name:38s} Lead={d['Lead_CRM']:.0f} SQL={d['Lead_SQL']:.0f} Xem={d['Di_Xem_Nha']:.0f} "
          f"Book={d['Booking']:.0f} Coc={d['Dat_Coc']:.0f} | "
          f"L→SQL={div(d['Lead_SQL'],d['Lead_CRM'])*100:5.1f}% SQL→Xem={div(d['Di_Xem_Nha'],d['Lead_SQL'])*100:5.1f}% "
          f"Xem→Book={div(d['Booking'],d['Di_Xem_Nha'])*100:5.1f}% Book→Coc={div(d['Dat_Coc'],d['Booking'])*100:5.1f}% "
          f"Xem→Coc={div(d['Dat_Coc'],d['Di_Xem_Nha'])*100:5.1f}% Lead→Coc={div(d['Dat_Coc'],d['Lead_CRM'])*100:5.2f}%")
funnel(TOT, 'TOAN KY')
for g in ('GĐ1','GĐ2','GĐ3'):
    funnel(agg([r for r in rows if r['Giai_doan'] == g]), g)
for c in camps:
    funnel(per_camp[c], c)
# pheu chi tren cac chien dich CO coc (Brand + Generic)
sea = agg([r for r in rows if r['Chien_dich'] in
           ('SEA_Brand_Vinhomes_HocMon','SEA_Generic_NhaPho_CanHo_TayBac')])
funnel(sea, 'CHI 2 CD SEARCH CO COC')

# ---------------------------------------------------------------- B4
out('B4. Nguoc tu KPI 32 coc / 2,1 ty')
BUDGET, TARGET_COC = 2_100 * M, 32
scen = {}
# KB (kich ban co so): giu nguyen ty le toan ky 90 ngay
r_l_sql = div(TOT['Lead_SQL'], TOT['Lead_CRM'])
r_sql_xem = div(TOT['Di_Xem_Nha'], TOT['Lead_SQL'])
r_xem_book = div(TOT['Booking'], TOT['Di_Xem_Nha'])
r_book_coc = div(TOT['Dat_Coc'], TOT['Booking'])
scen['KB1_toan ky 90d'] = (r_l_sql, r_sql_xem, r_xem_book, r_book_coc)
# KB2: chi lay GD3 (da co SLA 15p, LP v2, sat trang thai tuong lai)
g3 = agg([r for r in rows if r['Giai_doan'] == 'GĐ3'])
scen['KB2_GD3'] = (div(g3['Lead_SQL'],g3['Lead_CRM']), div(g3['Di_Xem_Nha'],g3['Lead_SQL']),
                   div(g3['Booking'],g3['Di_Xem_Nha']), div(g3['Dat_Coc'],g3['Booking']))
# KB3: chi 2 CD Search co coc, GD3 (tep se duoc tap trung vao day)
sea3 = agg([r for r in rows if r['Giai_doan']=='GĐ3' and r['Chien_dich'] in
            ('SEA_Brand_Vinhomes_HocMon','SEA_Generic_NhaPho_CanHo_TayBac')])
scen['KB3_Search GD3'] = (div(sea3['Lead_SQL'],sea3['Lead_CRM']), div(sea3['Di_Xem_Nha'],sea3['Lead_SQL']),
                          div(sea3['Booking'],sea3['Di_Xem_Nha']), div(sea3['Dat_Coc'],sea3['Booking']))
print(f"{'Kich ban':18s} {'L→SQL':>7s} {'SQL→Xem':>8s} {'Xem→Book':>9s} {'Book→Coc':>9s} {'SQL can':>8s} {'Lead can':>9s} {'CP/SQL max':>11s} {'CPL max':>9s}")
for k, (a,b,c_,d_) in scen.items():
    booking_need = TARGET_COC / d_ if d_ else float('nan')
    xem_need = booking_need / c_ if c_ else float('nan')
    sql_need = xem_need / b if b else float('nan')
    lead_need = sql_need / a if a else float('nan')
    print(f"{k:18s} {a*100:6.1f}% {b*100:7.1f}% {c_*100:8.1f}% {d_*100:8.1f}% {sql_need:8.0f} {lead_need:9.0f} "
          f"{BUDGET/sql_need/M:10.2f}tr {BUDGET/lead_need/M:8.2f}tr")
    scen[k] = (a,b,c_,d_,sql_need,lead_need)
# rang buoc nang luc sale
print(f"Nang luc sale 90 ngay = 8 x 12 x 90 = {8*12*90} lead (sheet 08B). "
      f"Lead thuc te 90 ngay qua = {TOT['Lead_CRM']:.0f} = {TOT['Lead_CRM']/(8*12*90)*100:.1f}% cong suat.")
print(f"KPI CP/SQL cua BGD = 2,20tr → voi 2,1 ty mua duoc {BUDGET/(2.2*M):.0f} SQL")
for k in scen:
    sql_need = scen[k][4]
    print(f"  {k}: SQL can {sql_need:.0f} → CP/SQL toi da {BUDGET/sql_need/M:.2f}tr "
          f"({'DAT' if BUDGET/sql_need >= 2.2*M else 'CANG'} so voi tran 2,2tr)")

# ---------------------------------------------------------------- B5
out('B5. Diem hoa von')
HH = 181 * M
for roas in (1.0, 2.0, 3.0, 3.5):
    print(f"  ROAS {roas:.1f}x → chi phi QC toi da/coc = {HH/roas/M:7.2f} tr")
print(f"Thuc te 90 ngay qua: CP/coc = {div(TOT['Chi_phi'],TOT['Dat_Coc'])/M:.1f} tr → ROAS {div(TOT['DoanhThu_HoaHong'],TOT['Chi_phi']):.2f}x")
print(f"Voi 2,1 ty & ROAS 3,0x → doanh thu HH can = {BUDGET*3/M:.0f} tr = {BUDGET*3/HH:.1f} coc (KPI 32 coc → ROAS {32*HH/BUDGET:.2f}x)")
print(f"Bien do an toan: 32 coc x 181tr = {32*HH/M:.0f} tr; nguong hoa von ROAS 3,0 can {BUDGET*3/HH:.1f} coc")
print(f"Voi CP/coc toi da 60,33tr va 2,1 ty → toi da {BUDGET/(HH/3)/1:.1f} coc")

# ---------------------------------------------------------------- B6
out('B6. Doi chieu 3 nguon: 3.820 (Ads/GA4) vs 2.557 (CRM)')
# hang so tu sheet 10_GA4 muc A & E
GL, C2C_ev, C2C_user, VPP, E30 = 1715, 1132, 779, 612, 361
assert GL + C2C_ev + VPP + E30 == 3820
dup = C2C_ev - C2C_user           # dem trung lot goi
rac = VPP + E30                   # su kien rac (khong phai KHTN)
ga4_real = GL + C2C_user
mat_the = 63                      # lead N44-46, sheet 12 v23/v24
print(f"  3.820 = generate_lead {GL} + click_to_call(luot) {C2C_ev} + view_price_page {VPP} + engaged_30s {E30}")
print(f"  (-) dem trung click_to_call        = {dup:5d}  ({dup/3820*100:.1f}% tong CD)")
print(f"  (-) su kien rac (VPP + engaged)    = {rac:5d}  ({rac/3820*100:.1f}%)")
print(f"  = Lead THAT do duoc bang the       = {ga4_real:5d}   (kiem tra: {3820-dup-rac})")
print(f"  (+) lead mat the ngay 44-46        = {mat_the:5d}")
print(f"  = Lead CRM                         = {ga4_real+mat_the:5d}   (CRM bao {TOT['Lead_CRM']:.0f})")
assert 3820 - dup - rac == ga4_real == 2494 and ga4_real + mat_the == 2557
print(f"  Chenh tong 3.820 - 2.557 = {3820-2557} = {dup} trung + {rac} rac - {mat_the} mat the  "
      f"→ kiem tra {dup+rac-mat_the} ✔")
print(f"  Ty le thoi phong = {3820/2557:.2f}x (benchmark sheet 09: bao dong > 1,8x; toan ky 3 CD PMax = "
      f"{div(per_camp['PMAX_VinhomesHM_Lead']['ChuyenDoi_Ads'],per_camp['PMAX_VinhomesHM_Lead']['Lead_CRM']):.2f}x)")
# kiem chung ngay 44-46 tren sheet 02
z = [r for r in rows if 44 <= r['Ngay_thu'] <= 46]
print(f"  Kiem chung sheet 02, ngay 44-46: ChuyenDoi_Ads = {sum(r['ChuyenDoi_Ads'] for r in z):.0f}, "
      f"Lead_CRM = {sum(r['Lead_CRM'] for r in z):.0f}, chi phi = {sum(r['Chi_phi'] for r in z)/M:.1f} tr")
n43 = [r for r in rows if r['Ngay_thu'] == 43]; n47 = [r for r in rows if r['Ngay_thu'] == 47]
print(f"  Ngay 43: CD_Ads={sum(r['ChuyenDoi_Ads'] for r in n43):.0f} | Ngay 47: CD_Ads={sum(r['ChuyenDoi_Ads'] for r in n47):.0f}")
# tien chay mu 3 ngay
print(f"  → 3 ngay chay mu, chi phi {sum(r['Chi_phi'] for r in z)/M:.1f} tr, may hoc nhan tin hieu CD=0")

# ---------------------------------------------------------------- B7
out('B7. Lead mat do loi ky thuat CHUA SUA (sheet 11 muc C, loi #4,#5,#6)')
lo = 280+60+30; hi = 340+90+50
cpl_crm = div(TOT['Chi_phi'], TOT['Lead_CRM'])
cp_sql = div(TOT['Chi_phi'], TOT['Lead_SQL'])
print(f"  So DO (Clarity): phien anh huong #4={4196}, #5={2741}, #6={1204}; JS error rate mobile v1=9,3% v2=8,9%")
print(f"  UOC TINH (doi UX, sheet 11): {lo}–{hi} lead / 90 ngay")
print(f"  CPL CRM thuc te toan ky = {cpl_crm/1000:,.0f}k d  → gia tri lead mat = "
      f"{lo*cpl_crm/M:.0f} – {hi*cpl_crm/M:.0f} tr d")
sqlrate = div(TOT['Lead_SQL'], TOT['Lead_CRM'])
print(f"  Quy ve SQL (ty le SQL/lead toan ky {sqlrate*100:.1f}%): {lo*sqlrate:.0f}–{hi*sqlrate:.0f} SQL, "
      f"gia tri {lo*sqlrate*cp_sql/M:.0f}–{hi*sqlrate*cp_sql/M:.0f} tr theo CP/SQL {cp_sql/M:.2f}tr")
coc_rate = div(TOT['Dat_Coc'], TOT['Lead_CRM'])
print(f"  Quy ve coc (ty le Lead→Coc toan ky {coc_rate*100:.3f}%): {lo*coc_rate:.1f}–{hi*coc_rate:.1f} coc "
      f"→ doanh thu HH bo lo {lo*coc_rate*181:.0f}–{hi*coc_rate*181:.0f} tr")
print(f"  (loi #1,#2,#3 da sua o v2: uoc {90+320+110}–{140+400+150} lead — da mat, khong con chay mau)")

# ---------------------------------------------------------------- PHAN A: cac o lang phi
out('A. DINH LUONG CAC O LANG PHI')
# A1 PMax
p = per_camp['PMAX_VinhomesHM_Lead']
print(f"A-PMax : chi {p['Chi_phi']/M:.0f} tr ({p['Chi_phi']/TOT['Chi_phi']*100:.1f}%), lead {p['Lead_CRM']:.0f}, SQL {p['Lead_SQL']:.0f}, "
      f"coc {p['Dat_Coc']:.0f}, doanh thu {p['DoanhThu_HoaHong']/M:.0f} → CP/SQL {div(p['Chi_phi'],p['Lead_SQL'])/M:.2f}tr, ROAS 0")
print(f"         Clarity: thoat<3s 74,3%, phien trung vi 3s, SQL/lead {div(p['Lead_SQL'],p['Lead_CRM'])*100:.1f}% (benchmark bao dong <12%)")
print(f"         Lead dung duoc chi 7% (sheet 08C) → lang phi ≈ {p['Chi_phi']*0.93/M:.0f} tr")
# A2 Competitor
cp = per_camp['SEA_Competitor_DoiThu']
print(f"A-Comp : chi {cp['Chi_phi']/M:.0f} tr, lead {cp['Lead_CRM']:.0f}, SQL {cp['Lead_SQL']:.0f}, coc {cp['Dat_Coc']:.0f} → "
      f"CPL {div(cp['Chi_phi'],cp['Lead_CRM'])/M:.2f}tr, lang phi ≈ {cp['Chi_phi']/M:.0f} tr (0 coc, 3 SQL)")
# A3 Brand mat IS ngan sach
b = [r for r in rows if r['Chien_dich'] == 'SEA_Brand_Vinhomes_HocMon' and r['Mat_IS_NganSach'] is not None]
wIS = sum(r['Mat_IS_NganSach'] * r['Chi_phi'] for r in b) / sum(r['Chi_phi'] for r in b)
bd = per_camp['SEA_Brand_Vinhomes_HocMon']
isw = sum(r['Impr_Share'] * r['Hien_thi'] for r in b) / sum(r['Hien_thi'] for r in b)
print(f"A-Brand: IS TB (theo hien thi) = {isw*100:.1f}% (benchmark tot >85%), Mat IS ngan sach TB (theo chi phi) = {wIS*100:.1f}%")
# uoc luong lead/doanh thu bo lo neu bit het mat IS ngan sach
lost_share = wIS / max(isw, 1e-9)   # so lan hien thi bo lo / hien thi da co
extra_lead = bd['Lead_CRM'] * lost_share
extra_coc = bd['Dat_Coc'] * lost_share
extra_cost = bd['Chi_phi'] * lost_share
print(f"         Brand hien tai: chi {bd['Chi_phi']/M:.0f} tr, lead {bd['Lead_CRM']:.0f}, coc {bd['Dat_Coc']:.0f}, "
      f"doanh thu {bd['DoanhThu_HoaHong']/M:.0f} tr, ROAS {div(bd['DoanhThu_HoaHong'],bd['Chi_phi']):.2f}")
print(f"         Neu bit mat IS ngan sach: +{extra_lead:.0f} lead, +{extra_coc:.1f} coc, "
      f"+{extra_coc*181:.0f} tr HH, ton them ~{extra_cost/M:.0f} tr → ROAS bien {div(extra_coc*181*M,extra_cost):.1f}x")
# theo giai doan
for g in ('GĐ1','GĐ2','GĐ3'):
    bg = [r for r in rows if r['Chien_dich']=='SEA_Brand_Vinhomes_HocMon' and r['Giai_doan']==g]
    w = sum(r['Mat_IS_NganSach']*r['Chi_phi'] for r in bg)/sum(r['Chi_phi'] for r in bg)
    i = sum(r['Impr_Share']*r['Hien_thi'] for r in bg)/sum(r['Hien_thi'] for r in bg)
    print(f"         Brand {g}: IS {i*100:.1f}%, mat IS ngan sach {w*100:.1f}%, chi {sum(r['Chi_phi'] for r in bg)/M:.1f} tr")
# A4 Search terms rac (sheet 04)
st = list(csv.DictReader(open(os.path.join(SH,'04_SEARCH_TERMS.csv'), encoding='utf-8')))
st = [r for r in st if r.get('Chi phí (đ)')]
zero_sql = [r for r in st if float(r['Lead chất lượng (SQL)']) == 0]
print(f"A-Terms: {len(zero_sql)}/{len(st)} cum tu co 0 SQL, tong chi phi {sum(float(r['Chi phí (đ)']) for r in zero_sql)/M:.0f} tr "
      f"({sum(float(r['Chi phí (đ)']) for r in zero_sql)/TOT['Chi_phi']*100:.1f}% tong tai khoan)")
IRR = ['tuyển dụng','vinschool','thuê nhà','nhà trọ','kho xưởng','việc làm','lừa đảo','chung cư mini',
       'bản đồ quy hoạch','giá đất','bán đất thổ cư']
irr = [r for r in st if any(k in r['Cụm từ tìm kiếm'] for k in IRR)]
print(f"         Cum tu LAC HOAN TOAN ({len(irr)} cum): chi {sum(float(r['Chi phí (đ)']) for r in irr)/M:.0f} tr, "
      f"lead {sum(float(r['Lead CRM']) for r in irr):.0f}, SQL {sum(float(r['Lead chất lượng (SQL)']) for r in irr):.0f}")
for r in irr:
    print(f"           - {r['Cụm từ tìm kiếm']:36s} {float(r['Chi phí (đ)'])/M:6.1f} tr  SQL={r['Lead chất lượng (SQL)']}")
# A5 Dia ly (sheet 06)
geo = list(csv.DictReader(open(os.path.join(SH,'06_DIA_LY.csv'), encoding='utf-8')))
geo = [g for g in geo if g['Khu vực'] and g['Khu vực'] != 'TỔNG' and g['Chi phí (đ)']]
OUT = ['Hà Nội','Đà Nẵng','Cần Thơ & ĐBSCL','Người dùng ngoài Việt Nam quan tâm đến Việt Nam']
o = [g for g in geo if g['Khu vực'] in OUT]
print(f"A-Geo  : 4 khu vuc ngoai tep ({', '.join(OUT)}): chi {sum(float(g['Chi phí (đ)']) for g in o)/M:.0f} tr "
      f"({sum(float(g['% chi phí']) for g in o)*100:.1f}%), SQL {sum(float(g['Lead chất lượng (SQL)']) for g in o):.0f}, "
      f"coc {sum(float(g['Đặt cọc']) for g in o):.0f}")
core = [g for g in geo if g['Khu vực'].startswith('TP.HCM')]
print(f"         Loi TP.HCM: chi {sum(float(g['Chi phí (đ)']) for g in core)/M:.0f} tr, "
      f"SQL {sum(float(g['Lead chất lượng (SQL)']) for g in core):.0f}, coc {sum(float(g['Đặt cọc']) for g in core):.0f} "
      f"→ CP/SQL {sum(float(g['Chi phí (đ)']) for g in core)/sum(float(g['Lead chất lượng (SQL)']) for g in core)/M:.2f}tr")
# A6 Khung gio + thiet bi (sheet 07)
print(f"A-Time : 20:00-24:00 chiem 22,7% chi phi (0,187+0,04) = {(0.187+0.04)*TOT['Chi_phi']/M:.0f} tr, "
      f"goi lai <30p chi 21%/12% → 0 coc o 23-24h")
print(f"         00:00-06:00: chi {0.041*TOT['Chi_phi']/M:.0f} tr, 18 SQL, 0 coc, CP/SQL 4,11tr")
print(f"A-Dev  : Mobile 78,1% chi phi ({0.781*TOT['Chi_phi']/M:.0f} tr) CVR 2,03% vs Desktop CVR 4,02%; "
      f"CP/SQL mobile 3,04tr vs desktop 1,85tr")
print(f"A-Week : T7+CN chi {(262814000+240996000)/M:.0f} tr voi 2 sale truc; T3+T4 chi "
      f"{(259227000+260849000)/M:.0f} tr chi ra 2 coc (CP/SQL 3,12 & 3,30tr)")
# A7 Toc do phan hoi (sheet 08A)
crm = [('Duoi 5 phut',281,0.0182),('5-30 phut',485,0.0121),('30p-2h',588,0.0058),
       ('2-12h',536,0.0021),('>12h',664,0.0004)]
tot_lead = sum(x[1] for x in crm)
cur_coc = sum(x[1]*x[2] for x in crm)
best_coc = tot_lead * 0.0182
print(f"A-CRM  : {tot_lead} lead mau; coc ky vong hien tai = {cur_coc:.1f}; neu 100% goi <5p = {best_coc:.1f} "
      f"→ +{best_coc-cur_coc:.1f} coc = +{(best_coc-cur_coc)*181:.0f} tr HH (khong ton them dong quang cao nao)")
lost_leads = 118+96+61
print(f"         Lead bi bo sot (sheet 08B): {lost_leads} lead x CPL CRM {cpl_crm/1000:,.0f}k = "
      f"{lost_leads*cpl_crm/M:.0f} tr d bi vut")
cons = 281+485, 588, 536+664
# kich ban thuc te: dua nhom >2h ve nhom 30p-2h, nhom 30p-2h ve nhom 5-30p
cons_coc = (281)*0.0182 + (485+588)*0.0121 + (536+664)*0.0058
print(f"         KICH BAN THUC TE (dich moi nhom len 1 bac, khong can goi 100% duoi 5p): "
      f"coc ky vong {cons_coc:.1f} → +{cons_coc-cur_coc:.1f} coc = +{(cons_coc-cur_coc)*181:.0f} tr HH")
print(f"         47% lead duoc goi sau 2 gio (536+664)/{tot_lead}={(536+664)/tot_lead*100:.0f}%")
# A8 Landing page v1 vs v2
print(f"A-LP   : v1 (N1-57) hoan tat form 20,4%, LCP 4,8s | v2 (N58-90) 28,0%, LCP 1,9s (sheet 10C)")
v1_fs, v1_gl, v2_rate = 4912, 1002, 0.280047132757266
print(f"         Neu v1 co ty le v2: {v1_fs*v2_rate:.0f} lead thay vi {v1_gl} → mat {v1_fs*v2_rate-v1_gl:.0f} lead x "
      f"{cpl_crm/M:.2f}tr = {(v1_fs*v2_rate-v1_gl)*cpl_crm/M:.0f} tr; quy ra coc {(v1_fs*v2_rate-v1_gl)*coc_rate:.1f} = "
      f"{(v1_fs*v2_rate-v1_gl)*coc_rate*181:.0f} tr HH")
# A9 attribution
print(f"A-Attr : mo hinh nhap cuoi thoi Brand +191 lead (+32%), dim YouTube -122 (-74%), GDN -54, "
      f"bo qua 71 lead ngoai Ads (sheet 10D)")
# A10 hao hut nhap->phien
print(f"A-Click: PMax hao hut nhap→phien 28,0% (39.701 nhap → 28.585 phien), GDN 45,0%, Brand 9,0% (sheet 10B)")
print(f"         PMax: {39701-28585} nhap tra tien khong tao phien x CPC PMax "
      f"{div(p['Chi_phi'],p['Nhap_chuot']):,.0f}d = {(39701-28585)*div(p['Chi_phi'],p['Nhap_chuot'])/M:.0f} tr")

# ---------------------------------------------------------------- C: phan bo ngan sach
out('C. PHAN BO NGAN SACH 2,1 TY / 90 NGAY')
alloc = {
 'SEA_Brand_Vinhomes_HocMon':         (170, 190, 200),
 'SEA_Generic_NhaPho_CanHo_TayBac':   (250, 270, 280),
 'SEA_HighIntent_DiXemNha (moi)':     ( 50,  80,  90),
 'PMAX_VinhomesHM_Lead (tai cau truc)':( 60, 100, 120),
 'GDN_Remarketing_Web30d':            ( 35,  45,  50),
 'YT_Video_TVC_MoBan':                (  0,  20,  30),
 'Du phong / thu nghiem':             ( 20,  20,  20),
}
print(f"{'Chien dich':38s} {'GD1':>6s} {'GD2':>6s} {'GD3':>6s} {'Tong':>7s}")
tt = [0,0,0]
for k,(a,b_,c_) in alloc.items():
    tt = [tt[0]+a, tt[1]+b_, tt[2]+c_]
    print(f"{k:38s} {a:6d} {b_:6d} {c_:6d} {a+b_+c_:7d}")
print(f"{'TONG (trieu d)':38s} {tt[0]:6d} {tt[1]:6d} {tt[2]:6d} {sum(tt):7d}")
assert sum(tt) == 2100, sum(tt)
print(f"Ngan sach/ngay: GD1 {tt[0]/30:.1f} tr, GD2 {tt[1]/30:.1f} tr, GD3 {tt[2]/30:.1f} tr "
      f"(90 ngay qua TB {TOT['Chi_phi']/90/M:.1f} tr/ngay)")
# muc tieu tung GD theo kich ban KB3
a,b_,c_,d_,sqlN,leadN = scen['KB3_Search GD3']
print(f"KB3 dung lam co so ke hoach: L→SQL {a*100:.1f}%, SQL→Xem {b_*100:.1f}%, Xem→Book {c_*100:.1f}%, Book→Coc {d_*100:.1f}%")
print(f"  → can {sqlN:.0f} SQL, {leadN:.0f} lead tho, CP/SQL toi da {BUDGET/sqlN/M:.2f} tr, CPL toi da {BUDGET/leadN/M:.2f} tr")
split = [0.25, 0.33, 0.42]
for i,g in enumerate(('GD1','GD2','GD3')):
    print(f"  {g}: coc {32*split[i]:.1f}, SQL {sqlN*split[i]:.0f}, lead {leadN*split[i]:.0f}, "
          f"ngan sach {tt[i]} tr → CP/SQL {tt[i]/(sqlN*split[i]):.2f} tr")

# ---------------------------------------------------------------- D3 PMax
out('D3. PMax — CP/chuyen doi thap nhat nhung...')
for c in camps:
    d = per_camp[c]
    print(f"{c:38s} CP/CD_Ads={div(d['Chi_phi'],d['ChuyenDoi_Ads'])/1000:7.0f}k  "
          f"CP/Lead_CRM={div(d['Chi_phi'],d['Lead_CRM'])/1000:8.0f}k  CP/SQL={div(d['Chi_phi'],d['Lead_SQL'])/M:6.2f}tr  "
          f"CP/coc={div(d['Chi_phi'],d['Dat_Coc'])/M:8.1f}tr  ROAS={div(d['DoanhThu_HoaHong'],d['Chi_phi']):.2f}")

# ---------------------------------------------------------------- D4 cat con 1,2 ty
out('D4. Kich ban ngan sach 1,2 ty')
cut = {'SEA_Brand (giu cuoi cung)':(420,'bit het mat IS ngan sach'),
       'SEA_Generic (loi)':(430,'chi giu exact/phrase co SQL'),
       'SEA_HighIntent':(150,'moi'),'PMAX (tai cau truc)':(120,'chi sau khi sach tin hieu'),
       'GDN_Remarketing':(60,''),'YT_Video':(0,'cat het'),
       'SEA_Competitor':(0,'cat het'),'Du phong':(20,'')}
print(sum(v[0] for v in cut.values()), 'trieu')
assert sum(v[0] for v in cut.values()) == 1200
for k,(v,n) in cut.items(): print(f"  {k:22s} {v:5d} tr  {n}")
coc_12 = 1200*M / (BUDGET/sqlN) * (d_*c_*b_)  # SQL mua duoc x ty le tiep
print(f"  Voi CP/SQL muc tieu {BUDGET/sqlN/M:.2f}tr → {1200*M/(BUDGET/sqlN):.0f} SQL → {coc_12:.1f} coc "
      f"(ROAS {coc_12*HH/(1200*M):.2f}x)")

out('XONG')
