"""rule-65: single source of canonical paths (docs/conventions/storage.md). Every generator imports from here."""
import json, os, shutil, sys, tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
HOME = Path.home()
TOOLS_DIR = Path(os.environ.get("ONEUP_TOOLS_DIR", str(HOME / "oneup-tools")))

def _first_existing(env_keys, candidates, fallback=""):
    for k in env_keys:
        v = os.environ.get(k)
        if v:
            return v
    for c in candidates:
        if c and Path(c).exists():
            return str(c)
    return fallback

def _find_node_bin():
    if os.environ.get("NODE22_BIN"):
        return os.environ["NODE22_BIN"]
    w = shutil.which("node")
    if w:
        return str(Path(w).parent)
    nvm = sorted((HOME / ".nvm/versions/node").glob("v22*/bin"), reverse=True)
    if nvm:
        return str(nvm[0])
    nvm_any = sorted((HOME / ".nvm/versions/node").glob("v*/bin"), reverse=True)
    if nvm_any:
        return str(nvm_any[0])
    return "/opt/homebrew/bin"

def _find_ffmpeg():
    if os.environ.get("FFMPEG_BIN"):
        return os.environ["FFMPEG_BIN"]
    for c in ("/opt/homebrew/opt/ffmpeg-full/bin/ffmpeg", "/usr/local/opt/ffmpeg-full/bin/ffmpeg", shutil.which("ffmpeg"), "/opt/homebrew/bin/ffmpeg"):
        if c and Path(c).exists():
            return str(c)
    return "ffmpeg"

def _find_ffprobe():
    ff = Path(_find_ffmpeg())
    fp = ff.parent / "ffprobe"
    if fp.exists():
        return str(fp)
    return shutil.which("ffprobe") or "/opt/homebrew/bin/ffprobe"

def _load_versions():
    vp = ROOT / "pipeline/versions.json"
    if vp.is_file():
        try:
            return json.loads(vp.read_text(encoding="utf-8"))
        except Exception:
            pass
    return {"hyperframes": "0.9.94", "capcut_cli": "0.37.1"}

VERSIONS = _load_versions()
HYPERFRAMES_VERSION = os.environ.get("HYPERFRAMES_VERSION", VERSIONS.get("hyperframes", "0.9.94"))

# Local Mac toolchain (no agent box/workspace dependency)
NODE_BIN = _find_node_bin()
FFMPEG_BIN = _find_ffmpeg()
FFPROBE_BIN = _find_ffprobe()
F5_PYTHON = _first_existing(
    ("F5_PYTHON", "F5_PY"),
    (TOOLS_DIR / "f5-venv/bin/python",),
    sys.executable,
)
ASR_PYTHON = _first_existing(
    ("ASR_PYTHON", "ASR_PY"),
    (TOOLS_DIR / "f5-venv/bin/python", TOOLS_DIR / "asr-venv/bin/python"),
    sys.executable,
)
def tools_env(key):
    """Read one `export KEY=value` from ~/oneup-tools/env.sh (outside git) when it is not already in the environment.
    Used for secrets such as APIFY_TOKEN, which must never be written into the repo."""
    if os.environ.get(key):
        return os.environ[key]
    f = TOOLS_DIR / "env.sh"
    if f.exists():
        for line in f.read_text().splitlines():
            line = line.strip()
            if line.startswith(f"export {key}=") or line.startswith(f"{key}="):
                return line.split("=", 1)[1].strip().strip('"').strip("'")
    return ""

def _which_any(name, env_key):
    v = os.environ.get(env_key)
    if v:
        return v
    nvm = sorted((HOME / ".nvm/versions/node").glob(f"v*/bin/{name}"), reverse=True)  # prefer user nvm installs over a stale /usr/local copy
    if nvm:
        return str(nvm[0])
    return shutil.which(name) or ""

TINYFISH_BIN = _which_any("tinyfish", "TINYFISH_BIN")   # @tiny-fish/cli: free search + fetch (TikTok pages are blocked for fetch, 26/11)
GEMINI_BIN = _which_any("gemini", "GEMINI_BIN")         # @google/gemini-cli: video teardown (pipeline/scripts/teardown.py)
AGY_BIN = _first_existing(("AGY_BIN",), ("/Applications/Gemini.app/Contents/Helpers/agy", HOME / ".local/bin/agy"), shutil.which("agy") or "")
# Antigravity CLI (Google). Gemini CLI's Google sign-in is refused for individual accounts since 2026-11, so teardown.py prefers agy.
EGO_BROWSER_BIN = _first_existing(("EGO_BROWSER_BIN",), (HOME / ".local/bin/ego-browser",), shutil.which("ego-browser") or "")
# Ego Lite browser CLI (DL-083): default browser for all web services, UI previews, and browser automation.

VIENEU_PYTHON = _first_existing(
    ("VIENEU_PYTHON",),
    (TOOLS_DIR / "tts-venv/bin/python",),
    sys.executable,
)
F5_CKPT_DIR = _first_existing(
    ("F5_CKPT_DIR",),
    (TOOLS_DIR / "f5-ckpt-6000h", TOOLS_DIR / "f5-ckpt"),
    str(TOOLS_DIR / "f5-ckpt-6000h"),
)
F5_VOCODER_DIR = _first_existing(
    ("F5_VOCODER_DIR",),
    (TOOLS_DIR / "vocos-mel-24khz",),
    "",
)
VOICE_WORK_DIR = Path(os.environ.get("VOICE_WORK_DIR", str(TOOLS_DIR / "voice-work" if TOOLS_DIR.exists() else Path(tempfile.gettempdir()) / "oneup-voice-work")))

def ckpt_fingerprint(ckpt_dir: str = F5_CKPT_DIR) -> str:
    p = Path(ckpt_dir)
    pt = p / "model_last.pt"
    sz = pt.stat().st_size if pt.is_file() else 0
    return f"{p.name}:{sz}"

# shared library (one copy, never per clip)
BRAND = ROOT / "brand"; FONTS = BRAND / "fonts"; LOGOS = BRAND / "logos"; BRAND_TOKENS = BRAND / "brand-tokens.json"
ASSETS = ROOT / "assets"; SFX = ASSETS / "sfx"; VOICE_REFS = ASSETS / "voice-refs"
VE = ROOT / "video-engine"; CHARACTERS = VE / "src/characters"; PROPS_SRC = VE / "src/composition/Props.tsx"
VOICE_CACHE = VE / "public/voice"          # all voice takes (content-hash keys / v8-<scene>), committed
ENGINE_OUT = VE / "out"                    # Remotion part renders (gitignored)
# per clip
CLIPS = ROOT / "content/clips"          # active clips
ARCHIVE = ROOT / "content/archive"     # rule-66: approved ("duyệt") clips with a complete post package
MEDIA_CLIPS = ROOT / "media/clips"     # final renders per clip (full + 720p), gitignored, manifested
POST_PACKAGE = ("final/post.md", "final/cover.png", "final/approved.json")
def clip_dir(clip: str) -> Path: return CLIPS / clip
def final_dir(clip: str) -> Path: return CLIPS / clip / "final"   # script, spec, plans, timing, cover, preview/
def out_dir(clip: str) -> Path: return final_dir(clip) / "out"     # final mp4, mix, generated sfx (gitignored)
def preview_dir(clip: str) -> Path: return final_dir(clip) / "preview"
# other
MEDIA = ROOT / "media"; MANIFEST = MEDIA / "MANIFEST.json"        # large binaries (gitignored, manifested)
RESEARCH = ROOT / "research"; TRENDS = RESEARCH / "trends"
LOGS = ROOT / "logs"; LESSONS = LOGS / "lessons.md"; DECISIONS = LOGS / "decision-log.md"
RULES = ROOT / "rules/video-rules.md"; DOCS = ROOT / "docs"; TESTS = ROOT / "tests"
SCRIPTS = ROOT / "pipeline/scripts"; TTS = ROOT / "pipeline/tts"; SKILLS_MIRROR = ROOT / "skills"
SKILL_LINK_DIRS = (ROOT / ".agents/skills", ROOT / ".claude/skills", ROOT / ".cursor/skills")  # per-agent symlink mirrors of the skill sources (Antigravity, Claude Code, Cursor); Grok reads docs/agents/skills-index.md
SKILLS_INDEX = DOCS / "agents/skills-index.md"
# allowed top-level dirs/files (check-assets.py enforces)
TOP_ALLOWED = {"GUIDE.md", "AGENTS.md", "CLAUDE.md", "GEMINI.md", "INDEX.md", "README.md", "index.json", ".gitignore", "assets", "brand", "channels", "content", "docs", "logs", "media",
               "pipeline", "research", "resources", "rules", "skills", "templates", "tests", "video-engine"}
SAMPLES = ROOT / "content/samples"; LAB = SAMPLES / "lab"; FOOTAGE = MEDIA / "footage"; EXT_REFS = ROOT / "resources/refs"
# per-clip standard layout: content/clips/<clip>/{README.md, final/, archive/}; drafts/old versions only in archive/
CLIP_TOP_ALLOWED = {"final", "archive", "README.md"}
# shared-type files that must NOT live inside content/ (derived copies are gitignored, see sync-shared.py)
SHARED_EXT = {".ttf", ".otf", ".woff", ".woff2"}
SHARED_NAMES = {"logo.svg", "thai-son.wav", "my-duyen.wav"}
# content-bot prompt mapping (storage.md "Ánh xạ prompt bot nội dung")
PROMPTS = DOCS / "prompts"; REFERENCES = RESEARCH / "references"; PUBLISHED = ROOT / "content/published"; SCRIPT_TEMPLATE = ROOT / "templates/script.md"
FM_REQUIRED = ("title", "date", "type", "tags", "status", "source")
FM_STATUS = {"draft", "ready", "published"}
FM_EXEMPT = ("CLAUDE.md", "GEMINI.md", "skills/", "video-engine/", "templates/hyperframes-base/", "docs/legacy-box/", "resources/refs/awesome-ai-motion/", "resources/refs/transitions.dev/", "resources/refs/motionmaxxing/", "resources/refs/anidoodle/", "brand/omi-exports/", "channels/vanhiep-tech/skills/")
FM_STRICT_STATUS = ("docs/prompts/", "research/references/", "content/published/", "templates/script.md")
