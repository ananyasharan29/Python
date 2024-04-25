from typing import Any


class MyClass:
    def __init__(self, value):
        self.value = value

    def method_One(self):
        return f'This is the method with value {self.value}'
    
#Inspecting class method and attributes
print(dir(MyClass))

MyClass.__class__

#Create an instance of MyClass
obj = MyClass(100)
print(obj.method_One())

print(obj.value)

print(dir(obj))

#Check if an attribute or a method exists
print(f'Obj has a value : {hasattr(obj, 'value')}')
print(f'Obj has a method : {hasattr(obj, 'method_One')}')
print(f'Obj has a method : {hasattr(obj, 'Method_one')}')

#Get the attribute of a class
if hasattr(obj, 'value'):
    print(f'Value of attribute is {getattr(obj, 'value')}')


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def greet(self):
        print(f'Hello, my name is {self.name} and age is {self.age}')

def introspect_method(obj):
    print(f'Type of object is {type(obj)}')
    print(f'Attributes are : {dir(obj)}')
    if hasattr(obj, 'greet'):
        print("Calling the method")
        obj.greet()

    print(f'Accessing the attributes : {getattr(obj, 'name')}')

obj = Person('BBB', 23)
print(introspect_method(obj))

#Dynamic Code execution
# code_string='''
# def greet(name):
# print(f'Hello, {name}')
# '''
# exec(code_string)
# greet('AAA')

# code_string_1='''
# def greet(name):
# print(f'Hello, {name}')
# '''
# exec(code_string_1)
# greet('AAA')

# def calculate_area(shape, *args):
#     if shape=='square':
#         side = args[0]
#         return side*side
#     elif shape=='rectangle':
#         length, width = args
#         return length*width
#     elif shape=='circle':
#         radius = args[0]
#         return 3.114159*radius*radius
#     else:
#         return ValueError("Invalid Shape")
    
# shape_code = input("Enter the shape and dimensions : ")
# code_part = shape_code.split()
# print(code_part)
# shape  = code_part[0]
# print(shape)
# args = tuple(map(float, code_part[1:]))
# print(args)

#isinstance()
c=["Hello"]
if isinstance(c, str):
    print(f'{c} is a string')
else:
    print(f'{c} is not a string')

class Person:
    pass
obj=Person()

if isinstance(obj, Person):
    print("obj is an instance of Person")
else:
    print("Obj is not instance of Person")

data = 42j
if isinstance(data, (int, float)):
    print(f'{data} can be either integer or float or complex')
else:
    print(f'{data} is neither integer not float or complex')

class Animal:
    pass
class Dog(Animal):
    pass
d=Dog()
a=Animal()
if isinstance(d, Animal):
    print("It is inherited")
else:
    print("It is not inherited")

if isinstance(a, Dog):
    print("It is inherited")
else:
    print("It is not inherited")

if isinstance(d, Dog):
    print("It is inherited")
else:
    print("It is not inherited")

#Dynamic Addition of Attributes and Methods
class Myclass:
    pass
o=Myclass()

#Adding attributes to o
setattr(o,'data', 45)
print(o.data)

#Adding method to o
def greet(self):
    return f'Hello, {self.name}'

#Adding attributes to o
o.name ='XYZ'
o.greet=greet.__get__(o)
print(o.greet())

#Another example
class DynamicObject:
    def __getattr__(self,attr):
        if attr.startswith("get_"):
            def getter():
                value = "Generating values for attributes {}".format(attr[4:])
                return value
            return getter
        else:
            raise AttributeError("Attribute {} not found".format(attr))
        
    def __setattr__(self, value):
        print("Setting attribute {} to {}".format(attr, value))
        self.__dict__[attr]= value

o = DynamicObject()
print(o.get_name())
print(o.get_age())

#Setting Dynamic Attribute
# o.name='ABC'
# o.age=25
# print(o.name, o.age)