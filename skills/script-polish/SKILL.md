---
name: Script polish (VI voice)
description: >-
  Use after a short-form video script is drafted (facts checked) and before it goes
  to the creator for approval: remove AI-writing tells with the vendored humanizer
  skill, adapt to spoken Vietnamese, and match the creator's voice profile, without
  changing any fact, number or citation.
---
# Script polish (VI voice)

## Inputs
- Draft script (VI voice lines + EN captions).
- `content/voice-profile.md`: the creator's voice. Its samples override generic rules.
- `skills/humanizer/SKILL.md`: the pattern list. Apply it in "embedded mode".

## Steps
1. **Fact lock.** List every fact, number, study, date and citation in the draft. These must appear unchanged in the output.
2. **Humanizer pass** on the VI lines and EN captions. The structural tells apply in any language. In Vietnamese, watch for:
   - "Không phải X, mà là Y" used just for emphasis.
   - Triads ("nhanh, gọn, hiệu quả").
   - Closers that only repeat the point ("Và đó chính là chìa khoá.").
   - Inflated words: "bí quyết", "thay đổi cuộc đời", "đỉnh cao", "chìa khoá vàng".
   - Staged openers: "Bạn có biết…", "Hãy cùng tìm hiểu…".
   - Every sentence the same length.
3. **Spoken VI pass.**
   - Write the way people talk: short phrases, natural particles where the profile allows (nha, á, thôi, đó). Don't put one on every line.
   - Use the profile's pronouns (mình/bạn by default).
   - Numbers are written the way they are read aloud ("chín mươi tư").
   - Leave room to breathe: mark `/` for a short pause.
4. **Voice pass.**
   - Use only the creator's real phrases, examples and level of humor from the profile.
   - Never invent a personal story. If a line needs one, insert `[VÍ DỤ THẬT CỦA HIỆP: ...]` as a placeholder.
5. **Trend check (rule-37).** At least one current phrase or situation from `research/trends/ingest.md` must stay in the script, used naturally.
6. **Diff + verify.** Output the old and new lines side by side, list the facts and confirm each is unchanged, and keep the target length (55–60s ≈ 150–170 Vietnamese words).
7. Save as `script-vX.Y-draft.md` next to the approved version. Never overwrite the approved script until the creator approves.
