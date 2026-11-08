#!/usr/bin/env python3
"""L-033 per-frame clearance scan for the Reels/Shorts cut (layout "reels"), every frame, not samples (Rule Reviewer round 2, 3d8f43d).
Inputs are two Remotion renders of the same plan: WITH captions and WITHOUT (scene.caption removed). Their difference is the exact caption
mask (plate + ink border + drop shadow + text, incl. pop-in scale/fade), so nothing is guessed from colours.
  caption clearance = background px between the caption mask and the nearest ink pixel (gray < 120) of the caption-less frame
                      (Thầy, hourglass, books, any prop; 8-neighbour / Chebyshev distance; an object under the caption = −1)
  right edge        = background px between Thầy's rightmost ink (rows 960–1365: head top ≈1040 … desk, below the speech bubbles; x 700–1045) and the ink frame (x 1046), cast scenes
  --final reels.mp4 = also checks that every delivered frame after the 0.5s cover is the scanned render (mean |Δ| < 4, grain only)
Pass: caption ≥ MIN and right edge ≥ MIN on every frame (MIN 16).
Usage: scan-reels-clearance.py <with-captions.mp4> <no-captions.mp4> <plan-reels.json> [--final reels.mp4 --cover 0.5] [--min 16] [--dump out.json]"""
import json, subprocess, sys
import numpy as np
A, B, planp = sys.argv[1:4]
arg = lambda k, d: type(d)(sys.argv[sys.argv.index(k) + 1]) if k in sys.argv else d
MIN, FINAL, COVER, DUMP = arg("--min", 16), arg("--final", ""), arg("--cover", 0.5), arg("--dump", "")
W, H, FPS, INK, FX0, FX1, D = 1080, 1920, 30, 120, 34, 1046, 64
plan = json.load(open(planp)); starts = []; acc = 0.0
for s in plan["scenes"]: starts.append((acc, s["id"], bool(s.get("characters")) and s["id"] != "endcard")); acc += s["duration"]
def scene(t):
    r = starts[0]
    for x in starts:
        if t >= x[0] - 1e-6: r = x
    return r
def reader(f): return subprocess.Popen(["ffmpeg", "-loglevel", "error", "-i", f, "-f", "rawvideo", "-pix_fmt", "gray", "-"], stdout=subprocess.PIPE)
def frames(p):
    while True:
        b = p.stdout.read(W * H)
        if len(b) < W * H: return
        yield np.frombuffer(b, np.uint8).reshape(H, W)
def dil(m, r):  # square (Chebyshev) dilation by r, separable, doubling shifts
    for ax in (0, 1):
        out = m.copy(); step = 1; done = 0  # OR with a copy shifted ±s grows the reach by s; s = 1, 2, 4, … until r
        while done < r:
            s = min(step, r - done)
            sh = np.zeros_like(out)
            if ax == 0: sh[s:] |= out[:-s]; sh[:-s] |= out[s:]
            else: sh[:, s:] |= out[:, :-s]; sh[:, :-s] |= out[:, s:]
            out = out | sh; done += s; step *= 2
        m = out
    return m
pa, pb = reader(A), reader(B); pf = reader(FINAL) if FINAL else None
gf = frames(pf) if pf else None
if gf:
    for _ in range(int(round(COVER * FPS))): next(gf)
rows = []; maxdiff = 0.0
for f, (a, b) in enumerate(zip(frames(pa), frames(pb))):
    t = f / FPS; st, sid, cast = scene(t); rec = {"f": f, "t": round(t, 3), "reels_t": round(t + COVER, 3), "beat": sid, "cap": None, "right": None}
    if gf is not None:
        c = next(gf, None)
        if c is not None: md = float(np.abs(c.astype(np.int16) - a.astype(np.int16)).mean()); maxdiff = max(maxdiff, md); rec["final_d"] = round(md, 2)
    ink = b < INK; ink[:, :FX0] = False; ink[:, FX1:] = False
    if cast:
        band = ink[960:1366, 700:FX1]; cols = np.where(band.any(axis=0))[0]
        rec["right"] = int(FX1 - 1 - (700 + cols.max())) if len(cols) else 999
    # caption zone only (Reels caption box lives at x 60–648, y 1000–1260): outside it the two encodes differ by codec noise/ambient motion.
    # Plate white 247 vs wall 227 is below the threshold, so the mask = ink border + shadow + words (ink vs wall Δ≈210) → its outer contour is the box edge.
    m = np.zeros((H, W), bool); z = (slice(990, 1278), slice(50, 662))  # the CSS box (60–640 × 1000–1250) + 6px border + 8/10px shadow, nothing else can be caption
    m[z] = np.abs(a[z].astype(np.int16) - b[z].astype(np.int16)) > 60
    if m.sum() > 1500:
        # keep only the plate: its top/bottom border+shadow rows are ≥200 px long and its side borders ≥40 px tall; a stray object diff
        # (two encodes of a moving prop) is narrower than that and is cut away instead of growing the box
        rr_ = np.where(m.sum(axis=1) >= 200)[0]; cc_ = np.where(m.sum(axis=0) >= 40)[0]
        if len(rr_) and len(cc_):
            keep = np.zeros_like(m); keep[rr_[0]:rr_[-1] + 1, cc_[0]:cc_[-1] + 1] = True; m &= keep
        ys, xs = np.nonzero(m); y0, y1, x0, x1 = ys.min(), ys.max(), xs.min(), xs.max()
        rec["box"] = [int(x0), int(y0), int(x1), int(y1)]
        a0, a1, b0, b1 = max(0, x0 - D), min(W, x1 + D + 1), max(0, y0 - D), min(H, y1 + D + 1)
        mm, kk = m[b0:b1, a0:a1], ink[b0:b1, a0:a1]
        if (mm & kk).any(): rec["cap"] = -1
        else:
            lo, hi = 0, D  # smallest r with dil(mm, r) ∩ ink ≠ ∅ → clearance r−1
            if not (dil(mm, D) & kk).any(): rec["cap"] = D
            else:
                while lo < hi:
                    mid = (lo + hi) // 2
                    if (dil(mm, mid) & kk).any(): hi = mid
                    else: lo = mid + 1
                rec["cap"] = lo - 1
                ky, kx = np.nonzero(dil(mm, lo) & kk); rec["near"] = [int(kx[0] + a0), int(ky[0] + b0)]
    rows.append(rec)
cap = [r for r in rows if r["cap"] is not None]; rgt = [r for r in rows if r["right"] is not None]
bad = [r for r in rows if (r["cap"] is not None and r["cap"] < MIN) or (r["right"] is not None and r["right"] < MIN)]
print(f"frames scanned {len(rows)} (render t 0–{rows[-1]['t']}s = Reels {COVER}–{rows[-1]['reels_t']}s) · caption on {len(cap)} · cast frames {len(rgt)}")
if FINAL: print(f"delivered Reels frames vs scanned render: max mean |Δ| {maxdiff:.2f} (grain only {'✓' if maxdiff < 4 else '✖'})")
if cap:
    m = min(cap, key=lambda r: r["cap"]); print(f"caption clearance min {m['cap']} px · Reels {m['reels_t']}s {m['beat']} · caption bbox {m['box']} · nearest ink {m.get('near')}")
    print(f"caption bbox (incl. border+shadow): right x ≤ {max(r['box'][2] for r in cap)}, bottom y ≤ {max(r['box'][3] for r in cap)}")
if rgt:
    m = min(rgt, key=lambda r: r["right"]); print(f"right edge clearance min {m['right']} px · Reels {m['reels_t']}s {m['beat']}")
print("per beat (Reels time): caption min · right-edge min")
for st, sid, cast in starts:
    rr = [r for r in rows if r["beat"] == sid]
    if not rr: continue
    cs = [r["cap"] for r in rr if r["cap"] is not None]; rs = [r["right"] for r in rr if r["right"] is not None]
    print(f"  {sid:8s} {rr[0]['reels_t']:6.2f}–{rr[-1]['reels_t']:6.2f}s  caption {min(cs) if cs else '—':>4} · right {min(rs) if rs else '—':>4}")
print(f"{'PASS' if not bad else 'FAIL'}: {len(bad)} frame(s) under {MIN}px")
for r in bad[:30]: print("  ✖", r)
if DUMP: json.dump(rows, open(DUMP, "w"))
sys.exit(1 if bad or (FINAL and maxdiff >= 4) else 0)
