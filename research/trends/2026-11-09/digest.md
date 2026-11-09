---
title: "Trend digest 2026-11-09"
source: "pipeline/scripts/trend-collect.py + X MCP extra + Treg TikTok (scrapecreators/tikhub)"
id: trends-2026-11-09
type: trend-digest
status: draft-needs-review
updated: 2026-11-09
tags: [trends, digest, daily]
date: 2026-11-09
collector: pipeline/scripts/trend-collect.py + X MCP + Treg
skill: trend-digest v4 (+ tiktok-research-via-treg, quyết định Hiệp 08/11)
---
# Trend digest 2026-11-09 (thứ Hai)

**Nguồn:** 34/36 collector ok. Lỗi: wiki-vi + wiki-en (HTTP 404, như các ngày trước). kym-memes hôm nay chạy lại được (16 mục). **X MCP: có chạy.** Trends VN 30 mục («Tuần», «Thứ 2», «Thứ Hai», «Khởi», «Mùng 1», «Lạnh» là móc lịch/thời tiết; còn lại fandom Thái, anime, Jensen Huang (scandal đời tư): bỏ). Worldwide 30 mục (bóng bầu dục Mỹ, Nvidia, Diwali: không dùng). 40 story X News từ 4 query (habits productivity, AI at work burnout, Vietnam gen Z, Monday motivation self improvement; max_age 72h). Gộp `x-extra.json` (100 mục), bản gốc trong `x-raw/`.
**Treg TikTok: CÓ chạy (Treg-first).** 12 call, tổng **$0,01904** (5 keyword search ScrapeCreators, 1 Viral 50 sound chart tikhub, 3 video detail + transcript, 3 comments qua route tikhub). 140 kết quả search (30 của query «moi ngay 1000 chu» là spam follow chéo, bỏ). Transcript thật 2/3; music 3/3 qua detail (đều original sound). **Không dùng Apify** (Treg đủ). Chi tiết call id, giới hạn: `treg/README.md`.
**Giới hạn TikTok:** keyword search, không phải bảng xếp hạng trend. `region=VN` chỉ là proxy (trường region trả về VN hoặc JP); `date_posted=this-week` không bảo đảm nhưng ngày đăng thật đều trong 02–09/11. Lượt xem là snapshot lifetime lúc ~08:15 giờ VN, không chứng minh đang tăng. Comment là trang đầu 20 cái theo thứ tự provider. Viral 50 không có bộ lọc vùng.
**Số lượng:** collector 500 thô → 466 cụm. raw.json 472 mục (thêm 6 TikTok-native): 375 ok · 24 caution · 73 drop (11 drop tay). **399 qua lọc.** Chấm tay 15 mục. Drop tay: vụ án Mr Pips (3 tin), ngoại tình CEO Nvidia (3 tin), diễn viên qua đời sau phẫu thuật, hoa hậu bị chê kém sắc, trầm cảm / ADHD (nhãn y khoa), «búp bê = cô đơn» (nhãn tâm lý). Đã bỏ trong TikTok: tai nạn CLB Tenerife, bệnh, chính trị (đoàn lãnh đạo), nổ ở Iran, lương tối thiểu (chính sách).

Dữ liệu: `collect.json`, `collect-run.log`, `x-extra.json`, `x-raw/`, `raw.json`, `score.txt`, `ideas.json`, `plans/`, `treg/`.

## Top 10 (đã lọc)
| # | Trend | rank | nov / sat | Nguồn | Bài học (phần.mục) | Theme |
|---|---|---|---|---|---|---|
| 1 | Kim Dung «17 năm không nghỉ, ít nhất 1.000 chữ mỗi ngày»; bài kể đơn vị làm việc là một kỳ báo 1.000–1.200 chữ, viết bộ đầu chưa biết có bộ thứ hai (Kenh14, 2 chuyên mục) | 0.919 | 1.0 / 0.05 | [Kenh14 09/11](https://kenh14.vn/kim-dung-va-hanh-trinh-viet-17-nam-khong-nghi-tu-1000-chu-moi-ngay-cho-den-3-lan-dai-tu-kiet-tac-215261108191318875.chn) | 4.7 / ô #27 | LIGHT |
| 2 | TikTok CafeF «Lương 31 triệu, tiết kiệm 20 triệu: Còn 11 triệu tiêu mãi không hết!» (171.197 xem, 112 comment, đăng 06/11, transcript thật); comment tự kể «sao mình với ck tháng làm 80 củ mà ko dư ngàn nào nhỉ» | 0.857 | 1.0 / 0.1 | [TikTok @cafef_official](https://www.tiktok.com/@cafef_official/video/7704990703348305160) | 5.1 / đăng #28 | DARK |
| 3 | TikTok «Cái bẫy so sánh… Social Comparison» (553.775 xem, 499 comment; search only) | 0.624 | 1.0 / 0.35 | [TikTok @ai.cbap](https://www.tiktok.com/@ai.cbap/video/7704737065958919444) | 3.20 / đăng #22: bão hoà (6 bridge), chỉ là bằng chứng | DARK |
| 4 | X: buông ghen tị, lo đường của mình | 0.548 | 1.0 / 0.3 | [X News](https://x.com/i/trending/2119396468901437905) | 3.20 (bằng chứng, như #3) | — |
| 5 | TikTok vợ chồng công nhân ghi chi tiêu «ăn uống 2tr5» (139.206 xem, 299 comment); comment «Thấy ngta tiết kiệm sao ngưỡng mộ ghê.. nhà t 2 vc ăn muốn mạt» (55 like) | 0.496 | 1.0 / 0.1 | [TikTok @thanhly2110](https://www.tiktok.com/@thanhly2110/video/7705026216276937992) | 5.1 (phụ) | — |
| 6 | VnExpress: thói quen chợp mắt nơi công cộng ở Nhật (chưa đọc bài) | 0.450 | 1.0 / 0.0 | [VnExpress](https://vnexpress.net/giai-ma-thoi-quen-ngu-gat-cua-nguoi-nhat-5141317.html) | 3.11 (phụ, đã có B-nap-01) | — |
| 7 | TikTok «Hôm nay Thứ Hai đầu tuần (09/11)… chỉ còn đúng 13 sáng Thứ Hai phải tắt báo thức… nữa là đến Tết!» (351.316 xem, 24.506 share, đăng 09/11) | 0.406 | 1.0 / 0.35 | [TikTok @sapdentet.vn](https://www.tiktok.com/@sapdentet.vn/video/7705840473956502802) | callback B-hetnam-01 (ô #27): cùng họ đếm ngược | — |
| 8 | Kenh14: «Càng cố tiết kiệm, càng dễ mất tiền vì 6 thứ này» (mã URL gợi ý bài gốc 07/2026, đăng lại; chưa tự kiểm) | 0.396 | 1.0 / 0.05 | [Kenh14](https://kenh14.vn/cang-co-tiet-kiem-cang-de-mat-tien-vi-6-thu-nay-215260711225621284.chn) | 5.x (phụ) | — |
| 9 | X: Sunday scaries trước thứ Hai 09/11 (số WSJ trong tóm tắt, chưa tự kiểm) | 0.393 | 1.0 / 0.25 | [X News](https://x.com/i/trending/2119594004484612213) | callback B-chunhatoi-01 (#24) | — |
| 10 | X: kỷ luật và kế hoạch hơn may rủi (dân trade) | 0.510 | 1.0 / 0.0 | [X News](https://x.com/i/trending/2119182988902601160) | pattern; trade = tiền đầu cơ, không bridge | — |

Đã xem và bỏ khỏi top: Bryan Johnson «động lực tới sau khi bắt đầu» (người nổi tiếng, đã thấy 08/11), «mất động lực, lười quá» (@tranen1990: comment toàn chào hỏi/sticker, không có pain), bảng giá 1938 (giá Mỹ), Quỳnh Lương / hoa hậu / showbiz, laptop khuyến mãi, «trì hoãn không phải lười» trên YouTube (bão hoà, chỉ là bằng chứng pattern).

## TikTok signals (Treg, snapshot 09/11 ~08:15 giờ VN)
| keyword | clip | xem / comment / share | hook / transcript (nguồn) | sound | brand-safe? | bridge |
|---|---|---|---|---|---|---|
| tiet kiem tien luong | [@cafef_official](https://www.tiktok.com/@cafef_official/video/7704990703348305160) · đăng 06/11 21:05 · 83s | 171.197 / 112 / 420 | transcript thật: «lương 31.000.000, tiết kiệm 20.000.000 còn 11.000.000 tiêu mãi không hết… cô gái 28 tuổi ở Thành phố Hồ Chí Minh»; comment (trích nguyên văn, mỗi cái một lời tự kể): «sao mình với ck tháng làm 80 củ mà ko dư ngàn nào nhỉ..» (0 like), «Nhiều người kiếm nhiều tiêu nhiều, chưa chắc đã để dư đâu» (1 like) | original sound (CafeF) | ok; không dùng tên/tuổi cô gái, không chê ai | B-ro-tien-01 → #28 |
| tiet kiem tien luong | [@thanhly2110](https://www.tiktok.com/@thanhly2110/video/7705026216276937992) · đăng 06/11 | 139.206 / 299 / 324 | caption «Tập 170: Nhiều ac nói khoản ăn uống mà có 2tr5 thì chắc ăn nước mắm»; comment «Thấy ngta tiết kiệm sao ngưỡng mộ ghê.. nhà t 2 vc ăn muốn mạt» (55 like) | chưa lấy (search trim) | ok; bỏ các comment chê mức lương | B-ro-tien-01 (phụ) |
| tiet kiem tien luong | [@radio.mi.ngy0](https://www.tiktok.com/@radio.mi.ngy0/video/7704714527283236117) · đăng 05/11 · 288s | 548 / 0 / 1 | transcript thật: «tại sao thu nhập của bạn đã tăng gấp đôi so với ba năm trước mà cuối tháng tài khoản vẫn cạn như cũ… bạn đang so sánh sai đối tượng» (phạm vi thấp; góc là so sánh 3.20) | original sound | ok | pattern P10 |
| so sanh ban than | [@ai.cbap](https://www.tiktok.com/@ai.cbap/video/7704737065958919444) · đăng 06/11 | 553.775 / 499 / 20.620 | caption «Cái bẫy so sánh điểm số và cuộc chiến với chính mình» (không lấy transcript) | chưa lấy | ok, nhưng L-087: không dùng «điểm số» làm ví dụ | 3.20 bão hoà |
| thu hai di lam | [@sapdentet.vn](https://www.tiktok.com/@sapdentet.vn/video/7705840473956502802) · đăng 09/11 | 351.316 / 215 / 24.506 | caption đếm 13 sáng thứ Hai tới Tết (ngày Tết chưa tự kiểm) | chưa lấy | ok | callback B-hetnam-01 |
| khong co dong luc | [@tranen1990](https://www.tiktok.com/@tranen1990/video/7704573745087663378) · đăng 05/11 · 52s | 11.762 / 62 / 61 | caption «Tự nhiên mất động lực..lười quá sao giờ»; transcript null; 20 comment đầu là chào hỏi/sticker | original sound | ok, không có bằng chứng pain | — |

**Sound (Viral 50, tikhub, cập nhật 09/11 07:00 giờ VN, không rõ vùng):** top gồm «Ramalama (Bang Bang)» (Róisín Murphy), «Time (2011 Remastered Version)» (Pink Floyd), «we fell in love in october» (girl in red, đã ghi 13/10), «All I Want For Christmas Is You» (Mariah Carey, mùa vụ). Đây là metadata, không phải quyền dùng lại audio; series là comic, không mượn audio nguồn.

## Learning
- **Thêm F10 (salary-split reveal):** «lương X, để dành Y, còn Z» xuất hiện ở ≥2 clip tín hiệu cao trong tuần (@cafef_official 171k, @thanhly2110 139k, cộng nhiều clip nhỏ chia 70/20/10). Comment dưới các clip này là chỗ người xem tự so mình («ngưỡng mộ ghê», «làm 80 củ mà ko dư») → nối được cả 5.x lẫn 3.20. Không thêm P-row. P03 / P10 / P05 / P12 +1.
- **Đơn vị việc thay cho ý chí:** bài Kim Dung là câu chuyện kỷ luật, nhưng chi tiết đắt nhất là đơn vị một kỳ báo trong một lần ngồi. Đây là cầu tốt hơn «10.000 giờ» (bài báo có nhắc, mình không dùng vì không có trong sách).
- **Treg:** search trim vẫn mất music (lần 2). Comment route tikhub rẻ ($0,001) nhưng clip có caption hay vẫn có thể ra 0 bằng chứng (@tranen1990 toàn chào hỏi): xem `comment_count` và mẫu caption trước khi trả tiền comment. Query tiếng Việt không dấu kiểu «moi ngay 1000 chu» kéo về spam follow chéo: tránh số + «moi ngay».
- Bão hoà nên tránh: so sánh 3.20 (6 bridge), đếm ngược Tết/hết năm (đã pick 08/11), trì hoãn góc thẳng, Sunday scaries (đã pick 08/11), «kỷ luật hơn động lực».

## Bridges
| id | Trend | Khoảnh khắc | Bài học | Hook VI (pattern) | Góc | Đích | Theme |
|---|---|---|---|---|---|---|---|
| B-moiky-01 | Kenh14 Kim Dung 1.000 chữ/ngày | mở file «Tổng kết 2026», nhìn tiêu đề rồi đi pha cà phê | 4.7 (mức B) | "Kim Dung viết mười lăm bộ truyện, mà chưa bao giờ lên kế hoạch cho cả mười lăm bộ. Mỗi ngày ông chỉ lo đúng một kỳ báo." (P03+P06) | contrarian / story | ô #27 (LIGHT) ứng viên, hoặc 4.7 ý tưởng mới (callback clip-03) | LIGHT |
| B-ro-tien-01 | TikTok CafeF «lương 31tr tiết kiệm 20tr» + comment | ngày lương về, app ngân hàng có một loạt dòng trừ nhỏ: phim, nhạc, lưu trữ ảnh, app tập mở một lần | 5.1 (mức C; bỏ phần luật Trung Quốc) | "Trên mạng có cô gái lương ba mươi mốt triệu, để dành được hai mươi triệu. Còn bạn làm cũng không ít, mà cuối tháng không dư đồng nào?" (P10+P03+F10) | empathy / data | đăng #28 (5.1, DARK), bridge đầu tiên cho ô này | DARK |

Cầu nối về trục kênh (trend chỉ là móc): B-moiky-01 → hôm nay cắt việc lớn đang dời ra phần đầu tiên vừa một lần ngồi, làm xong nó (+1). B-ro-tien-01 → tối nay tắt đúng một gói trả tiền tự động không còn dùng (+1). Cả hai không nhắc lại 08/11 (thức khuya #14, hết năm #27, Chủ nhật #24).

**Tách lớp bằng chứng:** (a) trend = bài Kenh14 và clip/comment TikTok ở trên; (b) fact sách = 4.7 (Kruger & Evans 2004, Steel 2007; mức B, sách ghi chưa kiểm được phần trăm) và 5.1 (mức C; nguồn là quy định Trung Quốc, chỉ dùng phần hành động); (c) cầu nối và hook = đề xuất biên tập của Social Research, chưa phải fact.

## Differentiation
- **B-moiky-01:** Mọi người đang nói: Kim Dung là bậc thầy kỷ luật, 17 năm không nghỉ, kèm luận điểm 10.000 giờ ([Kenh14](https://kenh14.vn/kim-dung-va-hanh-trinh-viet-17-nam-khong-nghi-tu-1000-chu-moi-ngay-cho-den-3-lan-dai-tu-kiet-tac-215261108191318875.chn)). Góc của mình: thứ giữ ông viết mỗi ngày là đơn vị việc đủ nhỏ (một kỳ, một lần ngồi), và ông không lên kế hoạch cả 15 bộ; đó đúng là 4.7. Khác clip-03 (mở bằng bẫy, DARK) và B-30canh-01 (4.12).
- **B-ro-tien-01:** Mọi người đang nói: tiết kiệm trước tiêu sau, chia 70/20/10, mang cơm nhà ([@dilamkhon](https://www.tiktok.com/@dilamkhon/video/7703802755164425490), [@dang199x.tietkiem](https://www.tiktok.com/@dang199x.tietkiem/video/7705274513352707348)), hoặc khen/so người để dành giỏi. Góc của mình: không so lương, không chê ai; trước khi tự trách, tìm khoản rò tự trừ mà không ai thấy. Khác B-gachngang-01 (5.24 giá gạch mùa sale) và B-cooloff-01 (5.23).

## Plan stubs
- `plans/plan-1-kim-dung-moi-ngay-mot-ky.json`: ✔ validate 9 cảnh, 68,00s (stub-needs-approval). Trend ở b01–b02 + thẻ chữ «Kim Dung · 1.000 chữ mỗi ngày · Kenh14 09/11» (L-084). Ví dụ đời thường: báo cáo cuối năm, cà phê. Tuần 5, không Omi. Theme light.
- `plans/plan-2-lam-nhieu-ma-khong-du.json`: ✔ validate 9 cảnh, 67,00s (stub-needs-approval). Trend ở b01–b02 + thẻ chữ «Lương 31tr tiết kiệm 20tr · TikTok CafeF 06/11» (L-084). Ví dụ: phim, nhạc, lưu trữ ảnh, app tập. Tuần 5, không Omi. Theme dark.
- `check-rules.py --subjects` (ideas + 2 stub): PASS (L-087).
- Độ dài stub ~68s chỉ là khung; độ dài thật theo L-099 (<300s, mục tiêu 2–3 phút) do OpenCreator quyết sau khi Deep Research kiểm 4.7 / 5.1. Stub không cho phép tạo hình, giọng, render hay đăng trước Chốt.

## Script hooks (cần Hiệp duyệt)
1. "Kim Dung viết mười lăm bộ truyện, mà chưa bao giờ lên kế hoạch cho cả mười lăm bộ. Mỗi ngày ông chỉ lo đúng một kỳ báo." (B-moiky-01, 4.7, ô #27, LIGHT). Caution: người thật đã mất, chỉ nói tích cực; không dùng chuyện giỗ.
2. "Trên mạng có cô gái lương ba mươi mốt triệu, để dành được hai mươi triệu. Còn bạn làm cũng không ít, mà cuối tháng không dư đồng nào?" (B-ro-tien-01, 5.1, đăng #28, DARK).
3. (phụ, không thành stub) "Còn mười ba sáng thứ Hai phải tắt báo thức nữa là Tết. Sáng nay bạn tắt báo thức xong làm gì đầu tiên?" (callback B-hetnam-01; cùng họ đếm ngược đã pick 08/11).

## Safety notes
- B-moiky-01: Kim Dung là người thật đã mất (caution, chỉ tích cực). Không vẽ chân dung, không ảnh bìa sách, không dùng «10.000 giờ». Chi tiết lịch sử theo Kenh14, chưa tự kiểm.
- B-ro-tien-01: không nêu tên/tuổi cô gái trong clip; không so lương người xem; không nói luật (nguồn sách là quy định Trung Quốc). Comment trích là lời tự kể của một người, không đại diện.
- @ai.cbap: caption nói điểm số → không dùng làm ví dụ (L-087).
- Chính trị, tội phạm, bệnh, bi kịch, tâm linh, vàng, xổ số, rượu bia, đời tư người nổi tiếng: bỏ.

## Trạng thái đang chờ
- Ô #27: B-thang11-01, B-muathoigian-01, B-chonviec-01, B-hetnam-01, **+ B-moiky-01**. Đăng #28 (5.1): **B-ro-tien-01 (đầu tiên)**.
- Hôm nay thứ Hai: không có weekly synthesis.
