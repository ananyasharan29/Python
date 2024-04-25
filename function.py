student = {'name': 'ABC', 'age': 20}
print("Before the function", student)
def func(student):
    new={'marks': [60,80,90]}
    student.update(new)
    print("Inside the function", student)
func(student)
print("After the function",student)


student = {'name': 'ABC', 'age': 20}
print("Before the function", student)
def func(student):
    student={'marks': [60,80,90]}
    print("Inside the function", student)
func(student)
print("After the function",student)



#variable-length arguments
def sum(*a):
    r =0
    for i in a:
        r = r+i
    return r
print(sum(10))
print(sum(10,20))
print(sum(10,20,30,40,50))
