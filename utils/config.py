import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


class Config:
    """Configuration class to manage environment variables and settings"""
    
    BASE_URL = os.getenv('BASE_URL', 'https://rahulshettyacademy.com/client/#/auth/login')
    EMAIL = os.getenv('EMAIL', 'Gauravtestuser1@gmail.com')
    PASSWORD = os.getenv('PASSWORD', 'Gauravtestuser123')
    BROWSER = os.getenv('BROWSER', 'chromium')
    HEADLESS = os.getenv('HEADLESS', 'false').lower() == 'true'
    
    # Viewport settings - smaller size to fit most screens
    VIEWPORT_WIDTH = int(os.getenv('VIEWPORT_WIDTH', '1080'))  # Default: 1280px
    VIEWPORT_HEIGHT = int(os.getenv('VIEWPORT_HEIGHT', '620'))  # Default: 720px
    
    # Timeout settings
    DEFAULT_TIMEOUT = 30000  # 30 seconds in milliseconds
    NAVIGATION_TIMEOUT = 60000  # 60 seconds in milliseconds

