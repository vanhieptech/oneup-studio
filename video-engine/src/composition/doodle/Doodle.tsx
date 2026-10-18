import React from "react";
import { BRAND } from "../theme";
import { doodleEase, doodlePaths, pathLength, toPathD, type DoodleKind, type Pt } from "./doodle";

export interface DoodleCue {
  kind: DoodleKind; x: number; y: number; w: number; h: number;
  at?: number; duration?: number; color?: string; seed?: number; width?: number; points?: Pt[];
}

/** One hand-drawn mark drawing itself on over `duration`s starting at `at` (scene time).
 *  Deterministic: same cue + frame = same pixels (anidoodle contract, L-047). */
export const Doodle: React.FC<{ cue: DoodleCue; t: number }> = ({ cue, t }) => {
  const at = cue.at ?? 0, dur = cue.duration ?? 0.6;
  const p = doodleEase((t - at) / dur);
  if (p <= 0) return null;
  const subs = doodlePaths(cue.kind, cue.x, cue.y, cue.w, cue.h, cue.seed ?? 7, cue.points);
  const total = subs.reduce((a, s) => a + pathLength(s), 0) || 1;
  let spent = 0;
  return (
    <g fill="none" stroke={cue.color ?? BRAND.accent} strokeWidth={cue.width ?? 10} strokeLinecap="round" strokeLinejoin="round" opacity={0.96}>
      {subs.map((pts, i) => {
        const len = pathLength(pts), local = Math.max(0, Math.min(1, (p * total - spent) / (len || 1))); spent += len;
        if (local <= 0) return null;
        return <path key={i} d={toPathD(pts)} strokeDasharray={len} strokeDashoffset={len * (1 - local)} />;
      })}
    </g>
  );
};
