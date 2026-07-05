import re

from playwright.sync_api import Page

class InventoryPage:

    def __init__(self, page:Page):
        self.page = page
        self.add_to_cart_button = page.get_by_test_id("add-to-cart-sauce-labs-backpack")
        self.cart_badge = page.get_by_test_id("shopping-cart-badge")
        self.cart_link = page.get_by_test_id("shopping-cart-link")

    def inventory(self):
        self.add_to_cart_button.click()

    def get_cart_count(self):
        return self.cart_badge.text_content()
    
    def go_to_cart(self):
        self.cart_link.click()

