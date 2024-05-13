from selenium.webdriver.common.by import By


class OrderLocators:
    SAUCE_LAB_BACKPACK_ITEM = (By.CSS_SELECTOR, '[data-test="inventory-item-name"]')
    CART_QUANTITY = (By.CSS_SELECTOR, '[data-test="item-quantity"]')
    ADD_TO_CART = (By.CSS_SELECTOR, '[data-test="add-to-cart"]')
    REMOVE = (By.CSS_SELECTOR, '[data-test="remove"]')
    CARD_PRODUCT_NAME = (By.CSS_SELECTOR, '[data-test="inventory-item-name"]')
    CHECKOUT_BTN = (By.CSS_SELECTOR, '[data-test="checkout"]')
    CONTINUE_BTN = (By.CSS_SELECTOR, '[data-test="continue"]')

    FIRSTNAME = (By.CSS_SELECTOR, '[data-test="firstName"]')
    LASTNAME = (By.CSS_SELECTOR, '[data-test="lastName"]')
    POSTALCODE = (By.CSS_SELECTOR, '[data-test="postalCode"]')
    FINISH_BTN = (By.CSS_SELECTOR, '[data-test="finish"]')
    COMPLETE_TEXT = (By.CSS_SELECTOR, '[data-test="complete-header"]')
