#!/usr/bin/env python3
"""Compile compact storyboard.yaml ↔ Remotion final/spec.json (make-video v3, DL-094).

  python3 pipeline/scripts/spec-compile.py --in <clip>/final/storyboard.yaml --out <clip>/final/spec.json
  python3 pipeline/scripts/spec-compile.py --in … --out … --merge-existing
  python3 pipeline/scripts/spec-compile.py --decompile <spec.json> --out <storyboard.yaml>
"""
from __future__ import annotations

import argparse
import copy
import json
import os
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import paths as P

try:
    import yaml  # type: ignore
except ImportError:  # pragma: no cover — PyYAML is in the Mac toolchain; fallback below
    yaml = None

# L-033-safe visual presets (TikTok 1080×1920 comic stage). Cast x in 0.35–0.65 keeps face clear of side UI.
VISUAL_PRESETS = {
    "character_closeup": {
        "background": "paper", "framing": "closeup", "push": 0.14,
        "cast": [{"id": "hiep", "x": 0.5, "facing": "right", "pose": "standing", "action": "talking", "expression": "neutral", "enter": "none"}],
        "props": [],
        "stage": {"action": "closeup Hiệp", "react": "nói thẳng"},
    },
    "desk_phone_buzz": {
        "background": "paper", "framing": "medium", "push": 0.1,
        "cast": [{"id": "hiep", "x": 0.42, "facing": "right", "pose": "standing", "action": "talking", "expression": "focused", "enter": "none"}],
        "props": [{"id": "phone", "x": 0.62, "y": 0.58, "scale": 0.9}],
        "stage": {"action": "Máy trên bàn", "react": "liếc máy"},
    },
    "explainer_card": {
        "background": "paper", "framing": "medium", "push": 0.08,
        "cast": [{"id": "hiep", "x": 0.38, "facing": "right", "pose": "standing", "action": "pointing", "expression": "focused", "enter": "none"}],
        "props": [{"id": "card", "x": 0.68, "y": 0.45, "scale": 1.0}],
        "stage": {"action": "Thẻ bằng chứng", "react": "chỉ số"},
    },
    "split_compare": {
        "background": "paper", "framing": "wide", "push": 0.06,
        "cast": [{"id": "hiep", "x": 0.5, "facing": "right", "pose": "standing", "action": "talking", "expression": "focused", "enter": "none"}],
        "props": [],
        "stage": {"action": "So sánh 2 khung", "react": "đối chiếu"},
    },
    "cta_peer": {
        "background": "paper", "framing": "closeup", "push": 0.12,
        "cast": [{"id": "hiep", "x": 0.5, "facing": "right", "pose": "standing", "action": "talking", "expression": "warm", "enter": "none"}],
        "props": [],
        "stage": {"action": "CTA ngang hàng", "react": "lắng nghe"},
    },
    "default": {
        "background": "paper", "framing": "medium", "push": 0.1,
        "cast": [{"id": "hiep", "x": 0.5, "facing": "right", "pose": "standing", "action": "talking", "expression": "neutral", "enter": "none"}],
        "props": [],
        "stage": {"action": "default", "react": "nói"},
    },
}

EMOTION_MAP = {
    "spark": "teasing",
    "dip": "reflective",
    "reflective": "reflective",
    "focused": "focused",
    "warm": "warm",
    "happy": "happy",
    "maxim": "maxim",
    "neutral": "neutral",
    "sad": "sad",
    "vulnerable": "reflective",
}

PART_BUCKET = {
    "hook": "hook",
    "story": "struggle",
    "dip": "struggle",
    "struggle": "struggle",
    "turn": "turn",
    "evidence": "evidence",
    "action": "action",
    "cta": "cta",
    "end": "cta",
}

DEFAULT_SFX = {
    "hook": "stamp",
    "struggle": "whoosh-soft",
    "dip": "whoosh-soft",
    "turn": "swish",
    "evidence": "click",
    "action": "click",
    "cta": "pop",
}


def load_yaml(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    if yaml is not None:
        return yaml.safe_load(text) or {}
    return _mini_yaml(text)


def dump_yaml(data: dict, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if yaml is not None:
        path.write_text(yaml.safe_dump(data, allow_unicode=True, sort_keys=False, default_flow_style=False), encoding="utf-8")
        return
    path.write_text(_mini_yaml_dump(data), encoding="utf-8")


def _mini_yaml(text: str) -> dict:
    """Tiny subset parser for storyboard files when PyYAML missing (dicts/lists/scalars)."""
    # Prefer json if someone passed JSON; else require PyYAML for full YAML.
    t = text.strip()
    if t.startswith("{"):
        return json.loads(t)
    raise SystemExit("PyYAML required to parse storyboard.yaml (pip install pyyaml)")


def _mini_yaml_dump(data: dict) -> str:
    return json.dumps(data, ensure_ascii=False, indent=2)


def hl_indices(text: str) -> list[int]:
    """Indexes of **bold** spans in `text` (word tokens). Prefer EN via hl_for_line()."""
    words = re.findall(r"\*\*([^*]+)\*\*|(\S+)", text or "")
    out, i = [], 0
    for bold, plain in words:
        if bold:
            out.append(i)
            i += len(bold.split())
        else:
            i += 1
    return out


_FUNC_EN = {
    "a", "an", "the", "to", "of", "in", "on", "at", "for", "and", "or", "but",
    "is", "are", "was", "were", "be", "it", "its", "i", "you", "we", "my", "your",
}


def hl_for_line(vi_text: str, en: str, fx_word: str = "") -> list[int]:
    """L-004: hl indexes EN caption words (not VI). Match fx.word / bold span into EN."""
    en_words = (en or "").split()
    if not en_words:
        return hl_indices(vi_text)
    anchors = []
    if fx_word:
        anchors.append(fx_word.strip())
    anchors.extend(re.findall(r"\*\*([^*]+)\*\*", vi_text or ""))
    out = []
    for a in anchors:
        al = a.lower().strip(".,!?;:…\"'")
        if not al:
            continue
        for i, w in enumerate(en_words):
            wl = w.lower().strip(".,!?;:…\"'")
            if wl == al or al in wl or wl in al:
                if wl not in _FUNC_EN and i not in out:
                    out.append(i)
                break
    if out:
        return out
    # fallback: last content word in EN (avoid function words)
    for i in range(len(en_words) - 1, -1, -1):
        wl = en_words[i].lower().strip(".,!?;:…\"'")
        if wl and wl not in _FUNC_EN:
            return [i]
    return [max(0, len(en_words) - 1)]


def text_to_phrases(text: str, emotion: str) -> list[dict]:
    """Build one {nhấn:} phrase from **highlight** markup."""
    def repl(m):
        return "{nhấn: " + m.group(1) + "}"
    t = re.sub(r"\*\*([^*]+)\*\*", repl, text or "")
    t = re.sub(r"\s+", " ", t).strip()
    emph = "{nhấn:" in t
    gap = 0.5 if emotion in ("reflective", "sad", "maxim", "dip") else 0.16
    return [{"t": t, "gap": gap, "tempo": 1.0, "semi": 0.0, "emph": emph, **({"emph_semi": -0.2} if emph else {})}]


def display_text(text: str) -> str:
    return text or ""


def say_from_text(text: str) -> str:
    return re.sub(r"\*\*([^*]+)\*\*", r"\1", text or "").strip()


def voice_ref_for(emotion: str, voice_engine: str) -> str:
    if voice_engine in ("direct", "vieneu"):
        # block mapping handled by voice-vieneu; line-level slot still useful for F5 fallback
        if emotion in ("spark", "teasing", "happy"):
            return "default"
        if emotion in ("reflective", "dip", "sad", "vulnerable"):
            return "default"
        if emotion in ("focused", "neutral"):
            return "default"
        return "default"
    return "default"


def expand_visual(name: str, emotion: str) -> dict:
    preset = copy.deepcopy(VISUAL_PRESETS.get(name) or VISUAL_PRESETS["default"])
    expr = {
        "spark": "happy", "teasing": "happy", "happy": "happy",
        "reflective": "sad", "dip": "sad", "sad": "sad", "vulnerable": "sad",
        "focused": "focused", "warm": "warm", "maxim": "neutral",
    }.get(emotion, "neutral")
    for c in preset["cast"]:
        c["expression"] = expr
    return preset


def compile_storyboard(sb: dict, existing: dict | None = None) -> dict:
    clip = sb.get("clip") or "clip-00"
    voice_engine = sb.get("voice_engine") or "vieneu"
    theme = (sb.get("theme") or "DARK").upper()
    theme_map = {"DARK": "dark", "LIGHT": "light", "dark": "dark", "light": "light"}
    beats = sb.get("beats") or []
    if not beats:
        raise SystemExit("storyboard: beats[] empty")

    scenes = []
    hook_ids = []
    for i, b in enumerate(beats):
        bid = b["id"]
        part = b.get("part") or "story"
        emo_in = b.get("emotion") or "neutral"
        emotion = EMOTION_MAP.get(emo_in, emo_in)
        text = display_text(b.get("text") or "")
        say = b.get("say") if voice_engine == "f5-tts" else (b.get("say") or say_from_text(text))
        en = b.get("en") or ""
        if isinstance(en, str) and len(en.split()) > 8:
            en = " ".join(en.split()[:8])
        visual = expand_visual(b.get("visual") or "character_closeup", emotion)
        fx = b.get("fx") or {}
        if isinstance(fx, str):
            fx = {"visual": fx, "word": ""}
        word = (fx.get("word") or "").strip()
        if not fx.get("visual"):
            raise SystemExit(f"beat {bid}: fx.visual required (rule-52)")
        sfx_name = b.get("sfx") or DEFAULT_SFX.get(part, "click")
        if isinstance(sfx_name, list):
            sfx_list = sfx_name
        else:
            sfx_list = [{"name": sfx_name, "atLine": 0, "offset": 0.0, **({"word": word} if word else {})}]

        if part == "hook":
            hook_ids.append(bid)

        # Prefer explicit beat.hl; else map highlight → EN caption (L-004)
        hl = b.get("hl")
        if not isinstance(hl, list) or not hl:
            hl = hl_for_line(text, en, word)
        line = {
            "speaker": b.get("speaker") or "hiep",
            "emotion": emotion,
            "voice_ref": voice_ref_for(emotion, voice_engine),
            "voice_role": "Hiệp",
            "text": text,
            "say": say,
            "en": en,
            "hl": hl,
            "phrases": text_to_phrases(text, emotion),
        }
        cast = visual["cast"]
        if i == 0 and cast:
            cast = copy.deepcopy(cast)
            cast[0]["enter"] = "pop"

        scene = {
            "id": bid,
            "beat": f"{clip}.{bid.rstrip('abcdefmid')}" if not bid.endswith("mid") else f"{clip}.b01",
            "part": PART_BUCKET.get(part, part),
            "role": "Hiệp",
            "background": visual["background"],
            "framing": visual["framing"],
            "push": visual["push"],
            "transition": "cut",
            "cast": cast,
            "fx": {"visual": fx.get("visual"), "word": word},
            "sfx": sfx_list,
            "props": visual["props"],
            "lines": [line],
            "stage": visual["stage"],
        }
        if b.get("link"):
            scene["link"] = b["link"]
        if b.get("narration"):
            scene["narration"] = b["narration"]
        scenes.append(scene)

    engagement = sb.get("engagement") or []
    if len(engagement) < 3:
        raise SystemExit(f"engagement needs ≥ 3 items (rule-56), got {len(engagement)}")

    hook_text = ""
    if sb.get("cover", {}).get("headline"):
        hook_text = sb["cover"]["headline"]
    elif scenes:
        hook_text = say_from_text(scenes[0]["lines"][0]["text"])
    # rule-55: first hook scene narration = hook text on frame 0
    if scenes and hook_ids and scenes[0]["id"] == hook_ids[0] and not scenes[0].get("narration"):
        scenes[0]["narration"] = hook_text

    spec = {
        "id": f"{clip}-final" if not str(clip).endswith("-final") else clip,
        "clip": re.sub(r"-final$", "", str(clip).split("/")[-1]) if True else clip,
        "title": sb.get("title") or clip,
        "week": sb.get("week") or 1,
        "theme": theme_map.get(theme, "dark"),
        "pillar": sb.get("pillar") or "",
        "trend": sb.get("trend") or "",
        "mode": sb.get("mode") or "default",
        "voice_engine": voice_engine,
        "voice_prefix": sb.get("voice_prefix") or "v1",
        "voice_refs": {"default": "thai-son-v2", "happy": "thai-son-v2", "serious": "thai-son-v2"},
        "voice_speed": float(sb.get("voice_speed") or 1.0),
        "mix": "linear",
        "layout": sb.get("layout") or "tiktok",
        "length_target": sb.get("length_target") or [60, 120],
        "pacing": {"lead": 0.06 if hook_ids else 0.15, "lead_tr": 0.05, "tail": 0.15 if hook_ids else 0.25, "swish": "beat"},
        "transition_sfx": {"part": "whoosh-soft", "scene": "swish"},
        "endcard": sb.get("endcard") or {
            "duration": 3.0, "y": 560,
            "safety": "Thông tin tham khảo, không thay thế tư vấn chuyên gia",
            "sources": "", "credit": "",
        },
        "engagement": engagement,
        "voices": {"Hiệp": "VieNeu · Thái Sơn" if voice_engine == "vieneu" else "F5 · Thái Sơn"},
        "hook": {
            "text": hook_text,
            "scenes": hook_ids or ([scenes[0]["id"]] if scenes else []),
            "format": sb.get("hook_format") or "",
        },
        "cover": {
            "headline": (sb.get("cover") or {}).get("headline") or hook_text,
            "sub": (sb.get("cover") or {}).get("sub") or "",
            "mood": (sb.get("cover") or {}).get("mood") or theme_map.get(theme, "dark"),
        },
        "parts": [{
            "id": "A",
            "engine": "remotion",
            "transitionOut": "fade",
            "scenes": scenes,
        }],
        "revisions": [],
        "storyboard_source": "storyboard.yaml",
    }

    # normalize clip id field (folder slug without -final)
    slug = sb.get("clip") or clip
    spec["clip"] = slug.replace("clip-", "clip-") if slug.startswith("clip-") else slug

    if existing and isinstance(existing, dict):
        # rule-36: keep revisions + manual overrides
        if existing.get("revisions"):
            spec["revisions"] = copy.deepcopy(existing["revisions"])
        for k in ("fact_lock", "throughline", "story", "hook_alt", "hook_question", "length_note", "post",
                  "voices", "voice_refs", "structure", "throughline_beats"):
            if k in existing and k not in sb:
                spec[k] = copy.deepcopy(existing[k])
        # preserve endcard sources/credit if storyboard omitted them
        if existing.get("endcard") and not (sb.get("endcard")):
            for k in ("sources", "credit", "safety"):
                if existing["endcard"].get(k):
                    spec["endcard"][k] = existing["endcard"][k]
        # preserve hand-tuned hl / stage / cast when beat text unchanged
        old_by_id = {}
        for p in existing.get("parts") or []:
            for sc in p.get("scenes") or []:
                old_by_id[sc.get("id")] = sc
        for p in spec["parts"]:
            for sc in p.get("scenes") or []:
                old = old_by_id.get(sc["id"])
                if not old:
                    continue
                ol = (old.get("lines") or [{}])[0]
                nl = (sc.get("lines") or [{}])[0]
                if say_from_text(ol.get("text") or "") == say_from_text(nl.get("text") or ""):
                    if "hl" in ol:
                        nl["hl"] = copy.deepcopy(ol["hl"])
                    if old.get("link") and not sc.get("link"):
                        sc["link"] = copy.deepcopy(old["link"])
                    if old.get("narration") and not sc.get("narration"):
                        sc["narration"] = old["narration"]
                    if old.get("stage"):
                        sc["stage"] = copy.deepcopy(old["stage"])
                    if old.get("cast"):
                        sc["cast"] = copy.deepcopy(old["cast"])
                    if old.get("props") is not None:
                        sc["props"] = copy.deepcopy(old["props"])
                    for extra in ("push", "framing", "background", "transition", "hits", "dropAt"):
                        if extra in old:
                            sc[extra] = copy.deepcopy(old[extra])
        if "callbacks" in existing:
            spec["callbacks"] = copy.deepcopy(existing["callbacks"])
        else:
            spec.setdefault("callbacks", [])
    return spec


def decompile_spec(spec: dict) -> dict:
    beats = []
    for part in spec.get("parts") or []:
        if part.get("engine") != "remotion":
            continue
        for sc in part.get("scenes") or []:
            if sc.get("id") == "endcard":
                continue
            lines = sc.get("lines") or [{}]
            line = lines[0]
            sfx = sc.get("sfx") or []
            sfx_name = sfx[0]["name"] if sfx and isinstance(sfx[0], dict) else (sfx[0] if sfx else None)
            # reverse visual preset by framing/props heuristic
            visual = "character_closeup"
            props = sc.get("props") or []
            framing = sc.get("framing") or ""
            if any(p.get("id") == "phone" for p in props if isinstance(p, dict)):
                visual = "desk_phone_buzz"
            elif any(p.get("id") == "card" for p in props if isinstance(p, dict)):
                visual = "explainer_card"
            elif framing == "wide":
                visual = "split_compare"
            elif (sc.get("part") or "") in ("cta",):
                visual = "cta_peer"
            emo = line.get("emotion") or "neutral"
            # map back spark/dip labels when possible
            emo_out = {"teasing": "spark", "reflective": "dip"}.get(emo, emo)
            part_name = sc.get("part") or "story"
            part_out = {"struggle": "dip", "hook": "hook", "evidence": "evidence", "action": "action", "cta": "cta", "turn": "story"}.get(part_name, part_name)
            beat = {
                "id": sc["id"],
                "part": part_out,
                "emotion": emo_out,
                "text": line.get("text") or "",
                **({"say": line["say"]} if line.get("say") and line.get("say") != say_from_text(line.get("text") or "") else {}),
                "en": line.get("en") or "",
                "visual": visual,
                "fx": sc.get("fx") or {"visual": "", "word": ""},
                **({"sfx": sfx_name} if sfx_name else {}),
            }
            if sc.get("link"):
                beat["link"] = sc["link"]
            if sc.get("narration"):
                beat["narration"] = sc["narration"]
            if "hl" in line:
                beat["hl"] = line["hl"]
            beats.append(beat)

    cover = spec.get("cover") or {}
    theme = (spec.get("theme") or "dark").upper() if (spec.get("theme") or "dark") in ("dark", "light") else (spec.get("theme") or "DARK")
    if theme in ("dark", "light"):
        theme = theme.upper()
    return {
        "clip": spec.get("clip") or spec.get("id"),
        "title": spec.get("title") or "",
        "theme": theme,
        "pillar": spec.get("pillar") or "",
        "trend": spec.get("trend") or "",
        "mode": spec.get("mode") or "default",
        "voice_engine": spec.get("voice_engine") or ("f5-tts" if "F5" in str((spec.get("voices") or {}).get("Hiệp", "")) else "vieneu"),
        "voice_prefix": spec.get("voice_prefix") or "v1",
        "voice_speed": spec.get("voice_speed") or 1.0,
        "layout": spec.get("layout") or "tiktok",
        "cover": {
            "headline": cover.get("headline") or (spec.get("hook") or {}).get("text") or "",
            "sub": cover.get("sub") or "",
            "mood": cover.get("mood") or theme.lower() if isinstance(theme, str) else "dark",
        },
        "engagement": spec.get("engagement") or [],
        "beats": beats,
    }


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="storyboard.yaml ↔ spec.json compiler")
    ap.add_argument("--in", dest="inp", default="")
    ap.add_argument("--out", dest="out", default="")
    ap.add_argument("--merge-existing", action="store_true")
    ap.add_argument("--decompile", default="", help="Path to existing spec.json")
    args = ap.parse_args(argv)

    if args.decompile:
        spec = json.load(open(args.decompile, encoding="utf-8"))
        sb = decompile_spec(spec)
        out = Path(args.out) if args.out else Path(args.decompile).with_name("storyboard.yaml")
        dump_yaml(sb, out)
        print(f"decompile → {out} ({len(sb.get('beats') or [])} beats)")
        return 0

    if not args.inp or not args.out:
        ap.error("--in and --out required (or --decompile)")
    sb = load_yaml(Path(args.inp))
    existing = None
    outp = Path(args.out)
    if args.merge_existing and outp.is_file():
        existing = json.load(open(outp, encoding="utf-8"))
    spec = compile_storyboard(sb, existing=existing)
    outp.parent.mkdir(parents=True, exist_ok=True)
    json.dump(spec, open(outp, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    print(f"compile → {outp} ({sum(len(p.get('scenes') or []) for p in spec['parts'])} scenes, hook={spec['hook']['scenes']})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
