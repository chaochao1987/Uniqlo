# -*- coding: utf-8 -*-
# data type and variable
"""转义字符\可以转义很多字符，比如\n表示换行，\t表示制表符，字符\本身也要转义，
所以\\表示的字符就是\，可以在Python的交互式命令行用print打印字符串看看：
"""
print '\\\n\\'
"""Python还允许用r''表示''内部的字符串默认不转义"""
print r"I'm girl"

a = None
print type(a)


"""
这种变量本身类型不固定的语言称之为动态语言，与之对应的是静态语言
"""
a = 123 # a是整数
print a
a = 'ABC' # a变为字符串
print a

#例如Java是静态语言，赋值语句如下
# int a = 123;

x = 10
x = x + 2
print x

#常量：全部大写
PI = 3.14159265359
"""
格式化
%d	整数
%f	浮点数
%s	字符串
%x	十六进制整数
"""
#有些时候，字符串里面的%是一个普通字符怎么办？这个时候就需要转义，用%%来表示一个%：
'growth rate: %d %%' % 7

L = ['Hello', 'World', 18, 'Apple', None]
L1 = [x.lower() if isinstance(x, str) else x for x in L]
print L1