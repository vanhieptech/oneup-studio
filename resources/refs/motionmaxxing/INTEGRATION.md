---
id: refs.motionmaxxing.integration
type: vendor-note
status: active
updated: 2026-11-07
tags: [skill, vendor, motionmaxxing, license]
---
# motionmaxxing — vendored copy + OneUp integration

- Provenance: https://github.com/Tejashmakwana/motionmaxxing @ `8c8ec0f2a6f6c9a0da15cd24f7b1298ab298368c`, nested `.git` removed. Full tree kept in git (Apache-2.0 `LICENSE` + `NOTICE` unmodified).
- Third-party inside the tree: see `THIRD_PARTY.md` (GSAP GreenSock Standard, three.js MIT, Inter OFL, showcase brand media).
- Agent skill entry: `skills/motionmaxxing` → symlink to this folder (relative `../resources/refs/motionmaxxing`). Re-link with `bash resources/refs/motionmaxxing/install.sh --dir skills/motionmaxxing --force` then replace the absolute link with the relative one if needed.
- Remotion ports (no GSAP at render time): `video-engine/src/composition/motionmaxxing/` (`catalog.json`, `mmx.ts`). Mapping: `research/references/motionmaxxing-notes.md`.
- Beat picks for @hi.oneup: `skills/motion-picks-per-script` (prefer `mmx-*` for timing / cut-on-motion; keep `tdev-*` for UI transitions).
- Series path (DL-027): comic + Remotion / HyperFrames. Do **not** run the upstream HTML+GSAP Chrome film pipeline for channel shorts unless Hiệp asks for a one-off promo film. Craft laws + measured eases still apply via the Remotion ports.
- This file (`INTEGRATION.md`) and `THIRD_PARTY.md` are ours; everything else in this folder is upstream.
