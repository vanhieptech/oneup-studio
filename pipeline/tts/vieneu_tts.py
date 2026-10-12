#!/usr/bin/env python3
"""Omi voice (rule-46): VieNeu-TTS v3 Turbo, local CPU/ONNX, Apache-2.0. Characters with a declared preset only (Hiệp: Đức Trí, Omi: Kim Thanh; DL-030).

stdin/argv: JSON {"fps":30,"jobs":[{"text","voice","emotion","out"}]}
For each job: synthesize (cached: skipped if out exists), apply emotion post-fx
(tempo/pitch via ffmpeg), trim silence, write <out>.wav and <out>.json
{duration, envelope[per frame 0..1]}. Prints a JSON summary on stdout.
Never clones a reference clip: only built-in preset voices are allowed.
"""
import json, subprocess, sys, os, wave, struct, math, tempfile

# emotion → (non-verbal tag prefix, tempo, pitch semitones). Tags are VieNeu experimental cues.
EMOTION = {
    "neutral":   ("", 1.00, 0.0),
    "happy":     ("[cười] ", 1.06, 1.0),
    "teasing":   ("[cười] ", 1.03, 0.5),
    "surprised": ("", 1.10, 1.5),
    "sad":       ("[thở dài] ", 0.92, -1.0),
    "focused":   ("", 0.98, 0.0),
    "confused":  ("[hắng giọng] ", 0.97, 0.0),
}

# Per-preset base tempo (pitch kept). Both presets read in a slow storybook pace (~3 syl/s);
# a 55-60s clip needs ~3.6-3.9 syl/s (DL-030). Checked by STT after every change.
VOICE_TEMPO = {"Đức Trí": 1.3, "Kim Thanh": 1.12}

def envelope(path, fps):
    with wave.open(path) as w:
        sr, n, ch = w.getframerate(), w.getnframes(), w.getnchannels()
        raw = w.readframes(n)
    s = struct.unpack("<%dh" % (len(raw) // 2), raw)[::ch]
    hop = sr / fps; env = []
    i = 0
    while i * hop < len(s):
        seg = s[int(i * hop):int((i + 1) * hop)]
        env.append(math.sqrt(sum(x * x for x in seg) / max(1, len(seg))) / 32768)
        i += 1
    peak = sorted(env)[int(len(env) * 0.95)] if env else 1
    return len(s) / sr, [round(min(1.0, e / max(peak, 1e-4)), 3) for e in env]

def main():
    spec = json.loads(sys.argv[1] if len(sys.argv) > 1 else sys.stdin.read())
    fps = spec.get("fps", 30)
    todo = [j for j in spec["jobs"] if not os.path.exists(j["out"] + ".wav")]
    tts = None
    if todo:
        from vieneu import Vieneu
        tts = Vieneu()
    out = []
    for j in spec["jobs"]:
        wav = j["out"] + ".wav"
        if not os.path.exists(wav):
            tag, tempo, semi = EMOTION.get(j.get("emotion", "neutral"), EMOTION["neutral"])
            audio = tts.infer(tag + j["text"], voice=j["voice"], temperature=0.6)
            with tempfile.TemporaryDirectory() as d:
                raw = os.path.join(d, "raw.wav"); tts.save(audio, raw)
                rate = 2 ** (semi / 12)
                tempo *= VOICE_TEMPO.get(j["voice"], 1.0)
                af = (f"asetrate=48000*{rate:.4f},aresample=48000,atempo={tempo / rate:.4f},"
                      "silenceremove=start_periods=1:start_threshold=-45dB,areverse,"
                      "silenceremove=start_periods=1:start_threshold=-45dB,areverse,"
                      "loudnorm=I=-16:TP=-1.5:LRA=11,aresample=48000")
                os.makedirs(os.path.dirname(wav) or ".", exist_ok=True)
                subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-i", raw, "-af", af, "-ac", "1", "-c:a", "pcm_s16le", wav], check=True)
        dur, env = envelope(wav, fps)
        meta = {"duration": round(dur, 3), "envelope": env, "engine": "VieNeu-TTS v3 Turbo (local ONNX)", "voice": j["voice"], "emotion": j.get("emotion", "neutral")}
        json.dump(meta, open(j["out"] + ".json", "w"))
        out.append({"out": j["out"], "duration": meta["duration"]})
    print(json.dumps(out))

if __name__ == "__main__":
    main()
