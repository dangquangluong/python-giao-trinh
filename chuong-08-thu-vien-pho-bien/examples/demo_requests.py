"""
Chuong 8: Vi du su dung requests va pandas

Luu y: De chay duoc can cai dat:
    pip install requests pandas

Vi du nay co the chay offline voi du lieu mau.
"""

import json                                  # Module xử lý dữ liệu JSON
from datetime import datetime                # Module xử lý ngày giờ


# === Demo requests (offline simulation) ===
def demo_requests_offline():                 # Hàm demo cách dùng requests (không cần mạng)
    """Demo cau truc su dung requests (khong can mang)."""  # Docstring
    print("=" * 50)                          # In đường kẻ
    print("=== DEMO REQUESTS (offline) ===") # In tiêu đề
    print("=" * 50)                          # In đường kẻ

    # Gia lap response tu API
    mock_response = {                        # Dict giả lập response từ API (để demo offline)
        "status_code": 200,                  # HTTP status code 200 = thành công
        "data": [                            # List dữ liệu bài viết
            {"id": 1, "title": "Python co ban", "author": "An", "views": 1500},      # Bài viết 1
            {"id": 2, "title": "Flask tutorial", "author": "Binh", "views": 800},    # Bài viết 2
            {"id": 3, "title": "Data Science", "author": "Chi", "views": 2300},      # Bài viết 3
            {"id": 4, "title": "Machine Learning", "author": "An", "views": 3100},   # Bài viết 4
            {"id": 5, "title": "Web Scraping", "author": "Dung", "views": 650},      # Bài viết 5
        ]
    }

    print(f"\n  Status Code: {mock_response['status_code']}")  # In mã trạng thái HTTP
    print(f"  So bai viet: {len(mock_response['data'])}")      # In số bài viết
    print("\n  Danh sach bai viet:")          # In tiêu đề danh sách
    for item in mock_response["data"]:       # Lặp qua từng bài viết
        print(f"    [{item['id']}] {item['title']} - {item['author']} ({item['views']} views)")  # In thông tin

    # Demo code thuc te (comment lai vi can mang)
    print("\n  Code thuc te:")               # In mẫu code thực tế
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
    print()                                  # In dòng trống


# === Demo pandas (offline) ===
def demo_pandas_offline():                   # Hàm demo pandas (thư viện phân tích dữ liệu)
    """Demo pandas voi du lieu mau."""       # Docstring
    print("=" * 50)                          # In đường kẻ
    print("=== DEMO PANDAS (offline) ===")   # In tiêu đề
    print("=" * 50)                          # In đường kẻ

    try:                                     # Thử import pandas (có thể chưa cài)
        import pandas as pd                  # Import pandas với alias pd (quy ước)

        # Tao DataFrame
        data = {                             # Dict chứa dữ liệu dạng cột
            "ten": ["An", "Binh", "Chi", "Dung", "Em", "Fong"],  # Cột tên
            "lop": ["CNTT", "KTPM", "CNTT", "MMT", "KTPM", "CNTT"],  # Cột lớp
            "diem_python": [8.5, 7.0, 9.2, 6.5, 8.0, 7.5],  # Cột điểm Python
            "diem_sql": [7.0, 8.5, 8.0, 7.5, 9.0, 6.0],     # Cột điểm SQL
            "diem_web": [8.0, 7.5, 9.0, 8.0, 7.0, 8.5],     # Cột điểm Web
        }
        df = pd.DataFrame(data)              # Tạo DataFrame từ dict (bảng 2 chiều)

        print("\n--- DataFrame ---")         # In tiêu đề
        print(df.to_string(index=False))     # In DataFrame không hiển thị index

        # Tinh diem trung binh
        df["diem_tb"] = df[["diem_python", "diem_sql", "diem_web"]].mean(axis=1)  # .mean(axis=1) tính TB theo hàng
        df["xep_loai"] = df["diem_tb"].apply(  # .apply() áp dụng hàm lên từng giá trị
            lambda d: "Gioi" if d >= 8 else "Kha" if d >= 7 else "TB"  # Lambda xếp loại theo điểm
        )

        print("\n--- Ket qua ---")           # In tiêu đề kết quả
        print(df[["ten", "lop", "diem_tb", "xep_loai"]].to_string(index=False))  # In cột chọn lọc

        # Thong ke theo lop
        print("\n--- Thong ke theo lop ---") # In tiêu đề thống kê
        stats = df.groupby("lop")["diem_tb"].agg(["mean", "max", "min", "count"])  # groupby nhóm theo lớp, agg tính nhiều thống kê
        print(stats.to_string())             # In bảng thống kê

        # Loc sinh vien gioi
        print("\n--- Sinh vien Gioi ---")    # In tiêu đề
        gioi = df[df["xep_loai"] == "Gioi"]  # Lọc DataFrame: chỉ lấy hàng có xếp loại "Gioi"
        print(gioi[["ten", "lop", "diem_tb"]].to_string(index=False))  # In kết quả lọc

    except ImportError:                      # Bắt lỗi nếu pandas chưa được cài
        print("\n  [SKIP] pandas chua duoc cai dat.")  # Thông báo chưa cài
        print("  Cai dat: pip install pandas")         # Hướng dẫn cài
        print("\n  Demo voi Python thuan:")  # Demo thay thế không cần pandas

        # Demo khong can pandas
        students = [                         # List dict sinh viên
            {"ten": "An", "lop": "CNTT", "diem": [8.5, 7.0, 8.0]},   # SV 1
            {"ten": "Binh", "lop": "KTPM", "diem": [7.0, 8.5, 7.5]}, # SV 2
            {"ten": "Chi", "lop": "CNTT", "diem": [9.2, 8.0, 9.0]},  # SV 3
        ]

        print(f"\n  {'Ten':<8} {'Lop':<6} {'DTB':<6} {'Xep loai'}")  # In header bảng (căn trái)
        print("  " + "-" * 35)               # In đường kẻ
        for sv in students:                  # Lặp qua từng sinh viên
            dtb = sum(sv["diem"]) / len(sv["diem"])  # Tính điểm TB
            loai = "Gioi" if dtb >= 8 else "Kha" if dtb >= 7 else "TB"  # Xếp loại
            print(f"  {sv['ten']:<8} {sv['lop']:<6} {dtb:<6.1f} {loai}")  # In thông tin

    print()                                  # In dòng trống


# === Main ===
if __name__ == "__main__":                   # Chỉ chạy khi thực thi file trực tiếp
    demo_requests_offline()                  # Gọi demo requests
    demo_pandas_offline()                    # Gọi demo pandas
