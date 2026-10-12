import React from "react";
import { AbsoluteFill, useCurrentFrame, useVideoConfig } from "remotion";
import { defaultRegistry } from "../characters/registry";
import { CharacterRenderer } from "../characters/CharacterRenderer";
import { getCharacterState } from "../animation/controller";
import { CharacterCueSchema, type Expression } from "../validation/schema";
import { BRAND } from "./theme";
import { ensureFonts, FONT_FAMILY } from "./fonts";

/** Visual QA sheet: every expression of every built-in character, animated (idle). */
export const CharacterSheet: React.FC = () => {
  ensureFonts();
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const rows: { id: string; scale: number; y0: number; cellH: number }[] = [
    { id: "hiep", scale: 0.42, y0: 200, cellH: 330 },
    { id: "omi", scale: 0.62, y0: 1060, cellH: 330 },
  ];
  return (
    <AbsoluteFill style={{ background: BRAND.paper, fontFamily: FONT_FAMILY }}>
      <svg width={1080} height={1920} style={{ position: "absolute" }}>
        {rows.map((r) => {
          const prof = defaultRegistry.get(r.id)!;
          return prof.expressions.map((ex: Expression, i) => {
            const cue = CharacterCueSchema.parse({ characterId: r.id, x: 0, expression: ex });
            const st = getCharacterState({ cue, profile: prof, frame, fps, sceneDuration: 99, dialogue: [] });
            const cx = 200 + (i % 3) * 340, gy = r.y0 + (Math.floor(i / 3) + 1) * r.cellH;
            return (
              <g key={r.id + ex}>
                <g transform={`translate(${cx - st.x} 0)`}>
                  <CharacterRenderer state={st} profile={prof} width={1} groundY={gy} scale={r.scale} uid={`sheet-${r.id}-${ex}`} />
                </g>
                <text x={cx} y={gy + 50} textAnchor="middle" fontFamily={FONT_FAMILY} fontWeight={600} fontSize={32} fill={BRAND.ink}>{ex}</text>
              </g>
            );
          });
        })}
      </svg>
      <div style={{ position: "absolute", left: 70, top: 80, fontSize: 54, fontWeight: 700, color: BRAND.ink }}>Hiệp · biểu cảm</div>
      <div style={{ position: "absolute", left: 70, top: 1000, fontSize: 54, fontWeight: 700, color: BRAND.ink }}>Omi · biểu cảm (từ tuần 5)</div>
    </AbsoluteFill>
  );
};
