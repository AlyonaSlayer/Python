from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from Pages.MainPage import MainPage
from Pages.CartPage import CartPage



def test_task_3():
    driver_chrom = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    main_page = MainPage(driver_chrom)
    cart_page = CartPage(driver_chrom)


    main_page.authorization()
    main_page.add_item()
    main_page.switch_to_card()
    cart_page.click_checkout()
    cart_page.fill_the_form()
    total_price = cart_page.total_price()
    driver_chrom.quit()
    assert total_price == "Total: $58.29"