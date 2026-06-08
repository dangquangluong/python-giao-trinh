# Ví dụ File I/O và Exception Handling
import json                                  # Import module json để làm việc với dữ liệu JSON
import os                                    # Import module os để thao tác file/thư mục
from pathlib import Path                     # Import Path từ pathlib - cách hiện đại thao tác đường dẫn

# === GHI FILE ===
print("=== GHI FILE ===")                    # In tiêu đề phần ghi file
data = [                                     # Tạo list chứa các dict (dữ liệu sinh viên)
    {"ten": "Nguyễn A", "tuoi": 22, "diem": 8.5},   # Dict sinh viên 1
    {"ten": "Trần B", "tuoi": 21, "diem": 7.0},     # Dict sinh viên 2
    {"ten": "Lê C", "tuoi": 23, "diem": 9.2},       # Dict sinh viên 3
]

# Ghi JSON
with open("/tmp/students.json", "w", encoding="utf-8") as f:  # with open = mở file an toàn (tự đóng), "w"=ghi đè
    json.dump(data, f, ensure_ascii=False, indent=2)  # json.dump() ghi object Python thành JSON vào file
print("Đã ghi /tmp/students.json")           # Xác nhận đã ghi xong

# Ghi text
with open("/tmp/report.txt", "w", encoding="utf-8") as f:  # Mở file text để ghi
    f.write("=== BÁO CÁO SINH VIÊN ===\n\n")       # f.write() ghi chuỗi vào file, \n = xuống dòng
    for sv in data:                                   # Lặp qua từng sinh viên
        f.write(f"{sv['ten']} | Tuổi: {sv['tuoi']} | Điểm: {sv['diem']}\n")  # Ghi thông tin mỗi sv
    tb = sum(s["diem"] for s in data) / len(data)    # Tính điểm trung bình lớp
    f.write(f"\nĐiểm trung bình lớp: {tb:.2f}\n")   # Ghi điểm TB vào file
print("Đã ghi /tmp/report.txt")              # Xác nhận

# === ĐỌC FILE ===
print("\n=== ĐỌC FILE ===")                  # In tiêu đề phần đọc file
with open("/tmp/report.txt", "r", encoding="utf-8") as f:  # Mở file để đọc ("r" = read)
    print(f.read())                           # f.read() đọc toàn bộ nội dung file thành chuỗi

# === ĐỌC JSON ===
print("=== ĐỌC JSON ===")                   # In tiêu đề
with open("/tmp/students.json", "r", encoding="utf-8") as f:  # Mở file JSON để đọc
    loaded = json.load(f)                    # json.load() đọc JSON từ file thành object Python
    for sv in loaded:                        # Lặp qua danh sách sinh viên đã đọc
        print(f"  {sv['ten']}: {sv['diem']}") # In tên và điểm từ dict

# === EXCEPTION HANDLING ===
print("\n=== EXCEPTION ===")                 # In tiêu đề phần xử lý ngoại lệ (lỗi)

def doc_va_xu_ly(filepath):                  # Hàm đọc file có xử lý lỗi
    try:                                     # try = thử chạy code, nếu lỗi sẽ nhảy sang except
        with open(filepath, "r") as f:       # Thử mở file
            content = f.read()               # Đọc nội dung
            return content                   # Trả về nội dung nếu thành công
    except FileNotFoundError:                # Bắt lỗi file không tồn tại
        print(f"  ❌ File không tồn tại: {filepath}")  # In thông báo lỗi
    except PermissionError:                  # Bắt lỗi không có quyền đọc
        print(f"  ❌ Không có quyền đọc: {filepath}")  # In thông báo
    except Exception as e:                   # Bắt mọi lỗi khác (Exception là lớp cha)
        print(f"  ❌ Lỗi: {type(e).__name__}: {e}")    # In tên loại lỗi và chi tiết
    return None                              # Trả về None nếu có lỗi

doc_va_xu_ly("/tmp/students.json")           # Gọi hàm với file tồn tại - OK
doc_va_xu_ly("/tmp/khong_co.txt")            # Gọi hàm với file không tồn tại - FileNotFoundError

# === PATHLIB ===
print("\n=== PATHLIB ===")                   # Pathlib = thư viện xử lý đường dẫn hiện đại
p = Path("/tmp")                             # Tạo đối tượng Path trỏ đến /tmp
py_files = list(p.glob("*.json"))            # .glob("*.json") tìm tất cả file có đuôi .json
print(f"File JSON trong /tmp: {[f.name for f in py_files]}")  # In tên các file JSON

# Dọn dẹp
os.remove("/tmp/students.json")              # os.remove() xóa file
os.remove("/tmp/report.txt")                 # Xóa file report
print("\n✅ Đã dọn dẹp file tạm")           # Xác nhận dọn dẹp xong
