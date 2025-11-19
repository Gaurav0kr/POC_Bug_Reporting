from playwright.sync_api import Page


class ProductsPage:
    """Page Object Model for Products Page"""
    
    def __init__(self, page: Page):
        self.page = page
        self.product_card = page.locator("div.card-body")
        self.add_to_cart_button = page.locator("button.btn.w-10.rounded")
        self.cart_icon = page.locator("button[routerlink*='cart']")
    
    def select_product_by_name(self, product_name: str):
        """Select a product by its name"""
        # Find the product card containing the product name
        product_locator = self.product_card.filter(has_text=product_name).first
        product_locator.wait_for(state='visible')
        return product_locator
    
    def add_product_to_cart(self, product_name: str):
        """Add a specific product to cart"""
        product_card = self.select_product_by_name(product_name)
        # Find the Add to Cart button within the product card
        add_button = product_card.locator("button").filter(has_text="Add to Cart")
        add_button.click()
        # Wait for the button text to change to "Added to Cart" or similar
        self.page.wait_for_timeout(1000)
    
    def navigate_to_cart(self):
        """Click on the cart icon to navigate to cart page"""
        self.cart_icon.click()
        self.page.wait_for_load_state('networkidle')

