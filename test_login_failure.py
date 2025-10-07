from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

def test_login_failure():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    
    driver.find_element(By.ID, "user-name").send_keys("locked_out_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    
    error = driver.find_element(By.CSS_SELECTOR, "h3[data-test='error']").text
    assert "locked out" in error.lower()
    driver.quit()
