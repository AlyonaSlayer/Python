from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from Pages.MainPage import MainPage

def test_task_2():
    driver_chrom = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    main_page = MainPage(driver_chrom)
    main_page.fill_deley("45")
    main_page.fill_the_form()
    assert "15" in main_page.get_total()
