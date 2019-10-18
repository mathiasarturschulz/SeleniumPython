from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()
browser.get('http://www.curvello.com/selenium/index03_login.html')

browser.find_element_by_name('user').send_keys('batata')
browser.find_element_by_name('pass').send_keys('batata')
browser.find_element_by_name('enviar').click()

f = open('names.txt', 'r')
lines = f.readlines()

for line in lines:
    input = browser.find_element_by_name('texto')
    input.send_keys(line.replace('\n', ''))
    browser.find_element_by_name('add').click()
    input.clear()
