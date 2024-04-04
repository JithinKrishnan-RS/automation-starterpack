# utils/helper_functions.py
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def wait_for_element_visible(browser, locator, timeout=10):
    return WebDriverWait(browser, timeout).until(EC.visibility_of_element_located(locator))
