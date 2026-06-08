# Chương 4: Hàm, Lambda & Module

## 4.1 Hàm (Functions)

```python
# Khai báo hàm
def chao(ten):                     # def = từ khóa định nghĩa hàm, ten = tham số (parameter)
    """Hàm chào hỏi"""            # docstring: mô tả hàm (nằm ngay sau def)
    print(f"Xin chào, {ten}!")    # Thân hàm: code chạy khi gọi hàm

chao("Python")                    # Gọi hàm, truyền "Python" vào tham số ten

# Hàm có giá trị trả về
def cong(a, b):                   # Hàm nhận 2 tham số a và b
    return a + b                  # return trả về kết quả (thoát hàm ngay)

ket_qua = cong(3, 5)  # 8        # Gọi hàm và lưu giá trị trả về vào biến
```

### Tham Số Mặc Định

```python
def chao_hoi(ten, loi_chao="Xin chào"):  # loi_chao có giá trị mặc định "Xin chào"
    print(f"{loi_chao}, {ten}!")           # Sử dụng cả hai tham số

chao_hoi("A")            # Xin chào, A! - dùng giá trị mặc định cho loi_chao
chao_hoi("B", "Hello")   # Hello, B! - ghi đè giá trị mặc định
```

### *args và **kwargs

```python
def tinh_tong(*args):              # *args = nhận số lượng tham số không giới hạn thành tuple
    """Nhận nhiều tham số không giới hạn"""  # Docstring
    return sum(args)               # sum() tính tổng tuple args

print(tinh_tong(1, 2, 3, 4, 5))  # 15 - truyền bao nhiêu tham số cũng được

def tao_profile(**kwargs):         # **kwargs = nhận keyword arguments thành dict
    """Nhận keyword arguments"""   # Docstring
    for key, value in kwargs.items():  # Lặp qua dict kwargs
        print(f"  {key}: {value}")     # In từng cặp key: value

tao_profile(ten="A", tuoi=25, nghe="Dev")  # Truyền keyword arguments
```

### Return Nhiều Giá Trị

```python
def thong_ke(numbers):             # Hàm nhận list số
    return min(numbers), max(numbers), sum(numbers) / len(numbers)  # Trả về tuple 3 giá trị

mn, mx, avg = thong_ke([85, 90, 78, 92, 88])  # Unpack tuple thành 3 biến
print(f"Min: {mn}, Max: {mx}, TB: {avg:.1f}")  # In kết quả
```

## 4.2 Lambda (Hàm Ẩn Danh)

```python
# Lambda - hàm 1 dòng (không cần def và tên)
binh_phuong = lambda x: x ** 2    # lambda tham_số: biểu_thức_trả_về
print(binh_phuong(5))  # 25       # Gọi lambda giống hàm bình thường

cong = lambda a, b: a + b         # Lambda 2 tham số
print(cong(3, 4))  # 7            # Gọi lambda

# Dùng với sorted, map, filter
students = [("A", 8.5), ("B", 7.0), ("C", 9.2)]  # List tuple (tên, điểm)
students.sort(key=lambda s: s[1], reverse=True)     # sort theo s[1]=điểm, giảm dần
print(students)  # Sắp theo điểm giảm dần

numbers = [1, 2, 3, 4, 5, 6]                       # List số
chan = list(filter(lambda x: x % 2 == 0, numbers))  # filter() lọc: giữ phần tử thỏa điều kiện
gap_doi = list(map(lambda x: x * 2, numbers))      # map() áp dụng hàm lên từng phần tử
```

## 4.3 Decorator

```python
import time                        # Module đo thời gian

def tinh_thoi_gian(func):          # Decorator: hàm nhận hàm khác làm tham số
    """Decorator đo thời gian chạy hàm"""  # Docstring
    def wrapper(*args, **kwargs):  # Hàm wrapper bọc hàm gốc, nhận mọi tham số
        start = time.time()        # Ghi thời điểm bắt đầu
        result = func(*args, **kwargs)  # Gọi hàm gốc
        end = time.time()          # Ghi thời điểm kết thúc
        print(f"{func.__name__} chạy trong {end-start:.4f}s")  # In thời gian chạy
        return result              # Trả về kết quả hàm gốc
    return wrapper                 # Trả về wrapper (thay thế hàm gốc)

@tinh_thoi_gian                    # @ = áp dụng decorator lên hàm bên dưới
def tinh_tong_lon():               # Hàm này sẽ được bọc bởi tinh_thoi_gian
    return sum(range(1_000_000))   # Tính tổng 0 đến 999999

tinh_tong_lon()                    # Gọi hàm (thực ra gọi wrapper, tự đo thời gian)
```

### Decorator Có Tham Số

```python
def repeat(n):                     # Hàm tạo decorator với tham số n
    def decorator(func):           # Decorator thực sự (nhận hàm)
        def wrapper(*args, **kwargs):  # Wrapper bọc hàm gốc
            for _ in range(n):     # Lặp n lần (_ = biến không dùng)
                result = func(*args, **kwargs)  # Gọi hàm gốc n lần
            return result          # Trả về kết quả lần cuối
        return wrapper             # Trả về wrapper
    return decorator               # Trả về decorator

@repeat(3)                         # Áp dụng decorator repeat với n=3
def chao():                        # Hàm sẽ được gọi 3 lần
    print("Hello!")

chao()  # In 3 lần                # Gọi 1 lần nhưng in "Hello!" 3 lần
```

## 4.4 Closure

```python
def tao_bo_dem(bat_dau=0):         # Hàm ngoài tạo closure
    count = [bat_dau]              # Dùng list (mutable) để lưu trạng thái trong closure

    def dem():                     # Hàm bên trong "nhớ" biến count từ hàm ngoài
        count[0] += 1              # Tăng giá trị (list mutable nên sửa được trong closure)
        return count[0]            # Trả về giá trị sau khi tăng

    return dem                     # Trả về hàm dem (closure)

counter = tao_bo_dem(10)           # Tạo closure, count bắt đầu từ [10]
print(counter())  # 11            # Gọi lần 1: count[0] = 11
print(counter())  # 12            # Gọi lần 2: count[0] = 12 (nhớ trạng thái)
print(counter())  # 13            # Gọi lần 3: count[0] = 13
```

## 4.5 Module & Package

### Import

```python
# Import module
import math                        # Import toàn bộ module math
print(math.pi)                     # Truy cập biến pi qua tên module
print(math.sqrt(16))               # Gọi hàm sqrt (căn bậc 2) qua module

# Import cụ thể
from math import pi, sqrt          # Chỉ import pi và sqrt (dùng trực tiếp, không cần math.)
print(pi)                          # Dùng trực tiếp không cần tiền tố math.

# Import với alias
import numpy as np                 # Đặt tên ngắn (alias) cho module
from datetime import datetime as dt  # Alias cho class/hàm cụ thể

# Import tất cả (không khuyến nghị)
from math import *                 # Import mọi thứ - dễ xung đột tên, khó debug
```

### Tạo Module Riêng

```python
# File: mymath.py
def cong(a, b):                    # Định nghĩa hàm trong module riêng
    return a + b

def nhan(a, b):                    # Hàm khác trong cùng module
    return a * b

PI = 3.14159                       # Hằng số trong module

# File: main.py
import mymath                      # Import module tự tạo (file mymath.py cùng thư mục)
print(mymath.cong(3, 5))           # Gọi hàm từ module
print(mymath.PI)                   # Truy cập hằng số từ module
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
from .math_utils import cong, tru      # . = import từ package hiện tại (relative import)
from .string_utils import viet_hoa     # Định nghĩa những gì export khi import package
```

## 4.6 Built-in Functions Hữu Ích

```python
# map - áp dụng hàm lên mỗi phần tử
nums = [1, 2, 3, 4, 5]                       # List số
squared = list(map(lambda x: x**2, nums))    # map(hàm, iterable) trả về iterator

# filter - lọc phần tử thỏa điều kiện
evens = list(filter(lambda x: x % 2 == 0, nums))  # Giữ phần tử mà hàm trả về True

# zip - ghép cặp phần tử từ nhiều list
names = ["A", "B", "C"]                      # List tên
scores = [85, 90, 78]                        # List điểm
pairs = list(zip(names, scores))  # [("A",85), ("B",90), ("C",78)] - ghép theo vị trí

# sorted - sắp xếp (trả về list mới, không thay đổi gốc)
sorted_desc = sorted(nums, reverse=True)     # Sắp xếp giảm dần
sorted_by_len = sorted(["Python", "Go", "Rust"], key=len)  # Sắp theo độ dài chuỗi

# any, all
print(any([False, True, False]))  # True  - any: True nếu có ít nhất 1 True
print(all([True, True, True]))    # True  - all: True nếu tất cả đều True

# enumerate - lặp kèm index
for i, val in enumerate(["a", "b", "c"]):  # enumerate trả về (index, value)
    print(f"{i}: {val}")                    # In index và giá trị
```

## 4.7 Bài Tập

1. Viết decorator `@cache` lưu kết quả hàm (memoization)
2. Hàm `flatten(nested_list)` biến list lồng thành phẳng
3. Tạo module `string_utils.py` với hàm: viet_hoa, dem_tu, dao_nguoc
4. Viết hàm đệ quy tính Fibonacci

---

📖 **Trước đó**: [Chương 3](../chuong-03-cau-truc-dieu-khien/README.md) | **Tiếp theo**: [Chương 5](../chuong-05-oop/README.md)
