from selenium import webdriver
import pytest
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


@pytest.fixture
def driver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--incognito')
    chrome_options.add_argument('--window-size=1440,1080')
    driver = webdriver.Chrome(options=chrome_options)
    yield driver
    driver.quit()


@pytest.fixture
def add_item_from_catalog(driver, auth_positive):
    driver.find_element(By.XPATH, '//*[@id="inventory_container"]/div/div[1]/div[3]/button').click()
    t = driver.find_element(By.XPATH, '//*[@class="btn_secondary btn_inventory"').accessible_name
    assert t == 'REMOVE'
    driver.find_element(By.CLASS_NAME, 'shopping_cart_link').click()
    assert driver.current_url == 'https://www.saucedemo.com/v1/cart.html'
    item = driver.find_element(By.XPATH, '//*[@id="item_4_title_link"]/div').text
    assert item == 'Sauce Labs Backpack'
    assert driver.find_element(By.CLASS_NAME, 'cart_quantity').text == '1'
