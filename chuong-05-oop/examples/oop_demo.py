"""
Chuong 5: Vi du ve Lap Trinh Huong Doi Tuong
"""

from abc import ABC, abstractmethod
import math


# === Class co ban ===
class SinhVien:
    """Class dai dien cho sinh vien."""

    so_sinh_vien = 0  # Thuoc tinh class

    def __init__(self, ten, mssv, diem=None):
        self.ten = ten
        self.mssv = mssv
        self.diem = diem or []
        SinhVien.so_sinh_vien += 1

    @property
    def diem_tb(self):
        if not self.diem:
            return 0
        return sum(self.diem) / len(self.diem)

    def xep_loai(self):
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

    def them_diem(self, diem):
        self.diem.append(diem)

    def __str__(self):
        return f"{self.ten} ({self.mssv}) - DTB: {self.diem_tb:.1f} - {self.xep_loai()}"

    def __repr__(self):
        return f"SinhVien('{self.ten}', '{self.mssv}', {self.diem})"


# === Ke thua va da hinh ===
class Shape(ABC):
    """Abstract class hinh hoc."""

    @abstractmethod
    def area(self) -> float:
        pass

    @abstractmethod
    def perimeter(self) -> float:
        pass

    def info(self):
        return f"{self.__class__.__name__}: DT={self.area():.2f}, CV={self.perimeter():.2f}"


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)


# === Magic methods ===
class Vector:
    """Vector 2D voi cac phep toan."""

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

    def __abs__(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"


# === Encapsulation voi property ===
class BankAccount:
    """Tai khoan ngan hang voi bao mat."""

    def __init__(self, owner, balance=0):
        self._owner = owner
        self.__balance = balance
        self.__history = []

    @property
    def balance(self):
        return self.__balance

    @property
    def owner(self):
        return self._owner

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("So tien nap phai lon hon 0")
        self.__balance += amount
        self.__history.append(f"+{amount:,}")
        return self.__balance

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("So tien rut phai lon hon 0")
        if amount > self.__balance:
            raise ValueError("So du khong du")
        self.__balance -= amount
        self.__history.append(f"-{amount:,}")
        return self.__balance

    def get_history(self):
        return self.__history.copy()

    def __str__(self):
        return f"Account({self._owner}: {self.__balance:,} VND)"


# === Demo ===
if __name__ == "__main__":
    print("=" * 50)
    print("=== SINH VIEN ===")
    print("=" * 50)

    sv1 = SinhVien("Nguyen Van A", "SV001", [8.5, 9.0, 7.5, 8.0])
    sv2 = SinhVien("Tran Thi B", "SV002", [9.0, 9.5, 9.0, 8.5])
    sv3 = SinhVien("Le Van C", "SV003", [6.0, 5.5, 7.0, 6.5])

    for sv in [sv1, sv2, sv3]:
        print(f"  {sv}")
    print(f"  Tong so SV: {SinhVien.so_sinh_vien}")
    print()

    print("=" * 50)
    print("=== HINH HOC (Da hinh) ===")
    print("=" * 50)

    shapes = [Circle(5), Rectangle(4, 6), Square(3)]
    for s in shapes:
        print(f"  {s.info()}")
    print()

    print("=" * 50)
    print("=== VECTOR (Magic methods) ===")
    print("=" * 50)

    v1 = Vector(3, 4)
    v2 = Vector(1, 2)
    print(f"  v1 = {v1}")
    print(f"  v2 = {v2}")
    print(f"  v1 + v2 = {v1 + v2}")
    print(f"  v1 - v2 = {v1 - v2}")
    print(f"  v1 * 3 = {v1 * 3}")
    print(f"  |v1| = {abs(v1):.2f}")
    print()

    print("=" * 50)
    print("=== BANK ACCOUNT (Encapsulation) ===")
    print("=" * 50)

    acc = BankAccount("An", 1000000)
    print(f"  {acc}")
    acc.deposit(500000)
    print(f"  Nap 500,000 -> So du: {acc.balance:,} VND")
    acc.withdraw(200000)
    print(f"  Rut 200,000 -> So du: {acc.balance:,} VND")
    print(f"  Lich su: {acc.get_history()}")
