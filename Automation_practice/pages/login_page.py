from selenium.webdriver.common.by import By
from pages.base_page import BasePage



class LoginPage(BasePage):
    def wrong_login(self):
        self.driver.find_element(By.XPATH, self.locators.USERNAME).send_keys(self.user.incorrect_user)
        self.driver.find_element(By.XPATH, self.locators.PASSWORD).send_keys(self.user.incorrect_password)
        self.driver.find_element(By.XPATH, self.locators.LOGIN_BUTTON).click()
