from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
driver_chrome = webdriver.Chrome()
driver_firefox = webdriver.Firefox()
def task(driver):
    driver.get("http://the-internet.herokuapp.com/inputs")
    surch_input = driver.find_element(By.CSS_SELECTOR, 'input[type="number"]')
    surch_input.send_keys("1000")
    sleep(2)
    surch_input.clear()
    surch_input.send_keys("999")
    sleep(2)
    driver.quit()
task(driver_chrome)
task(driver_firefox)
