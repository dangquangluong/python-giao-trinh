# Chương trình Hello World đầu tiên trong Python

# In ra màn hình
print("Xin chào, Python! 🐍")              # print() = hàm in ra màn hình, chuỗi nằm trong dấu ""
print("Đây là chương trình đầu tiên của tôi.")  # In thêm một dòng text khác

# Biến
ten = "Bạn"                                 # Tạo biến ten, gán giá trị chuỗi "Bạn" (str = string)
tuoi = 25                                   # Tạo biến tuoi, gán giá trị số nguyên 25 (int = integer)

# f-string (format string)
print(f"Xin chào, {ten}! Bạn {tuoi} tuổi.")  # f-string: dùng {biến} để chèn giá trị biến vào chuỗi

# Input từ người dùng
# ten_nhap = input("Bạn tên gì? ")         # input() = hàm nhận dữ liệu từ bàn phím (trả về str)
# print(f"Chào {ten_nhap}!")                # In ra giá trị vừa nhập

# Phép tính đơn giản
print(f"2 + 3 = {2 + 3}")                   # Phép cộng, kết quả = 5
print(f"10 / 3 = {10 / 3:.2f}")             # Phép chia, :.2f = làm tròn 2 chữ số thập phân
print(f"2 ** 10 = {2 ** 10}")               # ** = lũy thừa, 2 mũ 10 = 1024
