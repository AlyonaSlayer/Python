from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

def task():
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
task()

from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
task()