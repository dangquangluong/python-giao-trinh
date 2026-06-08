# Chuong 5: Lap Trinh Huong Doi Tuong (OOP)

## 5.1 Class Va Object

### Dinh nghia class

```python
class SinhVien:
    """Class dai dien cho sinh vien."""
    
    def __init__(self, ten, mssv, diem_tb=0):
        """Khoi tao doi tuong SinhVien."""
        self.ten = ten
        self.mssv = mssv
        self.diem_tb = diem_tb
    
    def xep_loai(self):
        """Xep loai hoc luc."""
        if self.diem_tb >= 9:
            return "Xuat sac"
        elif self.diem_tb >= 8:
            return "Gioi"
        elif self.diem_tb >= 7:
            return "Kha"
        elif self.diem_tb >= 5:
            return "Trung binh"
        return "Yeu"
    
    def __str__(self):
        return f"SinhVien({self.ten}, {self.mssv}, {self.diem_tb})"

# Tao doi tuong
sv1 = SinhVien("Nguyen Van A", "SV001", 8.5)
sv2 = SinhVien("Tran Thi B", "SV002", 9.2)

print(sv1)              # SinhVien(Nguyen Van A, SV001, 8.5)
print(sv1.xep_loai())   # Gioi
```

### Thuoc tinh class va instance

```python
class NhanVien:
    # Thuoc tinh class (chung cho tat ca doi tuong)
    cong_ty = "ABC Corp"
    so_nhan_vien = 0
    
    def __init__(self, ten, luong):
        # Thuoc tinh instance (rieng moi doi tuong)
        self.ten = ten
        self.luong = luong
        NhanVien.so_nhan_vien += 1
    
    @classmethod
    def tong_nhan_vien(cls):
        return cls.so_nhan_vien
    
    @staticmethod
    def tinh_thue(luong):
        if luong > 10000000:
            return luong * 0.1
        return 0
```

## 5.2 Ke Thua (Inheritance)

### Ke thua don

```python
class DongVat:
    def __init__(self, ten, tuoi):
        self.ten = ten
        self.tuoi = tuoi
    
    def keu(self):
        return "..."
    
    def __str__(self):
        return f"{self.ten} ({self.tuoi} tuoi)"

class Cho(DongVat):
    def __init__(self, ten, tuoi, giong):
        super().__init__(ten, tuoi)
        self.giong = giong
    
    def keu(self):
        return "Gau gau!"

class Meo(DongVat):
    def keu(self):
        return "Meo meo!"

# Su dung
dog = Cho("Buddy", 3, "Golden")
cat = Meo("Kitty", 2)

print(f"{dog} - {dog.keu()}")  # Buddy (3 tuoi) - Gau gau!
print(f"{cat} - {cat.keu()}")  # Kitty (2 tuoi) - Meo meo!
```

### Ke thua nhieu lop

```python
class Flyable:
    def fly(self):
        return "Dang bay..."

class Swimmable:
    def swim(self):
        return "Dang boi..."

class Duck(DongVat, Flyable, Swimmable):
    def keu(self):
        return "Quack quack!"

duck = Duck("Donald", 1)
print(duck.fly())   # Dang bay...
print(duck.swim())  # Dang boi...
print(duck.keu())   # Quack quack!
```

## 5.3 Da Hinh (Polymorphism)

```python
class HinhHoc:
    def dien_tich(self):
        raise NotImplementedError("Lop con phai override")
    
    def chu_vi(self):
        raise NotImplementedError("Lop con phai override")

class HinhTron(HinhHoc):
    def __init__(self, ban_kinh):
        self.ban_kinh = ban_kinh
    
    def dien_tich(self):
        import math
        return math.pi * self.ban_kinh ** 2
    
    def chu_vi(self):
        import math
        return 2 * math.pi * self.ban_kinh

class HinhChuNhat(HinhHoc):
    def __init__(self, dai, rong):
        self.dai = dai
        self.rong = rong
    
    def dien_tich(self):
        return self.dai * self.rong
    
    def chu_vi(self):
        return 2 * (self.dai + self.rong)

# Da hinh
shapes = [HinhTron(5), HinhChuNhat(4, 6), HinhTron(3)]
for shape in shapes:
    print(f"{shape.__class__.__name__}: DT={shape.dien_tich():.2f}, CV={shape.chu_vi():.2f}")
```

## 5.4 Encapsulation (Dong Goi)

```python
class TaiKhoanNganHang:
    def __init__(self, chu_tai_khoan, so_du=0):
        self._chu_tai_khoan = chu_tai_khoan  # Protected
        self.__so_du = so_du                 # Private
    
    @property
    def so_du(self):
        """Getter cho so du."""
        return self.__so_du
    
    @property
    def chu_tai_khoan(self):
        return self._chu_tai_khoan
    
    def nap_tien(self, so_tien):
        if so_tien <= 0:
            raise ValueError("So tien phai lon hon 0")
        self.__so_du += so_tien
        return self.__so_du
    
    def rut_tien(self, so_tien):
        if so_tien <= 0:
            raise ValueError("So tien phai lon hon 0")
        if so_tien > self.__so_du:
            raise ValueError("So du khong du")
        self.__so_du -= so_tien
        return self.__so_du

tk = TaiKhoanNganHang("An", 1000000)
tk.nap_tien(500000)
print(f"So du: {tk.so_du:,} VND")  # 1,500,000 VND
```

## 5.5 Magic Methods (Dunder Methods)

```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __repr__(self):
        return f"Vector({self.x}, {self.y})"
    
    def __str__(self):
        return f"({self.x}, {self.y})"
    
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)
    
    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)
    
    def __abs__(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
    def __len__(self):
        return 2
    
    def __getitem__(self, index):
        if index == 0:
            return self.x
        elif index == 1:
            return self.y
        raise IndexError("Chi co index 0 va 1")

v1 = Vector(3, 4)
v2 = Vector(1, 2)

print(f"v1 = {v1}")           # (3, 4)
print(f"v1 + v2 = {v1 + v2}") # (4, 6)
print(f"v1 - v2 = {v1 - v2}") # (2, 2)
print(f"v1 * 3 = {v1 * 3}")   # (9, 12)
print(f"|v1| = {abs(v1):.2f}") # 5.00
```

## 5.6 Abstract Class

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    """Abstract class cho hinh hoc."""
    
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimeter(self):
        pass
    
    def describe(self):
        return f"{self.__class__.__name__}: DT={self.area():.2f}, CV={self.perimeter():.2f}"

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        import math
        return math.pi * self.radius ** 2
    
    def perimeter(self):
        import math
        return 2 * math.pi * self.radius

# shape = Shape()  # TypeError: Can't instantiate abstract class
circle = Circle(5)
print(circle.describe())
```

## 5.7 Property Va Descriptor

```python
class NhietDo:
    def __init__(self, celsius=0):
        self._celsius = celsius
    
    @property
    def celsius(self):
        return self._celsius
    
    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("Nhiet do khong the thap hon -273.15C")
        self._celsius = value
    
    @property
    def fahrenheit(self):
        return self._celsius * 9/5 + 32
    
    @fahrenheit.setter
    def fahrenheit(self, value):
        self._celsius = (value - 32) * 5/9

temp = NhietDo(100)
print(f"{temp.celsius}C = {temp.fahrenheit}F")  # 100C = 212.0F

temp.fahrenheit = 72
print(f"{temp.celsius:.1f}C = {temp.fahrenheit}F")  # 22.2C = 72.0F
```

## Bai Tap

1. Tao class `SinhVien` voi thuoc tinh ten, mssv, danh sach diem. Them phuong thuc tinh diem TB va xep loai.
2. Tao he thong class ke thua: `PhuongTien` -> `Oto`, `XeMay`, `XeDap` voi cac thuoc tinh va phuong thuc phu hop.
3. Implement class `Matrix` voi magic methods: `__add__`, `__mul__`, `__str__`, `__eq__`
4. Tao class `BankAccount` voi property bao ve so_du, phuong thuc nap/rut tien co kiem tra hop le.
5. Su dung ABC tao abstract class `Database` voi cac method: connect, query, close. Implement `SQLiteDB` va `MemoryDB`.
6. Tao class `Stack` va `Queue` voi cac method push/pop/peek/is_empty.

## Tai Lieu Tham Khao

- [Python Classes](https://docs.python.org/3/tutorial/classes.html)
- [Data Model](https://docs.python.org/3/reference/datamodel.html)
- [ABC Module](https://docs.python.org/3/library/abc.html)
