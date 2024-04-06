import time
from locators import BurgerLocators
from data import BurgerTestData


class TestBurgerRegistration:

    def test_registration(self, driver):

        button_login = driver.find_element(*BurgerLocators.BUTTON_LOGIN_IN_ACCOUNT)
        button_login.click()

        registretion_link = driver.find_element(*BurgerLocators.REDISTRATION_LINK)
        registretion_link.click()

        name = driver.find_element(*BurgerLocators.ACCOUNT_NAME)
        name.send_keys(BurgerTestData.NAME)
        email = driver.find_element(*BurgerLocators.REGIDTER_ACCOUNT_EMAIL)
        email.send_keys(BurgerTestData.EMAIL)
        password = driver.find_element(*BurgerLocators.ACCOUNT_PASSWORD)
        password.send_keys(BurgerTestData.PASSWORD)

        button_registrat = driver.find_element(*BurgerLocators.BUTTON_REGISTRATION)
        button_registrat.click()

        assert driver.find_element(*BurgerLocators.BUTTON_LOGIN).is_displayed() and driver.find_element(*BurgerLocators.BUTTON_LOGIN).text == 'Вход', 'Registration Faild'

        driver.quit()

    def test_registration_accaunt_with_incorrect_password(self, driver):

        button_login = driver.find_element(*BurgerLocators.BUTTON_LOGIN_IN_ACCOUNT)
        button_login.click()

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

        driver.quit()