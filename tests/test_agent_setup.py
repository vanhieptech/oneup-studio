"""Agent-native setup guards (Claude Code, Antigravity, Cursor, Grok share one source of truth).

1. The per-agent skill mirrors (.agents/skills, .claude/skills, .cursor/skills) are identical sets of
   relative symlinks that resolve inside the repo to a folder with SKILL.md whose `name:` matches.
2. docs/agents/skills-index.md (what Grok reads) lists exactly those skills.
3. Live tracked files (rules, docs, skills, pipeline, video-engine src, agent entry points) contain no
   absolute machine / agent-workspace paths, so any agent on any checkout resolves paths the same way.
4. The pre-commit hook delegates to pipeline/scripts/preflight.sh (one gate for hook and hook-less agents).
"""
import os, re, subprocess, sys, unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "pipeline"))
import paths as P  # noqa: E402

LINK_DIRS = [d.relative_to(ROOT).as_posix() for d in P.SKILL_LINK_DIRS]
BANNED = re.compile(r"/Users/\w|/home/\w|/workspace/[\w<$]|/opt/cursor/\w|/private/tmp/\w|\b[C-Z]:\\{1,2}(?:Users|Program|Windows)\b")
ALLOWED = ("/opt/cursor/artifacts",)  # documented as a *banned* CapCut handoff source in channels/vanhiep-tech
SCAN = ["AGENTS.md", "CLAUDE.md", "GEMINI.md", "GUIDE.md", "README.md", "rules", "docs/conventions", "docs/agents",
        "docs/workflow", "docs/prompts", "skills", "channels/vanhiep-tech", "pipeline", "video-engine/src",
        "video-engine/README.md", "video-engine/scripts-still.ts", ".githooks", ".github", ".cursor/rules", "templates", "tests"]
SKIP_PREFIX = ("skills/hyperframes/", "skills/humanizer/", "templates/hyperframes-base/", "tests/test_agent_setup.py")
TEXT_EXT = {".md", ".mdc", ".py", ".sh", ".ts", ".tsx", ".js", ".mjs", ".json", ".yml", ".yaml", ".txt", ""}


def links(d):
    return {p.name: os.readlink(p) for p in sorted((ROOT / d).iterdir()) if p.is_symlink()}


class SkillMirrors(unittest.TestCase):
    def test_mirrors_identical(self):
        base = links(LINK_DIRS[0])
        self.assertGreater(len(base), 0)
        for d in LINK_DIRS[1:]:
            self.assertEqual(links(d), base, f"{d} differs from {LINK_DIRS[0]}: add/remove the same symlink in every agent dir")

    def test_only_relative_symlinks_into_repo(self):
        for d in LINK_DIRS:
            for p in (ROOT / d).iterdir():
                self.assertTrue(p.is_symlink(), f"{d}/{p.name} must be a symlink (never a copy)")
                target = os.readlink(p)
                self.assertFalse(os.path.isabs(target), f"{d}/{p.name} -> {target} must be relative")
                resolved = (p.parent / target).resolve()
                self.assertTrue(str(resolved).startswith(str(ROOT.resolve())), f"{d}/{p.name} escapes the repo")

    def test_targets_have_matching_skill_md(self):
        for name, target in links(LINK_DIRS[0]).items():
            skill = (ROOT / LINK_DIRS[0] / target / "SKILL.md")
            if not skill.exists():
                # only allowed for a symlinked local clone that is gitignored/not checked out (e.g. CI)
                self.assertTrue(os.path.islink(ROOT / LINK_DIRS[0] / target), f"{name}: missing SKILL.md")
                continue
            m = re.search(r"^name:\s*['\"]?([\w.-]+)", skill.read_text(encoding="utf-8"), re.M)
            self.assertIsNotNone(m, f"{name}: SKILL.md has no name:")
            self.assertEqual(m.group(1), name, f"{name}: symlink name must equal SKILL.md name:")

    def test_skills_index_lists_every_skill(self):
        idx = P.SKILLS_INDEX.read_text(encoding="utf-8")
        listed = set(re.findall(r"^\| `([\w.-]+)` \|", idx, re.M))
        self.assertEqual(listed, set(links(LINK_DIRS[0])), "docs/agents/skills-index.md out of sync with skill symlinks")


class NoAbsolutePaths(unittest.TestCase):
    def test_live_files_have_no_machine_paths(self):
        files = subprocess.run(["git", "ls-files", "-z", "--", *SCAN], cwd=ROOT, capture_output=True, text=True).stdout.split("\0")
        bad = []
        for f in files:
            if not f or f.startswith(SKIP_PREFIX) or Path(f).suffix not in TEXT_EXT:
                continue
            p = ROOT / f
            if p.is_symlink() or not p.is_file():
                continue
            for i, line in enumerate(p.read_text(encoding="utf-8", errors="ignore").splitlines(), 1):
                clean = line
                for a in ALLOWED:
                    clean = clean.replace(a, "")
                if BANNED.search(clean):
                    bad.append(f"{f}:{i}: {line.strip()[:120]}")
        self.assertEqual(bad, [], "absolute machine/agent paths (use git rev-parse --show-toplevel or pipeline/paths.py):\n" + "\n".join(bad))


class Gate(unittest.TestCase):
    def test_pre_commit_delegates_to_preflight(self):
        hook = (ROOT / ".githooks/pre-commit").read_text()
        self.assertIn("pipeline/scripts/preflight.sh", hook)
        for s in ("pipeline/scripts/preflight.sh", "pipeline/scripts/env-check.sh", ".githooks/pre-commit"):
            self.assertTrue(os.access(ROOT / s, os.X_OK), f"{s} must be executable")

    def test_thin_entry_points_point_to_agents_md(self):
        for f in ("CLAUDE.md", "GEMINI.md", ".cursor/rules/oneup.mdc"):
            self.assertIn("AGENTS.md", (ROOT / f).read_text(encoding="utf-8"), f"{f} must point to AGENTS.md")


if __name__ == "__main__":
    unittest.main()
