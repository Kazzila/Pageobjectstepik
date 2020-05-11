# № задания на курсе 4.2.7
# Команда для ком.строки  !!! pytest -v --tb=line --language=en test_main_page.py   !!!
'''
Суть
Они, конечно, снова упадут. Но теперь посчитайте, сколько строк вам нужно будет отредактировать,
когда тесты написаны в такой конфигурации?'''

from .pages.main_page import MainPage

def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                      # открываем страницу
    page.should_be_login_link()      # выполняем метод страницы - переходим на страницу логина
