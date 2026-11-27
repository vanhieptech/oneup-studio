---
name: make-video
description: >-
  Use whenever Hiệp asks for a clip ("Làm clip tiếp theo", "Làm clip về topic/trend",
  "làm lại clip-NN", or beat feedback like "b03: đổi câu …"). The single workflow from
  intake to post package that keeps every clip consistent with rules/video-rules.md:
  read sources → script → humanizer → check-rules → review gate 1 → render → check-rules
  --final → review gate 2 → log decisions. Edits go to the spec, never a regenerate.
version: "1.9.0"
metadata:
  author: OneUp Studio
  tags:
    - video
    - comic
    - hi-oneup
    - pipeline
---
# Make video (one workflow, rule-48)

## Purpose
Run the full @hi.oneup comic+motion clip workflow from intake through review gates, render, and decision logging so every clip stays consistent with `rules/video-rules.md`.


## Thời lượng và Chốt (cập nhật 27/11, DL-076; thay các override 08/11 cũ)
- Mục tiêu 60–180 s; clip cô đọng 60–119 s nằm trong mục tiêu. Giới hạn cứng: tổng **< 300 s** gồm end card, nghỉ, chuyển cảnh (đúng 300 s là fail). Khung gọn mặc định `ONEUP-CORE-ARC` ~60–90 s: đủ ý thì dừng, không kéo dài, không bóp cụt chất kể chuyện. Không quota chữ, không tăng tốc giọng.
- **Trước Chốt** = chỉ text: Script Draft + Bảng khung mạch + ý Hình / Caption EN / nhấn dạng chữ. Thời lượng chỉ là ƯỚC theo nhịp đọc tự nhiên; kiểm «đọc to nghe một lần» vẫn là NOT TESTED nếu chưa thật sự làm trên đúng lời đó. **Không** sinh ảnh, TTS, still, render hay đăng trước Chốt (L-098); đặc biệt đừng chạy `build-final.py --stage plans` vì nó có thể gọi voice. Lúc duyệt lời gửi script + kế hoạch cảnh/motion dạng text.
- **Sau Chốt** = dựng `final/spec.json` từ đúng lời đã duyệt, đo thời lượng thật (< 300 s gồm end card), rồi TTS / hình / render (§2P trở đi). Mọi luật sản xuất sau Chốt giữ nguyên.

Repo: `oneup-studio` (local Mac checkout `/Users/macbook/work/oneup-studio`; toolchain `~/oneup-tools/` qua `pipeline/paths.py`).
Active checklist rút gọn: `rules/ACTIVE-CHECKLIST.md`. Draft QA gộp 1 lệnh: `python3 pipeline/scripts/check-rules.py --draft <script.md>`.
Reference implementation: `content/archive/clip-01-implementation-intention/final/` (spec, explainer template, script-final, post).

## 0. How Hiệp asks (intake)
| Hiệp writes | Agent does |
|---|---|
| `/make-video` alone, or `tiếp` / `làm tiếp` | **Resume first.** Scan `content/clips/clip-NN-*/` (skip non-`clip-` folders) and find each clip's last step from its files: drafts only in `archive/` → review/factcheck verdicts → `final/spec.json` (gate 1 pending) → Chốt noted in `revisions`/DL → render in `final/out/` or `media/clips/` (gate 2 pending). Take the lowest-numbered unfinished clip. Reply in 2–3 Vietnamese sentences: which clip, which step it's at, what changed since then that affects it (newer DL/lessons/rules, e.g. the 08/11 duration override), and the open decisions left for Hiệp. Then ask one go-ahead and continue from that step; never redo approved work. If nothing is unfinished, fall through to `Làm clip tiếp theo`. Hiệp never has to list sources, rules or logs in the prompt; step 1 below reads them. |
| `Làm clip tiếp theo` | next row in `content/theme-map.md` without a `final/` folder → its topic, theme, week |
| `Làm clip về <chủ đề / trend>` | pick the best Bridge for it in `research/trends/ingest.md` (or make one, rule-39) → map to a HowToLiveBetter lesson → next free clip id; theme by tone (rule-17) |
| `Làm lại clip-NN` / `clip-NN v2` | reuse `content/clips/clip-NN-*/final/spec.json`, add a `revisions` row |
| Optional add-ons in the same message | `tuần N` (default: theme-map week) · `có Omi` / `không Omi` · `dark`/`light` · `chuyện: S-xx` (story-bank id) |
Ask only what blocks a decision (rule: ask before deciding). Never invent a personal story; unknown details stay generic and go to the confirm list.

## 1. Read before writing (always, in this order)
-1. **`docs/conventions/storage.md` (rule-65) + `logs/lessons.md`** before ANY clip work: write every file to its canonical path (`pipeline/paths.py`); shared fonts/logo/sfx/voice-refs/characters/props live once in `brand/`, `assets/`, `video-engine/src/` (runtime copies via `pipeline/scripts/sync-shared.py`, gitignored); clip folder = script, spec, plans, timing, cover, preview only. `check-assets.py` must PASS. Step-by-step order: `docs/workflow/per-video-pipeline.md`. Lifecycle (rule-66): active clips in `content/clips/<clip>/`; after full post package + Hiệp says "duyệt" → `content/archive/<clip>/` + `final/approved.json`, renders in `media/clips/<clip>/` (full + 720p), then `media-sync.py` to the Mac.
0. **`logs/lessons.md` (rule-49)**: read every lesson; avoid each known failure in this clip. On ANY correction from Hiệp: first add/update the lesson (symptom in his words, root cause, fix, detection) and, if measurable, a `L-NNN` check in `pipeline/scripts/check-rules.py`; then fix; then re-run check-rules (✖ blocks review).
1. `AGENTS.md` → `rules/video-rules.md` (current version) → `logs/decision-log.md` (all DL, rule-33).
2. `content/voice-profile.md`, `content/story-bank.md`, `content/theme-map.md` (theme + week; Omi only week ≥ 5, rule-11).
3. `research/trends/ingest.md` + newest `research/trends/YYYY-MM-DD/` digest (+ `patterns.md`) → ≥1 trend phrase/situation (rule-37), note its id.
   - **TikTok-native (rule-57, L-037, skill trend-digest v4):** open `research/trends/<date>/apify/top-clips.md` + `clips.json` (url, views/likes/comments, music, hashtags) and `apify/vtt/*.vtt` (subtitles = exact spoken phrasing/delivery) → copy the ranked clips into `final/trend-signals.md`. Actors/config: `pipeline/trends/apify.yaml`; blocked actors listed in the skill (do not retry).
4. The HowToLiveBetter source section → write the **Fact lock** list.
5. `logs/effects-log.md` (avoid repeating signature effects back-to-back).

**These reads are for planning and checking, not for the writing pass.** They decide the topic, Fact-lock, trend and what the checker/reviewer will hold the script to. When you actually write the words (§2 step 4), open only the 4 clean inputs listed there (brief Gate 0 · `voice-profile.md` §2–3 · 2–3 closest approved scripts · story-bank row + explainer). The rules come back at §2 steps 7–8, §4 and §4b.

## 2. TRƯỚC CHỐT: Script Draft + Bảng khung mạch + ý Hình/Caption/nhấn (chỉ text)
Một nguồn duy nhất cho quy trình viết: **Master Writer Prompt `docs/prompts/writer-hi-oneup.md`** (đồng bộ với `docs/research/craft-brief.md`, `skills/script-polish/SKILL.md`, `rules/ACTIVE-CHECKLIST.md` §3b và `gate0.py`). Bản nháp nằm ở `final/script-vN-draft.md` (mỗi clip một file; bản cũ dời `archive/`). `final/spec.json` chỉ được dựng sau khi Hiệp nói Chốt. Thứ tự cố định:

**Bước 1. Gate 0 (chọn ý, Hiệp ~30 s).** Nạp brief bằng một lệnh và giữ nó ở đầu bản nháp:
`python3 pipeline/scripts/gate0.py --idea "<từ khóa ý>" [--arc ARC-NNN] [--tone story_warm|tech_sharp] [--memo media/voice-memos/<x>.txt] [--clip content/clips/<clip>/] --out <draft.md>`
Brief in: (1) ý từ `content/idea-bank.md` + fact package; (2) mạch `ONEUP-CORE-ARC` (mặc định @hi.oneup: hook tình huống → bẻ thước đo + gài trend → 1 bằng chứng → 1 việc tối nay → CTA; ~60–90 s, `--extended` 120–180 s chỉ khi chủ đề có nhiều bước kỹ thuật thật); (3) chi tiết thật: dòng `content/story-bank.md` khớp + nhắc bắt buộc `content/voice-profile.md` §2 (miền Nam nhất quán, cấm trộn «ấy/thế/nhé» với «hông/nha», hài 4/5 tự giễu, 1–3 từ tiếng Anh, lời nội tâm trích); 5 bản Hiệp đã duyệt (`a-c01…a-c05`) với 1 dòng DNA mỗi bản, đánh dấu 2–3 bản gần nhất; (4) góp ý mới nhất (`resources/feedback.md`, checklist, `final/feedback.md`). Mảnh in «chưa có» thì tìm trước khi viết, không bịa.
Rồi: sinh 15–20 góc, mỗi góc một kiểu hook khác (đọc `logs/hook-moves.md`, mã P trong `research/trends/patterns.md`); gieo từ chất liệu thật (comment/phụ đề trong `research/trends/<date>/apify/`, `audience-pain-bank.md`, `research/explainers/`, story-bank, fact-lock, `ARC-NNN`). Bỏ góc lặp bản bị bác của cùng clip (`check-rules.py --fresh`, L-095). Chọn top 3 so với bản duyệt trong `research/review-golden/index.json`. Gửi Hiệp 3 dòng: ý một dòng · câu hook · `ARC-NNN` · khác clip trước ở đâu. Hiệp chọn thì cộng 1 vào `uses` của arc trong `research/blueprints/index.json`. Chờ. Ghi `## Gate 0` ở đầu nháp và lời Hiệp vào `final/feedback.md`.
Ngay ở bước này chốt **1 câu hỏi trung tâm duy nhất** («clip này trả lời câu hỏi gì?»): hook và bằng chứng phải là câu hỏi và câu trả lời của cùng câu đó (**Single-Point Alignment**, chi tiết ở `skills/script-polish`). Khóa **Fact-lock**: danh sách được nói và danh sách CẤM (số/từ bị cấm, cơ chế não hay tâm lý ngoài nguồn). Chạm danh sách cấm là H1.

**Bước 2. Gate 0.5 Hook Arena (bắt buộc trước thân bài).** 70% thành bại nằm ở 15 giây đầu; không chốt hook đầu tiên nghĩ ra. Viết 4 mở đầu (hook + beat 2) theo 4 góc khác nhau: **Pain-Mirror** (cảnh bế tắc/xấu hổ thật của người xem, hạt giống từ pain-bank hay comment) · **Counter-Intuitive** (bẻ niềm tin ai cũng tưởng đúng) · **In-Media-Res** (nhảy vào khoảnh khắc đang xảy ra, rồi tua ngược nguyên nhân) · **Self-Mocking Story** (Hiệp tự giễu một chuyện thật trong story-bank). Đọc 4 mở đầu thành tiếng, chọn **Top 1 + 1 dự phòng**. **Luật 3 Giây Rõ Nghĩa:** `b01` ≤ 20 âm tiết (1–2 câu cực ngắn); người lạ nghe 3 giây đầu hiểu ngay chủ đề và thấy chuyện của mình. Trong Hook Arena, rõ nghĩa và trúng nỗi đau trong 3s luôn thắng việc tránh trùng dạng câu hỏi với clip trước. (`logs/hook-moves.md` chỉ để tham khảo.) Ghi bảng đấu ngắn ở `## Gate 0.5 — Hook Arena`. Không chấm vòng này bằng `cadence-patterns.tsv` hay `ai-blacklist.tsv`. Hook không dùng ngôn ngữ nghiên cứu («theo một thí nghiệm», «trung bình») và không mở bằng số báo cáo khô (L-101, L-103).

**Bước 3. Bảng khung mạch TRƯỚC khi viết lời (L-107).** Mỗi beat đúng một câu tóm vai trò (chuyện → câu hỏi → trả lời → giới hạn → áp dụng → kết). Đọc riêng cột này từ trên xuống phải ra một mạch nhân quả liền («vì / nên / vậy / nhưng»): không nhảy cảnh, không tự mâu thuẫn mốc thời gian giữa các beat; lời hứa ở hook được trả lời ngay beat sau. Đứt ở đâu thì sửa khung, chưa viết lời.

**Bước 4. Viết độc thoại một hơi như kể bạn thân giọng miền Nam.** Chỉ mở **4 đầu vào sạch**: brief Gate 0 (kèm Fact-lock và trend) · `content/voice-profile.md` §2–3 · 2–3 bản đã duyệt gần nhất · dòng story-bank khớp + `research/explainers/<topic>.md`. KHÔNG mở `bookish.tsv`, `ai-blacklist.tsv`, `connectors.tsv`, `cadence-patterns.tsv`, style-pairs, lessons hay `video-rules.md` (L-106: viết với ~37k chữ luật mở thì lời đi né luật chứ không giống người nói). Áp DNA @hi.oneup: một bối cảnh đời thường xuyên suốt; từ vựng miền Nam nhất quán; CTA là câu hỏi hỏi chuyện thật, không ép kiểu sáo rỗng. Mỗi câu sau trả lời câu hỏi câu trước vừa gợi. **Luật Chống Nhồi Nhét:** 1 vấn đề · 1 câu hỏi · 1 ví dụ đại chúng (tập thể dục, đọc sách, dậy sớm, học tiếng Anh…, không chuyện ngách) · dẫn chứng ≤ 2 câu (≤ 35 âm tiết) · rào giới hạn ≤ 1 vế ngắn (clip-02 «Mới thấy đi chung thôi», clip-05 «Nhưng năm mấy chục cũng đâu phải nhớ hết»). 5–6 beat, ~170–230 âm tiết, không beat nào > 42. Gia vị giọng Hiệp (tự giễu, lời nội tâm, từ EN, callback) chọn tối đa 1–2 thứ thật tự nhiên. Cấm tuyệt đối chuyển cảnh giả để chèn trend («đúng lúc đó mình lướt trúng câu đang trend…») và callback phi thực tế («đánh răng xong thì đăng đại một video»); trend nếu dùng là xương sống ngay Hook, gãy mạch thì xin ngoại lệ như DL-069. Prompt: `docs/prompts/writer-hi-oneup.md` (@vanhiep.tech: `docs/prompts/writer-vanhiep-tech.md`). Nếu Hiệp ghi âm 60–90 s thì chép bằng `voice-memo.py` và sửa từ chính lời ông (giữ ≥ 80%). Đủ ý thì dừng; cắt 25–30% những câu nói lại điều người nghe đã hiểu.

**Bước 5. Quy ước số ở bản nháp:** viết **chữ số bình thường** (`2010`, `96`, `18`, `254`) để đọc duyệt sạch mắt và không làm câu phình. Chỉ chuyển sang cách đọc (`say`: «hai trăm năm mươi tư») khi dựng `spec.json` sau Chốt.

**Bước 6. Tách beat + cột Hình / Caption EN / `{nhấn:}` (chỉ text, chưa render).** Chỉ sau khi độc thoại nghe như một người nói, cắt thành `N. **[bNN · vai trò]** lời` (đúng thứ `check-rules` `draft_beats` đọc; cũng đọc được `N. [Nhãn] lời` và bảng `| bNN | … | lời | … |`). Giữ nguyên chữ; câu cuối beat gieo beat sau. Dưới mỗi beat: `Hình:` (cảnh comic / hit motion + SFX gắn chữ nào), `EN:` (caption, chunk ≤ 8 từ, L-051), `{nhấn: …}` một chữ mỗi câu (L-031). Cái hình đã diễn thì lời không kể lại (rule-60, rule-61). Sau khi tách, đọc lại cột vai trò: vẫn phải ra mạch nhân quả (L-107).

**Bước 7. Cổng tự kiểm Ngữ nghĩa tiếng Việt bản địa + Chống văn dịch (trước khi gửi reviewer).** Đọc từng câu riêng lẻ, ghi vào nháp 4 dòng trả lời:
- (a) Người miền Nam ngoài đời có nói cụm này không, hay đây là cấu trúc dịch từ tiếng Anh? (bắt kiểu «đòi thấy nhẹ», «lặp một việc đơn giản», «giữ mức nhỏ nhất», «đang sắp bị bỏ», «chê sao hông nở»).
- (b) Hình ảnh ẩn dụ có đúng vật lý và đúng chủ ngữ của động từ không? (tưới cây vs hoa nở).
- (c) Mốc thời gian và số liệu giữa các beat có khớp không? (b01 «tối thứ 5 mới oải» thì b02 không thể «oải ngày đầu»).
- (d) Có câu nào gượng, hoặc nhại lại nửa câu trước chỉ để qua checker không? Có thì viết lại theo nghĩa tự nhiên, kệ cảnh báo mềm.

**Bước 8. Kiểm máy + reviewer độc lập, rồi mới trình Hiệp.**
1. `python3 pipeline/scripts/check-rules.py --draft <draft.md>`: bắt buộc **0 lỗi cứng ✖**. ✖ chỉ phát cho Tier-1 và ràng buộc nguồn/cấu trúc thật: H1 (`L-088`, `L-096` dẫn chứng không nguồn), H2 (ước ≥ 300 s), H3 (`L-053`), H4 (không đọc được beat / beat trống), cùng `L-087` (ví dụ môn học). Mọi check phong cách (`choppy`, `flow`, `link`, `repeat`, `clarity`, `bookish`, `ai-structure`, `connector-stuffing`…) chỉ là ⚠ tham khảo: **không hàn câu hay nhại chữ để xoá ⚠ nếu câu đọc lên mất tự nhiên**. `check-rules.py --audit` in lại bộ style để tham khảo.
2. `python3 pipeline/scripts/audio-precheck.py <draft.md>` (hơi dài > 32 âm tiết không dấu ngắt; mở beat lặp; `HOOK_LONG` b01 > 22 · `SLOW_ENTRY` b01+b02 > 65 · `BEAT_BLOAT` beat > 45 âm tiết; `--audition-hook` chỉ khi Hiệp muốn nghe thử).
3. **BẮT BUỘC** chạy Reviewer độc lập trong subagent mới, **khác model với người viết** (§4b). Xác nhận `python3 pipeline/scripts/check-rules.py --review <draft.md>` PASS (0 `HARD_FAILS`, `review.md` khớp `script_hash`, `final/feedback.md` tồn tại và `feedback_seen` bằng số góp ý) trước khi gửi Hiệp. Tối đa 2 vòng review; vẫn CẦN SỬA thì gửi Hiệp kèm các điểm còn mở thay vì lặp.
Sau khi Hiệp Chốt: dựng `final/spec.json` từ đúng lời đã duyệt (cùng lời ⇒ cùng `script_hash`, review còn hiệu lực), chuyển số sang cách đọc, rồi §2P trở đi.

## 2P. SAU CHỐT: `final/spec.json` + TTS / Visual / Render (nguồn sự thật duy nhất của sản xuất)
Từ đây mới sinh voice, hình, render. Mọi luật sản xuất dưới đây giữ nguyên.

**Script template (sau Chốt, Hiệp 16/10, clip-02 v16/v17):** write `final/script-final.md` from `templates/script.md` — beat frame Hook (cut) → problem stems → evidence + signs → spoken HTB message → 2 concrete how-to beats (source + linked items, optional callback to the previous clip) → CTA echo; table `Beat | Giây | Người nói | Lời thoại | Hình / caption EN` with `|` phrase splits and `{nhấn:}` marks (L-036).
Build the spec from the approved draft words (format below). Structure rule-41: hook 0–3s → struggle → turn → lesson/explainer → evidence → payoff → CTA question, last line loops to the hook. Target 60–180s at natural pacing; a finished story shorter than 120s stays short. Finished total strictly <300s including endcard, pauses and transitions. No hard word quota. Numbers are written as read aloud in `say` (e.g. 254 → "hai trăm năm mươi tư").
- Story beats = comic (`engine: remotion`); explain/evidence beats = motion graphics (`engine: hyperframes`), rule-42.
- Voice: "bạn", Southern particles on some (not all) lines, humor 4/5 aimed at habits, 1–3 English words.
- Every line: `speaker`, `emotion`, `text` (bubble, `**bold**` = emphasis), `en` (caption, English only), `hl` (indexes of highlighted EN words), optional `say` (phonetic spelling for TTS, e.g. TOEIC → "tô ích", numbers as read), optional `take`.
- **Voices (DL-035):** Hiệp = "F5 · Thái Sơn", Omi = "F5 · Mỹ Duyên" (F5-TTS, synthetic VieNeu references in `assets/voice-refs/`; checkpoint CC-BY-NC-SA, risk accepted by Hiệp — do not re-ask, but flag it if the channel starts direct monetisation). F5 runs on CPU ≈40–70 s per take × 3 takes per phrase: a historical 55–60 s clip took ≈ 60–90 min voice stage the first time (historical estimate, not a length limit or runtime promise) (cached afterwards, so revise per line, not whole spec). Leakage of the reference sentence ("hôm nay trời Sài Gòn…") at a take's start is auto-trimmed; check `leak_trims` in the voice JSON and re-listen if many. F5 v4 (DL-038, L-016 — v2/v3 word-level cutting still stuttered): the line is split ONLY at punctuation (. , ? ! … ; :) into clause units, each unit is a separate F5 call (units < 4 syllables are merged), audio is never cut inside an F5 output; pauses come from punctuation (`,` 180 ms, `.` 350, `?`/`!` 400, `…` 500). So **write phrasing with punctuation**: to add a pause or isolate a punch word, add `,` / `...` / `.` in the text. For F5 lines `phrases` only set caption chunks (`en`); `gap`/`tempo`/`semi`/`emph` are ignored. Units and their seeds/scores are in the voice JSON `units`; check-rules L-016 fails any intra-output cut.
- **Voice prosody (required for new lines, DL-033):** give every line `phrases` so it sounds human, not read. `build-final.py` then voices it with `pipeline/scripts/voice-prosody.py` instead of the old sentence+stretch path:
  `"phrases": [{"t": "Kế hoạch học tô ích của mình là...", "gap": 0.42, "tempo": 0.96, "semi": -0.3}, {"t": "mai học.", "emph": true, "en": "…"}]`
  0. **Naturalness markup (DL-039, cheat-sheet in `content/voice-profile.md` §3c):** punctuation drives delivery (`?` rise, `!` energy, `…` trail, `—` interruption, `( )` quieter aside); fillers `{ừm}` `{ờ}` `{à}` `{ơ}` `{hừm}` `{ủa}` `{trời ơi}` `{thì là}` (spoken inside the next unit), `{bank:ừm}` (cached filler clip between units), `{ngập ngừng}`, `{kéo: nha}`. Particles are read plain by default (Hiệp prefers plain, DL-040/L-018); `{kéo: …}` lengthening is optional, explicit only, ≤ 1 per clip. Caps: ≤ 1 filler/line, ≤ max(2, lines/4)/clip (check-rules L-017). Markup only in `phrases[].t`, never in `text`/`en`.
  1. Split into breath groups of 3–8 syllables; keep each phrase's own punctuation (`...` trails off, `?` rises, `,` continues, `:` sets up). Never phrases of 1–2 syllables except a particle/interjection (`Ủa?`, `Nè,`).
  2. `gap` after each phrase 0.15–0.42 s (comma ≈0.18, colon ≈0.26, ellipsis ≈0.38, before the punchline ≈0.4). Gaps are filled with room tone.
  3. One `emph` per line (the punch word/phrase) → slower, +0.8 st, +1.5 dB. For a falling statement end use `"emph_semi": -0.5` (otherwise it can sound like a question).
  4. Vary `tempo` (0.9–1.08) and `semi` (−0.5…+1.2): question/tease up, tired/sad down. Particles (á, nha, hông, ủa, nè) at phrase ends or as a lead-in, max 1–2 per line, and keep them inside a ≥3-syllable phrase (alone they get mangled).
  5. Don't use `[cười]` / `[thở dài]` tags (VieNeu or F5): STT showed they get spoken as words ("Thì…", "hờt"). Show the laugh/sigh in the face instead.
  6. The script picks the best of 3 takes per phrase (STT ≥ 0.7 gate, F0 range, artifacts), checks the whole line by STT (toneless ≥ 0.92) and re-rolls weak phrases; a `warn: … line STT sim` in the build log = rewrite the phrase or the `say` spelling.
  7. Optional per-phrase `en` = caption chunk timed to that phrase (better sync than one EN line spread evenly).

```jsonc
{ "id": "clip-NN-final", "clip": "clip-NN", "title": "…", "week": 1, "theme": "light", "pillar": "…", "trend": "<ingest id>",
  "revisions": [{ "date": "YYYY-MM-DD", "dl": "DL-0xx", "note": "…" }],
  "parts": [
    { "id": "A", "engine": "remotion", "transitionOut": "slideleft",
      "scenes": [{ "id": "b01", "beat": "clip-NN.b01", "part": "hook", "background": "bed|desk|paper|grid|ink",
                   "framing": "medium", "push": 0.05, "transition": "cut|slide|iris|fade|wipe", "narration": "11:48 PM",
                   "cast": [{ "id": "hiep", "x": 0.5, "pose": "sitting", "action": "idle", "expression": "sad", "facing": "right", "enter": "pop" }],
                   "lines": [{ "speaker": "hiep", "emotion": "sad", "text": "…", "say": "…", "en": "…", "hl": [4],
                               "set": { "omi": { "expression": "happy", "action": "reacting" } } }],
                   "sfx": [{ "name": "pop|ding|whoosh", "atLine": 0, "offset": 0 }] }] },
    { "id": "E", "engine": "hyperframes", "dir": "explainer", "transitionOut": "circleopen",
      "sections": [{ "id": "e01", "beat": "clip-NN.b05", "part": "explain|evidence", "motion": "<awesome-ai-motion slug>", "lines": [ … ] }] },
    { "id": "B", "engine": "remotion", "scenes": [ … last scene part: "cta" … ] }
  ] }
```
**HyperFrames skills (required, rule-42, DL-032).** Before writing or editing any `engine: hyperframes` beat, read `skills/hyperframes/README.md` and then in order `hyperframes/SKILL.md` (router), `hyperframes-core`, `hyperframes-animation`, `hyperframes-creative` (brand rules win on palette/font), `hyperframes-registry` (check for a block before hand-building), `hyperframes-cli`. Run `npx hyperframes lint` (Node ≥ 22) on the explainer before rendering. Open gaps in the clip-01 reference: `logs/hyperframes-audit-2026-10-13.md`.

Explainer visuals: copy **`content/samples/sample-natural/explainer/`** (the lint-clean reference, DL-033: host `index.html.tpl` + one sub-composition per section in `compositions/<eNN>.html.tpl` + `compositions/captions.html.tpl`). Every `*.tpl` receives `__TIMING__`, `__DUR__` and per section `__START_<id>__` / `__DUR_<id>__`, used as the section host's real `data-start`/`data-duration` (the runtime hides it outside its window; never fake visibility with opacity). Inside a section: animate children with `fromTo` (never the clip, no CSS transform on tweened nodes, no exit tweens except the last scene), convert times with `t - __START_<id>__`. Captions = brand-styled adaptation of registry `caption-pill-karaoke` (group ≤4 words, karaoke step, hard-kill at group end), host carries `data-track-kind="captions"`. Section-to-section transitions: `hyperframes-animation/transitions/catalog.md` (push slide primary). Gate: `npx hyperframes lint` **and** `npx hyperframes check` must both report 0 errors / 0 warnings (build-final runs lint before rendering). GSAP local, Be Vietnam Pro.
Motion: run `skills/motion-picks-per-script` → one main effect per beat (`motion` field + table in script-final.md) → append to `logs/effects-log.md`.
**motionmaxxing (Remotion, rule-42):** craft laws + measured eases live in skill `skills/motionmaxxing` (symlink → `resources/refs/motionmaxxing/`, see `INTEGRATION.md`). Timing/ease picks use Remotion ports `video-engine/src/composition/motionmaxxing/` — set scene `transition: "mmx-…"` (e.g. `mmx-soft-land`, `mmx-snap-settle`, `mmx-oversize-land`, `mmx-cut-on-motion`) or call `mmxStyle/mmxEase` for an element; `tdev-*` stays first for UI-style transitions. Craft laws: land decelerates / leave accelerates, almost no scene fades, ≤1 visible spring per clip, cut on motion. Notes: `research/references/motionmaxxing-notes.md`.
**Meaning-by-objects, NOT word-drawing (L-050, APPROVED by Hiệp 18/10 «Tạm được»):** when a concept needs visual explanation, show **OBJECTS + ACTIONS + SCALE** that express the meaning — a pile growing taller than Thầy = «ngợp / việc to», that pile becoming 3 tidy bundles Thầy can carry = «chia nhỏ», Thầy carrying one small box past a big clock whose hand sweeps = «mười lăm phút», a thick calendar stack + dusty weight = «để cả năm». **NEVER draw/write the word itself**: no handwriting-path text, no decorative circle/underline/tick overlays on signs/captions (the caption + highlight already say the word). Reuse existing props first (incl. `pile/bundles/bundle/clock/dusty` from L-050); objects are filled brand props (paper #F7F7F5 / ink #111111 / accent #FF5A36 only, ≥60% frame width), never stroke-only sketches beside filled characters. **Old animation language stays primary**: persistent objects that enter, stay and transform in-scene, tdev/mmx easings, timing locked to the spoken phrase + SFX (as in locked clips 01–03). **Stills approved by eye before any render** (read stills at start/mid/end of the beat; a fuller frame that says less = reject).

**Doodle gate (research/references/doodle-audit.md §5, accepted 18/10): stroke doodle is BANNED by default.** Only allowed when ALL hold, stated in the beat's fx table: (1) the beat's content IS an act of drawing/writing/cutting/connecting/a path — removing the stroke removes meaning, not just emphasis; (2) it draws on an object already existing in the scene, which persists or transforms into the next object (no invented prop to draw on, no floating stroke in empty space); (3) it uses the running scene's tdev/mmx easing and locks `at` to the spoken phrase + SFX like existing `dropAt`s (no separate doodleEase); (4) max 1 drawn moment per clip unless the script truly needs more and Hiệp approves first. The 4 doodle demos + b06 crack test are rejected references — keep them to remember why, never use as standard.

### 2a. Script voice + structure (rule 64; writing-time summary now in `docs/research/craft-brief.md`, which replaces `docs/research/script-prompt-principles.md`)
- **Meme stem delivery (L-036, trend «bản chất», `research/trends/2026-10-15/audio/delivery-analysis.md`):** every meme line = **opener stem | content payload** split with `|` (e.g. `Thứ hai là {nhấn: khi nào} | xuất hiện cái cảm giác khó chịu | … thì phải đổi việc liền.`). Stem words (`Thì cái bản chất`, `Thứ nhất`, `Thứ hai`, `Và cuối cùng`) slap +1 st; the payload gets exactly one `{nhấn: …}` (slow .78, +0.8 st, +1.5 dB, stretched) and the line end falls (−1.5 st), never rises. Keep stems verbatim from the trend audio; break long payloads into 2–3 phrases of ≥4 syllables. `check-rules` L-036 errors on a flat stem line.
- **Voicing {nhấn:} lines:** `python3 pipeline/scripts/build-final.py <spec> --stage voice-phrase` runs `voice-phrase-f5.py` gen → F5 (2 seeds/phrase, 2 parallel batches) → STT pick + emphasis edits → stitch to `video-engine/public/voice/<voice_prefix>-<line>.wav` (+ `final/voice-stt-<prefix>.json`, L-016 exception). Set `spec.voice_prefix` (e.g. `v18`). `--stage all` runs it automatically when the spec contains `{nhấn:` and no cached `voice-stt-<prefix>.json`; specs without `{nhấn:` keep the old `voice-prosody.py` path.
- Structure in `spec.structure`: Hook (≤2 sentences, opens an info gap) → Intro (why keep watching, open loop, callback prior clip) → Body (problem → exploration w/ real study + caveat → climax/how-to) → 1-sentence summary answering the hook → ONE CTA shorter than a sentence.
- Hook type: direct (name the specific thing), controversy ("điều không ai nói về…", back it up), or negative ("Đừng…"). Never generic. Always add `hook_alt` of another type.
- **Default check for hook and angle** (adapted from mankidev/antialgorithm, MIT). Before writing the hook, put one line in the draft notes: "default hook here is X", meaning the hook any creator would write on this topic. Use X only if this clip's story-bank or source fact asks for it. Move away using a fact that belongs only to this clip (Hiệp's real moment, the study's odd detail, the trend's exact wording), not by flipping the cliché into its known opposite. Give each choice a one-sentence reason drawn from this clip. Test: if the hook could open another clip unchanged, rewrite it.
- **Options differ in kind.** When offering hooks or angles at gate 1, make them different moves (a real failure moment, a number, a direct "Đừng…", a quoted self-promise), not rewordings of one. If one is the safe pick, label it. Recommend one, with the reason.
- **Hook-move log** `logs/hook-moves.md`. Read it before choosing the hook. If the main move matches either of the last 2 clips, pick another kind or state in the notes why this clip needs it. After gate 1 approves, add one row: clip, hook text, the move in a few plain words.
- Voice: Hiệp telling a friend a real story; Southern particles; idioms/metaphors/anecdote; words a 12-year-old gets; one `{nhấn: …}` per sentence; visuals stay in the action column. Read aloud: anything you'd never say to a friend gets rewritten (anti "giả trân").

## 3. Polish (lời trước Chốt; áp lại trên `text`/`en` của spec chỉ khi Hiệp sửa lời)
Run `skills/script-polish` (humanizer + voice profile) on `text`/`en`. Fact lock unchanged. Personal stories: invent plausible comic details (rule 67); never ask Hiệp to confirm. Numbers/research stay real (rule 40).

## 4. Automated rules gate (SAU Chốt: bước `--stage plans` gọi TTS)
```bash
python3 pipeline/scripts/build-final.py <clip>/final/spec.json --stage plans   # TTS (cached) + timing.json + plans + explainer html
python3 pipeline/scripts/check-rules.py <clip>/ --stt                          # must PASS (0 ✖) before gate 1
```
`check-rules` covers: finished total <300s including endcard/pauses/transitions, 120–180s target warning only, no hard total-word quota, hook/CTA, scene ≤ 8s, Omi week (rule-11), theme vs theme-map, beat ids, comic vs motion engine, EN-only captions + highlight indexes, no emoji, Be Vietnam Pro only + no CDN, no music, SFX allowed + sourced, every transition has an SFX + ambience bed (rule-50, DL-042: default whoosh-soft at part xfades, swish at scene/section changes, 0.12s lead, quiet; continuous ambience; never music), content-specific motion + accent SFX on marked hits (rule-51, DL-043: section `hits: [{id, f, sfx}]` → template `H(id, hit)` + mixed SFX at the same time; scenes use `sfx`; ≤3 per section), AI-tell phrases, particles / "bạn" / English mix, unconfirmed story items, voice presets (no cloning), STT of every line, post package (credit + license link + "đã chuyển thể", AI toggle + disclosure), video-engine validator; with `--final` also MP4 spec, −14 LUFS, contact sheet. A line failing STT: fix `say` or bump `take`, rebuild.

## 4b. Claim check + score (before gate 1)
**Reviewer độc lập là BẮT BUỘC (§2 bước 8).** Ngoài Tầng 1 (H1–H4) và Pairwise 4 trục, reviewer soi **Điểm mù 5: sai ngữ nghĩa tiếng Việt / văn dịch (translationese) / tự mâu thuẫn nội bộ giữa các beat** (một lỗi rõ là `PAIRWISE: LOSE` + `CẦN SỬA`) và DNA kênh theo `voice-profile.md` (Trục 3); chạm danh sách CẤM của `fact_lock` là `H1`. Xem `docs/prompts/reviewer-script.md`.

**Run it in a fresh subagent, not in the writing session (26/11).** A model grading its own draft is lenient (self-preference; it also remembers why each line was written). Spawn a fresh subagent with the Agent tool, `model` different from the writer's (default `sonnet`), and give it only the prompt `docs/prompts/reviewer-script.md` with `{DRAFT}` = the draft path, `{CLIP_DIR}` = the clip folder and `{GOLDEN}` = `research/review-golden`; never the writer's reasons. It writes `final/review.md` (adds `reviewer_model`). The writer must not edit `review.md`; it only fixes the quoted lines. **At most 2 review rounds**; if still CHƯA ĐẠT, send Hiệp the draft with the open issues instead of looping. Self-review by the writer is a fallback only when no subagent can be spawned, and `review.md` must say so. How well the reviewer matches Hiệp is measured with `pipeline/scripts/review-eval.py` on `research/review-golden/` (result table in its README).

Taken from the old box agents Deep Research and Rule Reviewer (`docs/legacy-box/workflows-agents/`, retired 26/11). Run it after §4 passes, on every draft, and again when Hiệp sends a single script or a vX fix. Write the result to `final/review.md`, front-matter `title, date, type: review, tags, status: draft, source, verdict, score, script_hash, feedback_seen`. `script_hash` = the value `check-rules` prints: a hash of the spoken VI words only (markup and punctuation ignored, tones kept), so the draft and the later spec give the same hash; any wording change makes the review stale. Before the spec exists, check with `check-rules.py --review <clip>/final/script-vN-draft.md`; it also requires `final/feedback.md` to exist and `feedback_seen` to equal its row count. `feedback_seen` = number of rows in `final/feedback.md` the review has answered, one by one. Never edit the script inside this step, only quote lines and propose replacements.

1. **Claim table.** Every research claim in `text`/`en` (number, mechanism, "nghiên cứu cho thấy…", effect size) gets one row:

   | Claim (as allowed to say) | Original source (author/year + matching passage) | 2nd independent source | Confidence | Allowed wording | Banned wording |
   |---|---|---|---|---|---|

   - Open the original source and compare the exact passage (TinyFish fetch: MCP `fetch_content` or `python3 pipeline/scripts/tinyfish_client.py fetch <url>`; find it with `tinyfish_client.py search`); a search snippet or a source that won't open does not count.
   - Confidence: `cao` (original + ≥1 independent source agree), `vừa` (original only, or a moderate/conditional effect), `chặn` (secondary only, conflicting, or unreadable).
   - Keep 3 kinds apart: study result · speaker's inference · everyday illustration. An illustration (rule 67 comic detail, L-052) never carries a study number.
   - Say effects at the source's strength (g = 0,499 = "mức vừa"; banned: "chứng minh", "hơn hẳn", "nhớ hết", L-045). Any `chặn` row blocks gate 1 until the line is cut or reworded to what the source supports.
**Two tiers — Hard-Gate + Pairwise A/B (replaces absolute ≥85 score threshold).** Tier 1 hard fails (`H1–H4`) are the **sole hard blocker** for Gate 1: H1 fact without source / beyond the source · H2 estimated total ≥ 300 s (L-099) · H3 wrong brand/format for the channel or belittling the viewer (L-053) · H4 broken draft/spec structure. Tier 2 compares the draft side-by-side (**Pairwise A/B**) against the newest approved anchor clip from `research/review-golden/` across 4 relative axes (`Hook & Giữ chân`, `Mạch truyện & Chuyển ý`, `Văn nói tự nhiên VN`, `Độ đắt của ẩn dụ/payoff`) and ends with the 5-line block `HARD_FAILS / PAIRWISE / TOP_FIXES / CONFLICTS / VERDICT`; `pipeline/review_tiers.py` recomputes the verdict from it and `check-rules --review` hard-blocks only on Tier 1 `HARD_FAILS` (while `PAIRWISE: LOSE` with 0 hard fails warns with `TOP_FIXES`). Measured on the golden set by `pipeline/scripts/review-eval.py --mode pairwise`.

2. **Score** with `logs/rule-scoring-rubric.md` §3 (A Hook 20 · B Flow 15 · C Clarity 20 · D Fact 15 · E Length/caption 15 · F Tone 10 · G CTA/gate pack 5). Every deduction quotes the line. Measurable items come from `check-rules` output; mark the rest as manual reading, never as automated.
3. **Hard gates** (rubric §3b Tier 1: H1–H4; voice/render/publish before Chốt is a process error caught by `check-rules`). One hit = not ready, whatever the total. The old gate «hook must be "bạn" + question» is no longer a hard gate: a first-person story hook (L-103–L-105) and a "bạn" + pain + question hook both score full A when done well.
4. **Open conflicts** between rules (rubric C-1/C-3, checklist X-0N, or a rubric anchor vs a newer DL/lesson, e.g. hook-shape gate vs `logs/hook-moves.md` variety): list both sides, don't fix toward one side.
5. **Verdict** at the top of `review.md`: `ĐẠT — trình gate 1` (≥85, 0 hard gate, 0 open conflict) · `CHƯA ĐẠT — sửa nhỏ/vừa/lớn` (75–84 / 60–74 / <60: fix those lines, re-run §3–§4b, don't send yet) · `ĐẠT VỀ ĐIỂM — chờ Hiệp quyết <conflict>`. The thresholds and weights are still the rubric's proposal (§6); use them as the default until Hiệp changes them, and say so in `review.md`. **Enforced:** `check-rules.py content/clips/<clip>/` fails (✖ `review`) when `review.md` is missing, its `script_hash` doesn't match the current words, `feedback_seen` is below the rows in `final/feedback.md`, or `verdict` is CHƯA ĐẠT; ĐẠT VỀ ĐIỂM is a ⚠. `--review <draft.md>` runs the same check on a draft.

## 5. Review gate 1 (Hiệp): script
Send `final/script-final.md` (beat table: **beat · time · visual · VI line · EN caption · voice emotion**, motion picks, fact lock, confirm list) + the `final/review.md` verdict line, score and any open conflict + storyboard contact sheet (`storyboard/` or a draft render's `contact-sheet.png`) + one-line summary of voices/theme/week. Stop and wait.

### 5b. Học style-pairs sau khi Hiệp sửa lời (trước Chốt)
Khi Hiệp sửa lời thoại ở Gate 1 và **chưa** nói Chốt (comment theo beat, bản gửi lại, hoặc câu ông khóa khác câu trong nháp đã gửi):

1. Giữ nguyên file nháp trước sửa. Đối chiếu từng câu ông đổi với câu ông chốt.
2. Chọn **1–2 cặp đắt nhất**: nhịp nói đổi rõ, hình mắt thấy tai nghe thay câu trừu tượng, hoặc cụm AI/văn viết bị cắt. Bỏ cặp chỉ sửa chính tả hoặc đổi một từ không đổi giọng.
3. Thêm vào bảng `resources/vn-spoken/style-pairs.md` với id `SP-NN` kế tiếp, cột: kênh · chủ đề · **Bản nháp trước sửa** · **Bản Hiệp chốt** · vì sao tự nhiên hơn (ghi clip + lesson nếu có) · `tone` (`story_warm` nếu câu chốt có «mình»/«bạn» và nhịp kể ấm; `tech_sharp` nếu nhịp chặt hoặc tech). Cập nhật `updated` trong front-matter.
4. Không chép hai câu đó nguyên văn vào clip sau. `gate0.py` tự lấy 3 cặp gần chủ đề nhất cho brief kế. Bài `story_warm` truyền `--tone story_warm` để không nạp mẫu chặt chém. Học cách biến đổi, không học câu.


**Effects table, required at gate 1 (rule 52, DL-044, L-019).** Plan every effect *before* any render, so late requests don't cost extra re-renders. When drafting `spec.json`, fill in:
- `fx: {visual, word}` on every scene and section. `visual` is a content-specific metaphor or motion, including comic beats. `word` is the spoken word it lands on.
- `hits: [{id, f, sfx, word}]` on every explainer section (≥1, ≤3).
- `sfx: [{name, atLine, offset, word}]` on comic accents.
- `transition_sfx: {part: "whoosh-soft", scene: "swish"}` at clip level.

Then run `python3 pipeline/scripts/fx-table.py <clip>/final/spec.json --write`. It writes this section into `script-final.md`:

```
## Bảng hiệu ứng (rule-52, duyệt ở gate 1 trước khi render)
| Beat | Engine | Hiệu ứng / ẩn dụ hình ảnh | Gắn với chữ | SFX nhấn → chữ | Chuyển cảnh vào (+SFX) |
|---|---|---|---|---|---|
| e05 | hyperframes | Số 94 đếm lên, thước đầy tới vạch d = 0.65 | “chín mươi tư” | `rise` → “chín mươi tư”; `ding` → “vừa tới lớn” | push (`swish`) |
```

`check-rules <clip>/` (pre-render, no `--final`) blocks with rule-52 if any beat lacks `fx`, a word isn't in the line, an explainer has no hit+SFX, `transition_sfx` is missing, or the table misses a beat. Hiệp approves the table along with the script. Do not render before that.

## 6. Render + self-review
```bash
python3 pipeline/scripts/build-final.py <clip>/final/spec.json        # voice → plans → Remotion + HyperFrames → join, SFX, grain, −14 LUFS
python3 pipeline/scripts/build-final.py <clip>/final/spec.json --stage assemble   # mix/SFX only, reuses rendered parts (no re-voice/re-render)
ffmpeg -i <clip>/final/out/<id>.mp4 -vf "fps=1/2,scale=216:384,tile=8x4:padding=6:color=0x111111" -frames:v 1 <clip>/final/contact-sheet.png
python3 pipeline/scripts/check-rules.py <clip>/ --final --stt --out <clip>/final/check-rules.txt
python3 pipeline/scripts/gate2-qa.py <clip>/   # multimodal Gate 2 QA (skills/video-qa) → <clip>/final/gate2-qa-report.md
```
Look at full-size frames of every beat at least 2 rounds (rule-34): text inside safe area, nothing clipped, captions not covering faces, highlight on the right word, logo present. Fix in spec/template, add a `revisions` row, rebuild.

**Cover (rule 54, DL-046).** At the script stage, put `cover` props into `spec.json`. Use template A (`video-engine/src/composition/Cover.tsx`), with these fields:
- `direction: "a"`
- `theme` (rule 17)
- `series`, `ep`
- `hero` [old, new] with `strike: 0` and `accent: 1`
- `expression`, `action`, `emote`, `tilt`

Render a draft for gate 1 with `cd video-engine && npx remotion still src/index.ts Cover ../<clip>/final/cover.png --props="$(python3 -c 'import json,sys;print(json.dumps(json.load(open(sys.argv[1]))["cover"]))' ../<clip>/final/spec.json)"`. Keep a copy as `final/cover/cover-a.png` plus `cover-a.props.json`. Never use a video frame. `check-rules --final` blocks on rule-54 and L-020.

**Hook 0–3s (rule 55, DL-051).** Put `spec.hook = {text, scenes}`. The first scene narration must equal `hook.text`, which build-final shows from frame 0. Build the hook from 2–3 `cut` scenes marked `part: "hook"` (lead 0.06s, tail 0.15s). Use short repeated clauses (first clause ≤ 6 words), a strong push/zoom, stamp/click hits and an emotional voice. Never open with a neutral setup sentence. Needed: first word ≤ 0.3s, first visual change ≤ 1s, ≥ 2 cuts/hits (≥ 1 cut) in 0–3s. `check-rules` rule-55 blocks.

**Engagement (rule 56, DL-052).** Put `spec.engagement = [{type, beat, text[, hook_word]}]` with ≥ 3 types. comment-challenge (one word) and loop (last line repeats the hook keyword) are required. Add relatable-question ("Nghe quen không?") and/or save-prompt ("Lưu lại, lần sau … mở ra"). The pinned comment continues the challenge. Never beg ("like đi", "nhớ follow", "xin like"…). `check-rules` rule-56 blocks.

**Trend layer (rule 57, DL-053).** Before gate 1, write `final/trend-signals.md`. It needs TikTok clips on the topic ranked by views plus comments (VN first), with URL, views, comments and the beat where each trend is used. Use YouTube as a labeled proxy if TikTok blocks the box. List rejected trends with the reason. Weave the trend into the hook, cover and caption. `check-rules` rule-57 warns.

**Continuous story and sharp words (rule 58, DL-059).** Every non-hook beat opens with a connector or a callback (thế là / rồi / nhưng / hóa ra / tức là / bằng chứng / vì… nên / vậy / nếu / còn / ngược lại / phần mình). Never use vague shorthand ("điện thoại thắng", "một cảm giác", "mọi thứ"); write the concrete image instead. Run `python3 pipeline/scripts/vn-words.py --spec <spec>` and pick sharper words from `resources/vn-dict/thesaurus.md` (all checked against Viet74K). Keep each clause ≤ 12 words and put `hl` on the strongest word. Check saturation in today's `research/trends/*/patterns.md` before choosing the hook angle. `check-rules` rule-58 blocks.


**Post package (rule 53, DL-045).** Copy `templates/post-package.md` to `final/post.md` and fill in all 12 sections, each in its own code block:
- file specs;
- cover text (≤40 chars), the cover frame time, and `cover.png`. Export it with ffmpeg: grab the frame, then drawtext with BVP Bold on a #111 band;
- caption: hook first line, "bạn" voice, ≤2200 chars, SEO keywords, hashtags at the end;
- 3–5 hashtags taken from current VN trend data, with sources, no spammy tags;
- SEO keywords;
- pinned comment;
- VN posting time, with sources or flagged as default;
- sound note (Commercial Music Library, music at 5–10%);
- settings checklist (AI toggle, duet/stitch, audience, no location, commercial OFF, playlist);
- CC BY 4.0 credit;
- series;
- AI label.

Also write `post-checklist.md`. `check-rules --final` blocks on any gap.

## 7. Review gate 2 (Hiệp): final
Send the MP4 + `post.md` (caption VI in "bạn" voice that asserts no unconfirmed fact, hashtags, HowToLiveBetter CC BY 4.0 credit + license link + "đã chuyển thể", AI toggle + disclosure line naming the characters who speak, exact form: "Giọng của Hiệp (nhân vật) và Omi trong video là giọng AI tổng hợp (F5-TTS)." — rule-46/DL-035, check-rules errors if "F5-TTS" is missing) + `check-rules.txt` summary + confirm list. Agent never posts.

## 8. Feedback loop
**First, before anything else:** append a row to `final/feedback.md` (create it with front-matter `title, date, type: feedback, tags, status: living, source` and the table header if missing):

| thời gian | bản (commit) | lời Hiệp nguyên văn | đã xử lý ở |
|---|---|---|---|
| 2026-11-26 06:55 | 8df074e | «Các câu văn vẫn rời rạc…» | (điền khi sửa) |

Quote him word for word, never a summary. The reviewer (§4b) reads this file and must answer every row; `check-rules` blocks gate 1 while `feedback_seen` < rows. A note repeated twice still becomes a lesson (rule-36).

Hiệp gives feedback by beat id, one per line:
```
b03: đổi câu "…" thành "…"
b05: chậm lại / chữ to hơn / bỏ hiệu ứng
e03: số liệu sai → …
all: giọng Omi nhanh quá
```
For each: add `DL-NNN` (quote him) → edit `final/spec.json` (line text/emotion/take, cast, sfx) or `explainer/index.html.tpl` → append `revisions` → rebuild only what changed (TTS cache by text+preset+emotion+take) → steps 6–7 → commit `clip-NN: … (DL-NNN)`. Same feedback twice → promote to a rule or this skill (rule-33).

## 9. Close out
Copy deliverables if asked; `python3 pipeline/scripts/build-index.py`; commit; push (or bundle when the Mac is offline, AGENTS.md). Media stays out of git (`final/out/` is ignored).

## Requirements
- Read this skill before acting; follow linked channel/repo AGENTS.md when cited.
- Use tools and paths named in the steps; do not invent alternate pipelines.

## Limitations
- Comic/motion series only (DL-027); not for @vanhiep.tech CapCut A-roll.
- Do not regenerate from scratch on feedback — edit `spec.json` / script and re-render.
- Pre-Chốt: no TTS, images, or video render.

## Troubleshooting
| Error / symptom | Cause | Fix |
|---|---|---|
| check-rules fails | Spec/script violates a numbered rule | Read finding → edit source → re-run check |
| Duration ≥300s | Endcard/pauses pushed total over hard limit | Trim beats or pauses; remeasure finished cut |
| Wrong channel workflow | Request was for talking-head CapCut | Use `channels/vanhiep-tech` skills instead |
