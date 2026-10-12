import { describe, it, expect } from "vitest";
import { readFileSync } from "node:fs";
import { validatePlan } from "../src/validation/validate";

const plan = () => JSON.parse(readFileSync(new URL("../../content/samples/sample-full-w5/plan.json", import.meta.url), "utf8"));

describe("caption segments (per voice line)", () => {
  it("accepts ordered segments inside the scene", () => {
    const p = plan(); p.scenes[0].caption.segments = [{ text: "A b", start: 0.3, end: 1.5 }, { text: "C d", start: 1.6, end: 6.5, highlight: [0] }];
    expect(validatePlan(p).ok).toBe(true);
  });
  it("rejects overlapping or out-of-scene segments", () => {
    const p = plan(); p.scenes[0].caption.segments = [{ text: "A", start: 0.3, end: 2 }, { text: "B", start: 1.5, end: 9 }];
    const r = validatePlan(p); expect(r.ok).toBe(false);
    expect(r.issues.filter((i) => i.path.includes("segments")).length).toBeGreaterThanOrEqual(2);
  });
});
