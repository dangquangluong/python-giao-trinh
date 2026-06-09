# Lời Giải Chương 8

## Bài 1: Gọi API

```python
import json                                  # Module JSON
from urllib.request import urlopen, Request  # Module HTTP

def github_info(username):                   # Hàm lấy info GitHub
    url = f"https://api.github.com/users/{username}"
    req = Request(url, headers={"User-Agent": "Python"})  # Cần User-Agent
    with urlopen(req) as resp:               # Gửi request
        data = json.loads(resp.read())       # Parse JSON response
    print(f"  @{data['login']}")
    print(f"  Tên: {data.get('name', 'N/A')}")
    print(f"  Bio: {data.get('bio', 'N/A')}")
    print(f"  Repos: {data['public_repos']}")

github_info("torvalds")                      # Test với user torvalds
```

## Bài 2: Viết test

```python
def tinh_gia(gia_goc, giam_phan_tram, so_luong):
    gia_sau_giam = gia_goc * (1 - giam_phan_tram / 100)  # Giá sau giảm
    return gia_sau_giam * so_luong                         # Tổng tiền

# Test cases dùng assert
assert tinh_gia(100, 10, 1) == 90.0          # 100 giảm 10% = 90
assert tinh_gia(100, 0, 5) == 500.0          # Không giảm: 100 × 5
assert tinh_gia(200, 50, 2) == 200.0         # 200 giảm 50% = 100 × 2
assert tinh_gia(100, 100, 1) == 0.0          # Giảm 100% = 0
assert tinh_gia(0, 50, 10) == 0.0            # Giá 0 → luôn 0

print("✅ Tất cả test passed!")
```

## Bài 3: Lọc + sắp xếp + ghi JSON

```python
import json                                  # Module JSON

sinh_vien = [                                # Data mẫu
    {"ten": "An", "diem": 8.5},
    {"ten": "Binh", "diem": 5.0},
    {"ten": "Cuong", "diem": 9.2},
    {"ten": "Dung", "diem": 6.0},
    {"ten": "Em", "diem": 7.5},
]

# Pipeline: lọc → sắp xếp
gioi = [sv for sv in sinh_vien if sv["diem"] >= 7]  # Lọc >= 7
gioi.sort(key=lambda sv: sv["diem"], reverse=True)   # Sắp giảm dần

# Ghi JSON
with open("/tmp/gioi.json", "w", encoding="utf-8") as f:
    json.dump(gioi, f, ensure_ascii=False, indent=2)

print(f"Đã lọc {len(gioi)} SV giỏi:")
for sv in gioi:
    print(f"  {sv['ten']}: {sv['diem']}")
```
