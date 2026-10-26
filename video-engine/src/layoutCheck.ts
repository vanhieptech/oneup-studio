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
      if (d.bubble === false) continue; // v18: no bubble drawn
      const c = chars.find((x: { id: string }) => x.id === d.speaker); const ax = c ? c.x : d.anchor ? d.anchor[0] : 540; const ay = Math.max(c ? c.headY : d.anchor ? d.anchor[1] : 672, 420);
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
    // L-033 Reels (RR round 2, 3d8f43d): layout "reels" draws the EN caption in a fixed narrow box x 60–640 (+8 px shadow → 648), top 1000,
    // bottom = 1056 + 68·lines (border + padding + 10 px shadow). Thầy (after the camera push) and every prop need ≥16 px from it, and Thầy ≥16 px from the frame edge x 1046.
    if (plan.video?.layout === "reels" && sc.id !== "endcard") {
      const M = 16, push = 1 + (sc.camera?.push ?? 0), cx = 540, cy = fr.groundY - 320;
      const proj = (b: Box): Box => ({ ...b, x0: cx + (b.x0 - cx) * push, x1: cx + (b.x1 - cx) * push, y0: cy + (b.y0 - cy) * push, y1: cy + (b.y1 - cy) * push });
      const segs: { text: string; highlight?: number[] }[] = sc.caption ? (sc.caption.segments?.length ? sc.caption.segments : [sc.caption]) : [];
      const lines = (txt: string, hl: number[] = []) => { let n = 1, w = 0; txt.split(/\s+/).filter(Boolean).forEach((wd, i) => { const ww = wd.length * 24.5 + (hl.includes(i) ? 32 : 0); if (w && w + 14 + ww > 516) { n++; w = ww; } else w += (w ? 14 : 0) + ww; }); return n; };
      for (const sg of segs) {
        const cap: Box = { x0: 60, y0: 1000, x1: 648, y1: 1056 + 68 * lines(sg.text, sg.highlight), label: "reels caption" };
        const near = (b: Box) => !(b.x1 + M <= cap.x0 || b.x0 - M >= cap.x1 || b.y1 + M <= cap.y0 || b.y0 - M >= cap.y1);
        chars.forEach((c: { x: number; headY: number; id: string }) => { const cb = proj(charBox(c.x, c.headY, fr.groundY, fr.scale, c.id));
          if (near(cb)) msgs.push(`reels caption «${sg.text}» within ${M}px of ${c.id} (char x ${Math.round(cb.x0)}–${Math.round(cb.x1)})`); });
        (sc.props ?? []).forEach((p: never, i: number) => { const b = propBox(p, i); if (b && near(proj(b)) && (p as { kind: string }).kind !== "table") msgs.push(`reels caption «${sg.text}» within ${M}px of ${b.label}`); });
      }
      chars.forEach((c: { x: number; headY: number; id: string }) => { const cb = proj(charBox(c.x, c.headY, fr.groundY, fr.scale, c.id)); if (cb.x1 > 1046 - M) msgs.push(`${c.id} ${Math.round(1046 - cb.x1)}px from the right frame edge (reels, need ≥${M})`); });
    }
    if (msgs.length) { bad++; console.log(`✖ ${sc.id}: ${msgs.join(" · ")}`); } else console.log(`✔ ${sc.id}`);
  }
}
process.exit(bad ? 1 : 0);
