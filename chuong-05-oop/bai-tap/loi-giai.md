# Lời Giải Chương 5

## Bài 1: Class Sản phẩm

```python
class SanPham:                               # Khai báo class
    def __init__(self, ten, gia, so_luong):  # Constructor
        self.ten = ten                       # Lưu tên
        self.gia = gia                       # Lưu giá
        self.so_luong = so_luong             # Lưu số lượng

    def tong_gia_tri(self):                  # Tổng = giá × số lượng
        return self.gia * self.so_luong

    def giam_gia(self, phan_tram):           # Giảm giá theo %
        self.gia *= (1 - phan_tram / 100)    # VD: 20% → gia * 0.8

    def __str__(self):                       # In đẹp
        return f"{self.ten}: {self.gia:,.0f}đ x {self.so_luong}"

sp = SanPham("Laptop", 15_000_000, 5)
print(sp)                                    # Laptop: 15,000,000đ x 5
print(f"Tổng: {sp.tong_gia_tri():,.0f}đ")  # 75,000,000đ
sp.giam_gia(10)                             # Giảm 10%
print(f"Sau giảm: {sp.gia:,.0f}đ")         # 13,500,000đ
```

## Bài 2: Kế thừa

```python
class NhanVien:                              # Class cha
    def __init__(self, ten, luong):
        self.ten = ten
        self.luong = luong

    def mo_ta(self):                         # Method sẽ bị override
        return f"{self.ten} - Lương: {self.luong:,.0f}đ"

class QuanLy(NhanVien):                      # Kế thừa NhanVien
    def __init__(self, ten, luong, so_nv):
        super().__init__(ten, luong)          # Gọi constructor cha
        self.so_nv = so_nv

    def mo_ta(self):                         # Override
        return f"[QĐ] {self.ten} - {self.luong:,.0f}đ - Quản lý {self.so_nv} người"

class LapTrinhVien(NhanVien):                # Kế thừa NhanVien
    def __init__(self, ten, luong, ngon_ngu):
        super().__init__(ten, luong)
        self.ngon_ngu = ngon_ngu

    def mo_ta(self):                         # Override
        return f"[LTV] {self.ten} - {self.luong:,.0f}đ - {', '.join(self.ngon_ngu)}"

# Đa hình: cùng method mo_ta() nhưng khác kết quả
nhan_vien = [
    QuanLy("An", 30_000_000, 10),
    LapTrinhVien("Bình", 25_000_000, ["Python", "Rust"]),
]
for nv in nhan_vien:
    print(nv.mo_ta())                        # Gọi đúng version override
```

## Bài 3: Vector2D

```python
class Vector2D:                              # Class vector 2 chiều
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):                # v1 + v2
        return Vector2D(self.x + other.x, self.y + other.y)

    def __sub__(self, other):                # v1 - v2
        return Vector2D(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):               # v * 3
        return Vector2D(self.x * scalar, self.y * scalar)

    def __abs__(self):                       # abs(v) = độ dài
        return (self.x**2 + self.y**2) ** 0.5

    def __eq__(self, other):                 # v1 == v2
        return self.x == other.x and self.y == other.y

    def __str__(self):                       # print(v)
        return f"({self.x}, {self.y})"

a = Vector2D(1, 2)
b = Vector2D(3, 4)
print(f"a + b = {a + b}")                   # (4, 6)
print(f"a * 3 = {a * 3}")                   # (3, 6)
print(f"|b| = {abs(b):.2f}")                # 5.00
```
