#-*- coding: utf-8 -*-
import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select


def switch_to_specified_handle(title_name):
    handles = driver.window_handles
    print len(handles)
    for handle in handles:
        driver.switch_to.window(handle)
        if driver.title != title_name:
            continue
        else:
            break


driver = webdriver.Chrome()
driver.get("https://www.baidu.com")
# driver.implicitly_wait(10)
# driver.find_element_by_link_text(u'设置').click()
# driver.find_element_by_link_text(u'搜索设置').click()
# time.sleep(2)
# select_path = driver.find_element_by_name('NR')
# se = Select(select_path)
# se.select_by_value('20')
# save_btn = driver.find_element_by_xpath('//div[@id="gxszButton"]')
# save_btn.click()
# time.sleep(2)
# alert = driver.switch_to.alert
# print alert.text
# alert.accept()
# time.sleep(2)
kw = driver.find_element_by_id('kw')
kw.send_keys('python')
# print kw.tag_name

driver.find_element_by_id('su').click()
time.sleep(2)
# a_text = driver.find_element_by_xpath('//div[@id="content_left"]/div[3]/h3/a[1]')
# print a_text.text
# website_xuefeng = driver.find_element_by_partial_link_text(u'廖雪峰的官方网站')

# locator = (By.PARTIAL_LINK_TEXT, u'廖雪峰的官方网站1')
# # el = driver.find_element_by_partial_link_text(u'廖雪峰的官方网站')
# element = WebDriverWait(driver, 20).until(EC.presence_of_element_located(locator))

# print type(element)
target_element = driver.find_element_by_partial_link_text(u'廖雪峰的官方网站')
print target_element.get_attribute('href')
target_element.click()

# driver.find_element_by_xpath('//a[text()="教程 - 廖雪峰的官方网站"]').click()
# switch_to_specified_handle(u'Python教程 - 廖雪峰的官方网站')
#
# driver.find_element_by_link_text(u'2.7旧版教程').click()
# switch_to_specified_handle(u'python_百度搜索')
# print driver.title
#
# # time.sleep(5)
# # #
# # #
# # #
# driver.find_element_by_partial_link_text(u' 基础教程 | 菜鸟教程').click()
# driver.find_element_by_xpath(' //a[text()="基础教程 | 菜鸟教程"]').click()
# switch_to_specified_handle(u'python_百度搜索')
# driver.back()
# time.sleep(5)
# # handles = driver.window_handles()
# # for handle in handles:
# #     print handle.title()
# # print driver.current_url
# driver.quit()




