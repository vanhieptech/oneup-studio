---
title: "Shorts Cutter: nhịp cắt, hook 3 giây và chuyển bản sang Reels/Shorts (2026-10-20)"
date: 2026-10-20
id: research.shorts-cutter.pacing-hook-2026-10-20
type: research
status: draft-for-review
updated: 2026-10-20
tags: [shorts-cutter, pacing, hook, editing, safe-zone, reels, youtube-shorts, tiktok, hi.oneup]
source: "Dữ liệu Apify có sẵn trong research/trends/2026-10-16..20/apify (clips.json, vtt/), research/trends/2026-10-20/social-research, đo ffmpeg trên /tmp/vids (8 clip đã có sẵn trên box) và out/clip-04-final.mp4; web: TikTok Ads Help, Google Ads/YouTube Help, Meta Ads Guide, Dost & Huang 2026"
---

# Shorts Cutter: nhịp cắt, hook 3 giây và chuyển bản sang Reels/Shorts

File này chỉ là nghiên cứu. Mình không render, không commit, không đổi rule nào. Chỗ nào khác với rule đã chốt thì được ghi là **đề xuất, chờ Hiệp duyệt**.

**Cách đo và giới hạn (đọc trước khi dùng số):**
- Số cắt cảnh đo bằng `ffmpeg -vf "select='gt(scene,T)',showinfo"` với hai ngưỡng: T=0,3 (theo brief) và T=0,15 (cùng ngưỡng với `research/trends/2026-10-20/social-research/scene-cuts.txt`). Video gốc là 8 file 576×1024 đã có sẵn ở `/tmp/vids/`. Mình không tải thêm video nào.
- Scene detection chỉ bắt **cắt cứng / đổi khung lớn**. Nó không bắt chữ hiện dần, quiz đổi đáp án, bong bóng thoại đổi hay zoom nhẹ. Vì vậy clip "0 cắt" vẫn có thể đổi hình liên tục bên trong khung. Mình ghi rõ khi thấy chuyện này trên contact sheet.
- Thời điểm lời đầu và số âm tiết trong 0–3s lấy từ file VTT phụ đề tự động của TikTok (do Apify tải về). Timing chỉ gần đúng, sai khoảng ±0,1–0,3s. "Âm tiết" được tính bằng số từ tách theo khoảng trắng trong VTT.
- Mẫu nhỏ: 8 clip đo được hình (2 clip tiếng Anh, chỉ để tham khảo) và 24 clip có VTT. **Trong 30 ngày gần nhất (từ 2026-09-20) chỉ có 13/32 clip trong dữ liệu**. Clip đo được hình mà nằm trong 30 ngày chỉ có @gonaox (10/10). Đây không phải mẫu thống kê đại diện.
- Lượt này **không chạy Apify** (chi phí 0). Dữ liệu 5 ngày đã thu đủ cho câu hỏi về hook và lời; thứ còn thiếu là file video, mà Apify cấu hình `shouldDownloadVideos:false` và brief cấm tải hàng loạt.

## (a) Bảng clip tham chiếu

### a1. 8 clip đo được hình (ffmpeg trên /tmp/vids)

Views/likes/comments lấy từ `2026-10-20/social-research/tiktok-page-stats-2026-10-20.json` hoặc `apify/clips.json` của ngày ghi bên cạnh. "Cắt" = số lần đổi cảnh phát hiện được. "Shot TB" = độ dài clip ÷ (số cắt + 1) ở ngưỡng 0,15.

| # | Clip (URL) | Ngày đăng | Views | Likes / Cmt | Độ dài | Cắt @0,3 (0–3s) | Cắt @0,15 (0–3s) | Shot TB @0,15 | Kiểu hook 0–3s (đọc contact sheet + VTT) | Phụ đề / chữ |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | [@gonaox/7694997202954915079](https://www.tiktok.com/@gonaox/video/7694997202954915079) – hoạt hình người que, gần format OneUp nhất | 2026-10-10 | 331,7K | 31,2K / 151 | 143s | 2 (0) | 51 (1, ở 2,5s) | 2,8s | Lời từ 0,12s: "7 thói quen học tập của học sinh giỏi nhất lớp". Tiêu đề kinetic typography hiện từng cụm 0–2,5s (đỏ/đen/vàng), hình minh họa đầu tiên cắt vào ở ~2,5s | Không có dải phụ đề, chỉ có tiêu đề góc trên trái. Lưu ý: clip có câu "95% học sinh không biết" không có nguồn, **không học theo** |
| 2 | [@laygoctienganh100/7686060242202823943](https://www.tiktok.com/@laygoctienganh100/video/7686060242202823943) | 2026-09-16 | 3,6M | 323,9K / 1.625 | 54,7s | 2 (0) | 17 (2) | 3,0s | Cắt cảnh show truyền hình, câu hỏi ở caption "…tiếng Anh là gì?" | Phụ đề song ngữ ngay dưới khung hình ở giữa màn (~55–62% chiều cao), từ khóa tô đỏ, thẻ từ vựng nằm trên khung |
| 3 | [@vi_vocamore/7668955024902327568](https://www.tiktok.com/@vi_vocamore/video/7668955024902327568) | 2026-08-01 | 1,1M | 50,3K / 90 | 33,9s | 0 | 0 | (1 khung) | Quiz thách đố: "Có vài từ B1… bạn thử đoán hết không?", lời từ đầu đọc từ khóa | Không có phụ đề lời. UI quiz ở nửa trên: câu hỏi → 4 đáp án → đáp án đúng chuyển xanh. **Đổi trong khung liên tục nên scene detect không bắt được** |
| 4 | [@hoctienganhnhanhh/7649671232765332744](https://www.tiktok.com/@hoctienganhnhanhh/video/7649671232765332744) | 2026-06-10 | 1,2M | 75,5K / 500 | 30s | 0 | 0 | (1 khung) | Thẻ "Dịch là gì?" + chữ cái gợi ý (F____), đáp án hiện sau ~1 nhịp | Thẻ chữ ở giữa màn (~40–55%), nền tĩnh |
| 5 | [@camreadwonder/7614813783201975573](https://www.tiktok.com/@camreadwonder/video/7614813783201975573) | 2026-03-08 | 287,7K | 32,8K / 58 | 34,7s | 0 | 0 | (1 khung) | Câu than của người học (caption "Em học em không nhớ thì làm sao hả chị?"), một cảnh quay liền | Chữ trắng giữa màn (~55–65%), 2 dòng, đổi theo câu |
| 6 | [@phamthuykieuhuong/7665937572925066516](https://www.tiktok.com/@phamthuykieuhuong/video/7665937572925066516) | 2026-07-24 | 995,1K | 126,4K / 138 | 6,6s | 0 | 0 | (1 khung) | Danh sách "Top 5 phương pháp…" hiện từng dòng, nói nhanh 4 âm tiết/s | Tiêu đề trên, list bên trái ở giữa màn |
| 7 | [@jesstudyofficial/7372211750675942689](https://www.tiktok.com/@jesstudyofficial/video/7372211750675942689) (EN, chỉ tham khảo) | 2024-05-24 | 6,0M | 469,9K / 1.881 | 19,6s | 10 (0) | 20 (4) | 0,9s | Tiêu đề "How to REMEMBER EVERYTHING you read" từ frame 0, đổi tên phương pháp ở ~2,5s | Chữ vàng to ở giữa màn |
| 8 | [@studywithlizzz/7631060689825582367](https://www.tiktok.com/@studywithlizzz/video/7631060689825582367) (EN, chỉ tham khảo) | 2026-04-21 | 7,5M | 811,6K / 967 | 83,1s | 22 (2) | 31 (2) | 2,6s | Hình kết quả trước (xấp flashcard dày), lời "not everybody…" hiện từng chữ | Phụ đề từng chữ, nghiêng, nhỏ, ở giữa màn |
| — | **Đối chiếu nội bộ:** `content/clips/clip-04-gap-sach-tu-kiem/final/out/clip-04-final.mp4` (render lúc 11:25 ICT 20/10, **trước khi v18 khóa lúc 23:12 ICT**, không phải bản v18) | — | — | — | 69,0s | 0 (0) | 3 (0) | 17,2s | Chữ hook to ở frame 0 "HỌC THUỘC TỐI QUA, SÁNG DẬY QUÊN SẠCH?", cùng một khung bàn học suốt 0–3s; chỉ bong bóng và caption đổi | Dải tiêu đề trên y≈56–253px; caption EN trong plate y≈1490–1700px (đo trên frame 1,5s) |

### a2. Hook lời 0–3s từ VTT (24 clip VN, dữ liệu Apify 16–20/10)

Tổng hợp từ 24 clip: lời đầu xuất hiện ở trung vị **0,08s** (20/24 clip ≤ 0,3s). Trong 0–3s có trung vị **13,5 âm tiết** (khoảng 6–18). Tốc độ cả clip trung vị **4,1 âm tiết/s** (khoảng 2,6–6,3). Thời lượng trung vị của cả 32 clip là 58,5s, 16/32 clip ≤ 60s.

| Clip | Ngày đăng | Views | Độ dài | Lời đầu | Âm tiết 0–3s | Câu mở (VTT) | Kiểu hook |
|---|---|---|---|---|---|---|---|
| [@kbhoanganh/7534286009832393991](https://www.tiktok.com/@kbhoanganh/video/7534286009832393991) | 2025-08-03 | 3,7M | 18s | 0,08s | 11 | "mày dẹp điện thoại đi / suốt ngày mày cầm điện thoại lướt TikTok hoài" | Mắng thẳng người xem (gọi "mày") |
| [@hoang_hao209/7654547690730114322](https://www.tiktok.com/@hoang_hao209/video/7654547690730114322) | 2026-06-23 | 1,4M | 14s | 0,00s | 13 | "top những dấu hiệu nhận biết những đứa đang bị nghiện điện thoại… top một là mày đó" | Danh sách "top" + chỉ thẳng người xem |
| [@sabito_0668/7670995147995237640](https://www.tiktok.com/@sabito_0668/video/7670995147995237640) | 2026-08-06 | 606K | 100s | 0,00s | 14 | "phải thức khuya thì thức thôi nhưng để ý cơ thể một tí" | Chấp nhận nỗi đau, rồi đưa cách giảm hại |
| [@hoc.di.roi.biet/7695270625660652820](https://www.tiktok.com/@hoc.di.roi.biet/video/7695270625660652820) | 2026-10-11 | 390,7K | 48s | 0,16s | 18 | "Xin lỗi mọi người nhá… mình sẽ xóa video này sau 24 tiếng" | Gây gấp/bí mật (dạng câu kéo click, **không học theo**) |
| [@gonaox/7694997202954915079](https://www.tiktok.com/@gonaox/video/7694997202954915079) | 2026-10-10 | 331,7K | 143s | 0,12s | 13 | "7 thói quen học tập của học sinh giỏi nhất lớp" | Lời hứa dạng danh sách có số |
| [@colo.vn/7693555573517782278](https://www.tiktok.com/@colo.vn/video/7693555573517782278) | 2026-10-06 | 288,5K | 20s | 0,08s | 11 | "top BA dấu hiệu cho thấy hôm nay là một ngày làm việc kinh hoàng" | Danh sách "top" về nỗi khổ quen thuộc |
| [@biquyetdodaihoc/7620113093401627924](https://www.tiktok.com/@biquyetdodaihoc/video/7620113093401627924) | 2026-03-22 | 110,8K | 45s | 0,04s | 13 | "lười học quá bây giờ làm sao anh, giồi ôi" | Câu than của người học (đối thoại) |
| [@kyluat.1/7631923883968580885](https://www.tiktok.com/@kyluat.1/video/7631923883968580885) | 2026-04-24 | 101,9K | 54s | 0,12s | 10 | "bạn không cần một năm để thay đổi cuộc đời" | Phủ định niềm tin, gọi "bạn" |

Toàn bộ 32 dòng (kể cả clip không có VTT) có ở `research/trends/2026-10-1{6..9}/apify/clips.json` và `2026-10-20/apify/clips.json`.

## (b) Pattern rút ra

1. **Lời vào ngay, gần như không có khoảng lặng đầu.** 20/24 clip VN có lời đầu ≤ 0,3s, trung vị 0,08s (bảng a2). Điều này khớp với rule-55 ("lời đầu ≤ 0,3s").
2. **Mật độ lời 0–3s cao:** trung vị 13,5 âm tiết trong 3s (khoảng 4,5 âm tiết/s), cao hơn tốc độ cả clip (4,1/s). Nghĩa là creator nói nhanh nhất ở hook. Khớp với L-027 (hook speed 1.2, gap ≤ 0,1s).
3. **Nhịp cắt cứng không phải bắt buộc.** 4/6 clip VN đo được có 0 cắt cứng ở ngưỡng 0,3 nhưng vẫn 0,3–3,6M views. Thứ giữ mắt là **đổi trong khung**: chữ hiện từng cụm, quiz đổi trạng thái, thẻ đáp án lật (bảng a1, #3–#6). Clip có cắt (#1, #2, #8) đều ra shot trung bình **2,6–3,0s** ở ngưỡng 0,15. Con số này khớp với benchmark ngoài: 50 TikTok talking-head giáo dục có trung bình 0,37 cắt/s, mốc thấp/trung vị/cao là 0,189 / 0,331 / 0,517 cắt/s (Dost & Huang 2026, [PDF](https://archives.marketing-trends-congress.com/2026/pages/PDF/paper_professor_DOST_HUANG.pdf), mẫu TikTok Đức, đo bằng PySceneDetect). Cùng nghiên cứu (thí nghiệm N=242) thấy cắt nhanh hơn trung vị **không** làm người xem xem tiếp nhiều hơn: "Don't chase speed for its own sake".
4. **Hook format chạy trong ngách:** (i) gọi thẳng người xem và nêu nỗi đau ("mày/bạn…"); (ii) danh sách có số ("top 3 dấu hiệu", "7 thói quen"); (iii) câu than của người học dạng đối thoại; (iv) đưa hình kết quả trước (xấp flashcard). Dạng (i) và (iii) trùng với hướng L-057/L-064: nói thẳng pain point của người xem. Dạng "xóa video sau 24h" và số % không nguồn có xuất hiện nhưng phạm rule không bịa số, nên loại.
5. **Chữ hook ở frame 0, đặt ở giữa hoặc trên màn, không đặt sát đáy.** Ở cả 8 clip đo hình, chữ chính nằm trong khoảng ~20–65% chiều cao, không clip nào đặt chữ chính ở 20% đáy (đọc contact sheet). TikTok khuyên "introduce your content proposition in the first 3 seconds", ưu tiên hook trong 6s đầu, và chữ overlay ở mức 5–10 từ/giây ([TikTok Ads Help: Creative best practices, cập nhật 6/2025](https://ads.tiktok.com/help/article/creative-best-practices)). Đây là hướng dẫn cho quảng cáo, không phải cho video thường.
6. **Format gần OneUp nhất (@gonaox, hoạt hình người que, 143s, 331,7K views):** tiêu đề hiện từng cụm trong 0–2,5s, rồi cứ ~2,8s đổi một hình minh họa (51 lần đổi ở ngưỡng 0,15). Mỗi ý có một hình ẩn dụ riêng (đồng hồ gạch chéo, đám đông dấu hỏi, đồng hồ cát). Cách này cho thấy comic/vẽ tay giữ được nhịp bằng **đổi hình minh họa theo từng ý**, không cần cắt cảnh quay.

## (c) Đề xuất cho clip comic @hi.oneup (đối chiếu rule đã chốt)

| # | Đề xuất | Đối chiếu rule/lesson | Trạng thái |
|---|---|---|---|
| c1 | Giữ nguyên rule-55 cho 0–3s: chữ hook ở frame 0, lời đầu ≤ 0,3s, ≥ 2 cut/hit. Dữ liệu ở (b1)(b2) ủng hộ. | rule-55, L-021, L-027 | Khớp rule, không đổi |
| c2 | Trong rule-55 nên đếm "hit" gồm cả **đổi trong khung**: chữ hiện từng cụm, bong bóng đổi, prop pop, zoom/push. Không bắt cắt cứng. Bản render 11:25 của clip-04 có **0 cắt cứng** trong 0–3s (đo ở cả hai ngưỡng), nên muốn đạt ≥ 2 hit thì 0–3s phải có hit dạng này **đo được**: ví dụ tiêu đề hiện 2 cụm "HỌC THUỘC TỐI QUA," → "SÁNG DẬY QUÊN SẠCH?" như @gonaox, kèm 1 push vào mặt Thầy ở chữ "quên sạch". | rule-55 (check-rules đo từ timing.json) | Đề xuất kỹ thuật cho khâu dựng, không đổi lời đã khóa v18 |
| c3 | Mục tiêu nhịp thân clip: **đổi hình đáng kể khoảng mỗi 2,5–3,5s** (≈ 0,3 lần/s, gần trung vị Dost & Huang 0,331/s và @gonaox 2,8s), bằng góc/khung mới, insert prop, morph hoặc motion graphic. Không cần cắt cứng. Giới hạn hiện tại "mỗi beat ≤ 8s" (L-043) vẫn giữ; trong một beat 6–8s nên có 2 lần đổi hình. Bản render 11:25 có 3 lần đổi khung lớn trong 69s (≈ 17s/khung theo scene detect); contact sheet cho thấy ~27s đầu gần như cùng một khung bàn học. | L-043, L-047/L-048/L-049 (doodle/morph là hiệu ứng đổi hình chính) | **Đề xuất, chờ Hiệp duyệt** (chưa phải rule) |
| c4 | Không đẩy nhịp quá nhanh (dưới ~2s/shot) chỉ để "dồn dập". Bằng chứng cho thấy lợi ích về xem tiếp giảm dần ở nhịp cao (Dost & Huang 2026). Riêng 0–3s thì dồn được theo rule-55. | rule-55 chỉ áp cho 0–3s | Đề xuất |
| c5 | Hook lời: mẫu VN chạy tốt nhất là gọi thẳng "bạn" + nỗi đau quen thuộc, nói trong ≤ 3s (~10–15 âm tiết). Hook v18 "Học thuộc tối qua, sáng dậy quên sạch?" có 8 âm tiết, nằm trong khoảng 6–18 của mẫu. Không thêm dạng "xóa video sau 24h" hay số % không nguồn. | L-057, L-058, L-064, rule không bịa số | Khớp, không đổi lời đã khóa |
| c6 | **Vị trí caption khi cross-post:** caption plate của bản render 11:25 nằm ở y≈1490–1700px. Vị trí này lọt vào vùng đáy bị UI che theo template quảng cáo của cả 3 nền tảng (TikTok từ y≈1260, Reels/Shorts từ y≈1248, xem mục e1). Ở bản TikTok thường thì đáy bị che ít hơn (bên thứ ba đo được ~334px, tức từ y≈1586), nên plate vẫn chạm phần dưới. Trong dữ liệu trend, chữ chính đều nằm ở ~20–65% chiều cao (b5). Đề xuất: bản Reels/Shorts kéo plate lên vùng y≈1000–1240, hoặc giữ nguyên nếu Hiệp chấp nhận bị che một phần. | L-033 (vùng an toàn hiện tại y 150–1460), brand-tokens `caption.plate.bottomOffset: 420` | **Đề xuất, chờ Hiệp duyệt**, không sửa token |
| c7 | Dải tiêu đề hook (y≈56–253px) nằm trong vùng trên bị UI che của Reels (269px) và Shorts (288px), và chạm vùng 240px của TikTok ads. Nếu xuất riêng bản Reels/Shorts thì dời xuống ~y≥300. | — | Đề xuất, chờ Hiệp duyệt |
| c8 | Không chèn nhạc vào file (rule-21); Hiệp tự thêm nhạc lúc đăng. Đề xuất này không đụng tới âm thanh ngoài loudness. | rule-21, rule-4 | Khớp |

## (d) Áp cho việc cắt Shorts từ video dài sau này

1. **Chọn điểm vào:** đoạn cắt phải mở bằng câu có lời ngay ≤ 0,3s (cắt sát trước âm tiết đầu, bỏ "à, ừm, thì", bỏ hơi thở). Câu mở nên là câu gọi thẳng nỗi đau hoặc kết quả (b4), không mở bằng câu dẫn trung tính (L-021).
2. **Tiêu đề frame 0:** burn một dòng hook ≤ 7 chữ ở giữa hoặc trên màn ngay frame 0, hiện 2 cụm trong 0–2,5s như @gonaox. Video quay người thật sẽ có ít "đổi trong khung" hơn comic, nên chữ hiện dần chính là hit.
3. **Nhịp:** video nói chuyện có thể dùng jump cut bỏ khoảng lặng > 0,3s, nhắm khoảng 0,2–0,35 cắt/s (mốc thấp đến trung vị của Dost & Huang). Thêm punch-in 110–120% ở từ khóa để tạo hit thay cho cắt. Nghiên cứu cho thấy cắt "chồng nhẹ" (overlapping) ở nhịp thấp tốt cho xem tiếp; cắt liền mạch (seamless) tốt cho like.
4. **Đo trước khi trình:** chạy `select='gt(scene,0.15)'` và `0.3` trên mỗi Short, ghi số cắt, số cắt 0–3s và shot TB vào báo cáo, như bảng a1.
5. **Phụ đề:** một cụm 3–5 chữ (brand-tokens `caption.chunk`), đặt trong vùng an toàn chung của cả 3 nền tảng (mục e1). Luôn xuất `.srt` rời (tính năng PR #1 của Short Factory, đang chờ Hiệp duyệt).
6. Cổng bản quyền và cổng duyệt đoạn trong `workflows/agents/shorts-cutter.md` vẫn giữ nguyên: không có video tự sở hữu thì không cắt.

## (e) Chuyển bản TikTok 9:16 sang Instagram Reels và YouTube Shorts (2026)

Lưu ý chung: **không nền tảng nào công bố vùng an toàn cho video thường.** Các số dưới đây là template **quảng cáo** chính thức. Đây là ngưỡng an toàn nhất có nguồn chính thức.

### e1. Vùng an toàn UI (khung 1080×1920)

| Nền tảng | Trên | Dưới | Trái | Phải | Vùng sạch | Nguồn |
|---|---|---|---|---|---|---|
| TikTok (In-Feed ads) | 240 | 660 (từ y=1260) | 120 | 120, cộng cột nút 180px từ y=840 trở xuống (tổng 300) | 840×1020 | TikTok Ads Help, template In-Feed (số cột nút do bên thứ ba đo từ file, theo [Socialync](https://www.socialync.io/tools/safe-zones/tiktok), [AdCheckLab](https://adchecklab.com/faq)) |
| Instagram Reels | 14% = 269 | 35% = 672 (từ y=1248); quảng cáo có disclaimer 40% = 768 | 6% = 65 | 6% = 65 | 950×979 từ (65,269) | Meta Ads Guide – Instagram Reels: "leaving at least 14% of the top, 35% of the bottom and 6% on each side… free from text, logos" (trích theo [Solid](https://www.solidlabs.com/social-safe-zones), [anglr](https://anglr.co/tools/instagram-reels-safe-zone)) |
| YouTube Shorts | 288 | 672 (từ y=1248) | 48 | 192 | 840×960 từ (48,288) | Google Ads Help – safe zones vertical video ads ([support.google.com/google-ads/answer/13547298](https://support.google.com/google-ads/answer/13547298?hl=en)); số px lấy từ ảnh template, theo [Socialync](https://www.socialync.io/tools/safe-zones/youtube-shorts) |
| **Giao của cả 3** | **288** | **672 (nội dung chính kết thúc trước y=1248)** | **120** | **192 (300 nếu dưới y=840)** | x 120–888 (dưới y=840) / 120–960 (trên), y 288–1248 | Tính từ 3 dòng trên |

Vùng an toàn trong repo hiện là y 150–1460, x 60–1020 (L-033, `layout.ts`). Vùng này rộng hơn cả 3 template quảng cáo. Nó hợp với TikTok thường, nhưng bản Reels/Shorts có thể bị che (xem c6, c7).

### e2. Giới hạn độ dài

| | Giới hạn | Khuyến nghị | Nguồn |
|---|---|---|---|
| YouTube Shorts | Video dọc/vuông ≤ 3 phút (upload từ 15/10/2024) được tính là Short. **Short > 1 phút có claim bản quyền bất kỳ sẽ bị chặn toàn cầu** (bài Help tiếng Anh; bài Help tiếng Hàn ghi rằng không còn tự chặn nữa, hai bản đang mâu thuẫn, cần kiểm lại lúc đăng) | Với OneUp: 45–60s như hiện tại. Không có nhạc trong file (rule-21) nên rủi ro claim thấp, nhưng nếu thêm nhạc trên YouTube thì giữ ≤ 60s cho chắc | [YouTube Help 15424877](https://support.google.com/youtube/answer/15424877?hl=en), [Upload Shorts](https://support.google.com/youtubecreatorstudio/answer/12779649) |
| Instagram Reels | Trong app: tổng tối đa 20 phút. API: 3s–15 phút, ≤ 300MB, ≤ 25 Mbps VBR. **"Reels over 3 minutes won't be recommended to new audiences"** | ≤ 3 phút (OneUp 45–70s đạt) | Instagram Help "record a reel" và Meta IG User Media API (trích theo [Clapr, kiểm 16/9/2026](https://clapr.app/blog/instagram-reels-length-limit)) |

### e3. Ảnh bìa / thumbnail

- **Reels cover:** upload 1080×1920 (9:16). Lưới profile hiển thị **3:4 = 1080×1440 ở giữa** (cắt 240px trên và dưới) từ khi Instagram đổi sang lưới dọc tháng 1/2025 ([The Verge 17/1/2025](https://www.theverge.com/2025/1/17/24346304/instagram-profile-grids-rectangles-squares), [Mosseri trên Threads](https://www.threads.com/@mosseri/post/DFBmsT0SKO6)). Ảnh feed/carousel là 4:5 (1080×1350). Một số giao diện cũ vẫn có thể hiện lưới vuông, nên chữ chính đặt trong vùng 1080×1080 ở giữa là an toàn nhất (khuyến nghị của Hopper HQ, không phải số chính thức của Meta). Instagram cho chỉnh "Adjust preview" sau khi đăng.
- **Shorts thumbnail:** trên app di động chọn được **bất kỳ frame nào**. Trên Studio desktop chọn được 1 trong 3 frame gợi ý. **Upload ảnh riêng** chỉ dành cho kênh trong YouTube Partner Program (bắt đầu từ 24/7/2026, mở dần), làm trên Studio desktop, tài khoản phải đã xác minh: tỉ lệ 9:16, khuyến nghị 2160×3840, chiều cao tối thiểu 640px, JPG/PNG, ≤ 50MB ([YouTube Blog 24/7/2026](https://blog.youtube/news-and-events/youtube-studio-custom-thumbnail-updates/), [YouTube Help 72431](https://support.google.com/youtube/answer/72431)). Nếu dùng thumbnail 16:9 cho video dọc, YouTube sẽ thay bằng thumbnail 4:5 tự sinh ở Home/Explore/Subscriptions.
- `cover.png` của clip-04 đang là 1080×1920, dùng thẳng làm Reels cover được; cần soát vùng 3:4 và 1:1 (checklist e6).

### e4. Caption / tiêu đề / hashtag

| | Giới hạn | Nguồn |
|---|---|---|
| Instagram Reels | Caption 2.200 ký tự (tính cả hashtag, @). **Tối đa 5 hashtag mỗi post/Reel** (Instagram công bố 18/12/2025; tài liệu API vẫn ghi 30, nhưng nên viết theo 5). Tối đa 20 @mention | Instagram Help "Use hashtags", Meta IG User Media API (trích theo [Instapect](https://instapect.com/blog/do-hashtags-work-on-instagram), [PostDaily](https://www.postdaily.app/limits/instagram)) |
| YouTube Shorts | Tiêu đề ≤ 100 ký tự. Mô tả ≤ 5.000 ký tự. Hashtag: **trên 60 thì YouTube bỏ qua toàn bộ hashtag của video**; tối đa 3 hashtag trong mô tả được hiện cạnh tiêu đề | [YouTube Help 10059070](https://support.google.com/youtube/answer/10059070), [57404](https://support.google.com/youtube/answer/57404), [6390658](https://support.google.com/youtube/answer/6390658) (theo kết quả tìm kiếm, mình chưa mở từng trang) |
| Chung OneUp | Mô tả phải có dòng ghi công CC BY 4.0 và link HowToLiveBetter (rule attribution). Bản Reels dùng ≤ 5 hashtag; bản Shorts dùng 3 hashtag ở đầu mô tả | rule đã chốt |

### e5. Âm lượng, watermark, reupload

- **Âm lượng:** cả Instagram và YouTube đều **không công bố yêu cầu LUFS cho Reels/Shorts** (mình không tìm được trang chính thức nào). Giữ chuẩn nội bộ −14 LUFS ±1, peak ≤ −0,5 dBFS (rule-4, `build-final.py`), dùng chung một file master cho cả 3 nền tảng.
- **Watermark:** Instagram tuyên bố Reels có watermark/logo của app khác sẽ **ít được đề xuất** (Reels tab, Explore). Nguồn: thông báo @creators năm 2021 ([The Verge 9/2/2021](https://www.theverge.com/2021/2/9/22274332/instagram-algorithm-tiktok-watermark-recommendation-software-best-practices)) và trang Recommendation Guidelines help.instagram.com/1632656957065371 (trích lại qua bài viết bên thứ ba, mình chưa mở trực tiếp). Từ 30/4/2026 Instagram còn hạn chế đề xuất cho tài khoản chuyên đăng lại nội dung ([TechCrunch](https://techcrunch.com/2026/04/30/instagram-restricts-reach-of-content-aggregators-in-new-crackdown/)). YouTube: nội dung đăng lại không có đóng góp gốc thì không đủ điều kiện kiếm tiền (YPP reused content, [Help 56100](https://support.google.com/youtube/answer/56100)).
- **Hệ quả cho OneUp:** **không bao giờ** tải video từ TikTok về (có logo nảy và @handle) để đăng lên Reels/Shorts. Luôn đăng từ file master render ra `final/out/*.mp4`.

### e6. Checklist ffmpeg cắt bản Reels/Shorts từ final clip-04 (chạy khi đã có final v18 được duyệt; lượt này KHÔNG chạy)

```bash
F=content/clips/clip-04-gap-sach-tu-kiem/final/out/clip-04-final.mp4   # phải là bản final đã qua gate 2, không phải bản TikTok tải về
O=media/clips/clip-04/xpost; mkdir -p $O                                 # media/ gitignored, khai MANIFEST.json

# 1. Kiểm thông số master: 1080x1920, 30fps, h264 yuv420p, AAC 48 kHz; độ dài ≤ 180s (Shorts), ≤ 180s (Reels để còn được đề xuất)
ffprobe -v error -show_entries stream=codec_name,width,height,r_frame_rate,pix_fmt,sample_rate,bit_rate:format=duration -of default=nw=1 "$F"

# 2. Loudness (rule-4): mục tiêu −14 ±1 LUFS, peak ≤ −0,5 dBFS (lệch thì sửa ở build-final, không normalize lại ở đây)
ffmpeg -hide_banner -i "$F" -af loudnorm=I=-14:TP=-1.5:LRA=11:print_format=summary -f null - 2>&1 | tail -12

# 3. Soát vùng an toàn: phủ đỏ vùng UI của Reels + Shorts lên 4 mốc (0.5s hook, 1/3, 2/3, end card), đọc mắt xem chữ/mặt có bị che không
for t in 0.5 20 45 66; do ffmpeg -v error -y -ss $t -i "$F" -frames:v 1 -vf \
"drawbox=x=0:y=0:w=iw:h=288:color=red@0.35:t=fill,drawbox=x=0:y=1248:w=iw:h=672:color=red@0.35:t=fill,\
drawbox=x=0:y=288:w=65:h=960:color=red@0.35:t=fill,drawbox=x=888:y=288:w=192:h=960:color=red@0.35:t=fill" $O/safe-$t.png; done

# 4. Số cắt/hit để ghi báo cáo (đối chiếu mục a1)
ffmpeg -hide_banner -nostats -i "$F" -vf "select='gt(scene,0.15)',showinfo" -an -f null - 2>&1 | grep -o 'pts_time:[0-9.]*'

# 5. Bản Shorts + Reels: master đạt bước 1 thì chỉ remux (không encode lại, không mất chất lượng), đưa moov lên đầu file
ffmpeg -v error -y -i "$F" -c copy -map_metadata -1 -movflags +faststart $O/clip-04-shorts.mp4
ffmpeg -v error -y -i "$F" -c copy -map_metadata -1 -movflags +faststart $O/clip-04-reels.mp4
#   Nếu đăng Reels qua API mà bitrate > 25 Mbps hoặc file > 300MB thì mới encode lại:
#   ffmpeg -i "$F" -c:v libx264 -crf 18 -maxrate 20M -bufsize 40M -pix_fmt yuv420p -r 30 -c:a aac -b:a 192k -ar 48000 -movflags +faststart $O/clip-04-reels.mp4
#   (master hiện tại ~4 Mbps video, 192 kbps audio: không cần)

# 6. Reels cover: dùng cover.png 1080x1920; soát vùng lưới 3:4 (giữa 1080x1440) và vuông 1:1 (giữa 1080x1080)
C=content/clips/clip-04-gap-sach-tu-kiem/final/cover.png
ffmpeg -v error -y -i $C -vf crop=1080:1440:0:240 $O/cover-grid-3x4.png
ffmpeg -v error -y -i $C -vf crop=1080:1080:0:420 $O/cover-grid-1x1.png
ffmpeg -v error -y -i $C -vf crop=1080:1350:0:285 $O/cover-4x5.png

# 7. Shorts thumbnail: mặc định chọn frame trong app. Chỉ khi kênh có YPP và upload được ảnh riêng: render cover ở 2160x3840
#    (đừng upscale từ 1080x1920 nếu render lại được; tối thiểu cao 640px nên 1080x1920 vẫn hợp lệ)
ffmpeg -v error -y -i $C -q:v 2 $O/shorts-thumb-1080x1920.jpg

# 8. Phụ đề rời: nếu PR #1 được duyệt thì đính kèm .srt khi upload YouTube (Studio → Subtitles)
# 9. Trước khi giao: không có logo/handle TikTok trong bất kỳ frame nào (frame mốc ở bước 3); mô tả có dòng ghi công CC BY 4.0
```

Mỗi file sinh ra là media, không đưa vào git. Lưu ở `media/` và khai vào `media/MANIFEST.json` (L-023).

## Nguồn

- Dữ liệu nội bộ: `research/trends/2026-10-16..20/apify/{clips.json,vtt/}`, `research/trends/2026-10-20/social-research/{scene-cuts.txt,tiktok-page-stats-2026-10-20.json}`, `/tmp/vids/*.mp4` + `fr_*/sheet.jpg` (8 clip có sẵn trên box), `content/clips/clip-04-gap-sach-tu-kiem/final/out/clip-04-final.mp4`.
- TikTok Ads Help, Creative best practices for performance ads (cập nhật 6/2025): https://ads.tiktok.com/help/article/creative-best-practices
- Dost & Huang (2026), Jump Cut Editing Style and Transition Frequency…, Marketing Trends Congress: https://archives.marketing-trends-congress.com/2026/pages/PDF/paper_professor_DOST_HUANG.pdf
- Google Ads Help, video ad specs + safe zones: https://support.google.com/google-ads/answer/13547298
- YouTube Help: 15424877 (Shorts 3 phút), 72431 (thumbnail), 12779649 (upload); YouTube Blog 24/7/2026 (custom thumbnail Shorts)
- Meta Ads Guide Reels safe zone (trích qua solidlabs.com, anglr.co); Instagram Help hashtags/Reels length (trích qua instapect.com, postdaily.app, clapr.app)
- The Verge 2021 (watermark), The Verge 2025 (lưới 3:4), TechCrunch 30/4/2026 (aggregator)
