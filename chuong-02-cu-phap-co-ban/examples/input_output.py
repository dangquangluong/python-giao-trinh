"""
Chuong 2: Vi du ve nhap xuat du lieu
"""

# === Ham print() ===
print("=== Cac cach su dung print() ===")    # In tiêu đề phần demo

# In co ban
print("Hello, Python!")                       # print() in chuỗi ra màn hình rồi xuống dòng

# In nhieu gia tri
ten = "An"                                    # Tạo biến ten (kiểu str)
tuoi = 25                                     # Tạo biến tuoi (kiểu int)
print("Ten:", ten, "- Tuoi:", tuoi)           # print() nhận nhiều tham số, tự thêm dấu cách giữa

# Thay doi separator
print("2024", "01", "15", sep="-")            # sep="-" thay dấu cách mặc định bằng dấu "-"

# Khong xuong dong
print("Loading", end="")                      # end="" không xuống dòng sau khi in
print("...", end="")                           # Tiếp tục in trên cùng dòng
print(" Done!")                                # In xong mới xuống dòng (end mặc định = "\n")
print()                                        # In dòng trống (xuống dòng)

# === Dinh dang chuoi ===
print("=== Dinh Dang Chuoi ===")              # Tiêu đề phần định dạng chuỗi

# f-string
diem = 8.567                                   # Số thực cần định dạng
print(f"Diem trung binh: {diem:.2f}")          # :.2f = hiển thị 2 chữ số thập phân
print(f"Diem lam tron: {diem:.1f}")            # :.1f = hiển thị 1 chữ số thập phân

# Can chinh
for i in range(1, 6):                          # for lặp i từ 1 đến 5, range(1,6) = [1,2,3,4,5]
    print(f"| {i:>3} | {'*' * i:<10} | {i**2:>5} |")  # :>3 căn phải 3 ký tự, :<10 căn trái 10 ký tự
print()                                        # In dòng trống

# === Dinh dang so ===
print("=== Dinh Dang So ===")                  # Tiêu đề phần định dạng số
so_lon = 1234567890                            # Số nguyên lớn
print(f"So lon: {so_lon:,}")                   # :, thêm dấu phẩy phân cách hàng nghìn
print(f"Phan tram: {0.856:.1%}")               # :.1% chuyển thành phần trăm (85.6%)
print(f"Nhi phan: {42:b}")                     # :b chuyển sang hệ nhị phân (binary)
print(f"Thap luc: {255:x}")                    # :x chuyển sang hệ thập lục (hexadecimal)
print(f"Bat phan: {8:o}")                      # :o chuyển sang hệ bát phân (octal)
print()                                        # In dòng trống

# === Nhap du lieu (demo voi gia tri mac dinh) ===
print("=== Demo Input ===")                    # Tiêu đề phần nhập liệu
print("(Trong vi du nay su dung gia tri mac dinh)")  # Giải thích dùng giá trị mẫu

# Trong thuc te se dung:
# ten = input("Nhap ten: ")                    # input() hiện thông báo và chờ người dùng nhập
# tuoi = int(input("Nhap tuoi: "))             # int() ép kiểu chuỗi thành số nguyên

ten = "Nguyen Van A"                           # Gán giá trị mẫu thay vì nhập từ bàn phím
tuoi = 22                                      # Gán tuổi mẫu
chieu_cao = 1.72                               # Gán chiều cao mẫu

print(f"\n--- Thong tin ---")                  # \n = xuống dòng, in tiêu đề
print(f"Ten: {ten}")                           # In tên dùng f-string
print(f"Tuoi: {tuoi}")                         # In tuổi
print(f"Chieu cao: {chieu_cao}m")              # In chiều cao kèm đơn vị
print(f"Nam sinh: {2024 - tuoi}")              # Tính năm sinh = năm hiện tại - tuổi
