# Automation Starter Pack

> This starter pack provides a basic setup for writing Selenium tests using Python, Selenium, and Pytest framework.

## Directory Structure

project_root/<br>
│<br>
├── tests/<br>
│ ├── init.py<br>
│ ├── test_module1.py<br>
│ └── test_module2.py<br>
│<br>
├── pages/<br>
│ ├── init.py<br>
│ ├── base_page.py<br>
│ └── other_page.py<br>
│<br>
├── locators/<br>
│ ├── init.py<br>
│ ├── base_page_locators.py<br>
│ └── other_page_locators.py<br>
│<br>
├── configs/<br>
│ ├── init.py<br>
│ └── config.py<br>
│<br>
├── utils/<br>
│ ├── init.py<br>
│ ├── SeleniumExtended.py<br>
│ └── config.py<br>
│<br>
├── drivers/<br>
│ └── chromedriver.exe (or other WebDriver executables)<br>
│<br>
├── reports/<br>
│<br>
├── screenshots/<br>
│<br>
├── requirements.txt<br>
├── conftest.py<br>
└── pytest.ini<br>

## Folder Structure Explanation

- **tests/**: Contains test files with test cases.
- **pages/**: Contains page objects representing web pages.
- **locators/**: Contains files defining locators for web elements.
- **configs/**: Contains configuration files.
- **utils/**: Contains utility functions and configuration files.
- **drivers/**: Contains WebDriver executables for browsers.
- **reports/**: Optional folder for test execution reports.
- **screenshots/**: Contains screenshots generated upon test failure.
- **requirements.txt**: Lists Python dependencies.
- **conftest.py**: Fixture setup and teardown.
- **pytest.ini**: Configuration options for Pytest.

## Getting Started

1. Clone this repository.
2. Install Python if not already installed.
3. Install dependencies using `pip install -r requirements.txt`.
4. Create and activate a virtual environment (optional but recommended).
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Linux/Mac
   venv\Scripts\activate      # On Windows
5. Download WebDriver executables and place them in the `drivers/` directory.
6. Write your test cases in the `tests/` directory.
7. Run tests using Pytest: `pytest`.

## Usage Examples

Here's an example of how to write a test case:

```python
# tests/test_example.py
import pytest

from locators import base_page_locators
from pages.base_page import BasePage


@pytest.fixture
def base_page(setup_driver):
   return BasePage(setup_driver)


def test_example(base_page):
   base_page.open()
   assert "Example Domain" in base_page.get_title()
   base_page.input_text(base_page_locators.BasePageLocators.search_input)
```

## Environment Variables

This project uses environment variables for configuration. These are stored in a `.env` file. Here's a sample of what the `.env` file should look like:

```ini
email = "your-email@example.com"
password = "your-password"
otp = "your-otp"

invalid_email = "invalid-email@example.com"
invalid_password = "invalid-password"
invalid_otp = "invalid-otp"
```