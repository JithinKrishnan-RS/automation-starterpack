from selenium.webdriver.common.by import By


class LoginLocators:
    login_btn = By.XPATH, "(//button[normalize-space()='Log in'])[1]"
    email = By.ID, "login-email"
    password = By.ID, "login-password"
    sign_in = By.XPATH, "but_submit"
    profile_icon = By.ID, ""
    logout = By.ID, ""
    error_message = By.ID, ""
    validation_message = By.ID, ""
    remember_me = By.ID, ""
