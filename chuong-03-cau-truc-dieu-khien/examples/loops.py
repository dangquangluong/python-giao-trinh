"""
Chuong 3: Vi du ve vong lap va dieu kien
"""

# === If/Elif/Else ===
print("=== Xep loai diem ===")
diem_list = [9.5, 8.0, 6.5, 4.0, 7.5]

for diem in diem_list:
    if diem >= 9:
        xep_loai = "Xuat sac"
    elif diem >= 8:
        xep_loai = "Gioi"
    elif diem >= 7:
        xep_loai = "Kha"
    elif diem >= 5:
        xep_loai = "Trung binh"
    else:
        xep_loai = "Yeu"
    print(f"  Diem {diem:.1f} -> {xep_loai}")

print()

# === For loop ===
print("=== So nguyen to tu 2 den 50 ===")
primes = []
for num in range(2, 51):
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        primes.append(num)

print(primes)
print(f"Co {len(primes)} so nguyen to")
print()

# === While loop ===
print("=== Fibonacci ===")
n = 10
a, b = 0, 1
fib = []
while len(fib) < n:
    fib.append(a)
    a, b = b, a + b

print(f"{n} so Fibonacci dau tien: {fib}")
print()

# === Comprehensions ===
print("=== List Comprehension ===")

# So binh phuong
squares = [x**2 for x in range(1, 11)]
print(f"Binh phuong 1-10: {squares}")

# Loc so chan
evens = [x for x in range(1, 21) if x % 2 == 0]
print(f"So chan 1-20: {evens}")

# FizzBuzz bang comprehension
fizzbuzz = [
    "FizzBuzz" if i % 15 == 0
    else "Fizz" if i % 3 == 0
    else "Buzz" if i % 5 == 0
    else str(i)
    for i in range(1, 21)
]
print(f"FizzBuzz 1-20: {fizzbuzz}")
print()

# === Dict Comprehension ===
print("=== Dict Comprehension ===")
words = ["python", "java", "javascript", "go", "rust"]
word_lengths = {w: len(w) for w in words}
print(f"Do dai tu: {word_lengths}")
print()

# === Nested Loop ===
print("=== Tam giac sao ===")
for i in range(1, 6):
    print("* " * i)

print()
print("=== Tam giac so ===")
for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
