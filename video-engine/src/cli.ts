#!/usr/bin/env tsx
/**
 * oneup video-engine CLI
 *   validate <plan.json|script.txt>...            validate only (fast, no browser)
 *   plan <script.txt> [--out plan.json] [--llm]   script → JSON scene plan (rule-based unless --llm + env configured)
 *   render <plan.json|script.txt>... [--out-dir out] [--llm]   validate all, then render each to MP4 (one shared bundle)
 *   frames <video.mp4> [--every 1] [--out dir]    extract frames + contact sheet (needs ffmpeg) for visual QA
 */
import { readFileSync, writeFileSync, mkdirSync } from "node:fs";
import { execFileSync } from "node:child_process";
import path from "node:path";
import { validatePlan, formatIssues } from "./validation/validate";
import { getPlanner, planWithFallback } from "./providers/llm";
import { getBundle, renderPlan } from "./rendering/render";
import type { VideoPlan } from "./validation/schema";

const args = process.argv.slice(2);
const cmd = args[0];
const flag = (name: string, dflt?: string) => { const i = args.indexOf(name); return i >= 0 ? args[i + 1] : dflt; };
const files = args.slice(1).filter((a, i, all) => !a.startsWith("--") && !(i > 0 && all[i - 1].startsWith("--") && all[i - 1] !== "--llm"));
const useLlm = args.includes("--llm");

async function load(file: string): Promise<{ plan?: VideoPlan; ok: boolean; report: string }> {
  const text = readFileSync(file, "utf8");
  let input: unknown;
  let note = "";
  if (file.endsWith(".json")) {
    try { input = JSON.parse(text); } catch (e) { return { ok: false, report: `✖ ${file}: invalid JSON: ${(e as Error).message}` }; }
  } else {
    try {
      const r = await planWithFallback(text, getPlanner(process.env, useLlm), { id: path.basename(file).replace(/\.\w+$/, "") });
      input = r.plan; note = ` (planned by ${r.provider}${r.fallback ? ", LLM failed → fallback" : ""})`;
    } catch (e) { return { ok: false, report: `✖ ${file}: ${(e as Error).message}` }; }
  }
  const r = validatePlan(input);
  const issues = r.issues.length ? "\n" + formatIssues(r.issues).replace(/^/gm, "   ") : "";
  return r.ok ? { ok: true, plan: r.plan, report: `✔ ${file}${note}: ${r.plan.scenes.length} scenes, ${r.plan.scenes.reduce((a, s) => a + s.duration, 0).toFixed(2)}s${issues}` }
              : { ok: false, report: `✖ ${file}${note}: invalid plan${issues}` };
}

async function main() {
  if (!cmd || cmd === "help" || cmd === "--help") { console.log(readFileSync(new URL(import.meta.url), "utf8").split("*/")[0]); return; }
  if (cmd === "frames") {
    const video = files[0];
    const out = flag("--out", video.replace(/\.mp4$/, "") + "-frames")!;
    const every = Number(flag("--every", "1"));
    mkdirSync(out, { recursive: true });
    execFileSync("ffmpeg", ["-loglevel", "error", "-y", "-i", video, "-vf", `fps=1/${every},scale=360:-1`, path.join(out, "f%03d.png")]);
    const dur = Number(execFileSync("ffprobe", ["-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", video]).toString());
    const n = Math.ceil(dur / every), cols = Math.min(8, n), rows = Math.ceil(n / cols);
    execFileSync("ffmpeg", ["-loglevel", "error", "-y", "-i", video, "-vf", `fps=1/${every},scale=240:-1,tile=${cols}x${rows}:padding=8:color=0xCCCCCC`, "-frames:v", "1", path.join(out, "contact-sheet.png")]);
    console.log(`frames → ${out} (contact-sheet.png)`);
    return;
  }
  if (!files.length) throw new Error(`usage: ${cmd} <file>...`);
  const loaded = await Promise.all(files.map(load));
  loaded.forEach((l) => console.log(l.report));
  const bad = loaded.filter((l) => !l.ok).length;
  if (bad) { console.error(`\n${bad} file(s) invalid — nothing rendered.`); process.exit(1); }

  if (cmd === "validate") return;
  if (cmd === "plan") {
    const out = flag("--out");
    const json = JSON.stringify(loaded[0].plan, null, 2);
    if (out) { writeFileSync(out, json + "\n"); console.log(`plan → ${out}`); } else console.log(json);
    return;
  }
  if (cmd === "render") {
    const outDir = flag("--out-dir", "out")!;
    const serveUrl = await getBundle();
    for (const l of loaded) {
      const outFile = path.join(outDir, `${l.plan!.id}.mp4`);
      const t0 = Date.now();
      try {
        const r = await renderPlan(l.plan!, outFile, { serveUrl });
        console.log(`✔ ${outFile}: ${r.width}x${r.height} ${r.fps}fps ${r.frames} frames in ${((Date.now() - t0) / 1000).toFixed(1)}s`);
      } catch (e) {
        console.error(`✖ render failed for ${l.plan!.id}: ${(e as Error).message}`);
        process.exitCode = 1;
      }
    }
    return;
  }
  throw new Error(`unknown command "${cmd}" (validate | plan | render | frames)`);
}
main().catch((e) => { console.error(e instanceof Error ? e.message : e); process.exit(1); });
