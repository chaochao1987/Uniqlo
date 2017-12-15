# list1 = {'color': u'02\nLIGHT GRAY', 'quantity': u'5', 'size': u'S'}
# list2 = {'color': u'02 LIGHT GRAY', 'quantity': '5', 'size': u'S'}
# list1['color'] = list1['color'].replace('\n', ' ')
# print list1

# {'color': u'02 LIGHT GRAY', 'quantity': u'5',
#  'name': u'\u30b3\u30c3\u30c8\u30f3\u30ab\u30b7\u30df\u30e4\u30ea\u30d6\u30bb\u30fc\u30bf\u30fc\uff08\u9577\u8896\uff09', 'size': u'S'}
# {'color': u'02 LIGHT GRAY', 'quantity': '5', 'name': u'\u30b3\u30c3\u30c8\u30f3\u30ab\u30b7\u30df\u30e4\u30ea\u30d6\u30bb\u30fc\u30bf\u30fc\uff08\u9577\u8896\uff09', 'size': u''}
# str1 = u'02\nLIGHT GRAY'
# str1 = str1.replace('\n', ' ')
# print str1
# def fib(max):
#     n, a, b = 0, 0, 1
#     while n < max:
#         print b
#         a, b = b, a + b
#         n = n + 1
#
# fib(3)
# quantity = unicode(10)
# list1 = {'color': u'02 LIGHT GRAY', 'quantity': u'10', 'size': u'S'}
# list2 = {'color': u'02 LIGHT GRAY', 'quantity': quantity,  'size': 'S'}
# # list2 = {'color': u'02 LIGHT GRAY', 'quantity': u'10',  'size': 'S'}
#
# print list2
n = unicode(5+5)
list = ['a', n]
print list