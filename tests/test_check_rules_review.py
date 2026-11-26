# make-video §4b gate (26/11/2026): check-rules blocks gate 1 without final/review.md verdict ĐẠT for the current lines.
import importlib.util, os, tempfile
R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
spec_ = importlib.util.spec_from_file_location("check_rules_review", os.path.join(R, "pipeline/scripts/check-rules.py"))
cr = importlib.util.module_from_spec(spec_); spec_.loader.exec_module(cr)

SPEC = {"parts": [{"scenes": [{"lines": [{"text": "Bạn có hay bỏ dở thói quen?", "en": "Do you quit habits?"}]}], "sections": []}]}

def run(review=None, spec=SPEC):
    cr.res.clear()
    with tempfile.TemporaryDirectory() as d:
        if review is not None: open(os.path.join(d, "review.md"), "w", encoding="utf-8").write(review)
        cr.check_review(spec, d)
    return [(a, b) for a, b, _ in cr.res]

def fm(verdict, h=None, score=88):
    return f"---\ntitle: \"review\"\nverdict: {verdict}\nscore: {score}\nscript_hash: {h or cr.script_hash(SPEC)}\n---\nbody\n"

def test_missing_blocks(): assert run() == [("✖", "review")]
def test_dat_passes(): assert run(fm("ĐẠT — trình gate 1")) == [("✔", "review")]
def test_chua_dat_blocks(): assert run(fm("CHƯA ĐẠT — sửa nhỏ", score=80)) == [("✖", "review")]
def test_dat_ve_diem_warns(): assert run(fm("ĐẠT VỀ ĐIỂM — chờ Hiệp quyết C-1")) == [("⚠", "review")]
def test_stale_hash_blocks(): assert run(fm("ĐẠT", h="000000000000")) == [("✖", "review")]
def test_bad_verdict_blocks(): assert run(fm("ok")) == [("✖", "review")]
def test_hash_tracks_wording():
    changed = {"parts": [{"scenes": [{"lines": [{"text": "Bạn có hay bỏ dở thói quen không?", "en": "Do you quit habits?"}]}], "sections": []}]}
    assert cr.script_hash(changed) != cr.script_hash(SPEC)
