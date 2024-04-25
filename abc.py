class A:
    def write(self):
        print("I am Ananya Sharan")

class B:
    def write(self):
        print("I am ANANYA SHARAN")

class C(A, B):
    pass

class D(B, A):
    pass

c = C()
d = D()
print(c)
print(d)

print(c.write())
print(d.write())


