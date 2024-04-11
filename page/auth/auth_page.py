from page.auth.auth_locators import AuthLocators
from page.base_page import BasePage
from src.urls import Urls


class AuthPage(BasePage):
    auth_locators = AuthLocators()

    def auth(self, login: str, password: str):
        self.element_is_visibility(self.auth_locators.FIELD_USER).send_keys(login)
        self.element_is_visibility(self.auth_locators.FIELD_PASSWORD).send_keys(password)
        self.element_is_clickable(self.auth_locators.BUTTON_LOGIN).click()

    def get_text_error(self):
        return self.get_text_element(self.auth_locators.FIELD_ERROR)
