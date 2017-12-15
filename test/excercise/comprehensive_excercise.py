# -*- coding: utf-8 -*-
from selenium import webdriver
from time import sleep
#alert

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('http://www.uniqlo.cn/')

login_btn = driver.find_element_by_xpath('//img[contains(@alt, "登入")]').click()
sleep(3)
# iframe_ele = driver.find_element_by_xpath('//iframe[@id="mediav_cookiemapping"]')
# driver.switch_to.frame(iframe_ele)
confirm_btn = driver.find_element_by_xpath('//div[@id="TB_ajaxContent"]/ul/li/a[@id="Login"]/img[@alt="确定"]')
confirm_btn.click()
sleep(2)
