# Chuong 4: Ham Va Module

## 4.1 Dinh Nghia Ham

### Ham co ban

```python
def chao(ten):
    """In loi chao."""
    print(f"Xin chao, {ten}!")

chao("An")      # Xin chao, An!
chao("Binh")    # Xin chao, Binh!
```

### Ham co gia tri tra ve

```python
def tinh_dien_tich_hcn(dai, rong):
    """Tinh dien tich hinh chu nhat."""
    return dai * rong

dt = tinh_dien_tich_hcn(5, 3)
print(f"Dien tich: {dt}")  # 15
```

### Tra ve nhieu gia tri

```python
def thong_ke(numbers):
    """Tra ve min, max, trung binh."""
    return min(numbers), max(numbers), sum(numbers) / len(numbers)

nho_nhat, lon_nhat, trung_binh = thong_ke([4, 7, 2, 9, 1])
print(f"Min: {nho_nhat}, Max: {lon_nhat}, TB: {trung_binh:.1f}")
```

## 4.2 Tham So Ham

### Tham so mac dinh

```python
def chao_mung(ten, loi_chao="Xin chao"):
    print(f"{loi_chao}, {ten}!")

chao_mung("An")               # Xin chao, An!
chao_mung("An", "Hello")      # Hello, An!
```

### Keyword arguments

```python
def tao_user(ten, tuoi, email="", active=True):
    return {
        "ten": ten,
        "tuoi": tuoi,
        "email": email,
        "active": active
    }

user = tao_user("An", 25, email="an@example.com")
```

### *args va **kwargs

```python
# *args - nhan nhieu tham so vi tri
def tinh_tong(*args):
    return sum(args)

print(tinh_tong(1, 2, 3))       # 6
print(tinh_tong(1, 2, 3, 4, 5)) # 15

# **kwargs - nhan nhieu tham so ten
def in_thong_tin(**kwargs):
    for key, value in kwargs.items():
        print(f"  {key}: {value}")

in_thong_tin(ten="An", tuoi=25, lop="CNTT")
```

### Type hints

```python
def tinh_bmi(can_nang: float, chieu_cao: float) -> float:
    """Tinh chi so BMI."""
    return can_nang / (chieu_cao ** 2)

bmi = tinh_bmi(70, 1.75)
print(f"BMI: {bmi:.1f}")
```

## 4.3 Lambda Function

Lambda la ham an danh (khong ten), viet tren mot dong.

```python
# Cach thuong
def binh_phuong(x):
    return x ** 2

# Lambda tuong duong
binh_phuong = lambda x: x ** 2

print(binh_phuong(5))  # 25

# Su dung voi sorted()
students = [("An", 8.5), ("Binh", 7.0), ("Chi", 9.2)]
sorted_students = sorted(students, key=lambda s: s[1], reverse=True)
print(sorted_students)  # [('Chi', 9.2), ('An', 8.5), ('Binh', 7.0)]

# Su dung voi map(), filter()
numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x**2, numbers))
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(squares)  # [1, 4, 9, 16, 25]
print(evens)    # [2, 4]
```

## 4.4 Decorator

Decorator la ham bao ngoai mot ham khac, them chuc nang ma khong thay doi ham goc.

### Decorator co ban

```python
import time

def tinh_thoi_gian(func):
    """Decorator do thoi gian thuc thi."""
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} chay trong {end - start:.4f}s")
        return result
    return wrapper

@tinh_thoi_gian
def tinh_tong_lon():
    return sum(range(1000000))

ket_qua = tinh_tong_lon()
```

### Decorator voi tham so

```python
def repeat(n):
    """Decorator lap lai ham n lan."""
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(3)
def chao():
    print("Xin chao!")

chao()  # In "Xin chao!" 3 lan
```

### functools.wraps

```python
from functools import wraps

def my_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        """Wrapper function."""
        print("Truoc khi goi ham")
        result = func(*args, **kwargs)
        print("Sau khi goi ham")
        return result
    return wrapper

@my_decorator
def hello():
    """Ham chao."""
    print("Hello!")

print(hello.__name__)  # hello (khong mat ten goc)
print(hello.__doc__)   # Ham chao.
```

## 4.5 Scope Va Closure

### Pham vi bien

```python
x = "global"  # Bien toan cuc

def outer():
    x = "outer"  # Bien cuc bo cua outer
    
    def inner():
        x = "inner"  # Bien cuc bo cua inner
        print(f"inner: {x}")
    
    inner()
    print(f"outer: {x}")

outer()
print(f"global: {x}")
```

### Closure

```python
def tao_bo_dem(bat_dau=0):
    count = [bat_dau]
    
    def dem():
        count[0] += 1
        return count[0]
    
    return dem

counter = tao_bo_dem(10)
print(counter())  # 11
print(counter())  # 12
print(counter())  # 13
```

## 4.6 Module Va Package

### Import module

```python
# Import ca module
import math
print(math.pi)
print(math.sqrt(16))

# Import cu the
from math import pi, sqrt
print(pi)
print(sqrt(16))

# Import voi alias
import numpy as np
import pandas as pd

# Import tat ca (khong khuyen nghi)
from math import *
```

### Tao module rieng

File `utils.py`:
```python
"""Module tien ich."""

def tinh_dien_tich_tron(r):
    """Tinh dien tich hinh tron."""
    import math
    return math.pi * r ** 2

def tinh_giai_thua(n):
    """Tinh giai thua."""
    if n <= 1:
        return 1
    return n * tinh_giai_thua(n - 1)

PI = 3.14159
```

File `main.py`:
```python
from utils import tinh_dien_tich_tron, tinh_giai_thua

print(tinh_dien_tich_tron(5))
print(tinh_giai_thua(5))
```

### Package

```
my_package/
    __init__.py
    math_utils.py
    string_utils.py
    sub_package/
        __init__.py
        helper.py
```

```python
# __init__.py
from .math_utils import tinh_tong
from .string_utils import capitalize_vn

# Su dung
from my_package import tinh_tong, capitalize_vn
```

## 4.7 Module Tieu Chuan Hay Dung

```python
import os           # Thao tac he dieu hanh
import sys          # Thong tin he thong
import math         # Phep tinh toan hoc
import random       # So ngau nhien
import datetime     # Ngay gio
import json         # Xu ly JSON
import re           # Regular expression
import pathlib      # Xu ly duong dan
import collections  # Cau truc du lieu dac biet
import itertools    # Tien ich lap
```

## Bai Tap

1. Viet ham tinh giai thua (de quy va vong lap)
2. Viet ham kiem tra so nguyen to
3. Viet decorator `@log` in ten ham va tham so truoc khi goi
4. Tao module `geometry.py` voi cac ham tinh dien tich: hinh tron, hinh vuong, tam giac
5. Viet ham nhan list so va tra ve dict chua: min, max, sum, average, count
6. Viet ham su dung *args de tinh trung binh cong cac so
7. Su dung lambda va sorted() de sap xep danh sach dict theo mot key bat ky

## Tai Lieu Tham Khao

- [Python Functions](https://docs.python.org/3/tutorial/controlflow.html#defining-functions)
- [Decorators](https://docs.python.org/3/glossary.html#term-decorator)
- [Modules](https://docs.python.org/3/tutorial/modules.html)
