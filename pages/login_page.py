from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # Проверка корректности url-адреса
        assert 'login' in self.browser.current_url, f"Invalid URL-address, expected 'login' to be substring of '{self.browser.current_url}'"

    def should_be_login_form(self):
        # Проверка на наличие формы логина на странице
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        # Проверка на наличие формы регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"
