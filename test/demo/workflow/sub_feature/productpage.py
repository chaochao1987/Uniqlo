from demo.page_constant.page_locator.productpagelocator import ProductPage
from demo.util.webdriverfun import WebDriverFun


class ChooseProduct(object):
    def __init__(self, driver):
        self.driver = driver

    def choose_one_product(self, number):
        product_path = ProductPage.product
        product_scroll_path = ProductPage.product_name
        self.driver.scroll_to_element(product_scroll_path, number)
        self.driver.get_element_by_index(product_path, number)





