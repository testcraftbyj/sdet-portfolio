import re

from playwright.sync_api import Page, expect
from pages.login_page import LoginPage

def test_successful_login(page: Page) -> None:
    login_page = LoginPage(page)

    page.goto("https://www.saucedemo.com/")

    login_page.login("standard_user", "secret_sauce")

    expect(page).to_have_url(re.compile(".*inventory.html"))
    expect(page.locator(".title")).to_have_text("Products")

