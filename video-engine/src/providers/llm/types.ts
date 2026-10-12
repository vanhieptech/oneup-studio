import type { VideoPlanInput } from "../../validation/schema";

/** Vendor-agnostic scene planner. Rendering never depends on which implementation produced the plan. */
export interface ScenePlannerProvider {
  readonly name: string;
  plan(script: string, opts?: { id?: string; cast?: string[] }): Promise<VideoPlanInput>;
}
