from vieneu import Vieneu
t=Vieneu()
REF="Hôm nay trời Sài Gòn mát mẻ, mình ngồi cà phê một chút rồi về nhà làm việc tiếp nha."
for v in ["Đức Trí","Adam","Thái Sơn","Minh Triết","Kim Thanh","Thục Đoan","Mỹ Duyên","Thùy Dung"]:
    a=t.infer(REF,voice=v,temperature=0.6); t.save(a,f"refs/{v}.wav")
