# pages/other_page.py
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class OtherPage:
    def __init__(self, browser):
        self.browser = browser
        self.timeout = 10

    def open(self, url):
        self.browser.get(url)

    def get_title(self):
        return self.browser.title

    def find_element(self, locator):
        return WebDriverWait(self.browser, self.timeout).until(EC.presence_of_element_located(locator))
