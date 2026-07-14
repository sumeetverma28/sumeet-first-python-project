import json
from pathlib import Path
from playwright.sync_api import sync_playwright


with open(Path(__file__).with_name('test_data.json'), encoding='utf-8') as f:
    TEST_DATA = json.load(f)


class LoginPage:
    def __init__(self, page):
        self.page = page
        self.username_input = page.locator('input[name="user-name"]')
        self.password_input = page.locator('input[name="password"]')
        self.login_button = page.locator('input[type="submit"]')

    def goto(self):
        self.page.goto('https://www.saucedemo.com/')
        return self

    def login(self, username: str, password: str):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()
        return InventoryPage(self.page)

    def login_and_verify(self, username: str, password: str):
        self.goto()
        inventory_page = self.login(username, password)
        assert inventory_page.is_loaded(), 'Inventory page did not load after login.'
        return inventory_page


class InventoryPage:
    def __init__(self, page):
        self.page = page
        self.page_title = page.locator('.title')
        self.inventory_container = page.locator('#inventory_container')
        self.cart_button = page.locator('.shopping_cart_link')

    def is_loaded(self) -> bool:
        return self.inventory_container.is_visible() and self.page_title.inner_text().strip() == 'Products'

    def add_product_to_cart(self, product_name: str):
        self.page.locator(f'text="{product_name}"').locator('xpath=../..').locator('button').click()
        return self

    def open_cart(self):
        self.cart_button.click()
        return CartPage(self.page)

    def add_product_and_open_cart(self, product_name: str):
        self.add_product_to_cart(product_name)
        return self.open_cart()


class CartPage:
    def __init__(self, page):
        self.page = page
        self.cart_title = page.locator('.title')
        self.cart_items = page.locator('.cart_item')

    def is_loaded(self) -> bool:
        return self.cart_title.inner_text().strip() == 'Your Cart'

    def product_count(self) -> int:
        return self.cart_items.count()


def test_login_and_inventory_flow():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        page = browser.new_page()

        login_page = LoginPage(page)
        login_data = TEST_DATA['login']
        product_name = TEST_DATA['product']

        inventory_page = login_page.login_and_verify(login_data['username'], login_data['password'])
        cart_page = inventory_page.add_product_and_open_cart(product_name)

        assert cart_page.is_loaded(), 'Cart page did not open.'
        assert cart_page.product_count() == 1, 'Expected 1 item in the cart.'

        browser.close()


if __name__ == '__main__':
    test_login_and_inventory_flow()

