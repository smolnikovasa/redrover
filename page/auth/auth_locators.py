from selenium.webdriver.common.by import By

class AuthLocators():
    FIELD_USER = (By.XPATH, "//*[@id='user-name']")
    FIELD_PASSWORD = (By.XPATH, "//*[@id='password']")
    BUTTON_LOGIN = (By.XPATH, "//*[@id='login-button']")
    FIELD_ERROR = (By.CSS_SELECTOR, "h3[data-test='error']")
