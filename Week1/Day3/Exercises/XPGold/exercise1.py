import math

class Circle:
    def __init__(self, radius=1.0):
        self.radius = radius

    def calculate_area(self):
        print("Area:", math.pi * self.radius ** 2)

    def calculate_perimeter(self):
        print("Perimeter:", 2 * math.pi * self.radius)

    def describe(self):
        print("A circle is a shape with all points at the same distance from its center.")

circle = Circle(5)
circle.calculate_area()   
circle.calculate_perimeter()
circle.describe()