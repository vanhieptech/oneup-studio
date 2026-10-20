#!/usr/bin/env tsx
/** Render selected frames of a plan as PNG stills (fast visual QA without a full render).
 *  usage: npx tsx src/stills.ts plan.voiced.json outDir t1 t2 ... (seconds) [--layout reels] */
import { readFileSync, mkdirSync } from "node:fs";
import path from "node:path";
import { getBundle, findBrowser } from "./rendering/render";
import { VideoPlanSchema } from "./validation/schema";
const a = process.argv.slice(2); const li = a.indexOf("--layout"); const layout = li >= 0 ? a.splice(li, 2)[1] : undefined;
const [planF, outDir, ...ts] = a;
const raw = JSON.parse(readFileSync(planF, "utf8")); if (layout) raw.video.layout = layout;
const plan = VideoPlanSchema.parse(raw);
(async () => {
  const { renderStill, selectComposition } = await import("@remotion/renderer");
  const serveUrl = await getBundle(); const browserExecutable = findBrowser() ?? null; const inputProps = { plan };
  const composition = await selectComposition({ serveUrl, id: "ComicVideo", inputProps, browserExecutable });
  mkdirSync(outDir, { recursive: true });
  for (const t of ts) { const frame = Math.min(composition.durationInFrames - 1, Math.round(Number(t) * plan.video.fps));
    const out = path.join(outDir, `at-${Number(t).toFixed(2).padStart(5, "0")}s.png`);
    await renderStill({ serveUrl, composition, inputProps, frame, output: out, browserExecutable, scale: 0.5 }); console.log(out); }
})();
