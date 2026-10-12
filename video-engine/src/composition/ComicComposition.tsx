import React from "react";
import { AbsoluteFill, Sequence } from "remotion";
import type { VideoPlan } from "../validation/schema";
import { defaultRegistry } from "../characters/registry";
import { buildTimeline } from "../animation/timing";
import { SceneRenderer } from "./SceneRenderer";
import { ensureFonts } from "./fonts";
import { BRAND } from "./theme";

export type ComicProps = { plan: VideoPlan };

/** Multi-scene video: each scene is a Sequence; the incoming scene overlays the previous one during its transition. */
export const ComicComposition: React.FC<ComicProps> = ({ plan }) => {
  ensureFonts();
  const { scenes } = buildTimeline(plan);
  return (
    <AbsoluteFill style={{ background: BRAND.paper }}>
      {scenes.map((st, i) => {
        const next = scenes[i + 1];
        const hold = next ? next.transitionFrames : 0; // keep outgoing scene alive under the incoming transition
        return (
          <Sequence key={st.id} from={st.from} durationInFrames={st.durationInFrames + hold} name={st.id}>
            <SceneRenderer scene={plan.scenes[i]} video={plan.video} registry={defaultRegistry} transitionFrames={st.transitionFrames} durationInFrames={st.durationInFrames} />
          </Sequence>
        );
      })}
    </AbsoluteFill>
  );
};
