# pages/login/login.py
import os

from dotenv import load_dotenv

from configs.config import Config
from utils.helper_functions import HelperFunctions


# Function to load environment variables and get credentials
def get_credentials():
    load_dotenv()  # Load environment variables from .env file
    email = os.getenv('email')  # Get email from environment variable
    password = os.getenv('password')  # Get password from environment variable
    otp = os.getenv('otp')  # Get otp from environment variable
    invalid_email = os.getenv('invalid_email')  # Get invalid email from environment variable
    invalid_password = os.getenv('invalid_password')  # Get invalid password from environment variable
    return email, password, otp, invalid_email, invalid_password


class Login:
    def __init__(self, driver):
        self.driver = driver
        self.helper = HelperFunctions(self.driver)  # Create an instance of the Helper class

    # Function to open the base URL
    def open(self):
        self.driver.get(Config.base_url)

    # Function to get the title of the current page
    def get_title(self):
        return self.driver.title

    # Function to find an element using its locator
    def find_element(self, locator):
        return self.helper.wait_for_element_visible(self.driver, locator)

    # Function to input email into the email field
    def input_email(self, locator):
        element = self.find_element(locator)
        element.clear()
        email, _, _, _, _ = get_credentials()
        element.send_keys(email)  # Input email

    # Function to input invalid email into the email field
    def input_invalid_email(self, locator):
        element = self.find_element(locator)
        element.clear()
        _, _, _, invalid_email, _ = get_credentials()
        element.send_keys(invalid_email)  # Input invalid email

    # Function to input password into the password field
    def input_password(self, locator):
        element = self.find_element(locator)
        element.clear()
        _, password, _, _, _ = get_credentials()
        element.send_keys(password)  # Input password

    # Function to input invalid password into the password field
    def input_invalid_password(self, locator):
        element = self.find_element(locator)
        element.clear()
        _, _, _, _, invalid_password = get_credentials()
        element.send_keys(invalid_password)  # Input invalid password

    # Function to click the sign-in button
    def click_sign_in(self, locator):
        element = self.find_element(locator)
        element.click()  # Click sign in button

    # Function to input OTP into the OTP field
    def input_otp(self, locator):
        element = self.find_element(locator)
        element.clear()
        _, _, otp, _, _ = get_credentials()
        element.send_keys(otp)  # Input OTP

    # Function to click the verify button
    def click_verify(self, locator):
        element = self.find_element(locator)
        element.click()  # Click verify button

    # Function to get the error message text
    def get_error_message(self, locator):
        element = self.find_element(locator)
        return element.text  # Return error message text
