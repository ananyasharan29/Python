class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def start(self):
        print(f"{self.make} {self.model} has started")
        
    def stop(self):
        print(self.model + " of "+self.make+"has stopped")

car1 = Car('toyota', 'Camry', 2022)
car2 = Car('honda', 'civic', 2022)

print(id(Car))
print(id(car1))
print(id(car1.make))
print(id(car1.year))
print(car1)

print(car1.start())
print(car1.stop())

print(Car.start(car1))


print("I own "+car1.make+" that was made in "+str(car1.year))


class Dog:
    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age

    def bark(self):
        print(self.name+" Woof ")
        
    def sleep(self):
        print(self.name+" Zzzzzzzzzzzz ")

dog1 = Dog("Govuu", "Golden retriver",15)
dog2 = Dog("Anuaa", "Bull dog",16)

print(dog1.sleep())
print(dog2.bark())

'''class Car:
    def init (self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def start(self):
        print(f"{self.make} {self.model} has started")
        
    def stop(self):
        print(self.model + " of "+self.make+"has stopped")

car1 = Car('toyota', 'Camry', 2022)
car2 = Car('honda', 'civic', 2022)


print(car1.start())
print(car1.stop())'''

dog1.__init__("Ananya","Ananya",17)

print(dog1.sleep())
