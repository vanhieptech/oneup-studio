---
id: hyperframes-audit-2026-10-13
type: audit
status: open
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
