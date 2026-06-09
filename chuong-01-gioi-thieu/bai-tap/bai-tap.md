# Bài Tập Chương 1: Giới Thiệu Python

## Bài 1: Hello World (⭐ Dễ)

**Yêu cầu:** Viết chương trình in ra:
```
Xin chào! Tôi là [tên bạn].
Năm nay tôi [tuổi] tuổi.
Tôi đang học Python!
```

**Gợi ý:**
- Dùng biến `ten` và `tuoi`
- Dùng f-string: `print(f"... {ten} ...")`

---

## Bài 2: Tính tuổi (⭐ Dễ)

**Yêu cầu:** Nhập năm sinh, tính và in ra tuổi hiện tại.

**Gợi ý:**
- `input()` để nhập
- `int()` để chuyển string → số
- Năm hiện tại: `from datetime import datetime; datetime.now().year`

---

## Bài 3: Hoán đổi biến (⭐ Dễ)

**Yêu cầu:** Có 2 biến `a = 5`, `b = 10`. Hoán đổi giá trị rồi in ra.

**Gợi ý:**
- Python cách ngắn: `a, b = b, a`

---

## Bài 4: Máy tính đơn giản (⭐⭐ Trung bình)

**Yêu cầu:** Nhập 2 số từ bàn phím, in ra kết quả cộng, trừ, nhân, chia, chia lấy dư.

**Gợi ý:**
- `float(input("Nhập số: "))` để nhập số thực
- Cẩn thận chia cho 0!
