from playwright.sync_api import Page


class LoginPage:
    def __init__(self, page: Page):
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

        from pages.inventory_page import InventoryPage
        return InventoryPage(self.page)
