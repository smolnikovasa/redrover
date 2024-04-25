from selenium.webdriver.common.by import By


class CartLocators:
    PRODUCTS_NAME_TEXT = (By.XPATH, "div[data-test = 'inventory-item-name']")

    @staticmethod
    def item_name(product_name: str) -> str:
        return f"//div[text() ='{product_name}']"

    @staticmethod
    def button_item_remove_name(product_name: str) -> tuple:
        return (By.XPATH, f"{CartLocators().item_name(product_name)}//ancestor::div//button[text() ='Remove']")

