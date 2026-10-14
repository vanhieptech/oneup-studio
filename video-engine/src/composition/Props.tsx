import React from "react";
import { BRAND } from "./theme";
import { FONT_FAMILY } from "./fonts";

/** DL-056: comic props in brand style (ink on paper, round corners, 8px stroke, hard offset shadow, one accent).
 *  All times are scene seconds (build-final shifts them by the first line start). Drawn inside the camera group. */
export type PropCue = {
  kind: "laptop" | "phone" | "calendar" | "cloud" | "sign" | "vignette" | "words";
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
    {idx > 0 && fly < 1 && card(pages[idx - 1], "fly", `translate(${fly * 520} ${-fly * 160}) rotate(${fly * 38})`)}
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

export const Props: React.FC<{ props: PropCue[]; t: number; h: number }> = ({ props, t, h }) => <g>
  {props.map((p, i) => {
    if (p.until != null && t > p.until) return null;
    if (p.kind === "vignette") { const k = ease(t, p.at ?? 0, 0.6) * (p.dark ?? 0.55);
      return <g key={i}><defs><radialGradient id={`vg${i}`} cx="50%" cy="45%" r="70%"><stop offset="45%" stopColor={ink} stopOpacity={0} /><stop offset="100%" stopColor={ink} stopOpacity={k} /></radialGradient></defs><rect width={1080} height={h} fill={`url(#vg${i})`} /></g>; }
    const C = { laptop: Laptop, phone: Phone, calendar: Calendar, cloud: Cloud, sign: Sign, words: Words }[p.kind];
    return <g key={i} transform={`translate(${p.x ?? 540} ${p.y ?? 900}) rotate(${p.rot ?? 0}) scale(${p.s ?? 1})`}><C p={p} t={t} /></g>;
  })}
</g>;
