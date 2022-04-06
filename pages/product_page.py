from pages.base_page import BasePage
from pages.locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_basket(self):
        self.should_be_product_name()
        self.should_be_price()
        self.should_be_decription()
        self.should_be_add_button()

        self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_BASKET).click()
        self.solve_quiz_and_get_code()

        self.should_be_success()
        self.check_success_message()

    def should_be_product_name(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME), "Name of product not found"
        self.product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text

    def should_be_price(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_PRISE), "Price of product not found"
        self.product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRISE).text

    def should_be_decription(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_DESCRIPTION), "Description of product not found"
        self.product_decription = self.browser.find_element(*ProductPageLocators.PRODUCT_DESCRIPTION).text

    def should_be_add_button(self):
        assert self.is_element_present(*ProductPageLocators.BUTTON_ADD_TO_BASKET), "Button 'Add to basket' is not "

    def should_be_success(self):
        assert self.is_element_present(*ProductPageLocators.SUCCESS_MESSAGES), "Message of Success added product in " \
                                                                               "basket not found "

    def check_success_message(self):
        success_message = self.browser.find_elements(*ProductPageLocators.SUCCESS_MESSAGES)
        assert len(success_message) == 3, "Success message not found"

        assert self.product_name == success_message[0].text, "Wrong name product added to basket"
        assert self.product_price == success_message[2].text, "Wrong price product added to basket"
