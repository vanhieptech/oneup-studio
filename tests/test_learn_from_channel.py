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


class CompressionAuditTests(unittest.TestCase):
    SAMPLE = ("Mình mới mua đôi giày chạy, tối nào cũng đi mười phút. Sáng thứ sáu bước lên cân, không nhích ký nào. "
              "Bỏ cuộc chưa? Lally đo năm 2010, nhanh mười tám ngày. Chậm hai trăm năm mươi tư ngày. Tối nay xỏ giày.")

    def test_metrics_ratio_and_seconds_per_idea(self):
        a = mod.compression_audit(self.SAMPLE, duration=60)
        self.assertEqual(a["sentences"], 6)
        self.assertGreaterEqual(a["ideas"], 1)
        self.assertLessEqual(a["ideas"], a["sentences"])
        self.assertAlmostEqual(a["idea_ratio"], round(a["ideas"] / a["sentences"], 2))
        self.assertAlmostEqual(a["seconds_per_idea"], round(60 / a["ideas"], 1))
        self.assertIn("đo", a["seconds_source"])

    def test_repeated_sentence_is_not_a_new_idea(self):
        a = mod.compression_audit("Mình xỏ giày đi bộ. Mình xỏ giày đi bộ. Cân hông nhích ký nào.", duration=9)
        self.assertEqual(a["sentences"], 3)
        self.assertEqual(a["ideas"], 2)

    def test_duration_is_labelled_estimate_without_measurement(self):
        a = mod.compression_audit(self.SAMPLE)
        self.assertIn("ƯỚC", a["seconds_source"])
        self.assertEqual(a["seconds"], round(a["syllables"] / mod.EST_SYL_PER_S, 1))

    def test_three_cuts_are_observed_absences_only(self):
        a = mod.compression_audit(self.SAMPLE, duration=60)
        self.assertEqual(len(a["cuts"]), 3)
        joined = " ".join(a["cuts"])
        for label in ("cơ chế", "cỡ mẫu", "rào trước đón sau"):
            self.assertIn(label, joined)

    def test_cut_is_not_claimed_when_transcript_contains_it(self):
        a = mod.compression_audit("Hôm nay mình sẽ nói về giày. Nghiên cứu theo dõi 96 người. Vì sao? Do cơ chế của não.", duration=20)
        joined = " ".join(a["cuts"])
        self.assertNotIn("cơ chế sinh học/tâm lý", joined)
        self.assertNotIn("cỡ mẫu", joined)
        self.assertNotIn("rào trước đón sau", joined)

    def test_bridges_use_no_connector_and_quote_the_text(self):
        a = mod.compression_audit(self.SAMPLE, duration=60)
        self.assertTrue(1 <= len(a["bridges"]) <= 2)
        for b in a["bridges"]:
            self.assertIn("không từ nối", b)
        self.assertTrue(any("Bỏ cuộc chưa?" in b for b in a["bridges"]))
        self.assertFalse(any("thứ sáu" in b and "hai sự thật" in b and "Mình mới mua" in b for b in a["bridges"]))

    def test_bridge_skips_pairs_that_open_with_a_connector(self):
        a = mod.compression_audit("Mình mua giày. Nên mình đi. Nhưng mà cân hông nhích.", duration=9)
        self.assertEqual(a["bridges"], [])
        self.assertIn("Không bịa", mod.render_audit(a))

    def test_render_study_has_compression_audit_section(self):
        craft = mod.local_craft(self.SAMPLE, 60)
        text = mod.render_study("s", "Craft study s", "fixture", "transcript-local", craft)
        self.assertIn(f"## {mod.AUDIT_SECTION}", text)
        for key in ("Ý chính / tổng số câu", "Tốc độ chuyển ý (giây/ý)", "3 thứ tác giả không nói", "Mẫu câu chuyển ý không dùng liên từ"):
            self.assertIn(key, text)

    def test_render_without_compression_keeps_old_shape(self):
        text = mod.render_study("s", "t", "f", "x", {"verbatim": "a", "causal": "b", "skipped": "c", "peak": "d"})
        self.assertNotIn(mod.AUDIT_SECTION, text)

    def test_teardown_reports_beat_seconds_and_recorded_cuts(self):
        raw = ("## Khối 1 — Hook\n- nguyên văn: False\n- Chữ trên màn hình: 3 cách\n"
               "| mốc | giây | vai trò | chức năng | tóm ý | chuyển ý sang beat sau |\n|---|---|---|---|---|---|\n"
               "| 00:00–00:04 | 4 | dẫn dắt | — | Đặt 3 cách | Jump cut |\n"
               "| 00:04–00:20 | 16 | giải thích | — | Cách một | Jump cut |\n"
               "Người nói viện «đã được khoa học chứng minh» rồi chuyển cảnh.\n")
        c = mod.teardown_craft(raw)["compression"]
        self.assertEqual((c["sentences"], c["ideas"], c["seconds"]), (2, 2, 20.0))
        self.assertEqual(c["seconds_per_idea"], 10.0)
        self.assertTrue(len(c["cuts"]) <= 3 and any("cỡ mẫu" in x for x in c["cuts"]))

    def test_cli_duration_flag_writes_audit(self):
        with tempfile.TemporaryDirectory() as d:
            src = Path(d) / "n.txt"; src.write_text(self.SAMPLE, encoding="utf-8")
            out = Path(d) / "o.md"
            self.assertEqual(mod.main(["--transcript", str(src), "--slug", "n", "--out", str(out), "--duration", "60"]), 0)
            body = out.read_text(encoding="utf-8")
            self.assertIn(f"## {mod.AUDIT_SECTION}", body)
            self.assertIn("60.0s — đo (--duration)", body)


if __name__ == "__main__":
    unittest.main()
