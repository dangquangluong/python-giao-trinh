"""
Chuong 8: Vi du ve pytest

Chay: pytest demo_pytest.py -v
"""


# === Module can test ===
def tinh_giai_thua(n):                       # Định nghĩa hàm tính giai thừa (n!)
    """Tinh giai thua cua n."""              # Docstring mô tả hàm
    if not isinstance(n, int):               # isinstance() kiểm tra n có phải kiểu int không
        raise TypeError("n phai la so nguyen")  # raise = ném lỗi TypeError nếu không phải int
    if n < 0:                                # Kiểm tra n âm (giai thừa không định nghĩa cho số âm)
        raise ValueError("n phai >= 0")      # Ném lỗi ValueError nếu n < 0
    if n == 0:                               # Trường hợp cơ sở: 0! = 1
        return 1                             # Trả về 1
    return n * tinh_giai_thua(n - 1)         # Đệ quy: n! = n * (n-1)!


def fibonacci(n):                            # Hàm tính số Fibonacci thứ n
    """Tra ve so Fibonacci thu n."""          # Docstring
    if n <= 0:                               # Kiểm tra n phải > 0
        raise ValueError("n phai > 0")       # Ném lỗi nếu n <= 0
    if n <= 2:                               # Trường hợp cơ sở: F(1) = F(2) = 1
        return 1                             # Trả về 1
    a, b = 1, 1                              # Khởi tạo 2 số Fibonacci đầu
    for _ in range(n - 2):                   # Lặp n-2 lần (đã có 2 số đầu)
        a, b = b, a + b                      # Tính số tiếp: a mới=b cũ, b mới=a+b
    return b                                 # Trả về số Fibonacci thứ n


def is_palindrome(s):                        # Hàm kiểm tra chuỗi đối xứng (palindrome)
    """Kiem tra chuoi doi xung."""            # Docstring
    s = s.lower().replace(" ", "")           # Chuyển thường và xóa khoảng trắng để so sánh
    return s == s[::-1]                      # So sánh chuỗi với chuỗi đảo ngược ([::-1])


class Stack:                                 # Cấu trúc dữ liệu Stack (ngăn xếp) - LIFO
    """Cau truc du lieu Stack."""             # Docstring: LIFO = Last In First Out

    def __init__(self):                      # Constructor khởi tạo Stack rỗng
        self._items = []                     # _items: list lưu các phần tử (quy ước private)

    def push(self, item):                    # Method đẩy phần tử vào đỉnh stack
        self._items.append(item)             # .append() thêm vào cuối list (= đỉnh stack)

    def pop(self):                           # Method lấy phần tử từ đỉnh stack ra
        if self.is_empty():                  # Kiểm tra stack có rỗng không
            raise IndexError("Stack rong")   # Ném lỗi nếu stack rỗng
        return self._items.pop()             # .pop() lấy và xóa phần tử cuối (= đỉnh)

    def peek(self):                          # Method xem phần tử đỉnh (không xóa)
        if self.is_empty():                  # Kiểm tra rỗng
            raise IndexError("Stack rong")   # Ném lỗi nếu rỗng
        return self._items[-1]               # [-1] = phần tử cuối cùng (đỉnh stack)

    def is_empty(self):                      # Method kiểm tra stack rỗng
        return len(self._items) == 0         # Trả về True nếu không có phần tử nào

    def size(self):                          # Method trả về số phần tử trong stack
        return len(self._items)              # len() đếm số phần tử


# === Test ===
import pytest                                # Import thư viện pytest để viết unit test


class TestGiaiThua:                          # Class nhóm các test cho hàm tinh_giai_thua
    def test_base_case(self):                # Test trường hợp cơ sở (0! và 1!)
        assert tinh_giai_thua(0) == 1        # assert = xác nhận kết quả đúng, sai thì test fail
        assert tinh_giai_thua(1) == 1        # 1! = 1

    def test_normal_cases(self):             # Test trường hợp bình thường
        assert tinh_giai_thua(5) == 120      # 5! = 120
        assert tinh_giai_thua(10) == 3628800 # 10! = 3628800

    def test_negative(self):                 # Test trường hợp số âm (phải ném lỗi)
        with pytest.raises(ValueError):      # Kỳ vọng ValueError được ném ra
            tinh_giai_thua(-1)               # Gọi hàm với -1

    def test_invalid_type(self):             # Test trường hợp kiểu sai
        with pytest.raises(TypeError):       # Kỳ vọng TypeError được ném ra
            tinh_giai_thua(3.5)              # Gọi hàm với float (không phải int)


class TestFibonacci:                         # Class nhóm các test cho hàm fibonacci
    @pytest.mark.parametrize("n,expected", [ # @parametrize = chạy test nhiều lần với dữ liệu khác nhau
        (1, 1),                              # F(1) = 1
        (2, 1),                              # F(2) = 1
        (3, 2),                              # F(3) = 2
        (5, 5),                              # F(5) = 5
        (10, 55),                            # F(10) = 55
        (20, 6765),                          # F(20) = 6765
    ])
    def test_values(self, n, expected):      # Method test nhận n và expected từ parametrize
        assert fibonacci(n) == expected      # Kiểm tra kết quả khớp giá trị kỳ vọng

    def test_invalid(self):                  # Test trường hợp input không hợp lệ
        with pytest.raises(ValueError):      # Kỳ vọng ValueError
            fibonacci(0)                     # F(0) không hợp lệ
        with pytest.raises(ValueError):      # Kỳ vọng ValueError
            fibonacci(-5)                    # F(-5) không hợp lệ


class TestPalindrome:                        # Class nhóm test cho is_palindrome
    @pytest.mark.parametrize("s,expected", [ # Test nhiều trường hợp palindrome
        ("racecar", True),                   # "racecar" đối xứng
        ("hello", False),                    # "hello" không đối xứng
        ("A man a plan a canal Panama", True),  # Bỏ khoảng trắng vẫn đối xứng
        ("", True),                          # Chuỗi rỗng coi là đối xứng
        ("aba", True),                       # "aba" đối xứng
        ("abc", False),                      # "abc" không đối xứng
    ])
    def test_cases(self, s, expected):       # Method test từng trường hợp
        assert is_palindrome(s) == expected  # Kiểm tra kết quả


class TestStack:                             # Class nhóm test cho Stack
    @pytest.fixture                          # @fixture = hàm chuẩn bị dữ liệu test (setup)
    def empty_stack(self):                   # Fixture tạo stack rỗng
        return Stack()                       # Trả về Stack mới

    @pytest.fixture                          # Fixture tạo stack đã có dữ liệu
    def filled_stack(self):                  # Stack chứa 0,1,2,3,4
        s = Stack()                          # Tạo stack mới
        for i in range(5):                   # Lặp 0 đến 4
            s.push(i)                        # Đẩy từng số vào stack
        return s                             # Trả về stack đã điền

    def test_empty(self, empty_stack):       # Test stack rỗng (nhận fixture qua tham số)
        assert empty_stack.is_empty()        # Stack mới phải rỗng
        assert empty_stack.size() == 0       # Size phải = 0

    def test_push(self, empty_stack):        # Test push vào stack
        empty_stack.push(1)                  # Đẩy 1 vào
        assert not empty_stack.is_empty()    # Không còn rỗng
        assert empty_stack.size() == 1       # Size = 1

    def test_pop(self, filled_stack):        # Test pop từ stack (LIFO: phần tử cuối ra trước)
        assert filled_stack.pop() == 4       # Pop trả về 4 (phần tử cuối cùng push vào)
        assert filled_stack.size() == 4      # Size giảm 1

    def test_peek(self, filled_stack):       # Test peek (xem đỉnh không xóa)
        assert filled_stack.peek() == 4      # Peek trả về 4 (đỉnh stack)
        assert filled_stack.size() == 5      # Size không đổi (peek không xóa)

    def test_pop_empty(self, empty_stack):   # Test pop stack rỗng (phải ném lỗi)
        with pytest.raises(IndexError):      # Kỳ vọng IndexError
            empty_stack.pop()                # Pop stack rỗng

    def test_peek_empty(self, empty_stack):  # Test peek stack rỗng
        with pytest.raises(IndexError):      # Kỳ vọng IndexError
            empty_stack.peek()               # Peek stack rỗng
