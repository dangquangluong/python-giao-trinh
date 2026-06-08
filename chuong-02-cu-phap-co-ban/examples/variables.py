# Ví dụ về biến và kiểu dữ liệu

# === BIẾN ===
ten = "Nguyễn Văn A"                        # Tạo biến ten, kiểu str (chuỗi ký tự)
tuoi = 25                                    # Tạo biến tuoi, kiểu int (số nguyên)
chieu_cao = 1.75                             # Tạo biến chieu_cao, kiểu float (số thực)
la_sinh_vien = True                          # Tạo biến boolean (True/False = Đúng/Sai)

print(f"Tên: {ten}")                         # f-string: chèn biến ten vào chuỗi để in
print(f"Tuổi: {tuoi} ({type(tuoi).__name__})")       # type() trả về kiểu dữ liệu, __name__ lấy tên kiểu
print(f"Cao: {chieu_cao}m ({type(chieu_cao).__name__})")  # In chiều cao kèm kiểu dữ liệu (float)
print(f"Sinh viên: {la_sinh_vien}")          # In giá trị boolean

# === LIST ===
print("\n=== LIST ===")                      # \n = xuống dòng trước khi in
diem = [85, 90, 78, 92, 88]                 # Tạo list (danh sách) chứa 5 số nguyên
print(f"Điểm: {diem}")                      # In toàn bộ list
print(f"TB: {sum(diem)/len(diem):.1f}")      # sum()=tổng, len()=số phần tử, :.1f=1 số thập phân
print(f"Max: {max(diem)}, Min: {min(diem)}") # max()=giá trị lớn nhất, min()=giá trị nhỏ nhất

diem.sort()                                  # .sort() sắp xếp list tăng dần (thay đổi list gốc)
print(f"Sắp xếp: {diem}")                   # In list sau khi sắp xếp

# === DICT ===
print("\n=== DICTIONARY ===")                # Dictionary = từ điển, lưu dữ liệu dạng key:value
sv = {"ten": "Trần B", "tuoi": 22, "diem": 8.5}  # Tạo dict với 3 cặp key:value
for k, v in sv.items():                      # .items() trả về từng cặp (key, value), for lặp qua
    print(f"  {k}: {v}")                     # In từng cặp key: value

# === STRING ===
print("\n=== STRING METHODS ===")            # Các phương thức (method) xử lý chuỗi
text = "  Python Là Tuyệt Vời  "            # Chuỗi có khoảng trắng đầu/cuối
print(f"strip: '{text.strip()}'")            # .strip() xóa khoảng trắng đầu và cuối
print(f"upper: '{text.upper()}'")            # .upper() chuyển thành CHỮ HOA
print(f"lower: '{text.lower()}'")            # .lower() chuyển thành chữ thường
print(f"split: {text.split()}")              # .split() tách chuỗi thành list theo khoảng trắng
print(f"replace: '{text.replace('Python', 'Rust')}'")  # .replace() thay thế chuỗi con

# === SLICING ===
print("\n=== SLICING ===")                   # Slicing = cắt lấy một phần chuỗi/list
s = "Python"                                 # Chuỗi 6 ký tự, index từ 0 đến 5
print(f"s[0]   = '{s[0]}'")                  # s[0] = ký tự đầu tiên (index 0) = 'P'
print(f"s[2:5] = '{s[2:5]}'")               # s[2:5] = từ index 2 đến 4 (không bao gồm 5) = 'tho'
print(f"s[::-1]= '{s[::-1]}'")              # s[::-1] = đảo ngược chuỗi = 'nohtyP'
