# Chương 6: File I/O & Exception Handling

## 6.1 Đọc File

```python
# Cách 1: open + close
f = open("file.txt", "r", encoding="utf-8")  # open() mở file, "r"=read, encoding cho tiếng Việt
noi_dung = f.read()                           # .read() đọc toàn bộ nội dung thành chuỗi
f.close()                                     # .close() đóng file (PHẢI đóng sau khi dùng)

# Cách 2: with (khuyến nghị - tự đóng file)
with open("file.txt", "r", encoding="utf-8") as f:  # with tự động đóng file khi ra khỏi block
    noi_dung = f.read()       # Đọc toàn bộ file thành 1 chuỗi
    # hoặc
    dong = f.readline()        # Đọc 1 dòng (con trỏ dịch xuống)
    # hoặc
    tat_ca = f.readlines()     # Đọc tất cả dòng thành list ["dòng 1\n", "dòng 2\n", ...]

# Đọc từng dòng (tiết kiệm RAM cho file lớn)
with open("file.txt") as f:                   # Không cần "r" vì mặc định là read
    for dong in f:                            # File object là iterable, lặp qua từng dòng
        print(dong.strip())                   # .strip() xóa \n cuối dòng
```

## 6.2 Ghi File

```python
# Ghi đè (w) - xóa nội dung cũ
with open("output.txt", "w", encoding="utf-8") as f:  # "w"=write, tạo file mới hoặc ghi đè
    f.write("Dòng 1\n")                      # .write() ghi chuỗi vào file
    f.write("Dòng 2\n")                      # \n = ký tự xuống dòng

# Nối thêm (a) - giữ nội dung cũ
with open("output.txt", "a") as f:            # "a"=append, thêm vào cuối file
    f.write("Dòng thêm\n")                   # Nối thêm dòng mới

# writelines - ghi list chuỗi
lines = ["A\n", "B\n", "C\n"]                # List các chuỗi (cần tự thêm \n)
with open("output.txt", "w") as f:
    f.writelines(lines)                       # Ghi tất cả chuỗi trong list vào file
```

## 6.3 Làm Việc Với CSV

```python
import csv                                    # Module xử lý file CSV có sẵn trong Python

# Đọc CSV
with open("data.csv", "r") as f:             # Mở file CSV
    reader = csv.reader(f)                   # Tạo reader, mỗi dòng thành list
    header = next(reader)                    # next() lấy dòng đầu tiên (header)
    for row in reader:                       # Lặp qua các dòng còn lại
        print(row)                           # row là list: ["value1", "value2", ...]

# Đọc CSV thành dict
with open("data.csv", "r") as f:
    reader = csv.DictReader(f)               # DictReader: mỗi dòng thành dict {header: value}
    for row in reader:                       # Lặp qua từng dict
        print(row["ten"], row["diem"])       # Truy cập value bằng tên cột

# Ghi CSV
data = [["ten", "tuoi", "diem"], ["A", 20, 8.5], ["B", 21, 7.0]]  # List 2 chiều
with open("output.csv", "w", newline="") as f:  # newline="" tránh dòng trống thừa trên Windows
    writer = csv.writer(f)                   # Tạo writer
    writer.writerows(data)                   # Ghi tất cả rows cùng lúc
```

## 6.4 Làm Việc Với JSON

```python
import json                                   # Module xử lý JSON

# Đọc JSON từ file
with open("data.json", "r") as f:            # Mở file JSON
    data = json.load(f)                      # json.load() chuyển JSON trong file thành Python object

# Ghi JSON vào file
sinh_vien = {"ten": "A", "tuoi": 22, "mon_hoc": ["Python", "SQL"]}  # Dict Python
with open("sv.json", "w", encoding="utf-8") as f:
    json.dump(sinh_vien, f, ensure_ascii=False, indent=2)  # json.dump() ghi Python object thành JSON

# String <-> JSON
json_str = json.dumps(sinh_vien, ensure_ascii=False)  # dumps() = Python -> JSON string
obj = json.loads(json_str)                    # loads() = JSON string -> Python object
```

## 6.5 Thao Tác File & Thư Mục (os, pathlib)

```python
import os                                     # Module thao tác hệ điều hành
from pathlib import Path                      # Path = class xử lý đường dẫn hiện đại

# os module
os.listdir(".")              # Liệt kê tất cả file/folder trong thư mục
os.makedirs("a/b/c", exist_ok=True)  # Tạo thư mục lồng nhau (exist_ok=không lỗi nếu đã có)
os.rename("old.txt", "new.txt")      # Đổi tên file
os.remove("file.txt")       # Xóa file
os.path.exists("file.txt")  # Kiểm tra file/folder có tồn tại (True/False)
os.path.getsize("file.txt") # Lấy kích thước file (bytes)

# pathlib (khuyến nghị, hiện đại hơn)
p = Path("project/data")                     # Tạo đối tượng Path
p.mkdir(parents=True, exist_ok=True)         # Tạo thư mục (parents=True tạo cả thư mục cha)

for f in Path(".").glob("**/*.py"):          # glob("**/*.py") tìm đệ quy tất cả file .py
    print(f)                                 # In đường dẫn từng file

# Đọc/ghi nhanh bằng pathlib
Path("hello.txt").write_text("Xin chào!", encoding="utf-8")  # Ghi chuỗi vào file (1 dòng)
content = Path("hello.txt").read_text(encoding="utf-8")       # Đọc toàn bộ file (1 dòng)
```

## 6.6 Exception Handling

### try / except / else / finally

```python
try:                                          # try: thử chạy code (có thể phát sinh lỗi)
    x = int(input("Nhập số: "))              # Có thể lỗi ValueError (nhập chữ)
    ket_qua = 10 / x                         # Có thể lỗi ZeroDivisionError (x=0)
except ValueError:                            # Bắt lỗi khi ép kiểu thất bại
    print("Không phải số!")
except ZeroDivisionError:                     # Bắt lỗi chia cho 0
    print("Không thể chia cho 0!")
except Exception as e:                        # Bắt mọi lỗi khác (Exception = class cha)
    print(f"Lỗi khác: {e}")                  # e = object lỗi, in chi tiết
else:                                         # else chạy khi KHÔNG có lỗi nào xảy ra
    print(f"Kết quả: {ket_qua}")
finally:                                      # finally LUÔN chạy (dù có lỗi hay không)
    print("Luôn chạy (dọn dẹp)")
```

### Raise Exception

```python
def chia(a, b):                               # Hàm chia có kiểm tra
    if b == 0:                                # Kiểm tra điều kiện lỗi
        raise ValueError("Không thể chia cho 0!")  # raise = ném lỗi chủ động
    return a / b                              # Trả về kết quả nếu hợp lệ

try:
    chia(10, 0)                               # Gọi hàm với b=0 -> raise ValueError
except ValueError as e:                       # Bắt lỗi đã raise
    print(f"Lỗi: {e}")                       # In message lỗi
```

### Custom Exception

```python
class ValidationError(Exception):             # Tạo class lỗi riêng, kế thừa Exception
    def __init__(self, field, message):       # Constructor nhận tên trường và message
        self.field = field                    # Lưu tên trường bị lỗi
        self.message = message               # Lưu message lỗi
        super().__init__(f"{field}: {message}")  # Gọi constructor cha với message format

class TuoiKhongHopLe(ValidationError):       # Kế thừa ValidationError (class lỗi cụ thể hơn)
    pass                                     # pass = không thêm gì (chỉ đổi tên)

def kiem_tra_tuoi(tuoi):                     # Hàm validate tuổi
    if not isinstance(tuoi, int):            # isinstance() kiểm tra kiểu dữ liệu
        raise TuoiKhongHopLe("tuoi", "phải là số nguyên")  # Ném lỗi custom
    if tuoi < 0 or tuoi > 150:               # Kiểm tra phạm vi
        raise TuoiKhongHopLe("tuoi", f"{tuoi} không hợp lệ (0-150)")  # Ném lỗi
    return True                              # Trả về True nếu hợp lệ

try:
    kiem_tra_tuoi(200)                       # Gọi với tuổi không hợp lệ
except TuoiKhongHopLe as e:                  # Bắt lỗi custom
    print(f"❌ {e}")                         # In message lỗi
```

## 6.7 Context Manager

```python
class Timer:                                  # Class context manager đo thời gian
    """Context manager đo thời gian"""
    def __enter__(self):                      # __enter__ chạy khi bắt đầu block "with"
        import time
        self.start = time.time()             # Ghi thời điểm bắt đầu
        return self                          # Trả về self để dùng trong "as"

    def __exit__(self, *args):               # __exit__ chạy khi kết thúc block "with"
        import time
        self.elapsed = time.time() - self.start  # Tính thời gian đã qua
        print(f"Thời gian: {self.elapsed:.4f}s")  # In thời gian

with Timer():                                # Sử dụng context manager
    sum(range(1_000_000))                    # Code cần đo thời gian

# Hoặc dùng contextlib
from contextlib import contextmanager        # Import decorator tạo context manager

@contextmanager                              # Biến generator function thành context manager
def managed_file(path, mode):                # Hàm quản lý file
    f = open(path, mode)                     # Mở file (setup)
    try:
        yield f                              # yield = trả về f cho block "with" sử dụng
    finally:
        f.close()                            # Đóng file (cleanup) - luôn chạy
```

## 6.8 Bài Tập

1. Đọc file text, đếm số dòng/từ/ký tự
2. Đọc CSV sinh viên, tính ĐTB và xuất file JSON
3. Viết hàm safe_divide với exception handling
4. Tạo context manager `@log_to_file` ghi log vào file

---

📖 **Trước đó**: [Chương 5](../chuong-05-oop/README.md) | **Tiếp theo**: [Chương 7](../chuong-07-cau-truc-du-lieu-nang-cao/README.md)
