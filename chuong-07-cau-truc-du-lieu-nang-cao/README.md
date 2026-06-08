# Chương 7: Cấu Trúc Dữ Liệu Nâng Cao

## 7.1 Collections Module

```python
from collections import Counter, defaultdict, namedtuple, deque

# Counter - đếm tần suất
words = "python python java rust python java go".split()
counter = Counter(words)
print(counter)                    # Counter({'python': 3, 'java': 2, ...})
print(counter.most_common(2))    # [('python', 3), ('java', 2)]

# defaultdict - dict với giá trị mặc định
dd = defaultdict(list)
students = [("A", "Python"), ("B", "Java"), ("A", "SQL"), ("B", "Rust")]
for name, lang in students:
    dd[name].append(lang)
print(dict(dd))  # {'A': ['Python', 'SQL'], 'B': ['Java', 'Rust']}

# namedtuple - tuple có tên
Point = namedtuple("Point", ["x", "y"])
p = Point(3, 4)
print(f"({p.x}, {p.y}), distance = {(p.x**2 + p.y**2)**0.5:.2f}")

# deque - queue hai đầu (O(1) append/pop cả hai đầu)
dq = deque([1, 2, 3])
dq.appendleft(0)     # [0, 1, 2, 3]
dq.append(4)         # [0, 1, 2, 3, 4]
dq.popleft()         # 0
dq.rotate(2)         # Xoay phải 2 vị trí
```

## 7.2 Iterators

```python
# Iterator protocol: __iter__() + __next__()
class DemNguoc:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        self.current -= 1
        return self.current + 1

for n in DemNguoc(5):
    print(n, end=" ")  # 5 4 3 2 1
```

## 7.3 Generators

Generator = iterator lười biếng (lazy), tiết kiệm RAM:

```python
# Generator function (dùng yield)
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

for f in fibonacci(10):
    print(f, end=" ")  # 0 1 1 2 3 5 8 13 21 34

# Generator expression (giống list comprehension nhưng dùng ())
squares = (x**2 for x in range(1_000_000))  # Không tốn RAM!
print(next(squares))  # 0
print(next(squares))  # 1

# Đọc file lớn
def doc_tung_dong(filepath):
    with open(filepath) as f:
        for line in f:
            yield line.strip()

# Pipeline generators
def so_chan(numbers):
    for n in numbers:
        if n % 2 == 0:
            yield n

def binh_phuong(numbers):
    for n in numbers:
        yield n ** 2

nums = range(100)
result = binh_phuong(so_chan(nums))
print(list(result)[:10])  # [0, 4, 16, 36, 64, ...]
```

## 7.4 Dataclasses (Python 3.7+)

```python
from dataclasses import dataclass, field
from typing import List

@dataclass
class SinhVien:
    ten: str
    tuoi: int
    diem: float = 0.0
    mon_hoc: List[str] = field(default_factory=list)

    @property
    def xep_loai(self):
        if self.diem >= 8.5: return "Giỏi"
        if self.diem >= 7.0: return "Khá"
        return "TB"

# Tự động có __init__, __repr__, __eq__
sv1 = SinhVien("An", 20, 8.5, ["Python", "SQL"])
sv2 = SinhVien("Binh", 21, 7.0)
print(sv1)
print(f"{sv1.ten}: {sv1.xep_loai}")

# So sánh
sv3 = SinhVien("An", 20, 8.5, ["Python", "SQL"])
print(sv1 == sv3)  # True

# frozen=True → immutable
@dataclass(frozen=True)
class Point:
    x: float
    y: float
```

## 7.5 Type Hints

```python
from typing import List, Dict, Optional, Tuple, Union

def tinh_trung_binh(diem: List[float]) -> float:
    return sum(diem) / len(diem)

def tim_sinh_vien(
    ten: str,
    ds: List[Dict[str, Union[str, int]]]
) -> Optional[Dict]:
    for sv in ds:
        if sv.get("ten") == ten:
            return sv
    return None

# Python 3.10+: dùng | thay Union
def greet(name: str | None = None) -> str:
    if name is None:
        return "Hello, World!"
    return f"Hello, {name}!"
```

## 7.6 Itertools

```python
import itertools

# count - đếm vô hạn
for i in itertools.islice(itertools.count(1), 5):
    print(i, end=" ")  # 1 2 3 4 5

# cycle - lặp vòng
colors = itertools.cycle(["red", "green", "blue"])
for _ in range(6):
    print(next(colors), end=" ")

# chain - nối iterators
a = [1, 2, 3]
b = [4, 5, 6]
print(list(itertools.chain(a, b)))  # [1,2,3,4,5,6]

# product - tích Descartes
print(list(itertools.product("AB", "12")))
# [('A','1'),('A','2'),('B','1'),('B','2')]

# combinations, permutations
print(list(itertools.combinations("ABCD", 2)))
print(list(itertools.permutations("ABC", 2)))

# groupby
data = [("A", 8), ("B", 7), ("A", 9), ("B", 6)]
data.sort(key=lambda x: x[0])
for key, group in itertools.groupby(data, key=lambda x: x[0]):
    print(f"{key}: {list(group)}")
```

## 7.7 Bài Tập

1. Dùng Counter đếm tần suất ký tự trong chuỗi
2. Viết generator `prime_numbers()` sinh số nguyên tố vô hạn
3. Tạo dataclass `Order` với items, tính tổng tiền
4. Pipeline: đọc file CSV → filter → transform → output (dùng generators)

---

📖 **Trước đó**: [Chương 6](../chuong-06-xu-ly-file-exception/README.md) | **Tiếp theo**: [Chương 8](../chuong-08-thu-vien-pho-bien/README.md)
