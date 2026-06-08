# Chuong 6: Xu Ly File Va Exception

## 6.1 Doc File

### Doc toan bo file

```python
# Cach 1: Doc het noi dung
with open("data.txt", "r", encoding="utf-8") as f:
    noi_dung = f.read()
    print(noi_dung)

# Cach 2: Doc theo dong
with open("data.txt", "r", encoding="utf-8") as f:
    for dong in f:
        print(dong.strip())

# Cach 3: Doc tat ca dong thanh list
with open("data.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
    print(f"Tong so dong: {len(lines)}")
```

### Doc file CSV

```python
import csv

with open("data.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row)
```

## 6.2 Ghi File

### Ghi file text

```python
# Ghi moi (ghi de)
with open("output.txt", "w", encoding="utf-8") as f:
    f.write("Dong thu nhat\n")
    f.write("Dong thu hai\n")

# Ghi them (append)
with open("output.txt", "a", encoding="utf-8") as f:
    f.write("Dong them vao\n")

# Ghi nhieu dong
lines = ["Dong 1\n", "Dong 2\n", "Dong 3\n"]
with open("output.txt", "w", encoding="utf-8") as f:
    f.writelines(lines)
```

### Ghi file JSON

```python
import json

data = {
    "ten": "Nguyen Van A",
    "tuoi": 25,
    "ky_nang": ["Python", "SQL", "Git"]
}

# Ghi ra file
with open("data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

# Doc tu file
with open("data.json", "r", encoding="utf-8") as f:
    data = json.load(f)
    print(data)
```

## 6.3 Thao Tac Voi Duong Dan

```python
from pathlib import Path

# Tao duong dan
p = Path("thu_muc/file.txt")

# Thuoc tinh
print(p.name)       # file.txt
print(p.stem)       # file
print(p.suffix)     # .txt
print(p.parent)     # thu_muc

# Kiem tra ton tai
print(p.exists())
print(p.is_file())
print(p.is_dir())

# Tao thu muc
Path("output/data").mkdir(parents=True, exist_ok=True)

# Liet ke file
for f in Path(".").glob("*.py"):
    print(f)

# Liet ke de quy
for f in Path(".").rglob("*.txt"):
    print(f)
```

## 6.4 Exception (Ngoai Le)

### Try/Except co ban

```python
try:
    so = int(input("Nhap mot so: "))
    ket_qua = 100 / so
    print(f"100 / {so} = {ket_qua}")
except ValueError:
    print("Loi: Ban phai nhap mot so nguyen")
except ZeroDivisionError:
    print("Loi: Khong the chia cho 0")
```

### Try/Except/Else/Finally

```python
try:
    f = open("data.txt", "r")
    noi_dung = f.read()
except FileNotFoundError:
    print("Loi: File khong ton tai")
except PermissionError:
    print("Loi: Khong co quyen truy cap")
else:
    # Chay khi khong co loi
    print(f"Doc thanh cong: {len(noi_dung)} ky tu")
finally:
    # Luon chay du co loi hay khong
    print("Hoan tat xu ly file")
```

### Bat nhieu exception

```python
try:
    # Code co the gay loi
    result = risky_operation()
except (ValueError, TypeError) as e:
    print(f"Loi du lieu: {e}")
except Exception as e:
    print(f"Loi khong xac dinh: {e}")
```

## 6.5 Raise Exception

```python
def chia(a, b):
    if b == 0:
        raise ValueError("Mau so khong the bang 0")
    return a / b

def kiem_tra_tuoi(tuoi):
    if not isinstance(tuoi, int):
        raise TypeError("Tuoi phai la so nguyen")
    if tuoi < 0 or tuoi > 150:
        raise ValueError("Tuoi khong hop le (0-150)")
    return tuoi
```

## 6.6 Custom Exception

```python
class AppError(Exception):
    """Base exception cho ung dung."""
    pass

class ValidationError(AppError):
    """Loi xac thuc du lieu."""
    def __init__(self, field, message):
        self.field = field
        self.message = message
        super().__init__(f"{field}: {message}")

class NotFoundError(AppError):
    """Loi khong tim thay."""
    def __init__(self, resource, id):
        self.resource = resource
        self.id = id
        super().__init__(f"{resource} voi id={id} khong ton tai")

# Su dung
def tao_user(ten, email):
    if not ten:
        raise ValidationError("ten", "Khong duoc de trong")
    if "@" not in email:
        raise ValidationError("email", "Email khong hop le")
    return {"ten": ten, "email": email}

try:
    user = tao_user("", "test@example.com")
except ValidationError as e:
    print(f"Loi: {e}")
    print(f"Field: {e.field}")
```

## 6.7 Context Manager

### Su dung with

```python
# with tu dong dong file khi xong
with open("data.txt", "r") as f:
    data = f.read()
# f da duoc dong o day
```

### Tao context manager bang class

```python
class DatabaseConnection:
    def __init__(self, host, db_name):
        self.host = host
        self.db_name = db_name
        self.connection = None
    
    def __enter__(self):
        print(f"Ket noi den {self.host}/{self.db_name}")
        self.connection = f"Connection to {self.db_name}"
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Dong ket noi")
        self.connection = None
        return False  # Khong an exception

with DatabaseConnection("localhost", "mydb") as db:
    print(f"Dang dung: {db.connection}")
```

### Tao context manager bang contextmanager decorator

```python
from contextlib import contextmanager

@contextmanager
def timer(label):
    """Context manager do thoi gian."""
    import time
    start = time.time()
    print(f"[{label}] Bat dau...")
    try:
        yield
    finally:
        elapsed = time.time() - start
        print(f"[{label}] Hoan tat trong {elapsed:.4f}s")

with timer("Tinh toan"):
    total = sum(range(1000000))
    print(f"Tong: {total}")
```

## 6.8 Xu Ly File Nhi Phan

```python
# Doc file nhi phan
with open("image.png", "rb") as f:
    data = f.read()
    print(f"Kich thuoc: {len(data)} bytes")

# Ghi file nhi phan
with open("copy.png", "wb") as f:
    f.write(data)
```

## Bai Tap

1. Viet chuong trinh doc file text va dem so dong, so tu, so ky tu
2. Viet chuong trinh quan ly danh ba: them, xoa, tim, luu vao file JSON
3. Tao custom exception cho ung dung quan ly sinh vien (DuplicateError, NotFoundError)
4. Viet context manager `@contextmanager` de quan ly file tam (tao va tu dong xoa)
5. Viet chuong trinh doc file CSV va tinh diem trung binh cua sinh vien
6. Tao chuong trinh copy file voi thanh tien trinh (progress bar)

## Tai Lieu Tham Khao

- [Python File I/O](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files)
- [Errors and Exceptions](https://docs.python.org/3/tutorial/errors.html)
- [Context Managers](https://docs.python.org/3/reference/datamodel.html#context-managers)
