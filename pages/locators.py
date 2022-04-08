from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    INPUT_FIELD_REGISTRATION_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    INPUT_FIELD_REGISTRATION_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1")
    INPUT_FIELD_REGISTRATION_PASSWORD_REPEAT = (By.CSS_SELECTOR, "#id_registration-password2")
    BUTTON_REGISTRATION_SUBMIT = (By.NAME, "registration_submit")


class ProductPageLocators():
    PRODUCT_NAME = (By.CSS_SELECTOR, '.product_main h1')
    PRODUCT_PRISE = (By.CSS_SELECTOR, '.product_main p.price_color')
    BUTTON_ADD_TO_BASKET = (By.CLASS_NAME, "btn-add-to-basket")
    PRODUCT_DESCRIPTION = (By.CSS_SELECTOR, "#product_description+p")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alertinner strong")


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BUTTON_VIEW_THE_BASKET = (By.CSS_SELECTOR, ".btn-group a.btn-default")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators():
    EMPTY_BASKET_MESSAGE = (By.XPATH, '// p[contains(text(), "Your basket is empty")]')
    PRODUCT_IN_THE_BASKET = (By.CSS_SELECTOR, '.basket_summary')
