from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure
class MainPage:
    """
            Этот класс взаимодействует с сайтом "Калькулятор"
    """
    def __init__(self, driver):
        """
                Эта функция создает вебдрайвер
        """
        self._driver = driver
        self._driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
        self._driver.implicitly_wait(10)
        self._driver.maximize_window()

    @allure.step("Найти окно с устанавливаемым временем и заменить его")
    def fill_deley(self, sec: int):
        """
                Эта функция находит окно с устанавливаемым временем и меняет его
        """
        self.sec = sec
        deley = self._driver.find_element(By.CSS_SELECTOR, "#delay")
        deley.clear()
        deley.send_keys(str(self.sec))
    @allure.step("Ввести данные уравнения в калькулятор")    
    def fill_the_form(self, keys_calculator: str):
        """
                Эта функция нажимает на кнопки в калькуляторе
        """
        for val in keys_calculator:
            self._driver.find_element(By.XPATH, f'//span[text()="{val}"]').click()
    @allure.step("Получить результат через указанное время")
    def get_total(self) -> str:
        """
                Эта функция ждет указанное время и возвращает текст ответа
        """
        WebDriverWait(self._driver, (self.sec+1)).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "div.screen"), "15"))
        return self._driver.find_element(By.CSS_SELECTOR, "div.screen").text