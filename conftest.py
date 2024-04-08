import pytest
from selenium import webdriver
from random import randint
from data import BurgerTestData
from locators import BurgerLocators


@pytest.fixture(scope = 'function')
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.maximize_window()
    chrome_driver.get("https://stellarburgers.nomoreparties.site/")

    yield chrome_driver

    chrome_driver.quit()

@pytest.fixture(scope = 'function')
def gen_random_email():
    res = randint(000, 999)
    yield f"sidorovich7{res}@mail.ru"

def log_in(driver):
    email = driver.find_element(*BurgerLocators.ACCOUNT_EMAIL)
    email.send_keys(BurgerTestData.EMAIL)
    password = driver.find_element(*BurgerLocators.ACCOUNT_PASSWORD)
    password.send_keys(BurgerTestData.PASSWORD)
    button_login = driver.find_element(*BurgerLocators.BUTTON_LOGIN)
    button_login.click()
