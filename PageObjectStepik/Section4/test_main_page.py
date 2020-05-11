# № задания на курсе
# Команда для ком.строки  !!! pytest -v --tb=line --language=en test_main_page.py   !!!
'''
Суть
'''

from .pages.main_page import MainPage

def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                      # открываем страницу
    page.should_be_login_link()      # выполняем метод страницы - переходим на страницу логина
