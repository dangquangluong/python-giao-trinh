"""
Chuong 6: Vi du ve xu ly file va exception
"""

import json                                  # Module xử lý dữ liệu JSON
import os                                    # Module thao tác hệ điều hành (file, thư mục)
from pathlib import Path                     # Path = class hiện đại để xử lý đường dẫn file
from contextlib import contextmanager        # contextmanager = decorator tạo context manager dễ dàng
import time                                  # Module đo thời gian


# === Doc va ghi file text ===
def demo_text_file():                        # Định nghĩa hàm demo đọc/ghi file text
    """Demo doc/ghi file text."""             # Docstring mô tả hàm
    print("=== Doc/Ghi File Text ===")       # In tiêu đề

    # Ghi file
    with open("demo_output.txt", "w", encoding="utf-8") as f:  # Mở file để ghi ("w"=write), encoding utf-8 hỗ trợ tiếng Việt
        f.write("Dong 1: Xin chao Python!\n")       # .write() ghi chuỗi vào file
        f.write("Dong 2: Day la vi du ve file.\n")  # Ghi dòng 2
        f.write("Dong 3: Hoc Python rat thu vi.\n") # Ghi dòng 3

    # Doc file
    with open("demo_output.txt", "r", encoding="utf-8") as f:  # Mở file để đọc ("r"=read)
        for i, line in enumerate(f, 1):      # enumerate đánh số từ 1, lặp qua từng dòng
            print(f"  [{i}] {line.strip()}")  # .strip() xóa khoảng trắng/xuống dòng đầu cuối

    # Xoa file sau khi demo
    os.remove("demo_output.txt")             # os.remove() xóa file
    print()                                  # In dòng trống


# === Doc/Ghi file JSON ===
def demo_json_file():                        # Hàm demo xử lý JSON
    """Demo xu ly JSON."""                   # Docstring
    print("=== Doc/Ghi File JSON ===")       # In tiêu đề

    # Du lieu mau
    sinh_vien = [                            # List chứa các dict sinh viên
        {"ten": "Nguyen Van A", "diem": 8.5, "lop": "CNTT1"},  # Dict sinh viên 1
        {"ten": "Tran Thi B", "diem": 9.0, "lop": "CNTT2"},    # Dict sinh viên 2
        {"ten": "Le Van C", "diem": 7.0, "lop": "CNTT1"},      # Dict sinh viên 3
    ]

    # Ghi JSON
    with open("students.json", "w", encoding="utf-8") as f:    # Mở file JSON để ghi
        json.dump(sinh_vien, f, ensure_ascii=False, indent=2)  # json.dump() chuyển Python object thành JSON rồi ghi
    print("  Da ghi students.json")          # Xác nhận ghi xong

    # Doc JSON
    with open("students.json", "r", encoding="utf-8") as f:    # Mở file JSON để đọc
        data = json.load(f)                  # json.load() đọc JSON từ file thành Python object

    print("  Danh sach sinh vien:")          # In tiêu đề
    for sv in data:                          # Lặp qua từng sinh viên
        print(f"    - {sv['ten']}: {sv['diem']} ({sv['lop']})")  # In thông tin từ dict

    # Xoa file sau khi demo
    os.remove("students.json")               # Xóa file demo
    print()                                  # In dòng trống


# === Exception handling ===
def demo_exceptions():                       # Hàm demo xử lý ngoại lệ (exception)
    """Demo xu ly exception."""              # Docstring
    print("=== Exception Handling ===")      # In tiêu đề

    # Demo 1: ValueError
    values = ["42", "hello", "3.14", "", "100"]  # List các chuỗi, một số không phải số
    for v in values:                         # Lặp qua từng giá trị
        try:                                 # try = thử chạy code bên trong
            num = int(v)                     # int() ép kiểu chuỗi thành số nguyên (có thể lỗi)
            print(f"  '{v}' -> {num}")       # In kết quả nếu thành công
        except ValueError:                   # Bắt lỗi ValueError (chuỗi không phải số)
            print(f"  '{v}' -> [LOI: khong phai so nguyen]")  # In thông báo lỗi

    print()                                  # In dòng trống

    # Demo 2: Try/Except/Else/Finally
    print("  --- Try/Except/Else/Finally ---")  # In tiêu đề
    try:                                     # Thử thực hiện phép chia
        result = 100 / 5                     # Chia 100 cho 5 (có thể lỗi nếu chia cho 0)
    except ZeroDivisionError:                # Bắt lỗi chia cho 0
        print("  Loi chia cho 0!")           # In nếu lỗi chia cho 0
    else:                                    # else chạy khi KHÔNG có lỗi xảy ra
        print(f"  Ket qua: {result}")        # In kết quả thành công
    finally:                                 # finally LUÔN chạy dù có lỗi hay không
        print("  Block finally luon chay")   # In xác nhận

    print()                                  # In dòng trống


# === Custom Exception ===
class InsufficientFundsError(Exception):     # Tạo class lỗi riêng, kế thừa từ Exception
    """Loi so du khong du."""                # Docstring mô tả lỗi
    def __init__(self, balance, amount):     # Constructor nhận số dư và số tiền muốn rút
        self.balance = balance               # Lưu số dư hiện tại
        self.amount = amount                 # Lưu số tiền muốn rút
        super().__init__(                    # Gọi constructor của class cha (Exception)
            f"So du {balance:,} VND khong du de rut {amount:,} VND"  # Truyền message lỗi
        )


class BankAccount:                           # Class tài khoản ngân hàng
    """Tai khoan ngan hang don gian."""       # Docstring

    def __init__(self, owner, balance=0):    # Constructor, balance mặc định = 0
        self.owner = owner                   # Lưu tên chủ tài khoản
        self._balance = balance              # _balance: quy ước private (không truy cập trực tiếp)

    def deposit(self, amount):               # Method nạp tiền
        if amount <= 0:                      # Kiểm tra số tiền hợp lệ
            raise ValueError("So tien nap phai lon hon 0")  # raise = ném ra lỗi
        self._balance += amount              # Cộng số tiền vào số dư
        return self._balance                 # Trả về số dư mới

    def withdraw(self, amount):              # Method rút tiền
        if amount <= 0:                      # Kiểm tra số tiền hợp lệ
            raise ValueError("So tien rut phai lon hon 0")  # Ném lỗi nếu <= 0
        if amount > self._balance:           # Kiểm tra đủ tiền không
            raise InsufficientFundsError(self._balance, amount)  # Ném lỗi custom nếu không đủ
        self._balance -= amount              # Trừ tiền từ số dư
        return self._balance                 # Trả về số dư mới


def demo_custom_exception():                 # Hàm demo lỗi tự định nghĩa
    """Demo custom exception."""             # Docstring
    print("=== Custom Exception ===")        # In tiêu đề

    acc = BankAccount("An", 1000000)         # Tạo tài khoản với số dư 1 triệu
    print(f"  Tai khoan: {acc.owner}, So du: {acc._balance:,} VND")  # In thông tin

    try:                                     # Thử rút tiền nhiều hơn số dư
        acc.withdraw(1500000)                # Rút 1.5 triệu (nhiều hơn 1 triệu)
    except InsufficientFundsError as e:      # Bắt lỗi InsufficientFundsError
        print(f"  LOI: {e}")                 # In message lỗi
        print(f"  So du hien tai: {e.balance:,} VND")    # Truy cập thuộc tính balance của lỗi
        print(f"  So tien can rut: {e.amount:,} VND")    # Truy cập thuộc tính amount

    print()                                  # In dòng trống


# === Context Manager ===
@contextmanager                              # Decorator biến hàm generator thành context manager
def timer(label):                            # Hàm context manager đo thời gian
    """Context manager do thoi gian."""      # Docstring
    start = time.time()                      # Ghi thời điểm bắt đầu
    print(f"  [{label}] Bat dau...")         # In thông báo bắt đầu
    try:                                     # try...finally đảm bảo code finally luôn chạy
        yield                                # yield = điểm mà code bên trong "with" sẽ chạy
    finally:                                 # finally chạy sau khi block "with" kết thúc
        elapsed = time.time() - start        # Tính thời gian đã trôi qua
        print(f"  [{label}] Hoan tat trong {elapsed:.6f}s")  # In thời gian thực thi


def demo_context_manager():                  # Hàm demo context manager
    """Demo context manager."""              # Docstring
    print("=== Context Manager ===")         # In tiêu đề

    with timer("Tinh tong"):                 # with = sử dụng context manager, tự cleanup
        total = sum(range(1000000))          # Tính tổng 0 đến 999999
        print(f"  Tong 0-999999: {total:,}") # In kết quả với dấu phẩy phân cách

    print()                                  # In dòng trống


# === Pathlib ===
def demo_pathlib():                          # Hàm demo thư viện pathlib
    """Demo pathlib."""                       # Docstring
    print("=== Pathlib ===")                 # In tiêu đề

    current = Path(".")                      # Path(".") = đường dẫn thư mục hiện tại
    print(f"  Thu muc hien tai: {current.resolve()}")  # .resolve() trả về đường dẫn tuyệt đối

    # Liet ke file Python trong thu muc hien tai
    py_files = list(current.glob("*.py"))    # .glob("*.py") tìm tất cả file .py
    print(f"  File .py trong thu muc hien tai:")  # In tiêu đề
    for f in py_files:                       # Lặp qua từng file tìm được
        size = f.stat().st_size              # .stat().st_size lấy kích thước file (bytes)
        print(f"    - {f.name} ({size} bytes)")  # In tên file và kích thước

    print()                                  # In dòng trống


# === Main ===
if __name__ == "__main__":                   # Chỉ chạy khi file được thực thi trực tiếp
    demo_text_file()                         # Gọi hàm demo đọc/ghi text
    demo_json_file()                         # Gọi hàm demo JSON
    demo_exceptions()                        # Gọi hàm demo exception
    demo_custom_exception()                  # Gọi hàm demo custom exception
    demo_context_manager()                   # Gọi hàm demo context manager
    demo_pathlib()                           # Gọi hàm demo pathlib
