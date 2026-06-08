"""
Chuong 7: Vi du ve cau truc du lieu nang cao
"""

from collections import Counter, defaultdict, deque, namedtuple  # Import cấu trúc dữ liệu đặc biệt
from dataclasses import dataclass, field     # dataclass = tạo class ngắn gọn, field = tùy chỉnh thuộc tính
from itertools import islice, chain, groupby  # Công cụ xử lý iterator nâng cao
from typing import List                      # Type hint cho list


# === Collections ===
def demo_collections():                      # Hàm demo các cấu trúc dữ liệu collections
    """Demo cac cau truc du lieu tu collections."""  # Docstring
    print("=" * 50)                          # In đường kẻ 50 dấu =
    print("=== COLLECTIONS ===")             # In tiêu đề
    print("=" * 50)                          # In đường kẻ

    # Counter
    print("\n--- Counter ---")               # Counter = đếm tần suất phần tử
    text = "python la ngon ngu lap trinh pho bien python de hoc python manh me"  # Chuỗi văn bản
    word_count = Counter(text.split())       # split() tách thành list, Counter đếm từng từ
    print(f"  Top 3 tu xuat hien nhieu: {word_count.most_common(3)}")  # 3 từ phổ biến nhất

    # defaultdict
    print("\n--- defaultdict ---")           # defaultdict = dict tự tạo giá trị mặc định
    students = [                             # List tuple (khoa, tên sinh viên)
        ("CNTT", "An"), ("KTPM", "Binh"), ("CNTT", "Chi"),   # Dữ liệu mẫu
        ("KTPM", "Dung"), ("CNTT", "Em"), ("MMT", "Fong"),   # Dữ liệu mẫu
    ]
    groups = defaultdict(list)               # Tạo defaultdict, giá trị mặc định = list rỗng
    for dept, name in students:              # Lặp qua, unpack tuple thành (khoa, tên)
        groups[dept].append(name)            # Thêm tên vào list của khoa tương ứng
    for dept, names in groups.items():       # Lặp qua kết quả đã nhóm
        print(f"  {dept}: {names}")          # In khoa và danh sách sinh viên

    # deque
    print("\n--- deque ---")                 # deque = double-ended queue (hàng đợi hai đầu)
    recent = deque(maxlen=5)                 # maxlen=5: tối đa 5 phần tử, tự xóa cũ nhất
    for i in range(10):                      # Thêm 10 phần tử (chỉ giữ 5 cuối)
        recent.append(f"item_{i}")           # .append() thêm vào cuối
    print(f"  5 phan tu gan nhat: {list(recent)}")  # In 5 phần tử còn lại

    # namedtuple
    print("\n--- namedtuple ---")            # namedtuple = tuple có tên cho từng trường
    Point = namedtuple("Point", ["x", "y"]) # Tạo kiểu Point với 2 trường x, y
    points = [Point(1, 2), Point(3, 4), Point(5, 6)]  # Tạo 3 điểm
    for p in points:                         # Lặp qua từng điểm
        print(f"  Point({p.x}, {p.y}) - khoang cach goc: {(p.x**2 + p.y**2)**0.5:.2f}")  # Tính khoảng cách đến gốc

    print()                                  # In dòng trống


# === Generator ===
def fibonacci():                             # Hàm generator sinh Fibonacci vô hạn
    """Generator sinh so Fibonacci vo han.""" # Docstring
    a, b = 0, 1                              # Khởi tạo F(0)=0, F(1)=1
    while True:                              # Vòng lặp vô hạn (generator chỉ sinh khi cần)
        yield a                              # yield trả về a và tạm dừng hàm
        a, b = b, a + b                      # Tính số tiếp: a mới = b cũ, b mới = a+b


def collatz(n):                              # Generator sinh dãy Collatz
    """Generator sinh day Collatz."""         # Docstring: dãy Collatz luôn kết thúc ở 1
    yield n                                  # Trả về số đầu tiên
    while n != 1:                            # Lặp cho đến khi n = 1
        if n % 2 == 0:                       # Nếu n chẵn
            n = n // 2                       # Chia đôi (// = chia lấy phần nguyên)
        else:                                # Nếu n lẻ
            n = 3 * n + 1                    # Nhân 3 cộng 1
        yield n                              # Trả về số tiếp theo trong dãy


def demo_generators():                       # Hàm demo generators
    """Demo generators."""                   # Docstring
    print("=" * 50)                          # In đường kẻ
    print("=== GENERATORS ===")              # In tiêu đề
    print("=" * 50)                          # In đường kẻ

    # Fibonacci
    print("\n--- Fibonacci (15 so dau) ---") # In tiêu đề
    fib_15 = list(islice(fibonacci(), 15))   # islice(generator, 15) = lấy 15 phần tử đầu tiên
    print(f"  {fib_15}")                     # In 15 số Fibonacci

    # Collatz
    print("\n--- Day Collatz (bat dau tu 27) ---")  # Dãy Collatz bắt đầu từ 27
    seq = list(collatz(27))                  # Chuyển generator thành list (chạy hết dãy)
    print(f"  Do dai: {len(seq)} buoc")      # In độ dài dãy
    print(f"  5 so dau: {seq[:5]}")          # Slicing: lấy 5 phần tử đầu
    print(f"  5 so cuoi: {seq[-5:]}")        # Slicing: lấy 5 phần tử cuối
    print(f"  Gia tri lon nhat: {max(seq)}") # max() tìm giá trị lớn nhất

    # Generator expression vs list
    print("\n--- Generator vs List (bo nho) ---")  # So sánh bộ nhớ
    import sys                               # Module sys để kiểm tra kích thước object
    list_comp = [x**2 for x in range(1000)]  # List comprehension: tạo list 1000 phần tử ngay
    gen_exp = (x**2 for x in range(1000))    # Generator expression: chỉ tính khi cần (lazy)
    print(f"  List: {sys.getsizeof(list_comp)} bytes")  # Kích thước list (lớn)
    print(f"  Generator: {sys.getsizeof(gen_exp)} bytes")  # Kích thước generator (nhỏ hơn nhiều)

    print()                                  # In dòng trống


# === Dataclass ===
@dataclass                                   # Decorator tự tạo __init__, __repr__, __eq__
class SinhVien:                              # Class sinh viên dùng dataclass
    ten: str                                 # Thuộc tính tên (type hint: str)
    mssv: str                                # Mã số sinh viên
    diem: List[float] = field(default_factory=list)  # List điểm, mặc định = [] (dùng field)

    @property                                # @property biến method thành thuộc tính
    def diem_tb(self) -> float:              # Tính điểm trung bình (-> float = kiểu trả về)
        if not self.diem:                    # Nếu list điểm rỗng
            return 0.0                       # Trả về 0.0 tránh lỗi chia cho 0
        return sum(self.diem) / len(self.diem)  # Tính trung bình = tổng / số lượng

    @property                                # Thuộc tính xếp loại
    def xep_loai(self) -> str:               # Xếp loại dựa trên điểm TB
        dtb = self.diem_tb                   # Lấy điểm TB từ property ở trên
        if dtb >= 9:                         # Kiểm tra các mức xếp loại
            return "Xuat sac"                # >= 9: Xuất sắc
        elif dtb >= 8:                       # >= 8: Giỏi
            return "Gioi"
        elif dtb >= 7:                       # >= 7: Khá
            return "Kha"
        elif dtb >= 5:                       # >= 5: Trung bình
            return "Trung binh"
        return "Yeu"                         # < 5: Yếu


@dataclass(order=True)                       # order=True cho phép so sánh (<, >, ==) giữa các object
class Product:                               # Class sản phẩm có thể sắp xếp
    sort_index: float = field(init=False, repr=False)  # Trường ẩn dùng để sắp xếp (không hiện trong init/repr)
    ten: str                                 # Tên sản phẩm
    gia: float                               # Giá sản phẩm
    so_luong: int = 0                        # Số lượng, mặc định 0

    def __post_init__(self):                 # Chạy sau __init__, dùng để tính toán bổ sung
        self.sort_index = self.gia           # Dùng giá làm tiêu chí sắp xếp

    @property                                # Thuộc tính tính toán
    def tong_gia_tri(self):                  # Tổng giá trị = giá x số lượng
        return self.gia * self.so_luong      # Trả về tổng


def demo_dataclass():                        # Hàm demo dataclass
    """Demo dataclass."""                    # Docstring
    print("=" * 50)                          # In đường kẻ
    print("=== DATACLASS ===")               # In tiêu đề
    print("=" * 50)                          # In đường kẻ

    # SinhVien
    print("\n--- Sinh Vien ---")             # In tiêu đề
    students = [                             # Tạo list sinh viên
        SinhVien("Nguyen Van A", "SV001", [8.5, 9.0, 7.5]),  # Tạo SinhVien (dataclass tự có __init__)
        SinhVien("Tran Thi B", "SV002", [9.0, 9.5, 9.0]),    # Sinh viên 2
        SinhVien("Le Van C", "SV003", [6.0, 5.5, 7.0]),      # Sinh viên 3
    ]
    for sv in students:                      # Lặp qua từng sinh viên
        print(f"  {sv.ten} ({sv.mssv}): DTB={sv.diem_tb:.1f} - {sv.xep_loai}")  # In thông tin

    # Product
    print("\n--- San Pham (sap xep theo gia) ---")  # In tiêu đề
    products = [                             # Tạo list sản phẩm
        Product("Laptop", 15000000, 10),     # Sản phẩm 1
        Product("Phone", 8000000, 20),       # Sản phẩm 2
        Product("Tablet", 12000000, 5),      # Sản phẩm 3
        Product("Earbuds", 2000000, 50),     # Sản phẩm 4
    ]
    for p in sorted(products):               # sorted() sắp xếp theo sort_index (= giá)
        print(f"  {p.ten}: {p.gia:>12,.0f} VND x {p.so_luong} = {p.tong_gia_tri:>14,.0f} VND")  # In format đẹp

    print()                                  # In dòng trống


# === Iterator class ===
class Range:                                 # Tự tạo class Range giống range() của Python
    """Reimplementation don gian cua range()."""  # Docstring

    def __init__(self, start, stop=None, step=1):  # Constructor linh hoạt: Range(5) hoặc Range(1,10,2)
        if stop is None:                     # Nếu chỉ truyền 1 tham số: Range(n)
            start, stop = 0, start           # Thì start=0, stop=n (giống range(n))
        self.start = start                   # Lưu giá trị bắt đầu
        self.stop = stop                     # Lưu giá trị kết thúc
        self.step = step                     # Lưu bước nhảy
        self.current = start                 # Giá trị hiện tại (dùng khi lặp)

    def __iter__(self):                      # __iter__ trả về iterator (bắt buộc cho for...in)
        self.current = self.start            # Reset về đầu khi bắt đầu lặp mới
        return self                          # Trả về chính nó (object là iterator của chính nó)

    def __next__(self):                      # __next__ trả về giá trị tiếp theo
        if (self.step > 0 and self.current >= self.stop) or \
           (self.step < 0 and self.current <= self.stop):  # Kiểm tra đã hết range chưa
            raise StopIteration              # StopIteration = tín hiệu hết phần tử (for tự bắt)
        value = self.current                 # Lưu giá trị hiện tại
        self.current += self.step            # Tăng current thêm step
        return value                         # Trả về giá trị


def demo_iterator():                         # Hàm demo iterator tự tạo
    """Demo iterator."""                     # Docstring
    print("=" * 50)                          # In đường kẻ
    print("=== CUSTOM ITERATOR ===")         # In tiêu đề
    print("=" * 50)                          # In đường kẻ

    print("\n--- Range(1, 10, 2) ---")       # Demo Range bước 2
    print(f"  {list(Range(1, 10, 2))}")      # list() chuyển iterator thành list

    print("\n--- Range(10, 0, -3) ---")      # Demo Range đếm ngược
    print(f"  {list(Range(10, 0, -3))}")     # Đếm từ 10 về 0, bước -3

    print()                                  # In dòng trống


# === Main ===
if __name__ == "__main__":                   # Chỉ chạy khi thực thi file trực tiếp
    demo_collections()                       # Gọi demo collections
    demo_generators()                        # Gọi demo generators
    demo_dataclass()                         # Gọi demo dataclass
    demo_iterator()                          # Gọi demo iterator
