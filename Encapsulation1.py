class Student:
    def __init__(self, name, age):
        self.name = name
        self.__age = age
    def get_age(self):
        print("The student "+self.name+ " is "+str(self.__age))
    def set_age(self, n):
        if n <= 0:
            print("Invalid age")
        else:
            self.__age = n

s=Student("Colin", 12)
print(s.get_age())

print(s.get_age(17))
