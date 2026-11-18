#!/usr/bin/env python3
"""Expose every repo skill to AI coding agents via symlinks (single source of truth stays in skills/).

Canonical skill folders (edit these, never the links):
  skills/<id>/SKILL.md                      @hi.oneup + shared skills
  skills/hyperframes/<id>/SKILL.md          vendored HyperFrames (Apache-2.0)
  skills/motionmaxxing -> resources/refs/motionmaxxing (vendored)
  channels/<channel>/skills/<id>/SKILL.md   per-channel skills

Discovery folders (generated, flat, one symlink per skill):
  .claude/skills/<id>  -> Claude Code (project skills)
  .agents/skills/<id>  -> Codex CLI and other agents that read .agents/skills

Usage:
  python3 pipeline/scripts/sync-agent-skills.py           # create/refresh links, remove stale ones
  python3 pipeline/scripts/sync-agent-skills.py --check   # exit 1 if links are missing/stale/broken (CI, pre-commit)
"""
import os, re, sys, pathlib

R = pathlib.Path(__file__).resolve().parents[2]
TARGETS = [R / '.claude' / 'skills', R / '.agents' / 'skills']
SOURCES = ['skills/*/SKILL.md', 'skills/*/*/SKILL.md', 'channels/*/skills/*/SKILL.md']
NAME_RE = re.compile(r'^[a-z0-9][a-z0-9-]{0,63}$')


def skill_name(md: pathlib.Path) -> str:
    text = md.read_text(errors='ignore')
    if not text.startswith('---\n'):
        sys.exit(f'✖ {md.relative_to(R)}: missing front-matter')
    head = text.split('\n---', 1)[0]
    m = re.search(r'^name:\s*["\']?([^"\'\n]+)', head, re.M)
    if not m or 'description:' not in head:
        sys.exit(f'✖ {md.relative_to(R)}: front-matter needs name + description')
    name = m.group(1).strip()
    if not NAME_RE.match(name):
        sys.exit(f'✖ {md.relative_to(R)}: name "{name}" must be lowercase letters, digits, hyphens')
    if name != md.parent.name:
        sys.exit(f'✖ {md.relative_to(R)}: name "{name}" must equal folder name "{md.parent.name}"')
    return name


def collect() -> dict:
    found = {}
    for pat in SOURCES:
        for md in sorted(R.glob(pat)):
            rel = md.relative_to(R)
            if rel.parts[0] == 'skills' and len(rel.parts) == 4 and rel.parts[1] != 'hyperframes':
                continue  # only skills/hyperframes/* is a nested collection
            name = skill_name(md)
            if name in found and found[name] != md.parent:
                sys.exit(f'✖ duplicate skill name "{name}": {found[name].relative_to(R)} vs {md.parent.relative_to(R)}')
            found[name] = md.parent
    return found


def main() -> int:
    check = '--check' in sys.argv
    skills = collect()
    problems = 0
    for target in TARGETS:
        if not check:
            target.mkdir(parents=True, exist_ok=True)
        want = {n: os.path.relpath(src, target) for n, src in skills.items()}
        have = {p.name: p for p in target.iterdir()} if target.exists() else {}
        for name, rel in sorted(want.items()):
            link = target / name
            ok = link.is_symlink() and os.readlink(link) == rel and (link / 'SKILL.md').exists()
            if ok:
                continue
            problems += 1
            if check:
                print(f'✖ {link.relative_to(R)} missing or stale (want -> {rel})')
                continue
            if link.is_symlink() or link.exists():
                link.unlink()
            link.symlink_to(rel, target_is_directory=True)
            print(f'+ {link.relative_to(R)} -> {rel}')
        for name, p in sorted(have.items()):
            if name in want:
                continue
            problems += 1
            if check:
                print(f'✖ {p.relative_to(R)} is stale (no canonical skill)')
            elif p.is_symlink():
                p.unlink()
                print(f'- {p.relative_to(R)} (stale)')
            else:
                print(f'⚠ {p.relative_to(R)} is a real folder; move it under skills/ and rerun')
    total = len(skills)
    if check:
        print(f'{"✔" if not problems else "✖"} agent skills: {total} canonical, {problems} problem(s)')
        return 1 if problems else 0
    print(f'✔ agent skills: {total} skills linked into ' + ', '.join(str(t.relative_to(R)) for t in TARGETS))
    return 0


if __name__ == '__main__':
    sys.exit(main())
