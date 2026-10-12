import { execFileSync } from "node:child_process";
import { existsSync, mkdtempSync } from "node:fs";
import { tmpdir } from "node:os";
import path from "node:path";
import { describe, expect, it } from "vitest";
import { renderPlan } from "../src/rendering/render";
import { assertValidPlan } from "../src/validation/validate";

/** Opt-in (slow, needs Chrome + ffmpeg): RENDER_E2E=1 npm test */
describe.skipIf(!process.env.RENDER_E2E)("e2e render", () => {
  it("renders a 1s plan to a real MP4 with non-blank frames", async () => {
    const plan = assertValidPlan({ id: "e2e", video: { width: 540, height: 960 }, scenes: [{ id: "a", duration: 1, characters: [{ characterId: "hiep", action: "talking", expression: "happy" }], dialogue: [{ speaker: "hiep", text: "Xin chào!", start: 0.1, end: 0.9 }] }] });
    const out = path.join(mkdtempSync(path.join(tmpdir(), "ve-")), "e2e.mp4");
    const r = await renderPlan(plan, out, { log: () => {} });
    expect(existsSync(out)).toBe(true);
    expect(r.frames).toBe(30);
    const probe = execFileSync("ffprobe", ["-v", "error", "-select_streams", "v:0", "-count_frames", "-show_entries", "stream=width,height,nb_read_frames", "-of", "csv=p=0", out]).toString().trim().replace(/,$/, "");
    expect(probe).toBe("540,960,30");
    // blank-frame check: luma std-dev of the middle frame must be well above a flat image
    const mean = execFileSync("ffmpeg", ["-v", "error", "-ss", "0.5", "-i", out, "-frames:v", "1", "-vf", "scale=1:1", "-f", "rawvideo", "-pix_fmt", "gray", "-"]);
    expect(mean[0]).toBeLessThan(245); // not an all-paper frame: ink character present
    expect(mean[0]).toBeGreaterThan(60); // not an all-black frame
  });
});
