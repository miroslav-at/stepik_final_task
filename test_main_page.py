from pages.basket_page import BasketPage
from pages.locators import MainPageLocators
from pages.main_page import MainPage
from pages.login_page import LoginPage

link = "http://selenium1py.pythonanywhere.com/"

# Проверяет, что пользователь в роли гостя может перейти на страницу входа в систему
def test_guest_can_go_to_login_page(browser):
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

# Проверяет корзину с главной страницы
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    page = MainPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.check_for_the_absence_of_products_in_the_basket()