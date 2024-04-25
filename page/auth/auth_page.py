import allure

from page.auth.auth_locators import AuthLocators
from page.base_page import BasePage


class AuthPage(BasePage):
    auth_locators = AuthLocators()

    @allure.step("Авторизация")
    def auth(self, login: str, password: str):
        with allure.step(f"Пользователь {login}"):
            self.fill_field(self.auth_locators.FIELD_USER, 'Username', login)
            self.fill_field(self.auth_locators.FIELD_PASSWORD, 'Password', password)
            self.click_to_element(self.auth_locators.BUTTON_LOGIN, 'кнопке Login')

    @allure.step("Получаем текст ошибки")
    def get_text_error(self):
        return self.get_text_element(self.auth_locators.FIELD_ERROR)
