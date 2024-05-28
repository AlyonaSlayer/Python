from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from Pages.AuthorizationPage import AuthorizationPage
from Pages.MainPage import MainPage
from Pages.CartPage import CartPage
from Pages.PaymentPage import PaymentPage
from Pages.TotalPrice import TotalPrice


def test_task_3():
    driver_chrom = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    user = AuthorizationPage(driver_chrom)
    main_page = MainPage(driver_chrom)
    cart_page = CartPage(driver_chrom)
    payment_page = PaymentPage(driver_chrom)
    total = TotalPrice(driver_chrom)


    user.authorization()
    main_page.add_item()
    main_page.switch_to_card()
    cart_page.click_checkout()
    payment_page.fill_the_form()
    total_price = total.total_price()
    driver_chrom.quit()
    assert total_price == "Total: $58.29"