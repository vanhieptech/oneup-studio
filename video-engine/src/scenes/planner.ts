import { ACTIONS, EXPRESSIONS, POSES, type VideoPlanInput } from "../validation/schema";
import { parseTextScript, type RawLine, type RawScene } from "./textFormat";

const has = <T extends string>(xs: readonly T[], v: string): v is T => (xs as readonly string[]).includes(v);
const round = (x: number) => Math.round(x * 100) / 100;

/** Reading-speed estimate: ~15 chars/s for Vietnamese bubbles, plus settle time. */
export const lineSeconds = (text: string) => Math.max(1.2, text.replace(/\*\*/g, "").length / 15 + 0.5);

/** Keyword/punctuation analyzer (VI + EN). Deterministic; only used when a line has no explicit tags. */
export function inferMood(text: string): { expression?: string; action?: string; style?: "speech" | "thought" | "shout" } {
  const t = text.toLowerCase();
  if (/(nghĩ|hmm|suy|đọc được|think|wonder)/.test(t)) return { expression: "focused", action: "thinking", style: "thought" };
  if (/(buồn|mệt|chán|tiếc|haizz|sad|tired)/.test(t)) return { expression: "sad" };
  if (/(sao vậy|hả\?|gì vậy|\?\s*$|why|what)/.test(t)) return { expression: "confused" };
  if (/(xong|ngon|tuyệt|yay|được rồi|done|nice)/.test(t)) return { expression: "happy", action: "reacting", style: "shout" };
  if (/!\s*$/.test(t)) return { expression: "surprised", style: "shout" };
  return {};
}

function sceneFromRaw(raw: RawScene, cast: string[]) {
  const speakers = [...new Set(raw.lines.map((l) => l.speaker).filter((s) => s !== "narrator"))];
  const chars = speakers.length ? speakers : cast.slice(0, 1);
  const lead = 0.5, gap = 0.12;
  const natural = raw.lines.reduce((a, l) => a + lineSeconds(l.text) + gap, lead + 0.4);
  const duration = round(raw.duration ?? Math.max(2.5, natural));
  const scale = Math.min(1, (duration - lead - 0.2) / Math.max(0.1, natural - lead - 0.4 + 1e-9));
  let t = lead;
  const dialogue: NonNullable<VideoPlanInput["scenes"][number]["dialogue"]> = [];
  const cues = new Map<string, { pose?: string; action?: string; expression?: string; expressionChanges: { at: number; value: string }[]; actionChanges: { at: number; value: string }[] }>();
  for (const c of chars) cues.set(c, { expressionChanges: [], actionChanges: [] });

  raw.lines.forEach((l: RawLine) => {
    const d = lineSeconds(l.text) * scale;
    const start = round(t), end = round(Math.min(duration - 0.05, t + d));
    t += d + gap;
    const cue = cues.get(l.speaker);
    const inferred = inferMood(l.text);
    let style: "speech" | "thought" | "shout" = inferred.style ?? "speech";
    let expression: string | undefined, action: string | undefined;
    for (const tag of l.tags) {
      if (tag === "speech" || tag === "thought" || tag === "shout") style = tag;
      else if (has(EXPRESSIONS, tag)) expression = tag;
      else if (has(ACTIONS, tag)) action = tag;
      else if (has(POSES, tag) && cue) cue.pose = tag;
      else throw new Error(`scene "${raw.id}": unknown tag "${tag}" on line "${l.text}". Use a pose (${POSES.join("/")}), action (${ACTIONS.join("/")}), expression (${EXPRESSIONS.join("/")}) or speech/thought/shout`);
    }
    if (!l.tags.length) { expression = inferred.expression; action = inferred.action; }
    if (cue) {
      const first = cue.expression === undefined; // the speaker's first line sets the initial state
      if (first) { cue.expression = expression ?? "neutral"; cue.action = action ?? "idle"; }
      else {
        if (expression) cue.expressionChanges.push({ at: start, value: expression });
        if (action) cue.actionChanges.push({ at: start, value: action });
      }
      dialogue.push({ speaker: l.speaker, text: l.text, start, end, style });
    }
  });
  const n = chars.length;
  return {
    id: raw.id,
    duration,
    background: { kind: raw.background ?? "paper" },
    camera: { framing: raw.framing ?? (n > 1 ? "wide" : "medium") },
    transition: { type: raw.transition ?? "cut", duration: raw.transitionDuration ?? 0.4 },
    narration: raw.narration ? { text: raw.narration, start: 0.2 } : undefined,
    caption: raw.caption ? { text: raw.caption.text, start: lead, highlight: raw.caption.highlight } : undefined,
    characters: chars.map((id, i) => {
      const c = cues.get(id)!;
      return {
        characterId: id, x: n === 1 ? 0.5 : round(0.28 + (0.46 * i) / (n - 1)), facing: (n > 1 && i === n - 1 ? "left" : "right") as "left" | "right",
        pose: c.pose ?? "standing", action: c.action ?? "idle", expression: c.expression ?? "neutral",
        expressionChanges: c.expressionChanges, actionChanges: c.actionChanges, enter: i > 0 ? ("rise" as const) : ("none" as const),
      };
    }),
    dialogue,
    sfx: raw.sfx,
  };
}

/** Prose with no scene headers: 1–2 sentences per scene, spoken by the first cast member. */
function prosesToScenes(plain: string[], cast: string[]): RawScene[] {
  const sentences = plain.join(" ").match(/[^.!?…]+[.!?…]*/g)?.map((s) => s.trim()).filter(Boolean) ?? [];
  const scenes: RawScene[] = [];
  for (let i = 0; i < sentences.length; i += 2) {
    scenes.push({ id: `scene-${scenes.length + 1}`, lines: sentences.slice(i, i + 2).map((text) => ({ speaker: cast[0], tags: [], text })), sfx: [], transition: i ? "fade" : "cut" });
  }
  return scenes;
}

export interface PlanOptions { id?: string; defaultCast?: string[] }

/** Deterministic rule-based script → scene plan (no network, no API key). */
export function planFromText(src: string, opts: PlanOptions = {}): VideoPlanInput {
  const raw = parseTextScript(src);
  const cast = raw.cast.length ? raw.cast : opts.defaultCast ?? ["hiep"];
  const scenes = raw.scenes.length ? raw.scenes : prosesToScenes(raw.plain, cast);
  if (!scenes.length) throw new Error("script is empty: add text or `== scene` headers");
  return {
    version: 1,
    id: opts.id ?? (raw.title ? raw.title.toLowerCase().normalize("NFD").replace(/[\u0300-\u036f]/g, "").replace(/đ/g, "d").replace(/[^a-z0-9]+/g, "-").replace(/^-|-$/g, "") : "script"),
    title: raw.title,
    meta: raw.meta,
    video: raw.video,
    scenes: scenes.map((s) => sceneFromRaw(s, cast)),
  };
}
