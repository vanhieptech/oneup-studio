---
title: "motionmaxxing → Remotion mapping (comic shorts)"
date: 2026-10-16
type: reference
tags: [motion, remotion, motionmaxxing, comic]
status: ready
source: "https://github.com/Tejashmakwana/motionmaxxing @ 8c8ec0f (Apache-2.0; NOTICE: GSAP not redistributed)"
id: research.motionmaxxing
updated: 2026-10-16
---
# motionmaxxing → Remotion mapping (comic shorts)

Local clone (gitignored): `resources/refs/motionmaxxing/`  
`git clone https://github.com/Tejashmakwana/motionmaxxing resources/refs/motionmaxxing`  
Commit studied: `8c8ec0f2a6f6c9a0da15cd24f7b1298ab298368c` (2026-10-16 shallow).

Remotion ports (in git): `video-engine/src/composition/motionmaxxing/` (`catalog.json`, `mmx.ts`).  
Skill: `skills/motion-picks-per-script` (+ workflow mirror). Parent catalogs: awesome-ai-motion (637 effects), transitions.dev (8 tdev-* ports).

## 1. What it is
Agent skill + craft library for kinetic-type / product-promo films. Not a Remotion project. Evidence: 53 measured HyperFrames moments (M913–M974), ~4.3k moves, 12 fitted eases, 156 designer rules (PR-*), 507 film-decoded mechanics (PL*), HTML+GSAP runtime. Value for us: **measured timing + eases + beat grammar**, re-implemented with Remotion `interpolate` / custom ease fns. We do **not** take `runtime/vendor/gsap.min.js`, Chrome/ffmpeg renderer, or ElevenLabs scripts.

## 2. License
| Piece | License | Action |
|---|---|---|
| SKILL, references/, library/, taste/, templates/, docs text, `runtime/motion.js` (ideas) | **Apache-2.0** | OK to study; keep NOTICE attribution; port numbers into our code |
| `runtime/vendor/gsap.min.js` | GreenSock **Standard "No Charge"** (NOT open source) | **Do not commit or redistribute**; Remotion eases replace it |
| three.js / opentype / Inter fonts in hero3d | MIT / OFL | Only in gitignored clone; we don't ship them |
| Showcase brands in docs/media | trademarks | Demo only; not for OneUp output |

Attribution: Tejas Makwana / motionmaxxing · github.com/Tejashmakwana/motionmaxxing · Apache-2.0 + NOTICE.

## 3. Catalog sizes (source)
- 12 measured eases (`M.ease.*`)
- 156 PR rules + 53 HF moments + 507 PL film mechanics ≈ **716** rows in `library/moments.jsonl`
- Craft laws in `SKILL.md` + `references/motion.md`, `transitions.md`, `type.md`

## 4. Mapping: Remotion comic library

### 4.1 NEW (port / adopt) — 14
| mmx slug | Source | Remotion use (comic) | Params (30 fps) |
|---|---|---|---|
| `mmx-soft-land` | ease softLand | Panel / bubble / board entry | 12 f (6–21); 60–72% travel in first 4 f |
| `mmx-snap-settle` | ease snapSettle | Hook word, CTA sticker, hero prop | 11 f; CTA-heavy |
| `mmx-glide` | ease glide | Default x/y/scale land | 10 f |
| `mmx-cruise` | ease cruise | Drift, ken-burns creep, counters | linear; 1–3 px/f drift |
| `mmx-whip` | ease whip | Fast punch-in / whip accent (≤1/clip) | 7–13 f |
| `mmx-accel-exit` | ease accelExit | Leave frame / throw-away prop | 13 f; peak speed near end |
| `mmx-crash-out` | ease crashOut | Exit into hard cut | 17 f |
| `mmx-crash-in` | ease crashIn | Hook word / logo from ~3.5× | 10–18 f; overshoot then settle |
| `mmx-pop-over` | ease popOver | One visible spring per film | 15 f; peak 1.08 @ t≈0.72 |
| `mmx-soft-inout` | ease softInOut | Opacity/blur/colour ramps | 9 f |
| `mmx-gentle-in` | ease gentleIn | Soft exit starts / fade-out lead | 9 f |
| `mmx-cut-on-motion` | craft R3.1 / PR-A13 | Scene seam: cut mid-move; next beat already travelling | no fade between scenes |
| `mmx-oversize-land` | craft R3.3 / arrival | Thesis word / stamp from 2–3.5× → 1 | softLand or crashIn |
| `mmx-no-dead-frame` | craft R1.12 | Hold >3 f: keep drift/caret/light alive | breath 0.6–1.5 s before payoff OK |

### 4.2 DUPLICATE / overlap (prefer existing) — 12
| motionmaxxing idea | Already in our library | Prefer |
|---|---|---|
| softLand card/modal | `tdev-modal` | tdev for scene entrance; mmx-soft-land for element timing |
| panel rise + blur | `tdev-panel` | tdev-panel |
| text y+blur swap | `tdev-text-swap` | tdev-text-swap (MAI→NAY, LƯỜI→NÉ) |
| icon scale pop | `tdev-icon-swap` | tdev-icon-swap |
| stagger list | `tdev-stagger` | tdev-stagger; mmx CTA gap ~8 f as accent |
| badge spring | `tdev-badge` / popOver | tdev-badge; mmx-pop-over if one film spring needed |
| error shake | `tdev-shake` | tdev-shake (self-blame beat) |
| word-pop / kinetic words | awesome `word-pop-caption` | word-pop; mmx type cadence 2–12 f/word |
| karaoke / caption | awesome `karaoke-caption` | karaoke-caption |
| count-up / number roll | awesome `count-up` | count-up; step-per-frame from mmx optional |
| push-in / camera | awesome `push-in` / ken-burns | push-in; ease mmx-glide or cruise |
| highlight / strike | awesome highlight-sweep, strikethrough-replace | keep awesome cards |

### 4.3 Skip for comic shorts
- 3D hero / RoomEnvironment / bloom (hero3d)
- Cursor park/press demos (UI product films)
- Dot-grid floods, particle morphs, neon stroke, chromatic aberration heavy
- Page chrome / HUD / deck layouts (explicitly banned in SKILL "Never ship")
- Pure opacity scene fades (mmx default: almost nothing fades between beats)
- GSAP runtime, imagegen, ElevenLabs voice path

## 5. Standout motions for @hi.oneup comic clips
1. **`mmx-crash-in` + oversize land** on hook stamp «BẢN CHẤT LÀ GÌ?» (from ~3×, settle in ~0.4–0.6 s).
2. **`mmx-cut-on-motion`** at b01→b01b (laptop → TikTok already scrolling).
3. **`mmx-soft-land`** for research boards / STEEL 691 card.
4. **`tdev-text-swap` + mmx word cadence** for LƯỜI → NÉ / TRÁNH KHÓ CHỊU.
5. **`mmx-accel-exit`** when calendar tears to MAI or prop is thrown away.
6. **`mmx-pop-over` once** on CTA badge «Comment một chữ» (only spring in the film).
7. **`mmx-no-dead-frame`**: tiny drift on held science panel so it doesn't read as a slide.

## 6. Craft laws we keep (short)
1. Land decelerates; leave accelerates.
2. Cut on motion; start next beat already moving.
3. Almost no scene fades; move/cut/unmask instead.
4. At most one visible spring per film.
5. Words at speech rhythm (whole words 2–12 f apart).
6. End mid-motion or designed short hold ≤1.4 s (CTA).
7. One hero per frame; no page chrome / HUD.

## 7. Files touched in oneup-studio
- Clone: `resources/refs/motionmaxxing/` (gitignored)
- Ports: `video-engine/src/composition/motionmaxxing/{catalog.json,mmx.ts}`
- Notes: this file
- Skill: `skills/motion-picks-per-script/SKILL.md` + `/home/box/agent-data/workflows/motion-picks-per-script/SKILL.md`
- Index: `resources/refs/README.md`, `docs/conventions/storage.md`, INDEX via `build-index.py`
