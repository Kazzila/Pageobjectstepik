# № задания на курсе 4.2.7
from .base_page import BasePage # импорт базового класса BasePage
from .locators import MainPageLocators
from selenium.webdriver.common.by import By

'''
Обратите внимание здесь на символ *, он указывает на то, что мы передали именно пару, и этот кортеж нужно распаковать. 
'''
class MainPage(BasePage): # класс MAinPAge наследник класса BasePage. Класс-предок в Python указывается в скобках
    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"
