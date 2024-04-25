#Operator Polymorphism

print(10+5)

print("Hello" + " Python")

print([10,20,30]+[40, 60])

print((1, 2, 3) +(4,5))

#Doesn't work with set

print("Hello" *3)

print([10,20]*3)

#Function polymorphism
#Inbuilt function

print(len("Ananya"))
print(len([10,20,30]))

#user defined function
def add(x, y, z):
    return x+y+z

print(add('a','b','c'))
print(add([10, 20], [30], [40, 50]))

#Class polymorphism
'''class Cat():
    def _init_(self,name,age):
        self.name=name
        self.age=age
    def info(self):
        print("I am cat. My name is " +self.name+". I am "+str(self.age)+" years old")
    def makesound(self):
        print('Meoow')  
class Dog():
    def _init_(self,name,age):
        self.name=name
        self.age=age
    def info(self):
        print("I am Dog. My name is " +self.name+". I am "+str(self.age)+" years old")
    def makesound(self):
        print('Bark')
        
cat=Cat('kitty',5)
dog=Dog('kaman',12)
for animal in (cat,dog):
    print(animal.info())
    print(animal.makesound())'''

    
class India:
    def capital(self):
        print("The capital is new delhi")

class USA:
    def capital(self):
        print("The capital is Washington DC")

class Australia:
    def capital(self):
        print("The capital is Sydney")

class Singapore:
    def capital(self):
        print("The capital is Singapore")

i = India()
u = USA()
a = Australia()
s = Singapore()

for countries in [i,u,a,s]:
    print(countries.capital())


#Method Overriding
class Birds():
    def flight(self):
        print("Most birds fly")

class Eagle(Birds):
    def flight(self):
        print("An Eagle soars in the sky")

class Emu(Birds):
    def flight(self):
        print("An Emu only runs")

b = Birds()
e = Eagle()
em = Emu()

for i in {b,e,em}:
    print(i.flight())
        
    
#Duck Typing
class Duck():
    def quack(self):
        print("I am a duck and i quack")

class Goose():
    def quack(self):
        print("I am a Goose and i quack")

class Cat():
    def meow(self):
        print("I am a cat and i meow")
        
        
def sound(animal):
    animal.quack()


print(sound(Duck()))
print(sound(Goose()))
print(sound(Cat()))#it doesn't have method quack that's why it is showing error
    




    
