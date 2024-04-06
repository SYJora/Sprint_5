from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

import settings
from locators import BurgerLocators
from data import BurgerTestData

class TestTransitionsFromPersonalCabinet:

    def test_tansitions_from_personal_account_in_to_designer(self, driver):
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

        button_designer = driver.find_element(*BurgerLocators.BUTTON_DESIGNER)
        button_designer.click()

        WebDriverWait(driver, settings.MAX_WAIT_TIME).until(
            expected_conditions.text_to_be_present_in_element(BurgerLocators.TEXT_DESIGNER, 'Соберите бургер'))

        assert driver.find_element(*BurgerLocators.TEXT_DESIGNER).is_displayed() and driver.find_element(*BurgerLocators.TEXT_DESIGNER).text == 'Соберите бургер' , "Failde enter to designer"

    def test_tansitions_from_personal_account_in_to_designer_by_click_on_logo(self, driver):
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

        logo = driver.find_element(*BurgerLocators.LOGO)
        logo.click()

        WebDriverWait(driver, settings.MAX_WAIT_TIME).until(
            expected_conditions.text_to_be_present_in_element(BurgerLocators.TEXT_DESIGNER, 'Соберите бургер'))

        assert driver.find_element(*BurgerLocators.TEXT_DESIGNER).is_displayed() and driver.find_element(
            *BurgerLocators.TEXT_DESIGNER).text == 'Соберите бургер', "Failde enter to designer"