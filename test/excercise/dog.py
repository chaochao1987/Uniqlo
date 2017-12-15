class Animal(object):
    def run(self):
        print 'Animal is running'


class Dog(Animal):
    def run(self):
        print 'dog is running'


class Cat(Animal):
    def run(self):
        print 'cat is running'


class Tortoise(Animal):
    def run(self):
        print 'tortoise is running slowly'


def run_twice(animal):
        animal.run()
        animal.run()


run_twice(Tortoise())
