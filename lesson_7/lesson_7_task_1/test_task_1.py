from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from Pages.MainPage import MainPage
from Pages.DataFild import DataFild
from Data import *
from selenium.webdriver.common.by import By
def test_task_1():
    driver_chrom = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    main_page = MainPage(driver_chrom)
    data_fild = DataFild(driver_chrom)
    main_page.find_fields()
    main_page.fill_the_form()
    main_page.click_submit()
    data_fild.find_fields()
    
    
    assert "alert-danger" in data_fild.get_class_zip_code()
    assert "alert-success" in data_fild.get_class_first_name()
    assert "alert-success" in data_fild.get_class_last_name()
    assert "alert-success" in data_fild.get_class_address()
    assert "alert-success" in data_fild.get_class_city()
    assert "alert-success" in data_fild.get_class_country()
    assert "alert-success" in data_fild.get_class_email()
    assert "alert-success" in data_fild.get_class_phone_number()
    assert "alert-success" in data_fild.get_class_job_position()
    assert "alert-success" in data_fild.get_class_company()

    driver_chrom.quit()

