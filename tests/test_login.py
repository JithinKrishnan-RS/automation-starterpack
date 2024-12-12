import time

import pytest

from configs.config import LoginConfig
from locators.login_locators import LoginLocators
from pages.login.login import Login
from pages.login.logout import Logout


# Define a pytest fixture that returns a page instance
@pytest.fixture
def login_page(setup_driver):
    return Login(setup_driver)


@pytest.fixture
def logout_page(setup_driver):
    return Logout(setup_driver)


def test_login(login_page, logout_page):
    login_page.open()  # Open the login page
    time.sleep(2)  # Wait for 2 seconds
    assert "" in login_page.get_title()  # Assert that the page title is correct
    login_page.input_email(LoginLocators.email, LoginConfig.email)  # Input email
    login_page.input_password(LoginLocators.password, LoginConfig.password)  # Input password
    login_page.click(LoginLocators.sign_in)  # Click the sign-in button
    login_page.login_form_disappear(LoginLocators.sign_in)  # Wait for the login form to disappear
    time.sleep(5)  # Wait for 5 seconds
    assert login_page.driver.current_url == LoginConfig.base_url + ""  # Assert that the current URL is correct

    time.sleep(2)  # Wait for 2 seconds
    logout_page.click_profile_icon(LoginLocators.profile_icon)  # Click the profile icon
    time.sleep(1)  # Wait for 1 second
    logout_page.click(LoginLocators.logout)
    time.sleep(5)  # Wait for 5 seconds
    logout_page.login_form_visible(LoginLocators.sign_in)  # Wait for the login form to appear
    assert "" in logout_page.get_title()  # Assert that the page title is correct


def test_invalid_email_login(login_page):
    login_page.open()  # Open the login page
    time.sleep(2)  # Wait for 2 seconds
    assert "" in login_page.get_title()  # Assert that the page title is correct
    login_page.input_invalid_email(LoginLocators.email, LoginConfig.invalid_email)  # Input email
    login_page.input_password(LoginLocators.password, LoginConfig.password)  # Input password
    login_page.click(LoginLocators.sign_in)  # Click the sign-in button
    error_message = login_page.get_error_message(LoginLocators.error_message)  # Get the error message
    time.sleep(5)  # Wait for 5 seconds
    assert login_page.driver.current_url == LoginConfig.base_url + ""  # Assert that the current URL is correct
    assert error_message == "Email ID or Password is not valid"  # Assert that the error message is correct


def test_invalid_password_login(login_page):
    login_page.open()  # Open the login page
    time.sleep(2)  # Wait for 2 seconds
    assert "" in login_page.get_title()  # Assert that the page title is correct
    login_page.input_email(LoginLocators.email, LoginConfig.email)  # Input email
    login_page.input_invalid_password(LoginLocators.password, LoginConfig.invalid_password)  # Input invalid password
    login_page.click(LoginLocators.sign_in)  # Click the sign-in button
    error_message = login_page.get_error_message(LoginLocators.error_message)  # Get the error message
    time.sleep(5)  # Wait for 5 seconds
    assert login_page.driver.current_url == LoginConfig.base_url + ""  # Assert that the current URL is correct
    assert error_message == "Email ID or Password is not valid"  # Assert that the error message is correct


def test_empty_email_login(login_page):
    login_page.open()  # Open the login page
    time.sleep(2)  # Wait for 2 seconds
    assert "" in login_page.get_title()  # Assert that the page title is correct
    login_page.input_password(LoginLocators.password, LoginConfig.password)  # Input password
    login_page.click(LoginLocators.sign_in)  # Click the sign-in button
    validation_message = login_page.get_validation_message(LoginLocators.validation_message)  # Get the error message
    time.sleep(5)  # Wait for 5 seconds
    assert login_page.driver.current_url == LoginConfig.base_url + ""  # Assert that the current URL is correct
    assert validation_message == "This field is required"  # Assert that the error message is correct


def test_empty_password_login(login_page):
    login_page.open()  # Open the login page
    time.sleep(2)  # Wait for 2 seconds
    assert "" in login_page.get_title()  # Assert that the page title is correct
    login_page.input_email(LoginLocators.email, LoginConfig.email)  # Input email
    login_page.click(LoginLocators.sign_in)  # Click the sign-in button
    validation_message = login_page.get_validation_message(LoginLocators.validation_message)  # Get the error message
    time.sleep(5)  # Wait for 5 seconds
    assert login_page.driver.current_url == LoginConfig.base_url + ""  # Assert that the current URL is correct
    assert validation_message == "This field is required"  # Assert that the error message is correct


def test_inactive_account_login(login_page):
    login_page.open()  # Open the login page
    time.sleep(2)  # Wait for 2 seconds
    assert "" in login_page.get_title()  # Assert that the page title is correct
    login_page.input_inactive_credentials(LoginLocators.email, LoginConfig.inactive_email, LoginLocators.password,
                                          LoginConfig.inactive_password)  # Input email
    login_page.click(LoginLocators.sign_in)  # Click the sign-in button
    error_message = login_page.get_error_message(LoginLocators.error_message)  # Get the error message
    time.sleep(5)  # Wait for 5 seconds
    assert login_page.driver.current_url == LoginConfig.base_url + ""  # Assert that the current URL is correct
    assert error_message == "Logged in user is inactive"  # Assert that the error message is correct


def test_remember_me_checkbox(login_page, logout_page):
    login_page.open()  # Open the login page
    time.sleep(2)  # Wait for 2 seconds
    assert "" in login_page.get_title()  # Assert that the page title is correct
    login_page.input_email(LoginLocators.email, LoginConfig.email)  # Input email
    login_page.input_password(LoginLocators.password, LoginConfig.password)  # Input password
    login_page.remember_me_checkbox(LoginLocators.remember_me)  # Click the remember me checkbox
    login_page.click(LoginLocators.sign_in)  # Click the sign-in button
    login_page.login_form_disappear(LoginLocators.sign_in)  # Wait for the login form to disappear
    time.sleep(5)  # Wait for 5 seconds
    assert login_page.driver.current_url == LoginConfig.base_url + ""  # Assert that the current URL is correct
    login_page.open()  # Open the login page
    time.sleep(2)  # Wait for 2 seconds
    assert "" in login_page.get_title()  # Assert that the page title is correct

    time.sleep(2)  # Wait for 2 seconds
    logout_page.click_profile_icon(LoginLocators.profile_icon)  # Click the profile icon
    time.sleep(1)  # Wait for 1 second
    logout_page.click(LoginLocators.logout)
    time.sleep(5)  # Wait for 5 seconds
    logout_page.login_form_visible(LoginLocators.sign_in)  # Wait for the login form to appear
    assert "" in logout_page.get_title()  # Assert that the page title is correct


def test_give_url_after_login(login_page, logout_page):
    login_page.open()  # Open the login page
    time.sleep(2)  # Wait for 2 seconds
    assert "" in login_page.get_title()  # Assert that the page title is correct
    login_page.input_email(LoginLocators.email, LoginConfig.email)  # Input email
    login_page.input_password(LoginLocators.password, LoginConfig.password)  # Input password
    login_page.click(LoginLocators.sign_in)  # Click the sign-in button
    login_page.login_form_disappear(LoginLocators.sign_in)  # Wait for the login form to disappear
    time.sleep(5)  # Wait for 5 seconds
    assert login_page.driver.current_url == LoginConfig.base_url + ""  # Assert that the current URL is correct

    login_page.driver.execute_script("window.open('');")
    login_page.driver.switch_to.window(logout_page.driver.window_handles[1])
    login_page.open_dashboard()  # Open the login page
    time.sleep(2)  # Wait for 2 seconds
    assert login_page.driver.current_url == LoginConfig.base_url + ""  # Assert that the current URL is correct

    time.sleep(2)  # Wait for 2 seconds
    logout_page.click_profile_icon(LoginLocators.profile_icon)  # Click the profile icon
    time.sleep(1)  # Wait for 1 second
    logout_page.click(LoginLocators.logout)
    time.sleep(5)  # Wait for 5 seconds
    logout_page.login_form_visible(LoginLocators.sign_in)  # Wait for the login form to appear
    assert "" in logout_page.get_title()  # Assert that the page title is correct


def test_give_login_url_after_login(login_page, logout_page):
    login_page.open()  # Open the login page
    time.sleep(2)  # Wait for 2 seconds
    assert "" in login_page.get_title()  # Assert that the page title is correct
    login_page.input_email(LoginLocators.email, LoginConfig.email)  # Input email
    login_page.input_password(LoginLocators.password, LoginConfig.password)  # Input password
    login_page.click(LoginLocators.sign_in)  # Click the sign-in button
    login_page.login_form_disappear(LoginLocators.sign_in)  # Wait for the login form to disappear
    time.sleep(5)  # Wait for 5 seconds
    assert login_page.driver.current_url == LoginConfig.base_url + ""  # Assert that the current URL is correct

    login_page.driver.execute_script("window.open('');")
    login_page.driver.switch_to.window(logout_page.driver.window_handles[2])
    login_page.open()  # Open the login page
    time.sleep(2)  # Wait for 2 seconds
    assert login_page.driver.current_url == LoginConfig.base_url + ""  # Assert that the current URL is correct

    time.sleep(2)  # Wait for 2 seconds
    logout_page.click_profile_icon(LoginLocators.profile_icon)  # Click the profile icon
    time.sleep(1)  # Wait for 1 second
    logout_page.click(LoginLocators.logout)
    time.sleep(5)  # Wait for 5 seconds
    logout_page.login_form_visible(LoginLocators.sign_in)  # Wait for the login form to appear
    assert "" in logout_page.get_title()  # Assert that the page title is correct

# Run the test cases by executing the command: pytest tests/test_login.py
