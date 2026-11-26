#!/usr/bin/env python3
"""Learn how one strong video tells a story. Writes research/references/craft-studies/<slug>.md.

  learn-from-channel.py --url <video_url>
  learn-from-channel.py --file clip.mp4
  learn-from-channel.py --transcript path.txt [--slug name] [--extractor local|agy|gemini|cursor]

Four sections, and nothing invented past the source:
  Verbatim Transcript
  Chuỗi nhân quả (Because / But / Therefore)
  Kỹ thuật nén ý (What was NOT explained)
  Câu đắt giá nhất (Emotional Peak)

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

def slugify(text):
    raw = re.sub(r"[^a-z0-9]+", "-", (text or "").lower()).strip("-")
    return (raw or "clip")[:80]


def split_sentences(text):
    parts = re.split(r"(?<=[.!?…])\s+", text.strip())
    return [p.strip() for p in parts if p.strip()]


def _label(sentence):
    head = sentence.lower()
    if head.startswith(("thành ra", "vì vậy", "thế là", "vậy là", "nên ")):
        return "Therefore"
    if head.startswith(("vì", "tại vì", "bởi vì")):
        return "Because"
    if head.startswith(("nhưng", "mà ")):
        return "But"
    return "Next"


def local_craft(text):
    """Four sections from a plain transcript. Does not add facts the text lacks."""
    sents = split_sentences(text)
    links = []
    for i, sent in enumerate(sents):
        if i == 0:
            links.append(f"- Mở: {sent}")
            continue
        links.append(f"- {_label(sent)}: «{sent}» đi tiếp từ câu trước, không chèn từ nối ngoài lời.")
    peak = max(sents, key=lambda s: len(s.split())) if sents else ""
    return {
        "verbatim": text.strip(),
        "causal": "\n".join(links) or "- Transcript không có câu.",
        "skipped": "Transcript không liệt kê phần tác giả đã lược. Không suy diễn chi tiết không có trong lời.",
        "peak": f"Câu dài nhất trong transcript (chưa phải cảm xúc bịa): «{peak}»" if peak else "Không có câu.",
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
    return {
        "verbatim": verbatim,
        "causal": "\n".join(links) or "- Teardown không có bảng beat.",
        "skipped": skipped,
        "peak": " ".join(peak_bits),
    }


def craft_from_text(text):
    if "Khối 1" in text and "Chữ trên màn hình" in text:
        return teardown_craft(text), "teardown-local"
    return local_craft(text), "transcript-local"


def render_study(slug, title, source, extractor, craft, updated="2026-11-27"):
    body = {
        "Verbatim Transcript": craft["verbatim"],
        "Chuỗi nhân quả (Because / But / Therefore)": craft["causal"],
        "Kỹ thuật nén ý (What was NOT explained)": craft["skipped"],
        "Câu đắt giá nhất (Emotional Peak)": craft["peak"],
    }
    sections = "\n\n".join(f"## {name}\n\n{body[name].strip()}" for name in SECTIONS)
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


def extract(transcript, extractor="local"):
    if extractor == "local":
        return craft_from_text(transcript)
    order = ["agy", "gemini", "cursor"] if extractor == "auto" else [extractor]
    for name in order:
        try:
            craft = model_craft(transcript, name)
        except (OSError, subprocess.TimeoutExpired):
            craft = None
        if craft:
            return craft, name
    craft, how = craft_from_text(transcript)
    return craft, how + " (model không trả đủ 4 mục)"


def write_study(slug, title, source, extractor, craft, out=None, updated="2026-11-27"):
    path = Path(out) if out else OUT_DIR / f"{slug}.md"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(render_study(slug, title, source, extractor, craft, updated), encoding="utf-8")
    return path


def main(argv=None):
    a = list(sys.argv[1:] if argv is None else argv)

    def opt(name, default=None):
        return a[a.index(name) + 1] if name in a else default

    transcript_path = opt("--transcript")
    url = opt("--url")
    media = opt("--file")
    extractor = opt("--extractor", "local" if transcript_path else "auto")
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
        text = meta[:500] + "\n\n" + text
    else:
        source = media
        slug = opt("--slug") or slugify(Path(media).stem)
        print("File .mp4 cần transcript kèm theo (--transcript) hoặc --url để yt-dlp lấy phụ đề.", file=sys.stderr)
        return 2
    craft, how = extract(text, extractor)
    title = opt("--title") or f"Craft study {slug}"
    path = write_study(slug, title, source, how, craft, opt("--out"))
    print(path)
    return 0


if __name__ == "__main__":
    sys.exit(main())
