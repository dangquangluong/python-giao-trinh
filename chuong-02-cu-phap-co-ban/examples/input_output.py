"""
Chuong 2: Vi du ve nhap xuat du lieu
"""

# === Ham print() ===
print("=== Cac cach su dung print() ===")

# In co ban
print("Hello, Python!")

# In nhieu gia tri
ten = "An"
tuoi = 25
print("Ten:", ten, "- Tuoi:", tuoi)

# Thay doi separator
print("2024", "01", "15", sep="-")

# Khong xuong dong
print("Loading", end="")
print("...", end="")
print(" Done!")
print()

# === Dinh dang chuoi ===
print("=== Dinh Dang Chuoi ===")

# f-string
diem = 8.567
print(f"Diem trung binh: {diem:.2f}")
print(f"Diem lam tron: {diem:.1f}")

# Can chinh
for i in range(1, 6):
    print(f"| {i:>3} | {'*' * i:<10} | {i**2:>5} |")
print()

# === Dinh dang so ===
print("=== Dinh Dang So ===")
so_lon = 1234567890
print(f"So lon: {so_lon:,}")           # 1,234,567,890
print(f"Phan tram: {0.856:.1%}")       # 85.6%
print(f"Nhi phan: {42:b}")             # 101010
print(f"Thap luc: {255:x}")            # ff
print(f"Bat phan: {8:o}")              # 10
print()

# === Nhap du lieu (demo voi gia tri mac dinh) ===
print("=== Demo Input ===")
print("(Trong vi du nay su dung gia tri mac dinh)")

# Trong thuc te se dung:
# ten = input("Nhap ten: ")
# tuoi = int(input("Nhap tuoi: "))

ten = "Nguyen Van A"
tuoi = 22
chieu_cao = 1.72

print(f"\n--- Thong tin ---")
print(f"Ten: {ten}")
print(f"Tuoi: {tuoi}")
print(f"Chieu cao: {chieu_cao}m")
print(f"Nam sinh: {2024 - tuoi}")
