import sys
import traceback
import math

#Accessing system information
print(f"Python version is {sys.version}")
print(f"Operating system is {sys.platform}")

#Working with command line arguments
print(f"Command line arguments : {sys.argv}")

#Display Module search path
print(f"Module path is {sys.path}")

#Simulating command line arguments
sys.argv=['a.py', 'Ananya']

#Check the command line arguments
if len(sys.argv)<2:
    print("Provide a name as a command line arguments")
else:
    name=sys.argv[1]
    print(f"Hello {name}!")

sys.argv=['a.py']
if len(sys.argv)<2:
    print("Provide a name as a command line arguments")
    sys.exit(1)
else:
    name=sys.argv[1]
    print(f"Hello {name}!")


# print(type(%tb))
    
#provide a dictionary to display the loaded modules
m=sys.modules
print("Loaded modules : ")
for m1 in m:
    print(m1)

#Get the size of an objects in bytes
num=123
print(f"The size of {num} which is {type(num)} is {sys.getsizeof(num)}")

#Use Traceback
try:
    r=math.exp(1000)
except Exception as e:
    e_type, e_value, e_traceback = sys.exc_info()
    print("Traceback information")
    traceback.print_tb(e_traceback)
    print(f'Exception type : {e_type}')
    print(f'Exception type : {e_value}')

