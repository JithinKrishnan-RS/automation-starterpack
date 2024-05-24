# utils/helper_functions.py
import time

from selenium.common.exceptions import TimeoutException, StaleElementReferenceException
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class HelperFunctions:
    def __init__(self, driver):
        """
        Constructor for HelperFunctions class.

        :param driver: The WebDriver instance to be used for browser automation.
        """
        self.driver = driver
        self.default_timeout = 30

    def wait_and_input_text(self, locator, text, timeout=None):
        """
        Waits for an element to become visible and inputs text into it.

        :param locator: A tuple containing the method to locate elements and the locator value,
                        e.g., (By.ID, 'element_id') or (By.XPATH, 'element_xpath').
        :param text: The text to be input into the element.
        :param timeout: The maximum time to wait for the element to be visible (in seconds).
                        If not provided, the default timeout set for the class will be used.
        """
        timeout = timeout if timeout else self.default_timeout
        WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        ).send_keys(text)

    def wait_for_element_visible(self, locator, timeout=None):
        """
        Waits for an element to become visible.

        :param locator: A tuple containing the method to locate elements and the locator value.
        :param timeout: The maximum time to wait for the element to be visible (in seconds).
                        If not provided, the default timeout set for the class will be used.
        :return: The visible web element.
        """
        timeout = timeout if timeout else self.default_timeout
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def wait_for_element_to_be_clickable(self, locator, timeout=None):
        """
        Waits for an element to become clickable.

        :param locator: A tuple containing the method to locate elements and the locator value.
        :param timeout: The maximum time to wait for the element to be clickable (in seconds).
                        If not provided, the default timeout set for the class will be used.
        """
        timeout = timeout if timeout else self.default_timeout
        WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    def wait_and_click(self, locator, timeout=None):
        """
        Waits for an element to become clickable and then clicks it.

        :param locator: A tuple containing the method to locate elements and the locator value.
        :param timeout: The maximum time to wait for the element to be clickable (in seconds).
                        If not provided, the default timeout set for the class will be used.
        """
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
        """
        Waits for an element to become clickable and then clears its text.

        :param locator: A tuple containing the method to locate elements and the locator value.
        :param timeout: The maximum time to wait for the element to be clickable (in seconds).
                        If not provided, the default timeout set for the class will be used.
        """
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
        """
        Waits until an element contains the specified text.

        :param locator: A tuple containing the method to locate elements and the locator value.
        :param text: The text to be contained within the element.
        :param timeout: The maximum time to wait for the text to be present (in seconds).
                        If not provided, the default timeout set for the class will be used.
        """
        timeout = timeout if timeout else self.default_timeout
        WebDriverWait(self.driver, timeout).until(
            EC.text_to_be_present_in_element(locator, text)
        )

    def wait_until_element_is_visible(self, locator, timeout=None):
        """
        Waits until an element is visible.

        :param locator: A tuple containing the method to locate elements and the locator value.
        :param timeout: The maximum time to wait for the element to be visible (in seconds).
                        If not provided, the default timeout set for the class will be used.
        """
        timeout = timeout if timeout else self.default_timeout
        WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    def wait_until_elements_are_visible(self, locator, timeout=None):
        """
        Waits until all elements are visible.

        :param locator: A tuple containing the method to locate elements and the locator value.
        :param timeout: The maximum time to wait for the elements to be visible (in seconds).
                        If not provided, the default timeout set for the class will be used.
        """
        timeout = timeout if timeout else self.default_timeout
        WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_all_elements_located(locator)
        )

    def wait_and_get_elements(self, locator, timeout=None, err=None):
        """
        Waits for elements to become visible and returns them.

        :param locator: A tuple containing the method to locate elements and the locator value.
        :param timeout: The maximum time to wait for the elements to be visible (in seconds).
                        If not provided, the default timeout set for the class will be used.
        :param err: Custom error message to be displayed if elements are not found.
        :return: List of visible web elements.
        """
        timeout = timeout if timeout else self.default_timeout
        err = (
            err
            if err
            else f"Unable to find elements located by '{locator}' after timeout of {timeout} seconds."
        )
        try:
            elements = WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_all_elements_located(locator)
            )
        except TimeoutException:
            raise TimeoutException(err)

        return elements

    def wait_and_get_text(self, locator, timeout=None):
        """
        Waits for an element to be visible and returns its text.

        :param locator: A tuple containing the method to locate elements and the locator value.
        :param timeout: The maximum time to wait for the element to be visible (in seconds).
                        If not provided, the default timeout set for the class will be used.
        :return: The text content of the visible web element.
        """
        timeout = timeout if timeout else self.default_timeout
        elm = WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )
        element_text = elm.text

        return element_text

    def wait_and_get_text_by_presence(self, locator, timeout=None):
        """
        Waits for an element to be present in the DOM and returns its text.

        :param locator: A tuple containing the method to locate elements and the locator value.
        :param timeout: The maximum time to wait for the element to be present (in seconds).
                        If not provided, the default timeout set for the class will be used.
        :return: The text content of the present web element.
        """
        timeout = timeout if timeout else self.default_timeout
        elm = WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )
        element_text = elm.text

        return element_text

    def scroll_to_element(self, locator):
        """
        Scrolls the page until the specified element is in view.

        :param locator: A tuple containing the method to locate elements and the locator value.
        """
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    def move_to_element_action(self, locator):
        """
        Moves the mouse pointer to the specified element.

        :param locator: A tuple containing the method to locate elements and the locator value.
        """
        element = self.driver.find_element(*locator)
        ActionChains(self.driver).move_to_element(element).perform()

    def element_to_be_clickable(self, locator, timeout=None):
        """
        Waits for an element to be clickable.

        :param locator: A tuple containing the method to locate elements and the locator value.
        :param timeout: The maximum time to wait for the element to be clickable (in seconds).
                        If not provided, the default timeout set for the class will be used.
        """
        timeout = timeout if timeout else self.default_timeout
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable(locator)
            )
        except StaleElementReferenceException:
            time.sleep(3)
            WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable(locator)
            )

    def scroll_to_end_of_page(self):
        """
        Scrolls the page to the end (bottom) of the page.
        """
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def scroll_to_top_of_page(self):
        """
        Scrolls the page to the top of the page.
        """
        self.driver.execute_script("window.scrollTo(0, 0);")

    def presence_of_element_located(self, locator, timeout=None):
        """
        Waits for an element to be present in the DOM.

        :param locator: A tuple containing the method to locate elements and the locator value.
        :param timeout: The maximum time to wait for the element to be present (in seconds).
                        If not provided, the default timeout set for the class will be used.
        """
        timeout = timeout if timeout else self.default_timeout
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(locator)
            )
        except StaleElementReferenceException:
            time.sleep(3)
            WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(locator)
            )

    def wait_until_elements_are_invisible(self, locator, timeout=None):
        """
        Waits until elements are invisible.

        :param locator: A tuple containing the method to locate elements and the locator value.
        :param timeout: The maximum time to wait for the elements to be invisible (in seconds).
                        If not provided, the default timeout set for the class will be used.
        """
        timeout = timeout if timeout else self.default_timeout
        WebDriverWait(self.driver, timeout).until(
            EC.invisibility_of_element_located(locator)
        )
