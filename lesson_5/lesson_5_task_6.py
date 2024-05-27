from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
driver_chrome = webdriver.Chrome()
driver_firefox = webdriver.Firefox()
def task(driver):
    driver.get("http://the-internet.herokuapp.com/login")
    surch_input1 = driver.find_element(By.CSS_SELECTOR, "input#username")
    surch_input1.send_keys("tomsmith")
    sleep(1)
    surch_input2 = driver.find_element(By.CSS_SELECTOR, "input#password")
    surch_input2.send_keys("SuperSecretPassword!")
    sleep(1)
    surch_input3 = driver.find_element(By.CSS_SELECTOR, "button.radius")
    surch_input3.click()
    sleep(2)
    driver.quit()
task(driver_chrome)
task(driver_firefox)