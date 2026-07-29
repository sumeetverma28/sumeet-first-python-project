from playwright.sync_api import Page


class InventoryPage:
    def __init__(self, page: Page):
        self.page = page
        self.page_title = page.locator('.title')
        self.inventory_container = page.locator('[data-test="inventory-container"]')
        self.cart_button = page.locator('.shopping_cart_link')

    def is_loaded(self) -> bool:
        return self.inventory_container.is_visible() and self.page_title.inner_text().strip() == 'Products'

    def add_product_to_cart(self, product_name: str):
        product_card = self.page.locator(
            f'xpath=//div[contains(@class,"inventory_item") and .//div[text()="{product_name}"]]'
        )
        product_card.locator('button').click(timeout=10000)

    def open_cart(self):
        self.cart_button.click()
