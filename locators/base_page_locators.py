# locators/base_page_locators.py
from selenium.webdriver.common.by import By


class BasePageLocators:
    SEARCH_INPUT = (By.NAME, "q")
