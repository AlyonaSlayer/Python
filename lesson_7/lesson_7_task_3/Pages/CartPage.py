from selenium.webdriver.common.by import By

class CartPage():
    def __init__(self, driver):
        self._driver = driver

    def click_checkout(self):
        self._driver.find_element(By.ID, 'checkout').click()

    def fill_the_form(self):
        self._driver.find_element(By.ID, 'first-name').send_keys("Alyona")
        self._driver.find_element(By.ID, 'last-name').send_keys("Birukova")
        self._driver.find_element(By.ID, 'postal-code').send_keys("148264")
        self._driver.find_element(By.ID, 'continue').click()

    def total_price(self):
        total_price = self._driver.find_element(By.CLASS_NAME, 'summary_total_label').text
        return total_price
