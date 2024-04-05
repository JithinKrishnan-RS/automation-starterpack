# utils/helper_functions.py
import time

from selenium.common.exceptions import TimeoutException, StaleElementReferenceException
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class HelperFunctions:
    def __init__(self, driver):
        self.driver = driver
        self.default_timeout = 30

    def wait_and_input_text(self, locator, text, timeout=None):
        timeout = timeout if timeout else self.default_timeout
        WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        ).send_keys(text)

    def wait_for_element_visible(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def wait_for_element_to_be_clickable(self, locator, timeout=None):
        timeout = timeout if timeout else self.default_timeout
        WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    def wait_and_click(self, locator, timeout=None):
        timeout = timeout if timeout else self.default_timeout
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable(locator)
            ).click()
        except StaleElementReferenceException:
            time.sleep(3)
            WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable(locator)
            ).click()

    def wait_and_clear_text(self, locator, timeout=None):
        timeout = timeout if timeout else self.default_timeout
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable(locator)
            ).clear()
        except StaleElementReferenceException:
            time.sleep(3)
            WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable(locator)
            ).clear()

    def wait_until_element_contains_text(self, locator, text, timeout=None):
        timeout = timeout if timeout else self.default_timeout
        WebDriverWait(self.driver, timeout).until(
            EC.text_to_be_present_in_element(locator, text)
        )

    def wait_until_element_is_visible(self, locator, timeout=None):
        timeout = timeout if timeout else self.default_timeout
        WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    def wait_until_elements_are_visible(self, locator, timeout=None):
        timeout = timeout if timeout else self.default_timeout
        WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_all_elements_located(locator)
        )

    def wait_and_get_elements(self, locator, timeout=None, err=None):
        timeout = timeout if timeout else self.default_timeout
        err = (
            err
            if err
            else f"unable to find elements located by'{locator}','"
                 f"after timeout of {timeout}"
        )
        try:
            elements = WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_all_elements_located(locator)
            )

        except TimeoutException:
            raise TimeoutException(err)

        return elements

    def wait_and_get_text(self, locator, timeout=None):
        timeout = timeout if timeout else self.default_timeout
        elm = WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )
        element_text = elm.text

        return element_text

    def wait_and_get_text_by_visible_element(self, locator, timeout=None):
        timeout = timeout if timeout else self.default_timeout
        elm = WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )
        element_text = elm.text

        return element_text

    def wait_and_get_text_by_new(self, locator, timeout=None):
        timeout = timeout if timeout else self.default_timeout
        elm = WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )
        element_text = elm.text

        return element_text

    def scroll_to_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    def move_to_element_action(self, locator, timeout=None):
        timeout = timeout if timeout else self.default_timeout
        ActionChains(self.driver).move_to_element(locator).perform()

    def presence_of_element(self, locator, timeout=None):
        timeout = timeout if timeout else self.default_timeout
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable(locator)
            ).click()
        except StaleElementReferenceException:
            time.sleep(3)
            WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable(locator)
            ).click()

    def scroll_to_end_of_page(self, timeout=None):
        timeout = timeout if timeout else self.default_timeout
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def scroll_to_end_of_top(self, timeout=None):
        timeout = timeout if timeout else self.default_timeout
        self.driver.execute_script("window.scrollTo(0, 0);")

    def presence_of_element_located(self, locator, timeout=None):
        timeout = timeout if timeout else self.default_timeout
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(locator)
            ).click()
        except StaleElementReferenceException:
            time.sleep(3)
            WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(locator)
            ).click()

    def wait_until_elements_are_invisible(self, locator, timeout=None):
        timeout = timeout if timeout else self.default_timeout
        WebDriverWait(self.driver, timeout).until(
            EC.invisibility_of_element_located(locator)
        )
