# Chương 8: Thư Viện Phổ Biến

## 8.1 requests - HTTP Client

```bash
pip install requests
```

```python
import requests

# GET request
resp = requests.get("https://api.github.com/users/python")
print(f"Status: {resp.status_code}")
data = resp.json()
print(f"Name: {data['name']}")

# POST request
resp = requests.post("https://httpbin.org/post", json={
    "ten": "Python",
    "version": "3.12"
})
print(resp.json())

# Với headers & params
resp = requests.get(
    "https://api.example.com/search",
    params={"q": "python", "limit": 10},
    headers={"Authorization": "Bearer token123"},
    timeout=10
)

# Download file
resp = requests.get("https://example.com/file.pdf", stream=True)
with open("file.pdf", "wb") as f:
    for chunk in resp.iter_content(chunk_size=8192):
        f.write(chunk)
```

## 8.2 FastAPI - Web Framework

```bash
pip install fastapi uvicorn
```

```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

# Model
class SinhVien(BaseModel):
    id: Optional[int] = None
    ten: str
    tuoi: int
    diem: float

# "Database"
db: List[SinhVien] = []
next_id = 1

@app.get("/")
def home():
    return {"message": "API Quản lý Sinh viên"}

@app.get("/students", response_model=List[SinhVien])
def get_students():
    return db

@app.post("/students", response_model=SinhVien, status_code=201)
def create_student(sv: SinhVien):
    global next_id
    sv.id = next_id
    next_id += 1
    db.append(sv)
    return sv

@app.get("/students/{student_id}")
def get_student(student_id: int):
    for sv in db:
        if sv.id == student_id:
            return sv
    raise HTTPException(status_code=404, detail="Không tìm thấy")

@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    for i, sv in enumerate(db):
        if sv.id == student_id:
            db.pop(i)
            return {"message": "Đã xóa"}
    raise HTTPException(status_code=404, detail="Không tìm thấy")

# Chạy: uvicorn main:app --reload
# Docs: http://localhost:8000/docs
```

## 8.3 SQLAlchemy - Database ORM

```bash
pip install sqlalchemy
```

```python
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import declarative_base, sessionmaker

# Setup
engine = create_engine("sqlite:///students.db")
Base = declarative_base()
Session = sessionmaker(bind=engine)

# Model
class Student(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True)
    ten = Column(String(100), nullable=False)
    tuoi = Column(Integer)
    diem = Column(Float)

    def __repr__(self):
        return f"Student({self.ten}, {self.diem})"

# Tạo bảng
Base.metadata.create_all(engine)

# CRUD
session = Session()

# Create
sv = Student(ten="Nguyễn A", tuoi=22, diem=8.5)
session.add(sv)
session.commit()

# Read
all_students = session.query(Student).all()
gioi = session.query(Student).filter(Student.diem >= 8.0).all()

# Update
sv = session.query(Student).filter_by(ten="Nguyễn A").first()
sv.diem = 9.0
session.commit()

# Delete
session.query(Student).filter_by(ten="Nguyễn A").delete()
session.commit()
```

## 8.4 pytest - Testing

```bash
pip install pytest
```

```python
# file: test_calculator.py
def cong(a, b):
    return a + b

def chia(a, b):
    if b == 0:
        raise ValueError("Chia cho 0!")
    return a / b

# Tests
def test_cong():
    assert cong(2, 3) == 5
    assert cong(-1, 1) == 0
    assert cong(0, 0) == 0

def test_chia():
    assert chia(10, 2) == 5.0
    assert chia(7, 2) == 3.5

def test_chia_cho_0():
    import pytest
    with pytest.raises(ValueError):
        chia(10, 0)

# Chạy: pytest test_calculator.py -v
```

### Fixtures

```python
import pytest

@pytest.fixture
def sample_data():
    return [1, 2, 3, 4, 5]

@pytest.fixture
def empty_list():
    return []

def test_sum(sample_data):
    assert sum(sample_data) == 15

def test_empty(empty_list):
    assert len(empty_list) == 0
```

## 8.5 pandas - Data Analysis

```bash
pip install pandas
```

```python
import pandas as pd

# Tạo DataFrame
df = pd.DataFrame({
    "ten": ["An", "Binh", "Cuong", "Dung", "Em"],
    "tuoi": [22, 21, 23, 20, 22],
    "diem_python": [8.5, 7.0, 9.2, 6.5, 8.0],
    "diem_sql": [7.5, 8.0, 8.5, 7.0, 9.0],
})

# Thao tác cơ bản
print(df.head())
print(df.describe())
print(df.info())

# Thêm cột
df["diem_tb"] = (df["diem_python"] + df["diem_sql"]) / 2

# Lọc
gioi = df[df["diem_tb"] >= 8.0]
print(gioi)

# Sắp xếp
df_sorted = df.sort_values("diem_tb", ascending=False)

# Group by
# df.groupby("lop")["diem"].mean()

# Đọc/ghi CSV
df.to_csv("students.csv", index=False)
df2 = pd.read_csv("students.csv")
```

## 8.6 Các Thư Viện Khác Nên Biết

| Thư viện | Dùng cho |
|----------|----------|
| `matplotlib` / `seaborn` | Vẽ biểu đồ |
| `numpy` | Tính toán số học |
| `beautifulsoup4` | Web scraping |
| `selenium` | Tự động hóa browser |
| `celery` | Task queue |
| `pydantic` | Data validation |
| `click` / `typer` | CLI tool |
| `python-dotenv` | Quản lý env variables |
| `loguru` | Logging đẹp hơn |
| `httpx` | HTTP client async |

## 8.7 Bài Tập

1. Dùng requests: gọi API thời tiết, hiển thị kết quả
2. Tạo FastAPI CRUD cho quản lý sản phẩm
3. Viết test cho hàm tính toán
4. Dùng pandas phân tích file CSV

---

📖 **Trước đó**: [Chương 7](../chuong-07-cau-truc-du-lieu-nang-cao/README.md) | **Tiếp theo**: [Chương 9](../chuong-09-du-an-thuc-hanh/README.md)
