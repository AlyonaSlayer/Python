from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from Pages2.MainPage import MainPage
import allure

@allure.epic("Урок 7")
@allure.id("Тест 2")
@allure.severity("blocker")
@allure.title("Задание 2")
@allure.description("Проверить работу сайта Калькулятор")
def test_task_2():
    with allure.step("Инициализировать вебдрайвер"):
        driver_chrom = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        main_page = MainPage(driver_chrom)
    main_page.fill_deley(45)
    main_page.fill_the_form('C7+8=')
    with allure.step("Проверить итоговое значение"):
        assert '15' in main_page.get_total()

