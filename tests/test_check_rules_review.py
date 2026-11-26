# make-video §4b gate: final/review.md must carry verdict ĐẠT for the current spoken words (draft or spec) and answer every Hiệp note.
import importlib.util, os, tempfile
R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
spec_ = importlib.util.spec_from_file_location("check_rules_review", os.path.join(R, "pipeline/scripts/check-rules.py"))
cr = importlib.util.module_from_spec(spec_); spec_.loader.exec_module(cr)

SPEC = {"parts": [{"scenes": [{"lines": [{"text": "Bạn có hay **bỏ dở** thói quen?", "en": "Do you quit habits?"}]}], "sections": []}]}
DRAFT = "# nháp\n\n1. **[Hook]** Bạn có hay {nhấn: bỏ dở} thói quen?\n"

def run(review=None, spec=SPEC, want=None, feedback=None):
    cr.res.clear()
    with tempfile.TemporaryDirectory() as d:
        if review is not None: open(os.path.join(d, "review.md"), "w", encoding="utf-8").write(review)
        if feedback is not None: open(os.path.join(d, "feedback.md"), "w", encoding="utf-8").write(feedback)
        cr.check_review(spec, d, want=want)
    return [(a, b) for a, b, _ in cr.res]

def fm(verdict, h=None, score=88, extra=""):
    return f"---\ntitle: \"review\"\nverdict: {verdict}\nscore: {score}\nscript_hash: {h or cr.script_hash(SPEC)}\n{extra}---\nbody\n"

FB = "| thời gian | bản | lời Hiệp | đã xử lý |\n|---|---|---|---|\n| 2026-11-26 06:47 | 4b16165 | «xàm» | b02 |\n| 2026-11-26 06:55 | 8df074e | «rời rạc» | khung mạch |\n"

def test_missing_blocks(): assert run() == [("✖", "review")]
def test_dat_passes(): assert run(fm("ĐẠT — trình gate 1")) == [("✔", "review")]
def test_chua_dat_blocks(): assert run(fm("CHƯA ĐẠT — sửa nhỏ", score=80)) == [("✖", "review")]
def test_dat_ve_diem_warns(): assert run(fm("ĐẠT VỀ ĐIỂM — chờ Hiệp quyết C-1")) == [("⚠", "review")]
def test_stale_hash_blocks(): assert run(fm("ĐẠT", h="000000000000")) == [("✖", "review")]
def test_bad_verdict_blocks(): assert run(fm("ok")) == [("✖", "review")]
def test_hash_tracks_wording():
    changed = {"parts": [{"scenes": [{"lines": [{"text": "Bạn có hay bỏ dở thói quen không?"}]}], "sections": []}]}
    assert cr.script_hash(changed) != cr.script_hash(SPEC)
def test_draft_and_spec_same_hash_ignoring_markup():
    assert cr.draft_hash(DRAFT) == cr.script_hash(SPEC)
def test_hash_keeps_tones():
    a = {"parts": [{"scenes": [{"lines": [{"text": "ma"}]}], "sections": []}]}
    b = {"parts": [{"scenes": [{"lines": [{"text": "má"}]}], "sections": []}]}
    assert cr.script_hash(a) != cr.script_hash(b)
def test_hash_with_label_text_accepted():
    assert run(fm("ĐẠT", h=f"\"draft-{cr.script_hash(SPEC)} (ghi chú)\"")) == [("✔", "review")]
def test_review_on_draft_hash():
    assert run(fm("ĐẠT", h=cr.draft_hash(DRAFT)), spec=None, want=cr.draft_hash(DRAFT)) == [("✔", "review")]
def test_feedback_unseen_blocks():
    assert run(fm("ĐẠT", extra="feedback_seen: 1\n"), feedback=FB) == [("✖", "review")]
def test_feedback_missing_field_blocks():
    assert run(fm("ĐẠT"), feedback=FB) == [("✖", "review")]
def test_feedback_all_seen_passes():
    assert run(fm("ĐẠT", extra="feedback_seen: 2\n"), feedback=FB) == [("✔", "review")]
