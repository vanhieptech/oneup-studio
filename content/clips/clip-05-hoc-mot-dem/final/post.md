---
title: "Bộ final đăng clip-05 v4 «Học dồn một đêm» (TikTok · Threads · Instagram Reels · YouTube Shorts)"
date: 2026-10-22
source: "oneup-studio · lời khoá content/clips/clip-05-hoc-mot-dem/script-v4-LOCKED.md · HowToLiveBetter phần 23 mục 15"
id: clip-05.post
type: post-package
template: post-package v1 (rule-53, DL-045) + bản đa nền tảng (W-20)
status: bộ final v4, chờ Rule Reviewer soát phần chữ + Hiệp duyệt. CHƯA ĐĂNG.
video: "final/clip-05-v4-tiktok.mp4 (TikTok) · final/clip-05-v4-reels.mp4 (Reels, YouTube Shorts, Threads)"
cover: "final/cover.png (1080×1920) · final/cover-1080x1350.png (IG feed, Threads)"
hashtags: ["#hoctap", "#onthi", "#studytok", "#cachhoc"]
tags: [clip-05, post, tiktok, threads, instagram, youtube-shorts, w-20, final, dark]
---
# Bộ final đăng clip-05 v4 «Học dồn một đêm»

> **Bộ final, chưa đăng.** Không đăng, không lên lịch, không đăng nhập tài khoản nào. Hiệp tự đăng tay sau khi Rule Reviewer soát đạt và Hiệp duyệt.
> Claim chỉ lấy từ `script-v4-LOCKED.md` + `fact-package.md` + `final/script-final.md` (Fact lock). Trend: `final/trend-signals.md` (@ng__phanh, số chụp 20/10/2026).

Mục 1–12 là gói TikTok (rule-53). Mục 13–15 là Threads, Instagram Reels, YouTube Shorts. Mục 16 là thumbnail. Mục 17 là tự soát.

## 1. File video
```
TikTok:          content/clips/clip-05-hoc-mot-dem/final/clip-05-v4-tiktok.mp4 · 55,03s (1651 frame) · 1080×1920 · 30fps · H.264 High + AAC 48 kHz mono · -14,2 LUFS · peak -0,8 dBFS · 32,2 MB
Instagram Reels: content/clips/clip-05-hoc-mot-dem/final/clip-05-v4-reels.mp4 · 55,54s (1666 frame) · 1080×1920 · 30fps · H.264 High + AAC 48 kHz mono · -14,2 LUFS · peak -0,8 dBFS · 32,8 MB · khung cover 0–0,500s (15 frame = cover.png), giọng/phụ đề lùi +0,500s (L-083)
YouTube Shorts:  clip-05-v4-reels.mp4 (cùng file với Reels)
Threads:         clip-05-v4-reels.mp4 (cùng file với Reels)
Bản xem nhanh:   clip-05-v4-light.mp4 · 55,03s (1651 frame) · 540×960 · 30fps · H.264 High + AAC 48 kHz mono · -14,2 LUFS · peak -0,8 dBFS · 4,0 MB — chỉ để xem, không đăng
Mac:             ~/me/projects/oneup-studio/media/clips/clip-05-hoc-mot-dem/ (3 file trên)
```
- Số đo bằng ffprobe + ebur128 trên box (22/10/2026, giờ VN). File không có nhạc (luật 21), chỉ giọng + SFX + ambience.
- MP4 không nằm trong git. Không file nào có logo TikTok.
- Nền cảnh xám #E4E4DF, chữ khoá phụ đề ô mực (H1/H2 đã chốt). Nhân vật bản reels ở x .79.
- Bản reels dùng layout phụ đề riêng `video.layout="reels"` (như clip-04): phụ đề ở ô hẹp bên trái x 60–640, y ≈1000–1240, tiêu đề lời kể từ y 300. Đạo cụ nằm dưới vùng đó được dời bằng `pipeline/scripts/clip-05-reels-plan-v4.py` → `final/out/plan-reels.json` (layoutCheck sạch).


## 2. Chữ trên cover (≤ 40 ký tự)
```
HỌC DỒN 1 ĐÊM? 1 TUẦN SAU CÒN GÌ?
```
Render phương án A từ template `Cover.tsx` (props `final/cover/cover-a.props.json` = `spec.json → cover`, theme dark, tag `#05 HỌC ĐÚNG CÁCH`, hàng 2 là pill, chibi nghĩ ngợi). Không lấy frame video (luật 54, L-020).
Tiêu đề chung (dòng đầu caption TikTok/Reels): **Học dồn một đêm, sáng thi vẫn làm được đề, nhưng quên nhanh.**
Frame cover: **0s**. TikTok: tải `final/cover.png` lên riêng (bản TikTok không có khung cover). Reels · YouTube Shorts · Threads: chọn khung 0s của `clip-05-v4-reels.mp4` (= cover.png, ≤0,5s, L-083).

## 3. Caption / tiêu đề TikTok (VI)
```
Học dồn một đêm, sáng thi vẫn làm được đề, nhưng quên nhanh.
Cách thử: cùng ba tiếng đó, chia ra ba ngày, mỗi ngày một tiếng, mỗi buổi gấp sách tự kiểm.
Còn bạn, môn sắp thi còn cách mấy hôm? Comment số hôm nha.
Nghiên cứu: Rawson & Kintsch (2005); Cepeda và cộng sự (2006).
Giọng trong video là giọng AI tổng hợp (F5-TTS).
Thông tin tham khảo, không thay thế tư vấn chuyên gia
Nội dung dựa trên «Cẩm nang sống đáng giá» – chuanman2707, CC BY 4.0 – https://chuanman2707.github.io/HowToLiveBetter/
#hoctap #onthi #studytok #cachhoc
```
1 câu hook (khẳng định) · 1 câu cách làm · 1 CTA (câu hỏi duy nhất) · nguồn · công bố giọng AI · câu an toàn · credit nguyên văn như end card · hashtag. Không số nào ngoài năm của nguồn và «ba» trong cách làm. Không emoji.

## 4. Hashtag (4: rộng / ngách / VN)
```
#hoctap #onthi #studytok #cachhoc
```
- `#hoctap`: thẻ VN rộng (đã dùng clip-01..04).
- `#onthi`: đúng chủ đề ôn thi, và là thẻ của video trend @ng__phanh (`final/trend-signals.md`, bỏ #fyp #deadline #hoc).
- `#studytok`: thẻ học tập đã dùng ở clip-04.
- `#cachhoc`: thẻ ngách «cách học», đã có trong nháp clip-04.
Không #fyp/#viral/#xuhuong.

## 5. Từ khoá SEO (đã lồng trong caption)
```
học dồn một đêm, ôn thi, quên nhanh, chia ra ba ngày, gấp sách tự kiểm, cách học
```

## 6. Bình luận ghim
```
Thử đếm xem: môn sắp thi của bạn còn cách mấy hôm? Comment số hôm nha.
```

## 7. Giờ đăng đề xuất (giờ VN)
```
Mặc định 19:00 (giờ VN), theo luật 32 (thứ Hai/Tư/Sáu, kênh mới chưa có Analytics). Hiệp tự đăng tay, không lên lịch tự động. Ngày cụ thể do Hiệp xếp theo theme-map (clip-05 = DARK).
```

## 8. Âm thanh
```
Thêm 1 track trong app lúc đăng (bài nào cũng được, không bắt buộc Commercial Music Library; Hiệp 21/10/2026, L-083). Mood theme DARK: lofi chậm, hơi trầm, đêm khuya học bài, piano/Rhodes + beat nhẹ, không lời, 75–90 BPM, không drop. Âm lượng: giọng gốc 100%, nhạc 5% (tối đa 8%). Không dùng nhạc nền của video trend gốc (trend-signals.md). Trong file không có nhạc (luật 21); SFX + ambience đã mix sẵn.
```

## 9. Checklist cài đặt khi đăng
```
[ ] Bật "Nội dung do AI tạo" (AI-generated content): ON
[ ] Dòng công bố trong caption: "Giọng trong video là giọng AI tổng hợp (F5-TTS)."
[ ] Cho phép bình luận: ON · Duet: ON · Stitch: ON
[ ] Ai có thể xem: Mọi người (Everyone)
[ ] Vị trí: không gắn
[ ] Nội dung thương mại / quảng cáo: OFF (giọng F5 CC-BY-NC-SA, DL-035)
[ ] Thêm vào danh sách phát (playlist): "Học đúng cách"
[ ] Ảnh bìa: final/cover.png (1080×1920, template A, «Tải ảnh bìa lên», không chọn frame video)
[ ] Ghim bình luận ở mục 6 ngay sau khi đăng
```

## 10. Ghi nguồn (luật 13)
```
Nội dung dựa trên «Cẩm nang sống đáng giá» – chuanman2707, CC BY 4.0 – https://chuanman2707.github.io/HowToLiveBetter/
Đã chuyển thể từ HowToLiveBetter phần 23 mục 15 (học giãn cách) và mục 14 (gấp sách tự kiểm). Giấy phép: https://creativecommons.org/licenses/by/4.0/
Nghiên cứu: Rawson & Kintsch (2005), J Educ Psychol 97(1):70–80 · Cepeda et al. (2006), Psychol Bull 132(3):354–80, PubMed 16719566 · Yang et al. (2021), Psychol Bull 147(4) · Dunlosky et al. (2013), Psychol Sci Public Interest 14(1), PubMed 26173288.
Trend: @ng__phanh · TikTok (chỉ dựng lại khung + chữ ở 0–1,6s, không dùng footage/nhạc gốc).
```
Dòng 1 nguyên văn như end card, đặt trong caption. Dòng 2 («đã chuyển thể» + link giấy phép) đặt ở **bình luận thứ 2** trên TikTok và Reels, và ở **cuối mô tả YouTube**.

## 11. Series / playlist
```
Học đúng cách (#5)
```

## 12. Nhãn AI (luật 46)
```
Giọng nhân vật trong video là giọng AI tổng hợp (F5-TTS, giọng Thái Sơn). Hình: nhân vật và cảnh vẽ bằng code (video-engine), không dùng ảnh/video AI.
```
- Bật nhãn AI trên cả 4 nền tảng (TikTok mục 9, Reels mục 14, YouTube mục 15, Threads mục 13).

## 13. Threads (bài text kèm video, ngắn)
```
Học dồn một đêm, sáng thi vẫn làm được đề, nhưng quên nhanh.

Một nghiên cứu: đọc một bài hai lần liền thì kiểm tra ngay hơn người đọc một lần, hai ngày sau thì không. Ai đọc lần hai cách một tuần thì vẫn hơn.

Cách thử: cùng ba tiếng đó, chia ra ba ngày, mỗi buổi gấp sách tự kiểm.

Còn bạn, môn sắp thi còn cách mấy hôm?

Thông tin tham khảo, không thay thế tư vấn chuyên gia
Nội dung dựa trên «Cẩm nang sống đáng giá» – chuanman2707, CC BY 4.0 – https://chuanman2707.github.io/HowToLiveBetter/
```
- Đính kèm `final/clip-05-v4-reels.mp4`. Thumbnail: khung 0s của bản reels. Topic gợi ý: «Học tập» (1 topic). Không hashtag trong thân bài.
- Độ dài: 496 ký tự (giới hạn 500). Chỉ 1 câu hỏi, cũng là CTA duy nhất.
- Câu Rawson & Kintsch bám đúng lời khoá b03.

## 14. Instagram Reels (caption + hashtag)
```
Học dồn một đêm, sáng thi vẫn làm được đề, nhưng quên nhanh.

Cách thử: cùng ba tiếng đó, chia ra ba ngày, mỗi ngày một tiếng, mỗi buổi gấp sách tự kiểm.

Còn bạn, môn sắp thi còn cách mấy hôm? Comment số hôm nha.

Nghiên cứu: Rawson & Kintsch (2005); Cepeda và cộng sự (2006).

Giọng trong video là giọng AI tổng hợp (F5-TTS).
Thông tin tham khảo, không thay thế tư vấn chuyên gia
Nội dung dựa trên «Cẩm nang sống đáng giá» – chuanman2707, CC BY 4.0 – https://chuanman2707.github.io/HowToLiveBetter/

#hoctap #onthi #studytok #cachhoc
```
- Video: `final/clip-05-v4-reels.mp4`. Ảnh bìa Reels: khung 0s. Lưới 4:5: `final/cover-1080x1350.png` (cắt y 265–1615).
- Nhãn AI: bật «AI info / nhãn AI» nếu app hỏi.

## 15. YouTube Shorts
Tiêu đề (65 ký tự, không hashtag, không câu hỏi):
```
Học dồn một đêm vẫn làm được đề nhưng quên nhanh: chia ra ba ngày
```
Mô tả:
```
Học dồn một đêm, sáng thi vẫn làm được đề, nhưng quên nhanh.

Cách thử: cùng ba tiếng đó, chia ra ba ngày, mỗi ngày một tiếng, mỗi buổi gấp sách tự kiểm.
Một nghiên cứu cho sinh viên đọc một bài hai lần liền: kiểm tra ngay thì hơn người đọc một lần, hai ngày sau thì không còn hơn. Ai đọc lần hai cách một tuần thì hai ngày sau vẫn hơn.
Khi gom 317 thí nghiệm lại, các nhà nghiên cứu thấy muốn nhớ càng lâu thì khoảng cách giữa các lần ôn càng phải dài.

Còn bạn, môn sắp thi còn cách mấy hôm? Comment số hôm nha.

Nghiên cứu:
- Rawson & Kintsch (2005), Journal of Educational Psychology: https://doi.org/10.1037/0022-0663.97.1.70
- Cepeda et al. (2006), Psychological Bulletin: https://pubmed.ncbi.nlm.nih.gov/16719566/

Giọng trong video là giọng AI tổng hợp (F5-TTS).
Thông tin tham khảo, không thay thế tư vấn chuyên gia
Nội dung dựa trên «Cẩm nang sống đáng giá» – chuanman2707, CC BY 4.0 – https://chuanman2707.github.io/HowToLiveBetter/
Đã chuyển thể từ HowToLiveBetter phần 23 mục 15 và mục 14. Giấy phép: https://creativecommons.org/licenses/by/4.0/

#Shorts #hoctap #onthi
```
- **Khi tải lên: BẬT nhãn «Nội dung bị biến đổi hoặc tổng hợp» (altered or synthetic content)** (giọng AI tổng hợp).
- Video: `final/clip-05-v4-reels.mp4`. Thumbnail: khung 0s (cover). Playlist: «Học đúng cách».

## 16. Thumbnail
```
TikTok (tải lên riêng):           content/clips/clip-05-hoc-mot-dem/final/cover.png        1080×1920 · md5 bf27abd3… = final/cover/cover-a.png (template A Cover.tsx, props cover-a.props.json)
Reels · YouTube Shorts · Threads: khung 0s của final/clip-05-v4-reels.mp4 = cover.png (15 frame, SSIM 0,999)
IG feed/lưới hồ sơ:              content/clips/clip-05-hoc-mot-dem/final/cover-1080x1350.png 1080×1350 · cắt 4:5 từ cover.png (y 265–1615)
```
- Chữ trên ảnh: `#05 HỌC ĐÚNG CÁCH` · `HỌC DỒN 1 ĐÊM?` · `1 TUẦN SAU CÒN GÌ?` (pill) · `OneUp.`. Theme DARK, khớp video.
- Bản 1080×1350 không mất chữ nào: tag, hai hàng hero, logo và nhân vật nằm trọn trong khung.

## 17. Tự soát
| # | Tiêu chí | Kết quả |
|---|---|---|
| T1 | Tiêu đề ≤ 70 ký tự | Tiêu đề chung 60 ký tự · YouTube 65 ký tự |
| T2 | Hashtag | TikTok 4 thẻ (3–5) · Reels 4 · YouTube 3 ở cuối mô tả · Threads 0 |
| T3 | Credit CC BY 4.0 nguyên văn + câu an toàn ở cả 4 bản | Có ở mục 3, 13, 14, 15 (mô tả). End card trong video có câu an toàn, 4 nguồn, trend và credit |
| T4 | Không ám chỉ tác giả xác nhận/bảo trợ | Không có «xác nhận / bảo trợ / tài trợ / endorse» |
| T5 | Chỉ nói điều script khoá đã nói | Hook ← câu 1 + «Một câu cả clip» trong script khoá («quên nhanh»). Cách thử ← câu 5. CTA ← câu 8. Threads/YouTube câu nghiên cứu ← câu 3 và 6. Không %, không số ngày giãn cụ thể, không «học dồn vô dụng», không số share |
| T6 | Mỗi bản 1 CTA, 1 câu hỏi | TikTok 1 · Threads 1 · Reels 1 · YouTube mô tả 1, tiêu đề 0 |
| T7 | Không lên lịch / đăng tự động | Hiệp tự đăng tay |

### Việc còn mở (chờ Hiệp quyết)
- b03: cột thứ ba («Lần 2 cách 1 tuần») màu mực thay vì xanh, để giữ bảng màu thương hiệu. Ràng buộc FLUX vẫn đúng: mỗi cột chỉ so với cột xám, không số.
- Bìa sách Sinh màu xám nhạt thay vì xanh lá (giữ bảng màu thương hiệu).

### Đã chốt (Hiệp, Rule Reviewer chuyển lời 22/10/2026 08:47 giờ VN)
- H1 nền cảnh: xám #E4E4DF như clip-03 (sàn #D2D1CA, đậm hơn một bậc), khung ngoài mực = DARK. Bìa cũng nền xám #E4E4DF.
- H2 chữ khoá phụ đề: ô mực như clip-04 (bỏ cam #FF5A36, không còn `caption_accent`).
- Bản reels: nhân vật dời x .76 → .79 để ô phụ đề hẹp (x 60–640) không chạm tóc (L-033).
