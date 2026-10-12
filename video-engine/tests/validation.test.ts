import { describe, expect, it } from "vitest";
import { validatePlan } from "../src/validation/validate";
import clip01 from "../examples/clip-01-story.json";
import debug from "../examples/debugging-story.json";

const base = () => JSON.parse(JSON.stringify(debug));
const errs = (input: unknown) => { const r = validatePlan(input); return r.ok ? [] : r.issues.filter((i) => i.severity === "error").map((i) => `${i.path}: ${i.message}`); };

describe("plan validation", () => {
  it("accepts the example plans", () => {
    expect(validatePlan(clip01).ok).toBe(true);
    expect(validatePlan(debug).ok).toBe(true);
  });
  it("applies defaults (1080x1920 30fps light)", () => {
    const r = validatePlan({ id: "x", scenes: [{ id: "a", duration: 2 }] });
    expect(r.ok && r.plan.video).toEqual({ width: 1080, height: 1920, fps: 30, theme: "light" });
  });
  it("rejects duplicate scene ids", () => {
    const p = base(); p.scenes[1].id = p.scenes[0].id;
    expect(errs(p).join()).toMatch(/duplicate scene id "s1-bug"/);
  });
  it("rejects invalid durations", () => {
    const p = base(); p.scenes[0].duration = 0;
    expect(errs(p).join()).toMatch(/duration must be > 0/);
    const q = base(); q.scenes[0].duration = 0.01;
    expect(errs(q).join()).toMatch(/shorter than one frame/);
  });
  it("rejects unsupported action/expression/pose with the supported list", () => {
    const p = base();
    p.scenes[1].characters[1].action = "typing"; // Omi has no hands
    p.scenes[0].characters[0].expression = "angry";
    p.scenes[0].characters[0].pose = "lying";
    const e = errs(p).join("\n");
    expect(e).toMatch(/Omi does not support action "typing"\. Supported: idle, talking/);
    expect(e).toMatch(/unknown expression "angry"/);
    expect(e).toMatch(/unknown pose "lying"/);
  });
  it("rejects missing character profiles", () => {
    const p = base(); p.scenes[0].characters[0].characterId = "ghost";
    expect(errs(p).join()).toMatch(/no character profile "ghost"\. Known: hiep, omi/);
  });
  it("rejects dialogue outside scene bounds and inverted ranges", () => {
    const p = base(); p.scenes[0].dialogue[0].end = 9;
    expect(errs(p).join()).toMatch(/ends at 9s but scene is only 4s/);
    const q = base(); q.scenes[0].dialogue[0].start = 3; q.scenes[0].dialogue[0].end = 2;
    expect(errs(q).join()).toMatch(/must be after start/);
  });
  it("rejects speakers not in the scene", () => {
    const p = base(); p.scenes[0].dialogue[0].speaker = "omi";
    expect(errs(p).join()).toMatch(/speaker "omi" is not in this scene/);
  });
  it("rejects invalid video config and odd dimensions", () => {
    const p = base(); p.video.fps = 0;
    expect(errs(p).join()).toMatch(/video\.fps/);
    const q = base(); q.video.width = 1081;
    expect(errs(q).join()).toMatch(/must be even/);
  });
  it("rejects unsupported transitions, backgrounds, framings", () => {
    const p = base(); p.scenes[1].transition.type = "spin"; p.scenes[0].background.kind = "beach"; p.scenes[0].camera.framing = "drone";
    const e = errs(p).join("\n");
    expect(e).toMatch(/unsupported transition "spin"/);
    expect(e).toMatch(/unsupported background "beach"/);
    expect(e).toMatch(/unsupported framing "drone"/);
  });
  it("enforces Omi availability from week 5 (rule-11)", () => {
    const p = base(); p.meta.week = 2;
    expect(errs(p).join()).toMatch(/Omi may only appear from week 5/);
  });
  it("rejects walking while sitting", () => {
    const p = base(); p.scenes[0].characters[0].action = "walking";
    expect(errs(p).join()).toMatch(/cannot walk while sitting/);
  });
});
