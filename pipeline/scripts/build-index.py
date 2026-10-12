#!/usr/bin/env python3
"""Regenerate INDEX.md + index.json from front-matter, rules and folders. Run after adding/renaming docs."""
import re, json, pathlib
R = pathlib.Path(__file__).resolve().parents[2]
def fm(p):
    s = p.read_text(errors='ignore')
    if not s.startswith('---\n'): return None
    d = {}
    for l in s.split('\n---', 1)[0].splitlines()[1:]:
        if ':' in l and not l.startswith(' '): k, v = l.split(':', 1); d[k.strip()] = v.strip()
    h = re.search(r'^# (.+)$', s, re.M); d['title'] = h.group(1) if h else p.stem
    return d
docs = []
for p in sorted(R.rglob('*.md')):
    rel = p.relative_to(R).as_posix()
    if any(x in rel for x in ('node_modules', 'brand/omi-exports', '/.build/')) or rel.startswith(('brand/scripts',)): continue
    d = fm(p)
    if d and 'id' in d: docs.append({'id': d['id'], 'type': d.get('type'), 'status': d.get('status'), 'updated': d.get('updated'), 'path': rel, 'title': d['title']})
    elif d and 'name' in d: docs.append({'id': 'skill.' + p.parent.name, 'type': 'skill', 'status': 'active', 'path': rel, 'title': d['name']})
rules = []
for m in re.finditer(r'^(\d+)\. \*\*([^*]+)\*\*', (R/'rules/video-rules.md').read_text(), re.M):
    rules.append({'id': f'rule-{m.group(1)}', 'title': m.group(2).rstrip(':'), 'path': 'rules/video-rules.md'})
clips = []
for c in sorted((R/'content/clips').iterdir()):
    if c.is_dir():
        sp = c/'storyboard/spec.json'; spec = json.loads(sp.read_text()) if sp.exists() else {}
        clips.append({'id': c.name.split('-', 2)[0] + '-' + c.name.split('-', 2)[1], 'path': c.relative_to(R).as_posix(), 'theme': spec.get('theme'), 'files': sorted(x.name for x in c.iterdir() if not x.name.startswith('.'))})
assets = [
 {'id': 'asset.fonts', 'path': 'brand/fonts/', 'desc': 'Be Vietnam Pro (video), DM Sans (app) + OFL licenses'},
 {'id': 'asset.logos', 'path': 'brand/logos/', 'desc': 'Logo SVG/PNG; hero = 05-pair-plus.svg'},
 {'id': 'asset.omi', 'path': 'brand/omi-exports/', 'desc': 'Omi mascot SVG/PNG, 4 styles x 12 moods'},
 {'id': 'asset.app-icons', 'path': 'brand/app-icon-exports/', 'desc': 'App icons light/dark'},
 {'id': 'asset.tokens', 'path': 'brand/brand-tokens.json', 'desc': 'Colors/fonts/caption/logo tokens (machine-readable)'},
 {'id': 'asset.sfx', 'path': 'assets/sfx/', 'desc': 'CC0/Mixkit SFX + SOURCES.md'},
 {'id': 'asset.template', 'path': 'templates/hyperframes-base/', 'desc': 'HyperFrames 1080x1920 scaffold, local GSAP'},
 {'id': 'tool.storyboard', 'path': 'pipeline/storyboard/render.py', 'desc': 'Shared storyboard renderer (spec.json -> PNGs + contact sheet)'},
 {'id': 'tool.sync-trends', 'path': 'pipeline/scripts/sync-trends.sh', 'desc': 'Box -> repo trend sync, commit, push'},
 {'id': 'tool.build-index', 'path': 'pipeline/scripts/build-index.py', 'desc': 'Regenerates this index'},
 {'id': 'data.trends', 'path': 'research/trends/', 'desc': 'Daily digests YYYY-MM-DD/{digest.md,raw.json} + ingest.md'},
 {'id': 'dir.footage', 'path': 'footage/inbox/', 'desc': 'AirDrop inbox (media gitignored)'},
 {'id': 'dir.renders', 'path': 'renders/ready/', 'desc': 'Ready-to-post packages (media gitignored)'},
]
idx = {'generated_by': 'pipeline/scripts/build-index.py', 'docs': docs, 'rules': rules, 'clips': clips, 'assets': assets}
(R/'index.json').write_text(json.dumps(idx, ensure_ascii=False, indent=1))
L = ['---', 'id: index', 'type: index', 'status: generated', 'tags: [index, retrieval]', '---', '# INDEX (generated, do not hand-edit; run `python3 pipeline/scripts/build-index.py`)', '', '## Docs', '| id | type | status | path | title |', '|---|---|---|---|---|']
L += [f"| {d['id']} | {d['type']} | {d['status']} | `{d['path']}` | {d['title']} |" for d in docs]
L += ['', '## Rules (source: `rules/video-rules.md`)', '| id | title |', '|---|---|'] + [f"| {r['id']} | {r['title']} |" for r in rules]
L += ['', '## Clips', '| id | theme | path | files |', '|---|---|---|---|'] + [f"| {c['id']} | {c['theme']} | `{c['path']}` | {', '.join(c['files'])} |" for c in clips]
L += ['', '## Assets & tools', '| id | path | description |', '|---|---|---|'] + [f"| {a['id']} | `{a['path']}` | {a['desc']} |" for a in assets]
(R/'INDEX.md').write_text('\n'.join(L) + '\n'); print(len(docs), 'docs', len(rules), 'rules', len(clips), 'clips')
