#!/usr/bin/env python3
"""Preview stills of Remotion comic scenes before voice (DL-056). Estimated line durations, no audio.
usage: props-preview.py <spec.json> <outdir> scene:t1,t2 [scene:t ...]"""
import importlib.util, json, os, re, subprocess, sys
R = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
spec_ = importlib.util.spec_from_file_location("bf", os.path.join(R, "pipeline/scripts/build-final.py")); bf = importlib.util.module_from_spec(spec_); spec_.loader.exec_module(bf)
spec = json.load(open(sys.argv[1])); out = os.path.abspath(sys.argv[2]); os.makedirs(out, exist_ok=True)
for p in spec["parts"]:
    for sc in p.get("scenes", []):
        for i, l in enumerate(sc["lines"]):
            n = len(re.sub(r"\{[^}]*\}|\*", "", l["text"]).split())
            l.update(_dur=round(n * 0.27 + 0.3, 2), _env=[], _engine="preview", _phr=None, _key=f"preview-{sc['id']}-{i}")
part = spec["parts"][0]; plan, _, _ = bf.remotion_plan(spec, part)
for s in plan["scenes"]:
    for d in s["dialogue"]: d.pop("audio", None)
starts = {}; acc = 0.0
for s in plan["scenes"]:
    starts[s["id"]] = acc; acc += s["duration"]
pj = os.path.join(out, "preview-plan.json"); json.dump({"plan": plan}, open(pj, "w"), ensure_ascii=False)
env = dict(os.environ, PATH="/workspace/tools/node-v22.20.0-linux-x64/bin:" + os.environ["PATH"])
for arg in sys.argv[3:]:
    sid, ts = arg.split(":")
    for t in ts.split(","):
        fr = int(round((starts[sid] + float(t)) * 30)); f = os.path.join(out, f"{sid}-{t}s.png")
        r = subprocess.run(["npx", "remotion", "still", "src/index.ts", "ComicVideo", f, f"--props={pj}", f"--frame={fr}", "--log=error"], cwd=os.path.join(R, "video-engine"), env=env, capture_output=True, text=True)
        print(f, "OK" if r.returncode == 0 else r.stderr[-600:])
