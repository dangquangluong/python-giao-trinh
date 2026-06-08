"""
Chuong 9: Du an CLI Todo App

Su dung:
    python todo_cli.py add "Hoc Python"
    python todo_cli.py list
    python todo_cli.py done 1
    python todo_cli.py delete 1
"""

import json                                  # Module đọc/ghi dữ liệu JSON
import sys                                   # Module truy cập tham số dòng lệnh (sys.argv)
from dataclasses import dataclass, field, asdict  # dataclass tạo class nhanh, asdict chuyển thành dict
from datetime import datetime                # Module xử lý ngày giờ
from pathlib import Path                     # Path = cách hiện đại xử lý đường dẫn file
from typing import List, Optional            # Type hints: List = danh sách, Optional = có thể None


# === Model ===
@dataclass                                   # Decorator tự tạo __init__, __repr__ cho class
class Task:                                  # Class đại diện cho 1 task (công việc)
    id: int                                  # ID duy nhất của task
    title: str                               # Tiêu đề task
    done: bool = False                       # Trạng thái hoàn thành, mặc định = False
    created_at: str = field(default_factory=lambda: datetime.now().isoformat())  # Thời gian tạo (tự động)
    completed_at: Optional[str] = None       # Thời gian hoàn thành (None nếu chưa xong)


# === Storage ===
DATA_FILE = Path("todo_data.json")           # Đường dẫn file lưu trữ dữ liệu (dạng JSON)


def load_tasks() -> List[Task]:              # Hàm đọc danh sách task từ file, trả về List[Task]
    """Doc danh sach task tu file."""         # Docstring
    if not DATA_FILE.exists():               # .exists() kiểm tra file có tồn tại không
        return []                            # Nếu chưa có file, trả về list rỗng
    with open(DATA_FILE, "r", encoding="utf-8") as f:  # Mở file để đọc
        data = json.load(f)                  # Đọc JSON thành list các dict
    return [Task(**item) for item in data]   # **item unpack dict thành keyword arguments cho Task()


def save_tasks(tasks: List[Task]):           # Hàm lưu danh sách task vào file
    """Luu danh sach task vao file."""       # Docstring
    with open(DATA_FILE, "w", encoding="utf-8") as f:  # Mở file để ghi (ghi đè)
        json.dump([asdict(t) for t in tasks], f, ensure_ascii=False, indent=2)  # Chuyển list Task thành list dict rồi ghi JSON


def get_next_id(tasks: List[Task]) -> int:   # Hàm lấy ID tiếp theo (ID lớn nhất + 1)
    """Lay ID tiep theo."""                  # Docstring
    if not tasks:                            # Nếu danh sách rỗng
        return 1                             # Bắt đầu từ 1
    return max(t.id for t in tasks) + 1      # max() tìm ID lớn nhất, cộng 1


# === Commands ===
def cmd_add(title: str):                     # Hàm thêm task mới
    """Them task moi."""                     # Docstring
    tasks = load_tasks()                     # Đọc danh sách task hiện tại
    new_task = Task(id=get_next_id(tasks), title=title)  # Tạo Task mới với ID tự tăng
    tasks.append(new_task)                   # Thêm task mới vào list
    save_tasks(tasks)                        # Lưu list vào file
    print(f"Da them: [{new_task.id}] {new_task.title}")  # In xác nhận


def cmd_list(filter_status: Optional[str] = None):  # Hàm liệt kê task, có thể lọc theo trạng thái
    """Liet ke cac task."""                  # Docstring
    tasks = load_tasks()                     # Đọc danh sách task

    if filter_status == "done":              # Nếu lọc "done" (đã hoàn thành)
        tasks = [t for t in tasks if t.done]  # Chỉ giữ task có done=True
    elif filter_status == "pending":         # Nếu lọc "pending" (chưa xong)
        tasks = [t for t in tasks if not t.done]  # Chỉ giữ task có done=False

    if not tasks:                            # Nếu không có task nào
        print("Khong co task nao.")          # In thông báo
        return                               # Thoát hàm

    print(f"\n{'ID':<4} {'Trang Thai':<12} {'Tieu De'}")  # In header bảng (căn trái)
    print("-" * 50)                          # In đường kẻ phân cách
    for task in tasks:                       # Lặp qua từng task
        status = "[x]" if task.done else "[ ]"  # Ternary: đánh dấu [x] nếu xong, [ ] nếu chưa
        print(f"{task.id:<4} {status:<12} {task.title}")  # In thông tin task
    print(f"\nTong: {len(tasks)} task")      # In tổng số task


def cmd_done(task_id: int):                  # Hàm đánh dấu task đã hoàn thành
    """Danh dau task hoan thanh."""          # Docstring
    tasks = load_tasks()                     # Đọc danh sách task
    for task in tasks:                       # Lặp tìm task theo ID
        if task.id == task_id:               # Nếu tìm thấy ID khớp
            task.done = True                 # Đánh dấu hoàn thành
            task.completed_at = datetime.now().isoformat()  # Ghi thời gian hoàn thành
            save_tasks(tasks)                # Lưu thay đổi
            print(f"Da hoan thanh: [{task.id}] {task.title}")  # In xác nhận
            return                           # Thoát hàm
    print(f"Khong tim thay task voi ID={task_id}")  # Không tìm thấy


def cmd_delete(task_id: int):                # Hàm xóa task
    """Xoa task."""                          # Docstring
    tasks = load_tasks()                     # Đọc danh sách
    original_len = len(tasks)                # Lưu số lượng ban đầu để so sánh
    tasks = [t for t in tasks if t.id != task_id]  # Lọc bỏ task có ID cần xóa

    if len(tasks) == original_len:           # Nếu số lượng không đổi = không tìm thấy
        print(f"Khong tim thay task voi ID={task_id}")  # In thông báo
        return                               # Thoát

    save_tasks(tasks)                        # Lưu danh sách đã xóa
    print(f"Da xoa task ID={task_id}")       # In xác nhận


def cmd_clear():                             # Hàm xóa tất cả task đã hoàn thành
    """Xoa tat ca task da hoan thanh."""     # Docstring
    tasks = load_tasks()                     # Đọc danh sách
    remaining = [t for t in tasks if not t.done]  # Giữ lại task chưa xong
    removed = len(tasks) - len(remaining)    # Tính số task bị xóa
    save_tasks(remaining)                    # Lưu list còn lại
    print(f"Da xoa {removed} task da hoan thanh")  # In số task đã xóa


# === Main ===
def print_usage():                           # Hàm in hướng dẫn sử dụng
    """In huong dan su dung."""              # Docstring
    print("""
Todo CLI - Quan ly cong viec

Su dung:
    python todo_cli.py add <title>       Them task moi
    python todo_cli.py list [filter]     Liet ke task (filter: done/pending)
    python todo_cli.py done <id>         Danh dau hoan thanh
    python todo_cli.py delete <id>       Xoa task
    python todo_cli.py clear             Xoa tat ca task da hoan thanh
    """)


def main():                                  # Hàm chính xử lý command line
    if len(sys.argv) < 2:                    # sys.argv = list tham số dòng lệnh, [0]=tên file
        print_usage()                        # Nếu không có tham số, in hướng dẫn
        return                               # Thoát

    command = sys.argv[1].lower()            # Lấy lệnh (tham số thứ 2), chuyển thường

    if command == "add":                     # Xử lý lệnh "add"
        if len(sys.argv) < 3:                # Kiểm tra có nhập tiêu đề không
            print("Loi: Can nhap tieu de task")  # Thông báo thiếu tiêu đề
            return                           # Thoát
        cmd_add(" ".join(sys.argv[2:]))      # Nối tất cả tham số từ [2:] thành tiêu đề

    elif command == "list":                  # Xử lý lệnh "list"
        filter_status = sys.argv[2] if len(sys.argv) > 2 else None  # Lấy filter nếu có
        cmd_list(filter_status)              # Gọi hàm liệt kê

    elif command == "done":                  # Xử lý lệnh "done"
        if len(sys.argv) < 3:                # Kiểm tra có nhập ID không
            print("Loi: Can nhap ID task")   # Thông báo thiếu ID
            return                           # Thoát
        cmd_done(int(sys.argv[2]))           # Chuyển ID thành int và gọi hàm

    elif command == "delete":                # Xử lý lệnh "delete"
        if len(sys.argv) < 3:                # Kiểm tra có nhập ID không
            print("Loi: Can nhap ID task")   # Thông báo thiếu
            return                           # Thoát
        cmd_delete(int(sys.argv[2]))         # Chuyển ID thành int và gọi hàm xóa

    elif command == "clear":                 # Xử lý lệnh "clear"
        cmd_clear()                          # Gọi hàm xóa task đã hoàn thành

    else:                                    # Lệnh không hợp lệ
        print(f"Lenh khong hop le: {command}")  # In thông báo lỗi
        print_usage()                        # In hướng dẫn


if __name__ == "__main__":                   # Chỉ chạy khi thực thi file trực tiếp (không phải import)
    main()                                   # Gọi hàm main
