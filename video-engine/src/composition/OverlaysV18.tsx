import React from "react";
import { BRAND } from "./theme";
import { FONT_FAMILY, EN_FONT } from "./fonts";
import { springAt } from "../animation/timing";
import type { PropCue } from "./Props";
import { ICON } from "./PropsV18";

/** clip-04 v18 HTML overlays (real fonts, not drawn inside images): small study-credit tags, the b07 word tag, and the end card. */
const cl = (x: number) => Math.max(0, Math.min(1, x));
const eo = (u: number) => 1 - Math.pow(1 - u, 3);
const Check: React.FC<{ s: number }> = ({ s }) => <svg width={s} height={s} viewBox="-128 -128 256 256" style={{ display: "block" }}>
  <circle r={120} fill={BRAND.accent} stroke={BRAND.ink} strokeWidth={14} />
  <g transform="translate(-96 -96) scale(0.75)"><path d={ICON.check} fill={BRAND.paper} /></g>
</svg>;

export const Overlays: React.FC<{ props?: PropCue[]; t: number; H: number }> = ({ props, t }) => {
  if (!props?.length) return null;
  return <>{props.map((p, i) => {
    if (p.kind === "tag") {
      const at = (p.at as number) ?? 0, until = (p.until as number) ?? 999;
      if (t < at || t > until) return null;
      const k = Math.min(1.08, springAt(t - at, 17, 9)); const out = cl((until - t) / 0.15);
      const word = p.style === "word";
      return <div key={`tg${i}`} style={{ position: "absolute", left: (p.x as number) ?? 540, top: (p.y as number) ?? 300, transform: `translate(-50%, -50%) scale(${k}) rotate(${(p.rot as number) ?? 0}deg)`, opacity: out,
        display: "flex", alignItems: "center", gap: 14, whiteSpace: "nowrap",
        fontFamily: p.font === "en" ? EN_FONT : FONT_FAMILY, fontWeight: word ? 700 : 600, fontSize: (p.size as number) ?? (word ? 64 : 30), letterSpacing: word ? -0.5 : 0,
        color: word ? BRAND.paper : BRAND.ink, background: word ? BRAND.ink : BRAND.paper, border: `${word ? 0 : 5}px solid ${BRAND.ink}`,
        borderRadius: word ? 26 : 18, padding: word ? "12px 22px 16px 30px" : "8px 18px 10px", boxShadow: `${word ? 8 : 6}px ${word ? 10 : 7}px 0 ${word ? BRAND.soft : BRAND.ink}` }}>
        <span>{p.text as string}</span>{p.tick ? <Check s={word ? 66 : 34} /> : null}
      </div>;
    }
    if (p.kind === "counter") { // clip-05 v4: share counter counts up (e.g. 55,3K), Vietnamese decimal comma
      const at = (p.at as number) ?? 0; if (t < at) return null; const u = eo(cl((t - at) / ((p.dur as number) ?? 0.7)));
      const v = ((p.to as number) ?? 0) * u; const txt = v.toFixed((p.dec as number) ?? 1).replace(".", ",") + ((p.suffix as string) ?? "");
      const k = Math.min(1.08, springAt(t - at, 17, 9));
      return <div key={`ct${i}`} style={{ position: "absolute", left: (p.x as number) ?? 540, top: (p.y as number) ?? 300, transform: `translate(-50%, -50%) scale(${k})`, fontFamily: FONT_FAMILY, fontWeight: 700,
        fontSize: (p.size as number) ?? 34, color: BRAND.paper, background: BRAND.ink, borderRadius: 16, padding: "4px 14px 8px", whiteSpace: "nowrap", fontVariantNumeric: "tabular-nums" }}>{txt}</div>;
    }
    if (p.kind === "endcard") {
      const u = eo(cl((t - ((p.at as number) ?? 0)) / 0.3)); // soft-land 0.3s
      return <div key={`ec${i}`} style={{ position: "absolute", left: 0, top: 0, width: 1080, height: 1920 }}>
        <div style={{ position: "absolute", inset: 0, background: BRAND.ink, opacity: 0.35 }} />
        <div style={{ position: "absolute", left: 96, right: 96, top: (p.y as number) ?? 600, transform: `translateY(${(1 - u) * 70}px)`, opacity: u,
          background: BRAND.paper, border: `10px solid ${BRAND.ink}`, borderRadius: 44, boxShadow: `14px 16px 0 ${BRAND.ink}`, padding: "56px 58px 60px", fontFamily: FONT_FAMILY, color: BRAND.ink }}>
          <div style={{ fontWeight: 700, fontSize: 50, lineHeight: 1.25, letterSpacing: -0.5 }}>{p.text as string}</div>
          <div style={{ height: 8, background: BRAND.ink, borderRadius: 4, margin: "36px 0 30px", width: 120 }} />
          <div style={{ fontWeight: 600, fontSize: 34, lineHeight: 1.3, color: BRAND.ink, opacity: 0.8 }}>{p.sub as string}</div>
          {(() => { const c = String(p.stamp ?? ""); const m = c.match(/^(.*?)\s*(https?:\/\/\S+)$/); // URL on its own line, never broken
            return <div style={{ fontWeight: 500, fontSize: 30, lineHeight: 1.4, marginTop: 26 }}>{m ? m[1] : c}{m && <div style={{ fontSize: 27, whiteSpace: "nowrap", letterSpacing: -0.4, marginTop: 4 }}>{m[2]}</div>}</div>; })()}
        </div>
      </div>;
    }
    return null;
  })}</>;
};
