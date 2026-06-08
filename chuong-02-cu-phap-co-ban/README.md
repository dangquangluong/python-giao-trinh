# Chuong 2: Cu Phap Co Ban

## 2.1 Bien (Variables)

Bien la noi luu tru du lieu trong chuong trinh. Python la ngon ngu dynamic typing, khong can khai bao kieu du lieu truoc.

```python
# Khai bao bien
ten = "Nguyen Van A"
tuoi = 25
chieu_cao = 1.75
la_sinh_vien = True

# Gan nhieu bien cung luc
x, y, z = 1, 2, 3

# Gan cung mot gia tri
a = b = c = 0
```

### Quy Tac Dat Ten Bien

- Bat dau bang chu cai hoac dau gach duoi `_`
- Chi chua chu cai, so va `_`
- Phan biet chu hoa va chu thuong
- Khong dung tu khoa Python (if, for, class, ...)

```python
# Dung
ten_bien = "gia tri"
_private = 10
soLuong = 5
MAX_SIZE = 100

# Sai
2bien = "loi"       # Bat dau bang so
ten-bien = "loi"    # Chua dau gach ngang
class = "loi"       # Tu khoa Python
```

## 2.2 Kieu Du Lieu (Data Types)

### Kieu so (Numeric)

```python
# int - so nguyen
a = 42
b = -10
c = 0b1010    # Nhi phan (binary) = 10
d = 0o17      # Bat phan (octal) = 15
e = 0xFF      # Thap luc phan (hex) = 255

# float - so thuc
pi = 3.14159
nhiet_do = -5.5
khoa_hoc = 1.5e10  # 1.5 x 10^10

# complex - so phuc
z = 3 + 4j
```

### Kieu chuoi (String)

```python
# Khai bao chuoi
ten = "Nguyen Van A"
dia_chi = 'Ha Noi'
mo_ta = """Day la chuoi
nhieu dong"""

# Cac thao tac voi chuoi
s = "Hello Python"
print(len(s))        # Do dai: 12
print(s.upper())     # HOA: HELLO PYTHON
print(s.lower())     # thuong: hello python
print(s[0:5])        # Cat: Hello
print(s.replace("Hello", "Xin chao"))  # Thay the
print(s.split(" "))  # Tach: ['Hello', 'Python']

# f-string (format string)
ten = "An"
tuoi = 20
print(f"Toi la {ten}, {tuoi} tuoi")
```

### Kieu boolean

```python
dung = True
sai = False

# Ket qua cua phep so sanh
print(5 > 3)   # True
print(5 == 3)  # False
```

### Kieu None

```python
ket_qua = None  # Khong co gia tri
```

### Kieu danh sach (List)

```python
# List - co the thay doi (mutable)
fruits = ["tao", "cam", "chuoi"]
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", True, 3.14]

# Truy cap phan tu
print(fruits[0])    # tao
print(fruits[-1])   # chuoi

# Thay doi
fruits.append("nho")       # Them cuoi
fruits.insert(1, "buoi")   # Chen vao vi tri 1
fruits.remove("cam")       # Xoa theo gia tri
del fruits[0]              # Xoa theo index
```

### Kieu tuple

```python
# Tuple - khong the thay doi (immutable)
toa_do = (10, 20)
colors = ("do", "xanh", "vang")

x, y = toa_do  # Unpacking
```

### Kieu dictionary

```python
# Dictionary - cap key:value
sinh_vien = {
    "ten": "Nguyen Van A",
    "tuoi": 20,
    "diem": 8.5
}

# Truy cap
print(sinh_vien["ten"])
print(sinh_vien.get("email", "Khong co"))

# Them/sua
sinh_vien["email"] = "a@example.com"
sinh_vien["tuoi"] = 21
```

### Kieu set

```python
# Set - tap hop khong trung lap
numbers = {1, 2, 3, 4, 5}
letters = set("hello")  # {'h', 'e', 'l', 'o'}

# Phep toan tap hop
a = {1, 2, 3}
b = {2, 3, 4}
print(a | b)  # Hop: {1, 2, 3, 4}
print(a & b)  # Giao: {2, 3}
print(a - b)  # Hieu: {1}
```

## 2.3 Toan Tu (Operators)

### Toan tu so hoc

```python
a, b = 10, 3
print(a + b)   # Cong: 13
print(a - b)   # Tru: 7
print(a * b)   # Nhan: 30
print(a / b)   # Chia: 3.333...
print(a // b)  # Chia nguyen: 3
print(a % b)   # Chia du: 1
print(a ** b)  # Luy thua: 1000
```

### Toan tu so sanh

```python
x, y = 5, 10
print(x == y)  # Bang: False
print(x != y)  # Khac: True
print(x > y)   # Lon hon: False
print(x < y)   # Nho hon: True
print(x >= y)  # Lon hon hoac bang: False
print(x <= y)  # Nho hon hoac bang: True
```

### Toan tu logic

```python
a, b = True, False
print(a and b)  # Va: False
print(a or b)   # Hoac: True
print(not a)    # Phu dinh: False
```

### Toan tu gan

```python
x = 10
x += 5   # x = x + 5 = 15
x -= 3   # x = x - 3 = 12
x *= 2   # x = x * 2 = 24
x /= 4   # x = x / 4 = 6.0
x //= 2  # x = x // 2 = 3.0
x **= 3  # x = x ** 3 = 27.0
```

### Toan tu thanh vien va dinh danh

```python
# in, not in
fruits = ["tao", "cam", "chuoi"]
print("tao" in fruits)      # True
print("nho" not in fruits)  # True

# is, is not
a = [1, 2, 3]
b = a
c = [1, 2, 3]
print(a is b)      # True (cung doi tuong)
print(a is c)      # False (khac doi tuong)
print(a == c)      # True (cung gia tri)
```

## 2.4 Nhap Xuat (Input/Output)

### Ham print()

```python
# In co ban
print("Hello World")

# In nhieu gia tri
print("Ten:", "An", "Tuoi:", 20)

# Thay doi ky tu ngan cach
print("a", "b", "c", sep="-")  # a-b-c

# Khong xuong dong
print("Hello", end=" ")
print("World")  # Hello World

# Dinh dang
pi = 3.14159
print(f"Pi = {pi:.2f}")        # Pi = 3.14
print(f"{'Python':>10}")       # Can phai: "    Python"
print(f"{'Python':<10}")       # Can trai: "Python    "
print(f"{'Python':^10}")       # Can giua: "  Python  "
```

### Ham input()

```python
# Nhap du lieu tu ban phim
ten = input("Nhap ten cua ban: ")
tuoi = int(input("Nhap tuoi: "))
chieu_cao = float(input("Nhap chieu cao (m): "))

print(f"Xin chao {ten}, ban {tuoi} tuoi, cao {chieu_cao}m")
```

## 2.5 Chuyen Doi Kieu Du Lieu

```python
# Chuyen doi kieu
x = "123"
y = int(x)      # String -> int
z = float(x)    # String -> float

a = 42
b = str(a)      # int -> String
c = float(a)    # int -> float

# Chuyen doi list/tuple/set
lst = [1, 2, 3, 2, 1]
t = tuple(lst)   # List -> Tuple
s = set(lst)     # List -> Set (loai trung: {1, 2, 3})
lst2 = list(s)   # Set -> List
```

## Bai Tap

1. Viet chuong trinh nhap ten, tuoi, va in ra loi chao
2. Viet chuong trinh tinh dien tich va chu vi hinh tron (nhap ban kinh)
3. Viet chuong trinh doi nhiet do tu Celsius sang Fahrenheit va nguoc lai
4. Viet chuong trinh nhap 2 so va thuc hien cac phep tinh: +, -, *, /, //, %, **
5. Tao dictionary luu thong tin sinh vien (ten, mssv, diem) va in ra man hinh
6. Viet chuong trinh hoan doi gia tri 2 bien khong dung bien tam

## Tai Lieu Tham Khao

- [Python Data Types](https://docs.python.org/3/library/stdtypes.html)
- [Python Operators](https://docs.python.org/3/reference/expressions.html)
- [String Methods](https://docs.python.org/3/library/stdtypes.html#string-methods)
