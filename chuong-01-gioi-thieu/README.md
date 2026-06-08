# Chuong 1: Gioi Thieu Python

## 1.1 Python La Gi?

Python la mot ngon ngu lap trinh bac cao, da muc dich, duoc tao ra boi Guido van Rossum va phat hanh lan dau nam 1991. Python noi tieng voi cu phap don gian, de doc va de hoc.

### Dac Diem Noi Bat

- **De hoc**: Cu phap ro rang, gan voi ngon ngu tu nhien
- **Da muc dich**: Web, data science, AI, automation, game, ...
- **Thu vien phong phu**: PyPI co hon 400,000 package
- **Cong dong lon**: Ho tro tu cong dong toan cau
- **Da nen tang**: Chay tren Windows, Linux, macOS

## 1.2 Lich Su Phat Trien

| Nam | Su Kien |
|-----|---------|
| 1991 | Python 0.9.0 duoc phat hanh |
| 2000 | Python 2.0 - List comprehension, garbage collection |
| 2008 | Python 3.0 - Phien ban hien dai, khong tuong thich nguoc |
| 2020 | Python 2 ket thuc ho tro (EOL) |
| 2023 | Python 3.12 - Hieu suat cai thien, error message tot hon |
| 2024 | Python 3.13 - GIL tu chon, JIT compiler thi nghiem |

## 1.3 Ung Dung Cua Python

### Web Development
- Django, Flask, FastAPI
- Backend API, full-stack web

### Data Science & AI
- NumPy, Pandas, Matplotlib
- TensorFlow, PyTorch, scikit-learn

### Automation & Scripting
- Tu dong hoa tac vu
- Web scraping, xu ly file

### DevOps
- Ansible, SaltStack
- AWS SDK (boto3), scripting

## 1.4 Cai Dat Python

### Windows

1. Truy cap [python.org/downloads](https://www.python.org/downloads/)
2. Tai phien ban moi nhat (3.12+)
3. Chay file installer
4. **Quan trong**: Tick chon "Add Python to PATH"
5. Nhan "Install Now"

Kiem tra:
```bash
python --version
pip --version
```

### Linux (Ubuntu/Debian)

```bash
# Python thuong duoc cai san
python3 --version

# Neu chua co, cai dat:
sudo apt update
sudo apt install python3 python3-pip python3-venv
```

### macOS

```bash
# Su dung Homebrew
brew install python3

# Kiem tra
python3 --version
```

## 1.5 Thiet Lap IDE

### VS Code (Khuyen Nghi)

1. Tai VS Code tu [code.visualstudio.com](https://code.visualstudio.com)
2. Cai dat extension "Python" cua Microsoft
3. Cai dat extension "Pylance" de ho tro IntelliSense
4. Chon Python interpreter: `Ctrl+Shift+P` > "Python: Select Interpreter"

### PyCharm

1. Tai tu [jetbrains.com/pycharm](https://www.jetbrains.com/pycharm/)
2. Phien ban Community mien phi, du dung cho hoc tap
3. Tao project moi va chon Python interpreter

### Jupyter Notebook

```bash
pip install jupyter
jupyter notebook
```

Phu hop cho hoc tap, thi nghiem va data science.

## 1.6 Moi Truong Ao (Virtual Environment)

Moi truong ao giup cach ly cac thu vien giua cac du an khac nhau.

```bash
# Tao moi truong ao
python3 -m venv myproject_env

# Kich hoat (Linux/Mac)
source myproject_env/bin/activate

# Kich hoat (Windows)
myproject_env\Scripts\activate

# Huy kich hoat
deactivate
```

## 1.7 Chuong Trinh Dau Tien

Tao file `hello.py`:

```python
# Chuong trinh dau tien
print("Xin chao, Python!")

# In nhieu dong
print("Toi dang hoc Python")
print("Python rat thu vi!")

# Phep tinh don gian
print(f"2 + 3 = {2 + 3}")
print(f"10 / 3 = {10 / 3:.2f}")
```

Chay chuong trinh:
```bash
python3 hello.py
```

Ket qua:
```
Xin chao, Python!
Toi dang hoc Python
Python rat thu vi!
2 + 3 = 5
10 / 3 = 3.33
```

## 1.8 Python Interactive Shell (REPL)

```bash
$ python3
Python 3.12.0 (...)
>>> 2 + 3
5
>>> print("Hello")
Hello
>>> exit()
```

REPL (Read-Eval-Print Loop) rat huu ich de thu nghiem nhanh cac doan code.

## Bai Tap

1. Cai dat Python 3.12+ tren may tinh cua ban
2. Cai dat VS Code va extension Python
3. Tao moi truong ao va kich hoat no
4. Viet chuong trinh in ra ten, tuoi va so thich cua ban
5. Su dung Python REPL de thuc hien cac phep tinh: cong, tru, nhan, chia, luy thua
6. Tim hieu them ve `pip` bang lenh `pip --help`

## Tai Lieu Tham Khao

- [Python Official Documentation](https://docs.python.org/3/)
- [Python Tutorial](https://docs.python.org/3/tutorial/)
- [Real Python](https://realpython.com)
