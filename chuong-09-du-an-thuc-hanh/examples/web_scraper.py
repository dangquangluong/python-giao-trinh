"""
Chuong 9: Du an Web Scraper (Vi du minh hoa)

Luu y: De chay duoc can cai dat:
    pip install requests beautifulsoup4

Vi du nay minh hoa cau truc cua mot web scraper.
"""

from dataclasses import dataclass, field
from typing import List, Optional
import json
from datetime import datetime


@dataclass
class ScrapedItem:
    """Mot item da thu thap."""
    title: str
    content: str
    url: str
    tags: List[str] = field(default_factory=list)
    scraped_at: str = field(default_factory=lambda: datetime.now().isoformat())


class WebScraper:
    """
    Web scraper co ban.

    Vi du su dung:
        scraper = WebScraper(base_url="http://example.com")
        items = scraper.scrape(max_pages=3)
        scraper.export_json(items, "output.json")
    """

    def __init__(self, base_url: str, delay: float = 1.0):
        self.base_url = base_url
        self.delay = delay
        self.session = None

    def _init_session(self):
        """Khoi tao HTTP session."""
        try:
            import requests
            self.session = requests.Session()
            self.session.headers.update({
                "User-Agent": "Mozilla/5.0 (Educational Python Scraper)"
            })
        except ImportError:
            print("Can cai dat: pip install requests")
            return False
        return True

    def fetch_page(self, url: str) -> Optional[str]:
        """Tai noi dung trang web."""
        if not self.session:
            if not self._init_session():
                return None

        try:
            import time
            response = self.session.get(url, timeout=10)
            response.raise_for_status()
            time.sleep(self.delay)  # Rate limiting
            return response.text
        except Exception as e:
            print(f"Loi khi tai {url}: {e}")
            return None

    def parse_page(self, html: str) -> List[ScrapedItem]:
        """Parse HTML va trich xuat du lieu."""
        try:
            from bs4 import BeautifulSoup
        except ImportError:
            print("Can cai dat: pip install beautifulsoup4")
            return []

        soup = BeautifulSoup(html, "html.parser")
        items = []

        # Vi du: parse quotes tu quotes.toscrape.com
        for quote_div in soup.select(".quote"):
            text = quote_div.select_one(".text")
            author = quote_div.select_one(".author")
            tags = quote_div.select(".tag")

            if text and author:
                item = ScrapedItem(
                    title=author.get_text(),
                    content=text.get_text(),
                    url=self.base_url,
                    tags=[t.get_text() for t in tags]
                )
                items.append(item)

        return items

    def scrape(self, max_pages: int = 5) -> List[ScrapedItem]:
        """Thu thap du lieu tu nhieu trang."""
        all_items = []

        for page in range(1, max_pages + 1):
            url = f"{self.base_url}/page/{page}/"
            print(f"Dang xu ly trang {page}: {url}")

            html = self.fetch_page(url)
            if not html:
                break

            items = self.parse_page(html)
            if not items:
                print("Khong con du lieu. Dung lai.")
                break

            all_items.extend(items)
            print(f"  -> Thu thap duoc {len(items)} items")

        print(f"\nTong cong: {len(all_items)} items")
        return all_items

    @staticmethod
    def export_json(items: List[ScrapedItem], filename: str):
        """Xuat du lieu ra file JSON."""
        from dataclasses import asdict
        data = [asdict(item) for item in items]
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"Da luu {len(items)} items vao {filename}")

    @staticmethod
    def export_csv(items: List[ScrapedItem], filename: str):
        """Xuat du lieu ra file CSV."""
        import csv
        with open(filename, "w", encoding="utf-8", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["title", "content", "tags", "url", "scraped_at"])
            for item in items:
                writer.writerow([
                    item.title,
                    item.content,
                    ", ".join(item.tags),
                    item.url,
                    item.scraped_at
                ])
        print(f"Da luu {len(items)} items vao {filename}")


# === Demo (khong can ket noi mang) ===
def demo_without_network():
    """Demo cau truc scraper khong can mang."""
    print("=== Demo Web Scraper (offline) ===\n")

    # Gia lap du lieu da scrape
    sample_items = [
        ScrapedItem(
            title="Albert Einstein",
            content="Tri tuong tuong quan trong hon kien thuc.",
            url="http://example.com",
            tags=["khoa-hoc", "tri-tue"]
        ),
        ScrapedItem(
            title="Steve Jobs",
            content="Hay luon khat khao, hay luon dai kho.",
            url="http://example.com",
            tags=["cong-nghe", "truyen-cam-hung"]
        ),
        ScrapedItem(
            title="Lao Tu",
            content="Hanh trinh ngan dam bat dau tu mot buoc chan.",
            url="http://example.com",
            tags=["triet-hoc", "cuoc-song"]
        ),
    ]

    print("Du lieu thu thap duoc:")
    print("-" * 60)
    for item in sample_items:
        print(f"  Tac gia: {item.title}")
        print(f"  Noi dung: {item.content}")
        print(f"  Tags: {', '.join(item.tags)}")
        print()

    # Xuat ra JSON (demo)
    print("Xuat JSON:")
    from dataclasses import asdict
    print(json.dumps([asdict(item) for item in sample_items[:1]], ensure_ascii=False, indent=2))


if __name__ == "__main__":
    demo_without_network()
