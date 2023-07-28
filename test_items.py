from selenium import webdriver
from selenium.webdriver.common.by import By
import time



link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_button_to_add_item_to_basket(browser):
    browser.get(link)
    time.sleep(30)
    buttons = browser.find_elements(By.CLASS_NAME, "btn.btn-lg.btn-primary.btn-add-to-basket")
    assert len(buttons) > 0, "Button not found!"
