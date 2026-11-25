#!/usr/bin/env python3
"""Per-phrase F5 voice with {nhấn:} emphasis (L-036, clip-02 v17). Reusable for any clip spec.
  python3 pipeline/scripts/voice-phrase-f5.py gen    <spec.json> --work DIR            # write units + F5 batches (2 seeds/phrase)
  F5_THREADS=4 /workspace/f5-venv/bin/python pipeline/tts/f5tts_gen.py DIR/batch0.json   # (and batch1.json in parallel)
  /workspace/asr-venv/bin/python pipeline/scripts/voice-phrase-f5.py pick   <spec> --work DIR [unit keys…]  # STT pick + emphasis edits
  /workspace/asr-venv/bin/python pipeline/scripts/voice-phrase-f5.py stitch <spec> --work DIR --prefix v17 --listen out.mp3
Units: phrases split at '|' in spec `phrases[].t` (< 4 syllables merged). Emphasis: stem words +1 st +2 dB tempo .95; {nhấn:} words
tempo .78 +0.8 st +1.5 dB; stem line last word −1.5 st (fall). Hiệp-né role +2 st. Writes video-engine/public/voice/<prefix>-<line>.wav/.json
with emphasis_edits=true (check-rules L-016 exception) and final/voice-stt-<prefix>.json. Re-roll a failing unit: add seeds to a batch, re-run pick <key>.
Refs (DL-073, assets/voice-refs/voice-refs.json): spec without `voice_refs` -> thai-son for every line (old clips unchanged). With `voice_refs`
(true, or a dict overriding slots {"default","happy","serious"} with ref ids, plus optional {"lines": {<line key>: slot|ref id}}):
emotion happy/teasing -> happy; focused/neutral in a scene with part "evidence" -> serious; else default (thai-son-v2). A line may set `voice_ref`.
"""
import hashlib, json, re, os, sys, subprocess, unicodedata
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import paths as P
from tts import respell as RS
REPO = str(P.ROOT)
FFMPEG = P.FFMPEG_BIN
def final_tone(text):
    """Tone of the last Vietnamese syllable: huyen | nang | sac | hoi | nga | ngang (L-082)."""
    ws_ = re.findall(r"[\wÀ-ỹ]+", text or "")
    if not ws_: return "ngang"
    d = unicodedata.normalize("NFD", ws_[-1].lower())
    return "huyen" if "\u0300" in d else "nang" if "\u0323" in d else "sac" if "\u0301" in d else "hoi" if "\u0309" in d else "nga" if "\u0303" in d else "ngang"
L082_TONES = ("huyen", "nang")
def arg(k, d=None): return sys.argv[sys.argv.index(k) + 1] if k in sys.argv else d
CMD, SPEC = sys.argv[1], os.path.abspath(sys.argv[2]); W = os.path.abspath(arg("--work", str(P.VOICE_WORK_DIR))); os.makedirs(W, exist_ok=True)
PREFIX = arg("--prefix", "vp"); LISTEN = arg("--listen", os.path.join(W, "listen.mp3"))
ARGS = [a for i, a in enumerate(sys.argv[3:], 3) if not a.startswith("--") and not sys.argv[i - 1].startswith("--")]

VR = json.load(open(os.path.join(REPO, "assets/voice-refs/voice-refs.json")))
REF_SLOTS = {"default": "thai-son-v2", "happy": "thai-son-happy", "serious": "thai-son-serious"}
def pick_ref(S, sc, l, key):
    vr = S.get("voice_refs")
    if not vr: return "thai-son"
    slots = dict(REF_SLOTS); lines = {}
    if isinstance(vr, dict):
        slots.update({k: v for k, v in vr.items() if k in REF_SLOTS}); lines = vr.get("lines") or {}
    o = l.get("voice_ref") or lines.get(key)
    if o: r = slots.get(o, o)
    elif l.get("emotion") in ("happy", "teasing"): r = slots["happy"]
    elif l.get("emotion", "neutral") in ("focused", "neutral") and sc.get("part") == "evidence": r = slots["serious"]
    else: r = slots["default"]
    if r not in VR: sys.exit(f"voice_refs: unknown ref '{r}' for {key} (ids: {', '.join(k for k in VR if not k.startswith('_'))})")
    return r

def gen():
    import json,re
    S=json.load(open(SPEC))
    units=[]
    for sc in [s for part in S['parts'] for s in part.get('scenes',[])+part.get('sections',[])]:
      for li,l in enumerate(sc['lines']):
        key=sc['id']+('abcdef'[li] if len(sc['lines'])>1 else '')
        ref_id=pick_ref(S,sc,l,key)
        ph=[p['t'] for p in l['phrases']]; m=[]
        keep=[p.get('keep') for p in l['phrases']]
        for p in ph:  # merge <4 syllables into next (phrases flagged keep: one unit each, clip-04 v14b)
          if m and not any(keep) and len(re.sub(r"\{[^:]*: |\}","",m[-1]).split())<4: m[-1]=m[-1]+' '+p
          else: m.append(p)
        if len(m)>1 and not any(keep) and len(re.sub(r"\{[^:]*: |\}","",m[-1]).split())<3: x=m.pop(); m[-1]=m[-1]+' '+x
        for i,p in enumerate(m):
          emph=re.findall(r"\{nhấn: ([^}]*)\}",p)+[w for w in ("Thứ nhất","Thứ hai","cuối cùng") if w in p]; t=re.sub(r"\{nhấn: ([^}]*)\}",r"\1",p)
          units.append({"key":f"{key}-{i}","line":key,"ref":ref_id,"role":l['voice_role'],"t":t,"emph":emph,"last":i==len(m)-1,"stem":bool(re.match(r"(thì cái|thứ nhất|thứ hai|và cuối cùng)",l['text'].lower().replace('*','')))})
    json.dump(units,open(W+'/units.json','w'),ensure_ascii=False,indent=0)
    ref=REPO+"/assets/voice-refs/"+VR["thai-son"]["wav"];rt=VR["thai-son"]["ref_text"]
    ck_fp=P.ckpt_fingerprint()
    def _mk_item(u, sd):
      spd=float(S.get("voice_speed") or (arg("--speed","0.9") if u["role"]=="Thầy" else 0.95))
      ch=hashlib.sha256(json.dumps([u["t"],u["ref"],spd,sd,ck_fp],ensure_ascii=False).encode()).hexdigest()[:16]
      return {"t":u["t"],"ref":REPO+"/assets/voice-refs/"+VR[u["ref"]]["wav"],"ref_text":VR[u["ref"]]["ref_text"],"seed":sd,"speed":spd,"cache_hash":ch,"out":f"{W}/{u['key']}-{sd}.wav"}
    split=int(arg("--split","1"))
    if split<=1:
      it=[_mk_item(u,sd) for u in units for sd in (11,37)]
      json.dump({"ref":ref,"ref_text":rt,"items":it},open(f"{W}/batch.json","w"),ensure_ascii=False)
    else:
      for h in range(split):
        it=[_mk_item(u,sd) for n,u in enumerate(units) if n%split==h for sd in (11,37)]
        json.dump({"ref":ref,"ref_text":rt,"items":it},open(f"{W}/batch{h}.json","w"),ensure_ascii=False)
    print(len(units)); [print(u['key'],u['ref'],u['t'],u['emph']) for u in units]

def helpers():
    global m, pcm, stt, sim, n
    import json,re,subprocess,difflib,unicodedata,os,glob,numpy as np
    from faster_whisper import WhisperModel
    m=WhisperModel("small",device="cpu",compute_type=os.environ.get("ASR_COMPUTE","float32"))
    U=json.load(open(W+'/units.json')); OUT=REPO+"/video-engine/public/voice"; SR=48000; FPS=30
    AL=RS.STT_ALIASES
    LEAKS={}  # per ref: words of its ref_text (leading leaked words are cut from a take)
    def n(s):
      s=unicodedata.normalize("NFC",s.lower()); s=re.sub(r"[^\w ]"," ",s); s=" ".join(s.split())
      for a,b in AL: s=s.replace(a,b)
      return s.split()
    def tl(ws): return ["".join(c for c in unicodedata.normalize("NFD",w) if unicodedata.category(c)!="Mn").replace("đ","d") for w in ws]
    def sim(h,t): return round(0.5*difflib.SequenceMatcher(None,h,t).ratio()+0.5*difflib.SequenceMatcher(None,tl(h),tl(t)).ratio(),3)
    def pcm(f,sr=16000): return np.frombuffer(subprocess.run([FFMPEG,"-loglevel","error","-i",f,"-ac","1","-ar",str(sr),"-f","f32le","-"],capture_output=True,check=True).stdout,dtype="float32")
    def stt(a):
      best=None
      for pad in (8000,0):
        segs,_=m.transcribe(np.pad(a,pad),language="vi",beam_size=5,condition_on_previous_text=False,word_timestamps=True)
        ws=[(w.word.strip(),w.start-pad/16000,w.end-pad/16000) for s in segs for w in s.words]
        if best is None or len(ws)>len(best): best=ws
      return best
    def rb(x,tempo=1.0,semi=0.0,db=0.0):
      if len(x)<SR*0.05: return x
      af=f"rubberband=tempo={tempo}:pitch={2**(semi/12)}"+(f",volume={db}dB" if db else "")
      res=subprocess.run([FFMPEG,"-loglevel","error","-f","f32le","-ar",str(SR),"-ac","1","-i","-","-af",af,"-f","f32le","-"],input=x.astype("float32").tobytes(),capture_output=True)
      if res.returncode!=0 or not res.stdout:
        raise RuntimeError(f"ffmpeg rubberband failed ({FFMPEG}, rc={res.returncode}): {res.stderr.decode(errors='replace').strip()} — need ffmpeg-full with librubberband")
      return np.frombuffer(res.stdout,dtype="float32")
    def trim(x,thr=0.01):
      i=np.where(np.abs(x)>thr)[0]; return x[max(0,i[0]-int(.03*SR)):i[-1]+int(.06*SR)] if len(i) else x
    return dict(globals(), **locals())

if CMD == "gen": gen()
else:
    G = helpers(); globals().update(G)
    if CMD == "pick":
        res={}
        # emphasis words = **bold** of final/script-*-delivery.md when present (1 stressed chunk per sentence), else {nhấn:} of the spec
        import importlib.util as _iu
        _s=_iu.spec_from_file_location("pc",os.path.join(os.path.dirname(os.path.abspath(__file__)),"prosody-check.py")); PC=_iu.module_from_spec(_s); _s.loader.exec_module(PC)
        _fd=os.path.dirname(SPEC); _ds=PC.delivery_stream(_fd); EMPH={}
        if _ds:
          _bd=PC.delivery_bold(_fd); _pos=0; FWD=[(b,a) for a,b in PC.RESPELL]
          for _u in U:
            ow=re.findall(r"[\wÀ-ỹ]+",PC.unrespell(_u["t"])); fl=_bd[_pos:_pos+len(ow)]; _pos+=len(ow); runs=[]; cur=[]
            for w_,b_ in zip(ow,fl):
              if b_: cur.append(w_)
              elif cur: runs.append(cur); cur=[]
            if cur: runs.append(cur)
            ph=[]
            for r_ in runs:
              s_=" ".join(r_)
              for a,b in FWD: s_=re.sub(rf"\b{re.escape(a)}\b",b,s_)
              ph.append(s_)
            EMPH[_u["key"]]=ph
        EN_U={_u["key"]:re.sub(r"[^a-z]","",PC.unrespell(_u["t"]).lower()) for _u in U if PC.unrespell(_u["t"])!=_u["t"] and re.fullmatch(r"[A-Za-z ,.]+",PC.unrespell(_u["t"]))}
        ONLY=ARGS
        if ONLY: res=json.load(open(W+'/units-stt.json'))
        for u in U:
          if ONLY and u['key'] not in ONLY: continue
          # v14b (pacing-v14.md, Rule Reviewer): pick = STT sim − penalty if >5 syll/s + bonus if a question rises; emphasis = gain only (no tempo,
          # no word split), ≥2 dB over the rest of the unit; commas get a real 0.15–0.2s pause (inserted/trimmed at the low-energy point); questions: last syllable +2.5 st
          rid=u.get("ref","thai-son"); LEAK=LEAKS.get(rid) or LEAKS.setdefault(rid,set(n(VR[rid]["ref_text"]))); tgt=n(u["t"]); best=None; cands=[]; syl=max(1,len(tgt)); q=u["t"].rstrip().endswith("?")
          def voiced(a,t0,t1,sr=16000):
            h=int(.01*sr); fr=[float(np.sqrt(np.mean(a[j:j+h]**2))) for j in range(int(t0*sr),max(int(t0*sr),int(t1*sr)-h),h)]
            if not fr: return 0.3
            thr=max(0.01,0.06*sorted(fr)[int(len(fr)*.95)]); return max(0.3,sum(v>thr for v in fr)*.01)
          def f0(a,sr=16000):
            hop=int(.02*sr); win=int(.04*sr); o=[]
            for j in range(0,len(a)-win,hop):
              fr=a[j:j+win]-a[j:j+win].mean()
              if np.sqrt(np.mean(fr**2))<0.02: o.append(0); continue
              ac=np.correlate(fr,fr,"full")[win-1:]; lo,hi=int(sr/350),int(sr/70); k=lo+int(np.argmax(ac[lo:hi])); o.append(sr/k if ac[k]>0.3*ac[0] else 0)
            return np.array(o)
          def rise_st(a,wl):
            if not wl: return 0.0
            F=f0(a); t0=wl[-1][1]; p=F[:int(t0/.02)]; s=F[int(t0/.02):]; p,s=p[p>0],s[s>0]
            return float(12*np.log2(np.median(s)/np.median(p))) if len(p) and len(s) else 0.0
          for f in sorted(glob.glob(f"{W}/{u['key']}-[0-9]*.wav")):
            a16=pcm(f); ws=stt(a16); i=0; cut=0
            while i<len(ws) and n(ws[i][0]) and n(ws[i][0])[0] in LEAK and (not tgt or n(ws[i][0])[0]!=tgt[0]) and ws[i][2]<1.5: cut=ws[i][2]+0.03; i+=1
            w2=ws[i:]; sc=sim(n(" ".join(w[0] for w in w2)),tgt)
            if EN_U.get(u["key"]):  # respelled English word (b03b): Vietnamese STT cannot spell it -> also score an English transcript against the real word
              segs_,_=m.transcribe(np.pad(a16,8000),language="en",beam_size=5,condition_on_previous_text=False)
              he=re.sub(r"[^a-z]","","".join(s_.text for s_ in segs_).lower()); sc=max(sc,round(difflib.SequenceMatcher(None,he,EN_U[u["key"]]).ratio(),3))
            rate=syl/voiced(a16,w2[0][1],w2[-1][2]) if w2 else 9.0
            rs=rise_st(a16,w2) if q else 0.0
            # L-074: no >5 syll/s penalty (natural Vietnamese conversational speed is 5.0-6.5 syll/s)
            score=sc+(0.05 if q and rs>0 else 0)
            cands.append((os.path.basename(f),round(sc,3),round(rate,2),round(rs,2)))
            if best is None or score>best[0]: best=(score,f,cut,w2,sc,rate,rs)
          score,f,cut,ws,sc,rate,rs=best; x=pcm(f,SR); x=x[int(cut*SR):]
          ws=[(w,max(0,a-cut),max(0,b-cut)) for w,a,b in ws]
          flat=[(tok,wi) for wi,w in enumerate(ws) for tok in n(w[0])]
          smm=difflib.SequenceMatcher(None,tl([t for t,_ in flat]),tl(tgt),autojunk=False); tmap={}
          for a_,b_,k_ in smm.get_matching_blocks():
            for d in range(k_): tmap[b_+d]=flat[a_+d][1]
          span0=ws[0][1] if ws else 0; span1=ws[-1][2] if ws else len(x)/SR
          def ttime(k,end):  # time of target token k (aligned word, else proportional)
            if k in tmap: return ws[tmap[k]][2 if end else 1]
            return span0+(span1-span0)*((k+(1 if end else 0))/len(tgt))
          def db(seg): return 20*np.log10(max(1e-5,float(np.sqrt(np.mean(seg**2))))) if len(seg) else -100
          def gain(y,a,b,g,xf=int(.02*SR)):
            m=np.ones(len(y),'float32'); k=10**(g/20); a=max(0,a); b=min(len(y),b); m[a:b]=k
            r0=max(0,a-xf); m[r0:a]=np.linspace(1,k,a-r0); r1=min(len(y),b+xf); m[b:r1]=np.linspace(k,1,r1-b); return y*m
          emph_db=[]
          for e in EMPH.get(u["key"],u["emph"]):
            en=n(e); j=next((jj for jj in range(len(tgt)) if tl(tgt[jj:jj+len(en)])==tl(en)),None)
            if j is None: continue
            if len(en)>=0.75*len(tgt):  # the whole unit is the stressed chunk: no in-unit "rest" to beat; prosody-check voice() lifts the unit +3 dB vs its sentence
              emph_db.append((e,"unit",3.0)); continue
            a,b=int(ttime(j,False)*SR),int(ttime(j+len(en)-1,True)*SR)
            last_tok=len(tgt)-1; ra=int(ttime(last_tok,False)*SR) if j+len(en)-1<last_tok else len(x)  # rest excludes the sentence-final syllable
            rest=np.concatenate([x[:a],x[b:ra]]) if (a>0 or ra>b) else x
            if b<=a or not len(rest): continue
            have=db(x[a:b])-db(rest); g=float(min(7.0,max(3.0,2.5-have))); x=gain(x,a,b,g)
            emph_db.append((e,round(have,1),round(db(x[a:b])-db(np.concatenate([x[:a],x[b:ra]]) if (a>0 or ra>b) else x),1)))
          out=[]; pos=0; tail=x
          if u["last"] and u["stem"] and len(ws)>0:  # sentence-end fall on the last word (no tempo change)
            lw=int(ws[-1][1]*SR)
            if 0<lw<len(tail): out.append(tail[:lw]); tail=rb(tail[lw:],tempo=1.0,semi=-1.5)
          elif q and len(ws)>0 and final_tone(u["t"]) not in L082_TONES:  # L-082: never lift huyền/nặng ending questions
            lw=int(ttime(len(tgt)-1,False)*SR); semi=float(min(5.0,max(2.5,1.0-rs)))
            if 0<lw<len(tail): out.append(tail[:lw]); tail=rb(tail[lw:],tempo=1.0,semi=semi)
          out.append(tail); x=np.concatenate(out)
          # comma / colon pauses inside the unit: real 0.15–0.2s (':' 0.25s), never longer than a sentence pause
          edits=[]; h=int(.01*SR); toks_=re.findall(r"[\wÀ-ỹ]+|[,:]",u["t"]); kk=-1; cms=[]
          for tk in toks_:
            if tk in ",:": cms.append((kk,tk))
            else: kk+=1
          for k,p_ in cms:
            if k<0 or k>=len(tgt)-1: continue
            e0=ttime(k,True); s1=ttime(k+1,False); m0=(ttime(k,False)+e0)/2; m1=(s1+ttime(k+1,True))/2
            A=int(max(0,m0)*SR); B=int(min(len(x)/SR,m1)*SR)
            en_=np.array([np.sqrt(np.mean(x[j:j+h]**2)) for j in range(A,max(A,B-h),h)])
            if not len(en_): continue
            thr=max(0.008,0.06*float(np.percentile(np.abs(x),99.5))); sil=en_<thr
            best_run=(0,0); cur=0
            for j,v in enumerate(sil):
              cur=cur+1 if v else 0
              if cur>best_run[0]: best_run=(cur,j)
            have=best_run[0]*.01; want=0.25 if p_==":" else 0.18
            if have<0.15:
              at=A+int(np.argmin(en_))*h+h//2 if best_run[0]==0 else A+(best_run[1]-best_run[0]//2)*h
              edits.append(("ins",at,int((want-have)*SR)))
            elif have>0.22:
              c=A+(best_run[1]-best_run[0]//2)*h; r=int((have-want)*SR); edits.append(("del",c-r//2,r))
          for kind,at,ln in sorted(edits,key=lambda z:-z[1]):
            x=np.concatenate([x[:at],np.zeros(ln,'float32'),x[at:]]) if kind=="ins" else np.concatenate([x[:at],x[at+ln:]])
          y=trim(x)
          if u["role"]=="Hiệp-né": y=rb(y,semi=2.0)
          np.save(f"{W}/{u['key']}.npy",y)
          res[u["key"]]={"sim":sc,"take":os.path.basename(f),"stt":" ".join(w[0] for w in ws),"emph_found":len(emph_db),"emph_want":len(EMPH.get(u["key"],u["emph"])),
                         "emph_db_before_after":emph_db,"unit_gain_db":3.0 if any(z[1]=="unit" for z in emph_db) else 0.0,"syll_per_s":round(rate,2),"question_rise_st":round(rs,2) if q else None,"comma_edits":[(k_,round(l_/SR,2)) for k_,_,l_ in edits],"candidates":cands}
          print(u["key"],cands,"->",sc,os.path.basename(f),"rate",round(rate,2),"rise",round(rs,2) if q else "-","emph",emph_db,"commas",[(k_,round(l_/SR,2)) for k_,_,l_ in edits]," ".join(w[0] for w in ws),flush=True)
        json.dump(res,open(W+"/units-stt.json","w"),ensure_ascii=False,indent=1)
    elif CMD == "stitch":
        U=json.load(open(W+'/units.json')); SR=48000
        COMMA_GAP=float(json.load(open(SPEC)).get('comma_gap',0.18))
        LINE_TEMPO={k:float(v) for k,v in (json.load(open(SPEC)).get('line_tempo') or {}).items()}
        COMMA_GAP_LINE={k:float(v) for k,v in (json.load(open(SPEC)).get('comma_gap_line') or {}).items()}
        def gap(t,stemfirst,nxt=None):  # prosody-plan (b): comma .15-.25, period .35-.5, +0.08 before a stressed unit
          t=t.strip()
          if stemfirst: return 0.25
          # delivery rev3 (pacing-v14.md root fix): comma 0.18 < colon 0.25 < sentence 0.35; '///' before «Bút dừng» 0.4; voice-only uses prosody-check.py voice
          g=0.35 if t[-1:] in '.?!…' else 0.25 if t[-1:]==':' else COMMA_GAP if t[-1:]==',' else 0.0
          return 0.4 if nxt and nxt["t"].startswith("Bút dừng") else g
        def env(x):
          hop=SR/FPS; e=[float(np.sqrt(np.mean(x[int(i*hop):int((i+1)*hop)]**2))) if len(x[int(i*hop):int((i+1)*hop)]) else 0 for i in range(int(len(x)/hop)+1)]
          pk=sorted(e)[int(len(e)*0.95)]; return [round(min(1,v/max(pk,1e-4)),3) for v in e]
        lines={}; order=[]
        for u in U:
          if u["line"] not in lines: lines[u["line"]]=[]; order.append(u["line"])
          lines[u["line"]].append(u)
        stt_u=json.load(open(W+'/units-stt.json')); rep={}; full=[]; prev_scene=None
        for ln in order:
          segs=[np.zeros(int(.06*SR),'float32')]
          for i,u in enumerate(lines[ln]):
            _x=np.load(f"{W}/{u['key']}.npy").astype('float32'); _lt=LINE_TEMPO.get(ln,1.0)
            segs.append(rb(_x,tempo=_lt) if _lt!=1.0 else _x)  # spec line_tempo: slow a too-fast line (L-070), pitch kept
            if i<len(lines[ln])-1: segs.append(np.zeros(int((COMMA_GAP_LINE[ln] if ln in COMMA_GAP_LINE and u["t"].strip()[-1:]=="," else gap(u["t"],u["stem"] and i==0,lines[ln][i+1]))*SR),'float32'))  # spec comma_gap_line
          segs.append(np.zeros(int(.1*SR),'float32')); y=np.concatenate(segs); y=y/max(1e-4,np.abs(y).max())*0.89
          dst=f"{OUT}/{PREFIX}-{ln}"
          subprocess.run([FFMPEG,"-y","-loglevel","error","-f","f32le","-ar",str(SR),"-ac","1","-i","-",dst+".wav"],input=y.tobytes(),check=True)
          say=" ".join(u["t"] for u in lines[ln]); ws=stt(pcm(dst+".wav")); hyp=" ".join(w[0] for w in ws); sc=sim(n(hyp),n(say))
          rep[ln]={"line_sim":sc,"units":{u["key"]:stt_u[u["key"]]["sim"] for u in lines[ln]},"stt":hyp,"dur":round(len(y)/SR,2)}
          json.dump({"duration":round(len(y)/SR,3),"envelope":env(y),"engine":"F5-TTS hynt ViVoice "+"+".join(sorted({u.get("ref","thai-son") for u in lines[ln]}))+", per-phrase F5 (L-036, voice-phrase-f5.py), {nhấn:} rubberband stretch/pitch, stem end fall"+(", +2 semi" if lines[ln][0]["role"]=="Hiệp-né" else ""),
            "role":lines[ln][0]["role"],"stt":hyp,"stt_sim":sc,"intra_output_cuts":0,"emphasis_edits":True,"units":[{"text":u["t"],"take":stt_u[u["key"]]["take"],"sim":stt_u[u["key"]]["sim"]} for u in lines[ln]]},open(dst+".json","w"),ensure_ascii=False)
          scene=ln.rstrip('abcdef') if ln not in ('b01b',) else ln
          if full: full.append(np.zeros(int((0.12 if ln in ('b01b','b02') else 0.3 if scene==prev_scene else 0.42)*SR),'float32'))
          full.append(y); prev_scene=scene; print(ln,sc,rep[ln]["dur"],hyp,flush=True)
        z=np.concatenate(full)
        raw_l=os.path.join(W,"_listen_raw.wav")
        subprocess.run([FFMPEG,"-y","-loglevel","error","-f","f32le","-ar",str(SR),"-ac","1","-i","-",raw_l],input=z.tobytes(),check=True)
        err_l=subprocess.run([FFMPEG,"-hide_banner","-i",raw_l,"-af","ebur128","-f","null","-"],capture_output=True,text=True).stderr
        ms_l=re.findall(r"I:\s+(-?[\d.]+)\s+LUFS",err_l); g_l=-16.0-float(ms_l[-1]) if ms_l else 0.0
        subprocess.run([FFMPEG,"-y","-loglevel","error","-i",raw_l,"-af",f"volume={g_l:.2f}dB,alimiter=limit=0.84:attack=1:release=30:level=disabled","-c:a","libmp3lame","-b:a","160k",LISTEN],check=True)
        os.remove(raw_l)
        json.dump(rep,open(os.path.join(os.path.dirname(SPEC),f'voice-stt-{PREFIX}.json'),'w'),ensure_ascii=False,indent=1)
        print("total",round(len(z)/SR,2))
