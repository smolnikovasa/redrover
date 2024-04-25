import allure

from page.auth.auth_page import AuthPage
from page.inventory.inventory_page import InventoryPage
from src.assert_msg import AssertMsg
from src.urls import Urls
from src.user_names import UserNames


"""Каталог товаров."""


@allure.suite("Добавление товаров в корзину")
class TestInventoryPage:
    urls = Urls()
    assert_massage = AssertMsg()
    user_names = UserNames()

    # Добавление товара в корзину через каталог

    @allure.title("Добавление товара в корзину через каталог")
    def test_add_to_chart(self, driver):
        auth_page = AuthPage(driver)
        inventory_page = InventoryPage(driver)

        auth_page.open_page(self.urls.URL_BASE)
        auth_page.auth(self.user_names.STANDARD_USER, self.user_names.PASSWORD)
        count_product_defore_add = inventory_page.count_product_in_cart()
        inventory_page.add_item_to_cart("Sauce Labs Backpack")
        count_product_after_add = inventory_page.count_product_in_cart()
        assert count_product_after_add - count_product_defore_add == 1, (
            self.assert_massage.ASSERT_MASSAGE_INVALID_COUNT_IN_CART)

    # Успешный переход к карточке товара после клика на картинку товара
    @allure.title("Успешный переход к карточке товара из каталога")
    def test_go_to_card_01(self, driver):
        auth_page = AuthPage(driver)
        inventory_page = InventoryPage(driver)

        auth_page.open_page(self.urls.URL_BASE)
        auth_page.auth(self.user_names.STANDARD_USER, self.user_names.PASSWORD)
        inventory_page.click_to_picture("Sauce Labs Backpack")
        assert self.urls.URL_CARD in driver.current_url, self.assert_massage.ASSERT_MASSAGE_INVALID_URL

    # Успешный переход к карточке товара после клика на название товара
    @allure.title("Успешный переход к карточке товара из каталога 2")
    def test_go_to_card_02(self, driver):
        auth_page = AuthPage(driver)
        inventory_page = InventoryPage(driver)

        auth_page.open_page(self.urls.URL_BASE)
        auth_page.auth(self.user_names.STANDARD_USER, self.user_names.PASSWORD)
        inventory_page.click_to_item_name("Sauce Labs Backpack")
        assert self.urls.URL_CARD in driver.current_url, self.assert_massage.ASSERT_MASSAGE_INVALID_URL
