from selenium.webdriver.common.by import By


class MainLocators:
    TITLE = (By.XPATH,'//span[@data-test="title"]')
    ADD_SAUCE_LAB_BACKPACK= (By.CSS_SELECTOR, 'button[data-test="add-to-cart-sauce-labs-backpack"]')
    REMOVE_SAUCE_LAB_BACKPACK = (By.CSS_SELECTOR, 'button[data-test="remove-sauce-labs-backpack"]')
    BASKET= (By.CSS_SELECTOR,'[data-test="shopping-cart-link"]')
    SAUCE_LAB_BACKPACK_IMAGE=(By.CSS_SELECTOR, '[data-test="inventory-item-sauce-labs-backpack-img"]')
    SAUCE_LAB_BACKPACK_NAME = (By.XPATH, '//div[text()="Sauce Labs Backpack"]')
