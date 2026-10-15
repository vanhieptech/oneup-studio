---
name: Motion picks per script
description: >-
  Use when a short-form video script is approved (or drafted) and you need to
  choose motion/animation effects that fit THAT script's content, beat by beat,
  from the awesome-ai-motion catalog, transitions.dev ports, and motionmaxxing measured eases — instead of reusing a fixed effect set.
---
# Motion picks per script

Catalog: https://github.com/gongnyang/awesome-ai-motion (MIT). Clone to `resources/refs/awesome-ai-motion (clone, xem resources/refs/README.md)` if missing. Machine-readable index: `index.json` (`effects`[637], `recipes`[11], `routes`[7], `glossary`). Cards are mostly Korean with `en` names; read the per-effect folder under `effects/` for full params and demo mp4.

## In-house catalog (Remotion-ready, pick these first for transitions)
`video-engine/src/composition/transitions/catalog.json`: 8 frame-driven ports of transitions.dev (source tag `transitions.dev`, commit 8c92530): tdev-modal, tdev-page, tdev-panel, tdev-text-swap, tdev-icon-swap, tdev-stagger, tdev-badge, tdev-shake. Set scene `transition: "tdev-…"` or call `tdevStyle(name, p)` for an element. Plus built-ins cut/fade/slide/wipe/iris. Demo: `media/samples/lab/transitions-demo/transitions-demo.mp4 (+ .png contact sheet)`. In motion-spec.md write the slug with `(transitions.dev)`.

## Steps
1. **Read the inputs:** the script (beats with timestamps and spoken lines), the channel's video rules file (format, caption style, brand, banned effects, free/real-footage limits), and the route guide for the format (shorts: `routes/쇼츠.md` — 9:16, hook in 1–3s, bottom ~20% safe area, contrast, no flashes, one main effect per beat).
2. **Tag each beat by intent.** Map to catalog `purposes`:
   - hook / pattern break -> 주목 끌기
   - explain a concept or term -> 설명
   - not-X-but-Y, before/after -> 비교
   - steps, list, process -> 순서·흐름
   - key phrase, punchline -> 강조
   - scene or section change -> 전환
   - number, study, statistic -> 데이터 증명
   - mood, reflection, emotion -> 분위기
   - logo, CTA, series card -> 브랜딩
   Also note the footage type of the beat (talking head, b-roll, desk POV, screen recording, text-only).
3. **Shortlist candidates** with a quick filter: effects whose `media` includes 숏폼 (or 설명 영상 / 제품 시연 / 데이터 스토리 when the beat fits) and whose `purposes` include the beat's intent. Drop families that conflict with the rules (default: texture, generative, heavy glitch, flashy transitions, anything AI-generated imagery). Check `recipes` for a ready combo matching the beat (e.g. shorts-hook, before-after, data-story, concept-explainer, quote-card, product-demo).
4. **Pick one main effect per beat** (max one optional accent). Prefer variety across the clip and across recent clips: keep a log of effects used per clip and avoid repeating the same signature effect in back-to-back clips. Captions style from the rules is a constant layer, not a pick.
5. **Read each picked card**: `useWhen`, `avoid`, `params` (defaults and ranges). Set concrete values for this beat (duration, easing, offsets), respecting `avoid` and the route rules.
6. **Write the motion spec** to the clip folder as `motion-spec.md`: table of time | footage | intent | effect (slug + en name) | params | implementation note (e.g. Remotion `interpolate`/`spring`, FFmpeg). Note timings get re-snapped to the real voice recording.
7. **Rule check** before handing off: one main effect per beat, nothing in unsafe areas, text on screen >= 1s, no flashes, brand elements present, license OK. Append the effects used to the effects log.
8. Show the spec with the script for approval when the rules require it.

## motionmaxxing craft + eases (Remotion ports — pick for timing / comic punch)
Source: https://github.com/Tejashmakwana/motionmaxxing (Apache-2.0) @ 8c8ec0f. Clone: `resources/refs/motionmaxxing/` (gitignored; see `resources/refs/README.md`). Notes: `research/references/motionmaxxing-notes.md`.

In-house: `video-engine/src/composition/motionmaxxing/catalog.json` + `mmx.ts` — 12 measured eases (`mmx-soft-land`, `mmx-snap-settle`, `mmx-glide`, `mmx-cruise`, `mmx-whip`, `mmx-accel-exit`, `mmx-crash-out`, `mmx-crash-in`, `mmx-pop-over`, `mmx-soft-inout`, `mmx-gentle-in`, `mmx-bounce-hard`) and presets `mmx-oversize-land`, `mmx-cut-on-motion`, `mmx-no-dead-frame`. Call `mmxEase(name, p)` or `mmxStyle(name, p)`. In motion-spec.md write the slug with `(motionmaxxing)`.

**When to prefer mmx vs existing:**
- Scene/card transitions already covered → keep `tdev-*` (transitions.dev).
- Captions / count-up / strike / push-in → keep awesome-ai-motion cards.
- Entry/exit **timing curves**, hook oversize land, cut-on-motion seams, one film spring, living holds → use `mmx-*`.
- Craft laws (always): land decelerates / leave accelerates; almost no scene fades; ≤1 visible spring per film; words at speech rhythm (2–12 f); end mid-motion or hold ≤1.4 s.
- Skip: GSAP runtime, 3D hero, HUD/page chrome, heavy particles/glitch (banned by channel rules + mmx "Never ship").
