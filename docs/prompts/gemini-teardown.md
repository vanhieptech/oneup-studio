---
title: "Prompt Gemini: phân tích video clip nhiều view (teardown)"
date: 2026-11-26
id: prompts.gemini-teardown
type: prompt
status: ready
updated: 2026-11-26
tags: [prompt, gemini, teardown, trend, viral-dna, arc]
source: "Hướng dẫn Gemini Hiệp gửi 26/11 (5 phần: hook, nhịp, khung xương, âm thanh, kết) đã chỉnh theo luật kênh + templates/clip-teardown.md"
---
# Prompt Gemini teardown

`pipeline/scripts/teardown.py` gửi phần giữa hai dòng `<<<PROMPT
Bạn là chuyên gia phân tích retention (tỷ lệ giữ chân) video ngắn TikTok. Xem và nghe kỹ video đính kèm. Bóc tách "Viral DNA" của nó thành 6 khối, ngắn gọn, không kể lể.

Quy tắc:
- Mỗi ý ghi `"kind": "quan sát"` (thấy/nghe được, có mốc giờ mm:ss) hoặc `"kind": "suy đoán"` (giải thích lý do). Không bịa mốc giờ; không chắc thì ghi null.
- Trích lời nói chỉ khi nghe rõ; nếu không, tóm ý và ghi `"verbatim": false`.
- Không đánh giá đạo đức, không khuyên đăng bài.
- `beats[].role` chỉ dùng một trong: hook, dẫn dắt, câu hỏi, chứng minh, lật kèo, giải thích, áp dụng, kết.
- `arc.skeleton` là khung xương TRỐNG: thay mọi nội dung riêng của video bằng `[...]` có mô tả loại nội dung, ví dụ "[Lời hứa số lượng + chuẩn đáng tin]", để dùng cho một chủ đề hoàn toàn khác.
- `angles`: một góc chuyển thể cho mỗi kênh, chủ đề có thể khác video gốc, KHÔNG chép câu/hình/âm thanh:
  * hi_oneup: comic chibi + motion graphics, 120–180 giây, không quay mặt, không b-roll, không nhạc nền, giọng kể miền Nam xưng mình–bạn.
  * vanhiep_tech: talking-head tech/lập trình/tư duy + overlay diagram, 45–90 giây, cắt layer mỗi 3–5 giây.

Trả về DUY NHẤT một khối JSON (không markdown, không lời dẫn) đúng cấu trúc:
{
  "hook": {"spoken": "", "verbatim": true, "on_screen_text": "", "visual_action": "", "mechanism": "phản trực giác|nỗi đau|tò mò|kết quả sốc|khác", "mechanism_note": "", "implied_promise": ""},
  "beats": [{"from": "mm:ss", "to": "mm:ss", "seconds": 0, "role": "", "retention_function": "beat này giữ người xem bằng cách nào", "summary": "", "transition": "câu/kỹ thuật chuyển sang beat sau"}],
  "promise_answered_at": "mm:ss",
  "winning_points": {"best_metaphor": {"text": "", "t": "mm:ss", "kind": "quan sát"}, "quotable_line": {"text": "", "t": "mm:ss", "verbatim": true}, "interrupts_per_10s": null, "interrupts": [{"t": "mm:ss", "what": "", "kind": "quan sát"}]},
  "algorithmic_triggers": {"comment": [{"what": "", "why": "tranh luận|đồng cảm|hỏi thêm|khác", "kind": "suy đoán"}], "save_share": [{"what": "", "why": "checklist|kiến thức ngách|gửi bạn bè|khác", "kind": "suy đoán"}]},
  "audio": {"speech_pace": "", "emphasis": [{"t": "mm:ss", "what": ""}], "tone": "tâm sự|tranh luận|chia sẻ kinh nghiệm|khác", "music": "", "sfx": [{"t": "mm:ss", "what": ""}]},
  "ending": {"type": "bất ngờ|loop về đầu|kêu gọi hành động|khác", "cta": ""},
  "arc": {"name": "tên ngắn của mạch truyện", "skeleton": ["[...] bước 1", "[...] bước 2", "[...] bước 3", "[...] bước 4"], "hook_mechanism": ""},
  "angles": {"hi_oneup": {"idea": "", "hook": "", "length_s": 150}, "vanhiep_tech": {"idea": "", "hook": "", "length_s": 60}},
  "why_it_works": [{"claim": "", "evidence": "mm:ss hoặc khối", "kind": "suy đoán"}],
  "model_note": "tên model bạn đang chạy nếu biết"
}

`beats`: 4–6 beat theo mốc giờ, phủ toàn video. `arc.skeleton`: 4–6 bước, mỗi bước khớp thứ tự với `beats`.
PROMPT>>>` cho Gemini CLI kèm file video. Sửa prompt ở đây, không sửa trong code.

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
- Khối 1–6 của `templates/clip-teardown.md` lấy từ JSON này; Khối 0 (số liệu) lấy từ Apify / `radar.json`; comment thật (Khối 4) Claude bổ sung từ Apify comments.
- `arc` được `pipeline/arc_library.py` gộp vào thư viện `ARC-NNN` (`research/blueprints/index.json` → bảng trong `research/trends/patterns.md`); `angles` vào `content/idea-bank.md`.
- JSON cũ (trước 26/11 chiều: `spine`, `pacing`, `formula`) vẫn đọc được: `teardown.py --rerender <json>`.
- Kênh @hi.oneup không quay, không B-roll, không nhạc trong file: khi chuyển sang kênh, "ngắt nhịp" = đổi cảnh comic, hit motion + SFX (luật 50, 51).
