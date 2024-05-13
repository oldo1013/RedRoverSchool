from locators.main_locators import MainLocators
from locators.order_locators import OrderLocators
from pages.base_page import BasePage
from src.order_data import OrderData


class OrderPage(BasePage):
    main_locators = MainLocators()
    order_locators = OrderLocators()
    order = OrderData()

    def add_order_to_basket(self):
        self.click_element(self.main_locators.ADD_SAUCE_LAB_BACKPACK)

    def find_element(self, locator):
        return self.driver.find_element(*locator).is_displayed()

    def add_to_basket(self):
        self.click_element(self.order_locators.ADD_TO_CART)

    def remove_from_basket_card(self):
        self.click_element(self.order_locators.REMOVE)

    def fill_order(self):
        self.driver.find_element(*self.order_locators.FIRSTNAME).send_keys(self.order.first_name)
        self.driver.find_element(*self.order_locators.LASTNAME).send_keys(self.order.last_name)
        self.driver.find_element(*self.order_locators.POSTALCODE).send_keys(self.order.zip_code)
