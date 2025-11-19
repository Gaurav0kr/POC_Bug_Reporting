from playwright.sync_api import Page
import re


class CheckoutPage:
    """Page Object Model for Checkout/Payment Page"""
    
    def __init__(self, page: Page):
        self.page = page
        self.country_input = page.locator("input[placeholder*='Select Country']")
        self.country_dropdown = page.locator("section.ta-results")
        self.country_option = page.locator("button.ta-item")
        self.place_order_button = page.locator("a.btnn.action__submit")
        self.order_confirmation = page.locator("h1.hero-primary")
        self.order_id_element = page.locator("label.ng-star-inserted")  # Order ID appears in label element
        self.orders_link = page.locator("button[routerlink*='myorders']")  # Orders link in top right
    
    def enter_country(self, country_code: str):
        """Enter country code in the country input field using sequential press"""
        self.country_input.wait_for(state='visible')
        self.country_input.click()  # Click to focus
        # Type each character sequentially using press
        for char in country_code:
            self.country_input.press(char)
            self.page.wait_for_timeout(200)  # Small delay between each character
        self.page.wait_for_timeout(2000)  # Wait for dropdown to appear after typing
    
    def select_country_from_dropdown(self, country_name: str):
        """Select a country from the dropdown - ensures exact match to avoid selecting similar names"""
        # Wait for dropdown options to appear
        self.page.wait_for_selector("button.ta-item", state='visible', timeout=10000)
        
        # Get all dropdown options
        all_options = self.page.locator("button.ta-item")
        option_count = all_options.count()
        
        # Find the exact match for the country name
        for i in range(option_count):
            option_text = all_options.nth(i).inner_text()
            # Check for exact match (case-insensitive) and ensure it's not a substring match
            # For "India", we want to match exactly "India" and not "British Indian"
            if option_text.strip().lower() == country_name.lower():
                all_options.nth(i).click()
                self.page.wait_for_timeout(1000)
                return
        
        # If exact match not found, try the filter approach as fallback
        try:
            # Filter options and check each one for exact match
            country_option = self.page.locator("button.ta-item").filter(
                lambda locator: locator.inner_text().strip().lower() == country_name.lower()
            ).first
            country_option.wait_for(state='visible', timeout=5000)
            country_option.click()
            self.page.wait_for_timeout(1000)
            return
        except:
            pass
        
        # If all strategies fail, raise an error
        raise Exception(f"Could not select country '{country_name}' from dropdown. Tried multiple strategies.")
    
    def click_place_order(self):
        """Click on Place Order button"""
        self.place_order_button.wait_for(state='visible')
        self.place_order_button.click()
        self.page.wait_for_load_state('networkidle')
    
    def is_order_confirmed(self) -> bool:
        """Verify that order confirmation page is displayed"""
        try:
            # Wait for order confirmation message
            self.order_confirmation.wait_for(state='visible', timeout=15000)
            return True
        except:
            return False
    
    def get_order_confirmation_text(self) -> str:
        """Get the order confirmation message text"""
        return self.order_confirmation.inner_text()
    
    def capture_order_id(self) -> str:
        """Capture the complete order ID from the thank you page (format: | 691d7e005008f6a90929fbce |)"""
        try:
            # Wait for order confirmation page to be fully loaded
            self.page.wait_for_load_state('networkidle')
            
            # Try to find order ID in various elements
            # Pattern to match order ID: | followed by alphanumeric string starting with 691
            order_id_pattern = r'\|\s*(691[a-f0-9]+)\s*\|'
            
            # Strategy 1: Look in label elements (most common location)
            try:
                labels = self.page.locator("label.ng-star-inserted")
                label_count = labels.count()
                for i in range(label_count):
                    label_text = labels.nth(i).inner_text()
                    match = re.search(order_id_pattern, label_text)
                    if match:
                        return match.group(1)
            except:
                pass
            
            # Strategy 2: Look in all text content on the page
            try:
                # Use first() to handle multiple body elements
                page_text = self.page.locator("body").first.inner_text()
                match = re.search(order_id_pattern, page_text)
                if match:
                    return match.group(1)
            except:
                pass
            
            # Strategy 3: Look in specific container elements
            try:
                # Try finding in the thank you page container
                container = self.page.locator("app-thanksorder, .container, .thank-you")
                container_count = container.count()
                for i in range(container_count):
                    container_text = container.nth(i).inner_text()
                    match = re.search(order_id_pattern, container_text)
                    if match:
                        return match.group(1)
            except:
                pass
            
            # Strategy 4: Search in all visible text elements
            try:
                all_elements = self.page.locator("*").filter(has_text=re.compile(r'691[a-f0-9]+'))
                element_count = all_elements.count()
                for i in range(element_count):
                    element_text = all_elements.nth(i).inner_text()
                    match = re.search(order_id_pattern, element_text)
                    if match:
                        return match.group(1)
            except:
                pass
            
            raise Exception("Order ID not found on the page")
        except Exception as e:
            raise Exception(f"Failed to capture order ID: {str(e)}")
    
    def click_orders_link(self):
        """Click on Orders link present on top right of the page"""
        try:
            self.orders_link.wait_for(state='visible', timeout=10000)
            self.orders_link.click()
            self.page.wait_for_load_state('networkidle')
        except:
            # Try alternative locator if the first one doesn't work
            orders_alt = self.page.locator("button:has-text('ORDERS')")
            orders_alt.wait_for(state='visible', timeout=10000)
            orders_alt.click()
            self.page.wait_for_load_state('networkidle')

