from selenium.common.exceptions import NoSuchElementException

from page.base_page import BasePage
from page.inventory.inventory_locators import InventoryLocators
from src.urls import Urls


class InventoryPage(BasePage):
    url = Urls()
    inventory_locators = InventoryLocators()

    def add_item_to_cart(self, product_name: str):
        self.element_is_clickable(self.inventory_locators.button_add_to_cart(product_name)).click()

    def count_product_in_cart(self):
        try:
            return int(self.get_text_element(self.inventory_locators.SPAN_COUNT_PRODUCTS_IN_CART))
        except NoSuchElementException:
            return 0

    def click_to_picture(self, product_name: str):
        self.element_is_clickable(self.inventory_locators.img_item(product_name)).click()

    def click_to_item_name(self, driver, product_name: str):
        driver.find_element(*self.inventory_locators.text_item_name(product_name)).click()
