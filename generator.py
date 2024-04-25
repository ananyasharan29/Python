def m_gen():
    n=1
    print("first call")
    yield n

    n+=10
    print("second call")

    yield n

    n+=100
    print("third call")
    yield n

    print("fourth call")


n=m_gen()
res=next(n)
print(res)
print(next(n))
print(res)
print(next(n))
print(res)
print(res)

g=(i**2 for i in range(1,11) if i%2!=0)
print(next(g))
print(next(g))
print(next(g))
print(next(g))
for x in g:
    print(x)

#error here please fix it according to your need and try not to be over smart
str='python'
l=(str[i] for i in range(len(str)-1,-1,-1))
print(next(l))
for i in l:
    print(i)

    
    

   
