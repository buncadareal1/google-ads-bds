#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Script tính toàn bộ số liệu cho bài làm agent-7.md.
Nguồn: /home/docdang/Downloads/du_lieu_google_ads_90_ngay_1.csv (= sheet 02_DU_LIEU_NGAY)
       + các sheet CSV trong ../sheets/
Chạy: python3 agent-7-calc.py   (chỉ dùng stdlib)
"""
import csv, os, collections

CSV = "/home/docdang/Downloads/du_lieu_google_ads_90_ngay_1.csv"
SHEETS = "/home/docdang/Projects/google-ads/test/exam-vinhomes/sheets"

NUM = ["Hien_thi","Nhap_chuot","Chi_phi","ChuyenDoi_Ads","Lead_CRM","Lead_SQL",
       "Di_Xem_Nha","Booking","Dat_Coc","DoanhThu_HoaHong"]
FLT = ["Impr_Share","Mat_IS_NganSach","Mat_IS_ThuHang"]

rows = []
with open(CSV, encoding="utf-8-sig") as f:
    for r in csv.DictReader(f):
        for k in NUM: r[k] = int(float(r[k]))
        for k in FLT: r[k] = float(r[k])
        r["Ngay_thu"] = int(r["Ngay_thu"]); r["Tuan"] = int(r["Tuan"])
        rows.append(r)

def agg(rs):
    d = {k: sum(r[k] for r in rs) for k in NUM}
    d["n"] = len(rs)
    return d

def div(a, b): return a / b if b else None
def vnd(x): return "-" if x is None else f"{round(x):,}".replace(",", ".")
def pct(x, nd=1): return "-" if x is None else f"{x*100:.{nd}f}%"

def kpis(d):
    return dict(
        cpl_ads=div(d["Chi_phi"], d["ChuyenDoi_Ads"]),
        cpl_crm=div(d["Chi_phi"], d["Lead_CRM"]),
        cp_sql=div(d["Chi_phi"], d["Lead_SQL"]),
        cp_coc=div(d["Chi_phi"], d["Dat_Coc"]),
        roas=div(d["DoanhThu_HoaHong"], d["Chi_phi"]),
        sql_rate=div(d["Lead_SQL"], d["Lead_CRM"]),
        ads_vs_crm=div(d["ChuyenDoi_Ads"], d["Lead_CRM"]),
    )

OUT = []
def P(*a):
    s = " ".join(str(x) for x in a)
    OUT.append(s); print(s)

TOT = agg(rows)
P("=" * 78)
P("[0] TỔNG QUAN 90 NGÀY (02/03–30/05/2026)")
P("=" * 78)
k = kpis(TOT)
P(f"Chi phí        : {vnd(TOT['Chi_phi'])} đ   | Hiển thị {TOT['Hien_thi']:,} | Nhấp {TOT['Nhap_chuot']:,}")
P(f"CTR toàn TK    : {pct(div(TOT['Nhap_chuot'],TOT['Hien_thi']),2)}  | CPC TB {vnd(div(TOT['Chi_phi'],TOT['Nhap_chuot']))} đ")
P(f"ChuyenDoi_Ads  : {TOT['ChuyenDoi_Ads']}  | Lead_CRM {TOT['Lead_CRM']} | SQL {TOT['Lead_SQL']}")
P(f"Đi xem {TOT['Di_Xem_Nha']} | Booking {TOT['Booking']} | Cọc {TOT['Dat_Coc']} | DT {vnd(TOT['DoanhThu_HoaHong'])} đ")
P(f"CPL_Ads {vnd(k['cpl_ads'])} | CPL_CRM {vnd(k['cpl_crm'])} | CP/SQL {vnd(k['cp_sql'])} | CP/cọc {vnd(k['cp_coc'])}")
P(f"ROAS {k['roas']:.3f}x | SQL/Lead {pct(k['sql_rate'])} | Ads/CRM {k['ads_vs_crm']:.3f}x")

# ---------- B1 ----------
P("")
P("=" * 78)
P("[B1] CPL/CP-SQL/CP-CỌC THEO CHIẾN DỊCH (toàn kỳ)")
P("=" * 78)
by_cd = collections.OrderedDict()
for r in rows: by_cd.setdefault(r["Chien_dich"], []).append(r)
P(f"{'Chiến dịch':34}{'Chi phí':>16}{'%':>7}{'CĐ_Ads':>8}{'Lead':>7}{'SQL':>6}{'Cọc':>5}"
  f"{'CPL_Ads':>12}{'CPL_CRM':>12}{'CP/SQL':>14}{'ROAS':>7}")
camp_stat = {}
for cd, rs in by_cd.items():
    d = agg(rs); kk = kpis(d); camp_stat[cd] = (d, kk)
    P(f"{cd:34}{vnd(d['Chi_phi']):>16}{d['Chi_phi']/TOT['Chi_phi']*100:>6.1f}%"
      f"{d['ChuyenDoi_Ads']:>8}{d['Lead_CRM']:>7}{d['Lead_SQL']:>6}{d['Dat_Coc']:>5}"
      f"{vnd(kk['cpl_ads']):>12}{vnd(kk['cpl_crm']):>12}{vnd(kk['cp_sql']):>14}"
      f"{(f'{kk[chr(39)+chr(39)]}' if False else (f'{kk[
      ]:.2f}' if False else '')):>0}", end="")
    OUT.pop(); # tránh format lỗi, in lại gọn bên dưới
    line = (f"{cd:34}{vnd(d['Chi_phi']):>16}{d['Chi_phi']/TOT['Chi_phi']*100:>6.1f}%"
            f"{d['ChuyenDoi_Ads']:>8}{d['Lead_CRM']:>7}{d['Lead_SQL']:>6}{d['Dat_Coc']:>5}"
            f"{vnd(kk['cpl_ads']):>12}{vnd(kk['cpl_crm']):>12}{vnd(kk['cp_sql']):>14}"
            f"{(kk['roas'] or 0):>7.2f}")
    OUT.append(line); print(line)
d = TOT; kk = k
P(f"{'TỔNG':34}{vnd(d['Chi_phi']):>16}{100.0:>6.1f}%{d['ChuyenDoi_Ads']:>8}{d['Lead_CRM']:>7}"
  f"{d['Lead_SQL']:>6}{d['Dat_Coc']:>5}{vnd(kk['cpl_ads']):>12}{vnd(kk['cpl_crm']):>12}"
  f"{vnd(kk['cp_sql']):>14}{kk['roas']:>7.2f}")
P("CP/cọc từng chiến dịch:")
for cd, (d, kk) in camp_stat.items():
    P(f"   {cd:34} cọc={d['Dat_Coc']:>2}  CP/cọc={vnd(kk['cp_coc']):>14} đ  "
      f"SQL/Lead={pct(kk['sql_rate'])}  Ads/CRM={(kk['ads_vs_crm'] or 0):.2f}x")

# ---------- B2 ----------
P("")
P("=" * 78)
P("[B2] ROAS THEO GIAI ĐOẠN")
P("=" * 78)
by_gd = collections.OrderedDict()
for r in rows: by_gd.setdefault(r["Giai_doan"], []).append(r)
P(f"{'GĐ':6}{'Chi phí':>16}{'Doanh thu':>16}{'ROAS':>8}{'Cọc':>6}{'Lead':>7}{'SQL':>6}{'CP/SQL':>14}")
for gd, rs in by_gd.items():
    d = agg(rs); kk = kpis(d)
    P(f"{gd:6}{vnd(d['Chi_phi']):>16}{vnd(d['DoanhThu_HoaHong']):>16}{kk['roas']:>8.2f}"
      f"{d['Dat_Coc']:>6}{d['Lead_CRM']:>7}{d['Lead_SQL']:>6}{vnd(kk['cp_sql']):>14}")
P(f"{'TOÀN KỲ':6}{vnd(TOT['Chi_phi']):>16}{vnd(TOT['DoanhThu_HoaHong']):>16}{k['roas']:>8.2f}"
  f"{TOT['Dat_Coc']:>6}{TOT['Lead_CRM']:>7}{TOT['Lead_SQL']:>6}{vnd(k['cp_sql']):>14}")
P("ROAS chiến dịch × giai đoạn (chỉ CD có doanh thu):")
for cd, rs in by_cd.items():
    parts = []
    for gd in by_gd:
        d = agg([r for r in rs if r["Giai_doan"] == gd])
        parts.append(f"{gd}={(div(d['DoanhThu_HoaHong'],d['Chi_phi']) or 0):.2f}x")
    P(f"   {cd:34} " + "  ".join(parts))

# ---------- B3 ----------
P("")
P("=" * 78)
P("[B3] PHỄU CHUYỂN ĐỔI")
P("=" * 78)
def funnel(d, label):
    P(f"{label}: Lead {d['Lead_CRM']} → SQL {d['Lead_SQL']} ({pct(div(d['Lead_SQL'],d['Lead_CRM']))}) "
      f"→ Đi xem {d['Di_Xem_Nha']} ({pct(div(d['Di_Xem_Nha'],d['Lead_SQL']))}) "
      f"→ Booking {d['Booking']} ({pct(div(d['Booking'],d['Di_Xem_Nha']))}) "
      f"→ Cọc {d['Dat_Coc']} ({pct(div(d['Dat_Coc'],d['Booking']))})")
    P(f"   Lead→Cọc {pct(div(d['Dat_Coc'],d['Lead_CRM']),2)} | SQL→Cọc {pct(div(d['Dat_Coc'],d['Lead_SQL']),2)}"
      f" | Đi xem→Cọc {pct(div(d['Dat_Coc'],d['Di_Xem_Nha']),2)}")
funnel(TOT, "TOÀN KỲ")
for gd, rs in by_gd.items(): funnel(agg(rs), gd)
P("Phễu theo chiến dịch:")
for cd, (d, kk) in camp_stat.items(): funnel(d, "   " + cd)

# ---------- B4 ----------
P("")
P("=" * 78)
P("[B4] NGƯỢC TỪ KPI 32 CỌC / 2,1 TỶ")
P("=" * 78)
BUDGET = 2_100_000_000; TARGET_COC = 32; COMMISSION = 181_000_000
sql_view = div(TOT["Di_Xem_Nha"], TOT["Lead_SQL"])
view_book = div(TOT["Booking"], TOT["Di_Xem_Nha"])
book_coc = div(TOT["Dat_Coc"], TOT["Booking"])
sql_coc_hist = div(TOT["Dat_Coc"], TOT["Lead_SQL"])
# GĐ3 làm cơ sở (vận hành đã cải thiện: SLA 15', LP v2)
g3 = agg(by_gd["GĐ3"])
sql_coc_g3 = div(g3["Dat_Coc"], g3["Lead_SQL"])
sqlrate_g3 = div(g3["Lead_SQL"], g3["Lead_CRM"])
P(f"Tỷ lệ lịch sử toàn kỳ : SQL→Xem {pct(sql_view)}, Xem→Book {pct(view_book)}, Book→Cọc {pct(book_coc)},"
  f" SQL→Cọc {pct(sql_coc_hist,2)}")
P(f"Tỷ lệ GĐ3 (cơ sở dùng): SQL→Cọc {pct(sql_coc_g3,2)} | SQL/Lead {pct(sqlrate_g3)}"
  f" | SQL→Xem {pct(div(g3['Di_Xem_Nha'],g3['Lead_SQL']))}")
for name, r_sqlcoc, r_sqlrate in [
    ("KB thận trọng = tỷ lệ GĐ3", sql_coc_g3, sqlrate_g3),
    ("KB cơ sở = GĐ3 +25% (SLA 15' + LP v2 full kỳ)", sql_coc_g3 * 1.25, 0.35),
    ("KB tốt = 5,0% SQL→cọc, SQL/Lead 40%", 0.05, 0.40),
]:
    need_sql = TARGET_COC / r_sqlcoc
    need_lead = need_sql / r_sqlrate
    P(f"{name}:")
    P(f"   SQL→cọc {pct(r_sqlcoc,2)} ⇒ cần {need_sql:.0f} SQL; SQL/Lead {pct(r_sqlrate)} ⇒ cần {need_lead:.0f} lead thô")
    P(f"   CP/SQL tối đa = 2,1 tỷ / {need_sql:.0f} = {vnd(BUDGET/need_sql)} đ"
      f" | CPL tối đa = {vnd(BUDGET/need_lead)} đ | CP/cọc = {vnd(BUDGET/TARGET_COC)} đ")
P(f"Kiểm tra tải sale: 8 sale × 12 lead/ngày × 90 = {8*12*90} lead/90 ngày (trần lý thuyết).")
for nl in [640, 731, 800, 914]:
    P(f"   {nl} lead ⇒ {nl/90:.1f} lead/ngày (GĐ3 thực tế {g3['Lead_CRM']/30:.1f}/ngày)")

# ---------- B5 ----------
P("")
P("=" * 78)
P("[B5] ĐIỂM HÒA VỐN / TRẦN CHI PHÍ MỖI CỌC")
P("=" * 78)
P(f"ROAS 3,0x ⇒ chi phí QC tối đa/cọc = {COMMISSION}/3 = {vnd(COMMISSION/3)} đ")
P(f"ROAS 1,0x (hòa vốn trên chi phí QC) = {vnd(COMMISSION)} đ/cọc")
P(f"Sau chia 45% sale + 20% vận hành ⇒ đại lý còn {vnd(COMMISSION*0.35)} đ/cọc;"
  f" hòa vốn thật (biên đóng góp = 0) = {vnd(COMMISSION*0.35)} đ/cọc ⇒ ROAS tương đương {1/0.35:.2f}x")
P(f"Thực tế 90 ngày qua: CP/cọc = {vnd(k['cp_coc'])} đ ⇒ vượt trần ROAS 3x"
  f" {k['cp_coc']/(COMMISSION/3):.2f} lần")
P(f"Với 2,1 tỷ & ROAS 3,0x ⇒ doanh thu HH cần = {vnd(BUDGET*3)} đ = {BUDGET*3/COMMISSION:.1f} cọc"
  f" ⇒ KPI 32 cọc tương đương ROAS {32*COMMISSION/BUDGET:.2f}x (nhất quán)")

# ---------- B6 ----------
P("")
P("=" * 78)
P("[B6] ĐỐI CHIẾU 3 NGUỒN (sheet 10_GA4 mục A + 12_GTM v23/v24)")
P("=" * 78)
gl, c2c_tot, c2c_uni, vpp, e30 = 1715, 1132, 779, 612, 361
P(f"Google Ads 'Chuyển đổi' = {gl}+{c2c_tot}+{vpp}+{e30} = {gl+c2c_tot+vpp+e30} (khớp 3.820)")
dup = c2c_tot - c2c_uni; junk = vpp + e30
P(f"(a) Đếm trùng nhấp gọi   : {c2c_tot} lượt − {c2c_uni} người = {dup} ({dup/3820*100:.1f}% của 3.820)")
P(f"(b) Sự kiện rác (không phải lead): view_price_page {vpp} + engaged_30s {e30} = {junk} ({junk/3820*100:.1f}%)")
P(f"⇒ Lead thật đo được bằng thẻ = 3820 − {dup} − {junk} = {3820-dup-junk} (khớp 2.494)")
P(f"(c) Mất thẻ N44–46 (GTM v23 đổi class .form-dk-v1→.form-register) = 63 lead có trong CRM,"
  f" không có trong Ads/GA4")
P(f"⇒ CRM = 2.494 + 63 = {2494+63} (khớp 2.557)")
P(f"Tổng chênh Ads−CRM = 3820 − 2557 = {3820-2557} = +{dup} trùng +{junk} rác −63 mất thẻ"
  f" = {dup+junk-63}  {'✔' if dup+junk-63 == 3820-2557 else '✘'}")
P(f"Tỷ lệ thổi phồng Ads/CRM = {3820/2557:.3f}x (ngưỡng báo động sheet 09 = >1,8x;"
  f" trung bình ngành 1,2–1,5x)")
P(f"Nếu chỉ tính lead thật: CPL thật = {vnd(TOT['Chi_phi']/2557)} đ vs CPL Ads báo"
  f" {vnd(TOT['Chi_phi']/3820)} đ ⇒ Ads đang báo rẻ hơn thực tế {(1-3820**-1*0+0)+0:.0f}"
  f"{(TOT['Chi_phi']/2557)/(TOT['Chi_phi']/3820)-1:.1%}")

# --- ngày 44-46 ---
P("")
P("Kiểm chứng sự cố N44–46 trong sheet 02 (ChuyenDoi_Ads vs Lead_CRM theo ngày):")
by_day = collections.OrderedDict()
for r in rows: by_day.setdefault(r["Ngay_thu"], []).append(r)
for dnum in [42, 43, 44, 45, 46, 47, 48]:
    d = agg(by_day[dnum])
    P(f"   Ngày {dnum:>2} ({by_day[dnum][0]['Ngay']}): CĐ_Ads={d['ChuyenDoi_Ads']:>3}"
      f" Lead_CRM={d['Lead_CRM']:>3} Chi phí={vnd(d['Chi_phi']):>12}")
lost = agg([r for d in (44, 45, 46) for r in by_day[d]])
P(f"   Tổng N44–46: CĐ_Ads={lost['ChuyenDoi_Ads']} Lead_CRM={lost['Lead_CRM']}"
  f" Chi phí={vnd(lost['Chi_phi'])} đ ⇒ 3 ngày mù tín hiệu cho bidding")

# ---------- B7 ----------
P("")
P("=" * 78)
P("[B7] LEAD MẤT DO LỖI KỸ THUẬT CHƯA SỬA (sheet 11_CLARITY mục C, #4/#5/#6)")
P("=" * 78)
cpl_crm = TOT["Chi_phi"] / TOT["Lead_CRM"]
issues = [("#4 Lỗi JS TypeError e.setDate — Safari iOS, form không gửi được", 4196, 280, 340),
          ("#5 Nút CTA bị khung chat che (<380px)", 2741, 60, 90),
          ("#6 tel: không phản hồi trên desktop (1.847 dead click)", 1204, 30, 50)]
lo = hi = 0
for name, sess, a, b in issues:
    lo += a; hi += b
    P(f"{name}\n   phiên ảnh hưởng {sess:,} | lead mất ước tính {a}–{b}"
      f" | tiền = {vnd(a*cpl_crm)} – {vnd(b*cpl_crm)} đ")
P(f"TỔNG lead mất: {lo}–{hi} (khớp ghi chú sheet 11: 370–480)")
P(f"CPL thực tế (CRM) = {vnd(cpl_crm)} đ ⇒ giá trị lead mất = {vnd(lo*cpl_crm)} – {vnd(hi*cpl_crm)} đ")
P(f"Quy ra SQL (SQL/Lead toàn kỳ {pct(k['sql_rate'])}): {lo*k['sql_rate']:.0f}–{hi*k['sql_rate']:.0f} SQL")
P(f"Quy ra cọc (SQL→cọc {pct(sql_coc_hist,2)}): {lo*k['sql_rate']*sql_coc_hist:.1f}"
  f"–{hi*k['sql_rate']*sql_coc_hist:.1f} cọc = {vnd(lo*k['sql_rate']*sql_coc_hist*COMMISSION)}"
  f" – {vnd(hi*k['sql_rate']*sql_coc_hist*COMMISSION)} đ hoa hồng bỏ lỡ")
P("ĐO ĐƯỢC: số phiên ảnh hưởng, số dead click, tỷ lệ rage/dead click, tỷ lệ lỗi JS (Clarity).")
P("ƯỚC TÍNH (đội UX, không phải số đo): 370–480 lead. Phần quy ra SQL/cọc/tiền là ước tính của tôi,")
P("dùng tỷ lệ thực tế của chính tài khoản; Clarity chỉ lấy mẫu ~92% lưu lượng nên có thể còn thiếu.")

# ---------- Phần A: các phát hiện định lượng ----------
P("")
P("=" * 78)
P("[A] SỐ LIỆU CHO PHẦN CHẨN ĐOÁN")
P("=" * 78)

# A1 PMax
d, kk = camp_stat["PMAX_VinhomesHM_Lead"]
P(f"A-PMax: chi {vnd(d['Chi_phi'])} đ ({d['Chi_phi']/TOT['Chi_phi']*100:.1f}%),"
  f" CĐ_Ads {d['ChuyenDoi_Ads']}, Lead {d['Lead_CRM']}, SQL {d['Lead_SQL']}"
  f" (SQL/Lead {pct(kk['sql_rate'])}), cọc {d['Dat_Coc']}, DT 0 ⇒ ROAS 0")
P(f"   CPL_Ads {vnd(kk['cpl_ads'])} (rẻ nhất TK) nhưng CP/SQL {vnd(kk['cp_sql'])} đ"
  f" (ngưỡng báo động sheet 09 = >5 triệu)")
P(f"   Clarity: 74,3% thoát <3s, phiên trung vị 3s | GA4: tỷ lệ tương tác 8,7%, 11s, 1,09 trang/phiên")
P(f"   08_CRM C: lead dùng được chỉ 7%, trùng SĐT 31%, SĐT sai 24%")
P(f"   Lãng phí ước tính = 93% chi phí PMax không ra lead dùng được ="
  f" {vnd(d['Chi_phi']*0.93)} đ")

# A2 Competitor
d, kk = camp_stat["SEA_Competitor_DoiThu"]
P(f"A-Competitor: chi {vnd(d['Chi_phi'])} đ, Lead {d['Lead_CRM']}, SQL {d['Lead_SQL']},"
  f" cọc 0, DT 0 ⇒ ROAS 0. CP/SQL = {vnd(kk['cp_sql'])} đ. CPC TB"
  f" {vnd(div(d['Chi_phi'],d['Nhap_chuot']))} đ (>2x CPC generic).")
P(f"   ⇒ toàn bộ {vnd(d['Chi_phi'])} đ là lãng phí thuần (0 cọc trong 90 ngày).")

# A3 Brand bị bóp ngân sách
d, kk = camp_stat["SEA_Brand_Vinhomes_HocMon"]
br = by_cd["SEA_Brand_Vinhomes_HocMon"]
mis = sum(r["Mat_IS_NganSach"] for r in br) / len(br)
mir = sum(r["Mat_IS_ThuHang"] for r in br) / len(br)
ish = sum(r["Impr_Share"] for r in br) / len(br)
P(f"A-Brand: chi {vnd(d['Chi_phi'])} đ ({d['Chi_phi']/TOT['Chi_phi']*100:.1f}% NS) nhưng tạo"
  f" {d['Dat_Coc']}/{TOT['Dat_Coc']} cọc và {vnd(d['DoanhThu_HoaHong'])}/"
  f"{vnd(TOT['DoanhThu_HoaHong'])} đ DT ⇒ ROAS {kk['roas']:.2f}x, CP/cọc {vnd(kk['cp_coc'])} đ")
P(f"   IS TB {pct(ish)} (ngưỡng tốt >85%), mất IS do ngân sách TB {pct(mis)}"
  f" (báo động >20%), mất IS do thứ hạng {pct(mir)}")
for gd in by_gd:
    rs = [r for r in br if r["Giai_doan"] == gd]
    dd = agg(rs)
    P(f"   {gd}: IS {pct(sum(r['Impr_Share'] for r in rs)/len(rs))}"
      f" mất IS NS {pct(sum(r['Mat_IS_NganSach'] for r in rs)/len(rs))}"
      f" | chi {vnd(dd['Chi_phi'])} | cọc {dd['Dat_Coc']}"
      f" | ROAS {(div(dd['DoanhThu_HoaHong'],dd['Chi_phi']) or 0):.2f}x")
# ước tính doanh thu bỏ lỡ nếu IS brand lên 85%
brand_rev_per_click = d["DoanhThu_HoaHong"] / d["Nhap_chuot"]
uplift_clicks = d["Nhap_chuot"] * (mis / max(ish, 1e-9))
P(f"   Ước tính: bù mất IS do ngân sách ({pct(mis)}) ⇒ thêm ~{uplift_clicks:,.0f} nhấp"
  f" × DT/nhấp {vnd(brand_rev_per_click)} đ = {vnd(uplift_clicks*brand_rev_per_click)} đ DT bỏ lỡ"
  f" (chi phí thêm ~{vnd(uplift_clicks*d['Chi_phi']/d['Nhap_chuot'])} đ)")

# A4 Search terms rác
P("")
sts = []
with open(os.path.join(SHEETS, "04_SEARCH_TERMS.csv"), encoding="utf-8-sig") as f:
    for r in csv.DictReader(f):
        if not r["Chiến dịch"]: continue
        try: r["Chi phí (đ)"] = float(r["Chi phí (đ)"])
        except ValueError: continue
        r["SQL"] = float(r["Lead chất lượng (SQL)"]); r["Nhấp chuột"] = float(r["Nhấp chuột"])
        sts.append(r)
zero = [r for r in sts if r["SQL"] == 0]
P(f"A-SearchTerms: {len(sts)} cụm từ ≥40 nhấp, tổng chi {vnd(sum(r['Chi phí (đ)'] for r in sts))} đ")
P(f"   {len(zero)} cụm từ có 0 SQL, chi {vnd(sum(r['Chi phí (đ)'] for r in zero))} đ"
  f" = {sum(r['Chi phí (đ)'] for r in zero)/sum(r['Chi phí (đ)'] for r in sts)*100:.1f}% chi phí Search trong bảng")
irrelevant_kw = ["tuyển dụng", "học phí", "thuê", "trọ", "kho xưởng", "việc làm",
                 "lừa đảo", "chung cư mini", "quy hoạch", "giá đất", "100 triệu"]
irr = [r for r in sts if any(x in r["Cụm từ tìm kiếm"] for x in irrelevant_kw)]
P(f"   Trong đó {len(irr)} cụm từ SAI Ý ĐỊNH rõ ràng (tuyển dụng/học phí/thuê/trọ/kho xưởng/"
  f"việc làm/lừa đảo/chung cư mini/quy hoạch/giá đất/100 triệu):"
  f" chi {vnd(sum(r['Chi phí (đ)'] for r in irr))} đ, SQL = {sum(r['SQL'] for r in irr):.0f}")
for r in sorted(irr, key=lambda x: -x["Chi phí (đ)"]):
    P(f"      - {r['Cụm từ tìm kiếm']:38} {r['Loại đối sánh khớp']:9}"
      f" {vnd(r['Chi phí (đ)']):>12} đ  SQL={r['SQL']:.0f}")
P(f"   Cấu hình (05): đối sánh rộng = 71% chi phí Search, chính xác 9%, chỉ 12 từ phủ định,"
  f" không dùng danh sách phủ định chia sẻ")

# A5 địa lý
P("")
geo = []
with open(os.path.join(SHEETS, "06_DIA_LY.csv"), encoding="utf-8-sig") as f:
    for r in csv.DictReader(f):
        if r["Khu vực"] in ("", "TỔNG") or r["Khu vực"].startswith("Ghi chú"): continue
        geo.append((r["Khu vực"], float(r["Chi phí (đ)"]), int(r["Lead CRM"]),
                    int(r["Lead chất lượng (SQL)"]), int(r["Đặt cọc"])))
far = [g for g in geo if g[0] in ("Hà Nội", "Đà Nẵng", "Cần Thơ & ĐBSCL", "Đồng Nai",
                                 "Người dùng ngoài Việt Nam quan tâm đến Việt Nam")]
P(f"A-ĐịaLý: 5 khu vực xa vùng khách mục tiêu (HN, ĐN, Cần Thơ, Đồng Nai, ngoài VN):")
P(f"   chi {vnd(sum(g[1] for g in far))} đ = {sum(g[1] for g in far)/TOT['Chi_phi']*100:.1f}% ngân sách,"
  f" SQL {sum(g[3] for g in far)} = {sum(g[3] for g in far)/643*100:.1f}% SQL, CỌC = {sum(g[4] for g in far)}")
for g in sorted(far, key=lambda x: -x[1]):
    P(f"      - {g[0]:48} {vnd(g[1]):>14} đ  lead {g[2]:>3} SQL {g[3]:>3} cọc {g[4]}"
      f"  CP/SQL {vnd(g[1]/g[3]) if g[3] else '∞'} đ")
core = [g for g in geo if g[0].startswith("TP.HCM")]
P(f"   Lõi TP.HCM: chi {vnd(sum(g[1] for g in core))} đ ({sum(g[1] for g in core)/TOT['Chi_phi']*100:.1f}%),"
  f" SQL {sum(g[3] for g in core)}, cọc {sum(g[4] for g in core)}/18,"
  f" CP/SQL {vnd(sum(g[1] for g in core)/sum(g[3] for g in core))} đ")
P("   Cấu hình 05: nhắm 'Việt Nam toàn quốc' + tùy chọn 'Hiện diện HOẶC quan tâm', không loại trừ.")

# A6 khung giờ / thiết bị / thứ
P("")
P("A-KhungGiờ (07 mục A): 20:00–24:00 chi"
  f" {vnd(337261419+72141480)} đ = {(0.187+0.04)*100:.1f}% NS,"
  f" tỷ lệ gọi lại trong 30' chỉ 21% và 12%, CP/SQL 3,01 và 3,28 triệu (vs 09:00–12:00: 2,50 triệu, gọi lại 93%)")
P("A-ThiếtBị (07 mục B): di động 78,1% chi phí, CVR 2,03%, CP/SQL 3,04 triệu;"
  " máy tính 16,7% chi phí, CVR 4,02%, CP/SQL 1,85 triệu ⇒ chưa điều chỉnh giá thầu theo thiết bị")
wk_cost = 262814000 + 240996000
P(f"A-CuốiTuần (07 mục C): T7+CN chi {vnd(wk_cost)} đ ({wk_cost/TOT['Chi_phi']*100:.1f}% NS)"
  f" nhưng chỉ 2/8 sale trực; cọc T7+CN = 4/18; CP/SQL T7 3,02tr, CN 2,65tr vs T2 2,15tr")

# A7 CRM tốc độ phản hồi
P("")
crm_speed = [("Dưới 5 phút", 281, 0.87, 0.231, 0.0182), ("5–30 phút", 485, 0.74, 0.154, 0.0121),
             ("30' – 2h", 588, 0.58, 0.086, 0.0058), ("2–12h", 536, 0.41, 0.042, 0.0021),
             ("Trên 12h", 664, 0.22, 0.011, 0.0004)]
tot_lead_speed = sum(x[1] for x in crm_speed)
base = crm_speed[0][4]
cur_coc = sum(x[1] * x[4] for x in crm_speed)
best_coc = tot_lead_speed * base
P(f"A-TốcĐộPhảnHồi (08 mục A): {tot_lead_speed} lead phân theo tốc độ gọi lại."
  f" Cọc kỳ vọng hiện tại = {cur_coc:.1f}; nếu 100% gọi <5 phút = {best_coc:.1f}"
  f" ⇒ chênh {best_coc-cur_coc:.1f} cọc = {vnd((best_coc-cur_coc)*COMMISSION)} đ hoa hồng bỏ lỡ")
P(f"   47% lead ({588+536+664-536-664+536+664} = {588+536+664}) được gọi sau 30 phút;"
  f" 26% ({664}) gọi sau 12h (tỷ lệ liên hệ chỉ 22%)")
P(f"   08 mục B: lead bỏ sót không ai gọi = 118+96+61 = {118+96+61} lead"
  f" = {vnd((118+96+61)*cpl_crm)} đ chi phí đã trả cho lead không ai chạm")
P(f"   ⇒ quy ra cọc: {(118+96+61)*k['sql_rate']*sql_coc_hist:.1f} cọc ="
  f" {vnd((118+96+61)*k['sql_rate']*sql_coc_hist*COMMISSION)} đ")

# A8 landing page
P("")
P("A-LandingPage (10 mục C + 05): v1 N1–57 LCP 4,8s, form 7 trường, hoàn tất form 20,4%;"
  " v2 N58–90 LCP 1,9s, form 3 trường, hoàn tất form 28,0% (+37,3%)")
P("   Nếu v1 đạt tỷ lệ hoàn tất của v2: 4.912 form_start × 28,0% ="
  f" {4912*0.280047132757266:.0f} lead thay vì 1.002 ⇒ +{4912*0.280047132757266-1002:.0f} lead"
  f" = {vnd((4912*0.280047132757266-1002)*cpl_crm)} đ")
P("   Di động v2 vẫn chỉ hoàn tất 24,6% vs máy tính 41,3% ⇒ còn dư địa trên di động")

# A9 attribution
P("")
P("A-PhânBổ (10 mục D): mô hình nhấp cuối đang dùng để chia ngân sách."
  " Brand −191 lead (−32,3%), YouTube +122 (+283,7%), GDN +186 (+40,9%),"
  " kênh ngoài Ads +71 lead không được ghi nhận")

# A10 GTM
P("")
P("A-GTM (12): 34 thẻ, 412 KB JS bên thứ 3, +~0,8s LCP; GA4 Config trùng lặp từ v22/N31"
  " ⇒ page_view đếm đôi; 3 thẻ đối tác F2 không rõ nguồn gốc; không có Consent Mode v2;"
  " không có server-side; không có cảnh báo chuyển đổi = 0 (sự cố N44–46 mất 3 ngày mới phát hiện)")
P("A-GCLID (05 + 12 #15): CRM không lưu GCLID ⇒ không import offline conversion"
  " ⇒ bidding không bao giờ học được tín hiệu SQL/cọc (18 cọc thật vs 3.820 tín hiệu rác)")
P("A-Zalo/Download (10 mục E): zalo_click 894 lượt + file_download 1.206 lượt"
  " đang bị bỏ sót hoàn toàn, chưa đánh dấu sự kiện chính từ v26/N71")
P("A-EnhancedConversions TẮT (05, 12 #14): mất 10–20% khả năng khớp")
P("A-Chốngspam (05): không reCAPTCHA, không OTP ⇒ trùng SĐT 31% ở PMax (08 mục C)")

# A11 cấu trúc & tiện ích
P(f"A-CấuTrúc (05): 31 từ khóa/nhóm, 1 RSA/nhóm, Điểm chất lượng TB 5,2/10,"
  f" trải nghiệm trang đích 'Dưới trung bình'; Search Partners + Display network BẬT trong Search")
P("A-TiệnÍch (05): chỉ có 4 sitelink; thiếu Cuộc gọi, Biểu mẫu KH tiềm năng, Vị trí, Chú thích, Hình ảnh")

# A12 quá tải sale / khối lượng lead
P("")
P(f"A-TảiSale (08 mục B): GĐ3 35,4 lead mới/ngày trên năng lực 96 ⇒ chưa quá tải TỔNG,"
  f" nhưng T7/CN chỉ 2 sale ⇒ trần {2*12} lead/ngày trong khi"
  f" T7 chi {vnd(262814000)} đ, CN {vnd(240996000)} đ")

# Trend theo tuần
P("")
P("Xu hướng theo tuần (chi phí / lead / SQL / cọc):")
by_week = collections.OrderedDict()
for r in rows: by_week.setdefault(r["Tuan"], []).append(r)
for w, rs in by_week.items():
    d = agg(rs)
    P(f"   Tuần {w:>2}: chi {vnd(d['Chi_phi']):>13} | CĐ_Ads {d['ChuyenDoi_Ads']:>3}"
      f" | lead {d['Lead_CRM']:>3} | SQL {d['Lead_SQL']:>3} | cọc {d['Dat_Coc']:>2}"
      f" | DT {vnd(d['DoanhThu_HoaHong']):>13}")

# ---------- C: phân bổ ngân sách đề xuất ----------
P("")
P("=" * 78)
P("[C] KIỂM TRA PHÂN BỔ NGÂN SÁCH ĐỀ XUẤT (tổng phải = 2.100.000.000)")
P("=" * 78)
plan = {
    "GĐ1 (N1-30) 600tr": {
        "SEA_Brand": 180_000_000, "SEA_Generic_TáiCấuTrúc": 200_000_000,
        "PMax_Lead (ghìm, đã sạch tín hiệu)": 90_000_000,
        "GDN_Remarketing": 60_000_000, "SEA_DSA/Long-tail": 40_000_000,
        "Dự phòng test": 30_000_000},
    "GĐ2 (N31-60) 700tr": {
        "SEA_Brand": 200_000_000, "SEA_Generic_TáiCấuTrúc": 240_000_000,
        "PMax_Lead (ghìm, đã sạch tín hiệu)": 120_000_000,
        "GDN_Remarketing": 70_000_000, "SEA_DSA/Long-tail": 40_000_000,
        "Dự phòng test": 30_000_000},
    "GĐ3 (N61-90) 800tr": {
        "SEA_Brand": 230_000_000, "SEA_Generic_TáiCấuTrúc": 260_000_000,
        "PMax_Lead (ghìm, đã sạch tín hiệu)": 150_000_000,
        "GDN_Remarketing": 80_000_000, "SEA_DSA/Long-tail": 50_000_000,
        "Dự phòng test": 30_000_000},
}
grand = 0
camp_totals = collections.Counter()
for gd, alloc in plan.items():
    s = sum(alloc.values()); grand += s
    P(f"{gd}: tổng {vnd(s)} đ  ({s/90*3/1_000_000:.1f} tr/ngày)")
    for c, v in alloc.items():
        camp_totals[c] += v
        P(f"    {c:38} {vnd(v):>14} đ  ({v/s*100:>5.1f}%)  {vnd(v/30)} đ/ngày")
P(f"TỔNG 3 GIAI ĐOẠN = {vnd(grand)} đ  {'✔ ĐÚNG 2,1 tỷ' if grand == BUDGET else '✘ SAI'}")
P("Tổng theo chiến dịch toàn kỳ:")
for c, v in camp_totals.most_common():
    P(f"    {c:38} {vnd(v):>14} đ  ({v/BUDGET*100:>5.1f}%)")
P(f"So với kỳ trước: Brand {vnd(camp_stat['SEA_Brand_Vinhomes_HocMon'][0]['Chi_phi'])}"
  f" → {vnd(camp_totals['SEA_Brand'])} đ"
  f" ({camp_totals['SEA_Brand']/camp_stat['SEA_Brand_Vinhomes_HocMon'][0]['Chi_phi']-1:+.0%})")
P(f"                 PMax {vnd(camp_stat['PMAX_VinhomesHM_Lead'][0]['Chi_phi'])}"
  f" → {vnd(camp_totals['PMax_Lead (ghìm, đã sạch tín hiệu)'])} đ"
  f" ({camp_totals['PMax_Lead (ghìm, đã sạch tín hiệu)']/camp_stat['PMAX_VinhomesHM_Lead'][0]['Chi_phi']-1:+.0%})")
P(f"                 Competitor {vnd(camp_stat['SEA_Competitor_DoiThu'][0]['Chi_phi'])} → 0 đ (-100%)")
P(f"                 YouTube {vnd(camp_stat['YT_Video_TVC_MoBan'][0]['Chi_phi'])} → 0 đ (-100%)")

# kiểm tra kế hoạch có đạt KPI không
P("")
P("Kiểm tra khả thi kế hoạch (dùng KB cơ sở B4):")
r_sqlrate = 0.35; r_sqlcoc = sql_coc_g3 * 1.25
need_sql = TARGET_COC / r_sqlcoc; need_lead = need_sql / r_sqlrate
P(f"   Cần {need_lead:.0f} lead / {need_sql:.0f} SQL / CP-SQL ≤ {vnd(BUDGET/need_sql)} đ")
P(f"   ⇒ CPL mục tiêu {vnd(BUDGET/need_lead)} đ vs CPL_CRM hiện tại {vnd(cpl_crm)} đ"
  f" ({BUDGET/need_lead/cpl_crm-1:+.0%})")
P(f"   KPI CP/SQL ban giám đốc ≤ 2.200.000 đ ⇒ với 2,1 tỷ mua được"
  f" {BUDGET/2_200_000:.0f} SQL ⇒ ở SQL→cọc {pct(r_sqlcoc,2)} ra {BUDGET/2_200_000*r_sqlcoc:.1f} cọc"
  f" (KPI 32) ⇒ {'ĐỦ' if BUDGET/2_200_000*r_sqlcoc >= 32 else 'THIẾU, cần nâng SQL→cọc'}")
P(f"   Để 954 SQL × X = 32 cọc ⇒ X = {32/(BUDGET/2_200_000):.2%} (thấp hơn GĐ3 {pct(sql_coc_g3,2)})"
  f" ⇒ KPI CP/SQL 2,2 triệu là ràng buộc dễ hơn ràng buộc cọc? kiểm tra:")
P(f"   Ở CP/SQL 2,2 triệu + SQL→cọc GĐ3 {pct(sql_coc_g3,2)} ⇒"
  f" {BUDGET/2_200_000*sql_coc_g3:.1f} cọc; ROAS = {BUDGET/2_200_000*sql_coc_g3*COMMISSION/BUDGET:.2f}x")

# D3 số liệu
P("")
P("=" * 78)
P("[D3] PMAX vs PHẦN CÒN LẠI")
P("=" * 78)
pm, pmk = camp_stat["PMAX_VinhomesHM_Lead"]
br_, brk = camp_stat["SEA_Brand_Vinhomes_HocMon"]
ge_, gek = camp_stat["SEA_Generic_NhaPho_CanHo_TayBac"]
P(f"{'':34}{'CPL_Ads':>12}{'CPL_CRM':>12}{'CP/SQL':>14}{'CP/cọc':>16}{'ROAS':>7}")
for name, d_, k_ in [("PMAX_VinhomesHM_Lead", pm, pmk), ("SEA_Brand", br_, brk),
                     ("SEA_Generic", ge_, gek)]:
    P(f"{name:34}{vnd(k_['cpl_ads']):>12}{vnd(k_['cpl_crm']):>12}{vnd(k_['cp_sql']):>14}"
      f"{vnd(k_['cp_coc']):>16}{(k_['roas'] or 0):>7.2f}")
P(f"PMax rẻ nhất theo CPL_Ads ({vnd(pmk['cpl_ads'])}) nhưng đắt gần nhất theo CP/SQL"
  f" ({vnd(pmk['cp_sql'])}) và ROAS = 0 (0 cọc / {vnd(pm['Chi_phi'])} đ)")
P(f"Nếu dồn toàn bộ 2,1 tỷ vào PMax theo tỷ lệ hiện tại: SQL ="
  f" {BUDGET/pmk['cp_sql']:.0f}, cọc = 0 (lịch sử 90 ngày, 475 tỷ... không: {vnd(pm['Chi_phi'])} đ → 0 cọc)")
P(f"Ngược lại 2,1 tỷ vào Brand theo tỷ lệ Brand: cọc ="
  f" {BUDGET/brk['cp_coc']:.1f}, DT = {vnd(BUDGET*brk['roas'])} đ (không thực tế vì Brand"
  f" giới hạn bởi lượng tìm kiếm — IS {pct(ish)}, trần thực tế chỉ ~{d['Chi_phi']*0+1:.0f}x)")
brand_cap = br_["Chi_phi"] / max(ish, 1e-9)
P(f"   Trần chi Brand thực tế ≈ chi hiện tại / IS = {vnd(brand_cap)} đ / 90 ngày"
  f" (tức tối đa ~{vnd(brand_cap/90)} đ/ngày ở IS 100%)")

# D1 số liệu brand
P("")
P("=" * 78)
P("[D1] BRAND CÓ ĐÁNG GIỮ KHÔNG")
P("=" * 78)
P(f"Brand: {br_['Chi_phi']/TOT['Chi_phi']*100:.1f}% chi phí → {br_['Dat_Coc']}/{TOT['Dat_Coc']} cọc"
  f" ({br_['Dat_Coc']/TOT['Dat_Coc']*100:.0f}%) → {br_['DoanhThu_HoaHong']/TOT['DoanhThu_HoaHong']*100:.0f}% doanh thu")
P(f"Generic: {ge_['Chi_phi']/TOT['Chi_phi']*100:.1f}% chi phí → {ge_['Dat_Coc']} cọc,"
  f" ROAS {gek['roas']:.2f}x, CP/SQL {vnd(gek['cp_sql'])} đ (gấp {gek['cp_sql']/brk['cp_sql']:.1f}x Brand)")
P(f"CPC Brand {vnd(div(br_['Chi_phi'],br_['Nhap_chuot']))} đ vs Generic"
  f" {vnd(div(ge_['Chi_phi'],ge_['Nhap_chuot']))} đ ⇒ Generic đắt hơn"
  f" {div(ge_['Chi_phi'],ge_['Nhap_chuot'])/div(br_['Chi_phi'],br_['Nhap_chuot']):.1f}x")
P(f"CTR Brand {pct(div(br_['Nhap_chuot'],br_['Hien_thi']),2)} vs Generic"
  f" {pct(div(ge_['Nhap_chuot'],ge_['Hien_thi']),2)} (benchmark brand tốt >12%)")
P(f"Mất IS do ngân sách Brand {pct(mis)} ⇒ Brand đang bị BÓP, không phải thừa")
P(f"10_GA4 mục D: bỏ Brand thì mô hình dựa trên dữ liệu vẫn gán 401/1715 lead cho Brand"
  f" ({401/1715*100:.0f}% tổng generate_lead)")
P(f"Nếu cắt Brand, mất tối thiểu {vnd(br_['DoanhThu_HoaHong'])} đ DT để tiết kiệm"
  f" {vnd(br_['Chi_phi'])} đ chi phí ⇒ lỗ ròng {vnd(br_['DoanhThu_HoaHong']-br_['Chi_phi'])} đ")

# D4 cắt ngân sách 1,2 tỷ
P("")
P("=" * 78)
P("[D4] KỊCH BẢN NGÂN SÁCH 1,2 TỶ")
P("=" * 78)
B2 = 1_200_000_000
plan2 = [("SEA_Brand (giữ đến cùng)", 260_000_000),
         ("SEA_Generic — chỉ exact/phrase top 6 cụm từ có SQL", 480_000_000),
         ("GDN_Remarketing 30d", 150_000_000),
         ("PMax (chỉ bật sau khi sạch tín hiệu + brand exclusion)", 210_000_000),
         ("SEA_DSA/long-tail", 100_000_000)]
P(f"{'Hạng mục':56}{'Ngân sách':>16}{'%':>7}")
for c, v in plan2: P(f"{c:56}{vnd(v):>16}{v/B2*100:>6.1f}%")
P(f"{'TỔNG':56}{vnd(sum(v for _, v in plan2)):>16}"
  f"  {'✔' if sum(v for _, v in plan2) == B2 else '✘'}")
P(f"Cắt bỏ hoàn toàn: Competitor {vnd(camp_stat['SEA_Competitor_DoiThu'][0]['Chi_phi'])} đ (0 cọc),"
  f" YouTube {vnd(camp_stat['YT_Video_TVC_MoBan'][0]['Chi_phi'])} đ (0 cọc)")
P(f"Ở 1,2 tỷ & CP/SQL mục tiêu 2,2 triệu ⇒ {B2/2_200_000:.0f} SQL"
  f" ⇒ ở SQL→cọc {pct(sql_coc_g3*1.25,2)} ra {B2/2_200_000*sql_coc_g3*1.25:.1f} cọc"
  f" ⇒ ROAS {B2/2_200_000*sql_coc_g3*1.25*COMMISSION/B2:.2f}x")
P(f"⇒ KPI 32 cọc KHÔNG khả thi ở 1,2 tỷ; cam kết lại còn"
  f" ~{B2/2_200_000*sql_coc_g3*1.25:.0f} cọc (giảm {1-B2/BUDGET:.0%} ngân sách)")

# ---------- self-check ----------
def check():
    assert TOT["Chi_phi"] == 1_803_537_000, TOT["Chi_phi"]
    assert TOT["ChuyenDoi_Ads"] == 3820 and TOT["Lead_CRM"] == 2557
    assert TOT["Lead_SQL"] == 651 and TOT["Dat_Coc"] == 18
    assert TOT["DoanhThu_HoaHong"] == 3_130_000_000
    assert gl + c2c_tot + vpp + e30 == 3820
    assert 3820 - dup - junk == 2494 and 2494 + 63 == 2557
    assert dup + junk - 63 == 3820 - 2557
    assert lost["ChuyenDoi_Ads"] == 0, lost["ChuyenDoi_Ads"]
    assert grand == BUDGET
    assert sum(v for _, v in plan2) == B2
    assert lo == 370 and hi == 480
    print("\n[self-check] OK — mọi tổng khớp với sheet 03 và sheet 10.")
check()

with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "agent-7-calc.out"),
          "w", encoding="utf-8") as f:
    f.write("\n".join(OUT))
