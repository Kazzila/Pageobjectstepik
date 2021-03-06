# № задания на курсе

import pytest
from selenium import webdriver

'''
Создаем фикстуру browser для открытия и закрытия браузера перед/после теста
'''

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()