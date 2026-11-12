"""L-103 --story-hook tests: research wording in the first 2 hook sentences is a ⚠ hint only; no audio, image or render."""
import importlib.util
import os
import subprocess
import sys
import tempfile
import unicodedata
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CR = ROOT / "pipeline/scripts/check-rules.py"
spec = importlib.util.spec_from_file_location("check_rules_l103", CR)
cr = importlib.util.module_from_spec(spec)
spec.loader.exec_module(cr)

STORY = "1. Chủ nhật bạn đọc lại bài viết về tiêu tiền, vậy mà thứ ba bạn chỉ nhớ cái tiêu đề.\n"


def concept(cid, second):
    return f"## {cid} — x\n{STORY}2. {second}\n"


def run(md):
    cr.res.clear()
    cr.check_story_hook(cr.l102_hooks(md), "t.md")
    return [(sym, msg) for sym, rule, msg in cr.res if rule == "L-103"]


class StoryHookTests(unittest.TestCase):
    def assert_hit(self, sentence, phrase):
        out = run(concept("C1", sentence))
        self.assertEqual([s for s, _ in out], ["⚠"], out)
        self.assertIn(f"«{phrase}»", out[0][1])
        self.assertIn("không phải bằng chứng", out[0][1])

    def test_theo_mot_thi_nghiem(self):
        self.assert_hit("Theo một thí nghiệm, lượt thứ hai nên gấp bài lại.", "theo một thí nghiệm")

    def test_trong_mot_thi_nghiem(self):
        self.assert_hit("Trong một thí nghiệm, lượt thứ hai được gấp bài lại.", "trong một thí nghiệm")

    def test_trung_binh(self):
        self.assert_hit("Hai ngày sau, TRUNG BÌNH nhóm đó nhớ nhiều ý hơn.", "trung bình")

    def test_nguoi_ta(self):
        self.assert_hit("Hai ngày sau, người ta nhớ nhiều ý hơn.", "người ta")

    def test_nfd_input_is_normalized(self):
        self.assert_hit(unicodedata.normalize("NFD", "Hai ngày sau, người ta nhớ nhiều ý hơn."), "người ta")

    def test_word_boundary(self):
        out = run(concept("C1", "Bạn mở lại cuốn sổ trung bìnhxyz rồi bỏ xuống."))
        self.assertEqual([s for s, _ in out], ["✔"])

    def test_third_sentence_not_flagged(self):
        md = concept("C1", "Bạn mở lại cuốn sổ, rồi gấp vào.") + "3. Theo một thí nghiệm, trung bình người ta nhớ nhiều hơn.\n"
        self.assertEqual([s for s, _ in run(md)], ["✔"])

    def test_two_sentences_on_one_numbered_line(self):
        md = "## C1 — x\n1. Bạn đọc lại bài. Người ta bảo vậy là đủ.\n2. Rồi bạn quên.\n"
        out = run(md)
        self.assertEqual([s for s, _ in out], ["⚠"]); self.assertIn("câu 2 «người ta»", out[0][1])

    def test_per_concept_separation(self):
        md = concept("C1", "Bạn mở lại cuốn sổ, rồi gấp vào.") + concept("A'", "Theo một thí nghiệm, nhóm gấp bài nhớ hơn.")
        out = run(md)
        self.assertEqual([s for s, _ in out], ["✔", "⚠"])
        self.assertIn("A'", out[1][1]); self.assertNotIn("C1", out[1][1])

    def test_no_hook_is_info(self):
        self.assertEqual([s for s, _ in run("# tiêu đề\nkhông có hook\n")], ["ℹ"])

    def test_cli_warning_only_exit_zero(self):
        with tempfile.TemporaryDirectory() as d:
            p = os.path.join(d, "c.md")
            open(p, "w", encoding="utf8").write(concept("C1", "Theo một thí nghiệm, trung bình người ta nhớ hơn."))
            r = subprocess.run([sys.executable, str(CR), "--story-hook", p], capture_output=True, text=True)
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        self.assertIn("1 warning(s)", r.stdout); self.assertIn("0 error(s)", r.stdout)


if __name__ == "__main__":
    unittest.main()
