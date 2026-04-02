import pytest
from selenium.webdriver.common.by import By
import time  # <--- Agrega esto al inicio

def test_h1_login_exitoso(driver):
    driver.get("https://www.saucedemo.com/")
    time.sleep(2) # Pausa para el video
    
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    time.sleep(2)
    
    driver.find_element(By.ID, "login-button").click()
    time.sleep(2)
    
    driver.save_screenshot("1_login_exitoso.png")
    assert "Products" in driver.page_source