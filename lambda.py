x = lambda a : a* 5
print(x)
print((type(x)))
print(x(-3))

add_num = lambda a, b: a+b
print(add_num(10, 20))

print(lambda a, b: a+b(20, 40))

def f(n):
    return lambda a: a*n
print(f(3))


greet = lambda: print("Hello, How are you?")
greet()
print(greet)

(lambda x: x*x)(15)
print(x)

s = lambda*x: x[0]+x[1]+x[2]+x[3]
print(s(10,20,30,40))

a= ['icecream', 'pizza', 'idle', 'dosa']
b = list(map(len,a))
print(b)

l=[1,2,3,4,5,6,7,8,9,10]
res=map(lambda a: a*5, l)
print(list(res))

s =map(lambda x : x**5,[1,2,3,4,5,6,7,8,9,10])
print(list(s))

seq = [0,1,2,3,5,8,13]
list(filter(lambda x : x %2 !=0, seq))
print(seq)

sequence = [0,6, 2,3,5,9,13,15]
list(filter(lambda x : x %5 ==0, sequence))
print(sequence)

from functools import reduce
nums = [1,2,3,4]
ans = reduce(lambda x, y: x+y, nums)
print(ans)

a = list(input("Enter the elements ").split())
b = list(input("Enter the elements ").split())
zip(a, b)
print(list(zip(a, b)))
         
