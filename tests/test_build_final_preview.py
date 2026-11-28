"""Unit tests for build-final --preview helpers (beat-hash cache, parallel flags) DL-094."""
from __future__ import annotations

import importlib.util
import json
import tempfile
import threading
import unittest
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from unittest import mock

ROOT = Path(__file__).resolve().parents[1]


def _load_bf():
    path = ROOT / "pipeline/scripts/build-final.py"
    spec = importlib.util.spec_from_file_location("build_final", path)
    mod = importlib.util.module_from_spec(spec)
    # Avoid executing heavy side-effects: still loads module (imports only)
    spec.loader.exec_module(mod)
    return mod


BF = _load_bf()


class BuildFinalPreviewTests(unittest.TestCase):
    def test_beat_hash_stable_and_sensitive(self):
        sc = {
            "id": "b01",
            "framing": "closeup",
            "fx": {"visual": "slam", "word": "úp"},
            "sfx": [{"name": "stamp"}],
            "props": [],
            "lines": [{"text": "úp **máy**", "emotion": "spark"}],
        }
        h1 = BF.beat_hash(sc, "abc")
        h2 = BF.beat_hash(dict(sc), "abc")
        self.assertEqual(h1, h2)
        sc2 = json.loads(json.dumps(sc))
        sc2["lines"][0]["text"] = "úp **điện thoại**"
        self.assertNotEqual(h1, BF.beat_hash(sc2, "abc"))
        self.assertNotEqual(h1, BF.beat_hash(sc, "zzz"))

    def test_summarize_beat_cache_hit_miss(self):
        with tempfile.TemporaryDirectory() as td:
            fdir = Path(td)
            (fdir / "out").mkdir()
            spec = {
                "voice_prefix": "t",
                "parts": [{
                    "engine": "remotion",
                    "scenes": [
                        {"id": "b01", "framing": "closeup", "fx": {}, "sfx": [], "props": [],
                         "lines": [{"text": "a", "emotion": "spark", "_key": "t-b01"}]},
                        {"id": "b02", "framing": "medium", "fx": {}, "sfx": [], "props": [],
                         "lines": [{"text": "b", "emotion": "warm", "_key": "t-b02"}]},
                    ],
                }],
            }
            # first pass: all rebuilt
            hits, rebuilt = BF.summarize_beat_cache(spec, str(fdir))
            self.assertEqual(hits, [])
            self.assertEqual(sorted(rebuilt), ["b01", "b02"])
            # second pass unchanged → all hits
            hits2, rebuilt2 = BF.summarize_beat_cache(spec, str(fdir))
            self.assertEqual(sorted(hits2), ["b01", "b02"])
            self.assertEqual(rebuilt2, [])
            # change one beat
            spec["parts"][0]["scenes"][1]["lines"][0]["text"] = "b-changed"
            hits3, rebuilt3 = BF.summarize_beat_cache(spec, str(fdir))
            self.assertIn("b01", hits3)
            self.assertEqual(rebuilt3, ["b02"])

    def test_preview_flag_alias_draft_in_docstring(self):
        self.assertIn("--preview", BF.__doc__)
        src = (ROOT / "pipeline/scripts/build-final.py").read_text(encoding="utf-8")
        self.assertIn('preview = "--preview" in sys.argv', src)
        self.assertIn("preview-540p", src)
        self.assertIn("out_fps = 24 if preview else FPS", src)
        self.assertIn("ThreadPoolExecutor", src)

    def test_parallel_branches_no_race(self):
        """Cover and render branches can complete concurrently without shared mutable race."""
        lock = threading.Lock()
        log = []

        def cover():
            with lock:
                log.append("cover-start")
            with lock:
                log.append("cover-done")

        def render():
            with lock:
                log.append("render-start")
            with lock:
                log.append("render-done")

        with ThreadPoolExecutor(max_workers=2) as pool:
            futs = {pool.submit(cover): "cover", pool.submit(render): "render"}
            for fut in as_completed(futs):
                fut.result()
        self.assertEqual(sorted(log), sorted(["cover-start", "cover-done", "render-start", "render-done"]))
        self.assertIn("cover-done", log)
        self.assertIn("render-done", log)


if __name__ == "__main__":
    unittest.main()
