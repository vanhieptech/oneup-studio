import { readFileSync } from "node:fs";
import { describe, expect, it, vi } from "vitest";
import { planFromText } from "../src/scenes/planner";
import { validatePlan } from "../src/validation/validate";
import { getPlanner, planWithFallback, OpenAICompatiblePlanner, RuleBasedPlanner } from "../src/providers/llm";
import clip01 from "../examples/clip-01-story.json";

const txt = readFileSync(new URL("../examples/sample-script.txt", import.meta.url), "utf8");

describe("rule-based planner", () => {
  it("turns the text format into a valid plan", () => {
    const plan = planFromText(txt);
    const r = validatePlan(plan);
    expect(r.ok).toBe(true);
    if (!r.ok) return;
    expect(r.plan.id).toBe("mai-hoc-demo");
    expect(r.plan.meta.week).toBe(1);
    expect(r.plan.scenes.map((s) => s.id)).toEqual(["night", "turn"]);
    const [night, turn] = r.plan.scenes;
    expect(night.characters[0]).toMatchObject({ characterId: "hiep", pose: "sitting" });
    expect(night.dialogue[0].style).toBe("thought");
    expect(night.characters[0].expressionChanges[0].value).toBe("sad");
    expect(turn.transition).toEqual({ type: "iris", duration: 0.5 });
    expect(turn.caption?.highlight).toEqual([0, 1]);
    expect(turn.sfx).toEqual([{ name: "ding", at: 2.4 }]);
    for (const s of r.plan.scenes) for (const d of s.dialogue) { expect(d.start).toBeGreaterThanOrEqual(0); expect(d.end).toBeLessThanOrEqual(s.duration); }
  });
  it("is deterministic", () => { expect(planFromText(txt)).toEqual(planFromText(txt)); });
  it("handles plain prose with inferred moods", () => {
    const plan = planFromText("Hôm nay mệt quá. Sao bug này cứ chạy hoài vậy? Xong rồi!");
    const r = validatePlan(plan);
    expect(r.ok).toBe(true);
    expect(plan.scenes.length).toBe(2);
    expect(plan.scenes[0].characters![0].expression).toBe("sad");
  });
  it("gives actionable errors on bad tags", () => {
    expect(() => planFromText("== a | 3s\nhiep (dancing): hi")).toThrow(/unknown tag "dancing"/);
  });
});

describe("LLM provider abstraction", () => {
  it("defaults to rule-based with no API config", () => {
    expect(getPlanner({}, true)).toBeInstanceOf(RuleBasedPlanner);
    expect(getPlanner({ LLM_BASE_URL: "http://x", LLM_MODEL: "m" }, false)).toBeInstanceOf(RuleBasedPlanner);
    expect(getPlanner({ LLM_BASE_URL: "http://x", LLM_MODEL: "m" }, true)).toBeInstanceOf(OpenAICompatiblePlanner);
  });
  it("accepts a valid LLM response (mocked fetch)", async () => {
    const fetchMock = vi.fn(async () => new Response(JSON.stringify({ choices: [{ message: { content: JSON.stringify(clip01) } }] })));
    const p = new OpenAICompatiblePlanner({ baseUrl: "http://llm.local/v1", model: "m" }, fetchMock as unknown as typeof fetch);
    const plan = await p.plan("whatever");
    expect(validatePlan(plan).ok).toBe(true);
    expect(fetchMock).toHaveBeenCalledWith("http://llm.local/v1/chat/completions", expect.anything());
  });
  it("falls back to rule-based when the LLM output is invalid", async () => {
    const fetchMock = vi.fn(async () => new Response(JSON.stringify({ choices: [{ message: { content: "{\"id\":\"x\",\"scenes\":[]}" } }] })));
    const p = new OpenAICompatiblePlanner({ baseUrl: "http://llm.local/v1", model: "m" }, fetchMock as unknown as typeof fetch);
    const r = await planWithFallback(txt, p);
    expect(r.fallback).toBe(true);
    expect(r.provider).toBe("rule-based");
    expect(validatePlan(r.plan).ok).toBe(true);
  });
});
