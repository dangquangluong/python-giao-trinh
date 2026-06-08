"""
Chuong 8: Vi du ve pytest

Chay: pytest demo_pytest.py -v
"""


# === Module can test ===
def tinh_giai_thua(n):
    """Tinh giai thua cua n."""
    if not isinstance(n, int):
        raise TypeError("n phai la so nguyen")
    if n < 0:
        raise ValueError("n phai >= 0")
    if n == 0:
        return 1
    return n * tinh_giai_thua(n - 1)


def fibonacci(n):
    """Tra ve so Fibonacci thu n."""
    if n <= 0:
        raise ValueError("n phai > 0")
    if n <= 2:
        return 1
    a, b = 1, 1
    for _ in range(n - 2):
        a, b = b, a + b
    return b


def is_palindrome(s):
    """Kiem tra chuoi doi xung."""
    s = s.lower().replace(" ", "")
    return s == s[::-1]


class Stack:
    """Cau truc du lieu Stack."""

    def __init__(self):
        self._items = []

    def push(self, item):
        self._items.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack rong")
        return self._items.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("Stack rong")
        return self._items[-1]

    def is_empty(self):
        return len(self._items) == 0

    def size(self):
        return len(self._items)


# === Test ===
import pytest


class TestGiaiThua:
    def test_base_case(self):
        assert tinh_giai_thua(0) == 1
        assert tinh_giai_thua(1) == 1

    def test_normal_cases(self):
        assert tinh_giai_thua(5) == 120
        assert tinh_giai_thua(10) == 3628800

    def test_negative(self):
        with pytest.raises(ValueError):
            tinh_giai_thua(-1)

    def test_invalid_type(self):
        with pytest.raises(TypeError):
            tinh_giai_thua(3.5)


class TestFibonacci:
    @pytest.mark.parametrize("n,expected", [
        (1, 1),
        (2, 1),
        (3, 2),
        (5, 5),
        (10, 55),
        (20, 6765),
    ])
    def test_values(self, n, expected):
        assert fibonacci(n) == expected

    def test_invalid(self):
        with pytest.raises(ValueError):
            fibonacci(0)
        with pytest.raises(ValueError):
            fibonacci(-5)


class TestPalindrome:
    @pytest.mark.parametrize("s,expected", [
        ("racecar", True),
        ("hello", False),
        ("A man a plan a canal Panama", True),
        ("", True),
        ("aba", True),
        ("abc", False),
    ])
    def test_cases(self, s, expected):
        assert is_palindrome(s) == expected


class TestStack:
    @pytest.fixture
    def empty_stack(self):
        return Stack()

    @pytest.fixture
    def filled_stack(self):
        s = Stack()
        for i in range(5):
            s.push(i)
        return s

    def test_empty(self, empty_stack):
        assert empty_stack.is_empty()
        assert empty_stack.size() == 0

    def test_push(self, empty_stack):
        empty_stack.push(1)
        assert not empty_stack.is_empty()
        assert empty_stack.size() == 1

    def test_pop(self, filled_stack):
        assert filled_stack.pop() == 4
        assert filled_stack.size() == 4

    def test_peek(self, filled_stack):
        assert filled_stack.peek() == 4
        assert filled_stack.size() == 5  # peek khong xoa

    def test_pop_empty(self, empty_stack):
        with pytest.raises(IndexError):
            empty_stack.pop()

    def test_peek_empty(self, empty_stack):
        with pytest.raises(IndexError):
            empty_stack.peek()
