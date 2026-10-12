# OneUp Design System — MASTER

> Source of truth for all OneUp iOS UI. Phase UI-SPECs and `pages/*.md` may override per-screen.
> Generated via ui-ux-pro-max research, then **curated** to escape dataset bias (no purple-on-white, no cream/terracotta, no Inter default, no claymorphism toy look).

**Product:** OneUp — Personal Growth OS · Your next +1  
**Platform:** iOS 17+ SwiftUI · WidgetKit · Light-first · dark ramp in `brand/COLOR.md` (journey **Dark** toggle for side-by-side)  
**Updated:** 2026-09-30 · +1 loop contract → `DESIGN-TO-CODE.md` §14  
**Companion UX:** `UX-COMPANION-SYSTEM.md` · Interactive prototype: `prototype/oneup-journey/index.html`  
**Design → code:** [`DESIGN-TO-CODE.md`](DESIGN-TO-CODE.md) · Brand: `brand/COLOR.md` · `brand/LOGO.md` · `brand/omi-exports/`

---

## 1. Visual Direction

| Dial | Value | Meaning |
|------|-------|---------|
| Style | **Minimal Swiss + Soft Focus Card** | Clean grid, one hero card, generous whitespace |
| Variance | 3/10 | Centered, calm — not brutalist/bento chaos |
| Motion | 4/10 | Soft spring on complete; no carousel spam |
| Density | 4/10 | Spacious Today; denser Goals list OK |
| Mode | **Light primary** | Dark = later theme, not v1 default |

**Brand test:** First screen must scream “OneUp / +1” — wordmark + one action card. Remove nav and it should still feel like OneUp, not a generic todo app.

**Anti-patterns (locked out):**
- Purple / violet primary themes
- Warm cream (#F4F1EA-ish) + terracotta
- Emoji as icons
- Chat-bubble coach UI (Ask Omi guided rails may use a bubble thread on the Ask cover only; the Omi/Coach decision home must not)
- Task-dump lists as the hero
- Heavy XP / gamification chrome
- Glow effects, multi-layer shadows, pill cluster stats in hero

---

## 2. Color Tokens

> **Source of truth:** [`brand/COLOR.md`](brand/COLOR.md) — do not duplicate long tables here.

**Summary:** Confident **black / white**. CTA = ink `#111111`. Semantic hue only (success / danger / momentum).

| Role | Hex |
|------|-----|
| bg / surface / ink | `#F7F7F5` · `#FFFFFF` · `#111111` |
| primary CTA | `#111111` |
| success / momentum / danger | `#1A7F4B` · `#B45309` · `#B91C1C` |

Full tokens, application map, sync checklist → **`brand/COLOR.md`**.  
Logo marks → **`brand/LOGO.md`** · `brand/logos/`.

---

## 3. Typography

**Source of truth:** journey classes in `prototype/oneup-journey/index.html` (`.brand` · `.title` · `.body` · `.muted` · `.greet` · `.meta` · `.caption`). Code mirror: `OUTypography`.

| Role | Journey | Size | Weight | Use |
|------|---------|------|--------|-----|
| Brand | `.brand` | 28 | 700 | OneUp wordmark |
| Title | `.title` | 22 | 600 | Screen H2 (“Pick an alternative”) |
| Heading | Must card | 20 | 600 | Card / Must hero title only |
| Body | `.body` | 16 | 400 | Primary copy · CTA label (+ 600) |
| Muted | `.muted` | 14 | 400 | Supporting line under title |
| Chip | `.chip` | 14 | 500 | Pill labels |
| Greet | `.greet` | 13 | 400 | Eyebrow (“Change”, greeting) |
| Meta | `.meta` | 13 | 400 | Minutes · size-language · soft status |
| Caption | `.caption` | 12 | 400 | Smallest chrome |
| Countdown / Focus | `.countdown-num` / `.focus-timer` | 72 / 56 / 40 | 700 | Moments only |

**Hierarchy rule (never invert):** brand 28 > title 22 > heading 20 > body 16 > muted/chip 14 > greet/meta 13 > caption 12.

**Not Inter / Roboto / Arial / SF Pro for UI copy.** DM Sans only. SF Symbols may use `.font(.system)` for icon metrics.

EN primary · VI via String Catalog — same layout, no text clipping at largest Dynamic Type.

---

## 4. Spacing & Radius

| Token | Value |
|-------|-------|
| Space scale | 4 / 8 / 12 / 16 / 24 / 32 / 48 |
| Screen padding | 16–20 horizontal |
| Card padding | **16** (`OUSpacing.base`) — never 20/24 |
| Section gap | 24–32 |
| **Chip / pill gap** | **8** (`OUSpacing.chipGap`) — equal between every pill; never adaptive grid gutters |
| **CTA stack gap** | **8** (`OUSpacing.ctaStack` / `OUCTAStack`) — primary ↔ outline / muted row; journey `.btn-row`. Never inherit parent section `24`/`16` |
| Corner — card | 16–20 continuous |
| Corner — control | 12 |
| Touch target | ≥ 44×44 pt — outline CTAs use `OUOutlineButton` (full hit), not stroke+Text |
| Safe area | Always — header, tab/CTA, widget margins |

**CTA lock:** stacked primary + secondary = `OUCTAStack` only. See DESIGN-TO-CODE §6.12.

---

## 5. Iconography

- **SF Symbols** first (iOS-native). Weight: Regular; fill only for selected tab / completed.
- Semantic set: `checkmark.circle`, `target`, `flame` (momentum — muted), `calendar`, `sparkles` (coach), `arrow.triangle.2.circlepath` (Change), `bell`, `globe`
- No emoji icons. Consistent hierarchy: outline default, fill selected.

---

## 6. Motion

| Event | Spec |
|-------|------|
| Appear (Today card) | 280–360ms ease-out, slight y + opacity |
| Complete | Checkmark scale spring 0.85→1.0, 300ms; confetti **forbidden** |
| Accept / Change | Card crossfade 200ms |
| Reduced motion | Skip springs; snap to end state |
| Widget | No animation beyond timeline refresh |

---

## 7. Navigation IA (all product UI)

### Hierarchy (locked — *one thing at a time*)

```
Primary (do)     Today  =  +1 ink orb on floating dock
Secondary (plan) Goals  ·  Progress   ← quieter peers
Companion        Omi float (movable)  ← not a tab
Sheets           Reflect · Share · Memory · Ask cover
```

| Tier | Destinations | Visual |
|------|--------------|--------|
| **P0 · Do** | Today | Floating glass dock · **nested +1 ink orb** (short pedestal; active = filled) |
| **P1 · Frame** | Goals · Progress | Soft pill wash when active; quieter peers |
| **P2 · Think** | Omi | Floating companion — never 4th tab |
| **P3 · Moments** | Reflect / Share / Recovery / **Day check-in sheet** | Sheets / stacks, not chrome |

**Rules**
- Prefer **Today-first** — cold open lands on Today  
- Equal-weight 3-icon bars / edge-flush classic bars are **forbidden** (fights “one +1”)  
- Chrome = **inset floating dock** (blur + soft elevation), not a full-bleed strip  
- +1 orb = **nested pedestal** (`FloatingDockMetrics.orbRaise = -OUSpacing.sm`) — not a half-circle FAB island above the glass  
- Re-tap Today scrolls to top (convenience)  
- Goals/Progress support the day; they do not compete with Must  
- Omi adapts by surface; never duplicates Start OneUp CTA  
- Every touch pulses via `OUHaptics` / `.ouPress*` (see DESIGN-TO-CODE §6.9)  

See `pages/coach.md` (float) · `DESIGN-TO-CODE.md` §5 · `UX-COMPANION-SYSTEM.md` Phase 2.
---

## 8. Screen Contracts (product-wide)

### Today (hero)
- Greeting + **OneUp** wordmark small
- **One primary card** (goal area chip · action title · minutes · why snippet)
- Primary CTA: Start / Complete · **Resume · mm:ss left** when a focus session is paused
- Tiny link under Must CTAs: “Low on energy? Do the 2‑min version” (muted text link, not a second button)
- ≤2 secondary rows — visually de-emphasized
- No stats strip in first viewport (week +1 card lives below the fold)

### Goals
- Grouped by seed area
- Each goal → actions count
- Empty state: seed dogfood CTA

### Coach
- Decision card, not chat
- Proposal + why bullets + **Accept** / **Change**
- “I don’t know what to focus on” tertiary

### Reflection
- Done? · mood (4 options, SF Symbols not emoji-only) · blocker · lesson
- Finish Day → suggests tomorrow

### Progress
- Week trail Mon–Sun (full = ink dot, part = outlined, missed = blank)
- Momentum number + soft copy (no shame)
- Hierarchy: `ENGAGEMENT-INSIGHT.md` · `pages/progress.md` “Journey (latest)” · +1 story (Months / Moments / By goal)

### Plus (stage C — not v1)
- Paywall + inline lock rows: `pages/plus.md` · strategy `BUSINESS-REVIEW-MONETIZATION.md`
- Same ink/paper language; Omi proud pose; no gradients, timers, or strikethrough prices

### Widget
- Compact: action title + area
- Matches Today payload; App Group only

### Auth
- Google button + brand promise one line
- No guest mode

---

## 9. Copy Voice

- Short, decisive, kind. EN primary; VI equivalent tone.
- Prefer: “Your OneUp today” / “One step. That’s enough.”
- Avoid: hustle shame, “don’t break the streak!”

---

## 10. Case-study inputs (research)

See `.planning/phases/01-app-skeleton-locale/UI-RESEARCH-NOTES.md` for Dribbble / UX patterns distilled into do/don’t for OneUp.
