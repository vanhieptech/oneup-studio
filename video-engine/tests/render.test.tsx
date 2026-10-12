import React from "react";
import { renderToStaticMarkup } from "react-dom/server";
import { describe, expect, it } from "vitest";
import { RIGS } from "../src/characters/CharacterRenderer";
import { defaultRegistry } from "../src/characters/registry";
import { getCharacterState } from "../src/animation/controller";
import { CharacterCueSchema } from "../src/validation/schema";

/** Renders every supported (pose × action × expression) of every profile to SVG markup: no throw, non-trivial output, deterministic. */
describe("character rigs render every supported state", () => {
  for (const prof of defaultRegistry.values()) {
    it(`${prof.name}: ${prof.poses.length}×${prof.actions.length}×${prof.expressions.length} states`, () => {
      const Rig = RIGS[prof.rig];
      expect(Rig).toBeDefined();
      const seen = new Set<string>();
      for (const pose of prof.poses) for (const action of prof.actions) for (const expression of prof.expressions) {
        if (pose === "sitting" && action === "walking") continue;
        const cue = CharacterCueSchema.parse({ characterId: prof.id, pose, action, expression });
        const st = getCharacterState({ cue, profile: prof, frame: 17, fps: 30, sceneDuration: 5, dialogue: [] });
        const svg = renderToStaticMarkup(<svg><Rig state={st} profile={prof} uid="t" /></svg>);
        expect(svg.length).toBeGreaterThan(800);
        expect(svg).not.toMatch(/NaN|undefined/);
        expect(renderToStaticMarkup(<svg><Rig state={st} profile={prof} uid="t" /></svg>)).toBe(svg);
        seen.add(svg);
      }
      // expressions/actions must actually change the drawing
      expect(seen.size).toBeGreaterThan(prof.expressions.length * 2);
    });
  }
});
