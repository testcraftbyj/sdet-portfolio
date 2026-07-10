from pages.bookstore_page import BookstorePage

def test_search_nonexistent_book_returns_zero_results(page):
    bookstore = BookstorePage(page)
    bookstore.navigate("https://demoqa.com/books")
    bookstore.search_book("ThisBookDoesNotExist12345")

    assert bookstore.get_visible_book_count() == 0

def test_search_sql_injection_style_input_returns_zero_results(page):
    bookstore = BookstorePage(page)
    bookstore.navigate("https://demoqa.com/books")
    bookstore.search_book("' OR 1=1 --")

    assert bookstore.get_visible_book_count() == 0