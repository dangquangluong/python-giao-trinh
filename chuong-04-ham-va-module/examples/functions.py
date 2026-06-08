"""
Chuong 4: Vi du ve ham va decorator
"""

import time
from functools import wraps


# === Ham co ban ===
def chao(ten, loi_chao="Xin chao"):
    """In loi chao."""
    return f"{loi_chao}, {ten}!"


# === Ham voi *args, **kwargs ===
def tinh_tong(*args):
    """Tinh tong cac so."""
    return sum(args)


def tao_profile(**kwargs):
    """Tao profile tu cac keyword arguments."""
    profile = {}
    for key, value in kwargs.items():
        profile[key] = value
    return profile


# === Type hints ===
def tinh_bmi(can_nang: float, chieu_cao: float) -> tuple[float, str]:
    """Tinh BMI va phan loai."""
    bmi = can_nang / (chieu_cao ** 2)
    if bmi < 18.5:
        phan_loai = "Gay"
    elif bmi < 25:
        phan_loai = "Binh thuong"
    elif bmi < 30:
        phan_loai = "Thua can"
    else:
        phan_loai = "Beo phi"
    return bmi, phan_loai


# === De quy ===
def fibonacci(n: int) -> list[int]:
    """Tra ve n so Fibonacci dau tien."""
    if n <= 0:
        return []
    if n == 1:
        return [0]
    fib = [0, 1]
    for _ in range(2, n):
        fib.append(fib[-1] + fib[-2])
    return fib


# === Decorator ===
def timer(func):
    """Decorator do thoi gian thuc thi."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - start
        print(f"  [{func.__name__}] thoi gian: {elapsed:.6f}s")
        return result
    return wrapper


def log(func):
    """Decorator ghi log khi goi ham."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"  Goi {func.__name__}(args={args}, kwargs={kwargs})")
        result = func(*args, **kwargs)
        print(f"  Ket qua: {result}")
        return result
    return wrapper


# === Closure ===
def tao_bo_dem(bat_dau=0):
    """Tao bo dem su dung closure."""
    count = [bat_dau]

    def tang():
        count[0] += 1
        return count[0]

    def giam():
        count[0] -= 1
        return count[0]

    def gia_tri():
        return count[0]

    return tang, giam, gia_tri


# === Demo ===
if __name__ == "__main__":
    print("=== Ham co ban ===")
    print(chao("An"))
    print(chao("Binh", "Hello"))
    print()

    print("=== *args ===")
    print(f"Tong 1,2,3: {tinh_tong(1, 2, 3)}")
    print(f"Tong 1-10: {tinh_tong(*range(1, 11))}")
    print()

    print("=== **kwargs ===")
    profile = tao_profile(ten="An", tuoi=25, thanh_pho="Ha Noi")
    for k, v in profile.items():
        print(f"  {k}: {v}")
    print()

    print("=== Type hints ===")
    bmi, loai = tinh_bmi(70, 1.75)
    print(f"BMI: {bmi:.1f} - Phan loai: {loai}")
    print()

    print("=== Fibonacci ===")
    print(f"10 so dau: {fibonacci(10)}")
    print()

    print("=== Decorator @timer ===")

    @timer
    def tinh_tong_lon(n):
        return sum(range(n))

    tinh_tong_lon(1000000)
    print()

    print("=== Decorator @log ===")

    @log
    def cong(a, b):
        return a + b

    cong(3, 5)
    print()

    print("=== Closure (Bo dem) ===")
    tang, giam, gia_tri = tao_bo_dem(10)
    print(f"  Ban dau: {gia_tri()}")
    print(f"  Tang: {tang()}")
    print(f"  Tang: {tang()}")
    print(f"  Giam: {giam()}")
    print(f"  Hien tai: {gia_tri()}")
