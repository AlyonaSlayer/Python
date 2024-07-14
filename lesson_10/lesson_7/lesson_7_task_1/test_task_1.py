from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from Pages1.MainPage import MainPage
from Pages1.DataFild import DataFild
from Data import *
import allure
@allure.epic("7 урок")
@allure.severity("blocker")
@allure.id("Тест-1")
@allure.description("Заполнить данные на главной странице и собрать информацию со второй странцицы")
@allure.title("Задание 1")
def test_task_1():
    with allure.step("Инициализировать вебдрайвер"):
        driver_chrom = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        main_page = MainPage(driver_chrom)
        data_fild = DataFild(driver_chrom)
    with allure.step("Найти элементы на главной странице"):    
        main_page.find_fields()
    with allure.step("Заполнить данные на главной странице"):
        main_page.fill_the_form()
    with allure.step("Нажать на кнопку 'Продолжить'"):
        main_page.click_submit()
    with allure.step("Найти элементы со второй страницы"):
        data_fild.find_fields()
    with allure.step("Проверить элемент Zip-Code на второй странице"):
        assert "alert-danger" in data_fild.get_class_zip_code()
    with allure.step("Проверить элемент First-Name на второй странице"):
        assert "alert-success" in data_fild.get_class_first_name()
    with allure.step("Проверить элемент Last-Name на второй странице"):    
        assert "alert-success" in data_fild.get_class_last_name()
    with allure.step("Проверить элемент Address на второй странице"):
        assert "alert-success" in data_fild.get_class_address()
    with allure.step("Проверить элемент City на второй странице"):
        assert "alert-success" in data_fild.get_class_city()
    with allure.step("Проверить элемент Country на второй странице"):
        assert "alert-success" in data_fild.get_class_country()
    with allure.step("Проверить элемент Email на второй странице"):
        assert "alert-success" in data_fild.get_class_email()
    with allure.step("Проверить элемент Phone на второй странице"):
        assert "alert-success" in data_fild.get_class_phone_number()
    with allure.step("Проверить элемент Job-Position на второй странице"):
        assert "alert-success" in data_fild.get_class_job_position()
    with allure.step("Проверить элемент Company на второй странице"):
        assert "alert-success" in data_fild.get_class_company()
    driver_chrom.quit()

