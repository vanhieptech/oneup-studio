import React from "react";
import { BRAND } from "./theme";
import { springAt, hash01 } from "../animation/timing";
import { Tome, Tick, Icon } from "./PropsV18";

/** clip-05 v4 props (FLUX visual-plan-v4.md @97a50af). L-050: meaning by objects, no words drawn inside images
 *  (all on-screen words are template overlays: tag / counter / caption). Scene seconds, design px (1080 wide). */
const { ink, paper, soft, accent, muted } = BRAND;
type P = Record<string, any>; // eslint-disable-line @typescript-eslint/no-explicit-any
const cl = (x: number, a = 0, b = 1) => Math.max(a, Math.min(b, x));
const lin = (t: number, at: number, d: number) => cl((t - at) / Math.max(1e-3, d));
const eo = (u: number) => 1 - Math.pow(1 - u, 3);
const pop = (t: number, at: number) => (t < at ? 0 : Math.min(1.12, springAt(t - at, 18, 9)));
const keyed = (keys: [number, number][], t: number, k = 16, d = 7) => { let v = keys[0][1]; for (let i = 1; i < keys.length; i++) { const [at, n] = keys[i]; if (t < at) break; v = v + (n - v) * springAt(t - at, k, d); } return v; };

/** DNA helix badge (no letters): two phase-opposed sine strands along a vertical axis + rungs between them (front strand drawn last). */
const helix = (ph: number, A = 20, H = 72, n = 28) => Array.from({ length: n + 1 }, (_, i) => { const y = -H / 2 + (i / n) * H; return `${i ? "L" : "M"}${(A * Math.sin((i / n) * Math.PI * 3 + ph)).toFixed(2)},${y.toFixed(2)}`; }).join(" ");
export const Dna: React.FC<{ s?: number; c?: string; bg?: string }> = ({ s = 1, c = ink, bg }) => <g transform={`scale(${s})`}>
  {bg && <circle r={46} fill={bg} stroke={ink} strokeWidth={6} />}
  {Array.from({ length: 8 }, (_, i) => { const f = (i + 0.5) / 8; const y = -36 + f * 72; const w = 20 * Math.sin(f * Math.PI * 3); return Math.abs(w) < 5 ? null : <path key={i} d={`M${-w},${y} L${w},${y}`} stroke={c} strokeWidth={3.5} strokeLinecap="round" opacity={0.6} />; })}
  <path d={helix(Math.PI)} fill="none" stroke={c} strokeWidth={5} strokeLinecap="round" strokeLinejoin="round" opacity={0.55} />
  <path d={helix(0)} fill="none" stroke={c} strokeWidth={6} strokeLinecap="round" strokeLinejoin="round" />
</g>;

/** The genetics textbook (same book in b01/b02/b05/b07). keys [[t,"closed"|"open"]]; closed = cover seen face-on (DNA icon, no text);
 *  open = V18 tome (flips) + DNA sticker on the spine. glowAt: soft accent halo. */
const BioBook: React.FC<{ p: P; t: number }> = ({ p, t }) => {
  const keys: [number, string][] = p.keys ?? [[0, "closed"]];
  let st = keys[0][1]; for (const [at, v] of keys) if (t >= at) st = v;
  const g = p.glowAt != null ? eo(lin(t, p.glowAt, 0.5)) * (0.75 + 0.25 * Math.sin((t - p.glowAt) * 5)) : 0;
  const halo = g > 0 ? <circle r={st === "open" ? 300 : 230} fill={accent} opacity={0.22 * g} /> : null;
  if (st === "open") return <g>{halo}<Tome p={{ keys: [[0, "open"]], flips: p.flips }} t={t} /><g transform="translate(0 -168)"><Dna s={0.7} bg={paper} /></g></g>;
  return <g transform={`rotate(${p.tilt ?? -4})`}>
    {halo}
    <rect x={-140} y={-180} width={290} height={370} rx={26} fill={ink} transform="translate(12 14)" />
    <rect x={-150} y={-190} width={290} height={370} rx={26} fill={soft} stroke={ink} strokeWidth={10} />
    <rect x={-150} y={-190} width={54} height={370} rx={22} fill={ink} />
    <rect x={128} y={-176} width={12} height={342} rx={6} fill={paper} stroke={ink} strokeWidth={4} />
    <g transform="translate(22 -30)"><Dna s={1.6} /></g>
    <path d="M-40,110 H90" stroke={ink} strokeWidth={8} strokeLinecap="round" opacity={0.25} />
  </g>;
};

/** Brand-new textbook pile: crisp flat spines, no creases, shine strokes (comment «sách mới tinh kh vết gấp»). dropAt: books drop in. */
const Textbooks: React.FC<{ p: P; t: number }> = ({ p, t }) => {
  const n = p.n ?? 6, at = p.dropAt ?? -9;
  return <g>
    <ellipse cx={0} cy={24} rx={300} ry={20} fill={ink} opacity={0.16} />
    {Array.from({ length: n }, (_, i) => {
      const u = eo(lin(t, at + i * 0.06, 0.25)); const w = 420 - (hash01(`tw${i}`) * 70), h = 62 + (i % 3) * 10;
      const y = -i * 70 - h / 2 - (1 - u) * 240, x = (hash01(`tx${i}`) - 0.5) * 40, r = (hash01(`tr${i}`) - 0.5) * 5;
      const fill = [paper, ink, soft, accent, paper, ink][i % 6]; const dark = fill === ink;
      return <g key={i} transform={`translate(${x} ${y}) rotate(${r})`} opacity={u > 0 ? 1 : 0}>
        <rect x={-w / 2 + 8} y={-h / 2 + 8} width={w} height={h} rx={12} fill={ink} />
        <rect x={-w / 2} y={-h / 2} width={w} height={h} rx={12} fill={fill} stroke={ink} strokeWidth={8} />
        <rect x={w / 2 - 34} y={-h / 2 + 8} width={22} height={h - 16} rx={4} fill={paper} stroke={ink} strokeWidth={4} />
        <path d={`M${-w / 2 + 34},${-h / 2 + 16} H${-w / 2 + 120}`} stroke={dark ? paper : ink} strokeWidth={6} strokeLinecap="round" opacity={0.35} />
      </g>; })}
  </g>;
};

/** Hourglass = three study hours. flow [start, dur]: sand top→bottom. breakAt: the big glass cracks, 3 small glasses fly to `to` [[x,y]×3]
 *  (prop-local px) and land (each its own small flow `smallFlow` [[start,dur]×3]). */
const Glass: React.FC<{ u: number; s: number; t: number; crack?: number }> = ({ u, s, t, crack = 0 }) => {
  const top = 1 - u, flowing = u > 0.001 && u < 0.999;
  return <g transform={`scale(${s})`}>
    <rect x={-96} y={-176} width={200} height={34} rx={14} fill={ink} transform="translate(8 10)" opacity={0.6} />
    <path d="M-74,-150 C-74,-60 -12,-30 -12,0 C-12,30 -74,60 -74,150 H74 C74,60 12,30 12,0 C12,-30 74,-60 74,-150 Z" fill={paper} stroke={ink} strokeWidth={9} strokeLinejoin="round" />
    {top > 0.01 && <path d={`M${-62 * Math.sqrt(top)},${-6 - 120 * top} Q0,${-12 - 132 * top} ${62 * Math.sqrt(top)},${-6 - 120 * top} L14,-6 L-14,-6 Z`} fill={accent} stroke={ink} strokeWidth={4} />}
    {u > 0.01 && <path d={`M-66,146 Q0,${146 - 150 * u} 66,146 Z`} fill={accent} stroke={ink} strokeWidth={4} />}
    {flowing && <path d={`M0,0 V${146 - 120 * u}`} stroke={accent} strokeWidth={6} strokeDasharray="10 8" strokeDashoffset={-t * 90} />}
    <rect x={-96} y={-172} width={192} height={30} rx={14} fill={ink} />
    <rect x={-96} y={142} width={192} height={30} rx={14} fill={ink} />
    {crack > 0 && <path d="M-40,-90 L-10,-60 L-30,-20 L10,10 L-6,60 M30,-110 L14,-70 L40,-40" stroke={ink} strokeWidth={6} fill="none" strokeLinecap="round" opacity={crack} />}
  </g>;
};
const Hourglass: React.FC<{ p: P; t: number }> = ({ p, t }) => {
  const [fs, fd] = p.flow ?? [0, 0]; const u = p.level ?? (fd > 0 ? lin(t, fs, fd) : 0); const s = p.size ?? 1;
  const k = p.at != null ? pop(t, p.at) : 1; if (k <= 0) return null;
  if (p.breakAt == null || t < p.breakAt) return <g transform={`scale(${k})`}><Glass u={u} s={s} t={t} /></g>;
  const dt = t - p.breakAt; const to: [number, number][] = p.to ?? [[-260, 0], [0, 0], [260, 0]]; const sf: [number, number][] = p.smallFlow ?? [];
  const big = 1 - lin(dt, 0.12, 0.2);
  return <g>
    {big > 0 && <g opacity={big}><Glass u={u} s={s * (1 + 0.06 * Math.sin(dt * 60) * big)} t={t} crack={lin(dt, 0, 0.12)} /></g>}
    {to.map(([x, y], i) => { const v = eo(lin(dt, 0.15 + i * 0.07, 0.45)); if (v <= 0) return null;
      const arc = -180 * Math.sin(v * Math.PI); const fl = sf[i] ? lin(t, sf[i][0], sf[i][1]) : 0;
      return <g key={i} transform={`translate(${x * v} ${y * v + arc}) rotate(${(1 - v) * (i - 1) * 40})`}><Glass u={fl} s={(p.smallSize ?? 0.42)} t={t} /></g>; })}
  </g>;
};

/** Exam sheet with a 4×4 Punnett square (dihybrid cross). Cells hold only coloured dots (no letters). fillAt: dots fill cell by cell. */
const Punnett: React.FC<{ p: P; t: number }> = ({ p, t }) => {
  const C = 64, x0 = -2 * C, y0 = -2 * C + 40;
  const cols = [ink, accent, muted, paper];
  return <g transform={`rotate(${p.tilt ?? -2})`}>
    <rect x={-206} y={-266} width={420} height={540} rx={20} fill={ink} />
    <rect x={-216} y={-276} width={420} height={540} rx={20} fill={paper} stroke={ink} strokeWidth={10} />
    <path d="M-170,-224 H120 M-170,-190 H60" stroke={soft} strokeWidth={10} strokeLinecap="round" />
    {[0, 1, 2, 3].map((i) => <g key={i}>
      <circle cx={x0 + C * i + C / 2} cy={y0 - 26} r={9} fill={i % 2 ? accent : ink} opacity={0.75} />
      <circle cx={x0 - 26} cy={y0 + C * i + C / 2} r={9} fill={i % 2 ? ink : accent} opacity={0.75} />
    </g>)}
    {[0, 1, 2, 3, 4].map((i) => <g key={`g${i}`}><path d={`M${x0 + C * i},${y0} V${y0 + 4 * C}`} stroke={ink} strokeWidth={i % 4 ? 4 : 7} /><path d={`M${x0},${y0 + C * i} H${x0 + 4 * C}`} stroke={ink} strokeWidth={i % 4 ? 4 : 7} /></g>)}
    {p.fillAt != null && Array.from({ length: 16 }, (_, k) => { const r = Math.floor(k / 4), c = k % 4; const v = pop(t, p.fillAt + (r + c) * 0.07 + (k % 2) * 0.03); if (v <= 0) return null;
      const a = cols[(r + 2 * c) % 4], b = cols[(2 * r + c + 1) % 4];
      return <g key={k} transform={`translate(${x0 + C * c + C / 2} ${y0 + C * r + C / 2}) scale(${v})`}>
        <circle cx={-12} cy={0} r={11} fill={a} stroke={ink} strokeWidth={4} /><circle cx={12} cy={0} r={11} fill={b} stroke={ink} strokeWidth={4} />
      </g>; })}
    {p.tickAt != null && pop(t, p.tickAt) > 0 && <g transform={`translate(160 -232) scale(${pop(t, p.tickAt)})`}><Tick r={34} /></g>}
  </g>;
};

/** "?" mark (punctuation, not a word) that pops above a head; wobble. */
const QMark: React.FC<{ p: P; t: number }> = ({ p, t }) => {
  const k = pop(t, p.at ?? 0); if (k <= 0) return null;
  return <g transform={`scale(${k}) rotate(${8 * Math.sin((t - (p.at ?? 0)) * 5)})`}>
    <circle r={58} fill={paper} stroke={ink} strokeWidth={8} />
    <text x={0} y={30} textAnchor="middle" fontFamily="Be Vietnam Pro" fontWeight={800} fontSize={88} fill={ink}>?</text>
  </g>;
};

/** Tear-off day calendar without numbers: ring binding, accent header, blank page. tears: [t] each page flies off (0.4s). holdUp: lifted page bob. */
const TearPad: React.FC<{ p: P; t: number }> = ({ p, t }) => {
  const tears: number[] = p.tears ?? []; const W = 260, H = 300;
  const page = (key: string | number, tr = "", op = 1) => <g key={key} transform={tr} opacity={op}>
    <rect x={-W / 2} y={-H / 2 + 40} width={W} height={H - 40} rx={14} fill={paper} stroke={ink} strokeWidth={7} />
    <path d={`M${-W / 2 + 50},${40} H${W / 2 - 50} M${-W / 2 + 70},${86} H${W / 2 - 70}`} stroke={soft} strokeWidth={10} strokeLinecap="round" />
  </g>;
  const done = tears.filter((x) => t >= x + 0.4).length; const left = Math.max(1, (p.n ?? 8) - done);
  const k = p.at != null ? pop(t, p.at) : 1; if (k <= 0) return null;
  const bob = p.holdUp ? 8 * Math.sin(t * 4) : 0;
  return <g transform={`translate(0 ${bob}) scale(${k})`}>
    <rect x={-W / 2 + 12} y={-H / 2 + 14} width={W} height={H + Math.min(5, left) * 5} rx={18} fill={ink} />
    {Array.from({ length: Math.min(5, left) }, (_, i) => <rect key={`e${i}`} x={-W / 2} y={-H / 2 + 46 + (H - 46) - 8 + i * 5} width={W} height={8} rx={4} fill={soft} stroke={ink} strokeWidth={3} />)}
    {page("base")}
    <rect x={-W / 2} y={-H / 2} width={W} height={64} rx={16} fill={accent} stroke={ink} strokeWidth={7} />
    {[-70, 0, 70].map((x) => <rect key={x} x={x - 8} y={-H / 2 - 18} width={16} height={40} rx={8} fill={ink} />)}
    {tears.map((x, i) => { if (t < x || t > x + 0.4) return null; const u = eo(lin(t, x, 0.4));
      return page(`t${i}`, `translate(${-u * 380 * (i % 2 ? -1 : 1)} ${-u * 260}) rotate(${u * (i % 2 ? 60 : -60)})`, 1 - u * 0.8); })}
  </g>;
};

/** Desk lamp (time marker «ngay» in b03, night desk in b01). on: light cone. */
const Lamp: React.FC<{ p: P; t: number }> = ({ p }) => <g transform={`scale(${p.flip ? -1 : 1} 1)`}>
  {p.on !== false && <path d="M60,-210 L-80,40 L250,40 L170,-200 Z" fill={accent} opacity={0.16} />}
  <ellipse cx={0} cy={30} rx={90} ry={18} fill={ink} />
  <path d="M0,24 L40,-130 L120,-200" fill="none" stroke={ink} strokeWidth={16} strokeLinecap="round" strokeLinejoin="round" />
  <circle cx={40} cy={-130} r={14} fill={paper} stroke={ink} strokeWidth={6} />
  <path d="M80,-250 L180,-170 L210,-210 L130,-280 Z" fill={accent} stroke={ink} strokeWidth={8} strokeLinejoin="round" />
</g>;

/** Wall clock without numerals (tick marks only); hands at `h` (hours, e.g. 2.9 ≈ nearly 3 o'clock); spin: fast-forward from `spin` [start, dur, hours]. */
const WallClock: React.FC<{ p: P; t: number }> = ({ p, t }) => {
  let h = p.h ?? 2.9; if (p.spin) h += p.spin[2] * eo(lin(t, p.spin[0], p.spin[1]));
  const ha = (h / 12) * 360, ma = (h % 1) * 360;
  return <g>
    <circle cx={8} cy={10} r={110} fill={ink} /><circle r={110} fill={paper} stroke={ink} strokeWidth={10} />
    {Array.from({ length: 12 }, (_, i) => { const a = (i / 12) * Math.PI * 2, b = i % 3 === 0; return <path key={i} d={`M${Math.sin(a) * (b ? 76 : 86)},${-Math.cos(a) * (b ? 76 : 86)} L${Math.sin(a) * 96},${-Math.cos(a) * 96}`} stroke={ink} strokeWidth={b ? 9 : 5} strokeLinecap="round" />; })}
    <g transform={`rotate(${ha})`}><path d="M0,8 V-52" stroke={ink} strokeWidth={12} strokeLinecap="round" /></g>
    <g transform={`rotate(${ma})`}><path d="M0,10 V-78" stroke={accent} strokeWidth={8} strokeLinecap="round" /></g>
    <circle r={10} fill={ink} />
  </g>;
};

/** TikTok-style vertical feed frame rebuilt from objects (L-084 trend, no original footage): right action rail (avatar, heart, comment,
 *  bookmark, share), share pulses at shareAt, playback bar fills. Absolute coords. Words/numbers are overlays (tag/counter). */
const TtFrame: React.FC<{ p: P; t: number }> = ({ p, t }) => {
  const x = p.railX ?? 958, y0 = p.railY ?? 600, gap = 138;
  const sh = p.shareAt != null ? pop(t, p.shareAt) : 1; const lk = p.likeAt != null ? pop(t, p.likeAt) : 0;
  const btn = (i: number, child: React.ReactNode, sc = 1) => <g key={i} transform={`translate(${x} ${y0 + i * gap}) scale(${sc})`}>{child}</g>;
  const heart = (f: string) => <path d="M0,34 C-60,-6 -52,-52 -22,-52 C-8,-52 0,-40 0,-30 C0,-40 8,-52 22,-52 C52,-52 60,-6 0,34 Z" fill={f} stroke={ink} strokeWidth={7} strokeLinejoin="round" />;
  return <g>
    <rect x={x - 70} y={y0 - 90} width={140} height={gap * 4 + 180} rx={70} fill={ink} opacity={0.08} />
    {btn(0, <g><circle r={50} fill={ink} stroke={paper} strokeWidth={6} /><circle cy={-8} r={18} fill={paper} /><path d="M-28,30 Q0,6 28,30" fill={paper} /><g transform={`translate(0 52) scale(${1 + 0.1 * Math.sin(t * 6)})`}><circle r={16} fill={accent} stroke={ink} strokeWidth={5} /><path d="M-7,0 H7 M0,-7 V7" stroke={paper} strokeWidth={5} strokeLinecap="round" /></g></g>)}
    {btn(1, <g>{heart(lk > 0.5 ? accent : paper)}</g>, 1 + 0.25 * Math.max(0, lk - 1 + 0.12))}
    {btn(2, <g><path d="M0,-46 C-40,-46 -54,-20 -54,-4 C-54,16 -40,34 -14,38 L-26,58 L12,38 C40,34 54,16 54,-4 C54,-20 40,-46 0,-46 Z" fill={paper} stroke={ink} strokeWidth={7} strokeLinejoin="round" />{[-20, 0, 20].map((d) => <circle key={d} cx={d} cy={-4} r={6} fill={ink} />)}</g>)}
    {btn(3, <path d="M-30,-46 H30 V48 L0,24 L-30,48 Z" fill={paper} stroke={ink} strokeWidth={7} strokeLinejoin="round" />)}
    {btn(4, <g transform={`scale(${sh})`}><circle r={58} fill={accent} opacity={0.25 * Math.max(0, Math.sin((t - (p.shareAt ?? 0)) * 6))} /><path d="M10,-44 L54,-2 L10,40 V18 C-26,18 -44,30 -56,50 C-52,6 -30,-16 10,-20 Z" fill={paper} stroke={ink} strokeWidth={7} strokeLinejoin="round" /></g>, 1.05)}
    <rect x={80} y={p.barY ?? 1452} width={920} height={10} rx={5} fill={soft} stroke={ink} strokeWidth={3} />
    <rect x={80} y={p.barY ?? 1452} width={920 * cl(0.18 + t / (p.barDur ?? 12))} height={10} rx={5} fill={accent} />
  </g>;
};

/** String (rope) drawn from A to B with a sag; knots at both ends. at: draw-on 0.6s. */
const Rope: React.FC<{ p: P; t: number }> = ({ p, t }) => {
  const [ax, ay] = p.a, [bx, by] = p.b; const sag = p.sag ?? 90; const u = eo(lin(t, p.at ?? 0, 0.6));
  const d = `M${ax},${ay} Q${(ax + bx) / 2},${(ay + by) / 2 + sag} ${bx},${by}`; const L = Math.hypot(bx - ax, by - ay) * 1.15;
  return <g>
    <path d={d} fill="none" stroke={ink} strokeWidth={14} strokeLinecap="round" strokeDasharray={L} strokeDashoffset={L * (1 - u)} />
    <path d={d} fill="none" stroke={accent} strokeWidth={6} strokeLinecap="round" strokeDasharray={`18 14`} opacity={u >= 1 ? 1 : 0} />
    <circle cx={ax} cy={ay} r={14} fill={ink} />{u >= 1 && <circle cx={bx} cy={by} r={14} fill={ink} />}
  </g>;
};

/** Plain exam sheet (scribbled rows, no text). */
const Exam: React.FC<{ p: P; t: number }> = ({ p }) => <g transform={`rotate(${p.tilt ?? 0})`}>
  <rect x={-122} y={-152} width={250} height={310} rx={16} fill={ink} />
  <rect x={-130} y={-162} width={250} height={310} rx={16} fill={paper} stroke={ink} strokeWidth={8} />
  <rect x={-130} y={-162} width={250} height={40} rx={16} fill={p.head === "accent" ? accent : soft} stroke={ink} strokeWidth={6} />
  {[0, 1, 2, 3, 4].map((i) => <path key={i} d={`M-96,${-82 + i * 44} H${i % 2 ? 40 : 84}`} stroke={soft} strokeWidth={10} strokeLinecap="round" />)}
  <g transform="translate(44 70) scale(0.55)">{[0, 1, 2, 3, 4].map((i) => <g key={i}><path d={`M${-80 + 40 * i},-80 V80`} stroke={ink} strokeWidth={5} /><path d={`M-80,${-80 + 40 * i} H80`} stroke={ink} strokeWidth={5} /></g>)}</g>
</g>;

/** b03: three groups, each compared only with the grey «read once» bar (Rawson & Kintsch 2005 constraint, FLUX 97a50af).
 *  keys [[t, grey, orange, ink]] bar heights (px); reference dashed line at the grey height (refAt); focus [[t, [i...]]] dims the others.
 *  No numbers on bars, nothing compares orange vs the third bar directly. Third group is ink (brand palette) = «2nd read one week apart». */
const Groups3: React.FC<{ p: P; t: number }> = ({ p, t }) => {
  const X = [-330, 0, 330]; const fills = [muted, accent, ink];
  const keys: [number, number, number, number][] = p.keys ?? [[0, 0, 0, 0]];
  const hs = [0, 1, 2].map((i) => keyed(keys.map((k) => [k[0], k[i + 1]] as [number, number]), t, 14, 7));
  const fk: [number, number[]][] = p.focus ?? []; let foc: number[] | null = null; for (const [at, f] of fk) if (t >= at) foc = f;
  const ref = p.refAt != null ? eo(lin(t, p.refAt, 0.3)) : 0;
  const head = (i: number) => <g transform={`translate(${X[i]} 120)`}>
    {[-46, 0, 46].map((dx, j) => <circle key={j} cx={dx} cy={j === 1 ? -14 : 0} r={34} fill={fills[i]} stroke={ink} strokeWidth={6} />)}
  </g>;
  const book = (x: number, y: number, s = 1) => <g transform={`translate(${x} ${y}) scale(${s})`}><rect x={-58} y={-20} width={116} height={40} rx={8} fill={soft} stroke={ink} strokeWidth={6} /><rect x={-58} y={-20} width={20} height={40} rx={6} fill={ink} /></g>;
  return <g>
    <path d="M-500,0 H500" stroke={ink} strokeWidth={10} strokeLinecap="round" />
    {[0, 1, 2].map((i) => { const o = foc && !foc.includes(i) ? 0.28 : 1; const h = Math.max(0, hs[i]);
      return <g key={i} opacity={o}>
        {h > 2 && <g><rect x={X[i] - 80 + 10} y={-h + 10} width={160} height={h} rx={18} fill={ink} opacity={0.25} /><rect x={X[i] - 80} y={-h} width={160} height={h} rx={18} fill={fills[i]} stroke={ink} strokeWidth={8} /></g>}
        {head(i)}
        <g transform={`translate(${X[i]} 230)`}>
          {i === 0 && book(0, 0)}
          {i === 1 && <g>{book(0, 0)}{book(4, -40)}</g>}
          {i === 2 && <g>{book(-96, 0, 0.8)}{Array.from({ length: 7 }, (_, j) => <rect key={j} x={-44 + j * 13} y={-24} width={10} height={44} rx={3} fill={j === 6 ? accent : paper} stroke={ink} strokeWidth={3} />)}{book(96, 0, 0.8)}</g>}
        </g>
      </g>; })}
    {ref > 0 && <path d={`M${-430},${-hs[0]} H${430 * (2 * ref - 1)}`} stroke={ink} strokeWidth={6} strokeDasharray="18 12" opacity={0.85} />}
  </g>;
};

/** b06: long calendar strip (day cells, no numbers); flag («remember until») dragged along flagKeys [[t, frac]]; accent review dots sit at
 *  fixed fractions of the flag distance → they spread out as the flag moves away. hand follows the flag while dragging. */
const Strip: React.FC<{ p: P; t: number }> = ({ p, t }) => {
  const W = p.w ?? 860, N = p.cells ?? 24, x0 = -W / 2, cw = W / N;
  const fk: [number, number][] = p.flagKeys ?? [[0, 0.35]];
  let f = fk[0][1]; for (let i = 1; i < fk.length; i++) { const [at, v] = fk[i]; if (t < at) break; f = fk[i - 1][1] + (v - fk[i - 1][1]) * eo(lin(t, at, 0.9)); }
  const fr: number[] = p.dots ?? [0, 0.16, 0.42, 0.78];
  const fx = x0 + W * f; const dragging = fk.some(([at], i) => i > 0 && t >= at && t < at + 0.9);
  return <g>
    <rect x={x0 - 14} y={-70} width={W + 28} height={140} rx={24} fill={ink} transform="translate(10 12)" />
    <rect x={x0 - 14} y={-70} width={W + 28} height={140} rx={24} fill={paper} stroke={ink} strokeWidth={8} />
    {Array.from({ length: N + 1 }, (_, i) => <path key={i} d={`M${x0 + i * cw},-54 V54`} stroke={soft} strokeWidth={4} />)}
    <rect x={x0 - 14} y={-70} width={W + 28} height={28} rx={14} fill={soft} />
    {fr.map((q, i) => { const k = p.dotsAt != null ? pop(t, p.dotsAt + i * 0.1) : 1; return k > 0 ? <g key={i} transform={`translate(${x0 + 10 + (fx - x0 - 10) * q} 8) scale(${k})`}><circle r={24} fill={accent} stroke={ink} strokeWidth={6} /></g> : null; })}
    <g transform={`translate(${fx} 0)`}>
      <path d="M0,60 V-170" stroke={ink} strokeWidth={10} strokeLinecap="round" />
      <path d="M0,-170 L96,-140 L0,-110 Z" fill={accent} stroke={ink} strokeWidth={7} strokeLinejoin="round" />
      {(dragging || p.hand) && <g transform="translate(20 120) rotate(-10)"><Icon name="hand" size={110} fill={ink} /></g>}
    </g>
  </g>;
};

/** Red-pen ring around one spot (clip-04 callback: circle the mistake). at: draw-on 0.35s. */
const Ring: React.FC<{ p: P; t: number }> = ({ p, t }) => {
  const u = eo(lin(t, p.at ?? 0, 0.35)); if (u <= 0) return null; const rx = p.rx ?? 120, ry = p.ry ?? 44; const L = 2 * Math.PI * Math.max(rx, ry) * 1.1;
  return <path d={`M${rx},0 A${rx},${ry} 0 1,1 ${rx - 6},-10`} fill="none" stroke={accent} strokeWidth={12} strokeLinecap="round" strokeDasharray={L} strokeDashoffset={L * (1 - u)} transform={`rotate(${p.rot ?? -6})`} />;
};

/** Moon badge (one night per small hourglass). */
const MoonDot: React.FC<{ p: P; t: number }> = ({ p, t }) => {
  const k = p.at != null ? pop(t, p.at) : 1; if (k <= 0) return null;
  return <g transform={`scale(${k})`}><circle r={46} fill={ink} /><g transform="translate(-2 0)"><Icon name="moon" size={56} fill={paper} /></g></g>;
};

export const C05_KINDS: Record<string, React.FC<{ p: P; t: number }>> = {
  biobook: BioBook, textbooks: Textbooks, hourglass: Hourglass, punnett: Punnett, qmark: QMark, tearpad: TearPad, lamp: Lamp, wallclock: WallClock,
  ttframe: TtFrame, rope: Rope, exam: Exam, groups3: Groups3, strip: Strip, ring: Ring, moondot: MoonDot,
};
export const C05_ABS = new Set(["ttframe", "rope"]);
