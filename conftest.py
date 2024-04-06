import pytest
from selenium import webdriver
import settings
from data import BurgerTestData
from locators import BurgerLocators


@pytest.fixture(scope = 'function')
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.maximize_window()
    chrome_driver.get(settings.URL)
    return chrome_driver
