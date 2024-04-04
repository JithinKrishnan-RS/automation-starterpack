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
