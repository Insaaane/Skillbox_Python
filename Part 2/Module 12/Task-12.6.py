#Задача 6. Абстрактный класс

import math
from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height


circle = Circle(5)
print("Площадь круга:", circle.area())

rectangle = Rectangle(4, 6)
print("Площадь прямоугольника:", rectangle.area())

triangle = Triangle(3, 4)
print("Площадь треугольника:", triangle.area())