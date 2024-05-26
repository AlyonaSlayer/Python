from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

def task():
    for n in range(3):
        driver.get("http://uitestingplayground.com/dynamicid")
        surch_input = driver.find_element(By.CSS_SELECTOR, 'button.btn.btn-primary')
        surch_input.click()
        sleep(2)
    driver.quit()
    print("finish")

task()

from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
task()