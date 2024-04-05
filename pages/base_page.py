# pages/base_page.py
from configs.config import Config
from locators.base_page_locators import BasePageLocators
from utils.helper_functions import HelperFunctions


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.helper = HelperFunctions(self.driver)

    def open(self):
        self.driver.get(Config.base_url)

    def get_title(self):
        return self.driver.title

    def find_element(self, locator):
        return self.helper.wait_for_element_visible(self.driver, locator)

    def input_text(self, locator):
        element = self.find_element(locator)
        element.clear()
        element.send_keys(Config.search_text)
