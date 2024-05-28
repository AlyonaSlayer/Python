from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
driver_chrome = webdriver.Chrome()
driver_firefox = webdriver.Firefox()
def task(driver):
    for n in range(3):
        driver.get("http://uitestingplayground.com/dynamicid")
        surch_input = driver.find_element(By.CSS_SELECTOR, 'button.btn.btn-primary')
        surch_input.click()
        sleep(2)
    driver.quit()
    print("finish")

task(driver_chrome)
task(driver_firefox)