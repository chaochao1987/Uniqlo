from demo.page_constant.page_locator.cartpagelocator import CartPageLocator
from robot.api import logger


class CartPage(object):
    def __init__(self, driver):
        self.cp = CartPageLocator()
        self.driver = driver
        self.product = []
        self.product_with_property = {}

    def product_name_in_cart(self, number):
        product_name_path = self.cp.Product_Name.format([number])
        self.product_name = self.driver.get_element_text(product_name_path)
        # self.product_with_property['name'] = product_name
        # return product_name

    def product_color_in_cart(self, number):
        product_color_path = self.cp.Product_Color.format([number])
        self.product_color = self.driver.get_element_text(product_color_path)
        self.product_color = self.product_color.replace('\n', ' ')

    def product_size_in_cart(self, number):
        product_size_path = self.cp.Product_Size.format([number])
        self.product_size = self.driver.get_element_text(product_size_path)
        # self.product_with_property['size'] = product_size
        # return product_size

    def product_quantity_in_cart(self, number):
        product_quantity_path = self.cp.Product_Quantity.format([number])
        self.product_quantity = self.driver.get_attribute_value(product_quantity_path)
        # self.product_with_property['quantity'] = product_quantity
        # return product_quantity

    def tr_number_in_cart(self):
        tr_path = self.cp.Product_number
        products_amount = len(self.driver.locate_elements(tr_path))
        return products_amount

    def combine_to_product_list(self, products_amount):
        for i in range(products_amount):
            self.product_name_in_cart(i+1)
            self.product_color_in_cart(i+1)
            self.product_size_in_cart(i+1)
            self.product_quantity_in_cart(i+1)
            self.product_with_property = {'name': self.product_name,
                                        'color': self.product_color,
                                        'size': self.product_size,
                                        'quantity': self.product_quantity
                                        }
            self.product.append(self.product_with_property)
            logger.info('----cart page----'\
                        'product name: %s'\
                        'product color: %s' \
                        'product size: %s' \
                        'product quantity: %s'\
                        % (self.product_name, self.product_color, self.product_size, self.product_quantity)
                        )

    def compare_before_after(self, after, products_before):
        if len(products_before) == after:
            for i in range(after):
                if self.product[i] != products_before[i]:
                    logger.error("Product_in_detail page:%s \n cart_page:%s ") % (self.product[i], products_before[i])
                else:
                    continue













