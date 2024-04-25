import allure
from selenium.common.exceptions import NoSuchElementException

from page.base_page import BasePage
from page.cart.cart_locators import CartLocators
from src.urls import Urls


class CartPage(BasePage):
    url = Urls()
    cart_locators = CartLocators()

    @allure.step("Найти товары в корзине")
    def get_product_in_cart(self):
        return self.get_elements(self.cart_locators.PRODUCTS_NAME_TEXT)

    @allure.step("Удалить товар из корзины")
    def delete_item_in_cart(self, item_name):
        self.click_to_element(self.cart_locators.button_item_remove_name(item_name), "кнопке 'Remove'")
