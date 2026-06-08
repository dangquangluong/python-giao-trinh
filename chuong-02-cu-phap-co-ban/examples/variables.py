"""
Chuong 2: Vi du ve bien va kieu du lieu
"""

# === Kieu so ===
print("=== Kieu So ===")
so_nguyen = 42
so_thuc = 3.14
so_phuc = 2 + 3j

print(f"So nguyen: {so_nguyen} (type: {type(so_nguyen).__name__})")
print(f"So thuc: {so_thuc} (type: {type(so_thuc).__name__})")
print(f"So phuc: {so_phuc} (type: {type(so_phuc).__name__})")
print()

# === Kieu chuoi ===
print("=== Kieu Chuoi ===")
ten = "Nguyen Van A"
dia_chi = 'Ha Noi, Viet Nam'

print(f"Ten: {ten}")
print(f"Do dai ten: {len(ten)}")
print(f"Chu hoa: {ten.upper()}")
print(f"Chu thuong: {ten.lower()}")
print(f"Thay the: {ten.replace('A', 'B')}")
print()

# === Slicing ===
print("=== Slicing ===")
s = "Python Programming"
print(f"Chuoi: '{s}'")
print(f"s[0:6] = '{s[0:6]}'")
print(f"s[7:] = '{s[7:]}'")
print(f"s[-11:] = '{s[-11:]}'")
print(f"s[::2] = '{s[::2]}'")
print(f"Dao nguoc: '{s[::-1]}'")
print()

# === List ===
print("=== List ===")
fruits = ["tao", "cam", "chuoi", "nho", "xoai"]
print(f"Danh sach: {fruits}")
print(f"Phan tu dau: {fruits[0]}")
print(f"Phan tu cuoi: {fruits[-1]}")
print(f"Slice [1:3]: {fruits[1:3]}")

fruits.append("dua")
print(f"Sau khi them 'dua': {fruits}")

fruits.sort()
print(f"Sau khi sap xep: {fruits}")
print()

# === Dictionary ===
print("=== Dictionary ===")
sinh_vien = {
    "ten": "Tran Thi B",
    "mssv": "SV001",
    "diem_tb": 8.5,
    "mon_hoc": ["Python", "SQL", "Web"]
}

for key, value in sinh_vien.items():
    print(f"  {key}: {value}")
print()

# === Chuyen doi kieu ===
print("=== Chuyen Doi Kieu ===")
x = "123"
print(f"'{x}' -> int: {int(x)}")
print(f"'{x}' -> float: {float(x)}")
print(f"42 -> str: '{str(42)}'")
print(f"[1,2,2,3] -> set: {set([1, 2, 2, 3])}")
