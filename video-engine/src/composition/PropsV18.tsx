import React from "react";
import { BRAND } from "./theme";
import { springAt, hash01 } from "../animation/timing";
import { C05_KINDS, C05_ABS } from "./PropsC05";

/** clip-04 v18 props (L-050: meaning by objects, no text inside images). Scene seconds, design px (1080 wide).
 *  Icons: Phosphor Icons core 2.1.1 (MIT, https://github.com/phosphor-icons/core), paths inlined. */
const { ink, paper, soft, accent, muted } = BRAND;
type P = Record<string, any>; // eslint-disable-line @typescript-eslint/no-explicit-any
const cl = (x: number, a = 0, b = 1) => Math.max(a, Math.min(b, x));
const lin = (t: number, at: number, d: number) => cl((t - at) / Math.max(1e-3, d));
const eo = (u: number) => 1 - Math.pow(1 - u, 3);
const pop = (t: number, at: number) => (t < at ? 0 : Math.min(1.12, springAt(t - at, 18, 9)));

export const ICON: Record<string, string> = {
  "suitcase": "M216,56H176V48a24,24,0,0,0-24-24H104A24,24,0,0,0,80,48v8H40A16,16,0,0,0,24,72V200a16,16,0,0,0,16,16H216a16,16,0,0,0,16-16V72A16,16,0,0,0,216,56ZM96,72h64V200H96Zm0-24a8,8,0,0,1,8-8h48a8,8,0,0,1,8,8v8H96Z",
  "suitcase-line": "M216,56H176V48a24,24,0,0,0-24-24H104A24,24,0,0,0,80,48v8H40A16,16,0,0,0,24,72V200a16,16,0,0,0,16,16H216a16,16,0,0,0,16-16V72A16,16,0,0,0,216,56ZM96,48a8,8,0,0,1,8-8h48a8,8,0,0,1,8,8v8H96Zm64,24V200H96V72ZM40,72H80V200H40ZM216,200H176V72h40V200Z",
  "thumbs": "M234,80.12A24,24,0,0,0,216,72H160V56a40,40,0,0,0-40-40,8,8,0,0,0-7.16,4.42L75.06,96H32a16,16,0,0,0-16,16v88a16,16,0,0,0,16,16H204a24,24,0,0,0,23.82-21l12-96A24,24,0,0,0,234,80.12ZM32,112H72v88H32Z",
  "check": "M232.49,80.49l-128,128a12,12,0,0,1-17,0l-56-56a12,12,0,1,1,17-17L96,183,215.51,63.51a12,12,0,0,1,17,17Z",
  "hand": "M224,104v50.93c0,46.2-36.85,84.55-83,85.06A83.71,83.71,0,0,1,80.6,215.4C58.79,192.33,34.15,136,34.15,136a16,16,0,0,1,6.53-22.23c7.66-4,17.1-.84,21.4,6.62l21,36.44a6.09,6.09,0,0,0,6,3.09l.12,0A8.19,8.19,0,0,0,96,151.74V32a16,16,0,0,1,16.77-16c8.61.4,15.23,7.82,15.23,16.43V104a8,8,0,0,0,8.53,8,8.17,8.17,0,0,0,7.47-8.25V88a16,16,0,0,1,16.77-16c8.61.4,15.23,7.82,15.23,16.43V112a8,8,0,0,0,8.53,8,8.17,8.17,0,0,0,7.47-8.25v-7.28c0-8.61,6.62-16,15.23-16.43A16,16,0,0,1,224,104Z",
  "chat": "M128,24A104,104,0,0,0,36.18,176.88L24.83,210.93a16,16,0,0,0,20.24,20.24l34.05-11.35A104,104,0,1,0,128,24ZM84,140a12,12,0,1,1,12-12A12,12,0,0,1,84,140Zm44,0a12,12,0,1,1,12-12A12,12,0,0,1,128,140Zm44,0a12,12,0,1,1,12-12A12,12,0,0,1,172,140Z",
  "moon": "M235.54,150.21a104.84,104.84,0,0,1-37,52.91A104,104,0,0,1,32,120,103.09,103.09,0,0,1,52.88,57.48a104.84,104.84,0,0,1,52.91-37,8,8,0,0,1,10,10,88.08,88.08,0,0,0,109.8,109.8,8,8,0,0,1,10,10Z",
  "sun": "M120,40V16a8,8,0,0,1,16,0V40a8,8,0,0,1-16,0Zm8,24a64,64,0,1,0,64,64A64.07,64.07,0,0,0,128,64ZM58.34,69.66A8,8,0,0,0,69.66,58.34l-16-16A8,8,0,0,0,42.34,53.66Zm0,116.68-16,16a8,8,0,0,0,11.32,11.32l16-16a8,8,0,0,0-11.32-11.32ZM192,72a8,8,0,0,0,5.66-2.34l16-16a8,8,0,0,0-11.32-11.32l-16,16A8,8,0,0,0,192,72Zm5.66,114.34a8,8,0,0,0-11.32,11.32l16,16a8,8,0,0,0,11.32-11.32ZM48,128a8,8,0,0,0-8-8H16a8,8,0,0,0,0,16H40A8,8,0,0,0,48,128Zm80,80a8,8,0,0,0-8,8v24a8,8,0,0,0,16,0V216A8,8,0,0,0,128,208Zm112-88H216a8,8,0,0,0,0,16h24a8,8,0,0,0,0-16Z",
};
export const Icon: React.FC<{ name: string; size: number; fill?: string; opacity?: number; stroke?: string; sw?: number }> = ({ name, size, fill = ink, opacity = 1, stroke, sw = 0 }) =>
  <g transform={`translate(${-size / 2} ${-size / 2}) scale(${size / 256})`} opacity={opacity}>
    <path d={ICON[name]} fill={fill} stroke={stroke} strokeWidth={stroke ? sw * 256 / size : 0} strokeLinejoin="round" />
  </g>;

/** tick badge: accent disc + paper check */
export const Tick: React.FC<{ r?: number }> = ({ r = 34 }) => <g>
  <circle cx={4} cy={5} r={r} fill={ink} /><circle r={r} fill={accent} stroke={ink} strokeWidth={6} />
  <Icon name="check" size={r * 1.25} fill={paper} />
</g>;

/** Window = time marker (night: moon + stars; day: sun rises). sky: [[t, "night"|"day"], ...]; each change blends 0.55s. */
export const Window: React.FC<{ p: P; t: number }> = ({ p, t }) => {
  const x = p.wx ?? 640, y = p.wy ?? 250, w = p.ww ?? 320, h = p.wh ?? 300;
  const keys: [number, string][] = p.sky ?? [[0, "day"]];
  let d = keys[0][1] === "day" ? 1 : 0, lastAt = -99;
  for (let i = 1; i < keys.length; i++) { const [at, v] = keys[i]; if (t < at) break; const tgt = v === "day" ? 1 : 0; const u = eo(lin(t, at, 0.55)); d = d + (tgt - d) * u; lastAt = at; }
  void lastAt;
  const id = `win${Math.round(x)}${Math.round(y)}`;
  const sky = d > 0.5 ? soft : ink;
  const sunY = y + h + 70 - (h * 0.62 + 70) * eo(d), moonY = y + h * 0.36 + (1 - d) * 0 + d * (h * 0.9);
  return <g>
    <defs><clipPath id={id}><rect x={x} y={y} width={w} height={h} rx={36} /></clipPath></defs>
    <rect x={x + 10} y={y + 12} width={w} height={h} rx={36} fill={ink} />
    <g clipPath={`url(#${id})`}>
      <rect x={x} y={y} width={w} height={h} fill={ink} />
      <rect x={x} y={y} width={w} height={h} fill={soft} opacity={d} />
      {[[0.18, 0.2], [0.62, 0.14], [0.8, 0.42], [0.42, 0.62]].map(([a, b], i) => <circle key={i} cx={x + w * a} cy={y + h * b} r={6} fill={paper} opacity={(1 - d) * (0.6 + 0.4 * Math.sin(t * 3 + i))} />)}
      <g transform={`translate(${x + w * 0.3} ${moonY})`} opacity={1 - d}><Icon name="moon" size={104} fill={paper} /></g>
      <g transform={`translate(${x + w * 0.3} ${sunY}) rotate(${t * 12})`}><Icon name="sun" size={128} fill={accent} stroke={ink} sw={7} /></g>
    </g>
    <rect x={x} y={y} width={w} height={h} rx={36} fill="none" stroke={ink} strokeWidth={10} />
    <path d={`M${x + w / 2},${y} V${y + h} M${x},${y + h / 2} H${x + w}`} stroke={ink} strokeWidth={8} />
    <rect x={x - 18} y={y + h} width={w + 36} height={20} rx={10} fill={ink} />
    {void sky}
  </g>;
};

/** Tabletop in front of the character (things lie ON it). */
const Table: React.FC<{ p: P; t: number }> = ({ p }) => {
  const y = p.top ?? 1250, x0 = p.x0 ?? 40, x1 = p.x1 ?? 1040;
  return <g>
    <rect x={x0} y={y + 6} width={x1 - x0} height={2000} fill={soft} stroke={ink} strokeWidth={10} />
    <rect x={x0 - 10} y={y - 14} width={x1 - x0 + 20} height={40} rx={20} fill={ink} />
    <path d={`M${x0 + 30},${y + 60} H${x1 - 30}`} stroke={ink} strokeWidth={5} opacity={0.18} />
  </g>;
};

const Scrib: React.FC<{ x: number; y: number; w: number; dim?: boolean; k?: number; sw?: number }> = ({ x, y, w, dim, k = 1, sw = 7 }) =>
  <path d={`M${x},${y} q${w * 0.17},-9 ${w * 0.33},0 t${w * 0.33},0 t${w * 0.34},0`} fill="none" stroke={dim ? muted : ink} strokeWidth={sw} strokeLinecap="round"
    opacity={dim ? 0.6 : 0.85} strokeDasharray={w * 1.3} strokeDashoffset={w * 1.3 * (1 - k)} />;

/** Book with spine + page edges (L-050, no label). keys: [[t,"open"|"closed"]], flips: [t...] page turns (0.45s). */
export const Tome: React.FC<{ p: P; t: number }> = ({ p, t }) => {
  const keys: [number, string][] = p.keys ?? [[0, "closed"]];
  let st = keys[0][1], sq = 0;
  for (let i = 1; i < keys.length; i++) { const [at, v] = keys[i]; if (t < at) break; const u = (t - at) / 0.3; if (u >= 1) st = v; else { sq = Math.sin(u * Math.PI); if (u >= 0.5) st = v; } }
  const sy = 1 - sq * 0.55;
  if (st === "closed") return <g transform={`translate(0 ${p.closedDy ?? 0}) scale(${1 + sq * 0.08} ${sy})`}>
    {/* lying flat, seen from the front: top cover, page block with page-edge lines, rounded spine, bookmark */}
    <rect x={-176} y={-40} width={372} height={104} rx={18} fill={ink} transform="translate(10 10)" />
    <rect x={-160} y={-14} width={330} height={56} rx={6} fill={paper} stroke={ink} strokeWidth={6} />
    {[-2, 10, 22, 32].map((yy, i) => <path key={i} d={`M-150,${yy} H160`} stroke={muted} strokeWidth={3} opacity={0.8} />)}
    <rect x={-176} y={-44} width={368} height={36} rx={14} fill={ink} />
    <rect x={-176} y={40} width={368} height={20} rx={10} fill={ink} />
    <path d="M-150,-44 Q-206,8 -150,60 L-132,60 L-132,-44 Z" fill={ink} />
    <path d="M-178,-14 Q-186,8 -178,30" stroke={paper} strokeWidth={5} fill="none" opacity={0.5} />
    <path d="M118,42 V84 L130,74 L142,84 V42 Z" fill={accent} stroke={ink} strokeWidth={4} />
  </g>;
  const fl: number[] = p.flips ?? []; let fu = -1;
  for (const f of fl) if (t >= f && t < f + 0.45) fu = (t - f) / 0.45;
  const page = (side: 1 | -1, fill: string, dy = 0) => <path d={`M0,${-150 + dy} C${side * 60},${-172 + dy} ${side * 150},${-174 + dy} ${side * 212},${-152 + dy} L${side * 212},${120 + dy} C${side * 150},${100 + dy} ${side * 60},${100 + dy} 0,${124 + dy} Z`} fill={fill} stroke={ink} strokeWidth={7} strokeLinejoin="round" />;
  return <g transform={`scale(${1 + sq * 0.08} ${sy})`}>
    <rect x={-226} y={-132} width={452} height={282} rx={22} fill={ink} transform="translate(10 12)" />
    <rect x={-226} y={-132} width={452} height={282} rx={22} fill={ink} />
    {page(-1, soft, 16)}{page(1, soft, 16)}{page(-1, paper, 8)}{page(1, paper, 8)}
    {page(-1, paper)}{page(1, paper)}
    <rect x={-10} y={-150} width={20} height={274} fill={soft} opacity={0.9} />
    <path d="M0,-150 V124" stroke={ink} strokeWidth={6} />
    {[-96, -50, -4, 42].map((yy, i) => <Scrib key={"l" + i} x={-185} y={yy} w={150} dim={i % 2 === 1} sw={6} />)}
    {[-96, -50, -4, 42].map((yy, i) => <Scrib key={"r" + i} x={30} y={yy} w={150} dim={i % 2 === 0} sw={6} />)}
    {fu >= 0 && (() => { const c = Math.cos(fu * Math.PI); return <g transform={`translate(0 ${-14 * Math.sin(fu * Math.PI)}) scale(${c} 1)`}>{page(1, c > 0 ? paper : soft)}</g>; })()}
  </g>;
};

/** Self-test sheet, 10 ruled rows. rows: [[i, t]] = row i written (scribble draw-on 0.35s); ghost: {row, at} dotted suitcase outline; focus: {row, at} highlight. */
export const Paper: React.FC<{ p: P; t: number }> = ({ p, t }) => {
  const rows: [number, number][] = p.rows ?? [];
  const RY = (i: number) => -232 + i * 50;
  const g = p.ghost, f = p.focus;
  return <g transform={`rotate(${p.tilt ?? -2})`}>
    <rect x={-202} y={-282} width={420} height={580} rx={20} fill={ink} />
    <rect x={-212} y={-292} width={420} height={580} rx={20} fill={paper} stroke={ink} strokeWidth={10} />
    <rect x={-212} y={-292} width={420} height={36} rx={18} fill={soft} />
    {f && t >= f.at && <rect x={-196} y={RY(f.row) - 30} width={388} height={46} rx={14} fill={soft} opacity={eo(lin(t, f.at, 0.25))} />}
    {Array.from({ length: 10 }, (_, i) => <g key={i}>
      <path d={`M-150,${RY(i) + 14} H180`} stroke={soft} strokeWidth={4} />
      <circle cx={-176} cy={RY(i)} r={7} fill={muted} opacity={0.55} />
    </g>)}
    <g opacity={p.fadeAt != null ? 1 - lin(t, p.fadeAt, 0.6) : 1}>{rows.map(([i, at]) => t >= at ? <Scrib key={i} x={-148} y={RY(i)} w={i % 3 === 1 ? 250 : i % 3 === 2 ? 210 : 290} k={eo(lin(t, at, 0.35))} dim={!!p.dimRows} /> : null)}</g>
    {g && t >= g.at && <g transform={`translate(10 ${RY(g.row) - 4})`} opacity={0.75 * eo(lin(t, g.at, 0.3))}>
      <rect x={-46} y={-26} width={92} height={56} rx={10} fill="none" stroke={ink} strokeWidth={5} strokeDasharray="9 9" />
      <path d="M-16,-26 V-38 Q-16,-44 -10,-44 H10 Q16,-44 16,-38 V-26" fill="none" stroke={ink} strokeWidth={5} strokeDasharray="7 7" />
    </g>}
  </g>;
};

/** Flash card: face down (faint suitcase shadow) → flipAt: face up with clear suitcase + tick. shakeAt: small "stuck" shake. */
const Card: React.FC<{ p: P; t: number }> = ({ p, t }) => {
  const k = p.at != null ? pop(t, p.at) : 1; if (k <= 0) return null;
  let face = false, sx = 1;
  if (p.flipAt != null && t >= p.flipAt) { const u = lin(t, p.flipAt, 0.4); sx = Math.abs(Math.cos(u * Math.PI)); face = u >= 0.5; }
  const sh = p.shakeAt != null && t >= p.shakeAt && t < p.shakeAt + 0.5 ? 7 * Math.sin((t - p.shakeAt) * 48) * (1 - (t - p.shakeAt) / 0.5) : 0;
  const tickK = face ? pop(t, p.flipAt + 0.3) : 0;
  return <g transform={`translate(${sh} 0) scale(${k * Math.max(0.02, sx)} ${k})`}>
    <rect x={-146} y={-90} width={300} height={190} rx={22} fill={ink} transform="translate(10 12)" />
    {!face ? <g>
      <rect x={-150} y={-95} width={300} height={190} rx={22} fill={ink} stroke={ink} strokeWidth={8} />
      <rect x={-130} y={-75} width={260} height={150} rx={14} fill="none" stroke={paper} strokeWidth={4} opacity={0.35} />
      <Icon name="suitcase" size={120} fill={paper} opacity={p.shadow ?? 0.16} />
    </g> : <g>
      <rect x={-150} y={-95} width={300} height={190} rx={22} fill={paper} stroke={ink} strokeWidth={8} />
      <Icon name="suitcase" size={128} fill={ink} />
      {tickK > 0 && <g transform={`translate(122 -80) scale(${tickK})`}><Tick r={38} /></g>}
    </g>}
  </g>;
};

/** Generic icon with pop-in; droopAt (thumbs falls + greys), bob (pointing hand), rot. */
const IconProp: React.FC<{ p: P; t: number }> = ({ p, t }) => {
  const k = p.at != null ? pop(t, p.at) : 1; if (k <= 0) return null;
  const dr = p.droopAt != null ? eo(lin(t, p.droopAt, 0.6)) : 0;
  const bob = p.bob ? 14 * Math.sin((t - (p.at ?? 0)) * 6) : 0;
  const fill = dr > 0.5 ? muted : (p.fill === "accent" ? accent : p.fill === "paper" ? paper : ink);
  const size = p.size ?? 140;
  return <g transform={`translate(0 ${bob + dr * 40}) rotate(${(p.rot ?? 0) + dr * 150}) scale(${k})`}>
    {p.plate && <g><circle cx={8} cy={10} r={size * 0.66} fill={ink} /><circle r={size * 0.66} fill={paper} stroke={ink} strokeWidth={8} /></g>}
    {p.name === "tick" ? <Tick r={size / 2} /> : <Icon name={p.name} size={size} fill={fill} />}
  </g>;
};

/** Paper-stack bar: keys [[t, n]] sheets; height change = snap-settle spring. Base at y=0, grows up. */
const Stack: React.FC<{ p: P; t: number }> = ({ p, t }) => {
  const keys: [number, number][] = p.keys ?? [[0, 5]];
  let h = keys[0][1];
  for (let i = 1; i < keys.length; i++) { const [at, n] = keys[i]; if (t < at) break; h = h + (n - h) * springAt(t - at, 16, 7); }
  const n = Math.max(0, Math.round(h)); const W = p.w ?? 210; const step = 26;
  const grow = p.at != null ? eo(lin(t, p.at, 0.35)) : 1;
  return <g>
    <ellipse cx={0} cy={14} rx={W * 0.62} ry={14} fill={ink} opacity={0.18} />
    {Array.from({ length: Math.ceil(n * grow) }, (_, i) => { const r = (hash01(`${p.seed ?? 1}-${i}`) - 0.5) * 5; const dx = (hash01(`${p.seed ?? 1}x${i}`) - 0.5) * 14;
      return <g key={i} transform={`translate(${dx} ${-i * step}) rotate(${r})`}><rect x={-W / 2} y={-22} width={W} height={24} rx={7} fill={paper} stroke={ink} strokeWidth={6} /></g>; })}
  </g>;
};

/** 30 blank cards: pile (spillAt) → 3 stacks of 10 (splitAt, no bow) → stack 0 moves (pickAt → pickX/pickY) + tick (tickAt). */
const Deck: React.FC<{ p: P; t: number }> = ({ p, t }) => {
  const N = 30, sp = p.spillAt ?? 0, sa = p.splitAt ?? 99;
  const pk = p.pickAt != null ? eo(lin(t, p.pickAt, 0.45)) : 0;
  const cards = Array.from({ length: N }, (_, i) => {
    const px = (hash01(`dx${i}`) - 0.5) * 420, py = (hash01(`dy${i}`) - 0.5) * 120 - i * 2, pr = (hash01(`dr${i}`) - 0.5) * 70;
    const s = i % 3, lv = Math.floor(i / 3); const sx = (s - 1) * 250, sy = -lv * 10;
    const u = eo(lin(t, sa + lv * 0.03 + s * 0.04, 0.35));
    let x = px + (sx - px) * u, y = py + (sy - py) * u; const r = pr * (1 - u);
    if (s === 0) { x += (p.pickX ?? 0) * pk; y += (p.pickY ?? 0) * pk; }
    const drop = eo(lin(t, sp + i * 0.018, 0.3)); y -= (1 - drop) * 260;
    return { i, x, y, r, o: drop > 0 ? 1 : 0, s, lv };
  }).sort((a, b) => a.lv - b.lv);
  const tk = p.tickAt != null ? pop(t, p.tickAt) : 0;
  return <g>
    {cards.map((c) => c.o ? <g key={c.i} transform={`translate(${c.x} ${c.y}) rotate(${c.r})`}>
      <rect x={-62} y={-38} width={124} height={76} rx={12} fill={paper} stroke={ink} strokeWidth={5} />
      <path d="M-36,-6 H30" stroke={soft} strokeWidth={6} strokeLinecap="round" />
    </g> : null)}
    {tk > 0 && <g transform={`translate(${-250 + (p.pickX ?? 0) * pk + 70} ${(p.pickY ?? 0) * pk - 150}) scale(${tk})`}><Tick r={36} /></g>}
  </g>;
};

/** Growing pile of research papers (staggered drops). */
const Papers: React.FC<{ p: P; t: number }> = ({ p, t }) => {
  const n = p.n ?? 14, at = p.at ?? 0, stg = p.stagger ?? 0.09;
  return <g>
    <ellipse cx={0} cy={60} rx={230} ry={18} fill={ink} opacity={0.15} />
    {Array.from({ length: n }, (_, i) => { const u = eo(lin(t, at + i * stg, 0.28)); if (u <= 0) return null;
      const x = (hash01(`px${i}`) - 0.5) * 70, y = -i * 13 - (1 - u) * 300, r = (hash01(`pr${i}`) - 0.5) * 22;
      return <g key={i} transform={`translate(${x} ${y}) rotate(${r})`} opacity={u}>
        <rect x={-130} y={-46} width={260} height={92} rx={10} fill={paper} stroke={ink} strokeWidth={6} />
        <path d="M-100,-14 H80 M-100,12 H40" stroke={soft} strokeWidth={7} strokeLinecap="round" />
      </g>; })}
  </g>;
};

/** Two score bars (quiz class = ink, taller by a moderate amount; other = soft). riseAt; badgeAt = quiz sheet with tick above. */
const Bars: React.FC<{ p: P; t: number }> = ({ p, t }) => {
  const a = p.a ?? 330, b = p.b ?? 270, at = p.riseAt ?? 0;
  const ka = springAt(Math.max(0, t - at), 13, 7) * (t >= at ? 1 : 0), kb = springAt(Math.max(0, t - at - 0.12), 13, 7) * (t >= at + 0.12 ? 1 : 0);
  const base = p.base ?? 0.6; const ha = a * (base + (1 - base) * ka), hb = b * (base + (1 - base) * kb);
  const bk = p.badgeAt != null ? pop(t, p.badgeAt) : 0;
  return <g>
    <path d="M-300,0 H300" stroke={ink} strokeWidth={10} strokeLinecap="round" />
    <rect x={-235} y={-ha + 10} width={170} height={ha} rx={18} fill={ink} transform="translate(10 0)" opacity={0.25} />
    <rect x={-235} y={-ha} width={170} height={ha} rx={18} fill={ink} stroke={ink} strokeWidth={8} />
    <rect x={65} y={-hb} width={170} height={hb} rx={18} fill={soft} stroke={ink} strokeWidth={8} />
    {p.gapAt != null && t >= p.gapAt && (() => { const g = eo(lin(t, p.gapAt, 0.3)); return <g opacity={g}>
      <path d={`M-60,${-ha} H260`} stroke={ink} strokeWidth={5} strokeDasharray="14 10" />
      <path d={`M262,${-ha} V${-hb}`} stroke={accent} strokeWidth={12} strokeLinecap="round" />
    </g>; })()}
    {bk > 0 && <g transform={`translate(-150 ${-ha - 90}) scale(${bk}) rotate(-6)`}>
      <rect x={-52} y={-62} width={104} height={124} rx={12} fill={paper} stroke={ink} strokeWidth={6} />
      <path d="M-30,-28 H30 M-30,0 H30 M-30,28 H10" stroke={soft} strokeWidth={8} strokeLinecap="round" />
      <g transform="translate(46 -52)"><Tick r={26} /></g>
    </g>}
  </g>;
};

/** Two desk halves (b03): divider + two tabletops. */
const Halves: React.FC<{ p: P; t: number }> = ({ p }) => {
  const y = p.top ?? 1180;
  return <g>
    <rect x={40} y={200} width={500} height={1300} fill={soft} opacity={0.45} />
    <path d="M540,190 V1480" stroke={ink} strokeWidth={10} strokeDasharray="28 18" strokeLinecap="round" />
    {[[60, 520], [560, 1020]].map(([a, b], i) => <g key={i}>
      <rect x={a} y={y + 6} width={b - a} height={400} fill={soft} stroke={ink} strokeWidth={8} />
      <rect x={a - 6} y={y - 12} width={b - a + 12} height={34} rx={17} fill={ink} />
    </g>)}
  </g>;
};

export const V18_KINDS: Record<string, React.FC<{ p: P; t: number }>> = { ...C05_KINDS, window: Window, table: Table, tome: Tome, paper: Paper, card: Card, icon: IconProp, stack: Stack, deck: Deck, papers: Papers, bars: Bars, halves: Halves };
/** absolute-coordinate props (ignore x/y translate) */
export const V18_ABS = new Set(["window", "table", "halves", ...C05_ABS]);
