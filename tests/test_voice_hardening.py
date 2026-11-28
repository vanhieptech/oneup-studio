"""Regression tests for DL-087 / DL-088 / L-114 voice & build pipeline hardening."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]


def test_voice_phrase_single_ref_and_6000h_speed_default():
    src = (ROOT / "pipeline/scripts/voice-phrase-f5.py").read_text(encoding="utf-8")
    m = re.search(r"REF_SLOTS\s*=\s*(\{[^}]+\})", src)
    assert m, "REF_SLOTS not found in voice-phrase-f5.py"
    slots = eval(m.group(1))
    # All default slots must map to the same consistent ref (no cross-ref timbre jump)
    assert set(slots.values()) == {"thai-son-v2"}, f"Expected uniform thai-son-v2, got {slots}"
    assert "STRETCHED_6000H_REFS" in src
    assert "1.12" in src
    assert '"f0_hz":f0_hz' in src or '"f0_hz": f0_hz' in src


def test_build_final_auto_reuses_voice_prefix_stitched_files():
    src = (ROOT / "pipeline/scripts/build-final.py").read_text(encoding="utf-8")
    assert 'vpre = spec.get("voice_prefix")' in src
    assert 'cand = f"{vpre}-{lkey}"' in src


def test_prosody_check_voice_has_work_dir_fallback():
    src = (ROOT / "pipeline/scripts/prosody-check.py").read_text(encoding="utf-8")
    assert 'arg("--work") or str(P.VOICE_WORK_DIR' in src


def test_check_rules_has_l114_f0_and_rate_checks():
    src = (ROOT / "pipeline/scripts/check-rules.py").read_text(encoding="utf-8")
    assert '"L-114"' in src
    assert "avg_rate < 3.8" in src
    assert "abs(12 * math.log2(v / med_f0)) > 2.5" in src
