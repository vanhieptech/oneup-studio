/**
 * Plain-text script format ("comic script"), parsed deterministically by the rule-based planner.
 *
 *   # title: Clip 01 story
 *   @video 1080x1920 30fps light week=1 clip=clip-01
 *   @cast hiep omi
 *
 *   == b01-goal | 4s | desk | medium | cut
 *   NARRATION: Mục tiêu: TOEIC 700
 *   CAPTION: My study plan… "tomorrow." [6]
 *   hiep (sitting, typing, focused): Kế hoạch học của mình là…
 *   hiep (happy): "**Mai học.**"
 *   hiep (thought): Thôi… mai học.
 *   SFX: pop @2.0
 *
 * Scene header: `== id | duration | background | framing | transition[:seconds]` (only id is required).
 * Dialogue line: `<characterId> (<tags>): text`; tags may be any pose/action/expression or speech|thought|shout.
 * Lines without explicit timing are spread evenly through the scene in order.
 */
export const TEXT_FORMAT_DOC = "see src/scenes/textFormat.ts";

export interface RawLine { speaker: string; tags: string[]; text: string }
export interface RawScene {
  id: string; duration?: number; background?: string; framing?: string; transition?: string; transitionDuration?: number;
  narration?: string; caption?: { text: string; highlight: number[] }; lines: RawLine[]; sfx: { name: string; at: number }[];
}
export interface RawScript { title?: string; video: Record<string, unknown>; meta: Record<string, unknown>; cast: string[]; scenes: RawScene[]; plain: string[] }

export function parseTextScript(src: string): RawScript {
  const out: RawScript = { video: {}, meta: {}, cast: [], scenes: [], plain: [] };
  let cur: RawScene | null = null;
  const lines = src.split(/\r?\n/);
  lines.forEach((raw, n) => {
    const line = raw.trim();
    if (!line || line.startsWith("//")) return;
    let m: RegExpMatchArray | null;
    if ((m = line.match(/^#\s*title:\s*(.+)$/i))) { out.title = m[1]; return; }
    if (line.startsWith("@video")) {
      for (const tok of line.split(/\s+/).slice(1)) {
        if ((m = tok.match(/^(\d+)x(\d+)$/))) { out.video.width = +m[1]; out.video.height = +m[2]; }
        else if ((m = tok.match(/^(\d+)fps$/))) out.video.fps = +m[1];
        else if (tok === "light" || tok === "dark") out.video.theme = tok;
        else if ((m = tok.match(/^week=(\d+)$/))) out.meta.week = +m[1];
        else if ((m = tok.match(/^clip=(.+)$/))) out.meta.clip = m[1];
        else throw new Error(`line ${n + 1}: unknown @video token "${tok}"`);
      }
      return;
    }
    if (line.startsWith("@cast")) { out.cast = line.split(/\s+/).slice(1); return; }
    if (line.startsWith("==")) {
      const parts = line.slice(2).split("|").map((s) => s.trim());
      const [id, dur, bg, framing, tr] = parts;
      if (!id) throw new Error(`line ${n + 1}: scene header needs an id ("== my-scene | 4s")`);
      cur = { id, lines: [], sfx: [] };
      if (dur) { const d = parseFloat(dur); if (Number.isNaN(d)) throw new Error(`line ${n + 1}: bad duration "${dur}"`); cur.duration = d; }
      if (bg) cur.background = bg;
      if (framing) cur.framing = framing;
      if (tr) { const [type, secs] = tr.split(":"); cur.transition = type; if (secs) cur.transitionDuration = parseFloat(secs); }
      out.scenes.push(cur);
      return;
    }
    if (!cur) { out.plain.push(line); return; }
    const scene: RawScene = cur;
    if ((m = line.match(/^NARRATION:\s*(.+)$/i))) { scene.narration = m[1]; return; }
    if ((m = line.match(/^CAPTION:\s*(.+?)(?:\s*\[([\d,\s]+)\])?$/i))) { scene.caption = { text: m[1], highlight: m[2] ? m[2].split(",").map((x) => +x.trim()) : [] }; return; }
    if ((m = line.match(/^SFX:\s*(\S+)\s*@\s*([\d.]+)s?$/i))) { scene.sfx.push({ name: m[1], at: +m[2] }); return; }
    if ((m = line.match(/^([a-z][\w-]*)\s*(?:\(([^)]*)\))?\s*:\s*(.+)$/i))) {
      scene.lines.push({ speaker: m[1].toLowerCase(), tags: (m[2] ?? "").split(/[,\s]+/).filter(Boolean).map((x) => x.toLowerCase()), text: m[3] });
      return;
    }
    throw new Error(`line ${n + 1}: cannot parse "${line}". Expected "speaker (tags): text", NARRATION:, CAPTION:, SFX: or a "== scene" header`);
  });
  return out;
}
