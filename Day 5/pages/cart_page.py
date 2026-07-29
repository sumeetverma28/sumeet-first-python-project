from playwright.sync_api import Page


class CartPage:
    def __init__(self, page: Page):
        self.page = page
        self.cart_title = page.locator('.title')
        self.cart_items = page.locator('.cart_item')
        self.checkout_button = page.locator('#checkout')

    def is_loaded(self) -> bool:
        return self.cart_title.inner_text().strip() == 'Your Cart'

    def product_count(self) -> int:
        return self.cart_items.count()

    def checkout(self):
        self.checkout_button.click()
