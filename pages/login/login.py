# pages/login/login.py
import os

from dotenv import load_dotenv

from configs.config import Config
from utils.helper_functions import HelperFunctions


# Function to load environment variables and get credentials
def get_credentials():
    load_dotenv()  # Load environment variables from .env file
    credentials = {
        'email': os.getenv('EMAIL'),
        'password': os.getenv('PASSWORD'),
        'otp': os.getenv('OTP'),
        'invalid_email': os.getenv('INVALID_EMAIL'),
        'invalid_password': os.getenv('INVALID_PASSWORD')
    }
    return credentials


class Login:
    def __init__(self, driver):
        self.driver = driver
        self.helper = HelperFunctions(self.driver)  # Create an instance of the Helper class
        self.credentials = get_credentials()  # Fetch credentials once during initialization
        load_dotenv()  # Load environment variables from .env file

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
        email = self.credentials['email']
        self.helper.wait_and_input_text(locator, email)  # Input email

    # Function to input invalid email into the email field
    def input_invalid_email(self, locator):
        invalid_email = os.getenv('INVALID_EMAIL')
        self.helper.wait_and_input_text(locator, invalid_email)  # Input invalid email

    # Function to input password into the password field
    def input_password(self, locator):
        password = self.credentials['password']
        self.helper.wait_and_input_text(locator, password)  # Input password

    # Function to input invalid password into the password field
    def input_invalid_password(self, locator):
        element = self.find_element(locator)
        element.clear()
        invalid_password = self.credentials['invalid_password']
        element.send_keys(invalid_password)  # Input invalid password

    # Function to click the sign-in button
    def click_sign_in(self, locator):
        element = self.find_element(locator)
        element.click()  # Click sign in button

    # Function to input OTP into the OTP field
    def input_otp(self, locator):
        element = self.find_element(locator)
        element.clear()
        otp = self.credentials['otp']
        element.send_keys(otp)  # Input OTP

    # Function to click the verify button
    def click_verify(self, locator):
        element = self.find_element(locator)
        element.click()  # Click verify button

    # Function to get the error message text
    def get_error_message(self, locator):
        element = self.find_element(locator)
        return element.text  # Return error message text
