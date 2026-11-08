import json,numpy as np
R=json.load(open("analysis.json"))
EMPH={"b01a":["quên","sạch"],"b01b":["Không","nhìn","sách,"],"b02b":["thuộc","làu."],"b03c":["Bút","dừng."],"b04a":["quen","mắt?"],"b04b":["Giấy","trắng"],
"b05a":["mở","sách."],"b05b":["lắc","ghịt."],"b06a":["hai","trăm","hai","mươi","hai","nghiên","cứu."],"b07b":["nhóm","cao","nhất."],"b08a":["ba","chồng."],"b09b":["Viết","trước."],"b09c":["lắc","ghịt."],"b10a":["Lắc","ghịt"]}
print("== long runs (>=0.25) mapping")
for r in R:
  for st,d,jb in r['long_runs']:
    b=r['bnd'][jb]; print(r['key'],f"{r['t']+st:.2f}s",d,"after",b['after'],repr(b['punct']))
print("== inter-line gaps")
for a,b in zip(R,R[1:]):
  g=(b['t']+b['speech'][0])-(a['t']+a['speech'][1]); same=a['key'][:3]==b['key'][:3]
  print(f"{a['key']}->{b['key']} {g:.2f}s {'same-beat' if same else 'NEW-BEAT'} end={a['say'][-1]} at {a['t']+a['speech'][1]:.2f}")
print("== emphasis")
import math
def st(x,ref): return 12*math.log2(x/ref) if x and ref else None
for k,ws in EMPH.items():
  r=[x for x in R if x['key']==k][0]; F=r['feat']; n=len(F)
  # find sequence of emph syllables
  sy=[f['syl'] for f in F]; core=[w.strip(',.?:') for w in ws]
  idx=None
  for i in range(n-len(core)+1):
    if [s.lower() for s in sy[i:i+len(core)]]==[c.lower() for c in core]: idx=list(range(i,i+len(core))); break
  oth=[i for i in range(n) if i not in idx]
  # exclude sentence-final syllables (before . ? !) among others to avoid final lengthening bias
  punct={b['j']:b['punct'] for b in r['bnd']}; fin=[i for i in oth if punct.get(i,'') in ('.','?')] + ([n-1] if n-1 in oth else [])
  oth2=[i for i in oth if i not in fin] or oth
  E=lambda ids,key:[F[i][key] for i in ids if F[i][key] is not None and not (isinstance(F[i][key],float) and math.isnan(F[i][key]))]
  edb=np.mean(E(idx,'db')); odb=np.mean(E(oth2,'db')); edu=np.mean(E(idx,'vdur')); odu=np.mean(E(oth2,'vdur'))
  ef=np.median(E(idx,'f0')) if E(idx,'f0') else None; of=np.median(E(oth2,'f0')) if E(oth2,'f0') else None
  emph_final = (n-1) in idx
  print(f"{k} {' '.join(ws)} t={r['t']+F[idx[0]]['dur']*0+ (0):.2f} dB {edb-odb:+.1f} dur x{edu/odu:.2f} F0 {st(ef,of) if ef and of else float('nan'):+.1f}st final={emph_final} match={r['matched']}/{r['n']}")
print("== questions / sentence ends F0")
for r in R:
  F=r['feat']; last=F[-1]; med=r['f0_med']
  prev=[f['f0'] for f in F[:-1] if f['f0']]
  print(r['key'],r['say'][-1],'last',last['syl'],'head',last['f0_head'],'tail',last['f0_tail'],'linemed',med,
    'tail-vs-med %+.1fst'%(12*np.log2(last['f0_tail']/med)) if last['f0_tail'] and med else '', 'slope %+.1fst'%(12*np.log2(last['f0_tail']/last['f0_head'])) if last['f0_tail'] and last['f0_head'] else '')
