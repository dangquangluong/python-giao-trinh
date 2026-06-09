# Lời Giải Chương 1

## Bài 1: Hello World

```python
ten = "Nguyễn Văn A"          # Thay bằng tên bạn
tuoi = 22                      # Thay bằng tuổi bạn

print(f"Xin chào! Tôi là {ten}.")      # f-string: {} = chỗ điền biến
print(f"Năm nay tôi {tuoi} tuổi.")
print("Tôi đang học Python!")
```

---

## Bài 2: Tính tuổi

```python
from datetime import datetime          # Import module datetime

nam_sinh = int(input("Nhập năm sinh: "))  # input() nhập chuỗi, int() chuyển thành số
nam_hien_tai = datetime.now().year         # Lấy năm hiện tại
tuoi = nam_hien_tai - nam_sinh             # Tính tuổi

print(f"Bạn sinh năm {nam_sinh}, năm nay {tuoi} tuổi.")
```

---

## Bài 3: Hoán đổi biến

```python
a = 5
b = 10
print(f"Trước: a = {a}, b = {b}")

# Cách 1: Python way (tuple unpacking)
a, b = b, a                    # Hoán đổi 1 dòng!

# Cách 2: Dùng biến tạm
# temp = a
# a = b
# b = temp

print(f"Sau: a = {a}, b = {b}")   # a = 10, b = 5
```

---

## Bài 4: Máy tính đơn giản

```python
a = float(input("Nhập số thứ nhất: "))    # float() cho phép nhập số thực
b = float(input("Nhập số thứ hai: "))

print(f"{a} + {b} = {a + b}")              # Cộng
print(f"{a} - {b} = {a - b}")              # Trừ
print(f"{a} * {b} = {a * b}")              # Nhân

if b != 0:                                  # Kiểm tra chia cho 0
    print(f"{a} / {b} = {a / b:.2f}")      # Chia (2 số thập phân)
    print(f"{a} % {b} = {a % b}")          # Chia lấy dư
else:
    print("Không thể chia cho 0!")          # Thông báo lỗi
```
