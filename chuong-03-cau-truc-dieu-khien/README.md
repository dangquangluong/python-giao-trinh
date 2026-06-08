# Chương 3: Cấu Trúc Điều Khiển

## 3.1 If / Elif / Else

```python
diem = 75                          # Gán giá trị điểm

if diem >= 90:                     # if kiểm tra điều kiện đầu tiên (>= 90)
    print("Xuất sắc! 🌟")         # Chạy nếu điều kiện if đúng (True)
elif diem >= 80:                   # elif = else if, kiểm tra nếu if sai
    print("Giỏi! 👍")             # Chạy nếu 80 <= diem < 90
elif diem >= 65:                   # Tiếp tục kiểm tra nếu trên vẫn sai
    print("Khá!")                  # Chạy nếu 65 <= diem < 80
elif diem >= 50:                   # Kiểm tra tiếp
    print("Trung bình")           # Chạy nếu 50 <= diem < 65
else:                              # else = trường hợp còn lại (không cần điều kiện)
    print("Yếu - Cần cố gắng 💪") # Chạy nếu tất cả if/elif đều sai
```

### Toán Tử So Sánh

```python
# ==, !=, <, >, <=, >=            # Các toán tử so sánh cơ bản
# and, or, not                    # Toán tử logic (và, hoặc, phủ định)
# in, not in                      # Kiểm tra phần tử có trong list/str không
# is, is not                      # So sánh cùng object (dùng với None)

x = 10                             # Gán giá trị x = 10
if 0 < x < 100:                   # Chain comparison: kiểm tra x nằm giữa 0 và 100
    print("x trong khoảng 0-100") # In nếu điều kiện đúng

fruits = ["apple", "banana"]       # Tạo list
if "apple" in fruits:              # "in" kiểm tra "apple" có trong list không
    print("Có apple!")             # In nếu tìm thấy
```

### Ternary (Biểu thức điều kiện)

```python
tuoi = 20                                          # Gán tuổi
loai = "Người lớn" if tuoi >= 18 else "Trẻ em"    # Ternary: giá_trị_đúng if điều_kiện else giá_trị_sai
print(loai)                                        # In kết quả: "Người lớn"
```

## 3.2 Vòng Lặp For

```python
# Lặp qua range
for i in range(5):         # range(5) tạo dãy 0,1,2,3,4 - for lặp qua từng giá trị
    print(i)               # In giá trị i mỗi vòng lặp

for i in range(1, 11):    # range(1,11) = dãy từ 1 đến 10 (không bao gồm 11)
    print(i)               # In 1 đến 10

for i in range(0, 20, 2): # range(start, stop, step) - bước nhảy 2
    print(i)               # In 0, 2, 4, 6, ..., 18

# Lặp qua list
mon_hoc = ["Python", "Java", "SQL", "Git"]  # Tạo list các môn học
for mon in mon_hoc:        # for lặp qua từng phần tử trong list
    print(f"  - {mon}")    # In từng môn học

# enumerate (lặp với index)
for i, mon in enumerate(mon_hoc, start=1):  # enumerate trả về (index, value), start=1 đánh số từ 1
    print(f"  {i}. {mon}")                  # In số thứ tự và tên môn

# Lặp qua dict
sv = {"ten": "A", "tuoi": 22, "diem": 8.5}  # Tạo dictionary
for key, value in sv.items():                # .items() trả về từng cặp (key, value)
    print(f"  {key} = {value}")              # In từng cặp key=value

# Lặp qua string
for ch in "Python":        # Chuỗi cũng là iterable, lặp qua từng ký tự
    print(ch, end=" ")     # In từng ký tự, end=" " không xuống dòng: P y t h o n
```

## 3.3 Vòng Lặp While

```python
# Đếm ngược
n = 10                             # Khởi tạo biến đếm
while n > 0:                       # while lặp khi điều kiện còn True
    print(f"{n}...", end=" ")      # In giá trị n
    n -= 1                         # Giảm n đi 1 (n = n - 1), quan trọng để tránh lặp vô hạn
print("Phóng! 🚀")                # Chạy sau khi while kết thúc (n = 0)

# Input validation
while True:                        # Vòng lặp vô hạn (cần break để thoát)
    tuoi = input("Nhập tuổi (1-150): ")  # Nhận input từ người dùng
    if tuoi.isdigit() and 1 <= int(tuoi) <= 150:  # .isdigit() kiểm tra có phải số, chain comparison
        break                      # break thoát khỏi vòng while khi input hợp lệ
    print("Tuổi không hợp lệ, thử lại!")  # In nếu input sai, lặp lại
```

## 3.4 Break, Continue, Else

```python
# break - thoát vòng lặp
for i in range(100):               # Lặp từ 0 đến 99
    if i == 5:                     # Khi i = 5
        break                      # Thoát khỏi vòng for ngay lập tức
    print(i)  # 0, 1, 2, 3, 4     # Chỉ in được 0-4, vì i=5 thì break

# continue - bỏ qua lần lặp hiện tại
for i in range(10):                # Lặp từ 0 đến 9
    if i % 2 == 0:                 # Nếu i chẵn (chia 2 dư 0)
        continue                   # Bỏ qua, nhảy đến lần lặp tiếp theo
    print(i)  # 1, 3, 5, 7, 9     # Chỉ in số lẻ

# for-else: else chạy khi KHÔNG có break
for i in range(2, 20):             # Lặp i từ 2 đến 19
    for j in range(2, i):          # Lặp j từ 2 đến i-1 (kiểm tra ước số)
        if i % j == 0:             # Nếu i chia hết cho j (không phải nguyên tố)
            break                  # Thoát vòng for j
    else:                          # else của for: chỉ chạy nếu KHÔNG có break
        print(f"{i} là số nguyên tố")  # In số nguyên tố (không bị break)
```

## 3.5 List Comprehension

Cách viết gọn để tạo list:

```python
# Bình thường
binh_phuong = []                   # Tạo list rỗng
for i in range(1, 11):             # Lặp 1 đến 10
    binh_phuong.append(i ** 2)     # Thêm bình phương vào list

# List comprehension (ngắn gọn hơn)
binh_phuong = [i ** 2 for i in range(1, 11)]  # Cú pháp: [biểu_thức for biến in iterable]
print(binh_phuong)  # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# Với điều kiện
chan = [x for x in range(20) if x % 2 == 0]  # Thêm if để lọc: chỉ lấy x chẵn
print(chan)  # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

# Lồng nhau
matrix = [[i*3+j for j in range(3)] for i in range(3)]  # List comprehension lồng = tạo list 2 chiều
# [[0,1,2], [3,4,5], [6,7,8]]

# Dict comprehension
binh_phuong_dict = {x: x**2 for x in range(1, 6)}  # Tạo dict: {key: value for ...}
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# Set comprehension
unique_lengths = {len(word) for word in ["hi", "hello", "hey"]}  # Tạo set độ dài (tự loại trùng)
# {2, 3, 5}
```

## 3.6 Match-Case (Python 3.10+)

```python
command = "start"                  # Giá trị cần so khớp

match command:                     # match = switch/case trong Python (3.10+)
    case "start":                  # case kiểm tra command == "start"
        print("Bắt đầu!")         # Chạy nếu khớp
    case "stop":                   # Kiểm tra == "stop"
        print("Dừng lại!")
    case "pause":                  # Kiểm tra == "pause"
        print("Tạm dừng")
    case _:                        # _ = wildcard, khớp mọi giá trị còn lại (giống else)
        print("Lệnh không hợp lệ")

# Pattern matching với destructuring
point = (3, 4)                     # Tuple cần so khớp
match point:                       # Match với pattern phức tạp
    case (0, 0):                   # Khớp tuple (0, 0) - gốc tọa độ
        print("Gốc tọa độ")
    case (x, 0):                   # Khớp tuple có y=0, gán giá trị x
        print(f"Trên trục X: x={x}")
    case (0, y):                   # Khớp tuple có x=0, gán giá trị y
        print(f"Trên trục Y: y={y}")
    case (x, y):                   # Khớp mọi tuple 2 phần tử, gán x và y
        print(f"Điểm ({x}, {y})")
```

## 3.7 Bài Tập

1. FizzBuzz: in 1-100, chia hết 3→Fizz, 5→Buzz, cả hai→FizzBuzz
2. Tính giai thừa n! bằng while
3. In hình tam giác sao (input số dòng)
4. List comprehension: lọc số nguyên tố từ 1-100
5. Trò chơi đoán số (random 1-100, user nhập cho đến khi đúng)

---

📖 **Trước đó**: [Chương 2](../chuong-02-cu-phap-co-ban/README.md) | **Tiếp theo**: [Chương 4](../chuong-04-ham-va-module/README.md)
