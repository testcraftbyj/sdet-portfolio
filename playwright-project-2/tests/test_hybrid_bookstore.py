from api.api_client import DemoQABookstoreAPI
from pages.bookstore_page import BookstorePage

def test_api_book_appears_in_ui(page, api_base_url):
    #Step 1: Get book data from the API
    api = DemoQABookstoreAPI(api_base_url)
    response = api.get_all_books()
    books = response.json()["books"]
    first_book_title = books[0]["title"]

    #Step 2: Verify that same book appears in the UI
    bookstore = BookstorePage(page)
    bookstore.navigate("https://demoqa.com/books")
    bookstore.search_book(first_book_title)

    assert bookstore.get_visible_book_count() >= 1