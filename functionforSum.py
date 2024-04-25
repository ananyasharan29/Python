def sum(x):
    if x == 1:
        return 1
    else:
        return x+sum(x-1)

n = int(input("Enter a number : "))
print(sum(n))


