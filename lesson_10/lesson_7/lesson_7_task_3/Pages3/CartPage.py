from selenium.webdriver.common.by import By
import allure
@allure.feature("Страница Корзины")
class CartPage():
    """
            Этот класс взаимодействует со страницей корзины
    """
    def __init__(self, driver):
        """
                Эта функция инициализирует вебдрайвер
        """
        self._driver = driver
    @allure.step("Нажать на кнопку оплатить на страницы корзины")
    def click_checkout(self):
        """
                Эта функция нажимает на кнопку "Оплатить"
        """
        self._driver.find_element(By.ID, 'checkout').click()
    @allure.step("Заполнить данные для оформления заказа и нажать продолжить")
    def fill_the_form(self, first_name:str, last_name:str, postal_code:str):
        """
                Эта функция заполняет форму для оформления заказа
        """
        self._driver.find_element(By.ID, 'first-name').send_keys(first_name)
        self._driver.find_element(By.ID, 'last-name').send_keys(last_name)
        self._driver.find_element(By.ID, 'postal-code').send_keys(postal_code)
        self._driver.find_element(By.ID, 'continue').click()
    @allure.step("Получить сумму заказа")
    def total_price(self) -> str:
        """
                Эта функция возвращает сумму заказа
        """
        total_price = self._driver.find_element(By.CLASS_NAME, 'summary_total_label').text
        return total_price
