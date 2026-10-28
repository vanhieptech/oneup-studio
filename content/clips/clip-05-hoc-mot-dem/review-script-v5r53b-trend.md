---
title: "Review clip-05 v5 r5.3b — trend + ví dụ (L-090)"
date: 2026-10-28
reviewer: Rule Reviewer
target: content/clips/clip-05-hoc-mot-dem/script-v5-draft-opencreator.md @ ac691a8 (hook cuối «Sao ý đó trôi nhanh vậy?»)
verdict: CHƯA ĐẠT — làm lại toàn bộ (Hiệp 28/10 23:46 + 23:48)
---
# Review r5.3b theo nghiên cứu trend đã lưu (L-090)

**Kết luận: CHƯA ĐẠT, bỏ cả bản.** Hiệp (23:46) «sao script không dùng trend… phải làm theo hướng dẫn hot trend theo các rules đã tìm kiếm lưu trữ»; (23:48) «ví dụ ngu, trả liên quan, làm lại toàn bộ từ hook, câu văn, nội dung cần chia sẻ, ví dụ».
Lỗi của Rule Reviewer: các vòng r5.2→r5.3b chỉ chấm câu chữ, fact, liền mạch; không mở `research/trends/patterns.md` + digest 26–28/10 để đối chiếu, không hỏi ví dụ có đúng người xem không.

## 1. Luật trend đã lưu (nguồn) và kết quả
| # | Luật | Nguồn | r5.3b | Dòng |
|---|---|---|---|---|
| T1 | Script có ≥1 cụm từ/tình huống đang phổ biến **trong lời**, ghi id trend | rules/video-rules.md luật 37 | ✖ lời 172 chữ không có cụm/tình huống trend nào; id chỉ ghi «brain stacking» ở frontmatter | b01–b06; frontmatter `trend:` |
| T2 | Trend phải nghe/thấy ở hook b01–b02 bằng câu viral, format hoặc hình đặc trưng | L-084 | ✖ chỉ có hình «chồng tài liệu + cà phê» ở b01 (không nhận ra là brain stacking: trend gốc là bỏ điện thoại đọc sách thư giãn, còn hình là học dồn — ngược nghĩa); tên trend chỉ ở end card | b01 bảng hình; End card |
| T3 | Trend là cái móc ở hook, thông điệp bám trục +1 | L-088 §4 | ✖ không có móc nên hook là khuôn chung «trình bày trơn → đứng hình → sao…?» | b01 |
| T4 | Hook theo khuôn đang chạy trong thư viện pattern (P/F active), đổi kiểu so với 2 clip trước | research/trends/patterns.md (luật 47), L-088 §3, short-video-script-craft bước 4 | ✖ không khai P/F nào; hook giống khuôn clip-04 «làm X → mốc sau → quên» | b01 |
| T5 | Bridge trend → khoảnh khắc → bài học → hook VI → góc | luật 39, digest «Bridges», ingest.md | ✖ không có bridge id; B-brainstack-01 (26/10) là bridge cho 3.1 (điện thoại), không phải 23.15 | frontmatter |
| T6 | Tránh trend bão hoà; bão hoà chỉ dùng khi lật bằng fact sách | digest 28/10 «Bão hoà nên tránh: brain stacking (sat 0.97)»; patterns learnings 13/10 | ✖ brain stacking ngày 4, sat 0.97 | frontmatter, End card |
| T7 | Lớp trend lấy từ clip TikTok xếp theo view/comment, ghi beat dùng | luật 57, make-video §Trend layer | ⚠ Apify hết hạn mức 22–28/10, trend-signals.md chỉ có báo; không có số view | final/trend-signals.md |
| T8 | Ví dụ chính là nỗi đau phổ thông, ưu tiên nỗi đau có thật trong comment/trend, ghi nguồn | L-040, L-043 | ✖ không có comment/trend nào cho thấy người xem «đọc tài liệu họp hai lần liền rồi bị sếp hỏi lại» | b01–b02 |
| T9 | Ví dụ đời thường, không môn học | L-087 | ✔ | — |

`check-rules.py --trend` trên r5.3b: **6 ✖ · 1 ⚠ → FAIL** (thiếu trend_id, hook_pattern, trend_beats, trend_spoken; «brain stacking» chỉ ở end card; bão hoà 28/10; thiếu example_evidence).

## 2. Vì sao ví dụ họp/sếp hỏng (Hiệp «ví dụ ngu, trả liên quan»)
1. **Không phải nỗi đau của người xem kênh.** Kênh «how to live / +1» cho người trẻ; ít ai thuyết trình định kỳ, càng ít ai «đọc cả chồng tài liệu hai lần liền» trước họp. Không có tín hiệu comment/trend nào (T8).
2. **Ép nghiên cứu vào tình huống.** Rawson & Kintsch là đọc một bài rồi bị kiểm; «sếp hỏi lại một ý sau hai hôm» là phép thử bịa cho khớp F1.
3. **Lời khuyên không dùng được trong chính tình huống.** Lịch họp có sẵn, «chia ba tiếng ra ba ngày» cho một buổi họp là gượng; người xem không thấy mình làm theo được.
4. **Thông điệp nhỏ và tiêu cực** («đứng hình khi sếp hỏi»), không mở ra +1 mỗi ngày.
5. Trend gắn bằng hình ngược nghĩa (T2) nên cả clip không có điểm nào «đang nóng».

## 3. Brief viết lại cho OpenCreator (làm lại từ đầu)
**Thông điệp cốt lõi (chọn lại, bám 23.15 + 23.14, F1–F5 của fact-package-v5):** *Đọc/xem một lèo xong thấy «hiểu rồi» là cảm giác nhanh tan; cùng chừng đó thời gian chia ra vài ngày, mỗi lần gấp lại tự nhớ lại, thì cái mình đã học mới ở lại.* +1: mỗi ngày một buổi ngắn thay vì một đêm dồn. Không hứa kết quả.

### Ba hướng (xếp hạng)
| Hạng | Trend / pattern (nguồn) | Ví dụ đời thường | Hook nháp (OpenCreator viết lại chữ) | Vì sao |
|---|---|---|---|---|
| **A1 (đề xuất)** | **P15 Self-own first** (patterns.md, active) + **P03 Everyone says X, book says Y** (seen 26, cao nhất, +1 ngày 28/10). Móc tình huống: «Đọc nhiều có giúp viết hay hơn?» (X News, digest 26/10 #10, sat 0.30) + chuyện đọc sách thay lướt điện thoại đang được bàn (brain stacking chỉ nhắc kiểu lật nếu Hiệp duyệt, vì bão hoà) | Cuối tuần đọc một mạch hết cuốn sách / cày liền mấy video kỹ năng hay, gật gù «hay quá»; thứ Tư bạn bè hỏi «sách đó nói gì», không kể lại được ý nào | «Nói thiệt, video này bạn xem xong, chắc hai hôm nữa cũng quên. Mà đâu phải tại bạn.» → lật P03: ai cũng nghĩ đọc lại liền cho chắc | F1 đúng nguyên văn (đọc một bài hai lần liền vs cách một tuần) nên dẫn chứng lồng tự nhiên; khán giả kênh phát triển bản thân chính là người «cày» sách/video; tự nhận trước (P15) nghe như bạn bè, không giảng; hook mới hẳn so với clip-04/05 |
| A2 | **P10 Picture-this effort paradox** (seen 17, +1 ngày 28/10) + **B-tucantro-01 tự cản trở bản thân** (VnExpress, digest 28/10 #2, nov 1.0 / sat 0.15 — mới nhất, sạch) | Khoá học online (kỹ năng, nấu ăn, chụp ảnh… không môn học) mua từ đầu tháng, để tới tối trước hạn mới xem liền 6 bài, tuần sau mở ra như chưa xem | «Mua khoá học từ đầu tháng, vậy mà tới tối Chủ nhật cuối cùng bạn mới cày một lèo sáu bài?» | Trend mới 28/10, hợp trục «trì hoãn → dồn»; cần Deep Research xác nhận cách nói «xem video bài giảng» vẫn trong phạm vi F2/F3 (nguồn đo đọc/học tài liệu lời) |
| A3 | **P01 Trend-as-mirror** trên cụm viral «Học 1 đêm mới hiểu…» (@ng__phanh 1,1M / 55,3k share, comment «Sách mới tinh kh vết gấp mà😭» 3.269 like; ingest `cram-one-night`, `sach-moi-tinh`) — tín hiệu TikTok-native mạnh nhất cho đúng chủ đề | Ôn thi dồn một đêm nói chung (không môn, không giáo trình), thi xong một tuần trống trơn | «Một đêm đọc hết thứ cả tháng chưa mở…» | Mạnh nhất về số liệu nhưng: tín hiệu từ 20/10 (8 ngày, cảnh báo «không còn nóng»), v4 đã dùng (L-088 §3 cấm lặp hook bản cũ), và đụng L-087 «ôn thi» (được phép nói chung nhưng Hiệp đã từ chối hướng trường lớp) → **chỉ làm nếu Hiệp chọn** |

Không dùng lại: họp/sếp (Hiệp bác), «bông hoa chưa nở» (đang dùng cho clip-06), «đợt lạnh» (clip-07), brain stacking làm hook chính (bão hoà 28/10).

### Ràng buộc bắt buộc cho bản mới
- Frontmatter khai đủ để `check-rules.py --trend` PASS: `trend`, `trend_id` (B-… hoặc id trong ingest/digest), `hook_pattern` (P/F active), `trend_beats` (có b01/b02), `trend_spoken` (cụm trend nói thành lời ở b01–b02), `example_evidence` (link/file comment-trend chứng minh người xem có nỗi đau này).
- L-087 đời thường; L-088 dẫn chứng là một bước của chuyện (không «Một nghiên cứu cho thấy…» đứng riêng), hook/CTA mới, CTA không «Comment số…»; L-089 một ngôi kể, beat nối beat, đọc to trước khi đếm chữ.
- 140–175 chữ. Chỉ F1–F5 (fact-package-v5.md), không số %, không cơ chế não, không nói trend giúp nhớ; ví dụ đổi thì gửi Deep Research soát lại câu lồng F1.
- End card: «Thông tin tham khảo, không thay thế tư vấn chuyên gia» · «Cẩm nang sống đáng giá» – chuanman2707, CC BY 4.0 – https://chuanman2707.github.io/HowToLiveBetter/ · nguồn nghiên cứu · không ghi tác giả bảo trợ kênh · không nêu tên creator của trend.
- Social Research cập nhật `final/trend-signals.md` theo hướng được chọn (link, ngày, beat dùng, trend bỏ + lý do).
- Chạy `--subjects --l088 --flow --trend` trước khi gửi review; Rule Reviewer chấm trong group Agency; chưa Chốt thì không giọng/render.
