import pytest
from playwright.sync_api import sync_playwright, Page
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage


@pytest.fixture(scope='session')
def browser_context():
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    yield context
    context.close()
    browser.close()
    playwright.stop()


@pytest.fixture
def page(browser_context):
    page = browser_context.new_page()
    yield page
    page.close()


def test_saucedemo_add_to_cart(page: Page):
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)
    cart_page = CartPage(page)

    login_page.goto()
    login_page.login('standard_user', 'secret_sauce')

    assert inventory_page.is_loaded(), 'Inventory page did not load after login.'

    inventory_page.add_product_to_cart('Sauce Labs Backpack')
    inventory_page.open_cart()

    assert cart_page.is_loaded(), 'Cart page did not open.'
    assert cart_page.product_count() == 1, 'Expected 1 item in the cart.'
