from selenium import webdriver

driver = webdriver.Chrome()

driver.get('http://localhost:63342/test/excercise/uniqlo.html?_ijt=t5ckv026k452haka3oatmtkljf')


class Locator(object):
    name = '//tbody/tr{}/td[@class="cellName"]'
    size = '//tbody/tr{}/td[@class="cellSize"]'
    color = '//tbody/tr{}/td[@class="cellColor"]'
    product_number = '//tbody/tr'

class Cart_Page(object):
    def __init__(self):
        self.lo = Locator()

    def locate_element(self, el_path):
        pattern = el_path.split('=', 1) if '=' in el_path else []
        if not (all(pattern) and pattern):
            raise Exception('pattern:%s,[] list or empty element in pattern is not supported')
        k, v = pattern
        if k == 'xpath':
            element = self.driver.find_element_by_xpath(v)
        return element

    def get_name(self):
        pass

    def get_size(self):
        pass

    def get_color(self):
        pass

    def product_amount(self):
        tr_number_path = self.lo.product_number
        tr_numbers = len(self.locate_element(tr_number_path))
        return tr_numbers

c = Cart_Page()
print c.product_amount()