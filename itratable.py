
l=[1,2,3,4]

i_l=iter(l)
print(type(i_l))

print(next(i_l))
print(next(i_l))
print(i_l.__next__())


str='python'
i_s=iter(str)

print(type(i_s))
print(next(i_s))

t=(1,2,34)

i_t=iter(t)

print(next(i_t))


s={1,2,3,4,5,67,89}

i_s=iter(s)

print(next(i_s))
print(next(i_s))
print(next(i_s))
print(next(i_s))
print(next(i_s))

t=('A',1,2,34,'a','b',0.9,0)
i_t=iter(t)

for index, item in enumerate(i_t):
     print(item)
     if index==7:
         break
print("outside the loop")
print(next(i_t))
print(next(i_t))
print(next(i_t))
     



