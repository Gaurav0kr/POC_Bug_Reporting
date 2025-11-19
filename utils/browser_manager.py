from playwright.sync_api import sync_playwright
from behave import fixture
from utils.config import Config


@fixture
def browser_context(context):
    """Fixture to manage browser context lifecycle"""
    playwright = sync_playwright().start()
    browser_type = getattr(playwright, Config.BROWSER)
    browser = browser_type.launch(
        headless=Config.HEADLESS,
        args=['--window-size={},{}'.format(Config.VIEWPORT_WIDTH, Config.VIEWPORT_HEIGHT)] if not Config.HEADLESS else []
    )
    browser_context = browser.new_context(
        viewport={'width': Config.VIEWPORT_WIDTH, 'height': Config.VIEWPORT_HEIGHT},
        ignore_https_errors=True,
        device_scale_factor=1.0  # Ensure consistent scaling
    )
    browser_context.set_default_timeout(Config.DEFAULT_TIMEOUT)
    browser_context.set_default_navigation_timeout(Config.NAVIGATION_TIMEOUT)
    
    context.browser = browser
    context.browser_context = browser_context
    context.page = browser_context.new_page()
    # Explicitly set viewport size to ensure it fits the screen
    context.page.set_viewport_size({'width': Config.VIEWPORT_WIDTH, 'height': Config.VIEWPORT_HEIGHT})
    
    yield context.page
    
    # Cleanup
    browser_context.close()
    browser.close()
    playwright.stop()

