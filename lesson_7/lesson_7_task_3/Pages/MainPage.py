from selenium.webdriver.common.by import By

class MainPage():
    def __init__(self, driver):
        self._driver = driver
        self._driver.get("https://www.saucedemo.com")
        self._driver.implicitly_wait(4)
        self._driver.maximize_window()

    def authorization(self):
        self._driver.find_element(By.ID, 'user-name').send_keys("standard_user")
        self._driver.find_element(By.ID, 'password').send_keys("secret_sauce")
        self._driver.find_element(By.ID, 'login-button').click()

    def add_item(self):
        self._driver.find_element(By.ID, 'add-to-cart-sauce-labs-backpack').click()
        self._driver.find_element(By.ID, 'add-to-cart-sauce-labs-bolt-t-shirt').click()
        self._driver.find_element(By.ID, 'add-to-cart-sauce-labs-onesie').click()
    
    def switch_to_card(self):
        self._driver.find_element(By.ID, 'shopping_cart_container').click()