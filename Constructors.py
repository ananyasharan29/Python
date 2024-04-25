class Sample:
    def __init__(self, a, b):
        print("The sample has been created")
        self.a = a
        self.b = b
        print("The values in sample are "+str(self.a)+str(self.b))
s = Sample('a','b')
s1 = Sample(3, 2)
        
 #   def init(self):
   #     print("The sample has been initialized")
        

s = Sample()
#print(s)

#s1.__init__()
s1 = Sample()
s.init()
