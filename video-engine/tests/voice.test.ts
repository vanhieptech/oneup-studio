import { describe, it, expect } from "vitest";
import { readFileSync } from "node:fs";
import { validatePlan } from "../src/validation/validate";
import { collectVoiceJobs, spokenText } from "../src/voice/voice";
import { mouthFromEnvelope } from "../src/animation/controller";
import { hasAudio } from "../src/rendering/render";

const plan = () => JSON.parse(readFileSync(new URL("../../content/samples/sample-full-w5/plan.json", import.meta.url), "utf8"));

describe("Omi voice (rule-46)", () => {
  it("each character uses its own voice (Hiệp: F5 · Thái Sơn, Omi: F5 · Mỹ Duyên; DL-035)", () => {
    const r = validatePlan(plan()); expect(r.ok).toBe(true);
    const jobs = collectVoiceJobs(r.ok ? r.plan : (null as never));
    expect(jobs.length).toBe(4);
    expect(jobs.map((j) => j.voice)).toEqual(["F5 · Thái Sơn", "F5 · Mỹ Duyên", "F5 · Mỹ Duyên", "F5 · Thái Sơn"]);
    expect(jobs.every((j) => j.engine === "f5-tts" && !!j.ref && !!j.refText)).toBe(true);
    expect(jobs[1].emotion).toBe("teasing"); // explicit emotion wins
    expect(jobs[2].emotion).toBe("focused"); // falls back to expression at line start
  });
  it("cache key is stable for identical text/voice/emotion", () => {
    const r = validatePlan(plan()); if (!r.ok) throw 0;
    expect(collectVoiceJobs(r.plan)[0].key).toBe(collectVoiceJobs(r.plan)[0].key);
  });
  it("rejects AI audio on a speaker without a declared voice preset", () => {
    const p = plan(); p.scenes[0].dialogue.push({ speaker: "narrator", text: "x", start: 0.1, end: 0.5 }); p.scenes[0].dialogue[2].audio = { src: "voice/x.wav", duration: 1, envelope: [] };
    const r = validatePlan(p); expect(r.ok).toBe(false);
    expect(r.issues.some((i) => i.message.includes("rule-46"))).toBe(true);
  });
  it("rejects voice lines that run past the scene", () => {
    const p = plan(); p.scenes[0].dialogue[1].audio = { src: "voice/x.wav", duration: 9, envelope: [] };
    expect(validatePlan(p).ok).toBe(false);
  });
  it("mouth follows the audio envelope and closes in silence", () => {
    const env = [0, 0, 1, 1, 1, 0, 0];
    expect(mouthFromEnvelope(env, 3 / 30, 30)).toBeGreaterThan(0.9);
    expect(mouthFromEnvelope(env, 0, 30)).toBe(0);
    expect(mouthFromEnvelope(env, 5, 30)).toBe(0);
  });
  it("spoken text strips bubble markup; render unmutes only with audio", () => {
    expect(spokenText("Ủa, lại **mai học** nữa hả…")).toBe("Ủa, lại mai học nữa hả,");
    const r = validatePlan(plan()); if (!r.ok) throw 0;
    expect(hasAudio(r.plan)).toBe(false);
  });
  it("week < 5 still blocks Omi (rule-11)", () => {
    const p = plan(); p.meta.week = 4; expect(validatePlan(p).ok).toBe(false);
  });
});
