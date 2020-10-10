from selenium import webdriver 
from selenium.common.exceptions import ElementNotInteractableException
from selenium.webdriver.support.ui import Select , WebDriverWait
import time , random

def courtside_bot(shoe, size):

    browser = webdriver.Chrome()
    added = True
    while (added):
        try:
            browser.get(shoe)
            select = browser.find_elements_by_class_name('single-option-selector')
            Select(select[1]).select_by_value(size.upper())
            browser.find_element_by_class_name('add-to-cart').click()
            time.sleep(0.5)
            added = False
        except ElementNotInteractableException:
            time.sleep(random.uniform(1,3))

    browser.find_element_by_class_name('checkout-link').submit()
    browser.find_element_by_xpath('//*[@id="shopify-section-cart"]/section/form/div/div[2]/div[2]/button').click()

def nrml_bot(shoe, size):
    browser = webdriver.Chrome()
    added = True

    while (added):
        try:
            browser.get(shoe)
            x = browser.find_elements_by_class_name("option__variant")
            for i in x:
                if i.get_attribute("data-variant-title") == size.upper():
                    i.click()
                    break
            time.sleep(0.5)
            browser.find_element_by_name("add").click()
            time.sleep(0.5)
            browser.find_element_by_name("checkout").click()
            added = False
        except ElementNotInteractableException:
            time.sleep(random.uniform(1, 3))



def deadstock_bot(shoe, size):
    browser = webdriver.Chrome()
    browser.get(shoe)
    size_key = {"s": "SM", "m": "MED","l":"LRG", "xl" : "XLRG"}
    if size in (size_key.keys()):
        size = size_key[size]

    index = len(browser.find_elements_by_name("US Men's Size"))
    for i in range(1, index - 1):
        option = browser.find_element_by_xpath('//*[@id="ProductSelect-option-0"]/label[' + str(i) + ']')
        parse = len(size)
        if size == option.get_attribute("innerHTML")[0:parse]:
            option.click()
            break

    browser.find_element_by_id("AddToCart").submit()
    time.sleep(2)
    browser.find_element_by_xpath('//*[@id="CartContainer"]/form/div[2]/a').click()
    time.sleep(1)
    browser.find_element_by_xpath('//*[@id="PageContainer"]/main/div/div/div/form/div[3]/div/div[2]/button[3]').click()









