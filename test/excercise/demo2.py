# class test(object):
#     def __init__(self):
#         self.list1 = []
#
#     def add_to_list(self, size, color):
#         dict = {}
#         dict['size'] = size
#         dict['color'] = color
#         self.list1.append(dict)
#         return self.list1
#
# t= test()
# t.add_to_list('03 red', '02 xxl')
# t.add_to_list('02 white', '01 xxs')
# print t.list1



# list1 = [{'color': 'white', 'quantity': '3', 'name': 'a', 'size': 'xs'}, {'color': 'white', 'quantity': 2, 'name': 'b', 'size': 'xs'}]
# d1 = {'quantity': '4', 'name': 'a', 'size': 'xxs','color': 'white'}
# if d1 in list1:
#     print "in"
# else:
#     print "out"

class product_fun(object):
    def __init__(self):
        self.products = []

    def compare_in_products(self, name, size, color, quantity):
        flag = True
        if self.products == []:
            new_product = {'name': name, 'size': size, 'color': color, 'quantity': quantity}
            self.products.append(new_product)
        else:
            for prod in self.products:
                if prod['name'] == name and prod['size'] == size and prod['color'] == color:
                    prod['quantity'] = int(prod['quantity']) + int(quantity)
                    flag = False
                    break
            if flag:
                new_product = {'name': name, 'size': size, 'color': color, 'quantity': quantity}
                self.products.append(new_product)

    def reverse_products(self):
        self.products.reverse()

    def get_goods_by_order(self, number):
        self.reverse_products()
        if number > len(self.products):
            raise Exception("the number is out of index, please re-choose")
        return self.products[number-1]




pf = product_fun()
pf.compare_in_products('a', 'xs', 'white', '3')
pf.compare_in_products('b', 'xs', 'white', '1')
pf.compare_in_products('a', 'xs', 'white', '2')
pf.compare_in_products('b', 'xs', 'white', '1')

print pf.get_goods_by_order(2)['name']


