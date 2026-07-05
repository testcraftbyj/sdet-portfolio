import pytest
from playwright.sync_api import Page

#Added to override the get_by_test_id() issue when the attribute name is not hardcoded into data-testid
@pytest.fixture(autouse=True)
def set_test_id(playwright):
    playwright.selectors.set_test_id_attribute("data-test")
    yield