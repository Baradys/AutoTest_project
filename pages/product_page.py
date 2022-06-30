from .base_page import BasePage
from .locators import ProductPageLocators


class PageObject(BasePage):
    def should_be_object_page(self):
        self.should_be_item_url()
        self.should_be_review_button()
        self.should_be_add_to_basket_button()
        self.should_be_basket_link()

    def should_be_item_url(self):
        assert self.url.find('catalogue', -1), 'Wrong URL'

    def should_be_review_button(self):
        assert self.is_element_present(*ProductPageLocators.REVIEW_BUTTON)

    def should_be_add_to_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_BASKET_BUTTON)

    def should_be_basket_link(self):
        assert self.is_element_present(*ProductPageLocators.VIEW_BASKET_BUTTON)

    def add_to_basket(self):
        self.browser.find_element(*ProductPageLocators.ADD_BASKET_BUTTON).click()

    def check_name(self):
        assert self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text \
               == self.browser.find_element(*ProductPageLocators.MESSAGE_NAME).text, 'Wrong name'

    def check_price(self):
        assert self.browser.find_element(*ProductPageLocators.CART_VALUE).text \
               == self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text, 'Wrong price'

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_disappeared_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should be disappeared"
