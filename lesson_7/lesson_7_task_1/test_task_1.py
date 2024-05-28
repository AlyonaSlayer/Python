from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from Pages.MainPage import MainPage


def test_task_1():
    driver_chrom = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    main_page = MainPage(driver_chrom)
    main_page.fill_the_form()
    main_page.click_submit()
    assert "alert-danger" in driver_chrom.find_element(By.ID, "zip-code").get_attribute("class")
    assert "alert-success" in driver_chrom.find_element(By.ID, "first-name").get_attribute("class")
    assert "alert-success" in driver_chrom.find_element(By.ID, "last-name").get_attribute("class")
    assert "alert-success" in driver_chrom.find_element(By.ID, "address").get_attribute("class")
    assert "alert-success" in driver_chrom.find_element(By.ID, "city").get_attribute("class")
    assert "alert-success" in driver_chrom.find_element(By.ID, "country").get_attribute("class")
    assert "alert-success" in driver_chrom.find_element(By.ID, "e-mail").get_attribute("class")
    assert "alert-success" in driver_chrom.find_element(By.ID, "phone").get_attribute("class")
    assert "alert-success" in driver_chrom.find_element(By.ID, "job-position").get_attribute("class")
    assert "alert-success" in driver_chrom.find_element(By.ID, "company").get_attribute("class")
    driver_chrom.quit()

