# Ví dụ về hàm, lambda, decorator
import time

# === HÀM CƠ BẢN ===
def tinh_bmi(can_nang, chieu_cao):
    """Tính chỉ số BMI"""
    bmi = can_nang / (chieu_cao ** 2)
    if bmi < 18.5:
        phan_loai = "Gầy"
    elif bmi < 25:
        phan_loai = "Bình thường"
    elif bmi < 30:
        phan_loai = "Thừa cân"
    else:
        phan_loai = "Béo phì"
    return bmi, phan_loai

bmi, loai = tinh_bmi(70, 1.75)
print(f"BMI: {bmi:.1f} - {loai}")

# === *ARGS, **KWARGS ===
def log(*args, level="INFO", **kwargs):
    msg = " ".join(str(a) for a in args)
    extra = ", ".join(f"{k}={v}" for k, v in kwargs.items())
    print(f"[{level}] {msg} {extra}")

log("Server started", "port", 8080, level="INFO", host="localhost")

# === LAMBDA ===
print("\n=== LAMBDA + SORTED ===")
students = [
    {"ten": "An", "diem": 8.5},
    {"ten": "Binh", "diem": 7.0},
    {"ten": "Cuong", "diem": 9.2},
]
sorted_students = sorted(students, key=lambda s: s["diem"], reverse=True)
for s in sorted_students:
    print(f"  {s['ten']}: {s['diem']}")

# === DECORATOR ===
print("\n=== DECORATOR ===")

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - start
        print(f"  {func.__name__}: {elapsed*1000:.2f}ms")
        return result
    return wrapper

@timer
def tinh_tong(n):
    return sum(range(n))

@timer
def tinh_tong_bp(n):
    return sum(i**2 for i in range(n))

tinh_tong(1_000_000)
tinh_tong_bp(100_000)

# === CLOSURE ===
print("\n=== CLOSURE ===")

def multiplier(n):
    def multiply(x):
        return x * n
    return multiply

double = multiplier(2)
triple = multiplier(3)
print(f"double(5) = {double(5)}")
print(f"triple(5) = {triple(5)}")

# === ĐỆ QUY ===
print("\n=== ĐỆ QUY: FIBONACCI ===")

def fib(n, memo={}):
    if n <= 1:
        return n
    if n not in memo:
        memo[n] = fib(n-1) + fib(n-2)
    return memo[n]

for i in range(1, 11):
    print(f"  fib({i}) = {fib(i)}")
