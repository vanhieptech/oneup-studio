---
title: "Trend digest 2026-11-08"
source: "pipeline/scripts/trend-collect.py + X MCP extra + Treg TikTok (scrapecreators/tikhub)"
id: trends-2026-11-08
type: trend-digest
status: draft-needs-review
updated: 2026-11-08
tags: [trends, digest, daily]
date: 2026-11-08
collector: pipeline/scripts/trend-collect.py + X MCP + Treg
skill: trend-digest v4 (+ tiktok-research-via-treg, quyết định Hiệp 08/11)
---
# Trend digest 2026-11-08 (Chủ nhật)

**Nguồn:** 33/36 collector ok. Lỗi: kym-memes (HTTP 403), wiki-vi + wiki-en (HTTP 404, ngày thứ 24). **X MCP: có chạy.** Trends VN 20 mục («Chủ Nhật», «Cuối», «Chào», «Thứ 7» là móc giờ; còn lại fandom Thái, crypto MEXC, «Hạ Long»: bỏ). Worldwide 20 mục (anime Nhật, bóng bầu dục Mỹ, động đất Nhật: không dùng). 69 story X News duy nhất từ 4 query (productivity/burnout/habits, AI at work/vibe coding, Gen Z Vietnam, motivation/sleep/self-improvement; max_age 72h). Gộp `x-extra.json` (109 mục), bản gốc trong `x-raw/`.
**Treg TikTok: CÓ chạy (Treg-first, lần đầu).** 10 call, tổng **$0,01616** (4 keyword search ScrapeCreators, 3 video detail + transcript, 3 comments qua route tikhub). 119 kết quả search, shortlist 3 clip có comment (20/clip), music (cả 3 original sound) và transcript thật 2/3 (@hoanglongquoi chỉ có caption). **Không dùng Apify** (Treg đủ). Chi tiết call id, giới hạn: `treg/README.md`.
**Giới hạn TikTok:** đây là kết quả keyword search, không phải bảng xếp hạng trend. `region=VN` chỉ là proxy, `date_posted=this-week` không bảo đảm; ngày đăng thật 01–08/11. Lượt xem là snapshot lifetime lúc ~08:10 giờ VN, không chứng minh đang tăng. Comment là trang đầu 20 cái theo thứ tự provider.
**Số lượng:** collector 491 thô → 468 cụm. raw.json 471 mục (thêm 3 TikTok-native): 356 ok · 23 caution · 92 drop (13 drop tay). **~379 qua lọc.** Chấm tay 16 mục; mục chưa soát giới hạn fit và bridgeability ≤0,4. Drop tay: ADHD/trầm cảm (nhãn y khoa), suy thận, bắt giữ, cần sa, rượu, khách Ấn ở sân bay (dễ chế giễu), DST Mỹ, bầu cử, lính/chiến tranh, cháy ổ điện, «Tiến sĩ Toán bán nhà lấy vàng» (L-087 + vàng).

Dữ liệu: `collect.json`, `collect-run.log`, `x-extra.json`, `x-raw/`, `raw.json`, `score.txt`, `ideas.json`, `plans/`, `treg/`.

## Top 10 (đã lọc)
| # | Trend | rank | nov / sat | Nguồn | Bài học (phần.mục) | Theme |
|---|---|---|---|---|---|---|
| 1 | Revenge bedtime procrastination: thức khuya để đòi lại thời gian riêng sau ngày dài (tóm tắt X; bỏ phần ADHD) | 1.034 | 1.0 / 0.12 | [X News](https://x.com/i/trending/2118954260029444573) | 3.9 / đăng #14 (3.2) | DARK |
| 2 | TikTok «Cảm giác nó mệt mỏi uể oải chịu không nổi» (@phantai911809, 172,1k xem, 226 comment): làm 12 tiếng, định về ngủ liền, rồi lướt, cà phê, game tới 11 giờ đêm (transcript thật) | 0.942 | 1.0 / 0.12 | [TikTok @phantai911809](https://www.tiktok.com/@phantai911809/video/7704918939675118869) | 3.9 / đăng #14 | DARK |
| 3 | TikTok «Đúng 2 tháng nữa là hết năm 2026. Nay Chủ Nhật nằm ở nhà sướng he» (@hoanglongquoi, 258,9k xem, 39,1k share; đăng 01/11) | 0.815 | 1.0 / 0.1 | [TikTok @hoanglongquoi](https://www.tiktok.com/@hoanglongquoi/video/7703019605341555975) | 4.8 (+4.1) / ô #27 | LIGHT |
| 4 | TikTok «Chủ nhật ơi đừng đi mà» (@uyph100008, 228,7k xem, 1.243 comment; comment «tuần nào cũng thế», «team mai thi») | 0.530 | 1.0 / 0.17 | [TikTok @uyph100008](https://www.tiktok.com/@uyph100008/video/7703081372998503700) | 3.14 / đăng #24 | LIGHT |
| 5 | Chọn hai «nâng cấp đời»: sức khoẻ, kỹ năng hay tiền? | 0.476 | 1.0 / 0.05 | [X News](https://x.com/i/trending/2118474978517721193) | 4.14 (bằng chứng phụ B-muathoigian-01) | — |
| 6 | Cuối tuần sập nguồn, nằm tới trưa: «social jet lag» (thuật ngữ trong tóm tắt, chưa tự kiểm) | 0.471 | 1.0 / 0.2 | [X News](https://x.com/i/trending/2119167151189705069) | 3.2 (củng cố B-weekend-02) | DARK |
| 7 | Thức giấc 3h45, không ngủ quá 6h sáng (số Mỹ trong tóm tắt, chưa tự kiểm) | 0.348 | 1.0 / 0.2 | [X News](https://x.com/i/trending/2119084655991509446) | 3.3 (phụ) | — |
| 8 | Forbes: 5 thói quen nhỏ cho cuối tuần vui | 0.295 | 1.0 / 0.15 | [Forbes via Google News](https://news.google.com/rss/articles/CBMiywFBVV95cUxOdmZqYndfaTF6WFN5U1RJWVVmNy11TUdsQjhIN0xMYWJHd3JOWER1cmdkYkgyMVVFenhOa3RZZnVrcXpWNTNPQ0tUOUo3QmFvbDB4UldJUHowTE5ZVGNaa050UWdmV3VMVXJpNThiU2lhRWtxYmMxLTI2cFNYdGRzMmdEVUxKazBCX3Y2VEZ4dDk5X21oTm0wTWFoRjVISjBROG05bWRiNE91cTFFaWhGU0VXWlZndkZnaW1CR1MtbWI2ZzByVmNFWFpHSQ?oc=5) | pattern (listicle, tránh) | — |
| 9 | CafeBiz: thu nhập không cao mà tiết kiệm vẫn tăng nhờ 4 thay đổi cách nghĩ | 0.286 | 1.0 / 0.1 | [CafeBiz](https://cafebiz.vn/toi-khong-kiem-duoc-qua-nhieu-tien-nhung-khoan-tiet-kiem-van-tang-deu-tat-ca-nho-4-thay-doi-trong-cach-nghi-176261107203416961.chn) | 5.x (caution tiền) | — |
| 10 | Tối thứ Sáu cả mạng than mệt, mất ngủ quay lại | 0.231 | 1.0 / 0.2 | [X News](https://x.com/i/trending/2118980100951847234) | 3.3 (phụ) | — |


Đã xem và bỏ khỏi top: vibe coding (bão hoà, đã bridge 06/11), UK pub sau giờ làm (rượu; chỉ giữ caution), Bryan Johnson «kỷ luật thắng động lực» (người nổi tiếng, caution), hoa hậu / showbiz, «2 tỷ chỉ mua được studio» (tiền + so sánh), YT/Google Trends thời tiết.

## TikTok signals (Treg, snapshot 08/11 ~08:10 giờ VN)
| keyword | clip | xem / comment / share | hook / transcript (nguồn) | sound | brand-safe? | bridge |
|---|---|---|---|---|---|---|
| met moi sau gio lam | [@phantai911809](https://www.tiktok.com/@phantai911809/video/7704918939675118869) · đăng 06/11 · 53s | 172.119 / 226 / 662 | transcript thật: «vô làm công ty á ngày 12 tiếng… nghĩ trong đầu á, tối nay về ngủ liền một giấc tới sáng cho khỏe… vậy chứ đời đâu như mơ đâu, về nhà nằm lướt TikTok hết tiếng đồng hồ… về tới nhà 11 giờ đêm» | original sound (Tài Nè Ní) | ok, bỏ chi tiết thuốc lá; comment top là trò đùa nội bộ, không phải pain | B-bedtime-02 → #14 |
| chu nhat o nha | [@hoanglongquoi](https://www.tiktok.com/@hoanglongquoi/video/7703019605341555975) · đăng 01/11 · 16s | 258.934 / 140 / 39.129 | caption (không có transcript): «Đúng 2 tháng nữa là hết năm 2026»; comment «thấy ảnh là bt sắp tết rồi» (196 like) | original sound (Đồng chí Z) | ok | B-hetnam-01 → #27 |
| chu nhat o nha | [@uyph100008](https://www.tiktok.com/@uyph100008/video/7703081372998503700) · đăng 01/11 · 15s | 228.719 / 1.243 / 15.179 | transcript thật (phụ đề tự động): «mai là hết chủ nhật… tới thứ 2 là tất cả chúng ta sẽ quay lại trường thôi»; comment «tuần nào cũng thế» (197 like) | original sound (Huy hạt nhài) | ok; người comment chủ yếu học sinh: chỉ dùng «ôn thi» chung | B-chunhatoi-01 → #24 |
| tri hoan | [@vutru_codai](https://www.tiktok.com/@vutru_codai/video/7704969869502074132) | 327.602 / 158 / 4.294 | caption «Đừng để 10% sự cố… hỏng 90%» (gắn #dinhluatfestinger, chưa kiểm) | chưa lấy | caution (quy luật chưa kiểm) | — |
| thoi quen moi ngay | [@nguyenhoanganh29012003](https://www.tiktok.com/@nguyenhoanganh29012003/video/7704934218450619655) | 99.817 / 3 / 709 | caption «Mỗi ngày bớt đi một thói quen xấu» | chưa lấy | ok | pattern (+1 âm thầm) |

Âm thanh: cả 3 clip shortlist dùng original sound của creator. Metadata này không cho phép dùng lại audio; series là comic, không mượn audio nguồn.

## Learning
- Không thêm P-row. Clip @phantai911809 là F03 (kỳ vọng vs thực tế) kể bằng lời: «nghĩ trong đầu… vậy chứ đời đâu như mơ». P10 + P12 +1. Đếm ngược hết năm khớp P05 (+1). P15 +1.
- **Cross-source mạnh nhất hôm nay:** thức khuya «đòi lại thời gian» có cả X News (07/11) lẫn TikTok VN có transcript (06/11). Đây là tín hiệu tốt hơn một nguồn đơn lẻ, nhưng vẫn không chứng minh đang tăng.
- Treg so với Apify: rẻ (~$0,016 cho 10 call), có transcript thật và comment ngay, nhưng `trim=true` làm mất music trong search và search không sort theo like. Lần sau: không trim cho 1 query, hoặc lấy music qua video.detail như hôm nay.
- Mốc thời gian: còn 53 ngày tới 31/12 (8/11 → 31/12). «2 tháng nữa hết năm» lên ở TikTok 01/11, vẫn dùng được tới khoảng giữa tháng.
- Bão hoà nên tránh: vibe coding, AI-at-work generic, «trì hoãn không phải lười» góc thẳng, listicle cuối tuần, nonchalance/im lặng chọn bình yên (ngày 3+).

## Bridges
| id | Trend | Khoảnh khắc | Bài học | Hook VI (pattern) | Góc | Đích | Theme |
|---|---|---|---|---|---|---|---|
| B-bedtime-02 | revenge bedtime (X) + TikTok @phantai911809 | tan làm định ngủ liền, rốt cuộc lướt, ăn, tắm, bạn rủ đi, 11 giờ đêm mới về | 3.9 (+3.2) | "Tan làm, trong đầu chỉ có một câu: về ngủ liền một giấc cho khỏe. Rồi mười một giờ đêm bạn vẫn đang cầm điện thoại." (P10+P12+F03) | empathy / humor | đăng #14 (3.2) hook thay thế, củng cố B-bedtime-01 | DARK |
| B-hetnam-01 | TikTok «2 tháng nữa hết năm» | việc đã dời từ đầu năm: dọn tủ, gọi lại cho ai đó, sửa xe | 4.8 (+4.1) | "Còn năm mươi ba ngày nữa là hết năm hai không hai sáu. Bạn chưa cần kế hoạch năm mới, chỉ cần một việc xong trước ba mốt tháng mười hai." (P05+P15) | empathy / seasonal | ô #27 LIGHT, cạnh B-thang11-01 / B-chonviec-01 | LIGHT |
| B-chunhatoi-01 | TikTok «Chủ nhật ơi đừng đi mà» | tối Chủ nhật nằm nghĩ mãi về sáng thứ Hai | 3.14 | "Tối Chủ nhật nào cũng hát «mai là hết Chủ nhật»? Thử viết ra đúng một việc đầu tiên của sáng thứ Hai, rồi gấp sổ lại." (P12+P10) | empathy | đăng #24 (3.14, LIGHT) hook thay thế | LIGHT |
| B-weekend-03 | X social jet lag cuối tuần | thứ Bảy nằm tới trưa, tối Chủ nhật không buồn ngủ | 3.2 | "Cuối tuần nằm tới trưa cho bù, vậy mà tối Chủ nhật lại không ngủ được?" (P12+P03) | data | củng cố B-weekend-02 (#14) | DARK |

Cầu nối về trục kênh: trend chỉ là móc. B-bedtime-02: thời gian riêng có giờ kết thúc (+1 một báo thức «bắt đầu tắt»). B-hetnam-01: một việc có ngày hạn trước 31/12. B-chunhatoi-01: viết một việc đầu tiên của thứ Hai, rồi thôi nghĩ.

## Differentiation
- **B-bedtime-02**: Mọi người đang nói: thức khuya để đòi lại thời gian riêng sau ngày dài ([X News](https://x.com/i/trending/2118954260029444573)); TikTok kể y chang kịch bản đó ([@phantai911809](https://www.tiktok.com/@phantai911809/video/7704918939675118869)). Góc của mình: không bảo bỏ thời gian riêng, cho nó giờ kết thúc. Khác B-bedtime-01 (ghi giờ đặt điện thoại 7 ngày).
- **B-hetnam-01**: Mọi người đang nói: hết năm rồi, nôn Tết ([@hoanglongquoi](https://www.tiktok.com/@hoanglongquoi/video/7703019605341555975)). Góc của mình: không đợi resolution năm mới; 53 ngày cho đúng một việc, viết dạng nếu… thì… (callback clip-01).
- **B-chunhatoi-01**: Mọi người đang nói: tiếc Chủ nhật, sợ thứ Hai ([@uyph100008](https://www.tiktok.com/@uyph100008/video/7703081372998503700)). Góc của mình: 3.14, động tay một việc nhỏ để thoát vòng nghĩ.

## Plan stubs
- `plans/plan-1-dinh-ngu-som-thanh-11-gio-dem.json`: ✔ validate 9 cảnh, 68,00s (stub-needs-approval). Trend nói thành lời ở b03 và thẻ chữ b01 (L-084: «thức khuya đòi lại thời gian · TikTok + X 07/11»). Ví dụ đời thường: điện thoại, cơm, tắm, tin nhắn. Tuần 3, không Omi. Theme dark.
- `plans/plan-2-con-53-ngay-mot-viec-xong.json`: ✔ validate 8 cảnh, 62,00s (stub-needs-approval). Trend ở b02 + thẻ chữ b01 («2 tháng nữa hết năm · TikTok 01/11»). Ví dụ: tủ đồ, cuộc gọi, xe. Tuần 5, không Omi. Theme light.
- `check-rules.py --subjects` (ideas + 2 stub): PASS (L-087).
- Lưu ý môi trường: `video-engine/node_modules` bị thiếu trên box sáng nay; đã chạy `npm ci` (không đổi file tracked) rồi mới validate.
- Kịch bản thật do OpenCreator viết sau khi Deep Research kiểm 3.9 / 4.8, Rule Reviewer duyệt. Stub không cho phép tạo hình, giọng, render hay đăng trước Chốt.

## Script hooks (cần Hiệp duyệt)
1. "Tan làm, trong đầu chỉ có một câu: về ngủ liền một giấc cho khỏe. Rồi mười một giờ đêm bạn vẫn đang cầm điện thoại." (B-bedtime-02, 3.9, đăng #14, DARK). Vì sao dừng: đúng khoảng cách giữa dự định và thực tế mỗi tối.
2. "Còn năm mươi ba ngày nữa là hết năm hai không hai sáu. Bạn chưa cần kế hoạch năm mới, chỉ cần một việc xong trước ba mốt tháng mười hai." (B-hetnam-01, 4.8, ô #27, LIGHT). Số 53 đúng cho ngày 08/11; đổi theo ngày đăng.
3. "Tối Chủ nhật nào cũng hát «mai là hết Chủ nhật»? Thử viết ra đúng một việc đầu tiên của sáng thứ Hai, rồi gấp sổ lại." (B-chunhatoi-01, 3.14, đăng #24, LIGHT).

## Safety notes
- B-bedtime-02: bỏ thuốc lá, ADHD, «dopamine»; không chẩn đoán. Không quay lại hình hay audio clip nguồn; chỉ kể lại khung chuyện.
- B-hetnam-01: không hứa «đổi đời»; Tết 2027 không nêu ngày cụ thể (chưa kiểm).
- B-chunhatoi-01: comment nguồn nói thi cử: chỉ dùng «ôn thi» chung, không nêu môn (L-087).
- Chính trị, tội phạm, bệnh, bi kịch, tâm linh, vàng, xổ số, rượu bia, đời tư người nổi tiếng: bỏ.

## Trạng thái đang chờ
- clip-05 làm lại sau L-098 (Rule Reviewer/OpenCreator). Các bridge 01–07/11 vẫn `đề xuất` hoặc `stub, chờ duyệt`.
- Đăng #14 (3.2): B-weekend-02, B-bedtime-01, **+ B-bedtime-02, B-weekend-03**. Ô #27: B-thang11-01, B-muathoigian-01, B-chonviec-01, **+ B-hetnam-01**. Đăng #24 (3.14): **+ B-chunhatoi-01**.
