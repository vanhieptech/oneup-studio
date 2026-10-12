import type { CharacterCue, CharacterProfile, Dialogue, Expression, Action, Pose } from "../validation/schema";
import { clamp, easeInOutCubic, easeOutBack, hash01, lerp, progress, springAt } from "./timing";

/** Fully-resolved, render-ready state for one character at one frame. Pure data. */
export interface CharacterState {
  id: string;
  t: number;               // seconds since scene start
  x: number;               // 0..1 horizontal anchor
  offsetY: number;         // px (local units), negative = up
  scaleX: number; scaleY: number; rotation: number; opacity: number;
  pose: Pose;
  action: Action;
  expression: Expression;
  prevExpression: Expression;
  expressionBlend: number; // 0 = prev, 1 = current (for morphing rigs)
  blink: number;           // 0 open … 1 closed
  mouthOpen: number;       // 0..1 lip-flap while speaking
  speaking: boolean;
  look: number;            // -1..1 gaze
  headTilt: number;        // degrees
  armSwing: number;        // degrees, action-dependent
  walkPhase: number;       // radians
  typingPhase: number;     // 0..1 alternating hands
  facing: "left" | "right";
}

const EXPR_MORPH = 0.28; // seconds for expression blend
const BLINK = 0.16;

function valueAt<T extends string>(base: T, changes: { at: number; value: string }[], t: number) {
  let cur = base, prev = base, since = -1e9;
  for (const c of [...changes].sort((a, b) => a.at - b.at)) {
    if (c.at <= t) { prev = cur; cur = c.value as T; since = c.at; }
  }
  return { cur, prev, since };
}

/** Lip flap: syllable-like rhythm derived from text, deterministic. */
export function mouthAt(text: string, local: number, dur: number): number {
  if (local < 0 || local > dur) return 0;
  const syll = Math.max(2, text.split(/\s+/).length * 1.4);
  const rate = syll / Math.max(dur, 0.1);
  const ph = local * rate * Math.PI * 2;
  const v = 0.5 + 0.5 * Math.sin(ph) * (0.75 + 0.25 * Math.sin(ph * 0.37 + text.length));
  const fade = clamp(local / 0.08) * clamp((dur - local) / 0.1);
  return clamp(v) * fade;
}

export function getCharacterState(args: {
  cue: CharacterCue; profile: CharacterProfile; frame: number; fps: number;
  sceneDuration: number; dialogue: Dialogue[];
}): CharacterState {
  const { cue, profile, frame, fps, sceneDuration, dialogue } = args;
  const t = frame / fps;
  const seed = hash01(profile.id);

  const ex = valueAt(cue.expression as Expression, cue.expressionChanges, t);
  const ac = valueAt(cue.action as Action, cue.actionChanges, t);
  const expressionBlend = ex.since < -1e8 ? 1 : easeInOutCubic(progress(t, ex.since, ex.since + EXPR_MORPH));

  // speaking from dialogue lines owned by this character
  const line = dialogue.find((d) => d.speaker === cue.characterId && t >= d.start && t <= d.end);
  const speaking = !!line && line.style !== "thought";
  let action = ac.cur;
  if (speaking && action === "idle") action = "talking";
  const mouthOpen = speaking && line ? mouthAt(line.text, t - line.start, line.end - line.start) : 0;

  // blink: periodic, per-character offset, plus a forced blink at each expression change
  const period = profile.defaults.blinkEverySec;
  const ph = (t + seed * period) % period;
  let blink = ph < BLINK ? Math.sin((ph / BLINK) * Math.PI) : 0;
  const sinceEx = t - ex.since;
  if (sinceEx >= 0 && sinceEx < 0.2) blink = Math.max(blink, Math.sin((sinceEx / 0.2) * Math.PI));

  // base breathing
  const breath = Math.sin(t * 2.2 + seed * 6);
  let scaleX = 1 - 0.012 * breath, scaleY = 1 + 0.018 * breath;
  let offsetY = 0, rotation = 0, headTilt = 2 * Math.sin(t * 1.3 + seed * 3), armSwing = 2 * breath;
  let look = 0.25 * Math.sin(t * 0.7 + seed * 9);
  let walkPhase = 0, typingPhase = 0;
  let x = cue.x;

  switch (action) {
    case "talking":
      headTilt += 3 * Math.sin(t * 5.1);
      offsetY -= 4 * Math.abs(Math.sin(t * 5.1));
      armSwing = 10 + 14 * Math.max(0, Math.sin(t * 3.4));
      break;
    case "thinking":
      headTilt = 9 + 2 * Math.sin(t * 1.1);
      look = -0.6;
      break;
    case "typing":
      typingPhase = (t * 6) % 1;
      headTilt = -3 + 1.5 * Math.sin(t * 7);
      look = 0.15;
      break;
    case "walking": {
      walkPhase = t * Math.PI * 3.2;
      offsetY -= 14 * Math.abs(Math.sin(walkPhase));
      rotation = 3 * Math.sin(walkPhase);
      armSwing = 22 * Math.sin(walkPhase);
      break;
    }
    case "reacting": {
      const rs = ac.since > -1e8 ? ac.since : 0;
      const k = t - rs;
      const jump = k < 0.5 ? Math.sin((k / 0.5) * Math.PI) : 0;
      offsetY -= 70 * jump;
      const squash = k < 0.12 ? Math.sin((k / 0.12) * Math.PI) : 0;
      scaleX += 0.12 * squash - 0.05 * jump; scaleY += -0.1 * squash + 0.07 * jump;
      armSwing = 40 * jump + 20;
      break;
    }
  }

  // walk path: from x to toX during the walking window (persists after the action changes)
  if (cue.toX !== undefined) {
    const all = [{ at: 0, value: cue.action }, ...[...cue.actionChanges].sort((a, b) => a.at - b.at)];
    const wi = all.findIndex((c) => c.value === "walking");
    if (wi >= 0) {
      const ws = all[wi].at, we = all[wi + 1]?.at ?? sceneDuration * 0.85;
      x = lerp(cue.x, cue.toX, easeInOutCubic(progress(t, ws, we)));
    }
  }

  // emotion body language
  const e = ex.cur;
  if (e === "sad") { offsetY += 10; headTilt -= 6; scaleY -= 0.02; armSwing -= 6; }
  if (e === "surprised") { const k = clamp(sinceEx / 0.35); scaleY += 0.06 * (1 - k) * (sinceEx >= 0 ? 1 : 0); }

  // enter / exit
  let opacity = 1;
  const te = t;
  if (cue.enter === "pop") { const s = springAt(te * 1.2, 16, 7); scaleX *= s; scaleY *= s; }
  if (cue.enter === "rise") { const k = easeOutBack(clamp(te / 0.5)); offsetY += (1 - k) * 260; opacity *= clamp(te / 0.2); }
  if (cue.enter === "slide-left" || cue.enter === "slide-right") {
    const k = easeOutBack(clamp(te / 0.55)); x += (cue.enter === "slide-left" ? -0.7 : 0.7) * (1 - k);
  }
  const tx = sceneDuration - t;
  if (cue.exit === "fade") opacity *= clamp(tx / 0.3);
  if (cue.exit === "slide-left" || cue.exit === "slide-right") {
    const k = easeInOutCubic(1 - clamp(tx / 0.45)); x += (cue.exit === "slide-left" ? -0.8 : 0.8) * k;
  }

  return {
    id: cue.characterId, t, x, offsetY, scaleX, scaleY, rotation, opacity,
    pose: cue.pose as Pose, action, expression: ex.cur, prevExpression: ex.prev, expressionBlend,
    blink: clamp(blink), mouthOpen, speaking, look, headTilt, armSwing, walkPhase, typingPhase,
    facing: cue.facing,
  };
}
