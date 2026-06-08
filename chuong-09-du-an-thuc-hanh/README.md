# Chuong 9: Du An Thuc Hanh

## Tong Quan

Chuong nay bao gom 4 du an thuc hanh giup ban ap dung tat ca kien thuc da hoc tu chuong 1 den chuong 8.

## Du An 1: CLI Todo App

### Mo ta
Ung dung quan ly cong viec tren terminal voi cac chuc nang: them, xoa, danh dau hoan thanh, luu vao file.

### Cong nghe su dung
- `argparse` hoac `click` cho CLI
- File JSON de luu du lieu
- Dataclass cho model

### Tinh nang
- Them task moi
- Liet ke tat ca task
- Danh dau task hoan thanh
- Xoa task
- Loc theo trang thai (done/pending)
- Luu/Doc tu file JSON

### Cau truc

```
todo-cli/
    todo.py          # Entry point
    models.py        # Dataclass Task
    storage.py       # Doc/ghi JSON
    requirements.txt
```

### Vi du su dung

```bash
python todo.py add "Hoc Python chuong 9"
python todo.py list
python todo.py done 1
python todo.py delete 1
python todo.py list --filter pending
```

## Du An 2: Web Scraper

### Mo ta
Chuong trinh thu thap du lieu tu trang web, xu ly va luu vao file CSV.

### Cong nghe su dung
- `requests` de tai trang web
- `beautifulsoup4` de parse HTML
- `pandas` de xu ly va xuat du lieu
- `time` de rate limiting

### Tinh nang
- Tai noi dung trang web
- Parse HTML lay du lieu can thiet
- Xu ly pagination (nhieu trang)
- Luu ket qua ra CSV
- Xu ly loi va retry

### Cau truc

```
web-scraper/
    scraper.py       # Logic chinh
    parser.py        # Parse HTML
    exporter.py      # Xuat CSV/JSON
    config.py        # Cau hinh
    requirements.txt
```

### Vi du code

```python
import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

def scrape_quotes(base_url, max_pages=5):
    """Thu thap quotes tu trang web."""
    all_quotes = []
    
    for page in range(1, max_pages + 1):
        url = f"{base_url}/page/{page}/"
        print(f"Dang tai trang {page}...")
        
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
        except requests.RequestException as e:
            print(f"Loi: {e}")
            break
        
        soup = BeautifulSoup(response.text, "html.parser")
        quotes = soup.select(".quote")
        
        if not quotes:
            break
        
        for quote in quotes:
            text = quote.select_one(".text").get_text()
            author = quote.select_one(".author").get_text()
            tags = [tag.get_text() for tag in quote.select(".tag")]
            all_quotes.append({
                "text": text,
                "author": author,
                "tags": ", ".join(tags)
            })
        
        time.sleep(1)  # Rate limiting
    
    return pd.DataFrame(all_quotes)

# Su dung
df = scrape_quotes("http://quotes.toscrape.com")
df.to_csv("quotes.csv", index=False)
print(f"Da thu thap {len(df)} quotes")
```

## Du An 3: REST API

### Mo ta
Xay dung REST API quan ly sinh vien voi FastAPI, bao gom authentication va CRUD operations.

### Cong nghe su dung
- `fastapi` cho web framework
- `uvicorn` cho ASGI server
- `pydantic` cho validation
- `SQLite` cho database (hoac JSON file)
- `pytest` cho testing

### Tinh nang
- CRUD sinh vien (Create, Read, Update, Delete)
- Tim kiem va loc du lieu
- Phan trang (pagination)
- Validation du lieu dau vao
- Error handling

### Cau truc

```
student-api/
    main.py           # FastAPI app
    models.py         # Pydantic models
    database.py       # Database operations
    routers/
        students.py   # Student routes
    tests/
        test_api.py   # API tests
    requirements.txt
```

### Vi du code

```python
from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel, Field
from typing import Optional, List

app = FastAPI(title="Student Management API")

# Models
class StudentCreate(BaseModel):
    ten: str = Field(..., min_length=1, max_length=100)
    mssv: str = Field(..., pattern=r"^SV\d{3,}$")
    email: str
    diem_tb: float = Field(ge=0, le=10)
    lop: str

class StudentResponse(StudentCreate):
    id: int
    xep_loai: str

# Endpoints
@app.get("/api/students", response_model=List[StudentResponse])
def get_students(
    lop: Optional[str] = None,
    min_diem: Optional[float] = None,
    skip: int = Query(default=0, ge=0),
    limit: int = Query(default=10, ge=1, le=100)
):
    """Lay danh sach sinh vien voi filter va pagination."""
    pass

@app.post("/api/students", response_model=StudentResponse, status_code=201)
def create_student(student: StudentCreate):
    """Them sinh vien moi."""
    pass

@app.get("/api/students/{student_id}", response_model=StudentResponse)
def get_student(student_id: int):
    """Lay thong tin mot sinh vien."""
    pass

@app.put("/api/students/{student_id}", response_model=StudentResponse)
def update_student(student_id: int, student: StudentCreate):
    """Cap nhat thong tin sinh vien."""
    pass

@app.delete("/api/students/{student_id}", status_code=204)
def delete_student(student_id: int):
    """Xoa sinh vien."""
    pass
```

## Du An 4: Automation Script

### Mo ta
Bo cong cu tu dong hoa cac tac vu hang ngay: sao luu file, gui email bao cao, giam sat he thong.

### Cong nghe su dung
- `os` va `pathlib` cho file operations
- `shutil` cho copy/archive
- `schedule` cho lap lich
- `logging` cho ghi log
- `smtplib` cho gui email (optional)

### Tinh nang
- Sao luu thu muc theo lich
- Doc va phan tich file log
- Giam sat dung luong o dia
- Tao bao cao tu dong
- Gui thong bao khi co su co

### Cau truc

```
automation/
    backup.py         # Sao luu file
    monitor.py        # Giam sat he thong
    report.py         # Tao bao cao
    scheduler.py      # Lap lich chay
    config.yaml       # Cau hinh
    requirements.txt
```

### Vi du code

```python
import os
import shutil
from pathlib import Path
from datetime import datetime
import logging

# Cau hinh logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("backup.log"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

def backup_directory(source, backup_dir, max_backups=5):
    """Sao luu thu muc vao file zip."""
    source = Path(source)
    backup_dir = Path(backup_dir)
    backup_dir.mkdir(parents=True, exist_ok=True)
    
    # Tao ten file backup voi timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_name = f"{source.name}_{timestamp}"
    backup_path = backup_dir / backup_name
    
    # Tao archive
    logger.info(f"Bat dau sao luu: {source} -> {backup_path}.zip")
    shutil.make_archive(str(backup_path), "zip", str(source))
    
    size = os.path.getsize(f"{backup_path}.zip")
    logger.info(f"Hoan tat! Kich thuoc: {size / 1024 / 1024:.2f} MB")
    
    # Xoa backup cu neu vuot qua so luong toi da
    backups = sorted(backup_dir.glob(f"{source.name}_*.zip"))
    while len(backups) > max_backups:
        oldest = backups.pop(0)
        oldest.unlink()
        logger.info(f"Da xoa backup cu: {oldest.name}")
    
    return f"{backup_path}.zip"

def check_disk_usage(threshold=80):
    """Kiem tra dung luong dia."""
    import shutil
    total, used, free = shutil.disk_usage("/")
    percent = (used / total) * 100
    
    info = {
        "total_gb": total / (2**30),
        "used_gb": used / (2**30),
        "free_gb": free / (2**30),
        "percent_used": percent
    }
    
    if percent > threshold:
        logger.warning(f"CANH BAO: Dia da su dung {percent:.1f}%!")
    else:
        logger.info(f"Disk OK: {percent:.1f}% da su dung")
    
    return info
```

## Huong Dan Thuc Hien

### Buoc 1: Chon du an
Chon 1-2 du an phu hop voi trinh do va so thich cua ban.

### Buoc 2: Lap ke hoach
- Xac dinh cac tinh nang can lam
- Chia nho thanh cac task
- Thiet ke cau truc thu muc

### Buoc 3: Code va Test
- Code tung tinh nang mot
- Viet test cho moi tinh nang
- Commit thuong xuyen

### Buoc 4: Hoan thien
- Them error handling
- Viet documentation
- Refactor code

## Bai Tap

1. Hoan thanh du an CLI Todo App voi day du chuc nang
2. Xay dung web scraper thu thap du lieu tu mot trang web ban quan tam
3. Tao REST API hoan chinh voi CRUD, validation, va test
4. Viet automation script sao luu thu muc quan trong tren may tinh cua ban
5. Ket hop: Tao API + CLI client goi API do
6. Them feature cho bat ky du an nao: logging, configuration file, error handling nang cao

## Tai Lieu Tham Khao

- [Click Documentation](https://click.palletsprojects.com/)
- [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/doc/)
- [FastAPI Tutorial](https://fastapi.tiangolo.com/tutorial/)
- [Python Automation](https://automatetheboringstuff.com/)
