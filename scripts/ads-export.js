/**
 * Google Ads Script — xuất số liệu ngày ra Google Sheet để hệ đọc.
 * KHÔNG cần developer token / API. Chỉ cần quyền Chuẩn (Standard) trên tài khoản Ads.
 *
 * Cài: Google Ads → Công cụ → Thao tác hàng loạt → Tập lệnh → + → dán file này
 *      → sửa SHEET_URL → Chạy thử → Ủy quyền → Đặt lịch chạy HẰNG NGÀY (04:00).
 *
 * Sheet: tạo Google Sheet trống, dán URL vào SHEET_URL bên dưới.
 * Sau đó File → Chia sẻ → Xuất bản lên web → chọn từng tab → CSV → copy link cho Claude.
 *
 * ponytail: 1 script, 3 tab, không thư viện. Số liệu THEO NGÀY (không phải tổng kỳ)
 * vì quét điểm gãy chuỗi thời gian (playbook/monitoring.md §4) cần dữ liệu ngày.
 */

var SHEET_URL = 'DÁN_URL_GOOGLE_SHEET_VÀO_ĐÂY';
var DAYS = 90; // cửa sổ xuất, ghi đè toàn bộ mỗi lần chạy

function main() {
  var ss = SpreadsheetApp.openByUrl(SHEET_URL);
  var range = lastNDays(DAYS);

  dump(ss, 'campaign_daily',
    ['Ngay', 'Campaign', 'TrangThai', 'ChiPhi', 'Click', 'HienThi', 'CTR', 'CPC',
     'ChuyenDoi', 'ChiPhi/ChuyenDoi', 'IS_TimKiem', 'IS_Mat_NganSach', 'IS_Mat_ThuHang'],
    campaignRows(range));

  dump(ss, 'search_terms',
    ['CumTuTimKiem', 'Campaign', 'AdGroup', 'ChiPhi', 'Click', 'HienThi', 'ChuyenDoi'],
    searchTermRows(range));

  dump(ss, 'keyword_daily',
    ['Ngay', 'TuKhoa', 'KieuKhop', 'Campaign', 'ChiPhi', 'Click', 'ChuyenDoi', 'QualityScore'],
    keywordRows(range));

  Logger.log('Xong: ' + range.label);
}

/* ---------- truy vấn ---------- */

function campaignRows(r) {
  var q = 'SELECT segments.date, campaign.name, campaign.status, metrics.cost_micros, ' +
    'metrics.clicks, metrics.impressions, metrics.ctr, metrics.average_cpc, ' +
    'metrics.conversions, metrics.cost_per_conversion, ' +
    'metrics.search_impression_share, metrics.search_budget_lost_impression_share, ' +
    'metrics.search_rank_lost_impression_share ' +
    'FROM campaign WHERE segments.date BETWEEN "' + r.from + '" AND "' + r.to + '" ' +
    'AND metrics.impressions > 0';
  var out = [], it = AdsApp.search(q);
  while (it.hasNext()) {
    var x = it.next();
    out.push([x.segments.date, x.campaign.name, x.campaign.status,
      micros(x.metrics.costMicros), num(x.metrics.clicks), num(x.metrics.impressions),
      num(x.metrics.ctr), micros(x.metrics.averageCpc), num(x.metrics.conversions),
      micros(x.metrics.costPerConversion), num(x.metrics.searchImpressionShare),
      num(x.metrics.searchBudgetLostImpressionShare),
      num(x.metrics.searchRankLostImpressionShare)]);
  }
  return out;
}

function searchTermRows(r) {
  var q = 'SELECT search_term_view.search_term, campaign.name, ad_group.name, ' +
    'metrics.cost_micros, metrics.clicks, metrics.impressions, metrics.conversions ' +
    'FROM search_term_view WHERE segments.date BETWEEN "' + r.from + '" AND "' + r.to + '"';
  var out = [], it = AdsApp.search(q);
  while (it.hasNext()) {
    var x = it.next();
    out.push([x.searchTermView.searchTerm, x.campaign.name, x.adGroup.name,
      micros(x.metrics.costMicros), num(x.metrics.clicks),
      num(x.metrics.impressions), num(x.metrics.conversions)]);
  }
  return out;
}

function keywordRows(r) {
  var q = 'SELECT segments.date, ad_group_criterion.keyword.text, ' +
    'ad_group_criterion.keyword.match_type, campaign.name, metrics.cost_micros, ' +
    'metrics.clicks, metrics.conversions, ad_group_criterion.quality_info.quality_score ' +
    'FROM keyword_view WHERE segments.date BETWEEN "' + r.from + '" AND "' + r.to + '" ' +
    'AND metrics.impressions > 0';
  var out = [], it = AdsApp.search(q);
  while (it.hasNext()) {
    var x = it.next();
    var k = x.adGroupCriterion.keyword || {};
    var qi = x.adGroupCriterion.qualityInfo || {};
    out.push([x.segments.date, k.text, k.matchType, x.campaign.name,
      micros(x.metrics.costMicros), num(x.metrics.clicks),
      num(x.metrics.conversions), num(qi.qualityScore)]);
  }
  return out;
}

/* ---------- tiện ích ---------- */

function dump(ss, tabName, header, rows) {
  var sh = ss.getSheetByName(tabName) || ss.insertSheet(tabName);
  sh.clear();
  sh.getRange(1, 1, 1, header.length).setValues([header]);
  if (rows.length) sh.getRange(2, 1, rows.length, header.length).setValues(rows);
  Logger.log(tabName + ': ' + rows.length + ' dong');
}

function lastNDays(n) {
  var tz = AdsApp.currentAccount().getTimeZone();
  var to = new Date(); to.setDate(to.getDate() - 1);        // hôm qua (ngày đủ dữ liệu)
  var from = new Date(); from.setDate(from.getDate() - n);
  var f = function (d) { return Utilities.formatDate(d, tz, 'yyyy-MM-dd'); };
  return { from: f(from), to: f(to), label: f(from) + '..' + f(to) };
}

function micros(v) { return v ? Number(v) / 1000000 : 0; }
function num(v) { return v ? Number(v) : 0; }
