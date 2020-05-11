# № задания на курсе 4.2.6
# Команда для командной строки pytest -v --tb=line --language=en test_main_page.py
'''
Суть

'''

def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    browser.get(link)
    login_link = browser.find_element_by_css_selector("#login_link")
    login_link.click()