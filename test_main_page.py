from pages.locators import MainPageLocators
from pages.main_page import MainPage
from pages.login_page import LoginPage


# Проверяет, что пользователь в роли гостя может перейти на страницу входа в систему
def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    # инициализация Page Object, передача в конструктор экземпляра драйвера и url-адреса
    page = MainPage(browser, link)
    # открывает страницу
    page.open()
    # выполняет метод страницы — переходит на страницу логина
    page.go_to_login_page()
    # Инициализация страницы логина
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


# Переходит на страницу логина
def go_to_login_page(self):
    link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
    link.click()
    # return LoginPage(browser=self.browser, url=self.browser.current_url)
