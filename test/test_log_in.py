from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

import conftest
import settings
from locators import BurgerLocators


class TestBurgerLogin:

    def test_log_in_button_on_main_page(self, driver):
        button_login = driver.find_element(*BurgerLocators.BUTTON_LOGIN_IN_ACCOUNT)
        button_login.click()

        conftest.log_in(driver)

        WebDriverWait(driver, settings.MAX_WAIT_TIME).until(
            expected_conditions.text_to_be_present_in_element(BurgerLocators.BUTTON_MAKE_ORDER, 'Оформить заказ'))

        assert driver.find_element(*BurgerLocators.BUTTON_MAKE_ORDER).is_displayed() and driver.find_element(
            *BurgerLocators.BUTTON_MAKE_ORDER).text == 'Оформить заказ', 'Log-in, Faild'


    def test_login_in_by_button_personal_account(self, driver):
        button_personal_account = driver.find_element(*BurgerLocators.BUTTON_PERSONAL_ACCOUNT)
        button_personal_account.click()

        conftest.log_in(driver)

        WebDriverWait(driver, settings.MAX_WAIT_TIME).until(
            expected_conditions.text_to_be_present_in_element(BurgerLocators.BUTTON_MAKE_ORDER, 'Оформить заказ'))

        assert driver.find_element(*BurgerLocators.BUTTON_MAKE_ORDER).is_displayed() and driver.find_element(
            *BurgerLocators.BUTTON_MAKE_ORDER).text == 'Оформить заказ', 'Log-in, Faild'


    def test_login_use_link_in_registration_form(self, driver):
        button_login = driver.find_element(*BurgerLocators.BUTTON_LOGIN_IN_ACCOUNT)
        button_login.click()

        registretion_link = driver.find_element(*BurgerLocators.REDISTRATION_LINK)
        registretion_link.click()

        login_link = driver.find_element(*BurgerLocators.LINK_LOGIN)
        login_link.click()

        conftest.log_in(driver)

        WebDriverWait(driver, settings.MAX_WAIT_TIME).until(
            expected_conditions.text_to_be_present_in_element(BurgerLocators.BUTTON_MAKE_ORDER, 'Оформить заказ'))

        assert driver.find_element(*BurgerLocators.BUTTON_MAKE_ORDER).is_displayed() and driver.find_element(
            *BurgerLocators.BUTTON_MAKE_ORDER).text == 'Оформить заказ', 'Log-in, Faild'


    def test_login_use_link_in_password_reset_form(self, driver):
        button_login = driver.find_element(*BurgerLocators.BUTTON_LOGIN_IN_ACCOUNT)
        button_login.click()

        link_forgot_password = driver.find_element(*BurgerLocators.LINK_FORGOT_PASSWORD)
        link_forgot_password.click()

        login_link = driver.find_element(*BurgerLocators.LINK_LOGIN)
        login_link.click()

        conftest.log_in(driver)

        WebDriverWait(driver, settings.MAX_WAIT_TIME).until(
            expected_conditions.text_to_be_present_in_element(BurgerLocators.BUTTON_MAKE_ORDER, 'Оформить заказ'))

        assert driver.find_element(*BurgerLocators.BUTTON_MAKE_ORDER).is_displayed() and driver.find_element(
            *BurgerLocators.BUTTON_MAKE_ORDER).text == 'Оформить заказ', 'Log-in, Faild'
