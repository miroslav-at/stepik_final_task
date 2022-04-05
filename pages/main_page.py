from .base_page import BasePage
from .locators import MainPageLocators


# Представляет главную страницу
class MainPage(BasePage):
    # Переходит на страницу логина
    def go_to_login_page(self):
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()

    # Проверяет наличие элемента на странице
    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"
