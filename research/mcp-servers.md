# Research: MCP servers cho hệ thống ads (2026-07-28)

Nguồn: subagent research, số stars/last-push kiểm tra qua GitHub API ngày 2026-07-28.

## Ranked

| # | MCP | Author | Install | Verdict |
|---|-----|--------|---------|---------|
| 1 | googleads/google-ads-mcp | Google official | uvx/pipx từ git | **Must-have** — nhưng READ-ONLY, chỉ 3 tools (GAQL search, list accounts, metadata) |
| 2 | googleanalytics/google-analytics-mcp | Google official | `pipx run analytics-mcp` | **Must-have** |
| 3 | AminForou/mcp-gsc (Search Console) | community 1254★ | Python venv | **Must-have** (phase 2) |
| 4 | Meta Ads (Pipeboard) | Meta Business Partner | **đã có claude.ai connector** | Must-have, không cần cài |
| 5 | ncosentino/google-keyword-planner-mcp | community 27★ | binary Go | Nice-to-have — lấp lỗ Keyword Planner |
| 6 | FGRibreau/mcp-google-ads | community 17★ | cargo build | Nice-to-have — 48 tools, có write + Keyword Planner, trust thấp |
| 7 | xing5/mcp-google-sheets | community 964★ | `uvx mcp-google-sheets@latest` | **Must-have cho reporting** (phase 2) |
| 8 | DataForSEO | official | `npx dataforseo-mcp-server@latest` | **Must-have cho keyword VN** — pay-as-you-go, location_code 1028581 = Vietnam |
| 9 | Semrush | official | **đã có claude.ai connector** | Nice-to-have, data VN mỏng |
| 10 | HubSpot remote | official | url https://mcp.hubspot.com | Chỉ khi CRM là HubSpot |

## Bỏ hẳn
- Keap MCPs (0★, không license) → gọi Keap REST API trực tiếp
- Zalo MCPs (0★ hoặc automation cá nhân, risk khóa acc) → gọi ZNS API từ CRM webhook
- Ahrefs (repo archived + cần plan $129/mo), cohnen/mcp-google-ads (stale 9 tháng), gomarble (stale)
- irinabuht12-oss/google-meta-ads-ga4-mcp (star pattern đáng ngờ)

## Gaps quan trọng
1. **Keyword Planner KHÔNG có trong official Google Ads MCP** → dùng DataForSEO hoặc ncosentino khi cần volume/forecast.
2. **Call tracking VN: không có MCP** — Stringee/CareSoft có REST API, bọc script mỏng nếu cần.
3. **Developer token là bottleneck**: apply Basic access qua MCC mất 1-3 ngày, làm TRƯỚC TIÊN.

## Keyword Planner VN
`generate_keyword_ideas` nhận `languageConstants/1040` (Vietnamese) nhưng không rõ geo param → volume riêng HCM/HN dùng DataForSEO chắc hơn.

Full sources: xem transcript research 2026-07-28.
