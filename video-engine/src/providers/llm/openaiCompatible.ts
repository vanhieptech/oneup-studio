import { ACTIONS, BACKGROUNDS, EXPRESSIONS, FRAMINGS, POSES, TRANSITIONS, type VideoPlanInput } from "../../validation/schema";
import { validatePlan, formatIssues } from "../../validation/validate";
import type { ScenePlannerProvider } from "./types";

/**
 * OPTIONAL. Any OpenAI-compatible /chat/completions endpoint (e.g. a local Ollama / llama.cpp server — free).
 * Uses global fetch, no SDK dependency. Output is schema-validated; invalid output throws (caller may fall back).
 */
export class OpenAICompatiblePlanner implements ScenePlannerProvider {
  readonly name: string;
  constructor(private cfg: { baseUrl: string; model: string; apiKey?: string; timeoutMs?: number }, private fetchImpl: typeof fetch = fetch) {
    this.name = `llm:${cfg.model}`;
  }

  systemPrompt(cast: string[]) {
    return [
      "You convert a short-video script into a JSON scene plan. Output ONLY JSON, no prose.",
      `Shape: {"version":1,"id":string,"video":{"width":1080,"height":1920,"fps":30,"theme":"light"|"dark"},"scenes":[{"id","duration"(s),"background":{"kind"},"camera":{"framing"},"transition":{"type","duration"},"characters":[{"characterId","x"(0..1),"pose","action","expression","expressionChanges":[{"at","value"}]}],"dialogue":[{"speaker","text","start","end","style":"speech"|"thought"|"shout"}],"caption"?:{"text","start","end"},"narration"?:{"text"}}]}`,
      `Characters: ${cast.join(", ")}. Expressions: ${EXPRESSIONS.join("/")}. Actions: ${ACTIONS.join("/")}. Poses: ${POSES.join("/")}.`,
      `Backgrounds: ${BACKGROUNDS.join("/")}. Framings: ${FRAMINGS.join("/")}. Transitions: ${TRANSITIONS.join("/")}.`,
      "Dialogue times are seconds relative to the scene and must stay inside the scene. Keep the script language. Never invent facts.",
    ].join("\n");
  }

  async plan(script: string, opts: { id?: string; cast?: string[] } = {}): Promise<VideoPlanInput> {
    const cast = opts.cast ?? ["hiep"];
    const ctrl = new AbortController();
    const timer = setTimeout(() => ctrl.abort(), this.cfg.timeoutMs ?? 60_000);
    try {
      const res = await this.fetchImpl(`${this.cfg.baseUrl.replace(/\/$/, "")}/chat/completions`, {
        method: "POST",
        signal: ctrl.signal,
        headers: { "content-type": "application/json", ...(this.cfg.apiKey ? { authorization: `Bearer ${this.cfg.apiKey}` } : {}) },
        body: JSON.stringify({
          model: this.cfg.model, temperature: 0, response_format: { type: "json_object" },
          messages: [{ role: "system", content: this.systemPrompt(cast) }, { role: "user", content: script }],
        }),
      });
      if (!res.ok) throw new Error(`LLM HTTP ${res.status}`);
      const body = (await res.json()) as { choices?: { message?: { content?: string } }[] };
      const text = body.choices?.[0]?.message?.content ?? "";
      const json = JSON.parse(text.replace(/^```(?:json)?|```$/gm, "").trim());
      if (opts.id) json.id = opts.id;
      const r = validatePlan(json);
      if (!r.ok) throw new Error("LLM produced an invalid plan:\n" + formatIssues(r.issues));
      return json;
    } finally {
      clearTimeout(timer);
    }
  }
}
