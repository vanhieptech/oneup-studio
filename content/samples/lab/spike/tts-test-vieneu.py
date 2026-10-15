import time
from vieneu import Vieneu
v=Vieneu()
vs=v.list_preset_voices(); print(vs)
t=time.time(); a=v.infer("[cười] Ủa, lại 'mai học' nữa hả? Bạn nói câu đó tuần này ba lần rồi á nha.", voice=None if not vs else (vs[0] if isinstance(vs[0],str) else vs[0][0]))
v.save(a,"tts-test/o.wav"); print(len(a)/48000, time.time()-t)
