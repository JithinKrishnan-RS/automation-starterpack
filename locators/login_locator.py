from selenium.webdriver.common.by import By


class LoginLocators:
    EMAIL = By.ID, "email"
    PASSWORD = By.ID, "password"
    SIGN_IN = By.XPATH, "//button[normalize-space()='Sign In']"
