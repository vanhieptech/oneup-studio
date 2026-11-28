# TinyFish CLI wrapper (26/11/2026): parse JSON, discover TikTok links, degrade quietly without the binary.
import importlib.util, json, os, subprocess, tempfile, types, unittest
from unittest import mock
R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
spec_ = importlib.util.spec_from_file_location("tinyfish_client", os.path.join(R, "pipeline/scripts/tinyfish_client.py"))
tf = importlib.util.module_from_spec(spec_); spec_.loader.exec_module(tf)

SEARCH = {"results": [
    {"title": "Thói quen nhỏ", "url": "https://tiktok.com/@abc.xyz/video/7500043731798658312", "snippet": "ngâm chân", "date": "2025-05-03T02:40:15Z"},
    {"title": "dup", "url": "https://www.tiktok.com/@abc.xyz/video/7500043731798658312?lang=vi", "snippet": ""},
    {"title": "not a clip", "url": "https://www.tiktok.com/@abc.xyz", "snippet": ""}]}

def fake_run(payload, code=0):
    return lambda args, **kw: types.SimpleNamespace(returncode=code, stdout=json.dumps(payload), stderr="")

class TinyFish(unittest.TestCase):
    def setUp(self):
        self.d = tempfile.TemporaryDirectory(); self.exe = os.path.join(self.d.name, "tinyfish"); open(self.exe, "w").close()
    def tearDown(self): self.d.cleanup()

    def test_tiktok_discover_dedupes_and_parses(self):
        with mock.patch.object(tf.P, "TINYFISH_BIN", self.exe), mock.patch.object(subprocess, "run", fake_run(SEARCH)):
            c = tf.tiktok_discover(["thói quen"])
        self.assertEqual(len(c), 1); self.assertEqual(c[0]["creator"], "abc.xyz")
        self.assertEqual(c[0]["url"], "https://www.tiktok.com/@abc.xyz/video/7500043731798658312")

    def test_fetch_marks_blocked(self):
        with mock.patch.object(tf.P, "TINYFISH_BIN", self.exe), mock.patch.object(subprocess, "run", fake_run({"results": [{"url": "u", "title": "Site Maintenance"}]})):
            self.assertTrue(tf.fetch(["u"])[0]["blocked"])

    def test_missing_binary_returns_empty(self):
        # ego_fallback=False: prove TinyFish path alone returns [] when binary missing (DL-083 ego is optional).
        with mock.patch.object(tf.P, "TINYFISH_BIN", "/nope/tinyfish"):
            self.assertEqual(tf.search("x", ego_fallback=False), [])
            self.assertEqual(tf.tiktok_discover(["x"]), [])

    def test_nonzero_exit_returns_empty(self):
        with mock.patch.object(tf.P, "TINYFISH_BIN", self.exe), mock.patch.object(subprocess, "run", fake_run({}, code=1)):
            self.assertEqual(tf.search("x"), [])

if __name__ == "__main__":
    unittest.main()
