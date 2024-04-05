# pages/other_page.py
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class OtherPage:
    def __init__(self, browser):
        self.browser = browser
        self.timeout = 10

        # Method to open a URL
    def open(self, url):
        self.browser.get(url)  # Navigate to the URL

    # Method to get the title of the current page
    def get_title(self):
        return self.browser.title  # Return the title of the current page

    # Method to find an element using its locator
    def find_element(self, locator):
        # Wait for the element to be present and return it
        return WebDriverWait(self.browser, self.timeout).until(EC.presence_of_element_located(locator))
