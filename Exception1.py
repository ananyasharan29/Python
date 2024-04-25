#Try Except Else Block
'''try:
    n = int(input("Enter the number "))
    assert n %2 == 0
except:
    print("Number should be an even number")
else:
    try:
        r = 1/n
        print(r)
    except ZeroDivisionError as e:
            print(f"{e}")'''
    


#Try Except Finally Block
'''try:
    n = int(input("Enter the number "))
    assert n %2 == 0
except:
    print("Number should be an even number")
else:
    try:
        r = 1/n
        print(r)
    except ZeroDivisionError as e:
            print(f"{e}")
finally:
    print("The code got executed successfully")'''

#File exist error
import os
filepath = 'file.txt'
try:
    with open(filepath, 'x'):
        print(f"File '{filepath}' created successfully")
except FileExistsError as e:
    print(f"File '{filepath}' already exist: {e}")

#FileNotFoundError
try:
    f = open('file1.txt','rt')
    print("File open")
except FileNotFoundError as e:
    print(f"FileNotFound error: {e}")


#IO Error
try:
    f = open('file1.bin','r')
    print("File opened")
except IOError as e:
    print(f"IO error: {e}")


#Key Error
try:
    d = {'a':1, 'b':2, 'c':3}
    d['d']
except LookupError as e:
    print(f"Lookup error: {e}")


#OS Error
try:
    f = open("file1.txt",'r')
    data = f.read()
except OSError as e:
    print(f"Os error: {e}")


































    
