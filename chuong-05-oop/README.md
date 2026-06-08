# Chương 5: Lập Trình Hướng Đối Tượng (OOP)

## 5.1 Class & Object

```python
class SinhVien:
    # Class variable
    truong = "ĐH Bách Khoa"

    # Constructor
    def __init__(self, ten, tuoi, diem):
        self.ten = ten          # Instance variable
        self.tuoi = tuoi
        self.diem = diem

    # Method
    def xep_loai(self):
        if self.diem >= 8.5:
            return "Giỏi"
        elif self.diem >= 7.0:
            return "Khá"
        elif self.diem >= 5.0:
            return "Trung bình"
        return "Yếu"

    def __str__(self):
        return f"{self.ten} ({self.tuoi} tuổi) - {self.xep_loai()}"

# Tạo object
sv1 = SinhVien("Nguyễn A", 20, 8.5)
sv2 = SinhVien("Trần B", 21, 7.2)
print(sv1)
print(sv2)
print(f"Trường: {SinhVien.truong}")
```

## 5.2 Kế Thừa (Inheritance)

```python
class DongVat:
    def __init__(self, ten, tuoi):
        self.ten = ten
        self.tuoi = tuoi

    def keu(self):
        return "..."

    def __str__(self):
        return f"{self.ten} ({self.tuoi} tuổi)"

class Cho(DongVat):
    def __init__(self, ten, tuoi, giong):
        super().__init__(ten, tuoi)  # Gọi constructor cha
        self.giong = giong

    def keu(self):
        return "Gâu gâu! 🐕"

class Meo(DongVat):
    def keu(self):
        return "Meo meo! 🐱"

# Sử dụng
rex = Cho("Rex", 3, "Husky")
miu = Meo("Miu", 2)

for con in [rex, miu]:
    print(f"{con} - {con.keu()}")

print(isinstance(rex, DongVat))  # True
```

## 5.3 Đa Hình (Polymorphism)

```python
class HinhHoc:
    def dien_tich(self):
        raise NotImplementedError

    def __str__(self):
        return f"{self.__class__.__name__}: S={self.dien_tich():.2f}"

class HinhTron(HinhHoc):
    def __init__(self, ban_kinh):
        self.ban_kinh = ban_kinh

    def dien_tich(self):
        return 3.14159 * self.ban_kinh ** 2

class HinhVuong(HinhHoc):
    def __init__(self, canh):
        self.canh = canh

    def dien_tich(self):
        return self.canh ** 2

class HinhChuNhat(HinhHoc):
    def __init__(self, rong, dai):
        self.rong = rong
        self.dai = dai

    def dien_tich(self):
        return self.rong * self.dai

# Đa hình - cùng method, khác behavior
shapes = [HinhTron(5), HinhVuong(4), HinhChuNhat(3, 7)]
for s in shapes:
    print(s)

tong = sum(s.dien_tich() for s in shapes)
print(f"Tổng diện tích: {tong:.2f}")
```

## 5.4 Encapsulation (Đóng Gói)

```python
class TaiKhoanNganHang:
    def __init__(self, ten, so_du=0):
        self.ten = ten
        self.__so_du = so_du      # Private (name mangling)
        self._ma_pin = "1234"     # Protected (convention)

    @property
    def so_du(self):
        """Getter"""
        return self.__so_du

    def nap_tien(self, so_tien):
        if so_tien > 0:
            self.__so_du += so_tien
            print(f"✅ Nạp {so_tien:,}đ. Số dư: {self.__so_du:,}đ")
        else:
            print("❌ Số tiền không hợp lệ!")

    def rut_tien(self, so_tien):
        if 0 < so_tien <= self.__so_du:
            self.__so_du -= so_tien
            print(f"✅ Rút {so_tien:,}đ. Số dư: {self.__so_du:,}đ")
        else:
            print("❌ Không đủ tiền hoặc số tiền không hợp lệ!")

tk = TaiKhoanNganHang("Nguyễn A", 1_000_000)
tk.nap_tien(500_000)
tk.rut_tien(200_000)
print(f"Số dư: {tk.so_du:,}đ")
# tk.__so_du = 999  # ❌ Không truy cập trực tiếp được
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
        return (self.x**2 + self.y**2) ** 0.5

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __len__(self):
        return 2

a = Vector(1, 2)
b = Vector(3, 4)
print(f"a + b = {a + b}")
print(f"a * 3 = {a * 3}")
print(f"|b| = {abs(b):.2f}")
```

## 5.6 Class Methods & Static Methods

```python
class NhanVien:
    so_nhan_vien = 0

    def __init__(self, ten, luong):
        self.ten = ten
        self.luong = luong
        NhanVien.so_nhan_vien += 1

    @classmethod
    def tu_chuoi(cls, chuoi):
        """Tạo từ chuỗi 'ten-luong'"""
        ten, luong = chuoi.split("-")
        return cls(ten, int(luong))

    @staticmethod
    def la_ngay_lam_viec(ngay):
        """Kiểm tra ngày làm việc (0=T2, 6=CN)"""
        return ngay < 5

# Sử dụng
nv1 = NhanVien("An", 15_000_000)
nv2 = NhanVien.tu_chuoi("Bình-20000000")  # classmethod

print(f"Số NV: {NhanVien.so_nhan_vien}")
print(f"T2 là ngày làm việc: {NhanVien.la_ngay_lam_viec(0)}")
```

## 5.7 Abstract Class

```python
from abc import ABC, abstractmethod

class Database(ABC):
    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def query(self, sql):
        pass

    def close(self):
        print("Đóng kết nối")

class MySQL(Database):
    def connect(self):
        print("Kết nối MySQL...")

    def query(self, sql):
        print(f"MySQL query: {sql}")

class PostgreSQL(Database):
    def connect(self):
        print("Kết nối PostgreSQL...")

    def query(self, sql):
        print(f"PostgreSQL query: {sql}")

# db = Database()  # ❌ Không thể khởi tạo abstract class
db = MySQL()
db.connect()
db.query("SELECT * FROM users")
```

## 5.8 Bài Tập

1. Tạo class `SanPham` với tên, giá, số lượng. Thêm method giảm_gia(%), tong_gia_tri()
2. Hệ thống class: `PhuongTien` (cha) → `XeHoi`, `XeMay`, `XeDap` (con)
3. Class `Matrix` hỗ trợ phép +, *, str
4. Class `LinkedList` với insert, delete, search, display

---

📖 **Trước đó**: [Chương 4](../chuong-04-ham-va-module/README.md) | **Tiếp theo**: [Chương 6](../chuong-06-xu-ly-file-exception/README.md)
