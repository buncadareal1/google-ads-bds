import csv
from collections import defaultdict
rows = list(csv.DictReader(open('/home/docdang/Downloads/du_lieu_google_ads_90_ngay_1.csv', encoding='utf-8-sig')))
def f(r,k):
    v=r[k].strip(); return float(v) if v else 0.0
tot=defaultdict(float); by_cd=defaultdict(lambda:defaultdict(float)); by_gd=defaultdict(lambda:defaultdict(float))
KEYS=['Hien_thi','Nhap_chuot','Chi_phi','ChuyenDoi_Ads','Lead_CRM','Lead_SQL','Di_Xem_Nha','Booking','Dat_Coc','DoanhThu_HoaHong']
for r in rows:
    for k in KEYS:
        v=f(r,k); tot[k]+=v; by_cd[r['Chien_dich']][k]+=v; by_gd[r['Giai_doan']][k]+=v
print("rows:",len(rows))
print("== TOTAL =="); [print(k,f"{tot[k]:,.0f}") for k in KEYS]
print(f"CPL_Ads {tot['Chi_phi']/tot['ChuyenDoi_Ads']:,.0f} | CPL_CRM {tot['Chi_phi']/tot['Lead_CRM']:,.0f} | CP_SQL {tot['Chi_phi']/tot['Lead_SQL']:,.0f} | CP_Coc {tot['Chi_phi']/tot['Dat_Coc']:,.0f} | ROAS {tot['DoanhThu_HoaHong']/tot['Chi_phi']:.3f}")
print(f"Funnel L>S {tot['Lead_SQL']/tot['Lead_CRM']:.4f} S>X {tot['Di_Xem_Nha']/tot['Lead_SQL']:.4f} X>B {tot['Booking']/tot['Di_Xem_Nha']:.4f} B>C {tot['Dat_Coc']/tot['Booking']:.4f}")
print("== BY CAMPAIGN ==")
for cd,d in sorted(by_cd.items()):
    print(f"{cd}: chi {d['Chi_phi']/1e6:,.1f}tr convAds {d['ChuyenDoi_Ads']:.0f} leadCRM {d['Lead_CRM']:.0f} SQL {d['Lead_SQL']:.0f} coc {d['Dat_Coc']:.0f} DT {d['DoanhThu_HoaHong']/1e6:,.0f}tr CPLa {d['Chi_phi']/d['ChuyenDoi_Ads'] if d['ChuyenDoi_Ads'] else 0:,.0f} CPLc {d['Chi_phi']/d['Lead_CRM'] if d['Lead_CRM'] else 0:,.0f} CPSQL {d['Chi_phi']/d['Lead_SQL'] if d['Lead_SQL'] else 0:,.0f} ROAS {d['DoanhThu_HoaHong']/d['Chi_phi']:.2f}")
print("== BY PHASE ==")
for gd,d in sorted(by_gd.items()):
    print(f"{gd}: chi {d['Chi_phi']/1e6:,.1f}tr leadCRM {d['Lead_CRM']:.0f} SQL {d['Lead_SQL']:.0f} coc {d['Dat_Coc']:.0f} ROAS {d['DoanhThu_HoaHong']/d['Chi_phi']:.2f} CPSQL {d['Chi_phi']/d['Lead_SQL'] if d['Lead_SQL'] else 0:,.0f}")
print(f"B5 max chi/coc @ROAS3: {181e6/3:,.0f}")
print(f"B6 gap: {tot['ChuyenDoi_Ads']-tot['Lead_CRM']:.0f} (973 junk + 353 dup - 63 tag loss = 1263)")
