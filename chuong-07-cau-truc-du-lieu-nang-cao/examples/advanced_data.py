"""
Chuong 7: Vi du ve cau truc du lieu nang cao
"""

from collections import Counter, defaultdict, deque, namedtuple
from dataclasses import dataclass, field
from itertools import islice, chain, groupby
from typing import List


# === Collections ===
def demo_collections():
    """Demo cac cau truc du lieu tu collections."""
    print("=" * 50)
    print("=== COLLECTIONS ===")
    print("=" * 50)

    # Counter
    print("\n--- Counter ---")
    text = "python la ngon ngu lap trinh pho bien python de hoc python manh me"
    word_count = Counter(text.split())
    print(f"  Top 3 tu xuat hien nhieu: {word_count.most_common(3)}")

    # defaultdict
    print("\n--- defaultdict ---")
    students = [
        ("CNTT", "An"), ("KTPM", "Binh"), ("CNTT", "Chi"),
        ("KTPM", "Dung"), ("CNTT", "Em"), ("MMT", "Fong"),
    ]
    groups = defaultdict(list)
    for dept, name in students:
        groups[dept].append(name)
    for dept, names in groups.items():
        print(f"  {dept}: {names}")

    # deque
    print("\n--- deque ---")
    recent = deque(maxlen=5)
    for i in range(10):
        recent.append(f"item_{i}")
    print(f"  5 phan tu gan nhat: {list(recent)}")

    # namedtuple
    print("\n--- namedtuple ---")
    Point = namedtuple("Point", ["x", "y"])
    points = [Point(1, 2), Point(3, 4), Point(5, 6)]
    for p in points:
        print(f"  Point({p.x}, {p.y}) - khoang cach goc: {(p.x**2 + p.y**2)**0.5:.2f}")

    print()


# === Generator ===
def fibonacci():
    """Generator sinh so Fibonacci vo han."""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


def collatz(n):
    """Generator sinh day Collatz."""
    yield n
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        yield n


def demo_generators():
    """Demo generators."""
    print("=" * 50)
    print("=== GENERATORS ===")
    print("=" * 50)

    # Fibonacci
    print("\n--- Fibonacci (15 so dau) ---")
    fib_15 = list(islice(fibonacci(), 15))
    print(f"  {fib_15}")

    # Collatz
    print("\n--- Day Collatz (bat dau tu 27) ---")
    seq = list(collatz(27))
    print(f"  Do dai: {len(seq)} buoc")
    print(f"  5 so dau: {seq[:5]}")
    print(f"  5 so cuoi: {seq[-5:]}")
    print(f"  Gia tri lon nhat: {max(seq)}")

    # Generator expression vs list
    print("\n--- Generator vs List (bo nho) ---")
    import sys
    list_comp = [x**2 for x in range(1000)]
    gen_exp = (x**2 for x in range(1000))
    print(f"  List: {sys.getsizeof(list_comp)} bytes")
    print(f"  Generator: {sys.getsizeof(gen_exp)} bytes")

    print()


# === Dataclass ===
@dataclass
class SinhVien:
    ten: str
    mssv: str
    diem: List[float] = field(default_factory=list)

    @property
    def diem_tb(self) -> float:
        if not self.diem:
            return 0.0
        return sum(self.diem) / len(self.diem)

    @property
    def xep_loai(self) -> str:
        dtb = self.diem_tb
        if dtb >= 9:
            return "Xuat sac"
        elif dtb >= 8:
            return "Gioi"
        elif dtb >= 7:
            return "Kha"
        elif dtb >= 5:
            return "Trung binh"
        return "Yeu"


@dataclass(order=True)
class Product:
    sort_index: float = field(init=False, repr=False)
    ten: str
    gia: float
    so_luong: int = 0

    def __post_init__(self):
        self.sort_index = self.gia

    @property
    def tong_gia_tri(self):
        return self.gia * self.so_luong


def demo_dataclass():
    """Demo dataclass."""
    print("=" * 50)
    print("=== DATACLASS ===")
    print("=" * 50)

    # SinhVien
    print("\n--- Sinh Vien ---")
    students = [
        SinhVien("Nguyen Van A", "SV001", [8.5, 9.0, 7.5]),
        SinhVien("Tran Thi B", "SV002", [9.0, 9.5, 9.0]),
        SinhVien("Le Van C", "SV003", [6.0, 5.5, 7.0]),
    ]
    for sv in students:
        print(f"  {sv.ten} ({sv.mssv}): DTB={sv.diem_tb:.1f} - {sv.xep_loai}")

    # Product
    print("\n--- San Pham (sap xep theo gia) ---")
    products = [
        Product("Laptop", 15000000, 10),
        Product("Phone", 8000000, 20),
        Product("Tablet", 12000000, 5),
        Product("Earbuds", 2000000, 50),
    ]
    for p in sorted(products):
        print(f"  {p.ten}: {p.gia:>12,.0f} VND x {p.so_luong} = {p.tong_gia_tri:>14,.0f} VND")

    print()


# === Iterator class ===
class Range:
    """Reimplementation don gian cua range()."""

    def __init__(self, start, stop=None, step=1):
        if stop is None:
            start, stop = 0, start
        self.start = start
        self.stop = stop
        self.step = step
        self.current = start

    def __iter__(self):
        self.current = self.start
        return self

    def __next__(self):
        if (self.step > 0 and self.current >= self.stop) or \
           (self.step < 0 and self.current <= self.stop):
            raise StopIteration
        value = self.current
        self.current += self.step
        return value


def demo_iterator():
    """Demo iterator."""
    print("=" * 50)
    print("=== CUSTOM ITERATOR ===")
    print("=" * 50)

    print("\n--- Range(1, 10, 2) ---")
    print(f"  {list(Range(1, 10, 2))}")

    print("\n--- Range(10, 0, -3) ---")
    print(f"  {list(Range(10, 0, -3))}")

    print()


# === Main ===
if __name__ == "__main__":
    demo_collections()
    demo_generators()
    demo_dataclass()
    demo_iterator()
