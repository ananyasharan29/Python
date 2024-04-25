x = int(input("Enter first number : "))
y = int(input("Enter second number : "))

'''def gcd(x,y):
    if(y == 0):
        return x
    else:
        return gcd(y, x%y)'''

def gcd(a,b):
    if(a ==0):
        return b
    if(b==0):
        return a
    if(a==b):
        return a
    if(a>b):
        return gcd(a-b, b)
    return gcd(a, b-a)

print("GCD of two numbers is ",gcd(x,y))


