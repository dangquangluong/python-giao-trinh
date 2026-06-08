# Chương 9: Dự Án Thực Hành

## Dự Án 1: Todo CLI App ⭐⭐

### Mô Tả
Ứng dụng quản lý công việc trên terminal.

### Tính Năng
- Thêm/xóa/sửa task
- Đánh dấu hoàn thành
- Lưu vào file JSON
- Lọc theo trạng thái

### Sử Dụng
```bash
python todo.py add "Học Python"
python todo.py list
python todo.py done 1
python todo.py delete 1
```

### Code Khung

```python
import json                                  # Module đọc/ghi JSON
import sys                                   # Module truy cập tham số dòng lệnh
from pathlib import Path                     # Class xử lý đường dẫn file
from datetime import datetime                # Module xử lý ngày giờ

DATA_FILE = Path("todos.json")               # Đường dẫn file lưu dữ liệu

def load_todos():                            # Hàm đọc todos từ file
    if DATA_FILE.exists():                   # .exists() kiểm tra file có tồn tại
        return json.loads(DATA_FILE.read_text(encoding="utf-8"))  # Đọc file và parse JSON
    return []                                # Trả về list rỗng nếu file chưa có

def save_todos(todos):                       # Hàm lưu todos vào file
    DATA_FILE.write_text(                    # .write_text() ghi chuỗi vào file
        json.dumps(todos, ensure_ascii=False, indent=2),  # Chuyển list thành JSON string
        encoding="utf-8"
    )

def add_todo(text):                          # Hàm thêm todo mới
    todos = load_todos()                     # Đọc danh sách hiện tại
    todo = {                                 # Tạo dict todo mới
        "id": len(todos) + 1,                # ID = số lượng hiện tại + 1
        "text": text,                        # Nội dung task
        "done": False,                       # Chưa hoàn thành
        "created": datetime.now().isoformat()  # Thời gian tạo (format ISO)
    }
    todos.append(todo)                       # Thêm vào danh sách
    save_todos(todos)                        # Lưu vào file
    print(f"✅ Đã thêm: {text}")            # In xác nhận

def list_todos(show_all=True):               # Hàm liệt kê todos
    todos = load_todos()                     # Đọc danh sách
    if not todos:                            # Nếu danh sách rỗng
        print("📋 Không có task nào!")       # Thông báo
        return                               # Thoát hàm
    for t in todos:                          # Lặp qua từng task
        status = "✅" if t["done"] else "⬜"  # Emoji theo trạng thái
        if show_all or not t["done"]:        # Hiển thị tất cả hoặc chỉ chưa xong
            print(f"  {status} [{t['id']}] {t['text']}")  # In task

def mark_done(todo_id):                      # Hàm đánh dấu hoàn thành
    todos = load_todos()                     # Đọc danh sách
    for t in todos:                          # Tìm task theo ID
        if t["id"] == todo_id:               # Nếu khớp ID
            t["done"] = True                 # Đánh dấu xong
            save_todos(todos)                # Lưu thay đổi
            print(f"✅ Hoàn thành: {t['text']}")  # Xác nhận
            return                           # Thoát hàm
    print(f"❌ Không tìm thấy task #{todo_id}")  # Không tìm thấy

def delete_todo(todo_id):                    # Hàm xóa task
    todos = load_todos()                     # Đọc danh sách
    todos = [t for t in todos if t["id"] != todo_id]  # Lọc bỏ task có ID cần xóa
    save_todos(todos)                        # Lưu lại danh sách đã xóa
    print(f"🗑️ Đã xóa task #{todo_id}")     # Xác nhận

if __name__ == "__main__":                   # Chỉ chạy khi thực thi file trực tiếp
    if len(sys.argv) < 2:                    # Kiểm tra có tham số dòng lệnh không
        print("Sử dụng: python todo.py [add|list|done|delete] [args]")  # Hướng dẫn
        sys.exit(1)                          # Thoát với mã lỗi 1

    cmd = sys.argv[1]                        # Lấy lệnh (tham số thứ 2)
    if cmd == "add" and len(sys.argv) > 2:   # Lệnh add + có nội dung
        add_todo(" ".join(sys.argv[2:]))     # Nối tất cả tham số sau thành tiêu đề
    elif cmd == "list":                      # Lệnh list
        list_todos()                         # Gọi hàm liệt kê
    elif cmd == "done" and len(sys.argv) > 2:  # Lệnh done + có ID
        mark_done(int(sys.argv[2]))          # Ép kiểu ID thành int
    elif cmd == "delete" and len(sys.argv) > 2:  # Lệnh delete + có ID
        delete_todo(int(sys.argv[2]))        # Gọi hàm xóa
    else:                                    # Lệnh không hợp lệ
        print("Lệnh không hợp lệ!")          # Thông báo lỗi
```

---

## Dự Án 2: Web Scraper ⭐⭐

### Mô Tả
Thu thập dữ liệu từ website.

```bash
pip install beautifulsoup4 requests
```

```python
import requests                              # Thư viện gửi HTTP request
from bs4 import BeautifulSoup                # Thư viện parse (phân tích) HTML

def scrape_news(url):                        # Hàm scrape tiêu đề tin tức
    """Lấy tiêu đề tin tức"""                # Docstring
    resp = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})  # GET với User-Agent giả lập browser
    soup = BeautifulSoup(resp.text, "html.parser")  # Parse HTML thành cây DOM

    articles = []                            # List chứa kết quả
    for tag in soup.find_all("h2"):          # Tìm tất cả thẻ <h2> trong HTML
        link = tag.find("a")                 # Tìm thẻ <a> (link) bên trong <h2>
        if link:                             # Nếu tìm thấy link
            articles.append({                # Thêm vào kết quả
                "title": link.get_text(strip=True),  # .get_text() lấy text, strip=True xóa khoảng trắng
                "url": link.get("href", "")  # .get("href") lấy thuộc tính href (URL)
            })

    return articles                          # Trả về list bài viết

if __name__ == "__main__":                   # Chạy khi thực thi trực tiếp
    articles = scrape_news("https://news.ycombinator.com")  # Scrape Hacker News
    for i, a in enumerate(articles[:10], 1):  # Lấy 10 bài đầu, đánh số từ 1
        print(f"{i}. {a['title']}")          # In tiêu đề
        print(f"   {a['url']}\n")            # In URL
```

---

## Dự Án 3: REST API (FastAPI) ⭐⭐⭐

### Mô Tả
API quản lý sách cho thư viện.

```bash
pip install fastapi uvicorn pydantic
```

```python
from fastapi import FastAPI, HTTPException   # Framework web + class lỗi HTTP
from pydantic import BaseModel               # Validate dữ liệu tự động
from typing import List, Optional            # Type hints

app = FastAPI(title="API Thư Viện", version="1.0")  # Tạo app với title và version

class Sach(BaseModel):                       # Model Pydantic - tự validate kiểu dữ liệu
    id: Optional[int] = None                 # ID có thể None (server tự gán)
    tieu_de: str                             # Bắt buộc str
    tac_gia: str                             # Bắt buộc str
    nam: int                                 # Bắt buộc int
    the_loai: str                            # Bắt buộc str

db: List[Sach] = [                           # "Database" giả lập bằng list
    Sach(id=1, tieu_de="Clean Code", tac_gia="Robert Martin", nam=2008, the_loai="Tech"),
    Sach(id=2, tieu_de="Python Crash Course", tac_gia="Eric Matthes", nam=2019, the_loai="Tech"),
]
next_id = 3                                  # ID tiếp theo sẽ gán

@app.get("/books", response_model=List[Sach])  # GET /books - lấy danh sách
def get_books(the_loai: Optional[str] = None):  # Query parameter tùy chọn: ?the_loai=Tech
    if the_loai:                             # Nếu có filter thể loại
        return [s for s in db if s.the_loai.lower() == the_loai.lower()]  # Lọc
    return db                                # Trả về tất cả

@app.get("/books/{book_id}", response_model=Sach)  # GET /books/1 - lấy 1 cuốn
def get_book(book_id: int):                  # book_id từ URL path
    for s in db:                             # Tìm sách
        if s.id == book_id:
            return s                         # Trả về nếu tìm thấy
    raise HTTPException(404, "Sách không tồn tại")  # 404 nếu không tìm thấy

@app.post("/books", response_model=Sach, status_code=201)  # POST tạo mới
def create_book(sach: Sach):                 # Request body tự parse thành Sach
    global next_id                           # Sửa biến global
    sach.id = next_id                        # Gán ID
    next_id += 1                             # Tăng ID
    db.append(sach)                          # Thêm vào DB
    return sach                              # Trả về sách vừa tạo

@app.put("/books/{book_id}", response_model=Sach)  # PUT cập nhật toàn bộ
def update_book(book_id: int, sach_moi: Sach):  # Nhận ID từ URL và data từ body
    for i, s in enumerate(db):               # Tìm sách cần update
        if s.id == book_id:
            sach_moi.id = book_id            # Giữ nguyên ID
            db[i] = sach_moi                 # Thay thế trong list
            return sach_moi                  # Trả về sách đã update
    raise HTTPException(404, "Sách không tồn tại")

@app.delete("/books/{book_id}")              # DELETE xóa sách
def delete_book(book_id: int):
    for i, s in enumerate(db):               # Tìm sách
        if s.id == book_id:
            db.pop(i)                        # Xóa khỏi list
            return {"message": f"Đã xóa sách #{book_id}"}  # Xác nhận
    raise HTTPException(404, "Sách không tồn tại")

# Chạy: uvicorn main:app --reload
# Docs: http://localhost:8000/docs
```

---

## Dự Án 4: Automation Script ⭐⭐

### Mô Tả
Script tự động hóa: backup file, gửi email, monitor.

```python
import shutil                                # Module sao chép/nén file/thư mục
import os                                    # Module thao tác hệ điều hành
from datetime import datetime                # Xử lý ngày giờ
from pathlib import Path                     # Xử lý đường dẫn

def backup_directory(source, dest_base):     # Hàm backup thư mục
    """Backup thư mục với timestamp"""       # Docstring
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")  # Tạo chuỗi thời gian: 20240115_143022
    dest = Path(dest_base) / f"backup_{timestamp}"  # Tạo đường dẫn đích (/ nối path)

    shutil.copytree(source, dest)            # Sao chép toàn bộ thư mục nguồn sang đích
    print(f"✅ Backup: {source} → {dest}")   # In xác nhận

    # Nén
    archive = shutil.make_archive(str(dest), "zip", dest)  # Nén thư mục thành file .zip
    shutil.rmtree(dest)                      # Xóa thư mục (giữ file zip)
    print(f"📦 Nén: {archive}")              # In đường dẫn file zip
    return archive                           # Trả về đường dẫn archive

def cleanup_old_backups(backup_dir, keep=5):  # Hàm xóa backup cũ, giữ lại N bản mới nhất
    """Giữ lại N backup mới nhất"""          # Docstring
    backups = sorted(Path(backup_dir).glob("backup_*.zip"), reverse=True)  # Tìm và sắp xếp mới->cũ
    for old in backups[keep:]:               # Lấy từ vị trí keep trở đi (các bản cũ)
        old.unlink()                         # .unlink() xóa file
        print(f"🗑️ Xóa backup cũ: {old.name}")  # In xác nhận

def disk_usage_report():                     # Hàm báo cáo dung lượng ổ đĩa
    """Báo cáo dung lượng ổ đĩa"""          # Docstring
    total, used, free = shutil.disk_usage("/")  # Trả về (tổng, đã dùng, còn trống) bytes
    print(f"💾 Disk: {used//(2**30)}GB / {total//(2**30)}GB (Free: {free//(2**30)}GB)")  # 2**30 = 1GB

if __name__ == "__main__":                   # Chạy khi thực thi trực tiếp
    disk_usage_report()                      # In báo cáo ổ đĩa
    # backup_directory("/path/to/project", "/path/to/backups")
    # cleanup_old_backups("/path/to/backups", keep=5)
```

---

## Dự Án Nâng Cao (Tự Thực Hiện)

| # | Dự Án | Thư Viện |
|---|--------|----------|
| 5 | Chat bot Telegram | python-telegram-bot |
| 6 | Dashboard web | Streamlit / Dash |
| 7 | Image processor | Pillow |
| 8 | Database migration tool | Alembic |
| 9 | Task scheduler | APScheduler |
| 10 | CLI file manager | rich, click |

---

## 🎓 Tài Nguyên Tiếp Theo

- [Real Python](https://realpython.com/)
- [Python Design Patterns](https://python-patterns.guide/)
- [Full Stack Python](https://www.fullstackpython.com/)
- [Awesome Python](https://github.com/vinta/awesome-python)

---

🎉 **Chúc mừng hoàn thành giáo trình Python!**

📖 **Trước đó**: [Chương 8](../chuong-08-thu-vien-pho-bien/README.md)
