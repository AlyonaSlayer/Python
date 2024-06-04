from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MainPage:
    def __init__(self, driver):
        self._driver = driver
        self._driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
        self._driver.implicitly_wait(4)
        self._driver.maximize_window()

    def fill_deley(self, sec):
        deley = self._driver.find_element(By.CSS_SELECTOR, "#delay")
        deley.clear()
        deley.send_keys(sec)

    def fill_the_form(self, keys_calculator):
        for val in keys_calculator:
            self._driver.find_element(By.XPATH, f'//span[text()="{val}"]').click()
    
    def get_total(self):
        WebDriverWait(self._driver, 46).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "div.screen"), "15"))
        return self._driver.find_element(By.CSS_SELECTOR, "div.screen").text
    