import React from "react";
import type { CharacterProfile } from "../validation/schema";
import type { CharacterState } from "../animation/controller";
import { ChibiHiep } from "./rigs/ChibiHiep";
import { OmiBlob } from "./rigs/OmiBlob";

type Rig = React.FC<{ state: CharacterState; profile: CharacterProfile; uid: string }>;
/** rig key (profile.rig) → reusable SVG component. Add a new character = add a profile JSON + a rig here. */
export const RIGS: Record<string, Rig> = { "chibi-hiep": ChibiHiep, "liquid-omi": OmiBlob };

/** Places a rig in canvas space. `groundY`/`scale` come from the camera framing. */
export const CharacterRenderer: React.FC<{
  state: CharacterState; profile: CharacterProfile; width: number; groundY: number; scale: number; uid: string;
}> = ({ state, profile, width, groundY, scale: baseScale, uid }) => {
  let scale = baseScale;
  const Rig = RIGS[profile.rig];
  if (!Rig) throw new Error(`No rig "${profile.rig}" for character "${profile.id}". Known rigs: ${Object.keys(RIGS).join(", ")}`);
  const flip = state.facing === "left" ? -1 : 1;
  const x = state.x * width;
  scale = baseScale * (RIG_SIZE[profile.rig] ?? 1);
  return (
    <g opacity={state.opacity}
       transform={`translate(${x} ${groundY + state.offsetY * scale}) scale(${scale}) rotate(${state.rotation}) scale(${state.scaleX * flip} ${state.scaleY})`}>
      <Rig state={state} profile={profile} uid={uid} />
    </g>
  );
};

/** Local y of the top of the head per rig/pose (used to anchor dialogue bubbles). */
export const RIG_HEAD_TOP: Record<string, Record<string, number>> = {
  "chibi-hiep": { standing: -500, sitting: -404 },
  "liquid-omi": { standing: -300, sitting: -230 },
};

/** Per-rig size multiplier so a small companion still reads at 9:16 next to the chibi. */
export const RIG_SIZE: Record<string, number> = { "chibi-hiep": 1, "liquid-omi": 1.35 };
