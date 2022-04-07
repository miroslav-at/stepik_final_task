import pytest
from pages.product_page import ProductPage
from pages.login_page import LoginPage

link_product_page = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
link_product_page_promo = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"

xfile = 7
product_base_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
links = [f"{product_base_link}/?promo=offer{number}" for number in range(10) if number != xfile]
# Страница с багом
xlink = pytest.param(f"{product_base_link}/?promo=offer{xfile}", marks=pytest.mark.xfail(reason="mistake on page"))
# Добавление ссылки на страницу с багом перед указанным индексом
links.insert(xfile, xlink)


@pytest.mark.parametrize('link', links)
# Проверяет добавление в корзину со страницы товара
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()


@pytest.mark.xfail(reason="fixing this bug right now")
# Проверяет отсутствие сообщения об успешном завершении после добавления товара в корзину
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link_product_page_promo)
    page.open()
    page.add_product_to_basket()
    page.check_success_message_after_adding_product_to_basket()


# Проверяет отсутствие сообщения об успехе до добавления товара в корзину
def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, link_product_page_promo)
    page.open()
    page.check_for_missing_success_message()


@pytest.mark.xfail(reason="fixing this bug right now")
# Проверяет, что сообщение исчезло после добавления товара в корзину
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link_product_page_promo)
    page.open()
    page.add_product_to_basket()
    page.check_message_after_adding_product_to_basket()


# Проверяет наличие ссылки перехода на страницу логина со страницы товара
def test_guest_should_see_login_link_on_product_page(browser):
    page = ProductPage(browser, link_product_page)
    page.open()
    page.should_be_login_link()

# Переходит на страницу логина
def test_guest_can_go_to_login_page_from_product_page(browser):
    page = ProductPage(browser, link_product_page)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()
