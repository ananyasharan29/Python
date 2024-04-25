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


class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make,model, year)
        self.battery = 70

    def describe_battery(self):
        print("This car has a " +str(self.battery)+ " -kwh battery")

ecar1 = ElectricCar('Tesla', 'CyberTruck', 2023)

print(ecar1.describe_battery())
print(ecar1.start())
car1 = Car('AUDI', 'A4', 2016)
car2 = Car('honda', 'civic', 2022)
