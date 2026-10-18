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

describe("doodle drawing (creative multi-stroke, L-047)", () => {
  it("sequences strokes by offset and is deterministic", async () => {
    const { strokePaths, strokeWindow, interpTranslate, fadeFactor } = await import("../src/composition/doodle/doodle");
    const s = { points: [[0, 0], [100, 0]] as [number, number][], offset: 0.4, duration: 0.5 };
    expect(strokeWindow(2, s)).toEqual([2.4, 2.9]);
    expect(strokePaths(s, 7)).toEqual(strokePaths(s, 7));
    expect(strokePaths({ points: [[0, 0], [10, 0], [10, 10]], closed: true }, 7).length).toBeGreaterThan(3);
  });
  it("interpolates translate keyframes with hop and fades out", async () => {
    const { interpTranslate, fadeFactor } = await import("../src/composition/doodle/doodle");
    const keys = [{ at: 0, x: 100, y: 0 }, { at: 2, x: 0, y: -100 }];
    expect(interpTranslate(keys, 0)).toEqual({ x: 100, y: 0 });
    expect(interpTranslate(keys, 5)).toEqual({ x: 0, y: -100 });
    const mid = interpTranslate(keys, 1, 20);
    expect(mid.x).toBeCloseTo(50); expect(mid.y).toBeLessThan(-50); // hop lifts above the straight line
    expect(fadeFactor(1, 2, 0.4)).toBe(1); expect(fadeFactor(2.4, 2, 0.4)).toBeCloseTo(0);
  });
  it("validate requires strokes for drawing and rejects stroke overrun", () => {
    const bad1 = validatePlan({ id: "d", scenes: [{ id: "s", duration: 3, doodles: [{ kind: "drawing", x: 0, y: 0, w: 10, h: 10 }] }] });
    expect(bad1.ok).toBe(false);
    const bad2 = validatePlan({ id: "d", scenes: [{ id: "s", duration: 3, doodles: [{ kind: "drawing", x: 0, y: 0, w: 10, h: 10, strokes: [{ points: [[0, 0], [10, 10]], offset: 2.8, duration: 0.5 }] }] }] });
    expect(bad2.ok).toBe(false);
    const ok = validatePlan({ id: "d", scenes: [{ id: "s", duration: 3, doodles: [{ kind: "drawing", x: 0, y: 0, w: 10, h: 10, strokes: [{ points: [[0, 0], [10, 10]], offset: 0, duration: 0.5 }] }] }] });
    expect(ok.ok).toBe(true);
  });
});
