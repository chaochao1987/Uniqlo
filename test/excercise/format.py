# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains

# get attribute value
driver = webdriver.Chrome()

driver.get('https://baidu.com')
kw = driver.find_element_by_id('kw')
kw.click()
# setting = driver.find_element_by_xpath("//a[text()='设置']").click()
setting = driver.find_element_by_link_text("设置")
ActionChains(driver).move_to_element(setting).perform()

advanced_search = driver.find_element_by_link_text("搜索设置").click()

s = driver.find_element_by_xpath('//select[@id="nr"]')
Select(s).select_by_visible_text("每页显示20条")
