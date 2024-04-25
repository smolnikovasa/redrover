import datetime

import allure
import datetime
import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def driver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--incognito")
    service = Service(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    yield driver
    allure.attach(driver.get_screenshot_as_png(), f"скриншот от {datetime.datetime.now()}", allure.attachment_type.PNG)
    driver.quit()
