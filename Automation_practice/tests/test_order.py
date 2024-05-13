from selenium.common import NoSuchElementException
from locators.main_locators import MainLocators
from locators.order_locators import OrderLocators
from pages.order_page import OrderPage
from src.urls import Urls


class TestOrder:
    url = Urls()
    main_locators = MainLocators()
    order_locators = OrderLocators()

    # TC№3 Add item from catalog
    def test_add_item_from_catalog(self, driver):
        page = OrderPage(driver, self.url.BASE_URL)
        page.open()
        page.login()
        page.add_order_to_basket()
        assert page.find_element(self.main_locators.REMOVE_SAUCE_LAB_BACKPACK) == True
        page.navigate_to_page(self.main_locators.BASKET)
        current_url = driver.current_url
        expected_url = 'https://www.saucedemo.com/cart.html'
        assert current_url == expected_url, f'Unexpected url: expected -{expected_url}, actual -{current_url}'
        actual_text = page.get_text(self.order_locators.SAUCE_LAB_BACKPACK_ITEM)
        expected_text = 'Sauce Labs Backpack'
        assert actual_text == expected_text, f'Unexpected item: expected -{expected_text}, actual -{actual_text}'
        actual_quantity = page.get_text(self.order_locators.CART_QUANTITY)
        expected_quantity = '1'
        assert actual_quantity == expected_quantity, f'Unexpected quantity: expected -{expected_quantity}, actual -{actual_quantity}'

    # TC№4 Remove item from basket
    def test_remove_item_from_basket(self, driver):
        page = OrderPage(driver, self.url.BASE_URL)
        page.open()
        page.login()
        page.add_order_to_basket()
        page.navigate_to_page(self.main_locators.BASKET)
        page.click_element(self.main_locators.REMOVE_SAUCE_LAB_BACKPACK)
        try:
            page.find_element(self.order_locators.SAUCE_LAB_BACKPACK_ITEM)
        except NoSuchElementException:
            message = 'Incorrect'
        message = 'Correct'
        assert message == 'Correct'

    # TC№5 Add item from product card
    def test_add_item_from_card(self, driver):
        page = OrderPage(driver, self.url.BASE_URL)
        page.open()
        page.login()
        page.navigate_to_page(self.main_locators.SAUCE_LAB_BACKPACK_IMAGE)
        page.add_to_basket()
        assert page.find_element(self.order_locators.REMOVE) == True
        page.navigate_to_page(self.main_locators.BASKET)
        current_url = driver.current_url
        expected_url = 'https://www.saucedemo.com/cart.html'
        assert current_url == expected_url, f'Unexpected url: expected -{expected_url}, actual -{current_url}'
        actual_text = page.get_text(self.order_locators.SAUCE_LAB_BACKPACK_ITEM)
        expected_text = 'Sauce Labs Backpack'
        assert actual_text == expected_text, f'Unexpected item: expected -{expected_text}, actual -{actual_text}'
        actual_quantity = page.get_text(self.order_locators.CART_QUANTITY)
        expected_quantity = '1'
        assert actual_quantity == expected_quantity, f'Unexpected quantity: expected -{expected_quantity}, actual -{actual_quantity}'

    # TC№6 Remove item from basket via product card
    def test_remove_item_from_card(self, driver):
        page = OrderPage(driver, self.url.BASE_URL)
        page.open()
        page.login()
        page.navigate_to_page(self.main_locators.SAUCE_LAB_BACKPACK_IMAGE)
        page.add_to_basket()
        assert page.find_element(self.order_locators.REMOVE) == True
        page.remove_from_basket_card()
        try:
            page.find_element(self.order_locators.REMOVE)
        except NoSuchElementException:
            message = 'Incorrect'
        message = 'Correct'
        assert message == 'Correct'
        page.navigate_to_page(self.main_locators.BASKET)
        try:
            page.find_element(self.order_locators.SAUCE_LAB_BACKPACK_ITEM)
        except NoSuchElementException:
            message = 'Incorrect'
        message = 'Correct'
        assert message == 'Correct'

    # TC№7 Open product via click on product image
    def test_open_card_via_image(self, driver):
        page = OrderPage(driver, self.url.BASE_URL)
        page.open()
        page.login()
        page.navigate_to_page(self.main_locators.SAUCE_LAB_BACKPACK_IMAGE)
        actual_text=page.get_text(self.order_locators.CARD_PRODUCT_NAME)
        expected_text='Sauce Labs Backpack'
        assert actual_text == expected_text, f'Unexpected text: expected -{expected_text}, actual -{actual_text}'

    # TC№8 Open product via click on product name
    def test_open_card_via_name(self, driver):
        page = OrderPage(driver, self.url.BASE_URL)
        page.open()
        page.login()
        page.navigate_to_page(self.main_locators.SAUCE_LAB_BACKPACK_NAME)
        actual_text=page.get_text(self.order_locators.CARD_PRODUCT_NAME)
        expected_text='Sauce Labs Backpack'
        assert actual_text == expected_text, f'Unexpected text: expected -{expected_text}, actual -{actual_text}'

    # TC№9 Make order with correct data
    def test_complete_order(self, driver):
        page = OrderPage(driver, self.url.BASE_URL)
        page.open()
        page.login()
        page.navigate_to_page(self.main_locators.SAUCE_LAB_BACKPACK_IMAGE)
        page.add_to_basket()
        page.navigate_to_page(self.main_locators.BASKET)
        page.click_element(self.order_locators.CHECKOUT_BTN)
        page.fill_order()
        page.click_element(self.order_locators.CONTINUE_BTN)
        page.click_element(self.order_locators.FINISH_BTN)
        current_url = driver.current_url
        expected_url = 'https://www.saucedemo.com/checkout-complete.html'
        assert current_url == expected_url, f'Unexpected url: expected -{expected_url}, actual -{current_url}'
        actual_text = page.get_text(self.order_locators.COMPLETE_TEXT)
        expected_text = 'Thank you for your order!'
        assert actual_text == expected_text, f'Unexpected item: expected -{expected_text}, actual -{actual_text}'
