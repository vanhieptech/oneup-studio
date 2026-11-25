---
title: "Motion skills catalog (generators + samples)"
date: 2026-11-08
id: research.motion-skills-catalog
type: reference
status: ready
updated: 2026-11-08
tags: [motion, skills, hyperframes, remotion, samples]
source: "local inventory + GitHub clones 2026-11-08"
---
# Motion skills catalog

Inventory of **skills that can generate motion / video**, plus the **Motion 100** sample pack.

## Quick numbers
- awesome-ai-motion effects: **637** (MIT) · recipes 11 · routes 7
- Effects with HTML+MP4 demo: **128** → sample pack takes first **100**
- HF music-to-video primitives: **37**
- Sample gallery: `content/samples/lab/motion-100/index.html`

## In-repo generators (use these first)
| Path | Skill | What it generates |
|---|---|---|
| `skills/motionmaxxing` | motionmaxxing | HF/GSAP launch films; measured eases |
| `skills/hyperframes/motion-graphics` | motion-graphics | HF short motion units (kinetic/logo/L3/charts/…) |
| `skills/hyperframes/hyperframes-animation` | hyperframes-animation | GSAP blueprints + transitions catalog |
| `skills/hyperframes/music-to-video` | music-to-video | 37 motion primitives (HTML+GSAP) |
| `skills/hyperframes/faceless-explainer` | faceless-explainer | explainer motion packs |
| `skills/hyperframes/product-launch-video` | product-launch-video | launch film pipeline |
| `skills/hyperframes/embedded-captions` | embedded-captions | caption motion themes |
| `skills/motion-picks-per-script` | motion-picks-per-script | picker over awesome-ai-motion + tdev + mmx |
| `skills/make-video` | make-video | @hi.oneup comic+motion Remotion |
| `channels/vanhiep-tech/skills/make-layer` | make-layer | ov/cu HF layers for CapCut |
| `video-engine/src/composition/motionmaxxing` | mmx Remotion ports | 12 eases + 3 presets |
| `video-engine/src/composition/transitions` | tdev Remotion ports | 8 transitions.dev ports |

## GitHub skill packs (cloned under `resources/refs/`)
| Clone | Upstream | SKILL.md | Notes |
|---|---|---|---|
| `awesome-ai-motion` | https://github.com/gongnyang/awesome-ai-motion | 1 | 637 effects + agent skill. `SKILL.md` |
| `motionmaxxing` | https://github.com/Tejashmakwana/motionmaxxing | 1 | vendored; looksmaxxing craft. `SKILL.md` |
| `anidoodle` | https://github.com/alexgreensh/anidoodle | 2 | vendored doodle draw-on. `skills/anidoodle/SKILL.md`, `plugins/anidoodle/skills/anidoodle/SKILL.md` |
| `transitions.dev` | https://github.com/Jakubantalik/transitions.dev | 5 | transition library (ported subset). `refine/.agents/skills/refine-live/SKILL.md`, `skills/transitions-ui-generation/SKILL.md`, `skills/transitions-polish/SKILL.md`, `skills/transitions-dev/SKILL.md`, `agent/skill/SKILL.md` |
| `motion-video-skill` | https://github.com/mos-ski/motion-video-skill | 1 | 11 Claude video skills / Remotion studio. `SKILL.md` |
| `skill-motion-graphic` | https://github.com/hculap/skill-motion-graphic | 1 | code→headless render MP4. `SKILL.md` |
| `motion-graphics-skill` | https://github.com/cskwork/motion-graphics-skill | 1 | app-driven + vertical shorts. `skills/motion-graphics/SKILL.md` |
| `remotion-motion-graphics-skill` | https://github.com/Liamrjohnston/remotion-motion-graphics-skill | 4 | 4 Remotion skills. `skills/article-highlights/SKILL.md`, `skills/motion-graphics/SKILL.md`, `skills/terminal-inserts/SKILL.md`, `skills/cinematic-camera/SKILL.md` |
| `claude-motion-skills` | https://github.com/kevinbadi/claude-motion-skills | 0 | iart showcase (0 SKILL.md in tree). — |
| `iart-motion-skills` | https://github.com/iart-ai/motion-skills | 0 | iart motion-skills (0 SKILL.md). — |

## External lists (not fully cloned)
- https://github.com/zhuyansen/awesome-claude-video-skills — 427 graded video skill repos
- https://github.com/guanmo-ai/awesome-ai-motion — gallery of AI-coded motion works (different from gongnyang catalog)

## Setup (Mac)
```bash
cd /Users/macbook/me/projects/oneup-studio/resources/refs
git clone --depth 1 https://github.com/gongnyang/awesome-ai-motion.git   # if missing
git clone --depth 1 https://github.com/Jakubantalik/transitions.dev.git
# optional packs:
git clone --depth 1 https://github.com/mos-ski/motion-video-skill.git
git clone --depth 1 https://github.com/hculap/skill-motion-graphic.git
git clone --depth 1 https://github.com/cskwork/motion-graphics-skill.git
git clone --depth 1 https://github.com/Liamrjohnston/remotion-motion-graphics-skill.git
open content/samples/lab/motion-100/index.html   # from repo root
```

`awesome-ai-motion/` + `transitions.dev/` are gitignored (see `.gitignore`). Other clones above should stay local unless you decide to vendor.

## Motion 100 pack
Path: `content/samples/lab/motion-100/`
- `catalog.json` — 100 entries (slug, family, demo path)
- `demos/NNN-slug/` — symlink to effect `index.html` + `clip.mp4`
- `posters/` — symlink posters
- `index.html` — browseable gallery
- `local-primitives.json` — 37 HF primitives index

## How to pick / generate
1. Short @hi.oneup comic beat → `skills/motion-picks-per-script` + Remotion `mmx-*` / `tdev-*`
2. Standalone motion sting / kinetic / L3 → `skills/hyperframes/motion-graphics` (+ catalog search)
3. Launch / brand film craft → `skills/motionmaxxing`
4. CapCut overlay/cutaway → `channels/vanhiep-tech/skills/make-layer` (hard-edge ov, DL-069)
5. Browse technique demos → Motion 100 gallery or full `awesome-ai-motion/effects/`

