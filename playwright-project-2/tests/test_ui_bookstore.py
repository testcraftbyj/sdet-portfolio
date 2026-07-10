from pages.bookstore_page import BookstorePage

def test_bookstore_loads(page):
    bookstore = BookstorePage(page)

    bookstore.navigate("https://demoqa.com/books")
    bookstore.search_box.wait_for()
    assert bookstore.get_title() == "demosite"

    