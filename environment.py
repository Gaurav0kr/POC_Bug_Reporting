from utils.browser_manager import browser_context
from behave import use_fixture
import time


def before_scenario(context, scenario):
    """Hook to set up browser before each scenario"""
    use_fixture(browser_context, context)


def after_step(context, step):
    """Hook to add delay after each step for smooth execution visibility"""
    # Add 2 second delay after each step so user can see the execution smoothly
    time.sleep(2)


def after_scenario(context, scenario):
    """Hook to clean up after each scenario"""
    # Additional cleanup if needed
    pass

