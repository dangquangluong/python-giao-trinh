# Chương 6: File I/O & Exception Handling

## 6.1 Đọc File

```python
# Cách 1: open + close
f = open("file.txt", "r", encoding="utf-8")
noi_dung = f.read()
f.close()

# Cách 2: with (khuyến nghị - tự đóng file)
with open("file.txt", "r", encoding="utf-8") as f:
    noi_dung = f.read()       # Đọc toàn bộ
    # hoặc
    dong = f.readline()        # Đọc 1 dòng
    # hoặc
    tat_ca = f.readlines()     # List các dòng

# Đọc từng dòng (tiết kiệm RAM)
with open("file.txt") as f:
    for dong in f:
        print(dong.strip())
```

## 6.2 Ghi File

```python
# Ghi đè (w)
with open("output.txt", "w", encoding="utf-8") as f:
    f.write("Dòng 1\n")
    f.write("Dòng 2\n")

# Nối thêm (a)
with open("output.txt", "a") as f:
    f.write("Dòng thêm\n")

# writelines
lines = ["A\n", "B\n", "C\n"]
with open("output.txt", "w") as f:
    f.writelines(lines)
```

## 6.3 Làm Việc Với CSV

```python
import csv

# Đọc CSV
with open("data.csv", "r") as f:
    reader = csv.reader(f)
    header = next(reader)  # Dòng đầu (header)
    for row in reader:
        print(row)

# Đọc CSV thành dict
with open("data.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row["ten"], row["diem"])

# Ghi CSV
data = [["ten", "tuoi", "diem"], ["A", 20, 8.5], ["B", 21, 7.0]]
with open("output.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(data)
```

## 6.4 Làm Việc Với JSON

```python
import json

# Đọc JSON
with open("data.json", "r") as f:
    data = json.load(f)

# Ghi JSON
sinh_vien = {"ten": "A", "tuoi": 22, "mon_hoc": ["Python", "SQL"]}
with open("sv.json", "w", encoding="utf-8") as f:
    json.dump(sinh_vien, f, ensure_ascii=False, indent=2)

# String ↔ JSON
json_str = json.dumps(sinh_vien, ensure_ascii=False)
obj = json.loads(json_str)
```

## 6.5 Thao Tác File & Thư Mục (os, pathlib)

```python
import os
from pathlib import Path

# os module
os.listdir(".")              # Liệt kê thư mục
os.makedirs("a/b/c", exist_ok=True)  # Tạo thư mục
os.rename("old.txt", "new.txt")
os.remove("file.txt")       # Xóa file
os.path.exists("file.txt")  # Kiểm tra tồn tại
os.path.getsize("file.txt") # Kích thước

# pathlib (khuyến nghị, hiện đại hơn)
p = Path("project/data")
p.mkdir(parents=True, exist_ok=True)

for f in Path(".").glob("**/*.py"):  # Tìm đệ quy
    print(f)

# Đọc/ghi nhanh
Path("hello.txt").write_text("Xin chào!", encoding="utf-8")
content = Path("hello.txt").read_text(encoding="utf-8")
```

## 6.6 Exception Handling

### try / except / else / finally

```python
try:
    x = int(input("Nhập số: "))
    ket_qua = 10 / x
except ValueError:
    print("Không phải số!")
except ZeroDivisionError:
    print("Không thể chia cho 0!")
except Exception as e:
    print(f"Lỗi khác: {e}")
else:
    print(f"Kết quả: {ket_qua}")  # Chạy khi KHÔNG có lỗi
finally:
    print("Luôn chạy (dọn dẹp)")  # Luôn chạy
```

### Raise Exception

```python
def chia(a, b):
    if b == 0:
        raise ValueError("Không thể chia cho 0!")
    return a / b

try:
    chia(10, 0)
except ValueError as e:
    print(f"Lỗi: {e}")
```

### Custom Exception

```python
class ValidationError(Exception):
    def __init__(self, field, message):
        self.field = field
        self.message = message
        super().__init__(f"{field}: {message}")

class TuoiKhongHopLe(ValidationError):
    pass

def kiem_tra_tuoi(tuoi):
    if not isinstance(tuoi, int):
        raise TuoiKhongHopLe("tuoi", "phải là số nguyên")
    if tuoi < 0 or tuoi > 150:
        raise TuoiKhongHopLe("tuoi", f"{tuoi} không hợp lệ (0-150)")
    return True

try:
    kiem_tra_tuoi(200)
except TuoiKhongHopLe as e:
    print(f"❌ {e}")
```

## 6.7 Context Manager

```python
class Timer:
    """Context manager đo thời gian"""
    def __enter__(self):
        import time
        self.start = time.time()
        return self

    def __exit__(self, *args):
        import time
        self.elapsed = time.time() - self.start
        print(f"Thời gian: {self.elapsed:.4f}s")

with Timer():
    sum(range(1_000_000))

# Hoặc dùng contextlib
from contextlib import contextmanager

@contextmanager
def managed_file(path, mode):
    f = open(path, mode)
    try:
        yield f
    finally:
        f.close()
```

## 6.8 Bài Tập

1. Đọc file text, đếm số dòng/từ/ký tự
2. Đọc CSV sinh viên, tính ĐTB và xuất file JSON
3. Viết hàm safe_divide với exception handling
4. Tạo context manager `@log_to_file` ghi log vào file

---

📖 **Trước đó**: [Chương 5](../chuong-05-oop/README.md) | **Tiếp theo**: [Chương 7](../chuong-07-cau-truc-du-lieu-nang-cao/README.md)
