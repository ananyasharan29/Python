class MyMeta(type):
    pass
class MyClass(metaclass = MyMeta):
    pass
class MySubClass(MyClass):
    pass

print(type(MyMeta), type(MyClass), type(MySubClass))

print(MyMeta, MyClass, MySubClass)

# print(MyMeta(), MyClass(), MySubClass())

#Create a metaclass called MetaOne and MetaTwo
class MetaOne(type):
    def __new__(cls, name, bases, dict):
        print(f'Creating class {name} with bases {bases} and attributes {dict}')
        return super().__new__(cls, name, bases, dict)
    

class MetaTwo(type):
    def __init__(self, name, bases, dict):
        print(f'Initializing class {name} with bases {bases} and attributes {dict}')
        super().__init__(self, name, bases, dict)

#Create two classes MyClassOne and MyClassTwo that uses MetaOne and MetaTwo as its Metaclass
class MyClassOne(metaclass = MetaOne):
    def method_one(self):
        return 'The method "meta_one" is called'
    
class MyClassTwo(metaclass = MetaTwo):
    def method_two(self):
        return 'The method "meta_two" is called'
    

#Create objects of the class
in_one = MyClassOne()
in_two = MyClassTwo()

