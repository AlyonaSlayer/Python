from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
driver_chrome = webdriver.Chrome()
driver_firefox = webdriver.Firefox()
def task(driver):
    driver.get("http://the-internet.herokuapp.com/add_remove_elements/")
    surch_input = driver.find_element(By.CSS_SELECTOR, 'button[onclick="addElement()"]')
    for n in range(5):
        surch_input.click()
    sleep(2)
    delete = driver.find_elements(By.CSS_SELECTOR, "button.added-manually")
    print(len(delete))
    driver.quit()

task(driver_chrome)
task(driver_firefox)