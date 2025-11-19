from playwright.sync_api import Page
from utils.config import Config


class LoginPage:
    """Page Object Model for Login Page"""
    
    def __init__(self, page: Page):
        self.page = page
        self.email_input = page.locator("input[type='email']")
        self.password_input = page.locator("input[type='password']")
        self.login_button = page.locator("input[value='Login']")
    
    def navigate_to_login(self):
        """Navigate to the login page"""
        self.page.goto(Config.BASE_URL)
        self.page.wait_for_load_state('networkidle')
    
    def login(self, email: str, password: str):
        """Perform login with provided credentials"""
        self.email_input.fill(email)
        self.password_input.fill(password)
        self.login_button.click()
        self.page.wait_for_load_state('networkidle')
    
    def is_logged_in(self) -> bool:
        """Check if login was successful by looking for cart icon or products"""
        try:
            # Wait for cart icon or products page to appear
            self.page.wait_for_selector("button[routerlink*='cart']", timeout=10000)
            return True
        except:
            return False

