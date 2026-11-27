---
name: script-polish
description: >-
  Use after a short-form video script is drafted (facts checked) and before it goes
  to the creator for approval: remove AI-writing tells with the vendored humanizer
  skill, adapt to spoken Vietnamese, and match the creator's voice profile, without
  changing any fact, number or citation.
version: "1.8.0"
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
Quy trình viết một nguồn duy nhất: `docs/prompts/writer-hi-oneup.md` (Master Writer Prompt), cùng thứ tự với `skills/make-video/SKILL.md` §2, `docs/research/craft-brief.md` và `rules/ACTIVE-CHECKLIST.md` §3b. Skill này là bước **7 (tự kiểm) và chải chữ** sau khi độc thoại đã có.

Lúc tìm lời (nháp v1, v2) chỉ nạp **4 đầu vào sạch**: (1) brief Gate 0 (ý + Fact-lock + trend); (2) `content/voice-profile.md` §2–3; (3) 2–3 bản đã duyệt gần thể loại nhất trong `a-c01…a-c05` (gate0 gắn dấu); (4) dòng `content/story-bank.md` khớp + `research/explainers/<topic>.md`. Không nạp `connectors.tsv`, `bookish.tsv`, `ai-blacklist.tsv`, `cadence-patterns.tsv` hay `style-pairs.md` vào lượt viết đó.

Lượt chải chữ này chạy sau khi độc thoại đã có và sau khi cắt 25–30%. Lúc này mới được nhìn:
- Draft script (lời VI + caption EN).
- `content/voice-profile.md` và các bản đã duyệt. Nhịp của chúng thắng danh sách cấm.
- `resources/feedback.md`: Hiệp đã bác gì, bằng lời của ông.
- Tùy chọn **transcript voice memo** (`media/voice-memos/<name>.txt`): giữ ≥ 80% từ của ông.
- `skills/humanizer/SKILL.md` ở chế độ nhúng, cho những dấu hiệu còn sót sau khi cắt. Không dùng nó để nhồi liên từ.

## Two tiers — Hard-Gate + Pairwise A/B — what this pass may and may not "fix"
- **Tier 1, hard fails (`H1–H4`, sole hard blocker; never introduce, always fix):** H1 fact without source / beyond the source · H2 total ≥ 300 s (L-099) · H3 wrong brand/format for the channel (@hi.oneup DL-027; @vanhiep.tech its AGENTS.md) or mocking the viewer (L-053) · H4 broken draft/spec structure.
- **Tier 2, Pairwise A/B** (replaces absolute ≥85 score threshold): compared side-by-side against the theme/format-matched approved anchor clip on 4 relative axes (`Hook & Giữ chân`, `Mạch truyện & Chuyển ý`, `Văn nói tự nhiên VN`, `Độ đắt của ẩn dụ/payoff`). Also run `python3 pipeline/scripts/audio-precheck.py <draft.md>` to check spoken VN rhythm (2.6–3.4 syl/s, pacing contrast, no repeated consecutive beat openers, plus `FLAT_CADENCE`, `MISSING_VULNERABILITY_DIP`, and `VOICE_REF_MAP` mapping beats to `thai-son-v2/serious/happy`, `DL-082`). A narrative breath of about 15–25 syllables with a comma is healthy. A landing line of about 5–10 syllables is a punch, not a defect. Warn only on an unbroken span over 32 syllables.
- **Soft warnings are not errors.** Do NOT "correct" natural spoken variants that match the voice profile: particles (nè, á, hông, nghen), spoken connectors («thật ra thì», «nhưng mà khoan», «nghe quen không», «nói thẳng ra là», «thế mới có chuyện»), short punchy sentences, rhetorical questions that hold attention. Polishing these into tidy written Vietnamese is exactly what Hiệp rejects (L-105, L-106).

## Cut, then listen
1. Delete every sentence that explains again what the listener just understood, and every moral that repeats the image. That cut is about 25–30% on a stuffed draft. If what remains is 75–90 s, keep it.
2. Do not add a sentence so a beat has an "anchor", a connector, or a number. A physical detail stays only when the story was already using it.
3. `check-rules.py --draft` at the end is for hard errors only (H1–H4, `L-087`: 0 ✖; every style check is ⚠). `check-rules.py --audit` prints bookish, ai-structure and choppy. Leave a natural line alone when clearing the warning would make it sound written. Since DL-076 `choppy`, `flow`, `link`, `repeat`, `clarity`, `bookish`, `ai-structure` and `connector-stuffing` are all ⚠, never ✖.

## Chống nhồi liên từ, bịa chuyển cảnh, cắt nghĩa thừa (27/11, clip-06 v5 → v6)
Ba lỗi làm v5 dài và mùi AI. Áp dụng lúc cắt, trước mọi bước chải chữ. `check-rules.py --draft` báo `⚠ connector-stuffing` cho lỗi đầu.
1. **Cấm nhồi liên từ.** Không mở ≥ 2 câu liên tiếp bằng *Nên, Nhưng mà, Thành ra, Vì vậy, Do đó, Mà, Rồi, Thế là*, và các câu mở bằng liên từ không quá 25% tổng số câu. Muốn nối ý: đặt 2 sự thật cạnh nhau hoặc hỏi 1 câu ngắn để ý tự bật ra («Ba buổi. Cân hông nhích. Đo sai thước rồi.»). Tối đa 1 từ nối, ở chỗ lời thật sự rẽ hướng. Các cảnh báo `L-089 / L-093 / L-094` (liền mạch, lặp cụm, từ gọi lại) và `connector-stuffing` cùng chỉ là ⚠ và bóp chéo nhau: **không** nhại lại nửa câu trước, không hàn câu dài lủng củng, không lặp chữ chỉ để một cảnh báo hết. Chọn nghĩa tự nhiên.
2. **Cấm «kể lể chuyển cảnh giả».** Giữ đúng **1 bối cảnh/ví dụ xuyên suốt** từ hook tới việc làm tối nay. Không bịa hành động nối cảnh vô lý («đứng nhìn cái cây mỗi sáng», «úp chén xong kéo giày»), không ghép 3–4 bối cảnh rời (giày → cái cây → nghiên cứu → úp chén). Bằng chứng là 1 con số đặt cạnh ví dụ, không phải 1 cảnh mới.
3. **Cấm giải thích lại điều đã rõ (No Over-Explaining).** Mỗi ý nói 1 lần bằng hình ảnh hoặc con số cụ thể. Không viết câu tóm tắt bài học kiểu «Vì vậy điều đó có nghĩa là…», «Tức là…» lặp lại ẩn dụ vừa nói. Với bằng chứng: giữ đúng 1 kết luận từ fact-lock, bỏ cỡ mẫu và bối cảnh phụ nếu không phục vụ ý chính.
4. **Đúng chất giọng Hiệp (`content/voice-profile.md`) & CTA đối thoại thật (`DL-080`, `DL-081`).** Thẳng, đời thường, tự giễu thói quen của chính mình (không trêu người xem), kết ấm áp ngang hàng. Cấm câu sến kiểu «mình ngồi nghe nha», «mình ở đây đợi bạn». CTA phải đồng cảm («có ai bị giống mình… hông?») + mở cửa lắng nghe góc nhìn & cách vượt qua của mỗi người; **cấm** ép «comment 1 chữ / 1 con số» trái ngữ nghĩa và cấm khảo sát xã giao sáo rỗng («bạn đang tập gì, được bao lâu»).
5. **Luật 3 Giây Rõ Nghĩa: `b01` ≤ 20 âm tiết (1–2 câu cực ngắn); người lạ nghe 3 giây đầu hiểu ngay chủ đề và thấy chuyện của mình. Trong Hook Arena, rõ nghĩa và trúng nỗi đau trong 3s luôn thắng việc tránh trùng dạng câu hỏi với clip trước.** Cắt hook trước mọi thứ khác nếu b01 > 22 âm tiết (`audio-precheck` báo `HOOK_LONG`).
6. **Luật Chống Nhồi Nhét:** 1 vấn đề · 1 câu hỏi · 1 ví dụ đại chúng (tập thể dục, đọc sách, dậy sớm, học tiếng Anh…, không chuyện ngách) · dẫn chứng ≤ 2 câu (≤ 35 âm tiết) · rào giới hạn ≤ 1 vế ngắn (clip-02 «Mới thấy đi chung thôi», clip-05 «Nhưng năm mấy chục cũng đâu phải nhớ hết»). 6–7 beat, ~200–265 âm tiết, `b01+b02` ≤ 65, không beat nào > 45. **Đủ ý & Khép vòng:** số lớn đã nêu phải dịch nghĩa cho người nghe (254 ngày → «hơn 8 tháng»); trend và nghiên cứu có câu dẫn mượt từ beat trước, không nhảy cóc; phần cách làm có 1 đổi thước đo + 1 hành động cụ thể rồi khép vòng về nỗi lo ở Hook; cụt ý < 60s là lỗi như nhồi nhét. **Liên mạch bằng Ý, cấm dán keo từ nối (Thought-Flow over Connector-Glue; Hiệp 27/11, clip-06 v10 «kết nối câu không liền mạch, rập khuôn khi thêm từ nối»):** (1) không mở các beat/câu liên tiếp bằng công thức `Tại / Mà / Vậy / Nghĩa là / Nên / Còn… thì sao`; (2) câu sau nảy ra từ hình ảnh, cảm xúc hoặc hệ quả của câu trước (từ «hơn 8 tháng» tự dẫn sang «giữ cả mấy tháng trời kiểu gì cũng có hôm nghỉ ngang», không bật câu hỏi Q&A gượng); (3) không dùng câu meta như «dạo này có câu trend nói:», câu trend hoà vào mạch nghĩ của người kể và chỉ ra ngay điểm giống với chuyện đang kể; (4) không lặp số của câu trước chỉ để mở «Nghĩa là…», gộp số + quy đổi nghĩa trong một hơi. Cách kiểm: đọc bỏ hết từ nối đầu câu mà các ý vẫn tự kéo nhau đi thì mạch thật, từ nối chỉ là lớp phủ. Gia vị giọng Hiệp (tự giễu, lời nội tâm, từ EN, callback) chọn tối đa 1–2 thứ thật tự nhiên. Cấm tuyệt đối chuyển cảnh giả để chèn trend («đúng lúc đó mình lướt trúng câu đang trend…») và callback phi thực tế («đánh răng xong thì đăng đại một video»); trend nếu dùng là xương sống ngay Hook, gãy mạch thì xin ngoại lệ như DL-069.
7. **Khung mặc định `ONEUP-CORE-ARC`, 5 Archetypes (`M1..M5`) & Đường cong Cảm xúc 6 nhịp (`DL-079`, `DL-082`, `docs/research/storytelling-craft-guide.md`):** Pha 1 viết liền một hơi có hồn theo 1 trong 5 Archetypes (hoặc chạy 3 Writer song song qua `script-arena.py`) bám sóng cảm xúc (*Hook Spark → Vulnerability Dip bắt buộc → Curiosity → Aha Peak → Catharsis → Warm Peer CTA*); Pha 2 (skill này) chỉ chỉnh vi phẫu mà **không gọt phẳng khẩu ngữ miền Nam tự nhiên**, giữ đúng chiều tăng tiến số liệu (*Climactic Order*: nhỏ → lớn gây bất ngờ), dẫn vào nghiên cứu qua kỳ vọng sai → cú tỉnh ngộ (*Storytelling the Study*), và **cấm lạm dụng điệp từ cuối–đầu cơ học (*Anadiplosis*)**. Bảng Beat bắt buộc đánh dấu `**nhấn**` / `{nhấn: …}` mỗi câu.

## Một thông điệp xuyên suốt + cầu nối ngữ nghĩa (27/11, clip-06 v6 → v7; Hiệp: «rời rạc, hook không liên quan, nghe xong mù mờ»)
Chống nhồi liên từ không có nghĩa là cắt cụt. v6 qua được checker mà vẫn bị bác vì hai lỗi dưới đây.
1. **1 clip = 1 thông điệp (Single-Point Alignment).** Hook ở nhịp 1 phải đặt đúng vấn đề mà bằng chứng ở nhịp 3 giải quyết. Cấm mở bằng tình huống A (giảm cân) rồi lấy nghiên cứu về B (thói quen thành tự động) để trả lời. Kiểm: viết 1 câu «clip này trả lời câu hỏi gì», rồi đọc hook và bằng chứng, cả hai phải là câu hỏi và câu trả lời của cùng một câu đó. Hook là nỗi đau của chính người sẽ nghe câu trả lời.
2. **Cầu nối ngữ nghĩa (Semantic Bridge).** Cuối beat trước gieo 1 từ khóa hoặc 1 câu hỏi ngắn, đầu beat sau bắt đúng từ đó và trả lời. Không dùng *Nên / Vì vậy / Thành ra* ở đầu câu và cũng không để 2 beat đứng trơ cạnh nhau. Ví dụ: beat 2 kết «Vậy chưa quen nhịp là chờ bao lâu?», beat 3 mở bằng nghiên cứu đo đúng chuyện chờ bao lâu.
3. **Số liệu phải được dịch.** Mỗi số liệu nghiên cứu đi kèm 1 mệnh đề tiếng Việt đời thường nói nghiên cứu đo cái gì và con số đó nghĩa gì với người đang nản. Không ném tên tác giả cộng hai con số trơ trọi. Vẫn giữ 1 kết luận từ fact-lock; việc dịch không được thêm số hay kết luận mới.
4. **Đọc liền thành 1 đoạn văn xuôi** trước khi gửi duyệt. Người nghe không cần nghĩ vẫn thấy câu sau trả lời câu trước. Chỗ nào khựng thì sửa mối nối, đừng sửa từ ngữ.

## Cổng ngữ nghĩa tiếng Việt bản địa + Chống văn dịch (27/11, DL-076; bước 7 của Master Writer Prompt)
v6/v7 lọt checker mà vẫn sai nghĩa tiếng Việt và tự mâu thuẫn. Trước khi gửi reviewer, đọc **từng câu riêng lẻ** và trả lời 4 câu, ghi 4 dòng vào nháp:
- **(a)** Người miền Nam ngoài đời có nói cụm này không, hay đây là cấu trúc dịch từ tiếng Anh? Mẫu lỗi đã lọt: «đòi thấy nhẹ», «chê sao hông nở», «lặp một việc đơn giản», «giữ mức nhỏ nhất», «đang sắp bị bỏ».
- **(b)** Hình ảnh ẩn dụ có đúng vật lý và đúng chủ ngữ của động từ không? (Tưới cây thì không «chê hoa sao hông nở»; hoa nở là việc của cây, không phải của người tưới.)
- **(c)** Mốc thời gian và số liệu giữa các beat có khớp không? (b01 «hai tối đầu hăng», b02 «cái oải ngày đầu» là tự mâu thuẫn.)
- **(d)** Có câu nào gượng, hoặc nhại lại nửa câu trước chỉ để qua checker không? Có thì viết lại theo nghĩa tự nhiên, kệ cảnh báo mềm.
Ngoài ra, giữ DNA kênh: giọng miền Nam nhất quán (không trộn «ấy / thế / nhé» với «hông / nha»), gia vị (tự giễu, lời nội tâm) chỉ 1–2 thứ thật tự nhiên, không khô như tóm tắt sách. Không đọc ra tiếng Việt tự nhiên thì sửa nghĩa, đừng sửa chữ cho checker.

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
3. **Spoken VI pass.** Read the cut monologue aloud. A written tell («tuy nhiên», «do đó», «bạn có biết») goes only if the sentence still sounds like the same person after the change. Do not open `connectors.tsv` to insert a join. One «nha» is enough. Numbers stay as plain digits in the draft (`2010`, `96`, `254`) so the line reads clean and does not bloat; they become spoken forms (`say`, "chín mươi sáu") only when `spec.json` is built after Chốt.
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
