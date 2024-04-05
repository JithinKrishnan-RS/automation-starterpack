import time

import pytest

from locators.login_locator import LoginLocators
from configs.config import Config
from pages.login.login import Login


@pytest.fixture
def login_page(setup_driver):
    return Login(setup_driver)


def test_store_manager_login(login_page):
    login_page.open()
    assert "Test Title" in login_page.get_title()
    login_page.input_email(LoginLocators.email)
    login_page.input_password(LoginLocators.email)
    login_page.click_sign_in(LoginLocators.sign_in)
    login_page.input_otp(LoginLocators.otp)
    login_page.click_verify(LoginLocators.verify)
    time.sleep(5)
    assert login_page.driver.current_url == Config.base_url + "mystore"


def test_invalid_email(login_page):
    login_page.open()
    assert "Test Title" in login_page.get_title()
    login_page.input_invalid_email(LoginLocators.email)
    login_page.input_password(LoginLocators.email)
    login_page.click_sign_in(LoginLocators.sign_in)
    error_message = login_page.get_error_message(LoginLocators.error_message)
    time.sleep(5)
    assert error_message == "Error Message"
