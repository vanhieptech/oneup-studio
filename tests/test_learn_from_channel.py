"""learn-from-channel.py: four craft sections, no invented speech."""
import importlib.util
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location(
    "learn_from_channel", ROOT / "pipeline/scripts/learn-from-channel.py")
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)


class LearnFromChannelTests(unittest.TestCase):
    def test_render_has_front_matter_and_four_sections(self):
        text = mod.render_study(
            "sample", "Craft study sample", "fixture", "transcript-local",
            {"verbatim": "Một câu.", "causal": "- Mở: Một câu.",
             "skipped": "Không suy diễn.", "peak": "«Một câu.»"})
        for key in ("title:", "date:", "id: craft.sample", "type: research",
                    "status: draft", "updated:", "tags:", "source:"):
            self.assertIn(key, text)
        for name in mod.SECTIONS:
            self.assertIn(f"## {name}", text)

    def test_local_craft_does_not_add_facts(self):
        craft = mod.local_craft("Mình mua giày. Nhưng mà tuần sau mình bỏ. Thành ra mình để yên.")
        self.assertNotIn("Lally", craft["verbatim"])
        self.assertNotIn("Lally", craft["causal"])
        self.assertIn("But", craft["causal"])
        self.assertIn("Therefore", craft["causal"])
        self.assertIn("Không suy diễn", craft["skipped"])

    def test_teardown_does_not_invent_spoken_words(self):
        raw = (
            "## Khối 1 — Hook\n"
            "- nguyên văn: False\n"
            "- Chữ trên màn hình: 3 cách giúp bạn / Check\n"
            "## Khối 2\n"
            "| mốc | giây | vai trò | chức năng | tóm ý | chuyển ý sang beat sau |\n"
            "|---|---|---|---|---|---|\n"
            "| 00:00–00:04 | 4 | dẫn dắt | — | Đặt 3 cách | Jump cut |\n"
            "## Khối 3\n"
            "- Câu đáng lưu / share: — (—)\n"
            "- 00:04 Chữ vàng 'Check' bật lên.\n"
        )
        craft = mod.teardown_craft(raw)
        self.assertIn("không có", craft["verbatim"].lower())
        self.assertIn("3 cách giúp bạn", craft["verbatim"])
        self.assertIn("Jump cut", craft["causal"])
        self.assertIn("Không bịa", craft["peak"])
        self.assertNotIn("mình học", craft["verbatim"])

    def test_cli_writes_study(self):
        with tempfile.TemporaryDirectory() as d:
            src = Path(d) / "note.txt"
            src.write_text("Mình chạy. Nhưng mà chân mỏi. Thành ra mình nghỉ.", encoding="utf-8")
            out = Path(d) / "out.md"
            code = mod.main(["--transcript", str(src), "--slug", "note", "--out", str(out), "--extractor", "local"])
            self.assertEqual(code, 0)
            body = out.read_text(encoding="utf-8")
            self.assertIn("id: craft.note", body)
            self.assertIn("## Verbatim Transcript", body)
            self.assertIn("Mình chạy.", body)


if __name__ == "__main__":
    unittest.main()
