class MyLib(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print 'init'

    def cat(self):
        print self.name
        print self.age
