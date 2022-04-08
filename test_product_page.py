import pytest
from pages.basket_page import BasketPage
from pages.product_page import ProductPage
from pages.login_page import LoginPage

link_login_page = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
link_product_page = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
link_product_page_promo = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"

xfile = 7
links = [f"{link_product_page}/?promo=offer{number}" for number in range(10) if number != xfile]
# Страница с багом
xlink = pytest.param(f"{link_product_page}/?promo=offer{xfile}", marks=pytest.mark.xfail(reason="mistake on page"))
# Добавление ссылки на страницу с багом перед указанным индексом
links.insert(xfile, xlink)


@pytest.mark.login
class TestLoginFromProductPage():
    @pytest.mark.parametrize('link', links)
    # Проверяет добавление в корзину со страницы товара
    def test_guest_can_add_product_to_basket(self, browser, link):
        page = ProductPage(browser, link)
        page.open()
        page.add_product_to_basket()

    @pytest.mark.xfail(reason="fixing this bug right now")
    # Проверяет отсутствие сообщения об успешном завершении после добавления товара в корзину
    def test_guest_cant_see_success_message_after_adding_product_to_basket(self, browser):
        page = ProductPage(browser, link_product_page_promo)
        page.open()
        page.add_product_to_basket()
        page.check_success_message_after_adding_product_to_basket()

    # Проверяет отсутствие сообщения об успехе до добавления товара в корзину
    def test_guest_cant_see_success_message(self, browser):
        page = ProductPage(browser, link_product_page_promo)
        page.open()
        page.check_for_missing_success_message()

    @pytest.mark.xfail(reason="fixing this bug right now")
    # Проверяет, что сообщение исчезло после добавления товара в корзину
    def test_message_disappeared_after_adding_product_to_basket(self, browser):
        page = ProductPage(browser, link_product_page_promo)
        page.open()
        page.add_product_to_basket()
        page.check_message_after_adding_product_to_basket()

    # Проверяет наличие ссылки перехода на страницу логина со страницы товара
    def test_guest_should_see_login_link_on_product_page(self, browser):
        page = ProductPage(browser, link_product_page)
        page.open()
        page.should_be_login_link()

    # Переходит на страницу логина
    def test_guest_can_go_to_login_page_from_product_page(self, browser):
        page = ProductPage(browser, link_product_page)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()

    # Проверяет корзину со страницы товара
    def test_guest_cant_see_product_in_basket_opened_from_product_page(self, browser):
        page = ProductPage(browser, link_product_page)
        page.open()
        page.go_to_basket_page()
        basket_page = BasketPage(browser, browser.current_url)
        basket_page.check_for_the_absence_of_products_in_the_basket()


@pytest.mark.user
class TestUserAddToBasketFromProductPage():

    @pytest.fixture(scope="function", autouse=True)
    # Регистрация пользователя
    def setup(self, browser):
        login_page = LoginPage(browser, link_login_page)
        login_page.open()
        login_page.register_new_user()
        login_page.should_be_authorized_user()

    # Проверяет отсутствие сообщения об успехе до добавления товара в корзину
    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(browser, link_product_page)
        page.open()
        page.check_for_missing_success_message()

    # Проверяет корзину со страницы товара
    def test_user_cant_see_product_in_basket_opened_from_product_page(self, browser):
        page = ProductPage(browser, link_product_page)
        page.open()
        page.go_to_basket_page()
        basket_page = BasketPage(browser, browser.current_url)
        basket_page.check_for_the_absence_of_products_in_the_basket()
