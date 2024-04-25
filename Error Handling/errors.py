# There are 2 stages where errors may happen in a program -
# During Compilation-> Syntax Error
# During Execution-> Exception(logical Error)

# Some of them are Syntax Error, Runtime Error, Logical Error, Name Error, Type Error, Index Error, Attribute Error

#Syntax Error - Occurs when interpreter is unable to parse the code or code is violating the python program grammar.
# Such as inappropriate indentation, erroneous keyword usage, or incorrect operator use.
#Errors are raised by interpreter/compiler
#You can solve it by rectifying the program

# Code :
# x= 10
# if x==10
# print("x is 10")

# Error:
# File "c:\Users\91736\OneDrive\Desktop\MCA\1st Sem\Python\Error Handling\errors.py", line 8
#     if x==10
#             ^
# SyntaxError: expected ':'

# Solution:
x = 10
if x==10:
    print("x is 10")

#Runtime Error - occurs when the program is executing and encounters an unexpected
# condition that prevents it from continuing. 
# Runtime error are also known as exceptions and can occur for various reasons such as division by zero,
# trying to accessan index which is out of range, or calling a function that does not exist.

#Types of Runtime Error

# Name Error - raised when the interpreter encounters a variable or a function name that can't find in the current scope.
# Reasons : 1. misspelling a variable or function name
#           2. using a variable or function before it is defined
#           3. referencing a variable or function that is outside the current scope

# code:
# def sum(a, b):
    # total = a + b
    # return total

# x = 5
# y = 10
# z = sum(x, w)
# print(z)

# Error:
# File "c:\Users\91736\OneDrive\Desktop\MCA\1st Sem\Python\Error Handling\errors.py", line 46, in <module>
#     z = sum(x, w)
#                ^
# NameError: name 'w' is not defined

# Solution:
def sum(a, b):
    total = a + b
    return total

x = 5
y = 10
z = sum(x, y)
print(z)

#Index Error - thrown when tryig to access an item at an invalid index.

# code:
# l = [1, 2, 3]
# l[5]

# Error:
# File "c:\Users\91736\OneDrive\Desktop\MCA\1st Sem\Python\Error Handling\errors.py", line 70, in <module>
#     l[5]
#     ~^^^
# IndexError: list index out of range

# Solution:
l=[1, 2, 3, 4]
print(l[3])

#ModuleNotFoundError - thrown when a module could not be found.
# import mathi - Error: ModuleNotFoundError: No module named 'mathi'
import math
print(math.floor(5.3))

#Value Error - thrown when a function's argument is of an inapproprite type.
# print(int('a')) Error: ValueError: invalid literal for int() with base 10: 'a'
print(int(10))

# key Error - thrown when a key is not found, mostly this error occurs in dictionary
# d = {'name': 'Ananya'}
# print(d['age'])  --KeyError: 'age'
d = {'name': 'Ananya'}
print(d['name']) 

#Type Error - thrown when an operation or function is applied to an object of an inappropriate type. 
# x = "10"
# y = 5
# Z = x + y
# print(z) --TypeError: can only concatenate str (not "int") to str
x = "10"
y = 5
Z = x + str(y)
print(z)

#Attribute Error - when you try to access an attribute or method of an object that does not exist or is not defined for that object. 
# l=[2, 4, 6]
# print(l.upper()) --AttributeError: 'list' object has no attribute 'upper'

