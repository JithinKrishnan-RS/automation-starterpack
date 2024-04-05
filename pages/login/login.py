# pages/login/login.py
import os

from dotenv import load_dotenv

from configs.config import Config
from utils.helper_functions import HelperFunctions


def get_credentials():
    load_dotenv()
    email = os.getenv('email')
    password = os.getenv('password')
    otp = os.getenv('otp')
    invalid_email = os.getenv('invalid_email')
    invalid_password = os.getenv('invalid_password')
    return email, password, otp, invalid_email, invalid_password


class Login:
    def __init__(self, driver):
        self.driver = driver
        self.helper = HelperFunctions(self.driver)  # Create an instance of the Helper class

    def open(self):
        self.driver.get(Config.base_url)

    def get_title(self):
        return self.driver.title

    def find_element(self, locator):
        return self.helper.wait_for_element_visible(self.driver, locator)

    def input_email(self, locator):
        element = self.find_element(locator)
        element.clear()
        email, _, _, _, _ = get_credentials()
        element.send_keys(email)

    def input_invalid_email(self, locator):
        element = self.find_element(locator)
        element.clear()
        _, _, _, invalid_email, _ = get_credentials()
        element.send_keys(invalid_email)

    def input_password(self, locator):
        element = self.find_element(locator)
        element.clear()
        _, password, _, _, _ = get_credentials()
        element.send_keys(password)

    def input_invalid_password(self, locator):
        element = self.find_element(locator)
        element.clear()
        _, _, _, _, invalid_password = get_credentials()
        element.send_keys(invalid_password)

    def click_sign_in(self, locator):
        element = self.find_element(locator)
        element.click()

    def input_otp(self, locator):
        element = self.find_element(locator)
        element.clear()
        _, _, otp, _, _ = get_credentials()
        element.send_keys(otp)

    def click_verify(self, locator):
        element = self.find_element(locator)
        element.click()

    def get_error_message(self, locator):
        element = self.find_element(locator)
        return element.text
