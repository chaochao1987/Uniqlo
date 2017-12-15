import os
from selenium import webdriver


class Browser(object):
    def __init__(self):
        self.driver_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'driver')

    def open_browser(self, browser='Chrome'):
        if browser == 'chrome' or 'Chrome':
            driver_path = self.driver_dir + '\chromedriver.exe'
            self.driver = webdriver.Chrome(driver_path)
        elif browser == 'ie' or 'IE':
            driver_path = self.driver_dir + '\iedriver.exe'
            self.driver = webdriver.Ie(driver_path)
        else:
            raise Exception("the browser: %s is not support.")

    def open_url(self, url):
        self.driver.maximize_window()
        self.driver.get(url)
        return self.driver

    # def get_title(self):
    #     self.driver.get_title()
    #     assert











