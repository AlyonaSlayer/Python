from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

def task():
    driver.get("http://the-internet.herokuapp.com/add_remove_elements/")
    surch_input = driver.find_element(By.CSS_SELECTOR, 'button[onclick="addElement()"]')
    for n in range(5):
        surch_input.click()
    sleep(2)
    delete = driver.find_elements(By.CSS_SELECTOR, "button.added-manually")
    print(len(delete))
    driver.quit()
task()

from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
task()