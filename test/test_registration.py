from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

import settings
from locators import BurgerLocators
from data import BurgerTestData


class TestBurgerRegistration:

    def test_registration(self, driver, press_button_login_in_account, gen_random_email):

        registretion_link = driver.find_element(*BurgerLocators.REDISTRATION_LINK)
        registretion_link.click()

        name = driver.find_element(*BurgerLocators.ACCOUNT_NAME)
        name.send_keys(BurgerTestData.NAME)
        email = driver.find_element(*BurgerLocators.ACCOUNT_EMAIL)
        email.send_keys(gen_random_email)
        password = driver.find_element(*BurgerLocators.ACCOUNT_PASSWORD)
        password.send_keys(BurgerTestData.PASSWORD)

        button_registrat = driver.find_element(*BurgerLocators.BUTTON_REGISTRATION)
        button_registrat.click()

        WebDriverWait(driver, settings.MAX_WAIT_TIME).until(
            expected_conditions.text_to_be_present_in_element(BurgerLocators.BUTTON_LOGIN, 'Войти'))

        assert driver.find_element(*BurgerLocators.BUTTON_LOGIN).is_displayed() and driver.find_element(*BurgerLocators.BUTTON_LOGIN).text == 'Войти', 'Registration Faild'


    def test_registration_accaunt_with_incorrect_password(self, driver, press_button_login_in_account):

        registretion_link = driver.find_element(*BurgerLocators.REDISTRATION_LINK)
        registretion_link.click()

        name = driver.find_element(*BurgerLocators.ACCOUNT_NAME)
        name.send_keys(BurgerTestData.NAME)
        email = driver.find_element(*BurgerLocators.ACCOUNT_EMAIL)
        email.send_keys(BurgerTestData.EMAIL)
        password = driver.find_element(*BurgerLocators.ACCOUNT_PASSWORD)
        password.send_keys(BurgerTestData.INCORRECT_PASSWORD)

        button_registrat = driver.find_element(*BurgerLocators.BUTTON_REGISTRATION)
        button_registrat.click()

        assert driver.find_element(*BurgerLocators.ERROR_TEXT_INCORRECT_PASSWORD).is_displayed() and driver.find_element(*BurgerLocators.ERROR_TEXT_INCORRECT_PASSWORD).text == 'Некорректный пароль'
