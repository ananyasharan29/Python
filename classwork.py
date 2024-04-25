def sum(a, b, c):
    "Add three values"
    return a+b+c
print(sum(2,3,4)) #Required argumemnt
print(sum(c='a', a='b', b='c')) #Keyword arguments


#Default arguments
def sum(a, b, c):
    "Add three values a, b, c"
    return a+b+c
print(sum(b=30, a=90)) #Keyword with default
