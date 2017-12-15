from demo.page_constant.page_locator.productdetailpagelocator import Product_Detail_Page_Locator
from robot.api import logger

class ProductDetailPage(object):
    def __init__(self, driver, products):
        # self.product_list = product_list
        self.driver = driver
        self.pdpl = Product_Detail_Page_Locator()
        self.products = products
        self.product = {}

    def get_name(self):
        product_name_path = self.pdpl.PRODUCT_NAME
        self.name = self.driver.get_element_text(product_name_path)
        logger.info('the product you choose is : %s' % self.name)

    def choose_color(self, color):
        # color_path = self.pdpl.COLOR.format(color.upper())
        color_selected_path = self.pdpl.COLOR_SELECTED.format(color.upper())
        color_id = self.driver.click_element_not_selected(color_selected_path)
        self.product['color'] = color_id + ' ' + color
        logger.info('The color you choose is : %s' % self.product['color'])

    def choose_size(self, size):
        size_selected_path = self.pdpl.SIZE_SELECTED.format(size.upper())
        self.driver.click_element_not_selected(size_selected_path)
        self.product['size'] = size
        logger.info('The size you choose is : %s' % self.product['size'])
        # self.wbf.click(size_path)

    def choose_quantity(self, value):
        quantity_path = self.pdpl.QUANTITY
        self.driver.click_element_enabled(quantity_path, value)
        self.product['quantity'] = value
        logger.info('The quantity you choose is : %s' % self.product['quantity'])

    def add_to_cart(self):
        car_path = self.pdpl.CART
        # self.wbf.click(car_path)
        self.driver.click_element_displayed(car_path)

    def click_cart_logo(self):
        cart_logo = self.pdpl.CART_LOGO
        self.driver.click_element_displayed(cart_logo)

    def collect_new_product_to_products_list(self):
        color = self.product['color']
        size = self.product['size']
        quantity = self.product['quantity']
        name = self.name
        flag = True
        if self.products == []:
            new_product = {'name': name, 'size': size, 'color': color, 'quantity': quantity}
            self.products.append(new_product)
        else:
            for prod in self.products:
                if prod['name'] == name and prod['size'] == size and prod['color'] == color:
                    prod['quantity'] = unicode(int(prod['quantity']) + int(quantity))
                    flag = False
                    logger.info('the product is the same as the item in cart.yet the quantity need to be accumulated')
                    break
            if flag:
                # new_product = {'name': self.name, 'size': self.size, 'color': self.color, 'quantity': self.quantity}
                new_product = {'name': name, 'size': size, 'color': color, 'quantity': quantity}
                self.products.append(new_product)
                logger.info('the product is a new item')
            self.products.reverse()

    def get_the_number_of_goods(self):
        amounts_of_goods = len(self.products)
        logger.info('you have(has) choosen %s sku(s) to cart' % amounts_of_goods)
        return amounts_of_goods

    def back_to(self):
        self.driver.back_to_prepage()














