# -*- coding:utf-8 -*-
from demo.page_constant.page_locator.homepagelocator import HomePageLocator
from robot.api import logger


class HomePage(object):
    def __init__(self, driver):
        self.hp = HomePageLocator()
        # self.gt = GetTestData()
        self.driver = driver


    def click_logo(self):
        logo_path = self.hp.uniglo_logo
        # self.wbf.is_displayed_click(logo_path, self.driver)
        self.driver.click_element_displayed(logo_path)

    def choose_goods_by_classification(self, classify1_txt, classify2_txt):
        logger.info('you choose %s below %s' % (classify2_txt.decode('utf-8'), classify1_txt))
        primary_category = self.hp.primary_category.format(classify1_txt)
        secondary_category = self.hp.secondary_category.format(classify2_txt)
        self.driver.click_element_displayed(primary_category)
        self.driver.click_element_displayed(secondary_category)

























