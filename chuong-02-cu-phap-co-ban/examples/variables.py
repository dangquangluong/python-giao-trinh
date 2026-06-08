# Ví dụ về biến và kiểu dữ liệu

# === BIẾN ===
ten = "Nguyễn Văn A"
tuoi = 25
chieu_cao = 1.75
la_sinh_vien = True

print(f"Tên: {ten}")
print(f"Tuổi: {tuoi} ({type(tuoi).__name__})")
print(f"Cao: {chieu_cao}m ({type(chieu_cao).__name__})")
print(f"Sinh viên: {la_sinh_vien}")

# === LIST ===
print("\n=== LIST ===")
diem = [85, 90, 78, 92, 88]
print(f"Điểm: {diem}")
print(f"TB: {sum(diem)/len(diem):.1f}")
print(f"Max: {max(diem)}, Min: {min(diem)}")

diem.sort()
print(f"Sắp xếp: {diem}")

# === DICT ===
print("\n=== DICTIONARY ===")
sv = {"ten": "Trần B", "tuoi": 22, "diem": 8.5}
for k, v in sv.items():
    print(f"  {k}: {v}")

# === STRING ===
print("\n=== STRING METHODS ===")
text = "  Python Là Tuyệt Vời  "
print(f"strip: '{text.strip()}'")
print(f"upper: '{text.upper()}'")
print(f"lower: '{text.lower()}'")
print(f"split: {text.split()}")
print(f"replace: '{text.replace('Python', 'Rust')}'")

# === SLICING ===
print("\n=== SLICING ===")
s = "Python"
print(f"s[0]   = '{s[0]}'")
print(f"s[2:5] = '{s[2:5]}'")
print(f"s[::-1]= '{s[::-1]}'")
