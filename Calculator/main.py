import mathematical
import scientific
from AreaAndVolume import circleArea, triangleAarea, rectangleArea, cylinderVolume, sphereVolume

def main():
    print("Welcome to calculator ")

    print("Choose the type of functions: ")
    print("1. Mathematical Functions ")
    print("2. Scientific Functions ")
    print("3. Area and Volume Functions ")

    choice = input("Enter your choice (1, 2, or 3): ")

    if choice == '1':
        print('You selected mathematical functions')
        performMathematicalOperation()
    elif choice == '2':
        print('You selected Scientific functions')
        performScientificOperation()
    elif choice == '3':
        print('You selected area and volume functions')
        performAreaAndVolumeOperation()
    else:
        print('Invalid Choice')

def performMathematicalOperation():
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    c = int(input("Enter 1 for addition, 2 for subtraction, 3 for multiplication, 4 for division: "))

    if c == 1:
        r = mathematical.add(a, b)
        operation = "addition"
    elif c == 2:
        r = mathematical.diff(a, b)
        operation = "subtraction"
    elif c == 3:
        r = mathematical.mult(a, b)
        operation = "multiplication"
    elif c == 4:
        r = mathematical.div(a, b)
        operation = "division"
    else:
        print("Wrong choice")
        exit()

    print(f"The result of {operation} of {a} and {b} is {r}")

def performScientificOperation():
    choice = int(input("Enter 1 for power, 2 for exponential, 3 for factorial: "))

    if choice == 1:
        base = float(input("Enter the base: "))
        exponent = float(input("Enter the exponent: "))
        r = scientific.power(base, exponent)
        print(f"Result of {base} raised to the power of {exponent} is: {r}")
    elif choice == 2:
        num = float(input("Enter the number: "))
        r = scientific.exponential(num)
        print(f"Exponential of {num} is: {r}")
    elif choice == 3:
        num = int(input("Enter the number: "))
        r = scientific.factorial(num)
        print(f"Factorial of {num} is: {r}")
    else:
        print("Invalid choice")

def performAreaAndVolumeOperation():
    
    print("Choose the type of calculation:")
    print("1. Area of Circle")
    print("2. Area of Triangle")
    print("3. Area of Rectangle")
    print("4. Volume of Cylinder")
    print("5. Volume of Sphere")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        radius = float(input("Enter the radius of the circle: "))
        print(f"The area of the circle with radius {radius} is: {circleArea(radius)}")
    elif choice == '2':
        base = float(input("Enter the base of the triangle: "))
        height = float(input("Enter the height of the triangle: "))
        print(f"The area of the triangle with base {base} and height {height} is: {triangleAarea(base, height)}")
    elif choice == '3':
        length = float(input("Enter the length of the rectangle: "))
        width = float(input("Enter the width of the rectangle: "))
        print(f"The area of the rectangle with length {length} and width {width} is: {rectangleArea(length, width)}")
    elif choice == '4':
        radius = float(input("Enter the radius of the cylinder: "))
        height = float(input("Enter the height of the cylinder: "))
        print(f"The volume of the cylinder with radius {radius} and height {height} is: {cylinderVolume(radius, height)}")
    elif choice == '5':
        radius = float(input("Enter the radius of the sphere: "))
        print(f"The volume of the sphere with radius {radius} is: {sphereVolume(radius)}")
    else:
        print("Invalid choice")

