---
title: "Treg TikTok research 2026-11-10"
date: 2026-11-10
type: trend-source
id: trends-2026-11-10-treg
status: raw-evidence
updated: 2026-11-10
source: "Treg MCP (team levanhiep-s-team)"
tags: [trends, tiktok, treg]
---
# Treg TikTok research 2026-11-10

Fetched 10/11/2026 ~08:10–08:35 giờ VN (UTC+7). Treg-first theo quyết định Hiệp 08/11. **Không dùng Apify** (Treg đủ; một clip không lấy được detail là do video không còn trả về, không phải Treg thiếu capability). Đã đọc `catalog_get` (schema + giá) cho `scrapecreators.tiktok.search.videos` ($0.00188), `scrapecreators.tiktok.video.detail` ($0.00188), `treg.tiktok.video.comments` (route, $0.001 tikhub) và `treg.tiktok.video.detail` (route, $0.001–0.01476; gọi với `X-Treg-Route-Waterfall: 0`) trước khi gọi.

## Calls (actual charges)
| # | job | endpoint (provider served) | input | call_id | cost USD |
|---|---|---|---|---|---|
| 1 | search | scrapecreators.tiktok.search.videos | query=lam xong viec som bi giao them, date_posted=this-week, region=VN, trim=true | 6effff99ae9e48d1825da5d3cf0336ab | 0.00188 |
| 2 | search | scrapecreators.tiktok.search.videos | query=meo tiet kiem thoi gian van phong (same filters) | 277f510036824365a25694ace6424f58 | 0.00188 |
| 3 | search | scrapecreators.tiktok.search.videos | query=lam nhieu viec cung luc | 18401d67ff694341a0b91f87f20892b1 | 0.00188 |
| 4 | search | scrapecreators.tiktok.search.videos | query=dung AI di lam | 1365785970e948eabe4749c0c5ee955b | 0.00188 |
| 5 | search | scrapecreators.tiktok.search.videos | query=hit tho sau binh tinh lai | 442cf4c40213403c9b0173b6ad1a967f | 0.00188 |
| 6 | search | scrapecreators.tiktok.search.videos | query=lam cang gioi viec cang nhieu | 4f664ad7c15744f4b6b5b76153492fbf | 0.00188 |
| 7 | search | scrapecreators.tiktok.search.videos | query=ngu bao nhieu tieng la du | 9fb361ed9fe14930ae358ace4f019f33 | 0.00188 |
| 8 | detail+transcript | scrapecreators.tiktok.video.detail | @koravel0 7704296499475172616 | d3542eafa37a4942b5e4058797f71ac1 | 0.00188 |
| 9 | detail+transcript | scrapecreators.tiktok.video.detail | @nguyen_919191 7703783477799390516 | d05a12751d0f4dc6b08db24416eba7ee | 0.00188 |
| 10 | detail+transcript | scrapecreators.tiktok.video.detail | @giang.gia.doi 7704181828688579848 | 7029040b8b58415ea7f8f30d8d34f36d | 0.00188 |
| 11 | comments | treg.tiktok.video.comments (tikhub app-v3) | 7704181828688579848, limit 20 | d7fef987df334f9a8542a3b5429d3215 | 0.001 |
| 12 | detail+transcript | scrapecreators.tiktok.video.detail | @onsportsplus 7705013968930196744 → **404 Video not found** | 3b1839b5f7a343619845430120e7c8a8 | 0.00 |
| 13 | comments | treg.tiktok.video.comments (tikhub app-v3) | 7705013968930196744, limit 20 | 91801c007efb4393b82a5def7297fc29 | 0.001 |
| 14 | detail | treg.tiktok.video.detail (tikhub app-v3 fetch-one-video, waterfall 0) | 7705013968930196744 → **miss, video=null** | 5363dafe8a6d43f4853dba60dd8384a9 | 0.001 |

**Tổng: 14 call (13 tính tiền), $0.0218** (balance 0.96187 → 0.94007, khớp đúng tổng `cost_usd`). Comments: header `X-Treg-Route-Max-Cost: 0.005`, cả 2 trúng ngay provider đầu (tikhub).

## Coverage & limits
- **Videos:** 7 keyword search → 172 kết quả (14–30/query). Đây là keyword search, **không phải bảng xếp hạng trend**, không phải For You feed. `date_posted=this-week` và `region=VN` là bộ lọc gửi upstream (provider ghi rõ không được bảo đảm; region chỉ đặt proxy). Trả về: ngày đăng thật 03–10/11 (không mục nào ngoài 7 ngày); trường `region` = VN 166, KR 3, JP 1, US 1, SG 1. Lượt xem/like/share là snapshot lifetime lúc fetch, không chứng minh đang tăng hay xếp hạng. Không sort theo like (relevance mặc định).
- Query yếu: «lam nhieu viec cung luc» (đa phần việc nhà/công nhân, lượt xem thấp), «meo tiet kiem thoi gian van phong» (giải trí văn phòng, mẹo Excel 11k), «hit tho sau binh tinh lai» kéo về fandom/golf; «ngu bao nhieu tieng la du» kéo về show giải trí. Chủ đề «làm giỏi bị giao thêm việc» ở VN chỉ có clip phạm vi rất thấp (353 và 129 xem).
- **Sound:** search `trim=true` không trả music (lần 3). Music lấy qua detail cho 3 clip: cả 3 là original sound của creator. Không gọi sound chart hôm nay. Metadata âm thanh không phải quyền dùng lại audio.
- **Transcript:** 2/3 detail có WEBVTT provider trả (@giang.gia.doi, @koravel0); @nguyen_919191 = null (chỉ caption). @onsportsplus: không lấy được (404 / miss): video có thể đã gỡ hoặc bị chặn vùng sau khi search trả về; link cần mở lại trước khi dùng.
- **Comments:** 2 clip × trang đầu 20, thứ tự provider. @giang.gia.doi: phần lớn chế giễu người nói trong clip (không dùng); 1 lời tự kể có ích («Tao nghỉ làm ở nhà 3 ngày mỳ tôm ko có mà ăn lại phải đi làm», 83 like). @onsportsplus: đoán tên cầu thủ, đùa bóng đá; 1 câu «Áp lực vãi chứ đừng có hỏi». Mỗi comment là một lời tự kể, không đại diện đám đông.
- Bài học: đọc caption + transcript trước khi trả comments (bỏ @koravel0 sau transcript, bỏ @nguyen_919191 vì 0 comment). Clip thể thao bản quyền (VTVcab) có thể bị gỡ nhanh: lấy detail ngay trong lượt search.

Files: `raw-search-*.json`, `raw-detail-*.json`, `raw-comments-*.json`, `search-normalized.json` (172 dòng), `shortlist.json` (5 clip).
