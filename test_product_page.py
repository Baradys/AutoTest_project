from .pages.base_page import BasePage
from .pages.product_page import PageObject
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
import time
import pytest

test_link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


@pytest.mark.registration
class TestUserAddToBasketFromProductPage:

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, browser):
        register_page = PageObject(browser, test_link)
        register_page.open()
        register_page.go_to_login_page()
        register_page = LoginPage(browser, browser.current_url)
        email = str(time.time())
        LoginPage.register_new_user(register_page, f"{email}x@mail.ru", "9284391048NN")
        BasePage.should_be_authorized_user(register_page)

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        page = PageObject(browser, test_link)
        page.open()
        page.should_not_be_success_message()
        page.add_to_basket()
        page.check_price()
        page.check_name()

    def test_user_cant_see_success_message(self, browser):
        page = PageObject(browser, test_link)
        page.open()
        page.should_not_be_success_message()


@pytest.mark.need_review
@pytest.mark.parametrize('link', [i if i != 7 else pytest.param(7, marks=pytest.mark.xfail) for i in range(10)])
def test_guest_can_add_product_to_basket(browser, link):
    page = PageObject(browser, f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{link}')
    page.open()
    page.should_not_be_success_message()
    page.add_to_basket()
    BasePage.solve_quiz_and_get_code(page)
    page.check_price()
    page.check_name()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    page = PageObject(browser, test_link)
    page.open()
    page.go_to_login_page()
    page = LoginPage(browser, browser.current_url)
    LoginPage.should_be_login_url(page)


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = PageObject(browser, test_link)
    page.open()
    page.add_to_basket()
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    page = PageObject(browser, test_link)
    page.open()
    page.should_not_be_success_message()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = PageObject(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = PageObject(browser, test_link)
    page.open()
    page.add_to_basket()
    page.should_disappeared_success_message()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = PageObject(browser, test_link)
    page.open()
    page.go_to_basket_page()
    page = BasketPage(browser, browser.current_url)
    BasketPage.empty_basket(page)
    BasketPage.check_message(page)
