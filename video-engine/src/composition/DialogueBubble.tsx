import React from "react";
import { BRAND } from "./theme";
import { FONT_FAMILY } from "./fonts";
import { clamp, springAt } from "../animation/timing";

/**
 * Comic speech/thought bubble. Anchored so its tail points at (anchorX, anchorY) = top of the speaker's head.
 * Text supports **bold** spans for emphasis.
 */
export const DialogueBubble: React.FC<{
  text: string; style: "speech" | "thought" | "shout"; start: number; end: number; t: number;
  anchorX: number; anchorY: number; side: -1 | 1;
}> = ({ text, style, start, end, t, anchorX, anchorY, side }) => {
  if (t < start || t > end) return null;
  const k = springAt(t - start, 17, 8);
  const out = clamp((end - t) / 0.18);
  const W = Math.min(800, 170 + text.replace(/\*\*/g, "").length * 26);
  const left = clamp(anchorX - W / 2 + side * 90, 60, 1080 - 60 - W);
  const bottom = anchorY - 70;
  const border = style === "shout" ? 12 : 8;
  const parts = text.split(/(\*\*[^*]+\*\*)/g).filter(Boolean);
  const tailX = clamp(anchorX - left, 70, W - 70);
  return (
    <div style={{ position: "absolute", left, top: bottom, width: W, transform: `translateY(-100%) scale(${0.6 + 0.4 * k})`, transformOrigin: `${tailX}px 100%`, opacity: out * clamp((t - start) / 0.08) }}>
      <div style={{
        background: BRAND.paper, border: `${border}px solid ${BRAND.ink}`, borderRadius: style === "thought" ? 90 : 48,
        padding: "30px 40px 36px", fontFamily: FONT_FAMILY, fontSize: style === "shout" ? 64 : 56, fontWeight: 600,
        lineHeight: 1.22, textWrap: "balance" as React.CSSProperties["textWrap"], color: BRAND.ink, textAlign: "center", boxShadow: `10px 12px 0 ${BRAND.ink}`, letterSpacing: -0.5,
        fontStyle: style === "thought" ? "italic" : "normal",
      }}>
        {parts.map((p, i) => p.startsWith("**") ? <b key={i} style={{ fontWeight: 700, background: BRAND.ink, color: BRAND.paper, borderRadius: 12, padding: "0 10px", whiteSpace: "nowrap" }}>{p.slice(2, -2)}</b> : <span key={i}>{p}</span>)}
      </div>
      <svg width={W} height={80} style={{ position: "absolute", left: 0, top: "100%", marginTop: -border - 2, overflow: "visible" }}>
        {style === "thought" ? (
          <g fill={BRAND.paper} stroke={BRAND.ink} strokeWidth={7}>
            <circle cx={tailX - side * 6} cy={26} r={18} /><circle cx={tailX - side * 20} cy={62} r={11} />
          </g>
        ) : (
          <path d={`M${tailX - 34},0 Q${tailX - 6},30 ${tailX - side * 30},64 Q${tailX + 18},34 ${tailX + 34},0`} fill={BRAND.paper} stroke={BRAND.ink} strokeWidth={border} strokeLinejoin="round" />
        )}
        {style !== "thought" && <rect x={tailX - 30} y={-border - 2} width={60} height={border + 6} fill={BRAND.paper} />}
      </svg>
    </div>
  );
};
