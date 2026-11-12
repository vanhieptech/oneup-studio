# Treg TikTok — 2026-11-12

Treg-first theo quyết định của Hiệp 08/11/2026. **Không dùng Apify** (Treg có đủ capability; không có lỗi Treg thật).
Fetch: 2026-11-12 khoảng 07:52–08:00 (Asia/Saigon). Balance 0,83704 → 0,81280 = **$0,02424, 18 call** (tổng từng call khớp đúng hiệu balance, giả định không có agent khác tiêu cùng lúc).

## Call ledger

| # | Endpoint (provider) | Input | Call id | Cost | Ghi chú |
|---|---|---|---|---|---|
| 1 | scrapecreators.tiktok.search.videos | iphone 5c (this-week, region=VN, trim) | 4b4aeff58881453daaf859b7bca0cdbd | $0.00188 | MCP cắt 8 KB → chỉ đọc được dòng 1 |
| 2 | 〃 | chup anh retro dien thoai cu | 8455974a36f242778ccfe03bd97378fa | $0.00188 | cắt, 1 dòng |
| 3 | 〃 | chien tranh lanh im lang | 91c461cadc2a4cf5917bb8517d276c65 | $0.00188 | cắt, 1 dòng (lạc đề quân sự) |
| 4 | 〃 | nhan tin khong tra loi | edabf1b224f740ef8a871560dfbd77f8 | $0.00188 | cắt, 1 dòng (caption «nhờn», không dùng) |
| 5 | 〃 | luot dien thoai luc xep hang cho | 20269d26ec5a4eebacdcc5fc3b3356d6 | $0.00188 | cắt, 1 dòng (clickbait y khoa → drop) |
| 6 | 〃 | gioi thieu ban than bang 1 buc anh | bf3d5d37885544f1aa3cbd5168e54ef5 | $0.00188 | 0 kết quả, vẫn tính phí |
| 7 | 〃 | ngu bao nhieu tieng la du | c6eed97c4625422ca1e167d589da5214 | $0.00188 | cắt, 1 dòng (lạc đề mèo) |
| 8 | 〃 | dien thoai cuc gach detox | e912d433e11f4770a099b6e32b1ede32 | $0.00188 | cắt, 1 dòng |
| 9 | anyapi.tiktok.search.videos | iphone 5c (datePosted 7, không `fields`) | e3054ea9193a40a98d74f4f008b0ab8b | $0.0006 | 25,6 KB → vẫn bị cắt |
| 10 | 〃 | chup anh iphone 5c retro (+`fields`) | c461d5104fbc40baa4d230ee1bb135ee | $0.0026 | 8 dòng đầy đủ |
| 11 | 〃 | chien tranh lanh im lang khong noi chuyen (+fields) | 00e35f07c9ba41b396008dcb5bbb9ff3 | $0.0006 | 10 dòng |
| 12 | 〃 | luot dien thoai luc cho doi (+fields) | fb839ded085d427b962d040c0dba9a09 | $0.0026 | not_found, vẫn tính phí |
| 13 | 〃 | gen z mua iphone cu chup anh (+fields) | ee6cdc6318de4130920c446a7fe6c805 | $0.0006 | 12 dòng |
| 14 | crawl4ai.tiktok.video.detail | 7706520170398813470 | aa5e4ad439b043fc9d7867d87e21cf04 | $0.0005 | music + subtitle track vie-VN |
| 15 | anyapi.tiktok.video.comments (+fields) | 7706520170398813470 | e42c2b8a908948809f03b1569f988534 | $0.0006 | 20 comment |
| 16 | anyapi.tiktok.video.comments (+fields) | 7705797885052439826 | 958c5a80be6b477ebf8e488390184050 | $0.0006 | 19 comment |
| 17 | crawl4ai.tiktok.video.detail | 7705797885052439826 | 931ed9ffcb9541d6948e5d6223e2a453 | $0.0005 | music, không subtitle |
| 18 | (balance ×2, catalog_search/get: miễn phí) | | | $0 | |

Tổng: 8 × 0,00188 + (0,0006 + 0,0026 + 0,0006 + 0,0026 + 0,0006) + 2 × 0,0005 + 2 × 0,0006 = **$0,02424**.
Transcript: tải subtitle WEBVTT của clip #14 bằng curl từ URL CDN công khai mà crawl4ai trả (miễn phí) → `vtt-chientranhlanh-7706520170398813470.vtt`.

## Coverage / limits
- **Giới hạn quan trọng hôm nay:** client MCP chỉ nhận **8.192 byte** mỗi kết quả (cả text lẫn structured content). Search ScrapeCreators (~850 KB/trang, kể cả trim=true) chỉ đọc được dòng đầu → 8 call gần như phí. Cách xử lý: dùng `anyapi.*` với query param `fields` (Treg hỗ trợ `fields`/`max_items`/`jq` cho anyapi) và `crawl4ai.tiktok.video.detail` (trả gọn, có music + subtitle URL). File `raw-sc-*.json` và `raw-any-search-iphone-5c-nofields.json` chỉ chứa phần đầu bị cắt (có `_note`).
- Videos: 30 dòng chuẩn hoá đầy đủ từ anyapi (`search-normalized.json`) + 7 dòng đầu từ ScrapeCreators. Ngày đăng thật 05/11 08:05 → 12/11 07:50 (giờ VN). Region provider trên 30 dòng: VN 19, US 5, GB 2, TW/CA/GE/KR 1. region=VN của ScrapeCreators chỉ đặt proxy, không lọc; anyapi không lọc vùng. Không chứng minh người xem VN.
- Search keyword ≠ bảng xếp hạng/For You; lượt xem là snapshot lifetime lúc fetch, không chứng minh đang tăng; fetched hôm nay ≠ đăng hôm nay.
- Comments: 2 clip (đều ≥10k tương tác, đã đọc caption trước). Trang đầu 19–20 comment theo thứ tự provider; mỗi comment = 1 lời tự kể, không phải tâm lý đám đông.
- Sound: chỉ từ 2 detail crawl4ai: skit = âm thanh gốc; clip 5C = «still love you (super slowed + reverb)» – GLM-RST (không original). anyapi search không trả music. Metadata ≠ quyền dùng lại. Không gọi sound chart.
- Transcript: 1/2 detail có subtitle thật (skit, vie-VN, là lời lồng tiếng). Clip 5C không có subtitle (chỉ nhạc). Caption ≠ transcript.
- anyapi tính phí cả khi `not_found` (call #12, $0,0026) dù catalog ghi per_success; ScrapeCreators tính phí cả khi 0 kết quả (#6).

## Scrub
Đã quét raw bằng regex cho `cookie`, `set-cookie`, `tt_chain_token`, `token`, `access_token`, `sessionid`, `msToken`, `x-tt-token` → thay `[REDACTED]` trước khi lưu. URL CDN có chữ ký hết hạn (x-signature, refresh_token của ảnh) là tham số URL công khai, không phải thông tin đăng nhập.

## Lessons
- Trước call search/detail lớn: ưu tiên endpoint có `fields`/`jq` (anyapi) hoặc trả gọn (crawl4ai) vì MCP cắt 8 KB. ScrapeCreators search/detail không còn đọc được qua MCP ở box này.
- crawl4ai detail ($0,0005) cho music + danh sách subtitle; tải VTT qua URL CDN là miễn phí → rẻ hơn scrapecreators detail ($0,00188).
