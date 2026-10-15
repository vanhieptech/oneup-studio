import glob,re,json,subprocess,numpy as np,difflib,sys
from faster_whisper import WhisperModel
m=WhisperModel("small",device="cpu",compute_type="int8")
ref={"b05":"no we don't do that","b06":"clip nữa thôi","b07":"thứ hai là khi nào xuất hiện cái việc rối như canh hẹ thì chúng ta phải kiếm việc khác làm liền dọn bàn tưới cây xếp lại dép","b08":"ủa bàn sạch bong rồi giờ né cái gì nữa ta","b09":"và cuối cùng là các bạn phải tự chửi mình cho thật đã đồ lười đồ vô dụng","b10":"ghét bản thân mình ghê mai làm nha thôi để thứ hai cho tròn tuần","b11":"nghe quen hông mà khoa học nói vầy nè ông steel gom hơn sáu trăm nghiên cứu thấy mình né việc vì nó khó chịu chứ không phải vì lười càng chửi mình thì càng né thêm","b12":"vậy thì chia nhỏ ra ba gạch hẹn mười phút thôi chuông reo là được nghỉ","b13":"hết đường né luôn á","b14":"bạn đang né việc gì comment một chữ thôi nha"}
alias=[("nâu","no"),("uy","we"),("đôn","don't"),("đu","do"),("đét","that"),("sờ tiu","steel"),("com men","comment"),("cô men","comment"),("clíp","clip"),("không","hông") ]
def n(s):
  s=re.sub(r"[^\w' ]"," ",s.lower())
  for a,b in alias: s=re.sub(r"\b%s\b"%a,b,s)
  return s.split()
res=json.load(open("stt2.json")) if len(sys.argv)>1 else {}
done={x[1] for v in res.values() for x in v}
for f in sorted(glob.glob("/workspace/v8/b[01]?-*.wav")):
  b=f.split("/")[-1][:3]
  if b not in ref or f in done: continue
  a=np.frombuffer(subprocess.run(["ffmpeg","-loglevel","error","-i",f,"-ac","1","-ar","16000","-f","s16le","-"],capture_output=True).stdout,dtype="int16").astype("float32")/32768
  t=" ".join(s.text for s in m.transcribe(a,language="vi",beam_size=5)[0])
  r=ref[b].replace("hông","hông").split(); sim=difflib.SequenceMatcher(None,n(t),[w if w!="không" else "hông" for w in r]).ratio()
  res.setdefault(b,[]).append((round(sim,3),f,t.strip())); print(b,round(sim,3),f[-10:],t,flush=True)
json.dump(res,open("stt2.json","w"),ensure_ascii=False,indent=1)
