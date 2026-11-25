from pathlib import Path
import copy,json,re
B=Path('/workspace');s=json.loads((B/'opencreator-clip05-spec-r11.3-draft-2026-11-07.json').read_text());old=copy.deepcopy(s)
s.update(id='clip-05-r11.4-draft',version='r11.4')
b=s['beats'][0];before=b['text'];b['text']=before.replace('Bạn có thể nhận ra','Bạn vẫn có cách nhận ra')
b['marked_text']=b['marked_text'].replace('Bạn có thể nhận ra','Bạn vẫn có cách nhận ra')
for x in b['phrases_plan']:x['t']=x['t'].replace('Bạn có thể nhận ra','Bạn vẫn có cách nhận ra')
b['captions'][2]['vi_text']='Bạn vẫn có cách nhận ra chỗ thiếu,'
b['captions'][2]['en']='You still have a way to spot omissions,'
b['captions'][2]['hl']=[7]
b['emphasis_focus'][1]['caption_targets'][0].update(hl=[7],highlight_words=['omissions,'])
b['role']=b['role'].replace('Hứa: có thể nhận ra','Hứa: có cách nhận ra')
b['link']=b['link'].replace('hứa có thể nhận ra','hứa có cách nhận ra')
b['why_visual']=b['why_visual'].replace('→ có thể định danh','→ có cách định danh')
b['claim_source']='Chi tiết comic biên tập phát triển từ pain đọc–nhớ có nguồn cá nhân; không trích source như đã có cảnh này hoặc tần suất quên. Hứa có cách: gợi ý phương pháp tự kiểm rồi đối chiếu văn bản ở b05–b06, không bảo đảm hiệu quả/nhận ra mọi phần thiếu, không phải claim nghiên cứu.'
s['craft_qa_correction']={'reason':'Adding vẫn alone only broke a repeated ngram; retained có thể/promise form was still a craft defect, not resolved by checker silence.','before_promise':'Bạn vẫn có thể nhận ra chỗ thiếu, chứ không chỉ biết mình quên.','after_promise':'Bạn vẫn có cách nhận ra chỗ thiếu, chứ không chỉ biết mình quên.','scope':'One word thể→cách in b01 and the matching question reserve; b02–b07, first negative reserve and cover plan unchanged. Necessary EN/HL/metadata synchronization only.','claim_limit':'Có cách offers the existing self-test/compare method; no guarantee, new method, causal explanation or research claim.','approval':'Requested wording applied; human/read-aloud/fact-owner/reviewer gates still pending.'}
s['word_count']=150
s['hook_alts']=[copy.deepcopy(s['hook_alt']),{'type':'question + promise; not selected','text':'Bạn đọc để học, mà quên gì cũng không biết hả? Bạn vẫn có cách nhận ra chỗ thiếu, chứ không chỉ biết mình quên.','marked_text':'Bạn đọc để học, mà {nhấn: quên gì} cũng không biết hả? Bạn vẫn có cách nhận ra {nhấn: chỗ thiếu}, chứ không chỉ biết mình quên.','status':'Unselected reserve only; not in main transcript/count, not approved replacement'}]
s['hook_alts'][0]['marked_text']='Bạn đọc để học, đừng để {nhấn: chỗ chưa nhớ} chỉ mang tên “quên rồi”.'
s['hook_alts'][0]['status']='Unselected reserve only; preserved negative option, not in main count'
s['hook_alt']=copy.deepcopy(s['hook_alts'][0])
s['hook_alts_rules_audit']={'required':'checklist C44 L043 requires2 reserves; R64:231 requires at least1, not a cap. Keep hook_alt for compatibility plus explicit hook_alts[2].','options':[{'index':0,'type':'negative','word_count':len(s['hook_alts'][0]['text'].split()),'R64':'negative format, topic reading-to-learn; not a new method','P16_W16':'first clause4words; no niche/school subject/time jump; no procedure before goal','L094':'no open question to leave unanswered; editorial warning, not causal study claim','limitations':'warning is a proposal, not mandatory self-testing for pleasure reading; no listener approval'},{'index':1,'type':'question','word_count':len(s['hook_alts'][1]['text'].split()),'R64':'question about the same pain then a conditional promise; <=2sentences','P16_W16':'first clause4words, learning pain before promise; hả is a soft rhetorical invitation, no method before goal','L094':'second sentence answers the rhetorical unknown-omission pain with a promise of identifying missing content, not a new claim about texthip','limitations':'actual delivery/stranger/if selected whole-script fit pending; not counted or spoken'}],'selection':'Main hook retains accepted meaning/structure, promise revised to có cách after craft QA; thêm vẫn alone was insufficient for L093; neither reserve replaces it.'}
s['hook_alts_rules_audit']['options'][1]['R64']='question about the same pain followed by an offer of the existing method; <=2sentences'
s['hook_alts_rules_audit']['options'][1]['L094']='second sentence offers a way to identify missing content via b05–b06, not guaranteed effectiveness or a new research/texthip claim'
# Recompute only the provisional caption budget; all speech except b01 is byte-identical.
s['caption_segments_plan']=[];cursor=0
for i,b in enumerate(s['beats']):
    start=cursor
    if i==0:cursor+=.06
    wi=0
    for j,c in enumerate(b['captions']):
        n=len(c['vi_text'].split());dur=max(1.1,n/3.6)
        c['vi_word_range']=[wi,wi+n];c['interval_estimate_s']=[round(cursor,6),round(cursor+dur,6)]
        s['caption_segments_plan'].append({'id':c['id'],'beat':b['id'],'voice_line_ref':'vi-'+b['id'],'caption_ref':f'beats[{i}].captions[{j}]','en':c['en'],'hl':c['hl'],'vi_word_range':c['vi_word_range'],'interval_estimate_s':c['interval_estimate_s']})
        cursor+=dur;wi+=n
    assert ' '.join(c['vi_text'] for c in b['captions'])==b['text']
    b['estimate_s']=[round(start,6),round(cursor,6)];b['word_count']=wi
    for x in b['sfx']:
        tokens=b['text'].split();needle=x['word'].split();clean=lambda z:re.sub(r'[^\wÀ-ỹ]','',z).lower()
        loc=next(k for k in range(len(tokens)) if list(map(clean,tokens[k:k+len(needle)]))==list(map(clean,needle)))
        c=next(c for c in b['captions'] if c['vi_word_range'][0]<=loc<c['vi_word_range'][1]);at=round(c['interval_estimate_s'][0]+(loc-c['vi_word_range'][0])/3.6,6)
        x.update(word_range=[loc,loc+len(needle)],at_estimate_s=at,frame_estimate=round(at*30),line_offset_estimate_s=round(at-start,6),offset=None,frame=None)
    for hit,x in zip(b.get('hits',[]),b['sfx']):hit.update(at_estimate_s=x['at_estimate_s'],frame_estimate=x['frame_estimate'],word_range=x['word_range'],f=None)
    s['voice_lines_plan'][i]['interval_estimate_s']=b['estimate_s']
s['hook']['hits_estimate_s']=[x['at_estimate_s'] for x in s['beats'][0]['sfx']]
s['duration_estimate_s']=round(cursor+3,6);s['end_card']['estimate_s']=[round(cursor,6),round(cursor+3,6)]
s['hook_title_layer_plan']['interval_estimate_s']=s['beats'][0]['estimate_s']
s['scene_mapping']=[]
for part in s['parts_plan']:
    units=part.get('scenes',part.get('sections',[]))
    for u in units:
        b=next((b for b in s['beats'] if b['id']==u['beat']),None)
        if u['beat']=='b01':
            if u['id']=='b01-h3':u['interval_estimate_s'][1]=b['estimate_s'][1]
        elif b:u['interval_estimate_s']=b['estimate_s']
        else:u['interval_estimate_s']=s['end_card']['estimate_s']
        if b:
            u['voice_window_local_s_estimate']=[round(u['interval_estimate_s'][0]-b['estimate_s'][0],6),round(u['interval_estimate_s'][1]-b['estimate_s'][0],6)]
            u['sfx']=[copy.deepcopy(x) for x in b['sfx'] if u['interval_estimate_s'][0]<=x['at_estimate_s']<u['interval_estimate_s'][1]]
            u['hits']=copy.deepcopy(b.get('hits',[]))
            u['caption_segment_refs']=[c['id'] for c in b['captions'] if c['interval_estimate_s'][0]<u['interval_estimate_s'][1] and c['interval_estimate_s'][1]>u['interval_estimate_s'][0]]
        if u.get('transition_sfx_plan'):
            at=u['interval_estimate_s'][0];u['transition_sfx_plan'].update(at_estimate_s=round(max(0,at-.12),6),cut_at_estimate_s=at)
        for c in s['caption_segments_plan']:
            if c['id'] in u['caption_segment_refs']:c.setdefault('scene_refs',[]).append(u['id'])
        s['scene_mapping'].append({k:copy.deepcopy(u[k]) for k in ['beat','voice_line_ref','layout_ref','interval_estimate_s','caption_segment_refs']}|{'unit_id':u['id']})
    part['interval_estimate_s']=[units[0]['interval_estimate_s'][0],units[-1]['interval_estimate_s'][1]]
# Minimal illustration-group translation only: preserve A, colors, hero, all typography/logo slots.
cp=s['cover_plan'];baseline=copy.deepcopy(old['cover_plan']['conservative_allocations']);dx,dy=-40,-70
s['cover']['illustration_transform_plan']={'translate_x_px':dx,'translate_y_px':dy,'applies_to':['halo','chibi','emote'],'keep_unchanged':['direction A','dark theme','series/ep','hero/strike/accent','expression/action/tilt','text slots','logo slot'],'purpose':'Fix right30/bottom60 overshoot with10px right/bottom breathing room, without redesign','native_template_support':False,'status':'PLANNING override; current Cover.tsx fixed positions need adapter mapping later. No engine code/render/schema validation here.'}
s['cover']['note']='Native A props retained; one explicit illustration-group transform planned. Numeric bbox safe in this plan, not proof current fixed template implements override or images pass.'
fixed=[]
for o in baseline:
    x=copy.deepcopy(o)
    if o['id']=='rig+circle-reserve':x['bbox']=[o['bbox'][0]+dx,o['bbox'][1]+dy,*o['bbox'][2:]]
    fixed.append(x)
cp['baseline_observed_allocations_r11_3']=baseline
cp['conservative_allocations']=copy.deepcopy(fixed);cp['target_allocations']=copy.deepcopy(fixed)
cp['illustration_mapping']={'before_bbox':[390,1000,660,660],'translate_px':[dx,dy],'after_bbox':[350,930,660,660],'right_bottom_margins_px':[10,10],'props_ref':'cover.illustration_transform_plan','actual_renderer_implementation':'CHƯA KIỂM/NOT IMPLEMENTED in this read-only task'}
cp['observed_template']='Baseline Cover.tsx A fixed illustration envelope [390,1000,660,660] exceeded strict plan bounds. r11.4 translates illustration group(-40,-70); native template has no such exposed override yet, so planned mapping only, not a claim existing engine was fixed.'
cp['bounds_scope']='All r11.4 declared cover allocations map to one consistent transform and fit strict-safe numerically. Baseline kept separately for trace; no current-plan failure hidden. Not raster/glyph/rig/port validation.'
cp['target_status']='One unified r11.4 target, not two conflicting geometries. Native adapter/preview still OPEN; no images or engine edits.'
s['repeat_audit_note']='Craft QA rejected thêm vẫn alone: it only hid the ngram, retained có thể and the same promise form as b02. Replace b01 promise with Bạn vẫn có cách nhận ra chỗ thiếu, chứ không chỉ biết mình quên. This offers the existing method, does not guarantee effectiveness and is not a research claim. b02–b07 byte-identical; main150/pre50. Checker silence is not craft approval.'
s['patch_history']={'base_full_rewrite':'r11.2 architecture B','patch1':'r11.3: fixed hook pain–promise, semantic HL and planning map','patch2':'r11.4: promise-form wording corrected after craft QA, missing second reserve, cover safe translation and necessary synchronization','rewrite_threshold':'Do not count suffixes. Reviewer confirms patch2 does not trigger >=3 patches of same base; no new concept/outline requested.'}
s['patch_delta']=[{'issue':'L093 wording','location':'b01 canonical/marked_text/VI–EN caption slice; table/mapping','before':before,'after':s['beats'][0]['text'],'effect':'Compared with patch1: add vẫn and replace thể with cách; compared with initial r11.4: replace only thể with cách. Main150/pre50; b02–b07 unchanged; EN way/omissions, semantic HL and all bindings resynced. Prior ngram-only fix was insufficient; no craft pass inferred.','open':'actualSocial/Deep SHA; read-aloud/stranger'}, {'issue':'L043 two hook reserves','location':'hook_alt + hook_alts[0:2] + rules audit','before':'1 negative reserve','after':'2 reserves: retained negative + question/promise; neither reserve selected; main promise uses có cách after craft QA','effect':'R64 at least1 and checklist44 requires2 both represented; not part of count','open':'unselected alternatives not approved/voiced'}, {'issue':'Cover strict-safe bbox','location':'cover.illustration_transform_plan / cover_plan.illustration_mapping','before':'[390,1000,660,660]→right1050/bottom1660','after':'translation[-40,-70]→[350,930,660,660]→right1010/bottom1590','effect':'10px right/bottom margin versus strict x1020/y1600; A/theme/hero/text/logo/design unchanged','open':'native template override not implemented; actual images/schema/glyphs/rig unverified'}]
s['gates']['Deep_new_text']='CHƯA KIỂM actual r11.4 SHA';s['gates']['Social_new_wording']='CHƯA KIỂM actual r11.4 SHA';s['gates']['Reviewer']='CHƯA KIỂM r11.4';s['gates']['layout_arithmetic']='r11.4 dedicated numeric report; planned boxes/transform only, not actual renderer or image QA'
s['issue_resolution']=[{'issue':x['issue'],'location':x['location'],'change':x['after'],'open':x['open']} for x in s['patch_delta']]
s['revisions'].append({'date':'2026-11-07','note':'r11.4 = patch2 of B per Reviewer r11.3. Only3 scoped fixes; r11.3 untouched. No rewrite/research/code/image/audio/render/message.'})
assert [b['text'] for b in s['beats'] if b['id']!='b01']==[b['text'] for b in old['beats'] if b['id']!='b01']
assert sum(len(b['text'].split()) for b in s['beats'])==150
assert sum(len(b['text'].split()) for b in s['beats'][1:4])==50
(B/'opencreator-clip05-spec-r11.4-draft-2026-11-07.json').write_text(json.dumps(s,ensure_ascii=False,indent=2)+'\n')
print('Patched b01:',s['beats'][0]['text']);print('Cover:',cp['illustration_mapping']);print('Count150/pre50; patch2, not rewrite')
