---
title: "Tài liệu tham khảo (link ngoài, không đưa mã nguồn vào repo)"
date: 2026-10-12
source: "oneup-studio (soạn trong repo)"
id: refs
type: reference
status: active
updated: 2026-11-25
tags: [links]
---
# Tài liệu tham khảo (link ngoài, không đưa mã nguồn vào repo)

**Motion skills inventory (local + GitHub):** `research/references/motion-skills-catalog.md`  
**100-sample gallery:** `content/samples/lab/motion-100/index.html` (needs awesome-ai-motion clone)

- **awesome-ai-motion** (MIT): https://github.com/gongnyang/awesome-ai-motion
  Clone: `git clone --depth 1 https://github.com/gongnyang/awesome-ai-motion resources/refs/awesome-ai-motion` (gitignored). 637 effects · `index.json`. Skill `skills/motion-picks-per-script` đọc index này.
- HowToLiveBetter (CC BY 4.0): https://github.com/chuanman2707/HowToLiveBetter · https://chuanman2707.github.io/HowToLiveBetter/
- HyperFrames: https://github.com/heygen-com/hyperframes · tài liệu: https://hyperframes.heygen.com
- GSAP (free, Standard License): https://gsap.com/llms-full.txt
- Remotion (phương án thay thế): https://www.remotion.dev/docs/license/faq
- **transitions.dev** (Transitions.dev License: free transitions may be used/modified in commercial projects; no redistributing the collection as a library; tooling MIT): https://github.com/Jakubantalik/transitions.dev @ 8c92530c75b291affdcd39eb0db1df98a40acfef (2026-10-15)
  Clone: `git clone https://github.com/Jakubantalik/transitions.dev resources/refs/transitions.dev` (gitignored). Ported (8, frame-driven) in `video-engine/src/composition/transitions/tdev.ts` + `catalog.json`; only ported values are in git, not the library.
- **motionmaxxing** (Apache-2.0 + separate third-party licenses — see `resources/refs/motionmaxxing/THIRD_PARTY.md` and upstream `NOTICE`): https://github.com/Tejashmakwana/motionmaxxing
  **Vendored full tree in git** at `resources/refs/motionmaxxing/` (nested `.git` removed). Upstream commit: **`8c8ec0f2a6f6c9a0da15cd24f7b1298ab298368c`**. Keep `LICENSE` + `NOTICE` intact. Third-party inside the tree: GSAP (GreenSock Standard License), three.js (MIT), Inter (OFL), showcase brand media (trademarks). Agent skill: `skills/motionmaxxing` → symlink to this folder (see `INTEGRATION.md`). Remotion ports (12 eases + 3 presets, no GSAP): `video-engine/src/composition/motionmaxxing/`. Notes: `research/references/motionmaxxing-notes.md`.
- **anidoodle** (Apache-2.0): https://github.com/alexgreensh/anidoodle @ `4db69644b994ae9caf9e20936506954b2f5e4872` (v0.9.4)
  **Vendored full tree in git** at `resources/refs/anidoodle/` (nested `.git` removed; fork via gh failed — box not authenticated). Keep `LICENSE` + `NOTICE` intact; provenance in `resources/refs/anidoodle/INTEGRATION.md`. Remotion ports (seeded doodle draw-on: circle/underline/arrow/check/cross/sketch-box/path, no canvas/music): `video-engine/src/composition/doodle/`. Notes: `research/references/anidoodle-notes.md`.
- **ffmpeg-skill** (MIT): https://github.com/kajisho5/ffmpeg-skill · npm `ffmpeg-skill@4.7.1` (2026-11-25)
  **Không vendor.** Cài ở mức user cho Claude Code: `npx -y ffmpeg-skill@4.7.1` → `~/.claude/skills/ffmpeg-skill` (không chạy `setup`, vì nó cài cho mọi agent và có thể `brew install ffmpeg-full`). Dùng chủ yếu cho @vanhiep.tech (A-roll: `silence.py`, `caption.py`, `loudness.py`) và `check.py --platform tiktok` để kiểm tra spec trước khi đăng. Pipeline @hi.oneup vẫn giữ ffmpeg riêng trong `build-final.py` / `check-rules.py`. Với ffmpeg lean của Homebrew, tool caption/stabilize thiếu filter `drawtext`/`subtitles`/`vidstab` (`npx ffmpeg-skill doctor`); cần `brew install ffmpeg-full` (keg-only, skill tự dùng, không thay ffmpeg trên PATH). Lưu ý (25/11): cài ffmpeg-full đã nâng `x265` và làm hỏng ffmpeg lean trên PATH (`libx265.215.dylib` not loaded) → sửa bằng `brew upgrade ffmpeg` (8.0.1 → 9.1); các lệnh ffmpeg của build-final / check-rules / join-beats đã chạy thử OK trên 9.1.
