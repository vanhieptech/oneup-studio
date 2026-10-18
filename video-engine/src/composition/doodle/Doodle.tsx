import React from "react";
import { BRAND } from "../theme";
import { doodleEase, doodlePaths, fadeFactor, interpTranslate, pathLength, strokePaths, strokeWindow, toPathD, type DoodleKind, type DoodleStroke, type Pt, type TranslateKeyframe } from "./doodle";

export interface DoodleCue {
  kind: DoodleKind; x: number; y: number; w: number; h: number;
  at?: number; duration?: number; color?: string; seed?: number; width?: number; points?: Pt[];
  /** kind="drawing" (creative mode): ordered multi-stroke picture; the drawing IS the content. */
  strokes?: DoodleStroke[];
  label?: { text: string; x: number; y: number; at?: number; size?: number; color?: string };
  fadeOutAt?: number; fadeOutDuration?: number;
  translateKeyframes?: TranslateKeyframe[]; hop?: number;
}

/** Brand-fit (L-047): thin refined accent stroke (default 7px @1080, opacity .92), low jitter in doodle.ts — designed, not sketchy.
 *  One hand-drawn mark drawing itself on over `duration`s starting at `at` (scene time).
 *  Deterministic: same cue + frame = same pixels (anidoodle contract, L-047). */
export const Doodle: React.FC<{ cue: DoodleCue; t: number }> = ({ cue, t }) => {
  const at = cue.at ?? 0, dur = cue.duration ?? 0.6;

  if (cue.kind === "drawing") {
    const fade = fadeFactor(t, cue.fadeOutAt, cue.fadeOutDuration ?? 0.4);
    if (fade <= 0 || t < at) return null;
    const tr = interpTranslate(cue.translateKeyframes, t, cue.hop ?? 0);
    const labelP = cue.label ? Math.max(0, Math.min(1, (t - (cue.label.at ?? at + 0.8)) / 0.35)) : 0;
    return (
      <g opacity={0.98 * fade} transform={`translate(${tr.x} ${tr.y})`}>
        {(cue.strokes ?? []).map((s, i) => {
          const [st, en] = strokeWindow(at, s, i);
          const p = doodleEase((t - st) / Math.max(0.01, en - st));
          if (p <= 0) return null;
          const pts = strokePaths(s, (cue.seed ?? 7) + i * 13);
          const len = pathLength(pts) || 1;
          const fillP = s.fill ? Math.max(0, Math.min(1, (t - en) / 0.45)) : 0;
          return (
            <g key={i}>
              {s.fill && fillP > 0 ? <polygon points={pts.map((q) => `${q[0].toFixed(1)},${q[1].toFixed(1)}`).join(" ")} fill={s.fill} opacity={(s.fillOpacity ?? 0.9) * fillP} stroke="none" /> : null}
              <path d={toPathD(pts)} fill="none" stroke={s.color ?? cue.color ?? BRAND.ink} strokeWidth={s.width ?? cue.width ?? 7} strokeLinecap="round" strokeLinejoin="round" strokeDasharray={len} strokeDashoffset={len * (1 - p)} />
            </g>
          );
        })}
        {cue.label && labelP > 0 ? (
          <text x={cue.label.x} y={cue.label.y} textAnchor="middle" fontFamily="Be Vietnam Pro" fontWeight={800} fontSize={cue.label.size ?? 52} fill={cue.label.color ?? BRAND.ink} opacity={labelP}>{cue.label.text}</text>
        ) : null}
      </g>
    );
  }

  const p = doodleEase((t - at) / dur);
  if (p <= 0) return null;
  const fade = fadeFactor(t, cue.fadeOutAt, cue.fadeOutDuration ?? 0.4);
  if (fade <= 0) return null;
  const subs = doodlePaths(cue.kind, cue.x, cue.y, cue.w, cue.h, cue.seed ?? 7, cue.points);
  const total = subs.reduce((a, s) => a + pathLength(s), 0) || 1;
  let spent = 0;
  return (
    <g fill="none" stroke={cue.color ?? BRAND.accent} strokeWidth={cue.width ?? 7} strokeLinecap="round" strokeLinejoin="round" opacity={0.92 * fade}>
      {subs.map((pts, i) => {
        const len = pathLength(pts), local = Math.max(0, Math.min(1, (p * total - spent) / (len || 1))); spent += len;
        if (local <= 0) return null;
        return <path key={i} d={toPathD(pts)} strokeDasharray={len} strokeDashoffset={len * (1 - local)} />;
      })}
    </g>
  );
};
