from playwright.sync_api import Page


class CartPage:
    """Page Object Model for Cart Page"""
    
    def __init__(self, page: Page):
        self.page = page
        self.checkout_button = page.locator("button:has-text('Checkout')")
        self.cart_items = page.locator("div.cartSection")
    
    def click_checkout(self):
        """Click on the Checkout button"""
        self.checkout_button.wait_for(state='visible')
        self.checkout_button.click()
        self.page.wait_for_load_state('networkidle')
    
    def is_cart_page_loaded(self) -> bool:
        """Verify that cart page is loaded"""
        try:
            self.checkout_button.wait_for(state='visible', timeout=10000)
            return True
        except:
            return False

