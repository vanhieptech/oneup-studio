import { RuleBasedPlanner } from "./ruleBased";
import { OpenAICompatiblePlanner } from "./openaiCompatible";
import type { ScenePlannerProvider } from "./types";
export type { ScenePlannerProvider } from "./types";
export { RuleBasedPlanner, OpenAICompatiblePlanner };

/**
 * Picks a planner. LLM is used only when explicitly requested AND configured
 * (LLM_BASE_URL + LLM_MODEL, optional LLM_API_KEY). Otherwise the deterministic rule-based planner.
 */
export function getPlanner(env: Record<string, string | undefined> = process.env, wantLlm = false): ScenePlannerProvider {
  if (wantLlm && env.LLM_BASE_URL && env.LLM_MODEL) {
    return new OpenAICompatiblePlanner({ baseUrl: env.LLM_BASE_URL, model: env.LLM_MODEL, apiKey: env.LLM_API_KEY });
  }
  return new RuleBasedPlanner();
}

/** LLM with automatic fallback to rule-based on any error (network, invalid JSON, invalid plan). */
export async function planWithFallback(script: string, planner: ScenePlannerProvider, opts?: { id?: string; cast?: string[] }) {
  try {
    return { plan: await planner.plan(script, opts), provider: planner.name, fallback: false };
  } catch (e) {
    if (planner.name === "rule-based") throw e;
    const rb = new RuleBasedPlanner();
    return { plan: await rb.plan(script, opts), provider: rb.name, fallback: true, error: String(e) };
  }
}
