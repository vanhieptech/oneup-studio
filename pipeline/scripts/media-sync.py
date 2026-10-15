#!/usr/bin/env python3
"""rule-66 / storage.md §Gitignored: keep gitignored originals (media/**) on Hiệp's Mac.
Box has no GitHub creds and CopyFromBox caps at ~5 MB per file, so media travels as a tar split into ≤5 MB parts
inside the repo's .git/ dir (allowed local-exec root).
  box:  media-sync.py pack [--missing mac_list.txt]   → /workspace/media-sync/part.NN + media-sync.json (sha256 of tar)
        (agent copies each part with CopyFromBox to <repo>/.git/media-sync/part.NN on the Mac)
  mac:  media-sync.py unpack                          → joins .git/media-sync/part.*, checks sha256, untars into repo, verifies MANIFEST
  any:  media-sync.py verify                          → lists MANIFEST entries missing or with wrong sha256 (exit 1 if any)
"""
import hashlib, json, subprocess, sys, tarfile
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1])); import paths as P
PART = 5 * 1024 * 1024 - 64 * 1024
def sha(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for b in iter(lambda: f.read(1 << 20), b""): h.update(b)
    return h.hexdigest()
def manifest(): return json.loads(P.MANIFEST.read_text())
def verify():
    bad = [e["path"] for e in manifest() if not (P.ROOT / e["path"]).is_file() or sha(P.ROOT / e["path"]) != e["sha256"]]
    for b in bad: print("missing/stale:", b)
    print(f"media verify: {len(manifest()) - len(bad)}/{len(manifest())} ok"); return 1 if bad else 0
def pack(missing=None):
    out = Path("/workspace/media-sync"); out.mkdir(exist_ok=True); [p.unlink() for p in out.glob("part.*")]
    want = [e["path"] for e in manifest() if missing is None or e["path"] in missing]
    tp = out / "media.tar"
    with tarfile.open(tp, "w") as t:
        for p in want: t.add(P.ROOT / p, arcname=p)
    data = tp.read_bytes(); n = 0
    for i in range(0, len(data), PART): (out / f"part.{n:02d}").write_bytes(data[i:i + PART]); n += 1
    json.dump({"sha256": hashlib.sha256(data).hexdigest(), "parts": n, "files": want}, open(out / "media-sync.json", "w"), indent=1)
    tp.unlink(); print(f"packed {len(want)} files into {n} parts in {out}")
def unpack():
    d = P.ROOT / ".git/media-sync"; parts = sorted(d.glob("part.*")); data = b"".join(p.read_bytes() for p in parts)
    meta = json.loads((d / "media-sync.json").read_text()) if (d / "media-sync.json").exists() else {}
    if meta and hashlib.sha256(data).hexdigest() != meta["sha256"]: sys.exit("sha256 mismatch: re-copy parts")
    tp = d / "media.tar"; tp.write_bytes(data)
    with tarfile.open(tp) as t: t.extractall(P.ROOT)
    for p in parts + [tp]: p.unlink()
    sys.exit(verify())
if __name__ == "__main__":
    c = sys.argv[1] if len(sys.argv) > 1 else "verify"
    if c == "pack":
        miss = set(Path(sys.argv[sys.argv.index("--missing") + 1]).read_text().split()) if "--missing" in sys.argv else None; pack(miss)
    elif c == "unpack": unpack()
    else: sys.exit(verify())
