# locators/base_page_locators.py
from selenium.webdriver.common.by import By


class BasePageLocators:
    search_input = (By.NAME, "q")
