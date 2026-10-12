import React from "react";
import type { CharacterProfile, Expression } from "../../validation/schema";
import type { CharacterState } from "../../animation/controller";
import { easeInOutCubic, lerp } from "../../animation/timing";

/** Body-shape parameters per emotion (extends EMO in pipeline/characters-v2/chars.html). */
type Shape = { sx: number; sy: number; tear: number; wob: number; lean: number };
export const OMI_SHAPES: Record<Expression, Shape> = {
  neutral:   { sx: 1.0,  sy: 1.0,  tear: 0,     wob: 0.016, lean: 0 },
  happy:     { sx: 1.08, sy: 0.93, tear: 0,     wob: 0.02,  lean: 0 },
  sad:       { sx: 1.1,  sy: 0.86, tear: -0.12, wob: 0.008, lean: 0 },
  surprised: { sx: 0.9,  sy: 1.14, tear: 0.08,  wob: 0.03,  lean: 0 },
  confused:  { sx: 0.96, sy: 1.05, tear: -0.04, wob: 0.024, lean: 0.12 },
  focused:   { sx: 1.02, sy: 0.98, tear: 0.14,  wob: 0.01,  lean: 0 },
};

function blobPath(R: number, p: Shape, t: number): string {
  const N = 72, pts: [number, number][] = [];
  for (let i = 0; i < N; i++) {
    const a = (i / N) * Math.PI * 2;
    let r = R * (1 + p.wob * Math.sin(3 * a + t * 2.1) + p.wob * 0.7 * Math.sin(5 * a - t * 1.7) + p.wob * 0.5 * Math.sin(2 * a + t * 1.3));
    const yv = Math.sin(a);
    r *= 1 + p.tear * -yv * 0.5;
    const x = Math.cos(a) * r * p.sx;
    pts.push([x + p.lean * (-yv) * R * 0.4, yv * r * p.sy * (1 + p.tear * 0.25 * Math.max(0, yv))]);
  }
  const f = (n: number) => n.toFixed(1);
  let d = `M${f(pts[0][0])},${f(pts[0][1])}`;
  for (let i = 0; i < N; i++) {
    const p0 = pts[(i - 1 + N) % N], p1 = pts[i], p2 = pts[(i + 1) % N], p3 = pts[(i + 2) % N];
    d += ` C${f(p1[0] + (p2[0] - p0[0]) / 6)},${f(p1[1] + (p2[1] - p0[1]) / 6)} ${f(p2[0] - (p3[0] - p1[0]) / 6)},${f(p2[1] - (p3[1] - p1[1]) / 6)} ${f(p2[0])},${f(p2[1])}`;
  }
  return d + "Z";
}

export const OmiBlob: React.FC<{ state: CharacterState; profile: CharacterProfile; uid: string }> = ({ state: s, profile, uid }) => {
  const INK = profile.colors.ink, PAPER = profile.colors.paper;
  const t = s.t;
  const A = OMI_SHAPES[s.prevExpression], B = OMI_SHAPES[s.expression], k = easeInOutCubic(s.expressionBlend);
  const par = Object.fromEntries((Object.keys(A) as (keyof Shape)[]).map((key) => [key, lerp(A[key], B[key], k)])) as Shape;
  if (s.speaking) { par.sy += 0.04 * s.mouthOpen; par.sx -= 0.03 * s.mouthOpen; }
  const face: Expression = s.expressionBlend >= 0.5 ? s.expression : s.prevExpression;
  const sitting = s.pose === "sitting";
  const R = 110;
  const float = sitting ? 0 : 14 * Math.sin(t * 2.4);
  const cy = sitting ? -R * par.sy * 0.98 : -175 + float;
  const orbit = t * (s.action === "thinking" ? 0.7 : 1.4);
  const d1 = [Math.cos(orbit) * 128, Math.sin(orbit) * 52 + 20], d2 = [Math.cos(orbit + 2.6) * 120, Math.sin(orbit + 2.6) * 58];
  const pulse = 4 * Math.sin(t * 3);
  const shadowK = sitting ? 1 : 0.75 - float / 60;

  const eyes: React.ReactNode[] = [];
  for (const side of [-1, 1]) {
    const x = side * 36 + s.look * 8, y = -8;
    if (face === "happy") { eyes.push(<path key={side} d={`M${x - 15},${y + 6} Q${x},${y - 16} ${x + 15},${y + 6}`} fill="none" stroke={PAPER} strokeWidth={9} strokeLinecap="round" />); continue; }
    const big = face === "surprised" ? 1.3 : face === "confused" ? (side < 0 ? 0.85 : 1.12) : 1;
    const ry = (face === "focused" ? 14 : face === "sad" ? 17 : 21) * big;
    eyes.push(
      <g key={side}>
        <ellipse cx={x} cy={y} rx={17 * big} ry={Math.max(2, ry * (1 - s.blink))} fill={PAPER} />
        {s.blink < 0.5 && <circle cx={x + 4 + s.look * 4} cy={y + 4} r={8 * big} fill={INK} />}
        {face === "sad" && <path d={`M${x - 18 * side},${y - 30} L${x + 14 * side},${y - 22}`} stroke={PAPER} strokeWidth={7} strokeLinecap="round" />}
        {face === "focused" && <path d={`M${x - 18 * side},${y - 18} L${x + 16 * side},${y - 28}`} stroke={PAPER} strokeWidth={7} strokeLinecap="round" />}
      </g>,
    );
  }
  let mouth: React.ReactNode = null;
  if (s.mouthOpen > 0.06) mouth = <ellipse cx={0} cy={34} rx={12 + 4 * s.mouthOpen} ry={4 + 12 * s.mouthOpen} fill={PAPER} />;
  else if (face === "happy") mouth = <path d="M-16,26 Q0,44 16,26" fill="none" stroke={PAPER} strokeWidth={7} strokeLinecap="round" />;
  else if (face === "surprised") mouth = <ellipse cx={0} cy={36} rx={10} ry={13} fill={PAPER} />;
  else if (face === "sad") mouth = <path d="M-14,40 Q0,28 14,40" fill="none" stroke={PAPER} strokeWidth={7} strokeLinecap="round" />;
  else if (face === "confused") mouth = <path d="M-14,36 Q-7,30 0,36 T14,36" fill="none" stroke={PAPER} strokeWidth={6} strokeLinecap="round" />;
  else if (face === "focused") mouth = <path d="M-10,34 L10,34" stroke={PAPER} strokeWidth={7} strokeLinecap="round" />;
  else mouth = <path d="M-12,30 Q0,40 12,30" fill="none" stroke={PAPER} strokeWidth={6} strokeLinecap="round" />;

  return (
    <g>
      <defs>
        <filter id={`${uid}-goo`} x="-60%" y="-60%" width="220%" height="220%">
          <feGaussianBlur stdDeviation={12} />
          <feColorMatrix values="1 0 0 0 0  0 1 0 0 0  0 0 1 0 0  0 0 0 24 -10" />
        </filter>
      </defs>
      <ellipse cx={0} cy={4} rx={(84 - pulse * 2) * shadowK} ry={12} fill={INK} opacity={0.08} />
      <g transform={`translate(0 ${cy})`}>
        <g filter={`url(#${uid}-goo)`} fill={INK}>
          <path d={blobPath(R + pulse, par, t)} />
          <circle cx={d1[0]} cy={d1[1]} r={22 + 6 * Math.sin(t * 2)} />
          <circle cx={d2[0]} cy={d2[1]} r={16 + 5 * Math.cos(t * 2.4)} />
        </g>
        <path d="M-62,-58 Q-40,-84 -8,-86" fill="none" stroke={PAPER} strokeWidth={8} strokeLinecap="round" opacity={0.3} />
        <g transform={`scale(1 ${par.sy})`}>{eyes}{mouth}</g>
        {face === "confused" && <text x={96} y={-96} fontSize={84} fontWeight={700} fill={INK} fontFamily="Be Vietnam Pro">?</text>}
        {face === "surprised" && <g stroke={INK} strokeWidth={8} strokeLinecap="round"><path d="M-100,-120 L-118,-150" /><path d="M0,-150 L0,-186" /><path d="M100,-120 L118,-150" /></g>}
        {s.action === "thinking" && <g fill={INK}><circle cx={120} cy={-120} r={9} /><circle cx={148} cy={-156} r={13} /><circle cx={182} cy={-200} r={18} /></g>}
      </g>
    </g>
  );
};
