import { createHash } from "node:crypto";
import { existsSync, lstatSync, mkdirSync, readdirSync, readFileSync, rmSync, statSync, symlinkSync } from "node:fs";
import { createServer } from "node:net";
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

function ensurePublicLink(bundleOut: string) {
  const pubTarget = path.join(ROOT, "public");
  const pubLink = path.join(bundleOut, "public");
  try {
    if (lstatSync(pubLink).isSymbolicLink()) return;
    rmSync(pubLink, { recursive: true, force: true });
  } catch { /* does not exist yet */ }
  symlinkSync(pubTarget, pubLink, "dir");
}

function pruneBundleCache(keep = 2) {
  const base = path.join(ROOT, ".bundle-cache");
  if (!existsSync(base)) return;
  const dirs = readdirSync(base)
    .map((name) => {
      const p = path.join(base, name);
      try { const st = statSync(p); return st.isDirectory() ? { p, mtime: st.mtimeMs } : null; } catch { return null; }
    })
    .filter((x): x is { p: string; mtime: number } => Boolean(x))
    .sort((a, b) => b.mtime - a.mtime);
  for (const old of dirs.slice(keep)) rmSync(old.p, { recursive: true, force: true });
}

/** Webpack bundle, cached by content hash of src/ + package-lock.json only.
 *  public/ is symlinked so adding/updating voice WAVs never invalidates webpack. */
export async function getBundle(log = console.log): Promise<string> {
  const h = hashDir(path.join(ROOT, "src"));
  const lock = path.join(ROOT, "package-lock.json");
  if (existsSync(lock)) h.update(readFileSync(lock));
  const key = h.digest("hex").slice(0, 12);
  const out = path.join(ROOT, ".bundle-cache", key);
  if (existsSync(path.join(out, "index.html"))) {
    ensurePublicLink(out);
    log(`bundle: reuse ${path.relative(ROOT, out)}`);
    return out;
  }
  const { bundle } = await import("@remotion/bundler");
  log("bundle: building…");
  mkdirSync(out, { recursive: true });
  await bundle({ entryPoint: path.join(ROOT, "src/index.ts"), outDir: out, publicDir: null });
  ensurePublicLink(out);
  pruneBundleCache(2);
  return out;
}

function getFreePort(): Promise<number> {
  return new Promise((resolve, reject) => {
    const srv = createServer();
    srv.unref();
    srv.on("error", reject);
    srv.listen(0, "127.0.0.1", () => {
      const addr = srv.address();
      const port = typeof addr === "object" && addr ? addr.port : 3000;
      srv.close(() => resolve(port));
    });
  });
}

export async function renderPlan(plan: VideoPlan, outFile: string, opts: { serveUrl?: string; log?: (s: string) => void; concurrency?: number; crf?: number; scale?: number } = {}) {
  const log = opts.log ?? console.log;
  const { renderMedia, selectComposition } = await import("@remotion/renderer");
  const serveUrl = opts.serveUrl ?? (await getBundle(log));
  const browserExecutable = findBrowser() ?? null;
  const inputProps = { plan };
  const port = await getFreePort();
  const composition = await selectComposition({ serveUrl, id: "ComicVideo", inputProps, browserExecutable, port });
  mkdirSync(path.dirname(path.resolve(outFile)), { recursive: true });
  let last = -1;
  const renderPort = await getFreePort();
  await renderMedia({
    serveUrl, composition, inputProps, codec: "h264", crf: opts.crf ?? 18, scale: opts.scale ?? 1, pixelFormat: "yuv420p", muted: !hasAudio(plan), audioCodec: "aac", audioBitrate: "192k",
    outputLocation: outFile, browserExecutable, concurrency: opts.concurrency ?? null, port: renderPort,
    onProgress: ({ progress }) => { const p = Math.floor(progress * 10); if (p !== last) { last = p; log(`render ${plan.id}: ${p * 10}%`); } },
  });
  if (!existsSync(outFile) || statSync(outFile).size < 1000) throw new Error(`render finished but ${outFile} is missing or empty`);
  return { outFile, frames: composition.durationInFrames, fps: composition.fps, width: Math.round(composition.width * (opts.scale ?? 1)), height: Math.round(composition.height * (opts.scale ?? 1)) };
}

export const hasAudio = (plan: VideoPlan) => plan.scenes.some((s) => s.dialogue.some((d) => d.audio));
