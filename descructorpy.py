class Sample:
    def __init__(self):
        print("The sample has been created")
    def __del__(self):
        print("The sample has been destroyed")
    def show(self):
        print("The sample is present")

s= Sample()
print(s.show())
s.__del__()
s.show()


class Sample1:
    def __init__(self):
        print("The sample has been created")
    def init(self):
        print("The sample has been initialized")


s = Sample1()

'''class Sample1:
    def __init__(self):
        print("The sample has been created")
    def init(self):
        print("The sample has been initialized")
    def __init__(self, a, b):
        self.a = a
        self.b = b
        print("The values are "+str(self.a)+str(self.b))
s = Sample1()
'''
#pyhton allows n number of constructor but it calls only the last one

class Sample1:
    def __init__(self):
        print("Created")
    def __del__(self):
        print("destroyed")
    def __del__(self):
        print("DESTROYED")

s = Sample1()

#Any number of constructor and destructors are defined but the last method is called firstly





















