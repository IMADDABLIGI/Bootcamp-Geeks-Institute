import math

class Circle:

    circles = []

    def __init__(self, radius=0, diameter=0):
        if not radius and not diameter:
            raise Exception("Add either a Diameter or a Radius to define the circle")
        elif radius:
            self.radius = radius
            self.diameter = radius * 2
        else:
            self.diameter = diameter
            self.radius = diameter/2
        
    def get_radius(self):
        return self.radius

    def get_diameter(self):
        return self.diameter
    
    def get_area(self):
        calculate = math.pi * (self.radius ** 2)
        return (calculate)
    
    def __print_data__(self):
        print("\n----- Circle data: -----")
        print(f"Radius = {self.radius}")
        print(f"Diameter = {self.diameter}")
        print(f"Area = {self.get_area()}")
    
    def __merge_circles__(self, obj1, obj2):
        print("Merging two circles")
        new_obj = Circle(obj1.radius+obj2.radius)
        return new_obj
    
    def __compare__(self, obj):
        if self.radius > obj.radius:
            return True
        return False
    
    def __are_equal__(self, obj):
        if self.radius == obj.radius:
            return True
        return False

    def __lt__(self, other):
        return self.radius < other.radius
    
    @classmethod
    def __add_to_list__(cls, *circles):
        for c in circles:
            if isinstance(c, cls):
                cls.circles.append(c)
        cls.circles.sort(key=lambda x: x.radius)


dowara = Circle(4)
dowara2 = Circle(5)

# print("Circle Area: ", dowara.get_area())
# dowara.__print_data__()

dowara3 = Circle.__merge_circles__(Circle, dowara, dowara2) #I've just discovered we could do this hh
dowara3.__print_data__()


print("Is Dowara3 bigger than Dowara2:", dowara3.__compare__(dowara2))
print("Is Dowara3 equal to    Dowara2:", dowara3.__are_equal__(dowara2))

Circle.__add_to_list__(dowara, dowara2, dowara3)
circles = Circle.circles
print("\n--------------- All the circles inside the Circle class are: ---------------")
for circle in circles:
    circle.__print_data__()


