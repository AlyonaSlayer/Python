from selenium.webdriver.common.by import By

class TotalPrice():
    def __init__(self, driver):
        self._driver = driver

    def total_price(self):
        total_price = self._driver.find_element(By.CLASS_NAME, 'summary_total_label').text
        return total_price