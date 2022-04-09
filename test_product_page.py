from .pages.main_page import MainPage
import time
from .pages.product_page import ProductPage


def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page = MainPage(browser, link)
    page.open()                      # открываем страницу
    # выполняем метод страницы — переходим на страницу логина
    product_page = ProductPage(browser, browser.current_url)
    time.sleep(5)
    product_page.put_to_basket()
    product_page.should_be_in_basket()
    product_page.the_price_should_be_equal()


