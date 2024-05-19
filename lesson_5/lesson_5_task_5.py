from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

def task():
    driver.get("http://the-internet.herokuapp.com/inputs")
    surch_input = driver.find_element(By.CSS_SELECTOR, 'input[type="number"]')
    surch_input.send_keys("1000")
    sleep(2)
    surch_input.clear()
    surch_input.send_keys("999")
    sleep(2)
    driver.quit()
task()

from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
task()
