"""Comprehensive tests for OneUp Content Engine v2.0 (DL-082, F1..F6)."""
import importlib.util
import json
import os
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def _load(name, rel):
    sp = importlib.util.spec_from_file_location(name, str(ROOT / rel))
    mod = importlib.util.module_from_spec(sp)
    sp.loader.exec_module(mod)
    return mod


rf = _load("radar_fetch_v2", "pipeline/scripts/radar-fetch.py")
lfc = _load("learn_from_channel_v2", "pipeline/scripts/learn-from-channel.py")
td = _load("teardown_v2", "pipeline/scripts/teardown.py")
tm = _load("trend_match_v2", "pipeline/scripts/trend-match.py")
g0 = _load("gate0_v2", "pipeline/scripts/gate0.py")
ap = _load("audio_precheck_v2", "pipeline/scripts/audio-precheck.py")
sa = _load("script_arena_v2", "pipeline/scripts/script-arena.py")
gs = _load("golden_sync_v2", "pipeline/scripts/golden-sync.py")
ic = _load("ideate_clip_v2", "pipeline/scripts/ideate-clip.py")
arc_lib = _load("arc_library_v2", "pipeline/arc_library.py")


class ContentEngineV2Tests(unittest.TestCase):
    # --- F1: Teardown prompt, Radar v2 (southern_story_voice + velocity/engagement), learn-from-channel, ARC format isolation ---
    def test_f1_gemini_teardown_single_prompt_with_emotional_arc(self):
        raw = (ROOT / "docs/prompts/gemini-teardown.md").read_text(encoding="utf-8")
        self.assertEqual(raw.count("\n<<<PROMPT\n"), 1)
        self.assertEqual(raw.count("\nPROMPT>>>"), 1)
        prompt = td.load_prompt()
        self.assertIn("emotional_arc", prompt)
        self.assertIn("spoken_pivots", prompt)
        self.assertIn("format_compatibility", prompt)

    def test_f1_radar_southern_voice_and_velocity_fallback(self):
        cfg = {
            "min_ratio": 3.0,
            "min_views_per_day": 15000,
            "min_engagement_intensity": 0.015,
            "min_abs_views_for_velocity": 50000,
            "channels": [
                {
                    "handle": "vietcetera",
                    "platform": "youtube",
                    "role": "southern_story_voice",
                    "format_compatibility": "story_metaphor",
                    "url": "https://www.youtube.com/@Vietcetera/shorts",
                    "followers": 0,
                    "niche": ["storytelling"],
                    "niche_verified": True,
                }
            ],
            "topics": {"storytelling": ["kể chuyện"]},
        }
        # All 3 videos consistently get ~500k views (ratio_m = 1.0x < 3.0), but high engagement triggers velocity/engagement fallback
        def big_channel_fetcher(url, limit):
            return [
                {"id": "s1", "title": "Chuyện Sài Gòn", "view_count": 500000, "comment_count": 3000, "share_count": 500},
                {"id": "s2", "title": "Chuyện Sài Gòn 2", "view_count": 500000, "comment_count": 100, "share_count": 10},
                {"id": "s3", "title": "Chuyện Sài Gòn 3", "view_count": 500000, "comment_count": 80, "share_count": 5},
            ], ""

        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            cfg_p = root / "radar.yaml"
            cfg_p.write_text(json.dumps(cfg), encoding="utf-8")
            res = rf.run_fetch("2026-11-27", cfg_path=cfg_p, root=root, fetcher=big_channel_fetcher, enqueue=False)
            self.assertEqual(len(res["rows"]), 1)
            row = res["rows"][0]
            self.assertEqual(row["role"], "southern_story_voice")
            self.assertEqual(row["learn_scope"], "voice_cadence_only")
            self.assertEqual(row["format_compatibility"], "story_metaphor")
            self.assertTrue(any("engagement" in r for r in row["reasons"]))

    def test_f1_arc_library_format_isolation(self):
        arcs = [
            {"id": "ARC-001", "format_compatibility": "instructional_list", "wins": 5, "uses": 5, "win_rate": 1.0, "seen": 3},
            {"id": "ARC-002", "format_compatibility": "story_metaphor", "wins": 1, "uses": 2, "win_rate": 0.5, "seen": 1},
        ]
        self.assertEqual(arc_lib.best_arc(arcs)["id"], "ARC-001")
        self.assertEqual(arc_lib.best_arc(arcs, format_filter="story_metaphor")["id"], "ARC-002")

    def test_f1_learn_from_channel_emotional_peak_prefers_emotion_over_length(self):
        text = (
            "Hôm nay chúng ta sẽ cùng nhau đi qua một danh sách dài rất nhiều các bước lập kế hoạch chi tiết cho cả tháng tới. "
            "Mình từng tự trách bản thân tới mức muốn bỏ cuộc!"
        )
        craft = lfc.local_craft(text)
        self.assertIn("muốn bỏ cuộc", craft["peak"])
        self.assertNotIn("Câu dài nhất", craft["peak"])

    # --- F2: Reverse Hot-Trend Matcher + Agile Slot Swap + Pain-Wave Fallback ---
    def test_f2_trend_match_respects_light_dark_rule_and_agile_swap(self):
        res = tm.match_trends(
            ref_date="2026-11-27",
            explicit_trends=["Cứ ngồi lướt điện thoại TikTok hoài tới khuya mất tập trung"],
            recent_themes=["DARK", "DARK"],
            top_n=3,
        )
        self.assertEqual(res["mode"], "hot_trend_match")
        self.assertEqual(res["required_theme"], "LIGHT")
        self.assertTrue(res["matches"])
        for m in res["matches"]:
            self.assertEqual(m["lesson"]["theme"], "LIGHT")

    def test_f2_pain_wave_fallback_when_no_fresh_trend(self):
        with tempfile.TemporaryDirectory() as d:
            res = tm.match_trends(
                ref_date="2026-11-27",
                trends_dir=Path(d),  # empty trends dir -> 0 fresh trends
                recent_themes=["DARK", "DARK"],
                top_n=2,
            )
            self.assertEqual(res["mode"], "pain_wave_fallback")
            self.assertTrue(res["fallback_pains"])
            for m in res["fallback_pains"]:
                self.assertEqual(m["lesson"]["theme"], "LIGHT")

    # --- F3: Multi-Script Tournament Arena & 5 Archetypes in gate0 ---
    def test_f3_gate0_archetype_and_script_arena_prepare_and_score(self):
        b = g0.brief("giới hạn video ngắn", "hi", archetype="M4")
        self.assertIn("Archetype `M4`", b)
        self.assertIn("Self-Dialogue", b)

        with tempfile.TemporaryDirectory() as d:
            written = sa.prepare_arena(
                idea="giới hạn video ngắn",
                out_dir=d,
                archetypes=("M1", "M2", "M4"),
                trend="lướt reels quên giờ ngủ",
            )
            self.assertEqual(len(written), 3)
            # Fill one draft with realistic varied-cadence beats (~185 syl) and score the arena
            p0 = Path(written[0]["path"])
            p0.write_text(
                "1. **[b01 · 0–5s]** Ngộ ghê ha, tính lướt năm phút mà hết cả tiếng.\n"
                "2. **[b02 · 5–16s]** Hồi trước tối nào mình cũng tự trách hoài, thấy mình nản dễ sợ vì cứ cầm điện thoại lên là quên luôn giấc ngủ.\n"
                "3. **[b03 · 16–27s]** Mình cứ tưởng do bản thân yếu ý chí thôi. Ai dè tới lúc tìm hiểu kỹ cách app thiết kế thì mới ngửa người ra.\n"
                "4. **[b04 · 27–39s]** Nghiên cứu cho thấy cơ chế cuộn vô tận không có điểm dừng làm bộ não mình liên tục chờ cái mới, càng lướt càng khó tắt màn hình.\n"
                "5. **[b05 · 39–50s]** Thành ra chuyện này đâu phải tại mình lười đâu bạn. Tối nay cứ đặt giới hạn mười lăm phút trước khi nằm xuống, đầu óc nhẹ hẳn liền.\n"
                "6. **[b06 · 50–60s]** Mình thì đi nhẹ vậy thôi, chứ chuyện này mỗi người nghĩ mỗi khác. Có ai hay bị cuốn giống mình hông, comment kể mình nghe nha?\n",
                encoding="utf-8",
            )
            sc = sa.score_arena([Path(w["path"]) for w in written], archive_hooks=[])
            self.assertEqual(sc["top1"]["name"], p0.name)
            self.assertGreater(sc["top1"]["score"], 80.0)

    # --- F4: Emotional Trajectory & Voice Ref Map in audio-precheck ---
    def test_f4_flat_cadence_and_missing_vulnerability_dip_and_voice_ref_map(self):
        # 5 dry, uniform-length sentences with no personal vulnerability dip
        dry = (
            "1. **[b01 · 0–5s]** Thói quen tốt giúp tăng hiệu suất làm việc mỗi ngày rất rõ.\n"
            "2. **[b02 · 5–10s]** Nhiều phương pháp khoa học giúp xây dựng kỷ luật đều đặn hơn.\n"
            "3. **[b03 · 10–15s]** Nghiên cứu năm 2010 theo dõi chín mươi sáu người trong hai tháng.\n"
            "4. **[b04 · 15–20s]** Kết quả cho thấy hành động lặp lại tạo nên phản xạ ổn định.\n"
            "5. **[b05 · 20–25s]** Hãy áp dụng cách này ngay hôm nay để đạt mục tiêu dài hạn.\n"
        )
        res = ap.analyze_beats(ap.parse_beats(dry))
        codes = {w["code"] for w in res["warnings"]}
        self.assertIn("FLAT_CADENCE", codes)
        self.assertIn("MISSING_VULNERABILITY_DIP", codes)
        self.assertIn("b03", res["voice_ref_map"])
        self.assertEqual(res["voice_ref_map"]["b03"]["voice_ref"], "thai-son-serious")

    # --- F5: Closed-Loop Golden Sync & 3D Win Rate ---
    def test_f5_golden_sync_deduplicates_and_computes_3d_win_rate(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            cdir = root / "clip-99-demo"
            (cdir / "final").mkdir(parents=True)
            (cdir / "final/feedback.md").write_text(
                "| ngày | bản | góp ý | hành động |\n|---|---|---|---|\n"
                "| 2026-11-27 | v1 | CTA sáo rỗng quá | Đổi CTA đồng cảm (DL-081) |\n",
                encoding="utf-8",
            )
            gpath = root / "index.json"
            gpath.write_text(json.dumps({"id": "review-golden.index", "samples": []}), encoding="utf-8")
            r1 = gs.sync_feedback(cdir, golden_path=gpath)
            r2 = gs.sync_feedback(cdir, golden_path=gpath)
            self.assertEqual(r1["added"], 1)
            self.assertEqual(r2["added"], 0)
            self.assertEqual(r2["skipped"], 1)

            pdir = root / "published"
            pdir.mkdir()
            (pdir / "stats.json").write_text(
                json.dumps([
                    {"clip": "clip-01", "views_7d": 25000, "completion_pct": 42, "archetype": "M2", "hook_mechanism": "tự giễu", "cta_style": "shared_struggle"},
                    {"clip": "clip-02", "views_7d": 3000, "completion_pct": 18, "archetype": "M2", "hook_mechanism": "tự giễu", "cta_style": "survey"},
                ]),
                encoding="utf-8",
            )
            r3d = gs.compute_3d_win_rates(published_dir=pdir)
            self.assertEqual(r3d["records"], 2)
            self.assertEqual(r3d["dimensions"]["archetype"]["M2"]["win_rate"], 0.5)
            self.assertEqual(r3d["dimensions"]["cta_style"]["shared_struggle"]["win_rate"], 1.0)

    # --- F6: One-Command Ideate-Clip Orchestrator ---
    def test_f6_ideate_clip_runs_freshness_match_and_arena(self):
        with tempfile.TemporaryDirectory() as d:
            out_arena = Path(d) / "arena"
            res = ic.run_ideate(
                clip_slug="clip-07-test",
                ref_date="2026-11-27",
                idea="giới hạn video ngắn",
                trend="lướt điện thoại mất tập trung",
                out_dir=out_arena,
            )
            self.assertIn("freshness", res)
            self.assertEqual(res["trend_match"]["mode"], "hot_trend_match")
            self.assertEqual(len(res["arena_briefs"]), 3)

    # --- DL-084: Global English Intelligence & EN->VN Bilingual Matching ---
    def test_dl084_global_english_channels_and_bilingual_trend_match(self):
        cfg = rf.load_config()
        en_channels = [c for c in cfg["channels"] if c.get("lang") == "en"]
        self.assertGreaterEqual(len(en_channels), 12)
        self.assertTrue(any(c["handle"] == "betterideas" and c["role"] == "global_niche_source" for c in en_channels))

        # English trend matches Vietnamese theme-map lesson and flags EN->VN localization
        res = tm.match_trends(
            ref_date="2026-11-28",
            explicit_trends=["Why doomscrolling your phone at night destroys your focus and dopamine"],
            recent_themes=["DARK", "DARK"],
            top_n=3,
        )
        self.assertEqual(res["mode"], "hot_trend_match")
        self.assertTrue(res["matches"])
        self.assertTrue(res["matches"][0]["needs_localization"])
        self.assertEqual(res["matches"][0]["lang"], "en")
        self.assertEqual(res["matches"][0]["lesson"]["theme"], "LIGHT")
        self.assertIn("EN→VN Localize", tm.format_report(res))

        # Teardown prompt includes localization_vi block to prevent Translationese
        prompt = td.load_prompt()
        self.assertIn("localization_vi", prompt)
        self.assertIn("translationese_traps", prompt)


if __name__ == "__main__":
    unittest.main()
