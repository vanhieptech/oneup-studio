---
title: "Tài liệu tham khảo (link ngoài, không đưa mã nguồn vào repo)"
date: 2026-10-12
source: "oneup-studio (soạn trong repo)"
id: refs
type: reference
status: active
updated: 2026-10-16
tags: [links]
---
# Tài liệu tham khảo (link ngoài, không đưa mã nguồn vào repo)
- **awesome-ai-motion** (MIT): https://github.com/gongnyang/awesome-ai-motion
  Clone vào máy bằng `git clone https://github.com/gongnyang/awesome-ai-motion resources/refs/awesome-ai-motion` (đã có trong .gitignore). Skill `skills/motion-picks-per-script` đọc `resources/refs/awesome-ai-motion/index.json`.
- HowToLiveBetter (CC BY 4.0): https://github.com/chuanman2707/HowToLiveBetter · https://chuanman2707.github.io/HowToLiveBetter/
- HyperFrames: https://github.com/heygen-com/hyperframes · tài liệu: https://hyperframes.heygen.com
- GSAP (free, Standard License): https://gsap.com/llms-full.txt
- Remotion (phương án thay thế): https://www.remotion.dev/docs/license/faq
- **transitions.dev** (Transitions.dev License: free transitions may be used/modified in commercial projects; no redistributing the collection as a library; tooling MIT): https://github.com/Jakubantalik/transitions.dev @ 8c92530c75b291affdcd39eb0db1df98a40acfef (2026-10-15)
  Clone: `git clone https://github.com/Jakubantalik/transitions.dev resources/refs/transitions.dev` (gitignored). Ported (8, frame-driven) in `video-engine/src/composition/transitions/tdev.ts` + `catalog.json`; only ported values are in git, not the library.
- **motionmaxxing** (Apache-2.0 + separate third-party licenses — see `resources/refs/motionmaxxing/THIRD_PARTY.md` and upstream `NOTICE`): https://github.com/Tejashmakwana/motionmaxxing
  **Vendored full tree in git** at `resources/refs/motionmaxxing/` (nested `.git` removed). Upstream commit: **`8c8ec0f2a6f6c9a0da15cd24f7b1298ab298368c`**. Keep `LICENSE` + `NOTICE` intact. Third-party inside the tree: GSAP (GreenSock Standard License), three.js (MIT), Inter (OFL), showcase brand media (trademarks). Remotion ports (12 eases + 3 presets, no GSAP): `video-engine/src/composition/motionmaxxing/`. Notes: `research/references/motionmaxxing-notes.md`.
- **anidoodle** (Apache-2.0): https://github.com/alexgreensh/anidoodle @ `4db69644b994ae9caf9e20936506954b2f5e4872` (v0.9.4)
  **Vendored full tree in git** at `resources/refs/anidoodle/` (nested `.git` removed; fork via gh failed — box not authenticated). Keep `LICENSE` + `NOTICE` intact; provenance in `resources/refs/anidoodle/INTEGRATION.md`. Remotion ports (seeded doodle draw-on: circle/underline/arrow/check/cross/sketch-box/path, no canvas/music): `video-engine/src/composition/doodle/`. Notes: `research/references/anidoodle-notes.md`.
