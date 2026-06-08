# Chương 1: Giới Thiệu Python & Cài Đặt

## 1.1 Python Là Gì?

**Python** là ngôn ngữ lập trình bậc cao, đa năng, được Guido van Rossum tạo ra năm 1991. Python nổi tiếng vì cú pháp đơn giản, dễ đọc, dễ học.

### Đặc Điểm

| Đặc điểm | Mô tả |
|-----------|--------|
| **Dễ học** | Cú pháp gần tiếng Anh, ngắn gọn |
| **Đa năng** | Web, AI, Data Science, Automation, Game... |
| **Thông dịch** | Không cần compile, chạy trực tiếp |
| **Cộng đồng lớn** | Hàng triệu thư viện miễn phí (PyPI) |
| **Cross-platform** | Chạy trên Windows, Mac, Linux |

### Python Dùng Để Làm Gì?

| Lĩnh vực | Thư viện/Framework |
|-----------|-------------------|
| **Web Development** | Django, Flask, FastAPI |
| **Data Science** | Pandas, NumPy, Matplotlib |
| **Machine Learning** | TensorFlow, PyTorch, scikit-learn |
| **Automation** | Selenium, PyAutoGUI, Schedule |
| **Game** | Pygame |
| **Desktop App** | Tkinter, PyQt |
| **DevOps** | Ansible, Fabric |

## 1.2 Cài Đặt Python

### Windows

1. Tải từ [python.org/downloads](https://www.python.org/downloads/)
2. Chạy installer
3. ✅ **QUAN TRỌNG**: Tick "Add Python to PATH"
4. Nhấn Install Now

### macOS

```bash
# Cách 1: Homebrew (khuyến nghị)
brew install python

# Cách 2: Tải từ python.org
```

### Linux

```bash
# Ubuntu / Debian
sudo apt update
sudo apt install python3 python3-pip python3-venv

# Fedora
sudo dnf install python3 python3-pip
```

### Kiểm tra

```bash
python3 --version    # Python 3.12.x
pip3 --version       # pip 24.x
```

## 1.3 IDE / Editor

| Editor | Ưu điểm |
|--------|---------|
| **VS Code** | Miễn phí, nhẹ, nhiều extension (khuyến nghị) |
| **PyCharm** | IDE chuyên Python, mạnh mẽ |
| **Jupyter Notebook** | Tương tác, tốt cho Data Science |
| **IDLE** | Đi kèm Python, đơn giản |

### Cài VS Code + Python Extension

1. Tải [VS Code](https://code.visualstudio.com/)
2. Mở Extensions (Ctrl+Shift+X)
3. Tìm "Python" của Microsoft → Install

## 1.4 Chương Trình Đầu Tiên

### Cách 1: File .py

Tạo file `hello.py`:

```python
# Chương trình đầu tiên
print("Xin chào, Python! 🐍")

# Biến và in ra
ten = "Bạn"
print(f"Xin chào, {ten}! Chào mừng đến với Python.")
```

Chạy:
```bash
python3 hello.py
```

### Cách 2: Interactive (REPL)

```bash
python3
>>> print("Hello!")
Hello!
>>> 2 + 3
5
>>> exit()
```

## 1.5 Virtual Environment (Môi Trường Ảo)

```bash
# Tạo virtual environment
python3 -m venv myenv

# Kích hoạt
# Linux/Mac:
source myenv/bin/activate
# Windows:
myenv\Scripts\activate

# Cài package trong venv
pip install requests

# Thoát venv
deactivate
```

## 1.6 pip - Package Manager

```bash
pip install package_name       # Cài package
pip install requests flask     # Cài nhiều package
pip uninstall package_name     # Gỡ package
pip list                       # Danh sách đã cài
pip freeze > requirements.txt  # Xuất danh sách
pip install -r requirements.txt # Cài từ file
```

## 1.7 Bài Tập

1. Cài Python trên máy, kiểm tra version
2. Viết chương trình in ra tên và tuổi của bạn
3. Tạo virtual environment và cài thử package `requests`
4. Thử Python REPL: tính 2**100, len("xin chào")

---

📖 **Tiếp theo**: [Chương 2 - Cú pháp cơ bản](../chuong-02-cu-phap-co-ban/README.md)
