import allure

from page.auth.auth_page import AuthPage
from page.cart.cart_page import CartPage
from page.inventory.inventory_page import InventoryPage
from src.assert_msg import AssertMsg
from src.urls import Urls
from src.user_names import UserNames


"""Добавление товаров в корзину."""


@allure.suite("Добавление товаров в корзину")
class TestAddToChart:
    urls = Urls()
    assert_massage = AssertMsg()
    user_names = UserNames()

    # Добавление товара в корзину через каталог

    @allure.title("Добавление товара в корзину через каталог")
    def test_add_to_chart(self, driver):
        auth_page = AuthPage(driver)
        inventory_page = InventoryPage(driver)
        cart_page = CartPage(driver)
        auth_page.open_page(self.urls.URL_BASE)
        auth_page.auth(self.user_names.STANDARD_USER, self.user_names.PASSWORD)
        inventory_page.add_item_to_cart("Sauce Labs Backpack")
        inventory_page.go_to_card()
        cart_page.delete_item_in_cart("Sauce Labs Backpack")
        cart_page.elements_is_not_visibility(cart_page.cart_locators.PRODUCTS_NAME_TEXT)
        assert len(cart_page.get_product_in_cart()) == 0, "Корзина не пуста"
