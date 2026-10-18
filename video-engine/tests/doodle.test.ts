import { describe, expect, it } from "vitest";
import { doodleEase, doodlePaths, pathLength } from "../src/composition/doodle/doodle";
import { validatePlan } from "../src/validation/validate";

describe("doodle draw-on (anidoodle port)", () => {
  it("is deterministic for a fixed seed", () => {
    expect(doodlePaths("circle", 100, 100, 300, 120, 7)).toEqual(doodlePaths("circle", 100, 100, 300, 120, 7));
    expect(doodlePaths("circle", 100, 100, 300, 120, 8)).not.toEqual(doodlePaths("circle", 100, 100, 300, 120, 7));
  });
  it("builds every registered kind with positive length", () => {
    for (const k of ["circle", "underline", "arrow", "check", "cross", "sketch-box"] as const) {
      const subs = doodlePaths(k, 80, 200, 320, 140, 7);
      expect(subs.length).toBeGreaterThan(0);
      expect(subs.every((s) => pathLength(s) > 0)).toBe(true);
    }
    expect(doodlePaths("path", 0, 0, 10, 10, 7, [[0, 0], [100, 50]])[0].length).toBeGreaterThan(2);
  });
  it("ease is clamped and monotonic", () => {
    expect(doodleEase(-1)).toBe(0); expect(doodleEase(2)).toBe(1);
    expect(doodleEase(0.5)).toBeGreaterThan(doodleEase(0.25));
  });
  it("validate accepts a doodle inside the scene and rejects an overrun", () => {
    const ok = validatePlan({ id: "d", scenes: [{ id: "s", duration: 3, doodles: [{ kind: "circle", x: 100, y: 200, w: 300, h: 120, at: 1, duration: 0.6 }] }] });
    expect(ok.ok).toBe(true);
    const bad = validatePlan({ id: "d", scenes: [{ id: "s", duration: 3, doodles: [{ kind: "circle", x: 100, y: 200, w: 300, h: 120, at: 2.8, duration: 0.6 }] }] });
    expect(bad.ok).toBe(false);
  });
});
