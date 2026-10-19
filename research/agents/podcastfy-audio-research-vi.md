---
title: "Nghiên cứu: Podcastfy cho nội dung OneUp"
date: 2026-10-19
source: "Podcastfy Audio báo cáo tại group Agency Production 19/10/2026, chỉ đọc repo, chưa cài/chạy"
id: research.podcastfy-audio
type: research
status: reference
updated: 2026-10-19
tags: [podcastfy, podcast, tts, transcript]
---
# Nghiên cứu: Podcastfy (souzatharsis/podcastfy)

Nguồn: https://github.com/souzatharsis/podcastfy — báo cáo của agent Podcastfy Audio ngày 19/10/2026 (Asia/Saigon), chỉ đọc repo.

## Giấy phép
- Apache License 2.0 (file LICENSE trong repo): dùng thương mại và phân phối nội dung được; phân phối lại code phải kèm license, giữ copyright/NOTICE và đánh dấu file đã sửa.
- Điều khoản giọng/LLM cloud vẫn theo nhà cung cấp riêng.

## Dùng được cho oneup-studio
- Khung hội thoại 2 người Person1/Person2; tách được bước transcript-only để duyệt/chốt script trước khi làm giọng (khớp rule hiện tại).
- Có abstract TTSProvider + factory nên bọc F5-TTS/VieNeu-TTS thành provider local là khả thi về mặt code.

## Không hợp
- Tối ưu podcast 2–30+ phút; không có storyboard/video/phụ đề đồng bộ cho clip 45–60 giây.
- Không thấy hỗ trợ tiếng Việt chính thức (giọng mặc định en-US; repo ghi audio phi tiếng Anh còn work-in-progress); 5 TTS provider sẵn có đều cloud/online.

## Rủi ro
- Prompt sinh transcript nằm trên LangChain Hub ngoài repo; không có cơ chế trích dẫn, đối chiếu fact hay QA gate tự động — LLM có thể thêm fact ngoài nguồn. Creativity mặc định cao nên phải hạ và tự bổ sung bước đối chiếu item nguồn.

## Đề xuất (chờ Hiệp duyệt, chưa làm)
- Thử 1 item phần 4 ở chế độ transcript-only, tiếng Việt, creativity=0, chỉ dùng số liệu/nguồn trong item và chèn credit CC BY 4.0; đạt đối chiếu mới tính tiếp bước giọng.
