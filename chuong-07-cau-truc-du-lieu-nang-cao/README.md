# Chuong 7: Cau Truc Du Lieu Nang Cao

## 7.1 Module Collections

### namedtuple

```python
from collections import namedtuple

# Tao kieu namedtuple
Point = namedtuple("Point", ["x", "y"])
SinhVien = namedtuple("SinhVien", "ten mssv diem")

p = Point(3, 4)
print(p.x, p.y)  # 3 4

sv = SinhVien("An", "SV001", 8.5)
print(sv.ten)    # An
print(sv[2])     # 8.5
```

### defaultdict

```python
from collections import defaultdict

# Dict voi gia tri mac dinh
word_count = defaultdict(int)
text = "tao cam tao chuoi cam tao"
for word in text.split():
    word_count[word] += 1
print(dict(word_count))  # {'tao': 3, 'cam': 2, 'chuoi': 1}

# List mac dinh
groups = defaultdict(list)
students = [("A", "CNTT"), ("B", "KTPM"), ("C", "CNTT")]
for name, dept in students:
    groups[dept].append(name)
print(dict(groups))
```

### Counter

```python
from collections import Counter

# Dem phan tu
words = ["python", "java", "python", "go", "python", "java"]
counter = Counter(words)
print(counter)                    # Counter({'python': 3, 'java': 2, 'go': 1})
print(counter.most_common(2))     # [('python', 3), ('java', 2)]

# Dem ky tu
c = Counter("hello world")
print(c)  # Counter({'l': 3, 'o': 2, ...})
```

### deque

```python
from collections import deque

# Queue 2 dau
dq = deque([1, 2, 3])
dq.append(4)        # Them phai
dq.appendleft(0)    # Them trai
dq.pop()            # Xoa phai
dq.popleft()        # Xoa trai
print(dq)           # deque([1, 2, 3])

# Gioi han kich thuoc
last_5 = deque(maxlen=5)
for i in range(10):
    last_5.append(i)
print(last_5)  # deque([5, 6, 7, 8, 9])
```

### OrderedDict

```python
from collections import OrderedDict

# Dict giu thu tu chen (Python 3.7+ dict da giu thu tu)
od = OrderedDict()
od["c"] = 3
od["a"] = 1
od["b"] = 2
od.move_to_end("c")  # Chuyen "c" ve cuoi
print(od)
```

## 7.2 Iterator

### Iterator protocol

```python
# Moi iterable co __iter__() tra ve iterator
# Moi iterator co __next__() tra ve phan tu tiep theo

my_list = [1, 2, 3]
iterator = iter(my_list)
print(next(iterator))  # 1
print(next(iterator))  # 2
print(next(iterator))  # 3
# next(iterator) -> StopIteration
```

### Tao iterator tu class

```python
class CountDown:
    """Iterator dem nguoc."""
    
    def __init__(self, start):
        self.current = start
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        self.current -= 1
        return self.current + 1

for num in CountDown(5):
    print(num)  # 5, 4, 3, 2, 1
```

## 7.3 Generator

### Generator function

```python
def fibonacci(n):
    """Generator sinh n so Fibonacci."""
    a, b = 0, 1
    count = 0
    while count < n:
        yield a
        a, b = b, a + b
        count += 1

# Su dung
for num in fibonacci(10):
    print(num, end=" ")
# 0 1 1 2 3 5 8 13 21 34
```

### Generator khong gioi han

```python
def so_nguyen_to():
    """Generator sinh so nguyen to vo han."""
    num = 2
    while True:
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            yield num
        num += 1

# Lay 10 so nguyen to dau tien
from itertools import islice
primes = list(islice(so_nguyen_to(), 10))
print(primes)  # [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
```

### yield from

```python
def flatten(nested_list):
    """Lam phang list long nhau."""
    for item in nested_list:
        if isinstance(item, list):
            yield from flatten(item)
        else:
            yield item

nested = [1, [2, 3], [4, [5, 6]], 7]
print(list(flatten(nested)))  # [1, 2, 3, 4, 5, 6, 7]
```

## 7.4 Module Itertools

```python
import itertools

# count - dem vo han
for i in itertools.count(start=1, step=2):
    if i > 10:
        break
    print(i, end=" ")  # 1 3 5 7 9

# cycle - lap vo han
colors = itertools.cycle(["do", "xanh", "vang"])
for _, c in zip(range(6), colors):
    print(c, end=" ")  # do xanh vang do xanh vang

# chain - noi nhieu iterable
a = [1, 2, 3]
b = [4, 5, 6]
print(list(itertools.chain(a, b)))  # [1, 2, 3, 4, 5, 6]

# product - tich Descartes
for item in itertools.product("AB", [1, 2]):
    print(item)  # ('A', 1), ('A', 2), ('B', 1), ('B', 2)

# combinations
print(list(itertools.combinations("ABC", 2)))
# [('A', 'B'), ('A', 'C'), ('B', 'C')]

# permutations
print(list(itertools.permutations("ABC", 2)))
# [('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'C'), ('C', 'A'), ('C', 'B')]

# groupby
data = [("An", "CNTT"), ("Binh", "KTPM"), ("Chi", "CNTT")]
data.sort(key=lambda x: x[1])
for key, group in itertools.groupby(data, key=lambda x: x[1]):
    print(f"{key}: {list(group)}")
```

## 7.5 Dataclass

### Dataclass co ban

```python
from dataclasses import dataclass, field

@dataclass
class SinhVien:
    ten: str
    mssv: str
    diem: float = 0.0
    
sv = SinhVien("An", "SV001", 8.5)
print(sv)  # SinhVien(ten='An', mssv='SV001', diem=8.5)
```

### Dataclass nang cao

```python
from dataclasses import dataclass, field
from typing import List

@dataclass(order=True)
class Product:
    """San pham voi sap xep theo gia."""
    sort_index: float = field(init=False, repr=False)
    ten: str
    gia: float
    so_luong: int = 0
    tags: List[str] = field(default_factory=list)
    
    def __post_init__(self):
        self.sort_index = self.gia
    
    @property
    def tong_gia_tri(self):
        return self.gia * self.so_luong

p1 = Product("Laptop", 15000000, 10)
p2 = Product("Phone", 8000000, 20)
p3 = Product("Tablet", 12000000, 5)

products = sorted([p1, p2, p3])  # Sap xep theo gia
for p in products:
    print(f"  {p.ten}: {p.gia:,.0f} VND x {p.so_luong}")
```

### Frozen dataclass (immutable)

```python
@dataclass(frozen=True)
class Point:
    x: float
    y: float

p = Point(3, 4)
# p.x = 5  # FrozenInstanceError
print(p)
```

## 7.6 Typing Va Type Hints Nang Cao

```python
from typing import List, Dict, Optional, Union, Callable, TypeVar

# Co ban
def greet(name: str) -> str:
    return f"Hello, {name}"

# Optional (co the None)
def find_user(id: int) -> Optional[Dict]:
    pass

# Union (nhieu kieu)
def process(value: Union[int, str]) -> str:
    return str(value)

# Callable
def apply(func: Callable[[int, int], int], a: int, b: int) -> int:
    return func(a, b)

# TypeVar (generic)
T = TypeVar("T")
def first(items: List[T]) -> Optional[T]:
    return items[0] if items else None
```

## Bai Tap

1. Dung Counter dem tan suat cac tu trong mot doan van ban
2. Viet generator sinh day so Collatz (cho so n, neu chan thi /2, le thi *3+1, cho den khi bang 1)
3. Tao dataclass `Employee` voi cac field: ten, phong_ban, luong. Sap xep danh sach nhan vien theo luong giam dan.
4. Dung defaultdict nhom danh sach sinh vien theo lop
5. Viet iterator class `FileReader` doc file theo tung dong
6. Su dung itertools.combinations de tim tat ca cac cap so trong list co tong bang mot gia tri cho truoc

## Tai Lieu Tham Khao

- [Collections Module](https://docs.python.org/3/library/collections.html)
- [Itertools](https://docs.python.org/3/library/itertools.html)
- [Dataclasses](https://docs.python.org/3/library/dataclasses.html)
- [Typing](https://docs.python.org/3/library/typing.html)
