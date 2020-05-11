# № задания на курсе 3.6.8
#  Команда для консоли  !!!  pytest --language=es test_items.py  !!!
#  --language=fr
'''
                                            Суть

Добавьте в файл conftest.py обработчик, который считывает из командной строки параметр language.
Реализуйте в файле conftest.py логику запуска браузера с указанным языком пользователя.
Браузер должен объявляться в фикстуре browser и передаваться в тест как параметр.
В файл test_items.py напишите тест, который проверяет, что страница товара на сайте содержит кнопку добавления в корзину.
Например, можно проверять товар, доступный по "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/".
Тест должен запускаться с параметром language следующей командой:
            pytest --language=es test_items.py
и проходить успешно. Достаточно, чтобы код работал только для браузера Сhrome.
'''

import time
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_find_add_button(browser):
    browser.get(link)
    time.sleep(30)
    # assert проверяет наличие объекта на странице
    assert browser.find_element_by_class_name('btn-add-to-basket').is_displayed(), \
        'Кнопка добавления товара в корзину отсутсвует'
