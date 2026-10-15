---
title: "OneUp Color — source of truth"
date: 2026-10-12
type: brand
tags: [brand]
status: ready
source: "oneup-studio (soạn trong repo)"
---

# OneUp Color — source of truth

> **File này là nguồn màu.** `MASTER.md` §2 chỉ trỏ về đây.  
> `/colorize` updates belong here first, then `OUColor.swift` + prototype CSS.

**Showcase:** `prototype/oneup-brand/color.html`  
**Locked:** 2026-09-17 · Confident black / white · Dark ramp 2026-09-19 (paper-on-ink)

---

## Philosophy

**Ink + paper = brand.**  
CTA is black in light; **paper button on ink ground** in dark. Surfaces follow appearance. Hue is **semantic only** — never the identity.

Story fit: calm companion (Omi), decisive Today action, no hustle chrome. Light-first product; dark is a **designed companion ramp**, not inverted-light patches.

| Use hue for | Never use hue for |
|-------------|-------------------|
| Success (complete) | Primary CTA |
| Danger (errors) | Logo / wordmark |
| Soft momentum (at-risk insight) | Tab bar / chrome |
| | Rainbow Progress walls |

**Locked out:** purple AI · cream/terracotta · teal-as-brand sprawl · neon glow · pure sterile `#000` / `#FFF` as only pair.

---

## Tokens

### Light

| Role | Hex | Swift `Color.ou.*` | Notes |
|------|-----|-------------------|-------|
| Background | `#F7F7F5` | `bg` | Soft paper (not pure `#fff`) |
| Surface | `#FFFFFF` | `surface` | Cards |
| Ink | `#111111` | `ink` | Text, icons, brand |
| Muted | `#6B6B6B` | `muted` | Secondary copy |
| Border | `#E8E8E6` | `border` | Hairline |
| Primary / CTA | `#111111` | `primary` | Ink button |
| On Primary | `#FFFFFF` | `onPrimary` | |
| Accent (+1) | `#111111` | `accent` | Shape carries +1, not hue |
| Soft / coach | `#F4F4F2` | `coachTint` | Quiet wash |
| Soft track | `#F0F0EE` | `soft` | Chips / chart tracks |
| Momentum | `#B45309` | `momentum` | Semantic only |
| Success | `#1A7F4B` | `success` | Complete only |
| Danger | `#B91C1C` | `danger` | Errors only |

Journey extra (light): `--primary-press: #2A2A2A` (pressed ink).

### Dark (paper-on-ink)

Dark mirrors AppIcon Pair +Bond dark (`#111111` canvas · `#F7F7F5` mark) — **paper CTA on ink ground**, not a second ink button on charcoal.

| Role | Hex | Swift `Color.ou.*` | Notes |
|------|-----|-------------------|-------|
| Background | `#111111` | `bg` | Match AppIcon dark canvas |
| Surface | `#1C1C1A` | `surface` | Card lift — warm-neutral, not blue-gray |
| Ink | `#F7F7F5` | `ink` | Paper text / icons / mark |
| Muted | `#A3A3A0` | `muted` | Secondary copy ≥4.5:1 on bg/surface |
| Border | `#2E2E2C` | `border` | Hairline |
| Primary / CTA | `#F7F7F5` | `primary` | **Paper button** (inverted) |
| On Primary | `#111111` | `onPrimary` | Ink label on paper CTA |
| Accent (+1) | `#F7F7F5` | `accent` | Same as primary — shape carries +1 |
| Soft / coach | `#1A1A18` | `coachTint` | Quiet wash above bg |
| Soft track | `#242422` | `soft` | Chips / tracks |
| Success | `#2F9E66` | `success` | Lifted for dark contrast; complete only |
| Momentum | `#D97706` | `momentum` | Lifted amber; semantic only |
| Danger | `#DC2626` | `danger` | Lifted red; errors only |

Journey extra (dark): `--primary-press: #E8E8E6` (pressed paper slightly dimmed).

### Ratio

- **~90%** neutrals (bg / surface / ink / muted)  
- **~8%** CTA (ink in light · paper in dark)  
- **~2%** semantic hue  

### Contrast

Body text ≥ **4.5:1** on bg/surface. UI icons that convey state ≥ **3:1**.

### 60 / 30 / 10 summary

| Band | Light | Dark |
|------|-------|------|
| 60% dominant | `#F7F7F5` bg | `#111111` bg |
| 30% secondary | `#FFFFFF` surface + soft washes | `#1C1C1A` surface + coach/soft |
| 10% accent | `#111111` CTA | `#F7F7F5` CTA |
| Destructive | `#B91C1C` | `#DC2626` |

---

## Application map

| Surface | Color |
|---------|--------|
| Today Start / Accept CTA | Light: `primary` ink · Dark: `primary` paper on ink ground |
| Wordmark “OneUp.” | `ink` · period muted |
| Logo mark | `ink` on paper · invert on black (dark AppIcon = paper mark on `#111111`) |
| Complete check | `success` |
| Progress “at risk” | `momentum` + label (not color alone) |
| Omi coach wash | `coachTint` |
| Skip / quiet | `muted` — **never** danger red |

---

## Sync checklist

When changing color:

1. Update **this file**  
2. Update `OneUpShared/Design/OUColor.swift`  
3. Update `prototype/oneup-journey/index.html` `:root` (+ `@media (prefers-color-scheme: dark)`)  
4. Update `prototype/oneup-brand/color.html` swatches  
5. Keep `MASTER.md` §2 as a short pointer only  
