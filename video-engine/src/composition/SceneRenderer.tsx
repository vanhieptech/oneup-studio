import React from "react";
import { AbsoluteFill, Audio, OffthreadVideo, Sequence, staticFile, useCurrentFrame } from "remotion";
import type { Scene, VideoConfig } from "../validation/schema";
import type { ProfileRegistry } from "../characters/registry";
import { getCharacterState } from "../animation/controller";
import { CharacterRenderer, RIG_HEAD_TOP, RIG_SIZE } from "../characters/CharacterRenderer";
import { Background } from "./Background";
import { Props, type PropCue } from "./Props";
import { Doodle } from "./doodle/Doodle";
import { Caption, NarrationBox } from "./Caption";
import { DialogueBubble } from "./DialogueBubble";
import { BRAND, DESIGN_W, FRAMING } from "./theme";
import { transitionStyle } from "./transitions";
import { easeInOutCubic } from "../animation/timing";
import { sceneObstacles, placeBubble } from "./layout";
import { Overlays } from "./OverlaysV18";

export const SceneRenderer: React.FC<{
  scene: Scene; video: VideoConfig; registry: ProfileRegistry; transitionFrames: number; durationInFrames: number;
}> = ({ scene, video, registry, transitionFrames, durationInFrames }) => {
  const frame = useCurrentFrame();
  const { fps, width, height, theme } = video;
  const t = frame / fps;
  const k = width / DESIGN_W;
  const H = height / k; // design height
  const fr = FRAMING[scene.camera.framing as keyof typeof FRAMING] ?? FRAMING.medium;
  const groundY = H * (fr.groundY / 1920);
  const push = 1 + scene.camera.push * easeInOutCubic(Math.min(1, frame / Math.max(1, durationInFrames)));

  const states = scene.characters.map((cue) => {
    const profile = registry.get(cue.characterId)!;
    return { cue, profile, state: getCharacterState({ cue, profile, frame, fps, sceneDuration: scene.duration, dialogue: scene.dialogue }) };
  });

  const cx = 540, cy = groundY - 320;
  const camT = `translate(${cx} ${cy}) scale(${push}) translate(${-cx} ${-cy})`;
  const proj = (x: number, y: number) => ({ x: cx + (x - cx) * push, y: cy + (y - cy) * push });

  const tStyle = transitionFrames > 0 && frame < transitionFrames ? transitionStyle(scene.transition.type, frame / transitionFrames, width, height) : {};
  const frameColor = theme === "dark" ? BRAND.ink : BRAND.paper;
  const reels = video.layout === "reels"; // Reels/Shorts: captions y≈1000–1240, title y≥300
  const capTop = reels ? 1000 : H * 0.775;
  const ec = (scene.props as PropCue[] | undefined)?.find((p) => p.kind === "endcard");
  const plate = (scene.props as PropCue[] | undefined)?.find((p) => p.kind === "plate") as (PropCue & { src: string; from?: number }) | undefined; // rule-42: HyperFrames MG beat

  return (
    <AbsoluteFill style={{ ...tStyle, overflow: "hidden" }}>
      <div style={{ position: "absolute", width: DESIGN_W, height: H, transform: `scale(${k})`, transformOrigin: "0 0" }}>
        {plate && <OffthreadVideo src={staticFile(plate.src)} startFrom={Math.round((plate.from ?? 0) * fps)} muted style={{ position: "absolute", left: 0, top: 0, width: DESIGN_W, height: H }} />}
        <svg width={DESIGN_W} height={H} viewBox={`0 0 ${DESIGN_W} ${H}`} style={{ position: "absolute", inset: 0 }}>
          {ec && <defs><filter id={`ecb-${scene.id}`} x="-5%" y="-5%" width="110%" height="110%"><feGaussianBlur stdDeviation={14} /></filter></defs>}
          <g transform={camT} filter={ec ? `url(#ecb-${scene.id})` : undefined}>
            <Background kind={scene.background.kind} h={H} t={t} theme={theme} floorY={H * (1390 / 1920)} bg={video.sceneBg} floorFill={video.floorBg} />
            {states.map(({ state, profile }, i) => (
              <CharacterRenderer key={profile.id} uid={`${scene.id}-${profile.id}-${i}`} state={state} profile={profile} width={DESIGN_W} groundY={groundY} scale={fr.scale} />
            ))}
            {scene.props?.length ? <Props props={scene.props as PropCue[]} t={t} h={H} /> : null}
            {scene.doodles?.map((d, i) => <Doodle key={`doodle${i}`} cue={d} t={t} />)}
          </g>
          {/* comic panel frame */}
          <path fillRule="evenodd" fill={frameColor} d={`M0,0 H${DESIGN_W} V${H} H0 Z M84,28 H${DESIGN_W - 84} Q${DESIGN_W - 28},28 ${DESIGN_W - 28},84 V${H - 84} Q${DESIGN_W - 28},${H - 28} ${DESIGN_W - 84},${H - 28} H84 Q28,${H - 28} 28,${H - 84} V84 Q28,28 84,28 Z`} />
          <rect x={28} y={28} width={DESIGN_W - 56} height={H - 56} rx={56} fill="none" stroke={BRAND.ink} strokeWidth={12} />
        </svg>
        {scene.dialogue.map((d, i) => {
          if (d.bubble === false) return null; // v18: hook/b03/b06 voice + caption only
          const obstacles = sceneObstacles(scene.props as never, states.map(({ state, profile }) => ({ x: state.x * DESIGN_W, headY: groundY + (RIG_HEAD_TOP[profile.rig]?.[state.pose] ?? -480) * fr.scale * (RIG_SIZE[profile.rig] ?? 1), id: profile.id })), groundY, fr.scale);
          const s = states.find((x) => x.cue.characterId === d.speaker);
          const headTop = s ? RIG_HEAD_TOP[s.profile.rig]?.[s.state.pose] ?? -480 : -480;
          const ax = s ? s.state.x * DESIGN_W : d.anchor ? d.anchor[0] : 540;
          const ay = s ? groundY + (s.state.offsetY + headTop) * fr.scale * (RIG_SIZE[s.profile.rig] ?? 1) : d.anchor ? d.anchor[1] : H * 0.35;
          const p = proj(ax, Math.max(ay, 420));
          return <DialogueBubble key={i} text={d.text} style={d.style} start={d.start} end={d.end} t={t} anchorX={p.x} anchorY={p.y} side={ax > 540 ? -1 : 1} layout={placeBubble(d.text, p.x, p.y, ax > 540 ? -1 : 1, obstacles)} />;
        })}
        {scene.dialogue.map((d, i) => d.audio ? (
          <Sequence key={`a${i}`} from={Math.round(d.start * fps)} durationInFrames={Math.ceil(d.audio.duration * fps) + 2} layout="none">
            <Audio src={staticFile(d.audio.src)} />
          </Sequence>
        ) : null)}
        <Overlays props={scene.props as PropCue[] | undefined} t={t} H={H} />
        {scene.narration && <NarrationBox text={scene.narration.text} start={scene.narration.start} end={scene.narration.end ?? scene.duration} t={t} top={reels ? 300 : 66} />}
        {scene.caption && !scene.caption.segments?.length && <Caption text={scene.caption.text} start={scene.caption.start} end={scene.caption.end ?? scene.duration} t={t} highlight={scene.caption.highlight} top={capTop} theme={theme} narrow={reels} accent={video.captionAccent} />}
        {scene.caption?.segments?.map((sg, i) => <Caption key={`cs${i}`} text={sg.text} start={sg.start} end={sg.end} t={t} highlight={sg.highlight} top={capTop} theme={theme} narrow={reels} accent={video.captionAccent} />)}
      </div>
    </AbsoluteFill>
  );
};
