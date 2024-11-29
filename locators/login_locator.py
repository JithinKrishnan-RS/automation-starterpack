from selenium.webdriver.common.by import By


class LoginLocators:
    email = By.ID, "email"
    password = By.ID, "password"
    sign_in = By.XPATH, "//button[normalize-space()='Sign In']"
