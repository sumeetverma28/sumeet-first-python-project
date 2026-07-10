from playwright.sync_api import sync_playwright

# Page Object Model classes for Saucedemo

class LoginPage:
    def __init__(self, page):
        self.page = page
        self.username_input = page.locator('input[name="user-name"]')
        self.password_input = page.locator('input[name="password"]')
        self.login_button = page.locator('input[type="submit"]')

    def goto(self):
        self.page.goto('https://www.saucedemo.com/')

    def login(self, username: str, password: str):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()


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

    def open_cart(self):
        self.cart_button.click()


def test_login_and_inventory_flow():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        page = browser.new_page()

        login_page = LoginPage(page)
        inventory_page = InventoryPage(page)

        login_page.goto()
        login_page.login('standard_user', 'secret_sauce')

        assert inventory_page.is_loaded(), 'Inventory page did not load after login.'

        inventory_page.add_product_to_cart('Sauce Labs Backpack')
        inventory_page.open_cart()

        browser.close()


if __name__ == '__main__':
    test_login_and_inventory_flow()

