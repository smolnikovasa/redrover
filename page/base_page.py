import allure
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait as wait
from selenium.webdriver.remote.webelement import WebElement


class BasePage:
    timeout = 10

    def __init__(self, driver):
        self.driver = driver

    def open_page(self, url):
        with allure.step(f"Открытие страницы {url}"):
            self.driver.get(url)

    def element_is_visibility(self, locator, timeout=timeout) -> WebElement:
        with allure.step(f"Найти элемент {locator}"):
            return wait(self.driver, timeout).until(ec.visibility_of_element_located(locator))

    def elements_is_not_visibility(self, locator, timeout=timeout) -> WebElement:
        with allure.step(f"Дождаться исчезновения элементов {locator}"):
            return wait(self.driver, timeout).until(ec.invisibility_of_element_located(locator))


    def get_elements(self, locator, timeout=timeout) -> list:
        with allure.step(f"Найти элементы {locator}"):
            return self.driver.find_elements(*locator)


    def element_is_clickable(self, locator, timeout=timeout) -> WebElement:
        return wait(self.driver, timeout).until(ec.element_to_be_clickable(locator))

    def get_element(self, locator) -> WebElement:
        return self.driver.find_element(*locator)

    def get_text_element(self, locator) -> str:
        return self.get_element(locator).text


    def element_is_displaid(self: WebElement):
        return self.is_displayed()

    def fill_field(self, locator, name, value):
        with allure.step(f"Заполнить поле '{name}' значением {value}"):
            self.element_is_visibility(locator).send_keys(value)

    def click_to_element(self, locator, name):
        with allure.step(f"Кликнуть по '{name}'"):
            self.element_is_clickable(locator).click()
