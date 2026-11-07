from pathlib import Path
import json,re,hashlib,itertools,copy,sys
B=Path('/workspace');s=json.loads((B/'opencreator-clip05-spec-r11.4-plan-update2-2026-11-07.json').read_text());old=json.loads((B/'opencreator-clip05-spec-r11.4-draft-2026-11-07.json').read_text());script=B/'opencreator-clip05-script-r11.4-draft-2026-11-07.md';board=(B/'opencreator-clip05-storyboard-r11.4-plan-update2-2026-11-07.md').read_text();expected='dc42247775b8fdd0d6c5a6958e074a829e899f431efcc826516f61e21c53dd0e';checks=[]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def test(ok,name,detail=None):checks.append(dict(check=name,ok=bool(ok),detail=detail))
def inside(a,b):x,y,w,h=a;X,Y,W,H=b;return x>=X-1e-6 and y>=Y-1e-6 and x+w<=X+W+1e-6 and y+h<=Y+H+1e-6
def overlap(a,b):x,y,w,h=a;X,Y,W,H=b;return max(0,min(x+w,X+W)-max(x,X))*max(0,min(y+h,Y+H)-max(y,Y))
def envelope(o):
 x,y,w,h=o['bbox'];m=o['motion_envelope'];cx=x+w/2;cy=y+h/2
 r=[(cx-w*k/2+dx,cy-h*k/2+dy,cx+w*k/2+dx,cy+h*k/2+dy) for dx,dy,k in itertools.product(m['x'],m['y'],m['scale'])]
 return [min(t[0] for t in r),min(t[1] for t in r),max(t[2] for t in r)-min(t[0] for t in r),max(t[3] for t in r)-min(t[1] for t in r)]
frozen=json.loads((B/'clip05-r11.4-plan-update2-input-hashes-2026-11-07.json').read_text())
for f,h in frozen.items():test(sha(B/f)==h,'original input unchanged: '+f)
test(sha(script)==expected,'script SHA before/after exactly required',sha(script))
test(s['planning_only'] and not s['renderable'] and not s['locked'],'planning only not runnable/approved')
rows=re.findall(r'^\d+\. \*\*\[[^\]]+\]\*\* (.*)$',script.read_text(),re.M)
test(rows==[b['text'] for b in s['beats']],'all7 speech lines == frozen MD')
count=sum(len(b['text'].split()) for b in s['beats']);test(count==s['word_count']==150,'150 spoken words unchanged');test(sum(len(b['text'].split()) for b in s['beats'][1:4])==s['pre_method_words_after_hook']==50,'50 pre-method unchanged')
for b,o in zip(s['beats'],old['beats']):
 q=copy.deepcopy(b);q.pop('visual_object_plan_refs',None);test(q==o,b['id']+' entire beat unchanged apart from new visual refs')
 test(re.sub(r'\{nhấn: ([^}]+)\}',r'\1',b['marked_text'])==b['text'],b['id']+' marked text exact')
 test(b['marked_text'] in board,b['id']+' marked VI present unchanged in new storyboard')
 test(' '.join(re.sub(r'\{nhấn: ([^}]+)\}',r'\1',p['t']) for p in b['phrases_plan'])==b['text'],b['id']+' phrase speech exact')
 for c in b['captions']:
  test(c in o['captions'],c['id']+' complete caption/range/time/hl unchanged')
  test(len(c['en'].split())<=8,c['id']+' EN<=8',len(c['en'].split()))
  test(c['en'] in board and c['vi_text'] in board,c['id']+' VI/EN in new board')
  test(all(0<=i<len(c['en'].split()) for i in c['hl']),c['id']+' highlight indexes valid')
 test(1<=len(b['emphasis_focus'])<=2,b['id']+' semantic focus1–2')
 for focus in b['emphasis_focus']:
  for t in focus['caption_targets']:
   c=next(c for c in b['captions'] if c['id']==t['id']);test(t['hl']==c['hl'] and t['highlight_words']==[c['en'].split()[i] for i in c['hl']],t['id']+' semantic highlight unchanged/exact')
for k in ['source','throughline','hook_question','hook','hook_alt','hook_alts','callbacks','structure','caption_segments_plan','voice_lines_plan','timing_model','duration_estimate_s','duration_measured','engagement','pinned_comment_plan','transition_sfx','ambience','music']:
 test(s[k]==old[k],k+' unchanged')
caps=[c for b in s['beats'] for c in b['captions']];test(len(caps)==len(s['caption_segments_plan'])==23,'exactly23 main caption segments unchanged')
units=[u for p in s['parts_plan'] for u in p.get('scenes',p.get('sections',[]))];oldunits=[u for p in old['parts_plan'] for u in p.get('scenes',p.get('sections',[]))];cids={c['id'] for c in caps};vids={v['id'] for v in s['voice_lines_plan']}
for i,(u,v) in enumerate(zip(units,oldunits)):
 q=copy.deepcopy(u);q.pop('visual_object_plan_refs',None);q.pop('conditional_disclosure_ref',None);test(q==v,u['id']+' original unit properties/timing unchanged')
 a,z=u['interval_estimate_s'];test(0<z-a<=8+1e-6,u['id']+' valid estimated duration <=8')
 if i:test(abs(a-units[i-1]['interval_estimate_s'][1])<1e-5,u['id']+' contiguous estimated scene timeline')
 test(all(c in cids for c in u['caption_segment_refs']),u['id']+' captions resolve')
 test(u['voice_line_ref'] is None if u['beat']=='end' else u['voice_line_ref'] in vids,u['id']+' voice ref resolves')
 for ref in u.get('visual_object_plan_refs',[]):
  o=s['visual_objects_plan'][ref];a1,z1=o['visible_interval_estimate_s'];test(a<=a1<z1<=z+1e-6,u['id']+'/'+ref+' within estimated unit')
for a,b in zip(caps,caps[1:]):test(a['interval_estimate_s'][1]<=b['interval_estimate_s'][0]+1e-6,a['id']+' no caption time overlap')
# Declared layout allocations only, NOT font/renderer measurements.
for id,lay in s['layout_plans'].items():
 es=[]
 for o in lay['objects']:
  e=envelope(o);es.append((o['id'],e));test(inside(e,s['frame']['zones'][o['zone']]),id+'/'+o['id']+' declared envelope in zone')
 for (x,a),(y,b) in itertools.combinations(es,2):test(overlap(a,b)<1e-6,id+'/'+x+'/'+y+' top-level allocations disjoint')
 for engine,box in s['frame']['caption_reserved_bbox'].items():test(inside(box,s['frame']['zones']['caption']),id+'/'+engine+' caption zone separate')
# Resolve nested visuals against layout allocations; b06 children inherit parent x[0,8].
leafgroups={}
for u in units:
 lay=s['layout_plans'][u['layout_ref']];parents={o['id']:o for o in lay['objects']}
 for ref in u.get('visual_object_plan_refs',[]):
  o=s['visual_objects_plan'][ref];parent=o['parent_object'];p=parents[parent] if parent else parents[o['id']]
  test(inside(o['bbox'],p['bbox']),ref+' inside parent allocation')
  bound=envelope({'bbox':o['bbox'],'motion_envelope':p['motion_envelope']});test(inside(bound,s['frame']['zones']['content']),ref+' inherited motion inside content')
  test(not overlap(bound,s['frame']['zones']['caption']),ref+' avoids caption zone')
  leafgroups.setdefault(u['id'],[]).append(o)
for uid,ls in leafgroups.items():
 for a,b in itertools.combinations(ls,2):test(not overlap(a['bbox'],b['bbox']),uid+'/'+a['id']+'/'+b['id']+' leaf allocations disjoint')
label='MINH HỌA BIÊN TẬP CỦA KÊNH'
for bid in ['b05','b06']:
 u=next(u for u in units if u['beat']==bid);o=s['visual_objects_plan']['mock-label-'+bid]
 test(o['text']==label and o['id'] in u['visual_object_plan_refs'],bid+' explicit editorial label display mapping')
 test(label in board,bid+' editorial label in board')
model=s['mock_comparison_plan'];doc=copy.deepcopy(model['source_document']['content']);initial=copy.deepcopy(doc);retell=list(model['retelling_initial']);states=[]
for e in model['events']:
 test(not e['writes_document_content'],'mock event never edits source: '+e['operation'])
 if e['operation']=='append_retelling':
  test(e['target_column']=='PHẦN KỂ' and e['target_object']=='retelling-rent','Rent append exclusively targets PHẦN KỂ');retell.append(e['value'])
 states.append({'at_estimate_s':e['at_estimate_s'],'operation':e['operation'],'source_content':copy.deepcopy(doc),'retelling':copy.deepcopy(retell)})
test(doc==initial==['Record food expenses','Record rent'],'source content unchanged across simulated plan events')
test(states[0]['retelling']==['Food'] and retell==['Food','Rent'],'only retelling gains Rent after comparison')
test(s['visual_objects_plan']['source-rent']['visible_interval_estimate_s'][0]==model['events'][0]['at_estimate_s'],'source Rent uncovered at existing tiền thuê nhà cue')
test(s['visual_objects_plan']['retelling-rent']['visible_interval_estimate_s'][0]==model['events'][1]['at_estimate_s'],'retelling Rent appended at existing bổ sung cue')
test(model['events'][0]['at_estimate_s']<model['events'][1]['at_estimate_s'],'reveal before retelling addition')
# Cover meaning is represented explicitly; these do NOT certify the meaning of an actual image.
test(s['cover']['strike']==0 and s['cover']['accent']==1,'R54 whole old-habit strike0 / new pill accent1')
test(s['cover']['series']=='LOW/HIGH UTILITY' and s['cover']['hero']==['REREAD ONLY','SELF-TEST'],'cover whole exclusive-use habit, not bare technique, plus utility category context')
test(s['cover']['semantic_plan']['cover_text_character_count_including_native_ep_tag']==39,'cover planned text including native #05 <=40')
test([o for o in s['cover_plan']['conservative_allocations'] if o['id']!='hero']==[o for o in old['cover_plan']['conservative_allocations'] if o['id']!='hero'],'non-hero cover allocations unchanged');test(next(o['bbox'] for o in s['cover_plan']['conservative_allocations'] if o['id']=='hero')==[60,420,960,380],'hero strict reserve includes whole native stroke')
test(s['cover_plan']['illustration_mapping']==old['cover_plan']['illustration_mapping'],'cover -40/-70 affine mapping unchanged')
pa={o['id']:o['bbox'] for o in s['cover_plan']['conservative_allocations']}
for id,box in pa.items():test(inside(box,s['cover_plan']['rule_safe_zone']),'cover '+id+' strict-safe declared allocation')
for t in s['cover_plan']['text_mapping']:test(inside(t['bbox'],pa[t['parent_allocation']]),t['id']+' text allocation in strict parent')
# AI disclosure matches frozen MD, is conditional and never a24th caption or spoken line.
disc=s['publication_plan']['ai_disclosure'];entry=s['end_card']['conditional_text_lines'][0]
test(disc in script.read_text() and disc in board and entry['text']==disc,'AI disclosure literal matches frozen MD/spec/board')
test(entry['if']=='publication_plan.ai_voice_used == true' and not entry['include_now'] and not entry['spoken'],'AI disclosure conditional, no present speech/audio claim')
test(s['publication_plan']['ai_voice_used'] is None and not s['publication_plan']['current_artifact_has_audio'],'future AI use unknown; no audio now')
test(s['end_card']['text_lines']==old['end_card']['text_lines'],'base4 safety/credit/license lines unchanged')
test(s['end_card']['text_lines_if_ai_voice_used']==old['end_card']['text_lines']+[disc],'AI branch includes exact disclosure')
test(s['end_card']['text_lines_if_no_ai_voice_used']==old['end_card']['text_lines'],'non-AI branch omits disclosure')
test('NOT A BLOCKER' in s['gates']['callback04'],'release04 not carried as current blocker')
test(not s['callbacks'][0]['spoken_callback'],'no spoken release callback')
test('CHƯA CHUẨN BỊ ẢNH' in board and not s['preview_gate1']['storyboard_png'],'no preview fabricated')
# Literal R16/R54/source-read feasibility, not image/craft approval.
for id,expected_text in [('comparison-title-text','COMPARE YOUR RETELLING'),('source-header','SOURCE PAGE'),('retelling-header','YOUR RETELLING')]:
 o=s['visual_objects_plan'][id];test(o['text']==expected_text and o['language']=='en' and o['text'].isascii(),id+' English HF title/heading actual display')
 test(expected_text in board,id+' English display matches board')
test(sum(len(w.split()) for w in s['cover']['hero'])==3,'R54 hero2–4 words, actual3')
test(s['cover']['hero'][s['cover']['strike']]=='REREAD ONLY','strike entire qualified old habit, ONLY inseparable')
code=(B/'oneup-studio/video-engine/src/composition/Cover.tsx').read_text()
for token in ['hero: string[]; accent: number; strike?: number','i === p.accent, st = i === p.strike','left: -10, right: -10','p.hero.map((w, i) => <Word','left: 66, right: 60, top: 420']:
 test(token in code,'native source mapping token '+token)
rl=(B/'oneup-studio/rules/video-rules.md').read_text().splitlines()
test(s['rule_mapping']['R16']['quote']==rl[40],'R16 quote exact current line41')
test(s['rule_mapping']['R54']['quote']==rl[180],'R54 quote exact current line181')
for c in s['cover_plan']['native_mapping_analysis']['computed']:
 maxw=920 if c['hero']=='REREAD ONLY' else 840
 calc=min(196,int(maxw/(len(c['hero'])*.66)))
 test(calc==c['fit_font_px'],'native fit heuristic '+c['hero'],calc)
test(s['cover']['hero_group_transform_plan']['native_left_px']+s['cover']['hero_group_transform_plan']['translate_x_px']-10==70,'native left−10 stroke +14px plan starts70>=60')
test('## Toàn bộ7 beat + endcard' in board and '| end/' in board,'same9-column presentation includes non-spoken endcard')
test('REREAD: LOW' not in board and 'strike=null' not in board,'no stale active update1 cover grammar in new board')
errors=[c['check'] for c in checks if not c['ok']]
result={'scope':'Declared planning arithmetic, JSON/text identity and source-record scope only. NOT image/DOM/glyph/render/production schema/audio/read-aloud/stranger/visual semantic approval.','script_sha256_before':frozen[str(script)],'script_sha256_after':sha(script),'script_unchanged':sha(script)==expected,'spoken_words':count,'pre_method_after_hook':50,'beats_unchanged':7,'caption_segments_unchanged':len(caps),'EN_max':max(len(c['en'].split()) for c in caps),'planning_check_count':len(checks),'errors':errors,'mock_state_simulation':states,'cover_plan_text_characters_including_native_ep_tag':39,'source_scope':'Deep scoped main text/fact PASS per read report; Social scoped trend/pain PASS per user/Reviewer handoff, not independently read Social report. New visuals unreviewed.','open':['Read-aloud/one-listen/stranger CHƯA KIỂM before Chốt; real audio timing is after Chốt, not a wording blocker','Preview CHƯA CHUẨN BỊ ẢNH; new visual mapping/cover meaning/conditional disclosure not visually reviewed','Registry/storage OPEN; text checker failures retained separately','Hero+14x/rig−40−70 adapters and static-preview glyph/crop unverified before full gate1; native strike0 grammar source-mapped. Video schema/real timings/HF/STT/render remain after Chốt','Endcard3s remains estimated; extra conditional disclosure readability not certified'],'checks':checks}
(B/'clip05-r11.4-plan-update2-validation-2026-11-07.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n');print('VALIDATION',len(checks),'errors',errors,'speech',count,'captions',len(caps),'script SHA',sha(script));sys.exit(1 if errors else 0)
