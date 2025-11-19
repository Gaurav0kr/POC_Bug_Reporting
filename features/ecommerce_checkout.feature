Feature: E-commerce Checkout Flow
  As a user
  I want to complete a purchase flow
  So that I can buy products from the e-commerce site

  @smoke @regression
  Scenario Outline: Complete checkout flow with different user credentials and products
    Given I navigate to the login page
    When I login with credentials "<UserName>" and "<Password>"
    Then I should be successfully logged in
    When I select product "<Product>" and add it to cart
    And I navigate to cart page
    And I click on checkout button
    And I enter "<CountryCode>" in country textbox
    And I select "<Country>" from dropdown
    When I click on Place Order button
    Then order confirmation page should be displayed
    And I capture the order ID from thank you page
    When I click on Orders link present on top right
    Then the order ID should be present in "Your Orders" table

    Examples:
      | UserName                        | Password            | Product      | CountryCode | Country |
      | Gauravtestuser1@gmail.com       | Gauravtestuser123   | Gaurav_Bike  | ind         | India   |

