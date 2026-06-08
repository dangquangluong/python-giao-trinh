# Chương 2: Cú Pháp Cơ Bản & Kiểu Dữ Liệu

## 2.1 Biến (Variables)

Python **không cần khai báo kiểu** - tự suy luận:

```python
# Gán biến
ten = "Nguyễn Văn A"     # str (chuỗi ký tự) - dùng dấu "" hoặc ''
tuoi = 25                  # int (số nguyên) - không có dấu chấm
chieu_cao = 1.75           # float (số thực) - có dấu chấm thập phân
la_sv = True               # bool (boolean) - chỉ có True hoặc False

# Gán nhiều biến cùng lúc
x, y, z = 1, 2, 3         # Gán đồng thời: x=1, y=2, z=3
a = b = c = 0             # Gán cùng giá trị 0 cho cả 3 biến

# Kiểm tra kiểu
print(type(ten))       # <class 'str'> - type() trả về kiểu dữ liệu
print(type(tuoi))      # <class 'int'> - kiểu số nguyên
```

### Quy Tắc Đặt Tên

```python
# ✅ Đúng
ten_sinh_vien = "A"    # snake_case (khuyến nghị trong Python)
soLuong = 10           # camelCase (ít dùng trong Python)
MAX_SIZE = 100         # UPPER_CASE cho hằng số (constant)

# ❌ Sai
2name = "X"            # Không bắt đầu bằng số
my-var = 5             # Không dùng dấu gạch ngang
class = "A"            # Không dùng từ khóa (keyword) của Python
```

## 2.2 Kiểu Dữ Liệu

### Số (Numbers)

```python
# Integer (số nguyên)
x = 42                     # Số nguyên dương
y = -10                    # Số nguyên âm
lon = 1_000_000            # Dùng _ cho dễ đọc (= 1000000)

# Float (số thực)
pi = 3.14159               # Số có phần thập phân
nhiet_do = -5.5            # Float âm

# Complex (số phức)
z = 3 + 4j                 # j = phần ảo (dùng trong toán học)

# Phép tính
print(10 + 3)    # 13     (cộng)
print(10 - 3)    # 7      (trừ)
print(10 * 3)    # 30     (nhân)
print(10 / 3)    # 3.333  (chia - luôn trả về float)
print(10 // 3)   # 3      (chia lấy phần nguyên - bỏ phần thập phân)
print(10 % 3)    # 1      (chia lấy dư - modulo)
print(2 ** 10)   # 1024   (lũy thừa - 2 mũ 10)
```

### Chuỗi (String)

```python
# Khai báo
s1 = "Xin chào"           # Chuỗi dùng dấu ngoặc kép
s2 = 'Hello'              # Chuỗi dùng dấu ngoặc đơn (tương đương)
s3 = """Chuỗi
nhiều dòng"""              # Triple quotes cho chuỗi nhiều dòng

# Nối chuỗi
ho = "Nguyễn"             # Chuỗi họ
ten = "Nam"               # Chuỗi tên
ho_ten = ho + " " + ten   # Dùng + để nối chuỗi lại với nhau

# f-string (khuyến nghị)
tuoi = 25                  # Biến số
print(f"{ho_ten} - {tuoi} tuổi")  # f-string: chèn biến vào {} trong chuỗi

# Chuỗi methods
text = "  Hello World  "           # Chuỗi có khoảng trắng đầu cuối
print(text.upper())        # "  HELLO WORLD  " - chuyển thành CHỮ HOA
print(text.lower())        # "  hello world  " - chuyển thành chữ thường
print(text.strip())        # "Hello World" - xóa khoảng trắng đầu/cuối
print(text.replace("World", "Python"))  # Thay thế chuỗi con
print(text.split())        # ['Hello', 'World'] - tách thành list theo khoảng trắng
print(len(text))           # 15 - len() đếm số ký tự (kể cả khoảng trắng)

# Slicing (cắt chuỗi)
s = "Python"               # Chuỗi 6 ký tự, index: P=0, y=1, t=2, h=3, o=4, n=5
print(s[0])      # 'P'    - lấy ký tự đầu tiên (index bắt đầu từ 0)
print(s[-1])     # 'n'    - index âm: -1 = ký tự cuối cùng
print(s[0:3])    # 'Pyt'  - lấy từ index 0 đến 2 (không bao gồm 3)
print(s[2:])     # 'thon' - từ index 2 đến hết
print(s[::-1])   # 'nohtyP' - đảo ngược chuỗi (bước -1)
```

### Boolean

```python
x = True                   # Giá trị boolean True (Đúng)
y = False                  # Giá trị boolean False (Sai)

# So sánh → boolean
print(5 > 3)       # True  - 5 lớn hơn 3
print(5 == 3)      # False - == so sánh bằng (khác = gán giá trị)
print(5 != 3)      # True  - != nghĩa là "không bằng"

# Logic
print(True and False)   # False - and: cả hai đều True mới True
print(True or False)    # True  - or: một trong hai True là True
print(not True)         # False - not: đảo ngược giá trị

# Giá trị "falsy"
# False, 0, 0.0, "", [], {}, None → đều là False khi dùng trong if
```

### None

```python
ket_qua = None      # None = không có giá trị (khác 0, khác "")
print(ket_qua is None)  # True - dùng "is" để so sánh với None
```

## 2.3 List (Danh sách)

```python
# Tạo list
diem = [85, 90, 78, 92, 88]       # List chứa 5 số nguyên, dùng dấu []
hon_hop = [1, "hello", True, 3.14] # List có thể chứa nhiều kiểu khác nhau

# Truy cập
print(diem[0])      # 85 - phần tử đầu tiên (index 0)
print(diem[-1])     # 88 - phần tử cuối cùng (index -1)
print(diem[1:3])    # [90, 78] - slicing: từ index 1 đến 2

# Thay đổi
diem[0] = 95             # Gán giá trị mới cho phần tử index 0
diem.append(100)         # Thêm 100 vào cuối list
diem.insert(0, 70)       # Chèn 70 vào vị trí index 0
diem.remove(78)          # Xóa phần tử có giá trị 78 (xóa cái đầu tiên tìm thấy)
diem.pop()               # Xóa và trả về phần tử cuối cùng
diem.sort()              # Sắp xếp list tăng dần (thay đổi list gốc)
diem.reverse()           # Đảo ngược thứ tự list

# Thông tin
print(len(diem))         # Số phần tử trong list
print(max(diem))         # Giá trị lớn nhất
print(min(diem))         # Giá trị nhỏ nhất
print(sum(diem))         # Tổng tất cả phần tử
```

## 2.4 Tuple (Bộ - không thay đổi được)

```python
# Tuple - giống list nhưng IMMUTABLE (không thể sửa sau khi tạo)
toa_do = (10, 20)              # Tạo tuple dùng dấu ()
mau_rgb = (255, 128, 0)       # Tuple 3 phần tử

# Truy cập
print(toa_do[0])     # 10 - truy cập giống list

# Unpacking - gán từng phần tử vào biến riêng
x, y = toa_do               # x=10, y=20
r, g, b = mau_rgb           # r=255, g=128, b=0

# KHÔNG THỂ thay đổi
# toa_do[0] = 5  # ❌ TypeError! Tuple là immutable
```

## 2.5 Dictionary (Từ điển)

```python
# Tạo dict - lưu dữ liệu dạng key: value (khóa: giá trị)
sinh_vien = {
    "ten": "Nguyễn A",                    # key "ten", value "Nguyễn A"
    "tuoi": 22,                            # key "tuoi", value 22
    "diem": 8.5,                           # key "diem", value 8.5
    "mon_hoc": ["Python", "Java", "SQL"]   # value có thể là list
}

# Truy cập
print(sinh_vien["ten"])          # "Nguyễn A" - truy cập bằng key
print(sinh_vien.get("tuoi"))     # 22 - .get() an toàn hơn (không lỗi nếu key không có)
print(sinh_vien.get("lop", "N/A"))  # "N/A" - giá trị mặc định nếu key không tồn tại

# Thay đổi
sinh_vien["tuoi"] = 23             # Cập nhật value cho key "tuoi"
sinh_vien["email"] = "a@mail.com"  # Thêm cặp key:value mới
del sinh_vien["email"]              # Xóa cặp key:value

# Duyệt
for key, value in sinh_vien.items():  # .items() trả về từng cặp (key, value)
    print(f"{key}: {value}")          # In từng cặp

# Methods
print(sinh_vien.keys())     # Danh sách tất cả keys
print(sinh_vien.values())   # Danh sách tất cả values
```

## 2.6 Set (Tập hợp)

```python
# Set - không trùng lặp, không có thứ tự, dùng dấu {}
fruits = {"apple", "banana", "cherry", "apple"}  # "apple" trùng sẽ bị loại
print(fruits)   # {'apple', 'banana', 'cherry'} - chỉ còn 3 phần tử

# Phép toán tập hợp
a = {1, 2, 3, 4}          # Set a
b = {3, 4, 5, 6}          # Set b
print(a | b)    # Hợp: {1, 2, 3, 4, 5, 6} - tất cả phần tử của cả hai
print(a & b)    # Giao: {3, 4} - phần tử chung
print(a - b)    # Hiệu: {1, 2} - phần tử có trong a nhưng không có trong b
```

## 2.7 Ép Kiểu (Type Casting)

```python
# String → Int/Float
x = int("42")       # 42 - ép chuỗi "42" thành số nguyên 42
y = float("3.14")   # 3.14 - ép chuỗi thành số thực

# Int → String
s = str(100)         # "100" - ép số thành chuỗi

# List ↔ Tuple ↔ Set
lst = [1, 2, 2, 3]      # List (có trùng)
tup = tuple(lst)     # (1, 2, 2, 3) - chuyển list thành tuple
st = set(lst)        # {1, 2, 3} - chuyển thành set (loại bỏ trùng)
```

## 2.8 Input/Output

```python
# Output
print("Hello")                       # In chuỗi ra màn hình
print("A", "B", "C", sep="-")    # A-B-C - sep thay dấu phân cách (mặc định là space)
print("No newline", end=" ")      # end=" " không xuống dòng (mặc định end="\n")

# Input
ten = input("Tên bạn: ")            # Hiện "Tên bạn: " và chờ nhập, trả về str
tuoi = int(input("Tuổi: "))         # Nhập chuỗi rồi ép thành int
print(f"Chào {ten}, {tuoi} tuổi!")  # In kết quả dùng f-string

# Format
pi = 3.14159                         # Số cần format
print(f"Pi = {pi:.2f}")           # Pi = 3.14 - :.2f = 2 chữ số thập phân
print(f"{'Hello':>20}")           # Căn phải 20 ký tự
print(f"{'Hello':<20}")           # Căn trái 20 ký tự
print(f"{'Hello':^20}")           # Căn giữa 20 ký tự
print(f"{1000000:,}")             # 1,000,000 - thêm dấu phẩy phân cách hàng nghìn
```

## 2.9 Bài Tập

1. Viết chương trình tính BMI (nhập cân nặng, chiều cao)
2. Nhập chuỗi → đếm số nguyên âm (a, e, i, o, u)
3. Tạo dict lưu thông tin 3 sinh viên, in ra dạng bảng
4. Nhập list số → tính trung bình, max, min

---

📖 **Trước đó**: [Chương 1](../chuong-01-gioi-thieu/README.md) | **Tiếp theo**: [Chương 3](../chuong-03-cau-truc-dieu-khien/README.md)
