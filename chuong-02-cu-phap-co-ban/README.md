# Chương 2: Cú Pháp Cơ Bản & Kiểu Dữ Liệu

## 2.1 Biến (Variables)

Python **không cần khai báo kiểu** - tự suy luận:

```python
# Gán biến
ten = "Nguyễn Văn A"     # str
tuoi = 25                  # int
chieu_cao = 1.75           # float
la_sv = True               # bool

# Gán nhiều biến cùng lúc
x, y, z = 1, 2, 3
a = b = c = 0

# Kiểm tra kiểu
print(type(ten))       # <class 'str'>
print(type(tuoi))      # <class 'int'>
```

### Quy Tắc Đặt Tên

```python
# ✅ Đúng
ten_sinh_vien = "A"    # snake_case (khuyến nghị)
soLuong = 10           # camelCase (ít dùng trong Python)
MAX_SIZE = 100         # UPPER_CASE cho hằng số

# ❌ Sai
2name = "X"            # Không bắt đầu bằng số
my-var = 5             # Không dùng dấu gạch ngang
class = "A"            # Không dùng từ khóa
```

## 2.2 Kiểu Dữ Liệu

### Số (Numbers)

```python
# Integer (số nguyên)
x = 42
y = -10
lon = 1_000_000        # Dùng _ cho dễ đọc

# Float (số thực)
pi = 3.14159
nhiet_do = -5.5

# Complex (số phức)
z = 3 + 4j

# Phép tính
print(10 + 3)    # 13     (cộng)
print(10 - 3)    # 7      (trừ)
print(10 * 3)    # 30     (nhân)
print(10 / 3)    # 3.333  (chia)
print(10 // 3)   # 3      (chia lấy phần nguyên)
print(10 % 3)    # 1      (chia lấy dư)
print(2 ** 10)   # 1024   (lũy thừa)
```

### Chuỗi (String)

```python
# Khai báo
s1 = "Xin chào"
s2 = 'Hello'
s3 = """Chuỗi
nhiều dòng"""

# Nối chuỗi
ho = "Nguyễn"
ten = "Nam"
ho_ten = ho + " " + ten

# f-string (khuyến nghị)
tuoi = 25
print(f"{ho_ten} - {tuoi} tuổi")

# Chuỗi methods
text = "  Hello World  "
print(text.upper())        # "  HELLO WORLD  "
print(text.lower())        # "  hello world  "
print(text.strip())        # "Hello World"
print(text.replace("World", "Python"))
print(text.split())        # ['Hello', 'World']
print(len(text))           # 15

# Slicing (cắt chuỗi)
s = "Python"
print(s[0])      # 'P'
print(s[-1])     # 'n'
print(s[0:3])    # 'Pyt'
print(s[2:])     # 'thon'
print(s[::-1])   # 'nohtyP' (đảo ngược)
```

### Boolean

```python
x = True
y = False

# So sánh → boolean
print(5 > 3)       # True
print(5 == 3)      # False
print(5 != 3)      # True

# Logic
print(True and False)   # False
print(True or False)    # True
print(not True)         # False

# Giá trị "falsy"
# False, 0, 0.0, "", [], {}, None → đều là False
```

### None

```python
ket_qua = None      # Không có giá trị
print(ket_qua is None)  # True
```

## 2.3 List (Danh sách)

```python
# Tạo list
diem = [85, 90, 78, 92, 88]
hon_hop = [1, "hello", True, 3.14]

# Truy cập
print(diem[0])      # 85
print(diem[-1])     # 88
print(diem[1:3])    # [90, 78]

# Thay đổi
diem[0] = 95
diem.append(100)         # Thêm cuối
diem.insert(0, 70)       # Thêm vào vị trí 0
diem.remove(78)          # Xóa giá trị 78
diem.pop()               # Xóa và trả về phần tử cuối
diem.sort()              # Sắp xếp
diem.reverse()           # Đảo ngược

# Thông tin
print(len(diem))         # Số phần tử
print(max(diem))         # Giá trị lớn nhất
print(min(diem))         # Giá trị nhỏ nhất
print(sum(diem))         # Tổng
```

## 2.4 Tuple (Bộ - không thay đổi được)

```python
# Tuple - giống list nhưng IMMUTABLE
toa_do = (10, 20)
mau_rgb = (255, 128, 0)

# Truy cập
print(toa_do[0])     # 10

# Unpacking
x, y = toa_do
r, g, b = mau_rgb

# KHÔNG THỂ thay đổi
# toa_do[0] = 5  # ❌ TypeError!
```

## 2.5 Dictionary (Từ điển)

```python
# Tạo dict
sinh_vien = {
    "ten": "Nguyễn A",
    "tuoi": 22,
    "diem": 8.5,
    "mon_hoc": ["Python", "Java", "SQL"]
}

# Truy cập
print(sinh_vien["ten"])          # "Nguyễn A"
print(sinh_vien.get("tuoi"))     # 22
print(sinh_vien.get("lop", "N/A"))  # "N/A" (default)

# Thay đổi
sinh_vien["tuoi"] = 23
sinh_vien["email"] = "a@mail.com"  # Thêm mới
del sinh_vien["email"]              # Xóa

# Duyệt
for key, value in sinh_vien.items():
    print(f"{key}: {value}")

# Methods
print(sinh_vien.keys())     # Danh sách keys
print(sinh_vien.values())   # Danh sách values
```

## 2.6 Set (Tập hợp)

```python
# Set - không trùng lặp, không có thứ tự
fruits = {"apple", "banana", "cherry", "apple"}
print(fruits)   # {'apple', 'banana', 'cherry'}

# Phép toán tập hợp
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print(a | b)    # Hợp: {1, 2, 3, 4, 5, 6}
print(a & b)    # Giao: {3, 4}
print(a - b)    # Hiệu: {1, 2}
```

## 2.7 Ép Kiểu (Type Casting)

```python
# String → Int/Float
x = int("42")       # 42
y = float("3.14")   # 3.14

# Int → String
s = str(100)         # "100"

# List ↔ Tuple ↔ Set
lst = [1, 2, 2, 3]
tup = tuple(lst)     # (1, 2, 2, 3)
st = set(lst)        # {1, 2, 3}
```

## 2.8 Input/Output

```python
# Output
print("Hello")
print("A", "B", "C", sep="-")    # A-B-C
print("No newline", end=" ")

# Input
ten = input("Tên bạn: ")
tuoi = int(input("Tuổi: "))
print(f"Chào {ten}, {tuoi} tuổi!")

# Format
pi = 3.14159
print(f"Pi = {pi:.2f}")           # Pi = 3.14
print(f"{'Hello':>20}")           # Căn phải 20 ký tự
print(f"{'Hello':<20}")           # Căn trái
print(f"{'Hello':^20}")           # Căn giữa
print(f"{1000000:,}")             # 1,000,000
```

## 2.9 Bài Tập

1. Viết chương trình tính BMI (nhập cân nặng, chiều cao)
2. Nhập chuỗi → đếm số nguyên âm (a, e, i, o, u)
3. Tạo dict lưu thông tin 3 sinh viên, in ra dạng bảng
4. Nhập list số → tính trung bình, max, min

---

📖 **Trước đó**: [Chương 1](../chuong-01-gioi-thieu/README.md) | **Tiếp theo**: [Chương 3](../chuong-03-cau-truc-dieu-khien/README.md)
