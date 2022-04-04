from selenium.common.exceptions import NoSuchElementException


class BasePage():
    # Представляет экземпляр класса BasePage
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(10)

    # Открывает веб-страницу
    def open(self):
        self.browser.get(self.url)

    # Обрабатывает исключение при проверке элемента на странице
    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True
