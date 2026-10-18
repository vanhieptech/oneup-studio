// Doodle draw-on primitives for @hi.oneup comic scenes (anidoodle port, Apache-2.0).
// Adapted from alexgreensh/anidoodle @ 4db69644b994ae9caf9e20936506954b2f5e4872,
// skills/anidoodle/engine/src/canvas-core/core.ts: seeded rng(seed), jitter(),
// sample() (Catmull-Rom), oval()/line() geometry, and pen(progress) draw-on where
// only the first `progress` of the centreline is drawn. Re-implemented for SVG/
// Remotion (no canvas, no rng at render time beyond the seeded one, frame-pure).
// Full upstream tree + LICENSE + NOTICE: resources/refs/anidoodle/.
// See research/references/anidoodle-notes.md for what was adopted vs not.

export type Pt = [number, number];

/** Deterministic seeded RNG (mulberry-style, ported from anidoodle core rng). */
export const rng = (seed: number) => {
  let a = seed >>> 0;
  return () => { a = (a + 0x6d2b79f5) | 0; let t = Math.imul(a ^ (a >>> 15), 1 | a); t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t; return ((t ^ (t >>> 14)) >>> 0) / 4294967296; };
};

export const jitterPts = (pts: Pt[], amt: number, seed: number): Pt[] => {
  if (amt <= 0) return pts;
  const r = rng(seed);
  return pts.map(([x, y]) => [x + (r() - 0.5) * 2 * amt, y + (r() - 0.5) * 2 * amt] as Pt);
};

/** Catmull-Rom sampling (anidoodle sample(), per=6 default for SVG smoothness). */
export const samplePts = (pts: Pt[], closed = false, per = 6): Pt[] => {
  if (pts.length < 2) return pts;
  const n = pts.length, at = (i: number): Pt => (closed ? pts[((i % n) + n) % n] : pts[Math.max(0, Math.min(n - 1, i))]), out: Pt[] = [], segs = closed ? n : n - 1;
  for (let i = 0; i < segs; i++) {
    const [p0, p1, p2, p3] = [at(i - 1), at(i), at(i + 1), at(i + 2)];
    for (let k = 0; k < per; k++) { const t = k / per, t2 = t * t, t3 = t2 * t; out.push([0.5 * (2 * p1[0] + (-p0[0] + p2[0]) * t + (2 * p0[0] - 5 * p1[0] + 4 * p2[0] - p3[0]) * t2 + (-p0[0] + 3 * p1[0] - 3 * p2[0] + p3[0]) * t3), 0.5 * (2 * p1[1] + (-p0[1] + p2[1]) * t + (2 * p0[1] - 5 * p1[1] + 4 * p2[1] - p3[1]) * t2 + (-p0[1] + 3 * p1[1] - 3 * p2[1] + p3[1]) * t3)]); }
  }
  out.push(closed ? out[0] : pts[n - 1]);
  return out;
};

export const pathLength = (pts: Pt[]): number => pts.reduce((a, p, i) => (i ? a + Math.hypot(p[0] - pts[i - 1][0], p[1] - pts[i - 1][1]) : a), 0);
export const toPathD = (pts: Pt[]): string => pts.map((p, i) => `${i ? "L" : "M"}${p[0].toFixed(1)},${p[1].toFixed(1)}`).join(" ");

/** Hand-drawn ease: fast nib start, gentle lift at the end. Pure, frame-driven. */
export const doodleEase = (p: number): number => { const c = Math.max(0, Math.min(1, p)); return 1 - Math.pow(1 - c, 2.2); };

export type DoodleKind = "circle" | "underline" | "arrow" | "check" | "cross" | "sketch-box" | "path" | "drawing";

/** One stroke of a purposeful multi-stroke drawing (creative mode, L-047 amended).
 *  offset/duration are relative to the parent cue's `at`; fill fades in after the stroke completes. */
export interface DoodleStroke {
  points: Pt[]; closed?: boolean; offset?: number; duration?: number;
  color?: string; width?: number; seed?: number; fill?: string; fillOpacity?: number; smooth?: boolean;
}
export interface TranslateKeyframe { at: number; x: number; y: number }

/** Stroke geometry: sampled (+seeded jitter), closed strokes wrap around. Pure/deterministic. */
export function strokePaths(stroke: DoodleStroke, fallbackSeed = 7): Pt[] {
  const j = jitterPts(stroke.points, 1, stroke.seed ?? fallbackSeed);
  return stroke.smooth === false ? (stroke.closed ? [...j, j[0]] : j) : samplePts(j, !!stroke.closed, 6);
}
/** Absolute [start,end] window of a stroke inside its cue. */
export const strokeWindow = (cueAt: number, stroke: DoodleStroke, i = 0): [number, number] => {
  const start = cueAt + (stroke.offset ?? i * 0.15);
  return [start, start + (stroke.duration ?? 0.5)];
};
/** Piecewise-linear translate from keyframes (sorted by at); hop adds a small arc lift mid-segment. Pure. */
export function interpTranslate(keys: TranslateKeyframe[] | undefined, t: number, hop = 0): { x: number; y: number } {
  if (!keys?.length) return { x: 0, y: 0 };
  const ks = [...keys].sort((a, b) => a.at - b.at);
  if (t <= ks[0].at) return { x: ks[0].x, y: ks[0].y };
  for (let i = 1; i < ks.length; i++) {
    if (t <= ks[i].at) {
      const a = ks[i - 1], b = ks[i], span = Math.max(1e-6, b.at - a.at), p = (t - a.at) / span;
      const e = p * p * (3 - 2 * p); // smoothstep, brand ease
      return { x: a.x + (b.x - a.x) * e, y: a.y + (b.y - a.y) * e - hop * Math.sin(Math.PI * p) };
    }
  }
  const last = ks[ks.length - 1];
  return { x: last.x, y: last.y };
}
/** Fade-out factor: 1 before fadeOutAt, ->0 over fadeOutDuration. */
export const fadeFactor = (t: number, fadeOutAt?: number, fadeOutDuration = 0.4): number =>
  fadeOutAt === undefined ? 1 : Math.max(0, Math.min(1, 1 - (t - fadeOutAt) / Math.max(0.01, fadeOutDuration)));


/** Build the sub-paths (sampled points) for one doodle cue, in design px (1080-wide). */
export function doodlePaths(kind: DoodleKind, x: number, y: number, w: number, h: number, seed = 7, points?: Pt[]): Pt[][] {
  const cx = x + w / 2, cy = y + h / 2;
  switch (kind) {
    case "circle": {
      const ctrl: Pt[] = Array.from({ length: 12 }, (_, i) => { const a = -1.9 + (i / 12) * Math.PI * 2; return [cx + Math.cos(a) * w / 2, cy + Math.sin(a) * h / 2] as Pt; });
      return [samplePts(jitterPts(ctrl, 1.4, seed), true, 6)];
    }
    case "underline": return [samplePts(jitterPts([[x, cy], [cx, cy + h * 0.35], [x + w, cy]] as Pt[], 1.2, seed), false, 8)];
    case "arrow": {
      const shaft = samplePts(jitterPts([[x, cy], [cx, cy - h * 0.3], [x + w, cy]] as Pt[], 1.2, seed), false, 8);
      const tip: Pt = [x + w, cy], head = Math.max(18, Math.min(w, h) * 0.45);
      return [shaft, [[tip[0] - head, tip[1] - head * 0.55], tip] as Pt[], [[tip[0] - head * 0.9, tip[1] + head * 0.6], tip] as Pt[]];
    }
    case "check": return [samplePts(jitterPts([[x, cy], [x + w * 0.38, y + h], [x + w, y]] as Pt[], 1.2, seed), false, 6)];
    case "cross": return [
      samplePts(jitterPts([[x, y], [x + w, y + h]] as Pt[], 1.2, seed), false, 6),
      samplePts(jitterPts([[x + w, y], [x, y + h]] as Pt[], 1.2, seed + 3), false, 6),
    ];
    case "sketch-box": {
      const r = Math.min(28, w / 4, h / 4), ctrl: Pt[] = [[x + r, y], [x + w - r, y], [x + w, y + r], [x + w, y + h - r], [x + w - r, y + h], [x + r, y + h], [x, y + h - r], [x, y + r]];
      return [samplePts(jitterPts(ctrl, 1.4, seed), true, 5)];
    }
    case "path": return points && points.length > 1 ? [samplePts(jitterPts(points, 1, seed), false, 6)] : [];
    case "drawing": return []; // multi-stroke geometry lives in strokePaths(); see Doodle.tsx
  }
}
