---
id: hyperframes-audit-2026-10-13
type: audit
status: partial (sample fixed, clip-01 port pending)
updated: 2026-10-13
tags: [hyperframes, explainer, clip-01]
---
# Audit: clip-01 explainer vs HyperFrames skills (DL-032)
Scope: `content/clips/clip-01-implementation-intention/final/explainer/index.html.tpl`, `pipeline/scripts/build-final.py`, `templates/hyperframes-base`, `content/samples/sample-full-w5/explainer`.

OK: standalone root `data-composition-id="main"` + `data-width/height/duration`; one `gsap.timeline({paused:true})` registered at `window.__timelines["main"]`; GSAP local; fonts local (`@font-face`); no Math.random / setTimeout / network.

## TODO (no re-render done)
1. [ ] **Lint never run.** build-final.py renders without `hyperframes lint`/`check`; add a lint step (Node ≥ 22) that fails the build on error.
2. [ ] **Clip timing not used.** All `.sec.clip` sections have `data-start="0" data-duration="__DUR__"` on separate tracks; visibility is faked with GSAP opacity. Per core skill: give each section its real `data-start/data-duration` from `__TIMING__` and let the runtime hide clips.
3. [ ] **Tweens on `.clip` itself** (opacity + y on `.sec`). Core skill: animate a child, not the clip (autoAlpha/visibility is a lint error; transform on the clip is risky). Wrap content in an inner div and tween that.
4. [ ] Remove `window.__timelines = window.__timelines || {}` and `tl.seek(0)` (unneeded per core skill).
5. [ ] Transitions are hand-rolled push in/out; review `hyperframes-animation` transitions/blueprints and the registry before hand-building (rule: check registry first).
6. [ ] Captions (`#cap`) are hand-built; compare with `embedded-captions`/caption guidance in core (caption hard-kill rule).
7. [ ] Check `gsap_css_transform_conflict`: no CSS initial transform on tweened nodes.
8. [ ] Apply same fixes to `sample-full-w5/explainer` and `templates/hyperframes-base` scaffold.

## Update 2026-10-13 (DL-033) — reference fixed in `content/samples/sample-natural/explainer/`
- [x] 1 lint gate in build-final.py (`hyperframes lint` before every HF render). Sample: lint 0 errors / 0 warnings; `check`: runtime, layout (9 samples), motion 0/0, contrast 36/36 AA.
- [x] 2 real `data-start/data-duration` per section (`__START_<id>__`/`__DUR_<id>__` from the voiced timing); sections are sub-compositions (`compositions/e01.html`), fixing lint `nested_structure_needs_subcomposition`.
- [x] 3 only children are tweened (`fromTo`), never the clip; rotation moved from CSS into the tween.
- [x] 4 no `window.__timelines = … || {}`, no `tl.seek(0)`.
- [x] 5 registry checked (`catalog --query`): push/slide transitions → `transitions/catalog.md` push slide for section changes; part change stays ffmpeg xfade. Single-section sample has entrance only (exit banned except last scene).
- [x] 6 captions: brand-styled adaptation of registry `caption-pill-karaoke` in `compositions/captions.html`, ≤4-word groups, karaoke step, deterministic hard-kill, host `data-track-kind="captions"`.
- [x] 7 no CSS initial transform on tweened nodes.
- [ ] 8 port to `clip-01…/final/explainer` (e01–e04) and `templates/hyperframes-base` — still the old template; do it on the next clip-01 rebuild.
