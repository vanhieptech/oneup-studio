import React from "react";
import { AbsoluteFill, useCurrentFrame, useVideoConfig } from "remotion";
import { tdevStyle, TDEV_NAMES, TDEV_DURATION } from "./tdev";

/** Demo grid of the transitions.dev ports: each tile replays its entrance every 1.5s. */
export const TdevDemo: React.FC = () => {
  const f = useCurrentFrame(), { fps } = useVideoConfig();
  const t = (f % Math.round(fps * 1.5)) / fps - 0.2;
  return (
    <AbsoluteFill style={{ background: "#FFF7E8", padding: 40, display: "grid", gridTemplateColumns: "1fr 1fr", gap: 30, fontFamily: "sans-serif" }}>
      {TDEV_NAMES.map((n) => {
        const p = t / TDEV_DURATION[n];
        return (
          <div key={n} style={{ background: "#fff", borderRadius: 28, border: "4px solid #111", display: "flex", flexDirection: "column", alignItems: "center", justifyContent: "center", gap: 20, overflow: "hidden" }}>
            <div style={{ display: "flex", gap: 14, ...(n === "tdev-stagger" ? {} : tdevStyle(n, p)) }}>
              {(n === "tdev-stagger" ? [0, 1, 2] : [0]).map((i) => (
                <div key={i} style={{ width: n === "tdev-stagger" ? 90 : 220, height: 130, borderRadius: 22, background: "#FF6B3D", border: "4px solid #111", ...(n === "tdev-stagger" ? tdevStyle(n, p, { i: i * 3 }) : {}) }} />
              ))}
            </div>
            <div style={{ fontSize: 40, fontWeight: 700, color: "#111" }}>{n.replace("tdev-", "")}</div>
          </div>
        );
      })}
    </AbsoluteFill>
  );
};
