# Collections, Generators, Dataclasses demo
from collections import Counter, defaultdict, deque
from dataclasses import dataclass, field
from typing import List
import itertools

# === COUNTER ===
print("=== COUNTER ===")
text = "python is great python is easy python is powerful"
word_count = Counter(text.split())
print(f"Đếm từ: {dict(word_count)}")
print(f"Top 3: {word_count.most_common(3)}")

# === DEFAULTDICT ===
print("\n=== DEFAULTDICT ===")
grades = [("An", 8), ("Binh", 7), ("An", 9), ("Cuong", 6), ("Binh", 8)]
student_grades = defaultdict(list)
for name, grade in grades:
    student_grades[name].append(grade)

for name, g in student_grades.items():
    avg = sum(g) / len(g)
    print(f"  {name}: {g} -> TB: {avg:.1f}")

# === DEQUE ===
print("\n=== DEQUE (Queue) ===")
queue = deque(maxlen=5)
for i in range(7):
    queue.append(i)
    print(f"  Thêm {i}: {list(queue)}")

# === GENERATOR ===
print("\n=== GENERATOR: Fibonacci ===")

def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fib = fibonacci()
fib_10 = [next(fib) for _ in range(10)]
print(f"10 số Fibonacci: {fib_10}")

# === DATACLASS ===
print("\n=== DATACLASS ===")

@dataclass
class SanPham:
    ten: str
    gia: float
    so_luong: int = 0

    @property
    def tong_gia_tri(self):
        return self.gia * self.so_luong

    def __str__(self):
        return f"{self.ten}: {self.gia:,.0f}đ x {self.so_luong} = {self.tong_gia_tri:,.0f}đ"

kho = [
    SanPham("Laptop", 15_000_000, 10),
    SanPham("Chuột", 200_000, 50),
    SanPham("Bàn phím", 800_000, 30),
    SanPham("Màn hình", 5_000_000, 15),
]

for sp in kho:
    print(f"  {sp}")

tong = sum(sp.tong_gia_tri for sp in kho)
print(f"\n  Tổng giá trị kho: {tong:,.0f}đ")

# === ITERTOOLS ===
print("\n=== ITERTOOLS ===")
teams = ["A", "B", "C", "D"]
matches = list(itertools.combinations(teams, 2))
print(f"Lịch thi đấu ({len(matches)} trận):")
for i, (t1, t2) in enumerate(matches, 1):
    print(f"  Trận {i}: {t1} vs {t2}")
