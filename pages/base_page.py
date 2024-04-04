# pages/base_page.py
from configs.config import Config
from locators.base_page_locators import BasePageLocators
from utils.helper_functions import wait_for_element_visible


class BasePage:
    def __init__(self, browser):
        self.browser = browser

    def open(self):
        self.browser.get(BasePageLocators.BASE_URL)

    def get_title(self):
        return self.browser.title

    def find_element(self, locator):
        return wait_for_element_visible(self.browser, locator)

    def input_text(self, locator):
        element = self.find_element(locator)
        element.clear()
        element.send_keys(Config.SEARCH_TEXT)
