from pages.main_page import MainPage

link = "http://selenium1py.pythonanywhere.com/"


def test_guest_can_go_to_login_page(browser):
    # инициализация Page Object, передача в конструктор экземпляра драйвера и url адреса
    page = MainPage(browser, link)
    # открывает страницу
    page.open()
    # выполняет метод страницы — переходит на страницу логина
    page.go_to_login_page()

def go_to_login_page(browser):
    login_link = browser.find_element_by_css_selector("#login_link")
    login_link.click()
