import allure
from selenium.common.exceptions import NoSuchElementException

from page.base_page import BasePage
from page.inventory.inventory_locators import InventoryLocators
from src.urls import Urls


class InventoryPage(BasePage):
    url = Urls()
    inventory_locators = InventoryLocators()

    @allure.step("Добавление товара в корзину из каталога")
    def add_item_to_cart(self, product_name: str):
        self.click_to_element(self.inventory_locators.button_add_to_cart(product_name), "Название товара")

    def count_product_in_cart(self):
        try:
            return int(self.get_text_element(self.inventory_locators.SPAN_COUNT_PRODUCTS_IN_CART))
        except NoSuchElementException:
            return 0

    @allure.step("Кликнуть по картинке товара")
    def click_to_picture(self, product_name: str):
        self.click_to_element(self.inventory_locators.img_item(product_name), f'картинке товара {product_name}')

    @allure.step("Кликнуть по названию товара")
    def click_to_item_name(self, product_name: str):
        self.click_to_element(self.inventory_locators.text_item_name(product_name), f'названию товара {product_name}')

    @allure.step("Перейти в корзину")
    def go_to_card(self):
        self.click_to_element(self.inventory_locators.CART_IMG, "иконке корзины")

