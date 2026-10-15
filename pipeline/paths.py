"""rule-65: single source of canonical paths (docs/conventions/storage.md). Every generator imports from here."""
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
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
SKILLS_LIVE = Path("/home/box/agent-data/workflows")
# allowed top-level dirs/files (check-assets.py enforces)
TOP_ALLOWED = {"GUIDE.md", "AGENTS.md", "INDEX.md", "README.md", "index.json", ".gitignore", "assets", "brand", "content", "docs", "logs", "media",
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
FM_EXEMPT = ("skills/", "video-engine/", "templates/hyperframes-base/", "docs/legacy-box/", "resources/refs/awesome-ai-motion/", "resources/refs/transitions.dev/", "brand/omi-exports/")
FM_STRICT_STATUS = ("docs/prompts/", "research/references/", "content/published/", "templates/script.md")
