# class Circle:
#     color = "red"

# class NewCircle(Circle):
#     color = "blue"

# nc = NewCircle
# print(nc.color)

class Circle:
    def __init__(self, diameter):
      self.diameter = diameter

    def grow(self, factor=2):
        """grows the circle's diameter by factor"""
        print("grow1")
        self.diameter = self.diameter * factor

class NewCircle(Circle):
    def grow(self, factor=2):
        """grows the area by factor..."""
        print("grow2")
        self.diameter = (self.diameter * factor * 2)

nc = NewCircle(1)
print(nc.diameter)

nc.grow()

print(nc.diameter)