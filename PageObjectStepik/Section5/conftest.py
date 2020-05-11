# № задания на курсе
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Функция для обработки переданных в командной строке данных
def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                     help="Choose language: ru or other")

'''
Создаем фикстуру browser для открытия и закрытия браузера перед тестом
'''

@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption("language") # запрос параметра
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    browser = webdriver.Chrome(options=options)
    print("\nstart browser for test..")
    yield browser
    print("\nquit browser..")
    browser.quit()