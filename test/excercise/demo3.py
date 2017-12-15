#-*- coding: utf-8 -*-
# def my_abs(a, b):
#      return a, b
#
# t1 =  my_abs(2,3)
# print t1[0]
#
# def power(a):
#     return a * a
#
# def power3(a):
#     return a * a * a

# def power4(a, n = 1):
#     sum = 1
#     while n > 0:
#         sum = sum * a
#         n -= 1
#     return sum
#
# print power4(2)

# def enroll(name, age, city='shanghai', address='Road 10th'):
#     return name, age, city, address
#
# print enroll('apple', 20, address='tian 10th')
#
# class A(object):
#     def __init__(self, L):
#         self.L = L
#
#     def add_end(L):
#         L.append('END')
#         return L
# l = []
# a = A(l)
#
# print a.add_end()

# s = set([1,2,3,3,4])
# print s
# s.remove(4)
# print s

# def fun(*numbers):
#     sum = 0
#     print type(numbers)
#     for v in numbers:
#         sum += v * v
#     return sum
#
# t = [1, 2, 3, 4]
# print fun(*t)
#
# def fun2(**kw):
#     return kw
#
# dict = {'name': 'smy', 'age': 30}
#
# print fun2(**dict)

# list = [i*i if i % 2 == 0 else i for i in range(10) ]
# print list
#
# list2 = [x + y for x in ('a', 'b', 'c') for y in ('m', 'n')]
# print list2

# d = {'x': 'A', 'y': 'B', 'z': 'C'}
# for k in d.iteritems():
#     print k
# L = ['Hello', 'World', 'IBM', 'Apple', 5]
# print [s.lower() if isinstance(s, str) else s for s in L ]

# def fib(max):
#     n, a, b = 0, 0, 1
#     while n < max:
#         yield b
#         a, b = b, a + b
#         n = n + 1
#
# f = fib(6)
# # for i in range(6):
# #     print f.next()
#
# l = [f.next() for i in range(6)]
# print l

# def fib(max):
#     n, a, b = 0, 0, 1
#     while n < max:
#         yield b
#         a, b = b, a+b
#         n = n + 1
#
# def printb(min, max):
#     f = fib(max)
#     l = []
#     for i in range(max):
#         l.append(f.next())
#     print l[min: max+1]
#
# printb(2, 6)

# def printb(fr, to):
#     f = fib(to)
#     l = [f.next() for i in range(to)]
#     print l[fr-1:to]
#
# printb(3, 6)

# print map(str, [1, 2, 3, 4])
#
# def f(a, b):
#     return a + b
#
# # print map(f, [1,2,3])
# #但是如果要把序列[1, 3, 5, 7, 9]变换成整数13579，reduce就可以派上用场：
#
# def f(a, b):
#     return a*10 + b
#
# print reduce(f, [1,3,5,7,9])

# def fn(x, y):
#      return x * 10 + y
#
# def char2num(s):
#      dic = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
#      return dic[s]
#
# print reduce(fn, map(char2num, '13579'))

"""
利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。
输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']。
"""
# def to_upper(s):
#     for i in range(len(s)):
#         if i == 0:
#             s[i]=s[i].upper()
#             print s[i]
#         else:
#             s[i]=s[i].lower()
#     return s

# print map(to_upper, ['adam', 'LISA', 'barT'])
# s = 'adam'
# def f1(s):
#     s1 = ''
#     for index in range(len(s)):
#         if index == 0:
#             s1 += s[index].upper()
#         else:
#             s1 += s[index].lower()
#     return s1
#
#
# print map(f1, ['adam', 'LISA', 'barT'])
# # print f1('adam')
#
# def add(a, b):
#     return a + b
#
# print reduce(add, [1, 2, 3])
#
# def prod(a, b):
#     return a * b
#
# print reduce(prod, [1, 2, 3,4])
#
# def a (x):
#     x = x.lower()
#     x = x[0].upper()+x[1:]
#     return x
#
# print map(a,['adam','LISA','barT'])
#
# def change(name):
#     return name.capitalize()
#
# L1 = ['adam', 'LISA', 'barT']
# L2 = map(change, L1)
# print L2
#
# def cap(s):
#     s = s.lower()
#     s = s[0].upper() + s[1:]
#     return s
#
# print cap('abcdefkGGG')
# """
# 请尝试用filter()删除1~100的素数。
# """
#
# def number(n):
#     m = n-1
#     flag = True
#     while m > 1:
#         if n % m == 0:
#             flag = False
#             break
#         else:
#             m -= 1
#     return flag
#
#
# print filter(number, [1, 2, 4, 5, 6, 9, 10, 15])
#
#
# def sum(a, b):
#     return a*10 + b
#
#
# def trans_to_int(s):
#     dict = {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
#     return dict
#
#
#
# print map(trans_to_int, '123456')
#
#
# def reversed_cmp(x, y):
#     if x > y:
#         return -1
#     if x < y:
#         return 1
#     return 0
#
# print sorted([36, 5, 12, 9, 21], reversed_cmp)[::-1]

def lazy_sum(*args):
    def sum():
        total = 0
        for an in args:
            total += an
        return total
    return sum

l1 = lazy_sum(1,2,3,6,7)
l2 = lazy_sum(1,3,5,9,9)
print l1()
print l2()
# print l1 == l2



def log(func):
    def wrapper(*args, **kw):
        print 'call %s():' % func.__name__
        return func(*args, **kw)
    return wrapper

@log
def now():
    print 'now'
args = ('a', 'b')
kw = {'name': 'sss', 'age': 23}

now()


