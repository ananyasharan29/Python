#raise bulid-in Exception explicitly


x=int(input("Enter the 1st number: "))
y=int(input("Enter 2nd number: "))

try:
    z=x/y
    if z>10:
        raise ValueError(z)
    else:
        print(z)
except ValueError:
    print(f'valueError:invalid Range')
    
#raise exceptions explicitly

x=int(input("Enter the value"))
try:
    if x<0:
        raise Exception("negative value not allowed")
    else:
        print(x**2)

except Exception as e:
    print(f'Error occured: {e}')
    
    
