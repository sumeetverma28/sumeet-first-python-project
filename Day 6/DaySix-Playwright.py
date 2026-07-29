import json
from pathlib import Path

try:
    import pytest  # type: ignore
except ImportError as e:
    raise ImportError(
        "pytest is not installed or cannot be imported. Install it with:\n"
        "    pip install pytest"
    ) from e

# Type hints
import sys
if sys.version_info >= (3, 8):
    pass

# Ensure playwright is installed and provide a clear error if not.
try:
    from playwright.sync_api import Page, sync_playwright  # type: ignore
except ImportError as e:
    raise ImportError(
        "playwright is not installed or cannot be imported. Install it with:\n"
        "    pip install playwright\n"
        "and then run:\n"
        "    playwright install\n"
    ) from e

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


with open(Path(__file__).with_name('test_data.json'), encoding='utf-8') as f:
    TEST_DATA = json.load(f)


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


@pytest.fixture
def logged_in_page(page: Page):
    login_page = LoginPage(page)
    inventory_page = login_page.goto().login(
        TEST_DATA['login']['username'],
        TEST_DATA['login']['password']
    )

    assert inventory_page.is_loaded(), 'Login failed or inventory page did not load.'
    yield page


def test_login_with_reusable_fixture(logged_in_page: Page):
    assert 'inventory.html' in logged_in_page.url
    assert logged_in_page.locator('[data-test="inventory-container"]').is_visible()


def test_add_product_with_reusable_login(logged_in_page: Page):
    inventory_page = InventoryPage(logged_in_page)
    inventory_page.add_product_to_cart('Sauce Labs Backpack')
    cart_url = inventory_page.open_cart()

    assert cart_url.endswith('/cart.html')



