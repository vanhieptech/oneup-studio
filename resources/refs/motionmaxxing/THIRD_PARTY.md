# Third-party components in this vendored copy

This directory is a full vendor of [Tejashmakwana/motionmaxxing](https://github.com/Tejashmakwana/motionmaxxing) at commit `8c8ec0f2a6f6c9a0da15cd24f7b1298ab298368c`, kept inside oneup-studio at Hiệp’s request.

Upstream `LICENSE` (Apache License 2.0) and `NOTICE` are preserved unchanged next to this file. They remain authoritative for the original work. This note only lists separately licensed bundles that ship inside the tree so redistributors know what to comply with.

| Component | Path(s) | License | Notes |
|---|---|---|---|
| **GSAP 3.12.5** | `runtime/vendor/gsap.min.js` | GreenSock Standard “No Charge” License (https://gsap.com/standard-license) — **not** open source | Apache-2.0 of this repo does **not** grant GSAP rights. Read and comply with GreenSock terms before use or redistribution. Club GSAP members follow their membership agreement instead. |
| **three.js r186** | `runtime/hero3d/vendor/three.module.js`, `three.core.js`, `addons/` | MIT (`runtime/hero3d/vendor/three.LICENSE`) | Stock examples/jsm addons; EXRLoader embeds TinyEXR / OpenEXR BSD-3 notices; SVGLoader includes svg-numbers (MIT); `addons/libs/fflate.module.js` is fflate 0.8.2 (MIT). |
| **opentype.js 1.3.4** | `runtime/hero3d/vendor/opentype.module.js` | MIT (`runtime/hero3d/vendor/opentype.LICENSE`) | Bundles tiny-inflate and codePointAt polyfill (MIT). |
| **Inter** | `runtime/fonts/InterVariable.woff2`, `runtime/hero3d/fonts/Inter-Bold-Latin.ttf` | SIL Open Font License 1.1 (`runtime/fonts/OFL.txt`, `runtime/hero3d/fonts/OFL.txt`) | May be embedded/redistributed under OFL; not sold alone; reserved name “Inter” applies to derivatives. |
| **Showcase brand media** | `docs/media/*comparison*`, `*-poster.jpg` (Cluely, Spotify, Wispr Flow) | Trademark / brand assets of their owners | Unofficial before/after demos only. Apache-2.0 grants **no** trademark rights. Do not reuse as OneUp product assets. |

Remotion ports used by the video engine live separately at `video-engine/src/composition/motionmaxxing/` (pure ease functions; **no** GSAP). Mapping notes: `research/references/motionmaxxing-notes.md`.

For full provenance text, see upstream `NOTICE`.
