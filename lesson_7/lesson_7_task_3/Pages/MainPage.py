from selenium.webdriver.common.by import By

class MainPage():
    def __init__(self, driver):
        self._driver = driver

    def add_item(self):
        self._driver.find_element(By.ID, 'add-to-cart-sauce-labs-backpack').click()
        self._driver.find_element(By.ID, 'add-to-cart-sauce-labs-bolt-t-shirt').click()
        self._driver.find_element(By.ID, 'add-to-cart-sauce-labs-onesie').click()
    
    def switch_to_card(self):
        self._driver.find_element(By.ID, 'shopping_cart_container').click()