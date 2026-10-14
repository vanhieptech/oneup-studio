import React from "react";
import { AbsoluteFill, Img, staticFile } from "remotion";
import { defaultRegistry } from "../characters/registry";
import { CharacterRenderer } from "../characters/CharacterRenderer";
import { getCharacterState } from "../animation/controller";
import { CharacterCueSchema } from "../validation/schema";
import { ensureFonts, FONT_FAMILY } from "./fonts";

/** OneUp cover template (DL-046, draft): 1080×1920 still, fixed slots, brand tokens only.
 *  Profile-grid safe zone (TikTok 3:4 centre crop): y 240–1680 → every slot lives inside y 300–1620. */
export type CoverProps = {
  direction: "a" | "b" | "c"; theme: "light" | "dark"; series: string; ep: number;
  hero: string[]; accent: number; strike?: number; sub?: string;
  expression: string; action?: string; tilt?: number; emote?: "!" | "?" | "zzz" | "✓"; showSafe?: boolean;
};
const T = {
  light: { bg: "#F7F7F5", ink: "#111111", surface: "#FFFFFF", muted: "#6B6B6B", soft: "#F0F0EE" },
  dark: { bg: "#111111", ink: "#F7F7F5", surface: "#1C1C1A", muted: "#A3A3A0", soft: "#242422" },
};
const Chibi: React.FC<{ x: number; groundY: number; scale: number; expression: string; action?: string; tilt?: number; uid: string }> = ({ x, groundY, scale, expression, action, tilt = 0, uid }) => {
  const prof = defaultRegistry.get("hiep")!;
  const cue = CharacterCueSchema.parse({ characterId: "hiep", x: 0, expression, action: action ?? "reacting" });
  const st = { ...getCharacterState({ cue, profile: prof, frame: 12, fps: 30, sceneDuration: 99, dialogue: [] }), rotation: tilt };
  return <g transform={`translate(${x - st.x} 0)`}><CharacterRenderer state={st} profile={prof} width={1} groundY={groundY} scale={scale} uid={uid} /></g>;
};
const Emote: React.FC<{ kind?: string; x: number; y: number; c: string }> = ({ kind, x, y, c }) => !kind ? null : (
  <g transform={`translate(${x} ${y})`} fill={c} stroke={c}>
    {kind === "!" && <><rect x={-14} y={-120} width={28} height={86} rx={14} transform="rotate(12)" /><circle cx={10} cy={-8} r={16} /><rect x={36} y={-104} width={22} height={66} rx={11} transform="rotate(24)" /><circle cx={52} cy={-12} r={12} /></>}
    {kind === "zzz" && <text fontFamily={FONT_FAMILY} fontWeight={700} fontSize={70} stroke="none">z<tspan dy={-40} fontSize={54}>z</tspan></text>}
  </g>
);
const Series: React.FC<{ p: CoverProps; c: typeof T.light; x: number; y: number }> = ({ p, c, x, y }) => (
  <div style={{ position: "absolute", left: x, top: y, display: "flex", alignItems: "center", gap: 16 }}>
    <div style={{ background: c.ink, color: c.bg, fontSize: 40, fontWeight: 700, borderRadius: 18, padding: "6px 22px 10px" }}>#{String(p.ep).padStart(2, "0")}</div>
    <div style={{ color: c.ink, fontSize: 30, fontWeight: 600, letterSpacing: "0.14em", textTransform: "uppercase" }}>{p.series}</div>
  </div>
);
const Logo: React.FC<{ c: typeof T.light; dark: boolean; x: number; y: number }> = ({ dark, x, y, c }) => (
  <div style={{ position: "absolute", left: x, top: y, display: "flex", alignItems: "center", gap: 12 }}>
    <Img src={staticFile("brand/pair-plus.svg")} style={{ width: 56, height: 56, filter: dark ? "invert(0.97)" : "none" }} />
    <div style={{ fontSize: 36, fontWeight: 700, letterSpacing: "-0.03em", color: c.ink }}>OneUp<span style={{ opacity: 0.35 }}>.</span></div>
  </div>
);
const fit = (w: string, base: number, maxW = 900) => Math.min(base, Math.floor(maxW / (Math.max(1, w.length) * 0.66)));
const Word: React.FC<{ w: string; i: number; p: CoverProps; c: typeof T.light; size: number }> = ({ w, i, p, c, size: base }) => {
  const size = fit(w, base, i === p.accent ? 840 : 920);
  const acc = i === p.accent, st = i === p.strike;
  return (
    <span style={{ position: "relative", display: "inline-block", fontSize: size, fontWeight: 700, letterSpacing: "-0.035em", lineHeight: 1.0,
      color: acc ? c.bg : st ? c.muted : c.ink, background: acc ? c.ink : "transparent", borderRadius: acc ? 36 : 0, padding: acc ? `${Math.round(size*0.12)}px 30px ${Math.round(size*0.1)}px` : 0 }}>
      {w}{st && <span style={{ position: "absolute", left: -10, right: -10, top: "52%", height: size * 0.11, background: c.ink, borderRadius: 20, transform: "rotate(-4deg)" }} />}
    </span>
  );
};
export const Cover: React.FC<CoverProps> = (p) => {
  ensureFonts();
  const c = T[p.theme], dark = p.theme === "dark";
  const safe = p.showSafe ? <div style={{ position: "absolute", left: 0, right: 0, top: 240, height: 1440, outline: "6px dashed #B45309" }} /> : null;
  if (p.direction === "a") return ( // A · Big type: struck old habit → accent new word, chibi reacts below
    <AbsoluteFill style={{ background: c.bg, fontFamily: FONT_FAMILY }}>
      <Series p={p} c={c} x={72} y={310} />
      <div style={{ position: "absolute", left: 66, right: 60, top: 420, display: "flex", flexDirection: "column", gap: 22, alignItems: "flex-start" }}>
        {p.hero.map((w, i) => <Word key={i} w={w} i={i} p={p} c={c} size={196} />)}
      </div>
      <svg width={1080} height={1920} style={{ position: "absolute" }}>
        {dark && <circle cx={720} cy={1330} r={330} fill={c.ink} />}
        <Chibi x={720} groundY={1640} scale={1.25} expression={p.expression} action={p.action} tilt={p.tilt} uid="cv-a" />
        <Emote kind={p.emote} x={930} y={1060} c={dark ? c.bg : c.ink} />
      </svg>
      <Logo c={c} dark={dark} x={72} y={1470} />{safe}
    </AbsoluteFill>
  );
  if (p.direction === "b") return ( // B · Split: top = old habit (inverted panel), bottom = fix + chibi
    <AbsoluteFill style={{ background: c.bg, fontFamily: FONT_FAMILY }}>
      <div style={{ position: "absolute", left: 0, right: 0, top: 0, height: 900, background: c.ink }} />
      <div style={{ position: "absolute", left: 0, right: 0, top: 860, height: 90, background: c.bg, transform: "skewY(-4deg)" }} />
      <div style={{ position: "absolute", left: 72, top: 310, display: "flex", alignItems: "center", gap: 16 }}>
        <div style={{ background: c.bg, color: c.ink, fontSize: 40, fontWeight: 700, borderRadius: 18, padding: "6px 22px 10px" }}>#{String(p.ep).padStart(2, "0")}</div>
        <div style={{ color: c.bg, fontSize: 30, fontWeight: 600, letterSpacing: "0.14em", textTransform: "uppercase" }}>{p.series}</div>
      </div>
      <div style={{ position: "absolute", left: 66, top: 430, fontSize: 64, fontWeight: 600, color: dark ? "#6B6B6B" : "#A3A3A0" }}>Kế hoạch học:</div>
      <div style={{ position: "absolute", left: 60, top: 520, fontSize: fit(p.hero[0], 200, 920), fontWeight: 700, letterSpacing: "-0.035em", color: c.bg, lineHeight: 1 }}>
        <span style={{ position: "relative" }}>{p.hero[0]}<span style={{ position: "absolute", left: -12, right: -12, top: "50%", height: 22, background: c.bg, borderRadius: 20, transform: "rotate(-5deg)" }} /></span>
      </div>
      <div style={{ position: "absolute", left: 72, top: 1010, fontSize: 64, fontWeight: 600, color: c.muted }}>Đổi thành:</div>
      <div style={{ position: "absolute", left: 60, top: 1090 }}><Word w={p.hero[1]} i={p.accent} p={{ ...p, accent: p.accent }} c={c} size={140} /></div>
      <svg width={1080} height={1920} style={{ position: "absolute" }}>
        {dark && <circle cx={850} cy={1440} r={240} fill={c.ink} />}
        <Chibi x={850} groundY={1650} scale={0.8} expression={p.expression} action={p.action} tilt={p.tilt} uid="cv-b" />
      </svg>
      <Logo c={c} dark={dark} x={72} y={1470} />{safe}
    </AbsoluteFill>
  );
  return ( // C · Sticker card: the one-sentence "ticket" as hero object, chibi pointing at it
    <AbsoluteFill style={{ background: c.bg, fontFamily: FONT_FAMILY }}>
      <Series p={p} c={c} x={72} y={310} />
      <div style={{ position: "absolute", left: 66, top: 410, fontSize: 150, fontWeight: 700, letterSpacing: "-0.035em", color: c.ink, lineHeight: 1 }}>
        {(() => { const sz = fit(p.hero.join(" "), 150, 860); return <><Word w={p.hero[0]} i={0} p={p} c={c} size={sz} /> {p.hero[1] ? <Word w={p.hero[1]} i={1} p={p} c={c} size={sz} /> : null}</>; })()}
      </div>
      <div style={{ position: "absolute", left: 80, top: 660, width: 760, background: dark ? c.surface : "#FFFFFF", border: `8px solid ${c.ink}`, borderRadius: 44,
        boxShadow: `14px 16px 0 ${c.ink}`, transform: "rotate(-4deg)", padding: "40px 44px", display: "flex", flexDirection: "column", gap: 26 }}>
        {(p.sub ?? "NẾU ____|THÌ ____").split("|").map((r, i) => (
          <div key={i} style={{ display: "flex", alignItems: "center", gap: 22, fontSize: 64, fontWeight: 700, color: c.ink }}>
            <span style={{ background: c.ink, color: dark ? c.surface : "#FFFFFF", borderRadius: 20, padding: "2px 22px 10px", fontSize: 54 }}>{r.split(" ")[0]}</span>
            <span style={{ borderBottom: `6px dashed ${c.muted}`, flex: 1, paddingBottom: 6 }}>{r.split(" ").slice(1).join(" ").replace(/_+/g, "")}</span>
          </div>
        ))}
      </div>
      <svg width={1080} height={1920} style={{ position: "absolute" }}>
        {dark && <circle cx={770} cy={1400} r={290} fill={c.ink === "#F7F7F5" ? "#F7F7F5" : c.ink} />}
        <Chibi x={770} groundY={1650} scale={1.0} expression={p.expression} action={p.action} tilt={p.tilt} uid="cv-c" />
        <Emote kind={p.emote} x={960} y={1150} c={c.ink} />
      </svg>
      <Logo c={c} dark={dark} x={72} y={1470} />{safe}
    </AbsoluteFill>
  );
};
