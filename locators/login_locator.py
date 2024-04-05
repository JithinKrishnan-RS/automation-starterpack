from selenium.webdriver.common.by import By


class LoginLocators:
    email = By.ID, "email"
    password = By.ID, "password"
    sign_in = By.XPATH, "//button[normalize-space()='Sign In']"
    otp = By.ID, "otp"
    verify = By.XPATH, "//button[normalize-space()='Verify']"
    error_message = By.XPATH, "//div[@class='alert alert-danger']"
