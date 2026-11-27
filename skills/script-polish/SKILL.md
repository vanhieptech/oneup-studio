---
name: script-polish
description: >-
  Use after a short-form video script is drafted (facts checked) and before it goes
  to the creator for approval: remove AI-writing tells with the vendored humanizer
  skill, adapt to spoken Vietnamese, and match the creator's voice profile, without
  changing any fact, number or citation.
version: "1.6.0"
metadata:
  author: OneUp Studio
  tags:
    - script
    - vietnamese
    - voice
    - humanizer
---
# Script polish (VI voice)

## Purpose
Polish a fact-checked short-form script into spoken Vietnamese that matches the creator voice profile, removing both AI-writing vocabulary and structural AI-tells without changing facts.


## Inputs
While the words are still being found (draft v1 and v2), load only three things: the two approved scripts `a-c01` and `a-c04`, the idea plus the core fact, and the rule that each next sentence answers the question the previous one raised. Do not load `connectors.tsv`, `bookish.tsv`, `ai-blacklist.tsv`, `cadence-patterns.tsv` or `style-pairs.md` into that pass.

This polish pass runs after the monologue exists and after the 25–30% cut. It may then look at:
- Draft script (VI voice lines + EN captions).
- `content/voice-profile.md` and the two approved scripts above. Their rhythm overrides a ban list.
- `resources/feedback.md`: what Hiệp rejected, in his words.
- Optional **voice memo transcript** (`media/voice-memos/<name>.txt`). Keep ≥ 80% of his words when one exists.
- `skills/humanizer/SKILL.md` in embedded mode, for tells that survive the cut. Do not use it to stuff connectors.

## Two tiers — Hard-Gate + Pairwise A/B — what this pass may and may not "fix"
- **Tier 1, hard fails (`H1–H4`, sole hard blocker; never introduce, always fix):** H1 fact without source / beyond the source · H2 total ≥ 300 s (L-099) · H3 wrong brand/format for the channel (@hi.oneup DL-027; @vanhiep.tech its AGENTS.md) or mocking the viewer (L-053) · H4 broken draft/spec structure.
- **Tier 2, Pairwise A/B** (replaces absolute ≥85 score threshold): compared side-by-side against the theme/format-matched approved anchor clip on 4 relative axes (`Hook & Giữ chân`, `Mạch truyện & Chuyển ý`, `Văn nói tự nhiên VN`, `Độ đắt của ẩn dụ/payoff`). Also run `python3 pipeline/scripts/audio-precheck.py <draft.md>` to check spoken VN rhythm (2.6–3.4 syl/s, pacing contrast, no repeated consecutive beat openers). A narrative breath of about 15–25 syllables with a comma is healthy. A landing line of about 5–10 syllables is a punch, not a defect. Warn only on an unbroken span over 32 syllables.
- **Soft warnings are not errors.** Do NOT "correct" natural spoken variants that match the voice profile: particles (nè, á, hông, nghen), spoken connectors («thật ra thì», «nhưng mà khoan», «nghe quen không», «nói thẳng ra là», «thế mới có chuyện»), short punchy sentences, rhetorical questions that hold attention. Polishing these into tidy written Vietnamese is exactly what Hiệp rejects (L-105, L-106).

## Cut, then listen
1. Delete every sentence that explains again what the listener just understood, and every moral that repeats the image. That cut is about 25–30% on a stuffed draft. If what remains is 75–90 s, keep it.
2. Do not add a sentence so a beat has an "anchor", a connector, or a number. A physical detail stays only when the story was already using it.
3. `check-rules.py --draft` at the end is for hard errors (H1–H4, and any ✖ the draft gate still raises). `check-rules.py --audit` prints bookish, ai-structure and choppy. Leave a natural line alone when clearing the warning would make it sound written.

## Chống nhồi liên từ, bịa chuyển cảnh, cắt nghĩa thừa (27/11, clip-06 v5 → v6)
Ba lỗi làm v5 dài và mùi AI. Áp dụng lúc cắt, trước mọi bước chải chữ. `check-rules.py --draft` báo `⚠ connector-stuffing` cho lỗi đầu.
1. **Cấm nhồi liên từ.** Không mở ≥ 2 câu liên tiếp bằng *Nên, Nhưng mà, Thành ra, Vì vậy, Do đó, Mà, Rồi, Thế là*, và các câu mở bằng liên từ không quá 25% tổng số câu. Muốn nối ý: đặt 2 sự thật cạnh nhau hoặc hỏi 1 câu ngắn để ý tự bật ra («Ba buổi. Cân hông nhích. Đo sai thước rồi.»). Tối đa 1 từ nối, ở chỗ lời thật sự rẽ hướng.
2. **Cấm «kể lể chuyển cảnh giả».** Giữ đúng **1 bối cảnh/ví dụ xuyên suốt** từ hook tới việc làm tối nay. Không bịa hành động nối cảnh vô lý («đứng nhìn cái cây mỗi sáng», «úp chén xong kéo giày»), không ghép 3–4 bối cảnh rời (giày → cái cây → nghiên cứu → úp chén). Bằng chứng là 1 con số đặt cạnh ví dụ, không phải 1 cảnh mới.
3. **Cấm giải thích lại điều đã rõ (No Over-Explaining).** Mỗi ý nói 1 lần bằng hình ảnh hoặc con số cụ thể. Không viết câu tóm tắt bài học kiểu «Vì vậy điều đó có nghĩa là…», «Tức là…» lặp lại ẩn dụ vừa nói. Với bằng chứng: giữ đúng 1 kết luận từ fact-lock, bỏ cỡ mẫu và bối cảnh phụ nếu không phục vụ ý chính.
4. **Đúng chất giọng Hiệp (`content/voice-profile.md`).** Thẳng, đời thường, tự giễu thói quen của chính mình (không trêu người xem), kết gọn. Cấm câu sến kiểu «mình ngồi nghe nha», «mình ở đây đợi bạn». CTA là 1 câu hỏi trực diện để comment 1 chữ hoặc 1 con số.
5. **Khung mặc định `ONEUP-CORE-ARC`** (5 nhịp, 180–250 âm tiết ≈ 55–75s): hook tình huống → bẻ thước đo + gài trend → 1 bằng chứng → 1 việc tối nay → CTA 1 chữ. Chi tiết ở `skills/make-video/SKILL.md` (Gate 0).

## Một thông điệp xuyên suốt + cầu nối ngữ nghĩa (27/11, clip-06 v6 → v7; Hiệp: «rời rạc, hook không liên quan, nghe xong mù mờ»)
Chống nhồi liên từ không có nghĩa là cắt cụt. v6 qua được checker mà vẫn bị bác vì hai lỗi dưới đây.
1. **1 clip = 1 thông điệp (Single-Point Alignment).** Hook ở nhịp 1 phải đặt đúng vấn đề mà bằng chứng ở nhịp 3 giải quyết. Cấm mở bằng tình huống A (giảm cân) rồi lấy nghiên cứu về B (thói quen thành tự động) để trả lời. Kiểm: viết 1 câu «clip này trả lời câu hỏi gì», rồi đọc hook và bằng chứng, cả hai phải là câu hỏi và câu trả lời của cùng một câu đó. Hook là nỗi đau của chính người sẽ nghe câu trả lời.
2. **Cầu nối ngữ nghĩa (Semantic Bridge).** Cuối beat trước gieo 1 từ khóa hoặc 1 câu hỏi ngắn, đầu beat sau bắt đúng từ đó và trả lời. Không dùng *Nên / Vì vậy / Thành ra* ở đầu câu và cũng không để 2 beat đứng trơ cạnh nhau. Ví dụ: beat 2 kết «Vậy chưa quen nhịp là chờ bao lâu?», beat 3 mở bằng nghiên cứu đo đúng chuyện chờ bao lâu.
3. **Số liệu phải được dịch.** Mỗi số liệu nghiên cứu đi kèm 1 mệnh đề tiếng Việt đời thường nói nghiên cứu đo cái gì và con số đó nghĩa gì với người đang nản. Không ném tên tác giả cộng hai con số trơ trọi. Vẫn giữ 1 kết luận từ fact-lock; việc dịch không được thêm số hay kết luận mới.
4. **Đọc liền thành 1 đoạn văn xuôi** trước khi gửi duyệt. Người nghe không cần nghĩ vẫn thấy câu sau trả lời câu trước. Chỗ nào khựng thì sửa mối nối, đừng sửa từ ngữ.

## Emotional and logical flow
A beat is not a slide. The last sentence of a beat plants the question the next beat answers. «Nhưng mà» and «thành ra» are for that turn, not a connector quota (see the anti-stuffing rules above: never two openers in a row). If the next beat could be moved anywhere without the listener noticing, rewrite the join in the monologue before touching word choice.

## Steps
1. **Fact lock.** List every fact, number, study, date and citation in the draft. These must appear unchanged in the output.
2. **Humanizer pass** on the VI lines and EN captions. The structural tells apply in any language. In Vietnamese, watch for:
   - "Không phải X, mà là Y" used just for emphasis.
   - Triads ("nhanh, gọn, hiệu quả").
   - Closers that only repeat the point ("Và đó chính là chìa khoá.").
   - Inflated words: "bí quyết", "thay đổi cuộc đời", "đỉnh cao", "chìa khoá vàng".
   - Staged openers: "Bạn có biết…", "Hãy cùng tìm hiểu…".
   - Every sentence the same length.
   - **Paste test** (adapted from mankidev/antialgorithm, MIT): a line that could go into another clip unchanged is too general. Rewrite it around the concrete thing in this clip (something Hiệp saw, did or said, the study's real detail), not a bigger claim. Don't swap a cliché for its known opposite. Don't add a time, date or number just to sound concrete; keep one only when the viewer needs it. Never invent a fact to fill the gap (step 1 still holds).
3. **Spoken VI pass.** Read the cut monologue aloud. A written tell («tuy nhiên», «do đó», «bạn có biết») goes only if the sentence still sounds like the same person after the change. Do not open `connectors.tsv` to insert a join. One «nha» is enough. Numbers are written the way they are read aloud ("chín mươi sáu").
4. **Voice pass.** Apply the confirmed profile:
   - Use the profile's region and particles, sparingly.
   - Use its humor style. For @hi.oneup that is 4/5 sly teasing aimed at habits and at the creator himself, never at viewers or groups.
   - Use its English-mix rule: 1–3 words per clip, to lighten the mood or stress the key idea.
   - Copy the do/don't examples in the profile.
5. **Story pass (rule-41).** Prefer a personal story arc (situation → struggle → turn → lesson → invite) built from a story-bank entry. Mark each unconfirmed detail `[CẦN HIỆP XÁC NHẬN]`. Never invent outcomes, like "it worked", that the creator hasn't confirmed.
5b. **Voice-First Input** (when a memo transcript exists, `resources/vn-spoken/voice-first.md`): edit from Hiệp's words. Keep his vocabulary, comparisons and examples; only cut repeats, move the hook first, split beats and add connectors / source lines. Check `python3 pipeline/scripts/voice-memo.py keep <memo.txt> <draft.md>` ≥ 80%.
6. **Voice details.**
   - Use only the creator's real phrases, examples and level of humor from the profile.
   - Never invent a personal story. If a line needs one, insert `[VÍ DỤ THẬT CỦA HIỆP: ...]` as a placeholder.
7. **Trend check (rule-37).** At least one current phrase or situation from `research/trends/ingest.md` must stay in the script, used naturally.
8. **Diff + verify.** Output the old and new lines side by side, list the facts and confirm each is unchanged, and apply L-099: total strictly <300s INCLUDING end card, pauses and transitions; 60–180s is the target, and 60–119s is not a warning. No word quotas, no padding, no speed-up. Before Chốt label natural-reading duration ƯỚC/estimate; measure actual audio/video only after Chốt. This is not Chốt and does not waive W-16.
9. Save as `script-vX.Y-draft.md` next to the approved version. Never overwrite the approved script until the creator approves.

## Requirements
- Read this skill before acting; follow linked channel/repo AGENTS.md when cited.
- Use tools and paths named in the steps; do not invent alternate pipelines.

## Limitations
- Must not change facts, numbers, or citations.
- Depends on `content/voice-profile.md` and `skills/humanizer`.
- Not a topic researcher — facts must already be checked.

## Troubleshooting
| Error / symptom | Cause | Fix |
|---|---|---|
| Facts drifted | Over-aggressive rewrite | Diff against fact-lock list; restore numbers/citations |
| Still sounds AI | Residual humanizer tells | Re-run humanizer pass on VI + EN captions |
| Wrong pronouns/particles | Profile ignored | Re-read `content/voice-profile.md` samples |
| Reviewer flags colloquial lines | Soft warning treated as error | Soft warnings score 0 (rubric §3b); keep the line if it matches the voice profile |
| Voice-First ratio < 80% | Writer replaced Hiệp's words | Restore his phrasing from the memo; change order, not words |
