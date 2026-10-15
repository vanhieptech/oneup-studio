/** L-033: collision-aware layout. Shared by DialogueBubble placement (SceneRenderer) and `cli.ts layout-check`.
 *  All boxes are design px (1080 wide), computed at camera push = 1 (start of scene). */
export type Box = { x0: number; y0: number; x1: number; y1: number; label: string };
export type PropLike = { kind: string; x?: number; y?: number; s?: number; text?: string; words?: string[]; at?: number; until?: number; dropAt?: number[] };

/** breathing room around props (pop/wobble/rotation + bubble shadow) */
export const PAD = 36;
export const SAFE = { top: 150, bottom: 1460 /* caption band starts at H*0.775 ≈ 1488 */, left: 60, right: 1020 };

const local = (p: PropLike): [number, number, number, number] | null => {
  switch (p.kind) {
    case "laptop": return [-370, -360, 370, 46];
    case "phone": return [-170, -180, 170, 225];
    case "calendar": return [-210, -262, 270, 222];
    case "cloud": return [-240, -230, 240, 70 + Math.max(0, (p.words?.length ?? 1) - 1) * 104 + 40];
    case "sign": { const w = Math.max(320, (p.text ?? "?").length * 40 + 80); return [-w / 2, -100, w / 2, 40]; } // board only (post is thin)
    case "words": { const ws = p.words ?? []; const m = Math.max(1, ...ws.map((w) => w.length)); return [-m * 30 - 30, -58, m * 30 + 30, (ws.length - 1) * 120 + 42]; }
    default: return null; // vignette: full-screen tint, not an obstacle
  }
};
export const propBox = (p: PropLike, i = 0): Box | null => {
  const b = local(p); if (!b) return null; const s = p.s ?? 1, x = p.x ?? 540, y = p.y ?? 900, m = PAD;
  return { x0: x + b[0] * s - m, y0: y + b[1] * s - m, x1: x + b[2] * s + m, y1: y + b[3] * s + m, label: `${p.kind}#${i}${p.text ? `:${p.text}` : ""}` };
};
/** Character body box from head top to ground (chibi head ≈ ±175 at scale 1). */
export const charBox = (ax: number, headY: number, groundY: number, scale: number, id = "char"): Box =>
  ({ x0: ax - 175 * scale, y0: headY, x1: ax + 175 * scale, y1: groundY, label: id });

export const area = (a: Box, b: Box) => Math.max(0, Math.min(a.x1, b.x1) - Math.max(a.x0, b.x0)) * Math.max(0, Math.min(a.y1, b.y1) - Math.max(a.y0, b.y0));

export type BubbleLayout = { left: number; bottom: number; W: number; font: number; h: number; box: Box; overlap: number; hits: string[] };
const plain = (t: string) => t.replace(/\*\*/g, "");
export const bubbleSize = (text: string, font: number, Wmax = 800) => {
  const n = plain(text).length; const W = Math.min(Wmax, 170 + n * font * 0.46);
  const lines = Math.max(1, Math.ceil((n * font * 0.52) / (W - 80 - 16)));
  return { W, h: lines * font * 1.22 + 66 + 16 };
};
/** Pick the bubble rect (above-head default) that avoids obstacles; scans horizontal shifts, upward moves, smaller font. */
export const placeBubble = (text: string, anchorX: number, anchorY: number, side: -1 | 1, obstacles: Box[], baseFont = 56): BubbleLayout => {
  let best: BubbleLayout | null = null;
  const clampX = (l: number, W: number) => Math.max(SAFE.left, Math.min(SAFE.right - W, l));
  for (const font of [baseFont, baseFont - 6, baseFont - 12]) {
    const { W, h } = bubbleSize(text, font);
    const bottom0 = Math.min(anchorY - 70, SAFE.bottom);
    for (const dy of [0, -60, -120, -180, -260, -340, -440, -560]) {
      const bottom = bottom0 + dy; if (bottom - h < SAFE.top) continue;
      for (const dx of [side * 90, 0, -side * 90, side * 220, -side * 220, side * 400, -side * 400]) {
        const left = clampX(anchorX - W / 2 + dx, W);
        if (anchorX < left + 50 || anchorX > left + W - 50) continue; // tail must reach the speaker
        const box: Box = { x0: left, y0: bottom - h, x1: left + W, y1: bottom + 60, label: "bubble" };
        const hits = obstacles.filter((o) => area(box, o) > 400); const overlap = hits.reduce((s, o) => s + area(box, o), 0);
        const cost = overlap * 10 + Math.abs(dy) * 3 + Math.abs(dx) + (baseFont - font) * 400;
        const cand = { left, bottom, W, font, h, box, overlap, hits: hits.map((o) => o.label) };
        if (!best || cost < (best.overlap * 10 + Math.abs(best.bottom - bottom0) * 3 + Math.abs(best.left - clampX(anchorX - best.W / 2 + side * 90, best.W)) + (baseFont - best.font) * 400)) best = cand;
        if (overlap === 0 && dy === 0 && font === baseFont && dx === side * 90) return cand;
      }
    }
  }
  return best!;
};
export const sceneObstacles = (props: PropLike[] | undefined, chars: { x: number; headY: number; id: string }[], groundY: number, scale: number): Box[] => [
  ...(props ?? []).map((p, i) => propBox(p, i)).filter((b): b is Box => !!b),
  ...chars.map((c) => charBox(c.x, c.headY, groundY, scale, c.id)),
];
