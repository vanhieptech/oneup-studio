---
title: "anidoodle → Remotion doodle draw-on mapping (comic shorts)"
date: 2026-10-18
type: reference
tags: [motion, remotion, anidoodle, doodle, drawing]
status: ready
source: "https://github.com/alexgreensh/anidoodle @ 4db69644b994ae9caf9e20936506954b2f5e4872 (Apache-2.0)"
id: research.anidoodle
updated: 2026-10-18
---
# anidoodle → Remotion doodle draw-on (comic shorts)

Vendored full tree (in git, nested `.git` removed): `resources/refs/anidoodle/` — LICENSE + NOTICE kept intact.
Upstream: https://github.com/alexgreensh/anidoodle @ `4db69644b994ae9caf9e20936506954b2f5e4872` (v0.9.4, 2026-10-18 shallow clone).
Fork attempt: `gh repo fork` failed — box `gh` is not authenticated (no GH_TOKEN). Per house rule 2026-10-16 the full clone vendored in-repo with LICENSE/NOTICE satisfies the requirement; fork later from Mac if wanted.
Integration summary: `resources/refs/anidoodle/INTEGRATION.md`. Demo frame: `research/references/anidoodle-demo-frame90.png` (Remotion still, frame 90 of `video-engine/examples/doodle-demo.json`).

## 1. What it is
Agent skill + portable TypeScript art engine: hand-drawn stills, drawing timelapses, films, explainers and interactive web art in 32 code-drawn styles, plus music composed in code (21 vocabularies). Every mark is a function; `draw(ctx, frame, env)` is pure in (frame, env), randomness only from a seeded `rng(seed)`, so the same source redraws identical pixels on any machine. Rendering hosts: canvas/Playwright stills + MP4/GIF/WebM/HTML emit; optional Remotion host is only an optionalDependency upstream.

## 2. License
Apache-2.0 (`LICENSE`, Copyright 2026 Alex Greenshpun) + `NOTICE`. Third-party inside the tree: optional sound pack (NOT in repo; VCSL CC0 samples + OpenAIR CC BY 4.0 impulse responses, attribution in upstream NOTICE), Van Gogh Almond Blossom reference image (public domain, PROVENANCE.json kept). Our Remotion ports are new code implementing the same geometry ideas; upstream LICENSE/NOTICE travel with the vendored tree.

## 3. Technique studied (skills/anidoodle/engine/src/canvas-core/)
- `core.ts`: seeded mulberry-style `rng(seed)`; tileable gradient `fractal()` noise; Catmull-Rom `sample()`; `jitter()` hand wobble; geometry helpers `oval/line/arc/softBox/heart`; `ribbon()` turns a centreline into a tapered nib stroke (taper + pressure variation).
- `PenOpts.progress` + `upTo()`: draw-on — only the first `progress` of the centreline is drawn, cut on the centreline so the travelling tip keeps its taper. Medium order matters (pencil → washes light→dark → ink), nothing fades in.
- `drawingMarks.ts` / `drawingScore.ts`: a drawing is an ordered score of marks; the film's last frame equals the still, pixel for pixel.
- `camera.ts` / `timeRemap.ts` / `seams.ts`: named camera moves, slow-motion/freeze, motion-carrying cuts (deck of named moves).
- Determinism contract: no clock, no `Math.random`, no `ctx.filter`; texture/wobble baked into geometry.

## 4. Adopted (Remotion ports, in git)
`video-engine/src/composition/doodle/` (`doodle.ts`, `Doodle.tsx`, `catalog.json`):
| slug | kind | Use in @hi.oneup beats |
|---|---|---|
| `doodle-circle` | circle | khoanh từ khoá / dòng note đúng lúc nói tới |
| `doodle-underline` | underline | gạch chân keyword trên note/board |
| `doodle-arrow` | arrow | nhân → quả, việc to → bước nhỏ đầu tiên |
| `doodle-check` | check | tick bước nhỏ đã xong |
| `doodle-cross` | cross | gạch niềm tin sai / cái tên việc to đùng trước reframe |
| `doodle-sketch-box` | sketch-box | khung sticky-note tự vẽ ra thay vì pop-in |
| `doodle-path` | path | đường tự do (sợi dây, lộ trình) bằng `points[]` |

Schema/validate: `scene.doodles[]` in `validation/schema.ts` (`DOODLE_KINDS`, shared list — L-042), semantic checks in `validate.ts` (draw-on must end inside the scene, `path` needs points, caption-band warning y>1400). Rendered by `SceneRenderer` inside the comic SVG. Stroke defaults: `BRAND.accent` (#FF5A36), width **7** (đổi từ 10 ngày 18/10), opacity .92, jitter 1.2–1.4px, design px 1080-wide, seed cố định/cue.

**Brand-fit (L-047, Hiệp chê demo đầu «Quá xấu»):** demo đầu (`doodle-demo2.json`, 7 nét dồn trên giấy trơn, không nhân vật/bảng/caption) bị loại vì rời design system. Bản chuẩn `video-engine/examples/doodle-demo-brand.json` (10,5s, 2 cảnh theo grammar clip-03 b03/b07: nền grid/bed, Thầy chibi, sign `DỌN PHÒNG`/`~15' / VIỆC`, words, bong bóng thoại, caption plate, logo) chỉ dùng 2 nét: circle quanh sign + underline dưới sign. Quy trình bắt buộc: render still frames → tự nhìn so với contact-sheet clip thật → mới render video.

## 5. Not adopted (duplicates / out of scope)
- 32 full art styles + canvas engine: comic look của kênh đã có rig/brand riêng; port nguyên engine sẽ trùng và nặng.
- Music composer / sound pack / SFX kit: kênh cấm nhạc (rule), giọng F5 + SFX có pipeline riêng; sound pack là download 373MB ngoài repo.
- Interactive `<ani-doodle>` web component, launch-film kit, drawing lessons: ngoài format TikTok comic hiện tại.
- Camera/timeRemap/seams deck: chuyển cảnh đã có `tdev-*` + `mmx-*` (L-042); chỉ mượn nguyên tắc "cut on motion" đã có ở `mmx-cut-on-motion`.

## 6. Strengths / weaknesses for us
Strengths: draw-on đúng thứ tự tay vẽ làm motion graphics trông "người vẽ" hơn pop/fade; deterministic seeded nên Remotion frame-pure, render lại giống hệt; geometry helpers nhỏ, port rẻ.
Weaknesses: upstream là canvas raster (ribbon/tooth/wash) — port SVG chỉ giữ được nét bút, không giữ texture giấy/rửa màu; 32 styles cần plate riêng từng style, không hợp brand Be Vietnam Pro/DM Sans + chibi rig hiện tại; engine lớn (162 file canvas-core) nếu bê nguyên sẽ thành hệ render thứ hai phải bảo trì.
