# Chương 5: Lập Trình Hướng Đối Tượng (OOP)

## 5.1 Class & Object

```python
class SinhVien:                              # class = định nghĩa "khuôn mẫu" cho object
    # Class variable
    truong = "ĐH Bách Khoa"                 # Biến class: chung cho TẤT CẢ object SinhVien

    # Constructor
    def __init__(self, ten, tuoi, diem):     # __init__ = constructor, tự chạy khi tạo object mới
        self.ten = ten          # Instance variable - self = chính object đang tạo, lưu tên riêng
        self.tuoi = tuoi                     # Lưu tuổi vào object (mỗi object có giá trị khác nhau)
        self.diem = diem                     # Lưu điểm vào object

    # Method
    def xep_loai(self):                      # Method = hàm thuộc class, luôn có self là tham số đầu
        if self.diem >= 8.5:                 # Truy cập thuộc tính object qua self.
            return "Giỏi"                    # return trả về kết quả
        elif self.diem >= 7.0:
            return "Khá"
        elif self.diem >= 5.0:
            return "Trung bình"
        return "Yếu"                         # Nếu không thỏa điều kiện nào ở trên

    def __str__(self):                       # __str__ = method đặc biệt, gọi khi print(object)
        return f"{self.ten} ({self.tuoi} tuổi) - {self.xep_loai()}"  # Trả về chuỗi mô tả object

# Tạo object
sv1 = SinhVien("Nguyễn A", 20, 8.5)         # Tạo object, gọi __init__(self, "Nguyễn A", 20, 8.5)
sv2 = SinhVien("Trần B", 21, 7.2)           # Tạo object thứ 2 (khác giá trị)
print(sv1)                                   # Gọi __str__() tự động khi print
print(sv2)                                   # In thông tin sv2
print(f"Trường: {SinhVien.truong}")          # Truy cập class variable qua tên class
```

## 5.2 Kế Thừa (Inheritance)

```python
class DongVat:                               # Class cha (parent/base class)
    def __init__(self, ten, tuoi):           # Constructor class cha
        self.ten = ten                       # Thuộc tính chung cho mọi động vật
        self.tuoi = tuoi

    def keu(self):                           # Method chung (sẽ được override ở class con)
        return "..."                         # Giá trị mặc định

    def __str__(self):                       # Chuỗi mô tả
        return f"{self.ten} ({self.tuoi} tuổi)"

class Cho(DongVat):                          # Class con kế thừa DongVat (thừa hưởng mọi thứ)
    def __init__(self, ten, tuoi, giong):    # Constructor riêng, thêm tham số giong
        super().__init__(ten, tuoi)          # super() gọi constructor của class cha
        self.giong = giong                   # Thuộc tính riêng của Cho

    def keu(self):                           # Override (ghi đè) method keu() của class cha
        return "Gâu gâu! 🐕"               # Trả về tiếng kêu riêng

class Meo(DongVat):                          # Class con khác, cũng kế thừa DongVat
    def keu(self):                           # Override method keu()
        return "Meo meo! 🐱"               # Tiếng kêu riêng của mèo

# Sử dụng
rex = Cho("Rex", 3, "Husky")                # Tạo object Cho
miu = Meo("Miu", 2)                         # Tạo object Meo (không có giong)

for con in [rex, miu]:                       # Đa hình: cùng method keu() nhưng hành vi khác nhau
    print(f"{con} - {con.keu()}")            # print(con) gọi __str__() kế thừa từ DongVat

print(isinstance(rex, DongVat))  # True      # isinstance() kiểm tra object thuộc class nào (kể cả cha)
```

## 5.3 Đa Hình (Polymorphism)

```python
class HinhHoc:                               # Class trừu tượng (abstract concept)
    def dien_tich(self):                     # Method sẽ được override ở class con
        raise NotImplementedError            # Ném lỗi nếu class con quên override

    def __str__(self):                       # Chuỗi mô tả chung
        return f"{self.__class__.__name__}: S={self.dien_tich():.2f}"  # __class__.__name__ = tên class

class HinhTron(HinhHoc):                     # Kế thừa HinhHoc
    def __init__(self, ban_kinh):            # Constructor riêng
        self.ban_kinh = ban_kinh             # Lưu bán kính

    def dien_tich(self):                     # Override: công thức diện tích hình tròn
        return 3.14159 * self.ban_kinh ** 2  # S = pi * r^2

class HinhVuong(HinhHoc):                    # Kế thừa HinhHoc
    def __init__(self, canh):                # Constructor
        self.canh = canh                     # Lưu cạnh

    def dien_tich(self):                     # Override: diện tích hình vuông
        return self.canh ** 2                # S = a^2

class HinhChuNhat(HinhHoc):                  # Kế thừa HinhHoc
    def __init__(self, rong, dai):           # Constructor nhận chiều rộng và dài
        self.rong = rong
        self.dai = dai

    def dien_tich(self):                     # Override: diện tích hình chữ nhật
        return self.rong * self.dai          # S = rộng * dài

# Đa hình - cùng method, khác behavior
shapes = [HinhTron(5), HinhVuong(4), HinhChuNhat(3, 7)]  # List các hình khác loại
for s in shapes:                             # Lặp qua từng hình
    print(s)                                 # Gọi __str__() -> gọi dien_tich() tương ứng

tong = sum(s.dien_tich() for s in shapes)    # Generator: tính tổng diện tích
print(f"Tổng diện tích: {tong:.2f}")         # In tổng
```

## 5.4 Encapsulation (Đóng Gói)

```python
class TaiKhoanNganHang:                      # Class đóng gói dữ liệu (ẩn chi tiết bên trong)
    def __init__(self, ten, so_du=0):        # Constructor
        self.ten = ten                       # Public: truy cập tự do
        self.__so_du = so_du      # Private (name mangling): __ đầu tên = không truy cập trực tiếp từ ngoài
        self._ma_pin = "1234"     # Protected (convention): _ đầu tên = quy ước không nên truy cập

    @property                                # @property biến method thành thuộc tính (getter)
    def so_du(self):                         # Truy cập bằng obj.so_du (không cần ())
        """Getter"""
        return self.__so_du                  # Trả về giá trị private

    def nap_tien(self, so_tien):             # Method public để nạp tiền (kiểm soát logic)
        if so_tien > 0:                      # Validate: chỉ cho nạp số dương
            self.__so_du += so_tien          # Cập nhật số dư
            print(f"✅ Nạp {so_tien:,}đ. Số dư: {self.__so_du:,}đ")
        else:
            print("❌ Số tiền không hợp lệ!")

    def rut_tien(self, so_tien):             # Method rút tiền (có kiểm tra)
        if 0 < so_tien <= self.__so_du:      # Kiểm tra: > 0 và <= số dư
            self.__so_du -= so_tien          # Trừ tiền
            print(f"✅ Rút {so_tien:,}đ. Số dư: {self.__so_du:,}đ")
        else:
            print("❌ Không đủ tiền hoặc số tiền không hợp lệ!")

tk = TaiKhoanNganHang("Nguyễn A", 1_000_000)  # Tạo tài khoản
tk.nap_tien(500_000)                         # Nạp tiền qua method (có validation)
tk.rut_tien(200_000)                         # Rút tiền qua method
print(f"Số dư: {tk.so_du:,}đ")              # Dùng property để xem số dư
# tk.__so_du = 999  # ❌ Không truy cập trực tiếp được (name mangling)
```

## 5.5 Magic Methods (Dunder Methods)

```python
class Vector:                                # Class Vector 2D với magic methods
    def __init__(self, x, y):                # Constructor
        self.x = x                           # Tọa độ x
        self.y = y                           # Tọa độ y

    def __repr__(self):                      # __repr__ = biểu diễn chính thức (debug)
        return f"Vector({self.x}, {self.y})"

    def __str__(self):                       # __str__ = biểu diễn thân thiện (print)
        return f"({self.x}, {self.y})"

    def __add__(self, other):                # __add__ = định nghĩa phép + (a + b)
        return Vector(self.x + other.x, self.y + other.y)  # Trả về Vector mới

    def __sub__(self, other):                # __sub__ = định nghĩa phép - (a - b)
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):               # __mul__ = định nghĩa phép * (a * số)
        return Vector(self.x * scalar, self.y * scalar)

    def __abs__(self):                       # __abs__ = định nghĩa abs(a) - độ dài vector
        return (self.x**2 + self.y**2) ** 0.5  # Công thức khoảng cách

    def __eq__(self, other):                 # __eq__ = định nghĩa == (so sánh bằng)
        return self.x == other.x and self.y == other.y

    def __len__(self):                       # __len__ = định nghĩa len(a)
        return 2                             # Vector 2D luôn có 2 thành phần

a = Vector(1, 2)                             # Tạo vector a
b = Vector(3, 4)                             # Tạo vector b
print(f"a + b = {a + b}")                    # Gọi __add__: Vector(4, 6)
print(f"a * 3 = {a * 3}")                    # Gọi __mul__: Vector(3, 6)
print(f"|b| = {abs(b):.2f}")                 # Gọi __abs__: sqrt(9+16) = 5.0
```

## 5.6 Class Methods & Static Methods

```python
class NhanVien:                              # Class nhân viên
    so_nhan_vien = 0                         # Class variable đếm số nhân viên

    def __init__(self, ten, luong):          # Constructor
        self.ten = ten                       # Instance variable
        self.luong = luong
        NhanVien.so_nhan_vien += 1           # Tăng biến class mỗi khi tạo object mới

    @classmethod                             # @classmethod: method của class (không phải object)
    def tu_chuoi(cls, chuoi):                # cls = class hiện tại (thay vì self)
        """Tạo từ chuỗi 'ten-luong'"""       # Factory method: cách khác để tạo object
        ten, luong = chuoi.split("-")        # Tách chuỗi theo dấu -
        return cls(ten, int(luong))          # cls() = tạo object mới từ class

    @staticmethod                            # @staticmethod: hàm tiện ích, không cần self/cls
    def la_ngay_lam_viec(ngay):              # Không nhận self hay cls
        """Kiểm tra ngày làm việc (0=T2, 6=CN)"""
        return ngay < 5                      # True nếu T2-T6 (0-4)

# Sử dụng
nv1 = NhanVien("An", 15_000_000)            # Tạo bằng constructor
nv2 = NhanVien.tu_chuoi("Bình-20000000")    # Tạo bằng classmethod (factory)

print(f"Số NV: {NhanVien.so_nhan_vien}")    # Truy cập class variable
print(f"T2 là ngày làm việc: {NhanVien.la_ngay_lam_viec(0)}")  # Gọi staticmethod qua class
```

## 5.7 Abstract Class

```python
from abc import ABC, abstractmethod          # ABC = Abstract Base Class

class Database(ABC):                         # Kế thừa ABC = class trừu tượng (không tạo object được)
    @abstractmethod                          # Bắt buộc class con phải override method này
    def connect(self):                       # Method trừu tượng: chỉ khai báo, không có code
        pass                                 # pass = không làm gì

    @abstractmethod
    def query(self, sql):                    # Method trừu tượng khác
        pass

    def close(self):                         # Method bình thường (class con kế thừa)
        print("Đóng kết nối")

class MySQL(Database):                       # Kế thừa Database, PHẢI override connect() và query()
    def connect(self):                       # Override method trừu tượng
        print("Kết nối MySQL...")

    def query(self, sql):                    # Override method trừu tượng
        print(f"MySQL query: {sql}")

class PostgreSQL(Database):                  # Class con khác
    def connect(self):
        print("Kết nối PostgreSQL...")

    def query(self, sql):
        print(f"PostgreSQL query: {sql}")

# db = Database()  # ❌ Không thể khởi tạo abstract class (TypeError)
db = MySQL()                                 # Tạo object từ class con (OK)
db.connect()                                 # Gọi method đã override
db.query("SELECT * FROM users")              # Gọi method query
```

## 5.8 Bài Tập

1. Tạo class `SanPham` với tên, giá, số lượng. Thêm method giảm_gia(%), tong_gia_tri()
2. Hệ thống class: `PhuongTien` (cha) → `XeHoi`, `XeMay`, `XeDap` (con)
3. Class `Matrix` hỗ trợ phép +, *, str
4. Class `LinkedList` với insert, delete, search, display

---

📖 **Trước đó**: [Chương 4](../chuong-04-ham-va-module/README.md) | **Tiếp theo**: [Chương 6](../chuong-06-xu-ly-file-exception/README.md)
