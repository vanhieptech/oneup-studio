import { createHash } from "node:crypto";
import { existsSync, mkdirSync, readdirSync, readFileSync, statSync } from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";
import type { VideoPlan } from "../validation/schema";

const ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "../..");

/** Finds a local Chrome/Chromium so rendering needs no download. Override with REMOTION_BROWSER. */
export function findBrowser(env = process.env): string | undefined {
  const c = [env.REMOTION_BROWSER, "/usr/bin/google-chrome", "/usr/bin/chromium", "/usr/bin/chromium-browser",
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"].filter(Boolean) as string[];
  return c.find((p) => existsSync(p));
}

function hashDir(dir: string, h = createHash("sha1")) {
  for (const name of readdirSync(dir).sort()) {
    const p = path.join(dir, name);
    const st = statSync(p);
    if (st.isDirectory()) hashDir(p, h);
    else { h.update(p); h.update(readFileSync(p)); }
  }
  return h;
}

/** Webpack bundle, cached by content hash of src/ + examples/ so batch renders reuse one bundle. */
export async function getBundle(log = console.log): Promise<string> {
  const h = hashDir(path.join(ROOT, "src"));
  hashDir(path.join(ROOT, "examples"), h);
  hashDir(path.join(ROOT, "public"), h); // voice WAVs live in public/voice
  const key = h.digest("hex").slice(0, 12);
  const out = path.join(ROOT, ".bundle-cache", key);
  if (existsSync(path.join(out, "index.html"))) { log(`bundle: reuse ${path.relative(ROOT, out)}`); return out; }
  const { bundle } = await import("@remotion/bundler");
  log("bundle: building…");
  mkdirSync(out, { recursive: true });
  return bundle({ entryPoint: path.join(ROOT, "src/index.ts"), outDir: out, publicDir: path.join(ROOT, "public") });
}

export async function renderPlan(plan: VideoPlan, outFile: string, opts: { serveUrl?: string; log?: (s: string) => void; concurrency?: number } = {}) {
  const log = opts.log ?? console.log;
  const { renderMedia, selectComposition } = await import("@remotion/renderer");
  const serveUrl = opts.serveUrl ?? (await getBundle(log));
  const browserExecutable = findBrowser() ?? null;
  const inputProps = { plan };
  const composition = await selectComposition({ serveUrl, id: "ComicVideo", inputProps, browserExecutable });
  mkdirSync(path.dirname(path.resolve(outFile)), { recursive: true });
  let last = -1;
  await renderMedia({
    serveUrl, composition, inputProps, codec: "h264", crf: 18, pixelFormat: "yuv420p", muted: !hasAudio(plan), audioCodec: "aac", audioBitrate: "192k",
    outputLocation: outFile, browserExecutable, concurrency: opts.concurrency ?? null,
    onProgress: ({ progress }) => { const p = Math.floor(progress * 10); if (p !== last) { last = p; log(`render ${plan.id}: ${p * 10}%`); } },
  });
  if (!existsSync(outFile) || statSync(outFile).size < 1000) throw new Error(`render finished but ${outFile} is missing or empty`);
  return { outFile, frames: composition.durationInFrames, fps: composition.fps, width: composition.width, height: composition.height };
}

export const hasAudio = (plan: VideoPlan) => plan.scenes.some((s) => s.dialogue.some((d) => d.audio));
