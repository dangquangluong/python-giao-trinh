# Ví dụ sử dụng requests và json
import json
from urllib.request import urlopen, Request
from urllib.error import URLError

def fetch_github_user(username):
    """Lấy thông tin user GitHub (không cần cài requests)"""
    url = f"https://api.github.com/users/{username}"
    try:
        req = Request(url, headers={"User-Agent": "Python-Tutorial"})
        with urlopen(req, timeout=10) as response:
            data = json.loads(response.read().decode())
            return {
                "login": data.get("login"),
                "name": data.get("name"),
                "bio": data.get("bio"),
                "public_repos": data.get("public_repos"),
                "followers": data.get("followers"),
            }
    except URLError as e:
        print(f"Lỗi kết nối: {e}")
        return None
    except json.JSONDecodeError:
        print("Lỗi parse JSON")
        return None

def main():
    print("=== GitHub User Info ===\n")

    users = ["python", "torvalds", "guido"]
    for username in users:
        info = fetch_github_user(username)
        if info:
            print(f"👤 @{info['login']}")
            print(f"   Tên: {info['name']}")
            print(f"   Bio: {info['bio']}")
            print(f"   Repos: {info['public_repos']} | Followers: {info['followers']}")
            print()

    # === Demo JSON ===
    print("=== JSON Demo ===\n")
    data = {
        "sinh_vien": [
            {"ten": "An", "diem": 8.5, "mon": ["Python", "SQL"]},
            {"ten": "Binh", "diem": 7.0, "mon": ["Java", "C++"]},
        ]
    }

    # Python → JSON string
    json_str = json.dumps(data, ensure_ascii=False, indent=2)
    print("Python → JSON:")
    print(json_str)

    # JSON string → Python
    parsed = json.loads(json_str)
    print(f"\nJSON → Python:")
    for sv in parsed["sinh_vien"]:
        print(f"  {sv['ten']}: {sv['diem']} | Môn: {', '.join(sv['mon'])}")

if __name__ == "__main__":
    main()
