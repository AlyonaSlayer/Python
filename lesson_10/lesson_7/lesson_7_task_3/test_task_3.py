from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from Pages3.MainPage import MainPage
from Pages3.CartPage import CartPage
import allure

@allure.epic("7 урок")
@allure.severity("blocker")
@allure.id("Тест 3")
@allure.title("Задание 3")
@allure.description("Проверить работу сайта 'Магазин одежды'")
def test_task_3():
    with allure.step("Инициализировать драйвер"):
        driver_chrom = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        main_page = MainPage(driver_chrom)
        cart_page = CartPage(driver_chrom)

    main_page.authorization("standard_user", "secret_sauce")
    main_page.add_item()
    main_page.switch_to_card()
    cart_page.click_checkout()
    cart_page.fill_the_form("Alyona","Birukova","148264")
    total_price = cart_page.total_price()
    driver_chrom.quit()
    with allure.step("Проверить сумму заказа"):
        assert total_price == "Total: $58.29"