try:
    n = int(input("Enter the numerator : "))
    d = int(input("Enter the denominator : "))
    r = n/d
    print(r)
except:
    print("Error, denominator cannot be zero")


n = int(input("Enter the numerator : "))
d = int(input("Enter the denominator : "))
try:
    r = n/d
    l = [1, 2, 3, 4, 5, 6, 7, 8, 9,10]
    print(l[r])
except ZeroDivisionError as e:
    print(f"Zero division error :{e}")
except IndexError as e:
    print(f"IndexError : {e}")
    
