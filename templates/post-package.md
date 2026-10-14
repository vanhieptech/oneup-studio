---
id: clip-01.post
type: post-package
template: post-package v1 (rule-53, DL-045)
status: sẵn sàng đăng sau khi Hiệp xác nhận mục [CẦN HIỆP XÁC NHẬN] trong script-final.md
updated: 2026-10-14
tags: [clip-01, post, tiktok, week-1]
---
# Gói đăng TikTok: <clip-NN "<tên>">

## 1. File video
```
Đường dẫn: content/clips/clip-01-implementation-intention/final/out/clip-01-final.mp4
Thời lượng: 60.7s · 1080×1920 (9:16) · 30fps · H.264 + AAC 48 kHz · −14 LUFS
```

## 2. Chữ trên cover (≤ 40 ký tự)
```
MAI HỌC → NẾU–THÌ
```
Cover: **template A** (luật 54, DL-046), render từ `video-engine/src/composition/Cover.tsx`, props lấy từ `spec.json → cover` (`final/cover/cover-a.props.json`). File: `final/cover.png`. Frame cover: **0s** (ảnh bìa tải lên riêng, không lấy frame video). Lúc đăng, chọn "Tải ảnh bìa lên" → `cover.png`.

## 3. Caption / tiêu đề TikTok (VI)
```
Kế hoạch học của bạn có phải là… "mai học"? 😅
Thử viết sẵn một câu nếu… thì… (tâm lý học gọi là ý định thực hiện): mấy giờ, ở đâu, gặp gì, thì làm gì.
Ví dụ: 9h tối, gập laptop → mở một bài listening.
Vì sao hiệu quả: bạn quyết sẵn lúc còn tỉnh táo, tới lúc mệt khỏi phải cãi với chính mình.
94 kiểm nghiệm độc lập: người viết kiểu này đạt mục tiêu nhiều hơn rõ (hiệu ứng vừa tới lớn). Đa số nghiên cứu làm trên sinh viên và thói quen sức khoẻ.
Lỗi hay gặp: "rảnh thì học". Rảnh không phải tín hiệu, hãy dùng một giờ, một chỗ, hoặc một việc vừa xong.
Chỉ hiệu quả với việc bạn thật sự muốn. Viết mất 1–2 phút thôi.
Mẹo học tiếng Anh, chống trì hoãn, xây thói quen học mỗi ngày 👇 Câu nếu–thì của bạn là gì?
Giọng nhân vật là giọng AI tổng hợp (F5-TTS). Nội dung chuyển thể từ HowToLiveBetter (CC BY 4.0).
#learnontiktok #hoctap #hoctienganh #quanlythoigian #phattrienbanthan
```
Khoảng 800 ký tự (giới hạn 2200). Viết theo ngôi "bạn", không khẳng định chuyện đời thật nào của Hiệp. Emoji chỉ dùng trong caption, không có trong video (luật no-emoji áp dụng cho video).

## 4. Hashtag (5: rộng / ngách / VN)
```
#learnontiktok #hoctap #hoctienganh #quanlythoigian #phattrienbanthan
```
- `#learnontiktok`: thẻ rộng, TikTok đẩy cho nội dung giáo dục.
- `#hoctap`, `#phattrienbanthan`: thẻ VN rộng cho học tập và phát triển bản thân.
- `#hoctienganh`: thẻ ngách, đúng ví dụ listening.
- `#quanlythoigian`: thẻ ngách về chống trì hoãn.

Lấy từ danh sách hashtag học tập/năng suất TikTok VN 2026 (fptshop.com.vn, mktsoftware.vn, xgiare.com, tra cứu 14/10/2026). Công thức 1 thẻ chủ đề + 1 thẻ đối tượng + 1 thẻ kỹ năng; khuyến nghị 3–5 thẻ, đúng nội dung. Cố ý bỏ `#fyp`, `#xuhuong`, `#viral` (thẻ spam, không liên quan) và `#toeic` (chi tiết TOEIC của Hiệp chưa xác nhận).

## 5. Từ khoá SEO (đã lồng tự nhiên trong caption)
```
nếu thì, ý định thực hiện, chống trì hoãn, mẹo học tiếng anh, thói quen học mỗi ngày, mai học, tâm lý học
```

## 6. Bình luận ghim
```
Viết câu nếu–thì của bạn ở đây nha 👇 Mẫu: "Nếu 9h tối gập laptop, thì mình mở 1 bài listening." Mình sẽ đọc hết!
```

## 7. Giờ đăng đề xuất (giờ VN)
```
Thứ Năm 15/10/2026, đăng lúc 18:45 (khung 19:00–21:00)
```
Lý do (dữ liệu chung, kênh mới chưa có Analytics):
- ecomobi.com (phân tích hơn 2 tỷ lượt tương tác): 19:00–21:00 thứ Năm là khung tương tác cao nhất tại VN.
- multilogin.com / postify.tech: 19:00–21:00 hiệu quả ổn định mọi ngày, 20:00 là đỉnh.
- taki.vn: đăng sớm khoảng 15 phút trước giờ đỉnh.

Nội dung giáo dục cũng hợp khung 19:30–21:00 (mktsoftware.vn). Sau khoảng 14 ngày thì đổi sang giờ cao nhất trong Analytics → Người theo dõi. Nếu lịch tuần 1 trong theme-map đã định ngày khác, giữ ngày đó nhưng đăng lúc 18:45.

## 8. Âm thanh
```
Thêm nhạc từ TikTok Commercial Music Library (bắt buộc dùng thư viện này, không dùng nhạc trend bản quyền). Mood: lo-fi / chill acoustic, nhẹ, không lời. Âm lượng: giọng gốc 100%, nhạc 5–10%. Trong file không có nhạc (luật 21); SFX + ambience đã mix sẵn.
```

## 9. Checklist cài đặt khi đăng
```
[ ] Bật "Nội dung do AI tạo" (AI-generated content): ON
[ ] Dòng công bố trong caption: "Giọng nhân vật là giọng AI tổng hợp (F5-TTS)."
[ ] Cho phép bình luận: ON · Duet: ON · Stitch: ON
[ ] Ai có thể xem: Mọi người (Everyone)
[ ] Vị trí: không gắn
[ ] Nội dung thương mại / quảng cáo: OFF (giọng F5 CC-BY-NC-SA, không gắn tài trợ, DL-035)
[ ] Thêm vào danh sách phát (playlist): "Làm ít, xong nhiều"
[ ] Ảnh bìa: cover.png
[ ] Ghim bình luận ở mục 6 ngay sau khi đăng
```

## 10. Ghi nguồn (luật 13)
```
Nội dung chuyển thể từ "Cẩm nang sống đáng giá" / HowToLiveBetter (https://github.com/chuanman2707/HowToLiveBetter), CC BY 4.0, đã chuyển thể. Giấy phép: https://creativecommons.org/licenses/by/4.0/ · Nghiên cứu: Gollwitzer & Sheeran (2006).
```
Dòng này dán vào bình luận thứ 2 (hoặc phần mô tả nếu còn chỗ). Caption đã có câu credit ngắn.

## 11. Series / playlist
```
Làm ít, xong nhiều (#1)
```

## 12. Nhãn AI (luật 46)
```
Giọng của Hiệp (nhân vật) trong video là giọng AI tổng hợp (F5-TTS). Nhân vật vẽ bằng code, không dùng ảnh/video AI.
```
