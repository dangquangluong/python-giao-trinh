"""
Chuong 6: Vi du ve xu ly file va exception
"""

import json
import os
from pathlib import Path
from contextlib import contextmanager
import time


# === Doc va ghi file text ===
def demo_text_file():
    """Demo doc/ghi file text."""
    print("=== Doc/Ghi File Text ===")

    # Ghi file
    with open("demo_output.txt", "w", encoding="utf-8") as f:
        f.write("Dong 1: Xin chao Python!\n")
        f.write("Dong 2: Day la vi du ve file.\n")
        f.write("Dong 3: Hoc Python rat thu vi.\n")

    # Doc file
    with open("demo_output.txt", "r", encoding="utf-8") as f:
        for i, line in enumerate(f, 1):
            print(f"  [{i}] {line.strip()}")

    # Xoa file sau khi demo
    os.remove("demo_output.txt")
    print()


# === Doc/Ghi file JSON ===
def demo_json_file():
    """Demo xu ly JSON."""
    print("=== Doc/Ghi File JSON ===")

    # Du lieu mau
    sinh_vien = [
        {"ten": "Nguyen Van A", "diem": 8.5, "lop": "CNTT1"},
        {"ten": "Tran Thi B", "diem": 9.0, "lop": "CNTT2"},
        {"ten": "Le Van C", "diem": 7.0, "lop": "CNTT1"},
    ]

    # Ghi JSON
    with open("students.json", "w", encoding="utf-8") as f:
        json.dump(sinh_vien, f, ensure_ascii=False, indent=2)
    print("  Da ghi students.json")

    # Doc JSON
    with open("students.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    print("  Danh sach sinh vien:")
    for sv in data:
        print(f"    - {sv['ten']}: {sv['diem']} ({sv['lop']})")

    # Xoa file sau khi demo
    os.remove("students.json")
    print()


# === Exception handling ===
def demo_exceptions():
    """Demo xu ly exception."""
    print("=== Exception Handling ===")

    # Demo 1: ValueError
    values = ["42", "hello", "3.14", "", "100"]
    for v in values:
        try:
            num = int(v)
            print(f"  '{v}' -> {num}")
        except ValueError:
            print(f"  '{v}' -> [LOI: khong phai so nguyen]")

    print()

    # Demo 2: Try/Except/Else/Finally
    print("  --- Try/Except/Else/Finally ---")
    try:
        result = 100 / 5
    except ZeroDivisionError:
        print("  Loi chia cho 0!")
    else:
        print(f"  Ket qua: {result}")
    finally:
        print("  Block finally luon chay")

    print()


# === Custom Exception ===
class InsufficientFundsError(Exception):
    """Loi so du khong du."""
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        super().__init__(
            f"So du {balance:,} VND khong du de rut {amount:,} VND"
        )


class BankAccount:
    """Tai khoan ngan hang don gian."""

    def __init__(self, owner, balance=0):
        self.owner = owner
        self._balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("So tien nap phai lon hon 0")
        self._balance += amount
        return self._balance

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("So tien rut phai lon hon 0")
        if amount > self._balance:
            raise InsufficientFundsError(self._balance, amount)
        self._balance -= amount
        return self._balance


def demo_custom_exception():
    """Demo custom exception."""
    print("=== Custom Exception ===")

    acc = BankAccount("An", 1000000)
    print(f"  Tai khoan: {acc.owner}, So du: {acc._balance:,} VND")

    try:
        acc.withdraw(1500000)
    except InsufficientFundsError as e:
        print(f"  LOI: {e}")
        print(f"  So du hien tai: {e.balance:,} VND")
        print(f"  So tien can rut: {e.amount:,} VND")

    print()


# === Context Manager ===
@contextmanager
def timer(label):
    """Context manager do thoi gian."""
    start = time.time()
    print(f"  [{label}] Bat dau...")
    try:
        yield
    finally:
        elapsed = time.time() - start
        print(f"  [{label}] Hoan tat trong {elapsed:.6f}s")


def demo_context_manager():
    """Demo context manager."""
    print("=== Context Manager ===")

    with timer("Tinh tong"):
        total = sum(range(1000000))
        print(f"  Tong 0-999999: {total:,}")

    print()


# === Pathlib ===
def demo_pathlib():
    """Demo pathlib."""
    print("=== Pathlib ===")

    current = Path(".")
    print(f"  Thu muc hien tai: {current.resolve()}")

    # Liet ke file Python trong thu muc hien tai
    py_files = list(current.glob("*.py"))
    print(f"  File .py trong thu muc hien tai:")
    for f in py_files:
        size = f.stat().st_size
        print(f"    - {f.name} ({size} bytes)")

    print()


# === Main ===
if __name__ == "__main__":
    demo_text_file()
    demo_json_file()
    demo_exceptions()
    demo_custom_exception()
    demo_context_manager()
    demo_pathlib()
