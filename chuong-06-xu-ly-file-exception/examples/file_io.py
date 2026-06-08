# Ví dụ File I/O và Exception Handling
import json
import os
from pathlib import Path

# === GHI FILE ===
print("=== GHI FILE ===")
data = [
    {"ten": "Nguyễn A", "tuoi": 22, "diem": 8.5},
    {"ten": "Trần B", "tuoi": 21, "diem": 7.0},
    {"ten": "Lê C", "tuoi": 23, "diem": 9.2},
]

# Ghi JSON
with open("/tmp/students.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
print("Đã ghi /tmp/students.json")

# Ghi text
with open("/tmp/report.txt", "w", encoding="utf-8") as f:
    f.write("=== BÁO CÁO SINH VIÊN ===\n\n")
    for sv in data:
        f.write(f"{sv['ten']} | Tuổi: {sv['tuoi']} | Điểm: {sv['diem']}\n")
    tb = sum(s["diem"] for s in data) / len(data)
    f.write(f"\nĐiểm trung bình lớp: {tb:.2f}\n")
print("Đã ghi /tmp/report.txt")

# === ĐỌC FILE ===
print("\n=== ĐỌC FILE ===")
with open("/tmp/report.txt", "r", encoding="utf-8") as f:
    print(f.read())

# === ĐỌC JSON ===
print("=== ĐỌC JSON ===")
with open("/tmp/students.json", "r", encoding="utf-8") as f:
    loaded = json.load(f)
    for sv in loaded:
        print(f"  {sv['ten']}: {sv['diem']}")

# === EXCEPTION HANDLING ===
print("\n=== EXCEPTION ===")

def doc_va_xu_ly(filepath):
    try:
        with open(filepath, "r") as f:
            content = f.read()
            return content
    except FileNotFoundError:
        print(f"  ❌ File không tồn tại: {filepath}")
    except PermissionError:
        print(f"  ❌ Không có quyền đọc: {filepath}")
    except Exception as e:
        print(f"  ❌ Lỗi: {type(e).__name__}: {e}")
    return None

doc_va_xu_ly("/tmp/students.json")   # OK
doc_va_xu_ly("/tmp/khong_co.txt")    # FileNotFoundError

# === PATHLIB ===
print("\n=== PATHLIB ===")
p = Path("/tmp")
py_files = list(p.glob("*.json"))
print(f"File JSON trong /tmp: {[f.name for f in py_files]}")

# Dọn dẹp
os.remove("/tmp/students.json")
os.remove("/tmp/report.txt")
print("\n✅ Đã dọn dẹp file tạm")
