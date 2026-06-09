# Lời Giải Chương 4

## Bài 1: Decorator đo thời gian

```python
import time                                  # Import module time

def timer(func):                             # Decorator nhận hàm làm tham số
    def wrapper(*args, **kwargs):            # wrapper bọc hàm gốc
        start = time.time()                  # Ghi thời gian bắt đầu
        result = func(*args, **kwargs)       # Gọi hàm gốc
        elapsed = time.time() - start        # Tính thời gian chạy
        print(f"  {func.__name__}: {elapsed:.4f}s")  # In tên hàm + thời gian
        return result                        # Trả kết quả hàm gốc
    return wrapper                           # Trả wrapper

@timer                                       # Áp dụng decorator
def tinh_tong(n):                           # Hàm được đo thời gian
    return sum(range(n))                    # Tính tổng 0+1+...+(n-1)

print(tinh_tong(1_000_000))                 # Gọi → in thời gian + kết quả
```

## Bài 2: Fibonacci + Memoization

```python
def fib(n, memo={}):                         # memo = cache kết quả đã tính
    if n <= 1:                               # Base case: fib(0)=0, fib(1)=1
        return n
    if n not in memo:                        # Chưa tính → tính và lưu
        memo[n] = fib(n-1) + fib(n-2)       # Đệ quy
    return memo[n]                           # Trả từ cache

for i in range(1, 11):                       # Test fib(1) đến fib(10)
    print(f"  fib({i}) = {fib(i)}")
```

## Bài 3: *args trung bình

```python
def trung_binh(*args):                       # *args = nhận bao nhiêu số cũng được
    if not args:                             # Nếu không có tham số
        return 0                             # Trả 0 tránh chia cho 0
    return sum(args) / len(args)             # sum / số lượng

print(trung_binh(5, 10, 15))                # 10.0
print(trung_binh(8.5, 7.0, 9.2, 6.5))      # 7.8
print(trung_binh())                          # 0
```

## Bài 4: Closure - Bộ đếm

```python
def tao_bo_dem(start=0):                     # Hàm tạo bộ đếm
    count = [start]                          # Dùng list để mutable trong closure

    def dem():                               # Hàm bên trong (closure)
        count[0] += 1                        # Tăng giá trị (sửa list item)
        return count[0]                      # Trả giá trị mới

    return dem                               # Trả hàm dem

counter = tao_bo_dem(10)                     # Bắt đầu từ 10
print(counter())                             # 11
print(counter())                             # 12
print(counter())                             # 13
```
