# pages/base_page.py
from configs.config import Config
from locators.base_page_locators import BasePageLocators
from utils.helper_functions import HelperFunctions


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.helper = HelperFunctions(self.driver)

    # Method to open the base URL
    def open(self):
        self.driver.get(Config.base_url)  # Navigate to the base URL

    # Method to get the title of the current page
    def get_title(self):
        return self.driver.title  # Return the title of the current page

    # Method to find an element using its locator
    def find_element(self, locator):
        # Wait for the element to be visible and return it
        return self.helper.wait_for_element_visible(self.driver, locator)

    # Method to input text into a field identified by its locator
    def input_text(self, locator):
        element = self.find_element(locator)  # Find the element
        element.clear()  # Clear the field
        element.send_keys(Config.search_text)  # Input the text
