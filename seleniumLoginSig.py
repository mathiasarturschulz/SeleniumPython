from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()

# SIG IFC
browser.get('https://sig.ifc.edu.br/sigaa/verTelaLogin.do')

# LOGIN
browser.find_element_by_name('user.login').send_keys('mathiasschulz')
browser.find_element_by_name('user.senha').send_keys('senha')
browser.find_element_by_xpath('//input[@type="submit"]').click()

# ACESSAR A DISCIPLINA
browser.find_element_by_css_selector('form[name=form_acessarTurmaVirtualj_id_1] > a').click()

# ACESSAR A ABA ALUNOS E VER NOTAS
browser.find_element_by_xpath('//*[contains(text(), "Alunos")]').click()
browser.find_element_by_xpath('//*[contains(text(), "Ver Notas")]').click()
