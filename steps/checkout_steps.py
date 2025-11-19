from behave import given, when, then
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.orders_history_page import OrdersHistoryPage
from utils.config import Config


@given('I navigate to the login page')
def step_navigate_to_login(context):
    """Navigate to the login page"""
    context.login_page = LoginPage(context.page)
    context.login_page.navigate_to_login()


@when('I login with credentials "{UserName}" and "{Password}"')
def step_login(context, UserName, Password):
    """Perform login with provided credentials from Examples"""
    context.login_page.login(UserName, Password)


@then('I should be successfully logged in')
def step_verify_login(context):
    """Verify that login was successful"""
    assert context.login_page.is_logged_in(), "Login was not successful"


@when('I select product "{Product}" and add it to cart')
def step_select_and_add_product(context, Product):
    """Select a product and add it to cart from Examples"""
    context.products_page = ProductsPage(context.page)
    context.products_page.add_product_to_cart(Product)


@when('I navigate to cart page')
def step_navigate_to_cart(context):
    """Navigate to cart page"""
    context.products_page.navigate_to_cart()
    context.cart_page = CartPage(context.page)
    assert context.cart_page.is_cart_page_loaded(), "Cart page did not load successfully"


@when('I click on checkout button')
def step_click_checkout(context):
    """Click on checkout button"""
    context.cart_page.click_checkout()
    context.checkout_page = CheckoutPage(context.page)


@when('I enter "{CountryCode}" in country textbox')
def step_enter_country(context, CountryCode):
    """Enter country code in the country input field from Examples"""
    context.checkout_page.enter_country(CountryCode)


@when('I select "{Country}" from dropdown')
def step_select_country(context, Country):
    """Select a country from the dropdown from Examples"""
    context.checkout_page.select_country_from_dropdown(Country)


@when('I click on Place Order button')
def step_place_order(context):
    """Click on Place Order button"""
    context.checkout_page.click_place_order()


@then('order confirmation page should be displayed')
def step_verify_order_confirmation(context):
    """Verify that order confirmation page is displayed"""
    assert context.checkout_page.is_order_confirmed(), "Order confirmation page was not displayed"
    confirmation_text = context.checkout_page.get_order_confirmation_text()
    print(f"Order Confirmation Message: {confirmation_text}")


@then('I capture the order ID from thank you page')
def step_capture_order_id(context):
    """Capture the complete order ID from the thank you page"""
    context.order_id = context.checkout_page.capture_order_id()
    print(f"Captured Order ID: {context.order_id}")
    assert context.order_id is not None and len(context.order_id) > 0, "Order ID was not captured successfully"
    assert context.order_id.startswith('691'), f"Order ID should start with '691', but got: {context.order_id}"


@when('I click on Orders link present on top right')
def step_click_orders_link(context):
    """Click on Orders link present on top right of the page"""
    context.checkout_page.click_orders_link()
    context.orders_history_page = OrdersHistoryPage(context.page)
    assert context.orders_history_page.is_orders_page_loaded(), "Orders History page did not load successfully"


@then('the order ID should be present in "Your Orders" table')
def step_verify_order_id_in_table(context):
    """Verify that the captured order ID is present in the Your Orders table"""
    assert hasattr(context, 'order_id'), "Order ID was not captured in previous step"
    order_found = context.orders_history_page.find_order_id_in_table(context.order_id)
    assert order_found, f"Order ID '{context.order_id}' was not found in the Your Orders table"
    print(f"Order ID '{context.order_id}' successfully verified in Orders History table")

