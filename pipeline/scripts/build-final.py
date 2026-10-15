#!/usr/bin/env python3
"""Build a final clip from ONE source spec (content/clips/<clip>/final/spec.json).

  build-final.py <spec.json> [--stage voice|plans|render|assemble|all]   (default all)
                [--scenes b01,b01b,...]  partial preview: only these scene/section ids (parts left empty are dropped);
                                         outputs go to <final>/preview/ (plan-*-preview, timing-preview.json, <id>-preview.mp4)

Stages (each reuses cached output; edit the spec, never the generated files):
  voice    : every line -> the speaker profile's voice (rule-46). Default since DL-035: F5-TTS (hynt ViVoice, CC-BY-NC-SA,
             risk accepted) with synthetic refs (Hiệp: F5 · Thái Sơn, Omi: F5 · Mỹ Duyên), always via voice-prosody.py
             (phrase-level, leakage trim, 3 takes + STT pick). Lines without `phrases` become one phrase.
             Legacy profiles with engine vieneu-tts keep the DL-030/033 paths.
             cached in video-engine/public/voice/<key>.wav|json (key = engine+voice+ref+phrases)
  plans    : Remotion parts -> <final>/plan-<part>.voiced.json (timed from real audio, captions per line, lip-sync envelope)
             HyperFrames parts -> <final>/<dir>/index.html (from index.html.tpl) + <final>/out/<part>-voice.wav
  render   : npm run render (Remotion) / hyperframes render (explainer), then mux explainer voice
  assemble : xfade parts + acrossfade audio, in-house SFX, light grain (rule-20), -14 LUFS (rule-4), no music (rule-21)
Outputs: <final>/out/*.mp4 (gitignored) and <final>/<id>.mp4, timing.json (for STT/QA + script table).
"""
import hashlib, json, os, re, subprocess, sys, math, wave, struct

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
import paths as P  # rule-65 canonical paths
REPO = str(P.ROOT)
VE = str(P.VE)
NODE_BIN = os.environ.get("NODE22_BIN", "/workspace/tools/node-v22.20.0-linux-x64/bin")
PY = os.environ.get("VIENEU_PYTHON", "/workspace/tts-venv/bin/python")
FPS = 30
XF = 0.35  # cross-part transition

def sh(cmd, **kw):
    print("+", cmd if isinstance(cmd, str) else " ".join(cmd), flush=True)
    env = dict(os.environ, PATH=NODE_BIN + ":" + os.environ["PATH"])
    subprocess.run(cmd, shell=isinstance(cmd, str), check=True, env=env, **kw)

def profiles():
    d = os.path.join(VE, "src/characters/profiles")
    return {j["id"]: j for j in (json.load(open(os.path.join(d, f))) for f in os.listdir(d) if f.endswith(".json"))}

sys.path.insert(0, os.path.join(REPO, "pipeline/tts"))
import markup as MK  # DL-039 fillers/particles markup

def spoken(line):
    if line.get("phrases"): return MK.spoken(" ".join(re.sub(r"\[[^\]]*\]\s*", "", p["t"]) for p in line["phrases"]), line.get("speaker"))
    return line.get("say") or re.sub(r"\*\*|[“”\"]", "", line["text"]).replace("…", ",").strip()

def all_lines(spec):
    for p in spec["parts"]:
        for s in p.get("scenes", []) + p.get("sections", []):
            for l in s["lines"]:
                yield p, s, l

def voice_key(preset, emotion, text, take=1):
    return hashlib.sha1(json.dumps(["vieneu-tts", preset, emotion, text, 4] + ([take] if take != 1 else []), ensure_ascii=False).encode()).hexdigest()[:12]

def sync_shared():
    subprocess.run([sys.executable, str(P.SCRIPTS / "sync-shared.py")], check=True)

def stage_voice(spec):
    prof = profiles(); jobs = []; pjobs = []
    for _, _, l in all_lines(spec):
        if l.get("voice_file"):  # pre-voiced take (picked by STT outside the pipeline); <key>.wav/.json under public/voice
            l["_key"] = os.path.splitext(os.path.basename(l["voice_file"]))[0]
            if not os.path.exists(os.path.join(VE, "public/voice", l["_key"] + ".wav")): raise SystemExit(f"missing voice_file {l['voice_file']} (see media/MANIFEST.json)")
            continue
        pv = prof[l["speaker"]].get("voice") or {}
        if pv.get("engine") == "f5-tts" and not l.get("phrases"):
            l["phrases"] = [{"t": spoken(l), "gap": 0}]
        if l.get("phrases"):  # DL-033: phrase-level prosody path (voice-prosody.py), preferred for all new lines
            v = pv["preset"]; ph = [{k: x for k, x in p.items() if k != "en"} for p in l["phrases"]]
            if pv.get("engine") == "f5-tts":  # DL-035
                l["_key"] = "f5-" + hashlib.sha1(json.dumps([v, pv["ref"], ph, "vp5"] + ([l["takes"]] if l.get("takes") else []) + ([l.get("speed"), l.get("gap_max"), l.get("energetic"), l.get("whole"), l.get("alts")] + ([l.get("emph_tail"), l.get("emph_db")] if l.get("emph_tail") else []) + ([l.get("emph_head")] if l.get("emph_head") else []) if any(l.get(k) is not None for k in ("speed", "gap_max", "energetic", "whole", "alts")) else []), ensure_ascii=False).encode()).hexdigest()[:12]
                pjobs.append({"engine": "f5-tts", "speaker": l["speaker"], "voice": v, "ref": pv["ref"], "ref_text": pv["refText"], "phrases": l["phrases"], "takes": l.get("takes"), "speed": l.get("speed"), "gap_max": l.get("gap_max"), "energetic": l.get("energetic"), "whole": l.get("whole"), "alts": l.get("alts"), "emph_tail": l.get("emph_tail"), "emph_db": l.get("emph_db"), "emph_head": l.get("emph_head"), "out": os.path.join(VE, "public/voice", l["_key"])})
            else:
                l["_key"] = "vp-" + hashlib.sha1(json.dumps([v, ph, "vp1"], ensure_ascii=False).encode()).hexdigest()[:12]
                pjobs.append({"voice": v, "phrases": l["phrases"], "out": os.path.join(VE, "public/voice", l["_key"])})
            continue
        v = prof[l["speaker"]].get("voice")
        if not v: raise SystemExit(f"{l['speaker']} has no voice preset in its profile (rule-46)")
        k = voice_key(v["preset"], l["emotion"], spoken(l), l.get("take", 1))  # bump "take" in the spec to re-roll a line that fails STT
        l["_key"] = k
        jobs.append({"text": spoken(l), "voice": v["preset"], "emotion": l["emotion"], "out": os.path.join(VE, "public/voice", k)})
    todo = [j for j in jobs + pjobs if not os.path.exists(j["out"] + ".wav")]
    print(f"voice: {len(jobs) + len(pjobs)} lines ({len(pjobs)} prosody), {len(jobs) + len(pjobs) - len(todo)} cached")
    if jobs: sh([PY, os.path.join(REPO, "pipeline/tts/vieneu_tts.py"), json.dumps({"fps": FPS, "jobs": jobs}, ensure_ascii=False)], stdout=subprocess.DEVNULL)
    if pjobs:
        jf = os.path.join(VE, "public/voice", "_prosody-job.json"); json.dump({"jobs": pjobs}, open(jf, "w"), ensure_ascii=False)
        sh([PY, os.path.join(REPO, "pipeline/scripts/voice-prosody.py"), jf], stdout=subprocess.DEVNULL)
    for _, _, l in all_lines(spec):
        m = json.load(open(os.path.join(VE, "public/voice", l["_key"] + ".json")))
        l["_dur"], l["_env"], l["_engine"], l["_phr"] = m["duration"], m["envelope"], m["engine"], m.get("phrases")
        if m.get("stt_sim", 1) < 0.85: print(f"warn: {l['_key']} line STT sim {m['stt_sim']}: {m.get('stt')}")

def en_words(text, start, end, hl):
    ws = text.split(); w = [len(x) + 2 for x in ws]; tot = sum(w); acc = start; out = []
    for i, x in enumerate(ws):
        d = (end - start) * w[i] / tot; out.append({"word": x, "start": round(acc, 3)}); acc += d
    return out

def remotion_plan(spec, part):
    scenes = []; timing = []
    for si, sc in enumerate(part["scenes"]):
        tr = sc.get("transition", "cut"); trd = 0.0 if tr == "cut" else 0.4
        hook = sc.get("part") == "hook"  # rule-55: rapid hook, near-zero lead + short tail on cut scenes
        pc = spec.get("pacing") or {}  # optional per-clip pacing (clip-02 v17: match the approved listen file)
        t = 0.12 if (si == 0 and part is spec["parts"][0]) else (0.02 if hook and tr == "cut" else max(pc.get("lead", 0.3), trd + pc.get("lead_tr", 0.15)))
        cast = {c["id"]: {"characterId": c["id"], "x": c["x"], "pose": c.get("pose", "standing"), "action": c.get("action", "idle"),
                          "expression": c.get("expression", "neutral"), "facing": c.get("facing", "right"), "enter": c.get("enter", "none"),
                          "expressionChanges": [], "actionChanges": []} for c in sc["cast"]}
        dlg = []; segs = []
        for li, l in enumerate(sc["lines"]):
            st = round(t, 3); en = round(st + l["_dur"], 3)
            for cid, ch in (l.get("set") or {}).items():
                if "expression" in ch: cast[cid]["expressionChanges"].append({"at": st, "value": ch["expression"]})
                if "action" in ch: cast[cid]["actionChanges"].append({"at": st, "value": ch["action"]})
            dlg.append({"speaker": l["speaker"], "text": l["text"], "start": st, "end": round(en + 0.25, 3), "emotion": l["emotion"],
                        "audio": {"src": f"voice/{l['_key']}.wav", "duration": l["_dur"], "envelope": l["_env"], "engine": l["_engine"]}})
            segs.append({"text": l["en"], "start": 0.0 if (si == 0 and li == 0 and part is spec["parts"][0]) else round(st + 0.05, 3), "end": round(en + 0.2, 3), "highlight": l.get("hl", [])})  # rule-55/L-021: caption on frame 0
            timing.append({"beat": sc["beat"], "scene": sc["id"], "speaker": l["speaker"], "say": spoken(l), "en": l["en"], "emotion": l["emotion"], "key": l["_key"], "local": st, "dur": l["_dur"]})
            t = en + ((0.08 if hook else 0.2) if li < len(sc["lines"]) - 1 else 0)
        dur = round(t + (0.06 if hook else pc.get("tail", 0.45)), 3)
        dlg[-1]["end"] = min(dlg[-1]["end"], dur); segs[-1]["end"] = min(segs[-1]["end"], round(dur - 0.05, 3))
        for i in range(len(segs) - 1): segs[i]["end"] = min(segs[i]["end"], segs[i + 1]["start"])
        scene = {"id": sc["id"], "beat": sc["beat"], "duration": dur, "background": {"kind": sc["background"]},
                 "camera": {"framing": sc.get("framing", "medium"), "push": sc.get("push", 0.04)},
                 "transition": {"type": tr, "duration": trd or 0.4}, "characters": list(cast.values()), "dialogue": dlg,
                 "caption": {"text": " ".join(s["text"] for s in segs), "start": segs[0]["start"], "segments": segs},
                 "sfx": [{"name": x["name"], "at": round(max(0, dlg[x["atLine"]]["start"] + x.get("offset", 0)), 3)} for x in sc.get("sfx", [])]}
        if sc.get("props"):  # DL-056: prop times are relative to the first line start
            b0 = dlg[0]["start"]; sh = lambda v: round(v + b0, 3)
            scene["props"] = [{**p_, **{k: (sh(p_[k]) if not isinstance(p_[k], list) else [sh(v) for v in p_[k]]) for k in ("at", "until", "tearAt", "dropAt") if k in p_}} for p_ in sc["props"]]
        if sc.get("narration"): scene["narration"] = {"text": sc["narration"], "start": 0.0 if (si == 0 and part is spec["parts"][0]) else 0.05}  # rule-55: hook text on frame 0
        scenes.append(scene)
    plan = {"version": 1, "id": f"{spec['id']}-{part['id']}", "title": spec["title"], "meta": {"clip": spec["clip"], "week": spec["week"], "source": "final/spec.json"},
            "video": {"width": 1080, "height": 1920, "fps": FPS, "theme": spec["theme"]}, "scenes": scenes}
    return plan, timing, sum(s["duration"] for s in scenes)

def explainer(spec, part, fdir):
    t = 0.35; secs = []; timing = []; mix = []
    for sec in part["sections"]:
        s0 = t; t += 0.3; lines = []
        for li, l in enumerate(sec["lines"]):
            st = round(t, 3); d = l["_dur"]
            words = []
            if l.get("_phr"):  # real phrase boundaries from voice-prosody: spread words inside each phrase only
                for ph in l["_phr"]:
                    vw = re.sub(r"\[[^\]]*\]\s*", "", ph["text"]).split(); w = [len(x) + 2 for x in vw]; tot = sum(w); acc = st + ph["start"]
                    for i, x in enumerate(vw): words.append({"w": x, "start": round(acc, 3)}); acc += (ph["end"] - ph["start"]) * w[i] / tot
            else:
                vw = spoken(l).split(); w = [len(x) + 2 for x in vw]; tot = sum(w); acc = st
                for i, x in enumerate(vw): words.append({"w": x, "start": round(acc, 3)}); acc += d * w[i] / tot
            lines.append({"start": st, "end": round(st + d, 3), "capEnd": round(st + d + 0.25, 3), "words": words, "hl": l.get("hl", []),
                          "cap": ([w for ph, q in zip(l["phrases"], l["_phr"]) if ph.get("en") for w in en_words(ph["en"], st + q["start"], st + q["end"], [])]
                                  if l.get("_phr") and any(ph.get("en") for ph in l["phrases"]) else en_words(l["en"], st + 0.05, st + d - 0.1, l.get("hl", [])))})
            mix.append((l["_key"], st))
            timing.append({"beat": sec["beat"], "scene": sec["id"], "speaker": l["speaker"], "say": spoken(l), "en": l["en"], "emotion": l["emotion"], "key": l["_key"], "local": st, "dur": d})
            t = st + d + 0.25
        t += 0.3
        for i, ln in enumerate(lines[:-1]): ln["capEnd"] = min(ln["capEnd"], lines[i + 1]["start"])
        a0 = lines[0]["start"]; b0 = lines[-1]["capEnd"]  # same formula as the template's A(id, f)
        hits = [{"id": h["id"], "t": round(a0 + h["f"] * (b0 - a0), 3), "sfx": h.get("sfx")} for h in sec.get("hits", [])]
        secs.append({"id": sec["id"], "start": round(s0, 3), "end": round(t, 3), "lines": lines, "hits": hits})
    dur = round(t + 0.1, 2)
    # every *.tpl under the explainer dir (host index + sub-compositions) gets real timing (audit #2, DL-033):
    # __DUR__, __TIMING__ and per-section __START_<id>__ / __DUR_<id>__ for the clip's data-start/data-duration
    reps = {"__DUR__": str(dur), "__TIMING__": json.dumps({"sections": secs}, ensure_ascii=False)}
    for i, sc in enumerate(secs):
        end = secs[i + 1]["start"] if i + 1 < len(secs) else dur
        reps[f"__START_{sc['id']}__"] = str(sc["start"] if i else 0); reps[f"__DUR_{sc['id']}__"] = str(round(end - (sc["start"] if i else 0), 3))
    for root, _, files in os.walk(os.path.join(fdir, part["dir"])):
        if "node_modules" in root: continue
        for f in files:
            if f.endswith(".tpl"):
                txt = open(os.path.join(root, f)).read()
                for k, v in reps.items(): txt = txt.replace(k, v)
                open(os.path.join(root, f[:-4]), "w").write(txt)
    # voice track
    out = os.path.join(fdir, "out", f"{part['id']}-voice.wav")
    ins = []; flt = []
    for i, (k, st) in enumerate(mix):
        ins += ["-i", os.path.join(VE, "public/voice", k + ".wav")]
        flt.append(f"[{i}:a]aresample=48000,adelay={int(st*1000)}:all=1[a{i}]")
    flt.append("".join(f"[a{i}]" for i in range(len(mix))) + f"amix=inputs={len(mix)}:normalize=0,apad,atrim=0:{dur}[o]")
    sh(["ffmpeg", "-loglevel", "error", "-y", *ins, "-filter_complex", ";".join(flt), "-map", "[o]", "-ac", "1", "-ar", "48000", out])
    explainer.hits = [{"section": sc["id"], **h} for sc in secs for h in sc["hits"]]
    return timing, dur

SFX = {  # in-house synthesized (no third-party license; logged in assets/sfx/SOURCES.md)
    "pop": "sine=f=520:d=0.09,afade=t=out:st=0.02:d=0.07,volume=0.35",
    "ding": "sine=f=1318:d=0.5,afade=t=out:st=0.03:d=0.47,volume=0.22",
    "roomtone": "anoisesrc=d=120:c=brown:a=0.0025:r=48000,highpass=f=60,lowpass=f=3500",  # DL-033: bed under the whole clip, no digital silence between lines
    "whoosh": "anoisesrc=d=0.3:c=pink:a=0.25,bandpass=f=1500:w=900,afade=t=in:d=0.12,afade=t=out:st=0.14:d=0.16",
    # DL-042: transition SFX + ambience bed (in-house synthesized, see assets/sfx/SOURCES.md)
    "whoosh-soft": "anoisesrc=d=0.45:c=pink:a=0.32:r=48000,highpass=f=500,lowpass=f=2500,afade=t=in:d=0.2,afade=t=out:st=0.2:d=0.25",   # part change (xfade) ≈ −37 dBFS RMS pre-mix (bandpass made it inaudible, fixed)
    "swish": "anoisesrc=d=0.28:c=white:a=0.07:r=48000,highpass=f=2000,lowpass=f=6000,afade=t=in:d=0.1,afade=t=out:st=0.1:d=0.18",       # scene/section change ≈ −40 dBFS RMS pre-mix
    "ambience": "anoisesrc=d=120:c=brown:a=0.004:r=48000,highpass=f=50,lowpass=f=2200",                                          # continuous bed, replaces bare roomtone
}
# DL-043: accent SFX for key animation hits (in-house, ≈ −32…−37 dBFS RMS pre-mix → ~12–16 dB under voice)
SFX.update({
    "tick": "sine=f=2400:d=0.03:r=48000,afade=t=out:st=0.005:d=0.025,volume=0.25",
    "click": "anoisesrc=d=0.025:c=white:a=0.07:r=48000,highpass=f=1500,afade=t=out:st=0.003:d=0.022",
    "snap": "sine=f=180:d=0.08:r=48000,afade=t=out:st=0.01:d=0.07,volume=0.4",
    "pen": "anoisesrc=d=0.4:c=pink:a=0.5:r=48000,highpass=f=1800,lowpass=f=5000,tremolo=f=14:d=0.8,afade=t=in:d=0.05,afade=t=out:st=0.25:d=0.15",
    "stamp": "aevalsrc='0.08*sin(2*PI*95*t)*exp(-14*t)+0.02*(random(0)*2-1)*exp(-40*t)':d=0.2:s=48000",
    "sigh": "anoisesrc=d=0.75:c=pink:a=0.35:r=48000,highpass=f=250,lowpass=f=1800,afade=t=in:d=0.12,afade=t=out:st=0.2:d=0.55,volume=0.9",  # L-025: audible exhale on Haizz
    "rise": "aevalsrc='0.03*sin(2*PI*(300*t+500*t*t))':d=0.6:s=48000,afade=t=in:d=0.35,afade=t=out:st=0.45:d=0.15",
})
TRANS_SFX = {"part": "whoosh-soft", "scene": "swish"}
SFX_LEAD = 0.12  # SFX starts slightly before the cut so it overlaps across it

def main():
    specp = os.path.abspath(sys.argv[1]); stage = sys.argv[sys.argv.index("--stage") + 1] if "--stage" in sys.argv else "all"
    sync_shared()  # rule-65: fonts/logo copies from brand/ (gitignored)
    fdir = os.path.dirname(specp); spec = json.load(open(specp)); os.makedirs(os.path.join(fdir, "out"), exist_ok=True)
    sel = sys.argv[sys.argv.index("--scenes") + 1].split(",") if "--scenes" in sys.argv else None
    sfxn = "-preview" if sel else ""; odir = os.path.join(fdir, "preview") if sel else os.path.join(fdir, "out"); os.makedirs(odir, exist_ok=True)
    tj = os.path.join(odir, "timing-preview.json") if sel else os.path.join(fdir, "timing.json")
    if sel:
        for p in spec["parts"]:
            for k in ("scenes", "sections"):
                if k in p: p[k] = [x for x in p[k] if x["id"] in sel]
        spec["parts"] = [p for p in spec["parts"] if p.get("scenes") or p.get("sections")]
        spec["parts"][-1]["transitionOut"] = None
        print("preview scenes:", sel, "parts:", [p["id"] for p in spec["parts"]])
    stage_voice(spec)
    parts = []; timing = []; offset = 0.0
    for p in spec["parts"]:
        if p["engine"] == "remotion":
            plan, tm, dur = remotion_plan(spec, p); pp = os.path.join(odir if sel else fdir, f"plan-{p['id']}{sfxn}.voiced.json"); plan["id"] += sfxn
            json.dump(plan, open(pp, "w"), ensure_ascii=False, indent=1)
            # absolute times: Remotion scene starts are cumulative
            starts = {}; acc = 0
            for s in plan["scenes"]: starts[s["id"]] = acc; acc += s["duration"]
            sfx = [(x["name"], offset + starts[s["id"]] + x["at"]) for s in plan["scenes"] for x in s["sfx"]]
            parts.append({"id": p["id"], "engine": "remotion", "plan": pp, "dur": dur, "mp4": os.path.join(VE, "out", plan["id"] + ".mp4"), "sfx": sfx, "fx": p.get("transitionOut"),
                          "scene_starts": [starts[s["id"]] for s in plan["scenes"]][1:]})
            for x in tm: x["t"] = round(offset + starts[x["scene"]] + x["local"], 3); timing.append(x)
        else:
            tm, dur = explainer(spec, p, fdir)
            parts.append({"id": p["id"], "engine": "hyperframes", "dir": os.path.join(fdir, p["dir"]), "dur": dur, "mp4": os.path.join(fdir, "out", f"{p['id']}.mp4"),
                          "sfx": [(h["sfx"], offset + h["t"]) for h in explainer.hits if h.get("sfx")], "fx": p.get("transitionOut"),
                          "hits": [dict(h, t=round(offset + h["t"], 3)) for h in explainer.hits]})
            sec0 = {}
            for x in tm: sec0[x["scene"]] = min(sec0.get(x["scene"], 1e9), x["local"])
            parts[-1]["scene_starts"] = sorted(max(0, v - 0.3) for v in sec0.values())[1:]
            for x in tm: x["t"] = round(offset + x["local"], 3); timing.append(x)
        parts[-1]["_off"] = offset
        offset += parts[-1]["dur"] - XF
    total = round(offset + XF, 2)
    json.dump({"total": total, "parts": [{k: v for k, v in q.items() if k not in ("sfx", "hits")} for q in parts], "lines": timing}, open(tj, "w"), ensure_ascii=False, indent=1)
    print(f"plans: total ≈ {total}s")
    sh(["npx", "tsx", "src/cli.ts", "validate", *[q["plan"] for q in parts if q["engine"] == "remotion"]], cwd=VE)
    if stage in ("voice", "plans"): return
    if stage in ("render", "all"):
        sh(["npx", "tsx", "src/cli.ts", "render", *[q["plan"] for q in parts if q["engine"] == "remotion"], "--out-dir", "out"], cwd=VE)
        for q in parts:
            if q["engine"] == "hyperframes":
                silent = q["mp4"].replace(".mp4", "-silent.mp4")
                sh(["npx", "--yes", "hyperframes@0.8.150", "lint"], cwd=q["dir"])  # audit #1: lint gate (exit≠0 on error)
                open(os.path.join(fdir, "hf-check.txt"), "w").write(f"hyperframes@0.8.150 lint {q['id']}: 0 errors (build-final gate)\n")  # L-014
                sh(["npx", "--yes", "hyperframes@0.8.150", "render", ".", "-o", silent, "-f", str(FPS), "--quality", "delivery"], cwd=q["dir"])
                sh(["ffmpeg", "-loglevel", "error", "-y", "-i", silent, "-i", os.path.join(fdir, "out", f"{q['id']}-voice.wav"), "-map", "0:v", "-map", "1:a", "-c:v", "copy", "-c:a", "aac", "-b:a", "192k", "-shortest", q["mp4"]])
    # assemble (two passes: audio graph first, then video + mux; one big graph with lavfi sources can deadlock)
    for q in parts:
        real = float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", q["mp4"]], capture_output=True, text=True).stdout)
        if abs(real - q["dur"]) > 0.1: print(f"warn: part {q['id']} is {real:.2f}s, planned {q['dur']:.2f}s")
        q["dur"] = round(min(real, q["dur"] + 0.4), 3)
    ins = []; vf = []; af = []
    for i, q in enumerate(parts):
        ins += ["-i", q["mp4"]]
        vf.append(f"[{i}:v]trim=0:{q['dur']},setpts=PTS-STARTPTS,fps={FPS},scale=out_range=tv,format=yuv420p,setsar=1[v{i}]")
        af.append(f"[{i}:a]aresample=48000,aformat=channel_layouts=mono,apad,atrim=0:{q['dur']},asetpts=PTS-STARTPTS[a{i}]")
    vprev, aprev, acc = "v0", "a0", parts[0]["dur"]; starts = [0.0]
    for i in range(1, len(parts)):
        off = round(acc - XF, 3); fx = parts[i - 1]["fx"] or "fade"; starts.append(off)
        vf.append(f"[{vprev}][v{i}]xfade=transition={fx}:duration={XF}:offset={off}[vx{i}]"); af.append(f"[{aprev}][a{i}]acrossfade=d={XF}:c1=tri:c2=tri[ax{i}]")
        vprev, aprev, acc = f"vx{i}", f"ax{i}", acc + parts[i]["dur"] - XF
    total = round(acc, 3)
    trans = [{"at": round(st + XF / 2, 3), "kind": "part", "sfx": TRANS_SFX["part"]} for st in starts[1:]]
    for q, st in zip(parts, starts):
        trans += [{"at": round(st + t0, 3), "kind": "scene", "sfx": TRANS_SFX["scene"]} for t0 in q.get("scene_starts", [])]
    trans.sort(key=lambda x: x["at"])
    sfx = [(n, round(a - q["_off"] + st, 3)) for q, st in zip(parts, starts) for n, a in q["sfx"]] + [(t["sfx"], round(t["at"] - SFX_LEAD, 3)) for t in trans] + [("ambience", 0.0)]
    tjd = json.load(open(tj)); tjd["transitions"] = trans; tjd["sfx_mix"] = [{"name": n, "at": a} for n, a in sfx]
    # absolute (clip-time) hits; part offsets shift by xfade, so re-base on assembled starts
    tjd["hits"] = [dict(h, t=round(h["t"] - q["_off"] + st, 3)) for q, st in zip(parts, starts) for h in q.get("hits", [])]
    json.dump(tjd, open(tj, "w"), ensure_ascii=False, indent=1)
    tmp = os.path.join(fdir, "out", "sfx"); os.makedirs(tmp, exist_ok=True); mixl = [f"[{aprev}]"]
    for j, (name, at) in enumerate(sfx):
        w = os.path.join(tmp, name + ".wav")
        if not os.path.exists(w): sh(["ffmpeg", "-loglevel", "error", "-y", "-f", "lavfi", "-i", SFX[name], "-ac", "1", "-ar", "48000", w])
        ins_a = len(parts) + j; af.append(f"[{ins_a}:a]aresample=48000,adelay={int(max(0, at)*1000)}:all=1[s{j}]"); mixl.append(f"[s{j}]")
    af.append("".join(mixl) + f"amix=inputs={len(mixl)}:normalize=0:duration=first,loudnorm=I=-14:TP=-1.5:LRA=11,aresample=48000,atrim=0:{total}[a]")
    sfx_in = [x for (name, _) in sfx for x in ("-i", os.path.join(tmp, name + ".wav"))]
    wav = os.path.join(fdir, "out", f"mix{sfxn}.wav")
    sh(["ffmpeg", "-loglevel", "error", "-y", *ins, *sfx_in, "-filter_complex", ";".join(af), "-map", "[a]", "-ac", "1", "-ar", "48000", wav])
    # 2nd loudness pass: single-pass loudnorm lands ~1 LU low on short clips; correct with a linear gain to -14 LUFS (rule-4)
    m = subprocess.run(["ffmpeg", "-hide_banner", "-i", wav, "-af", "ebur128", "-f", "null", "-"], capture_output=True, text=True).stderr
    li = float(re.findall(r"I:\s+(-?[\d.]+) LUFS", m)[-1]); gain = round(-14.0 - li, 2)
    if abs(gain) > 0.2:
        sh(["ffmpeg", "-loglevel", "error", "-y", "-i", wav, "-af", f"volume={gain}dB,alimiter=limit=0.84:level=false", wav.replace(".wav", "-g.wav")]); os.replace(wav.replace(".wav", "-g.wav"), wav)
    vf.append(f"[{vprev}]noise=alls=4:allf=t,format=yuv420p[v]")  # light film grain over the whole clip (rule-20)
    out = os.path.join(odir, spec["id"] + sfxn + ".mp4")
    sh(["ffmpeg", "-loglevel", "error", "-y", *ins, "-i", wav, "-filter_complex", ";".join(vf), "-map", "[v]", "-map", f"{len(parts)}:a", "-c:v", "libx264", "-profile:v", "high", "-crf", "20", "-maxrate", "14M", "-bufsize", "28M",
        "-pix_fmt", "yuv420p", "-colorspace", "bt709", "-color_primaries", "bt709", "-color_trc", "bt709", "-color_range", "tv", "-r", str(FPS), "-c:a", "aac", "-b:a", "192k", "-ar", "48000", "-shortest", "-movflags", "+faststart", out])
    t2 = json.load(open(tj)); t2["total"] = total; t2["partStarts"] = starts
    json.dump(t2, open(tj, "w"), ensure_ascii=False, indent=1)
    print("final →", out, f"({total}s)")

if __name__ == "__main__":
    main()
