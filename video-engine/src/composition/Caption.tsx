import React from "react";
import { BRAND } from "./theme";
import { FONT_FAMILY } from "./fonts";
import { clamp, progress, springAt } from "../animation/timing";

/** Word-timed caption: weights by word length so long words stay up longer. Pure function of t. */
export function wordTimes(text: string, start: number, end: number) {
  const words = text.split(/\s+/).filter(Boolean);
  const w = words.map((x) => x.length + 2);
  const total = w.reduce((a, b) => a + b, 0);
  let acc = start;
  return words.map((word, i) => { const d = ((end - start) * w[i]) / total; const r = { word, start: acc, end: acc + d }; acc += d; return r; });
}

export const Caption: React.FC<{ text: string; start: number; end: number; t: number; highlight: number[]; top: number; theme: "light" | "dark" }> = ({ text, start, end, t, highlight, top }) => {
  if (t < start || t > end) return null;
  const words = wordTimes(text, start, end - 0.25);
  const out = clamp((end - t) / 0.15);
  return (
    <div style={{ position: "absolute", left: 70, right: 70, top, display: "flex", flexWrap: "wrap", justifyContent: "center", gap: "6px 14px", opacity: out, fontFamily: FONT_FAMILY,
      background: BRAND.paper, border: `6px solid ${BRAND.ink}`, borderRadius: 34, padding: "22px 30px 26px", boxShadow: `8px 10px 0 ${BRAND.ink}` }}>
      {words.map((w, i) => {
        const shown = t >= w.start;
        const active = t >= w.start && t < w.end;
        const k = springAt(t - w.start, 18, 9);
        const hl = highlight.includes(i);
        return (
          <span key={i} style={{
            fontSize: 54, fontWeight: 700, lineHeight: 1.18, letterSpacing: -0.5,
            color: hl ? BRAND.paper : BRAND.ink,
            background: hl ? BRAND.ink : "transparent", borderRadius: 18, padding: hl ? "2px 16px 6px" : "2px 0 6px",
            opacity: shown ? 1 : 0.16, transform: `translateY(${(1 - Math.min(1, k)) * 18}px) scale(${shown ? 0.9 + 0.1 * Math.min(1.05, k) : 0.9})`,
            textDecoration: active && !hl ? `underline ${BRAND.ink} 6px` : "none", textUnderlineOffset: 10,
            display: "inline-block",
          }}>{w.word}</span>
        );
      })}
    </div>
  );
};

export const NarrationBox: React.FC<{ text: string; start: number; end: number; t: number }> = ({ text, start, end, t }) => {
  if (t < start || t > end) return null;
  const k = Math.min(1, springAt(t - start, 16, 8));
  const out = clamp((end - t) / 0.2);
  return (
    <div style={{
      position: "absolute", left: 160, top: 66, maxWidth: 900, background: BRAND.ink, color: BRAND.paper,
      fontFamily: FONT_FAMILY, fontWeight: 700, fontSize: 36, letterSpacing: 1.5, textTransform: "uppercase",
      padding: "18px 30px 22px", borderRadius: 22, transform: `translateX(${(1 - k) * -80}px) rotate(-1.5deg)`, opacity: out * progress(t, start, start + 0.12),
      boxShadow: `8px 8px 0 ${BRAND.soft}`,
    }}>{text}</div>
  );
};
