---
title: "Trend digest 2026-11-02"
source: "pipeline/scripts/trend-collect.py + X MCP extra (Apify unavailable)"
id: trends-2026-11-02
type: trend-digest
status: draft-needs-review
updated: 2026-11-02
tags: [trends, digest, daily]
date: 2026-11-02
collector: pipeline/scripts/trend-collect.py + X MCP
skill: trend-digest v4
---
# Trend digest 2026-11-02 (thứ Hai)

**Nguồn:** 33/36 collector ok. Lỗi: kym-memes (HTTP 403), wiki-vi + wiki-en (HTTP 404, ngày thứ 18). vnexpress-giaitri lỗi SSL EOF ở lần chạy đầu, chạy lại một lần thì ok. **X MCP: có chạy**: trends VN 20 («Tuần», «Thứ Hai», «Thứ 2» top 3; còn lại là fandom Thái, Halloween, Binance) + worldwide 20 (NFL, F1 Mexico, không dùng được) + 40 story X News (4 query: productivity habits, AI at work, Gen Z Vietnam, self improvement motivation; max_age 72h) → `x-extra.json` 80 mục, bản gốc trong `x-raw/`.
**Apify TikTok-native: không chạy, vẫn hết hạn mức.** Kiểm rẻ 1 lần (`clockworks/tiktok-scraper`, hashtag `thoiquen`, resultsPerPage 5, commentsPerPost 0) bị từ chối: “Your remaining usage of $0.132525 this billing cycle isn't enough for this run”. Không có run id, 0 clip. Xem `apify/README.md`.
**Số lượng:** collector 465 thô → 446 cụm; raw.json 446 mục (248 ok · 11 caution · 187 drop, trong đó 129 drop tay) → 259 qua lọc. Chấm tay 27 mục; mục chưa soát giới hạn fit ≤0,4. Mở lại 2 story X bị bộ lọc từ khoá chặn nhầm (video 9-5 yên ổn, AI agent bận rộn diễn). Drop tay: chính trị/chính sách (biểu tình châu Âu, bầu cử Mỹ, căn cước/VNeID, quy định mới, sự cố trên sóng chung kết Olympia), tội phạm/bi kịch (vụ bắt giữ, giấy tờ giả, tai nạn, Binance bị hack), bệnh và claim y khoa (ung thư, cholesterol, đường huyết, kháng sinh), tiền ảo/vàng/chứng khoán, đời tư/ngoại hình người nổi tiếng, tử vi.
Dữ liệu: `collect.json`, `collect.log`, `x-extra.json`, `x-raw/`, `raw.json`, `score.txt`, `ideas.json`, `plans/`, `apify/README.md`.

## Top 10 (đã lọc)
| # | Trend | rank | nov / sat | Nguồn | Bài học (phần.mục) | Theme |
|---|---|---|---|---|---|---|
| 1 | Thợ sửa iPhone + coach năng suất: tắt thông báo không cần, vị trí chỉ «khi dùng», Focus Mode theo lịch, cho đỡ hao pin và đỡ bị làm phiền (số giờ pin chỉ từ tóm tắt, chưa tự kiểm) | 0.812 | 1.0 / 0.0 | [X News 01/11](https://x.com/i/trending/2116895165457875038) | 3.1 (clip-08) | DARK |
| 2 | «30s: kiếm nhiều tiền hơn mà vẫn ngại nâng cấp chất lượng sống» (ngại thuê người dọn, ghế ọp ẹp, nhà xa chỗ làm) | 0.729 | 1.0 / 0.0 | [Kenh14 01/11](https://kenh14.vn/30s-khi-kiem-duoc-nhieu-tien-hon-nhung-van-ngai-nang-cap-chat-luong-song-215261101202435341.chn) | 4.14 (ô #27) | LIGHT |
| 3 | Video một ngày 9-5 yên ổn (đi làm gần, 4h chiều xong) chia hai phe: ghen tị vs chê nhàm | 0.464 | 1.0 / 0.0 | [X News 01/11](https://x.com/i/trending/2116695189918019785) | 4.18 (củng cố B-commute-02) | DARK |
| 4 | «Housewife» (Tate McRae) thành sound TikTok khoe mình đã đi xa cỡ nào, tự làm ra tiền (>309k video theo InMusic/ET, chưa tự kiểm); nhánh trad wife gây tranh cãi | 0.444 | 1.0 / 0.1 | [Economic Times 02/11](https://economictimes.indiatimes.com/world/us/a-tate-mcrae-song-is-fuelling-a-tiktok-money-trend-and-creators-are-showing-how-far-theyve-come/articleshow/135436080.cms), [Rolling Stone](https://www.rollingstone.com/music/music-features/tate-mcrae-housewife-tradwives-tiktok-trend-1235648068/) | 3.20 (clip-22, caution) | DARK |
| 5 | Hà Nội: cất ô tô đi xe máy vì phí gửi tăng (số 8 triệu/tháng từ bài, chưa tự kiểm) | 0.367 | 1.0 / 0.0 | [VnExpress 02/11](https://vnexpress.net/cat-xe-ban-oto-vi-phi-trong-giu-tang-cao-5138950.html) | 5.x chi phí cố định (chưa bridge, caution chính sách địa phương) | — |
| 6 | «Muốn cả nhà bớt điện thoại thì bắt đầu từ mình» | 0.276 | 1.0 / 0.0 | [Movieguide qua Google News](https://news.google.com/rss/articles/CBMipgFBVV95cUxNRHlOYWRCb01OSEdRTUVJSGg0MmRvVmRvQUljaER3MXNtT1hQVndxOXhmajQ3OUdDUkpnUTcxTExsTnNWVm9jeTNpLXprcGRvRkJmcVYtbkRoaUVWMnVsT0dxZHVGQjlqWWlZeEY4dEpXbWoyREZoOU40ZFhsVmRrWkw1T0RVOW9Mc2FrS2JLdDllZFhSVkNKQWhOM2RTTjRNS0pPeTV3?oc=5) | 4.15 / P15 (bằng chứng) | — |
| 7 | «Tự tin ảo tưởng là cheat code của cuộc đời» | 0.243 | 1.0 / 0.0 | [X News 01/11](https://x.com/i/trending/2116940492940488972) | chưa có mục sách khớp gọn | — |
| 8 | Áp lực tiền khiến nhiều người không học được kỹ năng đời thường (đạp xe, ngoại ngữ) | 0.225 | 1.0 / 0.0 | [X News 01/11](https://x.com/i/trending/2116940492969824497) | caution, chưa bridge | — |
| 9 | «Chọn bình yên» + «so sánh lấy mất bình yên» ngày 3 | 0.211 | 0.5 / 0.45 | [X News 01/11](https://x.com/i/trending/2116684926288322666), [X News 31/10](https://x.com/i/trending/2116541178405679336) | 3.20 (B-yenlang-01) | DARK |
| 10 | Lãi suất tăng, có nên rút sổ tiết kiệm cũ gửi lại? | 0.203 | 1.0 / 0.0 | [CafeBiz 01/11](https://cafebiz.vn/lai-suat-tang-co-nen-rut-so-tiet-kiem-cu-de-gui-lai-176261101200950644.chn) | 5.x (caution tư vấn tài chính) | — |

Đã xem và bỏ khỏi top dù điểm cao: kỹ sư IT bỏ văn phòng xuống nhà máy (cross 3 VnExpress, nhưng AI ở chỗ làm bão hoà + bối cảnh Trung Quốc); «Entropy: vì sao căn phòng tự bừa ra» (Tinh tế; hợp việc nhà nhưng là kiến thức môn học, L-087); 72% sinh viên trì hoãn (số chỉ ở tiêu đề, trì hoãn bão hoà); bông hoa chưa nở + dàn sao (ngày 7, sat 0.95); brain stacking (ngày 8); X VN «Thứ Hai»/«Tuần» (chỉ móc giờ); Daylight saving (Mỹ, VN không đổi giờ).

## TikTok signals
Hôm nay không có dữ liệu Apify. Dưới đây là proxy từ báo, không có view/comment/transcript tự đo nên không xếp hạng:
| keyword | nguồn | tín hiệu | brand-safe? | bridge |
|---|---|---|---|---|
| Housewife (Tate McRae), «how far I've come» | [Economic Times 02/11](https://economictimes.indiatimes.com/world/us/a-tate-mcrae-song-is-fuelling-a-tiktok-money-trend-and-creators-are-showing-how-far-theyve-come/articleshow/135436080.cms), [InMusic](https://inmusicblog.com/news/tate-mcrae-housewife-tiktok-viral-trend/), [Rolling Stone](https://www.rollingstone.com/music/music-features/tate-mcrae-housewife-tradwives-tiktok-trend-1235648068/) | >309k video dùng sound (lời báo, chưa tự kiểm); hai nhánh: tự làm ra tiền vs trad wife | caution: chỉ mượn format «đã đi xa cỡ nào», không nhạc, không lời bài hát, không người nổi tiếng, không bàn vai trò giới | B-dixa-01 → 3.20 (clip-22) |
| bông hoa chưa nở (biến hình) | Google News «trend TikTok» (Tin tức 24h 01/11, Thanh Niên 30/10) | «tràn ngập TikTok», dàn sao Việt bắt trend (lời báo) | ok nếu tự trào bằng thói quen; bỏ ngoại hình và người nổi tiếng | clip-06 (script v1 đã dùng, chờ Hiệp chốt); bão hoà |
| wine trend, under-eye trick, Keon & Kavon | Google News US | không khớp kênh | bỏ | — |

## Learning
- Không thêm P-row. Mẹo chỉnh iPhone khớp P03 (mọi người nói «cho đỡ hao pin», sách nói chuyện khác) + P15. Kenh14 30s khớp P10 + P03. Video 9-5 khớp P11. X VN thứ Hai khớp P12. «Housewife» khoe tiến bộ là F04 (trước/sau). P03/P10/P11/P12/P15 +1, F04 +1.
- Mục 4.14 (thuê việc nhà theo giờ lương) lần đầu có trend VN bắc vào. Đây là một mục LIGHT hiếm cho ô #27, cạnh B-thang11-01 (mốc đầu tháng, phải chờ 1/12).
- Hôm nay X VN chỉ có móc giờ (thứ Hai) và fandom. Tín hiệu đáng dùng đều đến từ X News và báo đời sống.
- Bão hoà nên tránh: bông hoa chưa nở (ngày 7), brain stacking (ngày 8), chọn bình yên/so sánh (ngày 3), Musk tiết kiệm (ngày 3, sat 0.75), clean as you go (ngày 3, sat 0.7), AI ở chỗ làm.

## Bridges
| id | Trend | Khoảnh khắc | Bài học | Hook VI (pattern) | Góc | Đích | Theme |
|---|---|---|---|---|---|---|---|
| B-thongbao-01 | thợ sửa iPhone: tắt thông báo cho đỡ hao pin | đang gõ dở email gửi sếp, điện thoại rung một cái vì tin khuyến mãi, không mở mà vẫn quên câu đang viết | 3.1 (Stothart 2015, mức B) | "Một thợ sửa iPhone đang khuyên mọi người tắt bớt thông báo cho đỡ hao pin. Vậy mỗi lần điện thoại rung lúc bạn đang làm việc, bạn mất gì ngoài pin?" (P03+P15) | contrarian / data | clip-08 (3.1) hook thay thế mới | DARK |
| B-muathoigian-01 | Kenh14 30s ngại nâng cấp chất lượng sống | cả sáng Chủ nhật quét lau phơi đồ vì tiếc tiền thuê người, chiều mệt nên hủy hẹn | 4.14 (Whillans 2017, mức B) | "Ba mươi tuổi, lương đã tăng mấy lần mà vẫn ngại nâng cấp cuộc sống. Nếu chỉ được nâng cấp một thứ, bạn chọn mua thêm đồ hay mua lại thời gian?" (P10+P03) | empathy / data | ô đăng #27 (LIGHT trống) hoặc ý tưởng mới 4.14 | LIGHT |
| B-dixa-01 | «Housewife» khoe mình đã đi xa cỡ nào | cả feed khoe tiến bộ, mình lại đem bản thân so với bạn bè | 3.20 (mức A) | "Cả TikTok đang khoe mình đã đi xa cỡ nào. Còn bạn đang so mình với ai: bạn bè, hay chính bạn ba tháng trước?" (P08+P03) | contrarian / empathy | clip-22 hook thay thế (caution) | DARK |
| B-commute-03 | video 9-5 yên ổn chia hai phe | nửa feed ghen tị người đi làm năm phút là tới, nửa kia chê nhàm | 4.18 (sách ghi tranh cãi) | "Cả mạng đang cãi nhau về một ngày 9-5 bình thường: đi làm gần, bốn giờ chiều là xong. Mà cái làm nhiều người ghen tị nhất có khi là quãng đường đi làm ngắn." (P11+P03) | contrarian | củng cố B-commute-02 | DARK |

Cầu nối về trục kênh (luật 26/10): trend chỉ là cái móc ở hook. Thông điệp mỗi bridge là một việc nhỏ làm được hôm nay: tắt thông báo của đúng một app · bấm máy tính ra con số giờ lương của mình · viết một dòng «ba tháng trước mình… / hôm nay mình…» · cộng thử số phút đi làm một tuần.

## Differentiation
- **B-thongbao-01**: Mọi người đang nói: tắt thông báo, giới hạn vị trí, bật Focus Mode là mẹo chỉnh máy cho đỡ hao pin, đỡ phiền ([X News 01/11](https://x.com/i/trending/2116895165457875038)). Góc của mình: pin chỉ là cái lợi phụ. Sách 3.1 (Stothart 2015, mức B): chỉ cần nhận một thông báo, không xem không chạm, điểm bài tập trung đã tụt gần bằng lúc nghe máy hay nhắn tin. Tự nhận trước (P15): máy mình cũng để nguyên thông báo app mua sắm. Đây là thí nghiệm trong phòng lab, làm một lần; cộng dồn mỗi ngày thì chưa ai đo, voice nói rõ «trong phòng thí nghiệm». Không dùng số giờ pin của tóm tắt X.
- **B-muathoigian-01**: Mọi người đang nói: lương tăng thì nên tiêu cho bản thân, nhưng đừng chạy theo hình ảnh ([Kenh14 01/11](https://kenh14.vn/30s-khi-kiem-duoc-nhieu-tien-hon-nhung-van-ngai-nang-cap-chat-luong-song-215261101202435341.chn)). Góc của mình: không phải «mình đáng được tiêu». Có một phép đo: giờ lương (thu nhập sau thuế một tháng chia số giờ làm thật) so với giá thuê một việc mình ghét làm. Sách 4.14 (Whillans 2017, mức B): 6.271 người ở bốn nước, ai chi tiền mua thời gian thì hài lòng với cuộc sống hơn; thử thật ngoài đời thì cùng một khoản tiền, mua thời gian vui hơn mua đồ. Whillans đo độ vui, không đo số giờ tiết kiệm. Không dùng số khảo sát Trung Quốc.
- **B-dixa-01**: Mọi người đang nói: khoe mình đã đi xa cỡ nào, tự làm ra tiền ([Economic Times](https://economictimes.indiatimes.com/world/us/a-tate-mcrae-song-is-fuelling-a-tiktok-money-trend-and-creators-are-showing-how-far-theyve-come/articleshow/135436080.cms)). Góc của mình: xem video người khác khoe tiến bộ dễ biến thành so mình với họ. Mốc so đúng là chính mình ba tháng trước, và chỉnh từ chỗ feed hiện ra (sách 3.20, mức A, phần phân tích gộp chỉ là tương quan).
- **B-commute-03**: Mọi người đang nói: ghen tị hoặc chê một ngày 9-5 yên ổn ([X News](https://x.com/i/trending/2116695189918019785)). Góc của mình: ra khỏi hai phe. Cái người ta ghen tị trong video là quãng đường đi làm ngắn (4.18, sách ghi còn tranh cãi). Không dùng câu trích về chiến tranh trong thread, không dùng số 69% của tóm tắt.

## Plan stubs
- `plans/plan-1-thong-bao-hao-pin-hao-tap-trung.json`: ✔ validate 9 cảnh, 60,00s (stub-needs-approval). Trend ở b01 (L-084: thẻ chữ «Tắt thông báo cho đỡ hao pin · X News 01/11» cạnh biểu tượng pin, câu trend nói ở b01). Ví dụ đời thường: email gửi sếp, tin khuyến mãi, nhóm chat, cài đặt điện thoại. Dẫn chứng có tên + năm + so sánh (L-096). Sách 3.1 mức B.
- `plans/plan-2-luong-tang-mua-lai-thoi-gian.json`: ✔ validate 9 cảnh, 61,00s (stub-needs-approval). Trend ở b01 (thẻ chữ «30s: kiếm nhiều hơn mà vẫn ngại nâng cấp · Kenh14 01/11»). Ví dụ: việc nhà Chủ nhật, hẹn cà phê, máy tính bấm giờ lương. Sách 4.14 mức B. Không nêu số tiền cụ thể.
- `check-rules.py --subjects ideas.json`: PASS (L-087).
- Kịch bản thật do OpenCreator Studio viết sau khi Deep Research kiểm fact và Rule Reviewer duyệt.

## Script hooks (cần Hiệp duyệt)
1. "Một thợ sửa iPhone đang khuyên mọi người tắt bớt thông báo cho đỡ hao pin. Vậy mỗi lần điện thoại rung lúc bạn đang làm việc, bạn mất gì ngoài pin?" (B-thongbao-01, 3.1, clip-08, DARK)
2. "Ba mươi tuổi, lương đã tăng mấy lần mà vẫn ngại nâng cấp cuộc sống. Nếu chỉ được nâng cấp một thứ, bạn chọn mua thêm đồ hay mua lại thời gian?" (B-muathoigian-01, 4.14, ô #27, LIGHT)
3. "Cả TikTok đang khoe mình đã đi xa cỡ nào. Còn bạn đang so mình với ai: bạn bè, hay chính bạn ba tháng trước?" (B-dixa-01, 3.20, clip-22, DARK, caution)

## Trạng thái đang chờ
- clip-06: script v1 «bông hoa chưa nở» đã ĐẠT review cuối 31/10 (9a962b9), vẫn chờ Hiệp chốt. Trend bông hoa đã ngày 7 (sat 0.95): nếu chốt thì nên làm ngay.
- clip-05 v10 r10.2 đã ĐẠT review, chờ Hiệp chốt (theo digest 01/11; hôm nay không thấy commit mới).
- 5.27 Musk (B-tietkiem-01) và 4.9 Dọn liền tay (B-donlientay-01): script r3 ĐẠT review 31/10 (53a01a5). Musk còn mâu thuẫn L-096/mức C chờ Hiệp quyết.
- clip-22: B-ghenti-01 chờ fact 3.20. Hook thay thế đang có: B-30tuoi-01, B-yenlang-01, B-dixa-01 (mới, caution).
- Ô #27 (LIGHT trống): có hai ứng viên, B-thang11-01 (4.8, để dành cho 1/12) và B-muathoigian-01 (4.14, mới). Hiệp chọn.
- Apify: hết hạn mức từ 22/10 (còn $0,1325). Theo quyết định của Hiệp 22/10, chờ chu kỳ mới, không nâng gói.

## Safety notes
- B-thongbao-01: không dùng số giờ pin trong tóm tắt X; không nêu tên hãng như quảng cáo (chỉ nói «thợ sửa điện thoại / iPhone» như nguồn trend); voice không nói «sinh viên».
- B-muathoigian-01: chuyện tiền, không so lương, không khoe; nói rõ chưa dư tiền thì giữ quỹ dự phòng trước (nối 5.27); không số tiền cụ thể; không số khảo sát Trung Quốc.
- B-dixa-01: người nổi tiếng + tranh cãi vai trò giới → chỉ format, không nhạc, không lời bài hát, không tên ca sĩ trong voice nếu Hiệp không duyệt.
- B-commute-03: bỏ câu trích chiến tranh trong thread; 4.18 ghi tranh cãi.
- Entropy (Tinh tế): không dùng, L-087.
- Chính trị, tội phạm, bệnh, bi kịch, tiền ảo/vàng/chứng khoán, đời tư người nổi tiếng: bỏ.
