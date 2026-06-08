# Collections, Generators, Dataclasses demo
from collections import Counter, defaultdict, deque  # Import các cấu trúc dữ liệu đặc biệt
from dataclasses import dataclass, field     # dataclass = cách tạo class ngắn gọn
from typing import List                      # List dùng cho type hint (gợi ý kiểu dữ liệu)
import itertools                             # Module chứa các hàm tạo iterator nâng cao

# === COUNTER ===
print("=== COUNTER ===")                     # Counter = đếm tần suất xuất hiện
text = "python is great python is easy python is powerful"  # Chuỗi cần đếm từ
word_count = Counter(text.split())           # .split() tách thành list từ, Counter đếm mỗi từ
print(f"Đếm từ: {dict(word_count)}")         # Chuyển Counter thành dict để in
print(f"Top 3: {word_count.most_common(3)}") # .most_common(3) = 3 từ xuất hiện nhiều nhất

# === DEFAULTDICT ===
print("\n=== DEFAULTDICT ===")               # defaultdict = dict tự tạo giá trị mặc định nếu key chưa có
grades = [("An", 8), ("Binh", 7), ("An", 9), ("Cuong", 6), ("Binh", 8)]  # List tuple (tên, điểm)
student_grades = defaultdict(list)           # Tạo defaultdict, giá trị mặc định là list rỗng []
for name, grade in grades:                   # Lặp qua từng tuple, unpack thành name và grade
    student_grades[name].append(grade)       # Thêm điểm vào list của sinh viên (tự tạo key nếu chưa có)

for name, g in student_grades.items():       # Lặp qua từng cặp (tên, list điểm)
    avg = sum(g) / len(g)                    # Tính điểm trung bình
    print(f"  {name}: {g} -> TB: {avg:.1f}") # In tên, list điểm và điểm TB

# === DEQUE ===
print("\n=== DEQUE (Queue) ===")             # deque = hàng đợi hai đầu, thêm/xóa O(1) ở cả hai đầu
queue = deque(maxlen=5)                      # Tạo deque tối đa 5 phần tử (tự xóa cũ nhất khi đầy)
for i in range(7):                           # Lặp từ 0 đến 6 (7 phần tử, nhưng deque chỉ giữ 5)
    queue.append(i)                          # .append() thêm vào cuối, nếu đầy sẽ xóa đầu
    print(f"  Thêm {i}: {list(queue)}")      # In trạng thái deque sau mỗi lần thêm

# === GENERATOR ===
print("\n=== GENERATOR: Fibonacci ===")      # Generator = hàm sinh giá trị lười biếng (lazy), tiết kiệm RAM

def fibonacci():                             # Hàm generator sinh dãy Fibonacci vô hạn
    a, b = 0, 1                              # Khởi tạo 2 số đầu: F(0)=0, F(1)=1
    while True:                              # Vòng lặp vô hạn (generator chỉ sinh khi được yêu cầu)
        yield a                              # yield = trả về giá trị và "tạm dừng" hàm (khác return)
        a, b = b, a + b                      # Tính số tiếp theo: a=b, b=a+b (gán đồng thời)

fib = fibonacci()                            # Tạo generator object (chưa chạy code bên trong)
fib_10 = [next(fib) for _ in range(10)]      # next() lấy giá trị tiếp theo từ generator, lặp 10 lần
print(f"10 số Fibonacci: {fib_10}")          # In 10 số Fibonacci đầu tiên

# === DATACLASS ===
print("\n=== DATACLASS ===")                 # @dataclass tự tạo __init__, __repr__, __eq__ cho class

@dataclass                                   # Decorator biến class thành dataclass
class SanPham:                               # Định nghĩa class SanPham
    ten: str                                 # Thuộc tính tên, kiểu str (type hint)
    gia: float                               # Thuộc tính giá, kiểu float
    so_luong: int = 0                        # Thuộc tính số lượng, mặc định = 0

    @property                                # @property biến method thành thuộc tính (truy cập không cần ())
    def tong_gia_tri(self):                  # Method tính tổng giá trị = giá x số lượng
        return self.gia * self.so_luong      # Trả về tổng giá trị tồn kho

    def __str__(self):                       # Định nghĩa cách in object
        return f"{self.ten}: {self.gia:,.0f}đ x {self.so_luong} = {self.tong_gia_tri:,.0f}đ"  # Format tiền VN

kho = [                                      # Tạo list các sản phẩm trong kho
    SanPham("Laptop", 15_000_000, 10),       # Tạo object SanPham (dataclass tự có __init__)
    SanPham("Chuột", 200_000, 50),           # Sản phẩm thứ 2
    SanPham("Bàn phím", 800_000, 30),        # Sản phẩm thứ 3
    SanPham("Màn hình", 5_000_000, 15),      # Sản phẩm thứ 4
]

for sp in kho:                               # Lặp qua từng sản phẩm
    print(f"  {sp}")                         # print(sp) tự gọi __str__()

tong = sum(sp.tong_gia_tri for sp in kho)    # Generator expression tính tổng giá trị toàn kho
print(f"\n  Tổng giá trị kho: {tong:,.0f}đ") # In tổng với dấu phẩy phân cách

# === ITERTOOLS ===
print("\n=== ITERTOOLS ===")                 # itertools = module chứa công cụ xử lý iterator
teams = ["A", "B", "C", "D"]                # List các đội
matches = list(itertools.combinations(teams, 2))  # combinations(list, 2) = tất cả tổ hợp 2 phần tử
print(f"Lịch thi đấu ({len(matches)} trận):")    # In số trận đấu
for i, (t1, t2) in enumerate(matches, 1):    # Lặp với số thứ tự, unpack tuple thành t1, t2
    print(f"  Trận {i}: {t1} vs {t2}")       # In từng trận đấu
