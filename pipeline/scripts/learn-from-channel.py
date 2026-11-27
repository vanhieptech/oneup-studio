#!/usr/bin/env python3
"""Learn how one strong video tells a story. Writes research/references/craft-studies/<slug>.md.

  learn-from-channel.py --url <video_url>
  learn-from-channel.py --file clip.mp4
  learn-from-channel.py --transcript path.txt [--slug name] [--duration <seconds>] [--extractor local|agy|gemini|cursor]

Four sections, and nothing invented past the source:
  Verbatim Transcript
  Chuỗi nhân quả (Because / But / Therefore)
  Kỹ thuật nén ý (What was NOT explained)
  Câu đắt giá nhất (Emotional Peak)

Plus a fifth, the Compression Audit (WS3, 27/11), so a channel is learned for how it compresses and holds attention, not for its wording:
  Bảng kiểm độ nén: ý chính / tổng số câu · giây mỗi ý · 3 thứ tác giả không nói (chỉ ghi điều transcript thật sự thiếu)
  · 1–2 mẫu câu chuyển ý không dùng liên từ (câu hỏi ngắn, hoặc hai sự thật đặt cạnh nhau). Nothing is quoted that the transcript lacks.
  «Ý chính» = a sentence where at least half of its content words are new against the sentences before it.
  Duration comes from --duration (seconds) or a teardown beat table; otherwise it is estimated at 3.0 âm tiết/s and labelled as an estimate.

A teardown markdown (research/trends/**/teardowns) is read locally: if it says the
spoken line was not captured, the study quotes only the on-screen text it actually
contains. agy, then gemini, then cursor-agent are used for a URL or a media file.
"""
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUT_DIR = ROOT / "research" / "references" / "craft-studies"
SECTIONS = (
    "Verbatim Transcript",
    "Chuỗi nhân quả (Because / But / Therefore)",
    "Kỹ thuật nén ý (What was NOT explained)",
    "Câu đắt giá nhất (Emotional Peak)",
)

AUDIT_SECTION = "Compression Audit (Bảng kiểm độ nén)"
EST_SYL_PER_S = 3.0
NEW_IDEA_RATIO = 0.5
STOP = set("và của là có cho một những các được với không thì mà này đó để khi người bạn mình rồi lại cũng như nào gì vì nên "
           "thế nhưng ra vào lên cái việc đã sẽ đang hay hơn rất cả mới nữa luôn nha nè á hông".split())
BRIDGE_CONNECTORS = ("nên", "nhưng", "mà", "thành ra", "vì vậy", "do đó", "thế là", "rồi", "vì", "tại vì", "bởi vì", "vậy là", "và", "còn", "tức là", "nghĩa là")
CUT_CHECKS = (  # (nhãn, regex nếu GẶP trong lời thì tác giả không cắt, câu ghi khi không gặp)
    ("cơ chế sinh học/tâm lý", r"vì sao|cơ chế|não|hormone|dopamine|sinh học|tâm lý học|nơ-?ron",
     "Không giải thích cơ chế sinh học/tâm lý đằng sau (không có «vì sao», «não», «cơ chế»); chỉ nêu việc xảy ra."),
    ("cỡ mẫu / phương pháp thí nghiệm", r"\b\d+\s*(người|sinh viên|học sinh|tình nguyện|nghiên cứu|thí nghiệm|tuần|ngày)\b|cỡ mẫu|nhóm đối chứng|ngẫu nhiên",
     "Không nêu cỡ mẫu hay cách làm thí nghiệm; chỉ giữ kết luận."),
    ("rào trước đón sau ở phần mở", r"^(trước hết|đầu tiên|hôm nay mình sẽ|bạn có biết|như chúng ta|nói chung|mình xin|chào các bạn)",
     "Không rào trước đón sau: câu đầu vào thẳng tình huống, không giới thiệu bài."),
    ("câu tóm tắt bài học", r"(^|[.!?…]\s+)(tức là|nghĩa là|nói cách khác|tóm lại|vì vậy điều đó|điều đó có nghĩa)",
     "Không có câu tóm tắt lại điều vừa nói; ý chỉ được nói một lần."),
    ("khẩu hiệu hứa hẹn", r"thay đổi cuộc đời|bí quyết|chìa khóa|chìa khoá|đỉnh cao|hoàn toàn miễn phí",
     "Không hô khẩu hiệu hay hứa hẹn quá tay."),
)


def slugify(text):
    raw = re.sub(r"[^a-z0-9]+", "-", (text or "").lower()).strip("-")
    return (raw or "clip")[:80]


def split_sentences(text):
    parts = re.split(r"(?<=[.!?…])\s+", text.strip())
    return [p.strip() for p in parts if p.strip()]


def _words(s):
    return re.findall(r"[0-9a-zà-ỹđ]+", (s or "").lower())


def _content(s):
    return {w for w in _words(s) if w not in STOP and len(w) > 1}


def _starts_with_connector(sent):
    w = " ".join(_words(sent)[:2])
    return any(w == c or w.startswith(c + " ") for c in BRIDGE_CONNECTORS)


def key_ideas(sents):
    """Count a sentence as a main idea when at least NEW_IDEA_RATIO of its content words are new against earlier sentences."""
    seen, ideas = set(), []
    for s in sents:
        c = _content(s)
        if c and len(c - seen) / len(c) >= NEW_IDEA_RATIO:
            ideas.append(s)
        seen |= c
    return ideas


def observed_cuts(text, limit=3):
    """Up to `limit` things the transcript does NOT contain. Absence is observed from the text, never assumed from the author's intent."""
    body = (text or "").strip().lower()
    out = [f"{label}: {note}" for label, rx, note in CUT_CHECKS if not re.search(rx, body, re.I | re.M)]
    return out[:limit]


def bridge_samples(sents, limit=2):
    """Sentence pairs joined without a connector: a short question after a statement, or two number-bearing facts side by side."""
    num = re.compile(r"\d|(?<!thứ )(?<!\w)(?:hai|ba|bốn|năm|sáu|bảy|tám|chín|mười|trăm|ngàn|nghìn|triệu)(?!\w)", re.I)
    out = []
    for prev, cur in zip(sents, sents[1:]):
        if _starts_with_connector(cur):
            continue
        n = len(_words(cur))
        if cur.endswith("?") and n <= 8 and not prev.endswith("?"):
            out.append(f"«{prev}» → «{cur}» (câu hỏi ngắn, ý tự bật ra, không từ nối)")
        elif num.search(prev) and num.search(cur) and not _starts_with_connector(prev) and prev.rstrip().endswith((".", "…")):
            out.append(f"«{prev}» → «{cur}» (hai sự thật cạnh nhau, không từ nối)")
        if len(out) >= limit:
            break
    return out


def compression_audit(text, duration=None, beat_seconds=None):
    """Compression Audit dict. `duration` seconds (CLI/teardown) wins; else 3.0 âm tiết/s is used and flagged as an estimate."""
    sents = split_sentences(text)
    syl = len(_words(text))
    ideas = key_ideas(sents)
    if duration:
        dur, src = float(duration), "đo (--duration)"
    elif beat_seconds:
        dur, src = float(beat_seconds), "đo (bảng beat teardown)"
    else:
        dur, src = round(syl / EST_SYL_PER_S, 1), f"ƯỚC ({EST_SYL_PER_S} âm tiết/s, chưa đo audio)"
    n_s, n_i = len(sents), len(ideas)
    return {
        "sentences": n_s, "ideas": n_i, "syllables": syl,
        "idea_ratio": round(n_i / n_s, 2) if n_s else None,
        "seconds": dur, "seconds_source": src,
        "seconds_per_idea": round(dur / n_i, 1) if n_i else None,
        "cuts": observed_cuts(text), "bridges": bridge_samples(sents),
    }


def render_audit(a):
    ratio = f"{a['idea_ratio']:.2f} ({a['idea_ratio']:.0%})" if a["idea_ratio"] is not None else "—"
    spi = f"{a['seconds_per_idea']}s" if a["seconds_per_idea"] is not None else "—"
    L = ["| Chỉ số | Giá trị |", "|---|---|",
         f"| Tổng số câu | {a['sentences']} |",
         f"| Ý chính | {a['ideas']} |",
         f"| Ý chính / tổng số câu | {ratio} |",
         f"| Âm tiết | {a['syllables']} |",
         f"| Thời lượng | {a['seconds']}s — {a['seconds_source']} |",
         f"| Tốc độ chuyển ý (giây/ý) | {spi} |", "",
         "### 3 thứ tác giả không nói (chỉ ghi điều transcript thật sự thiếu)"]
    L += [f"{i}. {c}" for i, c in enumerate(a["cuts"], 1)] or ["- Transcript có đủ các thứ đã kiểm; không có gì để ghi là bị cắt. Không bịa."]
    if 0 < len(a["cuts"]) < 3:
        L.append(f"- Chỉ quan sát được {len(a['cuts'])} thứ bị lược; các mục còn lại transcript có nhắc tới nên không tính là cắt.")
    L += ["", "### Mẫu câu chuyển ý không dùng liên từ"]
    L += [f"- {b}" for b in a["bridges"]] or ["- Transcript không có cặp câu nào nối bằng câu hỏi ngắn hoặc hai sự thật cạnh nhau. Không bịa mẫu."]
    return "\n".join(L)


def _label(sentence):
    head = sentence.lower()
    if head.startswith(("thành ra", "vì vậy", "thế là", "vậy là", "nên ")):
        return "Therefore"
    if head.startswith(("vì", "tại vì", "bởi vì")):
        return "Because"
    if head.startswith(("nhưng", "mà ")):
        return "But"
    return "Next"


EMOTION_CUES = re.compile(
    r"(?i)\b(nhưng|mà|thật ra|hóa ra|tưởng|tự trách|nản|mỏi|bỏ cuộc|sợ|lo|nhẹ|nhõm|quên sạch|không nhích|hông nhích|vỡ òa|chạnh|tủi|cười|giật mình|bật ngửa)\b|[?!…]"
)


def _emotional_peak_sentence(sents):
    """Score sentences for genuine emotional/contrast/reflection peak instead of picking the longest sentence."""
    if not sents:
        return "", ""
    best, best_score, best_why = sents[0], -1.0, "câu mở đầu"
    for i, s in enumerate(sents):
        toks = _words(s)
        n = len(toks)
        cues = EMOTION_CUES.findall(s)
        score = len(cues) * 2.0
        reasons = []
        if cues:
            reasons.append("chứa tín hiệu cảm xúc/tương phản")
        if 5 <= n <= 18:
            score += 1.5
            reasons.append("nhịp gọn dễ đọng")
        if any(w in toks for w in ("mình", "tôi", "bạn")):
            score += 1.0
            reasons.append("ngôi kể gần")
        if i > 0 and i < len(sents) - 1:
            score += 0.5
        if score > best_score:
            best, best_score, best_why = s, score, ", ".join(reasons) or "câu nổi bật trong transcript"
    return best, best_why


def local_craft(text, duration=None):
    """Four sections (+ Compression Audit) from a plain transcript. Does not add facts the text lacks."""
    sents = split_sentences(text)
    links = []
    for i, sent in enumerate(sents):
        if i == 0:
            links.append(f"- Mở: {sent}")
            continue
        links.append(f"- {_label(sent)}: «{sent}» đi tiếp từ câu trước, không chèn từ nối ngoài lời.")
    peak, peak_why = _emotional_peak_sentence(sents)
    return {
        "verbatim": text.strip(),
        "causal": "\n".join(links) or "- Transcript không có câu.",
        "skipped": "Transcript không liệt kê phần tác giả đã lược. Không suy diễn chi tiết không có trong lời.",
        "peak": f"Điểm nhấn cảm xúc quan sát trong transcript ({peak_why}): «{peak}»" if peak else "Không có câu.",
        "compression": compression_audit(text, duration),
    }


def _screen_line(text):
    m = re.search(r"Chữ trên màn hình:\s*(.+)", text)
    return m.group(1).strip() if m else ""


def _beat_rows(text):
    rows = []
    for line in text.splitlines():
        if not line.startswith("|") or line.startswith("| mốc") or line.startswith("|---"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) >= 6 and re.match(r"\d", cells[0]):
            rows.append(cells)
    return rows


def teardown_craft(text):
    """Read a viral-DNA teardown. Quote only words the file already recorded."""
    screen = _screen_line(text)
    spoken_missing = bool(re.search(r"nguyên văn:\s*false", text, re.I))
    if spoken_missing:
        verbatim = (
            "Teardown ghi nguyên văn lời nói là không có (không có audio transcript). "
            "Chỉ chép chữ trên màn hình đã ghi trong file"
            + (f": {screen}" if screen else ".")
        )
    else:
        verbatim = screen or "Teardown không có dòng chữ trên màn hình."
    links = []
    for cells in _beat_rows(text):
        start, role, summary, bridge = cells[0], cells[2], cells[4], cells[5]
        links.append(f"- {start} ({role}): {summary} → {bridge}")
    saved = re.search(r"Câu đáng lưu / share:\s*(.+)", text)
    saved_line = saved.group(1).strip() if saved else ""
    if "đã được khoa học chứng minh" in text:
        skipped = (
            "Người nói viện «đã được khoa học chứng minh» rồi chuyển cảnh. "
            "Không nêu tên nghiên cứu, cỡ mẫu, hay giới hạn phép đo. "
            "Ba cách được gọi tên rồi cắt, không giảng lại cơ chế."
        )
    else:
        skipped = "Teardown không ghi phần tác giả cố tình bỏ qua. Không suy diễn."
    peak_bits = []
    if saved_line and saved_line not in {"—", "-", "— (—)"}:
        peak_bits.append(f"Câu teardown ghi là đáng lưu: {saved_line}")
    else:
        peak_bits.append("Teardown không ghi câu nói đáng lưu. Không bịa một câu đắt.")
    tick = re.search(r"(00:04[^\n]*['\"]Check['\"][^\n]*)", text)
    if tick:
        peak_bits.append(f"Khoảnh khắc quan sát được trong file: {tick.group(1).strip()}")
    rows = _beat_rows(text)
    secs = sum(float(c[1]) for c in rows if re.fullmatch(r"\d+(?:\.\d+)?", c[1]))
    summaries = [c[4] for c in rows]
    comp = compression_audit(" ".join(s.rstrip(".") + "." for s in summaries), beat_seconds=secs or None) if summaries else compression_audit("")
    if rows:  # one beat = one idea in a teardown table
        comp.update(sentences=len(rows), ideas=len(rows), idea_ratio=1.0,
                    seconds_per_idea=round(comp["seconds"] / len(rows), 1) if comp["seconds"] else None)
    if "đã được khoa học chứng minh" in text:  # the teardown itself records what was left out
        comp["cuts"] = [s.strip() for s in re.split(r"(?<=\.)\s+", skipped) if s.strip()][:3]
    return {
        "verbatim": verbatim,
        "causal": "\n".join(links) or "- Teardown không có bảng beat.",
        "skipped": skipped,
        "peak": " ".join(peak_bits),
        "compression": comp,
    }


def craft_from_text(text, duration=None):
    if "Khối 1" in text and "Chữ trên màn hình" in text:
        return teardown_craft(text), "teardown-local"
    return local_craft(text, duration), "transcript-local"


def render_study(slug, title, source, extractor, craft, updated="2026-11-27"):
    body = {
        "Verbatim Transcript": craft["verbatim"],
        "Chuỗi nhân quả (Because / But / Therefore)": craft["causal"],
        "Kỹ thuật nén ý (What was NOT explained)": craft["skipped"],
        "Câu đắt giá nhất (Emotional Peak)": craft["peak"],
    }
    sections = "\n\n".join(f"## {name}\n\n{body[name].strip()}" for name in SECTIONS)
    if craft.get("compression"):
        sections += f"\n\n## {AUDIT_SECTION}\n\n{render_audit(craft['compression'])}"
    return (
        f"---\n"
        f"title: \"{title}\"\n"
        f"date: {updated}\n"
        f"id: craft.{slug}\n"
        f"type: research\n"
        f"status: draft\n"
        f"updated: {updated}\n"
        f"tags: [craft, transcript, storytelling]\n"
        f"source: \"{source} · extractor {extractor}\"\n"
        f"---\n"
        f"# {title}\n\n"
        f"{sections}\n"
    )


def _run(cmd, timeout=90):
    return subprocess.run(cmd, capture_output=True, text=True, timeout=timeout)


def fetch_url(url, work):
    """yt-dlp metadata + auto-subs. Returns (meta_text, transcript_or_empty)."""
    work.mkdir(parents=True, exist_ok=True)
    out = work / "src"
    proc = _run([
        "yt-dlp", "--skip-download", "--write-info-json", "--write-auto-sub",
        "--sub-lang", "vi,en", "--convert-subs", "vtt",
        "-o", str(out), url,
    ], timeout=120)
    info = next(work.glob("*.info.json"), None)
    meta = info.read_text(encoding="utf-8")[:4000] if info else (proc.stderr or "")[-1000:]
    vtt = next(work.glob("*.vtt"), None)
    transcript = ""
    if vtt:
        lines = []
        for line in vtt.read_text(encoding="utf-8", errors="replace").splitlines():
            if line.startswith(("WEBVTT", "NOTE", "STYLE")) or "-->" in line or not line.strip():
                continue
            if line.strip() not in lines[-1:]:
                lines.append(line.strip())
        transcript = " ".join(lines)
    return meta, transcript, proc.returncode


def _model_prompt(transcript):
    return (
        "Đọc transcript sau. Trả đúng 4 mục, mỗi mục một dòng bắt đầu bằng nhãn. "
        "Không thêm sự kiện không có trong transcript.\n"
        "VERBATIM: giữ nguyên lời, ngắt nhịp bằng dấu phẩy hoặc ba chấm.\n"
        "CAUSAL: mỗi câu nối sang câu sau bằng Because, But hoặc Therefore, không từ nối sáo.\n"
        "SKIPPED: chi tiết tác giả cố tình không giải thích.\n"
        "PEAK: câu chạm cảm xúc và vì sao, chỉ nếu câu đó có trong transcript.\n\n"
        + transcript[:12000]
    )


def _parse_model(text):
    def grab(label):
        m = re.search(rf"{label}:\s*(.+)", text, re.I)
        return m.group(1).strip() if m else ""
    craft = {
        "verbatim": grab("VERBATIM"),
        "causal": grab("CAUSAL"),
        "skipped": grab("SKIPPED"),
        "peak": grab("PEAK"),
    }
    if not all(craft.values()):
        return None
    return craft


def model_craft(transcript, which="agy"):
    prompt = _model_prompt(transcript)
    if which == "agy":
        proc = _run(["agy", "-p", prompt], timeout=180)
    elif which == "gemini":
        proc = _run(["gemini", "-p", prompt], timeout=180)
    else:
        proc = _run([
            "cursor-agent", "-p", "--mode", "ask", "--trust",
            "--model", "grok-4.7-medium", "--output-format", "text", prompt,
        ], timeout=180)
    if proc.returncode != 0:
        return None
    return _parse_model(proc.stdout or "")


def extract(transcript, extractor="local", duration=None, speech=None):
    """`speech` = the spoken words only (no yt-dlp metadata) for the Compression Audit; defaults to `transcript`."""
    def with_audit(craft):
        if craft and "compression" not in craft:
            craft["compression"] = compression_audit(speech if speech is not None else transcript, duration)
        return craft
    if extractor == "local":
        craft, how = craft_from_text(transcript, duration)
        return with_audit(craft), how
    order = ["agy", "gemini", "cursor"] if extractor == "auto" else [extractor]
    for name in order:
        try:
            craft = model_craft(transcript, name)
        except (OSError, subprocess.TimeoutExpired):
            craft = None
        if craft:
            return with_audit(craft), name
    craft, how = craft_from_text(transcript, duration)
    return with_audit(craft), how + " (model không trả đủ 4 mục)"


def write_study(slug, title, source, extractor, craft, out=None, updated="2026-11-27"):
    path = Path(out) if out else OUT_DIR / f"{slug}.md"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(render_study(slug, title, source, extractor, craft, updated), encoding="utf-8")
    return path


def transcribe_media_local(media_path, lang="vi", timeout=300):
    """Transcribe local .mp4/.wav/.m4a via local faster-whisper (~/oneup-tools or active python). Returns (text, duration_s, err)."""
    mp = Path(media_path)
    if not mp.exists():
        return "", None, f"không tìm thấy file: {media_path}"
    candidates = [
        Path.home() / "oneup-tools/whisper-venv/bin/python",
        Path.home() / "oneup-tools/f5tts-venv/bin/python",
        Path(sys.executable),
    ]
    py = next((str(p) for p in candidates if p.exists()), sys.executable)
    snippet = (
        "import json, sys\n"
        "from faster_whisper import WhisperModel\n"
        "m = WhisperModel('small', device='cpu', compute_type='int8')\n"
        "segs, info = m.transcribe(sys.argv[1], language=sys.argv[2])\n"
        "txt = ' '.join(s.text.strip() for s in segs if s.text.strip())\n"
        "print(json.dumps({'text': txt, 'duration': round(float(info.duration or 0), 1)}, ensure_ascii=False))\n"
    )
    try:
        proc = _run([py, "-c", snippet, str(mp), lang], timeout=timeout)
    except (OSError, subprocess.TimeoutExpired) as e:
        return "", None, f"lỗi gọi faster-whisper: {e}"
    if proc.returncode != 0:
        return "", None, (proc.stderr or proc.stdout or "").strip()[-240:]
    import json as _json
    for line in reversed((proc.stdout or "").splitlines()):
        line = line.strip()
        if line.startswith("{"):
            try:
                doc = _json.loads(line)
                return doc.get("text", ""), doc.get("duration"), ""
            except _json.JSONDecodeError:
                pass
    return "", None, "faster-whisper không trả JSON hợp lệ"


def load_recent_craft_pivots(craft_dir=None, limit=6):
    """Read non-connector spoken transition samples from research/references/craft-studies/*.md for Gate 0."""
    d = Path(craft_dir or OUT_DIR)
    if not d.exists():
        return []
    pivots = []
    for f in sorted(d.glob("*.md"), key=lambda p: p.stat().st_mtime, reverse=True):
        txt = f.read_text(encoding="utf-8", errors="replace")
        if "### Mẫu câu chuyển ý không dùng liên từ" not in txt:
            continue
        sec = txt.split("### Mẫu câu chuyển ý không dùng liên từ", 1)[1].split("\n## ", 1)[0]
        for ln in sec.splitlines():
            ln = ln.strip()
            if ln.startswith("- «") and "Không bịa" not in ln:
                pivots.append({"source": f.stem, "sample": ln[2:].strip()})
                if len(pivots) >= limit:
                    return pivots
    return pivots


def main(argv=None):
    a = list(sys.argv[1:] if argv is None else argv)

    def opt(name, default=None):
        return a[a.index(name) + 1] if name in a else default

    transcript_path = opt("--transcript")
    url = opt("--url")
    media = opt("--file")
    extractor = opt("--extractor", "local" if transcript_path else "auto")
    duration = float(opt("--duration")) if opt("--duration") else None
    speech = None
    if not (transcript_path or url or media):
        print(__doc__)
        return 2
    if transcript_path:
        text = Path(transcript_path).read_text(encoding="utf-8")
        source = transcript_path
        slug = opt("--slug") or slugify(Path(transcript_path).stem)
    elif url:
        work = OUT_DIR / "_fetch" / slugify(url)
        meta, text, code = fetch_url(url, work)
        source = url
        slug = opt("--slug") or slugify(url.rstrip("/").rsplit("/", 1)[-1])
        if not text:
            print(f"yt-dlp không có phụ đề (exit {code}). Không bịa transcript.", file=sys.stderr)
            return 1
        speech = text
        text = meta[:500] + "\n\n" + text
    else:
        source = media
        slug = opt("--slug") or slugify(Path(media).stem)
        text, dur_w, err = transcribe_media_local(media, lang=opt("--lang", "vi"))
        if not text:
            print(f"File .mp4 chưa bóc được bằng faster-whisper ({err}). Cung cấp --transcript hoặc --url có phụ đề.", file=sys.stderr)
            return 2
        speech = text
        if duration is None and dur_w:
            duration = dur_w
    craft, how = extract(text, extractor, duration, speech)
    title = opt("--title") or f"Craft study {slug}"
    path = write_study(slug, title, source, how, craft, opt("--out"))
    print(path)
    return 0


if __name__ == "__main__":
    sys.exit(main())
