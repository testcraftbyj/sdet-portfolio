from playwright.sync_api import Page
from pages.base_page import BasePage

class BookstorePage(BasePage):
    def __init__(self, page:Page):
        super().__init__(page)
        self.search_box = page.locator("#searchBox")
        self.book_rows = page.locator("tbody tr")

    def search_book(self, book_name: str):
        self.search_box.fill(book_name)

    def get_visible_book_count(self) -> int:
        self.page.wait_for_timeout(500)
        return self.book_rows.count()