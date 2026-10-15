/**
 * Frame-driven ports of transitions.dev (https://transitions.dev, Jakub Antalik,
 * Transitions.dev License, commit 8c92530c). Original CSS transitions re-expressed as
 * pure functions of progress p (0→1) so Remotion renders are deterministic.
 * UI pixel values scaled ×S for a 1080×1920 frame. Used inside our videos only, not redistributed as a library.
 */
import type React from "react";

/** cubic-bezier(x1,y1,x2,y2) evaluated at t (Newton + bisection), same curve as CSS. */
export function bezier(x1: number, y1: number, x2: number, y2: number) {
  const cx = 3 * x1, bx = 3 * (x2 - x1) - cx, ax = 1 - cx - bx;
  const cy = 3 * y1, by = 3 * (y2 - y1) - cy, ay = 1 - cy - by;
  const sx = (t: number) => ((ax * t + bx) * t + cx) * t;
  const sy = (t: number) => ((ay * t + by) * t + cy) * t;
  return (x: number) => {
    if (x <= 0) return 0; if (x >= 1) return 1;
    let lo = 0, hi = 1, t = x;
    for (let i = 0; i < 24; i++) { const v = sx(t) - x; if (Math.abs(v) < 1e-6) break; if (v > 0) hi = t; else lo = t; t = (lo + hi) / 2; }
    return sy(t);
  };
}
const OUT = bezier(0.22, 1, 0.36, 1);       // transitions.dev --p*-ease (expo-out-ish)
const INOUT = bezier(0.42, 0, 0.58, 1);     // CSS ease-in-out
const POP = bezier(0.34, 1.36, 0.64, 1);    // badge spring pop
const S = 6;                                // UI px → video px
const clamp = (p: number) => Math.max(0, Math.min(1, p));
const lerp = (a: number, b: number, e: number) => a + (b - a) * e;

export type TdevName = "tdev-modal" | "tdev-page" | "tdev-panel" | "tdev-text-swap" | "tdev-icon-swap" | "tdev-stagger" | "tdev-badge" | "tdev-shake";

/** Entrance style at progress p. dir=-1 for back/left (page). i = stagger index (stagger). */
export function tdevStyle(name: TdevName, p: number, opt: { dir?: 1 | -1; i?: number; dur?: number } = {}): React.CSSProperties {
  const q = clamp(p);
  switch (name) {
    case "tdev-modal": { const e = OUT(q); return { opacity: e, transform: `scale(${lerp(0.96, 1, e)})`, transformOrigin: "center" }; }
    case "tdev-page": { const e = OUT(q); const d = (opt.dir ?? 1) * 8 * S; return { opacity: e, transform: `translateX(${(1 - e) * d}px)`, filter: `blur(${(1 - e) * 3 * S / 2}px)` }; }
    case "tdev-panel": { const e = OUT(q); return { opacity: e, transform: `translateY(${(1 - e) * 100 * S / 2}px)`, filter: `blur(${(1 - e) * 2 * S / 2}px)` }; }
    case "tdev-text-swap": { const e = INOUT(q); return { opacity: e, transform: `translateY(${(1 - e) * 4 * S}px)`, filter: `blur(${(1 - e) * 2 * S / 2}px)` }; }
    case "tdev-icon-swap": { const e = INOUT(q); return { opacity: e, transform: `scale(${lerp(0.25, 1, e)})`, filter: `blur(${(1 - e) * 2 * S / 2}px)` }; }
    case "tdev-stagger": { // 500ms each, 40ms stagger, as fraction of dur (default 0.5s)
      const dur = opt.dur ?? 0.5, off = ((opt.i ?? 0) * 0.04) / dur; const e = OUT(clamp((q - off) / Math.max(1e-3, 1 - off)));
      return { opacity: e, transform: `translateY(${(1 - e) * 12 * S}px)`, filter: `blur(${(1 - e) * 3 * S / 2}px)` };
    }
    case "tdev-badge": { // slide 260ms + pop 500ms + fade 400ms → normalised to pop duration
      const sl = OUT(clamp(q / 0.52)), pop = POP(q), fd = OUT(clamp(q / 0.8));
      return { opacity: fd, transform: `translate(${(1 - sl) * -8.2 * S}px, ${(1 - sl) * 12.4 * S}px) scale(${pop})`, filter: `blur(${(1 - fd) * 2 * S / 2}px)` };
    }
    case "tdev-shake": { // keyframes 0 → +d → -over → +over/2 → 0
      const d = 6 * S, o = 4 * S, k = [0, d, -o, o / 2, 0], seg = q * 4, j = Math.min(3, Math.floor(seg)), e = OUT(seg - j);
      return { transform: `translateX(${lerp(k[j], k[j + 1], q >= 1 ? 1 : e)}px)` };
    }
  }
}
/** Default durations (seconds) at video scale; UI originals are 150–500ms, stretched for readability on TikTok. */
export const TDEV_DURATION: Record<TdevName, number> = {
  "tdev-modal": 0.4, "tdev-page": 0.45, "tdev-panel": 0.5, "tdev-text-swap": 0.3, "tdev-icon-swap": 0.35, "tdev-stagger": 0.5, "tdev-badge": 0.5, "tdev-shake": 0.35,
};
export const TDEV_NAMES = Object.keys(TDEV_DURATION) as TdevName[];
