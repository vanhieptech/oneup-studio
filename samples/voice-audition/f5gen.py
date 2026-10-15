import sys,torch,soundfile as sf
torch.set_num_threads(4)
from f5_tts.api import F5TTS
from f5_tts.infer.utils_infer import preprocess_ref_audio_text
m=F5TTS(model="F5TTS_Base",ckpt_file="/workspace/f5-ckpt/model_last.pt",vocab_file="/workspace/f5-ckpt/vocab.txt",device="cpu")
REF="hôm nay trời sài gòn mát mẻ, mình ngồi cà phê một chút rồi về nhà làm việc tiếp nha."
M="thôi… mai học. mai học thiệt á! nếu chín giờ tối, thì mình mở sách năm phút. dễ hông?"
F="ủa? lại mai học nữa hả? ba lần rồi á nha! nè, thử vầy nè: nếu… thì… nghe giống code ghê á."
for v in sys.argv[1:]:
    txt=M if v in ["Đức Trí","Adam","Thái Sơn","Minh Triết"] else F
    w,sr,_=m.infer(ref_file=f"refs/{v}.wav",ref_text=REF,gen_text=txt,nfe_step=32,speed=1.0,seed=int(__import__("os").environ.get("SEED","7")),remove_silence=False)
    sf.write(f"work/f5-{v}.wav",w,sr); print("ok",v,len(w)/sr,flush=True)
