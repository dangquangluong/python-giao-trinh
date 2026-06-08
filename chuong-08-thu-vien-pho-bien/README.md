# Chuong 8: Thu Vien Pho Bien

## 8.1 Requests - HTTP Client

Thu vien `requests` giup gui HTTP request mot cach don gian.

### Cai dat

```bash
pip install requests
```

### GET request

```python
import requests

# GET don gian
response = requests.get("https://api.github.com/users/python")
print(f"Status: {response.status_code}")
print(f"Content-Type: {response.headers['content-type']}")
data = response.json()
print(f"Name: {data['name']}")

# GET voi params
params = {"q": "python", "sort": "stars"}
response = requests.get("https://api.github.com/search/repositories", params=params)
```

### POST request

```python
import requests

# POST voi JSON
data = {"title": "foo", "body": "bar", "userId": 1}
response = requests.post(
    "https://jsonplaceholder.typicode.com/posts",
    json=data
)
print(response.status_code)  # 201
print(response.json())
```

### Session va Headers

```python
import requests

session = requests.Session()
session.headers.update({
    "Authorization": "Bearer token_xyz",
    "Content-Type": "application/json"
})

# Tat ca request trong session se co headers nay
response = session.get("https://api.example.com/data")
```

### Xu ly loi

```python
import requests
from requests.exceptions import RequestException, Timeout

try:
    response = requests.get("https://api.example.com/data", timeout=5)
    response.raise_for_status()
    data = response.json()
except Timeout:
    print("Request qua thoi gian cho")
except RequestException as e:
    print(f"Loi request: {e}")
```

## 8.2 Pandas - Xu Ly Du Lieu

Thu vien `pandas` la cong cu manh me de xu ly va phan tich du lieu.

### Cai dat

```bash
pip install pandas
```

### DataFrame co ban

```python
import pandas as pd

# Tao DataFrame tu dict
data = {
    "ten": ["An", "Binh", "Chi", "Dung", "Em"],
    "tuoi": [22, 25, 23, 21, 24],
    "diem": [8.5, 7.0, 9.2, 6.5, 8.0],
    "lop": ["CNTT", "KTPM", "CNTT", "MMT", "KTPM"]
}
df = pd.DataFrame(data)
print(df)
```

### Doc/Ghi file

```python
# Doc file CSV
df = pd.read_csv("students.csv")

# Doc file Excel
df = pd.read_excel("data.xlsx")

# Ghi ra CSV
df.to_csv("output.csv", index=False)

# Ghi ra Excel
df.to_excel("output.xlsx", index=False)
```

### Loc va truy van du lieu

```python
# Loc theo dieu kien
gioi = df[df["diem"] >= 8.0]
cntt = df[df["lop"] == "CNTT"]

# Nhieu dieu kien
kq = df[(df["diem"] >= 8.0) & (df["tuoi"] < 24)]

# Chon cot
print(df[["ten", "diem"]])

# Sap xep
df_sorted = df.sort_values("diem", ascending=False)
```

### Thong ke va nhom

```python
# Thong ke co ban
print(df["diem"].describe())
print(f"Diem TB: {df['diem'].mean():.2f}")
print(f"Diem cao nhat: {df['diem'].max()}")

# Group by
nhom = df.groupby("lop").agg({
    "diem": ["mean", "max", "min", "count"],
    "tuoi": "mean"
})
print(nhom)
```

### Them va xu ly cot

```python
# Them cot moi
df["xep_loai"] = df["diem"].apply(
    lambda d: "Gioi" if d >= 8 else "Kha" if d >= 7 else "TB"
)

# Xu ly missing values
df.fillna(0, inplace=True)
df.dropna(subset=["diem"], inplace=True)
```

## 8.3 Flask / FastAPI - Web Framework

### Flask co ban

```bash
pip install flask
```

```python
from flask import Flask, jsonify, request

app = Flask(__name__)

# Danh sach du lieu mau
tasks = [
    {"id": 1, "title": "Hoc Python", "done": False},
    {"id": 2, "title": "Lam bai tap", "done": True},
]

@app.route("/")
def home():
    return "Xin chao! Day la API Flask."

@app.route("/api/tasks", methods=["GET"])
def get_tasks():
    return jsonify(tasks)

@app.route("/api/tasks", methods=["POST"])
def create_task():
    data = request.get_json()
    task = {
        "id": len(tasks) + 1,
        "title": data["title"],
        "done": False
    }
    tasks.append(task)
    return jsonify(task), 201

if __name__ == "__main__":
    app.run(debug=True)
```

### FastAPI co ban

```bash
pip install fastapi uvicorn
```

```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI(title="Task API", version="1.0")

# Model
class Task(BaseModel):
    title: str
    done: bool = False

class TaskResponse(Task):
    id: int

# Du lieu mau
tasks = []

@app.get("/")
def root():
    return {"message": "Xin chao! Day la API FastAPI."}

@app.get("/api/tasks", response_model=list[TaskResponse])
def get_tasks():
    return tasks

@app.post("/api/tasks", response_model=TaskResponse, status_code=201)
def create_task(task: Task):
    new_task = TaskResponse(id=len(tasks) + 1, **task.dict())
    tasks.append(new_task)
    return new_task

@app.get("/api/tasks/{task_id}", response_model=TaskResponse)
def get_task(task_id: int):
    for task in tasks:
        if task.id == task_id:
            return task
    raise HTTPException(status_code=404, detail="Task khong ton tai")

# Chay: uvicorn main:app --reload
```

## 8.4 Pytest - Testing

### Cai dat

```bash
pip install pytest
```

### Test co ban

```python
# File: test_calculator.py

def cong(a, b):
    return a + b

def tru(a, b):
    return a - b

def chia(a, b):
    if b == 0:
        raise ValueError("Khong the chia cho 0")
    return a / b

# Test functions
def test_cong():
    assert cong(2, 3) == 5
    assert cong(-1, 1) == 0
    assert cong(0, 0) == 0

def test_tru():
    assert tru(5, 3) == 2
    assert tru(0, 5) == -5

def test_chia():
    assert chia(10, 2) == 5
    assert chia(7, 2) == 3.5

def test_chia_cho_0():
    import pytest
    with pytest.raises(ValueError):
        chia(10, 0)
```

### Fixture

```python
import pytest

@pytest.fixture
def sample_data():
    """Fixture cung cap du lieu mau."""
    return {
        "students": [
            {"ten": "An", "diem": 8.5},
            {"ten": "Binh", "diem": 7.0},
            {"ten": "Chi", "diem": 9.2},
        ]
    }

def test_average(sample_data):
    diem = [s["diem"] for s in sample_data["students"]]
    avg = sum(diem) / len(diem)
    assert round(avg, 2) == 8.23

def test_max_score(sample_data):
    diem = [s["diem"] for s in sample_data["students"]]
    assert max(diem) == 9.2
```

### Parametrize

```python
import pytest

@pytest.mark.parametrize("input,expected", [
    (1, 1),
    (2, 1),
    (3, 2),
    (5, 5),
    (10, 55),
])
def test_fibonacci(input, expected):
    assert fib(input) == expected
```

### Chay test

```bash
# Chay tat ca test
pytest

# Chay voi thong tin chi tiet
pytest -v

# Chay mot file cu the
pytest test_calculator.py

# Chay voi coverage
pip install pytest-cov
pytest --cov=src tests/
```

## 8.5 Cac Thu Vien Khac Dang Chu Y

| Thu Vien | Muc Dich |
|----------|----------|
| `beautifulsoup4` | Web scraping, parse HTML |
| `selenium` | Browser automation |
| `sqlalchemy` | ORM cho database |
| `celery` | Task queue, background jobs |
| `click` | Tao CLI application |
| `rich` | Terminal UI dep |
| `httpx` | HTTP client (async support) |
| `pydantic` | Data validation |
| `pillow` | Xu ly hinh anh |
| `matplotlib` | Ve bieu do |

## Bai Tap

1. Su dung `requests` lay du lieu tu mot API cong khai va in ket qua
2. Tao DataFrame tu danh sach sinh vien, tinh diem TB theo lop
3. Tao REST API don gian voi Flask hoac FastAPI (CRUD cho mot resource)
4. Viet test voi pytest cho mot module tinh toan (cong, tru, nhan, chia)
5. Dung pandas doc file CSV va tao bao cao thong ke
6. Tao FastAPI app voi validation dung Pydantic model

## Tai Lieu Tham Khao

- [Requests Documentation](https://requests.readthedocs.io/)
- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [Flask Documentation](https://flask.palletsprojects.com/)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Pytest Documentation](https://docs.pytest.org/)
