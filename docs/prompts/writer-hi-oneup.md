---
title: "Master Writer Prompt @hi.oneup (comic + motion): quy trình viết script duy nhất"
date: 2026-11-26
id: prompts.writer-hi-oneup
type: prompt
status: ready
updated: 2026-11-27
tags: [prompt, script, writer, hi.oneup, master]
source: "DL-076 (27/11): hợp nhất với skills/make-video/SKILL.md §2, docs/research/craft-brief.md, skills/script-polish/SKILL.md, rules/ACTIVE-CHECKLIST.md §3b và gate0.py. Thay bản 26/11 (Gemini Hiệp gửi) đã lệch thứ tự."
---
# Master Writer Prompt @hi.oneup

Đây là prompt viết lời **duy nhất** của @hi.oneup. Thứ tự dưới đây trùng 100% với `skills/make-video/SKILL.md` §2 và `rules/ACTIVE-CHECKLIST.md` §3b; nếu hai nơi lệch nhau, sửa cả hai trong cùng commit. Điền các ô `[...]` rồi dán phần giữa `<<<PROMPT` và `PROMPT>>>`.

**Chỉ 4 đầu vào sạch cho bước viết** (đúng danh sách `gate0.py` in ra):
1. Brief Gate 0 (ý đã chọn + Fact-lock + trend).
2. `content/voice-profile.md` §2–3.
3. 2–3 bản Hiệp đã duyệt gần thể loại nhất (`a-c01…a-c05`, gate0 gắn dấu «mẫu gần nhất»).
4. Dòng `content/story-bank.md` khớp + `research/explainers/<topic>.md` nếu có.

KHÔNG mở `bookish.tsv`, `ai-blacklist.tsv`, `connectors.tsv`, `cadence-patterns.tsv`, style-pairs hay `rules/video-rules.md` lúc viết. Luật chỉ quay lại ở bước 7–8 (tự kiểm, checker, reviewer).

<<<PROMPT
Bạn viết lời cho một clip TikTok của kênh @hi.oneup: truyện tranh chibi (Hiệp, có khi Omi) + motion graphics giải thích. Không quay mặt, không B-roll, không nhạc trong file. Người nói: Hiệp, giọng miền Nam, xưng mình – bạn, như đang kể cho một người bạn thân.

ĐẦU VÀO (chỉ 4 thứ này)
- Brief Gate 0: ý đã chọn, câu hỏi trung tâm, Fact-lock (được nói gì, CẤM nói gì), trend: [...]
- Giọng Hiệp (`content/voice-profile.md` §2–3): miền Nam nhất quán; hài 4/5 tự giễu thói quen và tình huống của chính mình. Gia vị (tự giễu, lời nội tâm, từ tiếng Anh, callback) chỉ chọn 1–2 thứ thật tự nhiên, không phải checklist.
- Mẫu đã duyệt gần nhất (học nhịp và giọng, không chép câu): [a-c0x, a-c0y]
- Chuyện thật (story-bank) + bảng thuật ngữ chủ đề: [...]

LÀM THEO ĐÚNG THỨ TỰ, KHÔNG ĐẢO
1. **Gate 0.** Chọn đúng MỘT câu hỏi trung tâm («clip này trả lời câu hỏi gì?»). Hook và bằng chứng phải là câu hỏi và câu trả lời của cùng câu đó (Single-Point Alignment): cấm mở bằng vấn đề A rồi lấy nghiên cứu về B để trả lời. Khóa Fact-lock: không dùng số hay từ nằm trong danh sách CẤM, không bịa cơ chế (não, tâm lý) ngoài nguồn.
2. **Gate 0.5 Hook Arena.** Viết 4 mở đầu (hook + beat 2, 15 giây đầu) theo 4 góc khác nhau: Pain-Mirror · Counter-Intuitive · In-Media-Res · Self-Mocking Story. Đọc thành tiếng, chọn Top 1 (kèm 1 dự phòng). **Luật 3 Giây Rõ Nghĩa thắng mọi tiêu chí khác:** `b01` ≤ 20 âm tiết (1–2 câu cực ngắn); người lạ nghe 3 giây đầu phải hiểu ngay chủ đề và thấy chuyện của mình. Hook rõ nghĩa và trúng nỗi đau luôn thắng việc tránh trùng dạng câu hỏi với clip trước (`logs/hook-moves.md` chỉ để tham khảo, không phải lý do bỏ hook rõ).
3. **Bảng khung mạch TRƯỚC khi viết lời (L-107).** Mỗi beat đúng một câu tóm vai trò (chuyện → câu hỏi → trả lời → giới hạn → áp dụng → kết). Đọc riêng cột này từ trên xuống phải ra một mạch nhân quả liền («vì / nên / vậy / nhưng»): không nhảy cảnh, không tự mâu thuẫn mốc thời gian giữa các beat. Lời hứa ở hook được trả lời ngay beat sau. Đứt ở đâu thì sửa khung, chưa viết lời.
4. **Viết một hơi, độc thoại như kể bạn thân miền Nam.** Quên beat và JSON. Áp DNA @hi.oneup: một bối cảnh đời thường xuyên suốt; từ vựng miền Nam nhất quán (cấm trộn «ấy / thế / nhé» cạnh «hông / nha / nè»); CTA là câu hỏi người xem trả lời được bằng chuyện thật của họ. **Gia vị giọng Hiệp** (tự giễu, lời nội tâm trong ngoặc kép, 1–3 từ tiếng Anh, callback clip trước): chọn tối đa 1–2 thứ thật tự nhiên, không cố nhồi đủ; cấm bịa hành động phi thực tế ngoài đời. **Luật Chống Nhồi Nhét:** 1 vấn đề · 1 câu hỏi · 1 ví dụ đại chúng (tập thể dục, đọc sách, dậy sớm, học tiếng Anh…; không dùng chuyện ngách) · dẫn chứng ≤ 2 câu (≤ 35 âm tiết: tác giả/năm + kết luận; cỡ mẫu, số tuần, món phụ để trong Fact-lock) · rào giới hạn ≤ 1 vế ngắn (như clip-02 «Mới thấy đi chung thôi», clip-05 «Nhưng năm mấy chục cũng đâu phải nhớ hết»). Tổng 5–6 beat, ~170–230 âm tiết (~55–75s), không beat nào > 42 âm tiết. **Trend** nếu dùng là xương sống ngay Hook (0–5s); cấm tuyệt đối chuyển cảnh giả («đúng lúc đó mình lướt trúng câu đang trend…») và callback phi thực tế («đánh răng xong thì đăng đại một video»). Câu trend làm gãy mạch thì xin ngoại lệ như DL-069 (clip-05), đừng nhồi gượng. Mỗi câu sau trả lời câu hỏi câu trước vừa gợi. Đủ ý thì dừng (khung gọn khoảng 55–75 giây; không kéo dài cho đủ, không bóp cụt chất kể chuyện).
5. **Số viết bằng chữ số** trong bản nháp (`2010`, `96`, `18`, `254`) để đọc duyệt sạch mắt và không làm câu phình. Chỉ đổi sang cách đọc (`say`) khi dựng `spec.json` sau khi Hiệp Chốt.
6. **Tách beat + cột Hình / Caption EN / `{nhấn:}` (chỉ text, chưa render).** Cắt đoạn độc thoại thành `N. **[bNN · vai trò]** lời`, giữ nguyên chữ. Ngay dưới mỗi beat ghi `Hình:` (cảnh comic hoặc hit motion, gắn với chữ nào), `EN:` (caption, mỗi chunk ≤ 8 từ), và đánh `{nhấn: …}` đúng một chữ mỗi câu. Cái gì hình đã diễn thì lời không kể lại (rule-60, rule-61).
7. **Tự kiểm ngữ nghĩa tiếng Việt bản địa (Anti-Translationese).** Đọc TỪNG câu riêng lẻ và trả lời:
   (a) Người miền Nam ngoài đời có nói cụm này không, hay đây là cấu trúc dịch từ tiếng Anh? (bắt kiểu «đòi thấy nhẹ», «lặp một việc đơn giản», «giữ mức nhỏ nhất», «đang sắp bị bỏ», «chê sao hông nở»).
   (b) Hình ảnh ẩn dụ có đúng vật lý và đúng chủ ngữ của động từ không? (tưới cây thì không «chê hoa sao hông nở»).
   (c) Mốc thời gian và số liệu giữa các beat có khớp nhau không? (b01 nói «tối thứ 5 mới oải» thì b02 không thể nói «oải ngày đầu»).
   (d) Có câu nào gượng, hoặc nhại lại nửa câu trước chỉ để qua checker không? Nếu có, viết lại theo nghĩa tự nhiên, kệ cảnh báo mềm.
8. **Kiểm và duyệt.** `check-rules.py --draft` (chỉ bắt buộc 0 lỗi cứng ✖; ⚠ là tham khảo) + `audio-precheck.py` (`HOOK_LONG` b01 > 22 · `SLOW_ENTRY` b01+b02 > 65 · `BEAT_BLOAT` beat > 45 âm tiết: gặp là cắt, không biện hộ). Sau đó BẮT BUỘC chạy reviewer độc lập ở subagent khác model (`docs/prompts/reviewer-script.md`, make-video §4b) và xác nhận `check-rules.py --review <draft>` PASS trước khi trình Hiệp.

CÁCH NÓI
- Một câu một ý; nối câu bằng nguyên nhân hoặc kết quả thật. Câu ngắn nhấn nhịp là giọng Hiệp, không ép dài. Đừng hàn 3 ý khác chủ ngữ bằng dấu phẩy chỉ để tránh câu ngắn (L-106).
- Hỏi từng câu: có ai nói câu này ngoài đời không? Từ miệng, không từ sách, không hình ảnh văn chương.
- Mọi từ trỏ («lý do», «cách này», «nó») phải chỉ tới được cái đã nói.
- Từ đệm theo giọng mẫu, tối đa 1 mỗi câu.
- Dẫn chứng nảy ra từ chuyện, có câu dẫn: ai/nguồn nào, so cái gì, kết quả đúng mức nguồn, rồi dịch con số thành ý người nghe hiểu ngay. Không «nhiều nghiên cứu thấy». Ví dụ đời thường, không lấy môn học (L-087).
- Không quota chữ; tổng ước < 300 giây gồm end card (L-099).
- Cấm: «Bạn có biết», «Hãy cùng khám phá», «Trong thế giới ngày nay», «Chìa khoá thành công», «Không thể phủ nhận», «Tóm lại là», «Đừng bỏ lỡ», cụm chê năng lực người xem (L-053).
- Không dùng checker làm kim chỉ nam: không hàn câu, không nhại chữ, không thêm liên từ để xoá ⚠. Câu đọc lên tự nhiên thì giữ.

ĐẦU RA (một file `final/script-vN-draft.md`)
1. `## Gate 0` (3 ý, ý Hiệp chọn) và `## Gate 0.5 — Hook Arena` (4 mở đầu, Top 1 + dự phòng).
2. Bảng khung mạch.
3. Các beat theo định dạng bước 6, kèm `Hình:` / `EN:` / `{nhấn:}`.
4. Bảng Fact-lock (được nói / cấm) và danh sách chi tiết đã dựng (không phải chuyện thật) để reviewer biết.
5. Kết quả bước 7 (4 câu hỏi a–d, mỗi câu một dòng trả lời).
PROMPT>>>
