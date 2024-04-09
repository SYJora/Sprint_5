from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

import settings
from locators import BurgerLocators
from data import BurgerTestData

class TestPersonalAccountExit:

    def test_log_out(self, driver):

        button_login = driver.find_element(*BurgerLocators.BUTTON_LOGIN_IN_ACCOUNT)
        button_login.click()

        email = driver.find_element(*BurgerLocators.ACCOUNT_EMAIL)
        email.send_keys(BurgerTestData.EMAIL)
        password = driver.find_element(*BurgerLocators.ACCOUNT_PASSWORD)
        password.send_keys(BurgerTestData.PASSWORD)
        button_login = driver.find_element(*BurgerLocators.BUTTON_LOGIN)
        button_login.click()

        button_personal_account = driver.find_element(*BurgerLocators.BUTTON_PERSONAL_ACCOUNT)
        button_personal_account.click()

        WebDriverWait(driver, settings.MAX_WAIT_TIME).until(
            expected_conditions.text_to_be_present_in_element(BurgerLocators.BUTTON_LOGOUT, 'Выход'))

        button_log_out = driver.find_element(*BurgerLocators.BUTTON_LOGOUT)
        button_log_out.click()

        WebDriverWait(driver, settings.MAX_WAIT_TIME).until(
            expected_conditions.text_to_be_present_in_element(BurgerLocators.TEXT_LOGIN_PAGE, 'Вход'))

        assert driver.find_element(
            *BurgerLocators.TEXT_LOGIN_PAGE).is_displayed() and driver.find_element(
            *BurgerLocators.TEXT_LOGIN_PAGE).text == 'Вход', 'Log-out faield'

