import json,glob,os,sys,re,numpy as np,importlib.util
sys.argv=[sys.argv[0]]
s=importlib.util.spec_from_file_location('v','/workspace/oneup-studio/pipeline/scripts/voice-prosody.py');V=importlib.util.module_from_spec(s);s.loader.exec_module(V)
import librosa
D='/workspace/hi-oneup/natural-lab'
res={}
for ch in ['hiep','omi']:
    b=json.load(open(f'{D}/{ch}.json'))
    items=[i for i in b['items'] if os.path.exists(i['out'])]
    W=V.stt_words([i['out'] for i in items])
    for it in items:
        x,sr=V.read(it['out']); y,_,_=V._trim_unit(x,sr); ws=W[it['out']]; hyp=' '.join(w for w,_,_ in ws)
        r={'t':it['t'],'stt':hyp,'dur':round(len(y)/sr,2)}
        if it['kind']=='particle':
            p=it['p']; last=ws[-1] if ws else None
            heard=bool(last) and V.tl(' '.join(V.norm(last[0])))[:2]==V.tl(p)[:2]
            fdur=(len(y)/sr-(last[1]-_)) if False else ((ws[-1][2]-ws[-1][1]) if ws else 0)
            # F0 contour last 350 ms: slope in semitones
            yy=librosa.resample(y,orig_sr=sr,target_sr=16000)[-5600:]
            f0,vf,_p=librosa.pyin(yy,fmin=60,fmax=450,sr=16000,frame_length=1024); f=f0[vf&~np.isnan(f0)]
            slope=float(12*np.log2(np.mean(f[-4:])/np.mean(f[:4]))) if len(f)>=8 else 0.0
            sim=V.sim(hyp,it['t'],toneless=True)
            q=it['t'].rstrip()[-1]
            want = slope>0.5 if q=='?' else True
            score=sim+(0.4 if heard else -0.6)+min(fdur,0.6)*0.8+(0.3 if want else -0.3)-(0.6 if fdur>0.9 else 0)
            r.update(kind='particle',p=p,v=it['v'],heard=heard,final_dur=round(fdur,2),slope_st=round(slope,2),sim=round(sim,2),score=round(score,3))
        else:
            ok=0.25<=r['dur']<=1.4
            r.update(kind='filler',p=it['p'],v=it['v'],ok=ok)
        res.setdefault(ch,[]).append(r)
json.dump(res,open(f'{D}/analysis.json','w'),ensure_ascii=False,indent=1)
# particle table
tab={}
for ch,rs in res.items():
    tab[ch]={}
    for p in sorted({r['p'] for r in rs if r['kind']=='particle'}):
        c=sorted([r for r in rs if r['kind']=='particle' and r['p']==p],key=lambda r:-r['score']); best=c[0]
        word=re.findall(r'(\S+?)[!?.]+$',best['t'])[0] if re.findall(r'(\S+?)[!?.]+$',best['t']) else p
        long_=[r for r in c if r['v']==1][0]
        tab[ch][p]={'auto':word if best['v']!=2 else p,'auto_mark_extra':best['t'][-2:] if best['v']==2 else '', 'long':re.findall(r'(\S+?)[!?.]+$',long_['t'])[0],
                    'tested':[{k:r[k] for k in ('t','stt','final_dur','slope_st','heard','score')} for r in c]}
json.dump(tab,open('/workspace/oneup-studio/pipeline/tts/particle-styles.json','w'),ensure_ascii=False,indent=1)
for ch in tab:
    print(ch,{p:(v['auto'],v['tested'][0]['score'],v['tested'][0]['final_dur'],v['tested'][0]['slope_st']) for p,v in tab[ch].items()})
for ch,rs in res.items(): print(ch,'fillers',[(r['p'],r['v'],r['dur'],r['stt']) for r in rs if r['kind']=='filler'])
