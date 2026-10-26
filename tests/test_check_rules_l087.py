import importlib.util, os, sys
R=os.path.dirname(os.path.dirname(os.path.abspath(__file__))); spec_=importlib.util.spec_from_file_location("cr", R+"/pipeline/scripts/check-rules.py"); cr=importlib.util.module_from_spec(spec_); sys.argv=["x"]; spec_.loader.exec_module(cr)
fails=0
def T(name, cond):
    global fails; print(("PASS " if cond else "FAIL ")+name); fails+= (not cond)
H=lambda t: [h for h,_ in cr.subject_hits(t)]
# phải bắt (L-087)
for t in ["Ví dụ mình ôn chương Di truyền {nhấn: ba tiếng liền} trước hôm thi giữa kỳ.",
          "Tới cuối kỳ gặp lại dạng lai hai cặp **tính trạng**, mình không nhớ cách giải.",
          "Mai thi môn Sinh rồi.", "Còn bạn, môn Toán còn mấy hôm?", "Mình học Hóa tới 2 giờ sáng.",
          "Cuốn sách Sử dày cộm.", "Ôn vật lý cả đêm.", "Bài văn nghị luận", "Đạo hàm với tích phân", "mai kiểm tra môn Anh"]:
    T(f"hit: {t} → {H(t)}", H(t))
# không được bắt (đời thường)
for t in ["Một nghiên cứu cho sinh viên đọc một bài hai lần liền.", "Còn bạn, môn sắp thi còn cách mấy hôm?",
          "Sinh hoạt buổi tối của bạn ra sao?", "Lý do là điện thoại.", "Tính toán tiền nhà mỗi tháng.",
          "Bài toán tiền điện tháng này.", "Học sinh lớp 12 hay thức khuya.", "Học sử dụng app ghi chú.",
          "Giờ anh về nhà.", "Đọc tin nhắn sếp lúc nửa đêm.", "Văn phòng mở cửa 8 giờ.", "Hóa đơn tiền điện tới rồi.",
          "Lịch sử giao dịch ngân hàng.", "Địa chỉ nhà bạn.", "Sinh nhật mẹ tuần sau.", "Học lý thuyết rồi làm thử.",
          "Ôn tiếng Anh mười phút mỗi sáng.", "Gấp sách lại tự kiểm tra."]:
    T(f"no hit: {t} → {H(t)}", not H(t))
print("FAILS", fails); sys.exit(1 if fails else 0)
