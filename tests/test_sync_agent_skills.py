"""Agent skill links (.claude/skills, .agents/skills) must match the canonical skills/ folders."""
import pathlib, subprocess, sys

ROOT = pathlib.Path(__file__).resolve().parents[1]


def test_agent_skill_links_in_sync():
    r = subprocess.run([sys.executable, str(ROOT / 'pipeline/scripts/sync-agent-skills.py'), '--check'],
                       capture_output=True, text=True)
    assert r.returncode == 0, r.stdout + r.stderr


def test_write_script_skill_is_discoverable():
    for d in ('.claude/skills', '.agents/skills'):
        assert (ROOT / d / 'write-script' / 'SKILL.md').is_file()
