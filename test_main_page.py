import pytest

from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage

test_link = "http://selenium1py.pythonanywhere.com/"


@pytest.mark.login_guest
class TestLoginFromMainPage:
    def test_guest_can_go_to_login_page(self, browser):
        page = MainPage(browser,
                        test_link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page.open()  # открываем страницу
        page.go_to_login_page()  # Переходим на страницу login_page
        login_page = LoginPage(browser, browser.current_url)  # выполняем метод страницы — переходим на страницу логина
        login_page.should_be_login_page()

    def test_guest_should_see_login_link(self, browser):
        page = MainPage(browser, test_link)
        page.open()
        page.should_be_login_link()  # проверяем наличие кнопки


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    page = MainPage(browser, test_link)
    page.open()
    page.go_to_basket_page()
    page = BasketPage(browser, browser.current_url)
    BasketPage.empty_basket(page)
    BasketPage.check_message(page)


def test_guest_can_register(browser):
    page = MainPage(browser, test_link)
    page.open()
    page.go_to_login_page()
    page = LoginPage(browser, browser.current_url)
    LoginPage.register_new_user(page, "Baradys@mail.ru", "9284391048NN")
