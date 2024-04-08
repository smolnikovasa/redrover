from selenium.common.exceptions import NoSuchElementException
from Page.inventory.inventory_locators import InventoryLocators


class InventoryPage:

    @staticmethod
    def add_item_to_cart(driver, product_name: str):
        driver.find_element(*InventoryLocators().button_add_to_cart(product_name)).click()

    @staticmethod
    def count_product_in_cart(driver):
        try:
            return int(driver.find_element(*InventoryLocators().SPAN_COUNT_PRODUCTS_IN_CART).text)
        except NoSuchElementException:
            return 0

    @staticmethod
    def click_to_picture(driver, product_name: str):
        driver.find_element(*InventoryLocators().img_item(product_name)).click()

    @staticmethod
    def click_to_item_name(driver, product_name: str):
        driver.find_element(*InventoryLocators().text_item_name(product_name)).click()
