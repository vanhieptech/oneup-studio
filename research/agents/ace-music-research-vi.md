---
title: "Nghiên cứu: ACE-Step 1.5 cho nhạc nền OneUp"
date: 2026-10-19
source: "ACE Music báo cáo tại group Agency Production 19/10/2026, chỉ đọc repo/docs, chưa cài/chạy/tạo nhạc"
id: research.ace-music
type: research
status: reference
updated: 2026-10-19
tags: [ace-step, music, background-music]
---
# Nghiên cứu: ACE-Step 1.5 (ace-step/ACE-Step-1.5)

Nguồn: https://github.com/ace-step/ACE-Step-1.5 và model card https://huggingface.co/ACE-Step/Ace-Step1.5 — báo cáo của agent ACE Music ngày 19/10/2026 (Asia/Saigon), chỉ đọc repo/docs.

## Giấy phép
- Code và model weights đều MIT; model card ghi nhạc tạo ra dùng thương mại được.
- MIT không bảo đảm đầu ra không giống nhạc có bản quyền; cover/repaint nhạc có bản quyền vẫn là rủi ro của người đăng.

## Dùng được cho oneup-studio
- Tạo nhạc nền không lời từ mô tả (10 giây–10 phút/lần), có repaint để làm lại đúng một đoạn chưa ưng, hỗ trợ lời tiếng Việt nếu sau này cần.

## Không hợp lúc này
- Cần GPU tối thiểu khoảng 4–6GB VRAM và Python 3.11–3.12; máy hiện không có GPU nên chưa chạy thực tế được.

## Đề xuất
- Giữ rule hiện tại: không chèn nhạc vào file, Hiệp tự thêm nhạc TikTok khi đăng. ACE Music chuẩn bị prompt/phương án nhạc nền tự tạo ở mức ưu tiên trung bình; chờ Hiệp đổi rule hoặc muốn thử qua cloud GPU/acemusic.ai mới tính tiếp.
