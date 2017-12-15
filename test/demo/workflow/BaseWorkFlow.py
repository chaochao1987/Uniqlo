from demo.util.common import GetTestData
from demo.workflow.sub_feature.productpage import ChooseProduct
from demo.workflow.sub_feature.homepage import HomePage
from demo.workflow.sub_feature.productdetailpage import ProductDetailPage
from demo.workflow.sub_feature.cartpage import CartPage
from demo.util.webdriverfun import WebDriverFun
import time


class BaseWorkFlow(object):
    def __init__(self):
        self.driver = WebDriverFun()
        self.product_list = []
        self.test_data = {}

    def get_data_from_file(self, file_name):
        td = GetTestData()
        td.get_datas_in_file(file_name)
        self.test_data = td.data

    def open_url(self):
        self.driver.open_browser(self.test_data['type'])
        self.driver.open_url(self.test_data['url'])

    def choose_category(self):
        assert self.test_data['parent_classify'], 'please input parent_classify'
        assert self.test_data['sub_classify'], 'please input sub_classify'
        self.homepage = HomePage(self.driver)
        self.homepage.click_logo()
        isinstance(self.test_data['sub_classify'], unicode)
        self.homepage.choose_goods_by_classification(self.test_data['parent_classify'],
                                                     (self.test_data['sub_classify']).encode('utf-8'))



    def choose_product(self, number=1):
        self.cp = ChooseProduct(self.driver)
        self.cp.choose_one_product(number)

    def edit_product(self, color, size, quantity):

        pd = ProductDetailPage(self.driver, self.product_list)
        pd.get_name()
        pd.choose_color(color)
        pd.choose_size(size)
        pd.choose_quantity(quantity)
        pd.add_to_cart()
        pd.collect_new_product_to_products_list()
        # before_number = pd.get_the_number_of_goods()
        pd.click_cart_logo()
        # return before_number

    def choose_items(self):
        pd_list = self.test_data['products']
        for index in range(len(pd_list)):
            if index == len(pd_list)-1:
                assert pd_list[index]['color'], 'Please choose a kind of color'
                assert pd_list[index]['size'], 'Please choose a kind of size'
                assert pd_list[index]['quantity'], 'Please choose a quantity of the good'
                self.edit_product(pd_list[index]['color'], pd_list[index]['size'], str(pd_list[index]['quantity']))
            else:
                assert pd_list[index]['color'], 'Please choose a kind of color'
                assert pd_list[index]['size'], 'Please choose a kind of size'
                assert pd_list[index]['quantity'], 'Please choose a quantity of the good'
                self.edit_product(pd_list[index]['color'], pd_list[index]['size'], str(pd_list[index]['quantity']))
                self.driver.back_to_prepage()

    # def add_multiple_same_item(self, color, size, quantity):
    #     self.edit_product(color, size, quantity)
    #     self.driver.back_to_prepage()
    #     self.edit_product(color, size, quantity)

    def check_product_info(self):
        cp = CartPage(self.driver)
        after_number = cp.tr_number_in_cart()
        cp.combine_to_product_list(after_number)
        cp.compare_before_after(after_number, self.product_list)

    def choose_different_products(self):
        product_number = self.test_data['product_number']
        pd_list = self.test_data['products']
        for index in range(len(product_number)):
            self.choose_product(product_number[index]['product'])
        # for index in range(len(pd_list)):
            if index == len(pd_list)-1:
                self.edit_product(pd_list[index]['color'], pd_list[index]['size'], str(pd_list[index]['quantity']))
            else:
                self.edit_product(pd_list[index]['color'], pd_list[index]['size'], str(pd_list[index]['quantity']))
                self.driver.back_to_prepage()
                self.driver.get_page_title()
                self.driver.back_to_prepage()
                self.driver.back_to_prepage()

    def teardown(self):
        self.driver.close_driver()





if __name__ == '__main__':
    b = BaseWorkFlow()
    b.get_data_from_file('different_items.yaml')
    b.open_url()
    b.choose_category()
    # b.choose_product()
#     # products_details_before, amounts_before = b.edit_product('LIGHT GRAY', 'S', 5)
#     # b.check_product_info(products_details_before, amounts_before)
#     b.add_multiple_same_item('LIGHT GRAY', 'S', '5')
#     b.choose_items()
    b.choose_different_products()
    b.check_product_info()
#

    b.teardown()
