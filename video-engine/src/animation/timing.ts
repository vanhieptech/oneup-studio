import type { VideoPlan } from "../validation/schema";

export const secondsToFrames = (s: number, fps: number) => Math.round(s * fps);
export const clamp = (x: number, a = 0, b = 1) => Math.max(a, Math.min(b, x));
export const lerp = (a: number, b: number, t: number) => a + (b - a) * t;
export const easeInOutCubic = (t: number) => (t < 0.5 ? 4 * t * t * t : 1 - Math.pow(-2 * t + 2, 3) / 2);
export const easeOutBack = (t: number) => { const c = 1.7; return 1 + (c + 1) * Math.pow(t - 1, 3) + c * Math.pow(t - 1, 2); };
/** Damped spring 0→1 (overshoots), pure function of time in seconds. */
export const springAt = (t: number, stiffness = 14, damping = 6) => (t <= 0 ? 0 : 1 - Math.exp(-damping * t) * Math.cos(stiffness * t));
/** progress of t inside [a,b], clamped */
export const progress = (t: number, a: number, b: number) => (b <= a ? (t >= b ? 1 : 0) : clamp((t - a) / (b - a)));

/** Deterministic hash → [0,1). Same seed always gives same value (no Math.random). */
export function hash01(seed: string | number): number {
  let h = 2166136261;
  const s = String(seed);
  for (let i = 0; i < s.length; i++) { h ^= s.charCodeAt(i); h = Math.imul(h, 16777619); }
  h ^= h >>> 13; h = Math.imul(h, 0x5bd1e995); h ^= h >>> 15;
  return (h >>> 0) / 4294967296;
}

export interface SceneTiming { id: string; index: number; from: number; durationInFrames: number; transitionFrames: number }

/** Lays scenes end-to-end. Transitions overlap into the *incoming* scene's first frames, so total = Σ durations. */
export function buildTimeline(plan: VideoPlan): { scenes: SceneTiming[]; durationInFrames: number } {
  const { fps } = plan.video;
  let from = 0;
  const scenes = plan.scenes.map((s, index) => {
    const durationInFrames = Math.max(1, secondsToFrames(s.duration, fps));
    const transitionFrames = s.transition.type === "cut" ? 0 : Math.min(secondsToFrames(s.transition.duration, fps), Math.floor(durationInFrames / 2));
    const t = { id: s.id, index, from, durationInFrames, transitionFrames };
    from += durationInFrames;
    return t;
  });
  return { scenes, durationInFrames: Math.max(1, from) };
}
