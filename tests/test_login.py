from page.auth.auth_page import AuthPage
from src.assert_msg import AssertMsg
from src.urls import Urls
from src.user_names import UserNames


class TestLogin:
    urls = Urls()
    assert_massage = AssertMsg()
    user_names = UserNames()

    # Авторизация, используя корректные данные (standard_user, secret_sauce)
    def test_auth_01(self, driver):
        auth_page = AuthPage(driver)
        auth_page.open_page(self.urls.URL_BASE)
        auth_page.auth(self.user_names.STANDARD_USER, self.user_names.PASSWORD)
        assert driver.current_url == self.urls.URL_CATALOG, self.assert_massage.ASSERT_MASSAGE_INVALID_URL

    # Авторизация, используя некорректные данные (user, user)
    def test_auth_02(self, driver):
        auth_page = AuthPage(driver)
        auth_page.open_page(self.urls.URL_BASE)
        auth_page.auth(self.user_names.USER_WRONG, self.user_names.PASSWORD_WRONG)
        assert auth_page.get_text_error() == ("Epic sadface: Username and password do not match any user in this "
                                              "service"), self.assert_massage.ASSERT_MESSAGE_TEXT_WRONG
