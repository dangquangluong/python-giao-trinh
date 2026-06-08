# Ví dụ sử dụng requests và json
import json                                  # Module xử lý dữ liệu JSON (chuyển đổi Python <-> JSON)
from urllib.request import urlopen, Request  # Module HTTP có sẵn trong Python (không cần cài thêm)
from urllib.error import URLError            # Class lỗi khi kết nối URL thất bại

def fetch_github_user(username):             # Hàm lấy thông tin user GitHub từ API
    """Lấy thông tin user GitHub (không cần cài requests)"""  # Docstring
    url = f"https://api.github.com/users/{username}"  # f-string tạo URL API với username
    try:                                     # Thử gọi API (có thể lỗi mạng)
        req = Request(url, headers={"User-Agent": "Python-Tutorial"})  # Tạo request với header User-Agent
        with urlopen(req, timeout=10) as response:  # Gửi request, timeout 10 giây
            data = json.loads(response.read().decode())  # Đọc response, decode bytes thành str, parse JSON
            return {                         # Trả về dict với thông tin cần thiết
                "login": data.get("login"),  # .get() lấy giá trị an toàn (trả None nếu key không có)
                "name": data.get("name"),    # Tên hiển thị
                "bio": data.get("bio"),      # Mô tả ngắn
                "public_repos": data.get("public_repos"),  # Số repo công khai
                "followers": data.get("followers"),        # Số người theo dõi
            }
    except URLError as e:                    # Bắt lỗi kết nối (mất mạng, URL sai)
        print(f"Lỗi kết nối: {e}")          # In chi tiết lỗi
        return None                          # Trả về None nếu lỗi
    except json.JSONDecodeError:             # Bắt lỗi parse JSON (response không phải JSON hợp lệ)
        print("Lỗi parse JSON")             # In thông báo lỗi
        return None                          # Trả về None

def main():                                  # Hàm chính của chương trình
    print("=== GitHub User Info ===\n")      # In tiêu đề

    users = ["python", "torvalds", "guido"]  # List các username GitHub cần tra cứu
    for username in users:                   # Lặp qua từng username
        info = fetch_github_user(username)   # Gọi hàm lấy thông tin
        if info:                             # Nếu lấy được (không phải None)
            print(f"👤 @{info['login']}")    # In username
            print(f"   Tên: {info['name']}") # In tên
            print(f"   Bio: {info['bio']}")  # In mô tả
            print(f"   Repos: {info['public_repos']} | Followers: {info['followers']}")  # In số repo và followers
            print()                          # In dòng trống

    # === Demo JSON ===
    print("=== JSON Demo ===\n")             # In tiêu đề phần demo JSON
    data = {                                 # Tạo dict Python phức tạp (lồng nhau)
        "sinh_vien": [                       # Key "sinh_vien" chứa list các dict
            {"ten": "An", "diem": 8.5, "mon": ["Python", "SQL"]},   # SV có list môn học
            {"ten": "Binh", "diem": 7.0, "mon": ["Java", "C++"]},   # SV 2
        ]
    }

    # Python -> JSON string
    json_str = json.dumps(data, ensure_ascii=False, indent=2)  # dumps() chuyển Python object thành chuỗi JSON
    print("Python -> JSON:")                 # In tiêu đề chuyển đổi
    print(json_str)                          # In chuỗi JSON đã format đẹp

    # JSON string -> Python
    parsed = json.loads(json_str)            # loads() chuyển chuỗi JSON thành Python object
    print(f"\nJSON -> Python:")              # In tiêu đề chuyển đổi ngược
    for sv in parsed["sinh_vien"]:           # Lặp qua list sinh viên từ dict đã parse
        print(f"  {sv['ten']}: {sv['diem']} | Môn: {', '.join(sv['mon'])}")  # .join() nối list thành chuỗi

if __name__ == "__main__":                   # Chỉ chạy khi file được thực thi trực tiếp
    main()                                   # Gọi hàm main
