from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
driver_chrome = webdriver.Chrome()
driver_firefox = webdriver.Firefox()

def task(driver):
    driver.get("http://the-internet.herokuapp.com/entry_ad")
    sleep(1)
    driver.find_element(By.CSS_SELECTOR, 'div.modal-footer p').click
    sleep(2)
    driver.quit()
task(driver_chrome)
task(driver_firefox)