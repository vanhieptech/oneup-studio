---
id: trends-2026-10-13-v2
date: 2026-10-13
version: 2
supersedes: none (v1 = digest.md, giữ nguyên)
collector: pipeline/scripts/trend-collect.py v1 + X MCP extra
---
# Trend digest 2026-10-13 · v2 (chạy lại, nhiều nguồn)

## So với v1
| | v1 (7:55 sáng) | v2 (12:50 trưa) |
|---|---|---|
| Nguồn chạy được | ~5 (Google Trends, YT search, web search, vài RSS) | **36** (33 trong sources.yaml + 3 X qua MCP) |
| Ứng viên thô | 41 | **470** (+ 41 mục v1 = 490 trong raw.v2.json) |
| Sau gộp trùng | 41 | 449 cụm |
| Qua lọc an toàn | 27 | 366 ok · 13 caution · 70 drop |
| X | lỗi (MCP không kết nối) | ok: trends VN + worldwide, 13 story X News |
| TikTok Creative Center | chặn | vẫn chặn (API cần chữ ký trình duyệt) → thay bằng Google News "trend TikTok", Kenh14, X News |

Dữ liệu: `collect.json` (từng nguồn + trạng thái), `x-extra.json`, `raw.v2.json` (đã chấm điểm bằng trend-learn.py).

## Top 10 (đã lọc an toàn, bỏ mục "pattern-evidence")
| # | Trend | rank | Nguồn / tín hiệu | Bài học (theme-map) | Theme |
|---|---|---|---|---|---|
| 1 | Tranh cãi "lịch sống chuẩn": 10k bước + ngủ 8h + nấu ăn + dọn nhà + đi làm năng suất, ai làm nổi? | 0.954 | [X News](https://x.com/i/trending/2109882688521847142), cập nhật 12:47 | 4.1 nếu–thì (làm ít, xong nhiều) / 2.17 | LIGHT |
| 2 | 10.000 bước/ngày có thực tế? (gốc từ quảng cáo máy đếm bước 1965) | 0.774 | [X News](https://x.com/i/trending/2109372046493003926) | 2.17/2.11 đứng dậy, 7–8k bước (clip 18) | LIGHT |
| 3 | "Năng suất tuổi trưởng thành = thử mẹo tâm lý mới liên tục" | 0.731 | [Bluesky](https://bsky.app/profile/astrokatie.com/post/3mxh6wwsuku27) 3,7k like / 624 repost | 4.12 "21 ngày tạo thói quen" là myth (clip 6) | DARK |
| 4 | Sếp ôm thêm việc vì cấp dưới lạm dụng AI | 0.707 | [VnExpress](https://vnexpress.net/sep-om-them-viec-vi-cap-duoi-lam-dung-ai-5130995.html) | 4.7 chia việc tới mức xong (clip 3) | DARK |
| 5 | Dan Koe: 6 tháng = 1% đời, mà đa số bỏ sau 2 tuần | 0.671 | [X News](https://x.com/i/trending/2109031954121421089) | 4.12 myth 21 ngày; pattern P08 | DARK |
| 6 | Harvard: AI agent viết thêm 30% code, việc xong không tăng (v1) | 0.605 | Ars, Forkast + [X News "AI coding tools debate"](https://x.com/i/trending/2109535489006969212) | 4.7 (clip 3) | DARK |
| 7 | Chụp trần nhà nhận "thông điệp vũ trụ" (v1, vẫn nóng) | 0.592 | [Kenh14](https://kenh14.vn/mot-chiec-trend-dang-viral-chup-anh-tran-nha-de-nhan-thong-diep-tu-vu-tru-ban-bi-cuoc-doi-di-toi-muc-nay-roi-sao-215261013063429553.chn) + Google News "trend TikTok" (2 nguồn) | 4.8 tự đặt deadline (clip 4) | LIGHT |
| 8 | "AI tăng năng suất, team thì kiệt sức" | 0.560 | [Fast Company qua Google News](https://news.google.com/rss/articles/CBMiigFBVV95cUxOMXZLcGJhQlgwamdIcENmLWNlRWVXWVM2ZEVkMnl0cl9veHI1ejhDeGQ3NTNHYmxPZ2ZUWTh1SEdfZmdhUnRIaXFXMld2T0VLNTgwYzM5c3Z0SzFId0xaNjJEMjM3X2ZiTlhYS3BHYWdDc2Zxd25GQ3dLQnZqODlFaEF0TDBQYWtzT0E?oc=5) | 3.13 quá ~49h/tuần (clip 12) | DARK |
| 9 | Trì hoãn không phải lười (bão hoà: YT VN 1,4M view cùng góc) | 0.555 | [Google News](https://news.google.com/search?q=procrastination%20rigid%20thinking), [YT 1,4M](https://www.youtube.com/watch?v=eTMAOdNBIAQ) | 4.9 (clip 2), chỉ làm với góc ngược | DARK |
| 10 | Mệt vì ngày nào cũng phải nghĩ "ăn gì" | 0.539 | [X News](https://x.com/i/trending/2109687884089295006) | 6.25 "ý chí cạn như pin" là myth (clip 19) → góc ngược | DARK |

Đáng để ý thêm: [Hiệu trưởng dạy bằng laptop, học sinh không "dán mắt"](https://vnexpress.net/hieu-truong-thcs-giang-vo-noi-gi-ve-tiet-hoc-so-cho-100-hoc-sinh-dung-laptop-5131197.html) (3.1) · [Bớt vội mỗi ngày](https://x.com/i/trending/2109703689770307692) (3.21) · 連休明け "đi làm lại sau kỳ nghỉ" đang top X Nhật (3.2 ngủ bù) · [Giáo viên than học sinh thiếu tự lập](https://x.com/i/trending/2109053163361689608) (23.14).

## Learning
- Pattern P03 "Ai cũng nói X, sách nói Y" mạnh nhất hôm nay (#1, #3, #8, #10 đều là tranh luận). P08 (thử N ngày) có thêm Dan Koe.
- **Bão hoà, tránh góc thẳng:** "trì hoãn không phải lười" (YT VN 5/8 kết quả top cùng góc, 100k–1,4M view); "how to stop procrastinating" EN. Chỉ làm khi có góc ngược hoặc chuyện thật của Hiệp.
- Chủ đề "AI làm năng suất ảo" xuất hiện ở 4 nguồn độc lập (HN, X News x2, VnExpress, Fast Company) → cụm chủ đề nóng cho clip 3.

## Bridges mới (khác biệt)
- **B-routine-01** (#1+#2). Mọi người đang nói: lịch chuẩn là ảo, hoặc "kỷ luật thì làm được hết". Góc của mình: hông cần lịch chuẩn, cần MỘT câu nếu–thì cho ngày tệ nhất (4.1); bước chân thì 7–8k là đủ theo sách (2.17), con số 10k là quảng cáo. Hook P03: "Ai cũng cãi 10 ngàn bước. Sách nói bạn đang đếm dư." `[CẦN HIỆP XÁC NHẬN]` chuyện ngồi code cả ngày.
- **B-aiboss-01** (#4+#6+#8). Mọi người đang nói: AI giúp làm nhanh gấp mấy lần. Góc của mình: việc chưa "xong" thì nhanh mấy cũng đẩy sang người review, sếp ôm thêm việc. Chia việc tới mức một lần ngồi là xong (4.7). Hook: "AI viết code giùm bạn. Ai review giùm sếp bạn?"
- **B-tricks-01** (#3+#5). Mọi người đang nói: thử mẹo mới, thử thử thách 6 tháng. Góc của mình: thói quen không có "ngày 21" hay "tháng 6" thần kỳ (4.12), cái cần là giữ được ở ngày chán nhất. Omi cà khịa "mẹo thứ 37 rồi đó nha" (tuần ≥5).
- **B-anggi-01** (#10). Góc ngược: "ăn gì" mệt thật, nhưng không phải vì ý chí cạn như pin (6.25 nói đó là myth). Cần kiểm tra lại câu chữ trong sách trước khi viết.

## Plan stubs
Không tạo stub mới trong v2. Hai stub v1 (`plans/plan-1-ai-more-code-done-less.json`, `plans/plan-2-vu-tru-khong-gui-deadline.json`) vẫn là top 2 để làm. B-aiboss-01 nên nhập vào plan-1 (thêm số liệu VnExpress) khi Hiệp duyệt.

## An toàn
70 mục bị lọc tự động (chính trị, tai nạn, tội phạm, vé số/jackpot, nội dung người lớn trên Wikipedia top). Lọc từ khoá chỉ là bước đầu, top 10 ở trên đã được đọc lại thủ công.
