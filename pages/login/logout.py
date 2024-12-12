from configs.config import LoginConfig
from utils.helper_functions import HelperFunctions


class Logout:
    def __init__(self, driver):
        self.driver = driver
        self.helper = HelperFunctions(self.driver)  # Create an instance of the Helper class

    # Function to open the base URL
    def open(self):
        self.driver.get(LoginConfig.base_url + "")

    # Function to get the title of the current page
    def get_title(self):
        return self.driver.title

    def click_profile_icon(self, locator):
        self.helper.wait_and_click(locator)

    def click_logout(self, locator):
        self.helper.wait_and_click(locator)

    def login_form_visible(self, locator):
        self.helper.wait_for_element_visible(locator)
