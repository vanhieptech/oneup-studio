import { planFromText } from "../../scenes/planner";
import type { ScenePlannerProvider } from "./types";

export class RuleBasedPlanner implements ScenePlannerProvider {
  readonly name = "rule-based";
  async plan(script: string, opts: { id?: string; cast?: string[] } = {}) {
    return planFromText(script, { id: opts.id, defaultCast: opts.cast });
  }
}
