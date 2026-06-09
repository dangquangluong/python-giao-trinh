# Lời Giải Chương 6

## Bài 1: Đếm dòng/từ/ký tự

```python
def dem_file(path):                          # Hàm đếm
    with open(path, "r", encoding="utf-8") as f:  # Mở file đọc
        noi_dung = f.read()                  # Đọc toàn bộ

    so_dong = noi_dung.count("\n") + 1       # Đếm xuống dòng + 1
    so_tu = len(noi_dung.split())            # Tách theo khoảng trắng → đếm
    so_ky_tu = len(noi_dung)                 # Đếm ký tự (bao gồm spaces)

    print(f"  Dòng: {so_dong}")
    print(f"  Từ: {so_tu}")
    print(f"  Ký tự: {so_ky_tu}")

# Test: tạo file tạm rồi đếm
with open("/tmp/test.txt", "w") as f:
    f.write("Hello World\nXin chào Python\nDòng ba")

dem_file("/tmp/test.txt")                    # 3 dòng, 7 từ, 36 ký tự
```

## Bài 2: CSV → JSON

```python
import csv                                   # Module đọc CSV
import json                                  # Module xử lý JSON

def csv_to_json(csv_path, json_path):
    sinh_vien = []                           # List chứa kết quả

    with open(csv_path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)           # Đọc CSV có header
        for row in reader:                   # Mỗi row là dict
            sinh_vien.append({
                "ten": row["ten"],
                "tuoi": int(row["tuoi"]),    # Chuyển string → int
                "diem": float(row["diem"]),  # Chuyển string → float
            })

    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(sinh_vien, f, ensure_ascii=False, indent=2)  # Ghi JSON đẹp

    print(f"Đã chuyển {len(sinh_vien)} sinh viên sang JSON!")

# Tạo CSV test
with open("/tmp/sv.csv", "w") as f:
    f.write("ten,tuoi,diem\nAn,20,8.5\nBinh,21,7.0\n")

csv_to_json("/tmp/sv.csv", "/tmp/sv.json")
```

## Bài 3: Custom Exception

```python
class ValidationError(Exception):            # Kế thừa Exception
    def __init__(self, field, message):       # Nhận field + message
        self.field = field
        self.message = message
        super().__init__(f"{field}: {message}")

def validate_dang_ky(email, mat_khau):       # Hàm validate
    errors = []                              # List lỗi

    if "@" not in email:                     # Email phải có @
        errors.append(ValidationError("email", "phải chứa @"))

    if len(mat_khau) < 8:                    # Mật khẩu >= 8 ký tự
        errors.append(ValidationError("mat_khau", f"phải >= 8 ký tự (hiện {len(mat_khau)})"))

    if errors:                               # Nếu có lỗi
        for e in errors:
            print(f"  ❌ {e}")
        return False
    print("  ✅ Hợp lệ!")
    return True

validate_dang_ky("test@mail.com", "12345678")  # ✅
validate_dang_ky("invalid", "123")              # ❌ ❌
```
