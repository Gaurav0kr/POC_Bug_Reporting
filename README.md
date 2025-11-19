# E-commerce Automation Framework

This is a BDD (Behavior-Driven Development) automation framework using Behave, Playwright, and Python to automate e-commerce checkout flow testing.

## Project Structure

```
POC_Bug_Reporting/
├── features/              # Gherkin feature files
│   └── ecommerce_checkout.feature
├── steps/                 # Step definitions
│   └── checkout_steps.py
├── pages/                 # Page Object Model classes
│   ├── login_page.py
│   ├── products_page.py
│   ├── cart_page.py
│   └── checkout_page.py
├── utils/                 # Utility modules
│   ├── browser_manager.py
│   └── config.py
├── requirements.txt       # Python dependencies
├── behave.ini            # Behave configuration
├── environment.py        # Behave hooks for browser setup
├── env.example           # Environment variables template
├── .gitignore           # Git ignore file
└── README.md
```

## Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

## Setup Instructions

1. **Clone or navigate to the project directory**
   ```bash
   cd POC_Bug_Reporting
   ```

2. **Create a virtual environment (recommended)**
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On Linux/Mac
   source venv/bin/activate
   ```

3. **Install Python dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Install Playwright browsers**
   ```bash
   playwright install
   ```

5. **Configure environment variables**
   - Copy `env.example` to `.env` (or create `.env` manually)
   - Update the values in `.env` if needed (default values are already set in `env.example`)

## Test Flow

The automation covers the following test flow:

1. Navigate to login page: `https://rahulshettyacademy.com/client/#/auth/login`
2. Login with credentials: `Gauravtestuser1@gmail.com` / `Gauravtestuser123`
3. Select product "Gaurav_Bike" and add to cart
4. Navigate to cart page via cart icon
5. Click on Checkout button
6. Enter "ind" in country textbox
7. Select "India" from dropdown
8. Click Place Order
9. Verify order confirmation page is displayed

## Running Tests

### Run all tests
```bash
behave
```

### Run with specific tags
```bash
behave --tags @smoke
behave --tags @regression
```

### Run with different formatters
```bash
behave --format json
behave --format html
```

### Run in headless mode
Update `.env` file:
```
HEADLESS=true
```

## Configuration

### Environment Variables (.env)

- `BASE_URL`: Application base URL
- `EMAIL`: Login email
- `PASSWORD`: Login password
- `BROWSER`: Browser type (chromium, firefox, webkit)
- `HEADLESS`: Run browser in headless mode (true/false)

### Behave Configuration (behave.ini)

- `paths`: Location of feature files
- `step_definitions`: Location of step definition files
- `format`: Output format (pretty, json, html)
- `tags`: Default tags to run

## Framework Features

- **Page Object Model (POM)**: Maintainable and reusable page objects
- **BDD Approach**: Tests written in Gherkin syntax for better readability
- **Environment Configuration**: Centralized configuration management
- **Browser Management**: Automatic browser setup and teardown
- **Explicit Waits**: Proper wait strategies for element interactions
- **Error Handling**: Comprehensive error handling and assertions

## Troubleshooting

### Playwright browsers not installed
```bash
playwright install
```

### Import errors
Make sure you're in the project root directory and virtual environment is activated.

### Timeout errors
Increase timeout values in `utils/config.py` if needed.

## Notes

- The framework uses Playwright's sync API for simplicity
- Browser context is managed automatically via Behave fixtures
- All page objects follow the Page Object Model pattern
- Credentials are stored in `.env` file (not committed to version control)

