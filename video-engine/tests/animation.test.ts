import { describe, expect, it } from "vitest";
import { buildTimeline, hash01, secondsToFrames } from "../src/animation/timing";
import { getCharacterState } from "../src/animation/controller";
import { assertValidPlan } from "../src/validation/validate";
import { defaultRegistry, createRegistry } from "../src/characters/registry";
import { CharacterCueSchema } from "../src/validation/schema";
import { wordTimes } from "../src/composition/Caption";
import debug from "../examples/debugging-story.json";

describe("timing", () => {
  it("converts seconds to frames", () => {
    expect(secondsToFrames(1, 30)).toBe(30);
    expect(secondsToFrames(2.5, 30)).toBe(75);
    expect(secondsToFrames(0.4, 24)).toBe(10);
  });
  it("lays scenes in order with correct offsets", () => {
    const plan = assertValidPlan(debug);
    const tl = buildTimeline(plan);
    expect(tl.scenes.map((s) => s.id)).toEqual(["s1-bug", "s2-omi-arrives", "s3-think", "s4-win"]);
    expect(tl.scenes.map((s) => s.from)).toEqual([0, 120, 255, 375]);
    expect(tl.durationInFrames).toBe(510);
    expect(tl.scenes[1].transitionFrames).toBe(12);
    expect(tl.scenes[0].transitionFrames).toBe(0);
  });
  it("hash01 is deterministic and in [0,1)", () => {
    expect(hash01("hiep")).toBe(hash01("hiep"));
    expect(hash01("hiep")).not.toBe(hash01("omi"));
    for (let i = 0; i < 100; i++) { const v = hash01(i); expect(v).toBeGreaterThanOrEqual(0); expect(v).toBeLessThan(1); }
  });
});

describe("character state controller", () => {
  const plan = assertValidPlan(debug);
  const scene = plan.scenes[1];
  const state = (frame: number, cueIdx = 0) =>
    getCharacterState({ cue: scene.characters[cueIdx], profile: defaultRegistry.get(scene.characters[cueIdx].characterId)!, frame, fps: 30, sceneDuration: scene.duration, dialogue: scene.dialogue });

  it("is deterministic for the same frame", () => {
    for (const f of [0, 7, 33, 90, 134]) expect(state(f, 1)).toEqual(state(f, 1));
  });
  it("talks only inside its dialogue window", () => {
    expect(state(10, 1).speaking).toBe(false);           // 0.33s, before Omi's line (0.8s)
    expect(state(45, 1).speaking).toBe(true);            // 1.5s
    expect(state(45, 1).action).toBe("talking");
    expect(state(45, 0).speaking).toBe(false);           // Hiệp silent then
    const opens = Array.from({ length: 50 }, (_, i) => state(26 + i, 1).mouthOpen);
    expect(Math.max(...opens)).toBeGreaterThan(0.5);
    expect(Math.min(...opens)).toBeLessThan(0.2);        // lip flap actually moves
  });
  it("applies expression changes with a blend and a forced blink", () => {
    const s4 = plan.scenes[3];
    const st = (f: number) => getCharacterState({ cue: s4.characters[1], profile: defaultRegistry.get("omi")!, frame: f, fps: 30, sceneDuration: s4.duration, dialogue: s4.dialogue });
    expect(st(60).expression).toBe("neutral");
    expect(st(66).expression).toBe("surprised");      // 2.2s
    expect(st(67).expressionBlend).toBeLessThan(1);
    expect(st(68).blink).toBeGreaterThan(0.3);
    expect(st(80).expression).toBe("surprised");
    expect(st(90).expression).toBe("happy");
  });
  it("walks towards toX and keeps the position after the action changes", () => {
    const s4 = plan.scenes[3];
    const st = (f: number) => getCharacterState({ cue: s4.characters[0], profile: defaultRegistry.get("hiep")!, frame: f, fps: 30, sceneDuration: s4.duration, dialogue: s4.dialogue });
    expect(st(0).x).toBeCloseTo(0.04, 5);
    expect(st(30).x).toBeGreaterThan(0.04);
    expect(st(120).x).toBeCloseTo(0.38, 5);
    expect(st(120).action).toBe("reacting");
  });
  it("blinks periodically", () => {
    const blinks = Array.from({ length: 300 }, (_, f) => state(f, 0).blink).filter((b) => b > 0.9).length;
    expect(blinks).toBeGreaterThan(0);
  });
});

describe("profiles", () => {
  it("load once and are reused across plans", () => {
    expect(defaultRegistry.get("hiep")).toBe(defaultRegistry.get("hiep"));
    expect(defaultRegistry.get("hiep")!.expressions).toEqual(["neutral", "happy", "sad", "surprised", "confused", "focused"]);
    expect(defaultRegistry.get("omi")!.availableFromWeek).toBe(5);
  });
  it("can register an extra character without touching scenes", () => {
    const reg = createRegistry([{ ...defaultRegistry.get("hiep")!, id: "hiep-dark", name: "Hiệp (dark)" }]);
    expect(reg.get("hiep-dark")!.rig).toBe("chibi-hiep");
    expect(reg.size).toBe(3);
  });
  it("cue defaults come from schema", () => {
    expect(CharacterCueSchema.parse({ characterId: "hiep" })).toMatchObject({ pose: "standing", action: "idle", expression: "neutral", x: 0.5 });
  });
});

describe("captions", () => {
  it("word times cover the window in order", () => {
    const w = wordTimes("Then I found one sentence", 1, 3);
    expect(w[0].start).toBe(1);
    expect(w.at(-1)!.end).toBeCloseTo(3, 6);
    for (let i = 1; i < w.length; i++) expect(w[i].start).toBeCloseTo(w[i - 1].end, 6);
  });
});
