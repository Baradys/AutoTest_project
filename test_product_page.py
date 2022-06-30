from .pages.base_page import BasePage
from .pages.product_page import PageObject
import pytest

test_link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


@pytest.mark.parametrize('link', [i if i != 7 else pytest.param(7, marks=pytest.mark.xfail) for i in range(10)])
def test_guest_can_add_product_to_basket(browser, link):
    page = PageObject(browser, f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{link}')
    page.open()
    page.should_not_be_success_message()
    page.add_to_basket()
    BasePage.solve_quiz_and_get_code(page)
    page.check_price()
    page.check_name()


def test_guest_can_go_to_login_page_from_product_page(browser):
    page = PageObject(browser, test_link)
    page.open()
    page.go_to_login_page()
    assert page.url.find('login', -1), 'Wrong url'

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


def test_message_disappeared_after_adding_product_to_basket(browser):
    page = PageObject(browser, test_link)
    page.open()
    page.add_to_basket()
    page.should_disappeared_success_message()
