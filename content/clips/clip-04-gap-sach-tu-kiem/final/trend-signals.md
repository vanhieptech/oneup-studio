---
title: "clip-04 trend-signals — làm lại theo flow agents (Social Research)"
date: 2026-10-19
type: trend-signals
tags: [clip-04, trend-signals, rule-57, social-research]
status: draft
source: "research/trends/2026-10-17/apify/clips.json + raw-comments.json (Apify, thu 17/10/2026)"
id: clip-04.trend-signals
---

# clip-04 — Trend signals (bản làm lại, Social Research)

> **NOT-APPLICABLE cho việc chọn đề (theo điều phối của News): clip-04 được chọn từ handbook HTB 23.14, KHÔNG trend-driven — không dùng bất kỳ trend nào để biện minh cho việc chọn đề này.** File này chỉ đóng sổ rule-57: ghi tín hiệu TikTok gốc đã xem, đã loại và một tín hiệu hỗ trợ trùng phép thử của script, để gate 1 truy được nguồn. Dữ liệu lấy từ đợt Apify 17/10/2026 đã có trong repo — **chưa chạy scrape mới ngày 19/10**, số liệu là số thô tại thời điểm thu.

## 1. Evidence — clip TikTok đúng chủ đề học/active recall

| # | URL | Tác giả | Ngày lấy | View | Like | Comment | Tín hiệu dùng cho clip-04 |
|---|---|---|---|---:|---:|---:|---|
| 1 | https://www.tiktok.com/@phamthuykieuhuong/video/7665937572925066516 | @phamthuykieuhuong (Hương học lại) | 17/10/2026 | 995.100 | 126.400 | 138 | Video 6 giây liệt kê kỹ thuật học: lặp lại ngắt quãng, Feynman, mindmap, flashcard và **active recall** (phụ đề VTT trong `research/trends/2026-10-17/apify/`) — cùng họ phương pháp với "gấp sách tự kiểm" của HTB 23.14. Caption có hashtag #studymethod |

Nguồn số liệu: `research/trends/2026-10-17/apify/clips.json` (trường `play_count/like_count/comment_count`).

## 2. Comment mining — nỗi đau/ngôn ngữ thật dưới clip trên

Nguồn: `research/trends/2026-10-17/apify/raw-comments.json` (120 bình luận đã thu của đợt 17/10).

| Theme | Bằng chứng nguyên văn (rút gọn) | Lượt thích | Dùng ở beat |
|---|---|---:|---|
| Tự nói lại được = thuộc thật | "Feynman nó đỉnh vc, ko cần thuộc chỉ cần hiểu và hiểu rồi, nói được = lời của bản thân thì tự động thuộc" | 2.860 | b01 phép thử "tự nói lại được mấy ý", b08 "nói lại chương này" |
| Học từ vựng bằng flashcard/active recall | "Flashcard áp dụng cho học từ vựng dễ vào não lắm lun"; "Lặp lại ngắt quãng + flashcard cho từ vựng, active recall + freyman cho ngữ pháp" | 140 (bình luận thứ hai) | b02 ví dụ học 30 từ tiếng Anh (ghi rõ là minh hoạ cá nhân trong script, không phải số nghiên cứu) |
| Chỉ viết tay mới nhớ | "flashcard thì có mỗi t là phải viết tay mới nhớ hả ta" | 2 | b06/b07 viết ra giấy, giấy trắng chỗ nào chưa thuộc chỗ đó |

## 3. Pattern rút ra (chỉ nói tới mức dữ kiện cho phép)

- Một clip 6 giây chỉ nêu tên các kỹ thuật học đạt 995.100 view cho thấy chủ đề "phương pháp học" có sức hút thật trên TikTok VN tại thời điểm thu — đây là **một bài nổi bật, không tự gọi là trend** (đúng rule trong workflow Social Research).
- Bình luận được thích nhất không khen clip chung chung mà khẳng định phép thử "nói lại được bằng lời của mình" — khớp trực tiếp với hook và phép thử của script clip-04, nên giữ hook pain "sáng nay không mở sách, bạn tự nói lại được mấy ý?" thay vì đổi sang kể chuyện.

## 4. Trend/bài đã loại và lý do

| Bài | Lý do loại |
|---|---|
| @dacvubanana — nhảy dây buổi sáng, 675.800 view (17/10) | Chủ đề vận động/sức khỏe, không phải phương pháp học; chệch chủ đề clip-04 |
| @hoaquynh0000 — phát triển bản thân, 459.100 view (17/10) | Video dài 546 giây, nội dung chữa lành chung, không có tín hiệu active recall |
| @iamuyenvu — phát triển bản thân nguồn lực hạn chế, 459.100 view (17/10) | Chủ đề rộng, không gắn phép thử tự kiểm |
| Dữ liệu đợt 19/10 trong `research/trends/2026-10-19/apify/clips.json` | Chưa thấy clip nào đúng chủ đề phương pháp học trong danh sách đã thu; không bịa tín hiệu mới |

## 5. Caveat

- Số liệu là ảnh chụp tại 17/10/2026, có thể đã thay đổi; muốn số mới phải chạy lại Apify và ghi ngày lấy mới.
- Mẫu đúng chủ đề chỉ có 1 clip mạnh + bình luận của chính clip đó — đủ làm tín hiệu hỗ trợ cho clip chọn từ HTB, **không** đủ kết luận "active recall đang là trend toàn TikTok VN".
- Mọi claim khoa học trong script (Yang 2021, Dunlosky 2013) không lấy từ TikTok — phần đó chờ Deep Research kiểm chứng riêng.

## 6. Bàn giao

- Cho **Deep Research**: kiểm chứng các claim HTB 23.14/23.16 trước khi OpenCreator viết bản làm lại.
- Cho **Rule Reviewer**: file này là đầu vào rule-57 ở gate 1 của bản làm lại; xung đột cũ "trend not-applicable" trong script-v07 cần được ghi nhận là đã có trend-signals bổ sung.
