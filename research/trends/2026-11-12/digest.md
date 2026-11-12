---
title: "Trend digest 2026-11-12"
source: "pipeline/scripts/trend-collect.py + X MCP extra + Treg TikTok (anyapi/crawl4ai/scrapecreators)"
id: trends-2026-11-12
type: trend-digest
status: draft-needs-review
updated: 2026-11-12
tags: [trends, digest, daily]
date: 2026-11-12
collector: pipeline/scripts/trend-collect.py + X MCP + Treg
skill: trend-digest v4 (+ tiktok-research-via-treg, quyết định Hiệp 08/11)
---
# Trend digest 2026-11-12 (thứ Năm)

**Nguồn:** 34/36 collector ok. Lỗi: wiki-vi + wiki-en (HTTP 404, như các ngày trước). **X MCP: có chạy.** Trends VN 30 mục (toàn «Thứ 5», «Chào», «Sáng»… là từ chào/lịch, còn lại fandom Thái, crypto, Riyadh/Jeddah, «Inflation», Jensen: bỏ). Worldwide 30 mục (Nvidia/Jensen, Veterans Day, thể thao, Nhật/Brazil: bỏ). X News 39 tin từ 4 query (habits productivity, AI at work, Vietnam gen Z, burnout sleep; max_age_hours 72).
**Treg TikTok: CÓ chạy (Treg-first).** 18 call, tổng **$0,02424** (balance 0,83704 → 0,81280, khớp tổng từng call). **Không dùng Apify** (không thiếu capability, không có lỗi Treg thật). Chi tiết: `treg/README.md`.
**Giới hạn TikTok (quan trọng):** client MCP hôm nay cắt mọi kết quả ở **8.192 byte**, nên 8 call search ScrapeCreators chỉ đọc được dòng đầu (≈$0,015 gần như phí). Đổi sang `anyapi.tiktok.search.videos` + `fields` và `crawl4ai.tiktok.video.detail`. Keyword search, không phải bảng xếp hạng hay For You. Region là trường provider (30 dòng: VN 19, US 5, GB 2, khác 4), không chứng minh người xem VN. Ngày đăng thật 05–12/11. Lượt xem là snapshot lifetime lúc ~07:52–08:00 giờ VN, không chứng minh đang tăng. Comment = trang đầu 19–20 dòng theo thứ tự provider; mỗi comment là một lời tự kể. Music chỉ có ở 2 detail; transcript thật 1/2.
**Số lượng:** collector 499 thô → 475 cụm. raw.json 479 mục (thêm 4 TikTok-native): 297 ok · 14 caution · 168 drop (52 drop từ bộ lọc từ khoá của collector, 115 drop tay, 1 TikTok). **311 qua lọc.** Drop tay: scandal/ghế CEO Nvidia, chính trị VN/Mỹ/Iran, kỷ luật cán bộ, vụ án/thi thể/tai nạn, bán độ, đời tư/hôn nhân sao, ung thư/ADHD/«bác sĩ cảnh báo», tỷ phú/cổ phiếu/crypto, heightmaxxing, thuốc lá/vape, X trends chào hỏi/fandom.

Dữ liệu: `collect.json`, `collect-run.log`, `x-extra.json`, `x-raw/`, `raw.json`, `score.txt`, `ideas.json`, `plans/`, `treg/`.

## Top 10 (đã lọc)
| # | Trend | rank | nov / sat | Nguồn | Bài học (phần.mục) | Theme |
|---|---|---|---|---|---|---|
| 1 | Gen Z lùng mua iPhone 5C (2013) để chụp ảnh Y2K; Compare and Recycle: tìm «mua iPhone 5C» +40.500% trong năm qua (số qua báo, **chưa tự kiểm**, toàn cầu); chuyên gia: máy dừng iOS 10.3.3 (2017), chỉ dùng như máy ảnh | 0.742 | 1.0 / 0.05 | [Thanh Niên 11/11](https://thanhnien.vn/gen-z-lung-mua-iphone-5c-luot-tim-kiem-tang-40500-185261111144622021.htm) · [TechRadar 10/11](https://www.techradar.com/phones/iphone/iphone-5c-searches-are-up-40-500-percent-as-gen-z-boards-the-retro-camera-trend-but-privacy-experts-warn-it-cant-protect-personal-data-in-the-way-more-modern-iphones-do) · GNews (Thanh Niên, Thương gia, Vietnam.vn) | 14.6 (+5.23) ý tưởng mới | DARK |
| 2 | TikTok so ảnh iPhone 5S/5C (#2000s): 78.904 xem / 12.418 like / 39 comment / 491 share / 1.790 lưu, đăng 08/11 20:51; comment «đang phân vân nên mua ip 5 hay 6 về chụo kh😔», «có ai bt chỗ nào pass ip 5c ok ko ạ😭» | 0.649 | 1.0 / 0.05 | [TikTok @hhaibinh_](https://www.tiktok.com/@hhaibinh_/video/7705797885052439826) | bằng chứng TikTok cho #1 | — |
| 3 | Kenh14 «Silent treatment: Khi sự im lặng trở thành một thứ vũ khí» (11/11, theo Phụ Nữ Mới) | 0.631 | 1.0 / 0.05 | [Kenh14](https://kenh14.vn/silent-treatment-khi-su-im-lang-tro-thanh-mot-thu-vu-khi-215261111075058205.chn) | 3.17 (+10.17) ý tưởng mới | DARK |
| 4 | TikTok skit lồng tiếng «Khi chúng tôi vừa chiến tranh lạnh, nhưng tôi không dám ngủ một mình» (93.700 xem / 97 comment / 950 share, đăng 10/11 19:34; transcript thật; có dấu hiệu reupload) | 0.605 | 1.0 / 0.05 | [TikTok](https://www.tiktok.com/@user2906592877976/video/7706520170398813470) | bằng chứng TikTok cho #3 | — |
| 5 | VnExpress «Cô gái Thanh Hóa đưa đặc sản rừng lên chợ mạng» (2 mục VnExpress) | 0.729 | 1.0 / 0.0 | [VnExpress](https://vnexpress.net/co-gai-thanh-hoa-dua-dac-san-rung-len-cho-mang-5138532.html) | người thật, chuyện kinh doanh: không bridge | — |
| 6 | TikTok «Nasa phải gọi bằng cụ: … chỉ dùng 1 chiếc điện thoại cùi nhưng chụp được bức ảnh…» (342.302 xem / 361 comment / 4.429 share, đăng 11/11) | — | 1.0 / 0.1 | [TikTok](https://www.tiktok.com/@d.v.t.g.3.6.9/video/7706602182891654418) | bằng chứng phụ #1 («máy cũ vẫn chụp đẹp»), người thật → caution | — |
| 7 | X News «New Study Pinpoints Ideal Sleep Range» (6,4–7,8 giờ, UK Biobank; có chữ tử vong) | — | 0.5 / 0.6 | [X News](https://x.com/i/trending/2119681579760984324) | đã ingest 10/11 (x-sleep-range-nature) → chỉ callback 3.3 #15 | — |
| 8 | Cụm YT niche «trì hoãn» (VN + EN, 12 video) | — | — / 0.8 | yt-niche (collect.json) | pattern-evidence, bão hoà (4.9 đã là đăng #2) | — |
| 9 | Tinhte «Boox Picco: máy đọc sách to bằng tấm thẻ, cho những phút rảnh tay» (lúc chờ cà phê, xếp hàng mọi người lấy điện thoại ra lướt) | — | 1.0 / 0.2 | [Tinhte](https://tinhte.vn/thread/trai-nghiem-boox-picco-may-doc-sach-to-bang-tam-the-danh-cho-nhung-phut-ranh-tay-trong-ngay.4191282/) | bài review sản phẩm (PR) → chỉ ghi khoảnh khắc «phút chờ» | — |
| 10 | X News «Meme Questions Hard Work's Limits and Need for Grace» / «Traders Stress Patience» | — | 1.0 / 0.3 | [X News](https://x.com/i/trending/2119785692138176522) | bridge yếu, bỏ | — |

Đã xem và bỏ khỏi top: «Cô gái 25 tuổi lướt điện thoại hơn 10 tiếng… kết luận từ bác sĩ» (TikTok 288.749 xem, clickbait y khoa → drop), «Văn Mai Hương, Tóc Tiên: trend giới thiệu bản thân bằng 1 bức ảnh» (sao thật; TikTok search ra 0 kết quả), «Bác sĩ Bạch Mai cảnh báo người dùng máy tính» (y khoa, tóm tắt không có nội dung), «Stove Clock Meme Captures ADHD Time Blindness» (nhãn y khoa), Gen Z Kenh14/X hút thuốc thay vape (drop), «Kids and immunity» (y khoa trẻ em).

## TikTok signals (Treg, snapshot 12/11 ~07:52–08:00 giờ VN)
| keyword | clip | xem / comment / share | hook / transcript (nguồn) | sound | brand-safe? | bridge |
|---|---|---|---|---|---|---|
| chup anh iphone 5c retro | [@hhaibinh_](https://www.tiktok.com/@hhaibinh_/video/7705797885052439826) · đăng 08/11 · 22s | 78.904 / 39 / 491 | caption chỉ hashtag «#iphone5s #iphone5c #2000s»; không có subtitle (crawl4ai); comment trích nguyên văn ở Top 10 #2 | «still love you (super slowed + reverb)» – GLM-RST (không original) | ok | B-5c-01 |
| iphone 5c | [@fixi.mobile.54.tk](https://www.tiktok.com/@fixi.mobile.54.tk/video/7706845085262007558) · tin 60s | 7.278 / 7 / 2 | caption «"Thảm họa" iPhone 5C bất ngờ hot trở lại, lượt tìm kiếm tăng 40.000%: Netizen ngơ ngác "Ủa mua máy này về làm gì?"» (caption ghi 40.000%, báo ghi 40.500%) | chưa lấy | ok | consensus B-5c-01 |
| gen z mua iphone cu chup anh | [@d.v.t.g.3.6.9](https://www.tiktok.com/@d.v.t.g.3.6.9/video/7706602182891654418) · đăng 11/11 · 42s | 342.302 / 361 / 4.429 | caption (Top 10 #6); không gọi detail | chưa lấy | caution (người thật) | phụ B-5c-01 |
| chien tranh lanh im lang | [@user2906592877976](https://www.tiktok.com/@user2906592877976/video/7706520170398813470) · đăng 10/11 · 59s | 93.700 / 97 / 950 | transcript thật (trích nguyên văn): «khi chúng tôi vừa chiến tranh lạnh / nhưng tôi không dám ngủ một mình / cũng chẳng muốn nói chuyện với anh ấy thế là / tôi quyết định gọi người giao hàng đến giúp mình»; comment top «Giờ dịch vụ phát triển thật 🤣🤣» (96 like) | âm thanh gốc | caution (reupload, không chép) | B-chienlanh-01 |
| chien tranh lanh im lang | [@k.e.v.i.e.t.l.o.i](https://www.tiktok.com/@k.e.v.i.e.t.l.o.i/video/7706916498115333396) · đăng 11/11 | 13.891 / 0 / 67 | caption «“Những người đột nhiên im lặng ít xuất hiện, ít nói… bởi họ đang đánh trận chiến khó nhất đời mình.”» | chưa lấy | ok | đối trọng consensus |
| luot dien thoai luc xep hang cho | [@meo_.bel9](https://www.tiktok.com/@meo_.bel9/video/7704996120476699924) | 288.749 / 27 / 2.082 | caption clickbait «… kết luận từ bác sĩ» | chưa lấy | drop | — |

Query yếu/lạc: «chien tranh lanh im lang» (ScrapeCreators ra clip quân sự), «nhan tin khong tra loi», «ngu bao nhieu tieng la du» (ra mèo), «dien thoai cuc gach detox», «gioi thieu ban than bang 1 buc anh» (0), «luot dien thoai luc cho doi» (anyapi not_found, vẫn tính phí). Sound metadata ≠ quyền dùng lại; không gọi sound chart.

## Learning
- **Trend công nghệ tiêu dùng nối được sang an toàn tài khoản (phần 14) mà không cần bàn chuyện mua:** báo đã tự kèm cảnh báo bảo mật; góc khác biệt là quay sang cái máy cũ người xem đang có (14.6), không cổ vũ, không chê Gen Z.
- **Silent treatment: consensus nhìn từ phía người bị im;** sách 3.17 có góc ngược (người phạt nghĩ lâu hơn, nén giận vô ích) → P03 tốt, nhưng thí nghiệm là trò chơi, phải nói rõ giới hạn.
- **Treg qua MCP:** kết quả bị cắt 8 KB → chọn endpoint có `fields`/`jq` (anyapi) hoặc gọn (crawl4ai) TRƯỚC khi gọi; kiểm kích thước bằng một call nhỏ trước khi chạy cả loạt.
- Bão hoà nên tránh: trì hoãn (YT cả cụm), giấc ngủ 6,4–7,8 giờ (đã ingest), cà phê chiều (pick 11/11), AI ở chỗ làm / «làm nhanh bị giao thêm việc» (pick 10/11), mệt mỏi giữa tuần (X burnout, 07/11).

## Bridges
| id | Trend | Khoảnh khắc | Bài học | Hook VI (pattern) | Góc | Đích | Theme |
|---|---|---|---|---|---|---|---|
| B-5c-01 | iPhone 5C retro (báo + TikTok) | lục ngăn kéo thấy máy cũ, cắm sạc, Zalo/Facebook/email vẫn còn đăng nhập | 14.6 (mức C) (+5.23) | "Gen Z đang lùng mua lại iPhone 5C, máy từ năm 2013, chỉ để chụp ảnh kiểu ngày xưa. Còn cái điện thoại cũ trong ngăn kéo nhà bạn, nó còn đăng nhập tài khoản của bạn không?" (P13+P01) | contrarian / empathy | ý tưởng mới 14.6 (trụ 5) | DARK |
| B-chienlanh-01 | silent treatment (Kenh14) + skit chiến tranh lạnh | cãi nhau xong để «đã xem», tối lướt điện thoại vẫn tua lại câu nói | 3.17 (mức B) (+10.17) | "Chiến tranh lạnh với người yêu, bạn tưởng mình im thì người kia mới là người khổ? Trên mạng đang có clip: vợ chồng giận nhau, vợ không thèm nói một câu mà cũng không dám ngủ một mình." (P10+P03) | contrarian / data | ý tưởng mới 3.17 (trụ 4) | DARK |
| (callback) | X sleep range 6,4–7,8 giờ | — | 3.3 (đăng #15) | không viết hook mới (đã có B-mettamsau-01) | — | đăng #15 | — |

**Trend trong clip (L-084):** B-5c-01 b01 = câu «Gen Z đang lùng mua lại iPhone 5C…» + hình hai máy cũ nhiều màu và khung ảnh retro (không logo). B-chienlanh-01 b01 = tình huống «chiến tranh lạnh mà không dám ngủ một mình» kể lại bằng lời (paraphrase, không chép skit), b02 = chữ «silent treatment / im lặng như vũ khí».

## Differentiation
- **B-5c-01.** Mọi người đang nói: Gen Z săn 5C vì ảnh Y2K, hoặc chê «ủa mua máy này về làm gì» ([Thanh Niên](https://thanhnien.vn/gen-z-lung-mua-iphone-5c-luot-tim-kiem-tang-40500-185261111144622021.htm), [TikTok @fixi.mobile.54.tk](https://www.tiktok.com/@fixi.mobile.54.tk/video/7706845085262007558)); báo kèm cảnh báo cho máy MUA VỀ ([TechRadar](https://www.techradar.com/phones/iphone/iphone-5c-searches-are-up-40-500-percent-as-gen-z-boards-the-retro-camera-trend-but-privacy-experts-warn-it-cant-protect-personal-data-in-the-way-more-modern-iphones-do)). Góc của mình: không chê, không rủ mua; nói về cái máy cũ người xem ĐANG có: nó có thể vẫn đăng nhập tài khoản chính. +1 hôm nay: mở danh sách thiết bị, máy không còn cầm thì cho đăng xuất (14.6, phần báo không nói).
- **B-chienlanh-01.** Mọi người đang nói: im lặng là vũ khí làm người bị im đoán mò, xin lỗi; hãy tạm dừng mà đừng biến nó thành hình phạt ([Kenh14](https://kenh14.vn/silent-treatment-khi-su-im-lang-tro-thanh-mot-thu-vu-khi-215261111075058205.chn)); hoặc cảm thông «người im lặng đang đánh trận chiến khó nhất» ([TikTok](https://www.tiktok.com/@k.e.v.i.e.t.l.o.i/video/7706916498115333396)). Góc của mình: nhìn từ phía người đang im: sách dẫn thí nghiệm người đã phạt nghĩ về chuyện đó lâu hơn (Carlsmith 2008) và cố nén giận thì vô ích (Webb 2012). +1: rời đi thì được, nhưng nói trước một câu có giờ quay lại.

## Tách bằng chứng
| Bridge | Bằng chứng trend (nguồn) | Fact sách (mục, mức) | Phần biên tập |
|---|---|---|---|
| B-5c-01 | Thanh Niên/TechRadar (số 40.500%, 1.815% của Compare and Recycle, **chưa tự kiểm**, toàn cầu; iOS 10.3.3/2017 và lời khuyên dùng như máy ảnh là trích lời chuyên gia trong bài); TikTok @hhaibinh_ số liệu provider + 5 comment nguyên văn | 14.6 (C): danh sách thiết bị đăng nhập = máy còn dùng được tài khoản; máy lạ / app lâu không dùng → đổi mật khẩu trước rồi đăng xuất tất cả (thứ tự của UK NCSC); «định kỳ chủ động xem» là kinh nghiệm tác giả | «máy cũ trong ngăn kéo còn đăng nhập» là tình huống minh hoạ; Zalo/Facebook là ví dụ VN (sách nêu WeChat/Alipay/email/Apple/Android) |
| B-chienlanh-01 | Kenh14 11/11 (trích bài); skit TikTok: caption + transcript thật (lời lồng tiếng) + 3 comment nguyên văn (toàn đùa, không có nỗi đau tự kể) | 3.17 (B): rời đi khi giận; Webb 2012 d = 0,45 / 0,36 / −0,04 / −0,12; Carlsmith 2008 (3 thí nghiệm, người phạt nghĩ lâu hơn, đoán sai độ hả dạ); 10.17 (B) phụ | nối thí nghiệm trò chơi sang chiến tranh lạnh = suy luận; câu «mình cần ba mươi phút, lát nói tiếp» = đề xuất biên tập |

## Plan stubs
- `research/trends/2026-11-12/plans/plan-1-may-cu-trong-ngan-keo-con-dang-nhap.json` — validate ✔ (9 scenes, 59,00s). Status stub-needs-approval.
- `research/trends/2026-11-12/plans/plan-2-chien-tranh-lanh-im-de-nghi-khong-de-phat.json` — validate ✔ (8 scenes, 59,00s). Status stub-needs-approval.
Stub chỉ là khung beat (độ dài theo validator, không phải giới hạn L-099); OpenCreator viết script thật sau khi Hiệp chọn và Deep Research kiểm fact. Không làm hình/giọng/render.

## Script hooks (cần duyệt)
1. (B-5c-01, P13) "Gen Z đang lùng mua lại iPhone 5C, máy từ năm 2013, chỉ để chụp ảnh kiểu ngày xưa. Còn cái điện thoại cũ trong ngăn kéo nhà bạn, nó còn đăng nhập tài khoản của bạn không?"
2. (B-5c-01, P01 biến thể) "Bạn lục ngăn kéo, cắm sạc cái máy cũ định chụp ảnh retro như trên mạng. Màn hình sáng lên, Zalo vẫn còn đăng nhập."
3. (B-chienlanh-01, P10) "Chiến tranh lạnh với người yêu, bạn tưởng mình im thì người kia mới là người khổ?"
4. (B-chienlanh-01, P03) "Ai cũng nói im lặng là vũ khí làm người kia đau. Có một thí nghiệm cho thấy người cầm vũ khí mới là người nghĩ về chuyện đó lâu hơn." (cần Deep Research duyệt câu chữ: thí nghiệm là trò chơi, không phải yêu đương)

## Safety notes
- B-5c-01: không vẽ logo Apple; số 40.500% không vào voice (chỉ «tăng vọt») vì chưa tự kiểm và là số toàn cầu; không nêu tên/vẽ creator TikTok; không hướng dẫn mua máy cũ.
- B-chienlanh-01: không chép skit lồng tiếng (có dấu hiệu reupload), không vẽ/nêu creator; không bàn bạo hành, không gắn nhãn tâm lý (narcissist…) như caption của một số clip trong search; không gợi ý trị liệu.
- L-087: ví dụ đều đời thường (điện thoại, tài khoản, cãi nhau người yêu), không môn học.
