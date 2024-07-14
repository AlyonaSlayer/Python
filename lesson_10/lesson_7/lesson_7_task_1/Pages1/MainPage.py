from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Data import *  

class MainPage():
    """
            Этот класс позволяет заполнить данные на главной странице сайта
    """
    def __init__(self, driver):
        """
                Эта функция инициализирует веб драйвер
        """ 
        self._driver = driver
        self._driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
        self._driver.implicitly_wait(3)
        self._driver.maximize_window()
    
    def find_fields(self):
        """
                Эта функция находит элементы на странице
        """
        self._first_name = ('input[name="first-name"]')
        self._last_name = ('input[name="last-name"]')
        self._address = ('input[name="address"]')
        self._zip_code = ('input[name="zip-code"]')
        self._email = ('input[name="e-mail"]')
        self._phone = ('input[name="phone"]')
        self._city = ('input[name="city"]')
        self._country = ('input[name="country"]')
        self._job_postion = ('input[name="job-position"]')
        self._company = ('input[name="company"]')
    
    def fill_the_form(self):
        """
                Эта функция заполняет данные на странице
        """
        self._driver.find_element(By.CSS_SELECTOR,self._first_name).send_keys(first_name)
        self._driver.find_element(By.CSS_SELECTOR,self._last_name).send_keys(last_name)
        self._driver.find_element(By.CSS_SELECTOR,self._address).send_keys(address)
        self._driver.find_element(By.CSS_SELECTOR,self._zip_code).send_keys(zip_code)
        self._driver.find_element(By.CSS_SELECTOR,self._email).send_keys(email)
        self._driver.find_element(By.CSS_SELECTOR,self._phone).send_keys(phone_number)
        self._driver.find_element(By.CSS_SELECTOR,self._city).send_keys(city)
        self._driver.find_element(By.CSS_SELECTOR,self._country).send_keys(country)
        self._driver.find_element(By.CSS_SELECTOR,self._job_postion).send_keys(job_position)
        self._driver.find_element(By.CSS_SELECTOR,self._company).send_keys(company)
    
    def click_submit(self):
        """
                Эта функция нажимает на кнопку "Подтвердить"
        """
        WebDriverWait(self._driver, 40, 0.1).until(EC.element_to_be_clickable((By.TAG_NAME, "button"))).click()
    