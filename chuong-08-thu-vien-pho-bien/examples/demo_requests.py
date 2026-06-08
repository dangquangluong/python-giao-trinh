"""
Chuong 8: Vi du su dung requests va pandas

Luu y: De chay duoc can cai dat:
    pip install requests pandas

Vi du nay co the chay offline voi du lieu mau.
"""

import json
from datetime import datetime


# === Demo requests (offline simulation) ===
def demo_requests_offline():
    """Demo cau truc su dung requests (khong can mang)."""
    print("=" * 50)
    print("=== DEMO REQUESTS (offline) ===")
    print("=" * 50)

    # Gia lap response tu API
    mock_response = {
        "status_code": 200,
        "data": [
            {"id": 1, "title": "Python co ban", "author": "An", "views": 1500},
            {"id": 2, "title": "Flask tutorial", "author": "Binh", "views": 800},
            {"id": 3, "title": "Data Science", "author": "Chi", "views": 2300},
            {"id": 4, "title": "Machine Learning", "author": "An", "views": 3100},
            {"id": 5, "title": "Web Scraping", "author": "Dung", "views": 650},
        ]
    }

    print(f"\n  Status Code: {mock_response['status_code']}")
    print(f"  So bai viet: {len(mock_response['data'])}")
    print("\n  Danh sach bai viet:")
    for item in mock_response["data"]:
        print(f"    [{item['id']}] {item['title']} - {item['author']} ({item['views']} views)")

    # Demo code thuc te (comment lai vi can mang)
    print("\n  Code thuc te:")
    print("""
    import requests

    # GET request
    response = requests.get("https://api.example.com/posts")
    response.raise_for_status()
    data = response.json()

    # POST request
    new_post = {"title": "Bai viet moi", "author": "An"}
    response = requests.post("https://api.example.com/posts", json=new_post)
    print(response.status_code)  # 201
    """)
    print()


# === Demo pandas (offline) ===
def demo_pandas_offline():
    """Demo pandas voi du lieu mau."""
    print("=" * 50)
    print("=== DEMO PANDAS (offline) ===")
    print("=" * 50)

    try:
        import pandas as pd

        # Tao DataFrame
        data = {
            "ten": ["An", "Binh", "Chi", "Dung", "Em", "Fong"],
            "lop": ["CNTT", "KTPM", "CNTT", "MMT", "KTPM", "CNTT"],
            "diem_python": [8.5, 7.0, 9.2, 6.5, 8.0, 7.5],
            "diem_sql": [7.0, 8.5, 8.0, 7.5, 9.0, 6.0],
            "diem_web": [8.0, 7.5, 9.0, 8.0, 7.0, 8.5],
        }
        df = pd.DataFrame(data)

        print("\n--- DataFrame ---")
        print(df.to_string(index=False))

        # Tinh diem trung binh
        df["diem_tb"] = df[["diem_python", "diem_sql", "diem_web"]].mean(axis=1)
        df["xep_loai"] = df["diem_tb"].apply(
            lambda d: "Gioi" if d >= 8 else "Kha" if d >= 7 else "TB"
        )

        print("\n--- Ket qua ---")
        print(df[["ten", "lop", "diem_tb", "xep_loai"]].to_string(index=False))

        # Thong ke theo lop
        print("\n--- Thong ke theo lop ---")
        stats = df.groupby("lop")["diem_tb"].agg(["mean", "max", "min", "count"])
        print(stats.to_string())

        # Loc sinh vien gioi
        print("\n--- Sinh vien Gioi ---")
        gioi = df[df["xep_loai"] == "Gioi"]
        print(gioi[["ten", "lop", "diem_tb"]].to_string(index=False))

    except ImportError:
        print("\n  [SKIP] pandas chua duoc cai dat.")
        print("  Cai dat: pip install pandas")
        print("\n  Demo voi Python thuan:")

        # Demo khong can pandas
        students = [
            {"ten": "An", "lop": "CNTT", "diem": [8.5, 7.0, 8.0]},
            {"ten": "Binh", "lop": "KTPM", "diem": [7.0, 8.5, 7.5]},
            {"ten": "Chi", "lop": "CNTT", "diem": [9.2, 8.0, 9.0]},
        ]

        print(f"\n  {'Ten':<8} {'Lop':<6} {'DTB':<6} {'Xep loai'}")
        print("  " + "-" * 35)
        for sv in students:
            dtb = sum(sv["diem"]) / len(sv["diem"])
            loai = "Gioi" if dtb >= 8 else "Kha" if dtb >= 7 else "TB"
            print(f"  {sv['ten']:<8} {sv['lop']:<6} {dtb:<6.1f} {loai}")

    print()


# === Main ===
if __name__ == "__main__":
    demo_requests_offline()
    demo_pandas_offline()
