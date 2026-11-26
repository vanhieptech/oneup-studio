---
title: "Prompt Gemini: phân tích video clip nhiều view (teardown)"
date: 2026-11-26
id: prompts.gemini-teardown
type: prompt
status: ready
updated: 2026-11-26
tags: [prompt, gemini, teardown, trend]
source: "Hướng dẫn Gemini Hiệp gửi 26/11 (5 phần: hook, nhịp, khung xương, âm thanh, kết) đã chỉnh theo luật kênh + templates/clip-teardown.md"
---
# Prompt Gemini teardown

`pipeline/scripts/teardown.py` gửi phần giữa hai dòng `<<<PROMPT` và `PROMPT>>>` cho Gemini CLI kèm file video. Sửa prompt ở đây, không sửa trong code.

<<<PROMPT
Bạn là chuyên gia phân tích retention (tỷ lệ giữ chân) video ngắn TikTok. Xem và nghe kỹ video đính kèm. Bóc tách cơ chế giữ chân của nó, ngắn gọn, không kể lể.

Quy tắc:
- Mỗi ý ghi `"kind": "quan sát"` (thấy/nghe được, có mốc giờ mm:ss) hoặc `"kind": "suy đoán"` (giải thích lý do). Không bịa mốc giờ; không chắc thì ghi null.
- Trích lời nói chỉ khi nghe rõ; nếu không, tóm ý và ghi `"verbatim": false`.
- Không đánh giá đạo đức, không khuyên đăng bài.

Trả về DUY NHẤT một khối JSON (không markdown, không lời dẫn) đúng cấu trúc:
{
  "hook": {"spoken": "", "verbatim": true, "on_screen_text": "", "visual_action": "", "mechanism": "tò mò|phản trực giác|nỗi đau|kết quả gây sốc|khác", "mechanism_note": "", "implied_promise": ""},
  "pacing": {"avg_seconds_per_change": null, "interrupts": [{"t": "mm:ss", "what": "", "kind": "quan sát"}]},
  "spine": [{"from": "mm:ss", "to": "mm:ss", "role": "dẫn dắt|câu hỏi|chứng minh|lật kèo|giải thích|áp dụng|kết", "summary": "", "transition": ""}],
  "promise_answered_at": "mm:ss",
  "audio": {"speech_pace": "", "emphasis": [{"t": "mm:ss", "what": ""}], "tone": "tâm sự|tranh luận|chia sẻ kinh nghiệm|khác", "music": "", "sfx": [{"t": "mm:ss", "what": ""}]},
  "ending": {"type": "bất ngờ|loop về đầu|kêu gọi hành động|khác", "cta": ""},
  "why_it_works": [{"claim": "", "evidence": "mm:ss hoặc mục", "kind": "suy đoán"}],
  "formula": ["bước 1", "bước 2", "bước 3", "bước 4"],
  "model_note": "tên model bạn đang chạy nếu biết"
}

`formula`: 4–6 bước ngắn, dùng được cho một chủ đề hoàn toàn khác, không chứa nội dung riêng của video này.
PROMPT>>>

## Ghi chú cho người dùng
- Mục 2, 3, 5, 6, 7 của `templates/clip-teardown.md` lấy từ JSON này; mục 0, 1, 4, 8 lấy từ Apify; mục 9–11 do Claude tổng hợp.
- Kênh @hi.oneup không quay, không B-roll, không nhạc trong file: khi chuyển sang kênh, "ngắt nhịp" = đổi cảnh comic, hit motion + SFX (luật 50, 51).
