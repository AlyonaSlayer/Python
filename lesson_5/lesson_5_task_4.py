from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

def task():
    driver.get("http://the-internet.herokuapp.com/entry_ad")
    sleep(1)
    driver.find_element(By.CSS_SELECTOR, 'div.modal-footer p').click
    sleep(2)
    driver.quit()
task()

from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
task()