# Ví dụ về hàm, lambda, decorator
import time                                  # Import module time để đo thời gian

# === HÀM CƠ BẢN ===
def tinh_bmi(can_nang, chieu_cao):           # def = định nghĩa hàm, nhận 2 tham số
    """Tính chỉ số BMI"""                    # Docstring: mô tả ngắn về hàm
    bmi = can_nang / (chieu_cao ** 2)        # Công thức BMI = cân nặng / chiều cao bình phương
    if bmi < 18.5:                           # if kiểm tra điều kiện phân loại BMI
        phan_loai = "Gầy"                    # Gán chuỗi phân loại tương ứng
    elif bmi < 25:                           # elif = else if, kiểm tra điều kiện tiếp
        phan_loai = "Bình thường"            # BMI 18.5-25 là bình thường
    elif bmi < 30:                           # Kiểm tra thừa cân
        phan_loai = "Thừa cân"              # BMI 25-30 là thừa cân
    else:                                    # Còn lại (BMI >= 30)
        phan_loai = "Béo phì"               # BMI >= 30 là béo phì
    return bmi, phan_loai                    # return trả về 2 giá trị (tuple)

bmi, loai = tinh_bmi(70, 1.75)              # Gọi hàm, unpack 2 giá trị trả về vào 2 biến
print(f"BMI: {bmi:.1f} - {loai}")            # In kết quả, :.1f = 1 số thập phân

# === *ARGS, **KWARGS ===
def log(*args, level="INFO", **kwargs):      # *args = nhận nhiều tham số vị trí, **kwargs = nhận keyword arguments
    msg = " ".join(str(a) for a in args)     # Nối tất cả args thành chuỗi, cách nhau bởi dấu cách
    extra = ", ".join(f"{k}={v}" for k, v in kwargs.items())  # Nối kwargs thành chuỗi "key=value"
    print(f"[{level}] {msg} {extra}")        # In log với format [LEVEL] message extra_info

log("Server started", "port", 8080, level="INFO", host="localhost")  # Gọi hàm với *args và **kwargs

# === LAMBDA ===
print("\n=== LAMBDA + SORTED ===")           # Lambda = hàm ẩn danh (anonymous function) viết 1 dòng
students = [                                 # List chứa các dict (từ điển) thông tin sinh viên
    {"ten": "An", "diem": 8.5},              # Mỗi dict có key "ten" và "diem"
    {"ten": "Binh", "diem": 7.0},            # Sinh viên thứ 2
    {"ten": "Cuong", "diem": 9.2},           # Sinh viên thứ 3
]
sorted_students = sorted(students, key=lambda s: s["diem"], reverse=True)  # sorted() sắp xếp, lambda lấy điểm làm key, reverse=True = giảm dần
for s in sorted_students:                    # Lặp qua list đã sắp xếp
    print(f"  {s['ten']}: {s['diem']}")      # In tên và điểm

# === DECORATOR ===
print("\n=== DECORATOR ===")                 # Decorator = hàm bọc (wrap) hàm khác để thêm tính năng

def timer(func):                             # Decorator nhận vào một hàm (func) làm tham số
    def wrapper(*args, **kwargs):            # Hàm wrapper thay thế hàm gốc, nhận mọi tham số
        start = time.time()                  # Ghi lại thời điểm bắt đầu
        result = func(*args, **kwargs)       # Gọi hàm gốc và lưu kết quả
        elapsed = time.time() - start        # Tính thời gian chạy = thời điểm kết thúc - bắt đầu
        print(f"  {func.__name__}: {elapsed*1000:.2f}ms")  # In tên hàm và thời gian (mili giây)
        return result                        # Trả về kết quả của hàm gốc
    return wrapper                           # Trả về hàm wrapper (thay thế hàm gốc)

@timer                                       # @decorator = áp dụng decorator lên hàm bên dưới
def tinh_tong(n):                            # Hàm tính tổng 0 đến n-1
    return sum(range(n))                     # sum(range(n)) = 0+1+2+...+(n-1)

@timer                                       # Áp dụng timer cho hàm tinh_tong_bp
def tinh_tong_bp(n):                         # Hàm tính tổng bình phương
    return sum(i**2 for i in range(n))       # Generator expression: tính i^2 cho mỗi i

tinh_tong(1_000_000)                         # Gọi hàm (1_000_000 = 1000000, dấu _ cho dễ đọc)
tinh_tong_bp(100_000)                        # Gọi hàm tính tổng bình phương

# === CLOSURE ===
print("\n=== CLOSURE ===")                   # Closure = hàm bên trong "nhớ" biến của hàm bên ngoài

def multiplier(n):                           # Hàm tạo ra hàm nhân với n
    def multiply(x):                         # Hàm bên trong, "nhớ" giá trị n
        return x * n                         # Trả về x nhân n (n được "đóng" trong closure)
    return multiply                          # Trả về hàm multiply (chưa gọi, chỉ trả về)

double = multiplier(2)                       # Tạo hàm nhân 2 (n=2 được lưu trong closure)
triple = multiplier(3)                       # Tạo hàm nhân 3 (n=3 được lưu trong closure)
print(f"double(5) = {double(5)}")            # double(5) = 5*2 = 10
print(f"triple(5) = {triple(5)}")            # triple(5) = 5*3 = 15

# === ĐỆ QUY ===
print("\n=== ĐỆ QUY: FIBONACCI ===")        # Đệ quy = hàm gọi lại chính nó

def fib(n, memo={}):                         # memo = dict lưu kết quả đã tính (memoization)
    if n <= 1:                               # Trường hợp cơ sở: fib(0)=0, fib(1)=1
        return n                             # Trả về n (0 hoặc 1)
    if n not in memo:                        # Nếu chưa tính fib(n) trước đó
        memo[n] = fib(n-1) + fib(n-2)        # Tính bằng đệ quy: fib(n) = fib(n-1) + fib(n-2)
    return memo[n]                           # Trả về kết quả đã lưu (tránh tính lại)

for i in range(1, 11):                       # Lặp i từ 1 đến 10
    print(f"  fib({i}) = {fib(i)}")          # In số Fibonacci thứ i
