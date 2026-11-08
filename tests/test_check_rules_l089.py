# L-089 (Hiệp 27/10 02:37 «Xàm quá… đọc k thấy nó rời rạc à»): check-rules.py --flow — cờ liền mạch (chỉ ⚠)
import importlib.util, os, sys, subprocess, tempfile
R=os.path.dirname(os.path.dirname(os.path.abspath(__file__))); spec_=importlib.util.spec_from_file_location("cr", R+"/pipeline/scripts/check-rules.py"); cr=importlib.util.module_from_spec(spec_); sys.argv=["x"]; spec_.loader.exec_module(cr)
fails=0
def T(name, cond):
    global fails; print(("PASS " if cond else "FAIL ")+name); fails+= (not cond)
def run(md):
    cr.res.clear(); cr.check_flow_beats(cr.draft_beats(md), "t"); return list(cr.res)
def W(r, key): return [x for x in r if x[0]=="⚠" and key in x[2]]

# bản clip-05 v5 r4 (499376d) — Hiệp bác «rời rạc»
R4 = """1. **[Hook]** Hôm họp, bạn trình bày trơn tru. Hai hôm sau sếp hỏi lại một ý, bạn đứng hình. Sao ý đó trôi nhanh thế?
2. **[Ví dụ]** Thường thì tối trước buổi họp, mình dồn ba tiếng đọc chồng tài liệu hai lần liền.
3. **[Nguyên nhân]** Một nghiên cứu cũng thấy vậy. Người đọc hai lần liền kiểm tra ngay thì hơn người đọc một lần, nhưng hai ngày sau họ không còn hơn. Còn người đọc lần hai cách một tuần thì hai ngày sau vẫn hơn người đọc một lần.
4. **[Mục tiêu + cách làm]** Mình muốn nhớ lâu, mà càng muốn nhớ lâu thì các lần ôn càng nên cách xa nhau. Vậy mình giữ ba tiếng nhưng chia ra ba ngày, như cẩm nang gợi ý. Mỗi tối, mình úp tài liệu, tự nói lại ý chính rồi lật xem sót chỗ nào.
5. **[Kết quả]** Lần này sếp hỏi lại, mình dễ nhớ ra hơn. Mỗi ngày mình chỉ cần một buổi ngắn.
6. **[CTA]** Sắp tới bạn có buổi thuyết trình nào muốn ôn trong ba ngày không? Comment kể mình nghe nha.
"""
r=run(R4)
T("r4: ngôi kể đổi qua lại bạn→mình→bạn", W(r, "ngôi kể đổi qua lại"))
T("r4: khâu lặp «muốn nhớ lâu, mà càng muốn nhớ lâu»", any("muốn nhớ lâu" in x[2] for x in W(r, "khâu câu")))
cold = W(r, "beat mở không nối")
T("r4: b02/b04/b05 mở không nối", cold and all(b in cold[0][2] for b in ("b02", "b04", "b05")))
T("r4: b03 không bị cờ mở (có «cũng… vậy»)", cold and "b03" not in cold[0][2])
T("r4: b03 liệt kê «người đọc…»", W(r, "danh sách"))
T("r4: b05 câu +1 gắn thêm", W(r, "đứng trơ"))
T("r4: không có ✖ (chỉ cờ ⚠)", not any(x[0]=="✖" for x in r))

GOOD = """1. **[Hook]** Hôm họp, bạn trình bày trơn tru, hai hôm sau sếp hỏi lại một ý thì bạn đứng hình. Sao ý đó trôi nhanh vậy?
2. **[Ví dụ]** Có thể vì tối trước buổi họp, bạn dồn ba tiếng đọc chồng tài liệu hai lần liền.
3. **[Nguyên nhân]** Mà đọc liền như vậy thì chỉ giữ được lúc đó, Rawson với Kintsch cũng thấy hai ngày sau là hết hơn.
4. **[Cách làm]** Nên lần tới, bạn giữ ba tiếng đó nhưng chia ra ba ngày, mỗi tối úp tài liệu tự nói lại.
5. **[Kết quả]** Rồi hai hôm sau sếp hỏi lại, bạn nhớ ra ý đó dễ hơn.
6. **[CTA]** Sắp tới bạn có buổi họp nào muốn thử không?
"""
r=run(GOOD)
T("good: 0 cờ ⚠", not any(x[0]=="⚠" for x in r))
T("good: ngôi kể nhất quán", any(x[0]=="✔" and "nhất quán" in x[2] for x in r))

# đơn vị
T("person: «kể mình nghe» là tân ngữ, không tính ngôi kể", cr._l089_person("Bạn có buổi nào không? Comment kể mình nghe nha.") == "bạn")
T("conn: «Có thể vì…» có từ nối", cr._l089_starts_conn("Có thể vì tối trước buổi họp, bạn dồn."))
T("conn: «Thường thì…» không phải từ nối", not cr._l089_starts_conn("Thường thì tối trước buổi họp, mình dồn."))
T("conn: «Vậy nên…»", cr._l089_starts_conn("Vậy nên bạn chia ra ba ngày."))
T("càng…càng bình thường không bị coi là khâu lặp", not W(run("1. **[Hook]** Bạn bí? \n2. **[Ý]** Vì bạn càng muốn nhớ lâu thì càng nên giãn các lần ôn.\n3. **[CTA]** Bạn thử không?"), "khâu câu"))
T("parse: không đọc được beat → ✖", (cr.res.clear(), cr.check_flow_beats([], "t"), any(x[0]=="✖" for x in cr.res))[2])

# CLI --flow chạy được và chỉ cảnh báo (exit 0)
with tempfile.NamedTemporaryFile("w", suffix=".md", delete=False, encoding="utf8") as f: f.write(R4)
p = subprocess.run([sys.executable, R+"/pipeline/scripts/check-rules.py", "--flow", f.name], capture_output=True, text=True)
T("CLI --flow exit 0 + có ⚠ L-089", p.returncode == 0 and "⚠ L-089" in p.stdout); os.unlink(f.name)
print("FAILS", fails); sys.exit(1 if fails else 0)
