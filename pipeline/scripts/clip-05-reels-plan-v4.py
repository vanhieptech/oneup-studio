#!/usr/bin/env python3
"""clip-05 v4: derive the Reels/Shorts plan (final/out/plan-reels.json) from final/plan-A.voiced.json (Rule Reviewer final F4, bb7423c).
Reels safe zone: captions y≈1000–1240 in a narrow left box x 60–640 (engine video.layout=reels), narration title y≥300.
Props that would sit under that caption box are moved:
  paper scenes (no cast): everything up DY=380; source/credit tags → y 1300 (under the caption box); window top-right
  room scenes: desk props left of x 700 shrink k=0.6 about the desk line y=1395 (still sit on the desk, top under ~1190);
               b01a (no cast) lifts the whole desk (table top 1250 → 960) with its pile/lamp; b08 calendar/chat/hand go up
  grid scenes (b02b/b07b/b07c, same angle kept across all three): Punnett sheet k=0.62 to (330, 760), clock under the caption box, pen remapped
  cast scenes (RR round 2, 3d8f43d): framing "reels" (Thầy ×0.835) at x .776; hourglass b02a/b05a s .33 standing on the desk (top ≥1268)
Usage: python3 pipeline/scripts/clip-05-reels-plan-v4.py"""
import json, os
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../content/clips/clip-05-hoc-mot-dem/final")
p = json.load(open(os.path.join(D, "plan-A.voiced.json")))
p["id"] = "clip-05-final-reels"; p["video"]["layout"] = "reels"
DY, K, DESK = 380, 0.6, 1395

def desk(pr, k=K, xmax=700):  # shrink a desk object about the desk line, keep x
    if pr.get("x", 0) > xmax: return
    f = lambda y: round(DESK - (DESK - y) * k, 1)
    if "y" in pr: pr["y"] = f(pr["y"])
    if "s" in pr: pr["s"] = round(pr["s"] * k, 3)
    if "size" in pr: pr["size"] = round(pr["size"] * k, 1)
    for a in ("rx", "ry"):
        if a in pr: pr[a] = round(pr[a] * k, 1)
    if "mv" in pr: pr["mv"] = [[t, x, f(y)] for t, x, y in pr["mv"]]

def penmap(pr, fn):
    pr["keys"] = [[t, *fn(x, y)] for t, x, y in pr["keys"]]

for s in p["scenes"]:
    bg, props, cast = s["background"]["kind"], s.get("props", []), s.get("characters") or []
    if s["id"] == "endcard": continue
    if cast:  # RR round 2 R1/R3: caption box outer edge x 648 (border+shadow) vs frame edge x 1046 → Thầy ×0.78 (framing "reels", scale 0.9, head ≈320px) at x .78,
        # camera push ≤0.02 (push grows the head outward); thought dots + «?» glyph off (they sit left of the head = under the caption box). Verified per frame by scan-reels-clearance.py
        s["camera"]["framing"] = "reels"; s["camera"]["push"] = min(s["camera"].get("push", 0), 0.02)
        for c in cast: c["x"] = 0.79 if c.get("action") == "thinking" else 0.78; c["emote"] = False  # thinking: hand at the chin sits left of the head → +11px
    if bg == "paper":
        for pr in props:
            k = pr["kind"]
            if k == "tag" and pr.get("font") == "en" and pr["y"] > 1350: pr["y"] = 1330; continue  # source line under the caption box (3-line box ends y 1260 → tag top ≥ 1276 after push)
            if k == "tag" and pr.get("y") == 1330 and s["id"].startswith("b03"): pr["y"] = 925; continue  # «Đọc 1 lần…» labels: bottom ≥16px above the caption box top (y 1000)
            if k == "groups3": pr["y"] = round(pr["y"] - DY - 25, 1); continue  # groups3 rides up with its labels
            if k == "tag" and pr.get("style") == "word" and pr["y"] <= 300 and pr.get("size", 0) >= 150: continue  # big «1»/«2»
            if k == "window": pr.update(wx=800, wy=130); continue
            if k == "tag" and pr["text"] == "+2 ngày": pr.update(x=910, y=90); continue
            if k == "paper" and s["id"] == "b03a": pr.update(y=330, s=0.42); continue
            if k == "lamp": pr["y"] = 300; continue
            if k == "rope": pr["a"] = [pr["a"][0], pr["a"][1] - DY]; pr["b"] = [pr["b"][0], pr["b"][1] - DY]; continue
            if "y" in pr: pr["y"] = round(pr["y"] - DY, 1)
    elif bg == "grid":
        kk, cx, cy, ox, oy = 0.62, 330, 1130, 330, 760
        m = lambda x, y: (round(ox + (x - cx) * kk, 1), round(oy + (y - cy) * kk, 1))
        for pr in props:
            if pr["kind"] == "punnett": pr.update(x=ox, y=oy, s=round(pr["s"] * kk, 3))
            elif pr["kind"] == "pen": penmap(pr, m); pr["len"] = round(pr.get("len", 150) * kk); 
            elif pr["kind"] == "wallclock": pr.update(x=150, y=1320, s=0.55)
            elif pr["kind"] == "qmark": pr.update(x=640, y=700, s=0.65)
    elif bg == "room":
        if s["id"] == "b01a":
            for pr in props:
                # narration title sits at y≈300–500 in reels → night window + clock go below it, pile shrinks onto the lifted desk
                if pr["kind"] == "table": pr.update(top=935, x0=20)  # desk edge ≥16px above the caption box (y 1000); front panel's left side under the frame border (was 15px left of the box)
                elif pr["kind"] == "textbooks": pr.update(x=420, y=913, s=0.7)
                elif pr["kind"] == "lamp": pr.update(x=715, y=921, s=0.7)
                elif pr["kind"] == "wallclock": pr.update(x=150, y=650, s=0.5)
                elif pr["kind"] == "window": pr.update(wx=600, wy=540, ww=230, wh=190)
            continue
        for pr in props:
            k = pr["kind"]
            if k == "hourglass" and s["id"] in ("b02a", "b05a"):  # RR R2: desk-standing, top ≥ 1268 (caption box outer bottom 1252 + 16); b05a no lift into the box
                hs = 0.33; hy = round(DESK - 180 * hs, 1); pr.update(x=470, y=hy, s=hs)
                if "mv" in pr: pr["mv"] = [[t, x, hy] for t, x, _ in pr["mv"]]
                continue
            if k in ("biobook", "hourglass", "exam", "paper", "ring"): desk(pr)
            elif k == "pen": penmap(pr, lambda x, y: (x, round(DESK - (DESK - y) * K, 1)) if x <= 700 else (x, y))
            elif k == "icon" and pr.get("name") == "tick": desk(pr)
            elif k == "tearpad" and s["id"] == "b01c": pr.update(y=800, s=0.7)
            elif k == "tearpad" and s["id"] == "b08": pr.update(x=200, y=470, s=0.6, mv=[[0, 200, 640], [0.35, 200, 470]])  # reels bubble sits y≈540–760
            elif k == "window" and s["id"] == "b08": pr["wy"] = 120
            elif k == "icon" and pr.get("name") == "chat": pr["y"] = 800
            elif k == "icon" and pr.get("name") == "hand": pr.update(y=930, size=80)
os.makedirs(os.path.join(D, "out"), exist_ok=True)
json.dump(p, open(os.path.join(D, "out/plan-reels.json"), "w"), ensure_ascii=False, indent=1)
print("→ final/out/plan-reels.json")
