from .base_page import BasePage
from .locators import LoginPageLocators
from faker import Faker


class LoginPage(BasePage):
    # Проверяет страницу логина
    def should_be_login_page(self):
        # Проверяет корректность url-адреса
        self.should_be_login_url()
        # Проверяет наличие формы логина на странице
        self.should_be_login_form()
        # Проверяет наличие формы регистрации на странице
        self.should_be_register_form()

    def should_be_login_url(self):
        assert 'login' in self.browser.current_url, f"Invalid URL-address, expected 'login' to be substring of '{self.browser.current_url}'"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"

    # Регистрирует пользователя
    def register_new_user(self):
        faker = Faker()
        email = faker.email()
        password = "stepic1234"
        self.browser.find_element(*LoginPageLocators.INPUT_FIELD_REGISTRATION_EMAIL).send_keys(email)
        self.browser.find_element(*LoginPageLocators.INPUT_FIELD_REGISTRATION_PASSWORD).send_keys(password)
        self.browser.find_element(*LoginPageLocators.INPUT_FIELD_REGISTRATION_PASSWORD_REPEAT).send_keys(password)
        self.browser.find_element(*LoginPageLocators.BUTTON_REGISTRATION_SUBMIT).click()
