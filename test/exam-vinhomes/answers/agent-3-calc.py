#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Toàn bộ phép tính cho bài làm agent-3.md. Chạy: python3 agent-3-calc.py
Nguồn: /home/docdang/Downloads/du_lieu_google_ads_90_ngay_1.csv (= sheet 02_DU_LIEU_NGAY)
        + sheets/*.csv (10_GA4, 11_CLARITY, 12_GTM, 04, 06, 07, 08)
Không dùng thư viện ngoài (chỉ csv/stdlib)."""
import csv, collections, os

CSV = "/home/docdang/Downloads/du_lieu_google_ads_90_ngay_1.csv"
NUM = ["Ngay_thu","Hien_thi","Nhap_chuot","Chi_phi","Impr_Share","Mat_IS_NganSach","Mat_IS_ThuHang",
       "ChuyenDoi_Ads","Lead_CRM","Lead_SQL","Di_Xem_Nha","Booking","Dat_Coc","DoanhThu_HoaHong"]

rows = []
with open(CSV, encoding="utf-8-sig") as f:
    for r in csv.DictReader(f):
        if not (r.get("Chien_dich") or "").strip():
            continue  # bỏ dòng trống cuối file
        for k in NUM:
            r[k] = float(r[k] or 0)
        rows.append(r)

def agg(rs):
    d = {k: sum(r[k] for r in rs) for k in NUM
         if k not in ("Impr_Share","Mat_IS_NganSach","Mat_IS_ThuHang","Ngay_thu")}
    d["n"] = len(rs)
    return d

def div(a, b):
    return a / b if b else float("nan")

def vnd(x):
    return f"{x:,.0f}".replace(",", ".")

def pct(x):
    return f"{100*x:.2f}%"

out = []
P = lambda *a: out.append(" ".join(str(x) for x in a))

TOT = agg(rows)
P("="*70); P("== 0. TỔNG QUAN TOÀN KỲ (90 ngày, 02/03–30/05/2026) ==")
for k, v in TOT.items():
    P(f"  {k:20s} {v:,.0f}")

# ---------------- B1 ----------------
P(""); P("="*70); P("== B1. CPL Ads / CPL CRM / CP/SQL / CP/cọc ==")
P(f"{'Chiến dịch':40s} {'Chi phí':>15s} {'CPL_Ads':>12s} {'CPL_CRM':>12s} {'CP/SQL':>14s} {'CP/cọc':>16s}")
by_camp = collections.defaultdict(list)
for r in rows:
    by_camp[r["Chien_dich"]].append(r)
b1 = {}
for c, rs in list(by_camp.items()) + [("TOÀN KỲ", rows)]:
    a = agg(rs)
    b1[c] = dict(cost=a["Chi_phi"],
                 cpl_ads=div(a["Chi_phi"], a["ChuyenDoi_Ads"]),
                 cpl_crm=div(a["Chi_phi"], a["Lead_CRM"]),
                 cp_sql=div(a["Chi_phi"], a["Lead_SQL"]),
                 cp_coc=div(a["Chi_phi"], a["Dat_Coc"]),
                 **a)
    x = b1[c]
    P(f"{c:40s} {vnd(x['cost']):>15s} {vnd(x['cpl_ads']):>12s} {vnd(x['cpl_crm']):>12s} "
      f"{vnd(x['cp_sql']):>14s} {(vnd(x['cp_coc']) if a['Dat_Coc'] else '—(0 cọc)'):>16s}")
    P(f"{'':40s} clicks={a['Nhap_chuot']:,.0f} convAds={a['ChuyenDoi_Ads']:,.0f} "
      f"lead={a['Lead_CRM']:,.0f} SQL={a['Lead_SQL']:,.0f} xem={a['Di_Xem_Nha']:,.0f} "
      f"book={a['Booking']:,.0f} coc={a['Dat_Coc']:,.0f} DT={vnd(a['DoanhThu_HoaHong'])} "
      f"CPC={vnd(div(a['Chi_phi'],a['Nhap_chuot']))} CTR={pct(div(a['Nhap_chuot'],a['Hien_thi']))} "
      f"SQL/lead={pct(div(a['Lead_SQL'],a['Lead_CRM']))} Ads/CRM={div(a['ChuyenDoi_Ads'],a['Lead_CRM']):.2f}x")

# ---------------- B2 ----------------
P(""); P("="*70); P("== B2. ROAS toàn kỳ & theo giai đoạn ==")
by_gd = collections.defaultdict(list)
for r in rows:
    by_gd[r["Giai_doan"]].append(r)
for g in ["GĐ1", "GĐ2", "GĐ3"]:
    a = agg(by_gd[g])
    P(f"{g}: chi phí={vnd(a['Chi_phi'])} DT={vnd(a['DoanhThu_HoaHong'])} ROAS={div(a['DoanhThu_HoaHong'],a['Chi_phi']):.3f}x "
      f"cọc={a['Dat_Coc']:.0f} lead={a['Lead_CRM']:.0f} SQL={a['Lead_SQL']:.0f} "
      f"CP/SQL={vnd(div(a['Chi_phi'],a['Lead_SQL']))}")
P(f"TOÀN KỲ: chi phí={vnd(TOT['Chi_phi'])} DT={vnd(TOT['DoanhThu_HoaHong'])} "
  f"ROAS={div(TOT['DoanhThu_HoaHong'],TOT['Chi_phi']):.3f}x")
P("ROAS theo chiến dịch:")
for c in by_camp:
    a = agg(by_camp[c])
    P(f"  {c:40s} ROAS={div(a['DoanhThu_HoaHong'],a['Chi_phi']):.3f}x  lãi/lỗ={vnd(a['DoanhThu_HoaHong']-a['Chi_phi'])}")

# ---------------- B3 ----------------
P(""); P("="*70); P("== B3. Tỷ lệ chuyển đổi từng bước phễu (toàn kỳ) ==")
steps = [("Lead_CRM->SQL","Lead_CRM","Lead_SQL"),("SQL->Đi xem","Lead_SQL","Di_Xem_Nha"),
         ("Đi xem->Booking","Di_Xem_Nha","Booking"),("Booking->Cọc","Booking","Dat_Coc"),
         ("Lead->Cọc (tổng)","Lead_CRM","Dat_Coc")]
for name, a_, b_ in steps:
    P(f"  {name:22s} {TOT[b_]:.0f}/{TOT[a_]:.0f} = {pct(div(TOT[b_],TOT[a_]))}")
P("Phễu theo giai đoạn:")
for g in ["GĐ1","GĐ2","GĐ3"]:
    a = agg(by_gd[g])
    P(f"  {g}: SQL/lead={pct(div(a['Lead_SQL'],a['Lead_CRM']))} xem/SQL={pct(div(a['Di_Xem_Nha'],a['Lead_SQL']))} "
      f"book/xem={pct(div(a['Booking'],a['Di_Xem_Nha']))} coc/book={pct(div(a['Dat_Coc'],a['Booking']))} "
      f"coc/lead={pct(div(a['Dat_Coc'],a['Lead_CRM']))}")
P("Phễu chỉ tính 3 chiến dịch Search (loại PMax/GDN/YT — 0 cọc):")
sea = [r for r in rows if r["Chien_dich"].startswith("SEA_")]
a = agg(sea)
P(f"  lead={a['Lead_CRM']:.0f} SQL={a['Lead_SQL']:.0f} xem={a['Di_Xem_Nha']:.0f} book={a['Booking']:.0f} coc={a['Dat_Coc']:.0f}")
P(f"  SQL/lead={pct(div(a['Lead_SQL'],a['Lead_CRM']))} xem/SQL={pct(div(a['Di_Xem_Nha'],a['Lead_SQL']))} "
  f"book/xem={pct(div(a['Booking'],a['Di_Xem_Nha']))} coc/book={pct(div(a['Dat_Coc'],a['Booking']))} "
  f"coc/SQL={pct(div(a['Dat_Coc'],a['Lead_SQL']))}")
# GĐ3 (đã có LP v2 + SLA sale) — dùng làm cơ sở dự báo
g3s = [r for r in sea if r["Giai_doan"] == "GĐ3"]
a3 = agg(g3s)
P(f"  GĐ3-Search: lead={a3['Lead_CRM']:.0f} SQL={a3['Lead_SQL']:.0f} xem={a3['Di_Xem_Nha']:.0f} "
  f"book={a3['Booking']:.0f} coc={a3['Dat_Coc']:.0f} SQL/lead={pct(div(a3['Lead_SQL'],a3['Lead_CRM']))} "
  f"coc/SQL={pct(div(a3['Dat_Coc'],a3['Lead_SQL']))}")

# ---------------- B4 ----------------
P(""); P("="*70); P("== B4. Ngược từ KPI 32 cọc ==")
COC_KPI, BUDGET = 32, 2_100_000_000
scen = {
  "A. Toàn kỳ toàn tài khoản (bảo thủ)": dict(sql_lead=div(TOT["Lead_SQL"],TOT["Lead_CRM"]),
                                              coc_sql=div(TOT["Dat_Coc"],TOT["Lead_SQL"])),
  "B. Chỉ Search toàn kỳ": dict(sql_lead=div(a["Lead_SQL"],a["Lead_CRM"]),
                                coc_sql=div(a["Dat_Coc"],a["Lead_SQL"])),
  "C. Search GĐ3 (LP v2 + SLA 15') — kế hoạch dùng": dict(sql_lead=div(a3["Lead_SQL"],a3["Lead_CRM"]),
                                                          coc_sql=div(a3["Dat_Coc"],a3["Lead_SQL"])),
}
for name, s in scen.items():
    sql_need = COC_KPI / s["coc_sql"]
    lead_need = sql_need / s["sql_lead"]
    P(f"{name}")
    P(f"   SQL/lead={pct(s['sql_lead'])}  cọc/SQL={pct(s['coc_sql'])}")
    P(f"   → cần SQL={sql_need:.0f}  cần lead thô={lead_need:.0f}  "
      f"CP/SQL trần={vnd(BUDGET/sql_need)}  CPL trần={vnd(BUDGET/lead_need)}")
P(f"Ràng buộc KPI CP/SQL ≤ 2.200.000 → với 2,1 tỷ mua tối đa {BUDGET/2_200_000:.0f} SQL")
for name, s in scen.items():
    P(f"   {name}: {BUDGET/2_200_000:.0f} SQL × {pct(s['coc_sql'])} = {BUDGET/2_200_000*s['coc_sql']:.1f} cọc")
P(f"Năng lực sale: 8×12=96 lead/ngày ×90 = {8*12*90} lead; T7/CN chỉ 2 sale → "
  f"{ (2*12*2 + 8*12*5)/7 :.1f} lead/ngày bình quân có người xử lý = {(2*12*2+8*12*5)/7*90:.0f} lead/90 ngày")

# ---------------- B5 ----------------
P(""); P("="*70); P("== B5. Điểm hòa vốn / trần chi phí mỗi cọc ==")
HH = 181_000_000
for roas in [1.0, 2.0, 3.0, 4.0]:
    P(f"  ROAS {roas:.1f}x → chi phí quảng cáo tối đa/cọc = {vnd(HH/roas)}")
P(f"  KPI 32 cọc × {vnd(HH)} = doanh thu {vnd(32*HH)}; ROAS tại ngân sách 2,1 tỷ = {32*HH/BUDGET:.2f}x")
P(f"  Để ROAS=3,0x với ngân sách 2,1 tỷ → cần DT {vnd(3*BUDGET)} = {3*BUDGET/HH:.1f} cọc "
  f"(cao hơn KPI 32 cọc → KPI 32 cọc là ràng buộc CHẶT hơn? {'không' if 3*BUDGET/HH>32 else 'có'})")
P(f"  Hiện tại CP/cọc thực tế = {vnd(div(TOT['Chi_phi'],TOT['Dat_Coc']))} → "
  f"gấp {div(TOT['Chi_phi'],TOT['Dat_Coc'])/(HH/3):.2f} lần trần ROAS 3x")

# ---------------- B6 ----------------
P(""); P("="*70); P("== B6. Đối chiếu 3 nguồn (sheet 10_GA4 mục A + 12_GTM v23/v24) ==")
ga = dict(generate_lead=1715, c2c_events=1132, c2c_users=779, view_price=612, engaged=361)
ads_conv = 3820
crm = 2557
P(f"  Ads/GA4 'Chuyển đổi' = {ga['generate_lead']}+{ga['c2c_events']}+{ga['view_price']}+{ga['engaged']} "
  f"= {sum([ga['generate_lead'],ga['c2c_events'],ga['view_price'],ga['engaged']])} (khớp {ads_conv}: "
  f"{sum([ga['generate_lead'],ga['c2c_events'],ga['view_price'],ga['engaged']])==ads_conv})")
dup = ga["c2c_events"] - ga["c2c_users"]
junk = ga["view_price"] + ga["engaged"]
measured = ga["generate_lead"] + ga["c2c_users"]
P(f"  (1) đếm trùng click_to_call = {ga['c2c_events']}-{ga['c2c_users']} = {dup}")
P(f"  (2) sự kiện rác (view_price_page + engaged_30s) = {ga['view_price']}+{ga['engaged']} = {junk}")
P(f"  → lead thật đo được bằng thẻ = {ads_conv} - {dup} - {junk} = {ads_conv-dup-junk} (GA4 ghi {measured}: {ads_conv-dup-junk==measured})")
lost_tag = crm - measured
P(f"  (3) mất thẻ N44–46 (GTM v23 đổi class .form-dk-v1→.form-register) = {crm} - {measured} = {lost_tag} lead")
P(f"  PHÉP CỘNG KHỚP: {ads_conv} - {dup}(trùng) - {junk}(rác) + {lost_tag}(mất thẻ) = "
  f"{ads_conv-dup-junk+lost_tag} = CRM {crm} → {ads_conv-dup-junk+lost_tag==crm}")
P(f"  Tỷ trọng: trùng {dup/ads_conv:.1%}, rác {junk/ads_conv:.1%}, tổng thổi phồng "
  f"{(dup+junk)/ads_conv:.1%} của cột Chuyển đổi")
P(f"  Ads/CRM = {ads_conv/crm:.2f}x (benchmark sheet 09: báo động >1,8x)")
# kiểm chứng N44-46 từ CSV
P("  Kiểm chứng từ sheet 02 (Ngay_thu 44-46):")
for d in (43, 44, 45, 46, 47, 48):
    rs = [r for r in rows if r["Ngay_thu"] == d]
    aa = agg(rs)
    P(f"    N{d:02.0f} convAds={aa['ChuyenDoi_Ads']:.0f} leadCRM={aa['Lead_CRM']:.0f} chi phí={vnd(aa['Chi_phi'])}")
n446 = agg([r for r in rows if 44 <= r["Ngay_thu"] <= 46])
P(f"    Tổng N44-46: convAds={n446['ChuyenDoi_Ads']:.0f} leadCRM={n446['Lead_CRM']:.0f} "
  f"chi phí={vnd(n446['Chi_phi'])} → CRM-Ads={n446['Lead_CRM']-n446['ChuyenDoi_Ads']:.0f}")

# ---------------- B7 ----------------
P(""); P("="*70); P("== B7. Lead mất do lỗi kỹ thuật CHƯA SỬA (sheet 11_CLARITY mục C) ==")
CPL_REAL = div(TOT["Chi_phi"], TOT["Lead_CRM"])
CP_SQL_REAL = div(TOT["Chi_phi"], TOT["Lead_SQL"])
sql_rate = div(TOT["Lead_SQL"], TOT["Lead_CRM"])
coc_per_sql = div(TOT["Dat_Coc"], TOT["Lead_SQL"])
P(f"  CPL CRM thực tế toàn kỳ = {vnd(CPL_REAL)}; CP/SQL = {vnd(CP_SQL_REAL)}; "
  f"SQL/lead={pct(sql_rate)}; cọc/SQL={pct(coc_per_sql)}")
unfixed = [("#4 Lỗi JS setDate (Safari iOS) — form không gửi được", 4196, 280, 340),
           ("#5 Nút CTA bị khung chat che (<380px)", 2741, 60, 90),
           ("#6 tel: không phản hồi trên desktop (1.847 nhấp chết)", 1204, 30, 50)]
lo = sum(x[2] for x in unfixed); hi = sum(x[3] for x in unfixed)
for n, s, l, h in unfixed:
    P(f"  {n}: {s} phiên ảnh hưởng, lead mất {l}–{h} (SỐ ĐO Clarity: phiên; ƯỚC TÍNH đội UX: lead)")
P(f"  Tổng lead mất (đo/ước tính của Clarity) = {lo}–{hi} lead")
for lbl, v in (("thấp", lo), ("cao", hi)):
    P(f"  Kịch bản {lbl} {v} lead:")
    P(f"     giá trị theo CPL thực tế: {v} × {vnd(CPL_REAL)} = {vnd(v*CPL_REAL)}")
    P(f"     quy ra SQL (×{pct(sql_rate)}) = {v*sql_rate:.0f} SQL → giá trị theo CP/SQL = {vnd(v*sql_rate*CP_SQL_REAL)}")
    P(f"     quy ra cọc (×{pct(coc_per_sql)}) = {v*sql_rate*coc_per_sql:.1f} cọc → hoa hồng bỏ lỡ = {vnd(v*sql_rate*coc_per_sql*HH)}")
P(f"  Điều chỉnh Clarity lấy mẫu ~92% → quy toàn bộ lưu lượng: {lo/0.92:.0f}–{hi/0.92:.0f} lead")
P(f"  Clarity gắn từ ngày 5 → thiếu 4/90 ngày dữ liệu ({4/90:.1%}), ước tính là cận dưới.")

# ---------------- PHẦN A: bằng chứng số ----------------
P(""); P("="*70); P("== A. BẰNG CHỨNG SỐ CHO CHẨN ĐOÁN ==")

P("-- A1. PMax: chi phí, lead, chất lượng --")
pm = agg(by_camp["PMAX_VinhomesHM_Lead"])
P(f"  chi phí={vnd(pm['Chi_phi'])} ({pm['Chi_phi']/TOT['Chi_phi']:.1%} tài khoản) convAds={pm['ChuyenDoi_Ads']:.0f} "
  f"lead={pm['Lead_CRM']:.0f} SQL={pm['Lead_SQL']:.0f} cọc={pm['Dat_Coc']:.0f} DT={vnd(pm['DoanhThu_HoaHong'])}")
P(f"  Ads/CRM={div(pm['ChuyenDoi_Ads'],pm['Lead_CRM']):.2f}x; SQL/lead={pct(div(pm['Lead_SQL'],pm['Lead_CRM']))} "
  f"(benchmark <12% = nhắm sai tệp); CP/SQL={vnd(div(pm['Chi_phi'],pm['Lead_SQL']))} (báo động >5tr)")
P(f"  Clarity: thoát nhanh <3s = 74,3%; thời lượng phiên trung vị 3s; GA4 tỷ lệ tương tác 8,7%; "
  f"hao hụt nhấp→phiên 28,0%")
P(f"  CRM 08C: lead PMax dùng được 7% (trùng SĐT 31%, SĐT sai 24%, sai phân khúc 34%)")
P(f"  → lead dùng được ước tính = {pm['Lead_CRM']:.0f} × 7% = {pm['Lead_CRM']*0.07:.0f}; "
  f"chi phí/lead dùng được = {vnd(div(pm['Chi_phi'], pm['Lead_CRM']*0.07))}")
P(f"  Lãng phí (chi phí PMax - 0 doanh thu) = {vnd(pm['Chi_phi'])}")

P("-- A2. Chuyển đổi rác nhập vào Ads (view_price+engaged=973 = 25,5% cột Chuyển đổi) --")
P(f"  973/3820 = {973/3820:.1%}; máy học tối ưu theo 973 tín hiệu không phải lead")
P(f"  Phân bổ 973 sự kiện rác theo chiến dịch (sheet 10B): PMax 438+259={438+259}, "
  f"GDN 50+30={50+30}, YT 71+42={71+42}, Generic 38+22={38+22}, Brand 15+8={15+8} "
  f"→ PMax chiếm {697/973:.1%} sự kiện rác")

P("-- A3. Competitor campaign: 0 cọc, 0 doanh thu --")
cp = agg(by_camp["SEA_Competitor_DoiThu"])
P(f"  chi phí={vnd(cp['Chi_phi'])} lead={cp['Lead_CRM']:.0f} SQL={cp['Lead_SQL']:.0f} cọc={cp['Dat_Coc']:.0f} "
  f"CP/SQL={vnd(div(cp['Chi_phi'],cp['Lead_SQL']))} CPC={vnd(div(cp['Chi_phi'],cp['Nhap_chuot']))}")
P(f"  CTR={pct(div(cp['Nhap_chuot'],cp['Hien_thi']))} (benchmark generic báo động <2%); "
  f"CRM 08C: 26% lead là môi giới/đối thủ, chỉ 26% dùng được")

P("-- A4. YouTube & GDN: 0 cọc --")
for c in ["YT_Video_TVC_MoBan", "GDN_Remarketing_Web30d"]:
    x = agg(by_camp[c])
    P(f"  {c}: chi phí={vnd(x['Chi_phi'])} lead={x['Lead_CRM']:.0f} SQL={x['Lead_SQL']:.0f} cọc={x['Dat_Coc']:.0f} "
      f"CP/SQL={vnd(div(x['Chi_phi'],x['Lead_SQL']))}")
P(f"  Tổng 3 kênh không cọc (PMax+GDN+YT) = "
  f"{vnd(pm['Chi_phi']+agg(by_camp['GDN_Remarketing_Web30d'])['Chi_phi']+agg(by_camp['YT_Video_TVC_MoBan'])['Chi_phi'])} "
  f"= {(pm['Chi_phi']+agg(by_camp['GDN_Remarketing_Web30d'])['Chi_phi']+agg(by_camp['YT_Video_TVC_MoBan'])['Chi_phi'])/TOT['Chi_phi']:.1%} ngân sách, 0đ doanh thu")

P("-- A5. Brand bị bóp ngân sách (Impression Share) --")
for c in by_camp:
    rs = by_camp[c]
    rs2 = [r for r in rs if r["Chi_phi"] > 0]
    if not rs2: continue
    w = sum(r["Chi_phi"] for r in rs2)
    is_ = sum(r["Impr_Share"]*r["Chi_phi"] for r in rs2)/w
    lb = sum(r["Mat_IS_NganSach"]*r["Chi_phi"] for r in rs2)/w
    lr = sum(r["Mat_IS_ThuHang"]*r["Chi_phi"] for r in rs2)/w
    P(f"  {c:40s} IS={pct(is_)} mất_IS_ngân_sách={pct(lb)} mất_IS_thứ_hạng={pct(lr)} (bình quân có trọng số chi phí)")
br = by_camp["SEA_Brand_Vinhomes_HocMon"]
for g in ["GĐ1","GĐ2","GĐ3"]:
    rs = [r for r in br if r["Giai_doan"] == g and r["Chi_phi"] > 0]
    w = sum(r["Chi_phi"] for r in rs)
    P(f"    Brand {g}: IS={pct(sum(r['Impr_Share']*r['Chi_phi'] for r in rs)/w)} "
      f"mất_IS_NS={pct(sum(r['Mat_IS_NganSach']*r['Chi_phi'] for r in rs)/w)} "
      f"chi phí={vnd(w)} cọc={sum(r['Dat_Coc'] for r in rs):.0f} "
      f"ROAS={div(sum(r['DoanhThu_HoaHong'] for r in rs),w):.2f}x")
# Ước tính doanh thu bỏ lỡ do mất IS ngân sách của Brand
bra = agg(br)
lb_br = sum(r["Mat_IS_NganSach"]*r["Chi_phi"] for r in br if r["Chi_phi"]>0)/bra["Chi_phi"]
P(f"  Ước tính: Brand mất {pct(lb_br)} IS do ngân sách. Nếu bù đủ → hiển thị ×{1/(1-lb_br):.2f}, "
  f"giả định tuyến tính lead/cọc → cọc thêm ≈ {bra['Dat_Coc']*(1/(1-lb_br)-1):.1f}, "
  f"doanh thu thêm ≈ {vnd(bra['DoanhThu_HoaHong']*(1/(1-lb_br)-1))}, "
  f"chi phí thêm ≈ {vnd(bra['Chi_phi']*(1/(1-lb_br)-1))}")

P("-- A6. Search terms rác (sheet 04) --")
st = []
with open("/home/docdang/Projects/google-ads/test/exam-vinhomes/sheets/04_SEARCH_TERMS.csv", encoding="utf-8-sig") as f:
    for r in csv.DictReader(f):
        if r["Cụm từ tìm kiếm"] and r["Chi phí (đ)"]:
            try:
                st.append((r["Cụm từ tìm kiếm"], r["Chiến dịch"], r["Loại đối sánh khớp"],
                           float(r["Chi phí (đ)"]), float(r["Lead chất lượng (SQL)"]), float(r["Lead CRM"])))
            except ValueError:
                pass
zero = [x for x in st if x[4] == 0]
P(f"  Số cụm từ trong báo cáo: {len(st)}; chi phí phủ trong báo cáo: {vnd(sum(x[3] for x in st))}")
P(f"  Cụm từ 0 SQL: {len(zero)} cụm, chi phí = {vnd(sum(x[3] for x in zero))} "
  f"= {sum(x[3] for x in zero)/TOT['Chi_phi']:.1%} tổng chi phí tài khoản")
for x in sorted(zero, key=lambda y: -y[3])[:12]:
    P(f"     {x[0][:45]:45s} {x[2]:10s} {vnd(x[3]):>12s} lead={x[5]:.0f} SQL=0")
irrelevant = [x for x in zero if any(k in x[0] for k in
              ["tuyển dụng","học phí","thuê","trọ","kho xưởng","việc làm","lừa đảo","quy hoạch",
               "chung cư mini","100 triệu"])]
P(f"  Trong đó cụm từ SAI Ý ĐỊNH rõ ràng (tuyển dụng/thuê/trọ/việc làm/quy hoạch/lừa đảo/mini): "
  f"{len(irrelevant)} cụm, chi phí={vnd(sum(x[3] for x in irrelevant))}")
comp_terms = [x for x in zero if x[1] == "SEA_Competitor_DoiThu"]
P(f"  Cụm từ đối thủ 0 SQL: {len(comp_terms)} cụm, chi phí={vnd(sum(x[3] for x in comp_terms))}")
P(f"  Cấu hình 05: đối sánh rộng = 71% chi phí Search, chính xác 9%, chỉ 12 từ phủ định")
sea_cost = sum(agg(by_camp[c])["Chi_phi"] for c in by_camp if c.startswith("SEA_"))
P(f"  Chi phí Search toàn kỳ={vnd(sea_cost)} → 71% đối sánh rộng ≈ {vnd(sea_cost*0.71)}")

P("-- A7. Địa lý ngoài vùng bán --")
geo = []
with open("/home/docdang/Projects/google-ads/test/exam-vinhomes/sheets/06_DIA_LY.csv", encoding="utf-8-sig") as f:
    for r in csv.DictReader(f):
        if r["Khu vực"] and r["Khu vực"] != "TỔNG" and r["Chi phí (đ)"]:
            geo.append((r["Khu vực"], float(r["Chi phí (đ)"]), float(r["Lead CRM"]),
                        float(r["Lead chất lượng (SQL)"]), float(r["Đặt cọc"])))
far = [g for g in geo if any(k in g[0] for k in ["Hà Nội","Đà Nẵng","Cần Thơ","ngoài Việt Nam"])]
P(f"  Hà Nội + Đà Nẵng + Cần Thơ/ĐBSCL + ngoài VN: chi phí={vnd(sum(g[1] for g in far))} "
  f"({sum(g[1] for g in far)/TOT['Chi_phi']:.1%}), lead={sum(g[2] for g in far):.0f}, "
  f"SQL={sum(g[3] for g in far):.0f}, cọc={sum(g[4] for g in far):.0f}")
for g in far:
    P(f"     {g[0]:50s} {vnd(g[1]):>14s} SQL={g[3]:.0f} CP/SQL={vnd(div(g[1],g[3]))} cọc={g[4]:.0f}")
core = [g for g in geo if "TP.HCM" in g[0]]
P(f"  Lõi TP.HCM: chi phí={vnd(sum(g[1] for g in core))} ({sum(g[1] for g in core)/TOT['Chi_phi']:.1%}) "
  f"SQL={sum(g[3] for g in core):.0f} cọc={sum(g[4] for g in core):.0f} "
  f"CP/SQL={vnd(div(sum(g[1] for g in core), sum(g[3] for g in core)))}")
P(f"  LƯU Ý DỮ LIỆU: tổng lead sheet 06 = {sum(g[2] for g in geo):.0f} vs sheet 02 = {TOT['Lead_CRM']:.0f} "
  f"(lệch {sum(g[2] for g in geo)-TOT['Lead_CRM']:.0f}, do làm tròn % chi phí) → dùng sheet 02 làm chuẩn")

P("-- A8. Khung giờ / thiết bị / ngày trong tuần --")
P("  (sheet 07) 20:00–24:00 chiếm 22,7% chi phí (0,187+0,04) nhưng tỷ lệ gọi lại <30' chỉ 21%/12%")
c2023 = 337261419 + 72141480
P(f"     chi phí 20:00–24:00 = {vnd(c2023)} = {c2023/TOT['Chi_phi']:.1%}; SQL=134; cọc=3")
P(f"     CP/SQL khung 20-24h = {vnd(c2023/134)} vs khung 09-12h = {vnd(302994216/121)}")
P("  (sheet 07B) Di động: 78,1% chi phí, CVR 2,03%, CP/SQL 3.042.251đ; "
  "Máy tính: 16,7% chi phí, CVR 4,02%, CP/SQL 1.847.796đ")
P(f"     Chênh CP/SQL di động/máy tính = {3042251/1847796:.2f}x")
P("  (sheet 07C) T7+CN: chi phí 503.810.000đ, 6 cọc/178 SQL, chỉ 2 sale trực")
P(f"     T7+CN = {(262814000+240996000)/TOT['Chi_phi']:.1%} chi phí; CP/SQL={vnd((262814000+240996000)/178)}")
P(f"     T3+T4: chi phí={vnd(259227000+260849000)} SQL={83+79} cọc=2 CP/SQL={vnd((259227000+260849000)/162)}")

P("-- A9. Tốc độ phản hồi lead (sheet 08A) --")
resp = [("Dưới 5 phút",281,0.87,0.231,0.0182),("5–30 phút",485,0.74,0.154,0.0121),
        ("30'–2h",588,0.58,0.086,0.0058),("2–12h",536,0.41,0.042,0.0021),
        ("Trên 12h",664,0.22,0.011,0.0004)]
tot_lead_resp = sum(x[1] for x in resp)
coc_now = sum(x[1]*x[4] for x in resp)
P(f"  Tổng lead phân loại={tot_lead_resp}; cọc kỳ vọng theo phân bố hiện tại={coc_now:.1f}")
for tgt, lbl in [(0.0182,"tất cả <5 phút"),(0.0121,"tất cả <30 phút")]:
    P(f"  Nếu {lbl}: cọc kỳ vọng = {tot_lead_resp*tgt:.1f} → chênh {tot_lead_resp*tgt-coc_now:+.1f} cọc "
      f"= {vnd((tot_lead_resp*tgt-coc_now)*HH)} hoa hồng")
mix = 0.5*0.0182 + 0.3*0.0121 + 0.2*0.0058
P(f"  Kịch bản thực tế hơn (50% <5', 30% 5–30', 20% 30'–2h): cọc={tot_lead_resp*mix:.1f} "
  f"→ chênh {tot_lead_resp*mix-coc_now:+.1f} cọc = {vnd((tot_lead_resp*mix-coc_now)*HH)}")
P(f"  Lead bị bỏ sót (08B): 118+96+61 = {118+96+61} lead → theo CPL thực tế = "
  f"{vnd((118+96+61)*CPL_REAL)}; quy ra cọc = {(118+96+61)*sql_rate*coc_per_sql:.1f} = "
  f"{vnd((118+96+61)*sql_rate*coc_per_sql*HH)} hoa hồng")
P(f"  47% lead được gọi lại sau 2 giờ (0,21+0,26) — benchmark 09: >2h là ngưỡng báo động")

P("-- A10. Trang đích v1 vs v2 (sheet 10C) --")
P("  v1 (N1–57): 52.410 phiên, tương tác 34,2%, hoàn tất form 20,4%, LCP 4,8s")
P("  v2 (N58–90): 42.938 phiên, tương tác 58,7%, hoàn tất form 28,0%, LCP 1,9s")
P(f"  Nếu v1 đạt tỷ lệ hoàn tất form của v2: {4912} form_start × 28,0% = {4912*0.280047:.0f} lead "
  f"vs thực tế 1002 → mất {4912*0.280047-1002:.0f} lead")
P(f"  → giá trị mất theo CPL thực tế = {vnd((4912*0.280047-1002)*CPL_REAL)}; "
  f"quy ra cọc = {(4912*0.280047-1002)*sql_rate*coc_per_sql:.1f} = "
  f"{vnd((4912*0.280047-1002)*sql_rate*coc_per_sql*HH)}")
P("  Di động v1 hoàn tất form chỉ 16,1% vs máy tính 34,8% (10C chi tiết thiết bị)")

P("-- A11. Mô hình phân bổ (sheet 10D) --")
P("  Nhấp cuối vs Dựa trên dữ liệu: Brand 592→401 (-32,3%); YT 43→165 (+283,7%); "
  "GDN 132→186 (+40,9%); Generic 418→402 (-3,8%); PMax 510→466 (-8,6%); ngoài Ads 0→71")
P("  ⇒ Brand đang được ghi công QUÁ 191 lead; YT/GDN bị ghi công THIẾU 176 lead")

P("-- A12. Cấu hình tài khoản (sheet 05) — rủi ro không định lượng trực tiếp --")
P("  Search Partners BẬT + Display Network trong Search campaign BẬT (cả 3 chiến dịch Search)")
P("  Điểm chất lượng TB 5,2/10, trải nghiệm trang đích 'Dưới trung bình'")
P("  31 từ khóa/nhóm, 1 RSA/nhóm; 12 từ phủ định; không có ngân sách chia sẻ")
P("  Enhanced conversions TẮT; không nhập chuyển đổi ngoại tuyến; CRM không lưu GCLID")
P("  Không có reCAPTCHA/OTP → giải thích 31% trùng SĐT của PMax (sheet 08C)")
P("  Tiện ích: chỉ 4 sitelink; thiếu Cuộc gọi, Lead form, Vị trí, Chú thích, Hình ảnh")
P("  Generic + Competitor dùng 'Tối đa hóa số lần nhấp' không đặt trần CPC → "
  f"CPC Generic={vnd(div(agg(by_camp['SEA_Generic_NhaPho_CanHo_TayBac'])['Chi_phi'],agg(by_camp['SEA_Generic_NhaPho_CanHo_TayBac'])['Nhap_chuot']))} "
  f"(benchmark báo động >60.000đ), CPC Competitor={vnd(div(cp['Chi_phi'],cp['Nhap_chuot']))}")

P("-- A13. GTM: 34 thẻ, 412KB JS bên thứ ba, +0,8s LCP; GA4 config trùng lặp từ N31 --")
P("  Không có cảnh báo chuyển đổi=0 → sự cố N44–46 mất 3 ngày mới phát hiện")
P(f"  zalo_click 894 lượt + file_download 1.206 lượt chưa đo/chưa nhập (sheet 10E) — "
  f"tín hiệu ý định bị bỏ (đăng ký từ N71, GTM v26)")

P("-- A14. Tổng lãng phí có thể quy tiền (không cộng dồn trùng nhau) --")
waste = {
  "PMax (chi phí, 0 doanh thu)": pm["Chi_phi"],
  "Competitor (chi phí, 0 doanh thu)": cp["Chi_phi"],
  "YouTube (chi phí, 0 doanh thu)": agg(by_camp["YT_Video_TVC_MoBan"])["Chi_phi"],
  "GDN Remarketing (chi phí, 0 doanh thu)": agg(by_camp["GDN_Remarketing_Web30d"])["Chi_phi"],
  "Địa lý ngoài vùng bán (HN/ĐN/CT/ngoài VN)": sum(g[1] for g in far),
  "Cụm từ 0 SQL trong báo cáo search terms": sum(x[3] for x in zero),
}
for k, v in sorted(waste.items(), key=lambda x: -x[1]):
    P(f"  {k:48s} {vnd(v):>16s} ({v/TOT['Chi_phi']:.1%})")
P("  (các dòng trên CHỒNG LẤN nhau — không cộng tổng)")
lost_rev = {
  "Lỗi kỹ thuật chưa sửa (370–480 lead)": (lo*sql_rate*coc_per_sql*HH, hi*sql_rate*coc_per_sql*HH),
  "LP v1 kém (≈374 lead)": ((4912*0.280047-1002)*sql_rate*coc_per_sql*HH,)*2,
  "Lead bỏ sót không ai gọi (275 lead)": ((118+96+61)*sql_rate*coc_per_sql*HH,)*2,
  "Phản hồi chậm (nâng SLA)": ((tot_lead_resp*mix-coc_now)*HH, (tot_lead_resp*0.0182-coc_now)*HH),
  "Mất thẻ N44–46 (63 lead không có trong Ads)": (lost_tag*sql_rate*coc_per_sql*HH,)*2,
}
P("  Doanh thu (hoa hồng) bỏ lỡ, ước tính:")
for k, v in lost_rev.items():
    P(f"  {k:48s} {vnd(v[0])} – {vnd(v[1])}")

# ---------------- C: phân bổ ngân sách ----------------
P(""); P("="*70); P("== C. KIỂM TRA PHÂN BỔ NGÂN SÁCH 2,1 TỶ ==")
plan = {
 "GĐ1 (N1–30)": {"SEA_Brand": 150_000_000, "SEA_Generic_Cluster": 250_000_000,
                 "SEA_Competitor": 0, "PMAX_Feed_Lead": 60_000_000,
                 "GDN_Remarketing": 30_000_000, "YT_Video": 0, "Dự phòng": 10_000_000},
 "GĐ2 (N31–60)": {"SEA_Brand": 180_000_000, "SEA_Generic_Cluster": 300_000_000,
                  "SEA_Competitor": 20_000_000, "PMAX_Feed_Lead": 110_000_000,
                  "GDN_Remarketing": 40_000_000, "YT_Video": 20_000_000, "Dự phòng": 30_000_000},
 "GĐ3 (N61–90)": {"SEA_Brand": 220_000_000, "SEA_Generic_Cluster": 340_000_000,
                  "SEA_Competitor": 20_000_000, "PMAX_Feed_Lead": 150_000_000,
                  "GDN_Remarketing": 60_000_000, "YT_Video": 60_000_000, "Dự phòng": 50_000_000},
}
gt = 0
camps = ["SEA_Brand","SEA_Generic_Cluster","SEA_Competitor","PMAX_Feed_Lead","GDN_Remarketing","YT_Video","Dự phòng"]
P(f"{'Chiến dịch':24s}" + "".join(f"{g:>18s}" for g in plan) + f"{'TỔNG':>18s}{'%':>8s}")
for c in camps:
    tot_c = sum(plan[g][c] for g in plan)
    gt += tot_c
    P(f"{c:24s}" + "".join(f"{vnd(plan[g][c]):>18s}" for g in plan) + f"{vnd(tot_c):>18s}{tot_c/2_100_000_000:>7.1%}")
P(f"{'TỔNG GIAI ĐOẠN':24s}" + "".join(f"{vnd(sum(plan[g].values())):>18s}" for g in plan) + f"{vnd(gt):>18s}")
P(f"  Kiểm tra tổng = 2.100.000.000? {gt == 2_100_000_000} (chênh {vnd(gt-2_100_000_000)})")
P(f"  Ngân sách/ngày bình quân: " + ", ".join(f"{g}={vnd(sum(plan[g].values())/30)}" for g in plan))

P("-- Dự báo kết quả kế hoạch (dùng tỷ lệ Search GĐ3 làm cơ sở) --")
sql_lead_p = div(a3["Lead_SQL"], a3["Lead_CRM"])
coc_sql_p = div(a3["Dat_Coc"], a3["Lead_SQL"])
for cps in [1_800_000, 2_000_000, 2_200_000]:
    sqls = 2_100_000_000/cps
    P(f"  Nếu CP/SQL={vnd(cps)} → SQL={sqls:.0f}, lead thô={sqls/sql_lead_p:.0f}, "
      f"cọc={sqls*coc_sql_p:.1f}, DT={vnd(sqls*coc_sql_p*HH)}, ROAS={sqls*coc_sql_p*HH/2_100_000_000:.2f}x")
P(f"  Lead thô/ngày ở kịch bản CP/SQL 2,0tr = {2_100_000_000/2_000_000/sql_lead_p/90:.1f} "
  f"(năng lực sale bình quân có người trực ≈ {(2*12*2+8*12*5)/7:.0f}/ngày) → khả thi")

# ---------------- D3: PMax vs Brand ----------------
P(""); P("="*70); P("== D3. PMax CP/chuyển đổi thấp nhất — bóc tách ==")
P(f"{'Chiến dịch':40s}{'CP/convAds':>15s}{'CP/lead CRM':>15s}{'CP/SQL':>16s}{'CP/cọc':>18s}{'ROAS':>9s}")
for c in list(by_camp) + ["TOÀN KỲ"]:
    x = b1[c]
    P(f"{c:40s}{vnd(x['cpl_ads']):>15s}{vnd(x['cpl_crm']):>15s}{vnd(x['cp_sql']):>16s}"
      f"{(vnd(x['cp_coc']) if x['Dat_Coc'] else '∞ (0 cọc)'):>18s}"
      f"{div(x['DoanhThu_HoaHong'],x['Chi_phi']):>8.2f}x")
P(f"  PMax CP/convAds={vnd(b1['PMAX_VinhomesHM_Lead']['cpl_ads'])} rẻ nhất; nhưng CP/SQL="
  f"{vnd(b1['PMAX_VinhomesHM_Lead']['cp_sql'])} — đắt gấp "
  f"{b1['PMAX_VinhomesHM_Lead']['cp_sql']/b1['SEA_Brand_Vinhomes_HocMon']['cp_sql']:.1f} lần Brand "
  f"({vnd(b1['SEA_Brand_Vinhomes_HocMon']['cp_sql'])}) và 0 cọc")
P(f"  Nếu dồn toàn bộ 2,1 tỷ vào PMax theo CP/SQL hiện tại → SQL="
  f"{2_100_000_000/b1['PMAX_VinhomesHM_Lead']['cp_sql']:.0f}, cọc theo lịch sử PMax = 0 → ROAS = 0")

# ---------------- D1: Brand ----------------
P(""); P("="*70); P("== D1. Bảo vệ ngân sách Brand ==")
x = b1["SEA_Brand_Vinhomes_HocMon"]
P(f"  Brand: chi phí={vnd(x['Chi_phi'])} ({x['Chi_phi']/TOT['Chi_phi']:.1%} tài khoản) "
  f"DT={vnd(x['DoanhThu_HoaHong'])} ({x['DoanhThu_HoaHong']/TOT['DoanhThu_HoaHong']:.1%} doanh thu) "
  f"ROAS={div(x['DoanhThu_HoaHong'],x['Chi_phi']):.2f}x cọc={x['Dat_Coc']:.0f}/{TOT['Dat_Coc']:.0f}")
g = b1["SEA_Generic_NhaPho_CanHo_TayBac"]
P(f"  Generic: chi phí={vnd(g['Chi_phi'])} ({g['Chi_phi']/TOT['Chi_phi']:.1%}) DT={vnd(g['DoanhThu_HoaHong'])} "
  f"ROAS={div(g['DoanhThu_HoaHong'],g['Chi_phi']):.2f}x CP/SQL={vnd(g['cp_sql'])} vs Brand {vnd(x['cp_sql'])}")
P(f"  Đổi 1đ Brand sang Generic: mất {div(x['DoanhThu_HoaHong'],x['Chi_phi']):.2f}đ, được "
  f"{div(g['DoanhThu_HoaHong'],g['Chi_phi']):.2f}đ → lỗ ròng "
  f"{div(x['DoanhThu_HoaHong'],x['Chi_phi'])-div(g['DoanhThu_HoaHong'],g['Chi_phi']):.2f}đ/1đ chuyển")
P(f"  Chuyển toàn bộ {vnd(x['Chi_phi'])} → mất DT ≈ "
  f"{vnd(x['Chi_phi']*(div(x['DoanhThu_HoaHong'],x['Chi_phi'])-div(g['DoanhThu_HoaHong'],g['Chi_phi'])))}")
P(f"  Nhượng bộ mô hình phân bổ: nếu chỉ ghi công Brand 401/592 lead (DDA, sheet 10D) → "
  f"ROAS Brand điều chỉnh ≈ {div(x['DoanhThu_HoaHong'],x['Chi_phi'])*401/592:.2f}x — vẫn > "
  f"{div(g['DoanhThu_HoaHong'],g['Chi_phi']):.2f}x của Generic và > 3,0x mục tiêu")
P(f"  Brand mất IS do ngân sách {pct(lb_br)} → còn dư địa MỞ RỘNG, không phải cắt")

# ---------------- D4: cắt còn 1,2 tỷ ----------------
P(""); P("="*70); P("== D4. Kịch bản ngân sách 1,2 tỷ ==")
cut = {"SEA_Brand": 420_000_000, "SEA_Generic_Cluster (lõi TP.HCM, exact/phrase)": 520_000_000,
       "PMAX_Feed_Lead (giới hạn, tCPA)": 130_000_000, "GDN_Remarketing": 80_000_000,
       "Dự phòng/test": 50_000_000, "SEA_Competitor": 0, "YT_Video": 0}
for k, v in cut.items():
    P(f"  {k:48s} {vnd(v):>16s} {v/1_200_000_000:>7.1%}")
P(f"  TỔNG = {vnd(sum(cut.values()))} (khớp 1,2 tỷ: {sum(cut.values())==1_200_000_000})")
for cps in [1_800_000, 2_000_000]:
    sqls = 1_200_000_000/cps
    P(f"  CP/SQL={vnd(cps)} → SQL={sqls:.0f} cọc={sqls*coc_sql_p:.1f} DT={vnd(sqls*coc_sql_p*HH)} "
      f"ROAS={sqls*coc_sql_p*HH/1_200_000_000:.2f}x")

txt = "\n".join(out)
print(txt)
with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "agent-3-calc-output.txt"), "w", encoding="utf-8") as f:
    f.write(txt)

# --- self-check (ponytail: 1 check, fails nếu logic đối chiếu hoặc tổng ngân sách sai) ---
assert abs(TOT["Chi_phi"] - 1_803_537_000) < 1, TOT["Chi_phi"]
assert TOT["ChuyenDoi_Ads"] == 3820 and TOT["Lead_CRM"] == 2557 and TOT["Dat_Coc"] == 18
assert ads_conv - dup - junk + lost_tag == crm
assert gt == 2_100_000_000 and sum(cut.values()) == 1_200_000_000
