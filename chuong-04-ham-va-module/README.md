# Chương 4: Hàm, Lambda & Module

## 4.1 Hàm (Functions)

```python
# Khai báo hàm
def chao(ten):
    """Hàm chào hỏi"""  # docstring
    print(f"Xin chào, {ten}!")

chao("Python")

# Hàm có giá trị trả về
def cong(a, b):
    return a + b

ket_qua = cong(3, 5)  # 8
```

### Tham Số Mặc Định

```python
def chao_hoi(ten, loi_chao="Xin chào"):
    print(f"{loi_chao}, {ten}!")

chao_hoi("A")            # Xin chào, A!
chao_hoi("B", "Hello")   # Hello, B!
```

### *args và **kwargs

```python
def tinh_tong(*args):
    """Nhận nhiều tham số không giới hạn"""
    return sum(args)

print(tinh_tong(1, 2, 3, 4, 5))  # 15

def tao_profile(**kwargs):
    """Nhận keyword arguments"""
    for key, value in kwargs.items():
        print(f"  {key}: {value}")

tao_profile(ten="A", tuoi=25, nghe="Dev")
```

### Return Nhiều Giá Trị

```python
def thong_ke(numbers):
    return min(numbers), max(numbers), sum(numbers) / len(numbers)

mn, mx, avg = thong_ke([85, 90, 78, 92, 88])
print(f"Min: {mn}, Max: {mx}, TB: {avg:.1f}")
```

## 4.2 Lambda (Hàm Ẩn Danh)

```python
# Lambda - hàm 1 dòng
binh_phuong = lambda x: x ** 2
print(binh_phuong(5))  # 25

cong = lambda a, b: a + b
print(cong(3, 4))  # 7

# Dùng với sorted, map, filter
students = [("A", 8.5), ("B", 7.0), ("C", 9.2)]
students.sort(key=lambda s: s[1], reverse=True)
print(students)  # Sắp theo điểm giảm dần

numbers = [1, 2, 3, 4, 5, 6]
chan = list(filter(lambda x: x % 2 == 0, numbers))
gap_doi = list(map(lambda x: x * 2, numbers))
```

## 4.3 Decorator

```python
import time

def tinh_thoi_gian(func):
    """Decorator đo thời gian chạy hàm"""
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} chạy trong {end-start:.4f}s")
        return result
    return wrapper

@tinh_thoi_gian
def tinh_tong_lon():
    return sum(range(1_000_000))

tinh_tong_lon()
```

### Decorator Có Tham Số

```python
def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(3)
def chao():
    print("Hello!")

chao()  # In 3 lần
```

## 4.4 Closure

```python
def tao_bo_dem(bat_dau=0):
    count = [bat_dau]  # Dùng list để mutable trong closure

    def dem():
        count[0] += 1
        return count[0]

    return dem

counter = tao_bo_dem(10)
print(counter())  # 11
print(counter())  # 12
print(counter())  # 13
```

## 4.5 Module & Package

### Import

```python
# Import module
import math
print(math.pi)
print(math.sqrt(16))

# Import cụ thể
from math import pi, sqrt
print(pi)

# Import với alias
import numpy as np
from datetime import datetime as dt

# Import tất cả (không khuyến nghị)
from math import *
```

### Tạo Module Riêng

```python
# File: mymath.py
def cong(a, b):
    return a + b

def nhan(a, b):
    return a * b

PI = 3.14159

# File: main.py
import mymath
print(mymath.cong(3, 5))
print(mymath.PI)
```

### Package

```
my_package/
├── __init__.py
├── math_utils.py
└── string_utils.py
```

```python
# __init__.py
from .math_utils import cong, tru
from .string_utils import viet_hoa
```

## 4.6 Built-in Functions Hữu Ích

```python
# map - áp dụng hàm lên mỗi phần tử
nums = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, nums))

# filter - lọc phần tử
evens = list(filter(lambda x: x % 2 == 0, nums))

# zip - ghép cặp
names = ["A", "B", "C"]
scores = [85, 90, 78]
pairs = list(zip(names, scores))  # [("A",85), ("B",90), ("C",78)]

# sorted
sorted_desc = sorted(nums, reverse=True)
sorted_by_len = sorted(["Python", "Go", "Rust"], key=len)

# any, all
print(any([False, True, False]))  # True
print(all([True, True, True]))    # True

# enumerate
for i, val in enumerate(["a", "b", "c"]):
    print(f"{i}: {val}")
```

## 4.7 Bài Tập

1. Viết decorator `@cache` lưu kết quả hàm (memoization)
2. Hàm `flatten(nested_list)` biến list lồng thành phẳng
3. Tạo module `string_utils.py` với hàm: viet_hoa, dem_tu, dao_nguoc
4. Viết hàm đệ quy tính Fibonacci

---

📖 **Trước đó**: [Chương 3](../chuong-03-cau-truc-dieu-khien/README.md) | **Tiếp theo**: [Chương 5](../chuong-05-oop/README.md)
