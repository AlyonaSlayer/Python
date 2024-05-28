from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

def test_3():
    driver.get("https://www.saucedemo.com")
    driver.maximize_window()
    driver.find_element(By.ID, 'user-name').send_keys("standard_user")
    driver.find_element(By.ID, 'password').send_keys("secret_sauce")
    driver.find_element(By.ID, 'login-button').click()
    driver.find_element(By.ID, 'add-to-cart-sauce-labs-backpack').click()
    driver.find_element(By.ID, 'add-to-cart-sauce-labs-bolt-t-shirt').click()
    driver.find_element(By.ID, 'add-to-cart-sauce-labs-onesie').click()
    driver.find_element(By.ID, 'shopping_cart_container').click()
    driver.find_element(By.ID, 'checkout').click()
    driver.find_element(By.ID, 'first-name').send_keys("Alyona")
    driver.find_element(By.ID, 'last-name').send_keys("Birukova")
    driver.find_element(By.ID, 'postal-code').send_keys("148264")
    driver.find_element(By.ID, 'continue').click()
    total_price = driver.find_element(By.CLASS_NAME, 'summary_total_label').text
    driver.quit()
    assert total_price == "Total: $58.29"
    
    



    
    

