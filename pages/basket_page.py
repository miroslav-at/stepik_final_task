from pages.base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    # Проверка на отсутствие товаров в корзине
    def check_for_the_absence_of_products_in_the_basket(self):
        # Проверка на отсутствие товаров в корзине
        self.should_not_be_products_in_the_basket()
        # Проверяет наличие сообщения о том, что корзина пуста
        self.should_be_a_message_about_an_empty_basket()

    def should_not_be_products_in_the_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.PRODUCT_IN_THE_BASKET), \
            "There are products in the basket, but they should not be!"

    def should_be_a_message_about_an_empty_basket(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_MESSAGE), \
            "There is no message that the trash is empty!"
