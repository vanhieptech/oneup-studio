---
title: "Trend digest: 2026-10-13 (skill v2, chạy tự động 08:05–08:30 giờ VN)"
date: 2026-10-13
source: "oneup-studio (soạn trong repo)"
id: trends-2026-10-13
type: trend-digest
status: done
updated: 2026-10-13
tags: [trends, broad, bridges, vi, en, v2]
---
# Trend digest: 2026-10-13 (skill v2, chạy tự động 08:05–08:30 giờ VN)
**Nguồn:** Google Trends RSS VN + US: ok · YouTube qua yt-dlp `ytsearch` (24 truy vấn): ok, riêng `ytsearchdate` trả 0 kết quả nên chưa có số video 7 ngày · Web search: ok · News RSS: một phần (VnExpress giải trí/số hoá, Tuổi Trẻ, Ars, Verge ok; VnExpress tin mới và Kenh14 RSS rỗng) · X: không chạy được (công cụ X đi qua MCP, lần này MCP lỗi) · TikTok Creative Center: bị chặn (trang JS). Dữ liệu thô + điểm: `raw.json` (41 mục, 14 mục bị loại).

## Top trend (đã lọc brand-safety, xếp theo rank_score)
| # | Trend | rank | novelty | saturation | Ghi chú | Link |
|---|---|---|---|---|---|---|
| 1 | Nghiên cứu Harvard: AI coding agent +30% code, việc xong không tăng | 0.605 | 1.0 | 0.07 | hợp góc SE, gần như chưa ai làm góc bài học | [Ars](https://arstechnica.com/ai/2026/10/ai-coding-agents-generate-more-code-but-not-more-software/) |
| 2 | Chụp ảnh trần nhà nhận "thông điệp vũ trụ" | 0.592 | 1.0 | 0.10 | trend VN mới, Kenh14 13/10 | [Kenh14](https://kenh14.vn/mot-chiec-trend-dang-viral-chup-anh-tran-nha-de-nhan-thong-diep-tu-vu-tru-ban-bi-cuoc-doi-di-toi-muc-nay-roi-sao-215261013063429553.chn) |
| 3 | Dragon Ball Super: Beerus ra mắt gây sốt (trailer 4,5M view) | 0.340 | 1.0 | 0.05 | chỉ nhắc tên, không dùng hình | [Tuổi Trẻ](https://tuoitre.vn/dragon-ball-super-beerus-vua-ra-mat-da-gay-sot-100261013001914802.htm) |
| 4 | Format "This is your sign to…" (#2 tuần 5–11/10, top 8,8M) | 0.310 | 1.0 | 0.30 | dùng bản đảo ngược | [Postdom](https://postdom.com/blog/tiktok-trends) |
| 5 | "Làm content cả năm không ai hay, chọn vali số 7 cả nước biết" | 0.260 | 1.0 | 0.15 | meme tự giễu của creator | [35express](https://35express.org/trend-lam-content-ca-nam-khong-ai-hay-chon-vali-so-7-ca-nuoc-biet/) |

Tiếp theo: C1 Atletico–MU khuya nay (0.231, lặp lại, B-c1-01 đã có), Anthropic cấm "bắt nạt" Claude (0.210), No Man's Sky lên iOS (0.157), Halloween (0.146, toàn cầu nhưng ít hợp VN), "Đang bực mà còn kiếm tui" (0.143, lặp lại).

## Learning
- **Pattern mới:** P06 Actually-method (4 lần thấy), P07 This is your sign đảo ngược (3), P08 Thử N ngày (2), P09 Cố cả năm vs pha vô tri (2). Format mới: F02 POV (#1 tuần, 36,1M), F03 Kỳ vọng vs thực tế, F04 Biến hình trước/sau (Halloween).
- **Pattern tăng:** P01 (2), P03 (2), P04 (1), P05 (2).
- **Đã bão hoà, chỉ làm khi có fact sách ngược chiều:** Great Lock In (sat 0.60, đã gắn clip), Winter Arc (0.55), study-with-me (0.70), "dự án ma" (0.42, đã dùng cho clip-01; VTV3 cũng đã làm riêng một số).
- Gợi ý cho script: "dự án ma" vẫn là câu hot nhất tháng 10 nên giữ trong clip-01, nhưng đừng mở thêm clip mới quanh nó.

## Bridges
| id | Trend | Khoảnh khắc | Bài học (đã đối chiếu sách) | Hook VI (pattern) | Góc | Theme | Đích |
|---|---|---|---|---|---|---|---|
| B-aiagents-01 | AI agent +30% code | to-do dài thêm, việc xong không thêm | 4.7 chia tới mức mỗi phần xong trong một lần ngồi rồi mới ước giờ (Kruger & Evans 2004; sách chỉ kiểm được hướng, không có %) | "AI giúp dân code viết nhiều hơn 30%. Số việc xong thêm? Gần như hông có." (P04+P03) | data / humor | DARK | clip-03, hook thay thế |
| B-trannha-01 | chụp trần nhà nhận thông điệp | chờ "dấu hiệu" mới bắt đầu | 4.8 tự đặt ngày: hạn ngoài 80,6% xong vs tự dự tính 38,7% (Buehler 1994; hạn tự đặt chưa ai đo trực tiếp) | "Chụp trần nhà chờ vũ trụ gửi thông điệp hả? Thông điệp nè: vũ trụ hông gửi deadline đâu." (P07) | contrarian / humor | LIGHT | clip-04, hook thay thế |
| B-beerus-01 | Dragon Ball Super: Beerus | "ngủ 6 tiếng quen rồi" | 3.3 ngủ 6 tiếng × 14 đêm ≈ thức trắng 2 đêm, mà tự thấy không buồn ngủ thêm (Van Dongen 2003, RCT) | "Beerus ngủ một giấc mấy chục năm. Bạn ngủ 6 tiếng rồi nói đủ rồi." (P01) | humor / data | DARK | clip-15 hoặc ý tưởng mới |
| B-valiso7-01 | vali số 7 | làm kênh/side project lâu chưa ai biết | 4.12 thói quen 18–254 ngày, bỏ một ngày không reset | "Làm content cả năm hông ai hay… mình mới làm một tuần, chưa tới lượt hông ai hay." (P09) | story / humor | LIGHT | ý tưởng mới, cần S-04 |
| B-claude-01 | Anthropic cấm "bắt nạt" Claude | chửi chatbot, la khi deploy lỗi | 3.17 giận thì rời đi; đứng ở góc người kia d = 0,45, kìm nén d = −0,04; trả đũa làm nghĩ về chuyện lâu hơn | "Bạn có hay chửi AI hông? Omi hông buồn đâu, mà bạn thì bực lâu hơn đó." (P02) | humor / contrarian | DARK | ý tưởng mới, tuần ≥5 |
| B-nms-01 | No Man's Sky lên iOS | Winter Arc ngày 21 muốn bỏ | 4.12 | "Winter Arc 90 ngày? No Man's Sky mất 10 năm cho redemption arc." (P03) | contrarian | DARK | clip-06, hook phụ |

## Differentiation (top 2)
- **B-aiagents-01.** Mọi người đang nói: AI làm dev nhanh gấp mấy lần, hoặc AI chỉ là hype và dev sắp mất việc ([Forkast](https://forkast.news/ai-coding-agents-write-30-more-code-and-resolve-zero-additional-issues-harvard-study-finds/), [Data Phoenix](https://dataphoenix.info/news/harvard-coding-agent-gains-code-review)). Góc của mình: chính nghiên cứu cho thấy chỗ kẹt là khâu "xong" (review +49%), không phải khâu "viết". To-do của bạn cũng vậy, và sách chỉ cách chia việc tới mức một lần ngồi. Chuyện OneUp của Hiệp chỉ đưa vào khi Hiệp xác nhận `[CẦN HIỆP XÁC NHẬN]`.
- **B-trannha-01.** Mọi người đang nói: chụp trần nhà xem TikTok ghép bài gì, nghe trúng tâm trạng ghê; hoặc "this is your sign to go all in" ([Kenh14](https://kenh14.vn/mot-chiec-trend-dang-viral-chup-anh-tran-nha-de-nhan-thong-diep-tu-vu-tru-ban-bi-cuoc-doi-di-toi-muc-nay-roi-sao-215261013063429553.chn), [35express](https://35express.org/trend-trend-chup-tam-anh-tren-tran-nha-tiktok-se-ghep-nhac-thong-diep/)). Góc của mình: đảo trend, thông điệp duy nhất là vũ trụ không đặt hạn giùm bạn. Có số liệu 80,6% vs 38,7% mà video trend không có, và nói thẳng giới hạn bằng chứng như sách ghi. Chuyện TOEIC chỉ dùng khi Hiệp xác nhận (S-01).

## Plan stubs (status `stub-needs-approval`, tuần 1, chỉ Hiệp, không Omi)
| Plan | Bridge | Validate |
|---|---|---|
| `research/trends/2026-10-13/plans/plan-1-ai-more-code-done-less.json` | B-aiagents-01 → clip-03 | ✔ 8 cảnh, 51,0s |
| `research/trends/2026-10-13/plans/plan-2-vu-tru-khong-gui-deadline.json` | B-trannha-01 → clip-04 | ✔ 8 cảnh, 52,0s |
Mỗi stub có 1 beat chuyện thật để placeholder `[CẦN HIỆP XÁC NHẬN]`. Beat explainer ghi trong `ideas.json` (`explainer:`) cho HyperFrames, job không render. Chưa qua humanizer / check-rules (làm ở bước make-video khi Hiệp chọn).

## Script hooks (cần Hiệp duyệt)
1. **clip-03:** đổi hook sang B-aiagents-01 (data + góc SE) thay cho B-du-an-ma-02, để clip-01 và clip-03 không cùng dựa vào "dự án ma".
2. **clip-04:** dùng B-trannha-01. Trend còn mới nên nên đăng sớm, trước khi bão hoà.
3. **clip-06:** giữ B-winterarc-01, thêm câu phụ No Man's Sky (B-nms-01) nếu Hiệp thích.
4. **B-beerus-01:** chỉ hợp khi trend còn nóng. clip-15 nằm ở tuần 3 nên có thể đã nguội. Cần kiểm lại chi tiết lore ("ngủ mấy chục năm") trước khi dùng.
5. **B-claude-01:** để dành cho tuần ≥5 khi có Omi.

## Ghi chú an toàn
- Đã loại: thượng tướng QĐND, trộm cắp, bầu cử Mỹ / Musk tài trợ, Crown Jewel (tin kèm là tấn công), miền Trung mưa rất to, Nga miễn visa, FIFA bê bối, ca tử vong sởi, AI tố giác giả vụ giết người, hacker tủ lạnh, thiếu niên kẹt vách núi, tro cốt bị trộm, drone tấn công trung tâm dữ liệu.
- Caution: Ngày Doanh nhân (không nêu tên tỷ phú), robot/AI và việc làm, KOSPI, Tăng Thanh Hà, Chelsea Green, chiêu lừa xem phim ngắn (chỉ góc phòng tránh).
- Không dùng hình, nhạc hay cảnh của Dragon Ball, No Man's Sky, trận C1, cũng không dùng hiệu ứng hay âm thanh của trend trần nhà. Chỉ nhắc tên như bối cảnh.
- "dự án ma" còn có nghĩa gốc là bất động sản lừa đảo (YT có tin "400 người bị lừa mua đất dự án ma"), nên tránh mọi hình ảnh nhà đất.

## Sync
Box ghi vào `/workspace/oneup-studio-sync/research/trends/` (ngày 2026-10-13 + `ingest.md` + `patterns.md`) và `/workspace/oneup-studio-sync/content/idea-bank.md`. `sync-trends.sh` chỉ gộp thư mục ngày và `ingest.md`, nên `patterns.md` và dòng idea-bank mới được để thêm một bản trong thư mục ngày (`patterns.md`, `idea-bank-additions.md`) để gộp tay.
