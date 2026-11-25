"""Local text/geometry arithmetic only; never imports/builds a video engine."""
from pathlib import Path
import re,json,hashlib,itertools,math,sys
B=Path('/workspace');P=B/'opencreator-clip05-spec-r11.3-draft-2026-11-07.json';s=json.loads(P.read_text());errors=[];checks=[];cover_findings=[]
def test(ok,what,detail=None):
    checks.append({'check':what,'ok':bool(ok),'detail':detail})
    if not ok:errors.append(what)
def rect(box):x,y,w,h=box;return [x,y,x+w,y+h]
def inside(a,b):a=rect(a);b=rect(b);return a[0]>=b[0]-1e-6 and a[1]>=b[1]-1e-6 and a[2]<=b[2]+1e-6 and a[3]<=b[3]+1e-6
def envelope(o):
    x,y,w,h=o['bbox'];m=o['motion_envelope'];cx=x+w/2;cy=y+h/2;corners=[]
    for dx,dy,k in itertools.product(m['x'],m['y'],m['scale']):corners.append((cx-w*k/2+dx,cy-h*k/2+dy,cx+w*k/2+dx,cy+h*k/2+dy))
    return [min(c[0] for c in corners),min(c[1] for c in corners),max(c[2] for c in corners)-min(c[0] for c in corners),max(c[3] for c in corners)-min(c[1] for c in corners)]
def overlap(a,b):a=rect(a);b=rect(b);return max(0,min(a[2],b[2])-max(a[0],b[0]))*max(0,min(a[3],b[3])-max(a[1],b[1]))
units=[u for p in s['parts_plan'] for u in p.get('scenes',p.get('sections',[]))];ids={u['id'] for u in units};cids={c['id'] for c in s['caption_segments_plan']};lids={v['id'] for v in s['voice_lines_plan']}
transcript=' '.join(b['text'] for b in s['beats']);test(140<=len(transcript.split())<=175,'spoken word range',len(transcript.split()));test(s['word_count']==len(transcript.split()),'word metadata matches');test(sum(len(b['text'].split()) for b in s['beats'][1:4])==s['pre_method_words_after_hook']<=50,'pre-method <=50',s['pre_method_words_after_hook'])
for b in s['beats']:
    plain=re.sub(r'\{nhấn: ([^}]+)\}',r'\1',b['marked_text']);stress=re.findall(r'\{nhấn: ([^}]+)\}',b['marked_text'])
    test(plain==b['text'],b['id']+' markup/text');test(1<=len(stress)<=2,b['id']+' 1–2 VI stresses');test([x['vi'] for x in b['emphasis_focus']]==stress,b['id']+' focus exact markup')
    test(' '.join(c['vi_text'] for c in b['captions'])==b['text'],b['id']+' translation slice coverage')
    for c in b['captions']:
        w=c['en'].split();test(len(w)<=8,c['id']+' <=8 words',len(w));test(all(0<=i<len(w) for i in c['hl']),c['id']+' valid highlights')
        bad={"when","ah","say","would","comment","keep","become","the","a","an","you","it","and","but","or","to","for","of"}
        test(not any(re.sub(r'[^a-z]','',w[i].lower()) in bad for i in c['hl']),c['id']+' no flagged function-word focus',[w[i] for i in c['hl']])
        test(c['interval_estimate_s'][1]-c['interval_estimate_s'][0]>=1.-1e-6,c['id']+' planned display>=1s')
        gc=next(z for z in s['caption_segments_plan'] if z['id']==c['id']);test(gc['en']==c['en'] and gc['hl']==c['hl'],c['id']+' global binding')
    for sf in b['sfx']:
        test(sf['word'] in b['text'],b['id']+' SFX spoken anchor '+sf['word']);at=sf['at_estimate_s'];target=[u for u in units if u['beat']==b['id'] and u['interval_estimate_s'][0]<=at<u['interval_estimate_s'][1]]
        test(len(target)==1 and any(z['word']==sf['word'] and z['at_estimate_s']==at for z in target[0]['sfx']),b['id']+' SFX mapped once '+sf['word'])
    test(b['fx']['doodles']==[],b['id']+' doodle0')
for i,u in enumerate(units):
    a,z=u['interval_estimate_s'];test(0<z-a<=8+1e-6,u['id']+' positive/<=8 estimate',round(z-a,6));test(u['layout_ref'] in s['layout_plans'],u['id']+' layout ref')
    test(u['voice_line_ref'] is None if u['beat']=='end' else u['voice_line_ref'] in lids,u['id']+' narration-line mapping')
    test(all(c in cids for c in u['caption_segment_refs']),u['id']+' caption refs')
    if i:test(abs(a-units[i-1]['interval_estimate_s'][1])<1e-5,u['id']+' scene timeline contiguous')
for x,y in zip(s['caption_segments_plan'],s['caption_segments_plan'][1:]):test(x['interval_estimate_s'][1]<=y['interval_estimate_s'][0]+1e-6,x['id']+' no caption time overlap')
test(units[0]['narration']['text']==s['hook']['text'],'first scene narration.text == hook.text')
test(all(x in ids for x in s['hook']['scenes']),'hook ids resolve')
test(len(s['hook']['cuts_estimate_s'])>=1 and sum(x<3 for x in s['hook']['cuts_estimate_s'])+sum(x<3 for x in s['hook']['hits_estimate_s'])>=2,'hook >=2 cut/hit events incl cut in0–3 estimate')
layout_measurements=[]
for id,lay in s['layout_plans'].items():
    boxes=[]
    for o in lay['objects']:
        e=envelope(o);boxes.append((o['id'],e))
        if o.get('existing_prop_binding_plan'):
            q=o['existing_prop_binding_plan'];x,y,z,w=q['local_bounds'];m=q['padding'];k=q['s']
            calc=[q['x']+x*k-m,q['y']+y*k-m,(z-x)*k+2*m,(w-y)*k+2*m]
            test(all(abs(a-b)<1e-6 for a,b in zip(calc,o['bbox'])),id+'/'+o['id']+' matches existing prop arithmetic',calc)
        test(inside(e,s['frame']['zones'][o['zone']]),id+'/'+o['id']+' motion envelope inside '+o['zone'],e)
        test(inside(e,s['frame']['zones']['screen']),id+'/'+o['id']+' inside screen')
        if o['zone']=='content':test(not overlap(e,s['frame']['zones']['caption']),id+'/'+o['id']+' avoids caption zone')
    collisions=[]
    for (a,ab),(b,bb) in itertools.combinations(boxes,2):
        area=overlap(ab,bb)
        if area>1e-6:collisions.append({'a':a,'b':b,'area':area})
    test(not collisions,id+' allocated top-level envelopes disjoint',collisions)
    layout_measurements.append({'id':id,'motion_envelopes':dict(boxes),'collisions':collisions})
for engine,box in s['frame']['caption_reserved_bbox'].items():test(inside(box,s['frame']['zones']['caption']),engine+' caption allocation inside caption zone',box)
for c in s['cover_plan']['target_allocations']:test(inside(c['bbox'],s['cover_plan']['rule_safe_zone']),'cover target/'+c['id']+' strict-safe',c['bbox'])
for c in s['cover_plan']['conservative_allocations']:
    ok=inside(c['bbox'],s['cover_plan']['rule_safe_zone'])
    cover_findings.append({'id':c['id'],'bbox':c['bbox'],'inside_strict_rule_safe':ok,'status':'EXPECTED OPEN template envelope mismatch, not ignored' if not ok else 'allocated only; no image'})
md=B/'opencreator-clip05-script-r11.3-draft-2026-11-07.md'
if md.exists():
    rows=re.findall(r'^\d+\. \*\*\[[^\]]+\]\*\* (.*)$',md.read_text(),re.M);test(rows==[b['text'] for b in s['beats']],'MD canonical words == JSON')
sourcehash=json.loads((B/'clip05-r11.2-readonly-source-hashes-2026-11-07.json').read_text());changed=[]
for file,h in sourcehash.items():
    want=h if isinstance(h,str) else h['sha256'];got=hashlib.sha256((B/'oneup-studio'/file).read_bytes()).hexdigest()
    if got!=want:changed.append(file)
test(not changed,'7 recorded repo source hashes unchanged',changed)
result={'scope':'Arithmetic on declared PLANNED allocations/time budgets, NOT render/DOM/glyph QA, NOT production schema or manual semantic approval','script_words':len(transcript.split()),'per_beat_words':[len(b['text'].split()) for b in s['beats']],'pre_method_after_hook':s['pre_method_words_after_hook'],'EN_max':max(len(c['en'].split()) for b in s['beats'] for c in b['captions']),'planning_check_count':len(checks),'planning_arithmetic_errors':errors,'layout_measurements':layout_measurements,'cover_current_template_envelope_findings':cover_findings,'open':['Actual cover reserved rig+circle fails strict x/right and y/bottom, target is a future port not current props','Hook narration target170 vs current template default66 unresolved','EN_FONT/BVP compliance, actual caption wrapping/height, HF <=4 subgroups and timing not inspected in frames','Reels geometry not mapped; this standard1080x1920 TikTok plan only','Preview gate1 CHƯA CHUẨN BỊ ẢNH; read-aloud/stranger/timing CHƯA KIỂM; actualDeep/Social/Reviewer SHA pending'],'checks':checks}
(B/'clip05-r11.3-local-validation-2026-11-07.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print('Declared plan checks:',len(checks),'errors:',errors);print('Cover CURRENT template envelope:',cover_findings);print('Counts:',result['per_beat_words'],len(transcript.split()),'pre-method',s['pre_method_words_after_hook']);sys.exit(1 if errors else 0)
