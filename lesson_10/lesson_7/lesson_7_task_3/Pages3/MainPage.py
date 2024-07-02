from selenium.webdriver.common.by import By
import allure
@allure.feature("Главная страница")
class MainPage():
    """
            "Этот класс взаимодействет с главной страницей сайта
    """
    def __init__(self, driver):
        """
                Эта функция инициализирует вебдрайвер
        """
        self._driver = driver
        self._driver.get("https://www.saucedemo.com")
        self._driver.implicitly_wait(4)
        self._driver.maximize_window()
    @allure.step("Авторизоваться на странице авторизации")
    def authorization(self, user:str, password:str):
        """
                Эта функция заполняет форму авторизации (User и Password) и авторизуется на сайте
        """
        self._driver.find_element(By.ID, 'user-name').send_keys(user)
        self._driver.find_element(By.ID, 'password').send_keys(password)
        self._driver.find_element(By.ID, 'login-button').click()
    @allure.step("Найти товары на странице и положить их в корзину")
    def add_item(self):
        """
                Эта функция находит на сайте товары и кладет их в корзину
        """
        self._driver.find_element(By.ID, 'add-to-cart-sauce-labs-backpack').click()
        self._driver.find_element(By.ID, 'add-to-cart-sauce-labs-bolt-t-shirt').click()
        self._driver.find_element(By.ID, 'add-to-cart-sauce-labs-onesie').click()
    @allure.step("Перейти в корзину, нажав соответсвующую кнопку")
    def switch_to_card(self):
        """
                Эта функция нажимает на кнопку "Перейти в корзину"
        """
        self._driver.find_element(By.ID, 'shopping_cart_container').click()