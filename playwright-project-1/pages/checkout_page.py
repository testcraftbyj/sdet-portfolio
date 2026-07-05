from playwright.sync_api import Page

class CheckoutPage:

    def __init__(self, page:Page):
        self.page = page
        self.first_name = page.get_by_test_id("firstName")
        self.last_name = page.get_by_test_id("lastName")
        self.postal_code = page.get_by_test_id("postalCode")
        self.continue_button = page.get_by_test_id("continue")
        self.finish_button = page.get_by_test_id("finish")
        self.confirmation_message = page.get_by_test_id("complete-header")

    def fill_checkout_info(self, first_name, last_name, postal_code):
        self.first_name.fill(first_name)
        self.last_name.fill(last_name)
        self.postal_code.fill(postal_code)
        self.continue_button.click()

    def finish_order(self):
        self.finish_button.click()

    def check_confirmation(self):
        return self.confirmation_message.text_content()