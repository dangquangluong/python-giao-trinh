"""
Chuong 9: Du an Web Scraper (Vi du minh hoa)

Luu y: De chay duoc can cai dat:
    pip install requests beautifulsoup4

Vi du nay minh hoa cau truc cua mot web scraper.
"""

from dataclasses import dataclass, field     # dataclass tạo class ngắn gọn, field tùy chỉnh thuộc tính
from typing import List, Optional            # Type hints cho list và giá trị có thể None
import json                                  # Module xử lý JSON
from datetime import datetime                # Module xử lý ngày giờ


@dataclass                                   # Decorator tự tạo __init__, __repr__
class ScrapedItem:                           # Class đại diện cho 1 item đã thu thập
    """Mot item da thu thap."""              # Docstring
    title: str                               # Tiêu đề/tên tác giả
    content: str                             # Nội dung chính
    url: str                                 # URL nguồn
    tags: List[str] = field(default_factory=list)  # List tag, mặc định = [] (dùng field vì mutable)
    scraped_at: str = field(default_factory=lambda: datetime.now().isoformat())  # Thời gian thu thập (tự động)


class WebScraper:                            # Class chính thực hiện web scraping
    """
    Web scraper co ban.

    Vi du su dung:
        scraper = WebScraper(base_url="http://example.com")
        items = scraper.scrape(max_pages=3)
        scraper.export_json(items, "output.json")
    """

    def __init__(self, base_url: str, delay: float = 1.0):  # Constructor nhận URL gốc và delay giữa requests
        self.base_url = base_url             # Lưu URL gốc của website cần scrape
        self.delay = delay                   # Thời gian chờ giữa các request (giây) - tránh bị block
        self.session = None                  # HTTP session (khởi tạo sau)

    def _init_session(self):                 # Method private (quy ước _) khởi tạo HTTP session
        """Khoi tao HTTP session."""         # Docstring
        try:                                 # Thử import requests
            import requests                  # Thư viện HTTP phổ biến (cần pip install)
            self.session = requests.Session()  # Session giữ cookies, headers giữa các request
            self.session.headers.update({    # Cập nhật header mặc định
                "User-Agent": "Mozilla/5.0 (Educational Python Scraper)"  # Giả lập trình duyệt
            })
        except ImportError:                  # Nếu chưa cài requests
            print("Can cai dat: pip install requests")  # Hướng dẫn cài
            return False                     # Trả về False = thất bại
        return True                          # Trả về True = thành công

    def fetch_page(self, url: str) -> Optional[str]:  # Method tải nội dung trang web
        """Tai noi dung trang web."""        # Docstring
        if not self.session:                 # Nếu chưa có session
            if not self._init_session():     # Thử khởi tạo, nếu thất bại
                return None                  # Trả về None

        try:                                 # Thử tải trang
            import time                      # Module đo thời gian
            response = self.session.get(url, timeout=10)  # Gửi GET request, timeout 10s
            response.raise_for_status()      # Ném lỗi nếu status code >= 400
            time.sleep(self.delay)           # Chờ delay giây (rate limiting - lịch sự với server)
            return response.text             # Trả về HTML dạng chuỗi
        except Exception as e:              # Bắt mọi lỗi
            print(f"Loi khi tai {url}: {e}") # In lỗi
            return None                      # Trả về None

    def parse_page(self, html: str) -> List[ScrapedItem]:  # Method parse HTML thành dữ liệu
        """Parse HTML va trich xuat du lieu."""  # Docstring
        try:                                 # Thử import BeautifulSoup
            from bs4 import BeautifulSoup    # Thư viện parse HTML (cần pip install beautifulsoup4)
        except ImportError:                  # Nếu chưa cài
            print("Can cai dat: pip install beautifulsoup4")  # Hướng dẫn
            return []                        # Trả về list rỗng

        soup = BeautifulSoup(html, "html.parser")  # Parse HTML string thành cây DOM
        items = []                           # List chứa kết quả

        # Vi du: parse quotes tu quotes.toscrape.com
        for quote_div in soup.select(".quote"):  # .select() tìm tất cả thẻ có class="quote"
            text = quote_div.select_one(".text")    # .select_one() tìm 1 thẻ con có class="text"
            author = quote_div.select_one(".author")  # Tìm thẻ có class="author"
            tags = quote_div.select(".tag")  # Tìm tất cả thẻ có class="tag"

            if text and author:              # Nếu tìm thấy cả text và author
                item = ScrapedItem(          # Tạo ScrapedItem mới
                    title=author.get_text(), # .get_text() lấy text bên trong thẻ HTML
                    content=text.get_text(), # Lấy nội dung quote
                    url=self.base_url,       # URL nguồn
                    tags=[t.get_text() for t in tags]  # List comprehension lấy text từng tag
                )
                items.append(item)           # Thêm item vào kết quả

        return items                         # Trả về list các item đã parse

    def scrape(self, max_pages: int = 5) -> List[ScrapedItem]:  # Method scrape nhiều trang
        """Thu thap du lieu tu nhieu trang."""  # Docstring
        all_items = []                       # List chứa tất cả item từ mọi trang

        for page in range(1, max_pages + 1):  # Lặp qua các trang (1 đến max_pages)
            url = f"{self.base_url}/page/{page}/"  # Tạo URL cho từng trang
            print(f"Dang xu ly trang {page}: {url}")  # In tiến trình

            html = self.fetch_page(url)      # Tải nội dung trang
            if not html:                     # Nếu tải thất bại
                break                        # Dừng lại

            items = self.parse_page(html)    # Parse HTML thành items
            if not items:                    # Nếu không tìm được item nào
                print("Khong con du lieu. Dung lai.")  # In thông báo
                break                        # Dừng lại

            all_items.extend(items)          # .extend() thêm tất cả items vào list tổng
            print(f"  -> Thu thap duoc {len(items)} items")  # In số item thu được

        print(f"\nTong cong: {len(all_items)} items")  # In tổng số item
        return all_items                     # Trả về tất cả items

    @staticmethod                            # @staticmethod = method không cần self (gọi qua class)
    def export_json(items: List[ScrapedItem], filename: str):  # Xuất dữ liệu ra file JSON
        """Xuat du lieu ra file JSON."""     # Docstring
        from dataclasses import asdict       # asdict chuyển dataclass thành dict
        data = [asdict(item) for item in items]  # Chuyển list ScrapedItem thành list dict
        with open(filename, "w", encoding="utf-8") as f:  # Mở file để ghi
            json.dump(data, f, ensure_ascii=False, indent=2)  # Ghi JSON đẹp
        print(f"Da luu {len(items)} items vao {filename}")  # In xác nhận

    @staticmethod                            # Static method xuất CSV
    def export_csv(items: List[ScrapedItem], filename: str):  # Xuất dữ liệu ra file CSV
        """Xuat du lieu ra file CSV."""      # Docstring
        import csv                           # Module xử lý file CSV
        with open(filename, "w", encoding="utf-8", newline="") as f:  # Mở file CSV
            writer = csv.writer(f)           # Tạo CSV writer
            writer.writerow(["title", "content", "tags", "url", "scraped_at"])  # Ghi header
            for item in items:               # Lặp qua từng item
                writer.writerow([            # Ghi 1 hàng dữ liệu
                    item.title,              # Cột tiêu đề
                    item.content,            # Cột nội dung
                    ", ".join(item.tags),     # Nối tags thành chuỗi
                    item.url,                # Cột URL
                    item.scraped_at          # Cột thời gian
                ])
        print(f"Da luu {len(items)} items vao {filename}")  # In xác nhận


# === Demo (khong can ket noi mang) ===
def demo_without_network():                  # Hàm demo offline (không cần internet)
    """Demo cau truc scraper khong can mang."""  # Docstring
    print("=== Demo Web Scraper (offline) ===\n")  # In tiêu đề

    # Gia lap du lieu da scrape
    sample_items = [                         # Tạo dữ liệu mẫu giả lập kết quả scraping
        ScrapedItem(                         # Item 1
            title="Albert Einstein",         # Tác giả
            content="Tri tuong tuong quan trong hon kien thuc.",  # Nội dung quote
            url="http://example.com",        # URL nguồn
            tags=["khoa-hoc", "tri-tue"]     # Tags phân loại
        ),
        ScrapedItem(                         # Item 2
            title="Steve Jobs",              # Tác giả
            content="Hay luon khat khao, hay luon dai kho.",  # Quote
            url="http://example.com",        # URL
            tags=["cong-nghe", "truyen-cam-hung"]  # Tags
        ),
        ScrapedItem(                         # Item 3
            title="Lao Tu",                  # Tác giả
            content="Hanh trinh ngan dam bat dau tu mot buoc chan.",  # Quote
            url="http://example.com",        # URL
            tags=["triet-hoc", "cuoc-song"]  # Tags
        ),
    ]

    print("Du lieu thu thap duoc:")          # In tiêu đề
    print("-" * 60)                          # In đường kẻ
    for item in sample_items:                # Lặp qua từng item
        print(f"  Tac gia: {item.title}")    # In tác giả
        print(f"  Noi dung: {item.content}") # In nội dung
        print(f"  Tags: {', '.join(item.tags)}")  # In tags nối bằng dấu phẩy
        print()                              # In dòng trống

    # Xuat ra JSON (demo)
    print("Xuat JSON:")                      # In tiêu đề
    from dataclasses import asdict           # Import asdict để chuyển dataclass -> dict
    print(json.dumps([asdict(item) for item in sample_items[:1]], ensure_ascii=False, indent=2))  # In JSON 1 item đầu


if __name__ == "__main__":                   # Chỉ chạy khi file được thực thi trực tiếp
    demo_without_network()                   # Gọi hàm demo offline
