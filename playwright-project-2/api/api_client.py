import requests

class DemoQABookstoreAPI:
    def __init__(self, base_url: str):
        self.base_url = base_url

    def get_all_books(self):
        response = requests.get(f"{self.base_url}/Bookstore/v1/Books")
        return response
    