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
import json
import sys
from pathlib import Path
from datetime import datetime

DATA_FILE = Path("todos.json")

def load_todos():
    if DATA_FILE.exists():
        return json.loads(DATA_FILE.read_text(encoding="utf-8"))
    return []

def save_todos(todos):
    DATA_FILE.write_text(
        json.dumps(todos, ensure_ascii=False, indent=2),
        encoding="utf-8"
    )

def add_todo(text):
    todos = load_todos()
    todo = {
        "id": len(todos) + 1,
        "text": text,
        "done": False,
        "created": datetime.now().isoformat()
    }
    todos.append(todo)
    save_todos(todos)
    print(f"✅ Đã thêm: {text}")

def list_todos(show_all=True):
    todos = load_todos()
    if not todos:
        print("📋 Không có task nào!")
        return
    for t in todos:
        status = "✅" if t["done"] else "⬜"
        if show_all or not t["done"]:
            print(f"  {status} [{t['id']}] {t['text']}")

def mark_done(todo_id):
    todos = load_todos()
    for t in todos:
        if t["id"] == todo_id:
            t["done"] = True
            save_todos(todos)
            print(f"✅ Hoàn thành: {t['text']}")
            return
    print(f"❌ Không tìm thấy task #{todo_id}")

def delete_todo(todo_id):
    todos = load_todos()
    todos = [t for t in todos if t["id"] != todo_id]
    save_todos(todos)
    print(f"🗑️ Đã xóa task #{todo_id}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Sử dụng: python todo.py [add|list|done|delete] [args]")
        sys.exit(1)

    cmd = sys.argv[1]
    if cmd == "add" and len(sys.argv) > 2:
        add_todo(" ".join(sys.argv[2:]))
    elif cmd == "list":
        list_todos()
    elif cmd == "done" and len(sys.argv) > 2:
        mark_done(int(sys.argv[2]))
    elif cmd == "delete" and len(sys.argv) > 2:
        delete_todo(int(sys.argv[2]))
    else:
        print("Lệnh không hợp lệ!")
```

---

## Dự Án 2: Web Scraper ⭐⭐

### Mô Tả
Thu thập dữ liệu từ website.

```bash
pip install beautifulsoup4 requests
```

```python
import requests
from bs4 import BeautifulSoup

def scrape_news(url):
    """Lấy tiêu đề tin tức"""
    resp = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
    soup = BeautifulSoup(resp.text, "html.parser")

    articles = []
    for tag in soup.find_all("h2"):
        link = tag.find("a")
        if link:
            articles.append({
                "title": link.get_text(strip=True),
                "url": link.get("href", "")
            })

    return articles

if __name__ == "__main__":
    articles = scrape_news("https://news.ycombinator.com")
    for i, a in enumerate(articles[:10], 1):
        print(f"{i}. {a['title']}")
        print(f"   {a['url']}\n")
```

---

## Dự Án 3: REST API (FastAPI) ⭐⭐⭐

### Mô Tả
API quản lý sách cho thư viện.

```bash
pip install fastapi uvicorn pydantic
```

```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI(title="API Thư Viện", version="1.0")

class Sach(BaseModel):
    id: Optional[int] = None
    tieu_de: str
    tac_gia: str
    nam: int
    the_loai: str

db: List[Sach] = [
    Sach(id=1, tieu_de="Clean Code", tac_gia="Robert Martin", nam=2008, the_loai="Tech"),
    Sach(id=2, tieu_de="Python Crash Course", tac_gia="Eric Matthes", nam=2019, the_loai="Tech"),
]
next_id = 3

@app.get("/books", response_model=List[Sach])
def get_books(the_loai: Optional[str] = None):
    if the_loai:
        return [s for s in db if s.the_loai.lower() == the_loai.lower()]
    return db

@app.get("/books/{book_id}", response_model=Sach)
def get_book(book_id: int):
    for s in db:
        if s.id == book_id:
            return s
    raise HTTPException(404, "Sách không tồn tại")

@app.post("/books", response_model=Sach, status_code=201)
def create_book(sach: Sach):
    global next_id
    sach.id = next_id
    next_id += 1
    db.append(sach)
    return sach

@app.put("/books/{book_id}", response_model=Sach)
def update_book(book_id: int, sach_moi: Sach):
    for i, s in enumerate(db):
        if s.id == book_id:
            sach_moi.id = book_id
            db[i] = sach_moi
            return sach_moi
    raise HTTPException(404, "Sách không tồn tại")

@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    for i, s in enumerate(db):
        if s.id == book_id:
            db.pop(i)
            return {"message": f"Đã xóa sách #{book_id}"}
    raise HTTPException(404, "Sách không tồn tại")

# Chạy: uvicorn main:app --reload
# Docs: http://localhost:8000/docs
```

---

## Dự Án 4: Automation Script ⭐⭐

### Mô Tả
Script tự động hóa: backup file, gửi email, monitor.

```python
import shutil
import os
from datetime import datetime
from pathlib import Path

def backup_directory(source, dest_base):
    """Backup thư mục với timestamp"""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    dest = Path(dest_base) / f"backup_{timestamp}"

    shutil.copytree(source, dest)
    print(f"✅ Backup: {source} → {dest}")

    # Nén
    archive = shutil.make_archive(str(dest), "zip", dest)
    shutil.rmtree(dest)  # Xóa thư mục, giữ zip
    print(f"📦 Nén: {archive}")
    return archive

def cleanup_old_backups(backup_dir, keep=5):
    """Giữ lại N backup mới nhất"""
    backups = sorted(Path(backup_dir).glob("backup_*.zip"), reverse=True)
    for old in backups[keep:]:
        old.unlink()
        print(f"🗑️ Xóa backup cũ: {old.name}")

def disk_usage_report():
    """Báo cáo dung lượng ổ đĩa"""
    total, used, free = shutil.disk_usage("/")
    print(f"💾 Disk: {used//(2**30)}GB / {total//(2**30)}GB (Free: {free//(2**30)}GB)")

if __name__ == "__main__":
    disk_usage_report()
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
