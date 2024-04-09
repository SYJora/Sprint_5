from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

import conftest
import settings
from locators import BurgerLocators

class TestPersonal_account:

    def test_enter_personal_account(self, driver):
        button_login = driver.find_element(*BurgerLocators.BUTTON_LOGIN_IN_ACCOUNT)
        button_login.click()

        conftest.log_in(driver)

        button_personal_account = driver.find_element(*BurgerLocators.BUTTON_PERSONAL_ACCOUNT)
        button_personal_account.click()

        WebDriverWait(driver, settings.MAX_WAIT_TIME).until(
            expected_conditions.text_to_be_present_in_element(BurgerLocators.TAB_PROFAIL, 'Профиль'))

        assert driver.find_element(
            *BurgerLocators.TAB_PROFAIL).is_displayed() and driver.find_element(
            *BurgerLocators.TAB_PROFAIL).text == 'Профиль', 'Personal account enter faield'
