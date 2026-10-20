#!/usr/bin/env python3
"""clip-04 v18: derive the Reels/Shorts plan (final/out/plan-reels.json) from final/plan-A.voiced.json.
Reels safe zone: captions y≈1000–1240 (engine: video.layout=reels → narrow left caption box x 60–640),
title y≥300. Props that would sit under the caption band are moved above it:
  closeup: paper/card/pen/tag −200 · halves: everything but window −200, window wy 150
  plates (b03/b06 HyperFrames) untouched · room: small paper s.36 @y1300 (pen remapped), chat/hand icons lifted.
Usage: python3 pipeline/scripts/clip-04-reels-plan-v18.py"""
import json, os
D = os.path.join(os.path.dirname(__file__), "../../content/clips/clip-04-gap-sach-tu-kiem/final")
p = json.load(open(os.path.join(D, "plan-A.voiced.json")))
p["id"] = "clip-04-final-reels"; p["video"]["layout"] = "reels"

def shift(pr, dy):
    if pr["kind"] == "pen": pr["keys"] = [[t, x, round(y + dy, 1)] for t, x, y in pr["keys"]]
    elif pr["kind"] in ("halves", "table"): pr["top"] = pr["top"] + dy
    elif pr["kind"] == "window": pr["wy"] = 150
    elif pr["kind"] != "tag": pr["y"] = round(pr["y"] + dy, 1)

for s in p["scenes"]:
    fr, props = s["camera"]["framing"], s.get("props", [])
    kinds = {pr["kind"] for pr in props}
    if "plate" in kinds: continue  # HyperFrames MG plates (b03/b06) are laid out above y 1000 already (bars baseline 980)
    if fr == "closeup":
        for pr in props:
            if pr["kind"] in ("paper", "card", "pen"): shift(pr, -200)
            if pr["kind"] == "tag": pr["y"] -= 200
    elif "halves" in kinds or s["id"].startswith("b06"):
        for pr in props: shift(pr, -200)
    elif s["background"]["kind"] == "room":
        for pr in props:
            if pr["kind"] == "paper" and pr.get("s") == 0.45:
                pr["s"], pr["y"] = 0.36, 1300
            if pr["kind"] == "pen":  # remap pen strokes that write on the small paper
                pr["keys"] = [[t, x, y] if y >= 1400 else [t, round(480 + (x - 480) * 0.8, 1), round(1300 + (y - 1265) * 0.8, 1)] for t, x, y in pr["keys"]]
            if pr["kind"] == "icon" and pr.get("name") == "chat": pr["y"] = 800
            if pr["kind"] == "icon" and pr.get("name") == "hand" and pr.get("rot") == 180: pr["y"], pr["size"] = 935, 80
os.makedirs(os.path.join(D, "out"), exist_ok=True)
json.dump(p, open(os.path.join(D, "out/plan-reels.json"), "w"), ensure_ascii=False, indent=1)
print("→ final/out/plan-reels.json")
