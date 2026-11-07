from pathlib import Path
import copy,json,re,hashlib
B=Path('/workspace');V='r11.3';DATE='2026-11-07'
s=json.loads((B/'opencreator-clip05-spec-r11.2-draft-2026-11-07.json').read_text())
s.update(id='clip-05-r11.3-draft',version=V,word_count=149,throughline='Bạn đọc để học VÀ vẫn có thể đọc vui NHƯNG không gọi tên được phần mình chưa nhớ VÌ VẬY chọn mục tiêu nhận ra phần thiếu, tự kiểm rồi đối chiếu đúng văn bản. Đây là khung biên tập, không suy causal từ trend.',hook_question='Có thể nhận ra phần nội dung chưa nhớ thay vì chỉ biết mình quên không? (câu hỏi ngầm; không yêu cầu kể khi chưa giới thiệu thao tác)')
s['source']['pain']['limits']='One archived independent individual, not channel audience/texthip participant. Supports reading-memory illustration only; not proof of the hook scene, uncertainty about omissions, a retrieval test, frequency, mechanism or efficacy. Do not quote archive line18. No fresh raw/live.'
s['source']['metadata_addendum']={'path':'/workspace/clip05-texthip-metadata-2026-11-07.json','updated_at':'2026-11-07T14:51:17+07:00','commit':None,'status':'owner addendum outside repo; archive/registry unresolved; not edited in this revision'}
s['hook_alt']={'type':'negative; not selected','text':'Bạn đọc để học, đừng để chỗ chưa nhớ chỉ mang tên “quên rồi”.','status':'Unreviewed alternative, not spoken/count; no separate outline round'}
b=s['beats'][0]
b.update(text='Bạn đọc để học, mà quên gì cũng không biết. Bạn có thể nhận ra chỗ thiếu, chứ không chỉ biết mình quên.',marked_text='Bạn đọc để học, mà {nhấn: quên gì cũng không biết}. Bạn có thể nhận ra {nhấn: chỗ thiếu}, chứ không chỉ biết mình quên.',role='Pain: chưa gọi tên được nội dung đã quên. Hứa: có thể nhận ra phần thiếu; cùng một đối tượng nội dung, không nói phần kể đã tồn tại.',emotion='Khựng vì không gọi tên được điều đã quên, rồi tò mò; không chê người học.',context='Một lần đọc ở bàn, cùng sách mock; chưa giới thiệu thao tác tự kiểm, chưa có phần kể.',shot='h1 sách mở + người đọc; cut0.8s sang phản ứng khựng h2; cut2s về cuốn sách h3. Không lật tìm trang, không gấp sách làm test trong hook.',stage={'action':'Người đọc dừng mắt trên trang, nét mặt ngơ ngác, bàn tay mở nhẹ; rig thở/chớp mắt. Cuốn sách không đổi thành kết quả kiểm tra.','react':'Khựng vì không gọi tên được điều đã quên, rồi tò mò.'},pause_plan='Phẩy sau học; câu đầu rơi ở không biết. Câu hứa liền mạch, nhấn chỗ thiếu; không chia chữ theo cut.',link='S1 chưa gọi tên được phần quên → S2 hứa có thể nhận ra phần thiếu ấy. Không cần người nghe tự thêm hành động kể hoặc mốc ngay đó.',why_visual='Đảo ở nội dung: không biết mình quên gì → có thể định danh chỗ thiếu; không lấy whip thay novelty. Đây là giả thuyết lực mở, chưa người lạ/nghe/timing.',claim_source='Chi tiết comic biên tập phát triển từ pain đọc–nhớ có nguồn cá nhân; không trích source như đã có cảnh này hoặc tần suất quên. Hứa giới hạn có thể, chỉ đối chiếu văn bản.')
b['fx']['visual']='Whip vào phản ứng khựng khi không gọi tên được nội dung quên; cùng rig/sách, không tạo vật mới.'
b['fx']['word']='quên gì cũng không biết'
b['sfx'][0]['word']='quên gì cũng không biết';b['sfx'][1]['word']='chỗ thiếu'
b['captions']=[{'en':e,'hl':h} for e,h in [('You read to learn,',[]),("but can’t even tell what you forgot.",[6]),('You may spot what’s missing,',[4]),('instead of only knowing you forgot.',[])]]
# Every EN highlight is an explicit meaning choice, not a positional default.
for i,hs in {1:[[],[2],[1]],2:[[],[],[0,1],[0,1]],3:[[],[4,5]],4:[[6],[],[],[4]],5:[[],[1],[2]],6:[[],[3,5],[3,5]]}.items():
    for c,h in zip(s['beats'][i]['captions'],hs):c['hl']=h
# VI slices are complete, exact, ordered coverage; these are caption bindings, not TTS cuts.
vi_chunks=[
 ['Bạn đọc để học,','mà quên gì cũng không biết.','Bạn có thể nhận ra chỗ thiếu,','chứ không chỉ biết mình quên.'],
 ['Text hip ở Hàn gắn sách với phong cách sống;','bạn có thể vừa đọc vui','vừa học.'],
 ['Còn cách học,','nhóm Dunlosky năm 2013 đánh giá mười kỹ thuật,','xếp tự kiểm hữu ích cao,','đọc lại thấp.'],
 ['Bạn muốn biết chỗ nào','trong trang sách chưa nhớ hông?'],
 ['Muốn biết, Cẩm nang sống đáng giá khuyên tự kiểm nè.','Ví dụ đọc trang chi tiêu,','bạn gấp lại, kể điều nhớ được,','rồi mở ra dò.'],
 ['Lúc dò, bạn nhận ra bài nhắc ghi cả','tiền thuê nhà, còn phần kể chỉ có tiền ăn.','À, bạn bổ sung khoản vừa sót đó.'],
 ['Giả sử kể lại trang bạn vừa đọc,','bạn thấy đủ hay thiếu?','Bình luận một chữ đủ hoặc thiếu nha.']]
focus=[
 [('quên gì cũng không biết',[(1,[6])]),('chỗ thiếu',[(2,[4])])],
 [('vừa đọc vui vừa học',[(1,[2]),(2,[1])])],
 [('tự kiểm',[(2,[0,1])]),('đọc lại thấp',[(3,[0,1])])],
 [('chưa nhớ',[(1,[4,5])])],
 [('tự kiểm',[(0,[6])]),('dò',[(3,[4])])],
 [('tiền thuê nhà',[(1,[1])]),('bổ sung',[(2,[2])])],
 [('đủ hay thiếu',[(1,[3,5])]),('đủ hoặc thiếu',[(2,[3,5])])]]
s['timing_model']={'status':'ESTIMATE ONLY — CHƯA KIỂM timing, not word timestamps','method':'budget each VI caption slice at 3.6 whitespace words/s, minimum1.1s of planned caption time; voice onset0.06s only in b01. This is a provisional scheduling budget, NOT instructions to split/slow audio. Real voice remains one continuous line across hook cuts. Replace all estimated windows after Chốt/real voice.','caption_intervals':'half-open [start,end); global caption layer spans cuts; no two caption segments simultaneously','units':'seconds absolute from TikTok hook frame0; frame_estimate=round(seconds*30), never f measured','tts_warning':'VI slices bind translation only, NOT F5 generation units. No TTS cuts except punctuation, after Chốt.'}
s['caption_segments_plan']=[];s['voice_lines_plan']=[];cursor=0.;words=0
for i,b in enumerate(s['beats']):
    assert ' '.join(vi_chunks[i])==b['text'],b['id']
    b['phrases_plan']=[{'t':x.strip(),'pause_status':'punctuation-led only; no audio'} for x in re.findall(r'.+?(?:[.!?](?:\s|$)|$)',b['marked_text']) if x.strip()]
    start=cursor
    if i==0:cursor+=.06
    w=0
    for j,(cap,vi) in enumerate(zip(b['captions'],vi_chunks[i])):
        n=len(vi.split());dur=max(1.1,n/3.6);cid=f'{b["id"]}-cap{j+1:02d}'
        cap.update(id=cid,vi_text=vi,vi_word_range=[w,w+n],interval_estimate_s=[round(cursor,6),round(cursor+dur,6)],timing='ESTIMATE; not real voice alignment')
        s['caption_segments_plan'].append({'id':cid,'beat':b['id'],'voice_line_ref':'vi-'+b['id'],'caption_ref':f'beats[{i}].captions[{j}]','en':cap['en'],'hl':cap['hl'],'vi_word_range':cap['vi_word_range'],'interval_estimate_s':cap['interval_estimate_s']})
        cursor+=dur;w+=n
    assert w==len(b['text'].split())
    b['estimate_s']=[round(start,6),round(cursor,6)];b['word_count']=w;words+=w
    b['emphasis_focus']=[{'vi':vi,'caption_targets':[{'id':b['captions'][j]['id'],'hl':h,'highlight_words':[b['captions'][j]['en'].split()[x] for x in h]} for j,h in targets]} for vi,targets in focus[i]]
    b['emphasis_reason']='Only meaning-bearing targets above; unaccented lead-in chunks intentionally hl=[]. Multiple indexes within one semantic focus are not extra spoken stresses.'
    # Estimate a word anchor from the caption budget; never mark it a real cue.
    for sf in b['sfx']:
        needle=sf['word'].split();tokens=b['text'].split();clean=lambda t:re.sub(r'[^\wÀ-ỹ]','',t).lower()
        loc=next(k for k in range(len(tokens)) if list(map(clean,tokens[k:k+len(needle)]))==list(map(clean,needle)))
        cap=next(c for c in b['captions'] if c['vi_word_range'][0]<=loc<c['vi_word_range'][1])
        at=cap['interval_estimate_s'][0]+(loc-cap['vi_word_range'][0])/3.6
        sf.update(word_range=[loc,loc+len(needle)],at_estimate_s=round(at,6),frame_estimate=round(at*30),frame=None,cue='planned word onset inside matching caption slice; RESNAP after real voice; not measured')
    if b.get('hits'):
        for hit,sf in zip(b['hits'],b['sfx']):hit.update(at_estimate_s=sf['at_estimate_s'],frame_estimate=sf['frame_estimate'],f=None,timing_status='ESTIMATE ONLY; not voice-aligned',word_range=sf['word_range'])
    s['voice_lines_plan'].append({'id':'vi-'+b['id'],'beat':b['id'],'text_ref':f'beats[{i}].text','marked_text_ref':f'beats[{i}].marked_text','speaker':'hiep','interval_estimate_s':b['estimate_s'],'continuous_across_scenes':True,'audio_created':False,'word_timestamps':None})
s['word_count']=words;assert 140<=words<=175
s['pre_method_words_after_hook']=sum(b['word_count'] for b in s['beats'][1:4]);assert s['pre_method_words_after_hook']<=50
s['end_card']['estimate_s']=[round(cursor,6),round(cursor+3,6)];s['duration_estimate_s']=round(cursor+3,6)
s['frame']={'width':1080,'height':1920,'fps':30,'bbox_format':'x,y,width,height; includes declared margins/shadow reserve; NOT DOM measured bounds','zones':{'screen':[0,0,1080,1920],'content':[60,150,960,1310],'caption':[60,1488,960,312],'logo':[60,80,100,70],'cover_rule':[60,290,960,1310]},'caption_reserved_bbox':{'remotion':[70,1488,948,272],'hyperframes':[70,1500,948,272]},'font':'Be Vietnam Pro LOCAL required for all text','logo':'brand logo05-pair-plus top-left; own overlay slot, not an exception silently applied to content','colors':['#111111','#F7F7F5','#FF5A36'],'grain':'existing subtle layer; not created now','reference_geometry':[{'path':'video-engine/src/composition/layout.ts','lines':'6–8','observed':'content SAFE x60–1020/y150–1460; PAD36'},{'path':'video-engine/src/composition/SceneRenderer.tsx','lines':'41–42,80–82','observed':'standard capTop=1920*.775=1488; reels=1000, NOT this standard plan; standard narration top66'},{'path':'video-engine/src/composition/Caption.tsx','lines':'20–22,30','observed':'standard caption left/right70, shadow8/10; wrapping height dynamic; EN_FONT currently used (font compliance unresolved)'},{'path':'content/samples/sample-natural/explainer/compositions/captions.html.tpl','lines':'10–13,19–22','observed':'HF caption top1500, max-width940 + shadow; BVP58, subgroup MAXW4; exact actual subgroup timing/overflow not validated'}],'limits':'caption boxes reserve at most272px including shadow, NOT observed height; actual wrap/font/glyph metrics/reels remap must be checked later. Content and caption are separate zones, not contradictory safezone claims.'}
# Each declared envelope encloses all proposed entry/hold states, including named motion excursions.
def obj(id,box,zone='content',motion=None):return {'id':id,'bbox':box,'zone':zone,'motion_envelope':motion or {'x':[0,0],'y':[0,0],'scale':[1,1]},'bbox_status':'PLANNED allocation, not actual renderer projection'}
logo=obj('logo',[60,80,100,70],'logo')
actor=obj('hiep-rig',[660,390,300,350]);book=obj('same-book',[140,800,720,639]);bubble=obj('vi-bubble',[100,350,500,380]);head=obj('hook-title',[180,170,780,150]);panel=obj('context-panel',[180,180,780,130])
layouts={
 'hook-wide':{'objects':[copy.deepcopy(logo),copy.deepcopy(head),copy.deepcopy(actor),copy.deepcopy(book)],'bubble':False},
 'hook-reaction':{'objects':[copy.deepcopy(logo),copy.deepcopy(head),obj('hiep-rig',[211,390,648,700],motion={'x':[0,60],'y':[0,0],'scale':[1,1]})],'bubble':False},
 'reading-context':{'objects':[copy.deepcopy(logo),copy.deepcopy(panel),copy.deepcopy(bubble),copy.deepcopy(actor),copy.deepcopy(book)],'bubble':True},
 'reading-goal':{'objects':[copy.deepcopy(logo),copy.deepcopy(bubble),copy.deepcopy(actor),obj('same-book',[140,800,720,639],motion={'x':[0,18],'y':[0,0],'scale':[1,1]})],'bubble':True},
 'reading-method':{'objects':[copy.deepcopy(logo),copy.deepcopy(bubble),copy.deepcopy(actor),copy.deepcopy(book)],'bubble':True},
 'ranking':{'objects':[copy.deepcopy(logo),obj('ranking-heading',[100,220,880,100]),obj('ranking-objects',[90,350,900,1020],motion={'x':[0,0],'y':[0,16],'scale':[1,1]})],'bubble':False},
 'comparison':{'objects':[copy.deepcopy(logo),obj('comparison-heading',[100,220,880,100]),obj('source-retelling',[90,350,900,1020],motion={'x':[0,8],'y':[0,0],'scale':[1,1]})],'bubble':False},
 'cta':{'objects':[copy.deepcopy(logo),copy.deepcopy(bubble),copy.deepcopy(actor),obj('comment-options',[100,820,760,340],motion={'x':[0,0],'y':[0,0],'scale':[.96,1]})],'bubble':True},
 'credit':{'objects':[copy.deepcopy(logo),obj('credit-block',[70,240,940,1140])],'bubble':False}}
for lay in layouts.values():
    lay['camera_push']=0;lay['box_scope']='Top-level non-overlapping allocations only. Props/rig strokes, bubble tail and actual camera transform MUST be measured later; not renderer layoutCheck.'
    lay['bubble_policy']='Where true, VI display by punctuation-led phrase, font44 target; measured fit pending. Entire beat must not be pasted into one fixed bubble.'
s['layout_plans']=layouts
s['layout_port_requirements']=[{'item':'Hook title target y170 (inside content SAFE)','actual_default':'SceneRenderer standard narration top66; no claim target already implemented','status':'OPEN adapter/template mapping; cannot certify actual layout from plan'},{'item':'All fonts BVP local','actual_default':'Caption.tsx uses EN_FONT; this revision does not change fonts.ts/engine','status':'OPEN production font audit; no engine changes'},{'item':'Caption height <= declared reserve; HF may split <=4 words','actual_default':'Current wrap/HL padding/MAXW4 runtime can change real bounds/timing','status':'OPEN actual text measurement, subgroup timing and still QA; do not discard approved caption chunks'},{'item':'Reels/Shorts layout','actual_default':'reels captions top1000/narrow; different from this standard TikTok plan','status':'NOT MAPPED/NOT VERIFIED here; separate future layout, not safe by inheritance'}]
s['hook']={'text':'FORGOT... WHAT?','scenes':['b01-h1','b01-h2','b01-h3'],'voice_line_ref':'vi-b01','voice_onset_estimate_s':.06,'cuts_estimate_s':[.8,2.0],'hits_estimate_s':[x['at_estimate_s'] for x in s['beats'][0]['sfx']],'verified':False,'narration_semantics':'Display EN title, NOT spoken VI text. First scene narration.text equals hook.text exactly. One continuous VI line spans all three cuts; title/captions persist as global layers.','early_event_plan':'Two cuts .8/2.0 plus first semantic hit about1.45s. Second hit after3s; not falsely counted as early hit.'}
# Complete plan mapping: target parts[].scenes/sections, not runnable engine parts.
parts=[];s['scene_mapping']=[]
def unit(id,bid,interval,layout,narr=None,kind='scene'):
    b=next((x for x in s['beats'] if x['id']==bid),None)
    capids=[c['id'] for c in b['captions'] if c['interval_estimate_s'][0]<interval[1] and c['interval_estimate_s'][1]>interval[0]] if b else []
    return {'id':id,'beat':bid,'part':'hook' if bid=='b01' else ('end' if bid=='end' else b['label']),'interval_estimate_s':interval,'voice_line_ref':None if not b else 'vi-'+bid,'voice_window_local_s_estimate':None if not b else [round(interval[0]-b['estimate_s'][0],6),round(interval[1]-b['estimate_s'][0],6)],'narration':None if narr is None else {'text':narr,'start_estimate_s':interval[0],'end_estimate_s':interval[1]},'inherit_narration_from':'b01-h1' if bid=='b01' and narr is None else None,'caption_segment_refs':capids,'caption_layer':'global continuous segment layer; no restart at hook cut','layout_ref':layout,'transition':'cut' if bid=='b01' else 'cut-on-motion','fx':copy.deepcopy(s['end_card']['fx'] if not b else b['fx']),'sfx':[],'hits':copy.deepcopy(b.get('hits',[])) if b else [],'production_target':'parts[].sections[]' if kind=='section' else 'parts[].scenes[]','runnable':False}
def part(id,engine,units,kind):
    parts.append({'id':id,'engine':engine,'interval_estimate_s':[units[0]['interval_estimate_s'][0],units[-1]['interval_estimate_s'][1]],'scenes' if kind=='scene' else 'sections':units})
b=s['beats'];h=[unit('b01-h1','b01',[0,.8],'hook-wide',s['hook']['text']),unit('b01-h2','b01',[.8,2.0],'hook-reaction'),unit('b01-h3','b01',[2.0,b[0]['estimate_s'][1]],'hook-wide')]
part('A','remotion',h+[unit('b02-s1','b02',b[1]['estimate_s'],'reading-context')],'scene')
part('E1','hyperframes',[unit('b03-e1','b03',b[2]['estimate_s'],'ranking',kind='section')],'section')
part('B','remotion',[unit('b04-s1','b04',b[3]['estimate_s'],'reading-goal'),unit('b05-s1','b05',b[4]['estimate_s'],'reading-method')],'scene')
part('E2','hyperframes',[unit('b06-e1','b06',b[5]['estimate_s'],'comparison',kind='section')],'section')
part('C','remotion',[unit('b07-s1','b07',b[6]['estimate_s'],'cta'),unit('end-s1','end',s['end_card']['estimate_s'],'credit')],'scene')
allunits=[u for p in parts for u in p.get('scenes',p.get('sections',[]))]
for u in allunits:
    bb=next((x for x in b if x['id']==u['beat']),None)
    if bb:
        u['sfx']=[copy.deepcopy(sf) for sf in bb['sfx'] if u['interval_estimate_s'][0]<=sf['at_estimate_s']<u['interval_estimate_s'][1]]
    for k,at in enumerate(s['hook']['cuts_estimate_s'] if u['beat']=='b01' else []):
        if u['interval_estimate_s'][0]==at:u['transition_sfx_plan']={'name':'swish','at_estimate_s':round(at-.12,6),'cut_at_estimate_s':at,'cue_type':'CUT; not word emphasis'}
    for c in s['caption_segments_plan']:
        if c['id'] in u['caption_segment_refs']:c.setdefault('scene_refs',[]).append(u['id'])
    s['scene_mapping'].append({'beat':u['beat'],'unit_id':u['id'],'voice_line_ref':u['voice_line_ref'],'layout_ref':u['layout_ref'],'interval_estimate_s':u['interval_estimate_s'],'caption_segment_refs':u['caption_segment_refs']})
s['parts_plan']=parts
s['production_schema_status']='NOT VALIDATED/NOT RUNNABLE. parts_plan is explicit mapping, not production parts; no build, no npx, no engine code. Estimated f fields are separate from measured f=null.'
s['cover'].update(ep=5,emote='!',note='Plan only. ep number5; emote! supported in Cover.tsx. expressionconfused/actionthinking listed. Full engine schema validation and image review NOT done.')
s['cover_plan']={'preview_status':'CHƯA CHUẨN BỊ ẢNH','template':'video-engine/src/composition/Cover.tsx directiona','required_previews':['cover-a.png','cover-b.png','cover-c.png','profile-grid/contactsheet'],'rule_safe_zone':[60,290,960,1310],'observed_template':'Cover.tsx10 says slots300–1620, actual A series310/hero420/chibi ground1640/logo1470; circle x720 r330 extends1050, y1660. This is a real template/rule mismatch to verify later, not silently solved by a made-up cover bbox.','conservative_allocations':[{'id':'series','bbox':[72,310,850,80]},{'id':'hero','bbox':[66,420,930,380]},{'id':'rig+circle-reserve','bbox':[390,1000,660,660]},{'id':'logo','bbox':[72,1470,260,70]}],'bounds_scope':'Numeric screen+rule-envelope tests only, not actual raster or glyph bounds; rig+circle reserve intentionally exposes x/right/y/bottom exceeding strict rule-safe. Must resolve before visual gate.'}
s['preview_gate1']={'status':'CHƯA CHUẨN BỊ ẢNH','storyboard_png':False,'contactsheet':False,'cover_previews':False,'two_eye_review_rounds':False,'reason':'This task authorizes text/JSON/planning arithmetic only, NO images/voice/render. Preview images are a separate missing gate before presentation; they are NOT the same as Chốt lời or final video render. No claim images must wait until script Chốt in all cases.'}
s['gates'].update(Deep_new_text='CHƯA KIỂM actual r11.3 SHA',Social_new_wording='CHƯA KIỂM actual r11.3 SHA',Reviewer='CHƯA KIỂM r11.3',preview_gate1='CHƯA CHUẨN BỊ ẢNH',layout_arithmetic='See separate numeric validation report; only declared allocations, not renderer QA',schema='CHƯA KIỂM production schema; explicit plan map only')
s['revisions'].append({'date':DATE,'note':'r11.3 fixes Reviewer r11.2 F1/F2 hook target, F3 semantic highlight, F4 mapping/bounds and F5 preview disclosure. ContextB/method/ranking/CTA preserved; no new research/engine changes.'})
s['issue_resolution']=[
 {'issue':'F1/D23 pain–hứa–payoff','location':'beats.b01.text / b06; sentence audit','change':'Bỏ tìm trang/kể thiếu/ngay đó; cùng đối tượng nội dung chưa nhớ→có thể thấy chỗ thiếu→định danh tiền thuê nhà khi đối chiếu.','open':'Reviewer nghe/logic; actualDeep/Social SHA; not self-pass'},
 {'issue':'F2 hook force','location':'b01 / hook / b01-h1..h3','change':'Đảo từ không biết quên gì sang có thể nhận ra chỗ thiếu; 3s đầu chỉ đọc/học chung, không gài khoảnRent/nhân vật trend hay phép thử mới.','open':'Peak/stranger/read-aloud/timing CHƯA KIỂM'},
 {'issue':'F3 semantic EN highlights','location':'beats[].captions[].hl + emphasis_focus','change':'Audit từngchunk; b06 nhấnrent/add, b07complete/missing; bỏhl ởlead-in. VI/EN targets explicit, not index0 default.','open':'Translation/emphasis independent review; voice/frame future'},
 {'issue':'F4 mapping + hook narration','location':'parts_plan / voice_lines_plan / caption_segments_plan / scene_mapping','change':'Mỗi scene/section trỏline/caption/layout; firstnarration.text=hook.text; cuts không chia lời; wordSFX córange + thời gianước, earlycuts riêng.','open':'Không production schema/renderable; timing thật/f=null còn thiếu'},
 {'issue':'F4 safezone conflict','location':'frame.zones / layout_plans / numeric sidecar','change':'Tách content150–1460 và caption1488/1500 theoactualtemplate; kiểmallocation vàmotionenvelope số học; không gọiđã thấyframe.','open':'Actual font/wrap/bubble/camera/port title/reels chưaQA; coverstrictsafe mismatch côngkhai'},
 {'issue':'F5 preview gate1','location':'preview_gate1 / cover_plan / storyboard','change':'Ghi CHƯA CHUẨN BỊ ẢNH, phânbiệtpreview vsChốtlời vsvoice/video.','open':'PNG/contactsheet/cover3hướng/grid và2vòngsoátmắt thiếu; không tạoảnh'},
 {'issue':'L090 registry / source scope','location':'source / frontmatter / checker output','change':'Giữ ID vànguồn cá nhânarchive độc lập; không causal/cùngtrend/raw-live gate mới; không đổi checker/metadata.','open':'Registry FAIL riêng/manual chưađóng; archival điều phối'},
 {'issue':'W12 / no new outline / storage','location':'word_count / MD / allpaths','change':'149từ,50sauhook; giữ b02–b07 actual text; ghi r11.3 ởworkspace theo phạmvi.','open':'Repoarchive/log/commit dođiềuphối; không sửa repo'}]
sp=B/'opencreator-clip05-spec-r11.3-draft-2026-11-07.json';sp.write_text(json.dumps(s,ensure_ascii=False,indent=2)+'\n')
