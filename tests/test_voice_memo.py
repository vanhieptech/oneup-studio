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
