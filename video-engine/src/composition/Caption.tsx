import React from "react";
import { BRAND } from "./theme";
import { FONT_FAMILY, EN_FONT } from "./fonts";
import { clamp, progress, springAt } from "../animation/timing";

/** Word-timed caption: weights by word length so long words stay up longer. Pure function of t. */
export function wordTimes(text: string, start: number, end: number) {
  const words = text.split(/\s+/).filter(Boolean);
  const w = words.map((x) => x.length + 2);
  const total = w.reduce((a, b) => a + b, 0);
  let acc = start;
  return words.map((word, i) => { const d = ((end - start) * w[i]) / total; const r = { word, start: acc, end: acc + d }; acc += d; return r; });
}

export const Caption: React.FC<{ text: string; start: number; end: number; t: number; highlight: number[]; top: number; theme: "light" | "dark"; narrow?: boolean; accent?: boolean }> = ({ text, start, end, t, highlight, top, narrow, accent }) => {
  if (t < start || t > end) return null;
  const words = wordTimes(text, start, end - 0.25);
  const out = clamp((end - t) / 0.15);
  return (
    <div style={{ position: "absolute", left: narrow ? 60 : 70, right: narrow ? 440 : 70, top, display: "flex", flexWrap: "wrap", justifyContent: narrow ? "flex-start" : "center", // reels: narrow left box keeps the face (x≈.76) clear
 gap: "6px 14px", opacity: out, fontFamily: EN_FONT, // EN captions: DM Sans (brand pair)
      background: BRAND.paper, border: `6px solid ${BRAND.ink}`, borderRadius: 34, padding: narrow ? "18px 26px 22px" : "22px 30px 26px", boxShadow: `8px 10px 0 ${BRAND.ink}` }}>
      {words.map((w, i) => {
        const shown = t >= w.start;
        const active = t >= w.start && t < w.end;
        const k = springAt(t - w.start, 18, 9);
        const hl = highlight.includes(i);
        return (
          <span key={i} style={{
            fontSize: narrow ? 46 : 54, fontWeight: 700, lineHeight: 1.18, letterSpacing: -0.5,
            color: hl ? (accent ? BRAND.ink : BRAND.paper) : BRAND.ink,
            background: hl ? (accent ? BRAND.accent : BRAND.ink) : "transparent", borderRadius: 18, padding: hl ? "2px 16px 6px" : "2px 0 6px",
            opacity: shown ? 1 : 0.16, transform: `translateY(${(1 - Math.min(1, k)) * 18}px) scale(${shown ? 0.9 + 0.1 * Math.min(1.05, k) : 0.9})`,
            textDecoration: active && !hl ? `underline ${BRAND.ink} 6px` : "none", textUnderlineOffset: 10,
            display: "inline-block",
          }}>{w.word}</span>
        );
      })}
    </div>
  );
};

export const NarrationBox: React.FC<{ text: string; start: number; end: number; t: number; top?: number }> = ({ text, start, end, t, top = 66 }) => {
  if (t < start || t > end) return null;
  const hook = start === 0; // rule-55: hook text is fully visible and big on frame 0
  const k = hook ? 1 : Math.min(1, springAt(t - start, 16, 8));
  const out = clamp((end - t) / 0.2);
  return (
    <div style={{
      position: "absolute", left: 160, top, maxWidth: 900, background: BRAND.ink, color: BRAND.paper,
      fontFamily: FONT_FAMILY, fontWeight: hook ? 800 : 700, fontSize: hook ? 60 : 36, letterSpacing: hook ? 0.5 : 1.5, lineHeight: 1.15, textTransform: "uppercase",
      padding: "18px 30px 22px", borderRadius: 22, transform: `translateX(${(1 - k) * -80}px) rotate(-1.5deg)`, opacity: out * (hook ? 1 : progress(t, start, start + 0.12)),
      boxShadow: `8px 8px 0 ${BRAND.soft}`,
    }}>{text}</div>
  );
};
