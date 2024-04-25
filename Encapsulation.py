#default encapsulation

'''class Student:
    def __init__(self, name, rank, sem):
        self.name= name
        self.rank= rank
        self.sem = sem

    
    def display(self):
        print("Student is " +self.name+" with a  rank" +str(self.rank)+
              " from" +str(self.sem)" sememster.")

s1 = Student("Ananya", 1, 6)
s2 = Student("Colin", 2, 3)
s3 = Student("Buddy", 3, 4)
s4 = Student("Draco", 4, 5)

for i in (s1, s2, s3, s4):
    print(i.display())
    '''
#protected

#protected with inheritance

class A:
    def __init__(self, a):
        self._a = a

class B(A):
    def __init__(self, a):
        super().__init__(a)
    def display(self):
        print("The value is "+str(self._a))


b = B(5)
print(b.display())

print("The value in class B is "+str(b._a))


#privaate Access Specifier

class Employee:
    def __init__(self, name, project, salary):
        self.name= name
        self.project = project
        self.salary = salary
        


#Name Mangling

#private members and inheritance
class A:
    def __init__(self, a):
        self._a = a

class B(A):
    def __init__(self, a):
        super().__init__(a)
    def display(self):
        print("The value inside the class is "+str(self.__a))


b = B(5)
print(b.display())
