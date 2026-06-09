# Lời Giải Chương 3

## Bài 1: FizzBuzz

```python
for i in range(1, 101):                         # 1 đến 100
    if i % 15 == 0:                             # Chia hết 3 VÀ 5 (15 = 3×5)
        print("FizzBuzz")
    elif i % 3 == 0:                            # Chia hết 3
        print("Fizz")
    elif i % 5 == 0:                            # Chia hết 5
        print("Buzz")
    else:                                        # Còn lại
        print(i)
```

---

## Bài 2: Tam giác sao

```python
n = int(input("Nhập số dòng: "))                # Nhập số dòng

for i in range(1, n + 1):                       # i = 1, 2, ..., n
    spaces = " " * (n - i)                      # Số dấu cách (giảm dần)
    stars = "*" * (2 * i - 1)                   # Số sao (1, 3, 5, 7...)
    print(spaces + stars)                        # In: dấu cách + sao
```

---

## Bài 3: Số nguyên tố (list comprehension)

```python
# Hàm kiểm tra nguyên tố
def la_nguyen_to(n):
    if n < 2:                                    # 0, 1 không phải nguyên tố
        return False
    for i in range(2, int(n**0.5) + 1):         # Kiểm tra từ 2 đến sqrt(n)
        if n % i == 0:                           # Nếu chia hết → không phải
            return False
    return True                                  # Không chia hết cho ai → nguyên tố

# List comprehension
nguyen_to = [n for n in range(1, 101) if la_nguyen_to(n)]
print(f"Số nguyên tố từ 1-100 ({len(nguyen_to)} số):")
print(nguyen_to)
```

---

## Bài 4: Đoán số

```python
import random                                   # Import module random

so_bi_mat = random.randint(1, 100)              # Random số 1-100
so_lan = 0                                       # Đếm số lần đoán

print("Tôi đang nghĩ 1 số từ 1-100. Hãy đoán!")

while True:                                     # Lặp đến khi đúng
    doan = int(input("Đoán: "))                 # Nhập số đoán
    so_lan += 1                                  # Tăng đếm

    if doan < so_bi_mat:                        # Đoán nhỏ hơn
        print("📈 Lớn hơn!")
    elif doan > so_bi_mat:                      # Đoán lớn hơn
        print("📉 Nhỏ hơn!")
    else:                                        # Đoán đúng!
        print(f"🎉 Đúng rồi! Số là {so_bi_mat}. Bạn đoán {so_lan} lần.")
        break                                    # Thoát vòng lặp
```

---

## Bài 5: Giai thừa

```python
n = int(input("Nhập n: "))                      # Nhập số
ket_qua = 1                                     # Bắt đầu từ 1
i = 1                                            # Biến đếm

while i <= n:                                   # Lặp từ 1 đến n
    ket_qua *= i                                # Nhân thêm i (1×2×3×...×n)
    i += 1                                       # Tăng i

print(f"{n}! = {ket_qua}")                      # In kết quả
# VD: 5! = 120
```
