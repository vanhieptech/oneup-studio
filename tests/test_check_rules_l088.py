import importlib.util, os, sys
R=os.path.dirname(os.path.dirname(os.path.abspath(__file__))); spec_=importlib.util.spec_from_file_location("cr", R+"/pipeline/scripts/check-rules.py"); cr=importlib.util.module_from_spec(spec_); sys.argv=["x"]; spec_.loader.exec_module(cr)
import re
fails=0
def T(name, cond):
    global fails; print(("PASS " if cond else "FAIL ")+name); fails+= (not cond)
# (a) nguồn truy được
for t in ["Steel 2007 Psych Bull", "Yang et al. (2021) gộp 222 nghiên cứu", "Rawson & Kintsch 2005", "Yang và cộng sự (2021)", "PMID 16719566",
          "Gollwitzer & Sheeran 2006", "https://doi.org/10.1037/0033-2909.132.3.354"]:
    T(f"cite: {t} → {cr.citations(t)}", cr.citations(t))
for t in ["Hiệp 2026-10-26 21:44", "TikTok 2026", "CC BY 4.0", "đăng 29/07/2025, dài 20s", "October 2025", "@ng__phanh · TikTok", "clip-05 v4 (8ec205e)",
          "Rule Reviewer 21/10", "1.1M view (đo 20/10/2026)", "Gen Z 2024"]:
    T(f"no cite: {t} → {cr.citations(t)}", not cr.citations(t))
# lời đọc có dẫn chứng / kiểu chèn trích dẫn
def run(fn, *a):
    cr.res.clear(); fn(*a); return list(cr.res)
r=run(cr._l088_evidence, ["Rawson & Kintsch 2005"], "Sáng mai mình đọc lại bản báo cáo.", 6, "x")
T("clip-06 no spoken evidence → ✖", any(x[0]=="✖" and "không nhắc dẫn chứng" in x[2] for x in r))
r=run(cr._l088_evidence, ["Rawson & Kintsch 2005"], "Sáng mai mình đọc lại bản báo cáo.", 5, "x")
T("clip-05 no spoken evidence → ⚠ only", any(x[0]=="⚠" and "không nhắc dẫn chứng" in x[2] for x in r) and not any(x[0]=="✖" for x in r))
r=run(cr._l088_evidence, [], "Một nghiên cứu cho sinh viên đọc một bài.", 6, "x")
T("no citation → ✖", any(x[0]=="✖" and "không có nguồn" in x[2] for x in r))
r=run(cr._l088_evidence, ["Rawson & Kintsch 2005"], "Hồi đó Rawson với Kintsch cũng cho người ta đọc bài hai lần liền y chang mình.", 6, "x")
T("surname spoken, woven → ✔, no dry warn", not any(x[0] in "✖⚠" for x in r))
for t in ["Một nghiên cứu cho sinh viên đọc một bài hai lần.", "Theo nghiên cứu thì ngủ đủ giúp nhớ.", "Khi gom 317 thí nghiệm lại, các nhà nghiên cứu thấy…",
          "Chuyện này có nghiên cứu hẳn hoi.", "Nghiên cứu cho thấy ngủ trưa tốt."]:
    T(f"dry: {t}", re.search(cr.L088_DRY, t, re.I))
for t in ["Yang gộp 222 nghiên cứu.", "Mình đem báo cáo nghiên cứu lại từ đầu.", "Rawson với Kintsch cho người ta đọc một bài hai lần liền."]:
    T(f"not dry: {t}", not re.search(cr.L088_DRY, t, re.I))
# (b) hook/CTA rập khuôn — hiệu chỉnh trên hook/CTA thật clip 02–05
c04h="Học thuộc tối qua, sáng dậy **quên sạch**? Giả sử bây giờ **không nhìn sách**, bạn còn nhớ được những gì?"
c05h="Bạn học dồn **một đêm** cho cả kỳ, sáng ra vẫn làm được đề. Một tuần sau, bạn còn nhớ **bao nhiêu**?"
c03h="Có việc gì bạn hứa **cuối tuần** làm… …mà để **cả năm** rồi chưa đụng tới không?"
T("clip-05 hook ≠ clip-04/03 hook", not cr.similar_to(c05h, [("c04", c04h), ("c03", c03h)]))
T("v5 reuses v4 hook question → hit", cr.similar_to("Bạn đọc dồn bản báo cáo cả tối, sáng ra vẫn thuyết trình trôi chảy. Một tuần sau, bạn còn nhớ bao nhiêu?", [("c05", c05h)]))
T("same opening 6 words → hit", cr.similar_to("Bạn học dồn một đêm cho buổi họp, sáng ra trình bày ổn.", [("c05", c05h)]))
T("fresh hook → no hit", not cr.similar_to("Slide cuối còn trống mà 8 giờ sáng phải họp rồi.", [("c04", c04h), ("c05", c05h), ("c03", c03h)]))
c04c="Còn bạn, thử gấp sách lại thì viết được **mấy từ**? Comment **con số** nha."
c05c="Còn bạn, môn sắp thi còn cách **mấy hôm**? Comment **số hôm** nha."
T("CTA «Comment số hôm nha» ≈ «Comment con số nha» → hit", cr.similar_to(c05c, [("c04", c04c)]))
T("fresh CTA → no hit", not cr.similar_to("Lần gần nhất sếp hỏi lại mà bạn quên là chuyện gì? Kể mình nghe dưới comment.", [("c04", c04c), ("c05", c05c)]))
T("opener «Còn bạn» 3rd time → hit", cr.opener_reuse("Còn bạn, buổi họp tới còn mấy hôm?", [("c04", c04c), ("c05", c05c)]))
T("opener once before → no hit", not cr.opener_reuse("Còn bạn, buổi họp tới còn mấy hôm?", [("c04", c04c)]))
# draft parser
md="""---\ntitle: x\n---\n1. **[Hook, nỗi đau]** Câu hook. Câu hỏi?\n2. **[Ví dụ]** Mình đọc báo cáo.\n5. **[Cách làm]** Nên mình làm thế này.\n   - **Một.** Mình chia ba ngày.\n8. **[CTA]** Kể mình nghe nha.\n\n**End card:** Nguồn: Steel 2007\n## Bảng\n| b01 | x |"""
h,c,sp=cr.draft_parts(md)
T(f"draft hook/cta parsed ({h!r}, {c!r})", h=="Câu hook. Câu hỏi?" and c=="Kể mình nghe nha.")
T("draft spoken includes sub-bullet, excludes end card", "Mình chia ba ngày." in sp and "Steel" not in sp)
# (1)(2) Hiệp 21:47 qua News: file trend Social Research có link + file ràng buộc/kiểm fact Deep Research
import tempfile
d=tempfile.mkdtemp(); cd=os.path.join(d, "clip-99-test"); os.makedirs(os.path.join(cd, "final"))
r=run(cr._l088_trend, cd); T("clip-99 no trend file → ✖", any(x[0]=="✖" and "chưa có file trend" in x[2] for x in r))
open(os.path.join(cd, "final", "trend-signals.md"), "w").write("Trend trong clip: b01 · format\n")
r=run(cr._l088_trend, cd); T("trend file without link → ✖", any(x[0]=="✖" and "không có link" in x[2] for x in r))
open(os.path.join(cd, "final", "trend-signals.md"), "a").write("- https://www.tiktok.com/@x/video/1\n")
r=run(cr._l088_trend, cd); T("trend file with link → ✔", r and all(x[0]=="✔" for x in r))
r=run(cr._l088_facts, cd); T("clip-99 no DR fact file → ✖", any(x[0]=="✖" for x in r))
open(os.path.join(cd, "fact-package-v1.md"), "w").write("# Deep Research\n")
r=run(cr._l088_facts, cd); T("DR fact-package present → ✔", r and all(x[0]=="✔" for x in r))
cd5=os.path.join(d, "clip-05-test"); os.makedirs(cd5)
r=run(cr._l088_facts, cd5); T("clip ≤05 missing DR file → ⚠ only", any(x[0]=="⚠" for x in r) and not any(x[0]=="✖" for x in r))
T("stray ')' stripped: «Steel 2007)»", cr.citations("(Steel 2007 Psych Bull), Steel 2007)") == ["Steel 2007", "Steel 2007"])
print("FAILS", fails); sys.exit(1 if fails else 0)
