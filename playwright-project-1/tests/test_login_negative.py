from playwright.sync_api import Page, expect
from pages.login_page import LoginPage


def test_locked_out_user_shows_error(page: Page):
    page.goto("https://www.saucedemo.com")
    login_page = LoginPage(page)

    login_page.login("locked_out_user", "secret_sauce")

    expect(login_page.error_message).to_be_visible()
    expect(login_page.error_message).to_contain_text("Sorry, this user has been locked out.")
    expect(page).to_have_url("https://www.saucedemo.com/")
