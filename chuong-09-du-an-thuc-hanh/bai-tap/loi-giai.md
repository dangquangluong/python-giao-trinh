# Lời Giải Chương 9: Starter Code

## Dự Án 1: Todo CLI (starter)

```python
import json, sys                             # Import modules
from pathlib import Path

FILE = Path("todos.json")                    # File lưu data

def load():                                  # Đọc todos từ file
    if FILE.exists():
        return json.loads(FILE.read_text(encoding="utf-8"))
    return []                                # Trả list rỗng nếu chưa có file

def save(todos):                             # Ghi todos ra file
    FILE.write_text(json.dumps(todos, ensure_ascii=False, indent=2), encoding="utf-8")

def main():
    todos = load()
    if len(sys.argv) < 2:
        print("Dùng: python todo.py [add|list|done|del] [args]")
        return

    cmd = sys.argv[1]
    if cmd == "add":                         # Thêm todo mới
        text = " ".join(sys.argv[2:])
        todos.append({"text": text, "done": False})
        print(f"✅ Đã thêm: {text}")
    elif cmd == "list":                      # Liệt kê
        for i, t in enumerate(todos):
            icon = "✅" if t["done"] else "⬜"
            print(f"  {icon} [{i}] {t['text']}")
    elif cmd == "done":                      # Đánh dấu xong
        idx = int(sys.argv[2])
        todos[idx]["done"] = True
        print(f"✅ Hoàn thành!")
    elif cmd == "del":                       # Xóa
        idx = int(sys.argv[2])
        removed = todos.pop(idx)
        print(f"🗑️ Đã xóa: {removed['text']}")

    save(todos)

if __name__ == "__main__":
    main()
```

*(Xem Chương 9 README cho code đầy đủ các dự án)*
