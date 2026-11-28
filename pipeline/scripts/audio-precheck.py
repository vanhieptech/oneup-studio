#!/usr/bin/env python3
"""Audio-Back QA: Vietnamese spoken rhythm & breath pre-check before Gate 1 (+ optional 20s F5 hook audition).

  audio-precheck.py <script-draft.md> [--audition-hook] [--voice thai-son-v2] [--out final/out/hook-audition.wav] [--json] [--dry-run]

Checks per beat on spoken Vietnamese text (stripping markup like {nhấn: …}, **…**, |):
  1. Speech rate (âm tiết/giây): natural VN spoken target is 2.6–3.4 syl/s.
     - Warns if > 3.8 syl/s (nói vội) or < 2.2 syl/s (lê thê) against beat duration
       (from beat label `[b01 · 0–5s]`, table Giây column, Gate 0 timing table, or estimated breath pacing).
  2. Pacing contrast (nhịp sóng), not a short-sentence quota:
     - A spoken story mixes a narrative breath (about 15–25 âm tiết, commas as natural breaths)
       with a short landing line (about 5–10 âm tiết). Do not split every line to dodge this check.
     - Warns only when a sentence has > 32 âm tiết with no pause mark (`,` / `—` / `...` / `…`),
       or any unbroken segment between pause marks exceeds 32 âm tiết.
  3. Consecutive beat opener repetition:
     - Warns when 2 adjacent beats start with the same opening structure (same first 2 words,
       or same repeating starter word/connector).
  4. Cross-clip hook echo (Beat 1 vs approved hooks):
     - Warns when the draft's first beat matches an archived hook in
       `content/archive/clip-*/final/spec.json` on opening structure (first 3 syllables)
       or on opening content keywords (shared first keyword + another, or Jaccard ≥ 0.6).

  5. Hook gọn / vào ý sớm / beat không nhồi (số liệu 5 clip đã duyệt, Hiệp 27/11 về clip-06 v8):
     - HOOK_LONG: b01 > 22 âm tiết (~7.5s). Mục tiêu 9–20 âm tiết (3–6s), nghe phát hiểu ngay vấn đề.
     - SLOW_ENTRY: b01+b02 > 65 âm tiết (~22s) → mở bài lòng vòng.
     - BEAT_BLOAT: bất kỳ beat > 45 âm tiết (~15s) → nhồi nhiều ý vào 1 beat.

--audition-hook (explicit opt-in before Gate 1; never runs unless requested):
  Extracts the first ~20 seconds (Hook + Beat 2) and synthesizes `final/out/hook-audition.wav`
  via `pipeline/tts/f5tts_gen.py` so Hiệp can hear the real spoken cadence before Gate 1.
"""
import json
import os
import re
import subprocess
import sys
import tempfile
import unicodedata
from pathlib import Path

import sys as _s, os as _o; _s.path.insert(0, _o.path.join(_o.path.dirname(_o.path.abspath(__file__)), "..")); import paths as P  # rule-65

RATE_TARGET_MIN = 2.6
RATE_TARGET_MAX = 3.4
RATE_WARN_HIGH = 3.8
RATE_WARN_LOW = 2.2
MAX_UNBROKEN_SYLLABLES = 32
NATURAL_SYL_PER_SEC = 3.0
# Số liệu từ 5 clip đã duyệt: b01 9–21 âm tiết (3–6s). Ngưỡng cảnh báo cố ý hơi rộng hơn mục tiêu viết (b01 ≤ 20, beat ≤ 42).
HOOK_MAX_SYL = 22      # b01 > 22 (~7.5s) → HOOK_LONG
ENTRY_MAX_SYL = 65     # b01+b02 > 65 (~22s) → SLOW_ENTRY
BEAT_MAX_SYL = 45      # beat nào > 45 (~15s) → BEAT_BLOAT
HOOK_AUDITION_TARGET_S = 20.0
HOOK_AUDITION_MAX_SYL = 70
FLAT_CADENCE_RUN = 4
FLAT_CADENCE_SPREAD = 3
MIN_BEATS_FOR_DIP_CHECK = 5

VULNERABILITY_CUES_RE = re.compile(
    r"(?i)\b(mình|tự trách|nản|bỏ cuộc|sợ|ngại|mệt|chán|quên sạch|hông nổi|không nổi|thất vọng|ngợp|hoang mang|khó chịu|tưởng|tự hỏi|chạnh|tủi|mắc lười|rối|chưa xong|cạn|đuối|kỳ cục|lỡ)\b"
)
SERIOUS_EVIDENCE_RE = re.compile(
    r"(?i)\b(\d+\s*(%|ngày|tuần|tháng|năm|người|phút|giờ|lần)|nghiên cứu|thí nghiệm|đại học|đo được|trung bình|thật ra|hóa ra|con số)\b"
)
WARM_CTA_RE = re.compile(
    r"(?i)\b(comment|bình luận|kể mình nghe|giống mình|nghĩ sao|vượt qua|chia sẻ|góc nhìn)\b"
)
SOUL_REFLECTION_RE = re.compile(
    r"(?i)\b(cuộc đời|lý tưởng|mục tiêu|niềm vui|nỗi buồn|cô đơn|chạnh lòng|tử tế|bình yên|ý nghĩa|hạnh phúc|đủ đầy|tha thứ|trưởng thành|đêm muộn|lặng|thật lòng)\b"
)
AI_CHICKEN_SOUP_RE = re.compile(
    r"(?i)(cuộc đời là một hành trình|không phải đích đến|thành công không đến sau một đêm|phiên bản tốt (?:nhất|hơn) của chính mình|hãy trân trọng từng khoảnh khắc|mọi chuyện xảy ra đều có lý do|chữa lành đứa trẻ bên trong|khám phá giá trị bản thân)"
)


def suggest_voice_ref(beat_idx, total_beats, text):
    """Map beat to DL-073/DL-086 emotional F5 voice ref & delivery hint."""
    if beat_idx == total_beats - 1 and (WARM_CTA_RE.search(text) or "?" in text):
        return "thai-son-happy", "warm_cta"
    if SOUL_REFLECTION_RE.search(text) and not SERIOUS_EVIDENCE_RE.search(text):
        return "thai-son-v2", "soul_reflection"
    if 1 <= beat_idx <= max(1, total_beats // 2) and VULNERABILITY_CUES_RE.search(text) and not SERIOUS_EVIDENCE_RE.search(text):
        return "thai-son-v2", "vulnerability_dip"
    if SERIOUS_EVIDENCE_RE.search(text) and beat_idx >= 1:
        return "thai-son-serious", "aha_peak"
    if beat_idx == 0:
        return "thai-son-v2", "hook_spark"
    return "thai-son-v2", "catharsis" if beat_idx >= total_beats - 2 else "curiosity"

PAUSE_RE = re.compile(r"(?:,|—|–|\.\.\.|…|;|:)")
SENT_SPLIT_RE = re.compile(r"(?<=[.!?])\s+")
REPEATING_STARTERS = {
    "nhưng", "và", "rồi", "vậy", "nên", "vì", "bạn", "mình", "thật", "hóa",
    "tuy", "còn", "ngược", "đầu", "tiếp", "cuối", "thứ", "nếu", "khi", "cái",
}
HOOK_CONTENT_STOP = REPEATING_STARTERS | {
    "là", "có", "một", "này", "đó", "thì", "mà", "ạ", "à", "nha", "á", "của",
    "cho", "với", "không", "để", "khi", "người", "lại", "cũng", "như", "nào",
    "gì", "hay", "hơn", "vào", "ra", "lên", "về", "tới", "tại", "được", "các",
}


def strip_markup(text):
    """Remove voice/emphasis markup while keeping punctuation and Vietnamese syllables."""
    t = unicodedata.normalize("NFC", text or "")
    t = re.sub(r"\{[^{}:]*:\s*([^{}]*)\}", r"\1", t)  # {nhấn: từ} → từ
    t = re.sub(r"\{[^{}]*\}", " ", t)                 # {ừm} → space
    t = t.replace("**", "").replace("__", "").replace("`", "")
    t = re.sub(r"\s*\|\s*", " ", t)
    t = re.sub(r"\s+/\s+", ", ", t)  # delivery slash counts as short breath pause
    return re.sub(r"\s+", " ", t).strip()


def syllables(text):
    """Extract spoken Vietnamese syllable tokens (each whitespace-separated word/number token)."""
    clean = strip_markup(text)
    return re.findall(r"[0-9a-zA-Zà-ỹÀ-ỸđĐ]+", clean)


def _norm_toks(text):
    return [w.lower() for w in syllables(text)]


def _parse_duration_s(raw):
    """Parse duration hint like '0–5s', '0:05-0:12', '(6s)', '12s' → float seconds or None."""
    if not raw:
        return None
    s = raw.strip()
    m = re.search(r"(\d+):(\d+(?:\.\d+)?)\s*[–\-~]\s*(\d+):(\d+(?:\.\d+)?)", s)
    if m:
        t1 = int(m.group(1)) * 60 + float(m.group(2))
        t2 = int(m.group(3)) * 60 + float(m.group(4))
        return round(max(0.5, t2 - t1), 2)
    m = re.search(r"(\d+(?:\.\d+)?)\s*[–\-~]\s*(\d+(?:\.\d+)?)\s*s\b", s, re.I)
    if m:
        return round(max(0.5, float(m.group(2)) - float(m.group(1))), 2)
    m = re.search(r"(?:^|[\s(\[·|])(\d+(?:\.\d+)?)\s*s\b", s, re.I)
    if m:
        return round(float(m.group(1)), 2)
    return None


def _parse_gate0_durations(md):
    """Extract per-beat durations from an embedded Gate 0 timing table (`| 0–6 | hook | ... |`)."""
    durs = []
    if "GATE0-BRIEF:BEGIN" not in md:
        return durs
    block = md.split("GATE0-BRIEF:BEGIN", 1)[1].split("GATE0-BRIEF:END", 1)[0]
    for ln in block.splitlines():
        if not ln.startswith("|"):
            continue
        cells = [c.strip() for c in ln.strip("|").split("|")]
        if len(cells) >= 2 and re.match(r"^\d+\s*[–\-]\s*\d+$", cells[0]):
            a, b = re.split(r"\s*[–\-]\s*", cells[0])
            durs.append(max(1.0, float(b) - float(a)))
    return durs


def parse_beats(md):
    """Extract list of beats `{id, label, text, duration_s}` from a draft script markdown.

    Supports:
      1. Numbered beat list: `1. **[b01 · 0–5s]** lời thoại...` (plus indented sub-bullets)
      2. Markdown beat table: `| b01 | 0–5s | Hiệp | lời thoại... | ... |`
    """
    body = md.split("\n---", 1)[1] if md.startswith("---") and "\n---" in md[3:] else md
    g0_durs = _parse_gate0_durations(body)
    # Strip Gate 0 brief block so its tables don't pollute script parsing
    if "<!-- GATE0-BRIEF:BEGIN" in body and "<!-- GATE0-BRIEF:END -->" in body:
        body = body[: body.index("<!-- GATE0-BRIEF:BEGIN")] + body[body.index("<!-- GATE0-BRIEF:END -->") + len("<!-- GATE0-BRIEF:END -->"):]

    beats = []
    inside = False
    for ln in body.splitlines():
        m = re.match(r"^\s*(\d+)\.\s*\*\*\[([^\]]+)\]\*\*\s*(.*)$", ln)
        if m:
            idx = int(m.group(1))
            label = m.group(2).strip()
            dur = _parse_duration_s(label)
            bid_m = re.match(r"([a-zA-Z]\d+[a-z]?)", label)
            bid = bid_m.group(1) if bid_m else f"b{idx:02d}"
            beats.append({"id": bid, "label": label, "text": m.group(3).strip(), "duration_s": dur})
            inside = True
            continue
        if inside and (ln.startswith("## ") or ln.lstrip().startswith("**End card")):
            inside = False
            continue
        if inside and beats and re.match(r"^\s+[-*]\s+", ln):
            sub = re.sub(r"^\s+[-*]\s+(\*\*[^*]+\*\*\s*)?", "", ln).strip()
            if sub and not re.match(r"^(?:Visual|Hình|Motion|SFX|Caption|EN)\s*:", sub, re.I):
                beats[-1]["text"] = (beats[-1]["text"] + " " + sub).strip()

    # Fallback: script table `| Beat | Giây | Người nói | Lời thoại | ... |`
    if not beats:
        for ln in body.splitlines():
            if not ln.startswith("|") or re.match(r"^\|[-\s|:]+\|$", ln):
                continue
            cells = [c.strip() for c in ln.strip("|").split("|")]
            if len(cells) >= 4 and re.match(r"^(?:[be]\d+|hook|cta)", cells[0], re.I):
                bid = cells[0].split()[0]
                dur = _parse_duration_s(cells[1])
                text = cells[3] if len(cells) >= 4 else cells[2]
                if text and not re.match(r"^(?:lời thoại|vi line)$", text, re.I):
                    beats.append({"id": bid, "label": cells[0], "text": text, "duration_s": dur})

    # Attach Gate 0 durations only if counts match and beat lacked explicit duration
    if g0_durs and len(g0_durs) == len(beats):
        for b, d in zip(beats, g0_durs):
            if b["duration_s"] is None:
                b["duration_s"] = d
    return beats


def estimate_breath_duration(text, syl_count):
    """Estimate realistic spoken duration (s) from syllable count + punctuation pauses."""
    clean = strip_markup(text)
    commas = len(re.findall(r"[,;:]", clean))
    dashes = len(re.findall(r"[—–]", clean))
    ellipses = len(re.findall(r"(?:\.\.\.|…)", clean))
    ends = len(re.findall(r"(?<!\.)[.!?](?!\.)", clean))
    pause_s = commas * 0.16 + dashes * 0.22 + ellipses * 0.35 + max(0, ends - 1) * 0.30
    return round(syl_count / NATURAL_SYL_PER_SEC + pause_s, 2)


def spoken_hook_from_spec(data):
    """First spoken hook line in a clip spec: part=hook / b01 scene lines, else hook.text."""
    for part in data.get("parts") or []:
        for sc in (part.get("scenes") or []) + (part.get("sections") or []):
            sid = str(sc.get("id") or "")
            if sc.get("part") == "hook" or sid.startswith("b01"):
                text = " ".join(strip_markup(l.get("text") or "") for l in (sc.get("lines") or [])).strip()
                if text:
                    return text
    hook = data.get("hook")
    if isinstance(hook, dict) and hook.get("text"):
        return strip_markup(str(hook["text"]))
    return ""


def load_archive_hooks(root=None):
    """Spoken Beat-1 hooks from content/archive/clip-*/final/spec.json."""
    base = Path(root) if root else P.ROOT
    out = []
    for spec in sorted((base / "content/archive").glob("clip-*/final/spec.json")):
        try:
            data = json.loads(spec.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            continue
        text = spoken_hook_from_spec(data)
        if text:
            out.append({"clip": spec.parent.parent.name, "text": text})
    return out


def _hook_content_keys(text):
    sent = SENT_SPLIT_RE.split(strip_markup(text) + " ")[0]
    return [w for w in _norm_toks(sent)[:12] if w not in HOOK_CONTENT_STOP and len(w) > 2]


def hook_similarity(draft_text, prior_text):
    """Return (too_close, reason) for opening structure or opening keywords."""
    a, b = _norm_toks(strip_markup(draft_text))[:4], _norm_toks(strip_markup(prior_text))[:4]
    if len(a) >= 3 and len(b) >= 3 and a[:3] == b[:3]:
        return True, "cùng 3 âm tiết mở đầu «" + " ".join(a[:3]) + "»"
    ka, kb = _hook_content_keys(draft_text), _hook_content_keys(prior_text)
    if not ka or not kb:
        return False, ""
    inter = set(ka) & set(kb)
    if ka[0] == kb[0] and len(inter) >= 2:
        return True, "cùng từ khóa mở đầu «" + ka[0] + "»"
    jac = len(inter) / len(set(ka) | set(kb))
    if jac >= 0.6 and len(inter) >= 3:
        return True, f"từ khóa mở đầu trùng {jac:.0%}"
    return False, ""


def cross_clip_hook_warnings(hook_text, archive_hooks):
    warnings = []
    for prior in archive_hooks or []:
        close, why = hook_similarity(hook_text, prior.get("text") or "")
        if not close:
            continue
        clip = prior.get("clip") or "archive"
        warnings.append({
            "code": "HOOK_ECHO",
            "beat": "b01",
            "message": f"b01: Hook trùng cấu trúc/từ khóa mở đầu với {clip} ({why}) → đổi góc mở, đừng lặp hook clip đã duyệt",
        })
    return warnings


def analyze_beats(beats, archive_hooks=None):
    """Run Vietnamese Audio-Back QA checks on parsed beats.

    Returns dict:
      {beats: [...], warnings: [{code, beat, message}], total_syllables, estimated_total_s, ok}
    """
    report_beats = []
    warnings = []
    total_syl = 0
    total_est = 0.0

    all_sent_syls = []
    n_beats = len(beats)
    for idx, b in enumerate(beats):
        clean = strip_markup(b["text"])
        syls = syllables(clean)
        n_syl = len(syls)
        total_syl += n_syl
        est_s = estimate_breath_duration(clean, n_syl)
        dur_s = b.get("duration_s")
        used_dur = dur_s if dur_s and dur_s > 0 else est_s
        total_est += used_dur
        rate = round(n_syl / used_dur, 2) if used_dur > 0 else 0.0
        v_ref, emo_role = suggest_voice_ref(idx, n_beats, clean)

        b_warns = []
        # 0. AI Chicken-Soup Cliché detector (DL-086: protect human soul & earned maxims from AI platitudes)
        cm = AI_CHICKEN_SOUP_RE.search(clean)
        if cm:
            w = {"code": "CLICHE_MAXIM", "beat": b["id"],
                 "message": f"{b['id']}: dính câu đạo lý sáo rỗng mùi AI «{cm.group(0)}» → đổi sang cảnh đời thường cụ thể trước rồi tự rút câu đúc kết mộc (Earned Maxim, `content/philosophy-bank.md`)"}
            warnings.append(w); b_warns.append(w)
        # 1. Speech rate check (explicit duration vs natural pace, or severe breath-density anomaly)
        if dur_s and dur_s > 0:
            if rate > RATE_WARN_HIGH:
                w = {"code": "RATE_FAST", "beat": b["id"],
                     "message": f"{b['id']}: tốc độ ước {rate:.2f} âm tiết/s ({n_syl} âm tiết / {dur_s}s) > {RATE_WARN_HIGH} → nói vội, dễ hụt hơi (chuẩn {RATE_TARGET_MIN}–{RATE_TARGET_MAX})"}
                warnings.append(w); b_warns.append(w)
            elif rate < RATE_WARN_LOW:
                w = {"code": "RATE_SLOW", "beat": b["id"],
                     "message": f"{b['id']}: tốc độ ước {rate:.2f} âm tiết/s ({n_syl} âm tiết / {dur_s}s) < {RATE_WARN_LOW} → lê thê, tụt nhịp (chuẩn {RATE_TARGET_MIN}–{RATE_TARGET_MAX})"}
                warnings.append(w); b_warns.append(w)

        # 2. Unbroken breath (> 32 syllables without `,` / `—` / `...`). 15–25 with a comma is a narrative breath, not a warning.
        sents = [s.strip() for s in SENT_SPLIT_RE.split(clean) if s.strip()]
        long_sents = []
        for s in sents:
            s_syl = len(syllables(s))
            all_sent_syls.append((b["id"], s_syl))
            has_pause = bool(PAUSE_RE.search(s))
            if s_syl > MAX_UNBROKEN_SYLLABLES and not has_pause:
                long_sents.append((s_syl, s))
                w = {"code": "LONG_SENTENCE", "beat": b["id"],
                     "message": f"{b['id']}: câu {s_syl} âm tiết (> {MAX_UNBROKEN_SYLLABLES}) không có dấu ngắt nhịp (, / — / ...): «{s[:70]}»"}
                warnings.append(w); b_warns.append(w)
            elif has_pause:
                # Also catch a single unbroken breath span > 32 syllables inside a punctuated sentence
                for seg in PAUSE_RE.split(s):
                    seg_syl = len(syllables(seg))
                    if seg_syl > MAX_UNBROKEN_SYLLABLES:
                        long_sents.append((seg_syl, seg.strip()))
                        w = {"code": "LONG_CLAUSE", "beat": b["id"],
                             "message": f"{b['id']}: vế liền hơi {seg_syl} âm tiết (> {MAX_UNBROKEN_SYLLABLES}) thiếu ngắt nhịp: «{seg.strip()[:70]}»"}
                        warnings.append(w); b_warns.append(w)

        report_beats.append({
            "id": b["id"],
            "label": b["label"],
            "syllables": n_syl,
            "duration_s": dur_s,
            "estimated_s": est_s,
            "rate_syl_s": rate,
            "rate_in_target": RATE_TARGET_MIN <= rate <= RATE_TARGET_MAX,
            "voice_ref": v_ref,
            "emotion_role": emo_role,
            "opener_toks": _norm_toks(clean)[:3],
            "warnings": b_warns,
        })

    # 2b. Hook / entry / bloat (Hiệp 27/11 về clip-06 v8: hook dài, vào ý chậm, beat phình)
    def _flag(code, beat_ids, message, target):
        w = {"code": code, "beat": beat_ids, "message": message}
        warnings.append(w)
        target["warnings"].append(w)

    if report_beats:
        b1 = report_beats[0]
        if b1["syllables"] > HOOK_MAX_SYL:
            _flag("HOOK_LONG", b1["id"],
                  f"{b1['id']}: hook {b1['syllables']} âm tiết (> {HOOK_MAX_SYL}, ~{b1['syllables']/NATURAL_SYL_PER_SEC:.0f}s) → ép gọn 9–20 âm tiết (3–6s), nghe phát hiểu ngay vấn đề", b1)
        if len(report_beats) > 1:
            b2 = report_beats[1]
            entry = b1["syllables"] + b2["syllables"]
            if entry > ENTRY_MAX_SYL:
                _flag("SLOW_ENTRY", f"{b1['id']}+{b2['id']}",
                      f"{b1['id']}+{b2['id']}: {entry} âm tiết (> {ENTRY_MAX_SYL}, ~{entry/NATURAL_SYL_PER_SEC:.0f}s) trước khi vào câu hỏi chính → mở bài lòng vòng, đưa câu hỏi lên sớm", b2)
        for rb in report_beats:
            if rb["syllables"] > BEAT_MAX_SYL:
                _flag("BEAT_BLOAT", rb["id"],
                      f"{rb['id']}: beat {rb['syllables']} âm tiết (> {BEAT_MAX_SYL}, ~{rb['syllables']/NATURAL_SYL_PER_SEC:.0f}s) → nhồi nhiều ý vào 1 beat, tách hoặc cắt ý phụ", rb)

    # 3. Consecutive beat opener repetition
    for prev, cur in zip(report_beats, report_beats[1:]):
        pt, ct = prev["opener_toks"], cur["opener_toks"]
        if not pt or not ct:
            continue
        same_bi = len(pt) >= 2 and len(ct) >= 2 and pt[:2] == ct[:2]
        same_starter = pt[0] == ct[0] and pt[0] in REPEATING_STARTERS
        if same_bi or same_starter:
            phrase = " ".join(ct[:2] if same_bi else ct[:1])
            w = {"code": "REPEAT_OPENER", "beat": f"{prev['id']}→{cur['id']}",
                 "message": f"{prev['id']}→{cur['id']}: 2 beat liên tiếp trùng cấu trúc mở đầu «{phrase}» → đổi nhịp mở câu để khỏi đều giọng"}
            warnings.append(w)
            cur["warnings"].append(w)

    # 4. Beat 1 vs approved archive hooks (opening structure / keywords)
    if beats and archive_hooks:
        for w in cross_clip_hook_warnings(beats[0]["text"], archive_hooks):
            warnings.append(w)
            if report_beats:
                report_beats[0]["warnings"].append(w)

    # 5. Emotional Trajectory & Cadence Contrast (F4, DL-082)
    # 5a. FLAT_CADENCE: >= 4 consecutive sentences with syllable length spread <= 3 (monotonous pacing)
    if len(all_sent_syls) >= FLAT_CADENCE_RUN:
        for i in range(len(all_sent_syls) - FLAT_CADENCE_RUN + 1):
            window = all_sent_syls[i : i + FLAT_CADENCE_RUN]
            lens = [x[1] for x in window]
            if max(lens) - min(lens) <= FLAT_CADENCE_SPREAD:
                bid_span = f"{window[0][0]}..{window[-1][0]}"
                w = {
                    "code": "FLAT_CADENCE",
                    "beat": bid_span,
                    "message": f"{bid_span}: {FLAT_CADENCE_RUN} câu liên tiếp có độ dài đều nhau ({lens} âm tiết, chênh ≤ {FLAT_CADENCE_SPREAD}) → thiếu tương phản nhịp kể dài (16–24) và câu đọng ngắn (6–10)",
                }
                warnings.append(w)
                tgt = next((rb for rb in report_beats if rb["id"] == window[-1][0]), report_beats[-1])
                tgt["warnings"].append(w)
                break

    # 5b. MISSING_VULNERABILITY_DIP: full script (>= 5 beats) lacking personal/vulnerability dip in first half
    if len(beats) >= MIN_BEATS_FOR_DIP_CHECK:
        first_half = " ".join(strip_markup(b["text"]) for b in beats[: max(2, len(beats) // 2)])
        if not VULNERABILITY_CUES_RE.search(first_half):
            w = {
                "code": "MISSING_VULNERABILITY_DIP",
                "beat": f"{beats[0]['id']}..{beats[max(1, len(beats)//2 - 1)]['id']}",
                "message": "Nửa đầu kịch bản chưa có nhịp chùng đồng cảm / cảm giác thật của người trong cuộc (Vulnerability Dip) → dễ nghe khô như đọc báo cáo",
            }
            warnings.append(w)
            report_beats[1]["warnings"].append(w)

    voice_ref_map = {rb["id"]: {"voice_ref": rb["voice_ref"], "emotion_role": rb["emotion_role"]} for rb in report_beats}

    return {
        "beats": report_beats,
        "warnings": warnings,
        "voice_ref_map": voice_ref_map,
        "total_syllables": total_syl,
        "estimated_total_s": round(total_est, 1),
        "ok": len(warnings) == 0,
    }


def extract_hook_audition_text(beats):
    """Extract first ~20s (Hook + Beat 2) spoken text for quick F5-TTS audition."""
    if not beats:
        return ""
    picked = beats[:2]
    text = " ".join(strip_markup(b["text"]) for b in picked if b.get("text"))
    # Keep at most ~20s (~70 syllables) at natural sentence boundary if Hook + Beat 2 is unusually long
    syls = syllables(text)
    if len(syls) <= HOOK_AUDITION_MAX_SYL:
        return text.strip()
    sents = [s.strip() for s in SENT_SPLIT_RE.split(text) if s.strip()]
    acc, cnt = [], 0
    for s in sents:
        n = len(syllables(s))
        if acc and cnt + n > HOOK_AUDITION_MAX_SYL:
            break
        acc.append(s)
        cnt += n
    return " ".join(acc).strip() or text.strip()


def resolve_audition_out(script_path, explicit_out=None):
    if explicit_out:
        return Path(explicit_out)
    p = Path(script_path).resolve()
    # If inside content/clips/<clip>/(archive|final)/script.md → <clip>/final/out/hook-audition.wav
    for parent in p.parents:
        if parent.name in ("archive", "final") and (parent.parent / "final").exists():
            return parent.parent / "final/out/hook-audition.wav"
    return p.parent / "final/out/hook-audition.wav"


def run_audition_hook(beats, script_path, voice_key="thai-son-v2", out_path=None, dry_run=False):
    """Synthesize the first ~20s (Hook + Beat 2) with pipeline/tts/f5tts_gen.py."""
    text = extract_hook_audition_text(beats)
    if not text:
        raise ValueError("no spoken hook text to audition")
    refs_json = P.VOICE_REFS / "voice-refs.json"
    refs = json.loads(refs_json.read_text(encoding="utf-8")) if refs_json.exists() else {}
    ref_cfg = refs.get(voice_key) or refs.get("thai-son") or {"wav": "thai-son.wav", "ref_text": "Hôm nay trời Sài Gòn mát mẻ, mình ngồi cà phê một chút rồi về nhà làm việc tiếp nha."}
    ref_wav = str(P.VOICE_REFS / ref_cfg["wav"])
    dest = resolve_audition_out(script_path, out_path)
    batch = {
        "ref": ref_wav,
        "ref_text": ref_cfg["ref_text"],
        "items": [{"t": text, "seed": 7, "speed": 1.0, "out": str(dest)}],
    }
    if dry_run:
        return {"out": str(dest), "text": text, "syllables": len(syllables(text)), "batch": batch, "dry_run": True}
    dest.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False, encoding="utf-8") as tf:
        json.dump(batch, tf, ensure_ascii=False, indent=1)
        batch_path = tf.name
    try:
        cmd = [P.F5_PYTHON, str(P.TTS / "f5tts_gen.py"), batch_path]
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=600)
        if r.returncode != 0 or not dest.exists():
            raise RuntimeError(f"f5tts_gen failed (exit {r.returncode}): {(r.stderr or r.stdout)[-400:]}")
    finally:
        if os.path.exists(batch_path):
            os.remove(batch_path)
    return {"out": str(dest), "text": text, "syllables": len(syllables(text)), "dry_run": False}


def format_report(res, script_path):
    lines = [
        f"Audio-Back QA: {script_path}",
        f"Tổng: {len(res['beats'])} beat · {res['total_syllables']} âm tiết · ước ~{res['estimated_total_s']}s (chuẩn nói {RATE_TARGET_MIN}–{RATE_TARGET_MAX} âm tiết/s)",
        "",
        "| Beat | Âm tiết | Thời lượng | Tốc độ (âm tiết/s) | Giọng F5 (gợi ý) | Trạng thái |",
        "|---|---:|---:|---:|---|---|",
    ]
    for b in res["beats"]:
        dur = f"{b['duration_s']}s" if b["duration_s"] else f"~{b['estimated_s']}s"
        st = "⚠ " + ", ".join(w["code"] for w in b["warnings"]) if b["warnings"] else "✔ ổn"
        vr = f"`{b.get('voice_ref', 'thai-son-v2')}` ({b.get('emotion_role', '')})"
        lines.append(f"| {b['id']} | {b['syllables']} | {dur} | {b['rate_syl_s']:.2f} | {vr} | {st} |")
    if res["warnings"]:
        lines += ["", f"Cảnh báo ({len(res['warnings'])}):"] + [f"  ⚠ {w['message']}" for w in res["warnings"]]
    else:
        lines += ["", "✔ Nhịp thở & độ dài câu đạt chuẩn văn nói tiếng Việt."]
    return "\n".join(lines)


def main():
    a = sys.argv[1:]
    if not a or a[0] in ("-h", "--help"):
        print(__doc__)
        return 0 if a else 2
    def opt(n, d=None):
        return a[a.index(n) + 1] if n in a else d
    script_path = next((x for x in a if not x.startswith("-")), None)
    if not script_path or not Path(script_path).exists():
        print(f"missing script file: {script_path}", file=sys.stderr)
        return 2
    md = Path(script_path).read_text(encoding="utf-8")
    beats = parse_beats(md)
    if not beats:
        print(f"✖ không đọc được beat nào từ {script_path} (cần dạng `N. **[bNN]** lời` hoặc bảng beat)", file=sys.stderr)
        return 1
    res = analyze_beats(beats, archive_hooks=load_archive_hooks())
    audition = None
    if "--audition-hook" in a:
        audition = run_audition_hook(
            beats, script_path,
            voice_key=opt("--voice", "thai-son-v2"),
            out_path=opt("--out"),
            dry_run="--dry-run" in a,
        )
    if "--json" in a:
        print(json.dumps({"precheck": res, "audition": audition}, ensure_ascii=False, indent=1))
    else:
        print(format_report(res, script_path))
        if audition:
            print(f"\nHook audition ({audition['syllables']} âm tiết, ~{round(audition['syllables'] / NATURAL_SYL_PER_SEC, 1)}s) → {audition['out']}"
                  + (" (dry-run)" if audition["dry_run"] else ""))
    return 0


if __name__ == "__main__":
    sys.exit(main())
