import { createHash } from "node:crypto";
import { execFileSync } from "node:child_process";
import { existsSync, readFileSync } from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";
import type { VideoPlan } from "../validation/schema";
import { defaultRegistry, type ProfileRegistry } from "../characters/registry";

const ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "../..");
const SCRIPT = path.resolve(ROOT, "../pipeline/tts/vieneu_tts.py");

export type VoiceJob = { scene: number; line: number; text: string; voice: string; emotion: string; out: string; key: string };

/** Bubble markup → spoken text: strip **bold**, curly quotes, ellipsis noise. */
export const spokenText = (t: string) => t.replace(/\*\*/g, "").replace(/[“”"]/g, "").replace(/…/g, ", ").replace(/\s+/g, " ").trim();

function emotionAt(plan: VideoPlan, si: number, speaker: string, at: number): string {
  const cue = plan.scenes[si].characters.find((c) => c.characterId === speaker);
  if (!cue) return "neutral";
  let e = cue.expression;
  for (const c of [...cue.expressionChanges].sort((a, b) => a.at - b.at)) if (c.at <= at + 0.05) e = c.value;
  return e;
}

/** Lines that need a synthetic voice: speaker profile declares a `voice` preset (Hiệp chibi + Omi, DL-030). Never cloned. */
export function collectVoiceJobs(plan: VideoPlan, registry: ProfileRegistry = defaultRegistry): VoiceJob[] {
  const jobs: VoiceJob[] = [];
  plan.scenes.forEach((s, si) => s.dialogue.forEach((d, li) => {
    const v = registry.get(d.speaker)?.voice;
    if (!v || d.style === "thought") return;
    const text = spokenText(d.text);
    const emotion = d.emotion ?? emotionAt(plan, si, d.speaker, d.start);
    const key = createHash("sha1").update(JSON.stringify([v.engine, v.preset, emotion, text, 1])).digest("hex").slice(0, 12);
    jobs.push({ scene: si, line: li, text, voice: v.preset, emotion, key, out: path.join(ROOT, "public/voice", key) });
  }));
  return jobs;
}

/** Runs VieNeu-TTS (cached by content hash) and returns a new plan with dialogue.audio filled in. */
export function voicePlan(plan: VideoPlan, opts: { registry?: ProfileRegistry; python?: string; log?: (s: string) => void } = {}): VideoPlan {
  const log = opts.log ?? console.log;
  const jobs = collectVoiceJobs(plan, opts.registry);
  if (!jobs.length) { log("voice: no synthetic-voice lines"); return plan; }
  const py = opts.python ?? process.env.VIENEU_PYTHON ?? "/workspace/tts-venv/bin/python";
  if (!existsSync(py)) throw new Error(`voice: VieNeu python not found at ${py}. Install: python3 -m venv tts-venv && tts-venv/bin/pip install vieneu "onnxruntime==1.22.1" (see video-engine/README.md#voice). Set VIENEU_PYTHON.`);
  const cached = jobs.filter((j) => existsSync(j.out + ".wav")).length;
  log(`voice: ${jobs.length} line(s), ${cached} cached, synthesizing ${jobs.length - cached} with VieNeu-TTS…`);
  execFileSync(py, [SCRIPT, JSON.stringify({ fps: plan.video.fps, jobs: jobs.map(({ text, voice, emotion, out }) => ({ text, voice, emotion, out })) })], { stdio: ["ignore", "pipe", "inherit"] });
  const out: VideoPlan = structuredClone(plan);
  for (const j of jobs) {
    const meta = JSON.parse(readFileSync(j.out + ".json", "utf8"));
    const d = out.scenes[j.scene].dialogue[j.line];
    d.audio = { src: `voice/${j.key}.wav`, duration: meta.duration, envelope: meta.envelope, engine: meta.engine };
    d.emotion = j.emotion;
    d.end = Math.max(d.end, +(d.start + meta.duration + 0.2).toFixed(2)); // bubble stays up while Omi talks
    log(`voice: ${out.scenes[j.scene].id} "${j.text.slice(0, 40)}" [${j.emotion}] ${meta.duration}s`);
  }
  return out;
}
