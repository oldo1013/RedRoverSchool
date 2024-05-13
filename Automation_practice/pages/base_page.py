from selenium.webdriver.common import by
from selenium.webdriver.common.by import By

from locators.login_locators import LoginLocators
from src.user_data import UserData


class BasePage:
    locators = LoginLocators()
    user = UserData()

    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def open(self):
        self.driver.get(self.url)

    def login(self):
        self.driver.find_element(By.XPATH, self.locators.USERNAME).send_keys(self.user.standard_user)
        self.driver.find_element(By.XPATH, self.locators.PASSWORD).send_keys(self.user.password)
        self.driver.find_element(By.XPATH, self.locators.LOGIN_BUTTON).click()

    def get_text(self, locator):
        return self.driver.find_element(*locator).text

    def click_element(self, locator):
        self.driver.find_element(*locator).click()

    def navigate_to_page(self,locator):
        self.driver.find_element(*locator).click()
