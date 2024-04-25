class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age
    def get_name(self):
        print("The name of the person is "+self.name)
    def get_age(self):
        print("The age of the person is "+str(self.__age))
    def set_age(self, n):
        if n <= 0:
            print("Invalid age")
        else:
            self.__age = n

class Employee(Person):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self._salary = salary
    def get_salary(self):
        print("The salary of the employee is "+str(self.__salary))
    def set_salary(self, n):
        if n <= 0:
            print("Invalid salary")
        else:
            self.__salary = n

e = Employee("Ananya", 23, 1000000)
print(e.get_name())
print(e.get_age())
print(e.set_salary(0))
print(e.get_salary())
