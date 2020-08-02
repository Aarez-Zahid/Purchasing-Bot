from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time , random

def courtside_shoe_bot(shoe, size):

    browser = webdriver.Chrome()

    added = True
    while (added):
        try:
            browser.get(shoe)
            select = browser.find_elements_by_class_name('single-option-selector')
            Select(select[1]).select_by_value(size)
            browser.find_element_by_class_name('add-to-cart').click()
            time.sleep(0.5)
            added = False

        except:
            time.sleep(random.uniform(1,3))

    browser.find_element_by_class_name('checkout-link').submit()
    browser.find_element_by_xpath('//*[@id="shopify-section-cart"]/section/form/div/div[2]/div[2]/button').click()

