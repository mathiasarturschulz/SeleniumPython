from selenium import webdriver
from selenium.webdriver.common.keys import Keys

q = input("Palavra para consultar: ")
q = q.replace(' ', '')
browser = webdriver.Chrome()
counter = 0

for i in range(0, 20):
    browser.get('https://www.google.com/search?q=' + q + '&start=' + str(counter))
    counter += 10
