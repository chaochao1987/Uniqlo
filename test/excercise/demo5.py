# class Animal(object):
#     def run(self):
#         print 'Animal is running'
#
#     def eat(self):
#         print 'Animal is eating'
#
# class Cat(Animal):
#     def run(self):
#         print 'cat is running'
#
# class Dog(Animal):
#     def run(self):
#         print 'dog is running'
#
# def twice_run(Animal):
#     Animal.run()
#     Animal.eat()
#
# class Bee(object):
#     def run(self):
#         print 'Actually is flying..'
#     def sleep(self):
#         print 'take a nap..'
#
# twice_run(Dog())

list = [{'a': 'a', 'age': 10}, {'a': 'b', 'age': 10}]
list2 = [{'age': 10, 'a': 'a',}, {'a': 'b', 'age': 10}]
print list[0] == list2[0]
