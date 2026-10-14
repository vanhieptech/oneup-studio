import React from "react";
import { Composition } from "remotion";
import { ComicComposition, type ComicProps } from "./composition/ComicComposition";
import { CharacterSheet } from "./composition/CharacterSheet";
import { Cover, type CoverProps } from "./composition/Cover";
import { VideoPlanSchema } from "./validation/schema";
import { buildTimeline } from "./animation/timing";
import clip01 from "../examples/clip-01-story.json";

const defaultPlan = VideoPlanSchema.parse(clip01);

export const RemotionRoot: React.FC = () => (
  <>
    <Composition
      id="ComicVideo"
      component={ComicComposition}
      defaultProps={{ plan: defaultPlan } satisfies ComicProps}
      durationInFrames={buildTimeline(defaultPlan).durationInFrames}
      fps={defaultPlan.video.fps}
      width={defaultPlan.video.width}
      height={defaultPlan.video.height}
      calculateMetadata={({ props }) => {
        const plan = VideoPlanSchema.parse(props.plan); // props come from CLI JSON → re-parse for defaults
        return { durationInFrames: buildTimeline(plan).durationInFrames, fps: plan.video.fps, width: plan.video.width, height: plan.video.height, props: { plan } };
      }}
    />
    <Composition id="Cover" component={Cover as React.FC<CoverProps>} durationInFrames={1} fps={30} width={1080} height={1920}
      defaultProps={{ direction: "a", theme: "light", series: "Làm ít, xong nhiều", ep: 1, hero: ["MAI HỌC", "NẾU–THÌ"], accent: 1, strike: 0, expression: "surprised", emote: "!" } as CoverProps} />
    <Composition id="CharacterSheet" component={CharacterSheet} durationInFrames={90} fps={30} width={1080} height={1920} />
  </>
);
