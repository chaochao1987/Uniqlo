from selenium.webdriver.support.select import Select
from robot.api import logger
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium import webdriver
import os

class WebDriverFun(object):
    def __init__(self):
        self.driver = None
        self.driver_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'driver')

    def back_to_prepage(self):
        self.driver.back()

    def get_page_title(self):
        logger.info(self.driver.title)

    def open_browser(self, browser='Chrome'):
        if browser == 'chrome' or 'Chrome':
            driver_path = self.driver_dir + '\chromedriver.exe'
            self.driver = webdriver.Chrome(driver_path)
        elif browser == 'ie' or 'IE':
            driver_path = self.driver_dir + '\iedriver.exe'
            self.driver = webdriver.Ie(driver_path)
        else:
            raise Exception("the browser: %s is not support.")

    def close_driver(self):
        import os
        self.driver.close()
        os.system('taskkill /F /IM "chromedriver.exe"')

    def open_url(self, url):
        self.driver.maximize_window()
        self.driver.get(url)
        logger.info('Open %s ' % url)


    def locate_element(self, el_path):
        pattern = el_path.split('=', 1) if '=' in el_path else []
        if not (all(pattern) and pattern):
            raise Exception('pattern:%s,[] list or empty element in pattern is not supported')
        k, v = pattern
        if k == 'xpath':
            element = self.driver.find_element_by_xpath(v)
        elif k == 'id':
            element = self.driver.find_element_by_id(v)
        elif k == 'class_name':
            element = self.driver.find_element_by_class_name(v)
        elif k == 'tag_name':
            element = self.driver.find_element_by_tag_name(v)
        elif k == 'link_text':
            element = self.driver.find_element_by_link_text(v)
        elif k == 'partial_link_text':
            element = self.driver.find_element_by_partial_link_text(v)
        else:
            raise Exception("the locator_type:%s is not correct format.")
        return element

    def send_key(self, el_path):
        element = self.locate_element(el_path)
        if element:
            element.send_keys()

    def clear_input(self, el_path):
        element = self.locate_element(el_path)
        if element:
            element.clear()

    def locate_elements(self, el_path):
        pattern = el_path.split('=', 1) if '=' in el_path else []
        if not (all(pattern) and pattern):
            raise Exception('[] list or empty element in pattern is not supported')
        k, v = pattern
        if k == 'xpath':
            elements = self.driver.find_elements_by_xpath(v)
        elif k == 'id':
            elements = self.driver.find_elements_by_id(v)
        elif k == 'class_name':
            elements = self.driver.find_elements_by_class_name(v)
        elif k == 'tag_name':
            elements = self.driver.find_elements_by_tag_name(v)
        elif k == 'link_text':
            elements = self.driver.find_elements_by_link_text(v)
        elif k == 'partial_link_text':
            elements = self.driver.find_elements_by_partial_link_text(v)
        else:
            raise Exception("the locator_type:%s is not correct format." % v)
        return elements

    def get_element_by_index(self, el_path, number=1):
        self.explicit_wait_elements(el_path)
        elements = self.locate_elements(el_path)
        if elements:
            if number > len(elements):
                raise Exception("The product you choose can not found on the product page")
            element = elements[number-1]
            element.click()

    def get_element_by_index_not_click(self, el_path, number):
        self.explicit_wait_elements(el_path)
        elements = self.locate_elements(el_path)
        if elements:
            if number > len(elements):
                raise Exception("The product you choose can not found on the product page")
            element = elements[number - 1]
        return element

    # def get_element_by_select_tag(self, el_path, value):
    #     element = self.locate_element(el_path)
    #     if element:
    #         se = Select(element)
    #         se.select_by_visible_text(value)

    def click_element_enabled(self, el_path, value):
        if not isinstance(value, str):
            raise TypeError('bad operand for click_element_enabled()')
        self.explicit_wait_element(el_path)
        element = self.locate_element(el_path)
        if element.is_enabled():
            se = Select(element)
            se.select_by_visible_text(value)
        else:
            logger.error('The element is not enabled for it is grey button')

    def scroll_to_element(self, el_path, number):
        self.explicit_wait_element(el_path)
        target = self.get_element_by_index_not_click(el_path, number)
        self.driver.execute_script("arguments[0].scrollIntoView();", target)

    def click_element_not_selected(self, el_path):
        self.explicit_wait_element(el_path)
        element = self.locate_element(el_path)
        class_value = element.get_attribute('class')
        if element.get_attribute('class') == 'disable':
            raise Exception('this element is disable, please change another choose')
        else:
            if class_value == 'selected':
                logger.info("the color you choose is a default color, so you don't need click the element")
                if 'listChipColor' in el_path:
                    get_id = element.get_attribute('color')
                elif 'listChipSize' in el_path:
                    get_id = element.get_attribute('title')
            else:
                if 'listChipColor' in el_path:
                    get_id = element.get_attribute('color')
                    element.click()
                elif 'listChipSize' in el_path:
                    get_id = element.get_attribute('title')
                    element.click()
        return get_id

    def click_element_displayed(self, el_path):
        self.explicit_wait_element(el_path)
        element = self.locate_element(el_path)
        if element.is_displayed():
            element.click()
        else:
            logger.error('element is not displayed')

    def explicit_wait_element(self, el_path):
        pattern = el_path.split('=', 1) if '=' in el_path else []
        if not (all(pattern) and pattern):
            raise Exception('[] list or empty element in pattern is not supported')
        k, v = pattern
        if k == 'xpath':
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, v)))
        elif k == 'id':
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, v)))
        elif k == 'class_name':
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, v)))
        elif k == 'tag_name':
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, v)))
        elif k == 'link_text':
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, v)))
        elif k == 'partial_link_text':
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, v)))
        else:
            logger.error('please locates the element by xpath,id,class_name,tag_name,link_text or partial_link_text ')

    def explicit_wait_elements(self, el_path):
        pattern = el_path.split('=', 1) if '=' in el_path else []
        if not (all(pattern) and pattern):
            raise Exception('[] list or empty element in pattern is not supported')
        k, v = pattern
        if k == 'xpath':
            WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, v)))
        elif k == 'id':
            WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.ID, v)))
        elif k == 'class_name':
            WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, v)))
        elif k == 'tag_name':
            WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.TAG_NAME, v)))
        elif k == 'link_text':
            WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.LINK_TEXT, v)))
        elif k == 'partial_link_text':
            WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.PARTIAL_LINK_TEXT, v)))
        else:
            logger.error('please locates the element by xpath,id,class_name,tag_name,link_text or partial_link_text ')

    def get_element_text(self, el_path):
        element = self.locate_element(el_path)
        value = element.text
        return value

    def get_attribute_value(self, el_path, attribute='value'):
        element = self.locate_element(el_path)
        if attribute == 'value':
            value = element.get_attribute(attribute)
        return value

