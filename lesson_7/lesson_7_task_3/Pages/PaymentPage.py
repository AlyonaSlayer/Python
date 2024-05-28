from selenium.webdriver.common.by import By

class PaymentPage():
    def __init__(self, driver):
        self._driver = driver

    def fill_the_form(self):
        self._driver.find_element(By.ID, 'first-name').send_keys("Alyona")
        self._driver.find_element(By.ID, 'last-name').send_keys("Birukova")
        self._driver.find_element(By.ID, 'postal-code').send_keys("148264")
        self._driver.find_element(By.ID, 'continue').click()