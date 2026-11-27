---
title: "Craft brief: một trang hướng dẫn nghề lúc viết lời"
date: 2026-11-26
id: research.craft-brief
type: research
status: ready
updated: 2026-11-27
tags: [script, craft, writing, make-video]
source: "Rút từ L-089, L-094, L-096, L-099, L-103–L-107, DL-076 (27/11) và quy tắc văn nói trong hướng dẫn Gemini Hiệp gửi 26/11. Cùng thứ tự với docs/prompts/writer-hi-oneup.md (Master Writer Prompt), skills/make-video/SKILL.md §2, skills/script-polish/SKILL.md và rules/ACTIVE-CHECKLIST.md §3b."
---
# Craft brief (đọc lúc viết; luật đầy đủ để dành cho lúc kiểm)

Trang này là bản tóm tắt nghề của **Master Writer Prompt** (`docs/prompts/writer-hi-oneup.md`). Lúc viết lời chỉ mở **4 đầu vào sạch**: (1) brief Gate 0 (ý + Fact-lock + trend, in bởi `gate0.py`) · (2) `content/voice-profile.md` §2–3 · (3) 2–3 bản đã duyệt gần thể loại nhất (`a-c01…a-c05`, gate0 gắn dấu «mẫu gần nhất») · (4) dòng `content/story-bank.md` khớp + `research/explainers/<chủ-đề>.md` nếu có. Không mở bảng cấm hay lessons lúc này (`bookish.tsv`, `ai-blacklist.tsv`, `connectors.tsv`, `cadence-patterns.tsv`, style-pairs): quá nhiều luật cùng lúc làm lời gượng (L-106). Luật quay lại ở bước tự kiểm và reviewer.

## Thứ tự cố định (không đảo)
1. **Gate 0:** chọn đúng 1 câu hỏi trung tâm; hook và bằng chứng là câu hỏi và câu trả lời của cùng câu đó (Single-Point Alignment). Kiểm story-bank, khóa Fact-lock (số/từ CẤM, không bịa cơ chế ngoài nguồn).
2. **Gate 0.5 Hook Arena:** 4 mở đầu khác góc (Pain-Mirror · Counter-Intuitive · In-Media-Res · Self-Mocking Story), đọc thành tiếng, chọn Top 1 khác 2 clip gần nhất (`logs/hook-moves.md`).
3. **Bảng khung mạch TRƯỚC khi viết lời (L-107):** mỗi beat một câu vai trò; đọc cột đó phải ra mạch nhân quả liền, không nhảy cảnh, không tự mâu thuẫn mốc thời gian.
4. **Viết một hơi như kể bạn thân miền Nam.** Chỉ 4 đầu vào ở trên.
5. **Số bằng chữ số** trong nháp; đổi sang cách đọc (`say`) chỉ khi dựng spec sau Chốt.
6. **Tách beat + `Hình:` / `EN:` / `{nhấn:}` dạng text** (chưa render).
7. **Tự kiểm ngữ nghĩa tiếng Việt bản địa** (mục F).
8. `check-rules --draft` (0 ✖) + `audio-precheck.py` → reviewer độc lập khác model → `check-rules --review` PASS → trình Hiệp.

## A. Trước khi viết một chữ
- **Một câu tóm ý:** người xem đang khổ chuyện gì → clip hứa gì → trả lời bằng gì.
- Lời hứa ở hook được trả lời **ngay beat sau**; không chen câu trend hay ý phụ vào giữa (L-094, L-107). Cuối bài quay lại nỗi lo ở hook.

## B. Hook
- Hook là **mở đầu một câu chuyện**: ai, đang muốn gì, khoảnh khắc hụt, câu gợi chuyện gì xảy ra tiếp (L-103). Không dùng ngôn ngữ nghiên cứu («theo một thí nghiệm», «trung bình người ta») trong hook.
- Có **cái giá người xem thấy đáng bận tâm** và một chỗ bất ngờ trong 3 giây đầu; viết được câu «vì sao người lướt sẽ dừng» (L-096, L-104).

## C. Viết như nói (giọng Hiệp, `voice-profile.md` §2)
- **Viết liền một hơi**, rồi mới cắt thành beat. Không viết từng ô trong bảng (nguồn của câu rời).
- **Miền Nam nhất quán**, xưng mình–bạn. Cấm trộn chữ Bắc «ấy / thế / nhé» cạnh «hông / nha / nè».
- **Hài 4/5 tự giễu** thói quen và tình huống của chính mình; không trêu người xem. Có ít nhất 1 chi tiết tự giễu hoặc 1 **lời nội tâm trích trong ngoặc kép**.
- **Tiếng Anh chen 1–3 từ** mỗi clip, tự nhiên, không cả câu. Từ đệm tối đa 1 mỗi câu, không rải theo danh sách (voice-profile §3c).
- **Một câu một ý**, nối câu bằng nguyên nhân hoặc kết quả thật. Câu ngắn nhấn nhịp là giọng của Hiệp (clip-01 đã duyệt có 41% câu ≤ 10 chữ): không hàn ý khác chủ ngữ bằng dấu phẩy chỉ để tránh câu ngắn (L-106). Không quota chữ: đủ ý thì thôi, tổng < 300s (L-099).
- **Từ miệng, không từ sách:** hỏi «có ai nói câu này ngoài đời không» với từng câu (L-105).
- **Mọi từ trỏ phải chỉ tới được cái gì:** «lý do» là lý do gì, «cách này» là cách nào (L-098, L-106).
- Một ngôi kể xuyên suốt; «bạn» chỉ khi khung chuyện làm việc đó tự nhiên (L-089).
- Gọi lại clip trước nếu hợp tự nhiên (rule-62). CTA là câu hỏi người xem trả lời được bằng chuyện của chính họ; không ép kiểu sáo rỗng, không xin like/follow.

## D. Dẫn chứng
- Dẫn chứng **nảy ra từ chuyện**, có câu dẫn: ai/nguồn nào, so A với B, kết quả đúng mức nguồn (L-096, L-103), rồi dịch con số thành ý người nghe hiểu ngay. Cấm «nhiều nghiên cứu thấy…».
- Con số viết bằng chữ số trong nháp (`2010`, `96`); cách đọc để sau Chốt.
- Ví dụ đời thường, cụ thể; không lấy môn học (L-087). Chuyện thật của Hiệp ưu tiên (story-bank); chi tiết hài được phép dựng (luật 67), số liệu thì không. Không dùng số hay từ nằm trong danh sách CẤM của Fact-lock.

## E. Hình và nhịp
- Ngắt nhịp bằng **hình**, không bằng chữ: @hi.oneup = đổi cảnh comic, hit motion + SFX (luật 50, 51). Ghi ý hình ở dòng `Hình:`, caption ở `EN:` (mỗi chunk ≤ 8 từ), `{nhấn:}` một chữ mỗi câu. Cái hình đã diễn thì lời không kể lại (rule-60, rule-61). Lời đọc vẫn liền mạch.

## F. Tự kiểm ngữ nghĩa tiếng Việt bản địa (Anti-Translationese + tự mâu thuẫn)
Đọc từng câu riêng lẻ:
- **(a)** Người miền Nam ngoài đời có nói cụm này không, hay là cấu trúc dịch từ tiếng Anh? Ví dụ đã lọt: «đòi thấy nhẹ», «chê sao hông nở», «lặp một việc đơn giản», «giữ mức nhỏ nhất», «đang sắp bị bỏ».
- **(b)** Hình ảnh ẩn dụ có đúng vật lý và đúng chủ ngữ của động từ không? (tưới cây không «chê hoa sao hông nở».)
- **(c)** Mốc thời gian và số liệu giữa các beat có khớp không? (b01 «tối thứ 5 mới oải» thì b02 không thể «oải ngày đầu».)
- **(d)** Có câu nào gượng hoặc nhại nửa câu trước chỉ để qua checker không? Có thì viết lại theo nghĩa tự nhiên, kệ cảnh báo mềm.

## Sau khi viết
`check-rules --draft` (chỉ ✖ là bắt buộc; mọi ⚠ về phong cách là tham khảo, không hàn câu, không nhại chữ để xoá) → `script-polish` → make-video §4b (reviewer độc lập khác model). Checker PASS không chứng minh lời hay (L-098); đọc to là cổng thật.
