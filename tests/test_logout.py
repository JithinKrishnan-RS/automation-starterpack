import time

import pytest

from configs.config import LoginConfig
from locators.login_locators import LoginLocators
from pages.login.login import Login
from pages.login.logout import Logout


# Define a pytest fixture that returns a page instance
@pytest.fixture
def logout_page(setup_driver):
    return Logout(setup_driver)


@pytest.fixture
def login_page(setup_driver):
    return Login(setup_driver)


def test_admin_logout(logout_page, login_page):
    login_page.open()  # Open the login page
    time.sleep(2)  # Wait for 2 seconds
    assert "" in login_page.get_title()  # Assert that the page title is correct
    login_page.input_email(LoginLocators.email, LoginConfig.email)  # Input email
    login_page.input_password(LoginLocators.password)  # Input password
    login_page.click_login(LoginLocators.sign_in)  # Click the sign-in button
    login_page.login_form_disappear(LoginLocators.sign_in)  # Wait for the login form to disappear
    time.sleep(5)  # Wait for 5 seconds
    assert login_page.driver.current_url == LoginConfig.base_url + ""  # Assert that the current URL is correct

    time.sleep(2)  # Wait for 2 seconds
    logout_page.click_profile_icon(LoginLocators.profile_icon)  # Click the profile icon
    time.sleep(1)  # Wait for 1 second
    logout_page.click_logout(LoginLocators.logout)
    time.sleep(5)  # Wait for 5 seconds
    logout_page.login_form_visible(LoginLocators.sign_in)  # Wait for the login form to appear
    assert "" in logout_page.get_title()  # Assert that the page title is correct

    logout_page.driver.execute_script("window.open('');")
    logout_page.driver.switch_to.window(logout_page.driver.window_handles[1])
    login_page.open()  # Open the login page
    time.sleep(2)  # Wait for 2 seconds
    assert "" in login_page.get_title()  # Assert that the page title is correct


def test_url_after_admin_logout(logout_page, login_page):
    login_page.open()  # Open the login page
    time.sleep(2)  # Wait for 2 seconds
    assert "" in login_page.get_title()  # Assert that the page title is correct
    login_page.input_email(LoginLocators.email)  # Input email
    login_page.input_password(LoginLocators.password)  # Input password
    login_page.click_login(LoginLocators.sign_in)  # Click the sign-in button
    login_page.login_form_disappear(LoginLocators.sign_in)  # Wait for the login form to disappear
    time.sleep(5)  # Wait for 5 seconds
    assert login_page.driver.current_url == LoginConfig.base_url + ""  # Assert that the current URL is correct

    time.sleep(2)  # Wait for 2 seconds
    logout_page.click_profile_icon(LoginLocators.profile_icon)  # Click the profile icon
    time.sleep(1)  # Wait for 1 second
    logout_page.click_logout(LoginLocators.logout)
    time.sleep(5)  # Wait for 5 seconds
    logout_page.login_form_visible(LoginLocators.sign_in)  # Wait for the login form to appear
    assert "" in logout_page.get_title()  # Assert that the page title is correct

    logout_page.driver.execute_script("window.open('');")
    logout_page.driver.switch_to.window(logout_page.driver.window_handles[2])
    login_page.open_dashboard()  # Open the login page
    time.sleep(2)  # Wait for 2 seconds
    assert login_page.driver.current_url == LoginConfig.base_url + ""  # Assert that the current URL is correct

# Run the test cases by executing the command: pytest tests/test_logout.py
