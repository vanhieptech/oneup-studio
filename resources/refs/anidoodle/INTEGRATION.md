# anidoodle — vendored copy + OneUp integration

- Provenance: https://github.com/alexgreensh/anidoodle @ 4db69644b994ae9caf9e20936506954b2f5e4872 (v0.9.4), cloned 2026-10-18 on the box; nested `.git` removed. `gh repo fork` was attempted first and failed (box gh not authenticated) — this full vendored copy with LICENSE + NOTICE kept satisfies the house rule (2026-10-16).
- License: Apache-2.0 — see `LICENSE` and `NOTICE` in this folder, unmodified. Third-party notes inside NOTICE (sound pack CC0/CC BY 4.0, not included here) and `skills/anidoodle/engine/assets/refs/PROVENANCE.json` (public-domain Van Gogh reference) are kept as upstream shipped them.
- This file (INTEGRATION.md) is ours; everything else in this folder is upstream, byte-identical to the clone.
- Adopted: seeded-rng/jitter/Catmull-Rom/oval-line geometry + pen progress draw-on, re-implemented as SVG in `video-engine/src/composition/doodle/` (see `research/references/anidoodle-notes.md`).
- Not adopted: the canvas engine at runtime, 32 styles, music/sound, interactive web component, launch kit.
