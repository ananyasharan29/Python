class Battery:
    def __init__(self, battery = 70):
        self.battery = battery

    def describe_battery(self):
        print("THis car has a " +str(self.battery)+ "-kwh battery")

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


class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make,model, year)
        self.battery = 70

    def describe_battery(self):
        print("This car has a " +str(self.battery)+ " -kwh battery")

    def drive(self):
        print("Driving the electric car")

print(ecar1.battery.describe_battery())
