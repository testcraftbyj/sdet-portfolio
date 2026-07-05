from playwright.sync_api import Page

class CartPage:

    def __init__(self, page:Page):
        self.page = page
        self.item_name = page.get_by_test_id("inventory-item-name")
        self.checkout_button = page.get_by_test_id("checkout")

    def get_item_name(self):
        return self.item_name.text_content()
    
    def checkout(self):
        self.checkout_button.click()