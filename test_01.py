from Page.auth_page import AuthPage
from Page.inventory.inventory_page import InventoryPage
from Page.inventory.inventory_const import InventoryConst
from Page.inventory_item.inventory_item_const import InventoryItemConst


"""Авторизация."""

ASSERT_MASSAGE_INVALID_URL = "url не соответствует ожидаемому"
ASSERT_MASSAGE_INVALID_COUNT_IN_CART = "некорректное добавление товара в корзину"

# Авторизация, используя корректные данные (standard_user, secret_sauce)
def test_auth_01(driver):
    AuthPage().auth(driver, "standard_user", "secret_sauce")
    assert driver.current_url == InventoryConst().URL_CATALOG, ASSERT_MASSAGE_INVALID_URL


# Авторизация, используя некорректные данные (user, user)
def test_auth_02(driver):
    AuthPage().auth(driver, "user", "user")
    assert driver.current_url == InventoryConst().URL_CATALOG, ASSERT_MASSAGE_INVALID_URL


# Добавление товара в корзину через каталог
def test_add_to_chart(driver):
    AuthPage().auth(driver, "standard_user", "secret_sauce")
    inventory_page = InventoryPage()
    count_product_defore_add = inventory_page.count_product_in_cart(driver)
    inventory_page.add_item_to_cart(driver, "Sauce Labs Backpack")
    count_product_after_add = inventory_page.count_product_in_cart(driver)
    assert count_product_after_add-count_product_defore_add == 1, ASSERT_MASSAGE_INVALID_COUNT_IN_CART


# Успешный переход к карточке товара после клика на картинку товара
def test_go_to_card_01(driver):
    AuthPage().auth(driver, "standard_user", "secret_sauce")
    InventoryPage().click_to_picture(driver, "Sauce Labs Backpack")
    assert InventoryItemConst().URL_CARD in driver.current_url, ASSERT_MASSAGE_INVALID_URL


# Успешный переход к карточке товара после клика на название товара
def test_go_to_card_02(driver):
    AuthPage().auth(driver, "standard_user", "secret_sauce")
    InventoryPage().click_to_item_name(driver, "Sauce Labs Backpack")
    assert InventoryItemConst().URL_CARD in driver.current_url, ASSERT_MASSAGE_INVALID_URL
