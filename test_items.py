import time
from selenium.webdriver.common.by import By

def test_button_add_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    time.sleep(5)
    button_basket = browser.find_element(By.CSS_SELECTOR, '.btn-add-to-basket')
    assert button_basket, 'кнопка не найдена'