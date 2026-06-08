# Ví dụ về vòng lặp và cấu trúc điều khiển

# === FIZZBUZZ ===
print("=== FizzBuzz ===")
for i in range(1, 31):
    if i % 15 == 0:
        print("FizzBuzz", end=" ")
    elif i % 3 == 0:
        print("Fizz", end=" ")
    elif i % 5 == 0:
        print("Buzz", end=" ")
    else:
        print(i, end=" ")
    if i % 10 == 0:
        print()

# === LIST COMPREHENSION ===
print("\n\n=== List Comprehension ===")
binh_phuong = [x**2 for x in range(1, 11)]
print(f"Bình phương: {binh_phuong}")

chan = [x for x in range(1, 21) if x % 2 == 0]
print(f"Số chẵn: {chan}")

# Số nguyên tố
nguyen_to = [n for n in range(2, 50) if all(n % i != 0 for i in range(2, int(n**0.5)+1))]
print(f"Nguyên tố < 50: {nguyen_to}")

# === TAM GIÁC SAO ===
print("\n=== Tam giác sao ===")
n = 5
for i in range(1, n + 1):
    print(" " * (n - i) + "*" * (2*i - 1))

# === ENUMERATE ===
print("\n=== Enumerate ===")
mon_hoc = ["Python", "JavaScript", "Rust", "Go"]
for i, mon in enumerate(mon_hoc, 1):
    print(f"  {i}. {mon}")

# === WHILE + BREAK ===
print("\n=== Tìm số chia hết cho 7 và 11 ===")
n = 1
while True:
    if n % 7 == 0 and n % 11 == 0:
        print(f"Số nhỏ nhất chia hết cho 7 và 11: {n}")
        break
    n += 1
