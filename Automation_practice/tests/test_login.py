from selenium.webdriver.common.by import By

from locators.login_locators import LoginLocators
from locators.main_locators import MainLocators
from pages.login_page import LoginPage
from src.urls import Urls
from src.user_data import UserData


class TestLogin:
    url = Urls()
    main_locators = MainLocators()

    # TC №1 Correct auth

    def test_auth_positive(self, driver):
        page = LoginPage(driver, self.url.BASE_URL)
        page.open()
        page.login()
        actual_text = page.get_text(self.main_locators.TITLE)
        expected_text = "Products"
        assert actual_text == expected_text, f'Unexpected text: expected -{expected_text}, actual -{actual_text}'

    # TC №2 Incorrect auth
    def test_auth_negative(self, driver):
        page = LoginPage(driver, self.url.BASE_URL)
        page.open()
        page.wrong_login()
        actual_text = driver.find_element(By.XPATH, './/h3').text
        expected_text = "Epic sadface: Username and password do not match any user in this service"
        assert actual_text == expected_text, f'Unexpected text: expected -{expected_text}, actual -{actual_text}'
