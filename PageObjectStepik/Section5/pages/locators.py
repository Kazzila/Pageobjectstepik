'''
Внутри создайте новый класс. Каждый класс будет соответствовать каждому классу PageObject
Tеперь каждый селектор — это пара: как искать и что искать.

В файле main_page.py импортируйте новый класс с локаторами
'''

from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
