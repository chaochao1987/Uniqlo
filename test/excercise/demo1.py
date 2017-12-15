# -*- coding: utf-8 -*-
#
# def dec(f):
#     def wrap(*args, **kwargs):
#         print 'dec'
#         f(*args, **kwargs)
#         print 'end!'
#     return wrap
#
#
# class Foo():
#     @dec
#     def show(self, name):
#         print name, 'show!'
#
# Foo().show('Allen')

# 商品的name, size,color 先和products = {}中进行比较，如果有相同的，就不算新的item，只需要在找到原来的商品数量上累加
class product_fun(object):
    def __init__(self):
        self.products = []

    def compare_in_products(self, name, size, color, quantity):
        new_product = {}
        if self.products == []:
            new_product['name'] = name
            new_product['size'] = size
            new_product['color'] = color
            new_product['quantity'] = quantity
            self.products.append(new_product)
        else:
            for prod in self.products:
                if prod['name'] == name and prod['size'] == size and prod['color'] == color:
                    prod['quantity'] = int(prod['quantity']) + int(quantity)
                else:
                    new_product['name'] = name
                    new_product['size'] = size
                    new_product['color'] = color
                    new_product['quantity'] = quantity
                    self.products.append(new_product)

    def reverse_products(self):
        self.products.reverse()
        return len(self.products)


pf = product_fun()
pf.compare_in_products('a', 'xs', 'white', '3')
pf.compare_in_products('b', 'xs', 'white', '1')
pf.compare_in_products('b', 'xxl', 'white', '1')
for product in pf.products:
    print product


# list1 = [
#     {'color': 'white', 'quantity': '3', 'name': 'a', 'size': 'xs'},
#     {'color': 'white', 'quantity': '2', 'name': 'b', 'size': 'xs'},
#     {'color': 'red', 'quantity': '2', 'name': 'b', 'size': 'xs'},
# ]
#
# def compare(color, quantity, name, size):
#     for prod in dict:
#         if prod['name'] != name and prod['size'] != size and prod['color'] != color:







