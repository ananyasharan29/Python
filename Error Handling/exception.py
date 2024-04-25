#Exceptions - if things go wrong during the execution of the program(runtime).
# It generally happens when something unforceseen has happened.

# print(dir(locals()['__builtins__']))

# when we run a wrong code, we find a long message on console that is called STACKTRACE.
#Stacktrace contains type of error, in which line error has occured, and file name as well.

#Why Exception Handling is necessary?
# --For user experience
# --For Security

# How tohandle exceptions 
# -- Try Except block

# Create a file
with open('sample2.txt', 'w') as f:
    f.write('Hello World!')

# Try Except
try:
    with open('sample5.txt', 'r') as f:
        print(f.read())
except:
    print('File not found!')

# Catching different type of exception
try:
    m=2
    with open('sample2.txt', 'r') as f:
        print(f.read())
        print(m)
        print(5/2)
        l = [2, 3, 4, 5]
        print(l[12])
except FileNotFoundError:
    print('File not Found!')
except NameError:
    print('Variable not defined!')
except ZeroDivisionError:
    print('can not divide by 0!')
except Exception as e:
    print(e)

# else
try:
    f = open('sample2.txt', 'r')
except FileNotFoundError:
    print('File not found!')
except Exception:
    print('Something wrong is there')
else:
    print(f.read())

# finally
try:
    f = open('sample5.txt', 'r')
except FileNotFoundError:
    print('File not found!')
except Exception:
    print('Something wrong is there')
else:
    print(f.read())
finally:
    print('It will print always')

# Raise exception
# In python, exceptions are raised when errors occur at runtime
# we can also manually raise exceptions using the raise keyword
# we can optionally pass values to the exception to clarify why that exception was raised

class Bank():
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        if amount < 0:
            raise Exception('Amount should not be -ve')
        if self.balance < amount:
            raise Exception("Don't have enough money")
        self.balance = self.balance - amount

obj = Bank(10000)
try:
    obj.withdraw(-5000)
    # obj.withdraw(5000)
    # obj.withdraw(15000)
except Exception as e:
    print(e)
else:
    print(obj.balance)