import math
from abc import ABC, abstractmethod

#flagged as ABC, you will never create a Shape class
class Shape(ABC):

    number_of_shapes = 0

    def __new__(cls, colour):
        print("New shape object created.")
        obj = object.__new__(cls)
        return obj
    
    def __init__(self, colour):
        self.__colour = colour
        Shape.number_of_shapes += 1

    #property decorator returns get_colour rather than use of get_colour()
    @property
    def colour(self):
        return self.__colour
    
    #all classes inheriting the Shape class, MUST have a calc_area function
    @abstractmethod
    def calc_area(self):
        pass

class Square(Shape):
    def __init__(self,colour):
        #super, send colour up to parent init i.e Shape
        super().__init__(colour)
    
    def calc_area(self, size):
        return size * size
    
class Circle(Shape):
    def __init__(self, colour):
        super().__init__(colour)
    
    def calc_area(self, radius):
        return math.pi * radius * radius
    
sq = Square("blue")
circ = Circle("red")
print("Your {} box is {}m in area.".format(sq.colour, sq.calc_area(10)))
print(Shape.number_of_shapes)