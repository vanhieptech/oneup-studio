/**
 * Remotion ports of motionmaxxing measured eases (Apache-2.0 craft data from
 * https://github.com/Tejashmakwana/motionmaxxing @ 8c8ec0f, references/motion.md).
 * Pure functions of progress p ∈ [0,1] — no GSAP. Values approximate the
 * published 10/25/50/75 travel% clusters; overshoots may return >1.
 */
import type React from "react";

const clamp01 = (p: number) => Math.max(0, Math.min(1, p));
const lerp = (a: number, b: number, t: number) => a + (b - a) * t;

/** Power ease-out: 1 - (1-t)^k */
const powOut = (t: number, k: number) => 1 - Math.pow(1 - clamp01(t), k);
/** Power ease-in: t^k */
const powIn = (t: number, k: number) => Math.pow(clamp01(t), k);
/** Smoothstep-ish S-curve */
const softInOut = (t: number) => {
  const x = clamp01(t);
  return x * x * (3 - 2 * x);
};

/**
 * Piecewise linear through control points [[t,y],...] with t,y sorted by t.
 * Used to match published sample points (incl. overshoot y>1).
 */
function poly(pts: Array<[number, number]>) {
  return (t: number) => {
    if (t <= pts[0][0]) return pts[0][1];
    if (t >= pts[pts.length - 1][0]) return pts[pts.length - 1][1];
    for (let i = 0; i < pts.length - 1; i++) {
      const [t0, y0] = pts[i], [t1, y1] = pts[i + 1];
      if (t >= t0 && t <= t1) return lerp(y0, y1, (t - t0) / (t1 - t0));
    }
    return pts[pts.length - 1][1];
  };
}

/** snapSettle: ~54/84/96/98 at 10/25/50/75 → fast snap + soft tail */
const snapSettle = poly([[0, 0], [0.1, 0.54], [0.25, 0.84], [0.5, 0.96], [0.75, 0.98], [1, 1]]);
/** popOver: peak 1.08 at t≈0.72 */
const popOver = poly([[0, 0], [0.1, 0.1], [0.25, 0.46], [0.5, 0.96], [0.72, 1.08], [1, 1]]);
/** crashIn: peak ~1.18 early then settle */
const crashIn = poly([[0, 0], [0.1, 0.91], [0.27, 1.18], [0.5, 1.1], [0.75, 1.03], [1, 1]]);
/** bounceHard: peak ~1.48 mid */
const bounceHard = poly([[0, 0], [0.1, 0.13], [0.25, 0.62], [0.5, 1.38], [0.62, 1.48], [1, 1]]);

export type MmxEaseName =
  | "mmx-cruise" | "mmx-glide" | "mmx-soft-inout" | "mmx-soft-land" | "mmx-gentle-in"
  | "mmx-snap-settle" | "mmx-whip" | "mmx-accel-exit" | "mmx-crash-out"
  | "mmx-pop-over" | "mmx-crash-in" | "mmx-bounce-hard";

export type MmxPresetName = "mmx-oversize-land" | "mmx-cut-on-motion" | "mmx-no-dead-frame";

/** Ease 0→1 (may overshoot >1 for pop/crash/bounce). */
export function mmxEase(name: MmxEaseName, p: number): number {
  const t = clamp01(p);
  switch (name) {
    case "mmx-cruise": return t;
    case "mmx-glide": return powOut(t, 1.7);
    case "mmx-soft-inout": return softInOut(t);
    case "mmx-soft-land": return powOut(t, 3.4);
    case "mmx-gentle-in": return powIn(t, 2.07);
    case "mmx-snap-settle": return snapSettle(t);
    case "mmx-whip": return powOut(t, 2.5);
    case "mmx-accel-exit": return powIn(t, 2.6);
    case "mmx-crash-out": return powIn(t, 4);
    case "mmx-pop-over": return popOver(t);
    case "mmx-crash-in": return crashIn(t);
    case "mmx-bounce-hard": return bounceHard(t);
  }
}

export const MMX_DURATION_F: Record<MmxEaseName, number> = {
  "mmx-cruise": 26, "mmx-glide": 10, "mmx-soft-inout": 9, "mmx-soft-land": 12, "mmx-gentle-in": 9,
  "mmx-snap-settle": 11, "mmx-whip": 13, "mmx-accel-exit": 13, "mmx-crash-out": 17,
  "mmx-pop-over": 15, "mmx-crash-in": 10, "mmx-bounce-hard": 22,
};

/** Element CSS at progress p for common comic presets. */
export function mmxStyle(
  name: MmxEaseName | MmxPresetName,
  p: number,
  opt: { fromScale?: number; driftPx?: number; dir?: 1 | -1 } = {},
): React.CSSProperties {
  if (name === "mmx-cut-on-motion") return { opacity: 1 };
  if (name === "mmx-no-dead-frame") {
    const d = (opt.driftPx ?? 2) * p; // caller should pass looping p for hold
    return { transform: `translate(${d}px, ${d * 0.4}px)` };
  }
  if (name === "mmx-oversize-land") {
    const e = mmxEase("mmx-crash-in", p);
    const from = opt.fromScale ?? 3.2;
    const s = lerp(from, 1, Math.min(1, e));
    return { opacity: Math.min(1, e * 1.2), transform: `scale(${s})`, transformOrigin: "center" };
  }
  const e = mmxEase(name as MmxEaseName, p);
  switch (name as MmxEaseName) {
    case "mmx-soft-land":
    case "mmx-glide":
      return { opacity: Math.min(1, e), transform: `translateY(${(1 - Math.min(1, e)) * 24}px)` };
    case "mmx-snap-settle":
      return { opacity: Math.min(1, e), transform: `scale(${lerp(0.92, 1, Math.min(1, e))})` };
    case "mmx-pop-over":
      return { transform: `scale(${e})` };
    case "mmx-crash-in": {
      const from = opt.fromScale ?? 2.5;
      return { transform: `scale(${lerp(from, 1, Math.min(1, e))})`, opacity: Math.min(1, e) };
    }
    case "mmx-accel-exit":
    case "mmx-crash-out": {
      const d = (opt.dir ?? 1) * 120;
      return { opacity: 1 - e * 0.85, transform: `translateX(${e * d}px) scale(${lerp(1, 0.85, e)})` };
    }
    case "mmx-whip":
      return { opacity: Math.min(1, e), transform: `scale(${lerp(1.12, 1, Math.min(1, e))})` };
    default:
      return { opacity: Math.min(1, e) };
  }
}

export const MMX_EASE_NAMES = Object.keys(MMX_DURATION_F) as MmxEaseName[];
