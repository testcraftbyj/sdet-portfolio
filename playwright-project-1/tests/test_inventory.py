from playwright.sync_api import Page, expect
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

def test_add_to_cart(page:Page) -> None:
    page.goto("https://www.saucedemo.com/")

    login_page = LoginPage(page)
    login_page.login("standard_user", "secret_sauce")

    inventory_page = InventoryPage(page)
    inventory_page.inventory()
    #assert inventory_page.get_cart_count() == 1
    #switched to expect as assert doesnt "auto-wait"
    expect(inventory_page.cart_badge).to_have_text("1")