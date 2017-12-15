#-*- coding: utf-8 -*-
from selenium import webdriver
from time import sleep


driver = webdriver.Chrome()
driver.get('http://www.uniqlo.com/jp/store/goods/404008')
sleep(5)
color = driver.find_element_by_xpath('//div[contains(@title, "LIGHT GRAY")]')
# size = driver.find_element_by_partial_link_text('165/92A/XL')
# size.click()
# sleep(2)
# color = driver.find_element_by_xpath('//img[@alt="カートに追加"]')
# print color.is_enabled()
# print color.is_displayed()
# color.click()
quantity = driver.find_element_by_id('selectNum')
quantity.screenshot('/screenshot/foo.png')
print quantity.size
print quantity.location
