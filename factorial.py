def factorial(x):
    global counter
    counter +=1
    print("Inside factorial for count ", counter)
    if x==1:
        return 1
    else:
        return x*factorial(x-1)

n = int(input("Enter a number : "))
counter = 0
print(factorial(n))
print(counter)

