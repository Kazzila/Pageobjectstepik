# № задания на курсе 3.6.4
# Команда pytest -s -v test_conftest.py
'''
Суть
Создать Conftest.py
Создать фикстуру browser
Запустить test_conftest.py с помощбю команды
'''

link = "http://selenium1py.pythonanywhere.com/"

def test_guest_should_see_login_link(browser):
    browser.get(link)
    browser.find_element_by_css_selector("#login_link")

