import pytest
from pages.basket_page import BasketPage
from pages.main_page import MainPage
from pages.login_page import LoginPage

link_main_page = "http://selenium1py.pythonanywhere.com/"


@pytest.mark.login_guest
class TestLoginFromMainPage():
    # Проверяет, что пользователь в роли гостя может перейти на страницу входа в систему
    def test_guest_can_go_to_login_page(self, browser):
        page = MainPage(browser, link_main_page)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()

    # Проверяет корзину с главной страницы
    def test_guest_cant_see_product_in_basket_opened_from_main_page(self, browser):
        page = MainPage(browser, link_main_page)
        page.open()
        page.go_to_basket_page()
        basket_page = BasketPage(browser, browser.current_url)
        basket_page.check_for_the_absence_of_products_in_the_basket()
