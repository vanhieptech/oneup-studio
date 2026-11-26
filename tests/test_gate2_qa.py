# gate2-qa.py + skills/video-qa/SKILL.md: multimodal Gate 2 QA prompt, 720p discovery, L-099 override, report generation.
import importlib.util, os, tempfile
from pathlib import Path

R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
s = importlib.util.spec_from_file_location("gate2_qa", os.path.join(R, "pipeline/scripts/gate2-qa.py"))
g2 = importlib.util.module_from_spec(s); s.loader.exec_module(g2)


def test_skill_prompt_loads_and_covers_rule34_axes():
    p = g2.load_prompt()
    for needle in ("L-033", "L-099", "4 giây", "QA_VERDICT", "[MM:SS]"):
        assert needle in p


def test_find_video_prefers_720p_render():
    with tempfile.TemporaryDirectory() as d:
        clip = Path(d) / "clip-99-demo"
        out = clip / "final/out"
        out.mkdir(parents=True)
        (out / "clip-99-final.mp4").write_bytes(b"full")
        v720 = out / "clip-99-720.mp4"
        v720.write_bytes(b"720p")
        assert g2.find_video(clip) == v720


def test_parse_qa_verdict_enforces_l099_hard_cap():
    assert g2.parse_qa_verdict("Ổn hết.\nQA_VERDICT: PASS", duration_s=165.0, channel="hi-oneup") == "PASS"
    # Even if model says PASS, actual duration >= 300s must force NEEDS_FIX (L-099)
    assert g2.parse_qa_verdict("Ổn hết.\nQA_VERDICT: PASS", duration_s=300.0, channel="hi-oneup") == "NEEDS_FIX"
    assert g2.parse_qa_verdict("Lỗi safe-zone.\nQA_VERDICT: NEEDS_FIX", duration_s=140.0, channel="hi-oneup") == "NEEDS_FIX"


def test_render_report_has_required_front_matter():
    md = g2.render_report(
        "clip-99-demo",
        Path(R) / "media/clips/clip-99-demo/clip-99-720.mp4",
        Path(R) / "content/clips/clip-99-demo/final/spec.json",
        {"width": 720, "height": 1280, "duration_s": 152.4},
        "hi-oneup",
        {"engine": "agy", "model": "gemini-4-neon", "response": "### Tóm tắt Gate 2 QA\nQA_VERDICT: PASS"},
        "2026-11-26",
    )
    for field in ("title:", "date:", "id:", "type: qa-report", "status: draft", "tags:", "source:", "qa_verdict: PASS"):
        assert field in md
