# Ví dụ về vòng lặp và cấu trúc điều khiển

# === FIZZBUZZ ===
print("=== FizzBuzz ===")                    # In tiêu đề bài FizzBuzz
for i in range(1, 31):                       # for lặp i từ 1 đến 30, range(1,31) không bao gồm 31
    if i % 15 == 0:                          # % = chia lấy dư, nếu chia hết cho cả 3 và 5
        print("FizzBuzz", end=" ")           # In "FizzBuzz", end=" " không xuống dòng
    elif i % 3 == 0:                         # elif = else if, kiểm tra chia hết cho 3
        print("Fizz", end=" ")               # In "Fizz" nếu chia hết cho 3
    elif i % 5 == 0:                         # Kiểm tra chia hết cho 5
        print("Buzz", end=" ")               # In "Buzz" nếu chia hết cho 5
    else:                                    # Nếu không thỏa điều kiện nào ở trên
        print(i, end=" ")                    # In số i
    if i % 10 == 0:                          # Mỗi 10 số thì xuống dòng cho dễ đọc
        print()                              # print() không tham số = xuống dòng

# === LIST COMPREHENSION ===
print("\n\n=== List Comprehension ===")      # List comprehension = cách tạo list ngắn gọn
binh_phuong = [x**2 for x in range(1, 11)]  # Tạo list [1,4,9,...,100] - x**2 = x mũ 2
print(f"Bình phương: {binh_phuong}")         # In list các số bình phương

chan = [x for x in range(1, 21) if x % 2 == 0]  # Lọc số chẵn: chỉ lấy x nếu x%2==0
print(f"Số chẵn: {chan}")                    # In list các số chẵn từ 1-20

# Số nguyên tố
nguyen_to = [n for n in range(2, 50) if all(n % i != 0 for i in range(2, int(n**0.5)+1))]  # all() kiểm tra n không chia hết cho số nào từ 2 đến căn(n)
print(f"Nguyên tố < 50: {nguyen_to}")        # In danh sách số nguyên tố nhỏ hơn 50

# === TAM GIÁC SAO ===
print("\n=== Tam giác sao ===")              # In hình tam giác bằng dấu *
n = 5                                        # Số dòng của tam giác
for i in range(1, n + 1):                    # Lặp từ dòng 1 đến dòng n
    print(" " * (n - i) + "*" * (2*i - 1))   # In khoảng trắng (căn giữa) + số sao tăng dần

# === ENUMERATE ===
print("\n=== Enumerate ===")                 # enumerate = lặp kèm theo số thứ tự (index)
mon_hoc = ["Python", "JavaScript", "Rust", "Go"]  # List các môn học
for i, mon in enumerate(mon_hoc, 1):         # enumerate(list, 1) = đánh số từ 1, trả về (index, value)
    print(f"  {i}. {mon}")                   # In số thứ tự và tên môn học

# === WHILE + BREAK ===
print("\n=== Tìm số chia hết cho 7 và 11 ===")  # Bài toán tìm số nhỏ nhất
n = 1                                        # Bắt đầu từ 1
while True:                                  # while True = vòng lặp vô hạn, cần break để thoát
    if n % 7 == 0 and n % 11 == 0:           # and = cả hai điều kiện đều đúng
        print(f"Số nhỏ nhất chia hết cho 7 và 11: {n}")  # In kết quả
        break                                # break = thoát khỏi vòng lặp while
    n += 1                                   # n += 1 tương đương n = n + 1, tăng n lên 1
