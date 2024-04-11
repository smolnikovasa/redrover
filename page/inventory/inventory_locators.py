from selenium.webdriver.common.by import By


class InventoryLocators:

    @staticmethod
    def item_name(product_name: str) -> str:
        return f"//div[text() ='{product_name}']"

    @staticmethod
    def text_item_name(product_name: str) -> tuple:
        return By.XPATH, InventoryLocators().item_name(product_name)

    @staticmethod
    def button_add_to_cart(product_name: str) -> tuple:
        return (
            By.XPATH,
            f"{InventoryLocators().item_name(product_name)}//ancestor::div[@class='inventory_item_description']"
            f"//button"
        )

    @staticmethod
    def img_item(product_name: str) -> tuple:
        return (
            By.XPATH,
            f"{InventoryLocators().item_name(product_name)}//ancestor::div[@class='inventory_item']//img"
        )

    SPAN_COUNT_PRODUCTS_IN_CART = (By.XPATH, "//span[@class='shopping_cart_badge']")
