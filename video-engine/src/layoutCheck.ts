#!/usr/bin/env tsx
/** L-033 layout check: fails (exit 1) when a dialogue bubble (as placed by placeBubble) intersects a prop/sign/character box,
 *  or a prop covers a character. Usage: npx tsx src/layoutCheck.ts plan.voiced.json... */
import { readFileSync } from "node:fs";
import { area, charBox, placeBubble, propBox, sceneObstacles, type Box } from "./composition/layout";
import { FRAMING } from "./composition/theme";
const HEAD: Record<string, Record<string, number>> = { "chibi-hiep": { standing: -500, sitting: -404 }, "liquid-omi": { standing: -300, sitting: -230 } };
const SIZE: Record<string, number> = { "chibi-hiep": 1, "liquid-omi": 1.35 };
const RIG: Record<string, string> = { hiep: "chibi-hiep", omi: "liquid-omi" };
let bad = 0;
for (const f of process.argv.slice(2)) {
  const plan = JSON.parse(readFileSync(f, "utf8"));
  for (const sc of plan.scenes) {
    const fr = (FRAMING as Record<string, { scale: number; groundY: number }>)[sc.camera?.framing ?? "medium"] ?? FRAMING.medium;
    const chars = (sc.characters ?? []).map((c: { characterId: string; x: number; pose?: string }) => {
      const rig = RIG[c.characterId] ?? "chibi-hiep"; return { x: c.x * 1080, headY: fr.groundY + (HEAD[rig][c.pose ?? "standing"] ?? -480) * fr.scale * SIZE[rig], id: c.characterId };
    });
    const obs = sceneObstacles(sc.props, chars, fr.groundY, fr.scale);
    const msgs: string[] = [];
    for (const d of sc.dialogue ?? []) {
      const c = chars.find((x: { id: string }) => x.id === d.speaker); const ax = c ? c.x : 540; const ay = Math.max(c ? c.headY : 672, 420);
      const L = placeBubble(d.text, ax, ay, ax > 540 ? -1 : 1, obs);
      if (L.overlap > 0) msgs.push(`bubble ∩ ${L.hits.join(", ")} (${Math.round(L.overlap)} px²)`);
    }
    (sc.props ?? []).forEach((p: never, i: number) => { const b = propBox(p, i); if (!b) return;
      chars.forEach((c: { x: number; headY: number; id: string }) => { const cb: Box = charBox(c.x, c.headY, fr.groundY, fr.scale, c.id); const a = area(b, cb);
        // head zone only (top 55% of body) — props at the feet/desk are fine
        const head: Box = { ...cb, y1: cb.y0 + (cb.y1 - cb.y0) * 0.55 }; if (area(b, head) > 2500) msgs.push(`${b.label} covers ${c.id} head (${Math.round(area(b, head))} px²)`); void a; }); });
    // L-038: text props (sign/words/cloud/calendar) must stay above the caption band (Caption top = 0.775·H) and must not repeat the narration
    const CAP_Y = 1920 * 0.775 - 20;
    (sc.props ?? []).forEach((p: { kind?: string; text?: string; words?: string[] }, i: number) => { const b = propBox(p as never, i); if (!b || !["sign", "words", "cloud", "calendar"].includes(p.kind ?? "")) return;
      const hid = Math.max(0, b.y1 - Math.max(b.y0, CAP_Y)) * Math.max(0, b.x1 - b.x0); const tot = (b.y1 - b.y0) * (b.x1 - b.x0);
      if (tot > 0 && hid / tot > 0.15) msgs.push(`${b.label} behind caption box (${Math.round(100 * hid / tot)}%)`);
      const txt = (p.text ?? (p.words ?? []).join(" ")).trim(); if (sc.narration?.text && txt && txt === sc.narration.text.trim()) msgs.push(`${b.label} duplicates narration «${txt}»`); });
    if (msgs.length) { bad++; console.log(`✖ ${sc.id}: ${msgs.join(" · ")}`); } else console.log(`✔ ${sc.id}`);
  }
}
process.exit(bad ? 1 : 0);
