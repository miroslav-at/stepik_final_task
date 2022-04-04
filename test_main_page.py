from pages.main_page import MainPage

link = "http://selenium1py.pythonanywhere.com/"

# Проверяет, что пользователь в роли гостя может перейти на страницу входа в систему
def test_guest_can_go_to_login_page(browser):
    # инициализация Page Object, передача в конструктор экземпляра драйвера и url адреса
    page = MainPage(browser, link)
    # открывает страницу
    page.open()
    # выполняет метод страницы — переходит на страницу логина
    page.go_to_login_page()

# Переходит на страницу логина
def go_to_login_page(browser):
    login_link = browser.find_element_by_css_selector("#login_link")
    login_link.click()

# Проверяет на наличие ссылки для входа в систему
def test_guest_should_see_login_link(browser):
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()
