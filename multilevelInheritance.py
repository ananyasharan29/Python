import math

class Shape:
    def __init__(self, color):
        self.color =color

class Polygon(Shape):
    def __init__(self, color, sides):
        super().__init__(color)
        self.sides = sides

class Triangle(Polygon):
    def __init__(self, color, sides, side_length):
        super().__init__(color, sides)
        self.side_length = side_length

    def area(self):
        return self.side_length**2* math.sqrt(3)/4

tri = Triangle('red',3, 5)
print("The " +tri.color+" triange has an area of "+str(tri.area()))

#Method resolution operator or MRO

class Shape:
    def __init__(self, sides):
        self.sides = sides
    def __str__(self):
        return f"Shape with {self.sides} sides"

class Polygon(Shape):
    def area(self):
        raise NotImplementedError("Area not implemented for generic Polygon")


class Triangle(Polygon):
    def __init__(self, side_length):
        super().__init__(3)
        self.side_length = side_length
    def area(self):
        return self.side_length**2*math.sqrt(3)/4


class Square(Polygon):
    def __init__(self, side_length):
        super().__init__(4)
        self.side_length = side_length
    def area(self):
        return self.side_length**2
    
tri = Triangle(3)
print(tri.area())


sq = Square(4)
print(sq.area())

print(Triangle.mro())
print(tri.__str__())

print(Square.mro())
print(sq.__str__())
