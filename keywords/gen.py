#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Sinh bộ từ khóa Google Ads BĐS VN theo ma trận [loại hình] x [khu vực] x [modifier] + [dự án] x [modifier].
Chạy: python3 gen.py  -> ghi keywords/master-keywords.csv
Dữ liệu dự án thật đọc từ projects.tsv (tên|chủ đầu tư|loại hình|khu vực).
"""
import csv, os, re, sys, unicodedata
from datetime import date

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, "master-keywords.csv")
PROJ_FILE = os.path.join(HERE, "projects.tsv")

# ---------------------------------------------------------------- loại hình
# nhóm loại hình cho phép theo đặc thù khu vực (tránh sinh truy vấn vô nghĩa
# kiểu "condotel quận 3" hay "đất nền quận 1")
CORE = ["căn hộ", "chung cư", "officetel", "nhà phố", "shophouse", "penthouse"]
OUTER = ["căn hộ", "chung cư", "đất nền", "nhà phố", "biệt thự", "shophouse", "liền kề"]
PROV = ["căn hộ", "chung cư", "đất nền", "nhà phố", "biệt thự", "shophouse", "liền kề", "nhà xưởng"]
COAST = ["căn hộ", "condotel", "biệt thự biển", "shophouse", "đất nền", "nhà phố"]
CITY = ["căn hộ", "chung cư", "đất nền", "nhà phố", "biệt thự", "shophouse", "officetel", "liền kề"]
# ponytail: LAND = PROV đảo thứ tự, đất nền lên đầu. Chỉ cần cho vùng mà đất nền LÀ
# sản phẩm chính (Long An) — loại hình index 0 mới được fan-out đủ modifier + bản exact.
LAND = ["đất nền", "nhà phố", "biệt thự", "căn hộ", "shophouse", "liền kề", "nhà xưởng"]

# ---------------------------------------------------------------- khu vực
# (tên hiển thị trong keyword, tỉnh/thành, nhóm loại hình, hạng A/B)
REGIONS = [
    # --- cấp thành phố ---
    ("tphcm",            "TP.HCM",    CITY,  "A"),
    ("hồ chí minh",      "TP.HCM",    CITY,  "A"),
    ("sài gòn",          "TP.HCM",    CITY,  "B"),
    ("hà nội",           "Hà Nội",    CITY,  "A"),
    # --- HCM lõi ---
    ("quận 1",           "TP.HCM",    CORE,  "A"),
    ("quận 3",           "TP.HCM",    CORE,  "A"),
    ("quận 4",           "TP.HCM",    CORE,  "A"),
    ("quận 5",           "TP.HCM",    CORE,  "B"),
    ("quận 6",           "TP.HCM",    CORE,  "B"),
    ("quận 7",           "TP.HCM",    CORE,  "A"),
    ("quận 8",           "TP.HCM",    OUTER, "A"),
    ("quận 10",          "TP.HCM",    CORE,  "A"),
    ("quận 11",          "TP.HCM",    CORE,  "B"),
    ("quận 12",          "TP.HCM",    OUTER, "A"),
    ("bình thạnh",       "TP.HCM",    CORE,  "A"),
    ("phú nhuận",        "TP.HCM",    CORE,  "A"),
    ("tân bình",         "TP.HCM",    CORE,  "A"),
    ("tân phú",          "TP.HCM",    OUTER, "A"),
    ("gò vấp",           "TP.HCM",    CORE,  "A"),
    ("bình tân",         "TP.HCM",    OUTER, "A"),
    # --- HCM vùng ven / Thủ Đức ---
    ("thủ đức",          "TP.HCM",    OUTER, "A"),
    ("quận 2",           "TP.HCM",    OUTER, "A"),
    ("quận 9",           "TP.HCM",    OUTER, "A"),
    ("an phú",           "TP.HCM",    OUTER, "B"),
    ("thảo điền",        "TP.HCM",    CORE,  "A"),
    ("nhà bè",           "TP.HCM",    OUTER, "A"),
    ("bình chánh",       "TP.HCM",    OUTER, "A"),
    ("hóc môn",          "TP.HCM",    OUTER, "B"),
    ("củ chi",           "TP.HCM",    PROV,  "B"),
    ("cần giờ",          "TP.HCM",    PROV,  "B"),
    ("phú mỹ hưng",      "TP.HCM",    CORE,  "A"),
    # --- Hà Nội lõi ---
    ("cầu giấy",         "Hà Nội",    CORE,  "A"),
    ("tây hồ",           "Hà Nội",    CORE,  "A"),
    ("ba đình",          "Hà Nội",    CORE,  "A"),
    ("đống đa",          "Hà Nội",    CORE,  "A"),
    ("hai bà trưng",     "Hà Nội",    CORE,  "A"),
    ("hoàn kiếm",        "Hà Nội",    CORE,  "B"),
    ("thanh xuân",       "Hà Nội",    CORE,  "A"),
    # --- Hà Nội vùng ven ---
    ("nam từ liêm",      "Hà Nội",    OUTER, "A"),
    ("bắc từ liêm",      "Hà Nội",    OUTER, "A"),
    ("hoàng mai",        "Hà Nội",    OUTER, "A"),
    ("long biên",        "Hà Nội",    OUTER, "A"),
    ("hà đông",          "Hà Nội",    OUTER, "A"),
    ("gia lâm",          "Hà Nội",    OUTER, "A"),
    ("đông anh",         "Hà Nội",    OUTER, "A"),
    ("hoài đức",         "Hà Nội",    OUTER, "A"),
    ("thanh trì",        "Hà Nội",    OUTER, "B"),
    ("mê linh",          "Hà Nội",    OUTER, "B"),
    ("sóc sơn",          "Hà Nội",    PROV,  "B"),
    ("mỹ đình",          "Hà Nội",    OUTER, "A"),
    ("cổ nhuế",          "Hà Nội",    OUTER, "B"),
    # --- Bình Dương ---
    ("bình dương",       "Bình Dương", PROV, "A"),
    ("dĩ an",            "Bình Dương", PROV, "A"),
    ("thuận an",         "Bình Dương", PROV, "A"),
    ("thủ dầu một",      "Bình Dương", PROV, "A"),
    ("bến cát",          "Bình Dương", PROV, "B"),
    ("tân uyên",         "Bình Dương", PROV, "B"),
    # --- Đồng Nai ---
    ("đồng nai",         "Đồng Nai",  PROV,  "A"),
    ("biên hòa",         "Đồng Nai",  PROV,  "A"),
    ("nhơn trạch",       "Đồng Nai",  PROV,  "A"),
    ("long thành",       "Đồng Nai",  PROV,  "A"),
    ("trảng bom",        "Đồng Nai",  PROV,  "B"),
    # --- Long An ---
    ("long an",          "Long An",   LAND,  "A"),
    ("đức hòa",          "Long An",   LAND,  "A"),
    ("bến lức",          "Long An",   LAND,  "A"),
    ("cần giuộc",        "Long An",   LAND,  "A"),
    # --- BR-VT ---
    ("bà rịa vũng tàu",  "BR-VT",     COAST, "A"),
    ("vũng tàu",         "BR-VT",     COAST, "A"),
    ("phú mỹ",           "BR-VT",     PROV,  "B"),
    ("hồ tràm",          "BR-VT",     COAST, "B"),
    # --- miền Bắc ---
    ("hưng yên",         "Hưng Yên",  PROV,  "A"),
    ("văn giang",        "Hưng Yên",  PROV,  "A"),
    ("ecopark",          "Hưng Yên",  PROV,  "A"),
    ("bắc ninh",         "Bắc Ninh",  PROV,  "A"),
    ("từ sơn",           "Bắc Ninh",  PROV,  "B"),
    ("bắc giang",        "Bắc Giang", PROV,  "B"),
    ("hải phòng",        "Hải Phòng", PROV,  "A"),
    ("thủy nguyên",      "Hải Phòng", PROV,  "A"),
    ("quảng ninh",       "Quảng Ninh", COAST, "A"),
    ("hạ long",          "Quảng Ninh", COAST, "A"),
    ("vân đồn",          "Quảng Ninh", COAST, "B"),
    ("hải dương",        "Hải Dương", PROV,  "B"),
    ("vĩnh phúc",        "Vĩnh Phúc", PROV,  "B"),
    ("thái nguyên",      "Thái Nguyên", PROV, "B"),
    ("ninh bình",        "Ninh Bình", PROV,  "B"),
    ("hà nam",           "Hà Nam",    PROV,  "B"),
    ("thanh hóa",        "Thanh Hóa", PROV,  "B"),
    ("sầm sơn",          "Thanh Hóa", COAST, "B"),
    ("nghệ an",          "Nghệ An",   PROV,  "B"),
    ("vinh",             "Nghệ An",   PROV,  "B"),
    # --- miền Trung / biển ---
    ("đà nẵng",          "Đà Nẵng",   COAST, "A"),
    ("sơn trà",          "Đà Nẵng",   COAST, "B"),
    ("ngũ hành sơn",     "Đà Nẵng",   COAST, "B"),
    ("hải châu",         "Đà Nẵng",   CORE,  "B"),
    ("hội an",           "Quảng Nam", COAST, "B"),
    ("huế",              "Huế",       PROV,  "B"),
    ("quy nhơn",         "Bình Định", COAST, "B"),
    ("nha trang",        "Khánh Hòa", COAST, "A"),
    ("cam ranh",         "Khánh Hòa", COAST, "B"),
    ("phan thiết",       "Bình Thuận", COAST, "B"),
    ("mũi né",           "Bình Thuận", COAST, "B"),
    ("đà lạt",           "Lâm Đồng",  PROV,  "A"),
    ("bảo lộc",          "Lâm Đồng",  PROV,  "B"),
    # --- miền Tây ---
    ("cần thơ",          "Cần Thơ",   PROV,  "B"),
    ("phú quốc",         "Kiên Giang", COAST, "A"),
    ("tây ninh",         "Tây Ninh",  PROV,  "B"),
    ("bình phước",       "Bình Phước", PROV, "B"),
]

# ---------------------------------------------------------------- modifier
# (modifier, nhóm ad group, intent_tier, match_type, ưu tiên, ghi chú)
MOD_CORE = [
    ("",                "generic-{t}",      "T2_giao_dich",  "phrase", 1, "head term theo loại hình + khu vực"),
    ("giá",             "gia-bang-gia",     "T2_giao_dich",  "phrase", 1, "intent hỏi giá, dẫn về block bảng giá LP"),
    ("bảng giá",        "gia-bang-gia",     "T2_giao_dich",  "phrase", 1, "lead magnet: tải bảng giá"),
    ("giá bao nhiêu",   "gia-bang-gia",     "T2_giao_dich",  "phrase", 1, "long-tail hỏi giá"),
    ("mua",             "mua-ban",          "T2_giao_dich",  "phrase", 1, "intent mua trực tiếp"),
    ("bán",             "mua-ban",          "T2_giao_dich",  "phrase", 2, "cẩn thận: có thể là người bán, theo dõi search term"),
    ("mở bán",          "mo-ban-moi",       "T2_giao_dich",  "phrase", 1, "intent hàng mới, CPL thường tốt nhất"),
    ("dự án",           "du-an-khu-vuc",    "T2_giao_dich",  "phrase", 1, "duyệt danh mục dự án theo khu vực"),
]
MOD_MID = [
    ("dự án mới",       "mo-ban-moi",       "T2_giao_dich",  "phrase", 2, "hàng mới ra"),
    ("sắp mở bán",      "mo-ban-moi",       "T2_giao_dich",  "phrase", 2, "giữ chỗ sớm"),
    ("trả góp",         "tai-chinh",        "T2_giao_dich",  "phrase", 2, "dẫn về block chính sách vay"),
    ("trả góp ngân hàng", "tai-chinh",      "T2_giao_dich",  "phrase", 2, "hỗ trợ vay"),
    ("cao cấp",         "phan-khuc-cao",    "T2_giao_dich",  "phrase", 2, "phân khúc cao cấp"),
    ("bàn giao ngay",   "san-sang-o",       "T2_giao_dich",  "phrase", 2, "nhu cầu ở ngay, chốt nhanh"),
    ("2 phòng ngủ",     "cau-hinh-can",     "T2_giao_dich",  "phrase", 2, "lọc theo cấu hình"),
    ("3 phòng ngủ",     "cau-hinh-can",     "T2_giao_dich",  "phrase", 2, "lọc theo cấu hình"),
    ("dưới 2 tỷ",       "phan-khuc-ngan-sach", "T2_giao_dich", "phrase", 2, "phân khúc ngân sách"),
    ("dưới 3 tỷ",       "phan-khuc-ngan-sach", "T2_giao_dich", "phrase", 2, "phân khúc ngân sách"),
    ("dưới 5 tỷ",       "phan-khuc-ngan-sach", "T2_giao_dich", "phrase", 2, "phân khúc ngân sách"),
]
MOD_RESEARCH = [
    ("có nên mua",      "tu-van-quyet-dinh", "T3_nghien_cuu", "phrase", 3, "top-funnel, đẩy về bài SEO + remarketing"),
    ("review",          "tu-van-quyet-dinh", "T3_nghien_cuu", "phrase", 3, "cần negative 'lừa đảo'"),
    ("đánh giá",        "tu-van-quyet-dinh", "T3_nghien_cuu", "phrase", 3, "top-funnel"),
    ("pháp lý",         "phap-ly",           "T3_nghien_cuu", "phrase", 3, "quan tâm sổ hồng, giấy tờ"),
    ("tiến độ",         "tien-do",           "T3_nghien_cuu", "phrase", 3, "thường là khách đã mua, giá trị lead thấp hơn"),
    ("ở đâu tốt",       "tu-van-quyet-dinh", "T3_nghien_cuu", "phrase", 3, "top-funnel"),
]
# modifier chỉ dùng cho khu vực hạng A
MOD_B = MOD_CORE[:5]

# modifier áp cho tên dự án thật (intent thương hiệu, ưu tiên cao nhất)
MOD_PROJECT = [
    ("",                    "brand-{p}",     "T1_brand_du_an", "exact",  1, "brand dự án, exact - CPC rẻ nhất"),
    ("giá",                 "brand-{p}",     "T1_brand_du_an", "exact",  1, "hỏi giá brand"),
    ("bảng giá",            "brand-{p}",     "T1_brand_du_an", "exact",  1, "lead magnet bảng giá"),
    ("giá bao nhiêu",       "brand-{p}",     "T1_brand_du_an", "phrase", 1, "long-tail hỏi giá"),
    ("mở bán",              "brand-{p}",     "T1_brand_du_an", "exact",  1, "hàng mới"),
    ("mua",                 "brand-{p}",     "T1_brand_du_an", "phrase", 1, "intent mua"),
    ("chủ đầu tư",          "brand-{p}",     "T1_brand_du_an", "phrase", 2, "xác minh CĐT"),
    ("vị trí",              "brand-{p}",     "T1_brand_du_an", "phrase", 2, "dẫn về block vị trí LP"),
    ("mặt bằng",            "brand-{p}",     "T1_brand_du_an", "phrase", 2, "dẫn về block mặt bằng"),
    ("tiện ích",            "brand-{p}",     "T1_brand_du_an", "phrase", 2, "dẫn về block tiện ích"),
    ("chính sách bán hàng", "brand-{p}",     "T1_brand_du_an", "phrase", 1, "intent chốt cao"),
    ("tiến độ thanh toán",  "brand-{p}",     "T1_brand_du_an", "phrase", 1, "intent chốt cao"),
    ("pháp lý",             "brand-{p}",     "T1_brand_du_an", "phrase", 2, "yếu tố tin tưởng"),
    ("có nên mua",          "brand-{p}",     "T1_brand_du_an", "phrase", 2, "cân nhắc, đẩy content so sánh"),
    ("nhà mẫu",             "brand-{p}",     "T1_brand_du_an", "phrase", 2, "intent đi xem - lead chất lượng cao"),
    ("trả góp",             "brand-{p}",     "T1_brand_du_an", "phrase", 2, "tài chính"),
]
# 6 modifier phụ chỉ áp cho dự án hạng A (chủ đầu tư top / dự án hot)
MOD_PROJECT_EXTRA = [
    ("chiết khấu",       "brand-{p}", "T1_brand_du_an", "phrase", 2, "ưu đãi"),
    ("lãi suất",         "brand-{p}", "T1_brand_du_an", "phrase", 2, "tài chính"),
    ("tiến độ xây dựng", "brand-{p}", "T1_brand_du_an", "phrase", 3, "khách đã mua"),
    ("review",           "brand-{p}", "T1_brand_du_an", "phrase", 2, "cần negative 'lừa đảo'"),
    ("đánh giá",         "brand-{p}", "T1_brand_du_an", "phrase", 2, "cân nhắc"),
    ("bàn giao khi nào", "brand-{p}", "T1_brand_du_an", "phrase", 3, "khách đã mua"),
]

# ---------------------------------------------------------------- chủ đầu tư
DEVELOPERS = [
    ("vinhomes", "toàn quốc"), ("vingroup", "toàn quốc"),
    ("masterise homes", "toàn quốc"), ("ecopark", "Hưng Yên"),
    ("sun group", "toàn quốc"), ("novaland", "toàn quốc"),
    ("khang điền", "TP.HCM"), ("nam long", "TP.HCM"),
    ("phú mỹ hưng", "TP.HCM"), ("gamuda land", "toàn quốc"),
    ("capitaland", "toàn quốc"), ("keppel land", "TP.HCM"),
    ("đất xanh", "toàn quốc"), ("hưng thịnh", "toàn quốc"),
    ("phát đạt", "TP.HCM"), ("an gia", "TP.HCM"),
    ("bcons", "Bình Dương"), ("phú đông group", "Bình Dương"),
    ("kim oanh group", "Bình Dương"), ("becamex", "Bình Dương"),
    ("mik group", "Hà Nội"), ("brg group", "Hà Nội"),
    ("taseco land", "Hà Nội"), ("văn phú invest", "Hà Nội"),
    ("hải phát", "Hà Nội"), ("tnr holdings", "toàn quốc"),
    ("t&t group", "toàn quốc"), ("geleximco", "Hà Nội"),
    ("eurowindow", "Hà Nội"), ("him lam", "toàn quốc"),
    ("bim group", "Quảng Ninh"), ("flamingo", "toàn quốc"),
    ("hoàng huy", "Hải Phòng"), ("danh khôi", "toàn quốc"),
    ("thắng lợi group", "Long An"), ("trần anh group", "Long An"),
    ("vạn phúc group", "TP.HCM"), ("lotte", "toàn quốc"),
    ("ceo group", "Quảng Ninh"), ("bamboo capital", "toàn quốc"),
    ("regal group", "Đà Nẵng"), ("tt capital", "Bình Dương"),
    ("lê phong", "Bình Dương"), ("nhà ở xã hội hoàng quân", "toàn quốc"),
    ("prodezi", "Long An"),
]
MOD_DEV = [
    ("dự án",         "brand-cdt",  "T1_brand_cdt", "phrase", 1, "duyệt danh mục CĐT"),
    ("dự án mới",     "brand-cdt",  "T1_brand_cdt", "phrase", 1, "hàng mới của CĐT"),
    ("mở bán",        "brand-cdt",  "T1_brand_cdt", "phrase", 1, "hàng mới"),
    ("bảng giá",      "brand-cdt",  "T1_brand_cdt", "phrase", 1, "lead magnet"),
    ("căn hộ",        "brand-cdt",  "T1_brand_cdt", "phrase", 1, "loại hình chính"),
    ("chung cư",      "brand-cdt",  "T1_brand_cdt", "phrase", 2, "loại hình chính"),
    ("có uy tín không", "brand-cdt", "T3_nghien_cuu", "phrase", 3, "trust query, cần negative 'lừa đảo'"),
    ("chính sách bán hàng", "brand-cdt", "T1_brand_cdt", "phrase", 2, "intent chốt"),
]

# ---------------------------------------------------------------- keyword phi khu vực (top/mid funnel)
GENERIC = [
    # (keyword, adgroup, tier, match, ưu tiên, ghi chú)
    ("mua nhà trả góp lãi suất thấp",       "tai-chinh", "T2_giao_dich", "phrase", 2, "tài chính"),
    ("vay mua nhà ngân hàng nào tốt nhất",  "tai-chinh", "T3_nghien_cuu", "phrase", 3, "top-funnel"),
    ("lãi suất vay mua nhà 2026",           "tai-chinh", "T3_nghien_cuu", "phrase", 3, "top-funnel, cập nhật năm"),
    ("mua nhà trả góp cần bao nhiêu tiền",  "tai-chinh", "T3_nghien_cuu", "phrase", 3, "top-funnel"),
    ("mua căn hộ trả trước 20%",            "tai-chinh", "T2_giao_dich", "phrase", 2, "intent tốt"),
    ("ân hạn nợ gốc là gì",                 "tai-chinh", "T3_nghien_cuu", "phrase", 3, "kiến thức, chỉ dùng cho remarketing"),
    ("hỗ trợ lãi suất 0% mua căn hộ",       "tai-chinh", "T2_giao_dich", "phrase", 2, "chính sách"),
    ("thủ tục mua bán nhà đất",             "phap-ly",  "T3_nghien_cuu", "phrase", 3, "top-funnel"),
    ("sổ hồng riêng là gì",                 "phap-ly",  "T3_nghien_cuu", "phrase", 3, "kiến thức"),
    ("kiểm tra quy hoạch đất",              "phap-ly",  "T3_nghien_cuu", "phrase", 3, "kiến thức"),
    ("mua nhà hình thành trong tương lai",  "phap-ly",  "T3_nghien_cuu", "phrase", 3, "kiến thức"),
    ("người nước ngoài mua nhà tại việt nam", "phap-ly", "T2_giao_dich", "phrase", 2, "tệp riêng, giá trị cao"),
    ("phí bảo trì chung cư 2%",             "phap-ly",  "T3_nghien_cuu", "phrase", 3, "kiến thức"),
    ("thuế phí sang tên sổ đỏ",             "phap-ly",  "T3_nghien_cuu", "phrase", 3, "kiến thức"),
    ("có nên mua căn hộ chung cư không",    "tu-van-quyet-dinh", "T3_nghien_cuu", "phrase", 3, "top-funnel"),
    ("nên mua căn hộ hay nhà đất",          "tu-van-quyet-dinh", "T3_nghien_cuu", "phrase", 3, "top-funnel"),
    ("nên mua chung cư tầng bao nhiêu",     "tu-van-quyet-dinh", "T3_nghien_cuu", "phrase", 3, "top-funnel"),
    ("kinh nghiệm mua căn hộ lần đầu",      "tu-van-quyet-dinh", "T3_nghien_cuu", "phrase", 3, "top-funnel"),
    ("cách chọn căn hộ hướng tốt",          "tu-van-quyet-dinh", "T3_nghien_cuu", "phrase", 3, "top-funnel"),
    ("đầu tư bất động sản 2026 nên mua gì", "dau-tu",   "T3_nghien_cuu", "phrase", 3, "tệp đầu tư"),
    ("bất động sản nào sinh lời tốt nhất",  "dau-tu",   "T3_nghien_cuu", "phrase", 3, "tệp đầu tư"),
    ("đầu tư căn hộ dòng tiền",             "dau-tu",   "T3_nghien_cuu", "phrase", 3, "tệp đầu tư (tránh dùng cụm 'cho thuê' vì đã negative cấp account)"),
    ("căn hộ khai thác dòng tiền tốt",      "dau-tu",   "T3_nghien_cuu", "phrase", 3, "tệp đầu tư"),
    ("nhà ở xã hội điều kiện mua",          "nha-o-xa-hoi", "T3_nghien_cuu", "phrase", 3, "tệp riêng, ngân sách thấp"),
    ("nhà ở xã hội mở bán mới nhất",        "nha-o-xa-hoi", "T2_giao_dich", "phrase", 2, "tệp riêng"),
    ("đăng ký nhà ở xã hội ở đâu",          "nha-o-xa-hoi", "T3_nghien_cuu", "phrase", 3, "tệp riêng"),
    ("tư vấn mua căn hộ miễn phí",          "tu-van-quyet-dinh", "T2_giao_dich", "phrase", 1, "intent liên hệ trực tiếp"),
    ("tư vấn đầu tư bất động sản",          "dau-tu",   "T2_giao_dich", "phrase", 2, "intent liên hệ"),
    ("nhận bảng giá dự án mới nhất",        "gia-bang-gia", "T2_giao_dich", "phrase", 1, "lead magnet"),
    ("đăng ký nhận thông tin dự án",        "gia-bang-gia", "T2_giao_dich", "phrase", 1, "lead magnet"),
    ("xem nhà mẫu căn hộ",                  "san-sang-o", "T2_giao_dich", "phrase", 1, "intent đi xem"),
    ("đặt cọc giữ chỗ dự án",               "mo-ban-moi", "T2_giao_dich", "phrase", 1, "intent chốt rất cao"),
    ("suất ngoại giao dự án",               "mo-ban-moi", "T2_giao_dich", "phrase", 2, "intent chốt cao"),
    ("mở bán đợt 1 giá gốc chủ đầu tư",     "mo-ban-moi", "T2_giao_dich", "phrase", 1, "intent chốt cao"),
    ("giá gốc chủ đầu tư",                  "mo-ban-moi", "T2_giao_dich", "phrase", 1, "intent chốt cao"),
    ("condotel có sổ hồng không",           "phap-ly",  "T3_nghien_cuu", "phrase", 3, "rào cản pháp lý BĐS nghỉ dưỡng"),
    ("sổ hồng lâu dài hay 50 năm",          "phap-ly",  "T3_nghien_cuu", "phrase", 3, "rào cản pháp lý"),
    ("officetel và condotel khác nhau",     "phap-ly",  "T3_nghien_cuu", "phrase", 3, "so sánh loại hình"),
    ("kinh nghiệm mua condotel tránh rủi ro", "tu-van-quyet-dinh", "T3_nghien_cuu", "phrase", 3, "top-funnel"),
    ("bất động sản nghỉ dưỡng có nên đầu tư", "dau-tu", "T3_nghien_cuu", "phrase", 3, "tệp đầu tư nghỉ dưỡng"),
    ("giá 1m2 căn hộ bao nhiêu",            "gia-bang-gia", "T3_nghien_cuu", "phrase", 3, "tham chiếu giá"),
    ("mua nhà cần chuẩn bị bao nhiêu tiền", "tai-chinh", "T3_nghien_cuu", "phrase", 3, "top-funnel"),
    ("nên mua nhà năm nay hay chờ",         "tu-van-quyet-dinh", "T3_nghien_cuu", "phrase", 3, "top-funnel, timing"),
    ("bất động sản sau sáp nhập tỉnh",      "dau-tu",   "T3_nghien_cuu", "phrase", 3, "chủ đề nóng 2025-2026"),
    ("dự án nào đáng đầu tư nhất 2026",     "dau-tu",   "T3_nghien_cuu", "phrase", 3, "tệp đầu tư"),
]

# head term chạy broad match để khám phá search term mới (bắt buộc kèm negative list + tCPA)
BROAD_SEEDS = [
    "mua căn hộ", "mua chung cư", "mua đất nền", "mua nhà phố", "mua biệt thự",
    "dự án căn hộ mới", "căn hộ mở bán", "đất nền dự án", "shophouse dự án",
    "bảng giá căn hộ", "chung cư mới mở bán", "mua nhà ở thực",
]

TODAY = date.today().isoformat()
MAXLEN, MAXWORDS = 80, 10


def slug(s):
    s = unicodedata.normalize("NFD", s)
    s = "".join(c for c in s if unicodedata.category(c) != "Mn").replace("đ", "d").replace("Đ", "d")
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")


def load_projects():
    """projects.tsv: tên dự án | chủ đầu tư | loại hình | khu vực | hạng(A/B) [| alias1, alias2]

    Cột 6 (alias) không bắt buộc: tên khác của CÙNG dự án (tên marketing, tên kèm
    tỉnh, tên phân khu). Alias dùng chung ad group brand với dự án gốc.
    """
    out = []
    if not os.path.exists(PROJ_FILE):
        return out
    with open(PROJ_FILE, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            p = [x.strip() for x in line.split("|")]
            while len(p) < 6:
                p.append("")
            out.append(tuple(p[:6]))
    return out


def main():
    rows, seen = [], set()

    def add(kw, adgroup, tier, loai, khu, match, prio, note):
        kw = re.sub(r"\s+", " ", kw.strip().lower())
        if not kw:
            return
        if len(kw) > MAXLEN or len(kw.split()) > MAXWORDS:
            return  # Google Ads: keyword tối đa 80 ký tự / 10 từ
        key = (kw, match)
        if key in seen:
            return
        seen.add(key)
        rows.append([kw, adgroup, tier, loai, khu, match, prio, note, TODAY])

    # 1) ma trận loại hình x khu vực x modifier
    # Chỉ loại hình CHÍNH của khu vực mới được fan-out toàn bộ modifier;
    # loại hình phụ chỉ lấy modifier giao dịch lõi -> tránh rác kiểu
    # "shophouse quận 7 có nên mua".
    for name, tinh, types, rank in REGIONS:
        n_types = 4 if rank == "A" else 3
        for i, t in enumerate(types[:n_types]):
            if i == 0:
                mods = (MOD_CORE + MOD_MID + MOD_RESEARCH) if rank == "A" else MOD_CORE
            else:
                mods = MOD_CORE[:5] if rank == "A" else MOD_B[:3]
            for mod, ag, tier, match, prio, note in mods:
                # đất nền không có phòng ngủ, không "bàn giao ngay" -> chặn modifier vô nghĩa
                if t == "đất nền" and ag in ("cau-hinh-can", "san-sang-o"):
                    continue
                ag_name = ag.format(t=slug(t))
                if mod == "":
                    kw = f"{t} {name}"
                elif mod in ("mua", "bán"):
                    kw = f"{mod} {t} {name}"
                elif mod == "dự án":
                    kw = f"dự án {t} {name}"
                elif mod == "dự án mới":
                    kw = f"dự án {t} mới {name}"
                elif mod == "sắp mở bán":
                    kw = f"{t} {name} sắp mở bán"
                elif mod == "có nên mua":
                    kw = f"có nên mua {t} {name}"
                elif mod == "ở đâu tốt":
                    kw = f"nên mua {t} {name} ở đâu"
                else:
                    kw = f"{t} {name} {mod}"
                add(kw, f"{slug(name)}--{ag_name}", tier, t, f"{name} ({tinh})",
                    match, prio, note)
                # head term của loại hình chính ở khu vực hạng A: thêm bản exact
                # để kiểm soát bid riêng (exact + phrase song song là chuẩn)
                if i == 0 and rank == "A" and prio == 1:
                    add(kw, f"{slug(name)}--{ag_name}", tier, t, f"{name} ({tinh})",
                        "exact", 1, note + " | bản exact để kiểm soát bid")

    # 2) tên dự án thật x modifier
    projects = load_projects()
    for pname, cdt, loai, khu, prank, aliases in projects:
        mods = MOD_PROJECT + (MOD_PROJECT_EXTRA if prank.upper() == "A" else [])
        names = [pname] + [a.strip() for a in aliases.split(",") if a.strip()]
        for nm in names:
            for mod, ag, tier, match, prio, note in mods:
                kw = f"{nm} {mod}".strip()
                note2 = note if not cdt else f"{note} | CĐT: {cdt}"
                if nm != pname:
                    note2 += f" | alias của '{pname}'"
                # alias dùng chung ad group brand của dự án gốc (không tách nhóm mới)
                add(kw, ag.format(p=slug(pname)), tier, loai, khu, match, prio, note2)

    # 3) chủ đầu tư x modifier
    for dev, khu in DEVELOPERS:
        for mod, ag, tier, match, prio, note in MOD_DEV:
            add(f"{dev} {mod}".strip(), f"{ag}--{slug(dev)}", tier, "chủ đầu tư", khu,
                match, prio, note)

    # 4) keyword phi khu vực
    for kw, ag, tier, match, prio, note in GENERIC:
        add(kw, ag, tier, "tổng hợp", "toàn quốc", match, prio, note)

    # 5) broad seed để khám phá search term
    for kw in BROAD_SEEDS:
        add(kw, "discovery-broad", "T2_giao_dich", "tổng hợp", "toàn quốc", "broad", 2,
            "broad match khám phá search term - BẮT BUỘC gắn negative list + tCPA, review hàng tuần")

    os.makedirs(os.path.dirname(os.path.abspath(OUT)), exist_ok=True)
    with open(OUT, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["keyword", "nhom_adgroup", "intent_tier", "loai_hinh", "khu_vuc",
                    "match_type", "uu_tien", "ghi_chu", "ngay_them"])
        w.writerows(rows)

    from collections import Counter
    print(f"{OUT}: {len(rows)} keywords")
    for k, v in sorted(Counter(r[2] for r in rows).items()):
        print(f"  {k}: {v}")
    print("  match_type:", dict(Counter(r[5] for r in rows)))
    print("  uu_tien:", dict(Counter(r[6] for r in rows)))
    print(f"  dự án thật: {len(projects)}")
    return rows


def check(rows):
    """self-check: không trùng, đúng giới hạn Google Ads, lowercase, đủ cột."""
    assert rows, "không sinh được keyword nào"
    seen = set()
    for r in rows:
        kw, match = r[0], r[5]
        assert len(r) == 9, f"thiếu cột: {r}"
        assert kw == kw.lower().strip(), f"chưa lowercase: {kw!r}"
        assert "  " not in kw, f"double space: {kw!r}"
        assert len(kw) <= MAXLEN, f"quá 80 ký tự: {kw!r}"
        assert len(kw.split()) <= MAXWORDS, f"quá 10 từ: {kw!r}"
        assert match in ("exact", "phrase", "broad"), f"match_type lạ: {match}"
        assert r[2].startswith(("T1", "T2", "T3")), f"intent_tier lạ: {r[2]}"
        assert str(r[6]) in ("1", "2", "3"), f"ưu tiên lạ: {r[6]}"
        assert (kw, match) not in seen, f"trùng: {kw}"
        seen.add((kw, match))
    print("  self-check: OK")


if __name__ == "__main__":
    check(main())
