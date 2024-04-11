from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait as wait


class BasePage:
    timeout = 10

    def __init__(self, driver):
        self.driver = driver

    def open_page(self, url):
        self.driver.get(url)

    def element_is_visibility(self, locator, timeout=timeout):
        return wait(self.driver, timeout).until(ec.visibility_of_element_located(locator))

    def element_is_clickable(self, locator, timeout=timeout):
        return wait(self.driver, timeout).until(ec.element_to_be_clickable(locator))

    def get_element(self, locator):
        return self.driver.find_element(*locator)

    def get_text_element(self, locator) -> str:
        return self.get_element(locator).text
