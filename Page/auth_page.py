from Page.auth_locators import AuthLocators

URL_AUTH = "https://www.saucedemo.com/"

class AuthPage:

    @staticmethod
    def auth(driver, login: str, password: str):
        driver.get(URL_AUTH)
        driver.find_element(*AuthLocators().FIELD_USER).send_keys(login)
        driver.find_element(*AuthLocators().FIELD_PASSWORD).send_keys(password)
        driver.find_element(*AuthLocators().BUTTON_LOGIN).click()
