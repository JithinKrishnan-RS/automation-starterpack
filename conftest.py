from datetime import datetime

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


@pytest.fixture(scope="session")
def setup_driver():
    # Set up the driver
    service_obj = Service()
    driver = webdriver.Firefox(service=service_obj)
    driver.maximize_window()

    # Provide the driver object to the test functions
    yield driver

    # Tear down the driver
    driver.quit()


@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    config.option.htmlpath = config.option.htmlpath.replace(".html", f"_{now}.html")
