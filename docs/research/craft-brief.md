---
title: "Craft brief: một trang hướng dẫn nghề lúc viết lời"
date: 2026-11-26
id: research.craft-brief
type: research
status: ready
updated: 2026-11-26
tags: [script, craft, writing, make-video]
source: "Rút từ L-089, L-094, L-096, L-099, L-103–L-107, script-prompt-principles.md (15/10, bản 45s đã cũ) và quy tắc văn nói trong hướng dẫn Gemini Hiệp gửi 26/11 (đã chỉnh theo luật kênh)"
---
# Craft brief (đọc lúc viết; luật đầy đủ để dành cho lúc kiểm)

Lúc viết lời chỉ mở 4 thứ: trang này · bảng dịch thuật ngữ của chủ đề (`research/explainers/<chủ-đề>.md`, nếu có) · kho cụm từ `resources/vn-spoken/phrase-bank.md` · 2–3 mẫu giọng (voice memo của Hiệp ở `content/voice-profile.md` §4 khi có; phụ đề creator thật ở `research/hooks/2026-11-12-storytelling-hooks-vn/raw/*.vtt`; script đã duyệt `content/archive/clip-0*/final/script-final.md`). Không đọc lessons/rules lúc này: quá nhiều luật cùng lúc làm lời gượng (L-106).

## A. Trước khi viết một chữ
1. **Một câu tóm ý:** người xem đang khổ chuyện gì → clip hứa gì → trả lời bằng gì.
2. **Bảng khung mạch** (L-107): mỗi beat một câu + vai trò (chuyện → câu hỏi → trả lời → giới hạn → áp dụng → kết). Đọc riêng cột này phải ra một lập luận nối bằng «vì / nên / vậy / nhưng». Đứt ở đâu thì sửa khung, chưa viết lời.
3. Lời hứa ở hook được trả lời **ngay beat sau**; không chen câu trend hay ý phụ vào giữa (L-094, L-107). Cuối bài quay lại nỗi lo ở hook.

## B. Hook
4. Hook là **mở đầu một câu chuyện**: ai, đang muốn gì, khoảnh khắc hụt, câu gợi chuyện gì xảy ra tiếp (L-103). Không dùng ngôn ngữ nghiên cứu («theo một thí nghiệm», «trung bình người ta») trong hook.
5. Có **cái giá người xem thấy đáng bận tâm** và một chỗ bất ngờ trong 3 giây đầu; viết được câu «vì sao người lướt sẽ dừng» (L-096, L-104). Kiểu hook khác 2 clip trước (`logs/hook-moves.md`).

## C. Viết như nói
6. **Viết liền một hơi như đang kể cho bạn thân**, rồi mới cắt thành beat. Không viết từng ô trong bảng (đó là nguồn của câu rời).
7. **Một câu một ý**, nối câu bằng nguyên nhân hoặc kết quả thật («tại vì», «nên», «mà», «rồi»), không ghép các ý khác chủ ngữ bằng dấu phẩy (L-106). Không có hai câu cộc liền nhau (L-096). Không có quota chữ: đủ ý thì thôi, tổng < 300s (L-099).
8. **Từ miệng, không từ sách:** hỏi «có ai nói câu này ngoài đời không» với từng câu (L-105). Tránh cụm văn chương («im bặt», «cứ nghĩ mãi», «lời dặn ấy»). Danh sách hay gặp: `resources/vn-spoken/bookish.tsv` (`check-rules --bookish`).
9. **Mọi từ trỏ phải chỉ tới được cái gì:** «lý do» là lý do gì, «cách này» là cách nào (L-098, L-106). Không chèn câu tự giễu hay bình luận chỉ để tạo giọng.
10. Từ đệm (nha, á, hông, luôn…) lấy theo giọng thật, tối đa 1 mỗi câu, không rải theo danh sách (voice-profile §3c). Tiếng Anh chen 1–3 từ mỗi clip.
11. Một ngôi kể xuyên suốt; «bạn» chỉ khi khung chuyện làm việc đó tự nhiên (L-089).

## D. Dẫn chứng
12. Dẫn chứng **nảy ra từ chuyện**, có câu dẫn, nói được ai/nguồn nào, so A với B, kết quả theo đúng mức của nguồn (L-096, L-103). Cấm «nhiều nghiên cứu thấy…». Con số đọc như nói («chín mươi sáu người»).
13. Ví dụ đời thường, cụ thể, dễ hình dung; không lấy môn học làm ví dụ (L-087). Chuyện thật của Hiệp ưu tiên (story-bank); chi tiết hài được phép dựng (luật 67), số liệu thì không.

## E. Kết
14. Một CTA, câu hỏi người xem trả lời được bằng chính chuyện của họ. Không xin like/follow.
15. Ngắt nhịp mỗi vài giây bằng **hình**, không bằng chữ: @hi.oneup = đổi cảnh comic, hit motion + SFX (luật 50, 51); @vanhiep.tech = overlay/cutaway. Ghi ý hình ở cột riêng, lời đọc vẫn liền mạch.

## Sau khi viết
`check-rules --draft` (gồm `--bookish`) → `script-polish` → make-video §4b (reviewer độc lập). Checker PASS không chứng minh lời hay (L-098); đọc to là cổng thật.
