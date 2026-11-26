# voice-memo.py (26/11/2026): sample sentence picking for content/voice-profile.md §4.
import importlib.util, os, unittest
R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
spec_ = importlib.util.spec_from_file_location("voice_memo", os.path.join(R, "pipeline/scripts/voice-memo.py"))
vm = importlib.util.module_from_spec(spec_); spec_.loader.exec_module(vm)

class VoiceMemo(unittest.TestCase):
    def test_pick_samples_length_and_dedupe(self):
        segs = ["Ờ.", "Hôm qua mình định đi bộ mà trời mưa nên thôi luôn.", "Hôm qua mình định đi bộ mà trời mưa nên thôi luôn.",
                "Nói thật là mình lười lắm, mà cứ tưởng tại thiếu thời gian, hoá ra không phải vậy đâu."]
        s = vm.pick_samples(segs)
        self.assertEqual(len(s), 2); self.assertNotIn("Ờ.", s)
    def test_collect_filters_audio(self):
        self.assertEqual(vm.collect(["x.txt"]), [])

if __name__ == "__main__":
    unittest.main()


class VoiceFirstKeep(unittest.TestCase):
    """resources/vn-spoken/voice-first.md: ≥ 80% of the draft's content words come from Hiệp's memo."""
    MEMO = "Ờ thì hồi đó mình hứa chạy bộ mỗi sáng, mà được đúng ba hôm là bỏ, tại sáng nào cũng ngán cái lạnh."

    def test_restructured_in_his_words_passes(self):
        draft = "1. **[b01]** Mình hứa chạy bộ mỗi sáng. Được ba hôm là bỏ.\n2. **[b02]** Sáng nào cũng ngán cái lạnh nha."
        r, k, n, _ = vm.keep_ratio(self.MEMO, draft)
        self.assertGreaterEqual(r, 0.8)

    def test_rewritten_in_writer_words_fails(self):
        draft = "1. **[b01]** Thói quen vận động buổi sớm thường thất bại vì nhiệt độ thấp gây cảm giác khó chịu."
        self.assertLess(vm.keep_ratio(self.MEMO, draft)[0], 0.5)

    def test_citation_span_not_counted(self):
        draft = "1. **[b01]** Mình hứa chạy bộ mỗi sáng {nguồn: Lally và cộng sự năm 2010} được ba hôm là bỏ."
        self.assertEqual(vm.keep_ratio(self.MEMO, draft)[0], 1.0)
