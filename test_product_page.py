import pytest
from pages.product_page import ProductPage

xfile = 7
product_base_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
links = [f"{product_base_link}/?promo=offer{number}" for number in range(10) if number != xfile]
# Страница с багом
xlink = pytest.param(f"{product_base_link}/?promo=offer{xfile}", marks=pytest.mark.xfail(reason="mistake on page"))
# Вставляет элемент перед указанным индексом
links.insert(xfile, xlink)


@pytest.mark.parametrize('link', links)
# Проверяет добавление в корзину со страницы товара
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
