import time

import pytest

from configs.config import Config
from locators.login_locator import LoginLocators
from pages.login.login import Login


# Define a pytest fixture that returns a Login page instance
@pytest.fixture
def login_page(setup_driver):
    return Login(setup_driver)


# Test case for successful login of a store manager
def test_store_manager_login(login_page):
    login_page.open()  # Open the login page
    assert "Test Title" in login_page.get_title()  # Assert that the page title is correct
    login_page.input_email(LoginLocators.email)  # Input email
    login_page.input_password(LoginLocators.email)  # Input password
    login_page.click_sign_in(LoginLocators.sign_in)  # Click the sign in button
    login_page.input_otp(LoginLocators.otp)  # Input OTP
    login_page.click_verify(LoginLocators.verify)  # Click the verify button
    time.sleep(5)  # Wait for 5 seconds
    assert login_page.driver.current_url == Config.base_url + "mystore"  # Assert that the current URL is correct


# Test case for login with invalid email
def test_invalid_email(login_page):
    login_page.open()  # Open the login page
    assert "Test Title" in login_page.get_title()  # Assert that the page title is correct
    login_page.input_invalid_email(LoginLocators.email)  # Input invalid email
    login_page.input_password(LoginLocators.email)  # Input password
    login_page.click_sign_in(LoginLocators.sign_in)  # Click the sign in button
    error_message = login_page.get_error_message(LoginLocators.error_message)  # Get the error message
    time.sleep(5)  # Wait for 5 seconds
    assert error_message == "Error Message"  # Assert that the error message is correct
