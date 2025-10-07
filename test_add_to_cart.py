from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pytest

def test_add_to_cart():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    driver.find_element(By.CSS_SELECTOR, "button.btn_primary.btn_inventory").click()
    badge = driver.find_element(By.CSS_SELECTOR, "a.shopping_cart_link").text
    assert badge == "1"
    driver.quit()
