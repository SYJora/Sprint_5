from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

import settings
from locators import BurgerLocators
from data import BurgerTestData

class TestDesigner:

    def test_designer_select_filling(self, driver):

        tab_filling = driver.find_element(*BurgerLocators.TAB_DESIGNER_FILLING)
        tab_filling.click()

        WebDriverWait(driver, settings.MAX_WAIT_TIME).until(
            expected_conditions.text_to_be_present_in_element(BurgerLocators.TEXT_SECTION_DESIGNER_FILLING, 'Начинки'))

        assert driver.find_element(
            *BurgerLocators.TEXT_SECTION_DESIGNER_FILLING).is_displayed() and driver.find_element(
            *BurgerLocators.TEXT_SECTION_DESIGNER_FILLING).text == 'Начинки', "Filling is not set"



    def test_designer_select_sauces(self, driver):

        tab_sauces = driver.find_element(*BurgerLocators.TAB_DESIGNER_SAUCES)
        tab_sauces.click()

        WebDriverWait(driver, settings.MAX_WAIT_TIME).until(
            expected_conditions.text_to_be_present_in_element(BurgerLocators.TEXT_SECTION_DESIGNER_SAUCES, 'Соусы'))

        assert driver.find_element(
            *BurgerLocators.TEXT_SECTION_DESIGNER_SAUCES).is_displayed() and driver.find_element(
            *BurgerLocators.TEXT_SECTION_DESIGNER_SAUCES).text == 'Соусы', "Filling is not set"


    def test_designer_select_burgers(self, driver):

        tab_filling = driver.find_element(*BurgerLocators.TAB_DESIGNER_FILLING)
        tab_filling.click()

        tab_burgers = driver.find_element(*BurgerLocators.TAB_DESIGNER_BURGERS)
        tab_burgers.click()

        WebDriverWait(driver, settings.MAX_WAIT_TIME).until(
            expected_conditions.text_to_be_present_in_element(BurgerLocators.TEXT_SECTION_DESIGNER_BURGERS, 'Булки'))

        assert driver.find_element(
            *BurgerLocators.TEXT_SECTION_DESIGNER_BURGERS).is_displayed() and driver.find_element(
            *BurgerLocators.TEXT_SECTION_DESIGNER_BURGERS).text == 'Булки', "Filling is not set"
