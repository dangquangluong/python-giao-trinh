# Chương 8: Thư Viện Phổ Biến

## 8.1 requests - HTTP Client

```bash
pip install requests
```

```python
import requests                              # Thư viện HTTP phổ biến nhất Python

# GET request
resp = requests.get("https://api.github.com/users/python")  # Gửi GET request đến URL
print(f"Status: {resp.status_code}")         # In mã trạng thái HTTP (200=OK, 404=Not Found)
data = resp.json()                           # .json() parse response body thành dict/list Python
print(f"Name: {data['name']}")               # Truy cập dữ liệu từ JSON response

# POST request
resp = requests.post("https://httpbin.org/post", json={  # POST gửi dữ liệu lên server
    "ten": "Python",                         # json= tự chuyển dict thành JSON body
    "version": "3.12"
})
print(resp.json())                           # In response từ server

# Với headers & params
resp = requests.get(
    "https://api.example.com/search",        # URL cơ sở
    params={"q": "python", "limit": 10},     # params= tự thêm ?q=python&limit=10 vào URL
    headers={"Authorization": "Bearer token123"},  # headers= gửi kèm HTTP headers
    timeout=10                               # timeout=10: đợi tối đa 10 giây
)

# Download file
resp = requests.get("https://example.com/file.pdf", stream=True)  # stream=True: không load hết vào RAM
with open("file.pdf", "wb") as f:            # "wb" = write binary (file nhị phân)
    for chunk in resp.iter_content(chunk_size=8192):  # Đọc từng chunk 8KB
        f.write(chunk)                       # Ghi từng chunk vào file
```

## 8.2 FastAPI - Web Framework

```bash
pip install fastapi uvicorn
```

```python
from fastapi import FastAPI, HTTPException   # FastAPI framework + class lỗi HTTP
from pydantic import BaseModel               # Pydantic: validate dữ liệu tự động
from typing import List, Optional            # Type hints

app = FastAPI()                              # Tạo ứng dụng FastAPI

# Model - định nghĩa cấu trúc dữ liệu (Pydantic tự validate)
class SinhVien(BaseModel):                   # Kế thừa BaseModel để tự validate kiểu
    id: Optional[int] = None                 # Optional: có thể None, mặc định None
    ten: str                                 # Bắt buộc phải là str
    tuoi: int                                # Bắt buộc phải là int
    diem: float                              # Bắt buộc phải là float

# "Database" (giả lập bằng list)
db: List[SinhVien] = []                      # List lưu trữ sinh viên
next_id = 1                                  # Biến đếm ID

@app.get("/")                                # Decorator đăng ký route GET /
def home():                                  # Hàm xử lý khi truy cập GET /
    return {"message": "API Quản lý Sinh viên"}  # Trả về JSON tự động

@app.get("/students", response_model=List[SinhVien])  # GET /students, response là List SinhVien
def get_students():                          # Hàm lấy danh sách sinh viên
    return db                                # Trả về toàn bộ list

@app.post("/students", response_model=SinhVien, status_code=201)  # POST tạo mới, trả về 201
def create_student(sv: SinhVien):            # FastAPI tự parse JSON body thành SinhVien
    global next_id                           # global để sửa biến ngoài hàm
    sv.id = next_id                          # Gán ID
    next_id += 1                             # Tăng ID
    db.append(sv)                            # Thêm vào "database"
    return sv                                # Trả về object vừa tạo

@app.get("/students/{student_id}")           # {student_id} = path parameter (động)
def get_student(student_id: int):            # FastAPI tự ép kiểu từ URL string thành int
    for sv in db:
        if sv.id == student_id:
            return sv                        # Trả về nếu tìm thấy
    raise HTTPException(status_code=404, detail="Không tìm thấy")  # Ném lỗi 404

@app.delete("/students/{student_id}")        # DELETE method
def delete_student(student_id: int):
    for i, sv in enumerate(db):              # Lặp với index để xóa
        if sv.id == student_id:
            db.pop(i)                        # .pop(i) xóa phần tử tại index i
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
from sqlalchemy import create_engine, Column, Integer, String, Float  # SQLAlchemy components
from sqlalchemy.orm import declarative_base, sessionmaker  # ORM tools

# Setup
engine = create_engine("sqlite:///students.db")  # Tạo engine kết nối SQLite
Base = declarative_base()                    # Base class cho tất cả model
Session = sessionmaker(bind=engine)          # Factory tạo session (phiên làm việc với DB)

# Model - định nghĩa bảng bằng class
class Student(Base):                         # Kế thừa Base = đây là bảng trong DB
    __tablename__ = "students"               # Tên bảng trong database
    id = Column(Integer, primary_key=True)   # Cột id, số nguyên, khóa chính (tự tăng)
    ten = Column(String(100), nullable=False) # Cột tên, chuỗi max 100 ký tự, không được null
    tuoi = Column(Integer)                   # Cột tuổi, số nguyên
    diem = Column(Float)                     # Cột điểm, số thực

    def __repr__(self):                      # Chuỗi mô tả object
        return f"Student({self.ten}, {self.diem})"

# Tạo bảng
Base.metadata.create_all(engine)             # Tạo tất cả bảng đã định nghĩa trong DB

# CRUD operations
session = Session()                          # Tạo session mới

# Create
sv = Student(ten="Nguyễn A", tuoi=22, diem=8.5)  # Tạo object Student
session.add(sv)                              # Thêm vào session (chưa lưu DB)
session.commit()                             # commit() lưu thay đổi vào DB

# Read
all_students = session.query(Student).all()  # .all() lấy tất cả bản ghi
gioi = session.query(Student).filter(Student.diem >= 8.0).all()  # .filter() lọc

# Update
sv = session.query(Student).filter_by(ten="Nguyễn A").first()  # .first() lấy 1 kết quả
sv.diem = 9.0                                # Sửa thuộc tính
session.commit()                             # Lưu thay đổi

# Delete
session.query(Student).filter_by(ten="Nguyễn A").delete()  # Xóa bản ghi khớp
session.commit()                             # Lưu thay đổi
```

## 8.4 pytest - Testing

```bash
pip install pytest
```

```python
# file: test_calculator.py
def cong(a, b):                              # Hàm cần test
    return a + b

def chia(a, b):                              # Hàm chia có xử lý lỗi
    if b == 0:
        raise ValueError("Chia cho 0!")      # Ném lỗi khi chia cho 0
    return a / b

# Tests - tên hàm test bắt đầu bằng test_
def test_cong():                             # pytest tự tìm và chạy hàm test_*
    assert cong(2, 3) == 5                   # assert: nếu False thì test FAIL
    assert cong(-1, 1) == 0                  # Test với số âm
    assert cong(0, 0) == 0                   # Test với 0

def test_chia():                             # Test hàm chia
    assert chia(10, 2) == 5.0                # Kiểm tra kết quả đúng
    assert chia(7, 2) == 3.5

def test_chia_cho_0():                       # Test exception
    import pytest
    with pytest.raises(ValueError):          # Kỳ vọng ValueError được ném ra
        chia(10, 0)                          # Gọi hàm với b=0

# Chạy: pytest test_calculator.py -v
```

### Fixtures

```python
import pytest                                # Import pytest

@pytest.fixture                              # @fixture = hàm chuẩn bị dữ liệu test (setup)
def sample_data():                           # pytest tự gọi fixture khi test cần
    return [1, 2, 3, 4, 5]                  # Trả về dữ liệu mẫu

@pytest.fixture
def empty_list():                            # Fixture tạo list rỗng
    return []

def test_sum(sample_data):                   # Tham số trùng tên fixture = tự inject dữ liệu
    assert sum(sample_data) == 15            # Test với dữ liệu từ fixture

def test_empty(empty_list):                  # Nhận empty_list từ fixture
    assert len(empty_list) == 0              # Kiểm tra list rỗng
```

## 8.5 pandas - Data Analysis

```bash
pip install pandas
```

```python
import pandas as pd                          # Import pandas với alias pd (quy ước)

# Tạo DataFrame (bảng 2 chiều)
df = pd.DataFrame({                          # DataFrame từ dict (mỗi key = 1 cột)
    "ten": ["An", "Binh", "Cuong", "Dung", "Em"],  # Cột tên
    "tuoi": [22, 21, 23, 20, 22],           # Cột tuổi
    "diem_python": [8.5, 7.0, 9.2, 6.5, 8.0],  # Cột điểm Python
    "diem_sql": [7.5, 8.0, 8.5, 7.0, 9.0],     # Cột điểm SQL
})

# Thao tác cơ bản
print(df.head())                             # .head() in 5 dòng đầu
print(df.describe())                         # .describe() thống kê (mean, std, min, max)
print(df.info())                             # .info() thông tin kiểu dữ liệu, null

# Thêm cột mới
df["diem_tb"] = (df["diem_python"] + df["diem_sql"]) / 2  # Tạo cột mới từ phép tính

# Lọc dữ liệu
gioi = df[df["diem_tb"] >= 8.0]             # Lọc hàng: chỉ giữ dòng có diem_tb >= 8
print(gioi)                                  # In kết quả lọc

# Sắp xếp
df_sorted = df.sort_values("diem_tb", ascending=False)  # Sắp theo diem_tb giảm dần

# Group by
# df.groupby("lop")["diem"].mean()          # Nhóm theo lớp, tính điểm TB mỗi nhóm

# Đọc/ghi CSV
df.to_csv("students.csv", index=False)       # Ghi DataFrame ra file CSV
df2 = pd.read_csv("students.csv")            # Đọc CSV thành DataFrame
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
