import React from "react";
import { BRAND } from "./theme";
import { FONT_FAMILY } from "./fonts";

/** DL-056: comic props in brand style (ink on paper, round corners, 8px stroke, hard offset shadow, one accent).
 *  All times are scene seconds (build-final shifts them by the first line start). Drawn inside the camera group. */
export type PropCue = {
  kind: "laptop" | "phone" | "calendar" | "cloud" | "sign" | "vignette" | "words" | "pile" | "bundles" | "bundle" | "clock" | "dusty";
  count?: number;
  x?: number; y?: number; s?: number; rot?: number;
  text?: string; sub?: string; stamp?: string; at?: number; until?: number;
  pages?: string[]; tearAt?: number[]; words?: string[]; dropAt?: number[]; dark?: number;
};
const { ink, paper, soft, accent, muted } = BRAND;
const pop = (t: number, at = 0, d = 0.18) => { const k = Math.max(0, Math.min(1, (t - at) / d)); return k <= 0 ? 0 : k >= 1 ? 1 : 1 + 0.25 * Math.sin(k * Math.PI) * (1 - k) + (k - 1) * 0; };
const ease = (t: number, at: number, d: number) => Math.max(0, Math.min(1, (t - at) / d));
const T: React.FC<{ x: number; y: number; size: number; fill?: string; w?: number; anchor?: "start" | "middle" | "end"; children: React.ReactNode }> = ({ x, y, size, fill = ink, w = 700, anchor = "middle", children }) =>
  <text x={x} y={y} fontSize={size} fontWeight={w} fill={fill} textAnchor={anchor} fontFamily={FONT_FAMILY}>{children}</text>;

const Stamp: React.FC<{ x: number; y: number; text: string; t: number; at: number; rot?: number }> = ({ x, y, text, t, at, rot = -12 }) => {
  if (t < at) return null;
  const k = ease(t, at, 0.14); const sc = 1.8 - 0.8 * k; const w = text.length * 34 + 60;
  return <g transform={`translate(${x} ${y}) rotate(${rot}) scale(${sc})`} opacity={k}>
    <rect x={-w / 2} y={-46} width={w} height={92} rx={18} fill="none" stroke={accent} strokeWidth={9} />
    <T x={0} y={18} size={52} fill={accent} w={800}>{text}</T>
  </g>;
};

const Laptop: React.FC<{ p: PropCue; t: number }> = ({ p, t }) => {
  const blink = Math.floor(t * 2) % 2 === 0;
  return <g>
    <path d="M-300,-360 h600 a26,26 0 0 1 26,26 v330 h-652 v-330 a26,26 0 0 1 26,-26 Z" fill={ink} />
    <rect x={-270} y={-332} width={540} height={300} rx={14} fill={paper} />
    <rect x={-270} y={-332} width={540} height={46} rx={14} fill={soft} />
    {[0, 1, 2].map((i) => <circle key={i} cx={-240 + i * 26} cy={-309} r={8} fill={i === 0 ? accent : muted} />)}
    <T x={-246} y={-236} size={34} anchor="start" fill={muted} w={600}>{"// TODO"}</T>
    <T x={-246} y={-178} size={50} anchor="start" w={800}>{p.text ?? "Omi feature"}</T>
    <T x={-246} y={-122} size={30} anchor="start" fill={muted} w={500}>{p.sub ?? "0 dòng code"}{blink ? " ▌" : ""}</T>
    <path d="M-370,0 h740 l-50,46 h-640 Z" fill={ink} /><rect x={-80} y={4} width={160} height={14} rx={7} fill={soft} />
    {p.stamp && <Stamp x={120} y={-120} text={p.stamp} t={t} at={p.at ?? 0} />}
  </g>;
};

const Phone: React.FC<{ p: PropCue; t: number }> = ({ p, t }) => {
  const on = t >= (p.at ?? 0); const k = ease(t, p.at ?? 0, 0.2);
  return <g>
    {on && <circle cx={0} cy={-10} r={170 * k} fill={accent} opacity={0.18 * k} />}
    <rect x={-95} y={-180} width={190} height={340} rx={34} fill={ink} />
    <rect x={-80} y={-160} width={160} height={300} rx={22} fill={on ? paper : "#2a2a2a"} />
    {on && <g opacity={k}>
      {[0, 1, 2].map((i) => <rect key={i} x={-62} y={-130 + i * 92} width={124} height={78} rx={12} fill={i === 1 ? accent : soft} />)}
      <path d="M-14,-12 l30,18 l-30,18 Z" fill={paper} />
      <T x={0} y={175 + 46} size={36} w={800}>{p.text ?? "TikTok"}</T>
    </g>}
  </g>;
};

const Calendar: React.FC<{ p: PropCue; t: number }> = ({ p, t }) => {
  const pages = p.pages ?? ["T2", "T3", "T4"]; const tear = p.tearAt ?? [];
  const idx = tear.filter((a) => t >= a).length; const cur = Math.min(idx, pages.length - 1);
  const last = idx > 0 ? tear[idx - 1] : -9; const fly = ease(t, last, 0.35);
  const card = (label: string, key: string, extra?: string) => <g key={key} transform={extra}>
    <rect x={-210} y={-230} width={420} height={440} rx={34} fill={paper} stroke={ink} strokeWidth={10} />
    <path d="M-210,-196 a34,34 0 0 1 34,-34 h352 a34,34 0 0 1 34,34 v70 h-420 Z" fill={accent} />
    {[-110, 110].map((cx) => <rect key={cx} x={cx - 14} y={-262} width={28} height={64} rx={14} fill={ink} />)}
    <T x={0} y={-150} size={44} fill={paper} w={800}>{"DEADLINE"}</T>
    <T x={0} y={60} size={label.length > 7 ? 64 : label.length > 4 ? 84 : 120} w={800}>{label}</T>
    <T x={0} y={150} size={34} fill={muted} w={600}>{"Omi feature"}</T>
  </g>;
  return <g>
    <rect x={-202} y={-218} width={420} height={440} rx={34} fill={ink} />
    {card(pages[cur], "cur")}
    {idx > 0 && fly < 1 && card(pages[idx - 1], "fly", `translate(${fly * 150} ${-fly * 260}) rotate(${fly * 22}) scale(${1 - 0.25 * fly})`)}
    {idx > 0 && <g transform="translate(150 150) rotate(-14)"><rect x={-110} y={-40} width={220} height={80} rx={16} fill={ink} />
      <T x={0} y={16} size={44} fill={paper} w={800}>{`HOÃN x${idx}`}</T></g>}
  </g>;
};

const Cloud: React.FC<{ p: PropCue; t: number }> = ({ p, t }) => {
  const words = p.words ?? ["LƯỜI"]; const drop = p.dropAt ?? words.map((_, i) => i * 0.4);
  const k = ease(t, p.at ?? 0, 0.3); const wob = 6 * Math.sin(t * 3);
  return <g opacity={k} transform={`translate(0 ${wob})`}>
    <path d="M-230,40 a80,80 0 0 1 20,-150 a110,110 0 0 1 200,-50 a95,95 0 0 1 170,40 a80,80 0 0 1 60,160 Z" fill={ink} />
    {[-120, 0, 120].map((x, i) => <path key={i} d={`M${x},70 l-14,46 M${x + 30},70 l-14,46`} stroke={ink} strokeWidth={8} strokeLinecap="round" opacity={0.5 + 0.5 * Math.sin(t * 9 + i)} />)}
    {words.map((w, i) => { const d = drop[i] ?? 0; if (t < d) return null; const f = ease(t, d, 0.22); const y = -200 + f * (250 + i * 104);
      const sq = f >= 1 ? 1 + 0.18 * Math.max(0, 1 - (t - d - 0.22) / 0.15) : 1;
      return <g key={w} transform={`translate(0 ${y}) scale(${sq} ${2 - sq})`}>
        <rect x={-w.length * 26 - 34} y={-50} width={w.length * 52 + 68} height={86} rx={20} fill={i === words.length - 1 ? accent : paper} stroke={ink} strokeWidth={8} />
        <T x={0} y={14} size={52} w={800} fill={i === words.length - 1 ? paper : ink}>{w}</T></g>; })}
  </g>;
};

const Sign: React.FC<{ p: PropCue; t: number }> = ({ p, t }) => {
  const s = pop(t, p.at ?? 0, 0.2); if (s <= 0) return null; const txt = p.text ?? "?"; const w = Math.max(320, txt.length * 40 + 80);
  return <g transform={`scale(${s})`}>
    <rect x={-12} y={20} width={24} height={240} rx={10} fill={ink} />
    <rect x={-w / 2 + 10} y={-90} width={w} height={130} rx={28} fill={ink} />
    <rect x={-w / 2} y={-100} width={w} height={130} rx={28} fill={paper} stroke={ink} strokeWidth={10} />
    <T x={0} y={-12} size={58} w={800}>{txt}</T>
  </g>;
};

const Words: React.FC<{ p: PropCue; t: number }> = ({ p, t }) => {
  const words = p.words ?? []; const at = p.dropAt ?? words.map((_, i) => (p.at ?? 0) + i * 0.3);
  return <g>{words.map((w, i) => { if (t < at[i]) return null; const k = ease(t, at[i], 0.12); const sc = 1.6 - 0.6 * k; const jit = 4 * Math.sin(t * 40 + i);
    return <g key={i} transform={`translate(${jit} ${i * 120}) scale(${sc}) rotate(${i % 2 ? 4 : -4})`} opacity={k}>
      <rect x={-w.length * 30 - 30} y={-58} width={w.length * 60 + 60} height={100} rx={22} fill={i === words.length - 1 ? accent : ink} />
      <T x={0} y={12} size={64} w={800} fill={paper}>{w}</T></g>; })}</g>;
};


/** Meaning-by-objects props (Hiệp 18/10: draw scenes/objects/actions, never words).
 *  Same finished grammar as old props: flat fill, ink 9-10px, hard offset shadow, one accent. Local: centre (0,0), +y down. */
const Pile: React.FC<{ p: PropCue; t: number }> = () => (
  <g>
    <ellipse cx={0} cy={392} rx={330} ry={24} fill={ink} opacity={0.12} />
    {/* tall back mound */}
    <path d="M-290,390 C-310,150 -250,60 -175,35 C-150,-95 -55,-150 15,-105 C85,-185 235,-150 260,-35 C315,25 305,230 285,390 Z" fill={soft} stroke={ink} strokeWidth={10} strokeLinejoin="round" />
    {/* bottom box */}
    <rect x={-270} y={215} width={540} height={185} rx={22} fill={paper} stroke={ink} strokeWidth={10} />
    <path d="M-270,215 L-185,145 L260,145 L270,215Z" fill={soft} stroke={ink} strokeWidth={8} strokeLinejoin="round" />
    {/* books leaning left, mid */}
    <g transform="rotate(-8 -185 105)">
      <rect x={-300} y={78} width={230} height={50} rx={14} fill={ink} stroke={ink} strokeWidth={8} />
      <rect x={-288} y={28} width={205} height={50} rx={14} fill={paper} stroke={ink} strokeWidth={8} />
    </g>
    {/* small tilted box right, mid */}
    <g transform="rotate(6 165 55)">
      <rect x={55} y={-5} width={220} height={125} rx={18} fill={paper} stroke={ink} strokeWidth={9} />
      <path d="M55,35 H275" stroke={soft} strokeWidth={14} />
    </g>
    {/* clothes mounds */}
    <ellipse cx={-95} cy={155} rx={165} ry={88} fill={paper} stroke={ink} strokeWidth={10} />
    <ellipse cx={125} cy={165} rx={150} ry={80} fill={soft} stroke={ink} strokeWidth={9} />
    <path d="M-215,130 Q-130,82 -35,118 M35,140 Q115,102 205,132" fill="none" stroke={ink} strokeWidth={7} strokeLinecap="round" opacity={0.45} />
    {/* one leaning paper sheet, right */}
    <g transform="rotate(14 255 250)">
      <rect x={185} y={165} width={135} height={175} rx={10} fill={paper} stroke={ink} strokeWidth={8} />
      <path d="M208,205 H295 M208,242 H295 M208,279 H272" stroke={muted} strokeWidth={7} strokeLinecap="round" />
    </g>
    {/* accent T-shirt draped over the peak (overlaps mound, not floating) */}
    <path d="M-82,-302 L-30,-335 Q0,-318 30,-335 L82,-302 L118,-238 L66,-216 L66,-118 L-66,-118 L-66,-216 L-118,-238Z" fill={accent} stroke={ink} strokeWidth={10} strokeLinejoin="round" />
    <path d="M-30,-335 Q0,-318 30,-335 Q24,-296 0,-294 Q-24,-296 -30,-335Z" fill={paper} stroke={ink} strokeWidth={7} />
    <path d="M-66,-150 Q0,-132 66,-150" fill="none" stroke={ink} strokeWidth={6} opacity={0.4} />
    {/* crumpled ball + shoe pair at base front */}
    <circle cx={-195} cy={335} r={38} fill={paper} stroke={ink} strokeWidth={8} />
    <path d="M-216,318 L-176,352 M-176,318 L-216,352" stroke={muted} strokeWidth={6} strokeLinecap="round" />
    <path d="M92,352 L168,352 Q196,352 196,330 Q196,312 172,306 L128,292 Q104,308 92,330Z" fill={ink} stroke={paper} strokeWidth={5} strokeLinejoin="round" />
  </g>
);

const BundleBox: React.FC<{ x: number; accentTie?: boolean }> = ({ x, accentTie }) => (
  <g transform={`translate(${x} 0)`}>
    <rect x={-80} y={-58} width={180} height={148} rx={18} fill={ink} />
    <rect x={-90} y={-68} width={180} height={148} rx={18} fill={paper} stroke={ink} strokeWidth={10} />
    <path d="M-90,-28 H90" stroke={ink} strokeWidth={7} />
    <path d="M0,-68 V80" stroke={soft} strokeWidth={15} />
    <path d="M-28,-86 Q-52,-108 -68,-88 Q-54,-68 -26,-74 M28,-86 Q52,-108 68,-88 Q54,-68 26,-74" fill={accentTie ? accent : paper} stroke={ink} strokeWidth={7} strokeLinejoin="round" />
    <circle cx={0} cy={-78} r={10} fill={ink} />
  </g>
);
const Bundles: React.FC<{ p: PropCue; t: number }> = ({ p }) => {
  const n = p.count ?? 3; const xs = n === 1 ? [0] : n === 2 ? [-150, 150] : [-265, 0, 265];
  return <g><ellipse cx={0} cy={102} rx={n === 1 ? 150 : 430} ry={20} fill={ink} opacity={0.12} />{xs.map((x, i) => <BundleBox key={x} x={x} accentTie={i === 1} />)}</g>;
};
const Bundle: React.FC<{ p: PropCue; t: number }> = () => <g><BundleBox x={0} accentTie /></g>;

const Clock: React.FC<{ p: PropCue; t: number }> = () => (
  <g>
    <circle cx={10} cy={12} r={172} fill={ink} />
    <circle cx={0} cy={0} r={172} fill={paper} stroke={ink} strokeWidth={12} />
    {Array.from({ length: 12 }, (_, i) => { const a = (i / 12) * Math.PI * 2, big = i % 3 === 0; const r1 = big ? 128 : 140, r2 = 152; return <path key={i} d={`M${Math.cos(a) * r1},${Math.sin(a) * r1} L${Math.cos(a) * r2},${Math.sin(a) * r2}`} stroke={ink} strokeWidth={big ? 11 : 7} strokeLinecap="round" />; })}
    <path d="M0,0 L0,-92" stroke={ink} strokeWidth={13} strokeLinecap="round" />
    <path d="M0,0 L72,42" stroke={accent} strokeWidth={13} strokeLinecap="round" />
    <circle cx={0} cy={0} r={17} fill={ink} stroke={paper} strokeWidth={5} />
  </g>
);

const Dusty: React.FC<{ p: PropCue; t: number }> = () => (
  <g>
    <ellipse cx={0} cy={330} rx={400} ry={24} fill={ink} opacity={0.12} />
    {/* thick stack of blank calendar pages, left */}
    <g transform="rotate(-3 -190 60)">
      {Array.from({ length: 7 }, (_, i) => <rect key={i} x={-330 + i * 5} y={-150 + i * 13} width={300} height={360} rx={22} fill={i % 2 ? soft : paper} stroke={ink} strokeWidth={7} />)}
      <rect x={-302} y={-178} width={300} height={360} rx={22} fill={paper} stroke={ink} strokeWidth={10} />
      <path d="M-302,-128 a22,22 0 0 1 22,-22 h256 a22,22 0 0 1 22,22 v48 h-300Z" fill={accent} stroke={ink} strokeWidth={8} />
      {[-240, -90].map((cx) => <rect key={cx} x={cx - 13} y={-205} width={26} height={58} rx={13} fill={ink} />)}
      <path d="M-260,20 H-45 M-260,80 H-45 M-260,140 H-110" stroke={soft} strokeWidth={14} strokeLinecap="round" />
    </g>
    {/* untouched dumbbell gathering dust, front right */}
    <g transform="translate(215 255)">
      <rect x={-185} y={-16} width={370} height={32} rx={16} fill={ink} />
      <rect x={-215} y={-105} width={62} height={210} rx={20} fill={ink} stroke={paper} strokeWidth={6} />
      <rect x={-155} y={-82} width={44} height={164} rx={16} fill={soft} stroke={ink} strokeWidth={7} />
      <rect x={153} y={-105} width={62} height={210} rx={20} fill={ink} stroke={paper} strokeWidth={6} />
      <rect x={111} y={-82} width={44} height={164} rx={16} fill={soft} stroke={ink} strokeWidth={7} />
      <path d="M-228,-102 Q-184,-128 -140,-104 L-140,-88 Q-184,-100 -228,-86Z" fill={soft} stroke={ink} strokeWidth={6} strokeLinejoin="round" />
      <path d="M140,-104 Q184,-128 228,-102 L228,-86 Q184,-100 140,-88Z" fill={soft} stroke={ink} strokeWidth={6} strokeLinejoin="round" />
      <path d="M-90,-24 Q0,-38 90,-24 L90,-12 Q0,-20 -90,-12Z" fill={soft} opacity={0.9} />
    </g>
    {/* cobweb top-right corner + dust motes */}
    <g stroke={muted} strokeWidth={6} strokeLinecap="round" opacity={0.9}>
      <path d="M400,-330 L400,-190 M400,-330 L270,-330 M400,-330 L292,-222" />
      <path d="M400,-262 Q350,-268 322,-300 M400,-215 Q362,-218 338,-245 M348,-330 Q352,-285 322,-262" fill="none" />
    </g>
    {[-40, 90, 300].map((x, i) => <circle key={x} cx={x} cy={-190 + i * 55} r={8} fill={muted} opacity={0.55} />)}
    <ellipse cx={130} cy={318} rx={230} ry={18} fill={soft} stroke={ink} strokeWidth={6} opacity={0.9} />
  </g>
);

export const Props: React.FC<{ props: PropCue[]; t: number; h: number }> = ({ props, t, h }) => <g>
  {props.map((p, i) => {
    if (p.until != null && t > p.until) return null;
    if (p.kind === "vignette") { const k = ease(t, p.at ?? 0, 0.6) * (p.dark ?? 0.55);
      return <g key={i}><defs><radialGradient id={`vg${i}`} cx="50%" cy="45%" r="70%"><stop offset="45%" stopColor={ink} stopOpacity={0} /><stop offset="100%" stopColor={ink} stopOpacity={k} /></radialGradient></defs><rect width={1080} height={h} fill={`url(#vg${i})`} /></g>; }
    const C = { laptop: Laptop, phone: Phone, calendar: Calendar, cloud: Cloud, sign: Sign, words: Words, pile: Pile, bundles: Bundles, bundle: Bundle, clock: Clock, dusty: Dusty }[p.kind];
    return <g key={i} transform={`translate(${p.x ?? 540} ${p.y ?? 900}) rotate(${p.rot ?? 0}) scale(${p.s ?? 1})`}><C p={p} t={t} /></g>;
  })}
</g>;
