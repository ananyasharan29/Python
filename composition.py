class Component:
    def __init__(self):
        print("Component Object created")
    def method1(self):
        print('Component method exexcuted')

class Composite:
    def __init__(self):
        print('Composite object created')
        self.com=Component()
    def method2(self):
        print('Component method executed')
        print('Composite method calling component method')
        self.com.method1()

c = Composite()
c.method2()

#Single Component

class Engine:
    def __init__(self, fuel_type):
        self.fuel_type = fuel_type
    def start(self):
        print('Engine started using fuel '+self.fuel_type)
    def stop(self):
        print('Engine stopped')

class Car:
    def __init__(self, make, model, fuel_type):
        self.make = make
        self.model = model
        self.engine= Engine(fuel_type)
    def start_engine(self):
        self.engine.start()
    def stop(self):
        self.engine.stop()

c = Car('Toyota', 'Corolla', 'Fossil fuel')
c.start_engine()
c.engine.fuel_type


#Multiple Components

'''class Engine:
    def start(self):
        print('Engine started')
              
class Wheels:
    def roll(self):
        print('Wheels are rolling')

class Body:
    def paint(self):
        print(f"Body painted with {color}")

class Car:
    def __init__(self):
        self.engine= Engine()
        self.wheels = [Wheels() for _ in range(4)]
        self.body = Body()
    def start(self):
        self.engine.start()
    def rolls(self):
        for w in self.wheels:
            w.roll()
    def paint(self, color):
        self.body.paint(color)

c = Car()
print(c.start())
print(c.rolls())
print(c.paint('Red'))'''

#Inheritance and Composition

class Piece:
    def __init__(self, color):
        self.color = color

class Pawn(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.type = 'Pawn'

class Elephant(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.type = 'Elephant'

class Board:
    def __init__(self):
        self.grid = [[None for _ in range(8)] for _ in range(8)]
    def initialize_board(self):
        self.grid[0][0] = Elephant('white')
        self.grid[0][7] = Elephant('white')
        self.grid[1] = [Pawn('white') for _ in range(8)] #8 objects of white pawn is created
        self.grid[6] = [Pawn('black') for _ in range(8)] #8 objects of black pawn is created
        self.grid[7][0] = Elephant('white')
        self.grid[7][7] = Elephant('white')
        
    def print_board(self):
        for r in self.grid:
            print([piece.type if piece else '_*_' for piece in r])



class Game:
    def __init__(self):
        self.board = Board()
        self.board.initialize_board()
    def play(self):
        print('Initialize board')
        self.board.print_board()

c=Game()
print(c.play())
        

    
            
















        




















