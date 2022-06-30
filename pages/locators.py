from selenium.webdriver.common.by import By


class MainPageLocators:
    pass


class LoginPageLocators:
    REGISTRATION_FORM = (By.ID, 'register_form')
    LOGIN_FORM = (By.ID, 'login_form')


class ProductPageLocators:
    ADD_BASKET_BUTTON = (By.ID, 'add_to_basket_form')
    REVIEW_BUTTON = (By.ID, 'write_review')
    VIEW_BASKET_BUTTON = (By.CSS_SELECTOR, 'span > a')
    PRODUCT_PRICE = (By.CSS_SELECTOR, 'p.price_color')
    CART_VALUE = (By.CSS_SELECTOR, '.alertinner p strong')
    PRODUCT_NAME = (By.CSS_SELECTOR, 'div h1')
    MESSAGE_NAME = (By.CSS_SELECTOR, '.alertinner strong')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "[id='messages'] div")


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")