# -*- coding: utf-8 -*-
"""Bài thi Google Ads Vinhomes Hoc Mon - agent 8. Mọi số trong bài làm ra từ file này."""
import csv, collections, json, math

CSV = "/home/docdang/Downloads/du_lieu_google_ads_90_ngay_1.csv"
NUM = ["Hien_thi","Nhap_chuot","Chi_phi","Impr_Share","Mat_IS_NganSach","Mat_IS_ThuHang",
       "ChuyenDoi_Ads","Lead_CRM","Lead_SQL","Di_Xem_Nha","Booking","Dat_Coc","DoanhThu_HoaHong"]
rows=[]
with open(CSV, encoding="utf-8-sig") as f:
    for r in csv.DictReader(f):
        for k in NUM:
            r[k] = float(r[k]) if r[k] not in ("", None) else None
        rows.append(r)

def agg(rs, keys=NUM):
    d={k:0.0 for k in keys}
    for r in rs:
        for k in keys:
            if r[k] is not None: d[k]+=r[k]
    return d

def block(name, rs):
    a=agg(rs)
    o=dict(name=name, **{k:a[k] for k in ["Chi_phi","Nhap_chuot","Hien_thi","ChuyenDoi_Ads","Lead_CRM","Lead_SQL","Di_Xem_Nha","Booking","Dat_Coc","DoanhThu_HoaHong"]})
    div=lambda x,y: (x/y) if y else None
    o["CPC"]=div(a["Chi_phi"],a["Nhap_chuot"]); o["CTR"]=div(a["Nhap_chuot"],a["Hien_thi"])
    o["CPL_Ads"]=div(a["Chi_phi"],a["ChuyenDoi_Ads"]); o["CPL_CRM"]=div(a["Chi_phi"],a["Lead_CRM"])
    o["CP_SQL"]=div(a["Chi_phi"],a["Lead_SQL"]); o["CP_Coc"]=div(a["Chi_phi"],a["Dat_Coc"])
    o["ROAS"]=div(a["DoanhThu_HoaHong"],a["Chi_phi"])
    o["SQL_Lead"]=div(a["Lead_SQL"],a["Lead_CRM"]); o["Xem_SQL"]=div(a["Di_Xem_Nha"],a["Lead_SQL"])
    o["Book_Xem"]=div(a["Booking"],a["Di_Xem_Nha"]); o["Coc_Book"]=div(a["Dat_Coc"],a["Booking"])
    o["Coc_Xem"]=div(a["Dat_Coc"],a["Di_Xem_Nha"]); o["Ads_vs_CRM"]=div(a["ChuyenDoi_Ads"],a["Lead_CRM"])
    o["CVR_click"]=div(a["Lead_CRM"],a["Nhap_chuot"])
    return o

out={}
out["TOAN_KY"]=block("TOAN_KY", rows)
out["THEO_CD"]=[block(c,[r for r in rows if r["Chien_dich"]==c]) for c in sorted({r["Chien_dich"] for r in rows})]
out["THEO_GD"]=[block(g,[r for r in rows if r["Giai_doan"]==g]) for g in ["GĐ1","GĐ2","GĐ3"]]
out["CD_x_GD"]=[block(f"{c}|{g}",[r for r in rows if r["Chien_dich"]==c and r["Giai_doan"]==g])
                for c in sorted({r["Chien_dich"] for r in rows}) for g in ["GĐ1","GĐ2","GĐ3"]]

# --- Impression share / mất IS do ngân sách theo chiến dịch (weighted by cost) ---
isr=[]
for c in sorted({r["Chien_dich"] for r in rows}):
    rs=[r for r in rows if r["Chien_dich"]==c and r["Impr_Share"] is not None and r["Chi_phi"]>0]
    if not rs: continue
    w=sum(r["Chi_phi"] for r in rs)
    isr.append(dict(cd=c, IS=sum(r["Impr_Share"]*r["Chi_phi"] for r in rs)/w,
                    lostBudget=sum(r["Mat_IS_NganSach"]*r["Chi_phi"] for r in rs)/w,
                    lostRank=sum(r["Mat_IS_ThuHang"]*r["Chi_phi"] for r in rs)/w, cost=w))
out["IS"]=isr
# brand IS theo giai đoạn
out["IS_brand_gd"]=[]
for g in ["GĐ1","GĐ2","GĐ3"]:
    rs=[r for r in rows if r["Chien_dich"]=="SEA_Brand_Vinhomes_HocMon" and r["Giai_doan"]==g]
    w=sum(r["Chi_phi"] for r in rs)
    out["IS_brand_gd"].append(dict(gd=g, IS=sum(r["Impr_Share"]*r["Chi_phi"] for r in rs)/w,
        lostBudget=sum(r["Mat_IS_NganSach"]*r["Chi_phi"] for r in rs)/w,
        lostRank=sum(r["Mat_IS_ThuHang"]*r["Chi_phi"] for r in rs)/w, cost=w,
        ctr=sum(r["Nhap_chuot"] for r in rs)/sum(r["Hien_thi"] for r in rs)))

# --- Sự cố mất thẻ N44-46 ---
gap=[r for r in rows if 44<=int(r["Ngay_thu"])<=46]
out["N44_46"]=dict(chuyendoi_ads=sum(r["ChuyenDoi_Ads"] for r in gap),
                   lead_crm=sum(r["Lead_CRM"] for r in gap),
                   chi_phi=sum(r["Chi_phi"] for r in gap),
                   sql=sum(r["Lead_SQL"] for r in gap))
nb=[r for r in rows if int(r["Ngay_thu"]) in (41,42,43,47,48,49)]
out["N44_46_baseline_ads_per_day"]=sum(r["ChuyenDoi_Ads"] for r in nb)/6
out["N44_46_baseline_lead_per_day"]=sum(r["Lead_CRM"] for r in nb)/6

# --- Cuối tuần vs ngày thường (năng lực sale) ---
we=[r for r in rows if r["Thu"] in ("Thứ 7","Chủ nhật")]
wd=[r for r in rows if r["Thu"] not in ("Thứ 7","Chủ nhật")]
out["WEEKEND"]=block("T7-CN", we); out["WEEKDAY"]=block("T2-T6", wd)

# --- Lead/ngày vs năng lực sale ---
per_day=collections.defaultdict(float)
for r in rows: per_day[r["Ngay"]]+=r["Lead_CRM"]
vals=sorted(per_day.values())
out["LEAD_NGAY"]=dict(max=max(vals), min=min(vals), mean=sum(vals)/len(vals),
                      median=vals[len(vals)//2], so_ngay_vuot_96=sum(1 for v in vals if v>96),
                      so_ngay_vuot_24=sum(1 for v in vals if v>24))
# GĐ3 lead/ngày
for g in ["GĐ1","GĐ2","GĐ3"]:
    d=collections.defaultdict(float)
    for r in rows:
        if r["Giai_doan"]==g: d[r["Ngay"]]+=r["Lead_CRM"]
    out["LEAD_NGAY"][g]=sum(d.values())/len(d)

# --- Trang đích v1 (N1-57) vs v2 (N58-90) trên toàn tài khoản ---
v1=[r for r in rows if int(r["Ngay_thu"])<=57]; v2=[r for r in rows if int(r["Ngay_thu"])>=58]
out["LP_v1"]=block("LP v1 N1-57", v1); out["LP_v2"]=block("LP v2 N58-90", v2)

# ---------------- B4: KPI 32 cọc ----------------
T=out["TOAN_KY"]
b4={}
b4["coc_muc_tieu"]=32; b4["ngan_sach"]=2_100_000_000
# tỷ lệ nền toàn kỳ
r_coc_sql = T["Dat_Coc"]/T["Lead_SQL"]
r_sql_lead = T["SQL_Lead"]
b4["baseline_coc_tren_sql"]=r_coc_sql
b4["baseline_sql_tren_lead"]=r_sql_lead
b4["SQL_can_baseline"]=32/r_coc_sql
b4["lead_can_baseline"]=32/r_coc_sql/r_sql_lead
# kịch bản cải thiện: dùng tỷ lệ của kênh sạch (Brand+Generic) làm trần khả thi
clean=[r for r in rows if r["Chien_dich"] in ("SEA_Brand_Vinhomes_HocMon","SEA_Generic_NhaPho_CanHo_TayBac")]
C=block("Brand+Generic", clean); out["CLEAN"]=C
b4["clean_coc_tren_sql"]=C["Dat_Coc"]/C["Lead_SQL"]; b4["clean_sql_tren_lead"]=C["SQL_Lead"]
b4["SQL_can_clean"]=32/b4["clean_coc_tren_sql"]; b4["lead_can_clean"]=b4["SQL_can_clean"]/b4["clean_sql_tren_lead"]
# GĐ3 (gần nhất, LP v2 + SLA sale)
G3=out["THEO_GD"][2]
b4["gd3_coc_tren_sql"]=G3["Dat_Coc"]/G3["Lead_SQL"]; b4["gd3_sql_tren_lead"]=G3["SQL_Lead"]
b4["SQL_can_gd3"]=32/b4["gd3_coc_tren_sql"]; b4["lead_can_gd3"]=b4["SQL_can_gd3"]/b4["gd3_sql_tren_lead"]
for k in ["baseline","clean","gd3"]:
    b4["CP_SQL_toida_"+k]=2_100_000_000/b4["SQL_can_"+("baseline" if k=="baseline" else k)]
    b4["CPL_toida_"+k]=2_100_000_000/b4["lead_can_"+("baseline" if k=="baseline" else k)]
b4["CP_SQL_KPI"]=2_200_000
b4["SQL_mua_duoc_o_KPI_CPSQL"]=2_100_000_000/2_200_000
b4["coc_neu_gd3_rate"]=b4["SQL_mua_duoc_o_KPI_CPSQL"]*b4["gd3_coc_tren_sql"]
b4["coc_neu_clean_rate"]=b4["SQL_mua_duoc_o_KPI_CPSQL"]*b4["clean_coc_tren_sql"]
out["B4"]=b4

# ---------------- B5: hoà vốn ----------------
HH=181_000_000
out["B5"]=dict(hoa_hong=HH, chi_phi_toi_da_ROAS3=HH/3.0, ROAS1=HH,
               cp_coc_hien_tai=T["CP_Coc"], ROAS_hien_tai=T["ROAS"],
               so_coc_can_de_ROAS3_voi_2_1ty=2_100_000_000*3/HH,
               doanh_thu_can=2_100_000_000*3)
# nếu chỉ đạt 32 cọc với 2,1 tỷ
out["B5"]["ROAS_neu_32_coc"]=32*HH/2_100_000_000

# ---------------- B6: đối chiếu 3 nguồn ----------------
b6=dict(ads=3820, gl=1715, ctc_total=1132, ctc_uniq=779, vpp=612, e30=361, crm=2557)
b6["dup_call"]=b6["ctc_total"]-b6["ctc_uniq"]           # 353
b6["rac"]=b6["vpp"]+b6["e30"]                            # 973
b6["lead_do_duoc"]=b6["gl"]+b6["ctc_uniq"]               # 2494
b6["check_sum"]=b6["gl"]+b6["ctc_total"]+b6["vpp"]+b6["e30"]
b6["check_2494"]=b6["ads"]-b6["dup_call"]-b6["rac"]
b6["mat_the_N44_46"]=b6["crm"]-b6["lead_do_duoc"]        # 63
b6["check_crm"]=b6["lead_do_duoc"]+b6["mat_the_N44_46"]
b6["thoi_phong_tuyet_doi"]=b6["ads"]-b6["crm"]
b6["thoi_phong_pct"]=b6["ads"]/b6["crm"]-1
b6["pct_dup"]=b6["dup_call"]/b6["ads"]; b6["pct_rac"]=b6["rac"]/b6["ads"]
# tiền chi cho sự kiện rác: phân bổ theo tỷ trọng sự kiện rác trong tổng chuyển đổi
b6["tien_theo_su_kien_rac"]=T["Chi_phi"]*b6["rac"]/b6["ads"]
b6["tien_theo_trung_lap"]=T["Chi_phi"]*b6["dup_call"]/b6["ads"]
out["B6"]=b6

# ---------------- B7: Clarity ----------------
cpl_crm=T["CPL_CRM"]; cp_sql=T["CP_SQL"]
b7=dict(cpl_crm=cpl_crm, cp_sql=cp_sql, sql_rate=T["SQL_Lead"],
        coc_tren_sql=T["Dat_Coc"]/T["Lead_SQL"], hoa_hong=HH)
for lo,hi,lab in [(370,480,"chua_sua_tong"),(280,340,"loi_JS_safari"),(60,90,"nut_bi_che"),(30,50,"tel_desktop")]:
    b7[lab]=dict(lo=lo,hi=hi, tien_lo=lo*cpl_crm, tien_hi=hi*cpl_crm,
                 sql_lo=lo*T["SQL_Lead"], sql_hi=hi*T["SQL_Lead"],
                 coc_lo=lo*T["SQL_Lead"]*b7["coc_tren_sql"], coc_hi=hi*T["SQL_Lead"]*b7["coc_tren_sql"],
                 dt_lo=lo*T["SQL_Lead"]*b7["coc_tren_sql"]*HH, dt_hi=hi*T["SQL_Lead"]*b7["coc_tren_sql"]*HH)
# quy đổi 90 ngày -> phần thuộc v2 (33/90 ngày) chỉ để tham chiếu
out["B7"]=b7

# ---------------- A: ước tính lãng phí ----------------
w={}
cd={b["name"]:b for b in out["THEO_CD"]}
w["PMax_chi_phi"]=cd["PMAX_VinhomesHM_Lead"]["Chi_phi"]
w["PMax_coc"]=cd["PMAX_VinhomesHM_Lead"]["Dat_Coc"]
w["PMax_sql"]=cd["PMAX_VinhomesHM_Lead"]["Lead_SQL"]
w["PMax_CP_SQL"]=cd["PMAX_VinhomesHM_Lead"]["CP_SQL"]
w["Comp_chi_phi"]=cd["SEA_Competitor_DoiThu"]["Chi_phi"]; w["Comp_sql"]=cd["SEA_Competitor_DoiThu"]["Lead_SQL"]
w["YT_chi_phi"]=cd["YT_Video_TVC_MoBan"]["Chi_phi"]; w["YT_sql"]=cd["YT_Video_TVC_MoBan"]["Lead_SQL"]
w["GDN_chi_phi"]=cd["GDN_Remarketing_Web30d"]["Chi_phi"]; w["GDN_sql"]=cd["GDN_Remarketing_Web30d"]["Lead_SQL"]
# search terms rác
st_waste=0; st_rows=[]
with open("/home/docdang/Projects/google-ads/test/exam-vinhomes/sheets/04_SEARCH_TERMS.csv", encoding="utf-8-sig") as f:
    for r in csv.DictReader(f):
        if not r["Chi phí (đ)"]: continue
        try: cost=float(r["Chi phí (đ)"]); sql=float(r["Lead chất lượng (SQL)"])
        except: continue
        st_rows.append((r["Cụm từ tìm kiếm"], r["Chiến dịch"], cost, sql, r["Loại đối sánh khớp"]))
w["ST_tong_chi_phi"]=sum(x[2] for x in st_rows)
w["ST_0_SQL_chi_phi"]=sum(x[2] for x in st_rows if x[3]==0)
w["ST_0_SQL_so_cum"]=sum(1 for x in st_rows if x[3]==0)
w["ST_0_SQL_pct"]=w["ST_0_SQL_chi_phi"]/w["ST_tong_chi_phi"]
w["ST_rong_chi_phi"]=sum(x[2] for x in st_rows if x[4]=="Rộng")
w["ST_rong_0SQL"]=sum(x[2] for x in st_rows if x[4]=="Rộng" and x[3]==0)
# địa lý ngoài vùng
geo_out=["Hà Nội","Đà Nẵng","Cần Thơ & ĐBSCL","Đồng Nai","Người dùng ngoài Việt Nam quan tâm đến Việt Nam"]
gcost=0; gsql=0; glead=0
with open("/home/docdang/Projects/google-ads/test/exam-vinhomes/sheets/06_DIA_LY.csv", encoding="utf-8-sig") as f:
    for r in csv.DictReader(f):
        if r["Khu vực"] in geo_out:
            gcost+=float(r["Chi phí (đ)"]); gsql+=float(r["Lead chất lượng (SQL)"]); glead+=float(r["Lead CRM"])
w["GEO_ngoai_vung_chi_phi"]=gcost; w["GEO_ngoai_vung_SQL"]=gsql; w["GEO_ngoai_vung_lead"]=glead
w["GEO_ngoai_vung_coc"]=0; w["GEO_ngoai_vung_CP_SQL"]=gcost/gsql
w["GEO_pct_chi_phi"]=gcost/T["Chi_phi"]
# giờ đêm 20-24 + 0-6 (sale không trực)
w["GIO_dem_chi_phi"]=(0.187+0.04+0.041)*T["Chi_phi"]
w["GIO_dem_SQL"]=112+22+18
w["GIO_dem_coc"]=3+0+0
# tốc độ phản hồi: nếu toàn bộ lead được gọi <5 phút
crm_a=[(281,0.0182),(485,0.0121),(588,0.0058),(536,0.0021),(664,0.0004)]
w["CRM_lead_mau"]=sum(x[0] for x in crm_a)
w["CRM_coc_hien_tai"]=sum(a*b for a,b in crm_a)
w["CRM_coc_neu_duoi5p"]=sum(a for a,_ in crm_a)*0.0182
w["CRM_coc_neu_duoi30p"]=sum(a for a,_ in crm_a)*0.0121
w["CRM_coc_mat"]=w["CRM_coc_neu_duoi30p"]-w["CRM_coc_hien_tai"]
w["CRM_dt_mat_30p"]=w["CRM_coc_mat"]*HH
w["CRM_dt_mat_5p"]=(w["CRM_coc_neu_duoi5p"]-w["CRM_coc_hien_tai"])*HH
w["CRM_lead_bo_sot"]=118+96+61
w["CRM_tien_lead_bo_sot"]=(118+96+61)*cpl_crm
# LP v1: nếu v1 có tỷ lệ hoàn tất form của v2
w["LPv1_form_start"]=4912; w["LPv1_gl"]=1002; w["LPv2_rate"]=0.280047132757266
w["LPv1_gl_neu_v2_rate"]=4912*0.280047132757266
w["LPv1_lead_mat"]=w["LPv1_gl_neu_v2_rate"]-1002
w["LPv1_tien_mat"]=w["LPv1_lead_mat"]*cpl_crm
# brand mất IS do ngân sách
bg=out["IS_brand_gd"]
w["Brand_IS_toanky"]=[x for x in isr if x["cd"]=="SEA_Brand_Vinhomes_HocMon"][0]
bb=w["Brand_IS_toanky"]
brand=cd["SEA_Brand_Vinhomes_HocMon"]
w["Brand_click_mat_uoc"]=brand["Nhap_chuot"]*bb["lostBudget"]/max(bb["IS"],1e-9)
w["Brand_lead_mat_uoc"]=w["Brand_click_mat_uoc"]*brand["CVR_click"]
w["Brand_coc_mat_uoc"]=w["Brand_lead_mat_uoc"]*brand["SQL_Lead"]*(brand["Dat_Coc"]/brand["Lead_SQL"])
w["Brand_dt_mat_uoc"]=w["Brand_coc_mat_uoc"]*HH
w["Brand_chi_phi_them"]=w["Brand_click_mat_uoc"]*brand["CPC"]
out["WASTE"]=w

# ---------------- D3: PMax ----------------
pm=cd["PMAX_VinhomesHM_Lead"]
d3=dict(cp_conv_pmax=pm["CPL_Ads"], cp_conv_brand=cd["SEA_Brand_Vinhomes_HocMon"]["CPL_Ads"],
        cp_conv_generic=cd["SEA_Generic_NhaPho_CanHo_TayBac"]["CPL_Ads"],
        pmax_cpsql=pm["CP_SQL"], brand_cpsql=cd["SEA_Brand_Vinhomes_HocMon"]["CP_SQL"],
        generic_cpsql=cd["SEA_Generic_NhaPho_CanHo_TayBac"]["CP_SQL"],
        pmax_coc=pm["Dat_Coc"], pmax_dt=pm["DoanhThu_HoaHong"], pmax_cost=pm["Chi_phi"],
        pmax_sql_lead=pm["SQL_Lead"], pmax_ads_crm=pm["Ads_vs_CRM"],
        pmax_bounce3s=0.743, pmax_engage=0.087, pmax_trung_sdt=0.31, pmax_dung_duoc=0.07)
d3["pmax_lead_dung_duoc"]=pm["Lead_CRM"]*0.07
out["D3"]=d3

# ---------------- D1: Brand ----------------
br=cd["SEA_Brand_Vinhomes_HocMon"]
out["D1"]=dict(cost=br["Chi_phi"], pct_cost=br["Chi_phi"]/T["Chi_phi"], coc=br["Dat_Coc"],
               pct_coc=br["Dat_Coc"]/T["Dat_Coc"], dt=br["DoanhThu_HoaHong"],
               pct_dt=br["DoanhThu_HoaHong"]/T["DoanhThu_HoaHong"], roas=br["ROAS"],
               cp_sql=br["CP_SQL"], cp_coc=br["CP_Coc"], sql_lead=br["SQL_Lead"],
               generic_roas=cd["SEA_Generic_NhaPho_CanHo_TayBac"]["ROAS"],
               generic_cp_coc=cd["SEA_Generic_NhaPho_CanHo_TayBac"]["CP_Coc"],
               ddb_brand=401, lastclick_brand=592, ddb_delta=(401-592)/592)

# ---------------- D4: ngân sách 1,2 tỷ ----------------
d4={}
keep=["SEA_Brand_Vinhomes_HocMon","SEA_Generic_NhaPho_CanHo_TayBac","GDN_Remarketing_Web30d"]
d4["cat_pmax_comp_yt"]=sum(cd[c]["Chi_phi"] for c in ["PMAX_VinhomesHM_Lead","SEA_Competitor_DoiThu","YT_Video_TVC_MoBan"])
d4["pct_cat"]=d4["cat_pmax_comp_yt"]/T["Chi_phi"]
d4["sql_mat"]=sum(cd[c]["Lead_SQL"] for c in ["PMAX_VinhomesHM_Lead","SEA_Competitor_DoiThu","YT_Video_TVC_MoBan"])
d4["coc_mat"]=sum(cd[c]["Dat_Coc"] for c in ["PMAX_VinhomesHM_Lead","SEA_Competitor_DoiThu","YT_Video_TVC_MoBan"])
d4["giu_chi_phi"]=sum(cd[c]["Chi_phi"] for c in keep)
d4["giu_coc"]=sum(cd[c]["Dat_Coc"] for c in keep)
d4["giu_dt"]=sum(cd[c]["DoanhThu_HoaHong"] for c in keep)
d4["giu_roas"]=d4["giu_dt"]/d4["giu_chi_phi"]
d4["coc_ky_vong_1_2ty"]=1_200_000_000/ (d4["giu_chi_phi"]/d4["giu_coc"])
d4["roas_1_2ty"]=d4["coc_ky_vong_1_2ty"]*HH/1_200_000_000
out["D4"]=d4

if __name__=="__main__":
    def f(x):
        if isinstance(x,float): return round(x,6)
        return x
    print(json.dumps(out, ensure_ascii=False, indent=1, default=f))
    # self-check
    assert abs(out["TOAN_KY"]["Chi_phi"]-1803537000)<1, out["TOAN_KY"]["Chi_phi"]
    assert out["TOAN_KY"]["ChuyenDoi_Ads"]==3820 and out["TOAN_KY"]["Lead_CRM"]==2557
    assert out["TOAN_KY"]["Dat_Coc"]==18 and out["TOAN_KY"]["Lead_SQL"]==651
    assert out["B6"]["check_sum"]==3820 and out["B6"]["check_2494"]==2494 and out["B6"]["check_crm"]==2557
    print("SELF-CHECK OK")

# ============ PHẦN C: phân bổ ngân sách & dự báo ============
def phanbo():
    P={ # triệu VND
     "GĐ1 (N1-30)": {"Brand":130,"Generic_Exact/Phrase":250,"RMKT_Search+Display":60,"PMax_Clean":110,"DemandGen/YT":0,"Dự phòng":50},
     "GĐ2 (N31-60)":{"Brand":160,"Generic_Exact/Phrase":300,"RMKT_Search+Display":70,"PMax_Clean":120,"DemandGen/YT":30,"Dự phòng":20},
     "GĐ3 (N61-90)":{"Brand":190,"Generic_Exact/Phrase":330,"RMKT_Search+Display":80,"PMax_Clean":140,"DemandGen/YT":50,"Dự phòng":10},
    }
    tot=sum(sum(v.values()) for v in P.values())
    assert tot==2100, tot
    cd=collections.defaultdict(int)
    for g,v in P.items():
        for k,x in v.items(): cd[k]+=x
    return P, dict(cd), tot

P,CD,TOT=phanbo()
brand=[b for b in out["THEO_CD"] if b["name"]=="SEA_Brand_Vinhomes_HocMon"][0]
gen=[b for b in out["THEO_CD"] if b["name"]=="SEA_Generic_NhaPho_CanHo_TayBac"][0]
c={}
c["phan_bo"]=P; c["theo_chien_dich"]=CD; c["tong_trieu"]=TOT
# trần năng lực Brand: clicks tối đa nếu IS=100%
c["brand_click_toi_da_90n"]=brand["Nhap_chuot"]/[x for x in out["IS"] if x["cd"]=="SEA_Brand_Vinhomes_HocMon"][0]["IS"]
c["brand_chi_phi_de_full_IS"]=c["brand_click_toi_da_90n"]*brand["CPC"]
c["brand_ns_de_xuat"]=CD["Brand"]*1e6
c["brand_pct_nang_luc"]=c["brand_ns_de_xuat"]/c["brand_chi_phi_de_full_IS"]
# dự báo cọc
c["brand_cp_coc_toanky"]=brand["CP_Coc"]; c["brand_cp_coc_gd3"]=16287250.0
c["brand_coc_dubao"]=c["brand_ns_de_xuat"]/brand["CP_Coc"]
# Generic sau khi cắt search term 0-SQL (37,6% chi phí ST)
w=out["WASTE"]
c["generic_cat_rac_pct"]=w["ST_0_SQL_pct"]
c["generic_cp_coc_gd3"]=86386333.33333333
c["generic_cp_coc_sau_cat"]=c["generic_cp_coc_gd3"]*(1-w["ST_0_SQL_pct"])
c["generic_ns"]=CD["Generic_Exact/Phrase"]*1e6
c["generic_coc_dubao"]=c["generic_ns"]/c["generic_cp_coc_sau_cat"]
c["coc_dubao_tong"]=c["brand_coc_dubao"]+c["generic_coc_dubao"]
c["coc_dubao_than_trong"]=c["coc_dubao_tong"]*0.85
c["dt_dubao"]=c["coc_dubao_tong"]*181_000_000
c["roas_dubao"]=c["dt_dubao"]/2_100_000_000
c["dt_than_trong"]=c["coc_dubao_than_trong"]*181_000_000
c["roas_than_trong"]=c["dt_than_trong"]/2_100_000_000
c["coc_can_de_ROAS3"]=2_100_000_000*3/181_000_000
c["do_nhay_1_coc_ROAS"]=181_000_000/2_100_000_000
# SQL/lead cần theo B4 (dùng tỷ lệ GĐ3)
c["SQL_can"]=out["B4"]["SQL_can_gd3"]; c["lead_can"]=out["B4"]["lead_can_gd3"]
c["lead_can_moi_ngay"]=c["lead_can"]/90
c["nang_luc_sale_ngay"]=96
c["ty_le_dung_nang_luc"]=c["lead_can_moi_ngay"]/96
out["C"]=c

if __name__=="__main__":
    print(json.dumps({"C":out["C"]}, ensure_ascii=False, indent=1, default=lambda x: round(x,6) if isinstance(x,float) else x))
    assert abs(sum(sum(v.values()) for v in P.values())-2100)<1e-9
    print("C SELF-CHECK OK: tổng phân bổ = 2.100 triệu")
