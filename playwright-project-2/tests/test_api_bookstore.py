from api.api_client import DemoQABookstoreAPI

def test_get_all_books_returns_200(api_base_url):
    api = DemoQABookstoreAPI(api_base_url)
    response = api.get_all_books()

    assert response.status_code == 200
    data = response.json()
    assert "books" in data
    assert len(data["books"]) > 0