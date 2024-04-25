class Shape:
    def draw(self):
        print("Drawing a generic class")

#Parenr1 class
class ColoredShape(Shape):
    def __init__(self, color):
        self.color = color
    def draw(self):
        super().draw()
        print("Coloring the shape with " +self.color)

#Parent2 class
class TexturedShape(Shape):
    def __init__(self, texture):
        self.texture = texture
    def draw(self):
        super().draw()
        print("Adding the " +self.texture+ " to the shape")


#child class inherited from Parent1, Parent2
class TexturedColoredShape(ColoredShape, TexturedShape ):
    def __init__(self, color, texture):
        super().__init__(color)
        self.texture = texture

tcs = TexturedColoredShape('blue', 'dashed')
print(tcs.draw())


#child class inherited from Parent1, Parent2
class TexturedColoredShape_1(TexturedShape, ColoredShape ):
    def __init__(self, color, texture):
        super().__init__(texture)
        self.color = color

tcs_1 = TexturedColoredShape_1('yellow', 'dashed')
print(tcs_1.draw())
        
