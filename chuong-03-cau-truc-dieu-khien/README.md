# Chuong 3: Cau Truc Dieu Khien

## 3.1 Cau Lenh If/Else

### If don gian

```python
tuoi = 18

if tuoi >= 18:
    print("Ban da du tuoi")
```

### If/Else

```python
diem = 7.5

if diem >= 5:
    print("Dat")
else:
    print("Khong dat")
```

### If/Elif/Else

```python
diem = 8.5

if diem >= 9:
    xep_loai = "Xuat sac"
elif diem >= 8:
    xep_loai = "Gioi"
elif diem >= 7:
    xep_loai = "Kha"
elif diem >= 5:
    xep_loai = "Trung binh"
else:
    xep_loai = "Khong dat"

print(f"Diem: {diem} - Xep loai: {xep_loai}")
```

### Toan tu ba ngoi (Ternary)

```python
tuoi = 20
ket_qua = "Nguoi lon" if tuoi >= 18 else "Tre em"
print(ket_qua)
```

### Dieu kien long nhau

```python
username = "admin"
password = "123456"

if username == "admin":
    if password == "123456":
        print("Dang nhap thanh cong!")
    else:
        print("Sai mat khau!")
else:
    print("Sai ten dang nhap!")
```

## 3.2 Vong Lap For

### Duyet list

```python
fruits = ["tao", "cam", "chuoi", "nho"]
for fruit in fruits:
    print(f"Toi thich an {fruit}")
```

### Ham range()

```python
# range(stop)
for i in range(5):
    print(i)  # 0, 1, 2, 3, 4

# range(start, stop)
for i in range(1, 6):
    print(i)  # 1, 2, 3, 4, 5

# range(start, stop, step)
for i in range(0, 10, 2):
    print(i)  # 0, 2, 4, 6, 8

# Dem nguoc
for i in range(10, 0, -1):
    print(i)  # 10, 9, 8, ..., 1
```

### Duyet dictionary

```python
sinh_vien = {"ten": "An", "tuoi": 20, "lop": "CNTT"}

# Duyet key
for key in sinh_vien:
    print(key)

# Duyet key va value
for key, value in sinh_vien.items():
    print(f"{key}: {value}")
```

### enumerate() va zip()

```python
# enumerate - lay index va gia tri
fruits = ["tao", "cam", "chuoi"]
for index, fruit in enumerate(fruits, start=1):
    print(f"{index}. {fruit}")

# zip - ghep nhieu list
ten = ["An", "Binh", "Chi"]
diem = [8.5, 7.0, 9.2]
for t, d in zip(ten, diem):
    print(f"{t}: {d}")
```

## 3.3 Vong Lap While

### While co ban

```python
dem = 1
while dem <= 5:
    print(f"Lan thu {dem}")
    dem += 1
```

### While voi dieu kien phuc tap

```python
tong = 0
so = 1

while tong < 100:
    tong += so
    so += 1

print(f"Tong = {tong}, so cuoi = {so - 1}")
```

### Vong lap vo han va break

```python
while True:
    lenh = input("Nhap lenh (quit de thoat): ")
    if lenh == "quit":
        print("Tam biet!")
        break
    print(f"Ban da nhap: {lenh}")
```

## 3.4 Break, Continue, Pass

### break - thoat khoi vong lap

```python
for i in range(1, 11):
    if i == 5:
        break
    print(i)
# In: 1, 2, 3, 4
```

### continue - bo qua lan lap hien tai

```python
for i in range(1, 11):
    if i % 2 == 0:
        continue
    print(i)
# In: 1, 3, 5, 7, 9 (chi so le)
```

### pass - khong lam gi (placeholder)

```python
for i in range(10):
    if i < 5:
        pass  # Se xu ly sau
    else:
        print(i)
```

## 3.5 For/Else Va While/Else

```python
# Else duoc thuc hien khi vong lap ket thuc binh thuong (khong break)
numbers = [2, 4, 6, 8, 10]

for n in numbers:
    if n % 2 != 0:
        print(f"Tim thay so le: {n}")
        break
else:
    print("Tat ca deu la so chan")
```

## 3.6 Comprehensions

### List Comprehension

```python
# Cach thuong
squares = []
for i in range(1, 11):
    squares.append(i ** 2)

# List comprehension
squares = [i ** 2 for i in range(1, 11)]
print(squares)  # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# Voi dieu kien (filter)
even_squares = [i ** 2 for i in range(1, 11) if i % 2 == 0]
print(even_squares)  # [4, 16, 36, 64, 100]

# Voi if/else
results = ["chan" if i % 2 == 0 else "le" for i in range(1, 6)]
print(results)  # ['le', 'chan', 'le', 'chan', 'le']
```

### Dictionary Comprehension

```python
# Tao dict tu list
names = ["an", "binh", "chi"]
name_lengths = {name: len(name) for name in names}
print(name_lengths)  # {'an': 2, 'binh': 4, 'chi': 3}

# Loc dict
diem = {"An": 8, "Binh": 4, "Chi": 9, "Dung": 3}
dat = {k: v for k, v in diem.items() if v >= 5}
print(dat)  # {'An': 8, 'Chi': 9}
```

### Set Comprehension

```python
# Tap hop cac chu cai dau
words = ["apple", "avocado", "banana", "blueberry", "cherry"]
first_letters = {w[0] for w in words}
print(first_letters)  # {'a', 'b', 'c'}
```

### Generator Expression

```python
# Tuong tu list comp nhung dung () - tiet kiem bo nho
gen = (i ** 2 for i in range(1000000))
print(next(gen))  # 0
print(next(gen))  # 1
print(sum(gen))   # Tinh tong ma khong tao list
```

## 3.7 Vong Lap Long Nhau

```python
# Bang cuu chuong
for i in range(2, 10):
    print(f"\n=== Bang cuu chuong {i} ===")
    for j in range(1, 11):
        print(f"{i} x {j} = {i*j:>2}")
```

## Bai Tap

1. Viet chuong trinh nhap diem va xep loai (Xuat sac, Gioi, Kha, Trung binh, Yeu)
2. In cac so nguyen to tu 2 den 100
3. Viet chuong trinh doan so (may chon ngau nhien, nguoi dung doan)
4. In tam giac so:
   ```
   1
   1 2
   1 2 3
   1 2 3 4
   1 2 3 4 5
   ```
5. Dung list comprehension tao danh sach cac so chia het cho 3 hoac 5 trong khoang 1-100
6. Viet chuong trinh FizzBuzz: in tu 1-100, chia het cho 3 in "Fizz", cho 5 in "Buzz", cho ca 3 va 5 in "FizzBuzz"
7. Tao dictionary comprehension: key la so tu 1-20, value la binh phuong cua so do

## Tai Lieu Tham Khao

- [Python Control Flow](https://docs.python.org/3/tutorial/controlflow.html)
- [List Comprehensions](https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions)
