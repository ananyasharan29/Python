from subdirectory import module3
a = int(input("Enter the first number"))
b = int(input("Enter the second number"))
c = int(input("Enter 1 for multiplication, 2 for subtraction, 3 for division"))
if c ==1:
    r = module3.mult(a, b)
elif c == 2:
    r = module3.diff(a, b)
elif c == 3:
    r = module3.div(a, b)
else:
    print("Wrong choice")
print(f"The result of addition of {a} and {b} is {r}")