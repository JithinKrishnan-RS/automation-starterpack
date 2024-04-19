# Automation Starter Pack

> This starter pack provides a basic setup for writing Selenium tests using Python, Selenium, and Pytest framework.

## Contents

- [Tools & Frameworks](#tools--frameworks)
- [Directory Structure](#directory-structure)
- [Getting Started](#getting-started)
- [Environment Variables](#environment-variables)
- [Miscellaneous](#miscellaneous)
- [Download Links](#download-links)
- [Important Documentations](#important-documentations)

---

## Tools & Frameworks

### Selenium

Selenium is a popular open-source automation testing framework primarily used for web applications. It provides a set of
tools and libraries to automate web browser actions, such as clicking buttons, entering text, navigating through pages,
and verifying expected behaviors.

### Python

Python is a popular programming language for Selenium automation for several reasons:

- Simplicity and readability
- Large ecosystem
- Cross-platform compatibility
- Integration with Selenium
- Third-party packages

### Pytest

Pytest is a testing framework for Python that simplifies the process of writing and executing tests. It offers
simplicity, a fixture model, powerful assertions, console output, HTML report generation, and failure hooks.

---

## Directory Structure

The project follows a modular structure to separate concerns and improve maintainability. Here's an example of the
directory structure:

```plaintext

project_root/
│
├── tests/
│ ├── init.py
│ ├── test_module1.py
│ └── test_module2.py
│
├── pages/
│ ├── init.py
│ ├── base_page.py
│ └── other_page.py
│
├── locators/
│ ├── init.py
│ ├── base_page_locators.py
│ └── other_page_locators.py
│
├── configs/
│ ├── init.py
│ └── config.py
│
├── utils/
│ ├── init.py
│ ├── helper_functions.py
│ └── config.py
│
├── drivers/
│ └── chromedriver.exe (or other WebDriver executables)
│
├── reports/
│
├── screenshots/
│
├── requirements.txt
├── conftest.py
└── pytest.ini
```

**Folder Structure Explanation**

- **tests/**: Contains test files with test cases.
- **pages/**: Contains page objects representing web pages.
- **locators/**: Contains files defining locators for web elements.
- **configs/**: Contains configuration files.
- **utils/**: Contains utility functions and configuration files.
- **drivers/**: Contains WebDriver executables for browsers.
- **reports/**: Contains test reports, generated automatically on each execution.
- **screenshots/**: Contains screenshots generated upon test failure.
- **requirements.txt**: Lists Python dependencies.
- **conftest.py**: Fixture setup and teardown.
- **pytest.ini**: Configuration options for Pytest.

---

## Getting Started

1. Install Python, if not already installed.
    - Go to the official [Python Website](https://www.python.org/downloads/) and download the latest version suitable
      for your operating system.
    - Make sure to check the option ‘**Add Python to PATH**’ during installation.

2. Choose an IDE.
    - Go to the official websites of [PyCharm](https://www.jetbrains.com/pycharm/download/)
      or [Visual Studio Code](https://code.visualstudio.com/download) and download the version compatible with your
      operating system
    - Clone the repository
    - Open the [Bitbucket Repository](https://bitbucket.org/2basetech/starterpack-qa-automation/src/master/)
    - Click on the "Clone" option located in the top right corner.
    - Copy the command provided.

3. Clone the Repository using Terminal or IDE Command Line.
    - Open your terminal (Command Prompt on Windows or Terminal on Mac/Linux) or the command line interface within your
      IDE.
    - Use the command you copied earlier to clone the repository.
    - This command will download a copy of the repository to your local machine.

4. Open the Cloned Repository.
    - Navigate to the directory where the repository was cloned using the cd command followed by the directory path.
    - Alternatively, open your IDE and use the "Open Folder" option to navigate to the cloned repository directory.

5. Checkout to branch ***release/version-1.0***.
    - Use the command `git checkout origin release/version-1.0` to switch to the specified branch.

6. Install Dependencies.
    - Use the command `pip install -r requirements.txt` to install all dependencies listed in the `requirements.txt`
      file.
    - For mac devices, use the `pip3` command, instead of `pip`.

        - Workaround 01: If the above command is not working, try installing dependencies separately.
            - `pip install pytest`
            - `pip install selenium`
            - `pip install python-dotenv`
            - `pip install barnum`
            - `pip install pytest-html`
            - `pip install pytest-failed-screenshot`

7. Create and activate a virtual environment (optional but recommended).
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Linux/Mac
   venv\Scripts\activate      # On Windows
    ```
8. Download WebDriver Executables.
    - Download [ChromeDriver](https://chromedriver.chromium.org/downloads), [GeckoDriver]((https://github.com/mozilla/geckodriver/releases)),
    or [EdgeDriver]((https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/?form=MA13LH)) depending on
    the browsers you intend to test.
    - Place these executables in the drivers/ directory of your project.

9. Install Pending Dependencies from configs/config.py.
    - Check the config.py file imports for any additional dependencies that need to be installed

10. Execute Tests.
    - Run your tests using the command `pytest tests/test_filename.py`.
    - Replace test_filename.py with the name of the test file you want to execute.
        - Eg.: `pytest test_login.py`

By following these steps, you should be able to set up your development environment, clone the repository, install
dependencies, and run tests with ease.

---

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

---

## Environment Variables

This project uses environment variables for configuration. These are stored in a `.env` file. Here's a sample of what
the `.env` file should look like:

```ini
EMAIL = "your-email@example.com"
PASSWORD = "your-password"
```

## Miscellaneous

### Why Executing Scripts using Pytest Command?

Executing tests using the command line with the pytest command offers several advantages:

- **Simplicity**: Running tests from the command line with pytest is straightforward and requires minimal setup.
- **Customization**: The pytest command provides various options and flags that allow us to customize test execution
  behavior.
- **Parallel Execution**: pytest supports parallel test execution, allowing us to run tests concurrently across multiple
  processes or threads.
- **Output Formats**: pytest can generate test reports in different formats, such as plain text, JUnit XML, HTML, etc.
- **Plugin Integration**: pytest has a rich ecosystem of plugins that extend its functionality and integrate with other
  tools.

### Download Links

- [Python](https://www.python.org/downloads/)
- [PyCharm](https://www.jetbrains.com/pycharm/download/) / [Visual Studio Code](https://code.visualstudio.com/download)
- [WebDriver executables](https://www.selenium.dev/documentation/en/webdriver/driver_requirements/)
- [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/downloads) / [GeckoDriver](https://github.com/mozilla/geckodriver/releases) / [EdgeDriver](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/?form=MA13LH)

### Important Documentations

- [Selenium Python Documentation](https://selenium-python.readthedocs.io/)
- [Pytest Documentation](https://docs.pytest.org/en/stable/)
- [Python Virtual Environments](https://docs.python.org/3/library/venv.html)
- [WebDriver executables](https://www.selenium.dev/documentation/en/webdriver/driver_requirements/)
- [Environment Variables in Python](https://docs.python.org/3/library/os.html#os.environ)
- [Python dotenv](https://pypi.org/project/python-dotenv/)