class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.reading = 0

    def start(self):
        print(f"{self.make} {self.model} has started")
        
    def stop(self):
        print(self.model + " of "+self.make+"has stopped")

    def read_meter(self):
        print("This car has " +str(self.reading) + " kms on it")
    def increment_meter(self, kms):
        self.reading += kms


car1 = Car('AUDI', 'A4', 2016)
car2 = Car('honda', 'civic', 2022)


print(car1.increment_meter(300))
print(car1.read_meter())

car1.reading = 40
print(car1.read_meter())
