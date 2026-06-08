# Chương 7: Cấu Trúc Dữ Liệu Nâng Cao

## 7.1 Collections Module

```python
from collections import Counter, defaultdict, namedtuple, deque  # Import từ module collections

# Counter - đếm tần suất phần tử
words = "python python java rust python java go".split()  # .split() tách chuỗi thành list
counter = Counter(words)                     # Counter đếm số lần xuất hiện mỗi phần tử
print(counter)                    # Counter({'python': 3, 'java': 2, ...})
print(counter.most_common(2))    # [('python', 3), ('java', 2)] - 2 phần tử phổ biến nhất

# defaultdict - dict với giá trị mặc định (tự tạo nếu key chưa có)
dd = defaultdict(list)                       # Giá trị mặc định = list rỗng []
students = [("A", "Python"), ("B", "Java"), ("A", "SQL"), ("B", "Rust")]  # List tuple
for name, lang in students:                  # Lặp qua, unpack tuple
    dd[name].append(lang)                    # Tự tạo key+list nếu chưa có, rồi append
print(dict(dd))  # {'A': ['Python', 'SQL'], 'B': ['Java', 'Rust']}

# namedtuple - tuple có tên cho từng trường (truy cập bằng tên thay vì index)
Point = namedtuple("Point", ["x", "y"])      # Tạo kiểu Point với 2 trường x, y
p = Point(3, 4)                              # Tạo instance
print(f"({p.x}, {p.y}), distance = {(p.x**2 + p.y**2)**0.5:.2f}")  # Truy cập bằng tên

# deque - queue hai đầu (O(1) append/pop cả hai đầu, nhanh hơn list)
dq = deque([1, 2, 3])                       # Tạo deque từ list
dq.appendleft(0)     # [0, 1, 2, 3]         # Thêm vào đầu (list không có method này)
dq.append(4)         # [0, 1, 2, 3, 4]      # Thêm vào cuối
dq.popleft()         # 0                    # Lấy từ đầu ra (O(1), list là O(n))
dq.rotate(2)         # Xoay phải 2 vị trí   # Phần tử cuối chuyển lên đầu
```

## 7.2 Iterators

```python
# Iterator protocol: __iter__() + __next__()
class DemNguoc:                              # Class iterator tự tạo
    def __init__(self, start):               # Constructor nhận số bắt đầu
        self.current = start                 # Lưu giá trị hiện tại

    def __iter__(self):                      # __iter__ trả về iterator (bắt buộc cho for..in)
        return self                          # Trả về chính nó

    def __next__(self):                      # __next__ trả về giá trị tiếp theo
        if self.current <= 0:                # Kiểm tra điều kiện dừng
            raise StopIteration              # Ném StopIteration để báo hết phần tử
        self.current -= 1                    # Giảm current
        return self.current + 1              # Trả về giá trị trước khi giảm

for n in DemNguoc(5):                        # for tự gọi __iter__() rồi __next__() lặp lại
    print(n, end=" ")  # 5 4 3 2 1          # In từng giá trị cho đến StopIteration
```

## 7.3 Generators

Generator = iterator lười biếng (lazy), tiết kiệm RAM:

```python
# Generator function (dùng yield thay return)
def fibonacci(n):                            # Hàm generator (có yield = trở thành generator)
    a, b = 0, 1                              # Khởi tạo 2 số Fibonacci đầu
    for _ in range(n):                       # Lặp n lần
        yield a                              # yield trả về a rồi "tạm dừng" hàm (nhớ trạng thái)
        a, b = b, a + b                      # Tính số tiếp khi được gọi lại

for f in fibonacci(10):                      # Lặp qua generator (tự gọi next())
    print(f, end=" ")  # 0 1 1 2 3 5 8 13 21 34

# Generator expression (giống list comprehension nhưng dùng () - lazy)
squares = (x**2 for x in range(1_000_000))  # Không tốn RAM! Chỉ tính khi cần
print(next(squares))  # 0                   # next() lấy giá trị tiếp theo từ generator
print(next(squares))  # 1                   # Tiếp tục từ chỗ dừng

# Đọc file lớn (tiết kiệm RAM)
def doc_tung_dong(filepath):                 # Generator đọc file từng dòng
    with open(filepath) as f:                # Mở file
        for line in f:                       # Lặp qua từng dòng (không load hết vào RAM)
            yield line.strip()               # yield từng dòng đã strip

# Pipeline generators - nối nhiều generator
def so_chan(numbers):                        # Generator lọc số chẵn
    for n in numbers:
        if n % 2 == 0:                       # Chỉ yield số chẵn
            yield n

def binh_phuong(numbers):                    # Generator tính bình phương
    for n in numbers:
        yield n ** 2                         # yield n^2

nums = range(100)                            # range cũng là lazy (không tạo list)
result = binh_phuong(so_chan(nums))          # Nối pipeline: range -> lọc chẵn -> bình phương
print(list(result)[:10])  # [0, 4, 16, 36, 64, ...]  # Chỉ tính khi cần
```

## 7.4 Dataclasses (Python 3.7+)

```python
from dataclasses import dataclass, field     # Import dataclass tools
from typing import List                      # Type hint cho List

@dataclass                                   # Decorator tự tạo __init__, __repr__, __eq__
class SinhVien:                              # Định nghĩa class (ngắn gọn hơn viết __init__ tay)
    ten: str                                 # Thuộc tính + type hint (tự thêm vào __init__)
    tuoi: int                                # Số nguyên
    diem: float = 0.0                        # Giá trị mặc định = 0.0
    mon_hoc: List[str] = field(default_factory=list)  # Mutable default phải dùng field()

    @property                                # Biến method thành thuộc tính (gọi không cần ())
    def xep_loai(self):
        if self.diem >= 8.5: return "Giỏi"
        if self.diem >= 7.0: return "Khá"
        return "TB"

# Tự động có __init__, __repr__, __eq__
sv1 = SinhVien("An", 20, 8.5, ["Python", "SQL"])  # Tự tạo __init__ từ các field
sv2 = SinhVien("Binh", 21, 7.0)             # diem=0.0, mon_hoc=[] (mặc định)
print(sv1)                                   # Tự tạo __repr__ đẹp
print(f"{sv1.ten}: {sv1.xep_loai}")          # Truy cập property

# So sánh (tự tạo __eq__)
sv3 = SinhVien("An", 20, 8.5, ["Python", "SQL"])
print(sv1 == sv3)  # True                   # __eq__ so sánh từng field

# frozen=True -> immutable (không thể sửa sau khi tạo)
@dataclass(frozen=True)                      # frozen=True: object bất biến (như tuple)
class Point:
    x: float
    y: float
```

## 7.5 Type Hints

```python
from typing import List, Dict, Optional, Tuple, Union  # Import các type hint

def tinh_trung_binh(diem: List[float]) -> float:  # Tham số: List[float], trả về: float
    return sum(diem) / len(diem)

def tim_sinh_vien(
    ten: str,                                # Tham số kiểu str
    ds: List[Dict[str, Union[str, int]]]     # List chứa Dict (value là str hoặc int)
) -> Optional[Dict]:                         # Trả về Dict hoặc None (Optional = có thể None)
    for sv in ds:
        if sv.get("ten") == ten:
            return sv
    return None                              # Trả về None nếu không tìm thấy

# Python 3.10+: dùng | thay Union (ngắn gọn hơn)
def greet(name: str | None = None) -> str:   # str | None tương đương Optional[str]
    if name is None:
        return "Hello, World!"
    return f"Hello, {name}!"
```

## 7.6 Itertools

```python
import itertools                             # Module chứa công cụ iterator nâng cao

# count - đếm vô hạn
for i in itertools.islice(itertools.count(1), 5):  # count(1) đếm từ 1 vô hạn, islice lấy 5 phần tử
    print(i, end=" ")  # 1 2 3 4 5

# cycle - lặp vòng vô hạn
colors = itertools.cycle(["red", "green", "blue"])  # Lặp vòng: red, green, blue, red, ...
for _ in range(6):                           # Lấy 6 phần tử
    print(next(colors), end=" ")             # next() lấy giá trị tiếp theo

# chain - nối nhiều iterators thành 1
a = [1, 2, 3]
b = [4, 5, 6]
print(list(itertools.chain(a, b)))  # [1,2,3,4,5,6]  # Nối 2 list

# product - tích Descartes (mọi tổ hợp)
print(list(itertools.product("AB", "12")))   # Tất cả cặp: A1, A2, B1, B2
# [('A','1'),('A','2'),('B','1'),('B','2')]

# combinations, permutations
print(list(itertools.combinations("ABCD", 2)))  # Tổ hợp chập 2 (không quan tâm thứ tự)
print(list(itertools.permutations("ABC", 2)))   # Hoán vị chập 2 (quan tâm thứ tự)

# groupby - nhóm phần tử liên tiếp có cùng key
data = [("A", 8), ("B", 7), ("A", 9), ("B", 6)]
data.sort(key=lambda x: x[0])               # PHẢI sort trước khi groupby
for key, group in itertools.groupby(data, key=lambda x: x[0]):  # Nhóm theo phần tử [0]
    print(f"{key}: {list(group)}")           # In từng nhóm
```

## 7.7 Bài Tập

1. Dùng Counter đếm tần suất ký tự trong chuỗi
2. Viết generator `prime_numbers()` sinh số nguyên tố vô hạn
3. Tạo dataclass `Order` với items, tính tổng tiền
4. Pipeline: đọc file CSV → filter → transform → output (dùng generators)

---

📖 **Trước đó**: [Chương 6](../chuong-06-xu-ly-file-exception/README.md) | **Tiếp theo**: [Chương 8](../chuong-08-thu-vien-pho-bien/README.md)
