# Lời Giải Chương 2

## Bài 1: Tính BMI

```python
can_nang = float(input("Cân nặng (kg): "))     # Nhập cân nặng
chieu_cao = float(input("Chiều cao (m): "))     # Nhập chiều cao

bmi = can_nang / (chieu_cao ** 2)               # Công thức BMI

# Xếp loại
if bmi < 18.5:
    loai = "Gầy"
elif bmi < 25:
    loai = "Bình thường"
elif bmi < 30:
    loai = "Thừa cân"
else:
    loai = "Béo phì"

print(f"BMI: {bmi:.1f} - {loai}")               # In kết quả, 1 số thập phân
```

---

## Bài 2: Đếm nguyên âm

```python
chuoi = input("Nhập chuỗi: ")                  # Nhập chuỗi
dem = 0                                          # Biến đếm

for char in chuoi:                              # Duyệt từng ký tự
    if char.lower() in "aeiou":                 # Chuyển thường rồi kiểm tra
        dem += 1                                 # Tăng đếm

print(f"Chuỗi '{chuoi}' có {dem} nguyên âm")
```

---

## Bài 3: Thông tin sinh viên

```python
sinh_vien = [                                   # List chứa 3 dict
    {"ten": "Nguyễn A", "tuoi": 20, "diem": 8.5},
    {"ten": "Trần B", "tuoi": 21, "diem": 7.0},
    {"ten": "Lê C", "tuoi": 22, "diem": 9.2},
]

# In bảng
print(f"{'Tên':<15} {'Tuổi':<6} {'Điểm':<6}")  # Header, < = căn trái
print("-" * 30)                                  # Đường kẻ
for sv in sinh_vien:                             # Duyệt từng sinh viên
    print(f"{sv['ten']:<15} {sv['tuoi']:<6} {sv['diem']:<6}")
```

---

## Bài 4: Tính trung bình

```python
so_list = []                                    # List rỗng chứa các số

while True:                                     # Lặp vô hạn
    nhap = input("Nhập số (hoặc 'stop'): ")    # Nhập
    if nhap.lower() == "stop":                  # Kiểm tra dừng
        break                                    # Thoát vòng lặp
    try:
        so_list.append(float(nhap))             # Thêm số vào list
    except ValueError:                           # Nếu không phải số
        print("Không hợp lệ, thử lại!")

if so_list:                                     # Nếu list không rỗng
    print(f"Trung bình: {sum(so_list)/len(so_list):.2f}")
    print(f"Max: {max(so_list)}")
    print(f"Min: {min(so_list)}")
else:
    print("Chưa nhập số nào!")
```

---

## Bài 5: Palindrome

```python
chuoi = input("Nhập chuỗi: ")                  # Nhập chuỗi
nguoc = chuoi[::-1]                             # Đảo ngược (slicing bước -1)

print(f"Chuỗi gốc: {chuoi}")
print(f"Đảo ngược: {nguoc}")

if chuoi.lower() == nguoc.lower():              # So sánh (bỏ qua hoa/thường)
    print("✅ Là palindrome!")
else:
    print("❌ Không phải palindrome")
```
