---
id: skills-hyperframes
type: vendored-skills
source: https://github.com/heygen-com/hyperframes/tree/main/skills
commit: 893b4f6757f4d6e8c6a1deb9d2c4743119694b46
license: Apache-2.0
---
# HyperFrames official skills (vendored)

Copied verbatim from heygen-com/hyperframes `skills/` at commit `893b4f6757f4d6e8c6a1deb9d2c4743119694b46` (2026-10-13).
Licensed under the Apache License 2.0 (see `LICENSE`). Copyright HeyGen and contributors. Unmodified; this README is the only added file.
Update: re-clone and copy, bump the commit above. Live copies are also installed by `hyperframes init` at `~/.agents/skills/`.

## Required before any explainer beat (rule-42 / make-video step "Explainer")
1. `hyperframes/SKILL.md`: router, start here.
2. `hyperframes-core/`: composition contract (data-* timing, class="clip", tracks, window.__timelines).
3. `hyperframes-animation/`: motion rules, scene blueprints, transitions.
4. `hyperframes-creative/`: design spec, typography, beat planning (brand rules override palette).
5. `hyperframes-cli/`: lint / validate / inspect / render (Node ≥ 22).
6. `hyperframes-registry/`: check blocks before hand-building a named visual.
Optional: `hyperframes-keyframes`, `hyperframes-audio`, `media-use`, `embedded-captions`, `faceless-explainer`, `motion-graphics`.

## All skills
| Skill | Purpose |
|---|---|
| `embedded-captions` | Add captions or subtitles to an existing single-subject talking-head video without editing the footage |
| `faceless-explainer` | Turn arbitrary text — an article, notes, a topic, a brief — into a faceless explainer video: there is no site or footage to capture, so the visuals are invented |
| `figma` | Import Figma content into a HyperFrames composition — rendered assets, brand tokens, components, storyboard sections → reconstructed motion (frames read as stat |
| `general-video` | Author or edit a custom HyperFrames composition when no specialized workflow fits, or when BRIEF.md sets flow: companion |
| `hyperframes-animation` | All animation knowledge for HyperFrames — atomic motion rules, multi-phase scene blueprints, scene transitions, broader motion-design techniques, AND the seven  |
| `hyperframes-audio` | Use when audio already placed in a HyperFrames composition needs to be mixed: fade-in/fade-out, crossfade, track gain or volume, volume automation, ducking, a m |
| `hyperframes-cli` | Use the HyperFrames CLI development loop: init, add, catalog, capture, lint, check, snapshot, compare, grade-compare, preview, play, present, beats, keyframes,  |
| `hyperframes-core` | The HyperFrames composition contract — build one renderable project |
| `hyperframes-creative` | Non-animation creative direction for HyperFrames videos |
| `hyperframes-keyframes` | Use when a HyperFrames composition needs a punch-in, punch-out, zoom, reframe, Ken Burns treatment, camera move, visual match/whip handoff, or other seek-safe 2 |
| `hyperframes-registry` | Search, install, and wire registry blocks and components into HyperFrames compositions |
| `hyperframes-studio` | Use when working with a person on a HyperFrames project in Studio: first, whether their message asks for a change at all (questions, loose ideas and "don't chan |
| `hyperframes` | Mandatory entry point: read this first for any request to make, create, edit, animate, or render a video, animation, or motion graphic, including a promo, expla |
| `media-use` | Agent Media OS for a HyperFrames project |
| `motion-graphics` | A short, design-led motion graphic where motion is the message — kinetic typography, stat count-up, chart/data-viz hit, logo sting / brand lockup, lower-third / |
| `music-to-video` | Turn a music track (an audio file, a video to pull audio from, or a track generated from a mood brief) into a beat-synced video — lyric video, slideshow, or kin |
| `pr-to-video` | Turn a GitHub pull request (a PR URL, owner/repo#N, or 'this PR' in a checked-out repo) into a code-change explainer video — changelog, feature reveal, fix, or  |
| `product-launch-video` | Turn a product or marketing URL, pasted script, or brief into a product launch / promo video — SaaS promos, feature reveals, product demos, app and company laun |
| `remotion-to-hyperframes` | Port an existing Remotion (React) composition''s source to HyperFrames HTML |
| `slideshow` | Author a HyperFrames slideshow — a presentation, pitch deck, or interactive deck with discrete slides, fragment reveals, branching, hotspot navigation, and buil |
| `talking-head-recut` | Package an existing talking-head / interview / podcast video with timed, designed GRAPHIC OVERLAY cards — kinetic titles, lower-thirds, data callouts, quotes, s |
