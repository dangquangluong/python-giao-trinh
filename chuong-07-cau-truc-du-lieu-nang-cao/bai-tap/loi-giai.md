# Lời Giải Chương 7

## Bài 1: Generator số nguyên tố

```python
def nguyen_to():                             # Generator (dùng yield)
    n = 2                                    # Bắt đầu từ 2
    while True:                              # Lặp vô hạn
        is_prime = True
        for i in range(2, int(n**0.5) + 1):  # Kiểm tra 2 → sqrt(n)
            if n % i == 0:                   # Chia hết → không phải
                is_prime = False
                break
        if is_prime:                         # Nếu là nguyên tố
            yield n                          # yield = trả về + tạm dừng
        n += 1                               # Tiếp tục số kế

# Lấy 20 số nguyên tố đầu tiên
gen = nguyen_to()                            # Tạo generator
first_20 = [next(gen) for _ in range(20)]   # next() lấy giá trị tiếp
print(first_20)                              # [2, 3, 5, 7, 11, 13, ...]
```

## Bài 2: Dataclass Đơn hàng

```python
from dataclasses import dataclass, field     # Import dataclass
from typing import List

@dataclass
class SanPham:                               # Dataclass tự tạo __init__
    ten: str
    gia: float
    so_luong: int = 1

    @property
    def thanh_tien(self):                    # Property = method giả field
        return self.gia * self.so_luong

@dataclass
class DonHang:
    items: List[SanPham] = field(default_factory=list)  # Default = list rỗng

    def them(self, sp: SanPham):             # Thêm sản phẩm
        self.items.append(sp)

    def tong_tien(self) -> float:            # Tổng tiền
        return sum(sp.thanh_tien for sp in self.items)

    def hien_thi(self):
        for sp in self.items:
            print(f"  {sp.ten}: {sp.gia:,.0f}đ x {sp.so_luong} = {sp.thanh_tien:,.0f}đ")
        print(f"  TỔNG: {self.tong_tien():,.0f}đ")

don = DonHang()
don.them(SanPham("Laptop", 15_000_000))
don.them(SanPham("Chuột", 200_000, 2))
don.hien_thi()
```

## Bài 3: Counter Pipeline

```python
from collections import Counter             # Import Counter

text = """python là tuyệt vời python rất dễ học python có cộng đồng lớn
rust rất nhanh rust an toàn python và rust đều tuyệt vời
học python trước rồi học rust sau python dễ hơn rust"""

# Pipeline: tách → đếm → lọc → sắp xếp → top 10
words = text.split()                         # Tách thành list từ
counter = Counter(words)                     # Đếm tần suất
frequent = {w: c for w, c in counter.items() if c > 1}  # Lọc > 1 lần
sorted_words = sorted(frequent.items(), key=lambda x: x[1], reverse=True)  # Sắp giảm dần

print("Top từ xuất hiện > 1 lần:")
for word, count in sorted_words[:10]:        # Lấy top 10
    print(f"  '{word}': {count} lần")
```
