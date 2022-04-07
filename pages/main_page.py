from .base_page import BasePage
from .locators import MainPageLocators


# Представляет главную страницу
class MainPage(BasePage):
    # Заглушка
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)
