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
- **motionmaxxing** (Apache-2.0; NOTICE: GSAP Standard License in upstream runtime — not redistributed; three.js MIT; Inter OFL): https://github.com/Tejashmakwana/motionmaxxing @ 8c8ec0f2a6f6c9a0da15cd24f7b1298ab298368c (2026-10-16)
  Clone: `git clone https://github.com/Tejashmakwana/motionmaxxing resources/refs/motionmaxxing` (gitignored). Remotion ports (12 measured eases + 3 presets) in `video-engine/src/composition/motionmaxxing/`; mapping notes `research/references/motionmaxxing-notes.md`. Do not commit `runtime/vendor/gsap.min.js`.
