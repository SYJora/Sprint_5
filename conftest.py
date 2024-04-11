import pytest
import urls
from selenium import webdriver
from random import randint

from data import BurgerTestData
from locators import BurgerLocators


@pytest.fixture(scope = 'function')
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.maximize_window()
    chrome_driver.get(urls.URL)

    yield chrome_driver

    chrome_driver.quit()

@pytest.fixture(scope = 'function')
def gen_random_email():
    res = randint(000, 999)
    yield f"sidorovich7{res}@mail.ru"

@pytest.fixture(scope = 'function')
def log_in(driver):
    button_login = driver.find_element(*BurgerLocators.BUTTON_LOGIN_IN_ACCOUNT)
    button_login.click()

    email = driver.find_element(*BurgerLocators.ACCOUNT_EMAIL)
    email.send_keys(BurgerTestData.EMAIL)
    password = driver.find_element(*BurgerLocators.ACCOUNT_PASSWORD)
    password.send_keys(BurgerTestData.PASSWORD)
    button_login = driver.find_element(*BurgerLocators.BUTTON_LOGIN)
    button_login.click()
    yield

@pytest.fixture(scope = 'function')
def by_button_personal_account(driver):
    buttton_log_in_personal_account = driver.find_element(*BurgerLocators.BUTTON_PERSONAL_ACCOUNT)
    buttton_log_in_personal_account.click()

    email = driver.find_element(*BurgerLocators.ACCOUNT_EMAIL)
    email.send_keys(BurgerTestData.EMAIL)
    password = driver.find_element(*BurgerLocators.ACCOUNT_PASSWORD)
    password.send_keys(BurgerTestData.PASSWORD)
    button_login = driver.find_element(*BurgerLocators.BUTTON_LOGIN)
    button_login.click()
    yield