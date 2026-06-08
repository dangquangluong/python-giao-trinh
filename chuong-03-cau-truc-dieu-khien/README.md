# Chương 3: Cấu Trúc Điều Khiển

## 3.1 If / Elif / Else

```python
diem = 75

if diem >= 90:
    print("Xuất sắc! 🌟")
elif diem >= 80:
    print("Giỏi! 👍")
elif diem >= 65:
    print("Khá!")
elif diem >= 50:
    print("Trung bình")
else:
    print("Yếu - Cần cố gắng 💪")
```

### Toán Tử So Sánh

```python
# ==, !=, <, >, <=, >=
# and, or, not
# in, not in
# is, is not

x = 10
if 0 < x < 100:      # Chain comparison
    print("x trong khoảng 0-100")

fruits = ["apple", "banana"]
if "apple" in fruits:
    print("Có apple!")
```

### Ternary (Biểu thức điều kiện)

```python
tuoi = 20
loai = "Người lớn" if tuoi >= 18 else "Trẻ em"
print(loai)
```

## 3.2 Vòng Lặp For

```python
# Lặp qua range
for i in range(5):         # 0, 1, 2, 3, 4
    print(i)

for i in range(1, 11):    # 1 đến 10
    print(i)

for i in range(0, 20, 2): # 0, 2, 4, ..., 18 (bước 2)
    print(i)

# Lặp qua list
mon_hoc = ["Python", "Java", "SQL", "Git"]
for mon in mon_hoc:
    print(f"  - {mon}")

# enumerate (lặp với index)
for i, mon in enumerate(mon_hoc, start=1):
    print(f"  {i}. {mon}")

# Lặp qua dict
sv = {"ten": "A", "tuoi": 22, "diem": 8.5}
for key, value in sv.items():
    print(f"  {key} = {value}")

# Lặp qua string
for ch in "Python":
    print(ch, end=" ")  # P y t h o n
```

## 3.3 Vòng Lặp While

```python
# Đếm ngược
n = 10
while n > 0:
    print(f"{n}...", end=" ")
    n -= 1
print("Phóng! 🚀")

# Input validation
while True:
    tuoi = input("Nhập tuổi (1-150): ")
    if tuoi.isdigit() and 1 <= int(tuoi) <= 150:
        break
    print("Tuổi không hợp lệ, thử lại!")
```

## 3.4 Break, Continue, Else

```python
# break - thoát vòng lặp
for i in range(100):
    if i == 5:
        break
    print(i)  # 0, 1, 2, 3, 4

# continue - bỏ qua lần lặp hiện tại
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)  # 1, 3, 5, 7, 9

# for-else: else chạy khi KHÔNG có break
for i in range(2, 20):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        print(f"{i} là số nguyên tố")
```

## 3.5 List Comprehension

Cách viết gọn để tạo list:

```python
# Bình thường
binh_phuong = []
for i in range(1, 11):
    binh_phuong.append(i ** 2)

# List comprehension (ngắn gọn hơn)
binh_phuong = [i ** 2 for i in range(1, 11)]
print(binh_phuong)  # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# Với điều kiện
chan = [x for x in range(20) if x % 2 == 0]
print(chan)  # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

# Lồng nhau
matrix = [[i*3+j for j in range(3)] for i in range(3)]
# [[0,1,2], [3,4,5], [6,7,8]]

# Dict comprehension
binh_phuong_dict = {x: x**2 for x in range(1, 6)}
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# Set comprehension
unique_lengths = {len(word) for word in ["hi", "hello", "hey"]}
# {2, 3, 5}
```

## 3.6 Match-Case (Python 3.10+)

```python
command = "start"

match command:
    case "start":
        print("Bắt đầu!")
    case "stop":
        print("Dừng lại!")
    case "pause":
        print("Tạm dừng")
    case _:
        print("Lệnh không hợp lệ")

# Pattern matching với destructuring
point = (3, 4)
match point:
    case (0, 0):
        print("Gốc tọa độ")
    case (x, 0):
        print(f"Trên trục X: x={x}")
    case (0, y):
        print(f"Trên trục Y: y={y}")
    case (x, y):
        print(f"Điểm ({x}, {y})")
```

## 3.7 Bài Tập

1. FizzBuzz: in 1-100, chia hết 3→Fizz, 5→Buzz, cả hai→FizzBuzz
2. Tính giai thừa n! bằng while
3. In hình tam giác sao (input số dòng)
4. List comprehension: lọc số nguyên tố từ 1-100
5. Trò chơi đoán số (random 1-100, user nhập cho đến khi đúng)

---

📖 **Trước đó**: [Chương 2](../chuong-02-cu-phap-co-ban/README.md) | **Tiếp theo**: [Chương 4](../chuong-04-ham-va-module/README.md)
